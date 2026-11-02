---
type: method
tags: [method, statistics, nulls, permutation, calibration]
status: current
---

# Nulls and calibration

> [!summary] In one line
> The screen's analytic q value is wrong by a factor of 4.4 on the common slope, so every per-gene verdict
> rests on a permutation null instead — and the three nulls available are each valid for a different
> statistic, which is the single easiest thing to get wrong in this project.

This note is the mechanics: how each null is built and what it may be used on.
[[FDR calibration and the inflated null]] is what the inflation does to the conclusions.

## The analytic q, and why it is wrong here

`q_common` is BH over the 16,642 tested genes, on a *t* built from the conservative two-way (compound, line)
cluster SE ([[The screen model]]). The run checks that statistic against its own nulls and reports
λ = median *t*² / 0.4549, the median of *t*² under a correct null
[`genome_wide/genome_wide.py`:146, `LAMBDA_NULL`]. λ = 1 means calibrated.

| Statistic | λ | Genes at q < 0.1 |
|---|---|---|
| **common slope, observed** | **4.444** | **4,500 of 16,642 (27.0%)** |
| genotype difference, observed | 0.963 | 0 of 16,642 |
| common slope, exposure shuffled | 0.861 | 0, every replicate |
| common slope, response-matched placebos | 4.685 | median 3,196 (897 to 5,344) |
| common slope, expression-matched placebos | 5.518 | median 5,331 (2 to 8,381) |

[`genome_wide/tables/c_calibration.csv`, `lambda_common`/`lambda_diff`/`N_q01_common`]

So the common-slope statistic is about **4.4× too large on the test-statistic scale**. The cause is
structural, not a bug: the analytic two-way SE does not absorb the line-level structure in the exposure — a
line's consistent response across drug-doses — and that structure is shared between exposure and outcome.
The genotype difference is fine at λ 0.963, because differencing the two group slopes cancels what inflates
them.

Two readings follow, and both are needed. The **count** reading: 4,500 genes "passing" is 27% of the
genome, so passing means nothing on its own. The **placebo** reading: matched real genes put in MG53's place
inflate the same way or worse, so the inflation is a property of the model, not of MG53
([[Placebo genes and reference families]]).

## Null 1 — the exposure shuffle (the common slope's null)

**How it is built.** The exposure is shuffled **across lines within each drug-dose × TP53-group cell**, the
model is refitted, and the gene's observed |*t*| is compared against the pooled |*t*| of every gene in every
shuffle. That gives `p_xperm_pooled_common` and `q_xperm_common`, and the same shuffles serve
`p_xperm_pooled_diff`. Shuffles are fitted five at a time on one fixed-effect solve
[`genome_wide/genome_wide.py`:145, `XPERM_BATCH`; section C].

**What it is valid for: the per-gene studentised *t*, and nothing else.** This is stated in the script and
is worth restating because it reverses the usual intuition. The shuffle *destroys* the exposure's
line-level structure, so the permuted exposure carries more residual variance than the real one. For a
studentised *t* that is fine — the two-way SE carries that structure, so it shrinks with it, and the ratio
stays calibrated (λ 0.861). For an **unstudentised** statistic, or a **set-level** statistic, it is
anti-conservative and is not reported as a test
[`genome_wide/genome_wide.py` section C; `c_set_tests.csv` documentation].

This is why `q_xperm_common` is the verdict column (`mg53_verdict_common` reads it at < 0.1) while the
genome-wide shuffle count of 0 genes is **not** quoted as evidence that MG53 has no hits: the shuffles break
the exposure's structure by construction, so 0 is what they must give.

The same trap caught the sibling step. `two_way`'s within-cell permutation p (`p_*_perm_within_dd`) is
unstudentised, stays in `c_program_models.csv` as a record of within-cell noise, and is deliberately absent
from `key_results.csv` and the findings. [[The measurement with controls]] shows what it costs empirically:
the within-drug-dose shuffle's null SD is 0.47× the quoted SE in the functional arm and 0.19× in the
low-activity arm, against 0.94× and 0.54× for a whole-line permutation that keeps each trajectory intact.

## Null 2 — TP53 relabelling (the genotype difference's null, and only that)

**How it is built.** The TP53 wild-type / altered labels are permuted over the analysed lines, with the
**same permutation used for every gene**, so the gene–gene correlation structure survives. Because the
fixed effects themselves depend on the labels under `ddxg`, the whole model is refitted per relabelling
[`two_way/two_way.py`:697, `label_perm_ddxg`]. Two p values come out:

| Column | Built from | Resolution |
|---|---|---|
| `p_label_pooled_diff` → `q_label_diff` | the gene's \|t_diff\| against every relabelling × gene | fine |
| `p_label_own_diff` | the gene's **own** relabellings only | coarse — floor 1/21 = 0.048 |

[[FDXR]] is the worked example of the floor: its own-gene relabelling p sits at 0.048 and cannot go lower,
which is why a nominal p_diff of 0.0135 reads as nothing once multiplicity is applied (q_diff 0.999)
[`c_screen_genes.csv.gz`, `p_label_own_diff`/`q_diff`].

> [!warning] Relabelling is **not** a null for the common slope
> The common slope is fitted across both groups. Permuting the labels reshuffles which lines are called
> wild-type but leaves every line's own MG53-to-outcome association exactly as it was — the thing the common
> slope measures. The statistic is essentially unchanged by the permutation, so the p value would come out
> meaninglessly small. The script says so in both places it could be misapplied: the `c_calibration.csv`
> rows note that relabelling "keeps the within-line association, so it is NOT a null for the common slope",
> and `c_set_tests.csv` gives the common slope no permutation p at all
> [`genome_wide/genome_wide.py`:2185, :2213-2220].

