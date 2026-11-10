"""embed - one vector space for genes, drug-doses, drug-dose x cell-line contexts and cell lines.

Every gene is described by how it moves across perturbations: its per-line z (tensor DDL_z) in every
(drug-dose, cell line) context of an active, trustworthy drug-dose (active = >= min_active significant genes pooled
over lines, OR >= min_active genes at per-line |z| >= 5 in >= 2 lines, so a response confined to a few lines enters
too). Trustworthy = not 'unreliable plate only', 'position not correctable' or 'wells disagree': the values of those
drug-doses are technically unsound, so they are left out of the fit (computing, not showing: info.json lists every
drug-dose left out and why, drugdoses.parquet says it per drug-dose in fit_status, and their vectors are still
projected). Drug-doses with other artifact flags (toxic, transcription drop, cell-cycle shift, ...) measure what the
drug did to the cells and are contexts like any other.

A gene enters the space only if it reaches |z| >= 3 in >= min_responsive of these contexts AND has real evidence of a
response: a significant pooled drug-dose (the atlas's q < 0.1 and >= 1.2x, BH within the gene), or a per-line
|z| >= max(5, the tables stage's calibrated per-line cut) in >= 2 lines of one trustworthy drug-dose. At full scale
almost every expressed gene reaches a fixed count of |z| >= 3 contexts by chance alone, so the count is not enough.
Both kinds of evidence count whether or not the drug-dose carries an artifact flag for the gene ("if there is a reason
to doubt, do not remove, rather alert"). A gene whose evidence, pooled and per-line, is all at drug-doses that carry
an alert for it is in the space with genes.parquet evidence_flagged_only = True, and the vault, the map and the
look-ups show it with an alert. "Carries an alert for the gene" = an artifact flag in the gene-level flags of
tables/drug_effects.parquet (clean = False there); for a (drug-dose, gene) the tables stage did not write (no
significant pooled change), the drug-dose's own artifact flags or the gene's 'position correction uncertain' there
(atlas DD_posunc). genes.parquet line_evidence / line_evidence_clean say whether the gene has per-line evidence at
all, and at a drug-dose without an alert for it. That matrix X (genes x contexts) is factorised,
X ~ U S V', after removing the broad components that make every gene look related (global toxicity / shutdown axes;
the atlas's "programs" rule). Then, in one k-dimensional space:

    gene vector          g = U S          (its direction is the gene's response pattern; cosine between two genes
                                           = correlation of their denoised response profiles)
    context vector       c = V            (one per drug-dose x line)
    drug-dose vector     d = S^-1 U' x    (x = its pooled z profile, standardised like X; also for drug-doses that
                                           were not used to fit the space)
    drug vector          U' x = S d       (of the drug's best trustworthy dose; principal coordinates, for
                                           drug-drug cosine)
    predicted z          g . c  or  g . d (the dot product reproduces the observed activity)
    line vector          s_l[k] = how strongly component k responds in line l relative to the typical line
                                  (slope of the line's context vectors on the drug-doses' mean vectors)
    line baseline vector the line's untreated expression profile projected the same way

Sign matters in this space: two genes that respond in opposite directions to the same perturbations have cosine
near -1 and sit far apart; the nodal map (graph stage) uses |cosine| instead and puts them together.

Halves: compounds (salt forms merged) are dealt into two halves and the space is fitted again on each half;
relations.run compares gene-gene cosines between the halves (independent compounds; they share the lines and plates).

Flags (embed version 5). A drug-dose's flags are its flags of record (tables.dd_flags_of_record: the atlas's flags,
then the tables stage's 'like a neighbouring well' / '... (top dose)' and 'translation inhibitor'); an artifact flag
is one of common.ARTIFACT_FLAGS (common.has_artifact), so 'like a neighbouring well' counts as one. The fit is
unchanged: only the three technical flags above keep a drug-dose out of it. The new tokens change only
evidence_flagged_only and the alerts.

Alerts in the tables written here: genes.parquet evidence_flagged_only (above); drugs.parquet alert when the dose
whose vector a drug gets carries an artifact flag (trusted = False too when the drug has no trustworthy dose: its
vector is then that of an untrustworthy dose); components.parquet
lists the strongest genes and drug-doses of each axis in their ranked place, a drug-dose with an artifact flag
followed by '(⚠ its flags)' and a gene with evidence_flagged_only by ' ⚠', and when a list is cut at N it also keeps
the N strongest without an alert that would fall below the cut. broad_components.csv names, for every tested
component of each fit, the 5 drug-doses with the largest and the smallest mean loading over their contexts
(top_pos_drugdoses, top_neg_drugdoses), so the removed broad axes are named.

Drug-dose similarity (embed version 5). drug_similarity.parquet has one row per (drug-dose, rank) for rank 1..50:
each drug-dose's 50 most similar of the other 1,131 drug-doses (on the real data; all of them are compared, the
table keeps the top 50 of each), ranked by cos_pooled (ties by the other's dd):
    cos_pooled     cosine of the pooled signatures: the pooled z clipped to +-10 on the tables/drug_effects.parquet rows
                   (|z| >= 3 or q < 0.10), 0 elsewhere and on noise-class RNAs (NaN when either has no such gene)
    cos_contexts   cosine of the drug-doses' context vectors over the lines, concatenated (NaN when either has no
                   contexts: only active, trustworthy drug-doses have them)
    n_shared_sig   genes significant (the atlas's call: q < 0.1 and >= 1.2x) in the same direction in both
    same_salt_base the other is a dose or a salt form of the same compound
    other_moa_fine, other_classes, other_flags   the other's Tahoe class, mechanism classes (with their sources) and
                   flags of record
On the real data the pooled signature finds drugs of the same Tahoe class better than chance (AUROC 0.578, 18% of the
5 nearest of an annotated drug share its class), the contexts slightly better (0.584, 21%).
drugdoses.parquet resembles_class / resembles_n / resembles_drugdoses / resembles_note: among a drug-dose's 10 most
similar drug-doses of other compounds (other salt bases), those with cosine >= 0.5, a Tahoe class and >= 10
significant genes changed the same way with it (n_shared_sig: a cosine of one or two shared genes means nothing); when
>= 4 of them share one class that differs from its own, a note names them ('It may act like them, or carry a signal from
another well'; '... Its other doses do not resemble them.' when none of the drug's other doses has a drug-dose of that
class among its own 10). A note, never a flag. It catches glucocorticoid-like wells that the neighbouring-well rule
cannot (on the real data Phenylephrine 5 µM and Econazole 5 µM touch no glucocorticoid well).
drugs.parquet salt_form_alert: for drugs that share a salt base, per dose both forms have, 'signatures differ' when
both have >= 100 significant genes and their signature cosine is < 0.3, 'strength differs' when (max + 1) / (min + 1)
significant genes >= 10 and max >= 30; e.g. 'Salt forms disagree at 0.5 µM: Docetaxel 101 significant genes,
Docetaxel (Trihydrate) 829, signature cosine 0.06 (signatures differ).' (every pair-dose that disagrees, joined).
"""

import os
import time
import warnings

import numpy as np
import pandas as pd

from . import atlas_core as A
from . import tlib as T
from .common import (ARTIFACT_FLAGS, folder, has_artifact, log, read_effects_index, save_npy, stable_seed,
                     stamp_stage, write_json, write_parquet)

