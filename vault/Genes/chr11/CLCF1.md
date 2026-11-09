---
symbol: "CLCF1"
type: "gene"
col: 10617
ensembl_id: "ENSG00000175505"
name: "cardiotrophin like cytokine factor 1"
location: "11q13.2"
module: 101
arm: "+"
pooled_cpm: 20.06
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 17
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# CLCF1

*cardiotrophin like cytokine factor 1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.66× (z +4.5, q 0.003, up in 9 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.83× (z +4.0, q 0.014, up in 23 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 4.92×, SNU-423 5.17×, CFPAC-1 3.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 5.19×, A498 3.99×; ⚠ cell-cycle shift, explains ~34% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A498 6.00×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.148× (z -17.5, q 0e+00, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP5-DT]] (+0.68, fdr 7e-06), [[PLEKHN1]] (+0.68, fdr 7e-06), [[TLNRD1]] (+0.66, fdr 7e-06); moves opposite to [[ATP5F1C]] (-0.63, fdr 1e-05), [[SKIC3]] (-0.63, fdr 1e-05), [[PPP1CB]] (-0.61, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CCDC71L]] → it (grade B ⚠); 17 go from it, the strongest it → [[ZBTB7A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 4.92×, SNU-423 5.17×, CFPAC-1 3.74×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 5.19×, A498 3.99×; ⚠ cell-cycle shift, explains ~34% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A498 6.00×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.5 | 0.003 | 9/25 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +4.4 | 0.003 | 20/36 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.83×** | +4.0 | 0.014 | 23/39 (HT-29, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.020 | 23/39 (AN3 CA, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.7 | 0.023 | 21/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.5 | 0.048 | 15/37 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.42× | +3.2 | 0.10 | 17/39 (HT-29, A498, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.41× | +3.2 | 0.11 | 18/40 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[vincristine (drug)]] 5 µM |  | 2.07× | +3.1 | 0.11 | 13/35 (HT-29, HCT15, …) | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.11 | 18/39 (AN3 CA, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.40× | +3.1 | 0.11 | 12/32 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.39× | +3.0 | 0.11 | 19/39 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.59× | +3.0 | 0.11 | 13/39 (A549, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10617.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.148×** | -17.5 | 0e+00 | 36/40 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.152×** | -17.3 | 0e+00 | 36/40 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.180×** | -15.7 | 0e+00 | 36/40 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.408×** | -8.2 | 3e-14 | 34/40 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.199×** | -7.0 | 4e-10 | 32/39 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.621×** | -6.2 | 6e-08 | 29/41 (SW48, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.587×** | -4.5 | 5e-04 | 22/40 (SW48, BT-474, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.692×** | -4.0 | 0.004 | 21/40 (SW48, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.654×** | -3.9 | 0.006 | 19/39 (HOP62, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.745×** | -3.8 | 0.008 | 22/41 (SW48, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.650×** | -3.7 | 0.010 | 16/39 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.673×** | -3.6 | 0.013 | 16/40 (HOP62, SW 900, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.691×** | -3.4 | 0.031 | 18/39 (SW48, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.702×** | -3.2 | 0.048 | 19/39 (SW48, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.048 | 15/39 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.697×** | -3.2 | 0.052 | 19/39 (SW48, BT-474, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -3.0 | 0.066 | 14/39 (Panc 03.27, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 104 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0429× (z -16.1) |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0379× (z -24.5) |
| [[MIA PaCa-2 (line)]] | alt | 42.9 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.19× (z +9.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.0436× (z -17.2) |
| [[A498 (line)]] | wt | 14.9 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0921× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 22.2 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -11.5) |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0501× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 33.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0846× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0703× (z -14.0) |
| [[SNU-423 (line)]] | alt | 19.6 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.0517× (z -15.8) |
| [[A-172 (line)]] | wt | 12.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -11.1) |
| [[A549 (line)]] | wt | 31.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0948× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0785× (z -13.1) |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0498× (z -18.0) |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0608× (z -16.2) |
| [[J82 (line)]] | alt | 31.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 43.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0677× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.110× (z -12.6) |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0769× (z -15.7) |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0708× (z -12.2) |
| [[SW480 (line)]] | alt | 12.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -10.3) |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0477× (z -16.7) |
| [[LoVo (line)]] | wt | 10.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -12.0) |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -13.2) |
| [[A-427 (line)]] | wt | 9.02 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -9.1) |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0977× (z -10.1) |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.0692× (z -9.0) |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 9.21 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -9.1) |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP5-DT]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PLEKHN1]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[TLNRD1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ZNF562]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[C11orf91]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SMURF1]] | +0.62 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[STK10]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZSWIM4]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RFFL]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R14B-AS1]] | +0.59 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[S100A11]] | +0.59 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[TMEM217]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1C]] | -0.63 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[SKIC3]] | -0.63 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[PPP1CB]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[BBS2]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[RHOXF1]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CREG1]] | -0.58 | -0.49 / -0.60 | both halves | 2e-05 |  |
| [[SKP2]] | -0.57 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ZMYM3]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[IARS2]] | -0.57 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[SLC44A1]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[UBA5]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[EPHX2]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC71L]] | B | CCDC71L activity raises CLCF1's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 2.17× lower at baseline in the lines without CCDC71L | 0.009 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[EPHX2]] | B | EPHX2 activity raises CLCF1's level | lines that do not express EPHX2 (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without EPHX2 | 0.010 | ⚠ within organs, on part of the lines; also absent: MELTF, OPLAH, SEPTIN9-DT |
| [[PHLDA2]] | B | PHLDA2 activity raises CLCF1's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.75× lower at baseline in the lines without PHLDA2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[WFDC3]] | B | WFDC3 activity raises CLCF1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without WFDC3 | 0.032 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[MELTF]] | B | MELTF activity raises CLCF1's level | lines that do not express MELTF (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without MELTF | 0.060 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent; its own permutation p |
| [[MAP2K1]] | B | MAP2K1 activity raises CLCF1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[PLEKHN1]] | C | PLEKHN1 activity raises CLCF1's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 3.34× lower at baseline in the lines without PLEKHN1 | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBTB7A]] | B | CLCF1 activity raises ZBTB7A's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without CLCF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[CD58]] | B | CLCF1 activity raises CD58's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without CLCF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[SNX9]] | B | CLCF1 activity raises SNX9's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without CLCF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[HMGN3]] | B | CLCF1 activity lowers HMGN3's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.77× higher at baseline in the lines without CLCF1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[MAMLD1]] | B | CLCF1 activity raises MAMLD1's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without CLCF1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[S100A11]] | B | CLCF1 activity raises S100A11's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 3.12× lower at baseline in the lines without CLCF1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[STK10]] | B | CLCF1 activity raises STK10's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without CLCF1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[PPP1CC]] | B | CLCF1 activity lowers PPP1CC's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without CLCF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[ZSWIM4]] | B | CLCF1 activity raises ZSWIM4's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without CLCF1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[SLC25A45]] | B | CLCF1 activity raises SLC25A45's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.93× lower at baseline in the lines without CLCF1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[CCDC71L]] | B | CLCF1 activity raises CCDC71L's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without CLCF1 | 0.050 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[SKP2]] | B | CLCF1 activity lowers SKP2's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.55× higher at baseline in the lines without CLCF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.5, -7.0); signed map (1.9, 32.5). **Vector** length 107, 31.0% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +1.0 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | cardiotrophin like cytokine factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,364,168-67,374,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NNT1, BSF3, CLC, NR6, CISS2, BSF-3, NNT-1 |
| Gene groups (HGNC) | Interleukin 6 type cytokine family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBD9](https://www.uniprot.org/uniprotkb/Q9UBD9) (Cardiotrophin-like cytokine factor 1):

> Functions as a cytokine, either alone or by forming a stable complex with soluble CRLF1 or CNTFR. Binds to CNTFR complex (CNTFR, IL6ST/gp130, LIFR) or can signal via trans-signaling using soluble CNTFR subunits. Mechanistically, ligand binding to CNTFR, induces dimerization of the IL6ST/gp130 and LIFR, which activates JAK tyrosine kinases (JAK1 or JAK2 and to lesser extent TYK2) bound to their intracellular domains. These kinases subsequently phosphorylate IL6ST/gp130 and LIFR. The tyrosine …

**Summary**, from NCBI Gene [23529](https://www.ncbi.nlm.nih.gov/gene/23529):

> This gene is a member of the glycoprotein (gp)130 cytokine family and encodes cardiotrophin-like cytokine factor 1 (CLCF1). CLCF1 forms a heterodimer complex with cytokine receptor-like factor 1 (CRLF1). This dimer competes with ciliary neurotrophic factor (CNTF) for binding to the ciliary neurotrophic factor receptor (CNTFR) complex, and activates the Jak-STAT signaling cascade. CLCF1 can be actively secreted from cells by forming a complex with soluble type I CRLF1 or soluble CNTFR. CLCF1 is …

**Accessions** — [HGNC:17412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17412) · Entrez [23529](https://www.ncbi.nlm.nih.gov/gene/23529) · UniProt [Q9UBD9](https://www.uniprot.org/uniprotkb/Q9UBD9) · Ensembl [ENSG00000175505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175505)

## Data

Gene col 10617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10617); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10617]; `tensor/DDL_lfc|DDL_z.npy` [10617]; `embed/gene_vectors.npy` [10617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10617 or target_col == 10617). Every well: [[CLCF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
