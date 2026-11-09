---
symbol: "COX15"
type: "gene"
col: 290
ensembl_id: "ENSG00000014919"
name: "cytochrome c oxidase assembly factor COX15"
location: "10q24.2"
module: 17
arm: "+"
pooled_cpm: 34.28
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# COX15

*cytochrome c oxidase assembly factor COX15* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.40× (z +7.5, q 3e-11, up in 22 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.33× (z +6.6, q 9e-09, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.547× (z -14.0, q 5e-42, down in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.620× (z -11.1, q 3e-26, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC13]] (+0.65, fdr 7e-06), [[CEPT1]] (+0.62, fdr 1e-05), [[VIPAS39]] (+0.62, fdr 2e-05); moves opposite to [[TLNRD1]] (-0.60, fdr 1e-05), [[MAPKAPK2]] (-0.54, fdr 1e-05), [[ARHGAP39]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +7.5 | 3e-11 | 22/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +6.6 | 9e-09 | 25/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +6.4 | 3e-08 | 24/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.19× | +5.7 | 2e-06 | 20/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.2 | 3e-05 | 16/48 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **1.23×** | +4.9 | 9e-05 | 20/45 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.7 | 2e-04 | 19/46 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +4.5 | 5e-04 | 15/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 5e-04 | 16/47 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.4 | 7e-04 | 16/48 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.3 | 1e-03 | 16/46 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.2 | 0.001 | 18/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.005 | 13/46 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.005 | 11/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.17× | +3.8 | 0.006 | 8/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.008 | 9/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.012 | 7/49 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.012 | 9/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.021 | 10/48 (A-427, CFPAC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.027 | 9/46 (LOX-IMVI, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.029 | 9/48 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -14.0 | 5e-42 | 38/46 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.620×** | -11.1 | 3e-26 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -9.7 | 5e-20 | 35/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -9.0 | 2e-17 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -5.6 | 3e-06 | 24/46 (C-33 A, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.806×** | -5.0 | 5e-05 | 17/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.813×** | -4.8 | 1e-04 | 18/47 (LS 180, HS-578T, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.675×** | -4.8 | 1e-04 | 20/49 (NCI-H23, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.684×** | -4.6 | 2e-04 | 20/47 (NCI-H2030, AsPC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.848× | -3.8 | 0.008 | 11/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.855× | -3.6 | 0.015 | 7/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.856× | -3.6 | 0.015 | 13/47 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.863× | -3.4 | 0.027 | 12/47 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.4 | 0.028 | 14/46 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.860× | -3.4 | 0.028 | 17/48 (COLO 205, AsPC-1, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.903× | -3.3 | 0.031 | 9/48 (NCI-H23, NCI-H1573, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.864× | -3.2 | 0.044 | 12/47 (SW480, AN3 CA, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.830×** | -3.1 | 0.063 | 16/47 (RPMI-7951, H4, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.877× | -2.9 | 0.097 | 6/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 39.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.354× (z -9.9) |
| [[SW480 (line)]] | alt | 37.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.437× (z -10.5) |
| [[Hs 766T (line)]] | wt | 41.4 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0608× (z -16.4) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 37.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.13× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.458× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 55.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.509× (z -9.6) |
| [[A498 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 41.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.261× (z -9.4) |
| [[HCT15 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 32.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.429× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.86× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 33.7 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0831× (z -8.5) |
| [[A-172 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC13]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[CEPT1]] | +0.62 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[VIPAS39]] | +0.62 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[TRUB1]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PHC3]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TSNAX]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MIGA1]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[COPS5]] | +0.58 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[APOOL]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MIX23]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.60 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.54 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ARHGAP39]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[DMPK]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[FBRSL1]] | -0.51 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.50 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TMEM44]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PGAP6]] | -0.49 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[KLF16]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[BCAR3]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ATP8B5P-1]] | -0.48 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[MIDN]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.444). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-18.9, -4.9); signed map (-30.3, -15.8). **Vector** length 89.9, 18.5% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[NG25 (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.8 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -9.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -14.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor COX15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,710,868-99,732,127 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEMCOX2 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Oxidoreductases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins; Complex IV assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7KZN9](https://www.uniprot.org/uniprotkb/Q7KZN9) (Heme A synthase COX15):

> Catalyzes the second reaction in the biosynthesis of heme A, a prosthetic group of mitochondrial cytochrome c oxidase (CcO). Heme A is synthesized from heme B by two sequential enzymatic reactions catalyzed by heme O synthase (HOS) and heme A synthase (HAS). HAS catalyzes the conversion of heme O to heme A by two successive hydroxylations of the methyl group at C8, in a reaction that involves matrix ferredoxin and ferredoxin reductase. The first hydroxylation forms heme I, the second …

**Summary**, from NCBI Gene [1355](https://www.ncbi.nlm.nih.gov/gene/1355):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2263) · Entrez [1355](https://www.ncbi.nlm.nih.gov/gene/1355) · UniProt [Q7KZN9](https://www.uniprot.org/uniprotkb/Q7KZN9) · Ensembl [ENSG00000014919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014919)

## Data

Gene col 290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 290); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 290]; `tensor/DDL_lfc|DDL_z.npy` [290]; `embed/gene_vectors.npy` [290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 290 or target_col == 290). Every well: [[COX15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
