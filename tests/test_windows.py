#!/usr/bin/env python3
"""test_windows.py - the Windows-only behaviour of tahoemap, checked on Linux or macOS by simulation.

    python3 tests/test_windows.py [--workdir DIR]

(On Windows itself it does nothing: it fakes Windows on a POSIX system; there, run_tests.py and test_review.py run
the real thing.)

No data and no network; a few seconds. Each case puts Windows semantics in place for one call - os.name 'nt',
ntpath, os.replace / os.remove refused with PermissionError (a file another program has open), a directory symlink
taken for a junction (os.path.islink False for it), no git on PATH, a keys file written by Windows PowerShell 5.1,
std handles that are not the console - and checks what tahoemap does then:

  files      common.replace_file / remove_file try again, then raise FileInUse naming the file (and remove the .tmp);
             cli.run_stage turns that (and a PermissionError of the ported atlas code's own writes) into a message;
             POSIX keeps os.replace's own behaviour
  stream     a streamed build gets past files of an earlier build that are still in use, and sums into a folder of
             its own; _stop_pool ends each worker with its children (taskkill /T); the job object is Windows-only
  lock       OUT/.pipeline.lock: a second command refuses while the first (or a worker it left running) is alive,
             a stale lock is removed; cli.main refuses before computing anything
  git        common.find_git (TAHOE_GIT, PATH, the Git for Windows / MinGit places); `duplicate --repo` without git
             says so (not "not a git repository"); duplicated_from.json then records the commit and the uncommitted
             changes as unknown; git output is decoded as UTF-8
  links      common.is_link sees a junction; `duplicate` keeps one as a link (os.walk does not descend into it);
             the "destination inside the output" guard is case-insensitive with ntpath
  keys       a keys file / an --only file in UTF-8 with a BOM or UTF-16 (PowerShell's `>`) reads as plain keys and
             names; a malformed key's message names the invisible character; keys.terminal() needs stdin, stdout
             and stderr to be the console on Windows (POSIX: stdin a terminal, as before)
  signals    SIGBREAK (Ctrl-Break) stops a review like Ctrl-C; the console-close handler is Windows-only; a stop file
             of `review stop` is honoured only by the run it names
  review     tools.cache_put is best effort; fake.py raises a signal step with signal.raise_signal on Windows (and
             skips a signal the system lacks); the test harness copies (hard links) where it cannot make symlinks
  query      a closed pipe that Windows reports as EINVAL ends a look-up quietly; the FULL TABLES row of DDL_*.npy
             keeps its ' / DDL_z.npy' out of the path (ntpath.relpath)
  second     `signature --up @FILE` reads a list PowerShell or Notepad wrote (UTF-16 / UTF-8 with a BOM, CRLF); the
  wave       new words print on a cp1252 console; the new output and cache files have valid Windows names; the test
             runner's fresh copy of the reference fixture replaces an earlier copy with read-only files
  https      downloads are verified by Windows itself (truststore), a certificate failure is tried once against
             certifi's roots and is not retried by the reference stage, and its message says what to do
  explorer   long base paths: every file the explorer export writes goes through the extended-length path helper,
             and the record and PUBLISH.md say when paths pass 260 characters; odd drug and line names stay one
             path segment of a hash route, also in a file:// address of a Windows path, and the explorer's own file
             names never hold a name; the folder swap (explorer.tmp -> explorer) with a file held open stops with a
             message naming the folder, and nothing is lost; publish.ps1 pushes only HEAD:refs/heads/main to the data
             repository and HEAD:refs/heads/site to the code repository, checks git's exit code after every call,
             and quotes a path with an apostrophe

Prints PASS / FAIL per check; exit code 1 if anything fails.
"""

import argparse
import contextlib
import errno
import io
import json
import ntpath
import os
import pathlib
import shutil
import signal
import socket
import stat
import subprocess
import sys
import tempfile
import threading
import time
import traceback
import types

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

from tahoemap import cli, common as C, query as Q, stream  # noqa: E402
from tahoemap.review import fake as F, keys as K, runner as R, tools as TL  # noqa: E402

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
            fn(*a, **k)
        except Exception as e:  # noqa: BLE001
            check(fn.__name__, "ran without an exception", False,
                  f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}")
    wrapped.__name__ = fn.__name__
    return wrapped


@contextlib.contextmanager
def patched(obj, **attrs):
    """Set attributes for the block (missing ones are removed again afterwards)."""
    old = {k: getattr(obj, k, _MISSING) for k in attrs}
    for k, v in attrs.items():
        setattr(obj, k, v)
    try:
        yield
    finally:
        for k, v in old.items():
            if v is _MISSING:
                delattr(obj, k)
            else:
                setattr(obj, k, v)


_MISSING = object()


def windows():
    """os.name 'nt' for the block (only what tahoemap's own code reads at call time)."""
    return patched(os, name="nt")


def denied(path, winerror=32):
    e = PermissionError(errno.EACCES, "The process cannot access the file because it is being used by another "
                        "process", path)
    e.winerror = winerror
    return e


