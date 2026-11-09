---
symbol: "STK4"
type: "gene"
col: 2071
ensembl_id: "ENSG00000101109"
name: "serine/threonine kinase 4"
location: "20q13.12"
module: 78
arm: "+"
pooled_cpm: 191.72
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# STK4

*serine/threonine kinase 4* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.77× (z +38.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.829× (z -8.8, q 1e-15, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAP1]] (+0.70, fdr 7e-06), [[SEPTIN10]] (+0.70, fdr 7e-06), [[ARPC2]] (+0.69, fdr 1e-05); moves opposite to [[ADI1]] (-0.59, fdr 3e-05), [[DYRK1A]] (-0.59, fdr 6e-05), [[CHASERR]] (-0.58, fdr 4e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IL13RA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +38.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +37.0 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +33.7 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +17.1 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +13.2 | 2e-37 | 40/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +12.2 | 3e-32 | 38/48 (SW480, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +12.2 | 3e-32 | 39/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +10.1 | 4e-22 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +9.2 | 2e-18 | 38/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +8.0 | 8e-14 | 25/48 (AsPC-1, SW480, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +6.8 | 5e-10 | 35/49 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.6 | 2e-09 | 22/49 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +6.4 | 6e-09 | 30/48 (PANC-1, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.18× | +6.2 | 3e-08 | 20/48 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | 1.17× | +6.0 | 1e-07 | 23/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +4.6 | 1e-04 | 24/48 (NCI-H460, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +4.4 | 4e-04 | 15/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +4.3 | 4e-04 | 8/48 (A498, BT-474, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.006 | 8/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.10× | +3.5 | 0.009 | 0/48 | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.829×** | -8.8 | 1e-15 | 22/48 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.804×** | -7.9 | 7e-13 | 24/47 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.869× | -7.5 | 1e-11 | 21/48 (HEC-1-A, J82, …) | top dose only | composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | 0.864× | -7.4 | 2e-11 | 20/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.760×** | -7.4 | 2e-11 | 32/47 (SW1417, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.818×** | -7.3 | 3e-11 | 25/48 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.831×** | -7.0 | 2e-10 | 24/49 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.831×** | -7.0 | 2e-10 | 23/47 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.829×** | -6.8 | 6e-10 | 24/47 (J82, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.858× | -6.4 | 1e-08 | 20/50 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.851× | -6.1 | 7e-08 | 20/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.876× | -5.9 | 2e-07 | 17/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.877× | -4.8 | 8e-05 | 18/48 (KATO III, J82, …) | top dose only | composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.844× | -4.5 | 2e-04 | 18/48 (A-427, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.871× | -4.5 | 2e-04 | 18/48 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.873× | -4.5 | 3e-04 | 18/48 (A-427, RKO, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.916× | -4.4 | 4e-04 | 16/49 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.927× | -4.1 | 0.002 | 5/48 (RKO, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.884× | -4.1 | 0.002 | 13/47 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 399 | 3 | 9 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +16.2) | [[Cobimetinib (drug)]] 5 µM 0.493× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 142 | 12 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +25.2) | — |
| [[AsPC-1 (line)]] | alt | 237 | 9 (4 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.632× (z -8.6) |
| [[SW480 (line)]] | alt | 283 | 11 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +28.3) | — |
| [[A-427 (line)]] | wt | 209 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.17× (z +13.5) | [[Trametinib (drug)]] 0.5 µM 0.595× (z -10.9) |
| [[BT-474 (line)]] | alt | 331 | 8 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.76× (z +21.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.533× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 267 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +23.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.34× (z +22.0) | — |
| [[NCI-H1573 (line)]] | alt | 147 | 9 (6 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 194 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +18.0) | — |
| [[LoVo (line)]] | wt | 101 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +21.6) | [[Harringtonine (drug)]] 5 µM 0.567× (z -9.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[RKO (line)]] | wt | 411 | 4 (1 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +13.9) | [[Radotinib (drug)]] 5 µM 0.642× (z -12.0) |
| [[KATO III (line)]] | alt | 191 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +17.6) | [[Harringtonine (drug)]] 5 µM 0.516× (z -11.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HEC-1-A (line)]] | alt | 111 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +17.7) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -15.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 174 | 5 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +14.7) | — |
| [[LS 180 (line)]] | wt | 103 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +18.1) | — |
| [[NCI-H2030 (line)]] | alt | 213 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 199 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.95× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 231 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +17.0) | — |
| [[A498 (line)]] | wt | 108 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +22.8) | — |
| [[A549 (line)]] | wt | 147 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +15.8) | [[Cobimetinib (drug)]] 5 µM 0.484× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 145 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 194 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +14.8) | [[Harringtonine (drug)]] 5 µM 0.498× (z -9.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[J82 (line)]] | alt | 490 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 245 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +15.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 183 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +17.4) | — |
| [[SNU-1 (line)]] | wt | 172 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.25× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 124 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.04× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 286 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +18.8) | — |
| [[A-172 (line)]] | wt | 112 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +17.1) | — |
| [[AN3 CA (line)]] | alt | 145 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 241 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +11.0) | — |
| [[C32 (line)]] | wt | 108 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.10× (z +13.8) | — |
| [[H4 (line)]] | wt | 168 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 171 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 161 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 141 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 197 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 101 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +18.1) | — |
| [[Panc 03.27 (line)]] | alt | 139 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +16.7) | — |
| [[RPMI-7951 (line)]] | alt | 265 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 131 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 186 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +16.8) | — |
| [[SW48 (line)]] | wt | 155 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +13.4) | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 186 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAP1]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ARPC2]] | +0.69 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[LINC03009-1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[SFT2D1]] | +0.61 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[PHC2]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CDCP1]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL8]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[GP6-AS1]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PFDN2]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PAQR5]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADI1]] | -0.59 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[DYRK1A]] | -0.59 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[CHASERR]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[RAF1]] | -0.57 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[RNF115]] | -0.56 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CDKN1B]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RAB21]] | -0.55 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[CREB3L4]] | -0.55 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[TCEAL1]] | -0.55 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[TLK2]] | -0.54 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[RBM33]] | -0.53 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[CFAP418]] | -0.53 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL13RA2]] | B | IL13RA2 activity raises STK4's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 1.28× lower at baseline in the lines without IL13RA2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.2, 5.5); signed map (5.7, 45.1). **Vector** length 134, 43.4% of its response variance represented; |z| ≥ 3 in 1,496 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.2 | +38.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.1 | +33.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.3 | +37.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.2 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +6.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -11.5 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -8.2 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.1 | -8.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.8 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.3 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.1 | -7.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.0 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,966,494-45,080,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MST1, KRS2, YSK3 |
| Gene groups (HGNC) | STK3/STK4 kinase family |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13043](https://www.uniprot.org/uniprotkb/Q13043) (Serine/threonine-protein kinase 4):

> Stress-activated, pro-apoptotic kinase which, following caspase-cleavage, enters the nucleus and induces chromatin condensation followed by internucleosomal DNA fragmentation. Key component of the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and …

**Summary**, from NCBI Gene [6789](https://www.ncbi.nlm.nih.gov/gene/6789):

> The protein encoded by this gene is a cytoplasmic kinase that is structurally similar to the yeast Ste20p kinase, which acts upstream of the stress-induced mitogen-activated protein kinase cascade. The encoded protein can phosphorylate myelin basic protein and undergoes autophosphorylation. A caspase-cleaved fragment of the encoded protein has been shown to be capable of phosphorylating histone H2B. The particular phosphorylation catalyzed by this protein has been correlated with apoptosis, and …

**Accessions** — [HGNC:11408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11408) · Entrez [6789](https://www.ncbi.nlm.nih.gov/gene/6789) · UniProt [Q13043](https://www.uniprot.org/uniprotkb/Q13043) · Ensembl [ENSG00000101109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101109)

## Data

Gene col 2071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2071); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2071]; `tensor/DDL_lfc|DDL_z.npy` [2071]; `embed/gene_vectors.npy` [2071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2071 or target_col == 2071). Every well: [[STK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
