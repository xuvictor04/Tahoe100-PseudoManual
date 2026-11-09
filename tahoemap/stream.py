"""stream - the build driver, and the build without the 430 GB download: every expression file is fetched from
Hugging Face, summed into its plate's pseudobulk, and deleted. Disk need: the pseudobulk only (~17 GB), plus ~1 GB of
files in flight.

The summing is the ported atlas_core._build_group itself, unchanged: in each worker process the module's
`pq.ParquetFile` is swapped for a shim that downloads the requested file (and the next ones of the same plate, in the
background) before opening it, and deletes the files read before (on Windows a file still open is deleted at a
later call, once released). The output is the same pseudobulk folder a local build writes, so every later stage is
the same. Files are assigned to plates from their parquet footers (a file can span two plates; profiles are keyed by
well and line and summed across groups by the effects step, as in the atlas).

A stopped build keeps its finished plates and continues where it stopped (a streamed one keeps streaming: cli
switches to --stream when <out>/hf/file_plates.json is there). A build never deletes finished plates because fewer
files are found, and a local build stops when the download is incomplete (unless --allow-partial).

Windows: a process that is ended from outside (Stop-Process, taskkill without /T, Task Manager) does not take its
child processes with it, so the build puts itself in a job object that ends every process of the build - the
workers and their curl downloads - with it (_tie_children_to_this_process). Each streamed build sums its files in a
folder of its own (<out>/hf/in_flight/<pid>), and what an earlier build left there is removed as far as it can be.
"""

import glob
import json
import os
import re
import shutil
import subprocess
import threading
import time
import types
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import multiprocessing as mp

import pandas as pd
import pyarrow.parquet as _pq

from . import atlas_core as A
from . import tlib as T
from .common import log, mark_output, note_children, urlopen

REPO = "https://huggingface.co/datasets/tahoebio/Tahoe-100M/resolve/main/"
API = "https://huggingface.co/api/datasets/tahoebio/Tahoe-100M/tree/main/data"
META = ("gene_metadata", "sample_metadata", "cell_line_metadata", "drug_metadata")
PREFETCH = 2
FILE_PLATES = "file_plates.json"   # in <out>/hf: the plate of each streamed file (there = a streamed build)
IN_FLIGHT = "in_flight"            # in <out>/hf: the files being summed; never indexed as data
DELETE_TRIES = 3                   # failed deletions of a finished file before a warning (Windows: still open)
OF_RE = re.compile(r"-(\d+)-of-(\d+)\.parquet$")   # Tahoe's file naming: train-00012-of-03388.parquet


def fetch(url, dest, tries=6):
    """Download with curl (follows redirects, honours HTTPS_PROXY and the system CA store); verify it opens."""
    err = ""
    for k in range(tries):
        r = subprocess.run(["curl", "-sSfL", "--retry", "3", "-m", "1800", "-o", dest + ".part", url],
                           capture_output=True, text=True)
        if r.returncode == 0 and os.path.exists(dest + ".part") and os.path.getsize(dest + ".part") > 1000:
            os.replace(dest + ".part", dest)
            if not dest.endswith(".parquet"):
                return dest
            try:
                _pq.ParquetFile(dest).metadata
                return dest
            except Exception as e:  # noqa: BLE001
                err = str(e)
        else:
            err = r.stderr.strip()
        time.sleep(2 ** k)
    raise RuntimeError(f"download failed after {tries} tries: {url}: {err}")


def list_files():
    """Names of the expression files, from the Hugging Face API (paged); fallback: the known 3,388-file naming."""
    names, url = [], API
    try:
        while url:
            with urlopen(url, 60) as resp:
                names += [d["path"] for d in json.load(resp) if d.get("path", "").endswith(".parquet")]
                link = resp.headers.get("Link", "")
            m = re.search(r'<([^>]+)>;\s*rel="next"', link)
            url = m.group(1) if m else None
    except Exception as e:  # noqa: BLE001
        log(f"  could not list the files ({e}); using the known naming of 3,388 files")
        names = []
    if not names:
        names = [f"data/train-{i:05d}-of-03388.parquet" for i in range(3388)]
    return sorted(set(names))


