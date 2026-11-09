---
symbol: "NEK1"
type: "gene"
col: 6040
ensembl_id: "ENSG00000137601"
name: "NIMA related kinase 1"
location: "4q33"
module: 15
arm: "-"
pooled_cpm: 84.76
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NEK1

*NIMA related kinase 1* — 4q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.83× (z +12.0, q 3e-30, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.748× (z -8.1, q 3e-13, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP290]] (+0.62, fdr 7e-06), [[TBC1D19]] (+0.58, fdr 1e-05), [[CPLANE1]] (+0.56, fdr 1e-05); moves opposite to [[ZFYVE27]] (-0.61, fdr 1e-05), [[GOT1-DT]] (-0.58, fdr 1e-04), [[LINC00115]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +12.0 | 3e-30 | 44/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +10.6 | 1e-23 | 31/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.2 | 1e-17 | 43/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +9.0 | 3e-17 | 38/48 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +7.9 | 5e-13 | 38/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.9 | 4e-10 | 34/48 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.4 | 1e-08 | 29/48 (LS 180, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +6.0 | 1e-07 | 32/48 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.6 | 1e-06 | 28/48 (COLO 205, SW480, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +5.6 | 2e-06 | 38/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.5 | 2e-06 | 29/47 (C32, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.26×** | +4.7 | 1e-04 | 26/48 (COLO 205, HepG2/C3A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 23/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 26/49 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +4.3 | 7e-04 | 28/48 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 24/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.006 | 18/47 (C32, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.011 | 20/47 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -8.1 | 3e-13 | 31/49 (A498, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.9 | 9e-13 | 31/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -7.0 | 7e-10 | 29/48 (SNU-423, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -6.8 | 1e-09 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.743×** | -5.9 | 5e-07 | 31/48 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.570×** | -5.8 | 5e-07 | 25/36 (SK-MEL-2, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -5.3 | 1e-05 | 29/49 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.602×** | -5.3 | 1e-05 | 29/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.761×** | -5.2 | 1e-05 | 25/47 (SHP-77, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.788×** | -4.7 | 1e-04 | 27/48 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.812×** | -4.1 | 0.002 | 24/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.807×** | -4.1 | 0.002 | 25/47 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.821×** | -3.9 | 0.004 | 23/49 (SK-MEL-2, COLO 205, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.7 | 0.008 | 23/50 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.083 | 13/48 (HepG2/C3A, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 64.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +16.7) | — |
| [[LS 180 (line)]] | wt | 24.8 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.18× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 110 | 6 | 0 | [[Harringtonine (drug)]] 5 µM 3.34× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 47.5 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.40× (z +11.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 5.08× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 114 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.8) |
| [[PANC-1 (line)]] | alt | 71.5 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.452× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.484× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 131 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HT-29 (line)]] | alt | 34.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.6) | — |
| [[J82 (line)]] | alt | 81.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.429× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 89.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -9.3) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 39.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.8) | — |
| [[SW480 (line)]] | alt | 85.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +12.5) | — |
| [[A-172 (line)]] | wt | 120 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.9) |
| [[A549 (line)]] | wt | 72.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.4) |
| [[BT-474 (line)]] | alt | 31.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.519× (z -9.8) |
| [[Hs 766T (line)]] | wt | 96.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.388× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.9) |
| [[RKO (line)]] | wt | 83.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 60.0 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.108× (z -8.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.117× (z -8.6) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -12.0) |
| [[A498 (line)]] | wt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -12.7) |
| [[C32 (line)]] | wt | 170 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 75.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 193 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 66.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.03× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.178× (z -9.4) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.0) |
| [[KATO III (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 74.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.144× (z -10.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.416× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP290]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 | STRING 635 |
| [[TBC1D19]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CPLANE1]] | +0.56 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[PRXL2C]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[WDR7]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SLC36A4]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.55 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FAN1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FER]] | +0.54 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[SMARCA5]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[TTBK2]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ACOT13]] | +0.53 | +0.67 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE27]] | -0.61 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[GOT1-DT]] | -0.58 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[LINC00115]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[HOXB6]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SLC12A9]] | -0.54 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[MIR762HG]] | -0.53 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[PANK1]] | -0.52 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[EPB41L4B]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LRP5L]] | -0.52 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[CAPN10-DT]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[RNF4]] | -0.51 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[AGAP3]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.8, 24.7); signed map (-19.4, -24.9). **Vector** length 111, 33.0% of its response variance represented; |z| ≥ 3 in 1,298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +5.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.3 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q33 — chr4:169,369,704-169,612,632 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-55, KIAA1901 |
| Gene groups (HGNC) | NIMA related kinase family |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PY6](https://www.uniprot.org/uniprotkb/Q96PY6) (Serine/threonine-protein kinase Nek1):

> Phosphorylates serines and threonines, but also appears to possess tyrosine kinase activity. Involved in DNA damage checkpoint control and for proper DNA damage repair. In response to injury that includes DNA damage, NEK1 phosphorylates VDAC1 to limit mitochondrial cell death. May be implicated in the control of meiosis (By similarity). Involved in cilium assembly.

**Summary**, from NCBI Gene [4750](https://www.ncbi.nlm.nih.gov/gene/4750):

> The protein encoded by this gene is a serine/threonine kinase involved in cell cycle regulation. The encoded protein is found in a centrosomal complex with FEZ1, a neuronal protein that plays a role in axonal development. Defects in this gene are a cause of polycystic kidney disease (PKD). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:7744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7744) · Entrez [4750](https://www.ncbi.nlm.nih.gov/gene/4750) · UniProt [Q96PY6](https://www.uniprot.org/uniprotkb/Q96PY6) · Ensembl [ENSG00000137601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137601)

## Data

Gene col 6040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6040); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6040]; `tensor/DDL_lfc|DDL_z.npy` [6040]; `embed/gene_vectors.npy` [6040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6040 or target_col == 6040). Every well: [[NEK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
