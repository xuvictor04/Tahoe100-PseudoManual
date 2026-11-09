#!/usr/bin/env python3
"""test_export.py - `tahoemap export` (tahoemap/export.py): the shareable results of a finished output, ready for a
GitHub branch.

    python3 tests/test_export.py [--out FINISHED_OUTPUT] [--workdir DIR] [--keep]

Needs a finished tahoemap output folder: --out, else the one tests/run_tests.py leaves in --workdir/out_seed0
(default $TAHOE_TEST_DIR, else /tmp/tahoemap_test; on Windows tahoemap_test in the temp folder). That folder is only
read: the test copies it to DIR/export_test/out (without the big per-well and per-line arrays, which get small
stand-ins) and adds what an export must leave alone - review caches, key state, lock and stop files, temporary files,
raw reference downloads, hf/ - and a few literature-review results it must copy. No network; a few seconds.

Checks: the folders and files copied (direction/ whole, and described) and the ones never copied; --include;
MANIFEST.tsv (every file, bytes and sha256, nothing else in DEST); .gitattributes ('* -text'); README.md (folders,
provenance, stage states, what was left out and why, the files too large for GitHub); a file over the limit skipped
and listed (a 96 MiB sparse file at the default 95 MiB, and a lowered --max-file-mb); a DEST inside OUT (or holding
OUT) refused, also with other letter case on a case-insensitive system; a non-empty DEST refused without --force;
--force: unchanged files kept, files the source no longer has removed, the user's own files (a .git folder, notes)
left alone, a file in the way that the manifest does not list stops it before anything is copied; --with-effects; a
live pipeline lock refused; the command line (python -m tahoemap export ...) and its next steps; and, when git is
found (as the pipeline finds it: $TAHOE_GIT, PATH, or on Windows Git for Windows or a MinGit next to the
repository), a commit of DEST that stores a CRLF file byte for byte with core.autocrlf=true. DIR/export_test is
removed before and after (--keep keeps it), the commit's read-only git objects included.

The explorer (export DEST --explorer; needs an output whose explorer stage ran): site/ is the web volume byte for
byte, data/ the data volume as hard links (copies, checked against the stage's sha256, where links cannot be made);
the pages are copies (never links: the stage can rewrite its page files in place); the upload lists hold every
data file once, each within its limit, probe.js and MANIFEST.tsv last; publish.ps1 and
publish.sh push only HEAD:refs/heads/main to the data repository and HEAD:refs/heads/site to the code repository;
--pin-data rewrites site/d/hosts.js and its MANIFEST.tsv line and never the output's file; a small cap (pages,
file or upload list) is refused before anything is written; a stale explorer is refused; --force replaces only what
changed, removes what the explorer no longer has and stops at a file in the way; RELEASE_ASSETS.txt; the results
README names the explorer; and, with bash and git, publish.sh end to end against local bare repositories standing in
for GitHub (results and finalized untouched; the data branch keeps one snapshot).

Prints PASS / FAIL per check; exit code 1 if anything fails.
"""

import argparse
import hashlib
import json
import os
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DEFAULT_WORKDIR = "/tmp/tahoemap_test" if os.name != "nt" else os.path.join(tempfile.gettempdir(), "tahoemap_test")
sys.path.insert(0, REPO)

from tahoemap import export as X  # noqa: E402
from tahoemap.common import find_git  # noqa: E402

RESULTS = []


