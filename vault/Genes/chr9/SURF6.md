---
symbol: "SURF6"
type: "gene"
col: 7259
ensembl_id: "ENSG00000148296"
name: "surfeit 6"
location: "9q34.2"
module: 11
arm: "+"
pooled_cpm: 29.9
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SURF6

*surfeit 6* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 4.05× (z +17.3, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.695× (z -4.4, q 0.006, down in 18 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.811× (z -3.7, q 0.072, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SHP-77 0.171×, RPMI-7951 0.138×, A549 0.209×, C-33 A 0.287×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0968×, SK-MEL-2 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0928×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPZ]] (+0.85, fdr 7e-06), [[NIFK]] (+0.82, fdr 7e-06), [[REXO4]] (+0.82, fdr 7e-06); moves opposite to [[LAMP2]] (-0.68, fdr 7e-06), [[TMED4]] (-0.68, fdr 7e-06), [[TMEM30A]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.05×** | +17.3 | 0e+00 | 46/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.92×** | +17.1 | 0e+00 | 47/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.54×** | +15.1 | 0e+00 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.21×** | +14.4 | 4e-45 | 48/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.26×** | +10.1 | 9e-22 | 44/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.65×** | +10.0 | 2e-21 | 44/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.97×** | +8.4 | 4e-15 | 46/48 (AsPC-1, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.9 | 1e-13 | 40/46 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +7.8 | 4e-13 | 42/48 (AsPC-1, SW480, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.73×** | +6.7 | 9e-10 | 42/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +6.3 | 2e-08 | 38/47 (SW480, BT-474, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.58×** | +6.1 | 4e-08 | 35/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 3e-07 | 30/48 (NCI-H1792, BT-474, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.2 | 8e-06 | 29/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.0 | 2e-05 | 30/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 26/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.023 | 17/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7259.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (SHP-77 0.171×, RPMI-7951 0.138×, A549 0.209×, C-33 A 0.287×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.0968×, SK-MEL-2 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0928×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -4.4 | 0.006 | 18/38 (SHP-77, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.811×** | -3.7 | 0.072 | 19/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.752× | -3.3 | 0.14 | 9/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.770× | -3.3 | 0.14 | 13/47 (AsPC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.768× | -3.2 | 0.14 | 20/47 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.777× | -3.2 | 0.14 | 16/48 (HCT15, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 23.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.7 | 6 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.38× (z +10.8) | — |
| [[LoVo (line)]] | wt | 27.5 | 5 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.68× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 27.6 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.94× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 31.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 23.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +15.2) | — |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 40.3 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.23× (z +12.2) | — |
| [[A-172 (line)]] | wt | 29.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.8) | — |
| [[A498 (line)]] | wt | 32.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 52.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 18.9 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.87× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 18.5 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.90× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.62× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 26.7 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 8.99× (z +10.5) | — |
| [[H4 (line)]] | wt | 31.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 19.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 19.8 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.29× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.82× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 56.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 54.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0968× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 13.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.92× (z +10.7) | — |
| [[KATO III (line)]] | alt | 38.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.18× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 38.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.07× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 27.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +11.2) | — |
| [[A-427 (line)]] | wt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0928× (z -10.3) |
| [[Hs 766T (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 4.53× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | +0.85 | +0.83 / +0.87 | both halves | 7e-06 | STRING 902 |
| [[NIFK]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | STRING 978 |
| [[REXO4]] | +0.82 | +0.84 / +0.80 | both halves | 7e-06 | STRING 673 |
| [[UTP3]] | +0.79 | +0.84 / +0.83 | both halves | 7e-06 | STRING 874 |
| [[MRM2]] | +0.78 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[ESF1]] | +0.78 | +0.82 / +0.73 | both halves | 7e-06 | STRING 900 |
| [[PRPF38B]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.77 | +0.78 / +0.79 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | STRING 960 |
| [[UTP14A]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 | STRING 699 |
| [[ZNF146]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | -0.68 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[TMED4]] | -0.68 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[TMEM30A]] | -0.67 | -0.60 / -0.74 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[CMPK1]] | -0.65 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[TWSG1]] | -0.64 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[RCN2]] | -0.63 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.63 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[PGRMC1]] | -0.62 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[RNPEP]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[RTN3]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[TM9SF2]] | -0.61 | -0.60 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.813). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.3, 1.4); signed map (-1.4, -20.5). **Vector** length 102, 30.2% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.5 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.9 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +15.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.0 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.6 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | surfeit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,328,776-133,336,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30322, RRP14 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75683](https://www.uniprot.org/uniprotkb/O75683) (Surfeit locus protein 6):

> Binds to both DNA and RNA in vitro, with a stronger binding capacity for RNA. May represent a nucleolar constitutive protein involved in ribosomal biosynthesis or assembly (By similarity).

**Summary**, from NCBI Gene [6838](https://www.ncbi.nlm.nih.gov/gene/6838):

> This gene encodes a conserved protein that is localized to the nucleolus. The encoded protein may function as a nucleolar-matrix protein with nucleic acid-binding properties. There is a pseudogene for this gene on chromosome Y. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:11478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11478) · Entrez [6838](https://www.ncbi.nlm.nih.gov/gene/6838) · UniProt [O75683](https://www.uniprot.org/uniprotkb/O75683) · Ensembl [ENSG00000148296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148296)

## Data

Gene col 7259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7259); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7259]; `tensor/DDL_lfc|DDL_z.npy` [7259]; `embed/gene_vectors.npy` [7259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7259 or target_col == 7259). Every well: [[SURF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SURF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
