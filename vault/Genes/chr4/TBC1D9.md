---
symbol: "TBC1D9"
type: "gene"
col: 3049
ensembl_id: "ENSG00000109436"
name: "TBC1 domain family member 9"
location: "4q31.21"
module: 14
arm: "+"
pooled_cpm: 36.56
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TBC1D9

*TBC1 domain family member 9* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.51× (z +20.9, q 0e+00, up in 34 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.600× (z -8.0, q 1e-12, down in 22 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.528× (z -5.4, q 1e-05, down in 29 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.0903×, LoVo 0.116×, Panc 03.27 0.241×, BT-474 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (BT-474 0.195×, SNU-423 0.308×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.252×, BT-474 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (BT-474 0.267×, SK-MEL-2 0.321×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (BT-474 0.316×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.473×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX11]] (+0.61, fdr 1e-05), [[CCDC85A]] (+0.56, fdr 1e-05), [[ZBTB10]] (+0.55, fdr 4e-05); moves opposite to [[PDCD6]] (-0.45, fdr 4e-05), [[TUBGCP2]] (-0.45, fdr 6e-05), [[NUP214]] (-0.45, fdr 7e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RPS6KA6]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Erlotinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.51×** | +20.9 | 0e+00 | 34/42 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +11.8 | 8e-30 | 29/42 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.1 | 7e-22 | 34/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +8.3 | 2e-14 | 31/42 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.66×** | +8.1 | 5e-14 | 29/42 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +7.8 | 5e-13 | 31/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.51×** | +6.6 | 3e-09 | 28/41 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.49×** | +6.1 | 6e-08 | 26/41 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 7e-07 | 26/41 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +5.6 | 1e-06 | 21/42 (J82, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +5.4 | 3e-06 | 25/42 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +5.2 | 8e-06 | 22/42 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 21/41 (BT-474, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 3e-04 | 21/41 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +4.3 | 6e-04 | 20/42 (NCI-H1573, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.001 | 15/41 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 14/41 (NCI-H460, HOP62, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.005 | 15/42 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3049.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.0903×, LoVo 0.116×, Panc 03.27 0.241×, BT-474 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (BT-474 0.195×, SNU-423 0.308×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.252×, BT-474 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (BT-474 0.267×, SK-MEL-2 0.321×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (BT-474 0.316×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.473×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.600×** | -8.0 | 1e-12 | 22/36 (BT-474, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.670×** | -6.5 | 3e-08 | 24/38 (SNU-423, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.705×** | -5.7 | 3e-06 | 24/42 (BT-474, SNU-423, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.528×** | -5.4 | 1e-05 | 29/41 (Hs 766T, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -4.9 | 9e-05 | 24/42 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.752×** | -4.3 | 0.002 | 21/37 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.616×** | -4.1 | 0.004 | 17/40 (HEC-1-A, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.820×** | -3.2 | 0.089 | 16/42 (BT-474, HS-578T, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | 0.695× | -3.1 | 0.13 | 15/40 (HEC-1-A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.829× | -3.0 | 0.13 | 12/42 (BT-474, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 188 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -13.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.267× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 14.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +21.3) | — |
| [[LoVo (line)]] | wt | 16.4 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.17× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 34.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +18.9) | — |
| [[J82 (line)]] | alt | 63.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +23.7) | — |
| [[NCI-H1573 (line)]] | alt | 30.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 50.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0903× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.321× (z -9.2) |
| [[SNU-423 (line)]] | alt | 73.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 99.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +22.6) | — |
| [[A-427 (line)]] | wt | 45.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +17.4) | — |
| [[A498 (line)]] | wt | 53.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.5) | — |
| [[HS-578T (line)]] | alt | 47.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.370× (z -8.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H2347 (line)]] | alt | 64.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 41.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[PANC-1 (line)]] | alt | 22.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.90× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +12.7) | — |
| [[H4 (line)]] | wt | 59.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 61.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.88× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +23.2) | — |
| [[HT-29 (line)]] | alt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 38.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +14.1) | — |
| [[A549 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX11]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CCDC85A]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB10]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[BTG3]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SWAP70]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 | same gene group |
| [[ABRACL]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[RAB32]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[OTUD1]] | +0.54 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[BACH2]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[FILIP1L]] | +0.53 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ENTREP1]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[LITAF]] | +0.52 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6]] | -0.45 | -0.48 / -0.42 | both halves | 4e-05 | same gene group |
| [[TUBGCP2]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[NUP214]] | -0.45 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[SENP5]] | -0.45 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[TYW1]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[RNGTT]] | -0.44 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[AQR]] | -0.44 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[PPP2R5C]] | -0.43 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[FAM156A]] | -0.43 | -0.27 / -0.39 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6KA6]] | B | RPS6KA6 activity raises TBC1D9's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without RPS6KA6 | 0.078 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[SH3GL2]] | B | SH3GL2 activity weakens TBC1D9's drug response | lines that do not express SH3GL2 (14) vs lines expressing it (28) | the lines without SH3GL2 respond 1.27× as strongly (z diff -0.71); strongest at Vinblastine (sulfate) 5 µM: 1.58x vs 1.38x (z diff -1.8) | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM124A, SLC16A10, OLFM1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Erlotinib (drug)]] 0.05 µM | C | TBC1D9 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 1.32× the cells of the other lines | 0.042 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |
| cells under [[Almonertinib (hydrochloride) (drug)]] 0.5 µM | C | TBC1D9 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 0.81× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |
| cells under [[BAY1125976 (drug)]] 0.5 µM | C | TBC1D9 activity raises the cells' numbers under BAY1125976 0.5 µM (protects the cells) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 0.73× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |
| cells under [[Furosemide (drug)]] 0.5 µM | C | TBC1D9 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 1.20× the cells of the other lines | 0.068 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |
| cells under [[9-ING-41 (drug)]] 0.5 µM | C | TBC1D9 activity raises the cells' numbers under 9-ING-41 0.5 µM (protects the cells) | lines that do not express TBC1D9 (6) vs lines expressing it (42) | the lines without TBC1D9: 0.79× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; also absent: SIX1, TRPC1, MTERF1 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.2, 10.2); signed map (40.8, 15.5). **Vector** length 103, 24.7% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.1 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +20.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +8.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +5.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.6 | +4.1 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -3.9 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.5 | -5.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:140,620,782-140,756,385 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0882, MDR1, GRAMD9 |
| Gene groups (HGNC) | EF-hand domain containing; GRAM domain containing; TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZT07](https://www.uniprot.org/uniprotkb/Q6ZT07) (TBC1 domain family member 9):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [23158](https://www.ncbi.nlm.nih.gov/gene/23158):

> Predicted to enable GTPase activator activity. Predicted to be involved in system process. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21710) · Entrez [23158](https://www.ncbi.nlm.nih.gov/gene/23158) · UniProt [Q6ZT07](https://www.uniprot.org/uniprotkb/Q6ZT07) · Ensembl [ENSG00000109436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109436)

## Data

Gene col 3049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3049); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3049]; `tensor/DDL_lfc|DDL_z.npy` [3049]; `embed/gene_vectors.npy` [3049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3049 or target_col == 3049). Every well: [[TBC1D9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
