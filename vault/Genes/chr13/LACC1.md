---
symbol: "LACC1"
type: "gene"
col: 11049
ensembl_id: "ENSG00000179630"
name: "laccase domain multifunctional purine nucleosidase 1"
location: "13q14.11"
module: 68
arm: "+"
pooled_cpm: 13.6
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 20
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# LACC1

*laccase domain multifunctional purine nucleosidase 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +22.5, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.501× (z -10.2, q 9e-22, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF641]] (+0.75, fdr 7e-06), [[CCDC90B]] (+0.71, fdr 7e-06), [[LPXN]] (+0.71, fdr 1e-05); moves opposite to [[ATRN]] (-0.66, fdr 2e-05), [[SLC9A6]] (-0.65, fdr 6e-05), [[SDHAP1]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[C21orf91]] → it (grade B ⚠); 20 go from it, the strongest it → [[MAZ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.93×** | +22.5 | 0e+00 | 37/42 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.16×** | +16.3 | 0e+00 | 38/41 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +11.3 | 2e-27 | 34/38 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.4 | 2e-11 | 25/41 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +6.6 | 6e-09 | 26/41 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +5.4 | 8e-06 | 19/41 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 19/40 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.9 | 5e-05 | 14/40 (A-172, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.8 | 1e-04 | 17/42 (A498, A549, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +4.6 | 3e-04 | 15/41 (LS 180, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +4.6 | 3e-04 | 19/40 (LoVo, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 20/42 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 5e-04 | 15/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.3 | 6e-04 | 13/27 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +4.1 | 0.002 | 16/40 (NCI-H460, C32, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.011 | 12/41 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.015 | 4/41 (A-427, A-172, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.048 | 5/41 (C32, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.501×** | -10.2 | 9e-22 | 24/41 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.565×** | -8.4 | 7e-15 | 23/41 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.336×** | -8.4 | 7e-15 | 28/40 (RKO, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -7.7 | 2e-12 | 24/41 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -6.6 | 5e-09 | 22/41 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -6.6 | 5e-09 | 22/41 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -6.5 | 6e-09 | 26/39 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -6.1 | 7e-08 | 23/41 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.720×** | -4.9 | 7e-05 | 20/40 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[NG25 (drug)]] 5 µM |  | **0.535×** | -4.8 | 8e-05 | 19/38 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -4.3 | 1e-03 | 18/40 (COLO 205, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -4.1 | 0.002 | 12/41 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.9 | 0.005 | 4/42 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.064 | 10/41 (H4, RKO, …) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -3.1 | 0.084 | 9/41 (H4, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +13.2) | [[Digitoxin (drug)]] 0.05 µM 0.297× (z -9.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[C32 (line)]] | wt | 11.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +12.5) | — |
| [[LoVo (line)]] | wt | 17.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.201× (z -11.8) |
| [[SW480 (line)]] | alt | 20.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.222× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -10.8) |
| [[A498 (line)]] | wt | 10.3 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 59.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 6.95 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 10.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.9) | [[Digitoxin (drug)]] 0.5 µM 0.198× (z -12.1) |
| [[A549 (line)]] | wt | 19.0 | 1 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.217× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 10.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.0756× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.209× (z -10.0) |
| [[HOP62 (line)]] | alt | 6.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +16.1) | — |
| [[J82 (line)]] | alt | 24.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 16.7 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +10.6) | — |
| [[A-172 (line)]] | wt | 7.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 7.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.9) | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0900× (z -8.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0921× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~90% of this change |
| [[RKO (line)]] | wt | 23.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -8.9) |
| [[SW 900 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.4) | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF641]] | +0.75 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[CCDC90B]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[LPXN]] | +0.71 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[SDSL]] | +0.69 | +0.76 / +0.50 | both halves | 1e-05 | same gene group |
| [[PBDC1]] | +0.69 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.68 | +0.76 / +0.41 | both halves | 4e-05 |  |
| [[OGFRL1]] | +0.68 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[C21orf91]] | +0.68 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[XPC]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[TRIP6]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[CCDC122]] | +0.67 | +0.69 / +0.45 | both halves | 3e-05 | STRING 949; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TAF9]] | +0.67 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[GYG1]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRN]] | -0.66 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[SLC9A6]] | -0.65 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[SDHAP1]] | -0.63 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[GLG1]] | -0.63 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[SAP130]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TYW1]] | -0.62 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[NUP160]] | -0.61 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[TUFM]] | -0.61 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[ANKRD27]] | -0.61 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[KIAA2013]] | -0.61 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[GLRX5]] | -0.61 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[RAB40B]] | -0.61 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91]] | B | C21orf91 activity raises LACC1's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 2.71× lower at baseline in the lines without C21orf91 | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[TOP2A]] | B | TOP2A activity lowers LACC1's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02966]] | B | LINC02966 activity raises LACC1's level | lines that do not express LINC02966 (14) vs lines expressing it (36) | 2.10× lower at baseline in the lines without LINC02966 | 0.025 | ⚠ within organs, on part of the lines; also absent: JPH2, DNAH5, CCL20; maybe low, not absent |
| [[ABCA10]] | B | ABCA10 activity raises LACC1's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without ABCA10 | 0.058 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises LACC1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without ZNF341-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[PMAIP1]] | C | PMAIP1 activity raises LACC1's level | lines that do not express PMAIP1 (4) vs lines expressing it (46) | 3.33× lower at baseline in the lines without PMAIP1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: DOCK5, STAMBPL1, PERP; maybe low, not absent |
| [[CCDC122]] | C | CCDC122 activity raises LACC1's level | lines that do not express CCDC122 (5) vs lines expressing it (45) | 5.21× lower at baseline in the lines without CCDC122 | 0.060 | ⚠ within organs, on part of the lines; also absent: LACC1, SDC4, IL1RAP; co-absent with the target; its own permutation p |
| [[ZC3H12A]] | C | ZC3H12A activity raises LACC1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 4.13× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SLFN5]] | C | SLFN5 activity raises LACC1's level | lines that do not express SLFN5 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without SLFN5 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent; co-absent with the target |
| [[CDKN1A]] | C | CDKN1A activity raises LACC1's level | lines that do not express CDKN1A (3) vs lines expressing it (47) | 3.15× lower at baseline in the lines without CDKN1A | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 17, C 3. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAZ]] | B | LACC1 activity lowers MAZ's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.66× higher at baseline in the lines without LACC1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[PPP1R15A]] | B | LACC1 activity raises PPP1R15A's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without LACC1 | 0.021 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[RFFL]] | B | LACC1 activity raises RFFL's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without LACC1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[MOB3C]] | B | LACC1 activity raises MOB3C's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without LACC1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[ZNF341-AS1]] | B | LACC1 activity raises ZNF341-AS1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without LACC1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[KRCC1]] | B | LACC1 activity raises KRCC1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.67× lower at baseline in the lines without LACC1 | 0.035 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[PPIH]] | B | LACC1 activity lowers PPIH's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without LACC1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[CTXN1]] | B | LACC1 activity lowers CTXN1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 2.34× higher at baseline in the lines without LACC1 | 0.039 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[KHNYN]] | B | LACC1 activity raises KHNYN's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.40× lower at baseline in the lines without LACC1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[TYW1]] | B | LACC1 activity lowers TYW1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.36× higher at baseline in the lines without LACC1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | LACC1 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express LACC1 (6) vs lines expressing it (42) | the lines without LACC1: 0.74× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[TEP1]] | B | LACC1 activity raises TEP1's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without LACC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (12.2, 10.4); signed map (19.5, -16.3). **Vector** length 110, 26.4% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +22.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.1 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.0 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -10.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | laccase domain multifunctional purine nucleosidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:43,879,284-43,893,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38725, FAMIN; previously C13orf31 |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV20](https://www.uniprot.org/uniprotkb/Q8IV20) (Purine nucleoside phosphorylase LACC1):

> Purine nucleoside enzyme that catalyzes the phosphorolysis of adenosine, guanosine and inosine nucleosides, yielding D-ribose 1-phosphate and the respective free bases, adenine, guanine and hypoxanthine. Also catalyzes the phosphorolysis of S-methyl-5'-thioadenosine into adenine and S-methyl-5-thio-alpha-D-ribose 1-phosphate. Also has adenosine deaminase activity. Acts as a regulator of innate immunity in macrophages by modulating the purine nucleotide metabolism, thereby regulating the …

**Summary**, from NCBI Gene [144811](https://www.ncbi.nlm.nih.gov/gene/144811):

> This gene encodes an oxidoreductase that promotes fatty-acid oxidation, with concomitant inflammasome activation, mitochondrial and NADPH-oxidase-dependent reactive oxygen species production, and bactericidal activity of macrophages. The encoded protein forms a complex with fatty acid synthase on peroxisomes and is thought to be modulated by peroxisome proliferator-activated receptor signaling events. Naturally occurring mutations in this gene are associated with inflammatory bowel disease, …

**Accessions** — [HGNC:26789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26789) · Entrez [144811](https://www.ncbi.nlm.nih.gov/gene/144811) · UniProt [Q8IV20](https://www.uniprot.org/uniprotkb/Q8IV20) · Ensembl [ENSG00000179630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179630)

## Data

Gene col 11049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11049); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11049]; `tensor/DDL_lfc|DDL_z.npy` [11049]; `embed/gene_vectors.npy` [11049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11049 or target_col == 11049). Every well: [[LACC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LACC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
