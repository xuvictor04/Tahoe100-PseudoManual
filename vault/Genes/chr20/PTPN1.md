---
symbol: "PTPN1"
type: "gene"
col: 12197
ensembl_id: "ENSG00000196396"
name: "protein tyrosine phosphatase non-receptor type 1"
location: "20q13.13"
module: 97
arm: "+"
pooled_cpm: 155.85
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PTPN1

*protein tyrosine phosphatase non-receptor type 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.07× (z +36.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.772× (z -6.4, q 7e-08, down in 24 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.801× (z -4.1, q 0.005, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HT-29 0.455×, HOP62 0.431×, RKO 0.413×, SW1417 0.562×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 0.422×, Hs 766T 0.417×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.503×; ⚠ cell-cycle shift, explains ~1% of this change); [[Radotinib (drug)]] 5 µM in 1 line (RKO 0.512×); [[Ponatinib (drug)]] 5 µM in 1 line (RKO 0.413×); [[Trametinib (drug)]] 0.5 µM in 1 line (RKO 0.519×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERGIC1]] (+0.61, fdr 1e-05), [[ABLIM3]] (+0.59, fdr 1e-05), [[ITGA5]] (+0.57, fdr 3e-05); moves opposite to [[CLIP4]] (-0.46, fdr 7e-05), [[DNAI4]] (-0.46, fdr 2e-04), [[GALNT7-DT]] (-0.45, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SERPINE1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.07×** | +36.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.88×** | +34.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.63×** | +33.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +16.5 | 0e+00 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +16.1 | 0e+00 | 41/49 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.06×** | +15.0 | 0e+00 | 48/49 (BT-474, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +12.5 | 5e-34 | 33/48 (LS 180, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +9.3 | 1e-18 | 37/50 (C32, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +8.7 | 1e-16 | 39/48 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +8.6 | 5e-16 | 26/48 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +8.5 | 1e-15 | 39/48 (LS 180, KATO III, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +8.3 | 4e-15 | 37/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +7.9 | 1e-13 | 43/49 (J82, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +7.8 | 2e-13 | 37/48 (KATO III, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +7.6 | 1e-12 | 38/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +6.7 | 1e-09 | 30/48 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.7 | 5e-07 | 25/48 (BT-474, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.20×** | +4.7 | 7e-05 | 22/48 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12197.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HT-29 0.455×, HOP62 0.431×, RKO 0.413×, SW1417 0.562×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 0.422×, Hs 766T 0.417×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.503×; ⚠ cell-cycle shift, explains ~1% of this change); [[Radotinib (drug)]] 5 µM in 1 line (RKO 0.512×); [[Ponatinib (drug)]] 5 µM in 1 line (RKO 0.413×); [[Trametinib (drug)]] 0.5 µM in 1 line (RKO 0.519×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.772×** | -6.4 | 7e-08 | 24/44 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.807×** | -5.6 | 8e-06 | 26/49 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.800×** | -5.3 | 2e-05 | 24/45 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~4% of this change | 0.840× | -4.5 | 8e-04 | 20/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.801×** | -4.1 | 0.005 | 24/47 (hTERT-HPNE, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.902× | -3.8 | 0.012 | 12/48 (RKO, A498, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.865× | -3.8 | 0.013 | 15/49 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.862× | -3.7 | 0.014 | 18/48 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.870× | -3.6 | 0.017 | 19/48 (RKO, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.899× | -3.5 | 0.031 | 7/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.885× | -3.4 | 0.031 | 12/50 (RKO, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 187 | 24 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 186 | 9 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.524× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 383 | 2 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.8) | [[Selinexor (drug)]] 5 µM 0.503× (z -11.0) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.512× (z -10.7) |
| [[LS 180 (line)]] | wt | 94.2 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 4.21× (z +17.6) | — |
| [[BT-474 (line)]] | alt | 218 | 8 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.45× (z +20.3) | — |
| [[HT-29 (line)]] | alt | 147 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.34× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 277 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.18× (z +22.2) | [[Dinaciclib (drug)]] 0.5 µM 0.562× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 171 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.90× (z +21.0) | — |
| [[C32 (line)]] | wt | 116 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 129 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.89× (z +20.3) | — |
| [[KATO III (line)]] | alt | 91.8 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 7.25× (z +25.2) | — |
| [[NCI-H460 (line)]] | wt | 76.4 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.57× (z +28.0) | — |
| [[SW480 (line)]] | alt | 180 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +33.0) | — |
| [[A-427 (line)]] | wt | 98.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +21.1) | — |
| [[COLO 205 (line)]] | alt | 143 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 221 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.65× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -11.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 77.7 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +21.3) | — |
| [[Panc 03.27 (line)]] | alt | 146 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.54× (z +21.1) | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.90× (z +17.3) | — |
| [[A-172 (line)]] | wt | 126 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.91× (z +19.2) | — |
| [[A498 (line)]] | wt | 204 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.4) | — |
| [[HEC-1-A (line)]] | alt | 95.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 387 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 359 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +22.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 113 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 145 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +19.0) | — |
| [[NCI-H2030 (line)]] | alt | 130 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +22.0) | — |
| [[NCI-H23 (line)]] | alt | 192 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +20.1) | — |
| [[PANC-1 (line)]] | alt | 114 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +18.9) | — |
| [[SW 900 (line)]] | alt | 185 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +12.2) | [[Docetaxel (drug)]] 0.05 µM 0.466× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~4% of this change |
| [[C-33 A (line)]] | alt | 86.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.46× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 122 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.24× (z +20.0) | — |
| [[H4 (line)]] | wt | 139 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 135 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.57× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 250 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.07× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 94.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +16.8) | — |
| [[SNU-1 (line)]] | wt | 89.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +13.1) | — |
| [[A549 (line)]] | wt | 106 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +19.5) | — |
| [[HCT15 (line)]] | alt | 136 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 110 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +17.6) | — |
| [[SNU-423 (line)]] | alt | 201 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.36× (z +15.9) | — |
| [[SW48 (line)]] | wt | 84.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.67× (z +19.0) | — |
| [[AN3 CA (line)]] | alt | 86.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.78× (z +9.8) | [[AZD2858 (drug)]] 0.5 µM 0.120× (z -9.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 89.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.71× (z +9.5) | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 201 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ABLIM3]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ITGA5]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 | pathway: Cellular responses to mechanical stimuli |
| [[SEC14L2]] | +0.57 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SERPINE1]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 | pathway: Platelet activation, signaling and aggregation |
| [[ANGPTL4]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[AKAP13]] | +0.56 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[TGM2]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[MT1X]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 | STRING 443 |
| [[TBC1D2]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MEIS3]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[GBA2]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIP4]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[DNAI4]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | -0.45 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[PER3]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[BBOX1-AS1]] | -0.44 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[TESMIN]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE1]] | B | SERPINE1 activity weakens PTPN1's drug response | lines that do not express SERPINE1 (27) vs lines expressing it (23) | the lines without SERPINE1 respond 1.15× as strongly (z diff -0.95); strongest at Idarubicin (hydrochloride) 5 µM: 1.77x vs 1.35x (z diff -3.4) | 0.046 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615; artifact flags |
| [[ITGA5]] | B | ITGA5 activity raises PTPN1's level | lines that do not express ITGA5 (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without ITGA5 | 0.048 | ⚠ within organs, on part of the lines; also absent: CACNG6, PLAUR, CAV1 |
| [[SERPINE1]] | B | SERPINE1 activity raises PTPN1's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 1.49× lower at baseline in the lines without SERPINE1 | 0.063 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.6, 12.0); signed map (15.1, 35.8). **Vector** length 114, 35.4% of its response variance represented; |z| ≥ 3 in 1,692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +15.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.8 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +16.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.5 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.3 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +8.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.2 | +3.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.7 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -7.5 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.5 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.2 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,510,321-50,585,241 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PTP1B |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 25 pathways, smallest: PTK6 Down-Regulation; Regulation of IFNA/IFNB signaling; Regulation of IFNG signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P18031](https://www.uniprot.org/uniprotkb/P18031) (Tyrosine-protein phosphatase non-receptor type 1):

