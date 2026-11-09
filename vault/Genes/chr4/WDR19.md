---
symbol: "WDR19"
type: "gene"
col: 8101
ensembl_id: "ENSG00000157796"
name: "WD repeat domain 19"
location: "4p14"
module: 74
arm: "+"
pooled_cpm: 34.29
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 15
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# WDR19

*WD repeat domain 19* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.95× (z +22.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.557× (z -9.8, q 5e-20, down in 28 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.639× (z -7.5, q 2e-11, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABARAP]] (+0.58, fdr 2e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[MICU1]] (+0.58, fdr 1e-05), [[UMAD1]] (+0.57, fdr 2e-05), [[CFAP69]] (+0.57, fdr 1e-05); moves opposite to [[EXO5]] (-0.49, fdr 2e-04), [[UBE2N]] (-0.49, fdr 2e-05), [[NUDT15]] (-0.47, fdr 4e-04).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.95×** | +22.9 | 0e+00 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +20.5 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.10×** | +18.9 | 0e+00 | 47/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +18.7 | 0e+00 | 46/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +10.7 | 8e-25 | 40/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +9.6 | 1e-19 | 42/47 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.53×** | +7.0 | 2e-10 | 39/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.6 | 3e-09 | 25/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +5.8 | 4e-07 | 29/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.0 | 3e-05 | 23/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.31×** | +4.5 | 3e-04 | 22/48 (Hs 766T, A-172, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +4.3 | 1e-03 | 18/48 (A-172, A498, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 16/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.27×** | +4.0 | 0.002 | 17/48 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.002 | 15/47 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.002 | 20/48 (HOP62, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.68×** | +3.9 | 0.003 | 19/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.557×** | -9.8 | 5e-20 | 28/45 (SNU-423, SW480, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.639×** | -7.5 | 2e-11 | 32/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.649×** | -6.7 | 4e-09 | 29/44 (SK-MEL-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.693×** | -6.2 | 1e-07 | 29/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.705×** | -5.9 | 5e-07 | 25/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.711×** | -5.5 | 3e-06 | 19/38 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.707×** | -5.4 | 6e-06 | 25/47 (SW48, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -5.0 | 5e-05 | 19/48 (HOP62, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.763×** | -4.6 | 3e-04 | 24/48 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **0.794×** | -3.9 | 0.006 | 21/46 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.615×** | -3.7 | 0.012 | 17/47 (CFPAC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.6 | 0.014 | 2/48 (BT-474, SW 1271) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.033 | 8/48 (A498, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.768×** | -3.2 | 0.063 | 12/48 (SW 1271, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.1 | 0.083 | 18/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.776×** | -3.0 | 0.083 | 8/48 (MIA PaCa-2, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.676×** | -3.0 | 0.098 | 13/47 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.4 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.370× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 28.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 30.3 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 45.3 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.507× (z -8.8) |
| [[A-172 (line)]] | wt | 34.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.99× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 41.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.0) | — |
| [[LoVo (line)]] | wt | 23.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.08× (z +14.2) | — |
| [[RKO (line)]] | wt | 43.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -16.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 20.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.80× (z +14.5) | — |
| [[C-33 A (line)]] | alt | 56.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 24.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.42× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 35.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -12.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.53× (z +12.9) | — |
| [[J82 (line)]] | alt | 24.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 21.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 14.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.42× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.50× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 46.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 25.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.6) | — |
| [[A549 (line)]] | wt | 25.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.57× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 37.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 66.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.45× (z +9.7) | — |
| [[C32 (line)]] | wt | 20.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.87× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 36.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.31× (z +9.5) | [[Bortezomib (drug)]] 5 µM 0.0727× (z -9.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 34.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 42.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 26.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.50× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 11.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.16× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0859× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 64.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.357× (z -9.7) |
| [[SW 900 (line)]] | alt | 71.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | +0.58 | +0.58 / +0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MICU1]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[UMAD1]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CFAP69]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[WBP2]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[WDR48]] | +0.51 | +0.45 / +0.43 | both halves | 3e-05 | same gene group |
| [[ZFYVE1]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[NPC2]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[CSPP1]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D17]] | +0.51 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[TMEM120A]] | +0.50 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[UBXN1]] | +0.50 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[IFT88]] | +0.50 | +0.49 / +0.42 | both halves | 4e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 910 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO5]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[UBE2N]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NUDT15]] | -0.47 | -0.60 / -0.26 | both halves | 4e-04 |  |
| [[MACROH2A1]] | -0.44 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[CYCS]] | -0.43 | -0.28 / -0.37 | both halves | 3e-04 | pathway: Organelle biogenesis and maintenance |
| [[MFAP3]] | -0.43 | -0.22 / -0.38 | both halves | 6e-04 |  |
| [[COX10-DT]] | -0.42 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[SLC47A1]] | -0.42 | -0.24 / -0.37 | both halves | 5e-04 |  |
| [[ASAH2B]] | -0.42 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[RAN]] | -0.42 | -0.40 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.3, -47.3); signed map (-18.5, 4.4). **Vector** length 89.8, 23.3% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +18.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.7 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -5.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,182,504-39,285,810 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Pwdmp, KIAA1638, FLJ23127, ORF26, DYF-2, Oseg6, IFT144, NPHP13 |
| Gene groups (HGNC) | WD repeat domain containing; IFT-A complex |
| Reactome | 6 pathways, smallest: Intraflagellar transport; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEZ3](https://www.uniprot.org/uniprotkb/Q8NEZ3) (WD repeat-containing protein 19):

> As component of the IFT complex A (IFT-A), a complex required for retrograde ciliary transport and entry into cilia of G protein-coupled receptors (GPCRs), it is involved in cilia function and/or assembly. Essential for functional IFT-A assembly and ciliary entry of GPCRs. Associates with the BBSome complex to mediate ciliary transport (By similarity).

**Summary**, from NCBI Gene [57728](https://www.ncbi.nlm.nih.gov/gene/57728):

> The protein encoded by this gene is a member of the WD (tryptophan-aspartic acid) repeat family, which is a large family of structurally-related proteins known to participate in a wide range of cellular processes. Each WD repeat typically contains about 40 amino acids that are usually bracketed by glycine-histidine and tryptophan-aspartic acid (WD) dipeptides. This protein contains six WD repeats, three transmembrane domains, and a clathrin heavy-chain repeat. Mutations in this gene have been …

**Accessions** — [HGNC:18340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18340) · Entrez [57728](https://www.ncbi.nlm.nih.gov/gene/57728) · UniProt [Q8NEZ3](https://www.uniprot.org/uniprotkb/Q8NEZ3) · Ensembl [ENSG00000157796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157796)

## Data

Gene col 8101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8101); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8101]; `tensor/DDL_lfc|DDL_z.npy` [8101]; `embed/gene_vectors.npy` [8101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8101 or target_col == 8101). Every well: [[WDR19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