def check(case, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    RESULTS.append((case, name, status))
    print(f"  [{status}] {case}: {name}" + (f" -- {detail}" if detail else ""), flush=True)
    return ok


def case(fn):
    def wrapped(*a, **k):
        print(f"\n== {fn.__name__}", flush=True)
        try:
            return fn(*a, **k)
        except Exception as e:  # noqa: BLE001
            check(fn.__name__, "ran without an exception", False, f"{type(e).__name__}: {e}\n{traceback.format_exc()}")
    return wrapped


def refused(fn, *a, **k):
    """The SystemExit message of fn(*a, **k), or None when it did not exit."""
    try:
        fn(*a, **k)
    except SystemExit as e:
        return str(e.code)
    return None


def write(path, data=b"x"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data if isinstance(data, bytes) else data.encode("utf-8"))


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def manifest(dest):
    with open(os.path.join(dest, "MANIFEST.tsv"), encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    rows = [ln.split("\t") for ln in lines[1:] if ln]
    return lines[0], {p: (int(n), h) for p, n, h in rows}


def files_under(d):
    out = set()
    for root, dirs, fs in os.walk(d):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in fs:
            out.add(os.path.relpath(os.path.join(root, f), d).replace(os.sep, "/"))
    return out


def dead_pid():
    p = subprocess.Popen([sys.executable, "-c", "pass"])
    p.wait()
    return p.pid


def quiet(fn, *a, **k):
    """fn(*a, **k) with its log lines and printed next steps kept from the test's output."""
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        return fn(*a, **k)


# ----------------------------------------------------------------------------- the test copy
NEVER = ["tensor/DDL_z.npy", "atlas/pseudobulk/group000.npy", "hf/data/train-0000.parquet",
         "reference/downloads/hgnc_complete_set.txt", "review/cache/pubmed/ab/abcdef.json",
         "review/dry_run/summary.json", "review/keys_state.json", "review/ledger.unwritten.jsonl", "review/.run.lock",
         "review/.stop", "tables/genes.parquet.tmp", "vault/Home.md.part", ".pipeline.lock", ".job.pid"]
DIRECTION = ["direction/edges.parquet", "direction/groups.parquet", "direction/controls.json", "direction/info.json",
             "direction/README.md"]
REVIEW = ["review/reviews/gene/TP53.json", "review/notes/gene/TP53.md", "review/history/gene/TP53/20261109-0001.jsonl",
          "review/ledger.jsonl", "review/queue.parquet", "review/connections.parquet", "review/findings.parquet",
          "review/review.log"]


def _writable_again(_fn, path, _exc):
    """rmtree's error handler: make a read-only file writable and remove it again. git marks its object files
    read-only and Windows does not delete such a file: rmtree(ignore_errors=True) would leave DEST's .git behind,
    and the next run's export into it would be refused (a non-empty DEST)."""
    try:
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
        if os.path.isdir(path) and not os.path.islink(path):
            os.rmdir(path)
        else:
            os.unlink(path)
    except OSError:
        pass


def rm_tree(path):
    """Remove a folder of this test, read-only files included; True when it is gone."""
    if os.path.isdir(path) and not os.path.islink(path):
        kw = {"onexc": _writable_again} if sys.version_info >= (3, 12) else {"onerror": _writable_again}
        shutil.rmtree(path, **kw)
    return not os.path.lexists(path)


def make_copy(src, work):
    """OUT for the test: the finished output without its big arrays, plus the files an export must leave alone."""
    base = os.path.join(work, "export_test")
    if not rm_tree(base):
        sys.exit(f"test_export.py: could not remove {base} (left by an earlier run): close what has a file of it "
                 "open, or remove it yourself, and run again")
    out = os.path.join(base, "out")

    def ignore(d, names):
        rel = os.path.relpath(d, src).replace(os.sep, "/")
        if rel in ("tensor", "atlas/pseudobulk", "hf", "review"):
            return list(names)
        return [n for n in names if n in (".pipeline.lock", ".job.pid")]
    shutil.copytree(src, out, ignore=ignore, symlinks=True)
    dead = dead_pid()
    for rel in NEVER:
        data = b"x"
        if rel.endswith(".lock"):
            data = json.dumps({"pid": dead, "host": socket.gethostname(), "started": "2026-01-01T00:00:00"}).encode()
        write(os.path.join(out, *rel.split("/")), data)
    for rel in REVIEW:
        write(os.path.join(out, *rel.split("/")), f"review result {rel}\n")
    return base, out


# ----------------------------------------------------------------------------- cases
@case
def basic(base, out):
    dest = os.path.join(base, "dest")
    inc = os.path.join(base, "RUN_REPORT.md")
    write(inc, "# Run report\r\nwith Windows line ends\r\n")
    rec = quiet(X.export, out, dest, include=[inc])
    got = files_under(dest)
    must = ["vault/Home.md", "map/gene_map.html", "tables/drug_effects.parquet", "tables/README.md",
            "validation/report.md", "graph/nodes.parquet", "relations/gene_relations.parquet", "embed/genes.parquet",
            "embed/info.json", "reference/annotations.parquet", "reference/sources.json", "stages/embed.json",
            "run_options.json", "run.log", "RUN_REPORT.md", "README.md", "MANIFEST.tsv", ".gitattributes"] + REVIEW
    must += DIRECTION
    must = [m for m in must if os.path.exists(os.path.join(out, *m.split("/"))) or m in X.WRITTEN
            or m == "RUN_REPORT.md"]
    miss = [m for m in must if m not in got]
    check("basic", "the shareable results are copied (vault, map, tables, validation, direction, graph, relations, "
          "embed, reference tables, stages, run files, review results, --include)", not miss, f"missing {miss}")
    have_dir = all(os.path.exists(os.path.join(out, *m.split("/"))) for m in DIRECTION)
    n_dir = sum(1 for f in files_under(os.path.join(out, "direction"))) if have_dir else 0
    check("basic", "direction/ is copied whole (edges, groups, controls, info, README) and described in README.md",
          have_dir and sum(1 for f in got if f.startswith("direction/")) == n_dir and n_dir >= len(DIRECTION),
          f"{n_dir} files in OUT/direction" if have_dir else f"the output has no direction stage ({DIRECTION[0]})")
    n_vault = sum(1 for f in files_under(os.path.join(out, "vault")) if not f.endswith((".tmp", ".part")))
    check("basic", "every vault note is copied", sum(1 for f in got if f.startswith("vault/")) == n_vault,
          f"{n_vault} in OUT")
    bad = [g for g in got if g.split("/")[0] in ("atlas", "tensor", "hf") or g in NEVER
           or g.startswith(("reference/downloads/", "review/cache/", "review/dry_run/"))
           or g.endswith((".tmp", ".part"))]
    check("basic", "never copied: atlas/ (without --with-effects), tensor/, hf/, raw downloads, review caches and "
          "dry runs, key state, unwritten ledger lines, lock / stop / job / temporary files", not bad, f"{bad[:8]}")
    head, man = manifest(dest)
    listed = set(man)
    check("manifest", "MANIFEST.tsv: header path / bytes / sha256, one row per file in DEST (itself excepted)",
          head == "path\tbytes\tsha256" and listed == got - {"MANIFEST.tsv"},
          f"not listed {sorted(got - listed - {'MANIFEST.tsv'})[:5]}, listed but absent {sorted(listed - got)[:5]}")
    wrong = [p for p, (n, h) in man.items() if os.path.getsize(os.path.join(dest, *p.split("/"))) != n
             or sha(os.path.join(dest, *p.split("/"))) != h]
    check("manifest", "every size and sha256 matches the file", not wrong, f"{wrong[:5]}")
    same = [p for p in man if p not in X.WRITTEN and p != "RUN_REPORT.md"
            and sha(os.path.join(out, *p.split("/"))) != man[p][1]]
    check("manifest", "the copies are byte for byte the output's files", not same, f"{same[:5]}")
    with open(os.path.join(dest, ".gitattributes"), encoding="utf-8") as fh:
        ga = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    check("gitattributes", "'* -text' (git stores every file byte for byte)", ga == ["* -text"], f"{ga}")
    with open(os.path.join(dest, "README.md"), encoding="utf-8") as fh:
        rd = fh.read()
    want = ["## What each folder holds", "`vault`", "`map`", "`direction`", "probable direction", "Obsidian",
            "gene_map.html", "## Provenance", "| direction |",
            "tahoemap version", "code commit", "| embed |", "## What was left out, and why", "`tensor`",
            "`atlas/pseudobulk`", "`reference/downloads`", "`review/cache`", "`review/keys_state.json`",
            "MANIFEST.tsv"]
    check("readme", "README.md: folders, how to open the vault and the map, provenance, stage stamps, what was left "
          "out and why", all(w in rd for w in want), f"missing {[w for w in want if w not in rd]}")
    check("readme", "README.md names the code commit (or says git was not found)",
          (rec["code"]["commit"] or "unknown") in rd, f"{rec['code']['commit']}")
    with open(os.path.join(dest, "RUN_REPORT.md"), "rb") as fh:
        check("include", "--include FILE: copied to the top of DEST byte for byte (CRLF kept)",
              fh.read() == b"# Run report\r\nwith Windows line ends\r\n")
    msg = refused(quiet, X.export, out, os.path.join(base, "dest_inc"), include=[os.path.join(dest, "README.md")])
    check("include", "--include of a name the export writes (README.md) is refused", bool(msg and "README.md" in msg),
          msg or "")
    msg = refused(quiet, X.export, out, os.path.join(base, "dest_inc2"), include=[os.path.join(base, "nope.md")])
    check("include", "--include of a file that does not exist is refused", bool(msg and "does not exist" in msg),
          msg or "")
    return dest, rec


@case
def too_large(base, out):
    big = os.path.join(out, "tables", "huge_test.parquet")
    with open(big, "wb") as fh:                       # sparse where the file system allows it: no 96 MiB written
        fh.truncate(96 * 2 ** 20)
    try:
        dest = os.path.join(base, "dest_big")
        rec = quiet(X.export, out, dest)
        got = files_under(dest)
        with open(os.path.join(dest, "README.md"), encoding="utf-8") as fh:
            rd = fh.read()
        check("too large", "a 96 MiB file is not copied at the default limit (95 MiB) and is listed",
              "tables/huge_test.parquet" not in got and ("tables/huge_test.parquet", 96 * 2 ** 20) in rec["too_large"]
              and "`tables/huge_test.parquet` (96.0 MiB)" in rd and "Too large for GitHub" in rd,
              f"too_large {rec['too_large']}")
        _, man = manifest(dest)
        check("too large", "the skipped file is not in MANIFEST.tsv", "tables/huge_test.parquet" not in man)
    finally:
        os.remove(big)
    dest = os.path.join(base, "dest_small_limit")
    rec = quiet(X.export, out, dest, max_mb=0.5)
    over = sorted(r for r, n in rec["too_large"])
    real_over = sorted(r for _, r, n in X.plan(out)["files"] if n > 0.5 * 2 ** 20)
    got = files_under(dest)
    check("too large", "--max-file-mb 0.5: every file over 0.5 MiB skipped and listed, the rest copied",
          over == real_over and over and not (set(over) & got), f"{len(over)} skipped, e.g. {over[:3]}")


@case
def refusals(base, out, dest):
    for d, what in ((os.path.join(out, "export"), "a DEST inside OUT"),
                    (os.path.join(out, "vault", "x"), "a DEST deep inside OUT"),
                    (base, "a DEST that holds OUT")):
        msg = refused(quiet, X.export, out, d)
        check("refusals", f"{what} is refused", bool(msg and "outside the output folder" in msg), msg or "")
    probe = os.path.join(out, "CaseProbe")
    write(probe, "x")
    insensitive = os.path.exists(os.path.join(out, "caseprobe"))
    os.remove(probe)
    if insensitive:
        d = os.path.join(out.swapcase() if out.swapcase() != out else out, "export")
        msg = refused(quiet, X.export, out, d)
        check("refusals", "a DEST inside OUT written in other letter case is refused (case-insensitive file system)",
              bool(msg and "outside the output folder" in msg), msg or "")
    else:
        from tahoemap.cli import _inside
        import ntpath
        check("refusals", "(case-sensitive file system) the guard compares Windows paths case-insensitively",
              _inside("C:\\Users\\Me\\TAHOE\\out\\Export", "c:\\users\\me\\tahoe\\OUT", P=ntpath))
    msg = refused(quiet, X.export, out, dest)
    check("refusals", "a non-empty DEST without --force is refused", bool(msg and "--force" in msg), msg or "")
    msg = refused(quiet, X.export, os.path.join(base, "no_such_output"), os.path.join(base, "d_none"))
    check("refusals", "an OUT that is no tahoemap output is refused", bool(msg and "not a tahoemap output" in msg),
          msg or "")
    lock = os.path.join(out, ".pipeline.lock")
    with open(lock, encoding="utf-8") as fh:
        saved = fh.read()
    try:
        with open(lock, "w", encoding="utf-8") as fh:
            json.dump({"pid": os.getppid(), "host": socket.gethostname(), "command": "tahoemap run"}, fh)
        msg = refused(quiet, X.export, out, os.path.join(base, "d_busy"))
        check("refusals", "a pipeline command working on OUT (a live lock) is refused",
              bool(msg and "pipeline command" in msg), msg or "")
    finally:
        with open(lock, "w", encoding="utf-8") as fh:
            fh.write(saved)
    check("refusals", "stale locks (their process is gone) do not stop an export", os.path.isdir(dest))


@case
def force(base, out, dest):
    # the user's own files in DEST: a git repository and a note
    write(os.path.join(dest, ".git", "config"), "[core]\n")
    write(os.path.join(dest, "my_notes.txt"), "mine")
    _, man0 = manifest(dest)
    rec = quiet(X.export, out, dest, force=True, include=[os.path.join(base, "RUN_REPORT.md")])
    check("force", "--force on an unchanged output copies nothing again", rec["copied"] == 0 and rec["unchanged"] > 0,
          f"copied {rec['copied']}, unchanged {rec['unchanged']}")
    check("force", "the user's files (.git, notes) are left alone",
          os.path.exists(os.path.join(dest, ".git", "config")) and os.path.exists(os.path.join(dest, "my_notes.txt")))
    _, man1 = manifest(dest)
    check("force", "the manifest is the same", {k: v for k, v in man1.items() if k != "README.md"} ==
          {k: v for k, v in man0.items() if k != "README.md"})
    # the output changes: a note removed, a table changed, a new file
    notes = sorted(f for f in files_under(os.path.join(out, "vault", "Genes")) if f.endswith(".md"))
    gone = "vault/Genes/" + notes[0]
    keep = open(os.path.join(out, *gone.split("/")), "rb").read()
    os.remove(os.path.join(out, *gone.split("/")))
    changed = os.path.join(out, "validation", "report.md")
    old = open(changed, "rb").read()
    write(changed, old + b"\nchanged\n")
    new = os.path.join(out, "stages", "zz_test.json")
    write(new, "{}")
    try:
        rec = quiet(X.export, out, dest, force=True, include=[os.path.join(base, "RUN_REPORT.md")])
        got = files_under(dest)
        check("force", "a file the output no longer has is removed (the manifest listed it)",
              gone not in got and gone in rec["removed"], f"removed {rec['removed'][:3]}")
        check("force", "a changed file is copied again, a new one added",
              open(os.path.join(dest, "validation", "report.md"), "rb").read().endswith(b"changed\n")
              and "stages/zz_test.json" in got and rec["copied"] == 2, f"copied {rec['copied']}")
        check("force", "the user's files are still there", os.path.exists(os.path.join(dest, "my_notes.txt")))
        # a file in the way that no export wrote: refused before anything is copied
        write(os.path.join(dest, "stages", "zz_user.json"), "mine")
        new2 = os.path.join(out, "stages", "zz_user.json")
        write(new2, "{}")
        write(changed, old + b"\nchanged twice\n")
        msg = refused(quiet, X.export, out, dest, force=True)
        check("force", "a file in the way that MANIFEST.tsv does not list stops the export",
              bool(msg and "stages/zz_user.json" in msg), msg or "")
        check("force", "... before anything was copied (the user's file and the earlier copy unchanged)",
              open(os.path.join(dest, "stages", "zz_user.json")).read() == "mine"
              and open(os.path.join(dest, "validation", "report.md"), "rb").read().endswith(b"changed\n"))
        os.remove(new2)
        os.remove(os.path.join(dest, "stages", "zz_user.json"))
    finally:
        write(os.path.join(out, *gone.split("/")), keep)
        write(changed, old)
        if os.path.exists(new):
            os.remove(new)


@case
def with_effects(base, out):
    dest = os.path.join(base, "dest_fx")
    quiet(X.export, out, dest, with_effects=True)
    got = files_under(dest)
    fx = sorted(f for f in files_under(os.path.join(out, "atlas", "effects")))
    have = [f for f in fx if f"atlas/effects/{f}" in got]
    check("with effects", "--with-effects copies atlas/effects (the DD_*.npy matrices and the CSV tables)",
          len(have) == len(fx) and any(f.startswith("DD_") for f in have) and any(f.endswith(".csv") for f in have),
          f"{len(have)} of {len(fx)}")
    bad = [g for g in got if g.startswith(("atlas/pseudobulk", "tensor/", "hf/")) or g in NEVER]
    check("with effects", "... but never atlas/pseudobulk, tensor/ or hf/", not bad, f"{bad[:5]}")


@case
def command_line(base, out):
    dest = os.path.join(base, "dest_cli")
    r = subprocess.run([sys.executable, "-m", "tahoemap", "export", dest, "--out", out, "--include",
                        os.path.join(base, "RUN_REPORT.md"), "--max-file-mb", "95"], cwd=REPO, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    steps = ["git init", "git checkout --orphan results", "git add -A", "git commit", "git remote add origin",
             "git push -u origin results"]
    check("command line", "python -m tahoemap export DEST --out OUT --include FILE: exit 0, the total size and the "
          "git next steps", r.returncode == 0 and all(s in r.stdout for s in steps) and "Export done" in r.stdout
          + r.stderr and os.path.exists(os.path.join(dest, "RUN_REPORT.md")), (r.stdout + r.stderr)[-600:])
    r = subprocess.run([sys.executable, "-m", "tahoemap", "export", dest, "--out", out], cwd=REPO,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    check("command line", "again without --force: refused, exit code not 0", r.returncode != 0
          and "--force" in r.stderr, r.stderr[-300:])
    return dest


@case
def explorer_command_line(base, out):
    if not os.path.exists(os.path.join(out, "stages", "explorer.json")):
        return
    dest = os.path.join(base, "pub_cli")
    r = subprocess.run([sys.executable, "-m", "tahoemap", "export", dest, "--explorer", "--out", out, "--github",
                        "tahoe-test/Tahoe100-PseudoManual"], cwd=REPO, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    r2 = subprocess.run([sys.executable, "-m", "tahoemap", "export", dest, "--explorer", "--pin-data", "abcdef1"],
                        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace")
    h = _hosts(os.path.join(dest, "site", "d", "hosts.js")) if os.path.exists(os.path.join(dest, "site")) else {}
    check("explorer", "python -m tahoemap export DEST --explorer: exit 0, next steps printed (create the data "
          "repository, publish.ps1, Settings > Pages); --pin-data SHA from the command line",
          r.returncode == 0 and "publish.ps1" in r.stdout and "Settings > Pages" in r.stdout
          and "Tahoe100-PseudoManual-data" in r.stdout and r2.returncode == 0
          and "/abcdef1/" in (h.get("data") or [""])[0],
          (r.stdout + r.stderr)[-400:] + (r2.stdout + r2.stderr)[-200:])


@case
def git_commit(dest):
    git = find_git()             # as `tahoe` finds it: $TAHOE_GIT, PATH, then Git for Windows / a MinGit next to
    if not git:                  # the repository (the PC's git is such a MinGit, not on PATH)
        check("git", "(git not found: on PATH, $TAHOE_GIT, or a MinGit next to the repository; the commit check is "
              "skipped)", True)
        return
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", HOME=os.path.dirname(dest))
    g = [git, "-c", "user.name=tahoemap test", "-c", "user.email=test@example.invalid", "-c", "core.autocrlf=true",
         "-c", "init.defaultBranch=main"]

    def run(*args):
        return subprocess.run(g + list(args), cwd=dest, capture_output=True, text=True, env=env)
    steps = [run("init", "-q"), run("checkout", "-q", "--orphan", "results"), run("add", "-A"),
             run("commit", "-q", "-m", "tahoemap results")]
    ok = all(s.returncode == 0 for s in steps)
    blob = subprocess.run(g + ["cat-file", "-p", "HEAD:RUN_REPORT.md"], cwd=dest, capture_output=True,
                          env=env).stdout
    check("git", "DEST commits as an orphan branch 'results'; a CRLF file is stored byte for byte with "
          "core.autocrlf=true (.gitattributes '* -text')", ok and blob == b"# Run report\r\nwith Windows line ends\r\n",
          "; ".join(s.stderr.strip() for s in steps if s.returncode)[:300] or f"{blob[:40]!r}")
    n = len([ln for ln in run("ls-files").stdout.split("\n") if ln])
    _, man = manifest(dest)
    check("git", "git tracks every exported file (the manifest's and MANIFEST.tsv)", n == len(man) + 1,
          f"{n} tracked, {len(man) + 1} exported")


# ----------------------------------------------------------------------------- the explorer (export --explorer)
def _vol_manifest(root):
    with open(os.path.join(root, "MANIFEST.tsv"), encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    return {p: (int(n), h) for p, n, h in (ln.split("\t") for ln in lines[1:] if ln)}


def _hosts(path):
    import re
    with open(path, encoding="utf-8") as fh:
        return json.loads(re.match(r"^TAHOE_HOSTS\((.*)\);\s*$", fh.read(), re.S).group(1))


def _pushes(script):
    """(remote or variable, refspec) of every push line of a publish script, and the names of every branch it
    names anywhere."""
    import re
    pushes = []
    for ln in script.splitlines():
        t = ln.strip()
        if t.startswith("#") or " push " not in f" {t} ":
            continue
        pushes += re.findall(r"push\s+(?:-q\s+)?(?:--force\s+)?(\S+)\s+'?\"?([^\s'\"]+)", t)
    return pushes


def refspecs_ok(script, repo):
    """The publish scripts' rule: every push is HEAD:refs/heads/main (the data repository) or HEAD:refs/heads/site
    (the code repository); no line pushes or names results, finalized or master; the data remotes are
    <repo>-data(.git) and the site remote <repo>.git. Returns (ok, detail)."""
    import re
    pushes = _pushes(script)
    specs = sorted({sp for _r, sp in pushes})
    bad = [sp for sp in specs if sp not in ("HEAD:refs/heads/main", "HEAD:refs/heads/site")]
    named = [w for w in ("results", "finalized", "master") if re.search(rf"\b{w}\b", script)]
    remotes = re.findall(r"https://github\.com/[A-Za-z0-9._/-]+", script)
    data_r = [u for u in remotes if u.rstrip("/").endswith((f"{repo}-data.git", f"{repo}-data-dd.git"))]
    site_r = [u for u in remotes if u.rstrip("/").endswith(f"/{repo}.git")]
    others = [u for u in remotes if u not in data_r and u not in site_r]
    ok = bool(pushes) and not bad and not named and not others and bool(site_r) and bool(data_r) and \
        "HEAD:refs/heads/site" in specs and "HEAD:refs/heads/main" in specs
    return ok, f"push refspecs {specs}; other refspecs {bad}; forbidden names {named}; other remotes {others}"


@case
def explorer_export(base, out):
    xo = os.path.join(out, "explorer")
    if not os.path.exists(os.path.join(out, "stages", "explorer.json")):
        check("explorer", "(the output has no explorer: the explorer export checks are skipped)", True)
        return None
    web, dat = os.path.join(xo, "web"), os.path.join(xo, "data")
    dest = os.path.join(base, "pub")
    rec = quiet(X.explorer_export, out, dest, github="tahoe-test/Tahoe100-PseudoManual")
    want = ["site", "data", "batches", "publish.ps1", "publish.sh", "PUBLISH.md", "RELEASE_ASSETS.txt",
            "EXPLORER_EXPORT.json"]
    have = sorted(os.listdir(dest))
    check("explorer", "export --explorer writes site/, data/, batches/, publish.ps1, publish.sh, PUBLISH.md, "
          "RELEASE_ASSETS.txt and EXPLORER_EXPORT.json", all(w in have for w in want), f"{have}")
    wm = _vol_manifest(web)
    site = os.path.join(dest, "site")
    got = files_under(site)
    diff = [p for p, (n, h) in wm.items() if p != "d/hosts.js"
            and (not os.path.exists(os.path.join(site, *p.split("/"))) or sha(os.path.join(site, *p.split("/"))) != h)]
    links = [p for p in got if os.path.samefile(os.path.join(site, *p.split("/")), os.path.join(web, *p.split("/")))]
    check("explorer", "site/ is the web volume byte for byte, as copies (every MANIFEST.tsv row; .nojekyll, "
          "README.md, .gitattributes and MANIFEST.tsv included; nothing else)",
          not diff and got == set(wm) | {"MANIFEST.tsv"} and {".nojekyll", "README.md", ".gitattributes"} <= got
          and not links, f"{len(got)} files, {len(wm)} listed; different {diff[:3]}; extra "
                         f"{sorted(got - set(wm))[:4]}; hard links {links[:3]}")
    dm = _vol_manifest(dat)
    linked = [p for p in dm if os.path.samefile(os.path.join(dat, *p.split("/")),
                                                os.path.join(dest, "data", *p.split("/")))]
    check("explorer", "data/ is the data volume as hard links on the same disk (no extra space; its MANIFEST.tsv a "
          "copy: DEST's own record)", not os.path.samefile(os.path.join(dat, "MANIFEST.tsv"),
                                                           os.path.join(dest, "data", "MANIFEST.tsv"))
          and sha(os.path.join(dat, "MANIFEST.tsv")) == sha(os.path.join(dest, "data", "MANIFEST.tsv")))
    check("explorer", "data/ is the data volume as hard links on the same disk (no extra space)",
          rec["hard_links"] and len(linked) == len(dm) and files_under(os.path.join(dest, "data")) == set(dm) |
          {"MANIFEST.tsv"}, f"{len(linked)} of {len(dm)} files linked")
    lists = [ln for f in sorted(os.listdir(os.path.join(dest, "batches"))) if f.startswith("data_")
             for ln in open(os.path.join(dest, "batches", f), encoding="utf-8").read().split("\n") if ln]
    with open(os.path.join(dest, "batches", "site.txt"), encoding="utf-8") as fh:
        site_list = [ln for ln in fh.read().split("\n") if ln]
    check("explorer", "upload lists: every data file in one list, .gitattributes first, probe.js and MANIFEST.tsv "
          "last; site.txt lists every page file", sorted(lists) == sorted(set(dm) | {"MANIFEST.tsv"})
          and len(lists) == len(set(lists)) and lists[0] == ".gitattributes" and lists[-2:] == ["probe.js",
                                                                                                "MANIFEST.tsv"]
          and sorted(site_list) == sorted(got), f"{len(lists)} data paths, {len(site_list)} site paths")
    for name in ("publish.ps1", "publish.sh"):
        with open(os.path.join(dest, name), encoding="utf-8") as fh:
            ok, detail = refspecs_ok(fh.read(), "Tahoe100-PseudoManual")
        check("explorer", f"{name} pushes only HEAD:refs/heads/main to the data repository and HEAD:refs/heads/site "
              "to the code repository (never results, finalized or master)", ok, detail)
    with open(os.path.join(dest, "PUBLISH.md"), encoding="utf-8") as fh:
        md = fh.read()
    words = ["New repository", "Tahoe100-PseudoManual-data", "Public", "Deploy from a branch", "/ (root)", "**site**",
             "publish.ps1", "-ExecutionPolicy Bypass", "--force", "pages-build-deployment", "never touch"]
    check("explorer", "PUBLISH.md: the one-time GitHub steps (data repository, Pages from branch site / root), the "
          "upload and every later run", all(w in md for w in words), f"missing {[w for w in words if w not in md]}")
    with open(os.path.join(dest, "RELEASE_ASSETS.txt"), encoding="utf-8") as fh:
        ra = fh.read()
    npys = sorted(f for f in os.listdir(os.path.join(out, "atlas", "effects")) if f.endswith(".npy"))
    rows = {ln.split("\t")[0]: ln.split("\t") for ln in ra.splitlines() if ln.startswith("atlas/")}
    good = [f for f in npys if f"atlas/effects/{f}" in rows
            and rows[f"atlas/effects/{f}"][2] == sha(os.path.join(out, "atlas", "effects", f))]
    check("explorer", "RELEASE_ASSETS.txt: every atlas/effects/*.npy with its sha256, and the gh release command",
          len(good) == len(npys) > 0 and "gh release create explorer-" in ra and "-data" in ra,
          f"{len(good)} of {len(npys)}")
    # --pin-data
    hp_out = os.path.join(web, "d", "hosts.js")
    before = sha(hp_out)
    commit = "0123456789abcdef0123456789abcdef01234567"
    quiet(X.pin, dest, commit)
    hp = os.path.join(dest, "site", "d", "hosts.js")
    h = _hosts(hp)
    sm = _vol_manifest(os.path.join(dest, "site"))
    check("explorer", "--pin-data: site/d/hosts.js reads the data at that commit first, then the branch; its "
          "MANIFEST.tsv line matches; the output's hosts.js is unchanged",
          h["data"] == [f"https://raw.githubusercontent.com/tahoe-test/Tahoe100-PseudoManual-data/{commit}/",
                        "https://raw.githubusercontent.com/tahoe-test/Tahoe100-PseudoManual-data/main/"]
          and sm["d/hosts.js"] == (os.path.getsize(hp), sha(hp)) and sha(hp_out) == before
          and h["run"] == rec["run"], f"{h['data']}")
    msg = refused(quiet, X.pin, dest, "not-a-sha")
    check("explorer", "--pin-data with something that is no commit id is refused", bool(msg and "commit" in msg),
          msg or "")
    # refusals: not empty without --force; small caps before anything is written; a stale explorer
    msg = refused(quiet, X.explorer_export, out, dest, github="tahoe-test/Tahoe100-PseudoManual")
    check("explorer", "a DEST with an earlier explorer export is refused without --force", bool(msg and "--force" in
                                                                                                    (msg or "")), msg)
    caps = [("site_max_mb", 1, "--pages-max-mb"), ("max_mb", 0.01, "GitHub refuses files"),
            ("batch_bytes", 1000, "upload list")]
    res = []
    for k, v, word in caps:
        d = os.path.join(base, f"pub_cap_{k}")
        msg = refused(quiet, X.explorer_export, out, d, github="tahoe-test/Tahoe100-PseudoManual", **{k: v})
        res.append((k, bool(msg and word in msg and not os.path.exists(d)), (msg or "")[:90]))
    check("explorer", "small caps are refused before anything is written: the pages over --pages-max-mb, a file over "
          "the file limit, a file larger than an upload list", all(r[1] for r in res), res)
    stamp_p = os.path.join(out, "stages", "explorer.json")
    keep = open(stamp_p, "rb").read()
    st = json.loads(keep)
    st["info"]["assets_sha"] = "0" * 64
    write(stamp_p, json.dumps(st))
    try:
        msg1 = refused(quiet, X.explorer_export, out, os.path.join(base, "pub_stale"))
    finally:
        write(stamp_p, keep)
    tp = os.path.join(out, "stages", "tables.json")
    keep_t = open(tp, "rb").read()
    tt = json.loads(keep_t)
    tt["finished"] = "1999-01-01 00:00:00"
    write(tp, json.dumps(tt))
    try:
        msg2 = refused(quiet, X.explorer_export, out, os.path.join(base, "pub_stale2"))
    finally:
        write(tp, keep_t)
    check("explorer", "a stale explorer is refused: its page files changed (assets_sha), or a stage it was made from "
          "ran again (run id)", bool(msg1 and "page files" in msg1 and msg2 and "run id" in msg2),
          f"{(msg1 or '')[:80]} | {(msg2 or '')[:80]}")
    # --force: unchanged files kept, the pinned hosts.js replaced, a file the explorer no longer has removed
    gone = os.path.join(dest, "data", "x", "zz_old.js")
    write(gone, "old")
    with open(os.path.join(dest, "data", "MANIFEST.tsv"), "a", encoding="utf-8") as fh:
        fh.write(f"x/zz_old.js\t3\t{sha(gone)}\n")
    rec2 = quiet(X.explorer_export, out, dest, force=True, github="tahoe-test/Tahoe100-PseudoManual")
    v2 = rec2["volumes"]
    check("explorer", "--force: unchanged files kept, the pinned hosts.js replaced by the output's (publish pins it "
          "again), a file the explorer no longer has removed",
          v2["data"]["kept"] == len(dm) + 1 - 1 and v2["data"]["removed"] == 1 and not os.path.exists(gone)
          and v2["site"]["copied"] >= 1 and _hosts(hp)["data"] == [
              "https://raw.githubusercontent.com/tahoe-test/Tahoe100-PseudoManual-data/main/"], f"{v2}")
    victim = sorted(p for p in dm if p.startswith("x/"))[0]
    vp = os.path.join(dest, "data", *victim.split("/"))
    os.remove(vp)
    write(vp, "the user's own file")
    mp = os.path.join(dest, "data", "MANIFEST.tsv")
    with open(mp, encoding="utf-8") as fh:
        kept_m = fh.read()
    write(mp, "".join(ln + "\n" for ln in kept_m.split("\n") if ln and not ln.startswith(victim + "\t")))
    msg = refused(quiet, X.explorer_export, out, dest, force=True, github="tahoe-test/Tahoe100-PseudoManual")
    ok_way = bool(msg and victim in msg) and open(vp, encoding="utf-8").read() == "the user's own file"
    os.remove(vp)
    write(mp, kept_m)
    quiet(X.explorer_export, out, dest, force=True, github="tahoe-test/Tahoe100-PseudoManual")
    check("explorer", "--force: a file in the way that the earlier export did not write stops it, before anything is "
          "copied", ok_way and os.path.samefile(vp, os.path.join(dat, *victim.split("/"))), msg or "")
    # copies where hard links cannot be made
    dcp = os.path.join(base, "pub_copy")
    real_link = os.link

    def no_link(*a, **k):
        raise OSError(18, "Invalid cross-device link")
    os.link = no_link
    try:
        rc = quiet(X.explorer_export, out, dcp, github="tahoe-test/Tahoe100-PseudoManual")
    finally:
        os.link = real_link
    copies = [p for p in dm if not os.path.samefile(os.path.join(dat, *p.split("/")),
                                                    os.path.join(dcp, "data", *p.split("/")))
              and sha(os.path.join(dcp, "data", *p.split("/"))) == dm[p][1]]
    check("explorer", "without hard links (another disk): copies, each checked against the stage's sha256",
          not rc["hard_links"] and len(copies) == len(dm) and rc["volumes"]["data"]["copied"] == len(dm) + 1,
          f"{len(copies)} of {len(dm)} copied")
    # several upload lists
    dsm = os.path.join(base, "pub_parts")
    lim = max(4 * max(n for n, _h in dm.values()), sum(n for n, _h in dm.values()) // 3 + 1)
    rp = quiet(X.explorer_export, out, dsm, github="tahoe-test/Tahoe100-PseudoManual", batch_bytes=lim)
    sizes = rp["parts"]["data"]["bytes"]
    check("explorer", "upload lists of at most the limit (here a third of the data): several lists, each within it",
          len(sizes) > 1 and max(sizes) <= lim, f"{len(sizes)} lists, largest {max(sizes):,} of {lim:,} bytes")
    shutil.rmtree(dcp, ignore_errors=True)
    return dsm


@case
def results_readme_explorer(base, out):
    dest = os.path.join(base, "dest_x")
    rec = quiet(X.export, out, dest, github="tahoe-test/Tahoe100-PseudoManual")
    with open(os.path.join(dest, "README.md"), encoding="utf-8") as fh:
        rd = fh.read()
    lo = dict(rec["left_out"])
    want = ["**The explorer**", "https://tahoe-test.github.io/Tahoe100-PseudoManual/",
            "https://github.com/tahoe-test/Tahoe100-PseudoManual-data", "export DEST --explorer"]
    check("explorer", "the results README names the explorer's address and its data repository; the left-out list "
          "says the explorer and tensor/ are published with export --explorer",
          all(w in rd for w in want) and ("explorer" not in os.listdir(out) or "--explorer" in lo.get("explorer", ""))
          and "explorer" in X.LEFT_OUT["tensor"], f"missing {[w for w in want if w not in rd]}")


@case
def publish_end_to_end(base, out, dest):
    """publish.sh against local bare repositories (no network): GitHub's two repositories stand in."""
    git = find_git()
    bash = shutil.which("bash")
    if not (git and bash and dest and os.path.exists(os.path.join(dest, "publish.sh")) and os.name != "nt"):
        check("publish", "(bash, git or an explorer export missing: the end-to-end publish check is skipped)", True)
        return
    e2e = os.path.join(base, "e2e")
    home = os.path.join(e2e, "home")
    os.makedirs(home)
    env = dict(os.environ, HOME=home, GIT_CONFIG_NOSYSTEM="1", TAHOE_PYTHON=sys.executable, TAHOE_GIT=git)
    env.pop("GIT_CONFIG_GLOBAL", None)

    def g(*args, cwd=e2e):
        return subprocess.run([git, *args], cwd=cwd, capture_output=True, text=True, env=env)
    g("config", "--global", "user.name", "tahoemap test")
    g("config", "--global", "user.email", "test@example.invalid")
    site_r, data_r = os.path.join(e2e, "site.git"), os.path.join(e2e, "data.git")
    g("init", "-q", "--bare", site_r)
    g("init", "-q", "--bare", data_r)
    seed = os.path.join(e2e, "seed")
    os.makedirs(seed)
    g("init", "-q", cwd=seed)
    write(os.path.join(seed, "a.txt"), "code\n")
    g("add", "-A", cwd=seed)
    g("commit", "-q", "-m", "code", cwd=seed)
    g("push", "-q", site_r, "HEAD:refs/heads/finalized", cwd=seed)
    g("push", "-q", site_r, "HEAD:refs/heads/results", cwd=seed)
    g("symbolic-ref", "HEAD", "refs/heads/finalized", cwd=site_r)
    before = g("for-each-ref", "--format=%(refname) %(objectname)", cwd=site_r).stdout
    sp = os.path.join(dest, "publish.sh")
    with open(sp, encoding="utf-8") as fh:
        txt = fh.read()
    keep = txt
    txt = txt.replace("https://github.com/tahoe-test/Tahoe100-PseudoManual-data.git", data_r)
    txt = txt.replace("SITE_REMOTE=https://github.com/tahoe-test/Tahoe100-PseudoManual.git", f"SITE_REMOTE={site_r}")
    write(sp, txt)
    try:
        r1 = subprocess.run([bash, sp], cwd=e2e, capture_output=True, text=True, env=env)
        refs1 = g("for-each-ref", "--format=%(refname) %(objectname)", cwd=site_r).stdout
        n_parts = json.load(open(os.path.join(dest, "EXPLORER_EXPORT.json"), encoding="utf-8"))["parts"]["data"][
            "lists"]
        main1 = g("rev-parse", "main", cwd=data_r).stdout.strip()
        count1 = g("rev-list", "--count", "main", cwd=data_r).stdout.strip()
        hosts = g("show", "site:d/hosts.js", cwd=site_r).stdout
        n_site = len([x for x in g("ls-tree", "-r", "--name-only", "site", cwd=site_r).stdout.split("\n") if x])
        n_data = len([x for x in g("ls-tree", "-r", "--name-only", "main", cwd=data_r).stdout.split("\n") if x])
        dm = _vol_manifest(os.path.join(out, "explorer", "data"))
        wm = _vol_manifest(os.path.join(out, "explorer", "web"))
        kept = [ln for ln in before.split("\n") if ln and ln not in refs1.split("\n")]
        check("publish", "publish.sh: the data in parts to the data repository's main, the pages pinned to that "
              "commit on the branch site; results and finalized untouched; nothing else pushed",
              r1.returncode == 0 and not kept and f"/{main1}/" in hosts and count1 == str(n_parts)
              and n_site == len(wm) + 1 and n_data == len(dm) + 1
              and sorted(ln.split()[0] for ln in refs1.split("\n") if ln) == [
                  "refs/heads/finalized", "refs/heads/results", "refs/heads/site"],
              f"exit {r1.returncode}; {n_parts} part(s), main has {count1} commit(s); {n_site} site files, {n_data} "
              f"data files; refs {refs1.split()}; {(r1.stderr or '')[-300:]}")
        r2 = subprocess.run([bash, sp], cwd=e2e, capture_output=True, text=True, env=env)
        count2 = g("rev-list", "--count", "main", cwd=data_r).stdout.strip()
        site2 = g("rev-list", "--count", "site", cwd=site_r).stdout.strip()
        check("publish", "publish.sh again: both branches replaced (one snapshot each: the data branch keeps "
              f"{n_parts} commit(s), the site one)", r2.returncode == 0 and count2 == str(n_parts) and site2 == "1",
              f"exit {r2.returncode}; data main {count2} commits, site {site2}; {(r2.stderr or '')[-300:]}")
    finally:
        write(sp, keep)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=os.environ.get("TAHOE_TEST_DIR", DEFAULT_WORKDIR))
    ap.add_argument("--out", default=None, help="a finished tahoemap output (default WORKDIR/out_seed0)")
    ap.add_argument("--keep", action="store_true", help="keep WORKDIR/export_test after the test")
    a = ap.parse_args()
    src = os.path.abspath(a.out or os.path.join(a.workdir, "out_seed0"))
    if not os.path.exists(os.path.join(src, "stages", "tables.json")):
        sys.exit(f"test_export.py needs a finished tahoemap output: {src} has none (run tests/run_tests.py first, "
                 "or give --out)")
    work = os.path.abspath(a.workdir)
    os.makedirs(work, exist_ok=True)
    t0 = time.time()
    base, out = make_copy(src, work)
    print(f"test_export.py: output {src} (read only), copy {out}")
    res = basic(base, out)
    dest = res[0] if res else os.path.join(base, "dest")
    too_large(base, out)
    refusals(base, out, dest)
    force(base, out, dest)
    with_effects(base, out)
    cli_dest = command_line(base, out)
    git_commit(cli_dest or os.path.join(base, "dest_cli"))
    pub = explorer_export(base, out)
    results_readme_explorer(base, out)
    publish_end_to_end(base, out, pub)
    explorer_command_line(base, out)
    if not a.keep:
        check("cleanup", "DEST copies and their git repository removed (read-only git objects too)", rm_tree(base),
              base)
    n_fail = sum(1 for r in RESULTS if r[2] == "FAIL")
    print(f"\n{len(RESULTS)} checks, {n_fail} failed ({time.time() - t0:.0f} s)")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
