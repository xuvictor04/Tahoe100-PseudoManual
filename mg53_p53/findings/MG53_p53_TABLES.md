# MG53 (TRIM72) and p53 in Tahoe-100M: the correlation tables

From the full run over Tahoe-100M (50 pooled cancer cell lines, 379 drugs at 0.05 / 0.5 / 5 uM, 14 plates,
mRNA read 24 h after treatment). Every number below is reproduced by `make_tables.py` in this folder, which
writes the CSVs in `tables/`:

```
python3 mg53_p53/findings/make_tables.py --results ~/Tahoe-100M/mg53_p53
```

Basis labels: **data-defined** = genome-wide or derived from Tahoe with no curated list; **list-based** = rests
on a curated gene list. 53,331 line x drug-dose rows, 49 lines, 1,132 drug-doses.

## Scope and definitions

| Term | Meaning here | Where |
|---|---|---|
| **Upstream of MG53** | What raises or lowers MG53 expression: drugs, transcription factors, cell-line background | Table B |
| **Downstream of MG53** | What MG53's level does to p53 and to p53's output | Tables A and C |

**Out of scope:** whether p53 regulates MG53 ("MG53 downstream of p53"). No table here reports it. The
TP53 regulon and TP53-genotype rows are deliberately excluded from Table B, and the repository's
`p53_dependence` step — which tests whether MG53's induction differs by TP53 status, i.e. exactly that
question — is not drawn on. Results that rested on it, including the cardiac-glycoside lead, are therefore
not reported here.

**Not to be confused with either:** TRIM72 lies 10.6 kb 3' of PYCARD-AS1 and 17 kb 3' of FUS **on the same
strand**. Transcription running past those genes continues into TRIM72 and is counted as TRIM72 mRNA. That
is a fact about position on the chromosome and about the measurement, never a claim that anything regulates
anything. It is called **readthrough spillover** throughout, never "downstream". The orientation control
proves it is positional: the same-strand neighbours correlate with MG53 (+0.53 to +0.72) while **PYCARD**,
10.6 kb away but on the *opposite* strand, does not (-0.10).

Units: slopes are log2 of the read-out per doubling of MG53; +1 = 2x. "two-way" means both cell line and
drug-dose fixed effects are removed, so a drug's own effect on both variables is controlled. Slope intervals
are 95% with cell-line-clustered standard errors — a construction the caveats below record as 12–58% too
narrow, with one row refitted and three left unresolved.

## Table A — MG53 -> p53 target output, in the 17 TP53-wild-type lines

`tables/tableA_wt_p53_targets.csv`

| p53 read-out | basis | raw r | within-line | within-drug-dose | two-way r | two-way slope (95% CI) | direction |
|---|---|---|---|---|---|---|---|
| Data-defined p53 program P (180 genes) | data-defined | +0.091 | +0.093 | +0.009 | **+0.013** | +0.0009 (−0.0014, +0.0032) | **none** |
| Data-defined p53 repression arm (15 genes) | data-defined | +0.015 | +0.017 | −0.002 | **+0.000** | +0.0000 (−0.0072, +0.0073) | **none** |
| CollecTRI TP53 targets (612 genes) | list-based | +0.194 | +0.197 | +0.068 | **+0.074** | **+0.0029 (+0.0006, +0.0051)** | **positive** |
| Curated 21-gene P53_ACTIVITY | list-based | +0.074 | +0.075 | −0.008 | **−0.007** | −0.0011 (−0.0050, +0.0029) | none |
| Curated p53 primary targets | list-based | +0.031 | +0.031 | −0.019 | **−0.018** | −0.0039 (−0.0092, +0.0014) | none |
| Curated p53 all targets | list-based | +0.047 | +0.048 | −0.021 | **−0.020** | −0.0036 (−0.0080, +0.0007) | none |

The raw correlation is positive for every read-out, and it collapses to zero once drug identity is removed —
so it reflects drugs that move MG53 and p53 targets together, not MG53 acting on p53. The data-defined
program is flat. The only interval that excludes zero is **positive**, not negative — though that interval
uses the standard-error construction the caveats below now record as unresolved, so read it as a direction
rather than as a result.

## Table B — upstream of MG53: what moves its expression

`tables/tableB_upstream_mg53.csv` (38 rows; the strongest of each kind shown)

| Category | Driver | Statistic | Value | Direction | Basis |
|---|---|---|---|---|---|
| Readthrough spillover (positional) | PYCARD-AS1 (same strand, 10.6 kb) | r across drug-doses | **+0.722** | positive | data-defined |
| | FUS (same strand, 17 kb, 252 CPM) | r across drug-doses | +0.632 | positive | data-defined |
| | ITGAM (same strand, 28 kb) | r across drug-doses | +0.530 | positive | data-defined |
| | ITGAX (same strand, 124 kb) | r across drug-doses | +0.057 | none | data-defined |
| | **PYCARD (opposite strand, 10.6 kb)** | r across drug-doses | **−0.103** | **none — orientation control** | data-defined |
| | Genome-wide readthrough index | Spearman vs MG53 z | **+0.451** | positive | data-defined |
| | — antisense control | Spearman vs MG53 z | −0.052 | none | data-defined |
| Drug (raises) | Idarubicin 5 uM | corrected log2 fold | **+3.61** | positive | data-defined |
| | Homoharringtonine 5 uM | corrected log2 fold | +3.36 | positive | data-defined |
| | Auranofin 5 uM | corrected log2 fold | +2.71 | positive | data-defined |
| | Homoharringtonine 0.5 uM | corrected log2 fold | +2.55 | positive | data-defined |
| | Dinaciclib 5 uM (**withdrawn**) | corrected log2 fold | +2.48 | **none** — an artefact of the ratio-scale estimand, not a rise | data-defined |
| | Epirubicin 5 uM | corrected log2 fold | +2.18 | positive | data-defined |
| Drug (lowers) | Ponatinib 5 uM | corrected log2 fold | **−1.34** | negative | data-defined |
| | Trametinib 0.05 uM | corrected log2 fold | −1.05 | negative | data-defined |
| | Cabozantinib 5 uM | corrected log2 fold | −1.00 | negative | data-defined |
| | Anethole trithione 5 uM | corrected log2 fold | −0.72 | negative | data-defined |
| Transcription factor | ATF4 | r across drug-doses | +0.36 (to +0.09 once shared stress targets removed) | positive, collapses | list-based |
| | ATF5 / ELK4 / SRF | r across drug-doses | +0.36 / +0.35 / +0.31 | positive, collapses | list-based |
| | XBP1 / HSF1 / MEF2C | r across drug-doses | +0.29 / +0.22 / +0.21 | positive, collapses | list-based |
| | **MEF2A** (known TRIM72 promoter TF) | r across drug-doses | +0.13 (to −0.01) | none | list-based |
| | **MYOD1 / MYOG** (known TRIM72 promoter TFs) | r across drug-doses | +0.09 / −0.07 | none; **not expressed (0 CPM)** | list-based |
| Untreated level across lines | PYCARD-AS1 | Spearman across lines | **+0.821** (rank 1 of 46,775) | positive | data-defined |
| | CPLX4 / FNDC7 | Spearman across lines | +0.742 / +0.728 | positive | data-defined |
| Data-driven program | P24 (20.6% readthrough-geometry genes) | r across drug-doses | **+0.768** | positive | data-defined |
| | P29 / P43 | r across drug-doses | +0.559 / +0.493 | positive | data-defined |

