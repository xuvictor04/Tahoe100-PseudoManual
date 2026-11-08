"""common - shared helpers: logging, the output layout, stage stamps, safe writes, index tables."""

import hashlib
import json
import os
import re
import shutil
import socket
import stat
import subprocess
import sys
import time

import numpy as np
import pandas as pd

from . import tlib as T

log = T.log

# ----------------------------------------------------------------------------- output layout
# <out>/atlas      the build and the method-v3 effects (same layout as the old tahoe_atlas.py, so an old atlas folder
#                  can be reused);  <out>/tensor  per-cell-line layer;  <out>/tables  fold-change tables;
# <out>/embed      gene / drug / line vectors;  <out>/relations  gene-gene relations;  <out>/graph  nodal map;
# <out>/reference  public annotations;  <out>/validation;  <out>/vault  Obsidian;  <out>/map  interactive map;
# <out>/stages     one stamp per finished stage.
STAGES = ["build", "effects", "tensor", "tables", "embed", "reference", "relations", "graph", "validate",
          "vault", "map"]


def folder(out, name):
    d = os.path.join(out, name)
    os.makedirs(d, exist_ok=True)
    return d


def mark_output(out):
    """The old scripts index every parquet under the data folder unless the folder holds this marker."""
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, ".not_tahoe_input")
    if not os.path.exists(p):
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("tahoemap output: not Tahoe-100M input data\n")


def stamp_stage(out, stage, version, info=None):
    d = folder(out, "stages")
    rec = {"stage": stage, "version": version, "finished": time.strftime("%Y-%m-%d %H:%M:%S"),
           "info": info or {}}
    tmp = os.path.join(d, stage + ".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1, default=str)
    replace_file(tmp, os.path.join(d, stage + ".json"))


def read_stamp(out, stage):
    p = os.path.join(out, "stages", stage + ".json")
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def clear_stamps_from(out, stage):
    """A stage that runs again makes every later stage out of date."""
    for s in STAGES[STAGES.index(stage):]:
        p = os.path.join(out, "stages", s + ".json")
        if os.path.exists(p):
            os.remove(p)


# ----------------------------------------------------------------------------- files
# Windows: a file that another process has open (without FILE_SHARE_DELETE, as Python, numpy's memmap, pyarrow and
# Excel open files) or memory-mapped, or a read-only one, cannot be replaced or deleted: os.replace / os.remove raise
# PermissionError (WinError 5 or 32), where POSIX always succeeds. Antivirus and sync tools let go within moments.
REPLACE_WAITS = (0.1, 0.2, 0.4, 0.8, 1.5)        # seconds between the tries on Windows (~3 s in all)


class FileInUse(PermissionError):
    """Windows: a file of the output could not be replaced or removed (another program has it open, or it is
    read-only). str() says which file, the likely holders and what to do."""

    def __init__(self, path, cause=None):
        super().__init__(in_use_text(path, cause))
        self.path = path


def in_use_text(path, cause=None, verb="replace"):
    return (f"Cannot {verb} {path}" + (f" ({cause})" if cause else "") + ": another program has it open, and on "
            "Windows a file in use (or memory-mapped) cannot be replaced or deleted. Likely holders: a review run, a "
            "look-up or a Python / Jupyter session reading this output - or the other copy of a duplicate, whose "
            "big arrays are the same files (hard links) -, Excel with one of its CSV files open, or a sync or "
            "antivirus tool; or the file is read-only. Close it and run the same command again (the files written "
            "before are unchanged; the stage is redone).")


def replace_file(tmp, dst):
    """os.replace(tmp, dst). On Windows a file in use cannot be replaced: tried again for ~3 s, then tmp is removed
    and FileInUse (a PermissionError) raised, naming the file. Elsewhere exactly os.replace."""
    if os.name != "nt":
        return os.replace(tmp, dst)
    for w in REPLACE_WAITS + (None,):
        try:
            return os.replace(tmp, dst)
        except PermissionError as e:
            if w is None:
                try:
                    os.remove(tmp)
                except OSError:
                    pass
                raise FileInUse(dst, f"{type(e).__name__}: {e}") from e
            time.sleep(w)


def remove_file(path):
    """os.remove(path), with replace_file's retries and message on Windows."""
    if os.name != "nt":
        return os.remove(path)
    for w in REPLACE_WAITS + (None,):
        try:
            return os.remove(path)
        except PermissionError as e:
            if w is None:
                raise FileInUse(path, f"{type(e).__name__}: {e}") from e
            time.sleep(w)


def retry_io(fn, waits=(0.2, 0.5, 1.0, 2.0)):
    """fn(), tried again after each wait while it raises OSError (a file held for a moment by another program, a
    full disk freed); the last error is raised."""
    for w in waits:
        try:
            return fn()
        except OSError:
            time.sleep(w)
    return fn()


def save_npy(path, arr):
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        np.save(fh, arr)
    replace_file(tmp, path)


def open_memmap(path, shape, dtype):
    return np.lib.format.open_memmap(path, mode="w+", dtype=dtype, shape=tuple(int(s) for s in shape))


def load_npy(path, mmap=True):
    return np.load(path, mmap_mode="r" if mmap else None)


def write_parquet(df, path):
    tmp = path + ".tmp"
    df.to_parquet(tmp, index=False)
    replace_file(tmp, path)


def write_csv(df, path):
    tmp = path + ".tmp"
    df.to_csv(tmp, index=False)
    replace_file(tmp, path)


def write_json(obj, path):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, default=_json_default)
    replace_file(tmp, path)


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)


