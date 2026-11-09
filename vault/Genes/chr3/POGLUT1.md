---
symbol: "POGLUT1"
type: "gene"
col: 8682
ensembl_id: "ENSG00000163389"
name: "protein O-glucosyltransferase 1"
location: "3q13.33"
module: 137
arm: "+"
pooled_cpm: 11.83
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# POGLUT1

*protein O-glucosyltransferase 1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.89× (z +20.6, q 0e+00, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.650× (z -5.9, q 2e-06, down in 22 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.656× (z -5.8, q 2e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H7B]] (+0.77, fdr 7e-06), [[ST7L]] (+0.76, fdr 7e-06), [[GCFC2]] (+0.74, fdr 7e-06); moves opposite to [[MOSPD3]] (-0.73, fdr 7e-06), [[MED31]] (-0.70, fdr 7e-06), [[CBFA2T2]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TMEM92]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +20.6 | 0e+00 | 35/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.51×** | +16.5 | 0e+00 | 40/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +11.5 | 4e-28 | 40/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +10.6 | 5e-24 | 32/38 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.9 | 5e-17 | 16/20 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +8.5 | 1e-15 | 24/29 (RPMI-7951, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +6.9 | 5e-10 | 23/40 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +6.8 | 6e-10 | 26/47 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.3 | 8e-06 | 21/47 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.1 | 2e-05 | 16/48 (A-172, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +5.0 | 3e-05 | 17/47 (LS 180, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.011 | 11/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.056 | 14/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.094 | 11/47 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.0 | 0.100 | 4/21 (NCI-H2347, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.100 | 5/45 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.100 | 10/47 (PANC-1, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -5.9 | 2e-06 | 22/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -5.8 | 2e-06 | 22/47 (LS 180, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -5.5 | 7e-06 | 18/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -4.8 | 2e-04 | 20/47 (PANC-1, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.549×** | -4.3 | 0.002 | 14/44 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.751×** | -3.9 | 0.009 | 18/47 (SW480, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -3.7 | 0.015 | 18/47 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.778×** | -3.4 | 0.043 | 18/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.047 | 16/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.632×** | -3.3 | 0.060 | 12/47 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.790×** | -3.2 | 0.068 | 22/47 (NCI-H23, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.783×** | -3.2 | 0.075 | 14/46 (SW48, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.0 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.2) | [[Digitoxin (drug)]] 5 µM 0.324× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -9.0) |
| [[A-172 (line)]] | wt | 14.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +21.9) | — |
| [[HEC-1-A (line)]] | alt | 21.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.4) | — |
| [[HOP62 (line)]] | alt | 9.11 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 13.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.3) | — |
| [[J82 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +18.3) | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0470× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 5.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 7.66 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 15.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 7.15× (z +8.5) ⚠ toxic; transcription drop | [[Silodosin (drug)]] 5 µM 0.135× (z -9.0) |
| [[SW48 (line)]] | wt | 14.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +8.5) | [[Temsirolimus (drug)]] 0.5 µM 0.0879× (z -9.4) |
| [[A-427 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 9.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 7.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +10.0) | — |
| [[C32 (line)]] | wt | 9.05 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.131× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 7.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 8.17 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0960× (z -10.0) |
| [[SNU-423 (line)]] | alt | 5.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 19.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -8.7) |
| [[A498 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | +0.77 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[ST7L]] | +0.76 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.71 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD18A]] | +0.69 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[KICS2]] | +0.69 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[TASOR]] | +0.69 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[DIS3L]] | +0.69 | +0.77 / +0.45 | both halves | 3e-05 |  |
| [[RBM26-AS1]] | +0.68 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[TIA1]] | +0.68 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[YTHDC2]] | +0.68 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[NEK9]] | +0.68 | +0.72 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | -0.73 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[MED31]] | -0.70 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.69 | -0.73 / -0.50 | both halves | 1e-05 |  |
| [[UBE2O]] | -0.69 | -0.75 / -0.47 | both halves | 2e-05 |  |
| [[GNB2]] | -0.69 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[MACO1]] | -0.68 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.68 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[PLA2G15]] | -0.67 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[VRK3]] | -0.67 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.67 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[NTAN1]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[HEBP1]] | -0.66 | -0.61 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92]] | B | TMEM92 activity lowers POGLUT1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.45× higher at baseline in the lines without TMEM92 | 0.014 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[NDRG1]] | B | NDRG1 activity lowers POGLUT1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.80× higher at baseline in the lines without NDRG1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[FTCDNL1]] | B | FTCDNL1 activity raises POGLUT1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without FTCDNL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[RNF207]] | B | RNF207 activity raises POGLUT1's level | lines that do not express RNF207 (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without RNF207 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.8, 6.2); signed map (20.2, -31.5). **Vector** length 99.7, 22.5% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.1 | +20.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +16.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | protein O-glucosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:119,468,963-119,494,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS010, MGC32995, 9630046K23Rik, MDSRP, hCLP46, KDELCL1, Rumi; previously C3orf9, KTELC1 |
| Gene groups (HGNC) | Glycosyltransferase family 90 |
| Reactome | 3 pathways, smallest: Pre-NOTCH Processing in the Endoplasmic Reticulum; Pre-NOTCH Expression and Processing; Signaling by NOTCH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBL1](https://www.uniprot.org/uniprotkb/Q8NBL1) (Protein O-glucosyltransferase 1):

> Dual specificity glycosyltransferase that catalyzes the transfer of glucose and xylose from UDP-glucose and UDP-xylose, respectively, to a serine residue found in the consensus sequence of C-X-S-X-P-C. Specifically targets extracellular EGF repeats of protein such as CRB2, F7, F9 and NOTCH2. Acts as a positive regulator of Notch signaling by mediating O-glucosylation of Notch, leading to regulate muscle development. Notch glucosylation does not affect Notch ligand binding. Required during early …

**Summary**, from NCBI Gene [56983](https://www.ncbi.nlm.nih.gov/gene/56983):

> This gene encodes a protein with both O-glucosyltransferase and O-xylosyltransferase activity which localizes to the lumen of the endoplasmic reticulum. This protein has a carboxy-terminal KTEL motif which is predicted to function as an endoplasmic reticulum retention signal. This gene is an essential regulator of Notch signalling and likely plays a role in cell fate and tissue formation during development. It may also play a role in the pathogenesis of leukemia. Mutations in this gene have …

**Accessions** — [HGNC:22954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22954) · Entrez [56983](https://www.ncbi.nlm.nih.gov/gene/56983) · UniProt [Q8NBL1](https://www.uniprot.org/uniprotkb/Q8NBL1) · Ensembl [ENSG00000163389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163389)

## Data

Gene col 8682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8682); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8682]; `tensor/DDL_lfc|DDL_z.npy` [8682]; `embed/gene_vectors.npy` [8682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8682 or target_col == 8682). Every well: [[POGLUT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POGLUT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
