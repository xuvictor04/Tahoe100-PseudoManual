---
symbol: "CCNYL1"
type: "gene"
col: 8658
ensembl_id: "ENSG00000163249"
name: "cyclin Y like 1"
location: "2q33.3"
module: 81
arm: "+"
pooled_cpm: 83.76
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# CCNYL1

*cyclin Y like 1* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +25.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.681× (z -6.5, q 5e-08, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.570× (z -5.3, q 1e-05, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAP1]] (+0.63, fdr 1e-05), [[FAM107B]] (+0.63, fdr 1e-05), [[WNT9A]] (+0.62, fdr 1e-05); moves opposite to [[VPS50]] (-0.64, fdr 7e-06), [[NDUFAF5]] (-0.61, fdr 1e-05), [[MRRF]] (-0.61, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +25.5 | 0e+00 | 44/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.29×** | +21.5 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.94×** | +19.5 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +16.5 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +14.8 | 0e+00 | 41/49 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +13.2 | 5e-38 | 46/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +10.9 | 9e-26 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +9.9 | 4e-21 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +9.4 | 4e-19 | 36/50 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +9.3 | 8e-19 | 35/48 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +9.3 | 9e-19 | 42/48 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +9.1 | 6e-18 | 40/49 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +7.7 | 8e-13 | 31/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 7e-10 | 31/48 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.33×** | +5.1 | 1e-05 | 28/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 24/48 (PANC-1, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.681×** | -6.5 | 5e-08 | 30/44 (A-172, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.9 | 8e-07 | 27/41 (NCI-H23, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.727×** | -5.8 | 1e-06 | 26/49 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.570×** | -5.3 | 1e-05 | 28/47 (RPMI-7951, RKO, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.780×** | -4.5 | 6e-04 | 24/48 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.786×** | -4.4 | 0.001 | 26/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.006 | 20/48 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.043 | 17/48 (BT-474, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.4 | 0.047 | 7/48 (Hs 766T, SNU-1, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.834× | -3.3 | 0.047 | 19/48 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.047 | 21/48 (RKO, SW480, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.840× | -3.2 | 0.065 | 15/48 (AN3 CA, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.885× | -3.1 | 0.068 | 13/48 (BT-474, RKO, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.068 | 19/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.844× | -3.1 | 0.070 | 21/49 (BT-474, NCI-H23, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.847× | -3.0 | 0.073 | 15/49 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.890× | -3.0 | 0.073 | 8/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.073 | 18/48 (SW 900, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +23.9) | — |
| [[SW480 (line)]] | alt | 54.4 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +26.4) | — |
| [[C32 (line)]] | wt | 43.1 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +18.7) | — |
| [[AsPC-1 (line)]] | alt | 81.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +23.2) | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.9) | — |
| [[HOP62 (line)]] | alt | 60.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +21.9) | — |
| [[J82 (line)]] | alt | 141 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +18.6) | — |
| [[Panc 03.27 (line)]] | alt | 94.8 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +22.3) | [[Lonafarnib (drug)]] 5 µM 0.164× (z -9.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 82.9 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.41× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -12.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 75.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 92.7 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +13.6) | — |
| [[SW1417 (line)]] | alt | 71.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.4) | — |
| [[A498 (line)]] | wt | 122 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 52.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +16.7) | — |
| [[KATO III (line)]] | alt | 33.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.1) | — |
| [[LoVo (line)]] | wt | 176 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.3) | — |
| [[NCI-H23 (line)]] | alt | 85.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -18.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 59.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 66.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.44× (z +13.6) | — |
| [[SW48 (line)]] | wt | 43.3 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.1) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.237× (z -8.8) |
| [[A-427 (line)]] | wt | 52.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +11.1) | — |
| [[A549 (line)]] | wt | 94.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 44.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 31.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +17.4) | [[Thymol (drug)]] 0.5 µM 0.181× (z -9.9) |
| [[LS 180 (line)]] | wt | 48.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 76.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 64.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -14.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 94.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 60.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 78.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 73.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.0) | — |
| [[RKO (line)]] | wt | 67.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 55.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.5) | [[Ponatinib (drug)]] 0.5 µM 0.195× (z -8.8) |
| [[BT-474 (line)]] | alt | 68.2 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.181× (z -11.3) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.282× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 146 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 126 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 72.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 93.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +16.5) | — |
| [[H4 (line)]] | wt | 74.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 41.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +12.3) | — |
| [[SW 1088 (line)]] | alt | 72.8 | 0 | 1 | — | [[Ligustrazine (drug)]] 0.5 µM 0.0657× (z -9.4) |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAP1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 | same gene group |
| [[DPF3]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[LUCAT1]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[DLGAP4]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[EHD1]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[TRIOBP]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[HBEGF]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CIB1]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[PTPRH]] | +0.58 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PHLDA2]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS50]] | -0.64 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[NDUFAF5]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MRRF]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[CDKAL1]] | -0.60 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[CUEDC2]] | -0.60 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[NAGPA]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TRMT61B]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[TMLHE]] | -0.59 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[MRPS35]] | -0.59 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[ACBD6]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 | same gene group |
| [[KAT7]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[ZZZ3]] | -0.58 | -0.50 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCNYL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, -5.7); signed map (-1.0, 30.4). **Vector** length 112, 35.8% of its response variance represented; |z| ≥ 3 in 1,484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +9.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +9.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.5 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.3 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.0 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | cyclin Y like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:207,711,540-207,761,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40432 |
| Gene groups (HGNC) | Cyclins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N7R7](https://www.uniprot.org/uniprotkb/Q8N7R7) (Cyclin-Y-like protein 1):

> Key regulator of Wnt signaling implicated in various biological processes including male fertility, embryonic neurogenesis and cortex development. Activates the cyclin-dependent kinase CDK16, and promotes sperm maturation.

**Summary**, from NCBI Gene [151195](https://www.ncbi.nlm.nih.gov/gene/151195):

> Predicted to enable cyclin-dependent protein serine/threonine kinase activator activity. Predicted to be involved in neurogenesis and regulation of canonical Wnt signaling pathway. Predicted to act upstream of or within flagellated sperm motility; regulation of protein kinase activity; and spermatogenesis. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26868) · Entrez [151195](https://www.ncbi.nlm.nih.gov/gene/151195) · UniProt [Q8N7R7](https://www.uniprot.org/uniprotkb/Q8N7R7) · Ensembl [ENSG00000163249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163249)

## Data

Gene col 8658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8658); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8658]; `tensor/DDL_lfc|DDL_z.npy` [8658]; `embed/gene_vectors.npy` [8658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8658 or target_col == 8658). Every well: [[CCNYL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNYL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