MG53's expression is governed far more by its own genomic neighbourhood than by any transcription factor.
The muscle TFs that drive TRIM72 in its native tissue are absent or silent here. Every TF correlation
collapses once the shared stress-response targets are partialled out, i.e. they are reading general drug
stress rather than MG53-specific regulation.

Two corrections to the drug rows, from a later re-analysis on absolute rather than ratio scales.
**Dinaciclib 5 µM is withdrawn**: on an added-CPM scale all three doses score about zero (`R4_z` 0.674 /
−0.304 / 0.000, q up to 0.969), and with 71–82% cell loss, a 10.8× depth deficit, 25 of 44 lines carrying
zero MG53 reads at 5 µM, and a pseudocount floor of 2.545 CPM (half-count) or 5.090 (one-count) against a
plate baseline of 0.883, a line with **no reads at all** already scores 62–111% of the +2.48 shown. An
earlier version of this table read it as positive; a fold built on a pseudocount in a depleted well can be
produced with no added RNA. **And the remaining drug rows are not equally supported**: of the 21 drug-doses
the calling rule returns, only idarubicin 5 µM and homoharringtonine 5 µM pass in a second well, 17 rest on
one used well and cannot be tested for replication at any effect size, and mitoxantrone 5 µM passes in 1 of
2 wells with the two wells disagreeing in *sign*. Auranofin 5 µM and homoharringtonine 0.5 µM above are
single-well calls.

## Table C — MG53 -> p53 program, with mutants split by retained p53 activity

Activity = each line's mean p53-program induction under the p53-activating drug-doses. Reference points:
**null (truncating / splice / deletion) median = +0.0038; wild-type median = +0.1474.**

`tables/tableC_mutants_by_activity.csv`, per-line values in `tables/per_line_p53_activity.csv`

| Split | Group | Lines | two-way r (95% CI) | slope (95% CI) | direction |
|---|---|---|---|---|---|
| Data-defined inducibility | WT (functional p53) | 17 | +0.013 (−0.002, +0.027) | +0.0009 (−0.0014, +0.0032) | **none** |
| | Altered: **higher** activity (above null) | 18 | +0.024 (+0.010, +0.038) | +0.0010 (−0.0010, +0.0030) | **none** |
| | Altered: **lower** activity (at/below null) | 14 | +0.085 (+0.068, +0.101) | **+0.0043 (+0.0004, +0.0082)** | **positive** |
| Gene-panel functional call (list-based) | Responsive | 11 | +0.021 | +0.0014 (−0.0023, +0.0051) | none |
| | Unresponsive | 28 | +0.058 | **+0.0026 (+0.0001, +0.0052)** | positive |
| | Uncertain | 9 | −0.009 | −0.0006 (−0.0025, +0.0013) | none |

**The gradient runs the wrong way for anything mediated by p53.** The association is largest in the mutants
with the *least* p53 activity and absent in the wild-type lines and in the higher-activity mutants — and it
is positive. An effect working through p53 cannot be strongest in cells with the least functional p53. This
points to the readthrough / stress-amplitude confound rather than to biology.

Does a line's MG53 level predict its p53 activity? No, in any group:

| MG53 level vs | All (49) | Altered (32) | WT (17) |
|---|---|---|---|
| Data-defined inducibility | rho −0.125 (p 0.39) | −0.206 (p 0.26) | −0.186 (p 0.47) |
| Panel responsiveness | +0.013 (p 0.93) | +0.009 (p 0.96) | −0.025 (p 0.93) |
| Basal p53 activity | −0.014 (p 0.93) | +0.007 (p 0.97) | −0.282 (p 0.27) |

## How far p53 is disabled across the panel

`tables/p53_nullification.csv`, per-line detail in `tables/wt_lines_pathway.csv`

| Measure | Value | Note |
|---|---|---|
| TP53 driver mutation | **33 / 50** | genotype, from Tahoe's `cell_line_metadata` |
| Functionally responsive lines | **11 / 50 (22%)** | 29 unresponsive, 9 uncertain, 1 not measurable |
| Median responsiveness, WT vs altered | **0.948 vs 0.256 (3.7x)** | Mann-Whitney p 3.1e-07; the ranking is genotype-blind |
| Altered lines retaining a response | **0 / 33** | mutation is fully penetrant for canonical target induction |
| Genotype-WT lines not fully responsive | **6 / 17** | p53 damped with no TP53 mutation (Hs 766T is functionally dead) |
| Genotype-WT lines with CDKN2A/ARF loss | **9 / 17** | a second route to lowering p53 activity |

Altered lines retain roughly **5%** of the wild-type response, and their median sits barely above the
truncating-null reference — so the missense mutants are about as dead as outright deletions for this
read-out. (That particular comparison uses program P, which was selected with the WT/altered labels and is
therefore partly circular; the 3.7x genotype-blind figure above is the honest headline.)

The one non-tumour line, **hTERT-HPNE** (normal pancreatic cell immortalised with hTERT), is responsive and
carries no p53-pathway driver at all — consistent with the nullification being something the cancers acquired.

**Why this bounds everything in Tables A and C:** the effective sample for any MG53 -> p53 test is about
11 to 17 lines, not 50 and not 53,000 rows. Two-thirds of the panel contributes a floor of near-zero p53
output that cannot move in either direction.

## Caveats that apply to all three tables

- These are **associations in 24 h mRNA**. Tahoe contains no MG53 perturbation and no protein data, so
  nothing here speaks to what forcing MG53 up or down would do, nor to protein-level events.
- **No line carries a TRIM72/MG53 alteration**: all 50 have wild-type MG53 and differ only in expression
  level (0.93 to 23.6 CPM, median 5.9). Nothing here contrasts functional with non-functional MG53.
- MG53 is measured at trace level — median 5 UMIs per profile. An earlier version turned that into a
  conversion: split-half reliability 0.289, so bounds on true MG53 about 3.5× wider than bounds on measured
  MG53. Both halves of it are withdrawn. The division is not licensed, because MG53 and every read-out here
  are counted from the same cells, in the same well, against the same total-UMI denominator — the one case
  the classical correction excludes. And 0.289 is the optimistic floor of the attenuation factor's range: the
  split-half splits *cells* within each (well, line), so it measures cell-sampling noise only and books every
  well-level artefact as signal. Matched on the 102 replicated drug-doses the same statistic reads 0.425, and
  the factor the cross-batch replicate pairs support is **0.078–0.105 (0.055 trimmed)**, a 9–12× correction
  against the 3.46× the published `mde_diff_80_attenuation_corrected` applies — understated by about 3.6×.
  Every bound and slope in these tables is per doubling of **measured** MG53 and is left there.
- Part of the measured MG53 signal is readthrough spillover rather than MG53's own transcript, which dilutes
  MG53 as an exposure in every table.
