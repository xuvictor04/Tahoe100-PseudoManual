#!/usr/bin/env python3
"""Stream Tahoe-100M from Hugging Face through the repo's own atlas build and gene-panel extract, one file at a time.

Each expression file is downloaded just before tahoe_atlas._build_group reads it, then the gene panel's per-cell
extract (tahoe_mtap_gankyrin._extract_one) runs on it, then it is replaced by a zero-row parquet with the same
schema, so the folder is indexed exactly like a full download while never holding more than a few files.

    python3 stream_build.py metadata --data DIR          # the four small metadata tables the scripts need
    python3 stream_build.py plates   --data DIR          # file -> plate map (reads one column chunk per file)
    python3 stream_build.py stream   --data DIR          # workers: --workers N, default from CPUs and free memory
    python3 stream_build.py finish   --data DIR          # tahoe_atlas.py build on the finished groups (all reused)
Every command is resumable: finished plates, per-cell files and downloads are kept and skipped on a rerun. 'stream'
exits non-zero if any plate failed or any file is missing at the end (rerun it). Disk: ~25 GB at the end (atlas
pseudobulk ~20 GB, gene panel cells ~2.6 GB), plus ~0.3 GB per worker in flight. Memory: ~2.6 GB per worker.
"""
import argparse, concurrent.futures as cf, json, os, re, subprocess, sys, time, traceback
import multiprocessing as mp

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # the repo root
sys.path.insert(0, REPO)
HF = "https://huggingface.co/datasets/tahoebio/Tahoe-100M/resolve/main/"
API = "https://huggingface.co/api/datasets/tahoebio/Tahoe-100M/tree/main/data"
AHEAD = 3


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def remote_files():
    import requests
    out, url = [], API
    while url:
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        out += [x["path"] for x in r.json() if x["path"].endswith(".parquet")]
        m = re.search(r'<([^>]+)>;\s*rel="next"', r.headers.get("link", ""))
        url = m.group(1) if m else None
    return sorted(out)


METADATA = ["cell_line_metadata", "drug_metadata", "gene_metadata", "sample_metadata"]


def cmd_metadata(args):
    os.makedirs(os.path.join(args.data, "metadata"), exist_ok=True)
    for name in METADATA:
        path = os.path.join(args.data, "metadata", name + ".parquet")
        download(f"metadata/{name}.parquet", path)
        log(f"metadata: {name}.parquet ok")


def cmd_plates(args):
    import fsspec, pyarrow.parquet as pq
    out = os.path.join(args.data, "plate_map.json")
    if os.path.exists(out):
        with open(out) as fh:
            if len(json.load(fh)) == 3388:
                log("plate_map.json exists (3,388 files): kept")
                return
    fs = fsspec.filesystem("https", block_size=1 << 18)
    files = remote_files()
    log(f"{len(files)} expression files on Hugging Face")

    def plate(rel):
        for a in range(5):
            try:
                with fs.open(HF + rel, "rb") as fh:
                    t = pq.ParquetFile(fh).read_row_group(0, columns=["plate"])
                    return rel, str(t.column(0)[0].as_py())
            except Exception:  # noqa: BLE001
                time.sleep(2 ** a)
        raise RuntimeError("no plate for " + rel)

    with cf.ThreadPoolExecutor(32) as ex:
        m = dict(ex.map(plate, files))
    with open(os.path.join(args.data, "plate_map.json"), "w") as fh:
        json.dump(m, fh, indent=0)
    from collections import Counter
    log("files per plate: " + ", ".join(f"{p} {n}" for p, n in sorted(Counter(m.values()).items())))


def is_real(path):
    import pyarrow.parquet as pq
    try:
        return pq.ParquetFile(path).metadata.num_rows > 0
    except Exception:  # noqa: BLE001
        return False