# ----------------------------------------------------------------------------- files (W5)
@case
def files(work):
    c = "files"
    d = os.path.join(work, "files")
    os.makedirs(d)
    tmp, dst = os.path.join(d, "x.npy.tmp"), os.path.join(d, "x.npy")
    for p in (tmp, dst):
        with open(p, "w") as fh:
            fh.write(p)
    real_replace, real_remove = os.replace, os.remove
    tries = []

    def held(a, b):
        tries.append(b)
        raise denied(b)
    with windows(), patched(C, REPLACE_WAITS=(0.0, 0.0)), patched(os, replace=held):
        try:
            C.replace_file(tmp, dst)
            got = None
        except C.FileInUse as e:
            got = e
    check(c, "Windows: a replace refused by a file in use is tried again, then FileInUse (a PermissionError) names "
          "the file and the likely holders; the .tmp is removed, the file is unchanged",
          got is not None and isinstance(got, PermissionError) and len(tries) == 3 and dst in str(got)
          and "review run" in str(got) and "Excel" in str(got) and not os.path.exists(tmp)
          and open(dst).read() == dst, f"{len(tries)} tries; {str(got)[:120]}")
    with open(tmp, "w") as fh:
        fh.write("new")
    once = {"n": 0}

    def once_held(a, b):
        once["n"] += 1
        if once["n"] == 1:
            raise denied(b)
        return real_replace(a, b)
    with windows(), patched(C, REPLACE_WAITS=(0.0, 0.0)), patched(os, replace=once_held):
        C.replace_file(tmp, dst)
    check(c, "Windows: a file held for a moment (antivirus, a sync tool) is replaced on a later try",
          open(dst).read() == "new" and not os.path.exists(tmp), once)
    with open(tmp, "w") as fh:
        fh.write("posix")
    try:
        with patched(os, replace=held):
            C.replace_file(tmp, dst)
        raised = None
    except PermissionError as e:
        raised = e
    check(c, "POSIX: replace_file is os.replace itself (the same PermissionError, no retries, the .tmp kept)",
          raised is not None and not isinstance(raised, C.FileInUse) and os.path.exists(tmp), type(raised).__name__)
    with windows(), patched(C, REPLACE_WAITS=(0.0,)), patched(os, remove=lambda p: (_ for _ in ()).throw(denied(p))):
        try:
            C.remove_file(dst)
            got = None
        except C.FileInUse as e:
            got = e
    check(c, "Windows: remove_file (tensor's R.npy with --no-well-tensor) raises FileInUse naming the file",
          got is not None and dst in str(got), str(got)[:100])
    os.remove = real_remove
    # cli.run_stage: the message instead of a traceback (Windows only)
    a = types.SimpleNamespace(out=d)

    def stage_in_use(stage, a):
        raise C.FileInUse(os.path.join(d, "embed", "gene_unit.npy"))

    def atlas_write(stage, a):
        raise PermissionError(errno.EACCES, "Permission denied", os.path.join(d, "atlas", "effects",
                                                                              "drugdose.csv"))
    out = []
    for fn in (stage_in_use, atlas_write):
        with windows(), patched(cli, _run_stage=fn):
            try:
                cli.run_stage("embed", a)
                out.append(None)
            except SystemExit as e:
                out.append(str(e.code))
    with patched(cli, _run_stage=atlas_write):
        try:
            cli.run_stage("effects", a)
            posix = "no error"
        except PermissionError:
            posix = "PermissionError"
        except SystemExit:
            posix = "SystemExit"
    check(c, "cli.run_stage on Windows: FileInUse and a PermissionError of the ported atlas code's writes (Excel "
          "holding drugdose.csv) end the stage with a message naming the file; POSIX: the exception as before",
          out[0] and out[0].startswith("embed: Cannot replace") and "gene_unit.npy" in out[0]
          and out[1] and "Cannot write" in out[1] and "drugdose.csv" in out[1] and posix == "PermissionError",
          [o[:90] if o else o for o in out] + [posix])


# ----------------------------------------------------------------------------- stream (W1)
@case
def stream_build(work):
    c = "stream"
    hf = os.path.join(work, "hf")
    old_dir = os.path.join(hf, stream.IN_FLIGHT, "4242")
    os.makedirs(old_dir)
    loose = os.path.join(hf, stream.IN_FLIGHT, "train-00001-of-03388.parquet.part")
    held = [loose, os.path.join(old_dir, "train-00002-of-03388.parquet")]
    for p in held:
        with open(p, "wb") as fh:
            fh.write(b"x" * 10)
    real_remove = os.remove

    def remove(p, *a, **k):
        if os.path.abspath(p) in held:
            raise denied(p)
        return real_remove(p, *a, **k)

    class Reached(Exception):
        pass

    def discover(*a, **k):
        raise Reached
    args = types.SimpleNamespace(out=os.path.join(work, "atlas"), limit_files=0, workers=1, batch_size=10)
    got = None
    with patched(os, remove=remove), patched(stream, fetch_metadata=lambda d: None), \
            patched(stream.T, discover=discover), patched(shutil, rmtree=lambda p, ignore_errors=False: None), \
            contextlib.redirect_stdout(io.StringIO()):
        try:
            stream.build(args, hf)
        except Reached:
            got = "past the clean-up"
        except PermissionError as e:
            got = f"PermissionError: {e}"
    mine = os.path.join(hf, stream.IN_FLIGHT, str(os.getpid()))
    check(c, "a streamed build gets past files an earlier build still holds (PermissionError on delete) and sums "
          "into a folder of its own (in_flight/<pid>, under the folder's .not_tahoe_input marker)",
          got == "past the clean-up" and os.path.isdir(mine)
          and os.path.exists(os.path.join(hf, stream.IN_FLIGHT, ".not_tahoe_input")), got)
    shutil.rmtree(hf)
    calls = []

    class P:
        def __init__(self, pid):
            self.pid, self.terminated = pid, False

        def terminate(self):
            self.terminated = True

    class Ex:
        _processes = {1: P(1111), 2: P(2222)}

        def shutdown(self, wait=True, cancel_futures=False):
            calls.append(("shutdown", wait, cancel_futures))
    ex = Ex()
    with windows(), patched(stream.subprocess, run=lambda cmd, **k: calls.append(tuple(cmd))):
        stream._stop_pool(ex)
    check(c, "_stop_pool on Windows: each worker ended with the processes it started (taskkill /T /F: its curl)",
          ("taskkill", "/T", "/F", "/PID", "1111") in calls and ("taskkill", "/T", "/F", "/PID", "2222") in calls
          and all(p.terminated for p in ex._processes.values()), calls)
    calls.clear()
    stream._stop_pool(Ex())
    check(c, "_stop_pool on POSIX: terminate() only, as before", not any(x[0] == "taskkill" for x in calls), calls)
    check(c, "the job object (workers end with the build) is set up on Windows only",
          stream._tie_children_to_this_process() is False and not stream._JOB)


