"""export - the shareable results of a finished output folder, copied into a folder that is ready to be committed and
pushed to a GitHub branch.

    python -m tahoemap export DEST [--out OUT] [--with-effects] [--include FILE ...] [--force] [--max-file-mb 95]

What is copied from OUT to DEST (same relative paths):
    vault/        the Obsidian vault (every note, its .obsidian settings, the vault's own manifest)
    map/          gene_map.html, the self-contained interactive map
    tables/ validation/ direction/ graph/ relations/ embed/ stages/        every file
    reference/    the derived tables and the record of the sources: the files directly in reference/ (annotations,
                  gene sets, STRING pairs, sources.json); not reference/downloads/ (the raw downloaded sources)
    review/       the literature reviews, when there are any: reviews/, notes/, history/, ledger.jsonl, the queue and
                  the connection / finding tables, review.log; never cache/, dry_run/, keys_state.json,
                  ledger.unwritten.jsonl, .run.lock or .stop
    run_options.json, run.log
    --with-effects   also atlas/effects (the pooled gene x drug-dose matrices DD_*.npy and the atlas's CSV tables)
                     and atlas/reports
    --include FILE   these files (or folders) too, at the top of DEST under their own names (e.g. a RUN_REPORT.md)
Never: atlas/pseudobulk (the build), tensor/ (the per-line arrays), hf/ (streamed input), temporary files (*.tmp,
*.part), lock and job files. Links to folders are not followed.

GitHub refuses files over 100 MB, so a file over --max-file-mb (95 MiB) is not copied; the command's output and
DEST/README.md list every such file. DEST also gets:
    README.md        what each folder holds, the provenance (tahoemap version, code commit, date, stage stamps), the
                     sizes, what was left out and why, how to open the vault and the map
    MANIFEST.tsv     one line per copied file (and README.md, .gitattributes): path (relative, '/'), bytes, sha256
    .gitattributes   '* -text': git stores every file byte for byte (no line-ending conversion, e.g. on Windows)

Safety: DEST must lie outside OUT and must not contain it (compared as the file system does: case-insensitive on
Windows, links resolved). A DEST that is not empty needs --force, and --force replaces and removes only files that
DEST/MANIFEST.tsv of an earlier export lists: any other file in the way stops the export before anything is copied
(a .git folder and other files of the user's are left alone). The export refuses while a pipeline command or a
literature-review run works on OUT, since files would change while they are copied. Re-exporting with --force copies
only the files that changed (same size and modification time as the earlier copy: kept).
"""

import hashlib
import json
import os
import re
import shlex
import shutil
import sys
import time

from . import __version__
from . import links as LK
from .common import (STAGES, PIPELINE_LOCK, find_git, git_out, is_link, lock_state, log, printable, read_stamp,
                     remove_file, replace_file)

MAX_MB = 95.0                      # MiB: GitHub refuses files over 100 MB
WARN_MB = 50.0                     # MiB: GitHub accepts these but warns
PUSH_GB = 1.9                      # GB: GitHub refuses one push over 2 GB
FOLDERS = ("vault", "map", "tables", "validation", "direction", "graph", "relations", "embed", "stages")
TOP_FILES = ("run_options.json", "run.log")
EFFECTS = (("atlas", "effects"), ("atlas", "reports"))
WRITTEN = ("README.md", "MANIFEST.tsv", ".gitattributes")     # written by the export itself, at the top of DEST
MANIFEST = "MANIFEST.tsv"
MANIFEST_HEADER = "path\tbytes\tsha256"
GITATTRIBUTES = ("# written by tahoemap export: git stores every file byte for byte (no line-ending conversion)\n"
                 "* -text\n")
SKIP_NAMES = {".pipeline.lock", ".job.pid", ".run.lock", ".stop", "keys_state.json", "ledger.unwritten.jsonl",
              "desktop.ini", "Thumbs.db", ".DS_Store"}
SKIP_SUFFIX = (".tmp", ".part")
REVIEW_SKIP_DIRS = {"cache": "the literature cache (PubMed / Europe PMC answers, re-fetched when needed)",
                    "dry_run": "dry-run files (what a run would send; no results)"}
REVIEW_SKIP_FILES = {"keys_state.json": "which API keys a review run used up (key ids; not a result)",
                     "ledger.unwritten.jsonl": "ledger lines a run could not write yet (the next review run moves "
                                               "them into ledger.jsonl)",
                     ".run.lock": "the lock of a running review", ".stop": "a stop request to a review run"}
LEFT_OUT = {
    "atlas/pseudobulk": "the build: per-well pseudobulk counts (tens of GB at full scale); the build stage makes it "
                        "again from Tahoe-100M",
    "atlas/effects": "the pooled drug-dose x gene matrices (DD_*.npy, about 75 MB each at full scale) and the per-well "
                     "values (W1, W2, Z: about 89 MB each): only with --with-effects. Every value is also in the "
                     "explorer (export DEST --explorer)",
    "atlas/reports": "the atlas's reports: only with --with-effects",
    "atlas": "the atlas's index and build records (stages/build.json and stages/effects.json record the build)",
    "tensor": "the per-cell-line arrays (several GB at full scale): published per gene in the explorer's data "
              "repository (export DEST --explorer); the tensor stage computes them again from atlas/effects",
    "explorer": "the explorer (searchable pages with every value, exact): published separately, to GitHub Pages and "
                "a data repository, with export DEST --explorer",
    "explorer.tmp": "an explorer build in progress, or one the size guard stopped (not published)",
    "explorer.old": "an explorer being replaced (not published)",
    "hf": "streamed input files (Tahoe-100M itself, from Hugging Face)",
    "reference/downloads": "the raw downloaded sources (public files; reference/sources.json says where each came "
                           "from and when)",
    "pipeline_console.log": "the console of the background job (run.log holds the pipeline's log)",
    "duplicated_from.json": "where this output folder was copied from (paths on this computer)",
    ".not_tahoe_input": "a marker that keeps the old scripts from reading the output as input data",
    ".pipeline.lock": "the lock of a running pipeline command", ".job.pid": "the background job's process id",
}
DESCRIBE = {
    "vault": "the Obsidian vault: a note per gene, drug, cell line, module, plate and concept, and indexes (start at "
             "vault/Home.md)",
    "map": "gene_map.html: the interactive gene map, one self-contained HTML file (works offline)",
    "tables": "the fold-change tables: which drug-doses raise / lower each gene, pooled and line by line, with "
              "flags (parquet; tables/README.md documents every column)",
    "validation": "does the vector space recover known biology, and what in it is new (start at "
                  "validation/report.md; README.md there documents the columns)",
    "direction": "probable direction between genes, from the cell lines (which gene acts on which, or on the "
                 "cells' growth under a drug): edges with p, q, an evidence grade A / B / C and their alerts, the "
                 "groups compared and the controls (direction/README.md documents every column; a probable "
                 "direction, not proof of direct regulation)",
    "graph": "the nodal map: nodes (map coordinates, module, arm), edges and modules (parquet)",
    "relations": "gene x gene: each gene's 100 strongest partners, how reproducible, known or new (parquet)",
    "embed": "the vector space: gene, drug-dose, drug and cell-line vectors (numpy .npy) and their tables",
    "reference": "public annotation reduced to Tahoe's genes (annotations, gene sets, STRING pairs; parquet) and "
                 "sources.json (where each source came from)",
    "stages": "one stamp per finished stage: its method version, when it finished, its counts and options",
    "review": "the literature reviews by AI agents: reviews/, notes/, the histories, ledger.jsonl, the connection and "
              "finding tables",
    "atlas/effects": "the pooled drug-dose x gene matrices (DD_*.npy) and the atlas's CSV tables (drugdose.csv, "
                     "genes.csv, lines.csv, ...)",
    "atlas/reports": "the atlas's reports",
    "run_options.json": "the options that change results, as given to the runs on this output",
    "run.log": "the log of every pipeline command run on this output",
}


# ----------------------------------------------------------------------------- paths
def _lp(p, always=False):
    """p as Windows accepts it beyond 260 characters (the extended-length prefix \\\\?\\; always: whatever its
    length, for a folder to walk); unchanged elsewhere."""
    if os.name != "nt" or (len(p) < 240 and not always) or p.startswith("\\\\?\\"):
        return p
    p = os.path.abspath(p)
    return "\\\\?\\UNC\\" + p[2:] if p.startswith("\\\\") else "\\\\?\\" + p


def _key(rel):
    """A relative path as the file system compares names (case-insensitive on Windows)."""
    return os.path.normcase(rel.replace("/", os.sep))


def _mb(n):
    return f"{n / 2 ** 20:,.1f} MiB" if n < 2 ** 30 else f"{n / 2 ** 30:,.2f} GiB"


