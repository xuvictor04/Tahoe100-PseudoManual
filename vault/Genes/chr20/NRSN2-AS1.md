---
symbol: "NRSN2-AS1"
type: "gene"
col: 13453
ensembl_id: "ENSG00000225377"
name: "NRSN2 antisense RNA 1"
location: "20p13"
module: 133
arm: "+"
pooled_cpm: 19.38
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# NRSN2-AS1

*NRSN2 antisense RNA 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +13.8, q 1e-40, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.271× (z -17.1, q 0e+00, down in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.499× (z -9.5, q 2e-19, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBR2]] (+0.77, fdr 7e-06), [[ZNF460-AS1]] (+0.75, fdr 8e-06), [[PGLS-DT]] (+0.73, fdr 7e-06); moves opposite to [[THEM6]] (-0.65, fdr 2e-05), [[PDHB]] (-0.61, fdr 2e-05), [[HLTF]] (-0.59, fdr 3e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +13.8 | 1e-40 | 42/47 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +5.2 | 6e-05 | 26/48 (BT-474, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.27×** | +4.7 | 6e-04 | 20/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.002 | 20/47 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 21/48 (SW480, J82, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.32×** | +3.8 | 0.013 | 13/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +3.8 | 0.013 | 16/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.019 | 20/47 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.019 | 13/47 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.019 | 13/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.042 | 12/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.068 | 12/48 (J82, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.068 | 15/47 (SW480, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.18× | +3.1 | 0.068 | 15/48 (BT-474, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.25×** | +3.0 | 0.097 | 12/48 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.271×** | -17.1 | 0e+00 | 46/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.439×** | -15.8 | 0e+00 | 38/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.390×** | -12.8 | 3e-35 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.396×** | -12.6 | 3e-34 | 46/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.421×** | -11.8 | 7e-30 | 42/48 (COLO 205, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.455×** | -10.7 | 8e-25 | 42/47 (hTERT-HPNE, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.489×** | -9.7 | 2e-20 | 40/47 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.499×** | -9.5 | 2e-19 | 27/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.520×** | -8.9 | 4e-17 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -8.5 | 1e-15 | 31/47 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.312×** | -8.3 | 6e-15 | 38/46 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.317×** | -8.2 | 1e-14 | 40/48 (PANC-1, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -6.2 | 3e-08 | 32/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.632×** | -6.0 | 8e-08 | 24/45 (RPMI-7951, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -5.7 | 5e-07 | 22/47 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.730×** | -4.0 | 0.002 | 17/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.021 | 15/48 (SW 1271, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.3 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -22.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 22.3 | 1 | 10 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.7) | [[Harringtonine (drug)]] 0.5 µM 0.175× (z -15.3) |
| [[COLO 205 (line)]] | alt | 55.3 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -12.1) |
| [[SW480 (line)]] | alt | 21.3 | 1 | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.9) | [[Harringtonine (drug)]] 5 µM 0.177× (z -15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.368× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.155× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -10.4) |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 25.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -13.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -9.2) |
| [[HOP62 (line)]] | alt | 23.2 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 31.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -17.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A549 (line)]] | wt | 26.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -21.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -11.0) |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0844× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -8.5) |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0444× (z -15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.127× (z -10.7) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -14.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.273× (z -9.0) |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -8.6) |
| [[LoVo (line)]] | wt | 19.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 12.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.222× (z -9.0) |
| [[BT-474 (line)]] | alt | 20.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 3.33× (z +9.5) ⚠ cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LOX-IMVI (line)]] | wt | 14.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.122× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0777× (z -11.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.1) | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -10.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBR2]] | +0.77 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | +0.75 | +0.58 / +0.69 | both halves | 8e-06 | same gene group |
| [[PGLS-DT]] | +0.73 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.69 | +0.48 / +0.61 | both halves | 2e-05 | same gene group |
| [[GARS1-DT]] | +0.69 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RAB4B]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.67 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[BCL2L2-PABPN1]] | +0.67 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CCNO-DT]] | +0.65 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[SPAG7]] | +0.64 | +0.40 / +0.65 | both halves | 4e-05 |  |
| [[DMGDH]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[VLDLR-AS1]] | +0.63 | +0.43 / +0.61 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.65 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PDHB]] | -0.61 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[HLTF]] | -0.59 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PHF6]] | -0.58 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[COG2]] | -0.56 | -0.26 / -0.54 | both halves | 4e-04 |  |
| [[ARHGAP18]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZNF445]] | -0.55 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[NDFIP2]] | -0.55 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[MPHOSPH6]] | -0.54 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers NRSN2-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[NUPR1]] | B | NUPR1 activity raises NRSN2-AS1's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.40× lower at baseline in the lines without NUPR1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.2, 23.0); signed map (2.4, 0.6). **Vector** length 81.8, 18.9% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +13.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.0 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.8 | -12.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.7 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -17.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.2 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -4.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NRSN2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p13 — chr20:316,860-348,490 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51222) · Entrez [100507459](https://www.ncbi.nlm.nih.gov/gene/100507459) · Ensembl [ENSG00000225377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225377)

## Data

Gene col 13453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13453); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13453]; `tensor/DDL_lfc|DDL_z.npy` [13453]; `embed/gene_vectors.npy` [13453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13453 or target_col == 13453). Every well: [[NRSN2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRSN2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
