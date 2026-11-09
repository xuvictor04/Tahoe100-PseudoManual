"""python -m tahoemap <command> - the one-shot pipeline and the look-ups. The `tahoe` shell wrapper calls this.

    run         every stage that is missing or out of date, in order (the one-shot job)
    build ... map, explorer     one stage (and nothing else)
    status      what is done, what is out of date (and why), what runs next
    gene SYMBOL | drug NAME | line NAME | pair A B | module N     look-ups on a finished run
    review plan|run|status|tables|stop   the literature-review agents (tahoemap/review; docs/review.md)
    duplicate DEST [--repo DIR]     copy a finished output folder for review work (big arrays hard-linked)
    export DEST [--with-effects] [--include FILE ...] [--force]     the shareable results, ready to be committed and
                pushed to a GitHub branch (tahoemap/export.py)
    export DEST --explorer [--force] [--with-line-dd] [--github OWNER/REPO]     the explorer, ready to publish: the
                pages (GitHub Pages, branch 'site'), the data repository, and the scripts that push them

A stage is out of date when it never finished, its method changed, it ran with other values of the options that
change its results (--dims, --min-cells, ...: once given they stay in force for the output folder, so a stopped run
resumes with the settings it started with), or (reference, on a run with network) a source did not load last time.
`run --from reference` or `run --refresh-reference` fetches the public annotations again.
"""

import argparse
import atexit
import glob
import importlib
import json
import os
import shutil
import subprocess
import sys
import time
import warnings

from . import __version__
from . import atlas_core as A
from . import stream
from . import tlib as T
from .common import (GIT_MISSING, STAGES, PipelineLock, clear_stamps_from, find_git, git_out, in_use_text, is_link,
                     log, mark_output, read_stamp, remove_file, stamp_stage, write_json)

STAGE_MODULE = {"tensor": "tensor", "tables": "tables", "embed": "embed", "reference": "reference",
                "relations": "relations", "graph": "graph", "direction": "direction", "validate": "validate",
                "vault": "vault", "map": "html_map", "explorer": "explorer"}
LOOKUPS = ("gene", "drug", "line", "pair", "module")
EXTRA_COMMANDS = ("review", "duplicate", "export")   # not stages: they read a finished output (never run the
                                                     # pipeline)

# Options that change a stage's results. Each stage records them in its stamp (info.options); a run that sets one to
# another value than the stage ran with redoes that stage and every later one. Once given they are remembered for the
# output folder (RUN_OPTIONS) and used by later runs that do not give them.
RESULT_OPTIONS = {"build": ("layout",), "effects": ("min_cells", "unreliable_plates"),
                  "tensor": ("tensor_dtype", "no_well_tensor"), "embed": ("dims", "min_active", "min_responsive"),
                  "vault": ("site_url",), "map": ("site_url",),
                  "explorer": ("site_url", "data_url", "line_dd", "pooled_r")}
# Recorded too, but compared differently: --limit-files as it is (a trial build is redone by a run without it);
# --offline never forces a redo (it reads the same cache), but a run with network retries the sources that failed;
# --pages-max-mb only moves parts of the explorer between its two volumes (a run with another value does not redo it).
RECORDED_OPTIONS = {"build": ("limit_files",), "reference": ("offline",), "explorer": ("pages_max_mb",)}
REMEMBERED = tuple(dict.fromkeys(k for v in RESULT_OPTIONS.values() for k in v))
# on / off options: their two spellings
SWITCHES = {"no_well_tensor": ("--no-well-tensor", "--well-tensor"), "line_dd": ("--with-line-dd", "--no-line-dd"),
            "pooled_r": ("--with-pooled-r", "--no-pooled-r")}
PAGES_MAX_MB = 950.0                       # explorer.PAGES_MAX_MB: the default of --pages-max-mb (MiB)
RUN_OPTIONS = "run_options.json"           # in OUT: the result options given to earlier runs
RETRY_SOURCES = ("failed", "offline")      # reference source statuses (prefixes) that a run with network retries
REUSED = "reused_from.json"                # in OUT/atlas: the --reuse-atlas source and how it is linked
JOB_PID = ".job.pid"                       # in OUT: the background job's pid (written by the `tahoe` wrapper)
JOB_ENV = "TAHOE_JOB"                      # set by the wrapper for a background job