class RangeFile:
    """A read-only, seekable file over HTTP range requests (enough for pyarrow to read a parquet footer)."""

    def __init__(self, url, tail=1 << 16):
        self.url, self.pos, self.closed = url, 0, False
        data, total = self._get(f"bytes=-{tail}")
        self.size = total
        self.cache_start, self.cache = total - len(data), data

    def _get(self, rng):
        import urllib.request
        req = urllib.request.Request(self.url, headers={"Range": rng})
        with urlopen(req, 120) as r:
            data = r.read()
            cr = r.headers.get("Content-Range", "")
        total = int(cr.rsplit("/", 1)[1]) if "/" in cr else len(data)
        return data, total

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.size - self.pos
        n = max(0, min(n, self.size - self.pos))
        if not n:
            return b""
        a, b = self.pos, self.pos + n
        if a >= self.cache_start:
            out = self.cache[a - self.cache_start:b - self.cache_start]
        else:
            out, _ = self._get(f"bytes={a}-{b - 1}")
        self.pos += len(out)
        return out

    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.size + off)
        return self.pos

    def tell(self):
        return self.pos

    def readable(self):
        return True

    def seekable(self):
        return True

    def close(self):
        self.closed = True


def plate_of(rel):
    err = None
    for k in range(5):
        try:
            pf = _pq.ParquetFile(RangeFile(REPO + rel))
            md = pf.metadata
            ci = md.schema.to_arrow_schema().names.index("plate")
            vals = set()
            for g in range(md.num_row_groups):
                s = md.row_group(g).column(ci).statistics
                if s is None or not s.has_min_max:
                    b = next(pf.iter_batches(batch_size=1, columns=["plate"]))
                    return rel, str(b.column(0)[0].as_py())
                vals.update([s.min, s.max])
            v = sorted(vals)[0]
            return rel, v.decode() if isinstance(v, bytes) else str(v)
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 ** k)
    raise RuntimeError(f"could not read the plate of {rel}: {err}")


# ----------------------------------------------------------------------------- worker side
_W = {}


def _init_worker(next_of, tmp):
    _W.update(next_of=next_of, tmp=tmp, pool=ThreadPoolExecutor(PREFETCH), futs={}, prev=None, to_delete=[],
              lock=threading.Lock())
    shim = types.ModuleType("pq_shim")
    for k in dir(_pq):
        if not k.startswith("__"):
            setattr(shim, k, getattr(_pq, k))
    shim.ParquetFile = _open_streamed
    A.pq = shim                      # _build_group calls pq.ParquetFile(f) once per file, in order


def _local(url):
    return os.path.join(_W["tmp"], re.sub(r"[^\w.-]+", "_", url.rsplit("/", 1)[-1]))


def _want(url):
    if url and url not in _W["futs"]:
        _W["futs"][url] = _W["pool"].submit(fetch, url, _local(url))


def _open_streamed(url, *a, **kw):
    if not str(url).startswith("http"):
        return _pq.ParquetFile(url, *a, **kw)
    _want(url)
    nxt = url
    for _ in range(PREFETCH):
        nxt = _W["next_of"].get(nxt)
        _want(nxt)
    path = _W["futs"].pop(url).result()
    pf = _pq.ParquetFile(path, *a, **kw)
    prev, _W["prev"] = _W["prev"], path
    if prev:
        _W["to_delete"].append([prev, 0])
    _sweep()
    return pf


def _sweep():
    """Delete the files already read. On Windows the file read just before is often still open (the caller still holds
    its ParquetFile): it is kept on the list and deleted at a later call, once released."""
    keep = []
    for item in _W["to_delete"]:
        try:
            if os.path.exists(item[0]):
                os.remove(item[0])
        except OSError as e:
            item[1] += 1
            if item[1] == DELETE_TRIES:
                log(f"  could not delete {item[0]} yet ({e}); trying again with the next files")
            keep.append(item)
    _W["to_delete"] = keep


