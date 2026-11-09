---
symbol: "EPHX2"
type: "gene"
col: 4237
ensembl_id: "ENSG00000120915"
name: "epoxide hydrolase 2"
location: "8p21.2-p21.1"
module: 45
arm: "+"
pooled_cpm: 7.04
n_lines_expressing: 40
n_dd_up: 27
n_dd_down: 29
n_dd_up_clean: 20
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# EPHX2

*epoxide hydrolase 2* — 8p21.2-p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +7.6, q 1e-11, up in 19 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -15.5, q 0e+00, down in 29 of 32 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.321× (z -14.7, q 0e+00, down in 29 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PECR]] (+0.60, fdr 1e-05), [[PREPL]] (+0.59, fdr 1e-05), [[PRSS16]] (+0.58, fdr 1e-05); moves opposite to [[CLCF1]] (-0.57, fdr 2e-05), [[CRK]] (-0.57, fdr 1e-05), [[RASAL2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CMBL]] → it (grade B ⚠); 3 go from it, the strongest it → [[CLCF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.6 | 1e-11 | 19/36 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.2 | 2e-10 | 6/13 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.5 | 1e-08 | 11/26 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 7e-05 | 12/36 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.30×** | +4.9 | 1e-04 | 14/36 (A498, RKO, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.8 | 2e-04 | 13/37 (KATO III, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 2e-04 | 12/36 (LS 180, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.6 | 3e-04 | 11/35 (LS 180, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.6 | 3e-04 | 5/16 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.3 | 9e-04 | 13/33 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.006 | 9/36 (KATO III, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.006 | 10/36 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.006 | 14/36 (LS 180, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.008 | 8/36 (SW480, LS 180, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 9/36 (AsPC-1, LS 180, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.008 | 8/33 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 7/36 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.020 | 12/36 (KATO III, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.023 | 10/36 (AsPC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.430×** | -15.5 | 0e+00 | 29/32 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.321×** | -14.7 | 0e+00 | 29/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.361×** | -13.2 | 2e-37 | 30/36 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -9.1 | 2e-17 | 21/32 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.500×** | -9.0 | 3e-17 | 24/36 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.503×** | -8.9 | 6e-17 | 23/36 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.513×** | -8.3 | 9e-15 | 22/35 (SW480, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -7.1 | 1e-10 | 19/35 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.601×** | -6.3 | 2e-08 | 18/30 (NCI-H23, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -6.3 | 2e-08 | 19/36 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.727×** | -5.8 | 3e-07 | 17/36 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.407×** | -5.7 | 5e-07 | 15/31 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -5.3 | 4e-06 | 18/36 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.667×** | -5.2 | 7e-06 | 16/35 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.669×** | -4.9 | 4e-05 | 12/35 (AN3 CA, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.707×** | -4.5 | 2e-04 | 17/34 (A-427, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.732×** | -4.0 | 0.002 | 10/36 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.002 | 11/36 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.004 | 13/37 (SW480, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -3.7 | 0.005 | 13/34 (RKO, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.89 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -15.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -14.5) |
| [[SW480 (line)]] | alt | 13.2 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -17.4) |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -8.9) |
| [[A549 (line)]] | wt | 13.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -11.1) |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.237× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.52 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 4.43 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -9.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -8.8) |
| [[KATO III (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1573 (line)]] | alt | 4.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 7.05 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0746× (z -9.4) |
| [[A-172 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.783 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PECR]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM; STRING 439 |
| [[PREPL]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PRSS16]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[KCNK15-AS1]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC18B1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.54 | +0.49 / +0.60 | both halves | 1e-05 | pathway: Fatty acid metabolism |
| [[RHOXF1]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[USP30]] | +0.54 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[C20orf96]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ZNF594-DT]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TM7SF3]] | +0.53 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[MAP2K6]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCF1]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CRK]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RASAL2]] | -0.54 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[TUBB6]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[C11orf91]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RAB35]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[BACH1]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[S100A11]] | -0.50 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[UCKL1-AS1]] | -0.50 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[IQCJ-SCHIP1]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[STK10]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SCHIP1]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMBL]] | B | CMBL activity raises EPHX2's level | lines that do not express CMBL (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without CMBL | 0.013 | ⚠ within organs, on part of the lines; also absent: C2orf72 |
| [[MAP2K1]] | B | MAP2K1 activity lowers EPHX2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | EPHX2 activity raises CLCF1's level | lines that do not express EPHX2 (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without EPHX2 | 0.010 | ⚠ within organs, on part of the lines; also absent: MELTF, OPLAH, SEPTIN9-DT |
| [[LPIN3]] | B | EPHX2 activity raises LPIN3's level | lines that do not express EPHX2 (10) vs lines expressing it (40) | 3.17× lower at baseline in the lines without EPHX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: MELTF, OPLAH, SEPTIN9-DT |
| [[S100A11]] | B | EPHX2 activity raises S100A11's level | lines that do not express EPHX2 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without EPHX2 | 0.081 | ⚠ within organs, on part of the lines; also absent: MELTF, OPLAH, SEPTIN9-DT |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.8, 32.9); signed map (-25.0, -6.5). **Vector** length 61.8, 11.3% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +2.1 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.6 | -15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -9.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.2 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | epoxide hydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2-p21.1 — chr8:27,490,781-27,545,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ABHD20, sEH |
| Gene groups (HGNC) | Abhydrolase domain containing; HAD Asp-based non-protein phosphatases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ADIPOGENESIS |
| Reactome | 9 pathways, smallest: Biosynthesis of maresins; Synthesis of epoxy (EET) and dihydroxyeicosatrienoic acids (DHET); Biosynthesis of DHA-derived SPMs |
| Matched by | ensembl_id |

**Function**, from UniProt [P34913](https://www.uniprot.org/uniprotkb/P34913) (Bifunctional epoxide hydrolase 2):

> Bifunctional enzyme. The C-terminal domain has epoxide hydrolase activity and acts on epoxides (alkene oxides, oxiranes) and arene oxides. Plays a role in xenobiotic metabolism by degrading potentially toxic epoxides (By similarity). Also determines steady-state levels of physiological mediators.; Bifunctional enzyme. The N-terminal domain has lipid phosphatase activity, with the highest activity towards threo-9,10-phosphonooxy-hydroxy-octadecanoic acid, followed by …

**Summary**, from NCBI Gene [2053](https://www.ncbi.nlm.nih.gov/gene/2053):

> This gene encodes a member of the epoxide hydrolase family. The protein, found in both the cytosol and peroxisomes, binds to specific epoxides and converts them to the corresponding dihydrodiols. Mutations in this gene have been associated with familial hypercholesterolemia. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:3402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3402) · Entrez [2053](https://www.ncbi.nlm.nih.gov/gene/2053) · UniProt [P34913](https://www.uniprot.org/uniprotkb/P34913) · Ensembl [ENSG00000120915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120915)

## Data

Gene col 4237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4237); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4237]; `tensor/DDL_lfc|DDL_z.npy` [4237]; `embed/gene_vectors.npy` [4237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4237 or target_col == 4237). Every well: [[EPHX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
