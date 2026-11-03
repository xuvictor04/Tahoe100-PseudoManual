# Findings from the full Tahoe-100M run

Results written up from a completed `mg53_setup.sh --mode full` run. Nothing here reads Tahoe-100M itself;
everything comes from a run's output folder (`~/Tahoe-100M/mg53_p53` by default).

| File | What it holds |
|---|---|
| `MG53_p53_TABLES.md` | The three correlation tables: MG53 -> p53 targets in wild-type lines (A), what moves MG53 (B), and MG53 -> p53 split by how much p53 activity each mutant retains (C). Plus how far p53 is disabled across the panel. |
| `FINDINGS.md` | The long write-up: how the run reproduces the committed tables, upstream of MG53, downstream of MG53, how to read the 24 h snapshot, using the exported data, and what is left open. |
| `MDM2_MG53.md` | MDM2 against MG53 at every resolution the data allow: baseline across lines, exposure level and change, per line within an exposure, and the genome-wide screen. Includes the plate decomposition that explains the one large number, and the all-gene placebo that places MDM2 among ordinary genes. |
| `make_tables.py` | Regenerates every number in `MG53_p53_TABLES.md` into `tables/`. |
| `mdm2_mg53_levels.py` | Regenerates every number in `MDM2_MG53.md` into `tables/`. |
| `tables/*.csv` | The tables as CSV. |

Regenerate the tables on your own machine:

```
python3 mg53_p53/findings/make_tables.py --results ~/Tahoe-100M/mg53_p53
```

## Scope

Two questions, and only these two:

- **Upstream of MG53** — what raises or lowers MG53 expression: drugs, transcription factors, cell-line background.
- **Downstream of MG53** — what MG53's level does to p53 and to p53's output.

**Not in scope:** whether p53 regulates MG53 ("MG53 downstream of p53"). The repository's `p53_dependence`
step asks that question, so it is not drawn on here, and results that rested on it — including the
cardiac-glycoside lead — are not reported.

**A third thing, which is neither:** TRIM72 sits 10.6 kb 3' of PYCARD-AS1 and 17 kb 3' of FUS *on the same
strand*, so transcription running past those genes is counted as TRIM72 mRNA. This is called **readthrough
spillover**, never "downstream". It is a fact about position on the chromosome and about the measurement, and
it matters only because it means part of the measured MG53 signal is not MG53's own transcript.

## The short answer

- **Upstream:** MG53's expression tracks its own genomic neighbourhood far more than any transcription
  factor. Idarubicin and homoharringtonine at 5 uM raise it about 10-12x on two plates each; ponatinib and
  trametinib lower it. The muscle TFs that drive TRIM72 in its native tissue are silent or absent here.
- **Downstream:** in the TP53-wild-type lines, more MG53 shows no association with p53 target output or with
  p53-driven arrest. WT-specific effects above roughly 0.4-0.6% per doubling of measured MG53 are excluded.
  The matching bound on *true* MG53 is withdrawn: an earlier version of this bullet gave "about 1.3-2% of
  true MG53" by dividing the measured bound by a split-half reliability of 0.289, and exposure and outcome
  are counted from the same cells in the same well against the same total-UMI denominator, so that division
  has no estimand. The artefact-free quantity needs no divisor at all and is estimated directly, from
  cov(exposure in well A, outcome in well B) over 102 cross-batch replicate pairs: **+0.0074 to +0.0079
  program-log2 per doubling of true MG53 (95% CI -0.018 to +0.026)**, which is about +0.5% and not
  distinguishable from zero. The raw positive correlation is drug-driven and collapses once drug identity is
  controlled.
- **Caveat on all of it:** these are associations in 24 h mRNA. Tahoe has no MG53 perturbation and no protein
  data, every line carries wild-type MG53 at trace level, and p53 itself is functionally disabled in about
  four-fifths of the panel — so the effective sample for any MG53 -> p53 test is 11 to 17 lines.

