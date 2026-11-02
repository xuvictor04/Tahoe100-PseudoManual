---
type: method
tags: [method, statistics, regression, screen]
status: current
---

# The screen model

> [!summary] In one line
> One regression, fitted once per gene over all 16,642 expressed genes, is where every per-gene number in
> this study comes from — and its central output, `b_common`, means "log2 of the outcome gene per doubling
> of measured MG53, within line, across drugs".

## The equation

From `genome_wide/genome_wide.py` section C, which calls `two_way`'s `ddxg` model:

```
Y_gene = (drug-dose x TP53-group fixed effects)
       + (line fixed effects)
       + b_WT  x MG53 x 1[line is TP53 wild-type]
       + b_alt  x MG53 x 1[line is TP53 altered]
       + (covariates x TP53 group)
```

Unweighted OLS. `b_common` is the same model with the two slopes constrained equal — one slope for all
lines — while the fixed effects and the covariates stay group-specific. So three slopes come out of two
fits: `b_WT`, `b_alt`, their difference `diff = b_WT − b_alt`, and `b_common`.

### What Y and the exposure are

Both sides are the same quantity, for different genes, in the same cell of the design. A "cell" is one
(drug-dose, line) pair; there are 53,331 of them with usable data, over 49 lines and 1,132 drug-doses
[`genome_wide/tables/c_screen_genes.csv.gz`, `n_rows`/`n_drugdoses`; `MG53_p53_TABLES.md` header].

| | What it is |
|---|---|
| **Y** (outcome) | the gene's corrected log2 effect `r2` for that (drug-dose, line): log CPM of the line's profiles in each well, minus **that plate's drug-well median for that same line**, minus the composition shift, minus the atlas position effect (W1 − W2), averaged over the drug-dose's used wells |
| **X** (exposure) | [[TRIM72]]'s `r2` for the same cell, built the same way — see [[Why MG53 is hard to measure here]] for what that costs at 5 UMIs per profile |

The baseline is a drug well of the same line on the same plate, not vehicle and not untreated cells
[`genome_wide/genome_wide.py` section A; `export/README.md`, `r2`]. At programme level the DMSO-referenced
version runs 0.025 log2 higher
[`export/downstream/program_scores_per_drugdose_line.csv`, `P_r2_mean` vs `P_u_dmso_mean`].

## Why the fixed effects are shaped this way

**`ddxg`, not `dd`.** The pipeline supports two structures and reports both. `dd` gives each drug-dose one
mean; `ddxg` gives each drug-dose **its own wild-type mean and its own altered mean**, so a line is only
ever compared with lines of the same TP53 group under the same treatment. The reason is a baseline gap: if
wild-type and altered lines differ in level, `dd` lets that gap leak into the genotype contrast, and the
TP53-label permutation does not protect against it because permuting the labels breaks the gap too
[`two_way/two_way.py`:18-21]. The cost is real and visible — `two_way`'s own example moves `P53_SCORE`'s
`t_diff` from −10.4 under `dd` to −3.2 under `ddxg` [`two_way/two_way.py`:1445].

**Line fixed effects** remove each line's own average, so nothing in the estimate comes from lines
differing in their resting MG53 level. Together with the drug-dose cells, that is a two-way projection:
only residual co-variation survives, i.e. *for a given line under a given drug, does the gene deviate from
its expected level in the same direction MG53 does?* See [[Two-way fixed effects]] for what that removes
and what it leaves exposed.

**The design is smaller per gene than it looks.** `n_drugdoses` is 1,132 for every tested gene, but after
pruning the 195 programme genes contribute 11 to 17 wild-type and 22 to 30 altered lines (median 17 and 30)
at a median df of 46 — not the panel's 17 and 33
[`c_screen_genes.csv.gz`, `n_lines_WT`/`n_lines_alt`/`df`]. Inference is a 6-to-30-cluster problem
throughout.

## The covariate sets

Each set is entered **per TP53 group**, and every primary set is data-driven; the one curated set is
labelled as such and has list-free twins [`genome_wide/genome_wide.py`:128-136, `COVSETS`].

| Set | Members | Role |
|---|---|---|
| **`gw`** | `DD_beta` (the drug-dose's consensus response, 0 where it has none), `DD_A` (relative abundance), `resp_bg` (the line's mean \|r2\| over atlas genes **outside every data-derived programme and the exposure**) | **primary** — list-free |
| `gw_all` | `gw` with `resp_all` in place of `resp_bg` (mean \|r2\| over *all* genes) | sensitivity. `resp_all` contains the p53 programme in wild-type lines under p53 activators, so it can absorb part of `b_WT` — which is why it is not primary |
| `gw_pc` | `gw` + the line's scores on the top 3 genome-wide components (atlas W2 SVD) | sensitivity. This is the set under which [[FDXR]]'s genotype difference halves |
| `curated_cycle` | `DD_beta`, `DD_A`, `resp_bg` + the Tirosh S and G2M modules | sensitivity — **labelled, curated**; the bridge to `two_way`'s primary row |
| `gw_rt` | `gw` + the readthrough covariates (for TRIM72: [[FUS]] and PYCARD-AS1 `r2`) | the only columns that adjust for [[Readthrough spillover]]. **No programme column does** |
| `none` | — | sensitivity |

`resp_bg` is also what keeps the screen non-circular: its background gene set excludes the label-selected
programmes, so nothing in the MG53 block was chosen using the TP53 labels
([[Cross-fitting and circularity]]).

## `b_common`, in words and in units

> [!important] `b_common` is the **log2 change in the outcome gene per doubling of measured MG53**, at equal
> drug-dose × TP53 group and equal cell line — i.e. within line, across drugs, one slope shared by all
> lines. +1 would mean the gene doubles when measured MG53 doubles.

