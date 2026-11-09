---
symbol: "LDLRAD3"
type: "gene"
col: 11013
ensembl_id: "ENSG00000179241"
name: "low density lipoprotein receptor class A domain containing 3"
location: "11p13"
module: 18
arm: "+"
pooled_cpm: 81.68
n_lines_expressing: 43
n_dd_up: 34
n_dd_down: 13
n_dd_up_clean: 26
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 8
direction_downstream: 17
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# LDLRAD3

*low density lipoprotein receptor class A domain containing 3* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 1.90× (z +11.8, q 1e-29, up in 26 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -14.7, q 0e+00, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMSS1]] (+0.71, fdr 7e-06), [[USP31]] (+0.70, fdr 7e-06), [[RCL1]] (+0.69, fdr 7e-06); moves opposite to [[SYNRG]] (-0.58, fdr 1e-05), [[CDKN1B]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FAM78B]] → it (grade B ⚠); 17 go from it, the strongest it → [[ANKS6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.90×** | +11.8 | 1e-29 | 26/41 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.81×** | +10.9 | 4e-25 | 30/41 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.79×** | +10.7 | 2e-24 | 30/40 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.77×** | +10.5 | 2e-23 | 27/40 (HOP62, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.73×** | +10.1 | 6e-22 | 29/41 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.73×** | +10.1 | 6e-22 | 25/41 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.61×** | +8.8 | 1e-16 | 27/41 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.55×** | +8.1 | 4e-14 | 23/41 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.60×** | +8.0 | 1e-13 | 24/40 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.53×** | +7.8 | 2e-13 | 24/41 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.54×** | +7.7 | 9e-13 | 24/41 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.52×** | +7.6 | 1e-12 | 27/41 (A498, SNU-423, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +7.3 | 2e-11 | 23/41 (AsPC-1, H4, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +7.0 | 9e-11 | 25/41 (AsPC-1, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.7 | 7e-10 | 28/41 (SW480, LoVo, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.42×** | +6.5 | 3e-09 | 25/41 (A498, Panc 03.27, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.28×** | +6.4 | 4e-09 | 24/41 (A498, Panc 03.27, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11013.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -14.7 | 0e+00 | 28/42 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.601×** | -13.2 | 4e-37 | 26/41 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -11.3 | 3e-27 | 32/42 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -8.0 | 1e-13 | 24/43 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -7.9 | 3e-13 | 24/40 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.691×** | -6.6 | 4e-09 | 23/41 (PANC-1, SW48, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.707×** | -6.4 | 1e-08 | 25/39 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.778×** | -4.7 | 2e-04 | 20/41 (A-427, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.795×** | -4.0 | 0.005 | 20/37 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.9 | 0.007 | 19/41 (J82, RKO, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.800×** | -3.7 | 0.012 | 21/41 (AN3 CA, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.812×** | -3.4 | 0.027 | 14/42 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.027 | 16/42 (RKO, SW1417, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.712×** | -3.3 | 0.040 | 18/40 (RKO, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.6 | 18 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 5.05× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 59.1 | 18 (3 ⚠) | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 6.14× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 54.0 | 18 | 0 | [[Budesonide (drug)]] 5 µM 5.43× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 153 | 8 | 10 (7 ⚠) | [[Budesonide (drug)]] 5 µM 2.24× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -27.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -22.2) |
| [[SNU-423 (line)]] | alt | 65.5 | 17 | 1 | [[Budesonide (drug)]] 0.5 µM 5.73× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.8) |
| [[HOP62 (line)]] | alt | 58.4 | 17 | 0 | [[Dexamethasone (drug)]] 0.5 µM 5.58× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 69.8 | 16 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.99× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 39.7 | 13 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 4.83× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 160 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.9) |
| [[Hs 766T (line)]] | wt | 37.9 | 13 | 0 | [[Budesonide (drug)]] 5 µM 6.93× (z +12.6) | — |
| [[A-172 (line)]] | wt | 62.5 | 11 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.92× (z +11.0) | — |
| [[C32 (line)]] | wt | 277 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -23.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -18.2) |
| [[A549 (line)]] | wt | 107 | 8 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.97× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 30.0 | 9 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 5.59× (z +10.3) | — |
| [[SW48 (line)]] | wt | 152 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -19.0) |
| [[C-33 A (line)]] | alt | 194 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 97.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -18.8) |
| [[SNU-1 (line)]] | wt | 144 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.659× (z -15.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 69.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -20.2) |
| [[SW1417 (line)]] | alt | 72.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.7) |
| [[A-427 (line)]] | wt | 77.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -32.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 60.7 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.19× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -9.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.411× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 83.3 | 2 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.78× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.420× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 277 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.6) |
| [[SW480 (line)]] | alt | 96.9 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.76× (z +9.1) | [[TAK-901 (drug)]] 5 µM 0.174× (z -10.7) |
| [[AN3 CA (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -19.2) |
| [[BT-474 (line)]] | alt | 88.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.01× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0685× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[H4 (line)]] | wt | 54.5 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.12× (z +9.4) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.21× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -9.3) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H1573 (line)]] | alt | 23.9 | 1 | 0 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 3.84× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMSS1]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[USP31]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[RCL1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | same gene group |
| [[TSEN2]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MDN1]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LETM1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TBC1D16]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PXYLP1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GART]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[UCK2]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 | same gene group |
| [[TCOF1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[DKC1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNRG]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM78B]] | B | FAM78B activity raises LDLRAD3's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.10× lower at baseline in the lines without FAM78B | 0.012 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[NT5M]] | B | NT5M activity raises LDLRAD3's level | lines that do not express NT5M (7) vs lines expressing it (43) | 3.42× lower at baseline in the lines without NT5M | 0.034 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[STEAP3]] | B | STEAP3 activity raises LDLRAD3's level | lines that do not express STEAP3 (6) vs lines expressing it (44) | 2.87× lower at baseline in the lines without STEAP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: GPR155; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises LDLRAD3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[PRR5L]] | B | PRR5L activity raises LDLRAD3's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 2.81× lower at baseline in the lines without PRR5L | 0.076 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises LDLRAD3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MTHFD1L]], [[USP31]] | C | MTHFD1L, USP31 activity raises LDLRAD3's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 3.40× lower at baseline in the lines without MTHFD1L, USP31 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; co-absent genes |
| [[SLC26A2]] | C | SLC26A2 activity raises LDLRAD3's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without SLC26A2 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKS6]] | B | LDLRAD3 activity raises ANKS6's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.85× lower at baseline in the lines without LDLRAD3 | 0.011 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TSEN2]] | B | LDLRAD3 activity raises TSEN2's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.94× lower at baseline in the lines without LDLRAD3 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DDX31]] | B | LDLRAD3 activity raises DDX31's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without LDLRAD3 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NT5M]] | B | LDLRAD3 activity raises NT5M's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.62× lower at baseline in the lines without LDLRAD3 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[OSBPL5]] | B | LDLRAD3 activity raises OSBPL5's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without LDLRAD3 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[STEAP3]] | B | LDLRAD3 activity raises STEAP3's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.65× lower at baseline in the lines without LDLRAD3 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FAM78B]] | B | LDLRAD3 activity raises FAM78B's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 3.13× lower at baseline in the lines without LDLRAD3 | 0.042 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TANGO6]] | B | LDLRAD3 activity raises TANGO6's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without LDLRAD3 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CTIF]] | B | LDLRAD3 activity raises CTIF's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without LDLRAD3 | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC26A2]] | B | LDLRAD3 activity raises SLC26A2's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without LDLRAD3 | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PINX1]] | B | LDLRAD3 activity raises PINX1's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without LDLRAD3 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NBPF20]] | B | LDLRAD3 activity raises NBPF20's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without LDLRAD3 | 0.078 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (31.9, 10.5); signed map (-3.9, -54.0). **Vector** length 157, 54.9% of its response variance represented; |z| ≥ 3 in 1,581 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +8.3 | +10.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +7.6 | +10.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +7.6 | +10.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +7.3 | +8.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +7.1 | +10.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -11.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.9 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -3.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.9 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | low density lipoprotein receptor class A domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:35,943,981-36,232,136 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRAD3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YD5](https://www.uniprot.org/uniprotkb/Q86YD5) (Low-density lipoprotein receptor class A domain-containing protein 3):

> May influence APP processing, resulting in a decrease in sAPP-alpha production and increased amyloidogenic P3 peptide production. May regulate ITCH and NEDD4 E3 ligase activity and degradation.; (Microbial infection) Acts as a receptor for Venezuelan equine encephalitis virus.

**Summary**, from NCBI Gene [143458](https://www.ncbi.nlm.nih.gov/gene/143458):

> Predicted to enable amyloid-beta binding activity. Predicted to be involved in receptor-mediated endocytosis. Predicted to act upstream of or within regulation of protein processing. Predicted to be located in endomembrane system and membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27046) · Entrez [143458](https://www.ncbi.nlm.nih.gov/gene/143458) · UniProt [Q86YD5](https://www.uniprot.org/uniprotkb/Q86YD5) · Ensembl [ENSG00000179241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179241)

## Data

Gene col 11013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11013); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11013]; `tensor/DDL_lfc|DDL_z.npy` [11013]; `embed/gene_vectors.npy` [11013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11013 or target_col == 11013). Every well: [[LDLRAD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDLRAD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