The asymmetry is worth holding onto: **relabelling tests `diff`, shuffling tests `b_common`**, and each is
invalid for the other's job.

## Null 3 — the placebo families

**How they are built.** Real genes, chosen **before any fit and without looking at any outcome**, are put
in MG53's place as the exposure and the whole screen is refitted. Two families, matched on different axes
[`genome_wide/genome_wide.py` section C; `c_placebos.csv`]:

| Family | Matched on |
|---|---|
| expression-matched | log2 median line CPM, lines expressing, share of finite cells |
| response-matched | share of keep drug-doses with \|DD_z\| ≥ 3, residual SD after the fixed effects, lines expressing |

Candidates exclude the exposure, the readthrough covariates, and any gene in a data-derived programme; the
curated overlays play no part in the selection. Each placebo's own gene and the exposure are left out of its
own fit.

**What they answer that no permutation can.** A permutation asks "is this bigger than noise?". A placebo
asks "is MG53 special among genes like it?" — the question that actually matters once λ is 4.4, because the
inflation is shared. The answer across the screen is no: MG53's 4,500 genes at q_common < 0.1 sit inside
both placebo ranges [`c_calibration.csv`, `N_q01_common`].

> [!important] The resolution limit: **0.1**
> `c_placebos.csv` holds 200 placebo exposures at the genotype split, but the **per-gene** screen carries
> only **10 per family**. So `placebo_pct_common_*` and `placebo_pct_diff_*` are the share of 10 values
> below the gene's *t*, and the smallest step is 0.1. A 0.0 or a 1.0 there means "most extreme of ten" —
> an empirical two-sided p of about 2/11 — not a p value, and it cannot support a claim on its own
> [`MG53_p53_TABLES.md`, column glossary].

Where the placebo percentiles *are* informative is in a pattern across many genes. Among the 29 canonical
effectors, genes land in the outer tenths in **both directions at once** — [[CDKN1A]] 0.9/1.0, PMAIP1
1.0/1.0, AEN 1.0/1.0, BTG2 1.0/1.0 at one end; [[MDM2]] 0.1/0.0, [[DDB2]] 0.1/0.0, TP53I3 0.0/0.0 at the
other. That is the signature of MG53 tracking overall transcriptional response amplitude, which makes it a
better predictor than a matched gene for *any* responsive gene in whichever direction that gene happens to
move [`MG53_p53_TABLES.md`, Table D placebo reading].

## The permutation FDR used in the programme derivation

[[Program P derivation]] uses a fourth construction, which is not one of the three above: each permuted
labelling is treated as the truth and calibrated against the other permutations, the observed z is given a
pooled one-sided p against all of them, and BH is taken over that. It keeps the skew of the permutation null
and the fact that every drug-dose shares one labelling [`genome_wide/genome_wide.py` section B]. It is a
selection rule, not a test of MG53, and nothing in the MG53 block uses it.

## Which null for which statistic — the summary

| Statistic | Valid null | Column | Not valid |
|---|---|---|---|
| per-gene `b_common` studentised *t* | exposure shuffle | `q_xperm_common` | TP53 relabelling; analytic q |
| per-gene `diff` | TP53 relabelling | `q_label_diff` | — |
| set / programme-level common slope | none available | camera-style test only | exposure shuffle (anti-conservative), relabelling (leaves it unchanged) |
| set / programme-level `diff` | TP53 relabelling | `p_null_calibrated` | exposure shuffle |
| "is MG53 special?" | placebo families | `placebo_pct_*` | any permutation |
| arm-level slopes in the controlled measurement | whole-line exposure permutation | — | within-drug-dose shuffle |

The one gap in that table is real and should be stated plainly: **the programme-level common slope has no
permutation null.** It has the camera-style set test and the placebo families, and that is all
[`c_set_tests.csv`].

## Links

- [[FDR calibration and the inflated null]] — what λ 4.44 does to every per-gene reading
- [[Placebo genes and reference families]] — the families in detail, and the family-definition error that
  was corrected
- [[The screen model]] · [[Program P derivation]] · [[How the numbers are decided]] ·
  [[Two-way fixed effects]]
- [[The measurement with controls]] — the two nulls that disagree there, and why the calibrated one wins
- [[Corrections and retractions]] · [[Methods — Map of Content]]

## Sources

- `mg53_p53/genome_wide/genome_wide.py` — module docstring section C (which null applies to which
  statistic); `LAMBDA_NULL` and `XPERM_BATCH` at lines 145-146; the `c_calibration.csv` and
  `c_set_tests.csv` column documentation at lines 2180-2222.
- `mg53_p53/genome_wide/tables/c_calibration.csv` — one row per replicate per null kind: `observed`,
  `tp53_relabelling`, `exposure_shuffle`, `placebo_expression`, `placebo_response`, with `N_q01_common`,
  `N_q01_diff`, `lambda_common`, `lambda_diff`; plus `p_count` = (1 + replicates at or above the observed) /
  (1 + replicates).
- `mg53_p53/genome_wide/tables/c_placebos.csv` — the 200 placebo exposures with their family, rank, matching
  features and primary-model fit.
- `mg53_p53/two_way/two_way.py` — `label_perm_ddxg` (line 697) and the within-cell shuffle (line 597).