# ----------------------------------------------------------------------------- what to copy
def plan(out, with_effects=False, include=(), max_bytes=None):
    """What an export of `out` copies. Returns {"files": [(source path, relative destination '/'-path, bytes)],
    "too_large": [(relative path, bytes)], "left_out": [(relative path, why)], "folders": [top folders/files]}."""
    max_bytes = int(MAX_MB * 2 ** 20) if max_bytes is None else int(max_bytes)
    files, too_large, left_out, seen = [], [], [], set()

    def add(src, rel):
        if "\t" in rel or "\n" in rel or "\r" in rel:
            left_out.append((rel, "its name holds a tab or a line break (MANIFEST.tsv cannot list it)"))
            return
        try:
            n = os.path.getsize(_lp(src))
        except OSError as e:
            left_out.append((rel, f"cannot be read ({type(e).__name__}: {e})"))
            return
        if n > max_bytes:
            too_large.append((rel, n))
            return
        if _key(rel) in seen:
            left_out.append((rel, "a file of the same name (as this system compares names) is already copied"))
            return
        seen.add(_key(rel))
        files.append((src, rel, n))

    def walk(top_rel, skip_dirs=None, skip_files=None):
        """Every file under OUT/top_rel, with the skips."""
        skip_dirs, skip_files = skip_dirs or {}, skip_files or {}
        base = _lp(os.path.join(out, *top_rel.split("/")), always=True)
        for root, dirs, fs in os.walk(base):
            rel_root = os.path.relpath(root, base)
            rr = top_rel if rel_root == "." else top_rel + "/" + rel_root.replace(os.sep, "/")
            for d in sorted(dirs):
                sp = os.path.join(root, d)
                if rel_root == "." and d in skip_dirs:
                    left_out.append((f"{rr}/{d}", skip_dirs[d]))
                    dirs.remove(d)
                elif is_link(sp):
                    left_out.append((f"{rr}/{d}", "a link to a folder (not followed)"))
                    dirs.remove(d)
                elif d == "__pycache__":
                    dirs.remove(d)
            dirs.sort()
            for f in sorted(fs):
                if rel_root == "." and f in skip_files:
                    left_out.append((f"{rr}/{f}", skip_files[f]))
                elif f in SKIP_NAMES or f.endswith(SKIP_SUFFIX):
                    continue                                   # temporary, lock and job files: not worth a note
                else:
                    add(os.path.join(root, f), f"{rr}/{f}")

    folders = []
    for d in FOLDERS:
        if os.path.isdir(os.path.join(out, d)):
            walk(d)
            folders.append(d)
    rd = os.path.join(out, "reference")
    if os.path.isdir(rd):
        folders.append("reference")
        for f in sorted(os.listdir(rd)):
            p = os.path.join(rd, f)
            if os.path.isfile(p) and not (f in SKIP_NAMES or f.endswith(SKIP_SUFFIX)):
                add(p, f"reference/{f}")
            elif os.path.isdir(p):
                left_out.append((f"reference/{f}", LEFT_OUT.get(f"reference/{f}", "not a derived table")))
    vd = os.path.join(out, "review")
    if os.path.isdir(vd):
        n0 = len(files)
        walk("review", REVIEW_SKIP_DIRS, REVIEW_SKIP_FILES)
        if len(files) > n0:
            folders.append("review")
    for f in TOP_FILES:
        if os.path.isfile(os.path.join(out, f)):
            add(os.path.join(out, f), f)
            folders.append(f)
    for parts in EFFECTS:
        rel = "/".join(parts)
        if os.path.isdir(os.path.join(out, *parts)):
            if with_effects:
                walk(rel)
                folders.append(rel)
            else:
                left_out.append((rel, LEFT_OUT[rel]))
    for inc in include or ():
        src = os.path.abspath(os.path.expanduser(inc))
        name = os.path.basename(src.rstrip("/\\"))
        if not os.path.exists(src):
            sys.exit(f"export --include: {inc} does not exist")
        if name in WRITTEN or name in FOLDERS or name in TOP_FILES or name in ("reference", "review", "atlas"):
            sys.exit(f"export --include: '{name}' is a name the export itself writes at the top of DEST; rename "
                     "the file first")
        if os.path.isdir(src):
            for root, dirs, fs in os.walk(_lp(src, always=True)):
                dirs[:] = sorted(d for d in dirs if not is_link(os.path.join(root, d)))
                rr = os.path.relpath(root, _lp(src, always=True))
                for f in sorted(fs):
                    rel = name + ("" if rr == "." else "/" + rr.replace(os.sep, "/")) + "/" + f
                    add(os.path.join(root, f), rel)
        else:
            add(src, name)
        folders.append(name)
    # what else OUT holds, and why it stays out
    known = set(FOLDERS) | set(TOP_FILES) | {"reference", "review", "atlas"}
    for f in sorted(os.listdir(out)):
        if f in known:
            continue
        rel = f
        why = LEFT_OUT.get(f) or ("a temporary file" if f.endswith(SKIP_SUFFIX) else
                                  "not part of the shareable results")
        left_out.append((rel, why))
    ad = os.path.join(out, "atlas")
    if os.path.isdir(ad):
        if os.path.lexists(os.path.join(ad, "pseudobulk")):
            left_out.append(("atlas/pseudobulk", LEFT_OUT["atlas/pseudobulk"]))
        rest = [f for f in os.listdir(ad) if f not in ("pseudobulk", "effects", "reports")]
        if rest:
            left_out.append(("atlas/" + ", atlas/".join(sorted(rest)[:6]) + (", ..." if len(rest) > 6 else ""),
                             LEFT_OUT["atlas"]))
    return {"files": files, "too_large": too_large, "left_out": left_out, "folders": folders}


# ----------------------------------------------------------------------------- the copy
def read_manifest(dest):
    """{key: (relative path, bytes, sha256)} of DEST/MANIFEST.tsv written by an earlier export ({} when there is
    none, or it is not one of ours)."""
    p = os.path.join(dest, MANIFEST)
    try:
        with open(_lp(p), encoding="utf-8") as fh:
            lines = fh.read().split("\n")
    except OSError:
        return {}
    if not lines or lines[0].rstrip("\r") != MANIFEST_HEADER:
        return {}
    rec = {}
    for ln in lines[1:]:
        parts = ln.rstrip("\r").split("\t")
        if len(parts) == 3 and parts[0]:
            try:
                rec[_key(parts[0])] = (parts[0], int(parts[1]), parts[2])
            except ValueError:
                continue
    rec[_key(MANIFEST)] = (MANIFEST, -1, "")
    return rec


def _copy(src, dst):
    """Copy src to dst through dst.tmp (then replaced); dst gets src's modification time. Returns the sha256."""
    h = hashlib.sha256()
    tmp = dst + ".tmp"
    with open(_lp(src), "rb") as fi, open(_lp(tmp), "wb") as fo:
        while True:
            b = fi.read(1 << 20)
            if not b:
                break
            h.update(b)
            fo.write(b)
    st = os.stat(_lp(src))
    os.utime(_lp(tmp), ns=(st.st_atime_ns, st.st_mtime_ns))
    replace_file(_lp(tmp), _lp(dst))
    return h.hexdigest()


