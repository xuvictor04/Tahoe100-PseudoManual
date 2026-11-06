"""python -m tahoemap <command> - the one-shot pipeline and the look-ups. The `tahoe` shell wrapper calls this.

    run         every stage that is missing or out of date, in order (the one-shot job)
    build ... map   one stage (and nothing else)
    status      what is done, what is out of date, what runs next
    gene SYMBOL | drug NAME | line NAME | pair A B | module N     look-ups on a finished run
"""

import argparse
import importlib
import json
import os
import shutil
import sys
import time
import warnings

from . import __version__
from . import atlas_core as A
from . import tlib as T
from .common import STAGES, clear_stamps_from, log, mark_output, read_stamp, stamp_stage

STAGE_MODULE = {"tensor": "tensor", "tables": "tables", "embed": "embed", "reference": "reference",
                "relations": "relations", "graph": "graph", "validate": "validate", "vault": "vault",
                "map": "html_map"}
LOOKUPS = ("gene", "drug", "line", "pair", "module")


def default_data():
    return os.path.abspath(os.path.expanduser(os.environ.get("TAHOE_DATA", "~/Tahoe-100M")))


def atlas_args(a):
    """The namespace atlas_core.cmd_build / cmd_effects expect."""
    return argparse.Namespace(data=a.data_in, out=os.path.join(a.out, "atlas"), reindex=a.reindex,
                              limit_files=a.limit_files, workers=a.workers, batch_size=a.batch_size,
                              layout=a.layout, unreliable_plates=a.unreliable_plates, min_cells=a.min_cells)


def build_complete(out):
    atl = os.path.join(out, "atlas")
    p = os.path.join(atl, "build_info.json")
    if not (os.path.exists(p) and os.path.exists(os.path.join(atl, "sample_map.csv"))):
        return False
    try:
        info = json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return False
    import glob
    return len(glob.glob(os.path.join(atl, "pseudobulk", "group*_profiles.csv"))) == info.get("groups", -1)


def effects_complete(out):
    p = os.path.join(out, "atlas", "effects", "complete.json")
    try:
        return json.load(open(p, encoding="utf-8")).get("version") == A.EFFECTS_VERSION
    except (OSError, ValueError):
        return False


def stage_version(stage):
    if stage in ("build", "effects"):
        return A.EFFECTS_VERSION
    return getattr(importlib.import_module(f"tahoemap.{STAGE_MODULE[stage]}"), "VERSION", 1)


def is_current(out, stage):
    st = read_stamp(out, stage)
    if st is None:
        if stage == "build" and build_complete(out):          # e.g. a reused atlas: adopt it
            stamp_stage(out, "build", A.EFFECTS_VERSION, {"adopted": True})
            return True
        if stage == "effects" and effects_complete(out) and read_stamp(out, "build"):
            stamp_stage(out, "effects", A.EFFECTS_VERSION, {"adopted": True})
            return True
        return False
    try:
        return st.get("version") == stage_version(stage)
    except ImportError:
        return False


def plan(out, start=None, stop=None, redo=False, skip=()):
    """Stages to run: from the first missing / outdated one (or `start`) to `stop`; later stages always follow."""
    names = [s for s in STAGES if s not in skip]
    if stop:
        names = names[:names.index(stop) + 1]
    if start:
        return names[names.index(start):]
    if redo:
        return names
    for i, s in enumerate(names):
        if not is_current(out, s):
            return names[i:]
    return []


def reuse_atlas(src, out):
    """Use an old tahoe_atlas.py build (same format): link its pseudobulk, copy its build files."""
    src = os.path.abspath(os.path.expanduser(src))
    if not os.path.exists(os.path.join(src, "build_info.json")):
        sys.exit(f"--reuse-atlas: {src} holds no build_info.json")
    atl = os.path.join(out, "atlas")
    os.makedirs(atl, exist_ok=True)
    pb = os.path.join(atl, "pseudobulk")
    if not os.path.exists(pb):
        os.symlink(os.path.join(src, "pseudobulk"), pb, target_is_directory=True)
    for f in ("build_info.json", "sample_map.csv", "well_position_check.csv"):
        if os.path.exists(os.path.join(src, f)):
            shutil.copy2(os.path.join(src, f), os.path.join(atl, f))
    log(f"Reusing the build in {src} (its pseudobulk is linked, not copied)")


def tidy_atlas(out):
    """The ported atlas code makes angles/ and reports/ folders (for the old agents): remove them while empty."""
    for d in ("angles", "reports"):
        p = os.path.join(out, "atlas", d)
        try:
            if os.path.isdir(p) and not os.listdir(p):
                os.rmdir(p)
        except OSError:
            pass


def run_stage(stage, a):
    t0 = time.time()
    clear_stamps_from(a.out, stage)
    if stage == "build":
        if a.stream:
            from . import stream
            stream.build(atlas_args(a), a.data_in)
        else:
            A.cmd_build(atlas_args(a))
        info = json.load(open(os.path.join(a.out, "atlas", "build_info.json"), encoding="utf-8"))
        stamp_stage(a.out, "build", A.EFFECTS_VERSION, info)
        tidy_atlas(a.out)
        return
    if stage == "effects":
        A.cmd_effects(atlas_args(a))
        stamp_stage(a.out, "effects", A.EFFECTS_VERSION,
                    json.load(open(os.path.join(a.out, "atlas", "effects", "info.json"), encoding="utf-8")))
        tidy_atlas(a.out)
        return
    mod = importlib.import_module(f"tahoemap.{STAGE_MODULE[stage]}")
    kw = {}
    if stage == "tensor":
        kw = {"dtype": a.tensor_dtype, "keep_well": not a.no_well_tensor}
    elif stage == "embed":
        kw = {"dims": a.dims, "min_active": a.min_active, "min_responsive": a.min_responsive}
    elif stage == "reference":
        kw = {"offline": a.offline}
        if a.reference_cache:
            kw["cache_dir"] = a.reference_cache
    mod.run(a.out, **kw)
    log(f"  stage {stage} finished in {(time.time() - t0) / 60:.1f} min")