# ----------------------------------------------------------------------------- lock (W1, W-REV-4)
@case
def pipeline_lock(work):
    c = "lock"
    out = os.path.join(work, "lock_out")
    os.makedirs(out)
    lp = os.path.join(out, C.PIPELINE_LOCK)
    a = C.PipelineLock(out, "tahoemap run")
    ok, _ = a.acquire()
    rec = json.load(open(lp))
    C.note_children([os.getpid()])
    rec2 = json.load(open(lp))
    a.release()
    check(c, "the lock holds pid, host, process start and command; the build's workers are added (note_children); "
          "release removes it", ok and rec["pid"] == os.getpid() and rec["host"] == socket.gethostname()
          and rec["command"] == "tahoemap run" and [k["pid"] for k in rec2.get("children", [])] == [os.getpid()]
          and not os.path.exists(lp), rec2)
    gone = subprocess.Popen([sys.executable, "-c", "pass"])
    gone.wait()
    live = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    try:
        time.sleep(0.2)
        with open(lp, "w") as fh:
            json.dump({"pid": gone.pid, "host": socket.gethostname(), "started": "x"}, fh)
        ok1, _ = C.PipelineLock(out).acquire()
        C._HELD.clear()
        with open(lp, "w") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x",
                       "process_start": C.proc_start(live.pid)}, fh)
        ok2, why2 = C.PipelineLock(out).acquire()
        with open(lp, "w") as fh:
            json.dump({"pid": gone.pid, "host": socket.gethostname(), "started": "x",
                       "children": [{"pid": live.pid, "process_start": C.proc_start(live.pid)}]}, fh)
        ok3, why3 = C.PipelineLock(out).acquire()
        now = {gone.pid: False, live.pid: True}
        with windows(), patched(C, pid_alive=lambda p: now.get(p, False), proc_start=lambda p: None):
            _alive, why3w = C.lock_state(lp)
        with open(lp, "w") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x"}, fh)
        data = os.path.join(work, "lock_data")
        os.makedirs(data)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                cli.main(["tables", "--out", out, "--data", data])
            refused = None
        except SystemExit as e:
            refused = str(e.code)
    finally:
        live.kill()
        live.wait()
    check(c, "a lock whose process is gone is stale (removed); a live command's lock is refused; a lock whose "
          "command has ended but whose worker still runs is refused, naming the worker and how to end it "
          "(Windows: taskkill /T /F /PID)", ok1 and not ok2 and f"pid {live.pid}" in why2 and not ok3
          and str(live.pid) in why3 and "still run" in why3 and f"taskkill /T /F /PID {live.pid}" in why3w,
          [ok1, ok2, ok3, why2, why3w[-90:]])
    check(c, "cli.main refuses a second computing command on the same output before it computes anything",
          refused and "Another tahoemap command is working" in refused and lp in refused
          and not os.path.exists(os.path.join(out, "stages")), (refused or "")[:120])
    C._HELD.clear()


# ----------------------------------------------------------------------------- git (W4, W-REV-7)
@case
def git(work):
    c = "git"
    pf = os.path.join(work, "Program Files")
    exe = os.path.join(pf, "Git", "cmd", "git.exe")
    os.makedirs(os.path.dirname(exe))
    open(exe, "w").close()
    env = {k: v for k, v in os.environ.items() if k not in ("TAHOE_GIT", "ProgramFiles", "ProgramFiles(x86)",
                                                            "LOCALAPPDATA")}
    with patched(os, environ=dict(env, PATH="")):
        none = C.find_git()
        with windows(), patched(os, environ=dict(env, PATH="", ProgramFiles=pf)):
            win = C.find_git()
        with patched(os, environ=dict(env, PATH="", TAHOE_GIT=r"C:\tools\mingit\cmd\git.exe")):
            envg = C.find_git()
    check(c, "find_git: none on PATH -> None; Windows: Git for Windows under ProgramFiles; TAHOE_GIT first",
          none is None and win == exe and envg == r"C:\tools\mingit\cmd\git.exe", [none, win, envg])
    # duplicate with no git: the right message, and the record says "unknown"
    src = os.path.join(work, "dup_src")
    os.makedirs(os.path.join(src, "stages"))
    with patched(C, find_git=lambda: None), patched(cli, find_git=lambda: None):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                cli.duplicate(src, os.path.join(work, "dup1"), repo=os.path.join(work, "clone"))
            msg = None
        except SystemExit as e:
            msg = str(e.code)
        with contextlib.redirect_stdout(io.StringIO()):
            rec = cli.duplicate(src, os.path.join(work, "dup2"))
    check(c, "duplicate --repo without git: 'git was not found' (TAHOE_GIT), not '<repo> is not a git repository'",
          msg and "git was not found" in msg and "TAHOE_GIT" in msg and "not a git repository" not in msg, msg)
    check(c, "duplicate without git: commit and uncommitted_changes recorded as unknown (None, not False)",
          rec["code"]["commit"] is None and rec["code"]["uncommitted_changes"] is None, rec["code"])
    seen = {}

    def fake_run(cmd, **k):
        seen.update(k)
        return types.SimpleNamespace(returncode=0, stdout=" C:\\tahoe\\Ármin \n")
    with patched(C.subprocess, run=fake_run):
        out = C.git_out("git", "x", "rev-parse", "--show-toplevel")
    check(c, "git output decoded as UTF-8 (not the ANSI code page), undecodable bytes replaced",
          seen.get("encoding") == "utf-8" and seen.get("errors") == "replace" and "text" not in seen
          and out == "C:\\tahoe\\Ármin", seen)
    check(c, "(cp1252, Windows' default for text=True, cannot decode UTF-8 'Á' = C3 81)",
          _cp1252_fails(b"\xc3\x81"))


def _cp1252_fails(b):
    try:
        b.decode("cp1252")
        return False
    except UnicodeDecodeError:
        return True


# ----------------------------------------------------------------------------- links (W7, W-REV-8, W-REV-9)
@case
def links(work):
    c = "links"
    old_atlas = os.path.join(work, "old_atlas", "pseudobulk")
    os.makedirs(old_atlas)
    with open(os.path.join(old_atlas, "group000.npy"), "wb") as fh:
        fh.write(b"\x93NUMPY" + b"0" * 64)
    src = os.path.join(work, "jsrc")
    for d in ("stages", "atlas"):
        os.makedirs(os.path.join(src, d))
    pb = os.path.join(src, "atlas", "pseudobulk")
    os.symlink(old_atlas, pb, target_is_directory=True)      # stands for a junction (mklink /J)
    real_islink = os.path.islink
    junction = {os.path.abspath(pb)}

    def islink(p):                                           # ntpath.islink: False for a junction
        return False if os.path.abspath(p) in junction else real_islink(p)

    def isjunction(p):
        return os.path.abspath(p) in junction
    with patched(os.path, islink=islink, isjunction=isjunction):
        isl = C.is_link(pb)
        dest = os.path.join(work, "jdest")
        with contextlib.redirect_stdout(io.StringIO()):
            rec = cli.duplicate(src, dest)
    dpb = os.path.join(dest, "atlas", "pseudobulk")
    check(c, "is_link: a junction (os.path.islink False) counts as a link", isl)
    check(c, "duplicate keeps a junction as a link: no real folder of the old atlas's files in the copy (os.walk "
          "does not descend into it)", real_islink(dpb) and os.path.realpath(dpb) == os.path.realpath(old_atlas)
          and rec["files"]["symlinks"] == 1 and rec["files"]["hard_linked"] == 0 and rec["files"]["copied"] == 0,
          rec["files"])
    with patched(os.path, isjunction=None):
        delattr(os.path, "isjunction")
        tag = types.SimpleNamespace(st_reparse_tag=0xA0000003, st_mode=stat.S_IFDIR)   # IO_REPARSE_TAG_MOUNT_POINT
        with patched(os, lstat=lambda p: tag):
            posix_old = C.is_link(os.path.join(work, "nowhere"))
            with windows():
                old_py = C.is_link(os.path.join(work, "nowhere"))
    check(c, "is_link without os.path.isjunction (Python 3.10/3.11): on Windows the reparse tag of a mount point; "
          "on POSIX simply False", old_py and not posix_old)
    cases = {(r"c:\tahoe\out\review1", r"C:\tahoe\out"): True, (r"C:\TAHOE\OUT", r"C:\tahoe\out"): True,
             (r"D:\tm\review1", r"C:\tahoe\out"): False, (r"C:\tahoe\out2", r"C:\tahoe\out"): False,
             (r"C:\tahoe", r"C:\tahoe\out"): False}
    got = {k: cli._inside(*k, P=ntpath) for k in cases}
    old_guard = r"c:\tahoe\out\review1".startswith(r"C:\tahoe\out" + "\\")
    check(c, "duplicate's 'destination inside the output' guard: case-insensitive with ntpath (the old startswith "
          "missed c:\\tahoe\\out\\review1 inside C:\\tahoe\\out)", got == cases and not old_guard,
          {f"{a} in {b}": v for (a, b), v in got.items()})


