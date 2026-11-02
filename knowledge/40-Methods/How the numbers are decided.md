---
type: method
tags: [method, provenance, reproducibility, meta]
status: current
---

# How the numbers are decided

> [!summary] In one line
> Every number in this project is one of three kinds — read straight off a pipeline table, recomputed from
> exported per-cell values, or derived by hand — and the kind decides what the number may be used to claim,
> which is a different question from whether it is correct.

> [!note] Not the same tiers as the gene notes
> [[How this vault is built]] also uses "tier 1/2/3", for how much *written attention* a gene gets. That is
> an editorial scale. This note's tiers are about **where a number came from**. A tier-1 gene can quote a
> tier-3 number and usually does.

## The three tiers

| | Tier 1 — read off a table | Tier 2 — recomputed | Tier 3 — derived by hand |
|---|---|---|---|
| **Source** | a committed pipeline CSV | exported per-cell / per-gene values, re-aggregated | a formula applied to tier-1 or tier-2 inputs |
| **Written as** | `[c_screen_genes.csv.gz, b_common]` | `[... ; recomputed]` | `[... ; bound recomputed]`, or the step spelled out |
| **Reproducible by** | re-reading the file | re-running the aggregation | redoing the arithmetic from stated inputs |
| **Fails by** | being the wrong statistic | lacking a calibrated null | its model assumption being wrong |
| **Use it to** | quote an estimate, an SE, a q | count, compare, describe a pattern | **exclude** an effect size |

### Tier 1 — read straight off a pipeline table

A number copied from a committed CSV, with the file and the column named. `b_common` −0.0050 for [[MDM2]]
`[genome_wide/tables/c_screen_genes.csv.gz, b_common]`; λ 4.444
`[genome_wide/tables/c_calibration.csv, lambda_common]`; arm A's slope +0.00137
`[mg53_p53/findings/tables/mg53_to_p53_effect.csv]`; the fold change 1.255×
`[b_p53_program_genes.csv.gz, wt_mean_log2]`.

Tier 1 is as reproducible as this project gets. Each step is deterministic and seeded (`SEED` 20261030),
the gzip outputs are byte-identical across runs of the same data, and the committed `*/tables/*.csv` are a
**regression reference** a fresh run compares itself against table by table. The last full run came back 125
identical, 23 close, 22 differing, the differences being documented numerical and scope changes
([[Methods — Map of Content]]).

> [!warning] Tier 1 means reproducible, not valid.
> `q_common` is tier 1 and is also 4.4× inflated on the test-statistic scale
> ([[FDR calibration and the inflated null]]). Reading a number off the right file does not make it the
> right statistic. The commonest error in this project is a correctly-cited tier-1 q used as a p value.

### Tier 2 — recomputed from exported per-cell or per-gene values

The pipeline exports per-(drug-dose, line) and per-gene values; a tier-2 number re-aggregates them to answer
a question no table answers directly. In [`mg53_p53/findings/MG53_p53_TABLES.md`] these carry the word
**recomputed** in their bracket. Examples:

- the induction arm's fold-change range, 1.001× to 1.255×, median 1.060×
  [`b_p53_program_genes.csv.gz`, `wt_mean_log2`; recomputed]
- Spearman(`z_program`, `wt_mean_log2`) within P = 0.552 [same file; recomputed]
- median |`b_common`| by expression bin: 0.0140 below 1 CPM down to 0.0027 above 64
  [`c_screen_genes.csv.gz`; recomputed]
- 61 of the 100 top MG53 partners carry readthrough geometry against 9.5% among tested genes at matched
  expression — a 6.4× enrichment [`c_screen_genes.csv.gz`, `dog_class`; recomputed]
- the signed tally, 35 toward more p53 output against 32 toward less
  [`tableD_signed_tally.csv`; [[Signing genes by p53 direction]]]
- the same-well versus cross-well slopes in [[The measurement with controls]]
  [`w3_same_vs_cross_well.csv`, recomputed]

Tier 2 is where this project's best arguments live, because the patterns that decide the question — hit
rates matching the genome-wide base rate, slopes landing in both directions at once, the readthrough
enrichment — are all re-aggregations. None of them is a single table row.

> [!important] A tier-2 interval that "excludes zero" is **provisional until its null is calibrated.**
> A recomputation can be given a conventional standard error and a 1.96 multiplier in a few lines, and that
> interval is not a test in this design. Two live examples, both flagged in the source document and
> deliberately **not** reported as findings: the CollecTRI read-out at +0.0029 (+0.0006, +0.0051) and the
> low-p53-activity mutants at +0.0043 (+0.0004, +0.0082), both on cell-line-clustered SEs over 14 to 28
> lines, neither run through the label-permutation and placebo machinery the pipeline applies to its primary
> test [`MG53_p53_TABLES.md`, Tables A and C and their shared caveats].
>
> And three intervals that stopped excluding zero once the SE was corrected from CR0 cell-line to two-way
> (drug, line) CR1 on 10 df: arm C over all drug-doses, +0.304% (+0.022, +0.587) → (**−0.022**, +0.632);
> arm C p53-activating, (+0.048, +0.814) → (**−0.091**, +0.954); arm D p53-activating, (+0.007, +0.443) →
> (**−0.103**, +0.553) — see [[The measurement with controls]] and [[Corrections and retractions]].

The rule that follows: **a tier-2 interval is a finding only once a null built for it exists** — the
exposure shuffle, a whole-line permutation, a relabelling, or a placebo family, whichever is valid for that
statistic ([[Nulls and calibration]]).

