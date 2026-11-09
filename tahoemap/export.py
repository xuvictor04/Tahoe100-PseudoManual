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
import os
import shutil
import sys
import time

from . import __version__
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
    "atlas/effects": "the pooled drug-dose x gene matrices (hundreds of MB each at full scale): only with "
                     "--with-effects",
    "atlas/reports": "the atlas's reports: only with --with-effects",
    "atlas": "the atlas's index and build records (stages/build.json and stages/effects.json record the build)",
    "tensor": "the per-cell-line arrays (several GB at full scale): the tensor stage computes them again from "
              "atlas/effects",
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


def export(out, dest, with_effects=False, include=(), force=False, max_mb=MAX_MB):
    """Copy the shareable results of `out` into `dest` (module docstring). Returns the record of what it did."""
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
           "include": [os.path.abspath(i) for i in include or ()], "max_mb": float(max_mb)}
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
          "- **The validation**: `validation/report.md` reads well on GitHub.", "",
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


def cli(a):
    """python -m tahoemap export DEST (cli.main's namespace a)."""
    if len(a.names or []) != 1:
        sys.exit("usage: python -m tahoemap export DEST [--out OUTPUT] [--with-effects] [--include FILE ...] "
                 "[--force] [--max-file-mb 95]")
    inc = [x for grp in (a.include or []) for x in (grp if isinstance(grp, list) else [grp])]
    return export(a.out, a.names[0], with_effects=a.with_effects, include=inc, force=a.force,
                  max_mb=a.max_file_mb)