def download(rel, path):
    if os.path.exists(path) and is_real(path):
        return path
    tmp = path + ".part"
    for a in range(6):
        r = subprocess.run(["curl", "-sSfL", "--retry", "5", "--retry-delay", "2", "-o", tmp, HF + rel],
                           capture_output=True, text=True)
        if r.returncode == 0 and is_real(tmp):
            os.replace(tmp, path)
            return path
        time.sleep(2 ** a)
    raise RuntimeError(f"download failed: {rel}: {r.stderr[-300:]}")


def stub(path):
    import pyarrow.parquet as pq
    schema = pq.read_schema(path)
    os.remove(path)
    pq.write_table(schema.empty_table(), path)


def plate_job(job):
    """One plate: the repo's _build_group over its files, downloaded on demand; the panel extract per file."""
    gid, name, files, rels, G, pb, batch, panel = job
    try:
        import pyarrow.parquet as real_pq
        import tahoe_atlas as A
        import tahoe_mtap_gankyrin as T
        T._init_worker(*panel["init"])
        cells_dir, root = panel["cells_dir"], panel["root"]
        rel_of = dict(zip(files, rels))
        order = {f: i for i, f in enumerate(files)}
        pool = cf.ThreadPoolExecutor(2)
        futs, state = {}, {"prev": None, "n": 0, "t0": time.time()}

        def ensure(i):
            for k in range(i, min(i + AHEAD, len(files))):
                if files[k] not in futs:
                    futs[files[k]] = pool.submit(download, rel_of[files[k]], files[k])

        def dst_of(f):
            return os.path.join(cells_dir, re.sub(r"[^\w.-]+", "__", os.path.relpath(f, root)))

        def finalize(f):
            T._extract_one((f, dst_of(f)))
            stub(f)
            state["n"] += 1
            if state["n"] % 25 == 0:
                el = time.time() - state["t0"]
                log(f"  {name}: {state['n']}/{len(files)} files, {el / 60:.1f} min")

        class Shim:
            def __getattr__(self, k):
                return getattr(real_pq, k)

            def ParquetFile(self, f):
                i = order[f]
                ensure(i)
                futs[f].result()
                ensure(i + 1)
                if state["prev"] is not None:
                    finalize(state["prev"])
                state["prev"] = f
                return real_pq.ParquetFile(f)

        A.pq = Shim()
        r = A._build_group((gid, name, files, G, pb, batch))
        if state["prev"] is not None:
            finalize(state["prev"])
        for f in files:      # group reused after a crash between its write and the last extract: extract the rest
            if not os.path.exists(dst_of(f)):
                download(rel_of[f], f)
                finalize(f)
        pool.shutdown()
        return name, r[2], r[3], None
    except Exception:  # noqa: BLE001
        return name, 0, False, traceback.format_exc()


def groups(args):
    """The same plate groups, in the same order and with the same file lists, as tahoe_atlas.cmd_build."""
    with open(os.path.join(args.data, "plate_map.json")) as fh:
        pm = json.load(fh)
    root = os.path.abspath(args.data)
    rels = sorted(pm)
    by_plate = {}
    for rel in rels:
        by_plate.setdefault(pm[rel], []).append(rel)
    plates = sorted(by_plate, key=lambda p: (len(p), p))
    return root, pm, plates, by_plate


def full_files(root):
    """Expression files in <root>/data that hold cells (a download, or a stream's files in flight; stubs are ~3 KB)."""
    d = os.path.join(root, "data")
    return [f for f in (os.listdir(d) if os.path.isdir(d) else [])
            if f.endswith(".parquet") and os.path.getsize(os.path.join(d, f)) > 1 << 20]