def read_effects_index(fxd):
    """The index tables of atlas/effects with stable dtypes (dose and plate are strings, as the atlas wrote them)."""
    str_cols = {"sample": str, "plate": str, "dose": str, "drug": str, "well": str, "cell_line_id": str}
    genes = pd.read_csv(os.path.join(fxd, "genes.csv"), dtype={"symbol": str, "label": str, "kind": str})
    wells = pd.read_csv(os.path.join(fxd, "wells.csv"), dtype=str_cols, keep_default_na=False,
                        na_values=[""])
    for c in ("drug", "dose", "plate", "sample", "well"):
        if c in wells:
            wells[c] = wells[c].fillna("").astype(str)
    wells["is_dmso"] = wells["is_dmso"].astype(str).str.lower().isin(["true", "1"])
    for c in ("used_in_drugdose", "unreliable_plate", "position_not_correctable"):
        if c in wells:
            wells[c] = wells[c].astype(str).str.lower().isin(["true", "1"])
    dd = pd.read_csv(os.path.join(fxd, "drugdose.csv"), dtype={"drug": str, "dose": str, "plates": str,
                                                                "wells": str, "flags": str},
                     keep_default_na=False, na_values=[""])
    dd["flags"] = dd["flags"].fillna("").astype(str)
    lines = pd.read_csv(os.path.join(fxd, "lines.csv"), dtype={"cell_line_id": str})
    plates = pd.read_csv(os.path.join(fxd, "plates.csv"), dtype={"plate": str})
    info = {}
    p = os.path.join(os.path.dirname(fxd), "info.json")
    for cand in (os.path.join(fxd, "info.json"), p):
        if os.path.exists(cand):
            with open(cand, encoding="utf-8") as fh:
                info.update(json.load(fh))
    return {"genes": genes, "wells": wells, "drugdose": dd, "lines": lines, "plates": plates, "info": info}


# ----------------------------------------------------------------------------- names
_BAD = re.compile(r'[\\/:*?"<>|#^\[\]]')
_RESERVED = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}


def safe_filename(name, maxlen=120):
    """A file name every OS and Obsidian accept; keeps letters, digits, spaces, parentheses, dots, dashes."""
    s = _BAD.sub("_", str(name)).strip().rstrip(".")
    s = re.sub(r"\s+", " ", s)
    if s.upper().split(".")[0] in _RESERVED:
        s = "_" + s
    return s[:maxlen] or "_"


def stable_seed(*parts):
    """A seed that is the same in every process and on every machine (Python's hash() is salted)."""
    h = hashlib.blake2b("|".join(str(p) for p in parts).encode(), digest_size=8).digest()
    return int.from_bytes(h, "little") % (2 ** 32)


def read_text_file(path):
    """The text of a small file someone wrote by hand (a keys file, an --only list): UTF-8 with or without a BOM, or
    UTF-16 with a BOM (what Windows PowerShell 5.1 writes for `>` and Out-File; Notepad's 'UTF-8 with BOM')."""
    with open(path, "rb") as fh:
        raw = fh.read()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    return raw.decode("utf-8-sig")