def make_parser():
    ap = argparse.ArgumentParser(prog="tahoemap", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["run", "status"] + STAGES + list(LOOKUPS) + list(EXTRA_COMMANDS))
    ap.add_argument("names", nargs="*", help="look-ups: the gene / drug / line / module (pair: two genes); review: "
                                             "plan, run, status, tables or stop; duplicate, export: the destination "
                                             "folder")
    ap.add_argument("--data", default=None, help="Tahoe-100M folder (default $TAHOE_DATA or ~/Tahoe-100M)")
    ap.add_argument("--out", default=None, help="output folder (default <data>/tahoemap)")
    ap.add_argument("--stream", action="store_true",
                    help="build: read the expression files straight from Hugging Face, one at a time (no 430 GB "
                         "download; ~17 GB of disk for the build). A stopped streamed build continues streaming.")
    ap.add_argument("--reuse-atlas", default=None, help="an old tahoe_atlas.py output folder whose build to reuse")
    ap.add_argument("--from", dest="start", choices=STAGES, default=None, help="run: start at this stage")
    ap.add_argument("--to", dest="stop", choices=STAGES, default=None, help="run: stop after this stage")
    ap.add_argument("--redo", action="store_true",
                    help="run: redo every stage (the build sums every plate again: its finished plates are removed "
                         "first); review run: review entities again that are done")
    ap.add_argument("--offline", action="store_true",
                    help="no downloads: the reference stage uses only its cache (else Tahoe's own gene names)")
    ap.add_argument("--refresh-reference", action="store_true",
                    help="run: download the public annotations again even if cached (and redo the stages after)")
    ap.add_argument("--reference-cache", default=None, help="folder that keeps the reference downloads")
    ap.add_argument("--workers", type=int, default=0, help="build: plates at once (default: from CPUs and memory)")
    ap.add_argument("--batch-size", type=int, default=20000)
    ap.add_argument("--limit-files", type=int, default=0, help="trial build on the first N files (own --out!)")
    ap.add_argument("--allow-partial", action="store_true",
                    help="build: build from a download with files missing (else the build stops and names them)")
    ap.add_argument("--layout", default=None, help="CSV sample,well overriding the well positions")
    ap.add_argument("--unreliable-plates", default=None, help="effects: comma list or 'none' (default plate13)")
    ap.add_argument("--min-cells", type=int, default=0, help="cells per line per well (default 30)")
    ap.add_argument("--reindex", action="store_true")
    ap.add_argument("--tensor-dtype", choices=["float32", "float16"], default="float32",
                    help="tensor: storage of the per-well x line values R (float16 halves its 4.4 GB)")
    ap.add_argument("--no-well-tensor", action="store_true", help="tensor: do not keep R (per well x line)")
    ap.add_argument("--well-tensor", dest="no_well_tensor", action="store_false",
                    help="tensor: keep R again after an earlier --no-well-tensor")
    ap.add_argument("--dims", type=int, default=64, help="embed: dimensions of the vector space")
    ap.add_argument("--min-active", type=int, default=10, help="embed: significant genes a drug-dose needs")
    ap.add_argument("--min-responsive", type=int, default=5, help="embed: contexts with |z| >= 3 a gene needs")
    ap.add_argument("--top", type=top_value, default=None,
                    help="look-ups: rows per table (default 15; the probable-direction lists show 10 unless --top is "
                         "given); --top all (or 0) shows every row")
    ap.add_argument("--truth", default=None, help="validate: ground_truth.json of synthetic test data (tests only)")
    g = ap.add_argument_group("explorer (the searchable web pages over every result: OUT/explorer; "
                              "docs/explorer.md)")
    g.add_argument("--site-url", default=None,
                   help="the explorer's web address, which the vault, the map, the look-ups and the explorer link to "
                        "(default: the GitHub Pages address of this code's repository, https://OWNER.github.io/REPO/, "
                        "read from `git remote get-url origin`; 'none': no site, the links name the local files)")
    g.add_argument("--data-url", default=None,
                   help="explorer: where the pages read the data repository from (default: "
                        "https://raw.githubusercontent.com/OWNER/REPO-data/main/ of the same repository)")
    g.add_argument("--with-line-dd", dest="line_dd", action="store_true", default=False,
                   help="explorer: also the optional volume data_dd (per drug-dose, every gene's value in every cell "
                        "line; about 4.3 GB on the real data); export --explorer: publish it too")
    g.add_argument("--no-line-dd", dest="line_dd", action="store_false",
                   help="explorer: without data_dd again after an earlier --with-line-dd")
    g.add_argument("--with-pooled-r", dest="pooled_r", action="store_true", default=False,
                   help="explorer: also d/pooledr.js, a helper that ranks every gene by pooled-profile correlation "
                        "(about 40 MB on the real data)")
    g.add_argument("--no-pooled-r", dest="pooled_r", action="store_false",
                   help="explorer: without the pooled-r helper again")
    g.add_argument("--pages-max-mb", type=float, default=None,
                   help=f"explorer: the most the web volume may hold, in MiB (default {PAGES_MAX_MB:g}; GitHub Pages "
                        "publishes sites up to 1 GB). Above it, parts move to the data volume; nothing is dropped. If "
                        "moving is not enough, the stage stops and says what is too large")
    g = ap.add_argument_group("review (python -m tahoemap review plan|run|status|tables) and duplicate")
    g.add_argument("--kinds", default=None, help="review: which entities, a comma list of gene,drug,line (default all)")
    g.add_argument("--only", default=None, help="review: only these entities (comma list of names or ids such as "
                                                "gene:12, drug:NAME, line:CVCL_0023; or @FILE with one a line)")
    g.add_argument("--limit", type=int, default=0, help="review run: start at most N entities")
    g.add_argument("--max-usd", type=float, default=None,
                   help="review run: the most this run may spend, in USD (no default: give it, --limit, or --no-cap)")
    g.add_argument("--per-entity-usd", type=float, default=None,
                   help="review run: the most one entity's attempt may spend (default: the agent file's max_usd)")
    g.add_argument("--no-cap", action="store_true", help="review run: run without --max-usd / --limit")
    g.add_argument("--concurrency", type=int, default=4, help="review run: entities reviewed at once (threads)")
    g.add_argument("--model", default=None,
                   help="review: the reviewers' model (default: the one the agent files name); per agent: "
                        "AGENT=MODEL,... with AGENT gene, drug, line, checker, reviewers or all")
    g.add_argument("--effort", default=None,
                   help="review: the reviewers' effort, low|medium|high|xhigh|max (default: the agent files': "
                        "reviewers high, checker medium); per agent as for --model")
    g.add_argument("--verify", default="llm", choices=["llm", "ids", "off"],
                   help="review run: check cited ids (ids), and the claims against the abstracts (llm, default)")
    g.add_argument("--web", dest="web", action="store_true", default=True,
                   help="review run: let the agents use Anthropic's web search / fetch (default)")
    g.add_argument("--no-web", dest="web", action="store_false", help="review run: no web search / fetch")
    g.add_argument("--web-max-uses", type=int, default=5, help="review run: web searches (and fetches) per request")
    g.add_argument("--keys-file", default=None,
                   help="review run: Anthropic API keys, one a line (else ANTHROPIC_API_KEYS / ANTHROPIC_API_KEY)")
    g.add_argument("--no-prompt", action="store_true",
                   help="review run: never ask for a new key when every key is used up; pause (exit code 3) instead "
                        "(a run nobody watches, e.g. started with Start-Process)")
    g.add_argument("--dry-run", action="store_true",
                   help="review run: write the dossiers and first requests to OUT/review/dry_run/; send nothing")
    g.add_argument("--fake", default=None, metavar="SCRIPT",
                   help="review run: a scripted fake API instead of Anthropic's (tests; tahoemap/review/fake.py)")
    g.add_argument("--retry-failed", action="store_true",
                   help="review run: also retry entities left alone after repeated failures (not the done ones)")
    g.add_argument("--recheck", action="store_true",
                   help="review run: only complete the verification of stored reviews that lack it (ids that could "
                        "not be looked up, a citation check that did not run); the reviewer is not run again")
    g.add_argument("--tables", action="store_true", help="review status: also rebuild the review tables")
    g.add_argument("--repo", default=None, metavar="DIR",
                   help="duplicate: also clone this code repository into DIR (git clone)")
    g = ap.add_argument_group("export (python -m tahoemap export DEST: the shareable results for a GitHub branch)")
    g.add_argument("--with-effects", action="store_true",
                   help="export: also atlas/effects (the pooled gene x drug-dose matrices, CSV tables) and "
                        "atlas/reports")
    g.add_argument("--include", action="append", nargs="+", default=None, metavar="FILE",
                   help="export: also these files or folders, at the top of DEST (e.g. a RUN_REPORT.md)")
    g.add_argument("--force", action="store_true",
                   help="export: update an earlier export in DEST (only the files its MANIFEST.tsv lists are "
                        "replaced or removed)")
    g.add_argument("--max-file-mb", type=float, default=95.0,
                   help="export: files larger than this many MiB are not copied (GitHub refuses files over 100 MB); "
                        "export --explorer: such a file stops the export")
    g.add_argument("--explorer", action="store_true",
                   help="export: the explorer instead of the results: DEST/site (the pages, for GitHub Pages), "
                        "DEST/data (the data repository; hard links when on the same disk), the upload lists, "
                        "publish.ps1 / publish.sh and PUBLISH.md (the one-time GitHub steps). It never runs git push")
    g.add_argument("--github", default=None, metavar="OWNER/REPO",
                   help="export --explorer: the GitHub repository of the pages (branch 'site'); the data go to "
                        "OWNER/REPO-data (default: this code's repository, from `git remote get-url origin`)")
    g.add_argument("--pin-data", default=None, metavar="SHA",
                   help="export DEST --explorer --pin-data SHA: point DEST/site at this commit of the data repository "
                        "(rewrites site/d/hosts.js and its MANIFEST.tsv line; publish.ps1 does it)")
    g.add_argument("--pin-data-dd", default=None, metavar="SHA",
                   help="export DEST --explorer --pin-data-dd SHA: the same for the optional data_dd repository")
    return ap