# ----------------------------------------------------------------------------- keys (W-REV-6, W-REV-2)
@case
def keys(work):
    c = "keys"
    key = "sk-ant-fake-1234567890abcdef-KEYW"
    files = {"utf8": key.encode() + b"\n", "utf8-bom": b"\xef\xbb\xbf" + key.encode() + b"\r\n",
             "utf16le-bom (PowerShell 5.1 >)": ("\ufeff" + key + "\r\n").encode("utf-16-le"),
             "utf16be-bom": ("\ufeff" + key + "\n").encode("utf-16-be")}
    got = {}
    for name, data in files.items():
        p = os.path.join(work, f"keys-{len(got)}.txt")
        with open(p, "wb") as fh:
            fh.write(data)
        os.chmod(p, 0o600)
        try:
            pool = K.KeyPool(keys_file=p, env=False, default_chain=False, interactive=False)
            got[name] = [(k.secret == key, k.dead) for k in pool.keys]
        except Exception as e:  # noqa: BLE001
            got[name] = f"{type(e).__name__}: {e}"
    check(c, "a keys file in UTF-8, UTF-8 with a BOM (Notepad, Set-Content -Encoding UTF8) or UTF-16 with a BOM "
          "(Windows PowerShell's > and Out-File): the key as written, alive", all(v == [(True, False)]
                                                                                 for v in got.values()), got)
    p = os.path.join(work, "genes.txt")
    with open(p, "wb") as fh:
        fh.write("\ufeffTP53\r\nMDM2  # a comment\r\n".encode("utf-16-le"))
    p8 = os.path.join(work, "genes8.txt")
    with open(p8, "wb") as fh:
        fh.write(b"\xef\xbb\xbfTP53\nMDM2\n")
    check(c, "--only @FILE with a BOM (UTF-16 or UTF-8): the names without it", R.parse_only("@" + p) ==
          ["TP53", "MDM2"] and R.parse_only("@" + p8) == ["TP53", "MDM2"], [R.parse_only("@" + p)])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        pool = K.KeyPool(env=False, default_chain=False, interactive=False)
        k = pool.add(key + "\u200b", "typed in")
    check(c, "a key with an invisible character is dead (malformed) and the message names the character",
          k.dead and k.reason == K.MALFORMED and "U+200B" in buf.getvalue(), buf.getvalue()[-160:])

    class Std:
        def __init__(self, tty, console):
            self.tty, self.console = tty, console

        def isatty(self):
            return self.tty

        def fileno(self):
            return 0
    console = Std(True, True)
    nul = Std(True, False)            # the C runtime's isatty() is true for NUL; GetConsoleMode fails
    redirected = Std(False, False)
    res = {}
    for name, std in {"all console": (console, console, console),
                      "Start-Process, output redirected": (console, redirected, redirected),
                      "input from NUL": (nul, console, console)}.items():
        with windows(), patched(sys, stdin=std[0], stdout=std[1], stderr=std[2]), \
                patched(K, _win_console=lambda s: s.console):
            res[name] = K.terminal()
        with patched(sys, stdin=std[0], stdout=std[1], stderr=std[2]):
            res[name + " (POSIX)"] = K.terminal()
    check(c, "keys.terminal(): on Windows a prompt only when stdin, stdout and stderr are all the console (a "
          "Start-Process run with its output in files, or input from NUL, pauses instead); POSIX: stdin a terminal",
          res == {"all console": True, "Start-Process, output redirected": False, "input from NUL": False,
                  "all console (POSIX)": True, "Start-Process, output redirected (POSIX)": True,
                  "input from NUL (POSIX)": True}, res)


# ----------------------------------------------------------------------------- signals (W-REV-3, W-REV-4)
@case
def signals(work):
    c = "signals"
    got = []

    class Pool:
        def prompting_here(self):
            return False
    run = types.SimpleNamespace(stop=threading.Event(), pool=Pool(), keys_paused=False,
                                request_stop=lambda reason, sig=None: (got.append((reason, sig)),
                                                                       run.stop.set()))
    sigbreak = signal.SIGUSR1                                 # stands for Windows' SIGBREAK (Ctrl-Break)
    with patched(signal, SIGBREAK=sigbreak), contextlib.redirect_stdout(io.StringIO()):
        old = R._install_signals(run)
        try:
            installed = sigbreak in old
            signal.raise_signal(sigbreak)
            time.sleep(0.05)
            try:
                signal.raise_signal(sigbreak)                  # a second Ctrl-Break: stop at once
                second = "nothing"
            except KeyboardInterrupt:
                second = "KeyboardInterrupt"
        finally:
            R._restore_signals(old)
    check(c, "SIGBREAK (Ctrl-Break) is handled like Ctrl-C: the run is asked to stop; a second one stops at once",
          installed and got and got[0][1] == sigbreak and second == "KeyboardInterrupt", (got, second))
    check(c, "Ctrl-Break's exit code is 149; the console-close handler (CTRL_CLOSE_EVENT) is Windows-only",
          R.EXIT_SIGBREAK == 149 and R._console_close(run) is None)
    d = os.path.join(work, "stopfile")
    os.makedirs(d)
    p = os.path.join(d, R.STOP_FILE)
    with open(p, "w") as fh:
        json.dump({"pid": os.getpid()}, fh)
    mine = R._stop_requested(p)
    left1 = os.path.exists(p)
    with open(p, "w") as fh:
        json.dump({"pid": os.getpid() + 1}, fh)
    other = R._stop_requested(p)
    check(c, "review/.stop: honoured by the run it names (removed); another pid's is stale (removed, ignored)",
          mine and not left1 and not other and not os.path.exists(p), (mine, other))