# ----------------------------------------------------------------------------- driver
def fetch_metadata(meta_dir):
    os.makedirs(meta_dir, exist_ok=True)
    for t in META:
        p = os.path.join(meta_dir, t + ".parquet")
        if not os.path.exists(p) or os.path.getsize(p) < 1000:
            log(f"  fetching metadata/{t}.parquet")
            fetch(f"{REPO}metadata/{t}.parquet", p)


def clear_in_flight(root):
    """Remove what earlier builds left in <out>/hf/in_flight (their own subfolders, or loose files of older
    versions). A file still in use - on Windows, a process of an earlier build that is still running - stays; it is
    named, never an error. Returns the number of entries left."""
    left = []
    for e in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        p = os.path.join(root, e)
        if e == ".not_tahoe_input":
            continue
        if os.path.isdir(p) and not os.path.islink(p):
            shutil.rmtree(p, ignore_errors=True)
            if os.path.exists(p):
                left.append(p)
        else:
            try:
                os.remove(p)
            except OSError:
                left.append(p)
    if left:
        log(f"  {len(left)} file(s) or folder(s) of an earlier build in {root} are still in use and stay there (is a "
            "process of that build still running?): " + ", ".join(os.path.basename(x) for x in left[:5]))
    return len(left)


def build(args, hf_dir):
    """args as for atlas_core.cmd_build (out = <OUT>/atlas). hf_dir holds metadata/ and the plate map cache."""
    D = A.dirs(args.out)
    fetch_metadata(os.path.join(hf_dir, "metadata"))
    root = os.path.join(hf_dir, IN_FLIGHT)
    os.makedirs(root, exist_ok=True)
    mark_output(root)                                        # the files in flight are never indexed as the data
    clear_in_flight(root)
    tmp = os.path.join(root, str(os.getpid()))              # this build's own: a file an earlier build still holds
    os.makedirs(tmp, exist_ok=True)                          # never blocks it or collides with it
    idx = T.discover(hf_dir, args.out, refresh=True)
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    G = int(gm["token_id"].max()) + 1
    names = list_files()
    rels = names[:args.limit_files] if args.limit_files else names
    pmap_path = os.path.join(hf_dir, FILE_PLATES)
    pmap = json.load(open(pmap_path, encoding="utf-8")) if os.path.exists(pmap_path) else {}
    todo = [r for r in rels if r not in pmap]
    if todo:
        log(f"Finding the plate of {len(todo)} files from their footers ...")
        with ThreadPoolExecutor(24) as ex:
            for r, p in ex.map(plate_of, todo):
                pmap[r] = p
        with open(pmap_path, "w", encoding="utf-8") as fh:
            json.dump(pmap, fh, indent=0)
    by_plate = defaultdict(list)
    for r in rels:
        by_plate[pmap[r]].append(REPO + r)
    plates = sorted(by_plate, key=lambda p: (len(p), p))
    next_of = {}
    for p in plates:
        for a, b in zip(by_plate[p], by_plate[p][1:]):
            next_of[a] = b
    jobs = [(gid, p, by_plate[p], G, D["pb"], args.batch_size) for gid, p in enumerate(plates)]
    check_extra_groups(D["pb"], len(jobs), "the Hugging Face file list" +
                      (f" (--limit-files {args.limit_files})" if args.limit_files else ""))
    workers = min(args.workers or T.auto_workers(), len(jobs))
    per_worker = 5000 * G * 4 / 1e9 * 1.3 + 1.0
    mem = T.mem_available_gb()
    if mem:
        workers = max(1, min(workers, int(mem / per_worker)))
    log(f"{len(rels)} files on {len(plates)} plates, streamed from Hugging Face -> one group per plate, "
        f"{workers} at a time (~{per_worker:.1f} GB each)")
    run_groups(jobs, workers, initializer=_init_worker, initargs=(next_of, tmp), streamed=True)
    left = []
    for f in glob.glob(os.path.join(tmp, "*")):              # the last file of each plate
        try:
            os.remove(f)
        except OSError:
            left.append(f)
    if left:
        log(f"  {len(left)} finished file(s) could not be deleted from {tmp}; delete them by hand")
    else:
        try:
            os.rmdir(tmp)
        except OSError:
            pass
    finish_build(args, idx, len(jobs), "streamed from Hugging Face", n_files=len(rels), expected=len(names))