def top_value(v):
    """--top: a whole number of rows, or 'all' (also 0) for every row (query.parse_top)."""
    from .query import parse_top
    try:
        return parse_top(v)
    except ValueError as e:
        raise argparse.ArgumentTypeError(str(e)) from None


def given_options(argv):
    """The result options given on this command line (the others are at their defaults)."""
    unset = object()                     # not a string: argparse would convert a string default with the option's type
    probe = make_parser()
    probe.set_defaults(**{k: unset for k in REMEMBERED})
    got = probe.parse_args(argv)
    return {k for k in REMEMBERED if getattr(got, k) is not unset}


def option_text(k, v):
    if k in SWITCHES:
        return SWITCHES[k][0 if v else 1]
    return f"--{k.replace('_', '-')} " + ("(default)" if v is None else repr(v) if v == "" else str(v))


def remember_options(a, given, save):
    """Result options given now are remembered for this output; the ones not given come from earlier runs.
    Sets a.set_options (the options a user chose, now or before) and returns those taken from earlier runs."""
    p = os.path.join(a.out, RUN_OPTIONS)
    rem = read_json(p) or {}
    a.set_options, earlier = set(given), []
    for k in REMEMBERED:
        if k in given:
            rem[k] = getattr(a, k)
        elif k in rem:
            setattr(a, k, rem[k])
            a.set_options.add(k)
            if rem[k] != a.defaults[k]:
                earlier.append(option_text(k, rem[k]))
    if save and given:
        os.makedirs(a.out, exist_ok=True)
        write_json(rem, p)
    return earlier


def default_data():
    return os.path.abspath(os.path.expanduser(os.environ.get("TAHOE_DATA", "~/Tahoe-100M")))


def atlas_args(a):
    """The namespace atlas_core.cmd_build / cmd_effects (and stream.build / build_local) expect."""
    return argparse.Namespace(data=a.data_in, out=os.path.join(a.out, "atlas"), reindex=a.reindex,
                              limit_files=a.limit_files, workers=a.workers, batch_size=a.batch_size,
                              layout=a.layout, unreliable_plates=a.unreliable_plates, min_cells=a.min_cells,
                              allow_partial=a.allow_partial)


def read_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def build_complete(out):
    atl = os.path.join(out, "atlas")
    info = read_json(os.path.join(atl, "build_info.json"))
    if not info or not os.path.exists(os.path.join(atl, "sample_map.csv")):
        return False
    return len(glob.glob(os.path.join(atl, "pseudobulk", "group*_profiles.csv"))) == info.get("groups", -1)


def effects_complete(out):
    info = read_json(os.path.join(out, "atlas", "effects", "complete.json")) or {}
    return info.get("version") == A.EFFECTS_VERSION


def stage_version(stage):
    if stage in ("build", "effects"):
        return A.EFFECTS_VERSION
    return getattr(importlib.import_module(f"tahoemap.{STAGE_MODULE[stage]}"), "VERSION", 1)


def reference_missing(out, info):
    """Reference sources that did not load on its last run (failed, or skipped offline with no cached file)."""
    src = info.get("sources")
    if not isinstance(src, dict):
        recs = (read_json(os.path.join(out, "reference", "sources.json")) or {}).get("sources") or {}
        src = {k: (v or {}).get("status") for k, v in recs.items()}
    return sorted(k for k, s in src.items() if str(s or "").startswith(RETRY_SOURCES))


