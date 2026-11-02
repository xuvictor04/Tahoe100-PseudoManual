---
type: concept
tags: [concept, method, estimator, clustering, inference]
status: current
---

# Two-way fixed effects

> [!summary] In one line
> Remove both the cell-line mean and the drug-dose mean from outcome and exposure, then fit one slope on
> what is left — which is the estimator behind every headline number here, which is why the study's raw
> MG53/p53 correlation collapses from +0.091 to +0.013, and which costs an interval that rests on **ten**
> clusters.

## The estimator

The screen's model, from `genome_wide/genome_wide.py` section C:

```
Y_gene = (drug-dose × TP53-group fixed effects)
       + (line fixed effects)
       + b_common × MG53
       + (covariates × TP53 group)
```

`Y_gene` is the gene's corrected log2 fold change for a given line × drug-dose; MG53 is [[TRIM72]]'s
corrected log2 fold change for the **same cell**. So `b_common` is in **log2 of the gene per doubling of
measured MG53**; +1 means 2×. `b_WT` and `b_alt` are the same slope fitted separately per genotype group,
`diff` = `b_WT` − `b_alt`, and `b_common` constrains the two to be equal while leaving the fixed effects
and covariates group-specific.

## What residual co-variation means — and what it does not

Because both the line mean and the drug-dose mean are removed, only the residual is used. The question the
slope answers is:

> For a given cell line under a given drug at a given dose, when that line's MG53 deviates from what the
> line and the drug-dose would predict, does the outcome deviate in the same direction?

It is emphatically **not** "do drugs that raise MG53 also raise p53 targets". That question is answered by
the raw correlation, and the answer is yes — which is exactly why the two-way version is the one to read.

> [!warning] Residual co-variation is not mechanism, and the study has a demonstration
> In a within-drug-dose/within-line coupling model (n = 51,165, 49 lines × 1,086 drug-doses), MG53 tracks a
> line's own p53 output at **+0.0923 log2 per unit `P53_SCORE`** [+0.031, +0.154] — and its locus
> neighbour **PYCARD-AS1 matches it at +0.0829**, while in the 10 core p53-null lines, where p53 cannot
> act, **[[CDKN1A]] still couples at +0.5112** (p 0.0005) [`verify_p53_regulates_1/v11_coupling.csv`]. A
> statistic that fires at +0.51 where it must not cannot license "if p53 drove MG53 the coupling would be
> present in one arm and absent in the other". That argument was withdrawn; see
> [[Corrections and retractions]].

## Why the raw correlation collapses

The ladder in Table A of `MG53_p53_TABLES.md`, in the 17 TP53-wild-type lines — the same data with
progressively more removed:

| p53 read-out | raw *r* | within-line | within-drug-dose | **two-way** *r* | two-way slope (95% CI) |
|---|---|---|---|---|---|
| [[p53 program P]] (180 genes) | +0.091 | +0.093 | +0.009 | **+0.013** | +0.0009 (−0.0014, +0.0032) |
| Program P repression arm (15) | +0.015 | +0.017 | −0.002 | **+0.000** | +0.0000 (−0.0072, +0.0073) |
| CollecTRI TP53 targets (612) | +0.194 | +0.197 | +0.068 | **+0.074** | **+0.0029 (+0.0006, +0.0051)** |
| Curated 21-gene `P53_ACTIVITY` | +0.074 | +0.075 | −0.008 | **−0.007** | −0.0011 (−0.0050, +0.0029) |
| Curated p53 primary targets | +0.031 | +0.031 | −0.019 | **−0.018** | −0.0039 (−0.0092, +0.0014) |
| Curated p53 all targets | +0.047 | +0.048 | −0.021 | **−0.020** | −0.0036 (−0.0080, +0.0007) |

**Read the columns, not the rows.** Removing the cell line changes nothing — every `within-line` value is
within 0.003 of its raw value. Removing the drug-dose destroys the association in every row. The raw
positive correlation is therefore drugs that move MG53 and p53 targets together, not MG53 moving p53
targets. The single interval that excludes zero is **positive**, which is the wrong sign for any account in
which MG53 restrains p53.

The same arithmetic on a different nuisance dimension gives the same lesson: [[MDM2]]'s level correlation
with MG53 is **−0.614** pooled across exposures and **+0.074** once plate medians are removed
([[Plate batch effects]]). Pooling across a nuisance dimension is how a nuisance becomes a finding.

The surviving within-drug-dose association, such as it is, is **p53-genotype-independent**: in the
committed primary model (53,084 rows, 47 lines, drug-dose × gene fixed effects) `p_diff_twoway` is 0.2855,
the TP53-label permutation p is 0.3038, and the observed difference is **31% of its MDE and wrong-signed** —
the *altered* lines show the slightly stronger coupling [`genome_wide/tables/c_program_models.csv`, row 0].
That is the signature of a shared drug response, not of p53 arbitrating anything.

## The cost: inference on few clusters

Removing fixed effects is free; the standard error is not. Rows are not independent — they share a line and
they share a drug — so the SE must be clustered on both, and the number of **clusters**, not rows, sets the
degrees of freedom.

| | Rows | Design effect | n_eff | df |
|---|---|---|---|---|
| All lines | 53,331 | 14.8–15.1 | 3,527–3,597 | 48 lines |
| 11 p53-functional lines | 12,448 | 6.9–7.5 | 1,650–1,813 | **10** |
| 10 core p53-null lines | 11,315 | 2.4–2.7 | 4,265–4,738 | **9** |