def check_extra_groups(pb, n_groups, source):
    """Plate groups numbered n_groups and above belong to an earlier build that found more plates. The build stops
    rather than delete them: files that are missing now (an unfinished download, a folder of files in flight) must
    never cost finished plates."""
    extra = [f for f in glob.glob(os.path.join(pb, "group*_profiles.csv"))
             if int(re.search(r"group(\d+)_", os.path.basename(f)).group(1)) >= n_groups]
    if extra:
        raise SystemExit(f"build: {pb} holds {len(extra)} more plate groups than the {n_groups} plates found in "
                         f"{source}. Nothing was deleted. If those files are complete and the earlier build should "
                         f"go, delete {pb} (or use a new --out) and run again.")


def expected_files(exprs):
    """(total, missing): Tahoe names its expression files train-NNNNN-of-TOTAL.parquet; (None, 0) without such names."""
    seen = defaultdict(set)
    for f in exprs:
        m = OF_RE.search(os.path.basename(f))
        if m:
            seen[int(m.group(2))].add(int(m.group(1)))
    if not seen:
        return None, 0
    total = max(seen)
    return total, total - len(seen[total])


_JOB = []                       # Windows: the job object of this process (its handle is never closed)


def _tie_children_to_this_process():
    """Windows: put this process in a job object with JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE. Its handle closes only
    when this process ends - however it ends - and then every process of the job ends too: the build's workers
    (multiprocessing starts them with no job of their own, and a worker notices a vanished parent only between
    plates) and their curl downloads. Elsewhere, or when it cannot be done, nothing (False): Ctrl-C reaches every
    process of the console, `tahoe stop` the process group."""
    if os.name != "nt":
        return False
    if _JOB:
        return True
    try:
        import ctypes
        from ctypes import wintypes

        class Basic(ctypes.Structure):
            _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64), ("PerJobUserTimeLimit", ctypes.c_int64),
                        ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                        ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                        ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD),
                        ("SchedulingClass", wintypes.DWORD)]

        class Extended(ctypes.Structure):
            _fields_ = [("BasicLimitInformation", Basic), ("IoInfo", ctypes.c_uint64 * 6),
                        ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                        ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k32.CreateJobObjectW.restype = wintypes.HANDLE
        k32.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
        k32.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
        k32.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
        k32.GetCurrentProcess.restype = wintypes.HANDLE
        k32.CloseHandle.argtypes = [wintypes.HANDLE]
        job = k32.CreateJobObjectW(None, None)
        if not job:
            raise OSError(ctypes.get_last_error(), "CreateJobObject failed")
        info = Extended()
        info.BasicLimitInformation.LimitFlags = 0x2000                    # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        if not (k32.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info))   # ExtendedLimit
                and k32.AssignProcessToJobObject(job, k32.GetCurrentProcess())):
            err = ctypes.get_last_error()
            k32.CloseHandle(job)
            raise OSError(err, "the job object could not be set up")
        _JOB.append(job)               # never closed by us: closing it would end this process too
        return True
    except Exception as e:  # noqa: BLE001
        log(f"  note: the worker processes could not be tied to this one ({e}): if you end this run with "
            "Stop-Process or Task Manager, end its python.exe workers too (taskkill /T /F /PID <pid> ends a process "
            "and the ones it started)")
        return False