# ----------------------------------------------------------------------------- review layer (W-REV-11, W-REV-13)
@case
def review_bits(work):
    c = "review"
    ctx = types.SimpleNamespace(cache_dir=os.path.join(work, "cache"))
    with patched(os, replace=lambda a, b: (_ for _ in ()).throw(denied(b))), patched(TL.time, sleep=lambda s: None):
        try:
            ok = TL.cache_put(ctx, "ncbi", "ab1234", {"body": "x"})
            err = None
        except OSError as e:
            ok, err = None, e
    left = [f for _r, _d, fs in os.walk(ctx.cache_dir) for f in fs]
    check(c, "tools.cache_put: a write refused (a reader holds the entry, Windows) is skipped, not an error of the "
          "look-up (which would send the request again, or fail the tool); no .tmp left", ok is False and err is None
          and not left, (ok, err, left))
    fk = F.FakeAPI({})
    import httpx2
    req = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
    raised, killed = [], []
    with windows(), patched(signal, raise_signal=raised.append), patched(os, kill=lambda *a: killed.append(a)), \
            patched(F.time, sleep=lambda s: None):
        fk._answer(req, {}, {"signal": "SIGINT", "error": 400, "message": "x"}, 1, "k")
        fk._answer(req, {}, {"signal": "SIGNOTHERE", "error": 400, "message": "x"}, 2, "k")
    check(c, "fake.py on Windows: a signal step raises it in this process (signal.raise_signal: os.kill would end "
          "it), and a signal the system lacks is no step", raised == [signal.SIGINT] and not killed, (raised, killed))
    sys.path.insert(0, HERE)
    import test_review as TR
    srcd = os.path.join(work, "view_src")
    os.makedirs(os.path.join(srcd, "tables"))
    with open(os.path.join(srcd, "tables", "t.parquet"), "w") as fh:
        fh.write("t")
    with open(os.path.join(srcd, "run.log"), "w") as fh:
        fh.write("log")
    view = os.path.join(work, "view")

    def no_symlink(*a, **k):
        e = OSError(errno.EPERM, "A required privilege is not held by the client")
        e.winerror = 1314
        raise e
    with patched(os, symlink=no_symlink):
        os.makedirs(view)
        for e in ("tables", "run.log"):
            TR.link_entry(os.path.join(srcd, e), os.path.join(view, e))
    t1, t2 = os.path.join(view, "tables", "t.parquet"), os.path.join(view, "run.log")
    check(c, "test_review's view without symlink rights (Windows, no Developer Mode): entries copied as hard links",
          os.path.isfile(t1) and os.path.samefile(t1, os.path.join(srcd, "tables", "t.parquet"))
          and os.path.samefile(t2, os.path.join(srcd, "run.log")) and not os.path.islink(os.path.join(view, "tables")))


# ----------------------------------------------------------------------------- query (WIN-QUERY-1, WIN-QUERY-3)
@case
def query(work):
    c = "query"
    real = sys.stdout

    def closed(*a, **k):
        raise OSError(errno.EINVAL, "Invalid argument")
    import builtins
    try:
        with patched(builtins, print=closed):
            Q._emit(["a line"])
        quiet = sys.stdout is not real
    finally:
        if sys.stdout is not real:
            sys.stdout.close()
        sys.stdout = real
    try:
        with patched(builtins, print=lambda *a, **k: (_ for _ in ()).throw(OSError(errno.ENOSPC, "No space"))):
            Q._emit(["a line"])
        other = "swallowed"
    except OSError:
        other = "raised"
    check(c, "a look-up piped into a reader that quit: Windows' EINVAL ends it quietly like EPIPE; other errors "
          "still raise", quiet and other == "raised", (quiet, other))

    class Proxy:
        path = ntpath

        def __getattr__(self, k):
            return getattr(os, k)
    out = r"C:\tahoe\out"
    o = types.SimpleNamespace(out=out)
    P = []
    with patched(Q, os=Proxy()):
        Q._where(o, P, [["every drug-dose x line", (out + r"\tensor\DDL_lfc.npy", " / DDL_z.npy"), "[12]"]])
    row = next((ln for ln in P if "every drug-dose" in ln), "")
    whole = ntpath.relpath(out + r"\tensor\DDL_lfc.npy / DDL_z.npy", out)
    check(c, "FULL TABLES: the DDL_*.npy row reads 'tensor\\DDL_lfc.npy / DDL_z.npy' with ntpath (relpath of the "
          "whole text turned ' / ' into ' \\ ')", "tensor\\DDL_lfc.npy / DDL_z.npy" in row and " \\ " in whole,
          row.strip())