def stage_state(a, stage, assets=True):
    """'' when the stage's stamp is current for this run, else why the stage must run. Reads only. assets False: the
    explorer's page files (tahoemap/explorer_app) are not compared (explorer_assets_only)."""
    st = read_stamp(a.out, stage)
    if st is None:
        return "not run yet"
    try:
        if st.get("version") != stage_version(stage):
            return "its method changed"
    except ImportError:
        return "its module is missing"
    info = st.get("info") or {}
    ran = info.get("options") or {}
    for k in RESULT_OPTIONS.get(stage, ()):
        before = ran.get(k, a.defaults[k])
        if k in a.set_options and getattr(a, k) != before:
            return f"{option_text(k, getattr(a, k))} now, {option_text(k, before)} when it ran"
    if stage == "build":
        lim = int(info.get("limit_files") or 0)
        if lim != a.limit_files:
            return (f"it used only the first {lim} files" if lim else "it used every file") + \
                (f"; now --limit-files {a.limit_files}" if a.limit_files else "")
        n, data = info.get("n_files"), info.get("data")
        if info.get("partial") and n and data:
            now = len(glob.glob(os.path.join(data, "data", "*.parquet")))
            if now > n:
                return f"it was built from {n} files (--allow-partial); {now} are there now"
    if stage in ("vault", "map"):                    # they show the literature reviews of OUT/review (if any)
        from .vault import review_fingerprint
        now_fp = review_fingerprint(a.out)
        if (info.get("review") or None) != now_fp:
            return ("the literature reviews (review/) changed since it ran" if now_fp else
                    "the literature reviews it shows (review/) are gone")
    if stage == "reference" and not a.offline:
        if a.refresh_reference:
            return "--refresh-reference"
        miss = reference_missing(a.out, info)
        if miss:
            return (f"{len(miss)} source(s) did not load last time ({', '.join(miss)}); a run with network retries "
                    "them (--offline keeps the run as it is)")
    if stage == "explorer":
        from . import explorer as X
        if not os.path.isfile(os.path.join(a.out, "explorer", "manifest.json")):
            return "its folder (explorer/) is missing"
        if info.get("run") != X.run_id(a.out):
            return "the stages it was made from changed since it ran"
        if assets and (info.get("assets_sha") or None) != X.assets_sha():
            return EXPLORER_ASSETS
    return ""


EXPLORER_ASSETS = "its page files (tahoemap/explorer_app) changed: only they are copied again"


def explorer_assets_only(a):
    """True when the explorer is current in everything but its page files (tahoemap/explorer_app changed since it
    ran): then only those are copied again (explorer.refresh_assets: seconds, not the whole stage). --redo and
    --from explorer build it whole."""
    if a.redo or a.start == "explorer" or read_stamp(a.out, "explorer") is None:
        return False
    return stage_state(a, "explorer", assets=False) == "" and stage_state(a, "explorer") == EXPLORER_ASSETS


def plan(a, start=None, stop=None, redo=False, skip=()):
    """(stages to run, why): from the first stage that is missing or out of date (or `start`) to `stop`; every
    later stage follows. Reads only: the status command calls it too."""
    names = [s for s in STAGES if s not in skip]
    if stop:
        names = names[:names.index(stop) + 1]
    if start:
        return names[names.index(start):], f"--from {start}"
    if redo:
        return names, "--redo"
    for i, s in enumerate(names):
        why = stage_state(a, s)
        if why:
            return names[i:], f"{s}: {why}"
    return [], ""


def _link_dir(target, link):
    """A link to a folder: a symlink; on Windows without symlink rights a junction; else a copy. Returns how."""
    try:
        os.symlink(target, link, target_is_directory=True)
        return "symlink"
    except OSError as e:
        err = e
    if os.name == "nt":
        r = subprocess.run(["cmd", "/c", "mklink", "/J", link, target], capture_output=True, text=True)
        if r.returncode == 0 and os.path.isdir(link):
            return "junction"
    log(f"  could not link {target} ({err}); copying it instead (~17 GB on the full data) ...")
    tmp = link + ".part"
    shutil.rmtree(tmp, ignore_errors=True)
    shutil.copytree(target, tmp)
    os.replace(tmp, link)
    return "copy"


def reuse_atlas(src, out):
    """Use an old tahoe_atlas.py build (same format): link its pseudobulk, copy its build files."""
    src = os.path.abspath(os.path.expanduser(src))
    if not os.path.exists(os.path.join(src, "build_info.json")):
        sys.exit(f"--reuse-atlas: {src} holds no build_info.json")
    atl = os.path.join(out, "atlas")
    if os.path.isdir(atl) and os.path.samefile(src, atl):
        log(f"Reusing the build in {src} (this output's own atlas folder)")
        return
    os.makedirs(atl, exist_ok=True)
    pb, target = os.path.join(atl, "pseudobulk"), os.path.join(src, "pseudobulk")
    rec = read_json(os.path.join(atl, REUSED)) or {}
    if os.path.isdir(pb) and not is_link(pb) and not os.listdir(pb):
        os.rmdir(pb)                                          # an empty folder left by a build that never started
    if os.path.lexists(pb):
        if not (os.path.realpath(pb) == os.path.realpath(target) or rec.get("source") == src):
            sys.exit(f"--reuse-atlas: {pb} already holds a build that is not the one in {src}. Nothing was changed: "
                     "use a new, empty --out (or delete that pseudobulk folder) to reuse the old build.")
        how = rec.get("how", "symlink")
    else:
        how = _link_dir(target, pb)
        write_json({"source": src, "how": how}, os.path.join(atl, REUSED))
    for f in ("build_info.json", "sample_map.csv", "well_position_check.csv"):
        if os.path.exists(os.path.join(src, f)):
            shutil.copy2(os.path.join(src, f), os.path.join(atl, f))
    log(f"Reusing the build in {src} (its pseudobulk is " + ("copied)" if how == "copy" else f"linked: {how})"))