- **The interval construction used throughout these tables proved 12–58% too narrow wherever it was
  refitted.** A later controlled re-measurement replaced the cell-line-clustered CR0 standard error times
  1.96 with a per-arm CR1 factor, a conservative two-way (drug, line) cluster and a *t* on
  min(drugs, lines) − 1 df. One row here inherits a recomputed interval directly: Table C's **Responsive,
  11 lines** row is the same fit as that work's functional-p53 arm, so its interval is now
  **(−0.0023, +0.0051)**, corrected from (−0.0015, +0.0043). The point estimate is unchanged — the two fits
  agree to 1e−18 — and the verdict does not change. The CSVs behind these tables are **not** corrected,
  because `make_tables.py` was not refitted: `tableC_mutants_by_activity.csv` still carries `se_slope`
  0.0014888 with `slope_lo`/`slope_hi` −0.0015464 / +0.0042899 on that row, which is the CR0 × 1.96
  construction. The replacement lives in `tables/mg53_to_p53_effect.csv`, arm A, `lo`/`hi`, where `se_twoway`
  0.0016569 carries both the per-arm CR1 factor (1.10 here) and the two-way cluster.
- The three intervals that just exclude zero were **not** refitted and are unresolved rather than corrected:
  Table A's CollecTRI TP53 targets, +0.0029 (+0.0006, +0.0051) on 17 lines; Table C's low-activity mutants,
  +0.0043 (+0.0004, +0.0082) on 14 lines; and panel-unresponsive, +0.0026 (+0.0001, +0.0052) on 28 lines.
  All three rest on the construction above with 14 to 28 clusters, and they would probably not survive the
  label-permutation and placebo-gene machinery the pipeline applies to its primary test. They are not
  reported here as findings.
- Actual cell death and survival are effectively unmeasured: the per-line composition shift does not track
  surviving cell counts (r −0.01), and the atlas corrects composition out by design.

## Table D — per gene: the canonical p53 effectors

`tables/p53_effectors_per_gene.csv` (29 genes). One row per gene that actually carries out p53's effects —
the curated 21-gene P53_ACTIVITY panel plus the classic effectors it omits (PMAIP1, GADD45A, TNFRSF10B,
TIGAR, PPM1D, BTG2, CCNG1). The `role` column groups them by what they do once p53 is active; that grouping
is **literature annotation**, an overlay for reading the table, and selects nothing.

The companion `tables/tableD_p53_target_genes.csv` holds all 195 genes of the data-defined program, generated
and documented by `table_d()` in `make_tables.py`, with per-gene detectable-effect bounds and a readthrough
geometry flag. This table is the focused one; see the full-program section below.