# ----------------------------------------------------------------------------- explorer (the PC publishes it)
def _fake_export(root):
    """A small explorer output for the export: OUT/stages, OUT/explorer/{web,data} with MANIFEST.tsv files, a stamp
    that is current (run id, assets_sha), and atlas/effects with one array."""
    from tahoemap import explorer as XP
    out = os.path.join(root, "out")
    os.makedirs(os.path.join(out, "stages"))
    with open(os.path.join(out, "stages", "tables.json"), "w", encoding="utf-8") as fh:
        json.dump({"stage": "tables", "version": 1, "finished": "2026-01-01 00:00:00", "info": {}}, fh)
    vols = {"web": {"index.html": "<!DOCTYPE html>\n", ".nojekyll": "", "README.md": "web\n",
                    ".gitattributes": "* -text\n", "d/core.js": "TAHOE_SHARD(\"core\",\"\");\n",
                    "d/hosts.js": "TAHOE_HOSTS({\"data\":[],\"data_dd\":[],\"release\":[],\"run\":\"r\"});\n"},
            "data": {"README.md": "data\n", ".gitattributes": "* -text\n", "probe.js": "TAHOE_PROBE({});\n",
                     **{f"x/00/{c:05d}.js": f"TAHOE_SHARD(\"x/00/{c:05d}\",\"\");\n" for c in range(5)}}}
    import hashlib
    for v, files in vols.items():
        rows = []
        for rel, text in sorted(files.items()):
            pth = os.path.join(out, "explorer", v, *rel.split("/"))
            os.makedirs(os.path.dirname(pth), exist_ok=True)
            with open(pth, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            rows.append(f"{rel}\t{len(text.encode())}\t{hashlib.sha256(text.encode()).hexdigest()}\n")
        with open(os.path.join(out, "explorer", v, "MANIFEST.tsv"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("path\tbytes\tsha256\n" + "".join(rows))
    with open(os.path.join(out, "explorer", "manifest.json"), "w", encoding="utf-8") as fh:
        fh.write("{}")
    os.makedirs(os.path.join(out, "atlas", "effects"))
    with open(os.path.join(out, "atlas", "effects", "DD_lfc.npy"), "wb") as fh:
        fh.write(b"\x93NUMPY")
    info = {"run": XP.run_id(out), "assets_sha": XP.assets_sha(), "complete_ok": True,
            "checks": {"self_check": {"n_problems": 0}}, "site_url": None, "data_url": None}
    with open(os.path.join(out, "stages", "explorer.json"), "w", encoding="utf-8") as fh:
        json.dump({"stage": "explorer", "version": XP.VERSION, "finished": "2026-01-02 00:00:00", "info": info}, fh)
    return out


@case
def explorer(work):
    c = "explorer"
    from tahoemap import export as X, explorer as XP, links as LK
    import urllib.parse
    # long base paths
    long_p = "C:\\tahoe\\" + "x" * 240 + "\\site\\d\\g\\00\\0001.js"
    with patched(os, name="nt", path=ntpath):
        got = X._lp(long_p)
        short = X._lp("C:\\tahoe\\pub\\site\\index.html")
    check(c, "long base paths: a path of 240 characters or more gets the extended-length form (\\\\?\\) on Windows; "
          "a short one stays as it is", got == "\\\\?\\" + long_p and short == "C:\\tahoe\\pub\\site\\index.html",
          got[:20])
    out = _fake_export(work)
    dest = os.path.join(work, "p" * 200, "pub")
    seen = set()

    def rec_lp(pth, always=False):         # records the path; the real one would give it the \\?\ form here
        seen.add(os.path.abspath(pth))
        return pth
    with windows(), patched(X, _lp=rec_lp), contextlib.redirect_stdout(io.StringIO()):
        rec = X.explorer_export(out, dest, github="tahoe-test/Tahoe100-PseudoManual")
    written = [os.path.join(r_, f) for r_, _d, fs in os.walk(dest) for f in fs]
    missed = [w for w in written if os.path.abspath(w) not in seen]
    with open(os.path.join(dest, "PUBLISH.md"), encoding="utf-8") as fh:
        md = fh.read()
    with open(os.path.join(dest, "publish.ps1"), encoding="utf-8") as fh:
        ps1 = fh.read()
    check(c, "an explorer export into a long folder: every file it writes goes through the extended-length path "
          "helper; the record and PUBLISH.md say the paths pass 260 characters; git gets core.longpaths true",
          not missed and rec["long_paths"] and "Long paths" in md and "core.longpaths true" in ps1,
          f"{len(written)} files, {len(missed)} not through _lp: {missed[:2]}")
    # odd names in hash routes
    site = "https://tahoe-test.github.io/Tahoe100-PseudoManual/"
    names = ["Idarubicin (hydrochloride)", "HepG2/C3A", "Doxorubicin #2", "50% inhibitor?", "β-Lapachone",
             "N,N'-Dimethyl", "CON", "a&b=c", "100 µM", "back\\slash", "tab\tname"]
    win_page = pathlib.PureWindowsPath("C:/tahoe/out/explorer/web/index.html").as_uri()
    bad = []
    for n in names:
        for u in (LK.drug(site, n), LK.line(site, n), LK.gene(site, "TRIM72", sub=("line", n))):
            seg = u.rsplit("/", 1)[1]
            frag = urllib.parse.urlsplit(win_page + "#" + u.split("#", 1)[1]).fragment
            if (urllib.parse.unquote(seg) != n or not all(ch.isalnum() and ch.isascii() or ch in "-._~%" for ch in seg)
                    or frag != u.split("#", 1)[1] or frag.count("#")):
                bad.append((n, u))
    ids = [XP.g_id(b) for b in (0, 99, 100, 1040)] + [XP.x_id(c_) for c_ in (0, 16642)] + \
        [XP.p_id(d) for d in (0, 1131)] + [XP.dr_id(i) for i in (0, 378)] + [XP.l_id(49), XP.m_id(234), XP.dg_id(184)]
    odd_ids = [i for i in ids if not all(ch in "abcdefghijklmnopqrstuvwxyz0123456789/" for ch in i)]
    check(c, "odd drug and line names (parentheses, '/', '#', '%', '?', spaces, non-ASCII, a reserved name) stay one "
          "segment of a hash route and decode back, also after a file:// address of a Windows path; the explorer's "
          "file names are numbers only (no name, no case clash on Windows)", not bad and not odd_ids,
          f"bad {bad[:2]}; odd ids {odd_ids[:3]}; e.g. {LK.drug(site, names[0])}")
    # the folder swap with a file held open
    sw = os.path.join(work, "swap")
    os.makedirs(os.path.join(sw, "explorer", "web"))
    os.makedirs(os.path.join(sw, "explorer.tmp", "web"))
    for d_, t in (("explorer", "old"), ("explorer.tmp", "new")):
        with open(os.path.join(sw, d_, "web", "index.html"), "w") as fh:
            fh.write(t)
    real_replace = os.replace
    held = {"src": os.path.join(sw, "explorer"), "n": 0}

    def blocked(a, b):
        if os.path.abspath(a) == held["src"]:
            held["n"] += 1
            raise denied(a)
        return real_replace(a, b)

    def state():
        return {d_: (open(os.path.join(sw, d_, "web", "index.html")).read()
                     if os.path.exists(os.path.join(sw, d_, "web", "index.html")) else None)
                for d_ in ("explorer", "explorer.tmp", "explorer.old")}
    err1 = None
    with windows(), patched(C, REPLACE_WAITS=(0.0, 0.0)), patched(os, replace=blocked):
        try:
            XP.swap(sw, os.path.join(sw, "explorer.tmp"))
        except C.FileInUse as e:
            err1 = str(e)
    s1 = state()
    held["src"] = os.path.join(sw, "explorer.tmp")
    err2 = None
    with windows(), patched(C, REPLACE_WAITS=(0.0, 0.0)), patched(os, replace=blocked):
        try:
            XP.swap(sw, os.path.join(sw, "explorer.tmp"))
        except C.FileInUse as e:
            err2 = str(e)
    s2 = state()
    check(c, "the folder swap with a file held open (Windows): the old explorer held -> it stops with a message "
          "naming the folder, both folders unchanged; the new one held -> it stops, the old explorer moved back in "
          "place and the new one kept in explorer.tmp (nothing lost; OUT/explorer never missing; the stage builds "
          "it again)",
          bool(err1) and os.path.join(sw, "explorer") in err1 and "explorer.old" in err1 and "open" in err1
          and s1 == {"explorer": "old", "explorer.tmp": "new", "explorer.old": None}
          and bool(err2) and s2 == {"explorer": "old", "explorer.tmp": "new", "explorer.old": None},
          f"{s1} / {s2}; {(err1 or '')[:80]}")
    held["src"], held["n"] = os.path.join(sw, "nothing"), 0
    with windows(), patched(C, REPLACE_WAITS=(0.0, 0.0)):
        if s2["explorer"] is None and s2["explorer.old"] == "old":
            real_replace(os.path.join(sw, "explorer.old"), os.path.join(sw, "explorer"))
        XP.swap(sw, os.path.join(sw, "explorer.tmp"))
    check(c, "... and once nothing holds it, the swap completes: the new explorer in place, no explorer.old or "
          "explorer.tmp left", state() == {"explorer": "new", "explorer.tmp": None, "explorer.old": None}, state())
    # publish.ps1: fixed refspecs, exit codes, quoting
    sys.path.insert(0, HERE)
    import test_export as TE
    rec2 = dict(rec, repo_dir="C:\\Users\\O'Brien\\tahoe\\repo", python="C:\\tahoe\\.venv\\Scripts\\python.exe",
                git="C:\\tahoe\\mingit\\cmd\\git.exe")
    ps1 = X.publish_ps1(rec2)
    sh_ = X.publish_sh(rec2)
    ok1, d1 = TE.refspecs_ok(ps1, "Tahoe100-PseudoManual")
    ok2, d2 = TE.refspecs_ok(sh_, "Tahoe100-PseudoManual")
    lines = ps1.splitlines()
    body = [i for i, ln in enumerate(lines) if "& $Git" in ln and "@args" not in ln]
    unchecked = [lines[i] for i in body if not any("$LASTEXITCODE" in x for x in lines[i:i + 2])
                 and "config user.email" not in lines[i]]          # (empty = not set: the next line says so)
    check(c, "publish.ps1 (and publish.sh) push only HEAD:refs/heads/main to the data repository and "
          "HEAD:refs/heads/site to the code repository; never results, finalized or master",
          ok1 and ok2, f"ps1: {d1}; sh: {d2}")
    check(c, "publish.ps1 checks git's exit code after every call (PowerShell does not stop on it), finds a MinGit "
          "that is not on PATH, uses the venv's python.exe, and quotes a path with an apostrophe",
          not unchecked and "Git-Do" in ps1 and "'C:\\tahoe\\mingit\\cmd\\git.exe'" in ps1
          and "'C:\\tahoe\\.venv\\Scripts\\python.exe'" in ps1 and "'C:\\Users\\O''Brien\\tahoe\\repo'" in ps1
          and "$PSScriptRoot" in ps1 and "core.autocrlf false" in ps1, f"unchecked git calls: {unchecked[:2]}")


# ----------------------------------------------------------------------------- the second wave
@case
def second_wave(work):
    """The second wave's inputs and outputs on Windows: a gene list for `signature --up @FILE` written by PowerShell
    (UTF-16 with a BOM, CRLF) or Notepad (UTF-8 with a BOM) reads as the plain list; the new words (the
    neighbouring-well and translation-inhibitor flags, '< 1e-45', µM, ≥, ×) print on a cp1252 console without an
    error, ⚠ and → as '!' and '->'; every new output and cache file is a valid Windows file name, short enough
    under OUT; the fresh copy of the reference fixture (tests/run_tests.py fresh_cache) replaces an earlier copy
    whose files are read-only (a Windows file system refuses to remove those without an error handler)."""
    c = "second wave"
    from tahoemap import query as Q
    want = ["CDKN1A", "MDM2", "BAX"]
    got = {}
    for name, raw in (("utf-16", "\ufeffCDKN1A\r\nMDM2\r\nBAX\r\n".encode("utf-16-le")),
                      ("utf-8-sig", "\ufeffCDKN1A, MDM2,BAX\r\n".encode("utf-8")),
                      ("plain", b"CDKN1A\nMDM2\nBAX")):
        pth = os.path.join(work, f"genes_{name}.txt")
        with open(pth, "wb") as fh:
            fh.write(raw)
        with windows():
            got[name] = Q._gene_list("@" + pth)
    check(c, "signature --up @FILE: a list written by PowerShell (UTF-16, BOM, CRLF) or Notepad (UTF-8 with a BOM) "
          "reads as the plain list", all(v == want for v in got.values()), got)
    words = [C.FLAG_TEXT[k] for k in (C.NB_FLAG, C.NB_TOP, C.NB_CLEARED, C.TL_DD, C.TL_RISE)]
    words += ["⚠ Like a neighbouring well: 60 of its 60 significant genes ...", f"q {C.Q_ZERO}", C.Q_ZERO_TEXT,
              "Darinaparsin 0.5 µM; per-line |z| ≥ 5.90; 1.62× (z +4.1)", "TP53 → CDKN1A  [B]  ⚠ same locus"]

    class Cp1252:
        encoding = "cp1252"
    bad = []
    for w in words:
        t = C.printable(w, Cp1252())
        try:
            t.encode("cp1252")
        except UnicodeEncodeError as e:
            bad.append((w[:40], str(e)[:60]))
            continue
        if ("⚠" in w and "!" not in t) or ("→" in w and "->" not in t):
            bad.append((w[:40], t[:40]))
    check(c, "the new words print on a cp1252 console (⚠ -> '!', → -> '->'; µ, ≥ and × as the code page can)",
          not bad, bad[:3] or f"{len(words)} texts")
    names = ["reference/drug_annotations.parquet", "reference/drug_mechanisms.parquet",
             "reference/drug_classes.parquet", "reference/gene_coords.parquet", "reference/paralogues.parquet",
             "reference/downloads/chembl_drugs.json",
             "reference/downloads/chembl_drugs.json.meta.json", "reference/downloads/compara_human_paralogues.tsv.gz",
             "tables/drug_line_response.parquet", "tables/drugdose_signatures.gmt", "embed/drug_similarity.parquet",
             "direction/gene_tests.parquet", "direction/selectivity.parquet", "graph/modules.gmt",
             "validation/line_controls.csv"]
    reserved = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
    badn = [n for n in names for part in n.split("/")
            if set(part) & set('<>:"\\|?*') or part.endswith((".", " ")) or part.split(".")[0].upper() in reserved]
    longp = [n for n in names if len(n) > 80]
    check(c, "every new output and cache file is a valid Windows name (no reserved character or device name, no "
          "trailing dot or space) and at most 80 characters under OUT", not badn and not longp,
          f"{len(names)} files; bad {badn}; long {longp}")
    from tests import run_tests as RT
    if os.path.isdir(RT.FIXTURES):
        first = RT.fresh_cache(work, 9)
        ro = [os.path.join(first, f) for f in os.listdir(first)]
        for f in ro:
            os.chmod(f, stat.S_IREAD)
        real = os.unlink

        def unlink_win(path, *a, dir_fd=None, **k):       # Windows: a read-only file cannot be removed
            if not os.stat(path, dir_fd=dir_fd).st_mode & stat.S_IWRITE:
                raise PermissionError(errno.EACCES, "Access is denied", path)
            return real(path, *a, dir_fd=dir_fd, **k)
        try:
            with patched(os, unlink=unlink_win, remove=unlink_win):
                again = RT.fresh_cache(work, 9)
            ok = again == first and sorted(os.listdir(again)) == sorted(os.listdir(RT.FIXTURES))
            err = ""
        except OSError as e:
            ok, err = False, f"{type(e).__name__}: {e}"
        check(c, "run_tests.fresh_cache copies the reference fixture afresh over an earlier copy with read-only "
              "files (a Windows file system refuses to remove them)", ok, err or f"{len(ro)} read-only files")


# ----------------------------------------------------------------------------- https (the PC's Ensembl / NCBI failure)
@case
def https(work):
    c = "https"
    import ssl
    import urllib.error
    import urllib.request
    from tahoemap import reference as RF

    class FakeTS:                       # truststore: SSLContext(protocol) -> a context
        made = []

        @staticmethod
        def SSLContext(proto):
            FakeTS.made.append(proto)
            return "ts-context"
    C._SSL.clear()
    with windows(), patched(sys, modules={**sys.modules, "truststore": FakeTS}):
        ctx = C.https_context()
    C._SSL.clear()
    posix = C.https_context()
    C._SSL.clear()
    check(c, "Windows: downloads are verified by Windows itself (truststore's SSLContext); POSIX: Python's default",
          ctx == "ts-context" and FakeTS.made == [ssl.PROTOCOL_TLS_CLIENT] and posix is None, (ctx, posix))

    bad = urllib.error.URLError(ssl.SSLCertVerificationError(1, "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify "
                                                                "failed: self-signed certificate in certificate chain"))
    seen = []

    def opener(ok_with_certifi):
        def fn(req, timeout=None, context=None):
            seen.append(context)
            if context is not None and ok_with_certifi:
                return "response"
            raise bad
        return fn
    with patched(urllib.request, urlopen=opener(True)):
        r1 = C.urlopen("https://ftp.ncbi.nlm.nih.gov/x", 5)
    n1 = len(seen)
    with patched(urllib.request, urlopen=opener(False)):
        try:
            C.urlopen("https://ftp.ensembl.org/x", 5)
            r2 = "no error"
        except urllib.error.URLError as e:
            r2 = e
    check(c, "a certificate that fails verification is tried once against certifi's roots; when that fails too, the "
          "first error is raised", r1 == "response" and n1 == 2 and r2 is bad and len(seen) == 4, (r1, n1, r2))

    calls = []

    def fails():
        calls.append(1)
        raise bad
    with patched(RF.time, sleep=lambda s: calls.append(("sleep", s))):
        res, err = RF._retry(fails, 4, "ensembl")
    check(c, "reference: a certificate failure is not retried (it fails the same way each time) and its message says "
          "what to do", res is None and calls == [1] and "truststore" in err and "CERTIFICATE_VERIFY_FAILED" in err,
          err[:160])


@case
def docs(work):
    """docs/quick-start.md for the PC: git commands work with the portable MinGit that is not on PATH; the disk the
    published explorer needs (the upload's git copies, the previous run's data kept by the hard links) and the data
    repository's growth are said; the pages limit is given with its unit."""
    c = "docs"
    with open(os.path.join(REPO, "docs", "quick-start.md"), encoding="utf-8") as fh:
        qs = fh.read()
    want = {"update with MinGit": '& "C:\\tahoe\\mingit\\cmd\\git.exe" -C C:\\tahoe\\repo pull',
            "git copies": "about 4.5 GB", "kept by the hard links": "until `export --explorer --force` replaces them",
            "repository growth": "**The data repository grows.**", "pages limit unit": "`--pages-max-mb 905` (in MiB",
            "publishing disk row": "| publishing the explorer (optional) |",
            "the new look-ups on Windows": "-m tahoemap similar Dexamethasone 5",
            "a PowerShell gene list": "signature --up @FILE` can be written by PowerShell",
            "the stage order": "build → effects → tensor → reference → tables"}
    miss = [k for k, w in want.items() if w not in qs]
    bare = [ln.strip() for ln in qs.splitlines() if "git -C C:\\tahoe\\repo pull" in ln and "on PATH" not in ln]
    check(c, "quick-start.md: the Windows update uses the MinGit git.exe (git is not on PATH); publishing's disk "
          "and the data repository's growth are said; --pages-max-mb has its unit; the new look-ups in PowerShell "
          "form; the stage order (reference before tables)", not miss and not bare,
          f"missing {miss}; bare git lines {bare[:2]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=None, help="scratch folder (default: a temporary one, removed after)")
    a = ap.parse_args()
    if os.name == "nt":
        print("test_windows.py simulates Windows on Linux or macOS; on Windows run tests\\run_tests.py and "
              "tests\\test_review.py instead")
        return 0
    if a.workdir:
        os.makedirs(a.workdir, exist_ok=True)
    work = tempfile.mkdtemp(prefix="tahoemap_win_", dir=a.workdir)
    t0 = time.time()
    try:
        for fn in (files, stream_build, pipeline_lock, git, links, keys, signals, review_bits, query, second_wave,
                   https, explorer, docs):
            d = os.path.join(work, fn.__name__)
            os.makedirs(d)
            fn(d)
    finally:
        shutil.rmtree(work, ignore_errors=True)
    n_fail = sum(1 for r in RESULTS if r[2] == "FAIL")
    print(f"\ntest_windows.py: {len(RESULTS)} checks, {n_fail} failed, {time.time() - t0:.1f} s")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
