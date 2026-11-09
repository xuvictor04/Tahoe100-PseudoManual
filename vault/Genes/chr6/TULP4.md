---
symbol: "TULP4"
type: "gene"
col: 5054
ensembl_id: "ENSG00000130338"
name: "TUB like protein 4"
location: "6q25.3"
module: 143
arm: "+"
pooled_cpm: 147.96
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# TULP4

*TUB like protein 4* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +20.9, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.673× (z -4.6, q 0.003, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.784× (z -3.8, q 0.050, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.471×, C32 0.477×, AN3 CA 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.124×, SNU-1 0.404×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.341×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.433×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.584×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.598×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF12]] (+0.64, fdr 7e-06), [[ATE1]] (+0.63, fdr 1e-05), [[PRRC2B]] (+0.62, fdr 1e-05); moves opposite to [[GOLPH3L]] (-0.66, fdr 7e-06), [[KLHL28]] (-0.64, fdr 7e-06), [[TBC1D23]] (-0.62, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NLRP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +20.9 | 0e+00 | 40/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +11.6 | 1e-28 | 42/49 (BT-474, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +11.5 | 2e-28 | 40/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +9.3 | 2e-18 | 44/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +8.9 | 4e-17 | 40/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +8.7 | 3e-16 | 35/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +8.7 | 4e-16 | 39/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +8.5 | 1e-15 | 31/49 (Panc 03.27, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.1 | 4e-14 | 33/47 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.0 | 2e-10 | 30/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.33×** | +6.3 | 2e-08 | 30/48 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.8 | 3e-07 | 25/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +5.6 | 9e-07 | 36/48 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.8 | 5e-05 | 26/48 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.8 | 7e-05 | 19/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.4 | 4e-04 | 24/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.002 | 26/49 (CFPAC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 24/48 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.7 | 0.005 | 5/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.471×, C32 0.477×, AN3 CA 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.124×, SNU-1 0.404×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.341×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.433×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.584×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.598×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.673×** | -4.6 | 0.003 | 32/47 (A498, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.050 | 31/48 (HS-578T, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.855× | -3.5 | 0.070 | 15/48 (SW1417, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.850× | -3.5 | 0.070 | 21/47 (HepG2/C3A, SW1417, …) | inconsistent across doses |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.857× | -3.4 | 0.070 | 15/49 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 0.860× | -3.4 | 0.075 | 19/48 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.19 | 15/49 (SHP-77, SW48, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 197 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 105 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 108 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +21.9) | — |
| [[SW480 (line)]] | alt | 167 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.1) | — |
| [[C32 (line)]] | wt | 326 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -10.5) |
| [[HS-578T (line)]] | alt | 132 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.6) | — |
| [[Hs 766T (line)]] | wt | 81.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.2) | — |
| [[hTERT-HPNE (line)]] | wt | 112 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.3) | — |
| [[KATO III (line)]] | alt | 167 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +22.7) | — |
| [[RPMI-7951 (line)]] | alt | 165 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 48.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 169 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 94.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.0) | — |
| [[A-427 (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A498 (line)]] | wt | 98.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 74.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.8) | — |
| [[BT-474 (line)]] | alt | 163 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 93.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 173 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 260 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +20.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.341× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 154 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 115 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 86.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 212 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 94.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.0) | — |
| [[A-172 (line)]] | wt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.9) | — |
| [[A549 (line)]] | wt | 93.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 399 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 60.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) | — |
| [[LoVo (line)]] | wt | 158 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 81.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +21.0) | — |
| [[PANC-1 (line)]] | alt | 186 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 242 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.404× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 210 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 197 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 248 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 165 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 194 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF12]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ATE1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PRRC2B]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A13]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FBXL17]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PARD3B]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ZNF704]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[LARP1]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MTHFD1L]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ARID1B]] | +0.57 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[DOCK1]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLPH3L]] | -0.66 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[KLHL28]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[TBC1D23]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SWI5]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SEC22A]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[DIS3]] | -0.60 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RINT1]] | -0.60 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[EAF2]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NPRL2]] | -0.59 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[SRP54]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[GOLGA2]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[COG6]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLRP1]] | B | NLRP1 activity strengthens TULP4's drug response | lines that do not express NLRP1 (21) vs lines expressing it (28) | the lines without NLRP1 respond 0.71× as strongly (z diff +1.49); strongest at Digitoxin 5 µM: 1.18x vs 1.62x (z diff +2.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; target measured in part of the lines; artifact flags |
| [[CRPPA]] | B | CRPPA activity raises TULP4's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without CRPPA | 0.098 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent |
| [[ARID2]] | C | ARID2's natural level weakens TULP4's drug response | ARID2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.00; direction clear | 0.048 | ⚠ tissue can mimic it; precision caveat |
| [[MTHFD1L]] | C | MTHFD1L activity raises TULP4's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.0, -33.7); signed map (23.7, -31.9). **Vector** length 116, 38.6% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +9.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.5 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.5 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.0 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.9 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.8 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.7 | +6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TUB like protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:158,232,236-158,511,828 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TUSP, KIAA1397 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRJ4](https://www.uniprot.org/uniprotkb/Q9NRJ4) (Tubby-related protein 4):

> May be a substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins.

**Summary**, from NCBI Gene [56995](https://www.ncbi.nlm.nih.gov/gene/56995):

> Predicted to be involved in protein ubiquitination. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15530) · Entrez [56995](https://www.ncbi.nlm.nih.gov/gene/56995) · UniProt [Q9NRJ4](https://www.uniprot.org/uniprotkb/Q9NRJ4) · Ensembl [ENSG00000130338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130338)

## Data

Gene col 5054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5054); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5054]; `tensor/DDL_lfc|DDL_z.npy` [5054]; `embed/gene_vectors.npy` [5054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5054 or target_col == 5054). Every well: [[TULP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TULP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
