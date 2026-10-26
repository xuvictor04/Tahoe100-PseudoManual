"""Verifier v6: a pure-ambient negative control. In lines with a homozygous CDKN2A deletion (and MTAP-null lines), every
CDKN2A (MTAP) read is soup or cross-contamination. If 'CDKN2A detected' in those cells is associated with ATF3 / TP53 /
p53 targets as strongly as 'TRIM72 detected' (incl. TRIM72 in NCI-H661), ambient capture by stressed / damaged cells can
produce the TRIM72 co-occurrence signals. Same well x line fixed-effect quasi-Poisson model as v3 section 7.
Reads the first N cell files only (argv[4], default 500)."""
import glob, os, sys, time
import numpy as np, pandas as pd, pyarrow.parquet as pq
import json
D, data, outdir = sys.argv[1:4]
NF = int(sys.argv[4]) if len(sys.argv) > 4 else 500
t0 = time.time()
info = json.load(open(f"{D}/cache/run_info.json"))
PLAC = info["params"]["placebo"]
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
OUTDEF = {"P53_SCORE": P53, "MDM2": ["MDM2"], "XPC": ["XPC"], "DDB2": ["DDB2"], "ATF3": ["ATF3"], "TP53": ["TP53"],
          "PMAIP1": ["PMAIP1"]}
st = pd.read_csv(f"{data}/gene_panel/results/p53_functional_status.csv")
rho = pd.read_csv(f"{outdir}/ambient_rho_deleted_genes.csv")
true_del = set(rho[(rho.gene == "CDKN2A") & (rho.rho < 0.3)].line)          # HS-578T, NCI-H2122 are not deleted
true_mtap = set(rho[(rho.gene == "MTAP") & (rho.rho < 0.3)].line)
cd_ids = set(st[st.cell_name.isin(true_del)].cell_line_id.astype(str))
mt_ids = set(st[st.cell_name.isin(true_mtap)].cell_line_id.astype(str))
fail = set(pd.read_csv(f"{data}/atlas/effects/failed_wells.csv")["sample"].astype(str))
genes = list(dict.fromkeys(["CDKN2A", "MTAP", "TRIM72"] + PLAC + sum(OUTDEF.values(), [])))
cols = ["sample", "cell_line_id", "total_counts", "S_PHASE", "G2M_PHASE"] + genes
files = sorted(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet")))[:NF]
keep_ids = cd_ids | mt_ids
parts = []
for fi, f in enumerate(files):
    t = pq.read_table(f, columns=cols).to_pandas()
    t["cell_line_id"] = t["cell_line_id"].astype(str); t["sample"] = t["sample"].astype(str)
    t = t[t.cell_line_id.isin(keep_ids) & ~t["sample"].isin(fail)].copy()
    for c_ in cols[2:]:
        t[c_] = t[c_].astype(np.float32)
    parts.append(t)
C = pd.concat(parts, ignore_index=True)
print(f"{NF} files, {len(C):,} cells of {len(cd_ids)} CDKN2A-deleted / {len(mt_ids)} MTAP-null lines; {time.time() - t0:.0f} s", flush=True)


def fe_poisson(y, X, strata):
    us, si = np.unique(strata, return_inverse=True)
    keep = np.bincount(si, y, len(us))[si] > 0
    y, X, si = y[keep], X[keep], np.unique(si[keep], return_inverse=True)[1]
    ns = si.max() + 1
    b = np.zeros(X.shape[1])
    for _ in range(50):
        e = np.exp(X @ b); a = np.log(np.bincount(si, y, ns) / np.bincount(si, e, ns)); mu = e * np.exp(a[si])
        smu = np.bincount(si, mu, ns)
        mx = np.column_stack([np.bincount(si, mu * X[:, k], ns) for k in range(X.shape[1])])
        H = (X.T * mu) @ X - (mx.T / smu) @ mx
        step = np.linalg.solve(H, X.T @ (y - mu)); b = b + step
        if np.max(np.abs(step)) < 1e-10:
            break
    e = np.exp(X @ b); a = np.log(np.bincount(si, y, ns) / np.bincount(si, e, ns)); mu = e * np.exp(a[si])
    smu = np.bincount(si, mu, ns)
    mx = np.column_stack([np.bincount(si, mu * X[:, k], ns) for k in range(X.shape[1])])
    H = (X.T * mu) @ X - (mx.T / smu) @ mx
    phi = max(1.0, float(((y - mu) ** 2 / mu).sum() / max(1, len(y) - ns - X.shape[1])))
    return b, np.linalg.inv(H) * phi


rows = []
for label, ids, amb in (("CDKN2A-deleted lines", cd_ids, "CDKN2A"), ("MTAP-null lines", mt_ids, "MTAP")):
    x = C[C.cell_line_id.isin(ids)]
    T = x.total_counts.to_numpy(float); lt = np.log(T)
    strata = (x["sample"] + "|" + x.cell_line_id).to_numpy()
    _, si = np.unique(strata, return_inverse=True)
    cen = lambda v: v - (np.bincount(si, v) / np.bincount(si))[si]
    covs = [cen(lt), cen(np.log((x.S_PHASE.to_numpy(float) + 0.5) / T)), cen(np.log((x.G2M_PHASE.to_numpy(float) + 0.5) / T))]
    for pn in [amb, "TRIM72"] + PLAC:
        pv = x[pn].to_numpy(); nd = int((pv > 0).sum())
        if nd < 30:
            continue
        X = np.column_stack([(pv > 0).astype(float)] + covs)
        for o, mem in OUTDEF.items():
            y = x[mem].to_numpy(float).sum(1)
            b, V = fe_poisson(y, X, strata)
            rows.append(dict(cells=label, pred=pn, role="ambient-only gene" if pn == amb else ("TRIM72" if pn == "TRIM72" else "placebo"),
                             outcome=o, n_cells=len(y), n_det=nd, pct_det=100 * nd / len(y),
                             pct_1umi=100 * np.mean(pv[pv > 0] == 1), log_rr=b[0], se=np.sqrt(V[0, 0])))
R = pd.DataFrame(rows)
R.to_csv(f"{outdir}/v6_ambient_control.csv", index=False)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
for (cells, o), h in R.groupby(["cells", "outcome"], sort=False):
    a = h[h.role == "ambient-only gene"].iloc[0]; t = h[h.role == "TRIM72"].iloc[0]; p = h[h.role == "placebo"].log_rr
    print(f"{cells:22s} {o:9s} ambient {a.pred} det {a.pct_det:.2f}% ({a.pct_1umi:.0f}% 1 UMI): log RR {a.log_rr:+.3f} (se {a.se:.3f}) "
          f"pct among placebos {100 * np.mean(p < a.log_rr):.0f} | TRIM72 det {t.pct_det:.2f}%: {t.log_rr:+.3f} ({t.se:.3f}) "
          f"pct {100 * np.mean(p < t.log_rr):.0f} | placebo median {p.median():+.3f} max {p.max():+.3f}")
print(f"done {time.time() - t0:.0f} s")