## Per-gene tables

`tables/p53_effectors_per_gene.csv` — **the focused per-gene table**: the 29 canonical p53 effectors (the
curated 21-gene panel plus the classic effectors it omits), each with its fold change under a strong
activator, its wild-type-minus-altered difference, and MG53's slope on it. Grouped by what each gene does
once p53 is active. Start here.

**Direction first.** Every per-gene table carries `p53_direction` (induced or repressed by p53),
`p53_direction_source`, `frac_compounds_wt_up`, `direction_is_mixed` and `mg53_effect_on_p53_output`.
"Up with MG53" means *more* p53 output for a p53-induced gene and *less* for a p53-repressed one, so only
the signed column can be added across genes. Signed, the 67 program genes with a verdict split **35 toward
more p53 output and 32 toward less** — an even split, which is what a non-specific association looks like
and not what a coherent change in p53 output would look like. `tables/tableD_signed_tally.csv` and
`tables/p53_effectors_signed_tally.csv` hold the counts. And direction is not uniform: **65 of the 195
program genes, and 11 of the 29 canonical effectors, are moved up by between 35% and 65% of the 98
compounds** — BAX among them, at 54% — so for a third of the program the direction is not a fact about the
gene.

`tables/tableD_p53_target_genes.csv` — the full set: one row per gene in the data-defined p53 program (195:
180 induction arm, 15 repression arm), 67 columns, generated and documented by `table_d()` in
`make_tables.py`. Per gene it carries the p53-activation fold change, the wild-type-minus-altered
difference, cross-fitting stability (`n_folds_kept`, `loco_frequency`), MG53's slope with both the analytic
and exposure-shuffle FDR, per-gene detectable-effect bounds, and a readthrough geometry flag. The bounds to
read are the **measured**-MG53 ones; any true-MG53 column there is a reliability division of the same
quantity and carries the defect described under the short answer above. `tables/tableD_top_mg53_partners.csv`
is the other direction: the 100 genes MG53 tracks most strongly genome-wide, for contrast.

Read the fold change with care. Its baseline is **not vehicle**: it is the same line's median over that
plate's **drug wells**, and it is a compound-equal mean (each of 98 compounds carries 1/98) over the 142
p53-activating drug-doses. So a strong activator is averaged with 97 weaker ones, which is why the median
program gene reads only 1.06x. It is not the fold change under a strong p53 activator.

## Per-line p53 function

`PER_LINE_p53_FUNCTION.md` and `tables/per_line_p53_state.csv` — each of the 50 lines placed on a p53-output
axis against a null reference (the TP53-deletion and truncating lines), so a mutant can be read as retaining
activity, sitting at the null, or falling below it. Plus whether using that finer picture instead of the
yes/no genotype label changes what MG53's level does to p53. It does not.

Both a circularity-prone and a label-free version of each line's inducibility are given: program P and the
p53-activating drug-doses were selected using the TP53 labels, so `lf_P_on_LFP50_*` repeats the scoring on a
label-free program and drug-dose set. `ind_P_mean_frac_of_WT_gap` is the readable one: 1.0 means a line
reaches the wild-type median, 0.0 means it sits at the null.

| File | Contents |
|---|---|
| `tables/per_line_p53_state.csv` | 50 lines, 29 key columns: inducibility, distance from null with CI, the label-free repeat, panel responsiveness, literature-expected direction, GDSC Nutlin-3a AUC |
| `tables/per_line_p53_state_FULL.csv` | the same 50 lines with all 216 computed columns |
| `tables/tp53_mutation_annotation.csv` | per-variant annotation for the 33 mutant lines (41 rows): domain, hotspot, zygosity, reported transactivation class, dominant-negative and gain-of-function evidence |
| `tables/tp53db_variant_function.csv` | NCI/IARC TP53-database function reports per variant (25 rows) |
| `tables/wt_lines_annotation.csv` | the 17 genotype-WT lines: other routes that lower p53 (CDKN2A/ARF, MDM4, PPM1D, ATM, LKB1) |
| `tables/null_reference_lines.csv` | the lines used as the zero-p53-output anchor |