def run_groups(jobs, workers, initializer=None, initargs=(), streamed=False):
    """Run atlas_core._build_group (verbatim) for every plate group, biggest first, `workers` at a time.

    A process pool that loses a worker (most often: killed for lack of memory) makes multiprocessing.Pool wait
    forever; this executor raises instead. A plate that fails is logged at once and the build stops; finished plates
    are kept for the next run (the plates still being summed are redone). The workers' pids go into the pipeline lock
    (common.note_children), so a later command on this output waits while one of them still runs."""
    from concurrent.futures import ProcessPoolExecutor, as_completed
    from concurrent.futures.process import BrokenProcessPool
    again = "run again" + (" (it continues streaming; or with --stream)" if streamed else "")
    order = sorted(jobs, key=lambda j: -len(j[2]))            # biggest plates first: a shorter tail
    t0, done = time.time(), 0
    _tie_children_to_this_process()
    ex = ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn"), initializer=initializer,
                             initargs=initargs)
    try:
        futs = {ex.submit(A._build_group, j): j[1] for j in order}
        note_children([p.pid for p in list((getattr(ex, "_processes", None) or {}).values()) if p.pid])
        for fu in as_completed(futs):
            try:
                _gid, name, _nc, reused = fu.result()
            except BrokenProcessPool:
                raise
            except Exception as e:  # noqa: BLE001 - any plate's failure stops the build now, not after the others
                msg = f"{type(e).__name__}: {e}"
                log(f"  plate {futs[fu]} FAILED: {msg}")
                _stop_pool(ex)
                raise SystemExit(f"build: plate {futs[fu]} failed ({msg}). The {done} finished plates are kept: "
                                 f"fix the cause and {again} to continue.")
            done += 1
            log(f"  {name} {'already built' if reused else 'done'} ({done}/{len(jobs)} plates, "
                f"{(time.time() - t0) / 60:.1f} min)")
    except BrokenProcessPool:
        _stop_pool(ex)
        raise SystemExit(f"build: a worker process died (most often it ran out of memory with {workers} plates at "
                         f"a time). The {done} finished plates are kept: run again with --workers "
                         f"{max(1, workers - 1)}" + (" --stream." if streamed else "."))
    except BaseException:
        _stop_pool(ex)
        raise
    ex.shutdown(wait=True)


def _stop_pool(ex):
    """Cancel the queued plates and end the ones running (their partial sums are never written). On Windows each
    worker is ended with the processes it started (taskkill /T: its curl download), which terminate() leaves."""
    ex.shutdown(wait=False, cancel_futures=True)
    for p in list((getattr(ex, "_processes", None) or {}).values()):
        try:
            if os.name == "nt" and p.pid:
                subprocess.run(["taskkill", "/T", "/F", "/PID", str(p.pid)], capture_output=True, timeout=60)
            p.terminate()
        except Exception:  # noqa: BLE001
            pass