VERSION = 5                # 3: significant pooled drug-doses with artifact flags count as evidence (with an alert);
#                            4: evidence_flagged_only also looks at per-line evidence (clean or flagged for the gene)
#                            5: the drug-doses' flags of record (tables.dd_flags_of_record: + the neighbouring-well
#                               and translation-inhibitor tokens; artifact = common.has_artifact); drug_similarity
#                               .parquet; drugdoses resembles_*; drugs salt_form_alert; broad_components names the
#                               drug-doses of each tested component
UNTRUSTED = ("unreliable plate only", "position not correctable", "wells disagree")
ALERT = "⚠"
LINE_ACTIVE_Z = 5.0    # a drug-dose is also active when >= min_active genes reach this per-line |z| in >= 2 lines
Z_CLIP = 8.0
BROAD_R = 0.3          # a broad component: |gene-component r| >= this ...
BROAD_FRAC = 0.05      # ... for >= this share of the genes (and >= BROAD_MIN genes), among the first BROAD_MAXPC
BROAD_MIN = 200
BROAD_MAXPC = 3
BROAD_TOP_DD = 5       # broad_components.csv names each tested component by its 5 strongest drug-doses either way
# drug-dose similarity (module docstring, 'Drug-dose similarity')
UM = "µM"
SIM_TOP = 50           # embed/drug_similarity.parquet: each drug-dose's 50 most similar other drug-doses
SIM_CLIP = 10.0        # the pooled signature: z clipped to +-10 ...
SIM_KEEP_Z = 3.0       # ... on the drug_effects rows (|z| >= 3 or q < 0.10; tables.KEEP_Z), 0 elsewhere
SIM_K = 10             # unexpected similarity: among the 10 most similar drug-doses of other compounds ...
SIM_MIN_COS = 0.5      # ... those with cosine >= 0.5 ...
SIM_MIN_SHARE = 4      # ... >= 4 share one Tahoe moa_fine that differs from the drug-dose's own
SIM_MIN_SHARED = 10    # ... counting only those that share >= 10 significant genes changed the same way with it (a
#                        cosine of one or two shared genes means nothing: on the synthetic data one planted gene gave
#                        cosine 1.0 between unrelated 0.05 uM drug-doses; the real notes share 55 to 3,800 such genes)
SIM_NO_CLASS = ("", "unclear", "unknown")    # Tahoe moa_fine values that name no class
SALT_MIN_SIG = 100     # salt forms: 'signatures differ' when both have >= 100 significant genes ...
SALT_MAX_COS = 0.3     # ... and their signature cosine is below 0.3;
SALT_RATIO = 10.0      # 'strength differs' when (max + 1) / (min + 1) significant genes >= 10 ...
SALT_MIN_MAX = 30      # ... and the stronger form has >= 30

# the words of the columns and files this stage adds (embed version 5); the explorer and the docs show them
COLUMN_DOCS = {
    "embed/drug_similarity.parquet": {
        "dd": "drug-dose index", "drug": "drug", "dose": "dose (µM)",
        "rank": "rank of the other drug-dose by cos_pooled (1 = most similar; the 50 most similar of all others)",
        "other_dd": "the other drug-dose's index", "other_drug": "the other drug", "other_dose": "its dose (µM)",
        "cos_pooled": "cosine of the pooled signatures: z clipped to +-10 on the tables/drug_effects.parquet rows "
                      "(|z| >= 3 or q < 0.10), 0 elsewhere and on noise-class RNAs (empty when either has no such "
                      "gene)",
        "cos_contexts": "cosine of the drug-doses' context vectors over the lines, concatenated (empty when either has "
                        "no contexts: only active, trustworthy drug-doses have them)",
        "n_shared_sig": "genes significant in both (q < 0.1 and >= 1.2x) and changed the same way",
        "same_salt_base": "the other is a dose or a salt form of the same compound",
        "other_moa_fine": "the other's Tahoe class (moa_fine)",
        "other_classes": "the other's mechanism classes with their sources (tahoemap/data/drug_classes.json)",
        "other_flags": "the other's flags of record"},
    "embed/drugdoses.parquet": {
        "flags": "the drug-dose's flags of record (tables/drugdoses.parquet flags)",
        "resembles_class": f"the Tahoe class shared by >= {SIM_MIN_SHARE} of its {SIM_K} most similar drug-doses of "
                           f"other compounds (cosine >= {SIM_MIN_COS:g}, >= {SIM_MIN_SHARED} significant genes "
                           "changed the same way), when it differs from its own; '' none",
        "resembles_n": "how many of them are of that class",
        "resembles_drugdoses": "those drug-doses with their cosine",
        "resembles_note": "the unexpected-similarity note in plain words (a note, not a flag); '' none"},
    "embed/drugs.parquet": {
        "flags": "the flags of record of the dose whose vector the drug gets",
        "salt_form_alert": "where salt forms of one compound disagree at a dose both have: 'signatures differ' (both "
                           f">= {SALT_MIN_SIG} significant genes, cosine < {SALT_MAX_COS:g}) or 'strength differs' "
                           f"((max + 1) / (min + 1) significant genes >= {SALT_RATIO:g}, max >= {SALT_MIN_MAX}); "
                           "'' none"},
    "embed/broad_components.csv": {
        "top_pos_drugdoses": f"the {BROAD_TOP_DD} drug-doses with the largest mean loading over their contexts on "
                             "this component (flagged ones with '(⚠ flags)')",
        "top_neg_drugdoses": f"the {BROAD_TOP_DD} drug-doses with the smallest mean loading"}}



def capped(order, ok, n):
    """The items of a ranked list (order: indices, strongest first) to show when it is cut at n: the n strongest, and
    any of the n strongest without an alert (ok[i] True) that would fall below the cut, in their ranked order."""
    order = np.asarray(order, dtype=np.int64)
    if order.size <= n:
        return order
    ok = np.asarray(ok, dtype=bool)
    keep = np.zeros(order.size, dtype=bool)
    keep[:n] = True
    keep[np.flatnonzero(ok[order])[:n]] = True
    return order[keep]


def _artifact_text(flags):
    """The artifact flags of a flags string, comma-joined (plain words for an alert); '' when it has none."""
    return ", ".join(f for f in str(flags or "").split("; ") if f in ARTIFACT_FLAGS)


def _gene_level_overrides(out, clean_dd, gK):
    """The rows of tables/drug_effects.parquet whose gene-level clean differs from their drug-dose's (a gene's own
    'position correction uncertain' / 'position not correctable' make a clean drug-dose flagged for that gene; a
    cell-cycle shift that does not explain the gene's change makes a flagged one clean): (dd, col, clean) arrays, or
    None when the table or its columns are missing (then the drug-dose's own flags decide)."""
    p = os.path.join(out, "tables", "drug_effects.parquet")
    if not os.path.exists(p):
        return None
    import pyarrow.parquet as pq
    if not {"dd", "col", "clean"} <= set(pq.ParquetFile(p).schema_arrow.names):
        return None
    t = pd.read_parquet(p, columns=["dd", "col", "clean"])
    d_ = pd.to_numeric(t["dd"], errors="coerce").fillna(-1).to_numpy(np.int64)
    c_ = pd.to_numeric(t["col"], errors="coerce").fillna(-1).to_numpy(np.int64)
    cl = t["clean"].fillna(False).astype(bool).to_numpy()
    ok = (d_ >= 0) & (d_ < len(clean_dd)) & (c_ >= 0) & (c_ < gK)
    d_, c_, cl = d_[ok], c_[ok], cl[ok]
    diff = cl != clean_dd[d_]
    o = np.argsort(c_[diff], kind="mergesort")
    return d_[diff][o], c_[diff][o], cl[diff][o]


