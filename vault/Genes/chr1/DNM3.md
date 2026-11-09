---
symbol: "DNM3"
type: "gene"
col: 12498
ensembl_id: "ENSG00000197959"
name: "dynamin 3"
location: "1q24.3"
module: 8
arm: "+"
pooled_cpm: 43.04
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 15
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 12
direction_downstream: 6
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DNM3

*dynamin 3* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.08× (z +32.1, q 0e+00, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.596× (z -8.5, q 1e-14, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN22]] (+0.55, fdr 1e-05), [[LINC02331]] (+0.55, fdr 1e-05), [[TRIM2]] (+0.54, fdr 5e-05); moves opposite to [[ENTPD5]] (-0.52, fdr 7e-05), [[ABCC10]] (-0.49, fdr 0.002, ⚠ one half only (not replicated)), [[AP4E1]] (-0.47, fdr 0.003, ⚠ not reproduced), [[ZNF696]] (-0.46, fdr 4e-04), [[SIRT3]] (-0.45, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[LYPD1]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZNF623]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.08×** | +32.1 | 0e+00 | 36/41 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.55×** | +28.2 | 0e+00 | 38/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.98×** | +26.4 | 0e+00 | 36/41 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +23.1 | 0e+00 | 35/41 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.44×** | +17.5 | 0e+00 | 34/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +15.8 | 0e+00 | 35/41 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +13.7 | 8e-41 | 33/41 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +12.4 | 2e-33 | 32/43 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +11.5 | 1e-28 | 28/40 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.66×** | +11.1 | 4e-27 | 30/42 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +10.8 | 1e-25 | 31/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +10.3 | 4e-23 | 31/41 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.9 | 2e-21 | 30/41 (A-172, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +9.1 | 4e-18 | 24/41 (HOP62, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +5.2 | 9e-06 | 20/41 (A549, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -8.5 | 1e-14 | 31/41 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -8.2 | 5e-14 | 23/41 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.661×** | -6.8 | 2e-09 | 29/41 (NCI-H1792, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -6.6 | 5e-09 | 25/40 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.677×** | -6.4 | 2e-08 | 27/41 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.695×** | -6.0 | 2e-07 | 24/41 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -4.9 | 9e-05 | 23/42 (LS 180, CHP-212, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.775×** | -4.2 | 0.002 | 17/41 (SW480, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.772×** | -4.1 | 0.003 | 18/40 (LS 180, SNU-423, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.003 | 16/40 (LS 180, hTERT-HPNE, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.815×** | -3.3 | 0.043 | 14/41 (LS 180, CHP-212, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.818×** | -3.3 | 0.047 | 13/40 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.049 | 14/41 (LS 180, CHP-212, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.1 | 0.086 | 11/40 (COLO 205, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.825×** | -3.0 | 0.094 | 4/41 (HT-29, SW 1271, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 112 | 6 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.85× (z +14.8) | [[Ixazomib citrate (drug)]] 5 µM 0.283× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.469× (z -9.0) |
| [[HOP62 (line)]] | alt | 17.0 | 10 | 0 | [[Panobinostat (drug)]] 5 µM 21.3× (z +19.3) | — |
| [[NCI-H460 (line)]] | wt | 38.8 | 10 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 17.8× (z +22.5) | — |
| [[SW480 (line)]] | alt | 183 | 7 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.92× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[LoVo (line)]] | wt | 79.6 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 8.09× (z +22.0) | [[Digitoxin (drug)]] 5 µM 0.324× (z -11.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.2 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +17.0) | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 17.5× (z +19.7) | — |
| [[A498 (line)]] | wt | 45.9 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +24.0) | — |
| [[HS-578T (line)]] | alt | 23.8 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +17.0) | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 17.7× (z +19.3) | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +19.1) | — |
| [[SW 900 (line)]] | alt | 67.4 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +19.4) | — |
| [[A549 (line)]] | wt | 15.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 22.7× (z +16.2) | — |
| [[NCI-H1792 (line)]] | alt | 49.8 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 8.31× (z +18.8) | [[Harringtonine (drug)]] 0.5 µM 0.381× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 36.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.89× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 35.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.38× (z +14.5) | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.75× (z +13.6) | — |
| [[J82 (line)]] | alt | 11.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 23.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.89× (z +15.0) | — |
| [[PANC-1 (line)]] | alt | 11.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 19.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.2× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 108 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 47.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.42× (z +11.0) | — |
| [[H4 (line)]] | wt | 34.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 44.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 126 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 50.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.11× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 47.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.90× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 49.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 57.8 | 1 | 0 | [[Bimiralisib (drug)]] 5 µM 8.75× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.3) | — |
| [[NCI-H596 (line)]] | alt | 60.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.135× (z -8.5) |
| [[A-427 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 263 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN22]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[LINC02331]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TRIM2]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CHN2]] | +0.53 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[CCSER1]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RAMP1]] | +0.52 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[PLCH1]] | +0.52 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[DLEU1]] | +0.52 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[LINC02580]] | +0.49 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[NPSR1-AS1]] | +0.49 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[LINC02147]] | +0.49 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[AOAH]] | +0.49 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD5]] | -0.52 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[ABCC10]] | -0.49 | -0.59 / -0.13 | ⚠ one half (not replicated) | 0.002 | same gene group |
| [[AP4E1]] | -0.47 | -0.09 / -0.44 | ⚠ not reproduced | 0.003 |  |
| [[ACAD8]] | -0.46 | -0.19 / -0.21 | ⚠ not reproduced | 9e-04 |  |
| [[ZNF623]] | -0.46 | -0.15 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF696]] | -0.46 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[SIRT3]] | -0.45 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[STIMATE]] | -0.45 | -0.50 / -0.20 | ⚠ one half (not replicated) | 7e-04 | same gene group |
| [[LYSMD4]] | -0.44 | -0.39 / -0.21 | both halves | 6e-04 |  |
| [[KIFBP]] | -0.43 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[NEK4]] | -0.43 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[LOXL1-AS1]] | -0.43 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DMTF1]] | -0.41 | -0.29 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD1]] | B | LYPD1 activity raises DNM3's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 1.93× lower at baseline in the lines without LYPD1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[TRIM2]] | B | TRIM2 activity raises DNM3's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without TRIM2 | 0.025 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises DNM3's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 1.85× lower at baseline in the lines without ARHGEF38 | 0.027 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[TOP2A]] | B | TOP2A activity lowers DNM3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02147]] | B | LINC02147 activity raises DNM3's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without LINC02147 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |
| [[ATP1B1]] | B | ATP1B1 activity raises DNM3's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.35× lower at baseline in the lines without ATP1B1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[TOX3]] | B | TOX3 activity raises DNM3's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without TOX3 | 0.056 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[LINC01091]] | B | LINC01091 activity raises DNM3's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without LINC01091 | 0.062 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[CA8]] | B | CA8 activity raises DNM3's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without CA8 | 0.075 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[LINC01622]] | B | LINC01622 activity raises DNM3's level | lines that do not express LINC01622 (27) vs lines expressing it (23) | 1.38× lower at baseline in the lines without LINC01622 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GJB1, LINC02008, PROX1-AS1; maybe low, not absent |
| [[IL20RA]] | B | IL20RA activity raises DNM3's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 1.41× lower at baseline in the lines without IL20RA | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[IGFL2-AS1]] | B | IGFL2-AS1 activity raises DNM3's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 1.84× lower at baseline in the lines without IGFL2-AS1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF623]] | B | DNM3 activity lowers ZNF623's level | lines that do not express DNM3 (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without DNM3 | 0.019 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | B | DNM3 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.42× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| [[ZNF696]] | B | DNM3 activity lowers ZNF696's level | lines that do not express DNM3 (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without DNM3 | 0.079 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.05 µM | B | DNM3 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.38× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | B | DNM3 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.52× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 0.5 µM | B | DNM3 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.476). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 50.2); signed map (62.2, 2.9). **Vector** length 69.2, 14.0% of its response variance represented; |z| ≥ 3 in 1,285 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +12.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | dynamin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:171,817,887-172,418,466 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0820 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; MicroRNA protein coding host genes; Dynamins |
| Reactome | 16 pathways, smallest: Retrograde neurotrophin signalling; Recycling pathway of L1; L1CAM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ16](https://www.uniprot.org/uniprotkb/Q9UQ16) (Dynamin-3):

> Microtubule-associated force-producing protein involved in producing microtubule bundles and able to bind and hydrolyze GTP (By similarity). Most probably involved in vesicular trafficking processes, in particular endocytosis (By similarity).

**Summary**, from NCBI Gene [26052](https://www.ncbi.nlm.nih.gov/gene/26052):

> This gene encodes a member of a family of guanosine triphosphate (GTP)-binding proteins that associate with microtubules and are involved in vesicular transport. The encoded protein functions in the development of megakaryocytes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:29125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29125) · Entrez [26052](https://www.ncbi.nlm.nih.gov/gene/26052) · UniProt [Q9UQ16](https://www.uniprot.org/uniprotkb/Q9UQ16) · Ensembl [ENSG00000197959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197959)

## Data

Gene col 12498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12498); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12498]; `tensor/DDL_lfc|DDL_z.npy` [12498]; `embed/gene_vectors.npy` [12498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12498 or target_col == 12498). Every well: [[DNM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
