---
symbol: "PRKAG2"
type: "gene"
col: 2785
ensembl_id: "ENSG00000106617"
name: "protein kinase AMP-activated non-catalytic subunit gamma 2"
location: "7q36.1"
module: 113
arm: "+"
pooled_cpm: 77.93
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# PRKAG2

*protein kinase AMP-activated non-catalytic subunit gamma 2* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +8.5, q 1e-14, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.501× (z -13.6, q 1e-39, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLVCR2]] (+0.60, fdr 1e-05), [[FADS3]] (+0.58, fdr 1e-05), [[ERGIC1]] (+0.54, fdr 3e-05); moves opposite to [[MSS51]] (-0.52, fdr 9e-05), [[MORN1]] (-0.47, fdr 4e-05), [[EFCAB6]] (-0.43, fdr 1e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +8.5 | 1e-14 | 24/43 (HT-29, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.4 | 6e-08 | 22/43 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.36×** | +6.2 | 9e-08 | 27/44 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +5.9 | 4e-07 | 23/43 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +5.5 | 4e-06 | 20/44 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.8 | 1e-04 | 15/43 (RKO, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 5e-04 | 18/43 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.004 | 17/43 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +4.0 | 0.004 | 14/43 (HT-29, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 16/43 (SNU-423, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.006 | 15/43 (HOP62, A498, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.010 | 17/43 (HOP62, A498, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.010 | 16/43 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.011 | 15/43 (HOP62, A498, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.5 | 0.017 | 18/43 (HOP62, A498, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.017 | 17/43 (SNU-423, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.5 | 0.017 | 11/44 (J82, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.501×** | -13.6 | 1e-39 | 36/43 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -13.2 | 3e-37 | 31/44 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -11.3 | 2e-27 | 34/45 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.586×** | -11.0 | 8e-26 | 29/43 (NCI-H460, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.607×** | -9.5 | 3e-19 | 28/39 (A-427, SNU-1, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.732×** | -9.1 | 1e-17 | 26/43 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.635×** | -9.0 | 2e-17 | 23/38 (AsPC-1, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.754×** | -5.8 | 4e-07 | 24/44 (C32, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.757×** | -5.7 | 6e-07 | 26/43 (NCI-H2030, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.808×** | -4.2 | 0.001 | 21/42 (SNU-1, AsPC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.876× | -3.9 | 0.006 | 13/43 (NCI-H23, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.849× | -3.4 | 0.029 | 17/43 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.029 | 17/43 (SW48, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.891× | -3.4 | 0.029 | 3/43 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.731×** | -3.4 | 0.029 | 14/43 (HCT15, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.854× | -3.3 | 0.039 | 13/43 (A-172, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 172 | 2 (2 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -22.7) |
| [[A498 (line)]] | wt | 237 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 157 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -26.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -16.4) |
| [[HOP62 (line)]] | alt | 61.7 | 5 | 3 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.64× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.453× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 101 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -19.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -10.5) |
| [[SW48 (line)]] | wt | 152 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.9) |
| [[A-172 (line)]] | wt | 262 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.1) |
| [[A549 (line)]] | wt | 122 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.9) |
| [[LoVo (line)]] | wt | 91.0 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.1) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 77.8 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.19× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.7) |
| [[SNU-1 (line)]] | wt | 183 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 84.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 97.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 79.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -11.2) |
| [[RKO (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -8.7) |
| [[SW 900 (line)]] | alt | 83.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -12.6) |
| [[A-427 (line)]] | wt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 44.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 69.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.5) |
| [[HCT15 (line)]] | alt | 66.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 37.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 27.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 24.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 23.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 53.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 26.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.85× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 89.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLVCR2]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FADS3]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[RRAGD]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 | pathway: Autophagy; STRING 565 |
| [[TANC2]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC39A14]] | +0.52 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[CCDC112]] | +0.51 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[MCAM]] | +0.51 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[HRK]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[PKN1]] | +0.50 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[RETREG1]] | +0.50 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[AGTPBP1]] | +0.50 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSS51]] | -0.52 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[MORN1]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[EFCAB6]] | -0.43 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[GPATCH2]] | -0.43 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[LINC01134]] | -0.43 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[SERPINB9P1]] | -0.43 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[FANK1]] | -0.42 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[ZBED5]] | -0.42 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[MIRLET7IHG]] | -0.41 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[STRADA]] | -0.41 | -0.45 / -0.23 | both halves | 5e-04 | pathway: Energy dependent regulation of mTOR by LKB1-AMPK; STRING 739 |
| [[DDX5]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[CDKN2B-AS1]] | -0.41 | -0.39 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRKAG2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.7, 11.6); signed map (-27.5, 22.8). **Vector** length 114, 30.3% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.9 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -9.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase AMP-activated non-catalytic subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,556,124-151,877,214 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AAKG, AAKG2, H91620p, WPWS, CMH6 |
| Gene groups (HGNC) | Protein kinase AMP-activated non-catalytic subunit gamma family |
| Reactome | 36 pathways, smallest: AMPK inhibits chREBP transcriptional activation activity; Lipophagy; Activation of PPARGC1A (PGC-1alpha) by phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGJ0](https://www.uniprot.org/uniprotkb/Q9UGJ0) (5'-AMP-activated protein kinase subunit gamma-2):

> AMP/ATP-binding subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation …

**Summary**, from NCBI Gene [51422](https://www.ncbi.nlm.nih.gov/gene/51422):

> AMP-activated protein kinase (AMPK) is a heterotrimeric protein composed of a catalytic alpha subunit, a noncatalytic beta subunit, and a noncatalytic regulatory gamma subunit. Various forms of each of these subunits exist, encoded by different genes. AMPK is an important energy-sensing enzyme that monitors cellular energy status and functions by inactivating key enzymes involved in regulating de novo biosynthesis of fatty acid and cholesterol. This gene is a member of the AMPK gamma subunit …

**Accessions** — [HGNC:9386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9386) · Entrez [51422](https://www.ncbi.nlm.nih.gov/gene/51422) · UniProt [Q9UGJ0](https://www.uniprot.org/uniprotkb/Q9UGJ0) · Ensembl [ENSG00000106617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106617)

## Data

Gene col 2785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2785); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2785]; `tensor/DDL_lfc|DDL_z.npy` [2785]; `embed/gene_vectors.npy` [2785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2785 or target_col == 2785). Every well: [[PRKAG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
