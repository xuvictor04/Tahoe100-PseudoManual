---
symbol: "MAP2K6"
type: "gene"
col: 3016
ensembl_id: "ENSG00000108984"
name: "mitogen-activated protein kinase kinase 6"
location: "17q24.3"
module: 27
arm: "+"
pooled_cpm: 11.87
n_lines_expressing: 29
n_dd_up: 46
n_dd_down: 32
n_dd_up_clean: 39
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 14
direction_downstream: 21
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MAP2K6

*mitogen-activated protein kinase kinase 6* — 17q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 12.6× (z +22.6, q 0e+00, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.435× (z -7.5, q 5e-11, down in 18 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORL1]] (+0.64, fdr 1e-05), [[RORC]] (+0.63, fdr 1e-05), [[MPP7]] (+0.60, fdr 1e-05); moves opposite to [[C11orf91]] (-0.52, fdr 3e-05), [[WNT9A]] (-0.52, fdr 2e-05), [[TEP1]] (-0.51, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SORBS2]] → it (grade B ⚠); 21 go from it, the strongest it → [[HNF1A-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **12.6×** | +22.6 | 0e+00 | 24/26 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.26×** | +18.8 | 0e+00 | 23/25 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **7.29×** | +17.7 | 0e+00 | 24/25 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.94×** | +12.2 | 3e-32 | 6/17 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +12.2 | 3e-32 | 5/11 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **3.86×** | +12.0 | 2e-31 | 23/25 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **2.48×** | +11.4 | 2e-28 | 22/26 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.71×** | +8.9 | 4e-17 | 17/26 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +8.6 | 5e-16 | 4/22 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **2.41×** | +7.8 | 3e-13 | 21/26 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +7.6 | 2e-12 | 1/12 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.4 | 5e-12 | 16/26 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **4.89×** | +7.4 | 6e-12 | 19/24 (HEC-1-A, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **2.22×** | +6.7 | 9e-10 | 18/24 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.07×** | +6.5 | 3e-09 | 18/26 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **3.85×** | +6.3 | 1e-08 | 19/25 (A498, HEC-1-A, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **2.06×** | +6.2 | 2e-08 | 17/25 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Regorafenib (drug)]] 5 µM |  | **3.54×** | +5.9 | 1e-07 | 12/24 (NCI-H23, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.61×** | +5.9 | 1e-07 | 13/26 (SW480, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -7.5 | 5e-11 | 18/22 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.602×** | -6.4 | 3e-08 | 19/22 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.616×** | -6.2 | 1e-07 | 18/26 (CHP-212, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.521×** | -5.9 | 7e-07 | 19/26 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -5.6 | 2e-06 | 18/26 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -5.6 | 2e-06 | 12/25 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -5.2 | 2e-05 | 21/26 (COLO 205, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.567×** | -5.1 | 2e-05 | 17/24 (Panc 03.27, NCI-H661, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.554×** | -5.1 | 2e-05 | 13/25 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -5.0 | 3e-05 | 18/26 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.582×** | -4.9 | 6e-05 | 17/26 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.612×** | -4.4 | 5e-04 | 20/26 (Panc 03.27, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -4.3 | 6e-04 | 17/23 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.633×** | -4.1 | 0.002 | 14/26 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.636×** | -4.1 | 0.002 | 15/24 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.003 | 13/25 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.676×** | -3.4 | 0.021 | 13/25 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.693×** | -3.3 | 0.027 | 10/26 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.041 | 9/25 (COLO 205, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 160 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0143× (z -30.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0125× (z -22.3) |
| [[HEC-1-A (line)]] | alt | 55.1 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -14.4) |
| [[SW480 (line)]] | alt | 19.1 | 4 | 5 (2 ⚠) | [[Binimetinib (drug)]] 0.05 µM 4.06× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0982× (z -11.3) |
| [[SW1417 (line)]] | alt | 39.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -12.5) |
| [[LS 180 (line)]] | wt | 42.6 | 2 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.51× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -18.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0338× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.0805× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -11.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0697× (z -10.4) |
| [[SW48 (line)]] | wt | 48.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.159× (z -10.1) |
| [[A498 (line)]] | wt | 14.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 12.5× (z +12.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -10.0) |
| [[HT-29 (line)]] | alt | 8.88 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.1× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.0753× (z -14.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0494× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 6.58 | 3 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 3.73× (z +12.8) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 25.2× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.7× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -9.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 4.29 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0377× (z -9.3) |
| [[A549 (line)]] | wt | 4.89 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 29.3× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 3.22 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 39.5× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 3.68 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 40.2× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 46.4× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORL1]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RORC]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[MPP7]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[GYG2]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GALM]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[KCNK15-AS1]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ENPP5]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PBX1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.57 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[LINC00299]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf91]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[WNT9A]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TEP1]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[CSRNP2]] | -0.51 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[TRPC1]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SLC10A3]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TRIM65]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[STK10]] | -0.49 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[OSMR-DT]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[PLEKHN1]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[BCAR1]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORBS2]] | B | SORBS2 activity raises MAP2K6's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without SORBS2 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises MAP2K6's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without HNF1A-AS1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[LINC00992]] | B | LINC00992 activity raises MAP2K6's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 2.54× lower at baseline in the lines without LINC00992 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[CCR3]] | B | CCR3 activity raises MAP2K6's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without CCR3 | 0.057 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[VWA5A]] | B | VWA5A activity raises MAP2K6's level | lines that do not express VWA5A (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without VWA5A | 0.057 | ⚠ within organs, on part of the lines |
| [[SLC44A3]] | B | SLC44A3 activity raises MAP2K6's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without SLC44A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TNFRSF19]] | B | TNFRSF19 activity raises MAP2K6's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without TNFRSF19 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3 |
| [[ERBB3]] | B | ERBB3 activity raises MAP2K6's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without ERBB3 | 0.073 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[PROM1]] | B | PROM1 activity raises MAP2K6's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.63× lower at baseline in the lines without PROM1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[LINC01814]] | B | LINC01814 activity raises MAP2K6's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.39× lower at baseline in the lines without LINC01814 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[MTMR8]] | C | MTMR8 activity raises MAP2K6's level | lines that do not express MTMR8 (20) vs lines expressing it (30) | 2.82× lower at baseline in the lines without MTMR8 | 0.005 | ⚠ within organs, on part of the lines; also absent: MAP2K6, CXADR, BARX1; maybe low, not absent; co-absent with the target |
| [[CSRNP3]] | C | CSRNP3 activity raises MAP2K6's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 2.99× lower at baseline in the lines without CSRNP3 | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1A-AS1]] | B | MAP2K6 activity raises HNF1A-AS1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without MAP2K6 | 0.015 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[PKHD1]] | B | MAP2K6 activity raises PKHD1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without MAP2K6 | 0.015 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[PROM1]] | B | MAP2K6 activity raises PROM1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without MAP2K6 | 0.023 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[LINC01814]] | B | MAP2K6 activity raises LINC01814's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without MAP2K6 | 0.031 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[SEC16B]] | B | MAP2K6 activity raises SEC16B's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without MAP2K6 | 0.032 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[TNFRSF19]] | B | MAP2K6 activity raises TNFRSF19's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.43× lower at baseline in the lines without MAP2K6 | 0.033 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[LINC00299]] | B | MAP2K6 activity raises LINC00299's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without MAP2K6 | 0.033 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[PECR]] | B | MAP2K6 activity raises PECR's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.31× lower at baseline in the lines without MAP2K6 | 0.038 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[WDR72]] | B | MAP2K6 activity raises WDR72's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without MAP2K6 | 0.039 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[TMEM139]] | B | MAP2K6 activity raises TMEM139's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without MAP2K6 | 0.051 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[F5]] | B | MAP2K6 activity raises F5's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.23× lower at baseline in the lines without MAP2K6 | 0.056 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[FAAH2]] | B | MAP2K6 activity raises FAAH2's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.22× lower at baseline in the lines without MAP2K6 | 0.056 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 46.8); signed map (52.9, 3.7). **Vector** length 76.6, 18.2% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +17.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +12.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +11.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.8 | -4.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.4 | -5.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.3 — chr17:69,414,697-69,553,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEK6, MKK6, SAPKK3, MAPKK6, CRCMSL; previously PRKMK6 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 41 pathways, smallest: PI5P Regulates TP53 Acetylation; Uptake and function of anthrax toxins; Myogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P52564](https://www.uniprot.org/uniprotkb/P52564) (Dual specificity mitogen-activated protein kinase kinase 6):

> Dual specificity protein kinase which acts as an essential component of the MAP kinase signal transduction pathway. With MAP3K3/MKK3, catalyzes the concomitant phosphorylation of a threonine and a tyrosine residue in the MAP kinases p38 MAPK11, MAPK12, MAPK13 and MAPK14 and plays an important role in the regulation of cellular responses to cytokines and all kinds of stresses. Especially, MAP2K3/MKK3 and MAP2K6/MKK6 are both essential for the activation of MAPK11 and MAPK13 induced by …

**Summary**, from NCBI Gene [5608](https://www.ncbi.nlm.nih.gov/gene/5608):

> This gene encodes a member of the dual specificity protein kinase family, which functions as a mitogen-activated protein (MAP) kinase kinase. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals. This protein phosphorylates and activates p38 MAP kinase in response to inflammatory cytokines or environmental stress. As an essential component of p38 MAP kinase mediated signal transduction pathway, this gene is …

**Accessions** — [HGNC:6846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6846) · Entrez [5608](https://www.ncbi.nlm.nih.gov/gene/5608) · UniProt [P52564](https://www.uniprot.org/uniprotkb/P52564) · Ensembl [ENSG00000108984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108984)

## Data

Gene col 3016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3016); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3016]; `tensor/DDL_lfc|DDL_z.npy` [3016]; `embed/gene_vectors.npy` [3016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3016 or target_col == 3016). Every well: [[MAP2K6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