The two-way (drug, line) cluster SE runs about **3.9× the iid SE**, and the arm fits are referred to a *t*
with min(drugs, lines) − 1 = **10 df**. Three cautions, all of which bit in practice:

1. **n_eff invites exactly the misreading it is meant to prevent.** n_eff = 4,265 for the 10 p53-null lines
   *exceeds* n_eff = 1,650 for the 11 functional lines. That reflects a more homogeneous within-line
   association, not better power. With G = 9–10 clusters, no n_eff fixes the reference distribution.
2. **At G = 10–11 the analytic cluster-robust *t* referred to t(G−1) is anti-conservative.** A wild cluster
   bootstrap over lines (2,000 Rademacher draws, null imposed) gives critical |t| of **2.412** (11 lines)
   and **2.321** (10 lines) against the analytic 2.228 and 2.262 — widening the subgroup MDEs by
   **18–20%** [`verify_variance_1/q6_wildboot.csv`].
3. **Three committed intervals stop excluding zero once that is done**, and are listed in
   [[The measurement with controls]]: arm C over all drug-doses +0.304% (+0.022, +0.587) → (**−0.022**,
   +0.632); arm C on p53-activating drug-doses +0.430% (+0.048, +0.814) → (**−0.091**, +0.954); arm D on
   p53-activating drug-doses +0.225% (+0.007, +0.443) → (**−0.103**, +0.553). Logged in
   [[Corrections and retractions]].

### The analytic p is not usable on its own

The step's own calibration gives **λ_common = 4.4436** where 1.0 is correct: the analytic two-way SE does
not absorb the line-level structure, so the statistic is inflated about 4.4× and `q_common` must not be read
as a *p* value. Deflating a *t* by √4.44 is the pessimistic reading available for any single gene. But
matched placebo exposures show the **same inflation or more** (median λ 5.518 expression-matched, 4.685
response-matched), so the inflation belongs to line-level structure rather than to MG53 — see
[[FDR calibration and the inflated null]] and [[Placebo genes and reference families]].

The null matters more than the *p* does. A within-drug-dose exposure shuffle is **too tight** — its null SD
is 0.47× the quoted SE in arm A, 0.19× in arm C, 0.80× in arm D — because permuting MG53 across lines
inside a drug-dose destroys the line-level structure the line fixed effect would otherwise absorb. A
**whole-line exposure permutation**, which reassigns each line's entire MG53 trajectory to another line of
the same arm, is calibrated (0.94× / 0.54× / 0.90×) and reproduces the clustered SE. Read the line
permutation. See [[Nulls and calibration]].

## What the design can detect under it

| Unit | 80%-power MDE, program change per doubling of measured MG53 |
|---|---|
| Pooled, 49 lines | **0.18%** |
| 11 functional-p53 lines | **0.32–0.37%** |
| 10 core p53-null lines | **0.11–0.12%** |

Feasible pooled; subgroup inference needs the wild bootstrap. These MDEs are what the study's bound —
effects above roughly **0.4–0.6% of p53 output per doubling of measured MG53 are excluded** — is built
from; see [[What this study found]]. On the true-MG53 scale they widen by the factor discussed in
[[Reliability and disattenuation]], which is a range and not a number.

## Two practical notes

- **The estimand excludes anything that acts through drug choice.** Removing the drug-dose mean also
  removes a real uniform MG53 effect that happens to be delivered by the drug. The two-way slope is a
  within-cell deviation slope and should be quoted as one. Where a cleaner design exists, use it: the arm
  contrast `D_j` = mean(MG53 | functional) − mean(MG53 | null-core) is a **within-well** contrast across
  pooled lines and so cancels plate batch, dose, well and overall response amplitude at first order.
  *(That substitution was a declared deviation that was not declared — PRESPEC specifies the fixed-effects
  regression — but it was verified benign: the literal two-way FE gives β_INT +0.787 against the contrast's
  +0.800, a 1.7% difference.)*
- **Centring must be per well.** Residualising on the pooled drug-dose fixed effect before pairing wells
  forces the two wells anti-correlated and yields a negative σ²_DL. This is the detail a replicator most
  needs; see [[Reliability and disattenuation]].

## Links

- [[The measurement with controls]] — the central result, fitted this way, arm by arm
- [[Why MG53 is hard to measure here]] — the noise in the exposure this estimator uses
- [[Plate batch effects]] — the same collapse on the plate dimension
- [[Reliability and disattenuation]] — converting the slope to the true-MG53 scale
- [[Nulls and calibration]], [[FDR calibration and the inflated null]],
  [[Placebo genes and reference families]], [[Cross-fitting and circularity]]
- [[Downstream of MG53]], [[What this study found]], [[Corrections and retractions]]
- [[p53 program P]], [[Per-line p53 function]], [[TRIM72]], [[MDM2]], [[CDKN1A]]

## Sources

- `mg53_p53/findings/MG53_p53_TABLES.md` — Table A (the collapse ladder), and the `b_common` model
  definition with its λ_common calibration.
- `/tmp/claude-0/-home-user-Tahoe100-PseudoManual/6ff0eb71-456e-5d8b-af99-308c7803f336/tasks/w2dbqis5h.output`
  — *Upstream of MG53*, §§2.5, 2.7, 3.1, 3.5, 3.7, 6.3.
- `mg53_p53/findings/MDM2_MG53.md` — Table 2, the pooled-versus-within-plate decomposition.
- `genome_wide/genome_wide.py` section C; `genome_wide/tables/c_program_models.csv`,
  `c_calibration.csv`; `verify_variance_1/q6_wildboot.csv`;
  `verify_p53_regulates_1/v11_coupling.csv`.