def _sha256(path):
    h = hashlib.sha256()
    with open(_lp(path), "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _write_text(path, text):
    tmp = path + ".tmp"
    with open(_lp(tmp), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    replace_file(_lp(tmp), _lp(path))


def _free_bytes(path):
    p = os.path.abspath(path)
    while not os.path.exists(p):
        q = os.path.dirname(p)
        if q == p:
            return None
        p = q
    try:
        return shutil.disk_usage(p).free
    except OSError:
        return None


def _busy(out):
    """Why OUT cannot be exported now ('' when nothing works on it)."""
    for p, what in ((os.path.join(out, PIPELINE_LOCK), "a pipeline command"),
                    (os.path.join(out, "review", ".run.lock"), "a literature-review run")):
        if os.path.exists(p):
            alive, who = lock_state(p)
            if alive:
                return (f"{what} is working on {out} ({who}; lock file {p}): its files would change while they are "
                        "copied. Wait for it to finish, or stop it first.")
    return ""


def _provenance(out):
    code_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git = find_git()
    status = git_out(git, code_root, "status", "--porcelain")
    return {"version": __version__, "commit": git_out(git, code_root, "rev-parse", "HEAD"),
            "branch": git_out(git, code_root, "rev-parse", "--abbrev-ref", "HEAD"),
            "remote": git_out(git, code_root, "remote", "get-url", "origin"),
            "uncommitted_changes": None if status is None else bool(status), "git": git is not None}


def export(out, dest, with_effects=False, include=(), force=False, max_mb=MAX_MB, site_url=None, github=None):
    """Copy the shareable results of `out` into `dest` (module docstring). Returns the record of what it did.
    site_url / github: where the explorer is (or will be) published, for README.md (default: this code's GitHub
    repository, links.py)."""
    from .cli import _inside
    t0 = time.time()
    out, dest = os.path.abspath(os.path.expanduser(out)), os.path.abspath(os.path.expanduser(dest))
    if not os.path.isdir(os.path.join(out, "stages")):
        sys.exit(f"export: {out} is not a tahoemap output folder (no stages/); give --out with one")
    stamps = {s: read_stamp(out, s) for s in STAGES}
    if not any(stamps.values()):
        sys.exit(f"export: no stage of {out} has finished: nothing to export yet")
    if _inside(dest, out) or _inside(out, dest):
        sys.exit("export: the destination must lie outside the output folder (and not contain it)")
    if os.path.exists(dest) and not os.path.isdir(dest):
        sys.exit(f"export: {dest} exists and is not a folder")
    busy = _busy(out)
    if busy:
        sys.exit(f"export: {busy}")
    nonempty = os.path.isdir(dest) and bool(os.listdir(dest))
    if nonempty and not force:
        sys.exit(f"export: {dest} exists and is not empty. Give a new folder, or --force to update an earlier "
                 "export there (only the files its MANIFEST.tsv lists are replaced or removed)")
    owned = read_manifest(dest) if nonempty else {}
    max_bytes = int(float(max_mb) * 2 ** 20)
    pl = plan(out, with_effects, include, max_bytes)
    files = pl["files"]
    want = {_key(rel) for _, rel, _ in files} | {_key(w) for w in WRITTEN}

    # nothing in the way that an earlier export did not write (checked before anything is copied)
    if nonempty:
        clash = []
        for rel in sorted({rel for _, rel, _ in files} | set(WRITTEN)):
            parts = rel.split("/")
            for i in range(1, len(parts) + 1):
                sub = "/".join(parts[:i])
                p = os.path.join(dest, *parts[:i])
                if i < len(parts):
                    if os.path.lexists(_lp(p)) and not os.path.isdir(_lp(p)) and _key(sub) not in owned:
                        clash.append(sub)
                        break
                elif os.path.lexists(_lp(p)) and (os.path.isdir(_lp(p)) or _key(sub) not in owned):
                    clash.append(sub)
        if clash:
            sys.exit(f"export --force: {len(clash)} path(s) in {dest} are in the way and were not written by an "
                     f"earlier export (its MANIFEST.tsv does not list them): " + ", ".join(clash[:10])
                     + (", ..." if len(clash) > 10 else "") + ". Nothing was copied: move them, or use a new folder.")
    total = sum(n for _, _, n in files)
    # room for the files no earlier export copied, and for one replaced file at a time (its .tmp copy)
    need = sum(n for _, rel, n in files if _key(rel) not in owned) + max((n for _, _, n in files), default=0)
    free = _free_bytes(dest)
    if free is not None and free < need * 1.02 + 50 * 2 ** 20:
        sys.exit(f"export: {_mb(need)} to copy, but only {_mb(free)} free where {dest} is")

    log(f"Exporting {out} -> {dest}: {len(files):,} files, {_mb(total)}"
        + (f"; {len(pl['too_large'])} file(s) over {max_mb:g} MiB not copied" if pl["too_large"] else ""))
    os.makedirs(_lp(dest), exist_ok=True)
    rows, copied, kept = [], 0, 0
    for k, (src, rel, n) in enumerate(files):
        dst = os.path.join(dest, *rel.split("/"))
        old = owned.get(_key(rel))
        st, ds = os.stat(_lp(src)), None
        if old:
            try:
                ds = os.stat(_lp(dst))
            except OSError:
                pass
        if old and ds is not None and old[1] == n == ds.st_size and ds.st_mtime_ns == st.st_mtime_ns and old[2]:
            rows.append((rel, n, old[2]))                  # unchanged since the earlier export
            kept += 1
            continue
        os.makedirs(_lp(os.path.dirname(dst)), exist_ok=True)
        rows.append((rel, n, _copy(src, dst)))
        copied += 1
        if (k + 1) % 5000 == 0:
            log(f"  {k + 1:,} of {len(files):,} files ...")

    # files an earlier export wrote that this one does not: removed (then their folders, if empty)
    removed = []
    for key, (rel, _, _) in sorted(owned.items()):
        if key in want:
            continue
        p = os.path.join(dest, *rel.split("/"))
        if os.path.isfile(_lp(p)) or os.path.islink(_lp(p)):
            remove_file(_lp(p))
            removed.append(rel)
            d = os.path.dirname(p)
            while os.path.normcase(d) != os.path.normcase(dest) and os.path.isdir(_lp(d)) and not os.listdir(_lp(d)):
                os.rmdir(_lp(d))
                d = os.path.dirname(d)

    rec = {"source": out, "destination": dest, "date": time.strftime("%Y-%m-%d %H:%M:%S"), "code": _provenance(out),
           "stages": {s: v for s, v in stamps.items() if v}, "files": len(rows), "bytes": total,
           "copied": copied, "unchanged": kept, "removed": removed, "too_large": pl["too_large"],
           "left_out": pl["left_out"], "folders": pl["folders"], "with_effects": bool(with_effects),
           "include": [os.path.abspath(i) for i in include or ()], "max_mb": float(max_mb),
           "explorer": _explorer_where(out, site_url, github)}
    rec["sizes"] = _sizes(rows, pl["folders"])
    rec["stage_state"], rec["stale"] = _stage_states(stamps, pl["folders"])
    rec["large_warn"] = [(r, n) for r, n, _ in rows if n > WARN_MB * 2 ** 20]
    rec["long_paths"] = os.name == "nt" and any(len(os.path.join(dest, r)) >= 250 for r, _, _ in rows)
    _write_text(os.path.join(dest, ".gitattributes"), GITATTRIBUTES)
    _write_text(os.path.join(dest, "README.md"), readme(rec))
    for w in ("README.md", ".gitattributes"):
        p = os.path.join(dest, w)
        rows.append((w, os.path.getsize(_lp(p)), _sha256(p)))
    rows.sort(key=lambda r: r[0])
    _write_text(os.path.join(dest, MANIFEST), MANIFEST_HEADER + "\n" + "".join(f"{r}\t{n}\t{h}\n" for r, n, h in rows))
    rec["manifest_rows"] = len(rows)
    rec["seconds"] = round(time.time() - t0, 1)
    _report(rec)
    return rec


# the stage that writes each exported folder (a folder whose stage is not current may be out of date)
FOLDER_STAGE = {"tables": "tables", "embed": "embed", "reference": "reference", "relations": "relations",
                "graph": "graph", "direction": "direction", "validation": "validate", "vault": "vault", "map": "map",
                "atlas/effects": "effects"}


def _stage_states(stamps, folders):
    """({stage: '' when its stamp is current, else why not}, {exported folder: its alert when its stage is not
    current}). Current = finished, with this code's method version."""
    from .cli import stage_version
    state = {}
    for s in STAGES:
        st = stamps.get(s)
        if st is None:
            state[s] = "not finished (never run, or an earlier stage ran again since)"
            continue
        try:
            v = stage_version(s)
        except Exception:  # noqa: BLE001  (a stage module that cannot be imported: take the stamp as it is)
            v = st.get("version")
        state[s] = "" if st.get("version") == v else f"out of date (its method is now version {v})"
    stale = {}
    for f in folders:
        s = FOLDER_STAGE.get(f)
        if s and state.get(s):
            stale[f] = (f"the {s} stage is {state[s]}, so these files are from an earlier run and may not match the "
                        "others ('tahoe run' brings every stage up to date)")
    return state, stale


def _sizes(rows, folders):
    """[(top folder or file, files, bytes)] in the order of `folders`."""
    agg = {}
    for rel, n, _ in rows:
        top = next((f for f in sorted(folders, key=len, reverse=True) if rel == f or rel.startswith(f + "/")),
                   rel.split("/")[0])
        a = agg.setdefault(top, [0, 0])
        a[0] += 1
        a[1] += n
    return [(f, agg[f][0], agg[f][1]) for f in folders if f in agg]


# ----------------------------------------------------------------------------- README.md, the console
def readme(rec):
    c = rec["code"]
    L = ["# Tahoe-100M gene map: results", "",
         f"Exported by `tahoemap export` on {rec['date']} from the output folder `{rec['source']}`. Everything here "
         "was computed by tahoemap from the Tahoe-100M single-cell drug screen and public annotation sources "
         "(reference/sources.json names them); the code is the tahoemap repository named under Provenance.", "",
         "## What each folder holds", "",
         "| folder / file | files | size | what it is |", "|---|---|---|---|"]
    for f, n, b in rec["sizes"]:
        st = rec["stale"].get(f)
        L.append(f"| `{f}` | {n:,} | {_mb(b)} | {DESCRIBE.get(f, 'included with --include')}"
                 + (f" **⚠ {st}**" if st else "") + " |")
    L += ["", f"In all: {rec['files']:,} files, {_mb(rec['bytes'])}. `MANIFEST.tsv` lists every file with its size "
          "and sha256 (README.md and .gitattributes included; the manifest itself not); `.gitattributes` (`* -text`) "
          "makes git store every file byte for byte.", "",
          "## How to open them", "",
          "- **The vault**: get the files (clone the repository, or GitHub's *Code - Download ZIP*), then in "
          "[Obsidian](https://obsidian.md) choose *Open folder as vault* and pick the `vault` folder. Start at "
          "`Home.md`; `How to read this vault.md` explains the notes. On GitHub itself the notes read as plain "
          "Markdown, but the [[links]] between them do not work there.",
          "- **The map**: `map/gene_map.html` is one self-contained file. GitHub shows HTML as source code: download "
          "the file (*Download raw file*, or clone), then open it in any current browser (Chrome, Edge, Firefox, "
          "Safari); it needs no network.",
          "- **The tables**: parquet files, e.g. `pandas.read_parquet(\"tables/drug_effects.parquet\")` in Python or "
          "`arrow::read_parquet()` in R; each folder's README.md documents the columns.",
          "- **The validation**: `validation/report.md` reads well on GitHub."]
    L += _explorer_lines(rec.get("explorer") or {})
    L += ["",
          "Flags: nothing is left out of a table for a flag; an item with a reason for doubt keeps its ranked place "
          "and carries an alert (⚠ and the reason in plain words).", "",
          "## Provenance", "",
          f"- tahoemap version {c['version']}; code commit `{c['commit'] or 'unknown (git not found)'}`"
          + (f" on branch `{c['branch']}`" if c.get("branch") else "")
          + (f" of {c['remote']}" if c.get("remote") else "")
          + ("" if c.get("uncommitted_changes") is None else
             "; the code had uncommitted changes" if c["uncommitted_changes"] else "; no uncommitted changes"),
          f"- exported {rec['date']}" + (" with --with-effects" if rec["with_effects"] else ""), "",
          "Stage stamps (`stages/<stage>.json` holds each stage's counts and options):", "",
          "| stage | method version | finished | state |", "|---|---|---|---|"]
    for s in STAGES:
        st = rec["stages"].get(s)
        state = rec["stage_state"].get(s, "")
        L.append((f"| {s} | {st.get('version', '?')} | {st.get('finished', '?')} |" if st else f"| {s} | - | - |")
                 + (f" ⚠ {state} |" if state else " done |"))
    L += ["", "## What was left out, and why", ""]
    if rec["too_large"]:
        L += [f"**Too large for GitHub** (over {rec['max_mb']:g} MiB; GitHub refuses files over 100 MB): not copied. "
              "To share them, use Git LFS, or attach them to a GitHub release (up to 2 GB a file):", ""]
        L += [f"- `{r}` ({_mb(n)})" for r, n in rec["too_large"]] + [""]
    L += [f"- `{r}`: {why}" for r, why in rec["left_out"]]
    if not rec["left_out"]:
        L.append("- nothing")
    L += ["", "## Checking the files", "",
          "From this folder, every file against MANIFEST.tsv:", "", "```",
          "python -c \"import hashlib; rows = [l.rstrip('\\n').split('\\t') for l in open('MANIFEST.tsv', "
          "encoding='utf-8')][1:]; bad = [p for p, n, h in rows if hashlib.sha256(open(p, 'rb').read())"
          ".hexdigest() != h]; print(len(rows), 'files,', len(bad), 'differ:', bad[:10])\"", "```", ""]
    return "\n".join(L)


def next_steps(dest, total, long_paths=False):
    """The git commands that put DEST on a GitHub branch (as text lines)."""
    q = f'"{dest}"' if " " in dest else dest
    date = time.strftime("%Y-%m-%d")
    if os.path.isdir(os.path.join(dest, ".git")):
        steps = [f"cd {q}", "git add -A", f'git commit -m "tahoemap results {date}"', "git push"]
    else:
        steps = [f"cd {q}", "git init", "git checkout --orphan results"]
        if long_paths:
            steps.append("git config core.longpaths true")
        steps += ["git add -A", f'git commit -m "tahoemap results {date}"',
                  "git remote add origin URL      (URL: your GitHub repository, e.g. "
                  "https://github.com/USER/REPO.git)", "git push -u origin results"]
    out = ["Next steps (the branch 'results' then holds only these files):"] + ["  " + s for s in steps]
    if total > PUSH_GB * 1e9:
        out.append(f"  ({_mb(total)} in all: GitHub refuses one push over 2 GB, so commit and push in parts, e.g. "
                   "'git add vault' + commit + push, then the rest)")
    return out


def _report(rec):
    if rec["too_large"]:
        log(f"  NOT copied, over {rec['max_mb']:g} MiB (GitHub refuses files over 100 MB; listed in README.md):")
        for r, n in rec["too_large"]:
            log(f"    {r} ({_mb(n)})")
    warn = [r for r, _ in rec["large_warn"]]
    if warn:
        log(f"  {len(warn)} file(s) over {WARN_MB:g} MiB (GitHub accepts them, with a warning): "
            + ", ".join(warn[:5]) + (", ..." if len(warn) > 5 else ""))
    for f, why in rec["stale"].items():
        log(printable(f"  ⚠ {f}/: {why}"))             # '!' on a console that cannot show the sign (cp1252)
    if rec["removed"]:
        log(f"  {len(rec['removed']):,} file(s) of the earlier export that this one no longer has were removed")
    log(f"Export done in {rec['seconds']:.0f} s: {rec['files']:,} files, {_mb(rec['bytes'])} in {rec['destination']} "
        f"({rec['copied']:,} copied, {rec['unchanged']:,} unchanged since the earlier export)")
    for ln in next_steps(rec["destination"], rec["bytes"], rec["long_paths"]):
        print(ln, flush=True)


# ----------------------------------------------------------------------------- where the explorer is published
def _repo_of(github=None):
    """(owner, repo) from --github OWNER/REPO (or a GitHub URL), else this code's origin remote (links.py); None
    when there is neither."""
    if github:
        g = str(github).strip()
        got = LK.parse_remote(g) or (LK.parse_remote("https://github.com/" + g) if g.count("/") == 1 else None)
        if not got:
            sys.exit(f"export --github: '{github}' is not OWNER/REPO (letters, digits, '.', '-', '_')")
        return got
    return LK.github_repo()


def _explorer_where(out, site_url=None, github=None):
    """For the results README: the explorer's web address, its data repository, and whether this output has one."""
    r = _repo_of(github) if github else LK.github_repo()
    site = LK.site_url(site_url) if not github else (f"https://{r[0]}.github.io/{r[1]}/" if r else None)
    st = read_stamp(out, "explorer") or {}
    return {"site_url": site, "data_repo": f"https://github.com/{r[0]}/{r[1]}-data" if r else None,
            "built": bool(st), "run": (st.get("info") or {}).get("run")}


def _explorer_lines(x):
    """README.md lines about the explorer (results export)."""
    if not x:
        return []
    L = ["- **The explorer**: searchable web pages over every result of the run, with every value exact (every gene "
         "at every drug-dose, in every cell line, every well; nothing is capped or left out for a flag)."]
    if x.get("site_url"):
        L.append(f"  Web address: {x['site_url']}. Its data repository: {x.get('data_repo') or 'not known'}.")
    else:
        L.append("  No web address is known (the code's repository is not on GitHub, or --site-url none).")
    L.append("  It is published separately (`python -m tahoemap export DEST --explorer`, then DEST/publish.ps1 or "
             "publish.sh; DEST/PUBLISH.md has the one-time GitHub steps). On the computer that made the run, open "
             "`explorer/web/index.html` of the output folder." + ("" if x.get("built") else
                                                                    " This output has no explorer yet (the explorer "
                                                                    "stage has not run)."))
    return L


# ----------------------------------------------------------------------------- the explorer (export DEST --explorer)
SITE_MAX_MB = 950.0           # MiB: the most the pages may hold (explorer.PAGES_MAX_MB; GitHub Pages: sites to 1 GB)
BATCH_BYTES = 1.5e9           # bytes on disk per upload list: one commit and one push each (GitHub: 2 GB a push)
ASSET_MAX = 2 ** 31           # bytes: a GitHub release asset must be smaller than 2 GiB
RECORD = "EXPLORER_EXPORT.json"
FOLDER = {"web": "site", "data": "data", "data_dd": "data_dd"}       # OUT/explorer/<volume> -> DEST/<folder>
DATA_REPO = {"data": "-data", "data_dd": "-data-dd"}                 # data repositories: <repo><suffix>
FIRST = (".gitattributes", "README.md")    # first in the first upload list (git reads .gitattributes as it adds)
LAST = ("probe.js", "MANIFEST.tsv")        # in the last list: a data repository whose probe.js names the run is whole
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
HOSTS_RE = re.compile(r"^TAHOE_HOSTS\((.*)\);\s*$", re.S)
RELEASE_FILES = ("atlas/effects/*.npy", "tensor/DDL_lfc.npy", "tensor/DDL_z.npy")


def _vol_rows(root):
    """[(relative path, bytes, sha256)] of a volume's MANIFEST.tsv (the explorer stage writes it), MANIFEST.tsv
    itself last (sha256 None: it does not list itself)."""
    p = os.path.join(root, MANIFEST)
    try:
        with open(_lp(p), encoding="utf-8") as fh:
            lines = fh.read().split("\n")
    except OSError:
        sys.exit(f"export --explorer: {p} is missing: run the explorer stage again (python -m tahoemap explorer)")
    if not lines or lines[0].rstrip("\r") != MANIFEST_HEADER:
        sys.exit(f"export --explorer: {p} is not a manifest of the explorer stage")
    rows = []
    for ln in lines[1:]:
        parts = ln.rstrip("\r").split("\t")
        if len(parts) == 3 and parts[0]:
            rows.append((parts[0], int(parts[1]), parts[2]))
    rows.append((MANIFEST, os.path.getsize(_lp(p)), None))
    return rows


def _explorer_ready(out, line_dd):
    """The explorer of OUT, checked: it finished, it is current (the stages it was made from, its page files), its
    row counts and self-check passed. Returns (stamp info, {volume: its folder})."""
    from . import explorer as X
    st = read_stamp(out, "explorer")
    root = os.path.join(out, "explorer")
    if st is None or not os.path.isdir(os.path.join(root, "web")):
        sys.exit(f"export --explorer: {out} has no finished explorer: run it first (python -m tahoemap run, or "
                 "python -m tahoemap explorer)")
    info = st.get("info") or {}
    again = "python -m tahoemap run (or: python -m tahoemap explorer) brings it up to date"
    if st.get("version") != X.VERSION:
        sys.exit(f"export --explorer: the explorer was made by an older method (version {st.get('version')}, now "
                 f"{X.VERSION}): {again}")
    if info.get("run") != X.run_id(out):
        sys.exit("export --explorer: the stages the explorer was made from have changed since it ran (run id "
                 f"{info.get('run')}, now {X.run_id(out)}): {again}")
    if (info.get("assets_sha") or None) != X.assets_sha():
        sys.exit("export --explorer: the explorer's page files (tahoemap/explorer_app) changed since it ran: "
                 f"{again} (only the page files are copied again, in seconds)")
    if not info.get("complete_ok", False):
        sys.exit("export --explorer: the explorer's row counts did not match its sources (stages/explorer.json "
                 "'complete'): run it again; if that repeats, report it")
    sc = (info.get("checks") or {}).get("self_check") or {}
    if sc.get("n_problems"):
        sys.exit(f"export --explorer: the explorer's self-check found {sc['n_problems']} difference(s): run it again")
    vols = {"web": os.path.join(root, "web"), "data": os.path.join(root, "data")}
    if line_dd:
        if not os.path.isdir(os.path.join(root, "data_dd")):
            sys.exit("export --explorer --with-line-dd: this explorer has no data_dd volume: run the explorer stage "
                     "with --with-line-dd first (python -m tahoemap explorer --with-line-dd)")
        vols["data_dd"] = os.path.join(root, "data_dd")
    for v, p in vols.items():
        if not os.path.isdir(p):
            sys.exit(f"export --explorer: {p} is missing: run the explorer stage again")
    return info, vols


def _hosts_read(path):
    with open(_lp(path), encoding="utf-8") as fh:
        m = HOSTS_RE.match(fh.read())
    if not m:
        sys.exit(f"export --explorer: {path} is not the explorer's hosts file (TAHOE_HOSTS(...);)")
    return json.loads(m.group(1))


def _hosts_text(h):
    """The hosts file as the explorer stage writes it (tahoemap/explorer.py _hosts_text)."""
    return "TAHOE_HOSTS(" + json.dumps(h, sort_keys=True, separators=(",", ":")) + ");\n"


def _manifest_set(vol_dir, rel, path):
    """Rewrite the line of `rel` in vol_dir/MANIFEST.tsv with the bytes and sha256 of `path` (through a .tmp file:
    a hard-linked manifest of the output is never written into)."""
    p = os.path.join(vol_dir, MANIFEST)
    with open(_lp(p), encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    row = f"{rel}\t{os.path.getsize(_lp(path))}\t{_sha256(path)}"
    for k, ln in enumerate(lines):
        if ln.split("\t", 1)[0] == rel:
            lines[k] = row
            break
    else:
        sys.exit(f"export --explorer: {p} does not list {rel}")
    _write_text(p, "\n".join(lines))


def _raw(owner, name, ref):
    return f"https://raw.githubusercontent.com/{owner}/{name}/{ref}/"


def _place(src, dst, link):
    """dst = src, as a hard link (link) or a copy, through dst.tmp (then replaced). Returns the copy's sha256 (None
    for a link)."""
    tmp = dst + ".tmp"
    if os.path.lexists(_lp(tmp)):
        os.remove(_lp(tmp))
    if not link:
        return _copy(src, dst)
    os.link(_lp(src), _lp(tmp))
    replace_file(_lp(tmp), _lp(dst))
    if os.path.lexists(_lp(tmp)):           # POSIX: renaming a link onto another link of the same file does nothing
        os.remove(_lp(tmp))
    return None


def _same(a, b):
    try:
        return os.path.samefile(_lp(a), _lp(b))
    except OSError:
        return False


def _can_link(src, dest):
    """True when a hard link from src into dest works (the same disk, a file system with links)."""
    probe = os.path.join(dest, ".tahoemap_link_probe")
    try:
        if os.path.lexists(_lp(probe)):
            os.remove(_lp(probe))
        os.link(_lp(src), _lp(probe))
        os.remove(_lp(probe))
        return True
    except OSError:
        return False


def _batches(rows, limit):
    """Upload lists: the volume's files (FIRST first, LAST last) cut into lists of at most `limit` bytes each.
    Returns [[relative path, ...], ...] and [bytes of each list]."""
    first = [r for r in rows if r[0] in FIRST]
    last = sorted((r for r in rows if r[0] in LAST), key=lambda r: LAST.index(r[0]))
    mid = sorted(r for r in rows if r[0] not in FIRST and r[0] not in LAST)
    lists, sizes = [[]], [0]
    for rel, n, _h in sorted(first, key=lambda r: FIRST.index(r[0])) + mid + last:
        if n > limit:
            sys.exit(f"export --explorer: {rel} ({_mb(n)}) is larger than one upload list may be ({_mb(limit)})")
        if sizes[-1] + n > limit and lists[-1]:
            lists.append([])
            sizes.append(0)
        lists[-1].append(rel)
        sizes[-1] += n
    return lists, sizes


def _release_assets(out, dest, owner, repo, run):
    """RELEASE_ASSETS.txt: the exact arrays behind the explorer (atlas/effects/*.npy, tensor/DDL_*.npy) with bytes and
    sha256 (kept in batches/release_sha.json while a file's size and time are unchanged), and how to attach them to
    a GitHub release of the data repository. Returns the text."""
    import glob
    cache_p = os.path.join(dest, "batches", "release_sha.json")
    try:
        with open(_lp(cache_p), encoding="utf-8") as fh:
            cache = json.load(fh)
    except (OSError, ValueError):
        cache = {}
    rows, new = [], {}
    for pat in RELEASE_FILES:
        for p in sorted(glob.glob(os.path.join(out, *pat.split("/")))):
            st = os.stat(_lp(p))
            rel = os.path.relpath(p, out).replace(os.sep, "/")
            key = f"{rel}|{st.st_size}|{st.st_mtime_ns}"
            h = cache.get(key) or _sha256(p)
            new[key] = h
            rows.append((rel, p, st.st_size, h))
    _write_text(cache_p, json.dumps(new, indent=1, sort_keys=True) + "\n")
    data = f"{owner}/{repo}-data" if owner else "OWNER/REPO-data"
    tag = f"explorer-{run}"
    ok = [r for r in rows if r[2] < ASSET_MAX]
    big = [r for r in rows if r[2] >= ASSET_MAX]
    L = ["# Release assets (optional): the exact arrays behind the explorer",
         "#",
         f"# Written by `python -m tahoemap export ... --explorer` on {time.strftime('%Y-%m-%d %H:%M:%S')} (explorer "
         f"run {run}).",
         "# The explorer already holds every value of these arrays (per gene, per drug-dose). These are the same",
         "# numbers as whole numpy files, for anyone who wants the full matrices. Publishing them is optional.",
         "# A GitHub release file must be smaller than 2 GiB; each file below says whether it fits.",
         "",
         "path\tbytes\tsha256\tfits in one release file"]
    L += [f"{rel}\t{n}\t{h}\t{'yes' if n < ASSET_MAX else 'no (2 GiB or more)'}" for rel, _p, n, h in rows]
    L += ["", "# To attach them to a release of the data repository with the GitHub command line tool (gh):", ""]
    if ok:
        L.append(f"gh release create {tag} --repo {data} --title \"Explorer arrays, run {run}\" --notes "
                 "\"The exact numpy arrays behind the explorer (see RELEASE_ASSETS.txt).\" "
                 + " ".join(_qq(p) for _rel, p, _n, _h in ok))
    else:
        L.append("# (no file of these arrays was found in the output)")
    L += ["", "# Or on github.com: open the data repository, click Releases, then 'Draft a new release'.",
          f"# Choose the tag {tag}, then drag the files above into the box. Click 'Publish release'."]
    if big:
        L += ["", "# Too large for one release file (2 GiB or more): " + ", ".join(r[0] for r in big)]
    return "\n".join(L) + "\n"


def _qq(p):
    """A path quoted for both PowerShell and a POSIX shell (double quotes; no $ or ` expected in paths)."""
    return '"' + str(p).replace('"', '\\"') + '"'


def _ps(s):
    """A PowerShell single-quoted string."""
    return "'" + str(s).replace("'", "''") + "'"


def explorer_export(out, dest, force=False, line_dd=False, github=None, site_max_mb=SITE_MAX_MB, max_mb=MAX_MB,
                    batch_bytes=BATCH_BYTES, link=True):
    """Make DEST ready to publish the explorer of OUT (docs/explorer.md; PUBLISH.md, written here, says how):

        DEST/site/        the web volume (GitHub Pages, branch 'site' of OWNER/REPO): every file of
                          OUT/explorer/web, with its .nojekyll, README.md, MANIFEST.tsv and .gitattributes
        DEST/data/        the data volume (repository OWNER/REPO-data, branch main); DEST/data_dd/ with line_dd
        DEST/batches/     the upload lists: data_N.txt (at most batch_bytes each; one push each), site.txt
        DEST/publish.ps1, DEST/publish.sh   the upload (never run here: the export never pushes)
        DEST/PUBLISH.md   the one-time GitHub steps and the upload, in plain words
        DEST/RELEASE_ASSETS.txt   optional: the exact arrays as release files
        DEST/EXPLORER_EXPORT.json what this export did

    The data files are hard links to OUT's when DEST is on the same disk (no extra space), else copies (checked
    against the stage's sha256). The pages are always copies: the explorer stage rewrites its page files in place
    when only they changed (explorer.refresh_assets), which must not reach DEST behind the export's back. Checks
    before anything is written: the explorer is finished and current, the web volume is at most site_max_mb MiB,
    every file at most max_mb MiB, every upload list at most batch_bytes, and the free space. A DEST that is not
    empty needs force and an earlier explorer export there; force then replaces only what changed and removes what
    the explorer no longer has (files the earlier export did not write are left alone, and stop the export when they
    are in the way)."""
    from .cli import _inside
    t0 = time.time()
    out, dest = os.path.abspath(os.path.expanduser(out)), os.path.abspath(os.path.expanduser(dest))
    if not os.path.isdir(os.path.join(out, "stages")):
        sys.exit(f"export: {out} is not a tahoemap output folder (no stages/); give --out with one")
    if _inside(dest, out) or _inside(out, dest):
        sys.exit("export: the destination must lie outside the output folder (and not contain it)")
    if os.path.exists(dest) and not os.path.isdir(dest):
        sys.exit(f"export: {dest} exists and is not a folder")
    busy = _busy(out)
    if busy:
        sys.exit(f"export: {busy}")
    info, vols = _explorer_ready(out, line_dd)
    r = _repo_of(github)
    if not r:
        sys.exit("export --explorer: the GitHub repository is not known (this code's origin is not on GitHub): give "
                 "--github OWNER/REPO")
    owner, repo = r
    run = info.get("run")

    # the checks before anything is written
    rows = {v: _vol_rows(p) for v, p in vols.items()}
    web_bytes = sum(n for _r, n, _h in rows["web"])
    if web_bytes > site_max_mb * 2 ** 20:
        sys.exit(f"export --explorer: the pages (OUT/explorer/web) hold {_mb(web_bytes)}, above {site_max_mb:g} MiB "
                 "(GitHub Pages publishes sites up to 1 GB). Nothing was written. Build the explorer again with a "
                 "lower --pages-max-mb: it moves parts to the data repository (nothing is dropped)")
    big = [(f"{FOLDER[v]}/{rel}", n) for v in rows for rel, n, _h in rows[v] if n > max_mb * 2 ** 20]
    if big:
        sys.exit(f"export --explorer: {len(big)} file(s) over {max_mb:g} MiB (GitHub refuses files over 100 MB): "
                 + ", ".join(f"{p} ({_mb(n)})" for p, n in big[:5]) + ". Nothing was written.")
    plans = {v: _batches(rows[v], batch_bytes if v != "web" else max(batch_bytes, web_bytes + 1))
             for v in rows}
    over = [(v, k + 1, b) for v in plans for k, b in enumerate(plans[v][1]) if b > batch_bytes and v != "web"]
    if over:
        sys.exit(f"export --explorer: an upload list would hold more than {_mb(batch_bytes)}: {over[:3]}")
    nonempty = os.path.isdir(dest) and bool(os.listdir(dest))
    earlier = {}
    if nonempty:
        try:
            with open(_lp(os.path.join(dest, RECORD)), encoding="utf-8") as fh:
                earlier = json.load(fh)
        except (OSError, ValueError):
            earlier = {}
        if not earlier:
            sys.exit(f"export --explorer: {dest} is not empty and holds no earlier explorer export ({RECORD}). Give "
                     "a new folder.")
        if not force:
            sys.exit(f"export --explorer: {dest} holds an earlier explorer export. Give --force to update it (only "
                     "what changed is replaced), or a new folder.")
    owned = {v: (read_manifest(os.path.join(dest, FOLDER[v])) if nonempty else {}) for v in FOLDER}
    clash = []
    for v in rows:
        for rel, _n, _h in rows[v]:
            d = os.path.join(dest, FOLDER[v], *rel.split("/"))
            if os.path.lexists(_lp(d)) and _key(rel) not in owned[v] and not _same(d, os.path.join(vols[v], rel)):
                clash.append(f"{FOLDER[v]}/{rel}")
    if clash:
        sys.exit(f"export --explorer --force: {len(clash)} path(s) in {dest} are in the way and were not written by "
                 "the earlier export (its MANIFEST.tsv does not list them): " + ", ".join(clash[:10])
                 + ". Nothing was copied: move them, or use a new folder.")
    made = not os.path.isdir(dest)
    os.makedirs(_lp(dest), exist_ok=True)
    use_link = bool(link) and _can_link(os.path.join(vols["data"], rows["data"][0][0]), dest)
    todo = [(v, rel, n) for v in rows for rel, n, _h in rows[v]
            if not _same(os.path.join(dest, FOLDER[v], *rel.split("/")), os.path.join(vols[v], rel))]
    need = sum(n for v, _r, n in todo if v == "web" or not use_link) + 50 * 2 ** 20
    free = _free_bytes(dest)
    if free is not None and free < need * 1.02:
        if made:
            shutil.rmtree(_lp(dest), ignore_errors=True)
        sys.exit(f"export --explorer: {_mb(need)} to copy, but only {_mb(free)} free where {dest} is")

    log(f"Exporting the explorer of {out} (run {run}) -> {dest}: "
        + ", ".join(f"{FOLDER[v]}/ {len(rows[v]):,} files, {_mb(sum(n for _r, n, _h in rows[v]))}" for v in rows)
        + ("; the data as hard links (no extra disk space), the pages as copies" if use_link else " (copies)"))
    counts = {}
    for v in rows:
        droot = os.path.join(dest, FOLDER[v])
        link_v = use_link and v != "web"
        c = {"files": len(rows[v]), "bytes": sum(n for _r, n, _h in rows[v]), "linked": 0, "copied": 0, "kept": 0,
             "removed": 0}
        for k, (rel, n, h) in enumerate(rows[v]):
            s_, d = os.path.join(vols[v], *rel.split("/")), os.path.join(droot, *rel.split("/"))
            o = owned[v].get(_key(rel))
            link_f = link_v and rel != MANIFEST          # the manifest is DEST's own record (--force, the pin)
            if os.path.lexists(_lp(d)):
                if (link_f and _same(s_, d)) or (h and o and o[2] == h and os.path.getsize(_lp(d)) == n
                                                 and not (not link_f and _same(s_, d))):
                    c["kept"] += 1
                    continue
            os.makedirs(_lp(os.path.dirname(d)), exist_ok=True)
            got = _place(s_, d, link_f)
            if got is not None and h and got != h:
                sys.exit(f"export --explorer: {s_} does not match its MANIFEST.tsv line (sha256): it changed since the "
                         "explorer stage wrote it. Run the explorer stage again.")
            c["linked" if link_f else "copied"] += 1
            if (k + 1) % 5000 == 0:
                log(f"  {FOLDER[v]}/: {k + 1:,} of {len(rows[v]):,} files ...")
        want = {_key(rel) for rel, _n, _h in rows[v]}
        for key, (rel, _n, _h) in sorted(owned[v].items()):
            if key in want:
                continue
            p = os.path.join(droot, *rel.split("/"))
            if os.path.isfile(_lp(p)) or os.path.islink(_lp(p)):
                remove_file(_lp(p))
                c["removed"] += 1
                dd_ = os.path.dirname(p)
                while os.path.normcase(dd_) != os.path.normcase(droot) and os.path.isdir(_lp(dd_)) \
                        and not os.listdir(_lp(dd_)):
                    os.rmdir(_lp(dd_))
                    dd_ = os.path.dirname(dd_)
        counts[FOLDER[v]] = c
    for v in FOLDER:                                 # a volume the earlier export had and this one has not
        if v not in rows and owned[v]:
            droot = os.path.join(dest, FOLDER[v])
            n_rm = 0
            for key, (rel, _n, _h) in sorted(owned[v].items()):
                p = os.path.join(droot, *rel.split("/"))
                if os.path.isfile(_lp(p)):
                    remove_file(_lp(p))
                    n_rm += 1
            counts[FOLDER[v]] = {"files": 0, "removed": n_rm}

    # the hosts file: the data repositories this export publishes to (branch URLs; publish pins the commit)
    site = os.path.join(dest, "site")
    hp = os.path.join(site, "d", "hosts.js")
    h = _hosts_read(hp)
    want_h = dict(h, data=[_raw(owner, repo + DATA_REPO["data"], "main")],
                  data_dd=[_raw(owner, repo + DATA_REPO["data_dd"], "main")] if "data_dd" in rows else [])
    hosts_note = ""
    if want_h != h:
        hosts_note = (f"d/hosts.js rewritten for the repositories of {owner}/{repo} (the stage wrote "
                      f"{', '.join(h.get('data') or []) or 'no data address'})")
        _write_text(hp, _hosts_text(want_h))
        _manifest_set(site, "d/hosts.js", hp)

    # upload lists
    bdir = os.path.join(dest, "batches")
    os.makedirs(_lp(bdir), exist_ok=True)
    for f in os.listdir(_lp(bdir)):
        if f.endswith(".txt"):
            remove_file(_lp(os.path.join(bdir, f)))
    parts = {}
    for v in rows:
        lists, sizes = plans[v]
        if v == "web":
            _write_text(os.path.join(bdir, "site.txt"), "".join(x + "\n" for x in lists[0]))
            continue
        for k, lst in enumerate(lists):
            _write_text(os.path.join(bdir, f"{v}_{k + 1}.txt"), "".join(x + "\n" for x in lst))
        parts[v] = {"lists": len(lists), "bytes": sizes}

    site_url = f"https://{owner}.github.io/{repo}/"
    rec = {"generated_by": "tahoemap export --explorer", "version": __version__, "run": run,
           "date": time.strftime("%Y-%m-%d %H:%M:%S"), "source": out, "destination": dest, "owner": owner,
           "repo": repo, "site_url": site_url, "site_repo": f"https://github.com/{owner}/{repo}",
           "data_repos": {v: f"https://github.com/{owner}/{repo}{DATA_REPO[v]}" for v in rows if v != "web"},
           "built_for": {"site_url": info.get("site_url"), "data_url": info.get("data_url")},
           "volumes": counts, "parts": parts, "hard_links": use_link, "hosts": hosts_note, "pinned": {},
           "code": _provenance(out), "python": sys.executable, "repo_dir": os.path.dirname(os.path.dirname(
               os.path.abspath(__file__))), "git": find_git(), "batch_bytes": batch_bytes,
           "long_paths": os.name == "nt" and len(dest) + 1 + max(len(r_) for v in rows for r_, _n, _h in rows[v])
           >= 250}
    if info.get("site_url") and LK.norm_url(info["site_url"]) != site_url:
        rec["note_site"] = (f"the explorer was built for {info['site_url']}; this export publishes it at {site_url}. "
                            f"Its own links still name the first: run the explorer stage with --site-url {site_url} "
                            "to change them.")
    _write_text(os.path.join(dest, "publish.ps1"), publish_ps1(rec))
    _write_text(os.path.join(dest, "publish.sh"), publish_sh(rec))
    try:
        os.chmod(_lp(os.path.join(dest, "publish.sh")), 0o755)
    except OSError:
        pass
    _write_text(os.path.join(dest, "PUBLISH.md"), publish_md(rec))
    _write_text(os.path.join(dest, "RELEASE_ASSETS.txt"), _release_assets(out, dest, owner, repo, run))
    rec["seconds"] = round(time.time() - t0, 1)
    _write_text(os.path.join(dest, RECORD), json.dumps(rec, indent=1, sort_keys=True) + "\n")
    _explorer_report(rec)
    return rec


def pin(dest, sha, volume="data"):
    """Point the exported pages (DEST/site) at one commit of a data repository: d/hosts.js 'data' (or 'data_dd')
    becomes [the commit's raw URL, the branch's raw URL], and its line in site/MANIFEST.tsv is updated (both through
    .tmp files, so the output's own copies are never written into). publish.ps1 / publish.sh call it after the data
    upload. Returns the new address list."""
    dest = os.path.abspath(os.path.expanduser(dest))
    sha = str(sha or "").strip().lower()
    if not SHA_RE.match(sha):
        sys.exit(f"export --pin-data: '{sha}' is not a git commit id (7 to 40 hexadecimal characters)")
    try:
        with open(_lp(os.path.join(dest, RECORD)), encoding="utf-8") as fh:
            rec = json.load(fh)
    except (OSError, ValueError):
        sys.exit(f"export --pin-data: {dest} holds no explorer export ({RECORD}); run export DEST --explorer first")
    if volume not in rec.get("data_repos", {}):
        sys.exit(f"export --pin-{volume.replace('_', '-')}: this export has no {volume} volume")
    site = os.path.join(dest, "site")
    hp = os.path.join(site, "d", "hosts.js")
    h = _hosts_read(hp)
    name = rec["repo"] + DATA_REPO[volume]
    h[volume] = [_raw(rec["owner"], name, sha), _raw(rec["owner"], name, "main")]
    _write_text(hp, _hosts_text(h))
    _manifest_set(site, "d/hosts.js", hp)
    rec.setdefault("pinned", {})[volume] = sha
    _write_text(os.path.join(dest, RECORD), json.dumps(rec, indent=1, sort_keys=True) + "\n")
    log(f"Pinned the pages in {site} to {rec['owner']}/{name} commit {sha} (d/hosts.js and its MANIFEST.tsv line)")
    return h[volume]


# ----------------------------------------------------------------------------- the upload scripts and PUBLISH.md
def _script_facts(rec):
    o, r = rec["owner"], rec["repo"]
    vols = [v for v in ("data", "data_dd") if v in rec["data_repos"]]
    return o, r, vols


def publish_ps1(rec):
    """publish.ps1: data first (one commit and push per upload list; the first push replaces the branch), then the
    pin, then the pages. Its push refspecs are fixed: HEAD:refs/heads/main to the data repositories, and
    HEAD:refs/heads/site to the code repository; nothing else is ever pushed."""
    o, r, vols = _script_facts(rec)
    git = rec.get("git") or "git"
    L = ["# publish.ps1 - publishes the Tahoe-100M explorer (explorer run " + rec["run"] + ") to GitHub.",
         f"# Written by `python -m tahoemap export ... --explorer` on {rec['date']}. Read PUBLISH.md first: two",
         "# settings on github.com are needed once.",
         "#",
         "#   powershell -ExecutionPolicy Bypass -File publish.ps1",
         "#",
         "# In this order, and only to these branches (it never pushes anything else):"]
    for v in vols:
        n = rec["parts"][v]["lists"]
        L.append(f"#   {v}/  -> https://github.com/{o}/{r}{DATA_REPO[v]}.git, branch main, in {n} part(s)")
        L.append("#           (one commit and one push each; the first push replaces the branch, so the repository")
        L.append("#           keeps one snapshot: the newest)")
    L += ["#   then the pages are pinned to that data commit (python -m tahoemap export ... --pin-data <commit>)",
          f"#   site/  -> https://github.com/{o}/{r}.git, branch site (replaced: one snapshot).",
          "#           GitHub Pages then publishes it within about 10 minutes.",
          "# If an upload stops (network, sign-in), run the script again with -FromPart K, K the data part that",
          "# failed (-FromPart " + str(rec["parts"]["data"]["lists"] + 1) + " skips the data, for the pages only)."
          + (" -FromDdPart K does the same for data_dd." if "data_dd" in vols else ""),
          "param([int]$FromPart = 1, [int]$FromDdPart = 1)",
          '$ErrorActionPreference = "Stop"',
          "$Dest = $PSScriptRoot",
          f"$Repo = {_ps(rec['repo_dir'])}",
          f"$Python = if ($env:TAHOE_PYTHON) {{ $env:TAHOE_PYTHON }} else {{ {_ps(rec['python'])} }}",
          "$Git = if ($env:TAHOE_GIT) { $env:TAHOE_GIT }",
          "       elseif (Get-Command git -ErrorAction SilentlyContinue) { 'git' }",
          f"       else {{ {_ps(git)} }}",
          f"$SiteRemote = {_ps(f'https://github.com/{o}/{r}.git')}",
          f"$Run = {_ps(rec['run'])}",
          "",
          "function Git-Do {         # git, its output to the console (never into a function's return value)",
          "  & $Git @args | Out-Host",
          "  if ($LASTEXITCODE -ne 0) { throw \"git $($args -join ' ') failed (exit code $LASTEXITCODE)\" }",
          "}",
          "function New-Repo([string]$Remote, [string]$Branch) {",
          "  if (Test-Path .git) { Remove-Item -Recurse -Force .git }",
          "  Git-Do init -q",
          "  Git-Do config core.longpaths true",
          "  Git-Do config core.autocrlf false",
          "  Git-Do remote add origin $Remote",
          "  Git-Do checkout -q --orphan $Branch",
          "}",
          "function Push-Data([string]$Volume, [string]$Remote, [int]$Parts, [int]$From) {",
          "  Set-Location (Join-Path $Dest $Volume)",
          "  & $Git ls-remote $Remote | Out-Null",
          "  if ($LASTEXITCODE -ne 0) {",
          "    throw \"cannot reach $Remote : create it on github.com first (PUBLISH.md, step 1), and check the \" +",
          "      \"network and the GitHub sign-in\"",
          "  }",
          "  if ($From -le 1) { New-Repo $Remote 'publish' }",
          "  elseif (-not (Test-Path .git)) {",
          "    throw \"no earlier upload in $Volume to continue: run without -FromPart\"",
          "  }",
          "  for ($k = [Math]::Max(1, $From); $k -le $Parts; $k++) {",
          "    Write-Host \"$Volume part $k of $Parts ...\"",
          "    Git-Do --literal-pathspecs add \"--pathspec-from-file=../batches/$($Volume)_$k.txt\"",
          "    & $Git diff --cached --quiet",
          "    if ($LASTEXITCODE -eq 1) { Git-Do commit -q -m \"explorer $Volume $Run part $k/$Parts\" }",
          "    elseif ($LASTEXITCODE -ne 0) { throw \"git diff failed (exit code $LASTEXITCODE)\" }",
          "    if ($k -eq 1) { Git-Do push --force origin 'HEAD:refs/heads/main' }",
          "    else { Git-Do push origin 'HEAD:refs/heads/main' }",
          "    Write-Host \"$Volume part $k of $Parts uploaded\"",
          "  }",
          "  $sha = (& $Git rev-parse HEAD)",
          "  if ($LASTEXITCODE -ne 0) { throw \"no data commit in $Volume\" }",
          "  Set-Location $Dest",
          "  return $sha.Trim()",
          "}",
          "",
          "Set-Location $Dest",
          "$who = (& $Git config user.email)",
          "if (-not $who) {",
          "  throw (\"git needs your name and e-mail for the commits, once: & '$Git' config --global user.name \" +",
          "    \"'Your Name'; & '$Git' config --global user.email 'you@example.com'\")",
          "}",
          "$head = (& $Git ls-remote --symref $SiteRemote HEAD) -join \"`n\"",
          "if ($LASTEXITCODE -ne 0) { throw \"cannot reach $SiteRemote (network, or the GitHub sign-in)\" }",
          "if ($head -match 'ref: refs/heads/site\\s') {",
          "  throw (\"'site' is the default branch of $SiteRemote : this script replaces the branch site, so it \" +",
          "    \"stops. Choose another default branch on github.com first.\")",
          "}"]
    for v in vols:
        n = rec["parts"][v]["lists"]
        frm = "$FromPart" if v == "data" else "$FromDdPart"
        var = "$DataSha" if v == "data" else "$DdSha"
        L.append(f"{var} = Push-Data {_ps(v)} {_ps(f'https://github.com/{o}/{r}{DATA_REPO[v]}.git')} {n} {frm}")
    L += ["Push-Location $Repo",
          "try {",
          "  & $Python -m tahoemap export $Dest --explorer --pin-data $DataSha"
          + (" --pin-data-dd $DdSha" if "data_dd" in vols else ""),
          "  if ($LASTEXITCODE -ne 0) { throw \"pinning the pages to the data commit failed\" }",
          "} finally { Pop-Location }",
          "Set-Location (Join-Path $Dest 'site')",
          "New-Repo $SiteRemote 'site'",
          "Git-Do --literal-pathspecs add '--pathspec-from-file=../batches/site.txt'",
          "Git-Do commit -q -m \"explorer site $Run (data $DataSha)\"",
          "Git-Do push --force origin 'HEAD:refs/heads/site'",
          "Set-Location $Dest",
          f"Write-Host \"Done. The pages are on the branch site of {o}/{r}.\"",
          f"Write-Host \"GitHub Pages publishes them at {rec['site_url']} within about 10 minutes\"",
          "Write-Host \"(the Actions tab of the repository shows pages-build-deployment).\"",
          ""]
    return "\n".join(L)


def publish_sh(rec):
    """publish.sh: publish.ps1's steps for bash (Linux, macOS, Git Bash), with the same fixed refspecs."""
    o, r, vols = _script_facts(rec)
    git = rec.get("git") or "git"
    L = ["#!/usr/bin/env bash",
         "# publish.sh - publishes the Tahoe-100M explorer (explorer run " + rec["run"] + ") to GitHub.",
         f"# Written by `python -m tahoemap export ... --explorer` on {rec['date']}. Read PUBLISH.md first: two",
         "# settings on github.com are needed once.",
         "#",
         "#   bash publish.sh [--from-part K] [--from-dd-part K]",
         "#",
         "# The same steps as publish.ps1, and only to these branches (it never pushes anything else):"]
    for v in vols:
        L.append(f"#   {v}/  -> https://github.com/{o}/{r}{DATA_REPO[v]}.git, branch main (one snapshot, in parts)")
    L += [f"#   site/  -> https://github.com/{o}/{r}.git, branch site (one snapshot),",
          "#           pinned to the data commit",
          "set -euo pipefail",
          "FROM_PART=1",
          "FROM_DD_PART=1",
          "while [ $# -gt 0 ]; do",
          "  case \"$1\" in",
          "    --from-part) FROM_PART=\"$2\"; shift 2 ;;",
          "    --from-dd-part) FROM_DD_PART=\"$2\"; shift 2 ;;",
          "    *) echo \"publish.sh: unknown option $1 (--from-part K, --from-dd-part K)\" >&2; exit 2 ;;",
          "  esac",
          "done",
          "DEST=\"$(cd \"$(dirname \"${BASH_SOURCE[0]}\")\" && pwd)\"",
          f"REPO={shlex.quote(rec['repo_dir'])}",
          f"PYTHON=\"${{TAHOE_PYTHON:-{rec['python']}}}\"" if "\"" not in rec["python"] and "$" not in rec["python"]
          else f"PYTHON={shlex.quote(rec['python'])}",
          f"GIT=\"${{TAHOE_GIT:-$(command -v git || echo {shlex.quote(git)})}}\"",
          f"SITE_REMOTE={shlex.quote(f'https://github.com/{o}/{r}.git')}",
          f"RUN={shlex.quote(rec['run'])}",
          "",
          "new_repo() {             # remote, local branch",
          "  rm -rf .git",
          "  \"$GIT\" init -q",
          "  \"$GIT\" config core.longpaths true",
          "  \"$GIT\" config core.autocrlf false",
          "  \"$GIT\" remote add origin \"$1\"",
          "  \"$GIT\" checkout -q --orphan \"$2\"",
          "}",
          "push_data() {            # volume, remote, parts, first part; sets LAST_SHA to the data commit",
          "  local vol=\"$1\" remote=\"$2\" parts=\"$3\" from=\"$4\" k",
          "  cd \"$DEST/$vol\"",
          "  if ! \"$GIT\" ls-remote \"$remote\" >/dev/null; then",
          "    echo \"cannot reach $remote: create it on github.com first (PUBLISH.md, step 1)\" >&2",
          "    exit 1",
          "  fi",
          "  if [ \"$from\" -le 1 ]; then",
          "    new_repo \"$remote\" publish",
          "  elif [ ! -d .git ]; then",
          "    echo \"no earlier upload in $vol to continue: run without --from-part\" >&2",
          "    exit 1",
          "  fi",
          "  for ((k = from < 1 ? 1 : from; k <= parts; k++)); do",
          "    echo \"$vol part $k of $parts ...\"",
          "    \"$GIT\" --literal-pathspecs add --pathspec-from-file=\"../batches/${vol}_$k.txt\"",
          "    if ! \"$GIT\" diff --cached --quiet; then",
          "      \"$GIT\" commit -q -m \"explorer $vol $RUN part $k/$parts\"",
          "    fi",
          "    if [ \"$k\" -eq 1 ]; then",
          "      \"$GIT\" push -q --force origin HEAD:refs/heads/main",
          "    else",
          "      \"$GIT\" push -q origin HEAD:refs/heads/main",
          "    fi",
          "    echo \"$vol part $k of $parts uploaded\"",
          "  done",
          "  LAST_SHA=\"$(\"$GIT\" rev-parse HEAD)\"",
          "  cd \"$DEST\"",
          "}",
          "",
          "cd \"$DEST\"",
          "if [ -z \"$(\"$GIT\" config user.email || true)\" ]; then",
          "  echo \"git needs your name and e-mail once: git config --global user.name 'Your Name';\" \\",
          "    \"git config --global user.email you@example.com\" >&2",
          "  exit 1",
          "fi",
          "if ! HEAD_REF=\"$(\"$GIT\" ls-remote --symref \"$SITE_REMOTE\" HEAD)\"; then",
          "  echo \"cannot reach $SITE_REMOTE (network, or the GitHub sign-in)\" >&2",
          "  exit 1",
          "fi",
          "case \"$HEAD_REF\" in",
          "  *\"ref: refs/heads/site\"[[:space:]]*)",
          "    echo \"'site' is the default branch of $SITE_REMOTE: this script replaces the branch site, so it\" \\",
          "      \"stops. Choose another default branch on github.com first.\" >&2",
          "    exit 1 ;;",
          "esac"]
    for v in vols:
        n = rec["parts"][v]["lists"]
        frm = "$FROM_PART" if v == "data" else "$FROM_DD_PART"
        var = "DATA_SHA" if v == "data" else "DD_SHA"
        L.append(f"push_data {v} {shlex.quote(f'https://github.com/{o}/{r}{DATA_REPO[v]}.git')} {n} \"{frm}\"")
        L.append(f"{var}=\"$LAST_SHA\"")
    L += ["(cd \"$REPO\" && \"$PYTHON\" -m tahoemap export \"$DEST\" --explorer --pin-data \"$DATA_SHA\""
          + (" --pin-data-dd \"$DD_SHA\"" if "data_dd" in vols else "") + ")",
          "cd \"$DEST/site\"",
          "new_repo \"$SITE_REMOTE\" site",
          "\"$GIT\" --literal-pathspecs add --pathspec-from-file=../batches/site.txt",
          "\"$GIT\" commit -q -m \"explorer site $RUN (data $DATA_SHA)\"",
          "\"$GIT\" push -q --force origin HEAD:refs/heads/site",
          "cd \"$DEST\"",
          f"echo \"Done. The pages are on the branch site of {o}/{r}.\"",
          f"echo \"GitHub Pages publishes them at {rec['site_url']} within about 10 minutes.\"",
          ""]
    return "\n".join(L)


def publish_md(rec):
    """PUBLISH.md: what DEST holds, the one-time GitHub steps (design section 10) and the upload, in plain words."""
    o, r, vols = _script_facts(rec)
    dest = rec["destination"]
    win = "\\" in dest or (len(dest) > 1 and dest[1] == ":")
    sep = "\\" if win else "/"
    py = rec["python"]
    vb = rec["volumes"]
    L = ["# Publishing the explorer", "",
         f"This folder holds the explorer of run `{rec['run']}`, ready to publish on GitHub. It was written by "
         f"`python -m tahoemap export ... --explorer` on {rec['date']}, from `{rec['source']}`. Nothing has been "
         "uploaded yet: the export never pushes. The script `publish.ps1` (Windows) or `publish.sh` (Linux, macOS) "
         "does the upload when you run it.", "",
         "The explorer is a set of web pages over every result of the run. Every gene, drug, drug-dose and cell line "
         "has a page, and every value is exact. Nothing is capped, and nothing is left out because of a flag.", "",
         "## What is here", "",
         "| Folder or file | What it is | Files | Size |", "|---|---|---|---|",
         f"| `site{sep}` | The pages. GitHub Pages serves them from the branch `site` of `{o}/{r}`. | "
         f"{vb['site']['files']:,} | {_mb(vb['site']['bytes'])} |"]
    for v in vols:
        L.append(f"| `{v}{sep}` | The data files the pages read (one file per gene, one per drug-dose). They go to the "
                 f"repository `{o}/{r}{DATA_REPO[v]}`, branch `main`. | {vb[v]['files']:,} | {_mb(vb[v]['bytes'])} |")
    L += [f"| `batches{sep}` | The upload lists. Each data list is at most {rec['batch_bytes'] / 1e9:.1f} GB on disk, "
          "because GitHub refuses one push over 2 GB. | | |",
          "| `publish.ps1`, `publish.sh` | The upload scripts. | | |",
          "| `RELEASE_ASSETS.txt` | Optional: the exact arrays as release files, and how to attach them. | | |",
          f"| `{RECORD}` | What this export did (used by `--force` and `--pin-data`). | | |", ""]
    if rec["hard_links"]:
        L += ["The files in the data folders are hard links to the files in the output's `explorer` folder (all "
              "but MANIFEST.tsv). They take no extra disk space. Do not edit them: an edit would change the output's "
              "file too. The export and the pin step replace files instead of writing into them. The `site` folder "
              "holds copies.", ""]
    L += ["## Once: two settings on github.com", "",
          f"1. **Create the data repository.** On github.com, click **New repository**. Name it `{r}-data`. Choose "
          "**Public**. Do not add a README, a license or a .gitignore. Click **Create repository**."
          + (f" Do the same for `{r}-data-dd`." if "data_dd" in vols else ""),
          "2. **Upload** (next section). The first upload creates the branch `site`.",
          f"3. **Turn on GitHub Pages.** Open https://github.com/{o}/{r}. Click the **Settings** tab (or the \"...\" "
          "menu, then Settings). In the left sidebar, under \"Code and automation\", click **Pages**. Under \"Build "
          "and deployment\", set **Source** to **Deploy from a branch**. Choose the branch **site** and the folder "
          "**/ (root)**. Click **Save**.",
          "4. **Wait up to 10 minutes.** The **Actions** tab shows \"pages-build-deployment\". Then Settings, Pages "
          f"says \"Your site is live at {rec['site_url']}\".", "",
          "Why public: the pages read the data files straight from GitHub (raw.githubusercontent.com), and GitHub "
          "Pages of a free account needs a public repository. Everything uploaded becomes public.", "",
          "## Upload", "",
          "Windows (PowerShell):", "", "```powershell",
          f"powershell -ExecutionPolicy Bypass -File \"{os.path.join(dest, 'publish.ps1')}\"", "```", "",
          "Linux or macOS:", "", "```bash", f"bash {shlex.quote(os.path.join(dest, 'publish.sh'))}", "```", "",
          "The script does this, in order:", ""]
    k = 1
    for v in vols:
        p_ = rec["parts"][v]
        L.append(f"{k}. It uploads `{v}` to `{o}/{r}{DATA_REPO[v]}`, branch `main`, in {p_['lists']} part(s) (about "
                 f"{_mb(sum(p_['bytes']))} in all). Each part is one commit and one push. The first push replaces the "
                 "branch, so the data repository keeps one snapshot: the newest.")
        k += 1
    L += [f"{k}. It pins the pages to that data commit (`python -m tahoemap export ... --pin-data <commit>`). The "
          "pages then read exactly the data of this run, even while a later upload is under way.",
          f"{k + 1}. It uploads `site` to the branch `site` of `{o}/{r}` (one snapshot). GitHub Pages publishes it "
          "within about 10 minutes.", "",
          f"The scripts push only to the branch `main` of the data repositories and to the branch `site` of "
          f"`{o}/{r}`. They never touch `results`, `finalized` or the default branch of `{o}/{r}`, and they stop if "
          "`site` is its default branch.", "",
          "- **Sign-in.** The first push asks you to sign in to GitHub (Git Credential Manager opens a window or a "
          "browser page). Use an account that may write to both repositories.",
          "- **Name and e-mail.** Git needs them once for the commits: `git config --global user.name \"Your Name\"` "
          "and `git config --global user.email \"you@example.com\"`.",
          "- **If an upload stops** (network, sign-in), run the script again with `-FromPart K` (`--from-part K` for "
          "bash), K being the data part that failed. The script prints each part as it is uploaded.",
          f"- **Programs used.** Python: `{py}`. Git: `{rec.get('git') or 'git on PATH'}` (git on PATH is used "
          "first). To use others, set `$env:TAHOE_PYTHON` or `$env:TAHOE_GIT` (bash: `TAHOE_PYTHON`, `TAHOE_GIT`) "
          "before running the script. A portable MinGit that is not on PATH works when TAHOE_GIT names its "
          "`cmd\\git.exe`.", ""]
    if rec.get("long_paths"):
        L += ["- **Long paths.** Some paths here pass Windows' 260-character limit. The scripts set "
              "`core.longpaths true` for git; keep the folder name short if git still complains.", ""]
    if rec.get("note_site"):
        L += [f"- **Web address.** {rec['note_site']}", ""]
    L += ["## Every later run", "", "```powershell" if win else "```bash"]
    if win:
        L += [f"& \"{py}\" -m tahoemap run --out \"{rec['source']}\"",
              f"& \"{py}\" -m tahoemap export \"{dest}\" --explorer --force --out \"{rec['source']}\"",
              f"powershell -ExecutionPolicy Bypass -File \"{os.path.join(dest, 'publish.ps1')}\""]
    else:
        L += [f"python -m tahoemap run --out {shlex.quote(rec['source'])}",
              f"python -m tahoemap export {shlex.quote(dest)} --explorer --force --out {shlex.quote(rec['source'])}",
              f"bash {shlex.quote(os.path.join(dest, 'publish.sh'))}"]
    L += ["```", "",
          "`--force` replaces only the files that changed and removes the files the explorer no longer has. Files "
          "that an earlier export did not write are left alone (they are not uploaded: the upload lists name every "
          "file that is).", "",
          "## Look at it before uploading", "",
          f"Open `{os.path.join(rec['source'], 'explorer', 'web', 'index.html')}` in a browser (a double-click "
          "works). It reads the data folder next to it, so it needs no network.", ""]
    return "\n".join(L)


def _explorer_report(rec):
    for name, c in rec["volumes"].items():
        log(f"  {name}/: {c.get('files', 0):,} files, {_mb(c.get('bytes', 0))}: {c.get('linked', 0):,} linked, "
            f"{c.get('copied', 0):,} copied, {c.get('kept', 0):,} unchanged, {c.get('removed', 0):,} removed")
    if rec.get("hosts"):
        log(f"  {rec['hosts']}")
    if rec.get("note_site"):
        log(f"  note: {rec['note_site']}")
    parts = ", ".join(f"{v}: {p['lists']} upload list(s)" for v, p in rec["parts"].items())
    log(f"Explorer export done in {rec['seconds']:.0f} s ({parts}). Nothing was uploaded.")
    d = rec["destination"]
    for ln in ["Next steps (PUBLISH.md says the same, with the one-time GitHub settings):",
               f"  1. once: create the public repository {rec['owner']}/{rec['repo']}-data on github.com "
               "(no README)",
               f"  2. upload: powershell -ExecutionPolicy Bypass -File \"{os.path.join(d, 'publish.ps1')}\"   "
               f"(Linux / macOS: bash {shlex.quote(os.path.join(d, 'publish.sh'))})",
               f"  3. once: Settings > Pages of {rec['site_repo']}: Deploy from a branch, branch site, / (root)",
               f"  then: {rec['site_url']}"]:
        print(ln, flush=True)


def cli(a):
    """python -m tahoemap export DEST (cli.main's namespace a)."""
    pin_d, pin_dd = getattr(a, "pin_data", None), getattr(a, "pin_data_dd", None)
    if getattr(a, "explorer", False) or pin_d or pin_dd:
        if len(a.names or []) != 1:
            sys.exit("usage: python -m tahoemap export DEST --explorer [--out OUTPUT] [--force] [--with-line-dd] "
                     "[--github OWNER/REPO]   (or: export DEST --explorer --pin-data SHA)")
        if pin_d or pin_dd:
            if pin_d:
                pin(a.names[0], pin_d, "data")
            if pin_dd:
                pin(a.names[0], pin_dd, "data_dd")
            return None
        return explorer_export(a.out, a.names[0], force=a.force, line_dd=getattr(a, "line_dd", False),
                               github=getattr(a, "github", None), max_mb=a.max_file_mb)
    if len(a.names or []) != 1:
        sys.exit("usage: python -m tahoemap export DEST [--out OUTPUT] [--with-effects] [--include FILE ...] "
                 "[--force] [--max-file-mb 95]")
    inc = [x for grp in (a.include or []) for x in (grp if isinstance(grp, list) else [grp])]
    return export(a.out, a.names[0], with_effects=a.with_effects, include=inc, force=a.force,
                  max_mb=a.max_file_mb, site_url=getattr(a, "site_url", None), github=getattr(a, "github", None))