### Tier 3 — derived or bounded by hand

A formula applied to tier-1 or tier-2 inputs, with the inputs and the formula both stated. These are
mostly bounds, and they are the form the study's actual claim takes.

| Number | How it is built | Inputs |
|---|---|---|
| per-gene detectable-effect bound: \|diff\| ≥ 0.029 log2 = **+2.0% per doubling of measured MG53** at 80% power | p ≤ 0.1/16,642 → \|t\| ≥ 5.11 at df 46, times the median `se_diff` 0.0048 | `c_screen_genes.csv.gz`, `se_diff`/`df` |
| the same on the common slope | +1.0% measured | `se_common` |
| **per doubling of true MG53**: +7.1% (diff), +3.7% (common) | ÷ split-half reliability 0.289 | `two_way/tables/trim72_reliability.csv` |
| that bound as 1.43× the median programme gene's whole genotype effect (0.070 log2) | a ratio of the two above | both |
| MDE80 +0.357% for arm A | CR1 SE × few-cluster multiplier *t*(.975,10) + *t*(.80,10) = 3.11 | `w1_arm_slopes.csv` |
| deflating a *t* by √λ: MDM2 −2.51 → −1.19, p ≈ 0.24 | √4.444 | `c_calibration.csv` |
| "the effective sample is 11 to 17 lines" | the functional-p53 count, not the 50-line panel or the 53,331 rows | `p53_nullification.csv` |

> [!warning] A tier-3 bound is a statement about **what could not have been seen**, never an estimate.
> Disattenuating by 0.289 does not produce a better number for true MG53; it widens a bound. The classical
> correction needs exposure and outcome errors to be independent, and the cross-well test shows the
> association is same-well only — exactly the case where that assumption fails. The divisor is a range, not
> a point: the `ii_active` variant of the same split-half gives 0.610, which would halve the correction
> [`trim72_reliability.csv`; [[Reliability and disattenuation]]].

## Which tier to trust for what

| Question | Tier to use |
|---|---|
| "What is the slope / the q / the fold change for gene X?" | **1**, with the column named |
| "How does this gene compare with the genome, or with the other arm?" | **2** |
| "How big could the effect have been and still gone undetected?" | **3** — this is the study's claim |
| "Does this interval exclude zero?" | 1 or 2, **and only with a calibrated null beside it** |
| "Is MG53 special?" | neither a tier-1 q nor a tier-2 count — the placebo families ([[Placebo genes and reference families]]) |
| "Does MG53 change p53 output?" | no tier answers it; [[Tahoe-100M]] has no MG53 perturbation |

The study's headline is a **tier-3 bound on tier-1 and tier-2 inputs**: in TP53-wild-type lines, more MG53
mRNA shows no detectable association with p53 target output or p53-driven arrest, with effects above roughly
0.4–0.6% of p53 output per doubling of measured MG53 excluded ([[What this study found]],
[[The measurement with controls]]). Stated as a bound it is defensible; stated as "MG53 has no effect on
p53" it is an overstatement of the same evidence, and stated as "MG53 damps p53" it contradicts it —
[[CDKN1A]] and [[MDM2]] move in **opposite** directions ([[Downstream of MG53]], [[MDM2 and MG53]]).

## House rules this implies

1. **Name the file and the column, or say "recomputed", or show the formula.** A number with no bracket is
   a number nobody can check.
2. **Quote the interval, not the point estimate.** And no p value without its effect size next to it.
3. **Name the null.** "q 0.031" is incomplete; "`q_xperm_common` 0.031" says which null, and
   [[Nulls and calibration]] says whether that null is valid for that statistic.
4. **Mark a tier-2 interval as provisional** until a calibrated null for it exists, however small the p
   value looks.
5. **Never present a tier-3 disattenuated figure as an estimate.** Write it as a bound, with the divisor
   and its range.
6. **When a published number is corrected, keep both.** [[Corrections and retractions]] is the ledger, and
   where the committed text and a reanalysis disagree the note says which one wins and why.

## Links

- [[The screen model]] — where the tier-1 per-gene numbers come from
- [[Nulls and calibration]] · [[FDR calibration and the inflated null]] ·
  [[Placebo genes and reference families]] — what makes an interval a test
- [[Program P derivation]] · [[Cross-fitting and circularity]] — a column can be tier 1 and still unable to
  test what it looks like it tests
- [[Reliability and disattenuation]] · [[Two-way fixed effects]]
- [[How this vault is built]] · [[Corrections and retractions]] · [[Tables — what the study produced]] ·
  [[Methods — Map of Content]] · [[Home]]

## Sources

- `mg53_p53/findings/MG53_p53_TABLES.md` — the provenance brackets this taxonomy formalises; every
  "recomputed" marker is a tier-2 number and every "bound recomputed" a tier-3 one.
- `mg53_p53/findings/make_tables.py` — the tier-1 generator for Tables A–D (`fit()` carries the
  cell-line-clustered SE whose intervals the caveats qualify).
- `mg53_p53/genome_wide/tables/c_screen_genes.csv.gz`, `c_calibration.csv` — the per-gene and calibration
  inputs.
- `mg53_p53/two_way/tables/trim72_reliability.csv` — the disattenuation divisors, 0.289 and the 0.610
  variant.
- `mg53_p53/findings/tables/mg53_to_p53_effect.csv` plus the reanalysis tables listed in
  [[The measurement with controls]] — the arm-level numbers and the three corrected intervals.