# ----------------------------------------------------------------------------- links, git
def is_link(path):
    """A symbolic link or (Windows) a directory junction. os.path.islink is False for a junction - what
    --reuse-atlas makes on Windows without symlink rights (mklink /J) - and os.walk descends into one."""
    if os.path.islink(path):
        return True
    isj = getattr(os.path, "isjunction", None)            # Python 3.12+ (False on POSIX)
    if isj is not None:
        return bool(isj(path))
    if os.name != "nt":
        return False
    try:                                                  # Python 3.10 / 3.11 on Windows
        return getattr(os.lstat(path), "st_reparse_tag", 0) == getattr(stat, "IO_REPARSE_TAG_MOUNT_POINT",
                                                                         0xA0000003)
    except OSError:
        return False


def find_git():
    """git: $TAHOE_GIT, then PATH, then the usual Git for Windows / MinGit places; None when there is none."""
    env = os.environ.get("TAHOE_GIT")
    if env:
        return env
    g = shutil.which("git")
    if g:
        return g
    if os.name == "nt":
        repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        roots = [os.environ.get(v) for v in ("ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA")]
        cands = [os.path.join(r, *p) for r in roots if r for p in (("Git", "cmd", "git.exe"),
                                                                  ("Programs", "Git", "cmd", "git.exe"))]
        cands.append(os.path.join(os.path.dirname(repo), "mingit", "cmd", "git.exe"))   # a MinGit next to the repo
        for c in cands:
            if os.path.isfile(c):
                return c
    return None


GIT_MISSING = ("git was not found (it is not on PATH): put the folder holding git.exe on PATH (for a portable MinGit "
               "its cmd folder), or set TAHOE_GIT to git.exe")


def git_out(git, repo, *args, timeout=60):
    """stdout of `git -C repo ARGS` (decoded as UTF-8, as git writes it), or None when git is None, cannot run, or
    fails."""
    if not git:
        return None
    try:
        r = subprocess.run([git, "-C", repo, *args], capture_output=True, encoding="utf-8", errors="replace",
                           timeout=timeout)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


# ----------------------------------------------------------------------------- processes and lock files
def proc_start(pid):
    """The start time (epoch seconds) of process pid, where it can be told (psutil, Linux /proc, Windows); else
    None."""
    try:
        import psutil
        return float(psutil.Process(pid).create_time())
    except Exception:  # noqa: BLE001  (not installed, no such process, no access)
        pass
    if sys.platform.startswith("linux"):
        try:
            with open(f"/proc/{pid}/stat", encoding="utf-8") as fh:
                ticks = int(fh.read().rsplit(")", 1)[1].split()[19])
            with open("/proc/stat", encoding="utf-8") as fh:
                btime = next(int(x.split()[1]) for x in fh if x.startswith("btime"))
            return round(btime + ticks / os.sysconf("SC_CLK_TCK"), 2)
        except (OSError, ValueError, IndexError, StopIteration):
            return None
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes
            k32 = ctypes.WinDLL("kernel32", use_last_error=True)
            k32.OpenProcess.restype = wintypes.HANDLE
            k32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            k32.GetProcessTimes.argtypes = [wintypes.HANDLE] + [ctypes.POINTER(wintypes.FILETIME)] * 4
            k32.CloseHandle.argtypes = [wintypes.HANDLE]
            h = k32.OpenProcess(0x1000, False, pid)                     # PROCESS_QUERY_LIMITED_INFORMATION
            if not h:
                return None
            try:
                ft = [wintypes.FILETIME() for _ in range(4)]
                if not k32.GetProcessTimes(h, *(ctypes.byref(f) for f in ft)):
                    return None
                t = (ft[0].dwHighDateTime << 32) | ft[0].dwLowDateTime    # 100-ns ticks since 1601
                return round(t / 1e7 - 11644473600.0, 2)
            finally:
                k32.CloseHandle(h)
        except Exception:  # noqa: BLE001
            return None
    return None