def cmd_stream(args):
    import pandas as pd
    import tahoe_mtap_gankyrin as T
    import tahoe_gene_panel as P
    root, pm, plates, by_plate = groups(args)
    os.makedirs(os.path.join(root, "data"), exist_ok=True)
    mark = os.path.join(root, "data", ".streamed")      # this folder's files are the stream's to replace by stubs
    if not os.path.exists(mark):
        full = full_files(root)
        if full:
            sys.exit(f"{os.path.join(root, 'data')} already holds {len(full)} expression files with cells (a download?); "
                     "'stream' would replace them by empty stubs. Run tahoe_atlas.py build/effects and "
                     "tahoe_gene_panel.py extract/analyze on it instead, or stream into another folder.")
        open(mark, "w").close()
    gm = pd.read_parquet(os.path.join(root, "metadata", "gene_metadata.parquet"),
                         columns=["token_id", "gene_symbol", "ensembl_id"])
    G = int(gm["token_id"].max()) + 1
    genes, _missing = P.wanted_genes(argparse.Namespace(genes=""), gm["gene_symbol"].dropna().astype(str).tolist())
    targets, cols, lut, _report = T.build_columns(gm, genes)
    pb = os.path.join(root, "atlas", "pseudobulk")
    cells_dir = os.path.join(root, "gene_panel", "cells")
    os.makedirs(pb, exist_ok=True)
    os.makedirs(cells_dir, exist_ok=True)
    panel = {"init": (lut, cols, targets, args.batch_size), "cells_dir": cells_dir, "root": root}
    jobs = []
    for gid, p in enumerate(plates):
        files = [os.path.join(root, r) for r in by_plate[p]]
        jobs.append((gid, p, files, by_plate[p], G, pb, args.batch_size, panel))
    jobs.sort(key=lambda j: -len(j[2]))           # biggest plates first: shorter tail
    if args.only:
        jobs = [j for j in jobs if j[1] in args.only.split(",")]
    workers = args.workers or auto_workers()
    log(f"{len(jobs)} plates, {sum(len(j[2]) for j in jobs)} files, {workers} at a time")
    failed = []
    ctx = mp.get_context("spawn")
    with ctx.Pool(workers, maxtasksperchild=1) as pool:
        for name, n, reused, err in pool.imap_unordered(plate_job, jobs, chunksize=1):
            if err:
                failed.append(name)
                log(f"FAILED {name}:\n{err}")
            else:
                log(f"{name} {'already built' if reused else 'done'} ({n:,} cells)")
    missing_groups = [j[1] for j in jobs if not os.path.exists(os.path.join(pb, f"group{j[0]:03d}.npy"))]
    missing_cells = [f for j in jobs for f in j[2]
                     if not os.path.exists(os.path.join(cells_dir, re.sub(r"[^\w.-]+", "__", os.path.relpath(f, root))))]
    if failed or missing_groups or missing_cells:
        sys.exit(f"stream incomplete: failed plates {failed}, plates without output {missing_groups}, "
                 f"{len(missing_cells)} files without per-cell output; rerun 'stream' (finished work is kept)")
    log("stream complete: every plate and every file processed")


def auto_workers():
    """Plates in parallel: one per CPU, at most one per ~3 GB of free memory, at least 1."""
    try:
        import psutil
        free_gb = psutil.virtual_memory().available / 1e9
    except Exception:  # noqa: BLE001
        try:
            with open("/proc/meminfo") as fh:
                free_gb = int(next(l for l in fh if l.startswith("MemAvailable")).split()[1]) / 1e6
        except Exception:  # noqa: BLE001
            free_gb = 8.0
    return max(1, min(os.cpu_count() or 1, int(free_gb // 3)))


def cmd_finish(args):
    import tahoe_atlas as A
    root, pm, plates, by_plate = groups(args)
    m = {os.path.join(root, r): p for r, p in pm.items()}
    A._file_plate = lambda path: (path, m.get(os.path.abspath(path), "unknown"))
    sys.argv = ["tahoe_atlas.py", "build", "--data", root, "--workers", "1"]
    A.main()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["metadata", "plates", "stream", "finish"])
    ap.add_argument("--data", required=True)
    ap.add_argument("--workers", type=int, default=0, help="plates in parallel (default: from CPUs and free memory)")
    ap.add_argument("--batch-size", type=int, default=20000)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    a.data = os.path.abspath(os.path.expanduser(a.data))
    {"metadata": cmd_metadata, "plates": cmd_plates, "stream": cmd_stream, "finish": cmd_finish}[a.command](a)
