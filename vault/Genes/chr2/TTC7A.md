---
symbol: "TTC7A"
type: "gene"
col: 898
ensembl_id: "ENSG00000068724"
name: "tetratricopeptide repeat domain 7A"
location: "2p21"
module: 2
arm: "+"
pooled_cpm: 55.24
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TTC7A

*tetratricopeptide repeat domain 7A* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.58× (z +9.7, q 3e-19, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.600× (z -10.7, q 6e-24, down in 34 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.414× (z -9.7, q 1e-19, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERGIC1]] (+0.52, fdr 3e-05), [[MAP3K3]] (+0.51, fdr 3e-05), [[ADCY9]] (+0.50, fdr 3e-05); moves opposite to [[ZNF300]] (-0.51, fdr 4e-05), [[LPAR6]] (-0.50, fdr 6e-05), [[CHIC1]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZSCAN12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +9.7 | 3e-19 | 38/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +8.5 | 4e-15 | 38/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.8 | 9e-13 | 31/48 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +7.8 | 9e-13 | 35/48 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.6 | 3e-12 | 32/48 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +6.4 | 2e-08 | 24/48 (SW480, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 9e-07 | 24/48 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.5 | 3e-06 | 24/48 (LS 180, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 6e-06 | 22/48 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +5.2 | 1e-05 | 24/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +4.4 | 5e-04 | 14/49 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.9 | 0.004 | 14/48 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.010 | 15/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +3.6 | 0.014 | 15/49 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.6 | 0.014 | 9/48 (COLO 205, HCT15, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.6 | 0.014 | 11/48 (NCI-H460, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.026 | 11/48 (A498, AsPC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -10.7 | 6e-24 | 34/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -9.7 | 1e-19 | 35/49 (A-172, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.632×** | -9.3 | 4e-18 | 30/48 (AsPC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.675×** | -8.3 | 2e-14 | 29/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.759×** | -8.2 | 4e-14 | 23/47 (AsPC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -8.0 | 9e-14 | 28/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.764×** | -8.0 | 1e-13 | 29/48 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -7.3 | 2e-11 | 29/48 (hTERT-HPNE, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.579×** | -6.0 | 1e-07 | 25/47 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.762×** | -5.5 | 2e-06 | 23/47 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -5.2 | 1e-05 | 26/48 (A-172, SW 1271, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.774×** | -5.1 | 2e-05 | 22/48 (NCI-H2030, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -4.8 | 8e-05 | 22/48 (hTERT-HPNE, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.812×** | -4.4 | 5e-04 | 21/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.813×** | -4.3 | 5e-04 | 19/48 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.694×** | -4.0 | 0.002 | 18/48 (HS-578T, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.850× | -3.4 | 0.016 | 11/48 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.851× | -3.4 | 0.017 | 14/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.854× | -3.2 | 0.032 | 8/49 (BT-474, A549, …) | top dose only | plate-row cell shift |
| [[Docetaxel (drug)]] 5 µM |  | 0.908× | -2.8 | 0.091 | 11/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.865× | -2.8 | 0.099 | 15/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 128 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.221× (z -9.3) |
| [[A498 (line)]] | wt | 133 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -17.3) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.388× (z -13.1) |
| [[PANC-1 (line)]] | alt | 25.6 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 96.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.8) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.553× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 77.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.8) ⚠ cell-cycle shift, explains ~92% of this change |
| [[J82 (line)]] | alt | 66.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.526× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 25.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.0) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.34× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -10.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -12.0) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HOP62 (line)]] | alt | 59.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.1) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HS-578T (line)]] | alt | 83.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.527× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 42.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.316× (z -11.1) |
| [[RKO (line)]] | wt | 24.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.0) ⚠ cell-cycle shift, explains ~17% of this change | [[Harringtonine (drug)]] 5 µM 0.206× (z -10.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.2) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A-427 (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.436× (z -9.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 92.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.362× (z -9.3) |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0824× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.256× (z -8.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0981× (z -8.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LoVo (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.8) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[NCI-H1573 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.392× (z -8.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2347 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0996× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 1271 (line)]] | alt | 94.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0812× (z -10.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 45.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +11.1) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[MAP3K3]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[ADCY9]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[SRD5A1]] | +0.49 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[LPCAT1]] | +0.49 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[PCMT1]] | +0.49 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[CCM2]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[TMEM184B]] | +0.48 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[SLC27A4]] | +0.48 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[CDR2L]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[DCUN1D2]] | +0.47 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[CORO2A]] | +0.47 | +0.36 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF300]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[LPAR6]] | -0.50 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[CHIC1]] | -0.49 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[FMO4]] | -0.47 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[ZSCAN12]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ZNF780A]] | -0.45 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[AFG1L]] | -0.44 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[TRPM8]] | -0.43 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[HMG20A]] | -0.43 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[LYRM2]] | -0.43 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[KRR1]] | -0.43 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.42 | -0.16 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[POLR2M]] | -0.42 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN12 activity raises TTC7A's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.44× lower at baseline in the lines without ZSCAN12 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.353). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.6, 2.0); signed map (-43.7, -1.2). **Vector** length 99.0, 25.9% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -2.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.2 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +7.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.9 | -8.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -5.1 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -5.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,915,869-47,076,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1140; previously TTC7 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; PI4KA lipid kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULT0](https://www.uniprot.org/uniprotkb/Q9ULT0) (Tetratricopeptide repeat protein 7A):

> Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane. The complex acts as a regulator of phosphatidylinositol 4-phosphate (PtdIns(4)P) synthesis (Probable). In the complex, plays a central role in bridging PI4KA to EFR3B and HYCC1, via direct interactions (By similarity).

**Summary**, from NCBI Gene [57217](https://www.ncbi.nlm.nih.gov/gene/57217):

> This gene encodes a protein containing tetratricopeptide repeats. Mutations in this gene disrupt intestinal development and can cause early onset inflammatory bowel disease and intestinal atresia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:19750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19750) · Entrez [57217](https://www.ncbi.nlm.nih.gov/gene/57217) · UniProt [Q9ULT0](https://www.uniprot.org/uniprotkb/Q9ULT0) · Ensembl [ENSG00000068724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068724)

## Data

Gene col 898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 898); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 898]; `tensor/DDL_lfc|DDL_z.npy` [898]; `embed/gene_vectors.npy` [898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 898 or target_col == 898). Every well: [[TTC7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