def pid_alive(pid):
    """False when process pid is certainly gone (POSIX: kill 0; Windows: OpenProcess / GetExitCodeProcess, or
    psutil when installed); True when it runs or cannot be told."""
    if pid <= 0:
        return False
    if os.name == "posix":
        try:
            os.kill(pid, 0)
            return True
        except ProcessLookupError:
            return False
        except OSError:                                 # PermissionError: it exists (another user's)
            return True
    try:
        import psutil
        return bool(psutil.pid_exists(pid))
    except ImportError:
        pass
    try:
        import ctypes
        from ctypes import wintypes
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k32.OpenProcess.restype = wintypes.HANDLE
        k32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        k32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
        k32.CloseHandle.argtypes = [wintypes.HANDLE]
        h = k32.OpenProcess(0x1000, False, pid)                         # PROCESS_QUERY_LIMITED_INFORMATION
        if not h:
            return ctypes.get_last_error() == 5                         # ERROR_ACCESS_DENIED: it exists
        try:
            code = wintypes.DWORD()
            if not k32.GetExitCodeProcess(h, ctypes.byref(code)):
                return True
            return code.value == 259                                    # STILL_ACTIVE
        finally:
            k32.CloseHandle(h)
    except Exception:  # noqa: BLE001  (cannot tell: assume it runs; the message names the lock file)
        return True


def _same_process(pid, t0):
    """False when pid now belongs to a process that started at another time than t0 (both known)."""
    t1 = proc_start(pid)
    return not (isinstance(t0, (int, float)) and t1 is not None and abs(t1 - t0) > 2.0)


def lock_state(path):
    """(alive, description) of a lock file (review/.run.lock, OUT/.pipeline.lock): alive unless its process - and
    every worker process it lists under "children" - is certainly gone (or its pid now belongs to a younger
    process)."""
    try:
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
        pid = int(rec.get("pid"))
    except (OSError, ValueError, TypeError, AttributeError):
        return False, "unreadable lock"
    host = rec.get("host")
    who = f"pid {pid}" + (f" on {host}" if host else "") + (f", started {rec['started']}" if rec.get("started") else "")
    if host and host != socket.gethostname():
        return True, who + " (another computer: its process cannot be checked from here)"
    if pid != os.getpid() and pid_alive(pid):
        if _same_process(pid, rec.get("process_start")):
            return True, who
        who += " (that pid is now another process)"
    kids = []
    for c in rec.get("children") or []:
        try:
            cp = int(c.get("pid"))
        except (TypeError, ValueError, AttributeError):
            continue
        if cp != os.getpid() and pid_alive(cp) and _same_process(cp, c.get("process_start")):
            kids.append(str(cp))
    if kids:
        return True, (who + f"; it has ended, but its worker process(es) {', '.join(kids)} still run: stop them "
                      "first (" + " and ".join(("taskkill /T /F /PID " if os.name == "nt" else "kill ") + k
                                               for k in kids) + ")")
    return False, who


PIPELINE_LOCK = ".pipeline.lock"           # in OUT, while a pipeline command (run or a stage) computes there
_HELD = []                                 # the PipelineLock(s) this process holds (note_children adds to them)


class PipelineLock:
    """OUT/.pipeline.lock: one computing pipeline command per output folder at a time. It holds the pid, the host,
    the start time and the command, and the build's worker processes (note_children): a second command refuses while
    the first - or a worker of it that an abrupt end left running - is alive. A stale lock is removed."""

    def __init__(self, out, command=""):
        self.path = os.path.join(out, PIPELINE_LOCK)
        self.rec = {"pid": os.getpid(), "host": socket.gethostname(),
                    "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "process_start": proc_start(os.getpid()),
                    "command": command}
        self.held = False

    def acquire(self):
        """(True, '') or (False, a description of the command holding the lock)."""
        for _ in range(2):
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            except FileExistsError:
                alive, who = lock_state(self.path)
                if alive:
                    return False, who
                try:
                    os.remove(self.path)                # stale: its process (and its workers) are gone
                except OSError:
                    pass
                continue
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(self.rec, fh)
            self.held = True
            _HELD.append(self)
            return True, ""
        return False, f"cannot create {self.path}"

    def add_children(self, pids):
        if not self.held:
            return
        kids = {c["pid"]: c for c in self.rec.get("children", [])}
        for p in pids:
            kids.setdefault(int(p), {"pid": int(p), "process_start": proc_start(int(p))})
        self.rec["children"] = list(kids.values())
        with open(self.path, "w", encoding="utf-8") as fh:
            json.dump(self.rec, fh)

    def release(self):
        if self.held:
            try:
                os.remove(self.path)
            except OSError:
                pass
            self.held = False
            if self in _HELD:
                _HELD.remove(self)


def note_children(pids):
    """The build's worker processes, recorded in the pipeline lock this process holds."""
    for lk in list(_HELD):
        try:
            lk.add_children(pids)
        except OSError:
            pass