> Tyrosine-protein phosphatase which acts as a regulator of endoplasmic reticulum unfolded protein response. Mediates dephosphorylation of EIF2AK3/PERK; inactivating the protein kinase activity of EIF2AK3/PERK. May play an important role in CKII- and p60c-src-induced signal transduction cascades. May regulate the EFNA5-EPHA3 signaling pathway which modulates cell reorganization and cell-cell repulsion. May also regulate the hepatocyte growth factor receptor signaling pathway through …

**Summary**, from NCBI Gene [5770](https://www.ncbi.nlm.nih.gov/gene/5770):

> The protein encoded by this gene is the founding member of the protein tyrosine phosphatase (PTP) family, which was isolated and identified based on its enzymatic activity and amino acid sequence. PTPs catalyze the hydrolysis of the phosphate monoesters specifically on tyrosine residues. Members of the PTP family share a highly conserved catalytic motif, which is essential for the catalytic activity. PTPs are known to be signaling molecules that regulate a variety of cellular processes …

**Accessions** — [HGNC:9642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9642) · Entrez [5770](https://www.ncbi.nlm.nih.gov/gene/5770) · UniProt [P18031](https://www.uniprot.org/uniprotkb/P18031) · Ensembl [ENSG00000196396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196396)

## Data

Gene col 12197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12197); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12197]; `tensor/DDL_lfc|DDL_z.npy` [12197]; `embed/gene_vectors.npy` [12197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12197 or target_col == 12197). Every well: [[PTPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