def adopt_reused(a):
    """Right after reuse_atlas: stamp the reused build (and effects found complete beside it) as done."""
    if read_stamp(a.out, "build") is None:
        if not build_complete(a.out):
            sys.exit(f"--reuse-atlas: {a.reuse_atlas} is not a complete build (its build_info.json, sample_map.csv "
                     "and plate groups do not match)")
        info = read_json(os.path.join(a.out, "atlas", "build_info.json")) or {}
        stamp_stage(a.out, "build", A.EFFECTS_VERSION, {**info, "adopted": a.reuse_atlas})
    if read_stamp(a.out, "effects") is None and effects_complete(a.out):
        info = read_json(os.path.join(a.out, "atlas", "effects", "info.json")) or {}
        stamp_stage(a.out, "effects", A.EFFECTS_VERSION, {**info, "adopted": a.reuse_atlas})


def check_metadata(a):
    """The effects stage needs Tahoe's gene metadata: say where it is missing before starting."""
    idx = T.discover(a.data_in, os.path.join(a.out, "atlas"))
    if not idx.get("gene"):
        sys.exit(f"Tahoe's gene metadata (metadata/gene_metadata.parquet) is not under {a.data_in}: give --data "
                 "with the Tahoe-100M folder that holds metadata/, or add --stream to fetch the metadata tables")


def tidy_atlas(out):
    """The ported atlas code makes angles/ and reports/ folders (for the old agents): remove them while empty."""
    for d in ("angles", "reports"):
        p = os.path.join(out, "atlas", d)
        try:
            if os.path.isdir(p) and not os.listdir(p):
                os.rmdir(p)
        except OSError:
            pass


def stage_options(a, stage):
    return {k: getattr(a, k) for k in RESULT_OPTIONS.get(stage, ()) + RECORDED_OPTIONS.get(stage, ())}


def record_options(a, stage):
    """Add this run's options to the stamp the stage's run() wrote."""
    st = read_stamp(a.out, stage)
    if st is not None:
        stamp_stage(a.out, stage, st.get("version"), {**(st.get("info") or {}), "options": stage_options(a, stage)})


def run_stage(stage, a):
    """Run one stage. On Windows a file of the output that another program has open cannot be replaced
    (common.FileInUse, or a PermissionError from the ported atlas code's own writes): the stage stops with a message
    naming the file and the likely holders, not a traceback."""
    if os.name != "nt":
        return _run_stage(stage, a)
    try:
        return _run_stage(stage, a)
    except PermissionError as e:
        msg = str(e) if getattr(e, "path", None) else in_use_text(getattr(e, "filename", None) or "a file of the "
                                                                  "output", f"{type(e).__name__}: {e}", "write")
        sys.exit(f"{stage}: {msg}")


def remove_built_plates(atl):
    """--redo: the build sums every plate again. The build keeps a plate whose files exist while the plate's list of
    input files is unchanged (atlas_core._build_group, verbatim: that is how a stopped build resumes), so data files
    replaced under the same names would keep the old sums. A redo therefore removes the finished plates
    (atlas/pseudobulk/group*) first; a run without --redo resumes as before."""
    pb = os.path.join(atl, "pseudobulk")
    files = sorted(f for f in glob.glob(os.path.join(pb, "group*")) if os.path.isfile(f))
    for f in files:
        remove_file(f)
    n = len({os.path.basename(f).split("_")[0].split(".")[0] for f in files})
    if files:
        log(f"  --redo: removed the {n} finished plate(s) of an earlier build from {pb} ({len(files)} files); every "
            "plate is summed again")
    return len(files)


def _run_stage(stage, a):
    t0 = time.time()
    atl = os.path.join(a.out, "atlas")
    if stage == "explorer" and explorer_assets_only(a):
        from . import explorer as X
        log("  explorer: only its page files (tahoemap/explorer_app) changed since it ran; copying them again "
            "(--redo builds the whole explorer)")
        X.refresh_assets(a.out)
        log(f"  stage explorer finished in {(time.time() - t0) / 60:.1f} min (page files only)")
        return
    if stage == "build":
        rec = read_json(os.path.join(atl, REUSED)) or {}
        if rec.get("how") in ("symlink", "junction") or is_link(os.path.join(atl, "pseudobulk")):
            sys.exit(f"build: this output's build is linked from {rec.get('source', 'an old atlas')} (--reuse-atlas) "
                     "and is not rebuilt here, so that folder stays as it is. Run from effects (--from effects), or "
                     "use a new --out to build from the data.")
    clear_stamps_from(a.out, stage)
    if stage == "build":
        for f in ("build_info.json", "sample_map.csv", os.path.join("effects", "complete.json"), REUSED):
            try:                                                 # not complete until this build writes them again
                os.remove(os.path.join(atl, f))
            except FileNotFoundError:
                pass
        if a.redo:
            remove_built_plates(atl)
        if a.stream:
            stream.build(atlas_args(a), a.data_in)
        else:
            stream.build_local(atlas_args(a))
        info = read_json(os.path.join(atl, "build_info.json")) or {}
        stamp_stage(a.out, "build", A.EFFECTS_VERSION, {**info, "options": stage_options(a, "build")})
        tidy_atlas(a.out)
        return
    if stage == "effects":
        A.cmd_effects(atlas_args(a))
        info = read_json(os.path.join(atl, "effects", "info.json")) or {}
        stamp_stage(a.out, "effects", A.EFFECTS_VERSION, {**info, "options": stage_options(a, "effects")})
        tidy_atlas(a.out)
        return
    mod = importlib.import_module(f"tahoemap.{STAGE_MODULE[stage]}")
    kw = {}
    if stage == "tensor":
        kw = {"dtype": a.tensor_dtype, "keep_well": not a.no_well_tensor}
    elif stage == "embed":
        kw = {"dims": a.dims, "min_active": a.min_active, "min_responsive": a.min_responsive}
    elif stage == "direction":
        # the cell lines' genetics: the Tahoe metadata under the data folder (a streamed build's OUT/hf too), else
        # the files atlas/file_index.json lists
        kw = {"data": a.data_in}
    elif stage == "validate" and a.truth:
        kw = {"truth": a.truth}
    elif stage in ("vault", "map"):
        kw = {"site_url": a.site_url}                 # None: the GitHub Pages address of this code (links.py)
    elif stage == "explorer":
        from . import links
        kw = {"site_url": links.site_url(a.site_url), "data_url": links.data_url(a.data_url), "line_dd": a.line_dd,
              "pooled_r": a.pooled_r,
              "pages_max_mb": a.pages_max_mb if a.pages_max_mb is not None else getattr(mod, "PAGES_MAX_MB",
                                                                                        PAGES_MAX_MB)}
    elif stage == "reference":
        kw = {"offline": a.offline, "refresh": a.refresh_reference and not a.offline}
        if a.reference_cache:
            kw["cache_dir"] = a.reference_cache
    mod.run(a.out, **kw)
    if stage in RESULT_OPTIONS or stage in RECORDED_OPTIONS:
        record_options(a, stage)
    log(f"  stage {stage} finished in {(time.time() - t0) / 60:.1f} min")


