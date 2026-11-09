---
symbol: "SPAG16"
type: "gene"
col: 6880
ensembl_id: "ENSG00000144451"
name: "sperm associated antigen 16"
location: "2q34"
module: 10
arm: "+"
pooled_cpm: 42.27
n_lines_expressing: 44
n_dd_up: 29
n_dd_down: 23
n_dd_up_clean: 22
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 11
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SPAG16

*sperm associated antigen 16* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.55× (z +9.3, q 5e-18, up in 38 of 42 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.64× (z +7.2, q 1e-10, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.452× (z -11.9, q 4e-30, down in 37 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.455× (z -11.9, q 5e-30, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPOLA]] (+0.64, fdr 2e-05), [[SUCLG2-DT]] (+0.62, fdr 1e-05), [[EIF1B-AS1]] (+0.62, fdr 2e-05); moves opposite to [[EML2]] (-0.62, fdr 1e-05), [[ANKS6]] (-0.61, fdr 3e-05), [[ABHD6]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 11 go from it, the strongest it → cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.55×** | +9.3 | 5e-18 | 38/42 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +7.2 | 1e-10 | 31/41 (A498, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.1 | 2e-10 | 27/42 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.1 | 2e-10 | 26/41 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.5 | 9e-09 | 25/35 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +5.8 | 7e-07 | 28/41 (A-427, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.4 | 7e-06 | 28/42 (LoVo, J82, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-05 | 27/42 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 5e-04 | 18/42 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.4 | 5e-04 | 20/42 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.2 | 0.001 | 19/38 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 20/42 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.002 | 18/42 (A-427, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.003 | 17/42 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.008 | 15/42 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.012 | 16/43 (A-427, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.012 | 15/42 (A-427, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.013 | 19/41 (A-427, A498, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.013 | 12/43 (A-427, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -11.9 | 4e-30 | 37/41 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.455×** | -11.9 | 5e-30 | 38/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -10.5 | 2e-23 | 37/42 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -8.3 | 1e-14 | 33/42 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -5.9 | 4e-07 | 28/42 (LOX-IMVI, SW 900, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -5.3 | 1e-05 | 30/43 (A-427, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.702×** | -5.1 | 3e-05 | 23/41 (J82, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -4.7 | 2e-04 | 20/42 (CHP-212, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.730×** | -4.5 | 4e-04 | 26/42 (COLO 205, HepG2/C3A, …) | two highest doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.566×** | -4.5 | 4e-04 | 25/42 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.810×** | -4.5 | 4e-04 | 20/42 (CFPAC-1, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.755×** | -4.2 | 0.001 | 20/42 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.593×** | -4.1 | 0.002 | 21/42 (LOX-IMVI, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.762×** | -4.1 | 0.002 | 20/42 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.002 | 22/42 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.009 | 15/42 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.029 | 12/42 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.822×** | -2.9 | 0.087 | 11/41 (HT-29, H4, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.816×** | -2.9 | 0.087 | 10/41 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -2.9 | 0.089 | 12/42 (HOP62, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.9 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.324× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.344× (z -10.8) |
| [[J82 (line)]] | alt | 56.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -9.7) |
| [[COLO 205 (line)]] | alt | 50.1 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 57.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.215× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.238× (z -10.2) |
| [[HT-29 (line)]] | alt | 40.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 54.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.65× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 45.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -8.6) |
| [[LoVo (line)]] | wt | 30.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.97× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 36.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +8.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 51.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -8.7) |
| [[A-427 (line)]] | wt | 103 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.162× (z -10.6) |
| [[A498 (line)]] | wt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.310× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -12.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 57.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -11.0) |
| [[RKO (line)]] | wt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 109 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0770× (z -9.7) |
| [[SW 900 (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0531× (z -10.6) ⚠ toxic |
| [[SW480 (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.3) | — |
| [[A-172 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPOLA]] | +0.64 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | +0.62 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[EIF1B-AS1]] | +0.62 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[PDIA3P1]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[IFT81]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZSCAN30]] | +0.58 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[EIF4G2]] | +0.58 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[SUCLA2]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[HTATIP2]] | +0.58 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[MAMDC2-AS1]] | +0.57 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[HFE]] | +0.57 | +0.47 / +0.43 | both halves | 4e-05 |  |
| [[EFCAB6]] | +0.56 | +0.58 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML2]] | -0.62 | -0.52 / -0.54 | both halves | 1e-05 | same gene group |
| [[ANKS6]] | -0.61 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ABHD6]] | -0.58 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[VPS37C]] | -0.57 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[ARID3A]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[RALGDS]] | -0.54 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[CSNK1E]] | -0.54 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[DUSP5]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[HMOX2]] | -0.54 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[SPATA2L]] | -0.53 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[ETHE1]] | -0.53 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[TSEN54]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SPAG16's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | SPAG16 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.78× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Posaconazole (drug)]] 0.5 µM | C | SPAG16 activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.79× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | SPAG16 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.29× the cells of the other lines | 0.030 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | C | SPAG16 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.81× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Folic acid (drug)]] 5 µM | C | SPAG16 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.15× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Tranilast (drug)]] 0.5 µM | C | SPAG16 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.81× the cells of the other lines | 0.051 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Benproperine (phosphate) (drug)]] 0.05 µM | C | SPAG16 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.19× the cells of the other lines | 0.071 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[AZD2858 (drug)]] 5 µM | C | SPAG16 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.36× the cells of the other lines | 0.076 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Cepharanthine (drug)]] 5 µM | C | SPAG16 activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.18× the cells of the other lines | 0.080 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Cobimetinib (drug)]] 0.5 µM | C | SPAG16 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.29× the cells of the other lines | 0.086 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | SPAG16 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.78× the cells of the other lines | 0.097 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.0, 12.3); signed map (18.0, -35.6). **Vector** length 85.1, 20.7% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.6 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:213,284,389-214,410,501 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PF20, FLJ22724, DKFZp666P1710, WDR29 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0X2](https://www.uniprot.org/uniprotkb/Q8N0X2) (Sperm-associated antigen 16 protein):

> Necessary for sperm flagellar function. Plays a role in motile ciliogenesis. May help to recruit STK36 to the cilium or apical surface of the cell to initiate subsequent steps of construction of the central pair apparatus of motile cilia (By similarity).

**Summary**, from NCBI Gene [79582](https://www.ncbi.nlm.nih.gov/gene/79582):

> Cilia and flagella are comprised of a microtubular backbone, the axoneme, which is organized by the basal body and surrounded by plasma membrane. SPAG16 encodes 2 major proteins that associate with the axoneme of sperm tail and the nucleus of postmeiotic germ cells, respectively (Zhang et al., 2007 [PubMed 17699735]).[supplied by OMIM, Jul 2008]

**Accessions** — [HGNC:23225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23225) · Entrez [79582](https://www.ncbi.nlm.nih.gov/gene/79582) · UniProt [Q8N0X2](https://www.uniprot.org/uniprotkb/Q8N0X2) · Ensembl [ENSG00000144451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144451)

## Data

Gene col 6880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6880); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6880]; `tensor/DDL_lfc|DDL_z.npy` [6880]; `embed/gene_vectors.npy` [6880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6880 or target_col == 6880). Every well: [[SPAG16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
