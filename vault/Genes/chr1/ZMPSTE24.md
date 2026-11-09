---
symbol: "ZMPSTE24"
type: "gene"
col: 1391
ensembl_id: "ENSG00000084073"
name: "zinc metallopeptidase STE24"
location: "1p34.2"
module: 25
arm: "+"
pooled_cpm: 38.56
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ZMPSTE24

*zinc metallopeptidase STE24* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.19× (z +23.6, q 0e+00, up in 38 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +19.4, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Thymol (drug)]] 0.5 µM: 0.793× (z -4.9, q 5e-04, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSME3IP1]] (+0.77, fdr 7e-06), [[ZMYND11]] (+0.75, fdr 7e-06), [[ANKRD40]] (+0.71, fdr 7e-06); moves opposite to [[RPL18]] (-0.70, fdr 2e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[C19orf81]] (-0.69, fdr 3e-05), [[RNF114]] (-0.69, fdr 3e-05), [[LAMTOR5]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 21 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +23.6 | 0e+00 | 38/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +22.9 | 0e+00 | 44/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +19.4 | 0e+00 | 43/47 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +17.1 | 0e+00 | 40/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +16.5 | 0e+00 | 37/41 (A549, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +14.4 | 3e-45 | 41/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.52×** | +13.9 | 4e-42 | 43/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +12.9 | 2e-36 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +12.4 | 2e-33 | 40/48 (SW480, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.1 | 5e-22 | 33/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.0 | 5e-22 | 36/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +10.0 | 8e-22 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +9.7 | 9e-21 | 38/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +8.9 | 2e-17 | 38/45 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.7 | 2e-16 | 35/48 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +7.9 | 1e-13 | 34/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +6.5 | 3e-09 | 25/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.7 | 3e-07 | 22/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +5.1 | 7e-06 | 19/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 0.5 µM |  | **0.793×** | -4.9 | 5e-04 | 24/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.754×** | -4.3 | 0.004 | 19/46 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.812×** | -4.2 | 0.004 | 18/48 (HepG2/C3A, SW 1088, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.849× | -3.5 | 0.072 | 12/48 (CHP-212, RPMI-7951, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.851× | -3.3 | 0.11 | 11/48 (CHP-212, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.854× | -3.2 | 0.14 | 10/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.863× | -3.1 | 0.14 | 16/47 (A549, LoVo, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.862× | -3.0 | 0.16 | 11/48 (H4, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 31.4 | 11 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.1) | — |
| [[LoVo (line)]] | wt | 23.3 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 33.9 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 26.3 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.3 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 54.8 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.7) | — |
| [[A549 (line)]] | wt | 24.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.98× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 45.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 65.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 26.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[H4 (line)]] | wt | 39.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 32.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.90× (z +10.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 40.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +11.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 29.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.90× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 34.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 52.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 23.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.1) | — |
| [[A498 (line)]] | wt | 72.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +11.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 29.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.6× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 32.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 45.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 36.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 41.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +17.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 35.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.08× (z +8.5) ⚠ toxic | [[Digitoxin (drug)]] 5 µM 0.313× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 42.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.455× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 35.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | +0.77 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ZMYND11]] | +0.75 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ANKRD40]] | +0.71 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[VPS52]] | +0.70 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | +0.69 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.69 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.68 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[RCN1]] | +0.68 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[NRAS]] | +0.68 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[ABCF2]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[TWF1]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[DR1]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18]] ⚠ | -0.70 | -0.47 / -0.74 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C19orf81]] | -0.69 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[RNF114]] | -0.69 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[LAMTOR5]] | -0.67 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.65 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[RPL36]] | -0.64 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[AFMID]] | -0.64 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[RASSF7]] | -0.64 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[RPL36AL]] ⚠ | -0.64 | -0.42 / -0.71 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIEN1]] | -0.64 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[PIM2]] | -0.63 | -0.25 / -0.74 | both halves | 4e-04 |  |
| [[ENO2]] | -0.63 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RPS10]] | -0.62 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.62 | -0.41 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZMPSTE24's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF532]] | B | ZNF532 activity lowers ZMPSTE24's level | lines that do not express ZNF532 (6) vs lines expressing it (44) | 1.03× higher at baseline in the lines without ZNF532 | 0.077 | ⚠ within organs, on part of the lines; also absent: PXMP4, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.7, 3.6); signed map (-13.4, -37.8). **Vector** length 94.9, 24.5% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +23.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +22.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +16.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +19.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +4.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.1 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.8 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.7 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -4.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc metallopeptidase STE24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,258,041-40,294,180 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FACE-1, Ste24p, STE24, HGPS, PRO1 |
| Gene groups (HGNC) | M48 metallopeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75844](https://www.uniprot.org/uniprotkb/O75844) (CAAX prenyl protease 1 homolog):

> Transmembrane metalloprotease whose catalytic activity is critical for processing lamin A/LMNA on the inner nuclear membrane and clearing clogged translocons on the endoplasmic reticulum. Proteolytically removes the C-terminal three residues of farnesylated proteins. Also plays an antiviral role independently of its protease activity by restricting enveloped RNA and DNA viruses, including influenza A, Zika, Ebola, Sindbis, vesicular stomatitis, cowpox, and vaccinia. Mechanistically, controls …

**Summary**, from NCBI Gene [10269](https://www.ncbi.nlm.nih.gov/gene/10269):

> This gene encodes a member of the peptidase M48A family. The encoded protein is a zinc metalloproteinase involved in the two step post-translational proteolytic cleavage of carboxy terminal residues of farnesylated prelamin A to form mature lamin A. Mutations in this gene have been associated with mandibuloacral dysplasia and restrictive dermopathy. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12877) · Entrez [10269](https://www.ncbi.nlm.nih.gov/gene/10269) · UniProt [O75844](https://www.uniprot.org/uniprotkb/O75844) · Ensembl [ENSG00000084073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084073)

## Data

Gene col 1391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1391); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1391]; `tensor/DDL_lfc|DDL_z.npy` [1391]; `embed/gene_vectors.npy` [1391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1391 or target_col == 1391). Every well: [[ZMPSTE24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMPSTE24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