def cmd_status(a):
    print(f"tahoemap {__version__}   data: {a.data_in}   output: {a.out}")
    for s in STAGES:
        st = read_stamp(a.out, s)
        try:
            why = stage_state(a, s)
        except Exception as e:  # noqa: BLE001
            why = f"cannot tell: {e}"
        mark = "done" if not why else ("out of date" if st else "not run")
        when = st.get("finished", "") if st else ""
        print(f"  {s:<10} {mark:<12} {when}" + (f"  ({why})" if why and st else ""))
    for ln in explorer_status(a.out):
        print(ln)
    nxt, why = plan(a)
    print("next: " + (" -> ".join(nxt) + f"   ({why})" if nxt else "nothing; everything is up to date"))


def _mb(n):
    return f"{(n or 0) / 1e6:,.1f} MB"


def explorer_status(out):
    """What the explorer stage recorded (status): bytes and files per volume, its row-count checks (every row of each
    source table in each of its views), the exact check against tables/drug_effects, the self-check, the size
    guard's moves, its warnings, and where to open it. [] when it has not run."""
    st = read_stamp(out, "explorer")
    if not st:
        return []
    i = st.get("info") or {}
    vols = i.get("volumes") or {}
    L = ["explorer: " + "; ".join(f"{n} {_mb(v.get('bytes'))} in {v.get('files', 0):,} files" for n, v in vols.items())]
    comp = i.get("complete") or {}
    short = [f"{src} -> {view}: {got:,} of {want:,} rows" for src, r in sorted(comp.items())
             for view, (want, got) in sorted((r.get("views") or {}).items()) if want != got]
    n_views = sum(len(r.get("views") or {}) for r in comp.values())
    L.append(f"  rows: {len(comp)} source tables, shown in {n_views} places; " +
             ("each place holds every row of its table" if not short else
              f"{len(short)} place(s) miss rows: " + "; ".join(short[:5])))
    ch = i.get("checks") or {}
    de = ch.get("drug_effects") or {}
    if de:
        diff = sum(int(v or 0) for v in (de.get("different") or {}).values())
        L.append(f"  tables/drug_effects: {int(de.get('rows') or 0):,} rows compared with the explorer's values, "
                 f"{diff} difference(s)")
    sc = ch.get("self_check") or {}
    if sc:
        L.append(f"  self-check: {int(sc.get('files') or 0):,} of {int(sc.get('of') or 0):,} files decoded and "
                 f"compared with the sources, {int(sc.get('n_problems') or 0)} difference(s)")
    moves = i.get("moves") or []
    web0 = i.get("web_bytes_before_moves")
    lim = i.get("pages_max_mb")
    L.append("  size guard: " + ("no part moved" if not moves else "moved to the data volume (nothing dropped): "
                                    + "; ".join(f"{m.get('what', m.get('part'))} ({m.get('files', 0):,} files, "
                                                f"{_mb(m.get('bytes_freed'))})" for m in moves))
             + (f" (the pages held {_mb(web0)} before any move; the limit is {lim:g} MiB)"
                if web0 is not None and lim else ""))
    for w in (i.get("warnings") or [])[:5]:
        L.append(f"  warning: {w}")
    L.append(f"  open: {os.path.join(out, 'explorer', 'web', 'index.html')}"
             + (f"   (its address once published: {i['site_url']})" if i.get("site_url") else ""))
    return L


# duplicate: in these folders the arrays and tables are written once (to a .tmp file, then swapped in), so a hard link
# shares them safely: a stage that runs again in either copy replaces the file instead of writing into it. (On Windows
# a file in use cannot be replaced, and the two names are one file: not while the other copy has it open.)
HARDLINK_DIRS = ("atlas", "tensor", "tables", "embed", "relations", "graph", "direction")
HARDLINK_EXT = (".npy", ".npz", ".parquet")
DUPLICATED = "duplicated_from.json"


def _git(repo, *args):
    """stdout of `git -C repo ARGS`, or None (git not found - common.find_git -, or it failed)."""
    return git_out(find_git(), repo, *args)


def _inside(a, b, P=os.path):
    """a is b or lies inside b, compared as the file system does (case-insensitive on Windows; links and junctions
    resolved). P: the path module (ntpath in the tests)."""
    for f in (P.abspath, P.realpath):
        x, y = P.normcase(f(a)), P.normcase(f(b))
        if x == y or x.startswith(y.rstrip(P.sep) + P.sep):
            return True
    return False


def _keep_dir_link(sp, dp):
    """A link to a folder found by duplicate: a symbolic link is made again with its own target (relative ones
    stay relative); a junction (Windows: os.path.islink is False for one), or a symlink this account may not make,
    with _link_dir - a symlink, else a junction, else (the last resort) a copy. Returns how."""
    tgt = os.readlink(sp)
    if os.path.islink(sp):
        try:
            os.symlink(tgt, dp, target_is_directory=True)
            return "symlink"
        except OSError:
            pass
    if tgt.startswith("\\\\?\\") and not tgt.startswith("\\\\?\\UNC\\"):
        tgt = tgt[4:]                                   # (a junction's target as os.readlink gives it: \\?\C:\...)
    return _link_dir(os.path.join(os.path.dirname(sp), tgt), dp)


