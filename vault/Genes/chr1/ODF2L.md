---
symbol: "ODF2L"
type: "gene"
col: 4335
ensembl_id: "ENSG00000122417"
name: "outer dense fiber of sperm tails 2 like"
location: "1p22.3"
module: 7
arm: "-"
pooled_cpm: 77.61
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ODF2L

*outer dense fiber of sperm tails 2 like* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.32× (z +5.7, q 5e-06, up in 23 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.25× (z +4.8, q 3e-04, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.515× (z -14.2, q 4e-43, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT81]] (+0.52, fdr 5e-05), [[TMTC3]] (+0.48, fdr 2e-04), [[BCAP29]] (+0.47, fdr 2e-04); moves opposite to [[OXSM]] (-0.48, fdr 1e-04), [[AKAP17A]] (-0.45, fdr 1e-04), [[MMAA]] (-0.43, fdr 2e-04).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.7 | 5e-06 | 23/41 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.17× | +4.9 | 3e-04 | 18/47 (LoVo, LS 180, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +4.8 | 3e-04 | 24/47 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.24×** | +4.7 | 4e-04 | 21/47 (J82, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.5 | 8e-04 | 22/48 (LS 180, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.004 | 20/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.19× | +3.7 | 0.016 | 16/47 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.6 | 0.021 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.026 | 14/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.16× | +3.2 | 0.066 | 11/47 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.066 | 13/47 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.085 | 12/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.15× | +3.1 | 0.092 | 15/47 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.092 | 15/47 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.092 | 6/47 (C-33 A, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.515×** | -14.2 | 4e-43 | 43/47 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -11.8 | 2e-29 | 41/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.705×** | -10.6 | 7e-24 | 31/47 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.390×** | -10.5 | 7e-24 | 35/47 (RKO, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -9.4 | 6e-19 | 33/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.701×** | -7.6 | 3e-12 | 34/47 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.714×** | -6.9 | 4e-10 | 33/46 (RKO, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.734×** | -6.6 | 2e-09 | 28/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -5.0 | 3e-05 | 24/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.795×** | -4.9 | 5e-05 | 26/47 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.800×** | -4.8 | 9e-05 | 23/47 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.809×** | -4.5 | 3e-04 | 22/47 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -4.4 | 6e-04 | 21/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~71% of this change | **0.821×** | -4.2 | 1e-03 | 22/47 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.842× | -3.7 | 0.009 | 15/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.861× | -2.9 | 0.091 | 16/46 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 132 | 0 | 9 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.294× (z -15.6) |
| [[HS-578T (line)]] | alt | 115 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -13.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.213× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 66.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.4) |
| [[HOP62 (line)]] | alt | 89.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -12.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.206× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -11.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -9.0) |
| [[RKO (line)]] | wt | 128 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.244× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.240× (z -9.1) |
| [[A-172 (line)]] | wt | 49.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[C-33 A (line)]] | alt | 106 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +8.8) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.371× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.323× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 70.0 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 78.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.6) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.397× (z -9.8) |
| [[PANC-1 (line)]] | alt | 224 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.240× (z -12.9) |
| [[SNU-423 (line)]] | alt | 48.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -8.7) |
| [[SW480 (line)]] | alt | 74.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.454× (z -11.0) |
| [[A-427 (line)]] | wt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.72× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -12.9) ⚠ cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.1) |
| [[J82 (line)]] | alt | 98.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -11.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[LoVo (line)]] | wt | 48.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -12.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.310× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 94.4 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.215× (z -8.5) |
| [[SW 1088 (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0603× (z -9.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT81]] | +0.52 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[TMTC3]] | +0.48 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[BCAP29]] | +0.47 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[NEK1]] | +0.47 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[CSPP1]] | +0.46 | +0.49 / +0.37 | both halves | 8e-05 | same gene group |
| [[SLC36A4]] | +0.45 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[LINC00342]] | +0.44 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[NBDY]] | +0.44 | +0.21 / +0.53 | both halves | 7e-04 |  |
| [[NEK4]] | +0.44 | +0.26 / +0.45 | both halves | 3e-04 |  |
| [[GKAP1]] | +0.43 | +0.59 / +0.23 | both halves | 5e-04 |  |
| [[ANKRD36C]] | +0.42 | +0.35 / +0.40 | both halves | 1e-04 |  |
| [[ABCB7]] | +0.42 | +0.40 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXSM]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[AKAP17A]] | -0.45 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MMAA]] | -0.43 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[EXOSC7]] | -0.43 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TMEM186]] | -0.43 | -0.20 / -0.48 | both halves | 7e-04 |  |
| [[GOSR2]] | -0.43 | -0.30 / -0.41 | both halves | 2e-04 | same gene group |
| [[FBXL14]] | -0.42 | -0.12 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[METTL13]] | -0.41 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ZNF550]] | -0.41 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[SIAH2]] | -0.41 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[TBC1D14]] | -0.40 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[SLC2A14]] | -0.40 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[TTC28-AS1]] | -0.40 | -0.21 / -0.46 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises ODF2L's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without DYNC2H1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[JAZF1]] | B | JAZF1 activity raises ODF2L's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without JAZF1 | 0.093 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.172). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.9, -13.6); signed map (8.5, -7.9). **Vector** length 86.5, 20.6% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.8 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.9 | +4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.8 | -4.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.3 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.2 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | -2.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.5 | -14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.2 | -10.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~71% of this change | -4.0 | -4.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -3.4 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | outer dense fiber of sperm tails 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:86,346,824-86,396,342 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1229 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULJ1](https://www.uniprot.org/uniprotkb/Q9ULJ1) (Protein BCAP):

> Acts as a suppressor of ciliogenesis, specifically, the initiation of ciliogenesis.

**Summary**, from NCBI Gene [57489](https://www.ncbi.nlm.nih.gov/gene/57489):

> Involved in negative regulation of cilium assembly. Located in centriolar satellite and ciliary basal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29225) · Entrez [57489](https://www.ncbi.nlm.nih.gov/gene/57489) · UniProt [Q9ULJ1](https://www.uniprot.org/uniprotkb/Q9ULJ1) · Ensembl [ENSG00000122417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122417)

## Data

Gene col 4335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4335); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4335]; `tensor/DDL_lfc|DDL_z.npy` [4335]; `embed/gene_vectors.npy` [4335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4335 or target_col == 4335). Every well: [[ODF2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ODF2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
