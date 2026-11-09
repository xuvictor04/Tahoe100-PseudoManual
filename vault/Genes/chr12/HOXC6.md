---
symbol: "HOXC6"
type: "gene"
col: 12456
ensembl_id: "ENSG00000197757"
name: "homeobox C6"
location: "12q13.13"
module: 46
arm: "+"
pooled_cpm: 15.71
n_lines_expressing: 40
n_dd_up: 15
n_dd_down: 33
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 6
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXC6

*homeobox C6* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +9.0, q 9e-17, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.411× (z -13.3, q 1e-37, down in 31 of 38 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.595× (z -7.8, q 8e-13, down in 27 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXC9]] (+0.72, fdr 7e-06, ⚠ same locus), [[HOXC4]] (+0.71, fdr 7e-06, ⚠ same locus), [[ZNF362]] (+0.65, fdr 3e-05), [[SIAH1]] (+0.64, fdr 4e-05), [[LINC00938]] (+0.64, fdr 5e-05); moves opposite to [[PPARD]] (-0.51, fdr 3e-04), [[LRRFIP1]] (-0.51, fdr 2e-04), [[SERPINB1]] (-0.51, fdr 3e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HOXC10]] → it (grade B ⚠); 6 go from it, the strongest it → [[ZIC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.0 | 9e-17 | 18/36 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.35×** | +6.5 | 3e-08 | 18/37 (A-172, RKO, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +5.1 | 8e-05 | 14/38 (PANC-1, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 8e-05 | 11/36 (SW480, PANC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.5 | 7e-04 | 13/35 (PANC-1, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 7e-04 | 11/37 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.35×** | +4.4 | 8e-04 | 16/38 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 0.001 | 9/36 (HT-29, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.010 | 9/37 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.012 | 12/37 (PANC-1, A-427, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.012 | 10/36 (C32, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.012 | 8/36 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.014 | 7/37 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.014 | 7/38 (LoVo, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.018 | 6/37 (KATO III, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.028 | 9/38 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.045 | 7/35 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.411×** | -13.3 | 1e-37 | 31/38 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.425×** | -12.8 | 5e-35 | 30/38 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.430×** | -12.6 | 3e-34 | 32/37 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.499×** | -10.4 | 3e-23 | 29/35 (NCI-H1792, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.515×** | -9.9 | 4e-21 | 30/38 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.595×** | -7.8 | 8e-13 | 27/36 (A-427, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.589×** | -7.6 | 2e-12 | 22/38 (AN3 CA, C32, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.593×** | -7.5 | 4e-12 | 19/34 (NCI-H23, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.607×** | -7.5 | 5e-12 | 23/37 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.611×** | -7.4 | 9e-12 | 22/37 (BT-474, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.616×** | -7.2 | 2e-11 | 22/36 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -7.2 | 3e-11 | 22/37 (AN3 CA, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -7.0 | 1e-10 | 24/38 (AN3 CA, C32, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.674×** | -5.9 | 1e-07 | 20/37 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.504×** | -5.4 | 3e-06 | 16/37 (PANC-1, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.684×** | -5.4 | 3e-06 | 21/37 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.005 | 10/38 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.840× | -3.7 | 0.006 | 15/37 (HT-29, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.009 | 11/37 (HT-29, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.025 | 14/37 (AN3 CA, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.1 | 0.039 | 16/38 (C-33 A, PANC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.042 | 8/37 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.686×** | -2.9 | 0.060 | 7/35 (PANC-1, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.760×** | -2.9 | 0.063 | 10/35 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 125 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0716× (z -15.3) |
| [[C-33 A (line)]] | alt | 95.1 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0972× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 29.4 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0652× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -10.7) |
| [[A-427 (line)]] | wt | 27.3 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 61.5 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -18.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 36.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -11.7) |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0567× (z -14.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.204× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H661 (line)]] | alt | 79.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0229× (z -16.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 8.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0781× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 8.77 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.115× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 8.23 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.240× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXC9]] | +0.72 | +0.59 / +0.65 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXC4]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; STRING 966; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF362]] | +0.65 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[SIAH1]] | +0.64 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[LINC00938]] | +0.64 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[HOXC8]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 | same gene group; STRING 840; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXD3]] | +0.61 | +0.44 / +0.44 | both halves | 3e-05 | same gene group |
| [[INPPL1]] | +0.60 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[HOXB7]] | +0.60 | +0.26 / +0.61 | both halves | 4e-04 | same gene group; STRING 929 |
| [[TSTD3]] | +0.60 | +0.32 / +0.51 | both halves | 2e-04 |  |
| [[LDB1]] | +0.59 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[CDK2AP1]] | +0.59 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[PRRT2]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SETD1B]] | +0.58 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[CFAP418]] | +0.58 | +0.53 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPARD]] | -0.51 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[LRRFIP1]] | -0.51 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[SERPINB1]] | -0.51 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[OSBPL8]] | -0.51 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[RALGAPA2]] | -0.51 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[FLNB]] | -0.51 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[AKAP13]] | -0.50 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[LAMA3]] | -0.49 | -0.49 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC10]] | B | HOXC10 activity raises HOXC6's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 3.13× lower at baseline in the lines without HOXC10 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOTAIR]] | B | HOTAIR activity raises HOXC6's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without HOTAIR | 0.025 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[MAP2K1]] | B | MAP2K1 activity lowers HOXC6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXB-AS1]] | B | HOXB-AS1 activity raises HOXC6's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without HOXB-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[LINC01139]] | B | LINC01139 activity raises HOXC6's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.66× lower at baseline in the lines without LINC01139 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[ZIC2]] | B | ZIC2 activity raises HOXC6's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.58× lower at baseline in the lines without ZIC2 | 0.091 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |
| [[FLJ12825]] | C | FLJ12825 activity raises HOXC6's level | lines that do not express FLJ12825 (15) vs lines expressing it (35) | 3.78× lower at baseline in the lines without FLJ12825 | 0.001 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent; co-absent with the target |
| [[HOXC8]] | C | HOXC8 activity raises HOXC6's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 4.36× lower at baseline in the lines without HOXC8 | 0.001 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5; co-absent with the target |
| [[HOXC4]] | C | HOXC4 activity raises HOXC6's level | lines that do not express HOXC4 (11) vs lines expressing it (39) | 4.62× lower at baseline in the lines without HOXC4 | 0.006 | ⚠ within organs, on part of the lines; also absent: HOXC6, HOXC8, HOXC9; maybe low, not absent; co-absent with the target |
| [[HOXC9]] | C | HOXC9 activity raises HOXC6's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 3.49× lower at baseline in the lines without HOXC9 | 0.029 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZIC2]] | B | HOXC6 activity raises ZIC2's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without HOXC6 | 0.026 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent |
| [[HOXC10]] | B | HOXC6 activity raises HOXC10's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 3.68× lower at baseline in the lines without HOXC6 | 0.048 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent |
| [[HOXC9]] | C | HOXC6 activity raises HOXC9's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 4.24× lower at baseline in the lines without HOXC6 | 0.003 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |
| [[HOXC8]] | C | HOXC6 activity raises HOXC8's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 3.71× lower at baseline in the lines without HOXC6 | 0.006 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |
| [[HOXC4]] | C | HOXC6 activity raises HOXC4's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 3.35× lower at baseline in the lines without HOXC6 | 0.022 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |
| [[FLJ12825]] | C | HOXC6 activity raises FLJ12825's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 2.42× lower at baseline in the lines without HOXC6 | 0.043 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.0, 25.6); signed map (33.7, -22.6). **Vector** length 71.6, 13.5% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +9.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.4 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.6 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.9 | -12.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -13.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | homeobox C6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,990,624-54,030,823 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX3C, HOX3 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P09630](https://www.uniprot.org/uniprotkb/P09630) (Homeobox protein Hox-C6):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3223](https://www.ncbi.nlm.nih.gov/gene/3223):

> This gene belongs to the homeobox family, members of which encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, which are located on different chromosomes and consist of 9 to 11 genes arranged in tandem. This gene, HOXC6, is one of several HOXC genes located in a cluster on chromosome 12. Three genes, HOXC5, HOXC4 and HOXC6, share a 5' …

**Accessions** — [HGNC:5128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5128) · Entrez [3223](https://www.ncbi.nlm.nih.gov/gene/3223) · UniProt [P09630](https://www.uniprot.org/uniprotkb/P09630) · Ensembl [ENSG00000197757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197757)

## Data

Gene col 12456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12456); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12456]; `tensor/DDL_lfc|DDL_z.npy` [12456]; `embed/gene_vectors.npy` [12456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12456 or target_col == 12456). Every well: [[HOXC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