def _svd(X, k, seed):
    from sklearn.utils.extmath import randomized_svd
    k = int(max(1, min(k, min(X.shape) - 1)))
    U, S, Vt = randomized_svd(X, n_components=k, n_iter=6, n_oversamples=20, random_state=seed)
    return U.astype(np.float32), S.astype(np.float32), Vt.astype(np.float32)


def _standardise(X):
    """Centre each gene's row and scale it by max(its SD, the median SD): weakly responsive genes are not blown up."""
    mu = X.mean(axis=1, keepdims=True)
    X -= mu
    sd = np.sqrt(np.einsum("ij,ij->i", X, X) / max(X.shape[1], 1))[:, None]
    floor = float(np.median(sd[sd > 0])) if (sd > 0).any() else 1.0
    sc = np.maximum(sd, floor)
    X /= sc
    return mu.ravel(), sc.ravel()


def _top_drugdoses(v, ctx_dd, dlabel, n=BROAD_TOP_DD):
    """The n drug-doses with the largest and the smallest mean loading over their contexts (v: one right singular
    vector, one value per context; ctx_dd: the drug-dose of each context): ('; '-joined labels, '; '-joined labels)."""
    if ctx_dd is None or dlabel is None or not len(v):
        return "", ""
    u, inv = np.unique(ctx_dd, return_inverse=True)
    m = np.bincount(inv, weights=v, minlength=u.size) / np.maximum(np.bincount(inv, minlength=u.size), 1)
    o = np.lexsort((u, -m))
    p = np.lexsort((u, m))
    return "; ".join(dlabel[u[o[:n]]]), "; ".join(dlabel[u[p[:n]]])


def _remove_broad(X, seed, n_genes, tag, ctx_dd=None, dlabel=None):
    """Remove (in place) broad components among the first BROAD_MAXPC; return the record of every tested one (with
    its BROAD_TOP_DD strongest drug-doses either way when ctx_dd and dlabel are given)."""
    U, S, Vt = _svd(X, min(10, min(X.shape) - 1), seed)
    norms = np.sqrt(np.einsum("ij,ij->i", X, X))
    norms[norms == 0] = 1.0
    rows, removed = [], []
    need = max(BROAD_MIN, BROAD_FRAC * n_genes)
    tot = float(np.einsum("ij,ij->i", X, X).sum())
    for j in range(len(S)):
        r = U[:, j] * S[j] / norms
        n_follow = int((np.abs(r) >= BROAD_R).sum())
        broad = j < BROAD_MAXPC and n_follow >= need
        pos, neg = _top_drugdoses(Vt[j], ctx_dd, dlabel)
        rows.append({"fit": tag, "component": j + 1, "variance_pct": 100.0 * float(S[j] ** 2) / max(tot, 1e-12),
                     "genes_following": n_follow, "removed": broad, "top_pos_drugdoses": pos,
                     "top_neg_drugdoses": neg})
        if broad:
            removed.append(j)
    for j in removed:                                     # X -= u s v' in row blocks (no big temporary)
        u, s, v = U[:, j], S[j], Vt[j]
        for r0 in range(0, X.shape[0], 4096):
            X[r0:r0 + 4096] -= np.outer(u[r0:r0 + 4096] * s, v).astype(np.float32)
    return rows, removed, (U, S, Vt)


def _fit(X, k, seed, n_genes, tag, ctx_dd=None, dlabel=None):
    rows, removed, first = _remove_broad(X, seed, n_genes, tag, ctx_dd, dlabel)
    remaining = float(np.einsum("ij,ij->i", X, X).astype(np.float64).sum())
    U, S, Vt = _svd(X, k, seed + 1)
    return U, S, Vt, rows, removed, remaining


# ----------------------------------------------------------------------------- drug-dose similarity
def _unit_rows(M):
    """Rows scaled to unit length (float64); a row of zeros stays zero. Returns (unit rows, has: norm > 0)."""
    M = np.asarray(M, dtype=np.float64)
    nr = np.sqrt(np.einsum("ij,ij->i", M, M))
    has = nr > 0
    return M / np.where(has, nr, 1.0)[:, None], has


def pooled_signatures(out, Dn, gK, noise):
    """Drug-doses x genes float32: each drug-dose's pooled z clipped to +-SIM_CLIP on its tables/drug_effects.parquet
    rows (the keep rule: |z| >= 3 or q_up / q_down < 0.10), 0 elsewhere and on noise-class RNAs. Without that table:
    the same keep rule on the atlas matrices DD_z, DD_qup, DD_qdn."""
    S = np.zeros((Dn, gK), dtype=np.float32)
    p = os.path.join(out, "tables", "drug_effects.parquet")
    if os.path.exists(p):
        t = pd.read_parquet(p, columns=["dd", "col", "z"])
        d_ = pd.to_numeric(t["dd"], errors="coerce").fillna(-1).to_numpy(np.int64)
        c_ = pd.to_numeric(t["col"], errors="coerce").fillna(-1).to_numpy(np.int64)
        ok = (d_ >= 0) & (d_ < Dn) & (c_ >= 0) & (c_ < gK)
        S[d_[ok], c_[ok]] = np.nan_to_num(t["z"].to_numpy(np.float32)[ok], nan=0.0)
    else:
        fxd = os.path.join(out, "atlas", "effects")
        z = np.load(os.path.join(fxd, "DD_z.npy"), mmap_mode="r")
        qu = np.load(os.path.join(fxd, "DD_qup.npy"), mmap_mode="r")
        qd = np.load(os.path.join(fxd, "DD_qdn.npy"), mmap_mode="r")
        for g0 in range(0, gK, 4096):
            g1 = min(gK, g0 + 4096)
            zz = np.asarray(z[:, g0:g1], dtype=np.float32)
            keep = (np.abs(zz) >= SIM_KEEP_Z) | (np.asarray(qu[:, g0:g1]) < A.Q_CUT) | \
                (np.asarray(qd[:, g0:g1]) < A.Q_CUT)
            S[:, g0:g1] = np.where(keep, np.nan_to_num(zz, nan=0.0), 0.0)
    np.clip(S, -SIM_CLIP, SIM_CLIP, out=S)
    S[:, np.asarray(noise[:gK], dtype=bool)] = 0.0
    return S


def context_signatures(ctx_dd, ctx_line, V, Dn, L):
    """Drug-doses x (lines x k) float32: the drug-dose's context vectors over the lines, concatenated (zeros for a line
    without a context); has = the drug-dose has at least one context."""
    k = V.shape[1]
    C = np.zeros((Dn, L, k), dtype=np.float32)
    C[ctx_dd, ctx_line] = V
    has = np.zeros(Dn, dtype=bool)
    has[np.unique(ctx_dd)] = True
    return C.reshape(Dn, L * k), has


def similarity_matrix(M, has=None):
    """Cosine between the rows of M (drug-doses x features); NaN where either row has no signal (all zero, or has
    False)."""
    Uu, nz = _unit_rows(M)
    if has is not None:
        nz = nz & np.asarray(has, dtype=bool)
    Sm = Uu @ Uu.T
    Sm[~nz, :] = np.nan
    Sm[:, ~nz] = np.nan
    return Sm