def build_local(args):
    """atlas_core.cmd_build's driver, with run_groups' pool (the per-plate work is the verbatim _build_group)."""
    D = A.dirs(args.out)
    idx = T.discover(args.data, args.out, refresh=args.reindex)
    exprs = [f for f in idx["expression"] if IN_FLIGHT not in os.path.normpath(f).split(os.sep)]
    if not exprs:
        raise SystemExit("No expression parquet files found under " + os.path.abspath(args.data) + T.REINDEX_HINT)
    total, missing = expected_files(exprs)
    partial = bool(missing) and not args.limit_files
    if partial and not getattr(args, "allow_partial", False):
        raise SystemExit(f"build: {missing:,} of the {total:,} expression files are missing under "
                         f"{os.path.abspath(args.data)} (is the download unfinished?). Finish it ('tahoe download' "
                         f"resumes it) and run again, or add --allow-partial to build from the {len(exprs):,} files "
                         "there (the build is redone once the rest are there).")
    if partial:
        log(f"WARNING: {missing:,} of the {total:,} expression files are missing; building from the {len(exprs):,} "
            "there (--allow-partial)")
    if args.limit_files:
        exprs = exprs[:args.limit_files]
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    if gm is None:
        raise SystemExit("Gene metadata (token_id -> gene_symbol) not found" + T.REINDEX_HINT)
    G = int(gm["token_id"].max()) + 1
    log(f"Finding the plate of each of {len(exprs)} files ...")
    with ThreadPoolExecutor(16) as ex:
        fplate = dict(ex.map(A._file_plate, exprs))
    by_plate = defaultdict(list)
    for f in exprs:
        by_plate[fplate[f]].append(f)
    plates = sorted(by_plate, key=lambda p: (len(p), p))
    jobs = [(gid, p, by_plate[p], G, D["pb"], args.batch_size) for gid, p in enumerate(plates)]
    check_extra_groups(D["pb"], len(jobs), f"the {len(exprs)} files under {os.path.abspath(args.data)}")
    workers = min(args.workers or T.auto_workers(), len(jobs))
    per_worker = 5000 * G * 4 / 1e9 * 1.3 + 1.0
    mem = T.mem_available_gb()
    if mem:
        workers = max(1, min(workers, int(mem / per_worker)))
    log(f"{len(exprs)} files on {len(by_plate)} plates -> one group per plate, {workers} at a time "
        f"(~{per_worker:.1f} GB each)")
    if not args.workers and workers > 2 and T.disk_kind(args.data) == "hdd":
        log("  the data seem to sit on a hard drive: if reading is slow, stop and rerun with --workers 2")
    run_groups(jobs, workers)
    finish_build(args, idx, len(jobs), "local files", n_files=len(exprs), expected=total, partial=partial)


def finish_build(args, idx, n_groups, how, n_files=None, expected=None, partial=False):
    """The tail of atlas_core.cmd_build (sample map, well positions, build_info.json), for a build made elsewhere."""
    D = A.dirs(args.out)
    metas = sorted(glob.glob(os.path.join(D["pb"], "group*_profiles.csv")))
    prof = pd.concat([pd.read_csv(m, dtype={"sample": str, "cell_line_id": str}) for m in metas], ignore_index=True)
    bcf = pd.concat([pd.read_csv(m.replace("_profiles", "_barcodes"), dtype={"sample": str}) for m in metas],
                    ignore_index=True)
    smeta = pd.concat([pd.read_csv(m.replace("_profiles", "_samples"),
                                   dtype={"sample": str, "plate": str, "drug": str}) for m in metas],
                      ignore_index=True).drop_duplicates("sample")
    wl_like = prof.groupby("sample", as_index=False)["n_cells"].sum()
    sm, source, checks = T.build_sample_map(smeta, bcf, wl_like, idx, args.layout)
    sm.to_csv(os.path.join(args.out, "sample_map.csv"), index=False)
    checks.to_csv(os.path.join(args.out, "well_position_check.csv"), index=False)
    with open(os.path.join(args.out, "build_info.json"), "w", encoding="utf-8") as fh:
        json.dump({"G": _G(idx),
                   "groups": n_groups, "cells": int(prof["n_cells"].sum()), "profiles": len(prof),
                   "well_position_source": source, "limit_files": args.limit_files, "how": how,
                   "data": os.path.abspath(args.data), "n_files": n_files, "n_files_expected": expected,
                   "partial": bool(partial)}, fh, indent=1)
    log(f"Build done: {int(prof['n_cells'].sum()):,} cells in {len(prof):,} well x line profiles, "
        f"{sm['sample'].nunique()} wells ({how}); well positions from {source} "
        f"(median purity {sm['slot_purity'].median():.3f})")


def _G(idx):
    gm = T.read_tables(idx["gene"], ["token_id"])
    return int(gm["token_id"].max()) + 1
