---
symbol: "SPIRE2"
type: "gene"
col: 12943
ensembl_id: "ENSG00000204991"
name: "spire type actin nucleation factor 2"
location: "16q24.3"
module: 55
arm: "+"
pooled_cpm: 18.86
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 19
direction_downstream: 0
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SPIRE2

*spire type actin nucleation factor 2* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.28× (z +11.4, q 2e-27, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.424× (z -11.8, q 3e-29, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.471× (z -10.3, q 2e-22, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB4]] (+0.59, fdr 7e-05), [[TC2N]] (+0.57, fdr 3e-05), [[HNF4A]] (+0.57, fdr 2e-05); moves opposite to [[ACAD11]] (-0.52, fdr 3e-04), [[LINC01684]] (-0.52, fdr 9e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[CEACAM5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +11.4 | 2e-27 | 40/47 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +9.8 | 2e-20 | 37/47 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +8.3 | 1e-14 | 34/46 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +6.0 | 4e-07 | 23/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.002 | 15/47 (BT-474, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.34×** | +4.1 | 0.005 | 12/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.036 | 8/46 (A-172, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.044 | 15/42 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.050 | 11/46 (A-427, SW48, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.065 | 10/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.077 | 13/46 (NCI-H460, LS 180, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.26× | +3.0 | 0.12 | 3/47 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -11.8 | 3e-29 | 36/44 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -10.3 | 2e-22 | 38/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -8.7 | 1e-15 | 29/46 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -8.4 | 8e-15 | 29/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -7.6 | 3e-12 | 31/46 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.587×** | -7.3 | 3e-11 | 30/46 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.587×** | -7.3 | 3e-11 | 32/46 (HT-29, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -6.8 | 6e-10 | 28/46 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.603×** | -6.6 | 2e-09 | 25/46 (COLO 205, A-427, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -6.3 | 2e-08 | 27/46 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -6.0 | 8e-08 | 23/46 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -5.5 | 2e-06 | 26/42 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -5.4 | 3e-06 | 26/46 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.485×** | -5.2 | 9e-06 | 23/45 (KATO III, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.708×** | -4.7 | 1e-04 | 22/47 (BT-474, C-33 A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -4.6 | 1e-04 | 19/46 (COLO 205, HepG2/C3A, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.558×** | -4.2 | 0.001 | 20/40 (COLO 205, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.660×** | -4.0 | 0.002 | 11/47 (HT-29, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.735×** | -4.0 | 0.002 | 18/47 (NCI-H1792, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 66.3 | 0 | 11 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.233× (z -11.1) |
| [[COLO 205 (line)]] | alt | 62.2 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.161× (z -11.8) |
| [[HT-29 (line)]] | alt | 31.4 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.168× (z -11.8) |
| [[LoVo (line)]] | wt | 29.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -13.1) |
| [[A-427 (line)]] | wt | 24.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -11.7) ⚠ cell-cycle shift, explains ~85% of this change |
| [[AsPC-1 (line)]] | alt | 28.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -8.5) |
| [[BT-474 (line)]] | alt | 32.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -8.9) |
| [[LS 180 (line)]] | wt | 41.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.258× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 20.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 7.31 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM 0.0562× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0912× (z -11.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 8.18 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 7.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0711× (z -9.3) |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB4]] | +0.59 | +0.37 / +0.53 | both halves | 7e-05 |  |
| [[TC2N]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[HNF4A]] | +0.57 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[CATSPERB]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[VILL]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LSMEM2]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[EZR]] | +0.56 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[PIM1]] | +0.56 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[MROH7]] | +0.55 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NR4A1]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[NPSR1]] | +0.55 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[PCK1]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAD11]] | -0.52 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[LINC01684]] | -0.52 | -0.38 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM5]] | B | CEACAM5 activity raises SPIRE2's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without CEACAM5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[MCF2L]] | B | MCF2L activity raises SPIRE2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without MCF2L | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[LGALS4]] | B | LGALS4 activity raises SPIRE2's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.10× lower at baseline in the lines without LGALS4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises SPIRE2's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.99× lower at baseline in the lines without TMC6 | 0.036 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[ARHGEF16]] | B | ARHGEF16 activity raises SPIRE2's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without ARHGEF16 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[NPSR1]] | B | NPSR1 activity raises SPIRE2's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.49× lower at baseline in the lines without NPSR1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[MYO7B]] | B | MYO7B activity raises SPIRE2's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.47× lower at baseline in the lines without MYO7B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[NOXA1]] | B | NOXA1 activity raises SPIRE2's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without NOXA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[SHH]] | B | SHH activity raises SPIRE2's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.60× lower at baseline in the lines without SHH | 0.073 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[TJP3]] | B | TJP3 activity raises SPIRE2's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.87× lower at baseline in the lines without TJP3 | 0.073 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[HCN1]] | B | HCN1 activity raises SPIRE2's level | lines that do not express HCN1 (37) vs lines expressing it (13) | 1.31× lower at baseline in the lines without HCN1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, APOH, GCG; maybe low, not absent |
| [[PCDH1]] | B | PCDH1 activity raises SPIRE2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without PCDH1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, 52.1); signed map (62.2, 9.7). **Vector** length 73.2, 14.3% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +9.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | -0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | +0.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.7 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | spire type actin nucleation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,818,179-89,871,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | spir-2, KIAA1832 |
| Gene groups (HGNC) | KIND domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWL2](https://www.uniprot.org/uniprotkb/Q8WWL2) (Protein spire homolog 2):

> Acts as an actin nucleation factor, remains associated with the slow-growing pointed end of the new filament. Involved in intracellular vesicle transport along actin fibers, providing a novel link between actin cytoskeleton dynamics and intracellular transport (By similarity). Required for asymmetric spindle positioning and asymmetric cell division during meiosis. Required for normal formation of the cleavage furrow and for polar body extrusion during female germ cell meiosis. Also acts in the …

**Summary**, from NCBI Gene [84501](https://www.ncbi.nlm.nih.gov/gene/84501):

> Predicted to enable microtubule binding activity. Involved in establishment of meiotic spindle localization; formin-nucleated actin cable assembly; and positive regulation of double-strand break repair. Predicted to be located in cleavage furrow. Predicted to be active in cell cortex and cytoplasmic vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30623) · Entrez [84501](https://www.ncbi.nlm.nih.gov/gene/84501) · UniProt [Q8WWL2](https://www.uniprot.org/uniprotkb/Q8WWL2) · Ensembl [ENSG00000204991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204991)

## Data

Gene col 12943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12943); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12943]; `tensor/DDL_lfc|DDL_z.npy` [12943]; `embed/gene_vectors.npy` [12943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12943 or target_col == 12943). Every well: [[SPIRE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIRE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