## The measurement: change in p53 activity per change in MG53, with a knockout-like control

`mg53_to_p53_effect.py` and `tables/mg53_to_p53_effect.csv`.

Tahoe has no engineered p53 knockout, but it has the next best thing: **10 lines whose only TP53 allele is
truncated, splice-disrupted or deleted outright** (KATO III is a whole-gene deletion). Those cannot mount a
p53 response, so any MG53 -> p53-activity slope measured in them is being produced by something other than
p53. That makes them the control arm. A second, softer control is the 21 mutant lines retaining <= 15% of
the wild-type-minus-null gap.

Headline, over all drug-doses: in the 11 lines with functional p53, a **doubling of measured MG53 changes p53
activity by +0.095% (95% CI -0.161% to +0.352%)**. The knockout-controlled contrast (functional minus
p53-null) is +0.050% (-0.194 to +0.295). Both are indistinguishable from zero, and the arm could have
detected +0.357% at 80% power — 3.0% of the p53 response the same arm shows to a p53-activating drug-dose,
which is measured below.

**Those intervals are corrected; the estimates are not.** An earlier version of this section gave -0.11% to
+0.30% for the headline, -0.163 to +0.264 for the contrast, and an MDE of 0.29%. The slopes are unchanged
to 1e-18: the estimate reproduced and its interval was wrong. The earlier intervals came from a CR0
cell-line standard error with a 1.96 multiplier over 6 to 21 clusters, which puts them **12-58% too
narrow** across the ten pre-specified rows; they are replaced by a per-arm CR1 factor on a conservative
two-way (drug, line) cluster with a *t* on min(drugs, lines) - 1 degrees of freedom, and the MDE by the
few-cluster multiplier t(.975,df) + t(.80,df) = 3.11 at df 10 in place of the normal 2.8016. The contrast
is now fitted **jointly**, with (drug-dose x arm) fixed-effect cells and arm-specific slopes, so its
covariance is right under drug clustering; the earlier `hypot` of two separate SEs is valid only under
cell-line clustering, where the arms share no line and the covariance is zero.

**The control arm is not distinguishable from zero either, so the comparison between arms is uninformative at
this precision.** Over all drug-doses the p53-null control reads +0.045% (-0.042 to +0.132) and the
low-activity mutants +0.304% (-0.022 to +0.632); restricted to p53-activating drug-doses the control reads
+0.225% (-0.103 to +0.553), the functional arm -0.123% (-0.857 to +0.616) and the mutants +0.430% (-0.091 to
+0.954). An earlier version of this section read the control as coming out "as large or larger than the
functional arm", on intervals that excluded zero under p53-activating drugs for both the control (given as
+0.225% with a CI of +0.007 to +0.443) and the low-activity mutants (+0.430%, +0.048 to +0.814), and it
quoted the functional arm's -0.123% with no interval at all. The point estimates are unchanged; under the
corrected standard errors every one of those intervals includes zero. None of those orderings is a
demonstrated inequality, and the argument from them is withdrawn.

The conclusion that the slope is not p53-mediated rests on two other things instead. **First, the arms are
demonstrably far apart in p53 competence**, which is the positive control: a p53-activating drug-dose minus
the rest moves the program +0.1704 log2 (+12.5%) in the functional arm — all 11 lines between +0.103 and
+0.203 — against +0.0188 (+1.3%) in the p53-null arm, and the curated 21-gene panel +24.6% against +0.2%, a
gap of roughly 10x to 100x. A p53-mediated MG53 effect of any appreciable size would have appeared as a
functional-minus-null difference. **Second, the contrast itself is flat**: +0.050% (-0.194 to +0.295) over
all drug-doses against an MDE of +0.346%, and -0.347% (-1.014 to +0.324) under p53-activating drugs. What the
measured slope tracks is overall transcriptional response amplitude and MG53's own 3' neighbourhood, not p53
output: standardised by each outcome's residual spread, MG53's association is about 6x larger with a 5-gene
stress / ISR set and 4x larger with the FUS readthrough-spillover score than with the p53 program, and it is
the same in the arm with no p53 at all. The association is also same-well only — pairing MG53 from one well
with the program score from the other well of a replicated drug-dose puts every arm at or below zero.

