#!/usr/bin/env python3
"""test_export.py - `tahoemap export` (tahoemap/export.py): the shareable results of a finished output, ready for a
GitHub branch.

    python3 tests/test_export.py [--out FINISHED_OUTPUT] [--workdir DIR] [--keep]

Needs a finished tahoemap output folder: --out, else the one tests/run_tests.py leaves in --workdir/out_seed0
(default $TAHOE_TEST_DIR, else /tmp/tahoemap_test; on Windows tahoemap_test in the temp folder). That folder is only
read: the test copies it to DIR/export_test/out (without the big per-well and per-line arrays, which get small
stand-ins) and adds what an export must leave alone - review caches, key state, lock and stop files, temporary files,
raw reference downloads, hf/ - and a few literature-review results it must copy. No network; a few seconds.

Checks: the folders and files copied and the ones never copied; --include; MANIFEST.tsv (every file, bytes and
sha256, nothing else in DEST); .gitattributes ('* -text'); README.md (folders, provenance, stage states, what was
left out and why, the files too large for GitHub); a file over the limit skipped and listed (a 96 MiB sparse file at
the default 95 MiB, and a lowered --max-file-mb); a DEST inside OUT (or holding OUT) refused, also with other letter
case on a case-insensitive system; a non-empty DEST refused without --force; --force: unchanged files kept, files
the source no longer has removed, the user's own files (a .git folder, notes) left alone, a file in the way that the
manifest does not list stops it before anything is copied; --with-effects; a live pipeline lock refused; the command
line (python -m tahoemap export ...) and its next steps; and, when git is installed, a commit of DEST that stores a
CRLF file byte for byte with core.autocrlf=true.

Prints PASS / FAIL per check; exit code 1 if anything fails.
"""

import argparse
import hashlib
import json
import os
import shutil
import socket
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
REVIEW = ["review/reviews/gene/TP53.json", "review/notes/gene/TP53.md", "review/history/gene/TP53/20261109-0001.jsonl",
          "review/ledger.jsonl", "review/queue.parquet", "review/connections.parquet", "review/findings.parquet",
          "review/review.log"]


def make_copy(src, work):
    """OUT for the test: the finished output without its big arrays, plus the files an export must leave alone."""
    base = os.path.join(work, "export_test")
    shutil.rmtree(base, ignore_errors=True)
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
    must = [m for m in must if os.path.exists(os.path.join(out, *m.split("/"))) or m in X.WRITTEN
            or m == "RUN_REPORT.md"]
    miss = [m for m in must if m not in got]
    check("basic", "the shareable results are copied (vault, map, tables, validation, graph, relations, embed, "
          "reference tables, stages, run files, review results, --include)", not miss, f"missing {miss}")
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
    want = ["## What each folder holds", "`vault`", "`map`", "Obsidian", "gene_map.html", "## Provenance",
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
def git_commit(dest):
    git = shutil.which("git")
    if not git:
        check("git", "(git not installed: the commit check is skipped)", True)
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
    if not a.keep:
        shutil.rmtree(base, ignore_errors=True)
    n_fail = sum(1 for r in RESULTS if r[2] == "FAIL")
    print(f"\n{len(RESULTS)} checks, {n_fail} failed ({time.time() - t0:.0f} s)")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
