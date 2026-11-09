---
symbol: "DUBR"
type: "gene"
col: 14372
ensembl_id: "ENSG00000243701"
name: "DPPA2 upstream binding RNA"
location: "3q13.12"
module: 182
arm: "+"
pooled_cpm: 9.56
n_lines_expressing: 42
n_dd_up: 49
n_dd_down: 8
n_dd_up_clean: 38
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# DUBR

*DPPA2 upstream binding RNA* — 3q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.07× (z +14.4, q 2e-44, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.423× (z -8.9, q 4e-16, down in 26 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.483× (z -7.5, q 8e-12, down in 26 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.177×, HS-578T 0.220×, HEC-1-A 0.345×, LOX-IMVI 0.217×; ⚠ cell-cycle shift, explains ~89% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (Panc 03.27 0.0478×, HOP62 0.120×, HEC-1-A 0.313×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.0723×, A549 0.127×, A-172 0.237×; ⚠ cell-cycle shift, explains ~75% of this change); [[Menadione (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0807×); [[Decitabine (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0892×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMOD2]] (+0.62, fdr 8e-06), [[GNAI1]] (+0.59, fdr 1e-05), [[RFXAP]] (+0.58, fdr 1e-05); moves opposite to [[BCL2L12]] (-0.62, fdr 2e-05), [[SLC30A7]] (-0.53, fdr 4e-05), [[SLC35C2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KATNAL1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ESPL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.07×** | +14.4 | 2e-44 | 36/40 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.58×** | +13.1 | 9e-37 | 35/40 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +12.5 | 9e-34 | 35/40 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.29×** | +12.2 | 3e-32 | 34/39 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.88×** | +10.8 | 6e-25 | 35/40 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +9.5 | 3e-19 | 31/34 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.23×** | +8.2 | 2e-14 | 32/40 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +8.1 | 4e-14 | 27/38 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.72×** | +7.9 | 2e-13 | 22/40 (A498, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **3.68×** | +7.0 | 1e-10 | 32/40 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.94×** | +6.8 | 5e-10 | 27/40 (NCI-H1792, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +5.9 | 2e-07 | 20/38 (J82, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.7 | 5e-07 | 9/17 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.73×** | +5.6 | 8e-07 | 21/39 (C32, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.71×** | +5.3 | 5e-06 | 20/38 (A498, HS-578T, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.39×** | +4.7 | 7e-05 | 17/40 (SK-MEL-2, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +4.5 | 2e-04 | 14/39 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.60×** | +4.4 | 3e-04 | 16/40 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +4.4 | 3e-04 | 18/40 (PANC-1, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 3e-04 | 15/40 (NCI-H23, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14372.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.177×, HS-578T 0.220×, HEC-1-A 0.345×, LOX-IMVI 0.217×; ⚠ cell-cycle shift, explains ~89% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (Panc 03.27 0.0478×, HOP62 0.120×, HEC-1-A 0.313×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.0723×, A549 0.127×, A-172 0.237×; ⚠ cell-cycle shift, explains ~75% of this change); [[Menadione (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0807×); [[Decitabine (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0892×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -8.9 | 4e-16 | 26/38 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.551×** | -8.7 | 8e-16 | 21/38 (A-172, HS-578T, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.447×** | -8.3 | 2e-14 | 28/40 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.483×** | -7.5 | 8e-12 | 26/39 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.484×** | -7.5 | 8e-12 | 29/40 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.580×** | -5.4 | 6e-06 | 23/39 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.605×** | -5.2 | 2e-05 | 19/37 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.711×** | -3.5 | 0.029 | 18/39 (LOX-IMVI, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.741× | -3.1 | 0.12 | 13/40 (HS-578T, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.3) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0807× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 4.83 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 14.5× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.86× (z +9.8) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 11.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.86× (z +8.6) | — |
| [[A549 (line)]] | wt | 7.62 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -8.8) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HOP62 (line)]] | alt | 8.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LOX-IMVI (line)]] | wt | 8.43 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0654× (z -8.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 6.90 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0723× (z -9.3) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H23 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.89× (z +10.5) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 7.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.159× (z -9.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[Panc 03.27 (line)]] | alt | 8.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0478× (z -12.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 6.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +8.6) | — |
| [[SW480 (line)]] | alt | 3.59 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.95× (z +8.5) | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD2]] | +0.62 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[GNAI1]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RFXAP]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ABRAXAS1]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RAB4A]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[GNA13]] | +0.52 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[NXPE3]] | +0.51 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[WWP1]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TMEM185A]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[RPS3A]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[PPP1CB]] | +0.51 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[ZDHHC7]] | +0.51 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L12]] | -0.62 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SLC30A7]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[SLC35C2]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SETX]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[HOMER1]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[DNAH1]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SP2]] | -0.48 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[PINLYP]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PHF19]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.47 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[EGR3]] | -0.47 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[ALG13]] | -0.46 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises DUBR's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.89× lower at baseline in the lines without KATNAL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESPL1]] | B | DUBR activity raises ESPL1's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.98× lower at baseline in the lines without DUBR | 0.049 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |
| [[MBD2]] | B | DUBR activity raises MBD2's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without DUBR | 0.055 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |
| [[IFNGR1]] | B | DUBR activity lowers IFNGR1's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.97× higher at baseline in the lines without DUBR | 0.073 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |
| [[SLC39A6]] | B | DUBR activity raises SLC39A6's level | lines that do not express DUBR (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without DUBR | 0.080 | ⚠ within organs, on part of the lines; also absent: ATP10D, LRP12, CYP46A1 |

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.7, -5.1); signed map (-34.3, -19.0). **Vector** length 74.0, 14.5% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +7.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.5 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -4.2 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.8 | -5.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.2 | -3.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[Ritonavir (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -0.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | DPPA2 upstream binding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q13.12 — chr3:107,220,744-107,348,464 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00883 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48569) · Entrez [344595](https://www.ncbi.nlm.nih.gov/gene/344595) · Ensembl [ENSG00000243701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243701)

## Data

Gene col 14372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14372); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14372]; `tensor/DDL_lfc|DDL_z.npy` [14372]; `embed/gene_vectors.npy` [14372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14372 or target_col == 14372). Every well: [[DUBR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUBR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