**Read the direction columns before the slope columns.** Both tables carry `p53_direction` (induced or
repressed by p53), `p53_direction_source`, `frac_compounds_wt_up`, `direction_is_mixed`, and
`mg53_effect_on_p53_output` — MG53's slope re-expressed in p53-output units rather than in the gene's own.
The last of those is the only column that can be summed across genes: for a p53-repressed gene, "up with
MG53" means *less* p53 output, so the raw verdict columns point opposite ways for the two arms. All 29 genes
in this focused table happen to be p53-**induced** (26 by the data's own arm, 3 by curation), so for this
table the signed and unsigned readings agree — but 11 of the 29 are direction-mixed, so the per-gene
direction is not uniform even here. See the signed tally in the full-program section.

### Two fold changes, diluted in opposite ways

Neither available fold change is clean, so both are given:

| Column | What it is | How it is diluted |
|---|---|---|
| `fold_ida5` | the gene's fold change under idarubicin 5 uM, a strong p53 activator | it is the median over **all 50 lines**, and two-thirds of the panel is p53-dead, so the sharpest targets read low |
| `fold_WT_broad` | `2**wt_mean_log2`, **wild-type lines only** | its baseline is **not vehicle**: it is the same line's median over that plate's **drug wells**, and it is a compound-equal mean (each of 98 compounds carries 1/98) over the 142 p53-activating drug-doses, so a strong activator is averaged with 97 weaker ones (median 1.06x) |

An earlier version of this section said `fold_WT_broad` was diluted by averaging over drug-doses that
mostly do not activate p53. That was wrong: the average is taken over the 142 **p53-activating**
drug-doses specifically [`genome_wide/genome_wide.py`:1976 -> `set_stats`:957-984]. It reads low for the two
reasons given above instead.

The clean quantity — wild-type lines only, under one strong activator — needs a per-gene **per-line**
extraction that the export does not provide for arbitrary genes (only TRIM72 and the program scores reach
that granularity). That is a concrete pipeline addition, not a result that exists yet.

### The table

Sorted by fold change under idarubicin 5 uM. `b_common` is the MG53 slope on that gene (log2 of the gene per
doubling of MG53); `diff` is the wild-type-minus-altered version.

| Gene | Role | fold (ida 5 uM, all lines) | fold (WT, broad) | WT−alt log2 | MG53 b_common (q) | MG53 verdict | genotype verdict |
|---|---|---|---|---|---|---|---|
| SESN1 | metabolism / redox | **3.08x** | 1.14x | +0.134 | +0.0005 (0.92) | none | none |
| TIGAR | metabolism / redox | **2.65x** | 1.21x | +0.179 | +0.0043 (0.36) | none | none |
| FDXR | metabolism / redox | **2.06x** | 1.24x | +0.314 | +0.0025 (0.75) | none | none |
| ZMAT3 | negative feedback | 1.98x | 1.20x | +0.218 | +0.0012 (0.80) | none | none |
| POLH | DNA repair | 1.98x | 1.16x | +0.184 | +0.0021 (0.57) | none | none |
| BTG2 | cell-cycle arrest | 1.94x | 1.15x | +0.261 | +0.0153 (xperm q 0.055) | positive | none |
| XPC | DNA repair | 1.84x | 1.09x | +0.166 | +0.0004 (0.92) | none | none |
| DDB2 | DNA repair | 1.82x | 1.14x | +0.206 | **−0.0075 (0.084)** | negative | none |
| PMAIP1 (NOXA) | apoptosis | 1.82x | 1.06x | +0.019 | **+0.0081 (0.070)** | positive | none |
| ACER2 | metabolism / redox | 1.75x | 1.11x | +0.238 | +0.0136 (xperm q 0.052) | positive | none |
| PPM1D | negative feedback | 1.67x | 1.24x | +0.226 | −0.0020 (0.63) | none | none |
| GADD45A | cell-cycle arrest | 1.57x | 1.11x | +0.126 | +0.0065 (0.36) | none | none |
| TP53INP1 | apoptosis | 1.54x | 1.18x | +0.278 | −0.0058 (0.42) | none | none |
| RRM2B | DNA repair | 1.46x | 1.13x | +0.155 | +0.0010 (0.80) | none | none |
| TNFRSF10B (DR5) | apoptosis | 1.39x | 1.13x | +0.093 | +0.0039 (0.37) | none | none |
| AEN | apoptosis | 1.36x | 1.17x | +0.182 | **+0.0090 (0.082)** | positive | none |
| BAX | apoptosis | 1.33x | 1.06x | +0.143 | −0.0002 (0.98) | none | none |
| EDA2R | apoptosis | 1.33x | 1.07x | +0.243 | +0.0051 (0.63) | none | none |
| RPS27L | other | 1.32x | 1.02x | +0.135 | −0.0002 (0.95) | none | none |
| PLK3 | cell-cycle arrest | 1.27x | 1.09x | +0.163 | +0.0076 (0.30) | none | none |
| **CDKN1A (p21)** | cell-cycle arrest | 1.08x | 1.12x | +0.215 | **+0.0104 (0.031)** | **positive** | none |
| GDF15 | other (secreted) | 1.08x | 1.07x | +0.170 | +0.0015 (0.86) | none | none |
| **MDM2** | negative feedback | 1.06x | 1.25x | +0.257 | **−0.0050 (0.069)** | **negative** | none |
| CCNG1 | cell-cycle arrest | 0.87x | 1.05x | +0.107 | −0.0017 (0.52) | none | none |
| TP53I3 (PIG3) | metabolism / redox | 0.85x | 1.06x | +0.141 | **−0.0100 (0.090)** | negative | none |
| TRIAP1 | apoptosis (anti-) | 0.81x | 1.08x | +0.142 | −0.0038 (0.36) | none | none |
| BBC3 (PUMA) | apoptosis | 0.72x | 1.14x | +0.185 | +0.0017 (0.74) | none | none |
| PHLDA3 | other | 0.54x | 1.08x | +0.254 | −0.0059 (0.21) | none | none |
| SPATA18 | other | — | 1.05x | +0.154 | +0.0172 (0.196) | none | none |

### What it says

- **Every one of the 29 is a real p53 target in this data**: all have a positive wild-type-minus-altered
  difference (+0.019 to +0.314 log2), so p53 status does drive them.
- **Eight of 29 reach the calibrated threshold for an MG53 slope — five positive, three negative.**
  Positive: CDKN1A, PMAIP1, AEN, ACER2, BTG2. Negative: MDM2, DDB2, TP53I3. That is 28% against a
  genome-wide base rate of 27% (4,500 of 16,642), i.e. exactly chance, with signs split both ways.
- **The two most canonical effectors point opposite ways**: CDKN1A +0.0104 (q 0.031) and MDM2 −0.0050
  (q 0.069). If MG53 were damping p53's output, p21 and MDM2 would not move in opposite directions.
- **Not one gene differs by TP53 status.** Every `mg53_genotype_verdict` is "none"; across all 195 program
  genes the smallest q_diff is 0.999. No canonical effector shows a wild-type-specific MG53 slope.
- **FDXR**, the one gene with a negative lean in the earlier list-based work, has `diff` −0.0213 — the
  largest negative among the classics — but q 0.999 and a common slope of +0.0025 (q 0.75). It does not
  survive multiplicity.

### The MG53 slope columns, and why the q value needs care

`b_common` is the single MG53 slope fitted across all lines, from the screen's model
[`genome_wide/genome_wide.py` section C]:

    Y_gene = (drug-dose x TP53-group fixed effects) + (line fixed effects)
             + b_common x MG53 + (covariates x TP53 group)

Y is the gene's corrected log2 fold change for that line x drug-dose, MG53 is TRIM72's corrected log2 fold
change for the same cell, so the unit is **log2 of the gene per doubling of MG53**. Because both line and
drug-dose x group means are removed, only the residual co-variation is used: for a given line under a given
drug, does the gene deviate from expectation in the same direction as MG53 does. `b_WT` and `b_alt` are the
same slope fitted separately per genotype group and `diff` = `b_WT` - `b_alt`; `b_common` constrains the two
to be equal while leaving the fixed effects and covariates group-specific.

**The analytic q value is badly calibrated and must not be read as a p value.** The step's own calibration
gives `lambda_common` **4.444** for the observed fit, where 1.0 is correct — the analytic two-way standard
error does not absorb the line-level structure, so the statistic is inflated about 4.4x. Two things follow:

- Use `q_xperm_common` (the exposure shuffled across lines within each drug-dose x group cell), which is the
  null the step documents for the common slope. The verdict column uses it. The TP53-relabelling null is
  explicitly **not** valid here, because relabelling preserves the within-line association.
- Even the calibrated q does not make MG53 special, because **matched placebo genes show the same inflation
  or more**: lambda 4.685 (response-matched) and 5.518 (expression-matched), giving 3,196 and 5,330 genes at
  q_common < 0.1 against MG53's 4,500 [`genome_wide/tables/c_calibration.csv`]. MG53 sits inside the placebo
  range. So read `placebo_pct_common_expression` / `_response` alongside the q value — but note their
  **resolution is 0.1, because each family holds only 10 placebo exposures in the per-gene screen**. A 0.0 or
  1.0 there means "most extreme of ten", not a p value, and cannot support a claim on its own.

On that placebo reading the eight genes are extreme in opposite directions (CDKN1A 0.9/1.0, PMAIP1 1.0/1.0,
AEN 1.0/1.0, BTG2 1.0/1.0 at the positive end; MDM2 0.1/0.0, DDB2 0.1/0.0, TP53I3 0.0/0.0 at the negative
end). With only 10 placebos per family these are weak individually, but the pattern across the 29 is
informative: genes land in the outer tenths in **both** directions at once. That is the signature of MG53
tracking overall transcriptional response amplitude, which makes it a better predictor than a random matched
gene for any responsive gene, in whichever direction that gene happens to go. It is not a p53-directed
effect.

### Caveats

- The largest MG53 slope here, CDKN1A at +0.0104 log2 per doubling, is **+0.7% of p21 per doubling of MG53**
  — and positive. Nothing in this table is of a size that would matter biologically even if it were real.
- `wt_mean_log2`, `wt_minus_alt_log2` and program membership were all computed **using the TP53 wild-type /
  altered labels**, so they are circular as measures of p53 specificity. `b_common`, `diff` and the q values
  from the MG53 screen are not.
- 24 h mRNA associations only: no MG53 perturbation, no protein data, every line carries wild-type MG53 at
  trace level, and the effective sample is the 11-17 lines with functional p53.

---

## Full program (195 genes) - generated per-gene table: p53 target genes, their fold change, and MG53

`tables/tableD_p53_target_genes.csv` (195 rows, 67 columns) and `tables/tableD_top_mg53_partners.csv`
(100 rows), both written by `table_d()` in `make_tables.py`. This is the gene-level companion to the
per-line tables above, and the full-program version of the 29-gene effector table: it replaces the earlier
hand-made `tableD_p53_target_genes_RAW.csv` dump with a generated, documented file.

**One row is one gene of the data-defined p53 program** — 180 genes in the induction arm P, 15 in the
repression arm P-down [`genome_wide/tables/b_p53_program_genes.csv.gz`, `in_P` / `in_P_down`] — carrying
that gene's p53-activation fold change and that gene's own row from the genome-wide MG53 screen. Four
things carry the weight: `wt_fold` (how much the gene moves when p53 is activated in TP53-wild-type
lines), `wt_minus_alt_log2` (how much of that is genotype-specific), `n_folds_kept` with `loco_frequency`
(whether the gene survives cross-fitting — the only handles on a circular selection), and
`median_line_cpm` (whether the gene is expressed well enough for any of it to be measurable). The MG53
block is `b_common`, one slope shared by all lines, and `diff` = `b_WT` − `b_alt`, its
wild-type-minus-altered version.

**The fold change is `2**wt_mean_log2`, and its baseline is not DMSO.** `wt_mean_log2` is the
compound-equal weighted mean — each of **98 compounds** carries 1/98, split evenly across its doses — over
**the 142 S2 p53-activating drug-doses**, of the mean corrected log2 response of the **TP53-wild-type lines
that express the gene**; and that response is already relative to **the same line's median log2 CPM over
that plate's drug wells**, minus the composition shift and the well-position effect
[`genome_wide/genome_wide.py`:1976 → `set_stats`:957-984; `export/README.md`, `r2`]. So it is a fold change
against a typical drug well of the same line on the same plate, not against vehicle and not against
untreated cells, and it averages 142 treatments instead of reporting one strong activator. That is why the
numbers are small: across the 180 induction-arm genes it runs **1.001x to 1.255x, median 1.060x**, with 42
of 180 reaching 1.10x and 19 of 180 below 1.02x; the 15 repressed genes run 0.872x to 0.965x, median 0.935x
[`genome_wide/tables/b_p53_program_genes.csv.gz`, `wt_mean_log2`; recomputed]. Ranking by the fold change is
not the same as ranking by the program's own selection statistic — Spearman(`z_program`, `wt_mean_log2`)
within P is 0.552 [same file, `z_program`; recomputed] — so both are in the table.

### Column glossary

| column | means | units | circular? |
|---|---|---|---|
| `arm` | induction arm P or repression arm P-down of the data-defined program | label | **yes** — membership was selected using the TP53 labels |
| `wt_mean_log2`, `wt_fold` | the gene's corrected log2 change in TP53-WT lines, compound-equal mean over the 142 S2 p53-activating drug-doses, against that plate's drug-well median for the same line; `wt_fold` = 2** it | log2; fold (ratio) | **yes** — through the label-selected S2 drug-dose set |
| `wt_minus_alt_log2`, `wt_minus_alt_fold` | same mean, of (WT-line mean − altered-line mean). Positive = moves more in TP53-WT | log2; fold | **yes** — this is the selection functional itself |
| `z_program`, `q_arm` | the drug-equal mean WT-minus-altered contrast z, calibrated against 100 TP53-label permutations, and its own-direction BH FDR (`q_up` / `q_down` over 16,642 genes) | z; FDR | **yes** |
| `frac_compounds_up`, `frac_compounds_wt_up` | share of the 98 S2 compounds with a positive contrast, and with a positive WT arm. The program rule needs both ≥ 0.5 | share of 98 | **yes** |
| `n_folds_kept` of `n_folds_total` | how many of the 5 cross-fitted programs keep the gene (drug-doses re-selected without each compound fold) | count 0-5 | holds compounds out, not labels |
| `loco_frequency` | share of the 98 leave-one-compound-out programs keeping the gene. Blanked on P-down rows: those programs are derived in the induction direction only | share of 98 | holds compounds out, not labels |
| `median_line_cpm`, `n_lines_expressing` | the gene's median level across lines, and how many of 50 express it | CPM; count | **no** |
| `b_common`, `se_common`, `q_common`, `q_xperm_common` | log2 change in the gene per log2 change in **measured** MG53, one slope for all lines, at equal drug-dose × TP53-group and cell line, conservative two-way (compound, line) SE; BH FDR, and the FDR against the exposure shuffled within each cell | log2 per doubling; FDR | **no** — no label-based selection of genes or drug-doses (one covariate's background gene set excludes the label-selected programs) |
| `b_WT`, `b_alt`, `diff`, `se_diff`, `q_diff`, `q_label_diff` | the same slope fitted per TP53 group, their difference, and its two FDRs (BH, and the TP53-relabelling null) | log2 per doubling; FDR | **no** — label-tested, not label-selected |
| `crit_*_q01_measured`, `mde80_*_q01_measured` | smallest effect this gene could have shown as a lone discovery at q < 0.1, at 50% and 80% power, per doubling of **measured** MG53 | log2 per doubling | **no** |
| `mde80_*_q01_true` | the same bound ÷ reliability 0.289. **Do not read it**: the division is not licensed here (exposure and outcome are counted from the same cells in the same well) and 0.289 is the optimistic end of the factor's range. The column stays in the CSV so earlier readings can be traced | log2 per doubling | **no** |
| `placebo_pct_common_*`, `placebo_pct_diff_*` | share of that family's 10 placebo exposures whose t is below this gene's. Resolution 0.1, so 0.0 or 1.0 means "most extreme of ten", not a p value | share of 10 | **no** |
| `readthrough_geometry` | positional only, never regulation: `sense_exposed` = the gene sits ≤ 20 kb **3' of** an expressed same-strand gene at ≥ 8x its own level, so transcription running past that neighbour is counted as this gene — readthrough spillover. MG53 itself is such a gene | label | **no** (positional) |
| `mg53_verdict_common`, `mg53_verdict_genotype` | per-gene reading, each naming its own test in the next column: `q_xperm_common` < 0.1 on `b_common`, `q_label_diff` < 0.1 on `diff` | label | **no** |

### The 25 strongest p53 target genes by fold change

Sorted by `wt_fold`. ◆ = curated 21-gene P53_ACTIVITY panel, † = CollecTRI TP53-activated, ‡ = carries
readthrough spillover geometry. All 25 have `loco_frequency` 1.000 and are not fallback members.

| Gene | CPM | p53 fold change (WT) | WT−alt log2 | folds (of 5) | MG53 b_common (q_common; xperm q) | MG53 WT−alt diff (q_diff) | verdict |
|---|---|---|---|---|---|---|---|
| **MDM2** ◆† | 185.8 | **1.255x** | +0.257 | 5 | **−0.0050 (0.069; 0.031)** | −0.0006 (0.999) | **down** |
| GRIN2C | 2.08 | 1.244x | +0.412 | 5 | **+0.0511 (1.2e−04; 5.6e−05)** | +0.0081 (0.999) | **up** |
| PPM1D † | 56.2 | 1.243x | +0.226 | 5 | −0.0020 (0.63; 0.58) | −0.0086 (0.999) | none |
| **FDXR** ◆† | 10.5 | 1.237x | +0.314 | 5 | +0.0025 (0.75; 0.71) | −0.0213 (0.999) | none |
| TIGAR † | 35.7 | 1.209x | +0.179 | 5 | +0.0043 (0.36; 0.29) | −0.0118 (0.999) | none |
| ZMAT3 ◆† | 28.9 | 1.202x | +0.218 | 5 | +0.0012 (0.80; 0.77) | −0.0012 (0.999) | none |
| MIR3659HG ‡ | 2.43 | 1.194x | +0.201 | 4 | **+0.0241 (0.065; 0.028)** | −0.0022 (0.999) | **up** |
| PER1 | 73.2 | 1.186x | +0.075 | 4 | +0.0011 (0.87; 0.85) | +0.0088 (0.999) | none |
| PINCR | 0.65 | 1.183x | +0.392 | 5 | +0.0010 (0.95; 0.94) | −0.0353 (0.999) | none |
| TP53INP1 ◆† | 9.20 | 1.180x | +0.278 | 5 | −0.0058 (0.42; 0.35) | −0.0011 (0.999) | none |
| FAS † | 21.0 | 1.176x | +0.180 | 5 | +0.0000 (1.00; 1.00) | −0.0080 (0.999) | none |
| PURPL | 20.2 | 1.176x | +0.303 | 5 | +0.0048 (0.55; 0.49) | +0.0081 (0.999) | none |
| AEN ◆ | 17.0 | 1.167x | +0.182 | 5 | **+0.0090 (0.082; 0.039)** | −0.0125 (0.999) | **up** |
| ACTA2 | 4.25 | 1.163x | +0.259 | 5 | +0.0129 (0.28; 0.21) | −0.0145 (0.999) | none |
| ZNF79 | 7.20 | 1.160x | +0.150 | 5 | +0.0051 (0.41; 0.34) | −0.0012 (0.999) | none |
| POLH ◆ | 59.0 | 1.158x | +0.184 | 5 | +0.0021 (0.57; 0.51) | +0.0042 (0.999) | none |
| BTG2 † | 8.51 | 1.155x | +0.261 | 5 | **+0.0153 (0.11; 0.055)** | −0.0261 (0.999) | **up** |
| SESN1 ◆† | 44.6 | 1.144x | +0.134 | 5 | +0.0005 (0.92; 0.91) | −0.0105 (0.999) | none |
| DRAM1 † | 37.4 | 1.142x | +0.105 | 5 | **−0.0062 (0.16; 0.097)** | +0.0031 (0.999) | **down** |
| MIR34AHG | 21.8 | 1.140x | +0.220 | 5 | −0.0076 (0.41; 0.34) | −0.0094 (0.999) | none |
| **DDB2** ◆† | 54.3 | 1.139x | +0.206 | 5 | **−0.0075 (0.084; 0.041)** | +0.0060 (0.999) | **down** |
| BBC3 ◆† | 17.4 | 1.136x | +0.185 | 5 | +0.0017 (0.74; 0.71) | −0.0074 (0.999) | none |
| ENSG00000285901 | 4.68 | 1.135x | +0.177 | 5 | **+0.0351 (6.2e−04; 5.6e−05)** | −0.0170 (0.999) | **up** |
| TNFRSF10B † | 200.5 | 1.131x | +0.093 | 5 | +0.0039 (0.37; 0.30) | −0.0068 (0.999) | none |
| HSPA4L | 38.7 | 1.129x | +0.102 | 4 | −0.0038 (0.40; 0.33) | −0.0081 (0.999) | none |

[All values `genome_wide/tables/b_p53_program_genes.csv.gz` (`wt_mean_log2`, `wt_minus_alt_log2`,
`median_line_cpm`, `in_P_minus_fold0..4`, `loco_frequency`, overlay columns) and
`genome_wide/tables/c_screen_genes.csv.gz` (`b_common`, `q_common`, `q_xperm_common`, `diff`, `q_diff`,
`dog_class`); folds and verdicts recomputed.]

Three readings the table forces. **CDKN1A (p21) is not in the top 25 by fold change** — 1.117x, 23rd by
`wt_minus_alt_log2` — yet it has the largest positive slope among the classic effectors, +0.0104
(q_common 0.031; xperm 0.0089), i.e. **+0.72% of p21 per doubling of MG53**. **MDM2, the strongest p53
target here, moves the other way** (−0.0050, −0.35% per doubling), as does DDB2. Two canonical targets
pointing in opposite directions is not a p53-directed effect. And the two largest slopes in the program,
GRIN2C (+0.0511) and ENSG00000285901 (+0.0351), sit on genes of 2.1 and 4.7 CPM, where `|b_common|` is
largest genome-wide for reasons of expression alone (median `|b_common|` by CPM bin: 0.0140 below 1 CPM,
0.0144 at 1-4, 0.0059 at 4-16, 0.0036 at 16-64, 0.0027 above 64 [`c_screen_genes.csv.gz`, `b_common`;
recomputed]).

Only one gene in the top 25, **MIR3659HG**, carries readthrough spillover geometry; the only other one in
the whole program is **RRM2B** (26th by fold change at 1.127x, `b_common` +0.0010, q 0.80), so 2 of 195
program genes in total, against 702 of 16,642 tested genes (4.218%) genome-wide [`c_screen_genes.csv.gz`,
`dog_class`; recomputed].

### FDXR

FDXR is the gene most likely to be misread, because it was the one negative lean in the earlier list-based
work. As a p53 target it is impeccable: 1.237x in the wild-type lines, `wt_minus_alt_log2` +0.314 (the
third largest in the program), `z_program` 5.32 at q 1.5e−04, rank 5 by z, kept by all 5 cross-fitted
programs and by all 98 leave-one-compound-out programs, a member of both the curated 21-gene panel and the
curated p53-primary list, 10.5 CPM in 49 of 50 lines, and no readthrough geometry
[`b_p53_program_genes.csv.gz`]. **As an MG53 result it is not credible.** Its common slope is flat
(+0.0025, q_common 0.75, xperm q 0.71). Its genotype split looks suggestive — `b_WT` −0.0106 (se 0.0051)
against `b_alt` +0.0107 (se 0.0064), `diff` −0.0213 (se 0.0083), nominal p_diff 0.0135, pooled relabelling
p 0.0112 — but: q_diff is 0.999 and q_label_diff 0.999; the effect halves and the nominal p collapses to
0.111 when three response principal components are added (`diff_gw_pc` −0.0101), while holding under the
other covariate sets (−0.0200 to −0.0231); its own-gene relabelling p sits on its floor of 1/21 = 0.048 and
cannot go lower; its placebo percentiles are 0.1 and 0.0, i.e. 9 of 10 and 10 of 10 matched placebo
exposures give a *lower* t, an empirical two-sided p of roughly 2/11; and |diff| 0.0213 is **2.3x below
FDXR's own 80%-power detection bound of 0.0495** log2 per doubling of measured MG53
[`c_screen_genes.csv.gz`, `b_WT`/`b_alt`/`diff`/`se_diff`/`p_diff`/`q_diff`/`q_label_diff`/`diff_gw_pc`/
`p_diff_gw_pc`/`p_label_own_diff`/`placebo_pct_diff_*`; bound recomputed]. One gene out of 195 at nominal
p 0.013 is what the second-smallest of 195 tests gives.

### For contrast: what MG53's level actually tracks

`tables/tableD_top_mg53_partners.csv` — the 100 largest `|b_common|` among the 4,500 genes the screen calls
hits, with the p53 program selecting nothing. Top 10:

| Gene | b_common (se) | q_common | xperm q | CPM | readthrough geometry |
|---|---|---|---|---|---|
| ENSG00000283573 | +0.1431 (0.0198) | 1.4e−06 | 5.6e−05 | 3.91 | **yes** |
| FNDC7 | +0.1408 (0.0142) | 4.8e−09 | 5.6e−05 | 2.54 | **yes** |
| SEMA4A | +0.1325 (0.0163) | 3.2e−07 | 5.6e−05 | 13.83 | **yes** |
| LDHC | +0.1199 (0.0152) | 3.2e−07 | 5.6e−05 | 3.90 | **yes** |
| ENSG00000260177 | +0.1182 (0.0144) | 2.5e−07 | 5.6e−05 | 2.25 | no |
| ENSG00000289254 | +0.1161 (0.0145) | 3.2e−07 | 5.6e−05 | 4.33 | **yes** |
| MMP25 | +0.1136 (0.0135) | 1.5e−07 | 5.6e−05 | 2.36 | no |
| AZU1 | +0.1123 (0.0132) | 1.5e−07 | 5.6e−05 | 1.50 | **yes** |
| GRAMD2A | +0.1079 (0.0168) | 7.0e−06 | 5.6e−05 | 1.24 | **yes** |
| ENSG00000205890 | +0.1074 (0.0119) | 8.4e−08 | 5.6e−05 | 3.18 | no |

All 100 slopes are positive, from 0.062 to 0.143 (median 0.073); none of the 100 is a p53 program member;
median expression is 2.77 CPM against 54.19 CPM for the program; and **61 of 100 carry readthrough
spillover geometry** against the genome-wide 4.218% [`c_screen_genes.csv.gz`, `b_common`/`q_common`/
`dog_class`; `b_p53_program_genes.csv.gz`, `median_line_cpm`; recomputed]. That 61% is not just an
expression artefact: among the 4,087 tested genes at or below the list's own 75th-percentile expression
(3.94 CPM) the rate is 9.5%, so it is still a **6.4x** enrichment [recomputed]. The magnitude gap is
largely artefact, though: the 20x ratio between the partners' median `|b_common|` and the program's
(0.0037) is about 4x expression level and the rest selection of the top 100 of 16,642 on `|b|`. What this
list shows is the genes MG53's residual variation co-moves with — dominated by low-expressed genes whose
measurement shares a readthrough neighbourhood with MG53's own — not a biology list, and not anything that
resembles the p53 program.

### The per-gene bottom line

**How many p53 targets show any MG53 association: the background number, with no direction.** 53 of 195 at
the analytic q_common < 0.1 (24 positive, 29 negative) and 67 of 195 at the exposure-shuffle
q_xperm_common < 0.1 (34 positive, 33 negative). Both are exactly the genome-wide rate: 4,500 of 16,642
tested genes (27.04%) pass q_common and 5,746 (34.5%) pass q_xperm_common, against 27.2% and 34.4% here.
The one thing that differs is sign and size: the 4,447 non-program hits are 71.7% positive with a median
`|b_common|` of 0.0153, while the program's hits split 24/29 with a median of 0.0037
[`c_screen_genes.csv.gz`; recomputed]. The repressed arm is the same story on 15 genes (4 hits).

### Signed by the direction p53 moves each gene — which is the only way to add these up

A gene's MG53 slope is in that gene's own units, and "up with MG53" means opposite things in the two arms.
For a gene **p53 induces**, more of it means more p53 output. For a gene **p53 represses**, more of it means
**less**. An unsigned tally adds the two together, so it reads as noise whatever the truth is. Signed
[`tables/tableD_signed_tally.csv`, `tables/p53_effectors_signed_tally.csv`]:

| Direction p53 moves the gene | genes | with a verdict | **toward MORE p53 output** | **toward LESS** | direction mixed | membership unstable |
|---|---|---|---|---|---|---|
| induced by p53 (arm P) | 180 | 62 | **32** | **30** | 63 | 43 |
| repressed by p53 (arm P-down) | 15 | 5 | **3** | **2** | 2 | 2 |
| **all 195 program genes** | 195 | **67** | **35** | **32** | 65 | 45 |
| *the 29 canonical effectors* | *29* | *8* | *5* | *3* | *11* | *3* |

**35 against 32.** A coherent change in p53 output would push the two arms in opposite *gene-level*
directions and so land almost entirely on one side of this split. It lands on both sides equally, in the
full program and in the curated effector list alike. That is what a non-specific association looks like, and
it is only visible once direction is accounted for — the unsigned "34 positive, 33 negative" above conceals
the fact that three of those "positives" are repressed genes moving the p53-output score the other way.

Where direction comes from, and what "mixed" means:

- **Data-defined**, from the arm the gene was selected into. The two arms are disjoint, no gene is
  significant in both directions (`q_up` and `q_down` are never both < 0.1), and the separation is wide:
  induction-arm genes are moved up by 64–99% of the 98 compounds (median 79%), repression-arm genes moved
  **down** by 70–81%.
- **Curation agrees wherever it speaks.** Not one of the 15 repression-arm genes appears in any curated
  p53-activated set, including CollecTRI's 723 TP53 targets — so `direction_conflicts_curation` is **0 of
  195**. Curation also fills the gaps: PMAIP1 (NOXA), TP53I3 and SPATA18 are canonical targets that the
  data-defined program does not contain, and without the curated fallback they would drop out of a signed
  tally for want of a sign. `p53_direction_source` records which applied.
- **Mixed is a property of the gene, not a defect.** `frac_compounds_wt_up` is the share of the 98 compounds
  that move the gene up in wild-type lines; at 0.5 the gene goes each way equally often and its direction is
  not a fact about the gene. **65 of 195 program genes** sit between 0.35 and 0.65, and so do **11 of the 29
  canonical effectors** — among them **BAX at 0.541**, EDA2R 0.541, RPS27L 0.510, XPC 0.571, PMAIP1 0.571,
  GDF15 0.592, TRIAP1 0.612, PHLDA3 0.622 and GADD45A 0.633. A canonical p53 apoptosis target moving up in
  only 54% of compounds is a caution about reading any single gene as a p53 readout.
- **Program membership is often unstable, and that does not track the verdict.** `n_folds_kept` counts the
  cross-fitting folds (of 5) in which a gene was re-selected. Of the 67 genes with a verdict, 20 were kept
  in 0 or 1 folds — and those 20 split 11 toward less output and 9 toward more, the same even split as the
  stable ones (15 against 20). `loco_frequency` is computed for the **induction arm only**, so every
  repression-arm gene reads blank there and must be judged on `n_folds_kept` alone; of the five
  repression-arm genes with a verdict, MBOAT1 was kept in 1 fold of 5 and SMC1A in 2.

**How many by genotype: none.** 0 of 195 — and 0 of all 16,642 tested genes — reach q_diff < 0.1 or
q_label_diff < 0.1. q_diff cannot even rank genes: 194 of the 195 sit at its minimum, 0.99879. On the
nominal p_diff the extreme gene is INKA2 at 1.9e−03 (the only program gene q_label_diff separates at all,
0.888), and its difference is carried by the **altered** arm (`b_alt` +0.0202, p 0.0043; `b_WT` −0.0046,
p 0.39) — the wrong arm for anything MG53 does to p53's output. The minimum of 195 independent tests is
expected to fall that low about 30% of the time [`c_screen_genes.csv.gz`, `p_diff`/`q_diff`/
`q_label_diff`/`b_WT`/`b_alt`; recomputed].

**The per-gene detectable-effect bound.** A lone discovery at q_diff < 0.1 needs p ≤ 0.1/16,642 =
6.0e−06, i.e. |t| ≥ 5.11 at the median df of 46. With a median `se_diff` of 0.0048 across the 195 genes
that is **|diff| ≥ 0.029 log2 at 80% power = +2.0% in the gene per doubling of measured MG53**; for the
common slope the same bound is **+1.0% measured**. **No gene reaches its own bound**: the largest |diff|
in the table is 0.035 and 0 of 195 clear their own 80% threshold (13 exceed the much weaker 1.96 × se).
That bound is **41% of the median gene's entire wild-type-minus-altered genotype effect** (0.070 log2), so on
the measured scale this screen could have seen only an MG53 effect about two-fifths the size of what TP53
genotype itself does to the median program gene [`c_screen_genes.csv.gz`, `se_diff`/`se_common`/`df`;
recomputed].

An earlier version restated both bounds per doubling of **true** MG53 — **+7.1%** and **+3.7%**, dividing by
MG53's split-half reliability of 0.289 — and put the genotype comparison at 1.43× on that scale. Those
restatements are withdrawn rather than widened. MG53 and every outcome gene are counted from the same cells,
in the same well, against the same total-UMI denominator, so the classical correction's independence
condition fails by construction and the quotient has no estimand. How little it pinned down is visible in
its sensitivity to the divisor: at the 0.105–0.080 attenuation factor the cross-batch replicate pairs
support, the same arithmetic gives **+21% to +29%** and **+10% to +13%**. The measured bounds are the ones
that stand [`two_way/tables/trim72_reliability.csv`, `reliability_full_spearman_brown` row
i_all / ddxg / full / all lines; recomputed].

### Caveats

- **The fold-change columns are circular.** The program's genes **and** the S1 / S2 p53-activating
  drug-doses were both selected using the TP53 wild-type / altered labels, at the drug-dose-selection step
  and again at the contrast step. So `arm`, `z_program`, `q_arm`, `wt_mean_log2`, `wt_minus_alt_log2`,
  `frac_compounds_*`, `rank_in_P`, `loco_frequency` and `n_folds_kept` are all circular as evidence of p53
  specificity — the genes were picked for showing this pattern — and the magnitudes are selected-on
  maxima, optimistically large for these genes. `wt_mean_log2` inherits it through the S2 selection even
  though it is a one-arm mean. The cross-fitting and leave-one-compound-out columns hold **compounds** out,
  not labels: they bound compound-driven instability, they do not remove the circularity. The whole MG53
  screen block is **not** circular (one covariate's background gene set excludes the label-selected
  programs; nothing else uses the labels for selection).
- **The baseline is a drug well, not DMSO or untreated.** Every `wt_fold` is against the same line's
  median log2 CPM over that plate's drug wells; at program level the DMSO-referenced version is 0.025 log2
  larger [`export/downstream/program_scores_per_drugdose_line.csv`, `P_r2_mean` vs `P_u_dmso_mean`].
- **The effects are small and averaged over 142 treatments.** Median 1.060x, maximum 1.255x; 19 of 180
  induction-arm genes are below 1.02x. A single strong activator gives much larger folds — see the
  `fold_ida5` column in the effector table above — and the clean quantity (wild-type lines only, one
  activator) still needs a per-gene per-line extraction the export does not provide.
- **q_common must not be read as a p value.** `lambda_common` is 4.44 with 4,500 of 16,642 genes passing,
  and matched placebo exposures — real genes chosen before any fit — give **2 to 8,381** genes at
  q_common < 0.1 (median 5,331, expression-matched) and 897 to 5,344 (median 3,196, response-matched), so
  MG53 sits inside the placebo range [`genome_wide/tables/c_calibration.csv`, `N_q01_common`]. The
  exposure shuffles give 0 every time, but they break the exposure's line-level structure by construction,
  so they are not the yardstick. Only the comparison against background (27.0% / 34.5%) and the placebo
  percentiles are informative per gene, and the latter have 0.1 resolution.
- **q_diff saturates.** Its 0.99879 floor is a real BH value, not a missing one, so "none" for all 195
  means nowhere near significance, not "untested".
- **Low counts.** 13 of the 180 induction-arm genes sit below 5 CPM and one below 1 (PINCR, 0.65), where
  a zero count still receives a log2 CPM set by library size alone. `|diff|` is also not comparable across
  rows: `se_diff` spans 0.0021 to 0.0209, a 9.8x range, and the two largest `|diff|` values in the table
  (ZNF423 −0.0354 at 1.26 CPM, PINCR −0.0353 at 0.65 CPM) are its two noisiest rows. Read every slope next
  to `median_line_cpm` and its own `mde80_*` column.
- **The repressed arm is the weakest part.** Only 4 of its 15 genes are kept by all 5 cross-fitted
  programs, and those fold programs were top-25 fallbacks in 4 of the 5 folds
  [`export/downstream/program_flags.csv`, `flag`]. `loco_frequency` is blank for all 15 by construction
  (the leave-one-compound-out programs are derived in the induction direction only) and `rank_in_P` is
  blank for all 15 (it is a rank within the induction arm) — neither blank means missing data.
- **The design is smaller per gene than it looks.** `n_drugdoses` is 1,132 for every tested gene, but
  after pruning the 195 genes contribute 11 to 17 wild-type and 22 to 30 altered lines (median 17 and 30,
  df median 46), not the panel's 17 and 33 [`c_screen_genes.csv.gz`, `n_lines_WT`/`n_lines_alt`/`df`].
- **There is no true-MG53 scale here.** An earlier version of this caveat called it a range rather than a
  point, noting that the `ii_active` variant of the same split-half gives 0.610 and would halve the
  de-attenuation. That understates the problem twice. `ii_active` is estimated on the active exposures, not
  on the all-drug-dose scope these slopes are fitted at, so it is not scope-matched — and no subset variant
  is: 0.585 is `ii_p53` (the 50 drug-doses with curated P53_ACTIVITY z ≥ 3) and 0.706 is `ii_trim72` (the 23
  MG53-moving ones). More basically, dividing at all requires exposure error independent of outcome error,
  which same-well, same-denominator counting rules out. Every slope and bound here is per doubling of
  **measured** MG53 [`two_way/tables/trim72_reliability.csv`, `n_drugdoses`].
- **Readthrough spillover is positional and is never called "downstream".** TRIM72 lies 10.6 kb **3' of**
  PYCARD-AS1 and 17 kb **3' of** FUS on the same strand, so transcription running past them is counted as
  TRIM72; `readthrough_geometry` applies the same test to each outcome gene. It says nothing about
  regulation. Only the screen's `b_common_gw_rt` / `diff_gw_rt` columns adjust for it; no program column
  does. "Downstream" in this section means regulatory downstream of MG53 and nothing else.
- **Whether p53 regulates MG53 is out of scope** and no column here reports it. A gene's p53-activation
  fold change is in scope because it defines the read-out being tested.
- **Everything here is an association in mRNA 24 h after treatment.** Tahoe contains no MG53 perturbation
  and no protein data, so no slope in this table can separate MG53 changing a p53 target from the two
  moving together; and every mean over lines is over the lines that still had cells in the well at 24 h,
  which is not a random subset.
- If a per-gene fold change is needed for a gene **outside** the program, it is only in
  `genome_wide/tables/b_p53_program_genes.csv.gz`: `export/downstream/genes.csv` carries
  `program_wt_mean_log2` on just 195 of its 4,642 rows.