"""stream - the build driver, and the build without the 430 GB download: every expression file is fetched from Hugging Face, summed into
its plate's pseudobulk, and deleted. Disk need: the pseudobulk only (~17 GB), plus ~1 GB of files in flight.

The summing is the ported atlas_core._build_group itself, unchanged: in each worker process the module's
`pq.ParquetFile` is swapped for a shim that downloads the requested file (and the next ones of the same plate, in the
background) before opening it, and deletes the file read before. The output is the same pseudobulk folder a local
build writes, so every later stage is the same. Files are assigned to plates from their parquet footers (a file can
span two plates; profiles are keyed by well and line and summed across groups by the effects step, as in the atlas).
"""

import glob
import json
import os
import re
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
from .common import log

REPO = "https://huggingface.co/datasets/tahoebio/Tahoe-100M/resolve/main/"
API = "https://huggingface.co/api/datasets/tahoebio/Tahoe-100M/tree/main/data"
META = ("gene_metadata", "sample_metadata", "cell_line_metadata", "drug_metadata")
PREFETCH = 2


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
    import urllib.request
    names, url = [], API
    try:
        while url:
            with urllib.request.urlopen(url, timeout=60) as resp:
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
        with urllib.request.urlopen(req, timeout=120) as r:
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
    _W.update(next_of=next_of, tmp=tmp, pool=ThreadPoolExecutor(PREFETCH), futs={}, prev=None,
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
    if prev and os.path.exists(prev):
        try:
            os.remove(prev)
        except OSError:
            pass
    return pf


# ----------------------------------------------------------------------------- driver
def fetch_metadata(meta_dir):
    os.makedirs(meta_dir, exist_ok=True)
    for t in META:
        p = os.path.join(meta_dir, t + ".parquet")
        if not os.path.exists(p) or os.path.getsize(p) < 1000:
            log(f"  fetching metadata/{t}.parquet")
            fetch(f"{REPO}metadata/{t}.parquet", p)


def build(args, hf_dir):
    """args as for atlas_core.cmd_build (out = <OUT>/atlas). hf_dir holds metadata/ and the plate map cache."""
    D = A.dirs(args.out)
    fetch_metadata(os.path.join(hf_dir, "metadata"))
    tmp = os.path.join(hf_dir, "in_flight")
    os.makedirs(tmp, exist_ok=True)
    for f in glob.glob(os.path.join(tmp, "*")):
        os.remove(f)
    idx = T.discover(hf_dir, args.out, refresh=True)
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    G = int(gm["token_id"].max()) + 1
    rels = list_files()
    if args.limit_files:
        rels = rels[:args.limit_files]
    pmap_path = os.path.join(hf_dir, "file_plates.json")
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
    for old in glob.glob(os.path.join(D["pb"], "group*_profiles.csv")):
        gid = int(re.search(r"group(\d+)_", old).group(1))
        if gid >= len(jobs):
            for f in glob.glob(old.replace("_profiles.csv", "*")):
                os.remove(f)
    workers = min(args.workers or T.auto_workers(), len(jobs))
    per_worker = 5000 * G * 4 / 1e9 * 1.3 + 1.0
    mem = T.mem_available_gb()
    if mem:
        workers = max(1, min(workers, int(mem / per_worker)))
    log(f"{len(rels)} files on {len(plates)} plates, streamed from Hugging Face -> one group per plate, "
        f"{workers} at a time (~{per_worker:.1f} GB each)")
    run_groups(jobs, workers, initializer=_init_worker, initargs=(next_of, tmp))
    for f in glob.glob(os.path.join(tmp, "*")):              # the last file of each plate
        os.remove(f)
    finish_build(args, idx, len(jobs), "streamed from Hugging Face")


def run_groups(jobs, workers, initializer=None, initargs=()):
    """Run atlas_core._build_group (verbatim) for every plate group, biggest first, `workers` at a time.

    A process pool that loses a worker (most often: killed for lack of memory) makes multiprocessing.Pool wait
    forever; this executor raises instead, and finished plates are kept for the next run."""
    from concurrent.futures import ProcessPoolExecutor, as_completed
    from concurrent.futures.process import BrokenProcessPool
    order = sorted(jobs, key=lambda j: -len(j[2]))            # biggest plates first: a shorter tail
    t0, done = time.time(), 0
    try:
        with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn"), initializer=initializer,
                                 initargs=initargs) as ex:
            futs = [ex.submit(A._build_group, j) for j in order]
            for fu in as_completed(futs):
                _gid, name, _nc, reused = fu.result()
                done += 1
                log(f"  {name} {'already built' if reused else 'done'} ({done}/{len(jobs)} plates, "
                    f"{(time.time() - t0) / 60:.1f} min)")
    except BrokenProcessPool:
        raise SystemExit(f"build: a worker process died (most often it ran out of memory with {workers} plates at "
                         f"a time). The {done} finished plates are kept: run again with --workers "
                         f"{max(1, workers - 1)}.")


def build_local(args):
    """atlas_core.cmd_build's driver, with run_groups' pool (the per-plate work is the verbatim _build_group)."""
    D = A.dirs(args.out)
    idx = T.discover(args.data, args.out, refresh=args.reindex)
    exprs = idx["expression"]
    if not exprs:
        raise SystemExit("No expression parquet files found under " + os.path.abspath(args.data) + T.REINDEX_HINT)
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
    for old in glob.glob(os.path.join(D["pb"], "group*_profiles.csv")):
        gid = int(re.search(r"group(\d+)_", old).group(1))
        if gid >= len(jobs):
            for f in glob.glob(old.replace("_profiles.csv", "*")):
                os.remove(f)
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
    finish_build(args, idx, len(jobs), "local files")


def finish_build(args, idx, n_groups, how):
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
                   "well_position_source": source, "limit_files": args.limit_files, "how": how}, fh, indent=1)
    log(f"Build done: {int(prof['n_cells'].sum()):,} cells in {len(prof):,} well x line profiles, "
        f"{sm['sample'].nunique()} wells ({how}); well positions from {source} "
        f"(median purity {sm['slot_purity'].median():.3f})")


def _G(idx):
    gm = T.read_tables(idx["gene"], ["token_id"])
    return int(gm["token_id"].max()) + 1