Two consequences of those units.

**They are small by construction, so read them as percentages.** `b_common` = 0.0104 for [[CDKN1A]] is
2^0.0104 − 1 = **+0.72% of p21 per doubling of MG53** — the largest slope among the 29 canonical effectors
[`c_screen_genes.csv.gz`, `b_common`; `MG53_p53_TABLES.md`, Table D]. That is the scale the study's bound
lives on: effects above roughly 0.4–0.6% of p53 output per doubling of measured MG53 are excluded, which is
the headline in [[What this study found]] and the measurement it rests on is [[The measurement with
controls]].

**They are not comparable across genes of different expression.** Median |`b_common`| by expression bin:
0.0140 below 1 CPM, 0.0144 at 1–4, 0.0059 at 4–16, 0.0036 at 16–64, 0.0027 above 64
[`c_screen_genes.csv.gz`, `b_common`; recomputed]. The two largest slopes in [[p53 program P]] —
GRIN2C +0.0511 and ENSG00000285901 +0.0351 — sit on genes of 2.1 and 4.7 CPM. Every slope is read next to
`median_line_cpm` and the gene's own `mde80_*` bound.

**`measured`, not true.** The exposure's split-half reliability is 0.289 full-data, so a bound on true MG53
is about 3.5× wider than the same bound on measured MG53 — and that correction is a statement about
looseness, not a better estimate. See [[Reliability and disattenuation]]
[`two_way/tables/trim72_reliability.csv`].

## Inference

`se_common` and `se_diff` are the **conservative two-way (compound, line) CR1 cluster** SE:
`sqrt(max(V_drug + V_line − V_inter, V_drug, V_line))`, i.e. never smaller than either one-way SE
[`two_way/two_way.py`:178]. `q_common` and `q_diff` are BH over the tested genes.

**The analytic q must not be read as a p value for the common slope.** The run's own calibration puts
`lambda_common` at 4.444, where 1.0 is correct, and 4,500 of 16,642 genes pass `q_common` < 0.1
[`genome_wide/tables/c_calibration.csv`]. The verdict statistic is the exposure-shuffle
`q_xperm_common` instead. `lambda_diff` is 0.963, so the genotype difference needs no such correction.
Which null goes with which statistic is [[Nulls and calibration]]; what the inflation does to every
per-gene reading is [[FDR calibration and the inflated null]].

## Which genes are fitted

A gene is `tested` when it has ≥ 50 rows, ≥ 3 lines in **each** TP53 group, ≥ 10 compounds, and the
exposure varies in both groups [`genome_wide/genome_wide.py`:140, `MIN_ROWS`/`MIN_LINES_GROUP`/`MIN_DRUGS`].
That gives 16,642 tested genes of the 16,643-gene atlas.

The exposure itself — and every placebo gene, when it takes the exposure's place — is **never an outcome of
its own fit**; its row carries `tested = False` [`genome_wide.py` section C]. Without that, MG53 would
appear as its own most significant hit.

## The primary test, declared before any real-data run

`PRIMARY` is a literal in the script, above the analysis [`genome_wide/genome_wide.py`:127]:

| Field | Value |
|---|---|
| fixed effects | `ddxg` |
| drug-doses | all 1,132 |
| covariate set | `gw` |
| outcome | `P53PROG_UP_cf` — the cross-fitted [[p53 program P]] score ([[Program P derivation]]) |
| estimand | `b_WT − b_alt` |
| inference | conservative two-way SE, with the TP53-label permutation p beside it |

Everything else in the run — the common slope of that same model included — is secondary, sensitivity,
screen, overlay or check. That matters when reading the per-gene tables: `b_common` is the number most of
the gene notes quote, and it was not the declared test.

## What this model cannot do

- **No direction of effect.** [[Tahoe-100M]] holds no MG53 perturbation, so "Y moves with MG53" and "MG53
  moves Y" are the same number here.
- **mRNA at 24 h only**, and every mean over lines is over lines that still had cells in the well.
- **The two-way projection does not remove shared measurement error inside one profile.** That is the
  channel the cross-well test isolates, and it is the leading explanation of what residual association
  remains — see [[The measurement with controls]] and [[Why MG53 is hard to measure here]].
- **Readthrough is only adjusted in `gw_rt`.** `b_common` in the primary set does not control for
  transcription running into the TRIM72 locus from 5′ neighbours ([[The TRIM72 locus]]).

## Links

- [[Two-way fixed effects]] · [[Nulls and calibration]] · [[Program P derivation]] ·
  [[How the numbers are decided]]
- [[FDR calibration and the inflated null]] · [[Placebo genes and reference families]] ·
  [[Reliability and disattenuation]] · [[Cross-fitting and circularity]]
- [[Downstream of MG53]] · [[The measurement with controls]] — what the model was used to answer
- [[Tables — what the study produced]] · [[Methods — Map of Content]]

## Sources

- `mg53_p53/genome_wide/genome_wide.py` — module docstring section C; `PRIMARY` and `COVSETS` at lines
  127-136; the `tested` thresholds at line 140; the section C table documentation at lines 2140-2200.
- `mg53_p53/two_way/two_way.py` — `se_conservative` (line 178), the `dd` / `ddxg` comparison (lines 18-21,
  1445), `FE_NAME` (line 131).
- `mg53_p53/genome_wide/tables/c_screen_genes.csv.gz` — one row per gene: every slope, SE, q and null column
  named above.
- `mg53_p53/findings/MG53_p53_TABLES.md` — "The MG53 slope columns, and why the q value needs care", and the
  column glossary of the full-programme section.