def shared_sig_counts(sig3):
    """Drug-doses x drug-doses int32: genes significant in the same direction in both (sig3: +1 / -1 / 0)."""
    up = (sig3 > 0).astype(np.float32)
    dn = (sig3 < 0).astype(np.float32)
    return np.rint(up @ up.T + dn @ dn.T).astype(np.int32)


def ranked_others(Sp, top):
    """Per drug-dose, the `top` other drug-doses by cos_pooled descending (NaN last), ties by the other's dd."""
    Dn = Sp.shape[0]
    top = int(min(top, Dn - 1))
    key = np.where(np.isfinite(Sp), Sp, -np.inf)
    out = np.zeros((Dn, top), dtype=np.int64)
    idx = np.arange(Dn)
    for d in range(Dn):
        o = np.lexsort((idx, -key[d]))                     # cos descending, then dd ascending
        out[d] = o[o != d][:top]
    return out


def _dl(drug, dose):
    return f"{drug} {_fmt_dose(dose)} {UM}"


def _fmt_dose(dose):
    try:
        return f"{float(dose):g}"
    except (TypeError, ValueError):
        return str(dose)


def drug_similarity_table(meta, Sp, Sc, shared, top=SIM_TOP):
    """embed/drug_similarity.parquet: one row per (drug-dose, rank) for its `top` most similar other drug-doses (by
    cos_pooled; module docstring). meta: one row per dd with drug, dose, salt_base, moa_fine, classes, flags."""
    R = ranked_others(Sp, top)
    Dn, k = R.shape
    d = np.repeat(np.arange(Dn), k)
    o = R.ravel()
    sb = meta["salt_base"].astype(str).to_numpy()
    return pd.DataFrame({
        "dd": d.astype(np.int32), "drug": meta["drug"].to_numpy()[d], "dose": meta["dose"].to_numpy()[d],
        "rank": np.tile(np.arange(1, k + 1), Dn).astype(np.int16), "other_dd": o.astype(np.int32),
        "other_drug": meta["drug"].to_numpy()[o], "other_dose": meta["dose"].to_numpy()[o],
        "cos_pooled": Sp[d, o].astype(np.float32), "cos_contexts": Sc[d, o].astype(np.float32),
        "n_shared_sig": shared[d, o].astype(np.int32), "same_salt_base": sb[d] == sb[o],
        "other_moa_fine": meta["moa_fine"].fillna("").astype(str).to_numpy()[o],
        "other_classes": meta["classes"].fillna("").astype(str).to_numpy()[o],
        "other_flags": meta["flags"].fillna("").astype(str).to_numpy()[o]})


def _similar_kept(Sp, d, sb, moa, k, min_cos, shared=None, min_shared=SIM_MIN_SHARED):
    """Drug-dose d's k most similar drug-doses of other salt bases (cos_pooled, ties by dd) that have cos >= min_cos,
    a Tahoe class (moa_fine not in SIM_NO_CLASS) and (shared given) >= min_shared significant genes changed the same
    way with d; most similar first."""
    row = np.where(np.isfinite(Sp[d]), Sp[d], -np.inf)
    o = np.lexsort((np.arange(len(row)), -row))
    o = [j for j in o if j != d and sb[j] != sb[d]][:k]
    return [j for j in o if row[j] >= min_cos and moa[j].strip().lower() not in SIM_NO_CLASS
            and (shared is None or shared[d, j] >= min_shared)]


def _main_class(Sp, d, kept, moa):
    """The class most of `kept` share (ties: the larger summed cosine, then the name) and its members."""
    if not kept:
        return None, []
    cls = {}
    for j in kept:
        cls.setdefault(moa[j], []).append(j)
    best = sorted(cls.items(), key=lambda kv: (-len(kv[1]), -sum(Sp[d, j] for j in kv[1]), kv[0]))[0]
    return best[0], best[1]


def resembles(meta, Sp, chembl=None, shared=None, k=SIM_K, min_cos=SIM_MIN_COS, min_share=SIM_MIN_SHARE,
              min_shared=SIM_MIN_SHARED):
    """The unexpected-similarity note of every drug-dose (module docstring): columns resembles_class, resembles_n,
    resembles_drugdoses ('Drug dose µM (cos)', '; '-joined) and resembles_note ('' when the rule does not hold).
    'Its other doses do not resemble them' is added when none of the drug's other doses has a drug-dose of that
    class among its own k most similar drug-doses of other compounds with cosine >= min_cos. chembl: {drug: ChEMBL
    mechanism text} (optional); shared: drug-doses x drug-doses, significant genes changed the same way (a neighbour
    counts only with >= min_shared; None: not required). A note, never a flag."""
    Dn = len(meta)
    sb = meta["salt_base"].astype(str).to_numpy()
    moa = meta["moa_fine"].fillna("").astype(str).to_numpy()
    drug = meta["drug"].astype(str).to_numpy()
    dose = meta["dose"].to_numpy()
    chembl = chembl or {}
    kept = [_similar_kept(Sp, d, sb, moa, k, min_cos, shared, min_shared) for d in range(Dn)]
    cls_ = np.full(Dn, "", dtype=object)
    n_ = np.zeros(Dn, dtype=np.int16)
    lst = np.full(Dn, "", dtype=object)
    note = np.full(Dn, "", dtype=object)
    for d in range(Dn):
        c, js = _main_class(Sp, d, kept[d], moa)
        if c is None or len(js) < min_share or c == moa[d]:
            continue
        cls_[d], n_[d] = c, len(js)
        lst[d] = "; ".join(f"{_dl(drug[j], dose[j])} ({Sp[d, j]:.2f})" for j in js)
        own = moa[d].strip() or "not given"
        ch = str(chembl.get(drug[d], "") or "").strip()
        txt = (f"Its {k} most similar drug-doses of other compounds include {len(js)} {c} drug-doses with cosine "
               f"{min_cos:g} or more ({', '.join(f'{_dl(drug[j], dose[j])} {Sp[d, j]:.2f}' for j in js)}). Its own "
               f"annotation is {own} (Tahoe)" + (f"; ChEMBL: {ch}" if ch else "") +
               ". It may act like them, or carry a signal from another well.")
        others = [j for j in range(Dn) if j != d and drug[j] == drug[d]]
        if others and not any(moa[x] == c for j in others for x in kept[j]):
            txt += " Its other doses do not resemble them."
        note[d] = txt
    return pd.DataFrame({"resembles_class": cls_, "resembles_n": n_, "resembles_drugdoses": lst,
                         "resembles_note": note})


