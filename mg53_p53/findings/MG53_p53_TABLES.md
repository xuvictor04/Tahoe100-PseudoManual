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
are 95% with cell-line-clustered standard errors.

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
program is flat. The only interval that excludes zero is **positive**, not negative.

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
| | Dinaciclib 5 uM | corrected log2 fold | +2.48 | positive | data-defined |
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

## Table C — MG53 -> p53 program, with mutants split by retained p53 activity

Activity = each line's mean p53-program induction under the p53-activating drug-doses. Reference points:
**null (truncating / splice / deletion) median = +0.0038; wild-type median = +0.1474.**

`tables/tableC_mutants_by_activity.csv`, per-line values in `tables/per_line_p53_activity.csv`

| Split | Group | Lines | two-way r (95% CI) | slope (95% CI) | direction |
|---|---|---|---|---|---|
| Data-defined inducibility | WT (functional p53) | 17 | +0.013 (−0.002, +0.027) | +0.0009 (−0.0014, +0.0032) | **none** |
| | Altered: **higher** activity (above null) | 18 | +0.024 (+0.010, +0.038) | +0.0010 (−0.0010, +0.0030) | **none** |
| | Altered: **lower** activity (at/below null) | 14 | +0.085 (+0.068, +0.101) | **+0.0043 (+0.0004, +0.0082)** | **positive** |
| Gene-panel functional call (list-based) | Responsive | 11 | +0.021 | +0.0014 (−0.0015, +0.0043) | none |
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
- MG53 is measured at trace level — median 5 UMIs per profile — and its split-half reliability is 0.289, so
  bounds on true MG53 are about 3.5x wider than bounds on measured MG53.
- Part of the measured MG53 signal is readthrough spillover rather than MG53's own transcript, which dilutes
  MG53 as an exposure in every table.
- The two intervals that just exclude zero (CollecTRI +0.0006; low-activity mutants +0.0004) rest on
  cell-line-clustered standard errors with 14 to 28 lines. They would probably not survive the
  label-permutation and placebo-gene machinery the pipeline applies to its primary test, and are not
  reported here as findings.
- Actual cell death and survival are effectively unmeasured: the per-line composition shift does not track
  surviving cell counts (r −0.01), and the atlas corrects composition out by design.
