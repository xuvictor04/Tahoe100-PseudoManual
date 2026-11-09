---
symbol: "RBM28"
type: "gene"
col: 2746
ensembl_id: "ENSG00000106344"
name: "RNA binding motif protein 28"
location: "7q32.1"
module: 1
arm: "+"
pooled_cpm: 84.59
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RBM28

*RNA binding motif protein 28* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +19.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.825× (z -6.8, q 6e-09, down in 26 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (RKO 0.414×, A498 0.498×, LOX-IMVI 0.515×, NCI-H23 0.632×, …); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (AN3 CA 0.0945×; ⚠ toxic); [[Roxadustat (drug)]] 0.5 µM in 1 line (SW 1088 0.0851×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAK16]] (+0.77, fdr 7e-06), [[BMS1]] (+0.77, fdr 7e-06), [[AGK]] (+0.74, fdr 7e-06); moves opposite to [[GNAS]] (-0.64, fdr 7e-06), [[TMEM59]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APLP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +19.3 | 0e+00 | 42/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +18.9 | 0e+00 | 43/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +12.1 | 2e-31 | 41/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.61×** | +11.8 | 6e-30 | 43/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +11.4 | 5e-28 | 40/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.52×** | +10.4 | 4e-23 | 42/48 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.51×** | +10.3 | 6e-23 | 43/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +8.9 | 3e-17 | 40/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +8.8 | 1e-16 | 40/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +8.4 | 3e-15 | 38/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +7.9 | 1e-13 | 37/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +7.9 | 1e-13 | 31/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.36×** | +7.3 | 2e-11 | 27/44 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +7.2 | 2e-11 | 34/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.32×** | +6.9 | 3e-10 | 29/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +6.1 | 4e-08 | 33/48 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +5.8 | 2e-07 | 31/48 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +5.3 | 4e-06 | 32/49 (KATO III, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +5.2 | 7e-06 | 17/49 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +5.0 | 1e-05 | 27/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +5.0 | 1e-05 | 28/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.7 | 5e-05 | 21/48 (SW480, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2746.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (RKO 0.414×, A498 0.498×, LOX-IMVI 0.515×, NCI-H23 0.632×, …); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (AN3 CA 0.0945×; ⚠ toxic); [[Roxadustat (drug)]] 0.5 µM in 1 line (SW 1088 0.0851×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -6.8 | 6e-09 | 26/49 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.863× | -3.7 | 0.069 | 14/47 (A-172, LoVo, …) | two highest doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.870× | -3.5 | 0.098 | 14/48 (KATO III, C-33 A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.11 | 12/47 (A-172, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.893× | -3.3 | 0.11 | 7/48 (MIA PaCa-2, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | 0.875× | -3.2 | 0.12 | 6/48 (NCI-H1792, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.879× | -3.1 | 0.17 | 14/47 (LoVo, LOX-IMVI, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 72.1 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.86× (z +16.2) | — |
| [[SW480 (line)]] | alt | 90.2 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.01× (z +11.6) | — |
| [[C32 (line)]] | wt | 134 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.7) | — |
| [[LoVo (line)]] | wt | 89.0 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -8.7) |
| [[PANC-1 (line)]] | alt | 89.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.6) | — |
| [[A549 (line)]] | wt | 75.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 73.5 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[CFPAC-1 (line)]] | alt | 52.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.3) | — |
| [[H4 (line)]] | wt | 85.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 52.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 79.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 56.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 43.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 36.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 183 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 73.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 88.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 66.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 52.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.9) | — |
| [[A-172 (line)]] | wt | 45.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.5) | — |
| [[A498 (line)]] | wt | 148 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -15.4) |
| [[AN3 CA (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0945× (z -10.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 67.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[J82 (line)]] | alt | 75.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.0) | — |
| [[KATO III (line)]] | alt | 77.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.01× (z +8.7) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 66.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +10.8) | — |
| [[RKO (line)]] | wt | 165 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -17.5) |
| [[SHP-77 (line)]] | alt | 89.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0851× (z -9.8) |
| [[SW 900 (line)]] | alt | 59.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) | — |
| [[SW48 (line)]] | wt | 141 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.8) |
| [[A-427 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAK16]] | +0.77 | +0.79 / +0.80 | both halves | 7e-06 | same gene group; STRING 941 |
| [[BMS1]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 986 |
| [[AGK]] | +0.74 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 | STRING 599 |
| [[ZNHIT6]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[LTV1]] | +0.73 | +0.76 / +0.77 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 864 |
| [[PUM3]] | +0.73 | +0.73 / +0.74 | both halves | 7e-06 | STRING 972 |
| [[RRP15]] | +0.72 | +0.68 / +0.76 | both halves | 7e-06 | STRING 919 |
| [[PRMT5]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[NOP14]] | +0.71 | +0.74 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 946 |
| [[EIF2B3]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 976 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.64 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | APLP1 activity raises RBM28's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without APLP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.5, -39.3); signed map (-2.8, -42.2). **Vector** length 98.1, 28.3% of its response variance represented; |z| ≥ 3 in 1,303 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.56 to 15); *MYC targets v2* (hallmark, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +18.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.5 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,297,685-128,343,908 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10377, NOP4 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NW13](https://www.uniprot.org/uniprotkb/Q9NW13) (RNA-binding protein 28):

> Nucleolar component of the spliceosomal ribonucleoprotein complexes.

**Summary**, from NCBI Gene [55131](https://www.ncbi.nlm.nih.gov/gene/55131):

> The protein encoded by this gene is a specific nucleolar component of the spliceosomal small nuclear ribonucleoprotein (snRNP)complexes . It specifically associates with U1, U2, U4, U5, and U6 small nuclear RNAs (snRNAs), possibly coordinating their transition through the nucleolus. Mutation in this gene causes alopecia, progressive neurological defects, and endocrinopathy (ANE syndrome), a pleiotropic and clinically heterogeneous disorder. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:21863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21863) · Entrez [55131](https://www.ncbi.nlm.nih.gov/gene/55131) · UniProt [Q9NW13](https://www.uniprot.org/uniprotkb/Q9NW13) · Ensembl [ENSG00000106344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106344)

## Data

Gene col 2746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2746); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2746]; `tensor/DDL_lfc|DDL_z.npy` [2746]; `embed/gene_vectors.npy` [2746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2746 or target_col == 2746). Every well: [[RBM28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