def salt_form_alerts(meta, Sp):
    """{drug: text} for drugs that share a salt base with another drug: for every dose both forms have, 'signatures
    differ' when both have >= SALT_MIN_SIG significant genes and their signature cosine is < SALT_MAX_COS, 'strength
    differs' when (max + 1) / (min + 1) >= SALT_RATIO and max >= SALT_MIN_MAX. Also returns the list of judged
    pair-doses (dicts) for info.json."""
    sb = meta["salt_base"].astype(str).to_numpy()
    drug = meta["drug"].astype(str).to_numpy()
    dose = meta["dose"].to_numpy()
    conc = pd.to_numeric(meta["dose"], errors="coerce").to_numpy(np.float64)
    nsig = pd.to_numeric(meta["n_sig_genes"], errors="coerce").fillna(0).to_numpy(np.int64)
    texts, judged = {}, []
    for base in sorted(set(sb)):
        dr = sorted(set(drug[sb == base]))
        if len(dr) < 2:
            continue
        for i in range(len(dr)):
            for j in range(i + 1, len(dr)):
                a, b = dr[i], dr[j]
                for c in sorted(set(conc[drug == a]) & set(conc[drug == b])):
                    ia = np.flatnonzero((drug == a) & (conc == c))[0]
                    ib = np.flatnonzero((drug == b) & (conc == c))[0]
                    na, nb = int(nsig[ia]), int(nsig[ib])
                    cs = float(Sp[ia, ib])
                    why = []
                    if min(na, nb) >= SALT_MIN_SIG and np.isfinite(cs) and cs < SALT_MAX_COS:
                        why.append("signatures differ")
                    if (max(na, nb) + 1) / (min(na, nb) + 1) >= SALT_RATIO and max(na, nb) >= SALT_MIN_MAX:
                        why.append("strength differs")
                    judged.append({"salt_base": base, "drug_a": a, "drug_b": b, "dose": _fmt_dose(dose[ia]),
                                   "n_sig_a": na, "n_sig_b": nb, "cos_pooled": round(cs, 4) if np.isfinite(cs) else
                                   None, "alert": ", ".join(why)})
                    if why:
                        cos_t = f"{cs:.2f}" if np.isfinite(cs) else "not defined (a form changes no gene)"
                        t = (f"Salt forms disagree at {_fmt_dose(dose[ia])} {UM}: {a} {na} significant genes, {b} "
                             f"{nb}, signature cosine {cos_t} ({' and '.join(why)}).")
                        for x in (a, b):
                            texts[x] = (texts[x] + " " + t) if x in texts else t
    return texts, judged


def _similarity(out, ed, dd, flags, sig3, noise, gK, ctx_dd, ctx_line, V, L):
    """Write embed/drug_similarity.parquet and return (info, resembles columns, salt-form texts, judged pair-doses)."""
    Dn = len(dd)
    meta = pd.DataFrame({"drug": dd["drug"].astype(str).to_numpy(), "dose": dd["dose"].to_numpy(),
                         "salt_base": [T.salt_base(x) for x in dd["drug"].astype(str)],
                         "moa_fine": dd["moa_fine"].fillna("").astype(str).to_numpy() if "moa_fine" in dd else "",
                         "flags": flags.to_numpy(), "n_sig_genes": dd["n_sig_genes"].to_numpy()})
    classes, chembl = {}, {}
    try:                                                  # mechanism classes and ChEMBL's mechanisms (reference stage)
        from . import mechanisms as M
        classes = {x: M.class_text(out, x) for x in sorted(set(meta["drug"]))}
        an = M.drug_annotations(out)
        if "chembl_mechanisms" in an:
            chembl = dict(zip(an["drug"].astype(str), an["chembl_mechanisms"].fillna("").astype(str)))
    except Exception as e:  # noqa: BLE001
        log(f"  drug classes not read ({type(e).__name__}: {e}); other_classes left empty")
    meta["classes"] = meta["drug"].map(classes).fillna("")
    sig3 = sig3.copy()
    sig3[:, np.asarray(noise[:gK], dtype=bool)] = 0
    Sp = similarity_matrix(pooled_signatures(out, Dn, gK, noise))
    C, has = context_signatures(ctx_dd, ctx_line, V, Dn, L)
    Sc = similarity_matrix(C, has)
    del C
    shared = shared_sig_counts(sig3)
    tab = drug_similarity_table(meta, Sp, Sc, shared)
    write_parquet(tab, os.path.join(ed, "drug_similarity.parquet"))
    notes = resembles(meta, Sp, chembl, shared)
    salt_txt, judged = salt_form_alerts(meta, Sp)
    hit = np.flatnonzero(notes["resembles_note"].to_numpy() != "")
    info = {"rows": int(len(tab)), "top": int(tab["rank"].max()) if len(tab) else 0, "of_others": int(Dn - 1),
            "pooled": f"pooled z clipped to +-{SIM_CLIP:g} on the tables/drug_effects.parquet rows (|z| >= 3 or q < "
                      "0.10), 0 elsewhere and on noise-class RNAs; cosine",
            "contexts": "the drug-dose's context vectors over the lines, concatenated (NaN when either has no "
                        "contexts)",
            "drugdoses_with_contexts": int(has.sum()),
            "resembles_rule": f"among its {SIM_K} most similar drug-doses of other salt bases (cos_pooled), those "
                              f"with cosine >= {SIM_MIN_COS:g}, a Tahoe moa_fine and >= {SIM_MIN_SHARED} significant "
                              f"genes changed the same way with it; >= {SIM_MIN_SHARE} share one moa_fine that "
                              "differs from its own",
            "resembles_notes": int(hit.size),
            "resembles": [f"{_dl(meta['drug'][i], meta['dose'][i])}: {notes['resembles_class'][i]} "
                          f"({int(notes['resembles_n'][i])})" for i in hit]}
    log(f"  drug-dose similarity: {len(tab):,} rows (each drug-dose's {info['top']} most similar of {Dn - 1:,} "
        f"others); {hit.size} unexpected-similarity notes; {sum(1 for x in judged if x['alert'])} salt-form alerts "
        f"of {len(judged)} pair-doses")
    return info, notes, salt_txt, judged


