---
symbol: "LPCAT3"
type: "gene"
col: 3263
ensembl_id: "ENSG00000111684"
name: "lysophosphatidylcholine acyltransferase 3"
location: "12p13.31"
module: 39
arm: "+"
pooled_cpm: 33.52
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 15
n_dd_up_clean: 27
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# LPCAT3

*lysophosphatidylcholine acyltransferase 3* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.86× (z +30.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.667× (z -7.7, q 8e-12, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42SE2]] (+0.59, fdr 1e-05), [[IFNGR1]] (+0.54, fdr 3e-05), [[ABHD12]] (+0.54, fdr 3e-05); moves opposite to [[LINC00486]] (-0.53, fdr 7e-05), [[ZNF23]] (-0.53, fdr 4e-05), [[SAMD4A]] (-0.52, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OXTR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.86×** | +30.0 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.24×** | +27.4 | 0e+00 | 47/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.24×** | +24.8 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +14.0 | 2e-42 | 38/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +13.6 | 3e-40 | 43/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **1.50×** | +10.9 | 2e-25 | 35/48 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.76×** | +10.3 | 5e-23 | 35/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.74×** | +9.5 | 2e-19 | 38/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.65×** | +9.4 | 2e-19 | 40/48 (SW480, KATO III, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +8.7 | 2e-16 | 33/47 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.60×** | +8.5 | 8e-16 | 28/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +8.5 | 9e-16 | 38/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.1 | 2e-14 | 34/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.48×** | +7.4 | 4e-12 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +7.3 | 8e-12 | 27/47 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.36×** | +5.8 | 2e-07 | 25/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.35×** | +5.7 | 3e-07 | 20/48 (SW480, SW1417, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -7.7 | 8e-12 | 24/47 (A-427, SHP-77, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.673×** | -7.2 | 1e-10 | 29/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.778×** | -6.8 | 3e-09 | 26/48 (HT-29, A-427, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.704×** | -6.7 | 4e-09 | 30/48 (HT-29, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.718×** | -6.3 | 3e-08 | 24/47 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.747×** | -5.5 | 3e-06 | 23/47 (HT-29, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -5.3 | 1e-05 | 23/47 (SW480, A-427, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.759×** | -5.2 | 1e-05 | 20/47 (HT-29, H4, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.832×** | -4.9 | 5e-05 | 20/48 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.772×** | -4.7 | 1e-04 | 20/48 (CFPAC-1, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.793×** | -4.4 | 5e-04 | 20/47 (SNU-1, NCI-H1792, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.643×** | -4.4 | 6e-04 | 18/44 (SNU-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Naproxen (drug)]] 5 µM |  | **0.803×** | -4.0 | 0.003 | 22/47 (RPMI-7951, C-33 A, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.756×** | -3.8 | 0.006 | 15/48 (SNU-1, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -3.4 | 0.023 | 15/48 (AN3 CA, C32, …) | all doses, flat |  |
| [[Naproxen (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.044 | 4/48 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.725×** | -3.2 | 0.048 | 8/47 (Hs 766T, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.848× | -3.0 | 0.077 | 12/47 (A-427, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 75.6 | 8 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.53× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[NCI-H460 (line)]] | wt | 16.6 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.27× (z +17.7) | — |
| [[A-427 (line)]] | wt | 106 | 3 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.60× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -10.5) |
| [[SW1417 (line)]] | alt | 63.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.17× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[AsPC-1 (line)]] | alt | 26.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.13× (z +13.7) | — |
| [[HT-29 (line)]] | alt | 39.2 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 5.76× (z +14.5) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.354× (z -8.7) |
| [[LoVo (line)]] | wt | 31.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 8.04× (z +18.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.84× (z +16.1) | — |
| [[A549 (line)]] | wt | 28.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.06× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.40× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 36.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 34.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.69× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 19.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.22× (z +15.9) | — |
| [[Panc 03.27 (line)]] | alt | 56.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +16.4) | — |
| [[A-172 (line)]] | wt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.49× (z +10.8) | — |
| [[A498 (line)]] | wt | 33.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 41.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 18.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.65× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 33.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.77× (z +11.1) | — |
| [[J82 (line)]] | alt | 29.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.08× (z +13.8) | — |
| [[KATO III (line)]] | alt | 59.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 27.3 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.57× (z +12.6) | — |
| [[RKO (line)]] | wt | 38.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 44.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.93× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 34.0 | 2 | 0 | [[Retinoic acid (drug)]] 5 µM 3.81× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 46.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.13× (z +9.9) | — |
| [[H4 (line)]] | wt | 31.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.12× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 44.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.2) | — |
| [[SW48 (line)]] | wt | 21.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.34× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.108× (z -10.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42SE2]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[IFNGR1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[ABHD12]] | +0.54 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ERG28]] | +0.54 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[LY6E]] | +0.53 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[ZNRF2]] | +0.53 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ADAM15]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[STAT3]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CD46]] | +0.53 | +0.46 / +0.37 | both halves | 7e-05 |  |
| [[SUMF2]] | +0.52 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[GINM1]] | +0.51 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[ACO1]] | +0.50 | +0.44 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00486]] | -0.53 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[ZNF23]] | -0.53 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SAMD4A]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[C3orf20]] | -0.52 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[PLAC8L1]] | -0.51 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[LY6K]] | -0.50 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MPP4]] | -0.50 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[MSANTD3-TMEFF1]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TAS2R4]] | -0.49 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[NEPRO-AS1]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TIAM2]] | -0.49 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[DUS4L]] | -0.48 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OXTR]] | B | OXTR activity lowers LPCAT3's level | lines that do not express OXTR (5) vs lines expressing it (45) | 1.81× higher at baseline in the lines without OXTR | 0.084 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[IMPA2]] | C | IMPA2 activity raises LPCAT3's level | lines that do not express IMPA2 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without IMPA2 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ATP11A, PLEKHG3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction -0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, -45.7); signed map (-54.1, 29.2). **Vector** length 92.0, 21.9% of its response variance represented; |z| ≥ 3 in 1,303 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | +3.2 | +3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +7.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -7.2 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.8 | -7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.6 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -6.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.0 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidylcholine acyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,976,185-7,018,477 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C3F, nessy, LPLAT12; previously OACT5, MBOAT5 |
| Gene groups (HGNC) | Membrane bound O-acyltransferase family; Lysophospholipid acyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Acyl chain remodelling of PS; Acyl chain remodelling of PC; Acyl chain remodelling of PE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1A2](https://www.uniprot.org/uniprotkb/Q6P1A2) (Lysophospholipid acyltransferase 5):

> Lysophospholipid O-acyltransferase (LPLAT) that catalyzes the reacylation step of the phospholipid remodeling process also known as the Lands cycle. Catalyzes transfer of the fatty acyl chain from fatty acyl-CoA to 1-acyl lysophospholipid to form various classes of phospholipids. Converts 1-acyl lysophosphatidylcholine (LPC) into phosphatidylcholine (PC) (LPCAT activity), 1-acyl lysophosphatidylserine (LPS) into phosphatidylserine (PS) (LPSAT activity) and 1-acyl lysophosphatidylethanolamine …

**Summary**, from NCBI Gene [10162](https://www.ncbi.nlm.nih.gov/gene/10162):

> Enables 1-acylglycerophosphocholine O-acyltransferase activity; 1-acylglycerophosphoethanolamine O-acyltransferase activity; and 1-acylglycerophosphoserine O-acyltransferase activity. Involved in phosphatidylcholine acyl-chain remodeling; phosphatidylethanolamine acyl-chain remodeling; and phosphatidylserine acyl-chain remodeling. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30244) · Entrez [10162](https://www.ncbi.nlm.nih.gov/gene/10162) · UniProt [Q6P1A2](https://www.uniprot.org/uniprotkb/Q6P1A2) · Ensembl [ENSG00000111684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111684)

## Data

Gene col 3263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3263); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3263]; `tensor/DDL_lfc|DDL_z.npy` [3263]; `embed/gene_vectors.npy` [3263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3263 or target_col == 3263). Every well: [[LPCAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPCAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