def duplicate(src, dest, repo=None):
    """Copy the output folder `src` to `dest` for review work: large immutable arrays hard-linked when on the same
    file system (else copied), everything else copied, symbolic links kept as links; temporary and job files left
    out. Writes dest/duplicated_from.json. With `repo`, also `git clone`s this code repository there. Returns the
    record."""
    src, dest = os.path.abspath(src), os.path.abspath(dest)
    if not os.path.isdir(os.path.join(src, "stages")):
        sys.exit(f"duplicate: {src} is not a tahoemap output folder (no stages/); give --out with one")
    if os.path.exists(dest) and (not os.path.isdir(dest) or os.listdir(dest)):
        sys.exit(f"duplicate: {dest} exists and is not empty; give a new folder")
    if _inside(dest, src) or _inside(src, dest):
        sys.exit("duplicate: the destination must lie outside the output folder (and not contain it)")
    code_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git = find_git()
    if repo:
        repo = os.path.abspath(os.path.expanduser(repo))
        if os.path.exists(repo) and os.listdir(repo):
            sys.exit(f"duplicate --repo: {repo} exists and is not empty; give a new folder")
        if git is None:
            sys.exit(f"duplicate --repo: {GIT_MISSING}")
        if git_out(git, code_root, "rev-parse", "--show-toplevel") is None:
            sys.exit(f"duplicate --repo: {code_root} is not a git repository (or {git} could not be run)")
    os.makedirs(dest, exist_ok=True)
    n = {"hard_linked": 0, "copied": 0, "symlinks": 0, "skipped": 0}
    size = {"hard_linked": 0, "copied": 0}
    t0 = time.time()
    log(f"Duplicating {src} -> {dest} ...")
    for root, dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        top = rel.split(os.sep)[0] if rel != "." else ""
        droot = os.path.join(dest, rel) if rel != "." else dest
        os.makedirs(droot, exist_ok=True)
        for d in list(dirs):
            sp = os.path.join(root, d)
            if is_link(sp):                        # e.g. atlas/pseudobulk of a --reuse-atlas output: keep the link
                if _keep_dir_link(sp, os.path.join(droot, d)) != "copy":     # (a symlink or a junction)
                    n["symlinks"] += 1
                dirs.remove(d)
        for f in files:
            sp, dp = os.path.join(root, f), os.path.join(droot, f)
            if f.endswith((".tmp", ".part")) or f in (JOB_PID, ".run.lock", ".pipeline.lock", ".stop") \
                    or (rel == "." and f == DUPLICATED):
                n["skipped"] += 1
                continue
            if os.path.islink(sp):
                os.symlink(os.readlink(sp), dp)
                n["symlinks"] += 1
                continue
            if top in HARDLINK_DIRS and f.endswith(HARDLINK_EXT):
                try:
                    os.link(sp, dp)
                    n["hard_linked"] += 1
                    size["hard_linked"] += os.path.getsize(sp)
                    continue
                except OSError:                    # another file system, or links not allowed: copy
                    pass
            shutil.copy2(sp, dp)
            n["copied"] += 1
            size["copied"] += os.path.getsize(sp)
    stamps = {s: read_stamp(src, s) for s in STAGES}
    status = git_out(git, code_root, "status", "--porcelain")
    rec = {"source": src, "destination": dest, "date": time.strftime("%Y-%m-%d %H:%M:%S"),
           "code": {"version": __version__, "repository": code_root,
                    "commit": git_out(git, code_root, "rev-parse", "HEAD"),
                    "branch": git_out(git, code_root, "rev-parse", "--abbrev-ref", "HEAD"),
                    "uncommitted_changes": None if status is None else bool(status),     # None: unknown (no git)
                    "remote": git_out(git, code_root, "remote", "get-url", "origin")},
           "stages": {s: v for s, v in stamps.items() if v}, "files": n,
           "bytes": size, "hard_linked": f"*{', *'.join(HARDLINK_EXT)} under {', '.join(HARDLINK_DIRS)} "
                                         "(when on the same file system)", "repo_clone": None}
    if repo:
        if rec["code"]["uncommitted_changes"]:
            log("  note: the code repository has uncommitted changes; the clone gets only what is committed")
        try:
            r = subprocess.run([git, "clone", "--quiet", code_root, repo], capture_output=True, encoding="utf-8",
                               errors="replace")
            err = r.stderr.strip()[:500] if r.returncode != 0 else ""
        except OSError as e:
            err = f"{git} could not be run: {e}"
        if err:
            log(f"  git clone failed: {err}")
        else:
            rec["repo_clone"] = {"path": repo, "commit": git_out(git, repo, "rev-parse", "HEAD"),
                                 "branch": git_out(git, repo, "rev-parse", "--abbrev-ref", "HEAD")}
            log(f"  code cloned to {repo} (branch {rec['repo_clone']['branch']}, its origin is {code_root})")
    if git is None:
        log(f"  note: {GIT_MISSING}; {DUPLICATED} records no commit")
    write_json(rec, os.path.join(dest, DUPLICATED))
    log(f"Duplicated in {time.time() - t0:.0f} s: {n['hard_linked']:,} files hard-linked "
        f"({size['hard_linked'] / 1e9:.2f} GB shared), {n['copied']:,} copied ({size['copied'] / 1e9:.2f} GB), "
        f"{n['symlinks']} links kept, {n['skipped']} temporary files left out. Use --out {dest} for the copy.")
    return rec


def cmd_duplicate(a):
    if len(a.names or []) != 1:
        sys.exit("usage: python -m tahoemap duplicate DEST [--out SOURCE_OUTPUT] [--repo DIR]")
    return duplicate(a.out, os.path.expanduser(a.names[0]), a.repo)