def cmd_status(a):
    print(f"tahoemap {__version__}   data: {a.data_in}   output: {a.out}")
    for s in STAGES:
        st = read_stamp(a.out, s)
        try:
            cur = is_current(a.out, s)
        except Exception:  # noqa: BLE001
            cur = False
        mark = "done" if cur else ("out of date" if st else "not run")
        when = st.get("finished", "") if st else ""
        print(f"  {s:<10} {mark:<12} {when}")
    nxt = plan(a.out, skip=("reference",) if a.offline else ())
    print("next: " + (" -> ".join(nxt) if nxt else "nothing; everything is up to date"))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tahoemap", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["run", "status"] + STAGES + list(LOOKUPS))
    ap.add_argument("names", nargs="*", help="look-ups: the gene / drug / line / module (pair: two genes)")
    ap.add_argument("--data", default=None, help="Tahoe-100M folder (default $TAHOE_DATA or ~/Tahoe-100M)")
    ap.add_argument("--out", default=None, help="output folder (default <data>/tahoemap)")
    ap.add_argument("--stream", action="store_true",
                    help="build: read the expression files straight from Hugging Face, one at a time (no 430 GB "
                         "download; ~17 GB of disk for the build)")
    ap.add_argument("--reuse-atlas", default=None, help="an old tahoe_atlas.py output folder whose build to reuse")
    ap.add_argument("--from", dest="start", choices=STAGES, default=None, help="run: start at this stage")
    ap.add_argument("--to", dest="stop", choices=STAGES, default=None, help="run: stop after this stage")
    ap.add_argument("--redo", action="store_true", help="run: redo every stage")
    ap.add_argument("--offline", action="store_true", help="no downloads: skip the reference annotations")
    ap.add_argument("--reference-cache", default=None, help="folder that keeps the reference downloads")
    ap.add_argument("--workers", type=int, default=0, help="build: plates at once (default: from CPUs and memory)")
    ap.add_argument("--batch-size", type=int, default=20000)
    ap.add_argument("--limit-files", type=int, default=0, help="trial build on the first N files (own --out!)")
    ap.add_argument("--layout", default=None, help="CSV sample,well overriding the well positions")
    ap.add_argument("--unreliable-plates", default=None, help="effects: comma list or 'none' (default plate13)")
    ap.add_argument("--min-cells", type=int, default=0, help="cells per line per well (default 30)")
    ap.add_argument("--reindex", action="store_true")
    ap.add_argument("--tensor-dtype", choices=["float32", "float16"], default="float32",
                    help="tensor: storage of the per-well x line values R (float16 halves its 4.4 GB)")
    ap.add_argument("--no-well-tensor", action="store_true", help="tensor: do not keep R (per well x line)")
    ap.add_argument("--dims", type=int, default=64, help="embed: dimensions of the vector space")
    ap.add_argument("--min-active", type=int, default=10, help="embed: significant genes a drug-dose needs")
    ap.add_argument("--min-responsive", type=int, default=5, help="embed: contexts with |z| >= 3 a gene needs")
    ap.add_argument("--top", type=int, default=15, help="look-ups: rows per table")
    a = ap.parse_args(argv)
    a.data = os.path.abspath(os.path.expanduser(a.data)) if a.data else default_data()
    a.out = os.path.abspath(os.path.expanduser(a.out)) if a.out else os.path.join(a.data, "tahoemap")
    a.data_in = os.path.join(a.out, "hf") if a.stream else a.data
    if a.stream:
        os.makedirs(a.data_in, exist_ok=True)
    elif not os.path.isdir(a.data) and a.command in ("run", "build"):
        sys.exit(f"No data folder {a.data}: download Tahoe-100M there (tahoe download), give --data, or use "
                 "--stream to read it from Hugging Face")
    if a.stream is False and os.path.isdir(os.path.join(a.out, "hf", "metadata")) and \
            not os.path.isdir(os.path.join(a.data, "metadata")):
        a.data_in = os.path.join(a.out, "hf")                    # a streamed build: keep using its metadata
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    T.safe_console()
    if a.command in LOOKUPS:
        from . import query
        return query.main(a)
    if a.command == "status":
        return cmd_status(a)
    mark_output(a.out)
    T.start_run_log(os.path.join(a.out, "run.log"), "tahoemap " + " ".join(sys.argv[1:] if argv is None else argv))
    try:
        with T.keep_awake(f"tahoemap {a.command}"):
            if a.reuse_atlas:
                reuse_atlas(a.reuse_atlas, a.out)
            if a.command == "run":
                todo = plan(a.out, a.start, a.stop, a.redo, skip=("reference",) if a.offline else ())
                log("Plan: " + (" -> ".join(todo) if todo else "nothing to do; everything is up to date"))
                t0 = time.time()
                for s in todo:
                    log(f"===== stage {s} =====")
                    run_stage(s, a)
                log(f"Run done in {(time.time() - t0) / 60:.1f} min. Vault: {os.path.join(a.out, 'vault')}  "
                    f"map: {os.path.join(a.out, 'map', 'gene_map.html')}")
            else:
                run_stage(a.command, a)
    except SystemExit as e:
        T.log_exit(e)
        raise


if __name__ == "__main__":
    main()