def run(out, dims=64, min_active=10, min_responsive=5, chunk=512, halves=True):
    t0 = time.time()
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    ed = folder(out, "embed")
    fxd = os.path.join(out, "atlas", "effects")
    ix = read_effects_index(fxd)
    genes, dd, lines = ix["genes"], ix["drugdose"], ix["lines"]
    gK = int((genes["kind"] == "gene").sum())
    Dn, L = len(dd), len(lines)
    DDL_z = np.load(os.path.join(out, "tensor", "DDL_z.npy"), mmap_mode="r")
    from .tables import dd_flags_of_record
    # the flags of record (the atlas's + the tables stage's neighbouring-well and translation-inhibitor tokens); only
    # the three technical flags keep a drug-dose out of the fit, as before
    flags = pd.Series(dd_flags_of_record(out), dtype=object).fillna("").astype(str)
    trusted = ~flags.apply(lambda f: any(u in f for u in UNTRUSTED)).to_numpy()
    pooled_active = trusted & (dd["n_sig_genes"].to_numpy() >= min_active)
    noise = genes["symbol"].astype(str).str.match(A.NOISE_RNA_RE).to_numpy()[:gK]

    # pass 1 over every drug-dose: per gene x drug-dose, how many lines reach |z| >= 3 and |z| >= line_z; per
    # drug-dose x line, how many genes reach |z| >= LINE_ACTIVE_Z (a response confined to a few lines)
    line_z = LINE_ACTIVE_Z
    tinfo = os.path.join(out, "tables", "info.json")
    if os.path.exists(tinfo):                             # the calibrated per-line cut of the tables stage
        import json
        with open(tinfo, encoding="utf-8") as fh:
            line_z = max(line_z, float(json.load(fh).get("line_z_threshold", line_z) or line_z))
    hit = np.zeros((gK, Dn), dtype=np.int16)
    strong = np.zeros((gK, Dn), dtype=np.int16)
    line_hits = np.zeros((Dn, L), dtype=np.int64)
    for g0 in range(0, gK, chunk):
        Z = np.abs(np.nan_to_num(np.asarray(DDL_z[g0:g0 + chunk], dtype=np.float32)))   # chunk x Dn x L
        hit[g0:g0 + chunk] = (Z >= 3).sum(axis=2)
        strong[g0:g0 + chunk] = (Z >= line_z).sum(axis=2)
        line_hits += (Z >= LINE_ACTIVE_Z).sum(axis=0)
    line_active = trusted & ((line_hits >= min_active).sum(axis=1) >= 2)
    active = pooled_active | line_active
    dsel = np.flatnonzero(active)
    if dsel.size < 5:                                     # tiny runs: fall back to every trusted drug-dose
        dsel = np.flatnonzero(trusted)
    log(f"Embed: {dsel.size:,} active trustworthy drug-doses (of {Dn:,}; {int((line_active & ~pooled_active).sum())} "
        f"of them active only in single lines) x {L} lines as contexts")

    # a gene enters the space only if it really responds: a fixed count of |z| >= 3 contexts is reached by chance by
    # almost every expressed gene at full scale, so it also needs a significant pooled drug-dose (the atlas's BH
    # within the gene), or a strong per-line response (|z| >= line_z) in >= 2 lines of one trustworthy drug-dose;
    # either counts at a drug-dose with an artifact flag for the gene too, and the gene carries an alert when that is
    # all it has
    n_resp = hit[:, dsel].sum(axis=1).astype(np.int64)
    qup = np.load(os.path.join(fxd, "DD_qup.npy"), mmap_mode="r")
    qdn = np.load(os.path.join(fxd, "DD_qdn.npy"), mmap_mode="r")
    lfc = np.load(os.path.join(fxd, "DD_lfc.npy"), mmap_mode="r")
    clean = ~flags.apply(has_artifact).to_numpy()
    over = _gene_level_overrides(out, clean, gK)          # gene-level clean where it differs from the drug-dose's
    pu_path = os.path.join(fxd, "DD_posunc.npy")          # the gene's own 'position correction uncertain'
    posunc = np.load(pu_path, mmap_mode="r") if os.path.exists(pu_path) else None
    sig3 = np.zeros((Dn, gK), dtype=np.int8)              # the atlas's significance call (+1 / -1 / 0)
    n_sig = np.zeros(gK, dtype=np.int64)                  # significant pooled drug-doses per gene, any flags
    n_sig_clean = np.zeros(gK, dtype=np.int64)            # ... of them without an artifact flag for this gene
    line_resp = ((strong >= 2) & trusted[None, :]).any(axis=1)
    line_resp_clean = np.zeros(gK, dtype=bool)            # ... per-line evidence at a drug-dose clean for this gene
    for g0 in range(0, gK, 4096):
        g1 = min(gK, g0 + 4096)
        u = (np.asarray(qup[:, g0:g1]) < A.Q_CUT) & (np.asarray(lfc[:, g0:g1]) >= A.LFC_MIN)
        d_ = (np.asarray(qdn[:, g0:g1]) < A.Q_CUT) & (np.asarray(lfc[:, g0:g1]) <= -A.LFC_MIN)
        s_ = u | d_
        sig3[:, g0:g1] = u.astype(np.int8) - d_.astype(np.int8)
        # clean for the gene (drug-doses x genes): no artifact flag in the drug-dose's flags and no 'position
        # correction uncertain' for the gene; where tables/drug_effects.parquet has the row, its gene-level clean
        # decides (it also applies the cell-cycle rule)
        cg = np.repeat(clean[:, None], g1 - g0, axis=1)
        if posunc is not None and posunc.shape[1] >= g1:
            cg &= ~np.asarray(posunc[:, g0:g1], dtype=bool)
        if over is not None:
            i0, i1 = np.searchsorted(over[1], [g0, g1])
            cg[over[0][i0:i1], over[1][i0:i1] - g0] = over[2][i0:i1]
        n_sig[g0:g1] = s_.sum(axis=0)
        n_sig_clean[g0:g1] = (s_ & cg).sum(axis=0)
        line_resp_clean[g0:g1] = ((strong[g0:g1] >= 2).T & trusted[:, None] & cg).any(axis=0)
    sig = n_sig > 0
    sig_clean = n_sig_clean > 0
    evidence_ok = sig | line_resp
    by_chance = (n_resp >= min_responsive) & ~evidence_ok
    gsel = np.flatnonzero((n_resp >= min_responsive) & evidence_ok & ~noise)
    flagged_only = np.zeros(gK, dtype=bool)               # in the space only through drug-doses with an alert
    flagged_only[gsel] = (~sig_clean & ~line_resp_clean)[gsel]
    del hit, strong
    ctx_fin = np.zeros(dsel.size * L, dtype=np.int64)
    for g0 in range(0, gK, chunk):
        Z = np.asarray(DDL_z[g0:g0 + chunk][:, dsel, :], dtype=np.float32).reshape(-1, dsel.size * L)
        ctx_fin += np.isfinite(Z).sum(axis=0)
    cmask = ctx_fin >= max(10, 0.2 * gK)
    cidx = np.flatnonzero(cmask)
    log(f"  {gsel.size:,} responsive genes of {gK:,} (|z| >= 3 in >= {min_responsive} contexts, and a significant "
        f"pooled drug-dose ({int((sig & ~noise).sum()):,} genes; {int((sig_clean & ~noise).sum()):,} with a clean "
        f"one) or per-line |z| >= {line_z:g} in >= 2 lines of one drug-dose ({int((line_resp & ~noise).sum()):,})); "
        f"{int(flagged_only.sum()):,} of them only through drug-doses that carry an alert for them, pooled and per "
        f"line (marked); "
        f"{int(by_chance.sum()):,} reached the count without either; {cidx.size:,} contexts with data")
    if gsel.size < 10 or cidx.size < 10:
        raise SystemExit("embed: too few responsive genes or contexts to build a vector space")

    X = np.empty((gsel.size, cidx.size), dtype=np.float32)
    for i0 in range(0, gsel.size, chunk):
        gg = gsel[i0:i0 + chunk]
        Z = np.asarray(DDL_z[gg][:, dsel, :], dtype=np.float32).reshape(len(gg), dsel.size * L)[:, cidx]
        np.clip(Z, -Z_CLIP, Z_CLIP, out=Z)
        X[i0:i0 + len(gg)] = np.nan_to_num(Z, nan=0.0)
    ctx_dd = np.repeat(dsel, L)[cidx]
    ctx_line = np.tile(np.arange(L), dsel.size)[cidx]

    # halves by compound (salt forms together)
    base = dd["drug"].astype(str).map(T.salt_base).to_numpy()
    half_of_dd = np.array([stable_seed("half", b) % 2 for b in base])
    Xh = None
    if halves:
        Xh = [X[:, half_of_dd[ctx_dd] == h].copy() for h in (0, 1)]

    art = [_artifact_text(f) for f in flags]
    dlabel = np.array([f"{a} {_fmt_dose(b)} {UM}" + (f" ({ALERT} {t})" if t else "")
                       for a, b, t in zip(dd["drug"].astype(str), dd["dose"], art)], dtype=object)
    mu, sc = _standardise(X)
    seed = stable_seed("embed", gsel.size, cidx.size)
    U, S, Vt, broad_rows, removed, remaining = _fit(X, dims, seed, gsel.size, "all", ctx_dd, dlabel)
    k = len(S)
    captured = 100.0 * float((S.astype(np.float64) ** 2).sum()) / max(remaining, 1e-12)
    log(f"  broad components removed: {', '.join(str(j + 1) for j in removed) or 'none'}; space: {k} dimensions "
        f"holding {captured:.1f}% of the remaining variance")
    gvec = U * S[None, :]                                  # gene vectors (principal coordinates)
    gnorm = np.sqrt((gvec ** 2).sum(axis=1))
    rownorm = np.sqrt(np.einsum("ij,ij->i", X, X))
    represented = np.where(rownorm > 0, (gnorm / np.maximum(rownorm, 1e-12)) ** 2, np.nan)
    del X

    def full(rows_vals, width):
        arr = np.full((gK, width), np.nan, dtype=np.float32)
        arr[gsel] = rows_vals
        return arr

    unit = gvec / np.maximum(gnorm[:, None], 1e-12)
    save_npy(os.path.join(ed, "gene_vectors.npy"), full(gvec, k))
    save_npy(os.path.join(ed, "gene_unit.npy"), full(unit, k))
    save_npy(os.path.join(ed, "singular_values.npy"), S)
    save_npy(os.path.join(ed, "context_vectors.npy"), Vt.T.copy())

    # half spaces
    if halves:
        for h in (0, 1):
            Xh_ = Xh[h]
            _standardise(Xh_)
            Uh, Sh, _Vh, rows_h, rem_h, _ = _fit(Xh_, dims, seed + 10 + h, gsel.size, f"half{h + 1}",
                                                 ctx_dd[half_of_dd[ctx_dd] == h], dlabel)
            broad_rows += rows_h
            gh = Uh * Sh[None, :]
            gh /= np.maximum(np.sqrt((gh ** 2).sum(axis=1))[:, None], 1e-12)
            save_npy(os.path.join(ed, f"gene_unit_half{h + 1}.npy"), full(gh, len(Sh)))
            log(f"  half {h + 1}: {Xh_.shape[1]:,} contexts, broad removed: "
                f"{', '.join(str(j + 1) for j in rem_h) or 'none'}")
        del Xh

    # projections: every drug-dose (pooled z) and every line's baseline
    DD_z = np.load(os.path.join(fxd, "DD_z.npy"), mmap_mode="r")
    P = (U / S[None, :]).astype(np.float32)               # x (standardised, over gsel) -> S^-1 U' x
    xd = np.clip(np.nan_to_num(np.asarray(DD_z[:, gsel], dtype=np.float32), nan=0.0), -Z_CLIP, Z_CLIP)
    xd = (xd - mu[None, :]) / sc[None, :]
    dvec = xd @ P                                          # Dn x k
    save_npy(os.path.join(ed, "drugdose_vectors.npy"), dvec.astype(np.float32))

    line_cpm = np.load(os.path.join(fxd, "line_cpm.npy"))[:, gsel]
    yb = np.log2(line_cpm + 1.0)
    yb = yb - np.median(yb, axis=0, keepdims=True)
    lb = (yb / sc[None, :]) @ P
    save_npy(os.path.join(ed, "line_baseline_vectors.npy"), lb.astype(np.float32))

    # line response sensitivity: slope of each line's context vectors on the drug-dose's mean over lines
    V = Vt.T                                               # contexts x k
    dpos = {d: i for i, d in enumerate(dsel)}
    D_mean = np.zeros((dsel.size, k), dtype=np.float64)
    cnt = np.zeros(dsel.size)
    for j in range(V.shape[0]):
        i = dpos[ctx_dd[j]]
        D_mean[i] += V[j]
        cnt[i] += 1
    D_mean /= np.maximum(cnt, 1)[:, None]
    sens = np.full((L, k), np.nan, dtype=np.float32)
    for l in range(L):
        jj = np.flatnonzero(ctx_line == l)
        if jj.size < 5:
            continue
        ref = D_mean[[dpos[d] for d in ctx_dd[jj]]]
        den = (ref ** 2).sum(axis=0)
        sens[l] = np.where(den > 0, (V[jj] * ref).sum(axis=0) / np.maximum(den, 1e-12), np.nan)
    save_npy(os.path.join(ed, "line_response_vectors.npy"), sens)

    # drug-dose similarity (module docstring): the pooled signatures (sparse z) and the contexts' vectors
    sim, notes, salt_txt, salt_judged = _similarity(out, ed, dd, flags, sig3, noise, gK, ctx_dd, ctx_line, V, L)

    # tables
    sym = genes["symbol"].astype(str).to_numpy()
    lab = genes["label"].astype(str).to_numpy()
    inc = np.zeros(gK, dtype=bool)
    inc[gsel] = True
    gtab = pd.DataFrame({"col": np.arange(gK), "symbol": sym[:gK], "label": lab[:gK], "included": inc,
                         "n_responsive_contexts": n_resp, "vector_norm": np.nan, "represented_fraction": np.nan,
                         "noise_rna": noise, "n_sig_drugdoses": n_sig, "n_sig_drugdoses_clean": n_sig_clean,
                         "line_evidence": line_resp, "line_evidence_clean": line_resp_clean,
                         "evidence_flagged_only": flagged_only})
    gtab.loc[gsel, "vector_norm"] = gnorm
    gtab.loc[gsel, "represented_fraction"] = represented
    write_parquet(gtab, os.path.join(ed, "genes.parquet"))
    cell = lines["cell_name"].fillna(lines["cell_line_id"]).astype(str).to_numpy()
    ctab = pd.DataFrame({"j": np.arange(cidx.size), "dd": ctx_dd, "line": ctx_line,
                         "drug": dd["drug"].to_numpy()[ctx_dd], "dose": dd["dose"].to_numpy()[ctx_dd],
                         "cell_line_id": lines["cell_line_id"].to_numpy()[ctx_line], "cell_name": cell[ctx_line],
                         "half": half_of_dd[ctx_dd] + 1})
    write_parquet(ctab, os.path.join(ed, "contexts.parquet"))

    # which drug-doses the fit used, and why the others are not in it
    untrusted_why = [", ".join(u for u in UNTRUSTED if u in f) for f in flags]
    used = np.isin(np.arange(Dn), dsel)
    status = np.where(used, "in the fit", np.where(
        ~trusted, np.array([f"left out: technically untrustworthy ({w})" for w in untrusted_why], dtype=object),
        f"not active (fewer than {min_active} significant genes, pooled or in >= 2 single lines)"))
    ddt = dd[["drug", "dose", "conc", "n_sig_genes"]].copy()
    ddt["flags"] = flags.to_numpy()
    ddt.insert(0, "dd", np.arange(Dn))
    ddt["active_context"] = used
    ddt["fit_status"] = status
    ddt["half"] = half_of_dd + 1
    ddt["vector_norm"] = np.sqrt((dvec.astype(np.float64) ** 2).sum(axis=1))
    for c in notes.columns:
        ddt[c] = notes[c].to_numpy()
    write_parquet(ddt, os.path.join(ed, "drugdoses.parquet"))
    left_out = [{"dd": int(i), "drug": str(dd["drug"].iat[i]), "dose": str(dd["dose"].iat[i]),
                 "n_sig_genes": int(pd.to_numeric(dd["n_sig_genes"], errors="coerce").fillna(0).iat[i]),
                 "why": untrusted_why[i]} for i in np.flatnonzero(~trusted)]
    if left_out:
        log(f"  {len(left_out):,} technically untrustworthy drug-doses left out of the fit (listed in info.json; "
            "their vectors are still projected)")

    # one vector per drug: its best trustworthy dose (most significant genes; tie -> higher dose), in principal
    # coordinates (U'x = S d), which weight the components by their size: these are for drug-drug cosine. A drug with
    # no trustworthy dose keeps its best dose, with trusted = False and an alert.
    dd2 = dd.assign(dd=np.arange(Dn), conc_num=pd.to_numeric(dd["conc"], errors="coerce").fillna(0),
                    trusted=trusted, untrusted=~trusted, flags=flags.to_numpy())
    best = dd2.sort_values(["drug", "untrusted", "n_sig_genes", "conc_num"], ascending=[True, True, False, False]) \
        .drop_duplicates("drug").sort_values("drug")
    save_npy(os.path.join(ed, "drug_vectors.npy"), (dvec[best["dd"].to_numpy()] * S[None, :]).astype(np.float32))
    cols_ = [c for c in ("drug", "dose", "dd", "n_sig_genes", "trusted", "flags", "moa_fine", "targets")
             if c in best.columns]
    dtab = best[cols_].reset_index(drop=True)
    dtab["alert"] = [f"{ALERT} no trustworthy dose: this vector is of {d} uM ({untrusted_why[int(i)]})" if not t else
                     (f"{ALERT} this vector is of {d} uM, which carries an artifact flag ({a})" if a else "")
                     for d, i, t, a in zip(best["dose"].astype(str), best["dd"], best["trusted"],
                                           (_artifact_text(f) for f in best["flags"]))]
    dtab["salt_form_alert"] = [salt_txt.get(str(x), "") for x in dtab["drug"]]
    write_parquet(dtab, os.path.join(ed, "drugs.parquet"))

    # components: what each axis is (strongest first; alerts in place, see the module docstring)
    comp = []
    var_tot = float((S.astype(np.float64) ** 2).sum())
    d_ok = np.array([not t for t in art], dtype=bool)
    glabel = np.array([s + (f" {ALERT}" if f_ else "") for s, f_ in zip(sym[gsel], flagged_only[gsel])], dtype=object)
    g_ok = ~flagged_only[gsel]
    for j in range(k):
        o = np.argsort(U[:, j])
        od = np.argsort(dvec[:, j])
        oline = np.argsort(-np.nan_to_num(sens[:, j], nan=-np.inf))
        comp.append({"component": j + 1, "variance_pct_of_space": 100.0 * float(S[j]) ** 2 / max(var_tot, 1e-12),
                     "top_pos_genes": ", ".join(glabel[capped(o[::-1], g_ok, 15)]),
                     "top_neg_genes": ", ".join(glabel[capped(o, g_ok, 15)]),
                     "top_pos_drugdoses": "; ".join(dlabel[capped(od[::-1], d_ok, 10)]),
                     "top_neg_drugdoses": "; ".join(dlabel[capped(od, d_ok, 10)]),
                     "most_sensitive_lines": ", ".join(cell[oline[:8]])})
    write_parquet(pd.DataFrame(comp), os.path.join(ed, "components.parquet"))
    pd.DataFrame(broad_rows).to_csv(os.path.join(ed, "broad_components.csv"), index=False)
    n_fo = int(flagged_only.sum())
    info = {"version": VERSION, "dims": k, "genes_included": int(gsel.size), "genes_total": gK,
            "contexts": int(cidx.size), "drugdoses_active": int(dsel.size), "drugdoses_total": Dn, "lines": L,
            "min_active": min_active, "min_responsive": min_responsive, "z_clip": Z_CLIP,
            "drugdoses_active_pooled": int(pooled_active.sum()), "drugdoses_active_lines_only":
                int((line_active & ~pooled_active).sum()), "line_active_z": LINE_ACTIVE_Z,
            "line_z_responsive": line_z, "n_genes_significant_pooled": int((sig & ~noise).sum()),
            "n_genes_significant_pooled_clean": int((sig_clean & ~noise).sum()),
            "n_genes_line_responsive": int((line_resp & ~noise).sum()),
            "n_genes_line_responsive_clean": int((line_resp_clean & ~noise).sum()),
            "n_genes_evidence_flagged_only": n_fo,
            "evidence_rule": "a significant pooled drug-dose (q < 0.1, >= 1.2x), with or without an artifact flag, "
                             "or a per-line |z| >= line_z_responsive in >= 2 lines of one trustworthy drug-dose, "
                             "with or without an artifact flag for the gene; "
                             f"{n_fo:,} genes are in the space only through drug-doses that carry an alert for them, "
                             "pooled and per line (genes.parquet evidence_flagged_only; shown with an alert)",
            "gene_level_clean": "tables/drug_effects.parquet clean" if over is not None else
                                "the drug-doses' own flags (tables/drug_effects.parquet has no clean column)",
            "n_genes_excluded_chance": int(by_chance.sum()),
            "drugdoses_left_out_untrusted": len(left_out),
            "drugdoses_not_active": int((trusted & ~used).sum()),
            "left_out_rule": "drug-doses flagged " + ", ".join(f"'{u}'" for u in UNTRUSTED) + " are technically "
                             "untrustworthy and stay out of the fit (their vectors are still projected); "
                             "drugdoses.parquet fit_status says it per drug-dose",
            "left_out_untrusted": left_out,
            "broad_removed": [int(j) + 1 for j in removed], "halves": bool(halves),
            "variance_captured_pct": round(captured, 2),
            "singular_values": [float(s) for s in S], "drug_similarity": sim,
            "salt_forms": {"rule": f"for drugs that share a salt base, per dose both forms have: 'signatures differ' "
                                   f"when both have >= {SALT_MIN_SIG} significant genes and their signature cosine is "
                                   f"< {SALT_MAX_COS:g}; 'strength differs' when (max + 1) / (min + 1) significant "
                                   f"genes >= {SALT_RATIO:g} and max >= {SALT_MIN_MAX}",
                           "pair_doses": len(salt_judged),
                           "salt_bases": len({x["salt_base"] for x in salt_judged}),
                           "alerts": sum(1 for x in salt_judged if x["alert"]),
                           "signatures_differ": sum(1 for x in salt_judged if "signatures differ" in x["alert"]),
                           "strength_differs": sum(1 for x in salt_judged if "strength differs" in x["alert"]),
                           "judged": salt_judged},
            "flags": "the drug-doses' flags of record (tables/drugdoses.parquet flags: the atlas's, the "
                     "neighbouring-well and the translation-inhibitor tokens); artifact = common.has_artifact; only "
                     "the three technical flags keep a drug-dose out of the fit",
            "minutes": round((time.time() - t0) / 60, 2),
            "model": "X ~ U S V'; gene g = U S; context c = V; drug-dose d = S^-1 U' x; predicted z = g . c or "
                     "g . d (in standardised units); drug_vectors = U' x of the best trustworthy dose (cosine)"}
    write_json(info, os.path.join(ed, "info.json"))
    save_npy(os.path.join(ed, "gene_row_mean.npy"), mu.astype(np.float32))
    save_npy(os.path.join(ed, "gene_row_scale.npy"), sc.astype(np.float32))
    save_npy(os.path.join(ed, "included_cols.npy"), gsel.astype(np.int64))
    stamp_stage(out, "embed", VERSION, info)
    log(f"Embed done: {gsel.size:,} genes in {k} dimensions from {cidx.size:,} contexts ({info['minutes']} min)")
    return info