def _drop_pid_file(path, pid):
    try:
        with open(path, encoding="utf-8") as fh:
            mine = fh.read().strip() == str(pid)
        if mine:
            os.remove(path)
    except OSError:
        pass


def job_setup(out):
    """A background job of the `tahoe` wrapper leads its own process group (so `tahoe stop` reaches its workers and
    downloads too); every pipeline command removes the wrapper's pid file when it ends, if the file names it."""
    if os.environ.pop(JOB_ENV, None) and hasattr(os, "setpgrp") and os.getpgrp() != os.getpid():
        try:
            os.setpgrp()
        except OSError:
            pass
    atexit.register(_drop_pid_file, os.path.join(out, JOB_PID), os.getpid())


def main(argv=None):
    ap = make_parser()
    a = ap.parse_args(argv)
    if a.start and a.stop and STAGES.index(a.start) > STAGES.index(a.stop):
        sys.exit(f"--from {a.start} comes after --to {a.stop}: nothing to run (the stages in order: "
                 f"{' '.join(STAGES)})")
    if a.reuse_atlas and (a.command == "build" or "build" in (a.start, a.stop)):
        sys.exit("--reuse-atlas reuses the build: it does not go with the build command or with --from / --to build")
    a.defaults = {k: ap.get_default(k) for k in REMEMBERED}
    a.data = os.path.abspath(os.path.expanduser(a.data)) if a.data else default_data()
    a.out = os.path.abspath(os.path.expanduser(a.out)) if a.out else os.path.join(a.data, "tahoemap")
    if a.layout:
        a.layout = os.path.abspath(os.path.expanduser(a.layout))
    computes = a.command == "run" or a.command in STAGES
    earlier = remember_options(a, given_options(argv), save=computes)
    notes = [f"Options given to an earlier run on this output: {', '.join(earlier)} (give one to change it)"] \
        if earlier else []
    hf = os.path.join(a.out, "hf")
    if not a.stream and a.command in ("run", "build") and os.path.exists(os.path.join(hf, stream.FILE_PLATES)) \
            and not glob.glob(os.path.join(a.data, "data", "*.parquet")) and not a.reuse_atlas \
            and (a.command == "build" or stage_state(a, "build")):
        a.stream = True                       # never index the files in flight as if they were the whole data
        notes.append("This output's build was started with --stream and is not finished: it continues streaming "
                     "(as with --stream)")
    if a.stream:
        a.data_in = hf
        os.makedirs(hf, exist_ok=True)
    elif os.path.isdir(os.path.join(hf, "metadata")) and not os.path.isdir(os.path.join(a.data, "metadata")):
        a.data_in = hf                                          # a streamed build: keep using its metadata
    else:
        a.data_in = a.data
    if a.data_in == a.data and not os.path.isdir(a.data) and a.command in ("run", "build"):
        sys.exit(f"No data folder {a.data}: download Tahoe-100M there (tahoe download), give --data, or use "
                 "--stream to read it from Hugging Face" + (" (with --reuse-atlas it fetches the metadata tables)"
                                                            if a.reuse_atlas else ""))
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    T.safe_console()
    if a.command in LOOKUPS:
        from . import query
        return query.main(a)
    if a.command == "status":
        return cmd_status(a)
    if a.command == "review":
        from .review import runner
        from .vault import review_fingerprint
        job_setup(a.out)                               # `tahoe review run --background`: a job like `tahoe run`
        fp0 = review_fingerprint(a.out)
        code = runner.cli(a)
        if (a.names or ["status"])[0] in ("run", "tables") and review_fingerprint(a.out) != fp0 \
                and read_stamp(a.out, "vault") is not None:
            print("To put the reviews into the vault notes and the map, rebuild those two stages: `tahoe vault` "
                  "then `tahoe map` (python -m tahoemap vault, then map, with this --out); `tahoe run` does the same, "
                  "as it sees both out of date.")
        if code:
            sys.exit(code)
        return None
    if a.command == "duplicate":
        return cmd_duplicate(a)
    if a.command == "export":
        from . import export
        return export.cli(a)
    mark_output(a.out)
    lock = PipelineLock(a.out, "tahoemap " + " ".join(sys.argv[1:] if argv is None else argv))
    ok, who = lock.acquire()
    if not ok:                                  # two commands computing on one output would overwrite each other
        sys.exit(f"Another tahoemap command is working on {a.out} ({who}; lock file {lock.path}). Wait for it to "
                 "finish, or stop it first. If you are sure that nothing runs there, delete that file.")
    job_setup(a.out)
    T.start_run_log(os.path.join(a.out, "run.log"), "tahoemap " + " ".join(sys.argv[1:] if argv is None else argv))
    try:
        with T.keep_awake(f"tahoemap {a.command}"):
            for n in notes:
                log(n)
            skip = ()
            if a.reuse_atlas:
                if a.stream:
                    stream.fetch_metadata(os.path.join(a.data_in, "metadata"))
                reuse_atlas(a.reuse_atlas, a.out)
                adopt_reused(a)
                skip = ("build",)
            if a.command == "run":
                todo, why = plan(a, a.start, a.stop, a.redo, skip)
                log("Plan: " + (" -> ".join(todo) + f"   ({why})" if todo else
                                "nothing to do; everything is up to date"))
            else:
                todo = [a.command]
            if "effects" in todo and "build" not in todo:
                check_metadata(a)
            t0 = time.time()
            for s in todo:
                if a.command == "run":
                    log(f"===== stage {s} =====")
                run_stage(s, a)
            if a.command == "run":
                xi = os.path.join(a.out, "explorer", "web", "index.html")
                log(f"Run done in {(time.time() - t0) / 60:.1f} min. Vault: {os.path.join(a.out, 'vault')}  "
                    f"map: {os.path.join(a.out, 'map', 'gene_map.html')}"
                    + (f"  explorer: {xi}" if os.path.exists(xi) else ""))
    except SystemExit as e:
        T.log_exit(e)
        raise
    finally:
        lock.release()


if __name__ == "__main__":
    main()