The CSV carries 54 rows: the pre-specified family (the p53 program in four fittable arms plus the contrast,
both scopes, 10 tests, flagged `prespecified`), the same fits on four secondary outcomes — the curated
21-gene panel and three non-p53 read-outs — and a continuous version in which the dependence on retained p53
activity is a coefficient rather than an arm. Both intervals are given per row: `lo`/`hi` is the two-way
cluster interval to quote, `lo_line`/`hi_line` the same fit clustered on cell line alone. That is the
dimension the earlier text used but not its interval: that one took this SE divided by the arm's CR1 factor
(1.05 to 1.20) and multiplied by 1.96, so `lo_line`/`hi_line` is already wider than what was published. Two
nulls are given as well, and the one to read is `p_line`, the whole-line exposure permutation, which
reassigns each line's entire MG53 trajectory to another line of the same arm; the within-drug-dose
`p_shuffle` is anti-conservative here, because permuting raw MG53 inside a drug-dose destroys the line-level
structure the line fixed effect would otherwise absorb. `pct_true` divides by that arm's group-specific
reliability (0.301 wild-type, 0.283 altered) and is **a statement about how loose the bound is, not a
corrected estimate** — the classical correction needs exposure and outcome errors to be independent, and
here they are counted from the same cells in the same well against the same total-UMI denominator.

Not computable from a run's output alone: per-arm placebo-gene pseudo-controls (a matched gene put in MG53's
place inside each arm) need per-line values for arbitrary genes, which only `export/all_genes` on the full
data provides. `genome_wide/tables/c_placebos.csv` has 200 placebo exposures at the wild-type / altered split
only.

## MDM2 against MG53

`MDM2_MG53.md`, `mdm2_mg53_levels.py`, and fifteen `tables/mdm2_mg53_*.csv`.

MDM2 is a p53 **regulator**, not a reading of p53's output — p53 induces it, and the MDM2 protein then
degrades p53 — so a link to MG53 would point toward p53 rather than away from it. It is well measured
(185.8 CPM, all 50 lines, moved up by 96 of 98 compounds) and carries the largest p53-activation fold change
of all 195 program genes.

The short answer is a small bounded association and no p53 route, with the measurement proving itself along
the way: MDM2's baseline runs **3.07x higher in TP53-wild-type lines than in TP53-altered ones**
(p 3.4e-12), exactly as the p53 feedback loop predicts, while MG53's baseline shows nothing (1.08x, p 0.77)
— so MDM2's side of every null below is sound. Across MG53 fold-change deciles MDM2 stays within 2% of 1.00
with no trend. The one large number, a -0.614 correlation between the two genes' CPM, is a plate batch
effect in full (between plate medians -0.763, within plate **+0.074**). In the unselected 16,642-gene
reference family MDM2 sits at the 36th and 60th percentiles — the middle. The screen's -0.35% per doubling
(95% CI -0.61% to -0.08%) is the smallest slope of the eight effectors that cleared the threshold.

Two things that would have been read as findings without their controls, and are documented as such: the
CPM correlation above, and the per-line genotype interaction, which reads **p 2e-06 with the wild-type slope
six times the altered one** until each exposure's mean is removed, after which it is p 0.36 — and whose
contrast gene behaves identically, including a sign flip between arms that no p53 route predicts. The
document also records seven corrections to its own earlier claims, including that its reference family was
called "all genes" when 97% of it had been selected for association with MG53.
