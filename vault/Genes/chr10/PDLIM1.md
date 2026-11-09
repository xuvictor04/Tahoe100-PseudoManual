---
symbol: "PDLIM1"
type: "gene"
col: 2851
ensembl_id: "ENSG00000107438"
name: "PDZ and LIM domain 1"
location: "10q23.33"
module: 106
arm: "+"
pooled_cpm: 48.88
n_lines_expressing: 39
n_dd_up: 29
n_dd_down: 19
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 16
direction_downstream: 21
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PDLIM1

*PDZ and LIM domain 1* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.73× (z +10.2, q 2e-21, up in 26 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 1.36× (z +6.5, q 3e-08, up in 23 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.537× (z -16.2, q 0e+00, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STOM]] (+0.70, fdr 7e-06), [[MAP2]] (+0.68, fdr 1e-05), [[B4GALT1]] (+0.67, fdr 7e-06); moves opposite to [[ANTXR2]] (-0.60, fdr 1e-05), [[TMEM158]] (-0.60, fdr 1e-05), [[PRDM8]] (-0.54, fdr 3e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PLSCR4]] → it (grade B ⚠); 21 go from it, the strongest it → [[DENND3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +10.2 | 2e-21 | 26/35 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.36×** | +6.5 | 3e-08 | 23/37 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +6.4 | 3e-08 | 25/37 (A549, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.38×** | +5.9 | 6e-07 | 20/37 (A549, H4, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-06 | 18/37 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +5.4 | 7e-06 | 23/37 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +5.3 | 1e-05 | 22/37 (A549, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 2e-05 | 19/37 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +5.0 | 3e-05 | 18/37 (CFPAC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +5.0 | 3e-05 | 16/31 (Panc 03.27, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.9 | 4e-05 | 14/29 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 4e-05 | 19/37 (A549, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +4.9 | 5e-05 | 20/36 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +4.7 | 9e-05 | 16/37 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 1e-04 | 18/37 (A549, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.30×** | +4.6 | 1e-04 | 22/37 (A549, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 3e-04 | 17/36 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 6e-04 | 15/36 (A549, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -16.2 | 0e+00 | 31/37 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -14.2 | 3e-43 | 25/37 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.597×** | -9.5 | 3e-19 | 27/37 (Hs 766T, AsPC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.615×** | -9.0 | 4e-17 | 27/37 (Hs 766T, LoVo, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -7.7 | 2e-12 | 27/36 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.683×** | -7.0 | 2e-10 | 22/37 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -6.9 | 5e-10 | 18/37 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -6.8 | 6e-10 | 22/37 (Hs 766T, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -6.4 | 1e-08 | 23/37 (Hs 766T, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -5.8 | 5e-07 | 21/35 (Hs 766T, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.745×** | -5.4 | 3e-06 | 20/37 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -5.3 | 6e-06 | 19/37 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.764×** | -4.8 | 8e-05 | 18/37 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.002 | 17/37 (LoVo, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.805×** | -4.0 | 0.002 | 15/37 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.810×** | -3.9 | 0.004 | 12/37 (NCI-H2030, A498, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.799×** | -3.8 | 0.004 | 12/35 (CFPAC-1, A-172, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.812×** | -3.6 | 0.008 | 12/37 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | **0.703×** | -3.1 | 0.047 | 4/38 (KATO III, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.896× | -2.9 | 0.091 | 14/37 (CFPAC-1, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 66.4 | 12 | 2 (2 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.20× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.256× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 273 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -26.8) |
| [[LoVo (line)]] | wt | 65.0 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -20.7) |
| [[KATO III (line)]] | alt | 75.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -14.3) |
| [[A498 (line)]] | wt | 152 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.470× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.0) |
| [[HT-29 (line)]] | alt | 64.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -14.6) |
| [[PANC-1 (line)]] | alt | 56.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.9) |
| [[HOP62 (line)]] | alt | 49.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.8) |
| [[LS 180 (line)]] | wt | 66.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 34.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -8.8) |
| [[A-427 (line)]] | wt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 96.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.3) |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.1) |
| [[H4 (line)]] | wt | 33.4 | 1 | 0 | [[Dexamethasone (drug)]] 0.5 µM 5.12× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.8) |
| [[J82 (line)]] | alt | 54.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.309× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 62.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.3) |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.451× (z -9.0) |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0773× (z -10.0) ⚠ toxic |
| [[SW480 (line)]] | alt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.4) |
| [[AN3 CA (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STOM]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MAP2]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[B4GALT1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MAOA]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ACSL1]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ALDH3B1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SORT1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CCDC6]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EPS8]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PLCE1]] | +0.58 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[IFNGR1]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR2]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[TMEM158]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[PRDM8]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ANXA10]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[LHX1]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ITGA2-AS1]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[RABGEF1P3]] | -0.51 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[LUCAT1]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[LIF]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[UPP1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.48 | -0.36 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR4]] | B | PLSCR4 activity raises PDLIM1's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without PLSCR4 | 0.007 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[DPP4]] | B | DPP4 activity raises PDLIM1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without DPP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[TOP2A]] | B | TOP2A activity raises PDLIM1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP1]] | B | DUSP1 activity raises PDLIM1's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 4.90× lower at baseline in the lines without DUSP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[VSIR]] | B | VSIR activity raises PDLIM1's level | lines that do not express VSIR (14) vs lines expressing it (36) | 2.48× lower at baseline in the lines without VSIR | 0.030 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[EPS8]] | B | EPS8 activity raises PDLIM1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 2.94× lower at baseline in the lines without EPS8 | 0.031 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises PDLIM1's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without SHROOM3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[DENND3]] | B | DENND3 activity raises PDLIM1's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 3.16× lower at baseline in the lines without DENND3 | 0.043 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[TNS3]] | B | TNS3 activity raises PDLIM1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.45× lower at baseline in the lines without TNS3 | 0.053 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[NR3C1]] | B | NR3C1 activity raises PDLIM1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[ALDH3B1]] | B | ALDH3B1 activity raises PDLIM1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 3.31× lower at baseline in the lines without ALDH3B1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[TRIM29]] | B | TRIM29 activity raises PDLIM1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without TRIM29 | 0.073 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND3]] | B | PDLIM1 activity raises DENND3's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.86× lower at baseline in the lines without PDLIM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[B4GALT1]] | B | PDLIM1 activity raises B4GALT1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without PDLIM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[MBNL1]] | B | PDLIM1 activity raises MBNL1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without PDLIM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[SHROOM3]] | B | PDLIM1 activity raises SHROOM3's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without PDLIM1 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[DUSP1]] | B | PDLIM1 activity raises DUSP1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without PDLIM1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[PLSCR4]] | B | PDLIM1 activity raises PLSCR4's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without PDLIM1 | 0.030 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[TES]] | B | PDLIM1 activity raises TES's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 3.22× lower at baseline in the lines without PDLIM1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[ALDH3B1]] | B | PDLIM1 activity raises ALDH3B1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.26× lower at baseline in the lines without PDLIM1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | B | PDLIM1 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express PDLIM1 (11) vs lines expressing it (37) | the lines without PDLIM1: 0.59× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | B | PDLIM1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express PDLIM1 (11) vs lines expressing it (37) | the lines without PDLIM1: 1.23× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | PDLIM1 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express PDLIM1 (11) vs lines expressing it (37) | the lines without PDLIM1: 0.92× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[TNS3]] | B | PDLIM1 activity raises TNS3's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.70× lower at baseline in the lines without PDLIM1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.2, 18.2); signed map (18.7, 28.4). **Vector** length 115, 31.9% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.3 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.7 | +4.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.4 | +4.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -7.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.5 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -16.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -3.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -6.8 |
|  | [[Ritonavir (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | PDZ and LIM domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:95,237,572-95,291,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLP-36, hCLIM1, CLP36; previously CLIM1 |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O00151](https://www.uniprot.org/uniprotkb/O00151) (PDZ and LIM domain protein 1):

> Cytoskeletal protein that may act as an adapter that brings other proteins (like kinases) to the cytoskeleton. Involved in assembly, disassembly and directioning of stress fibers in fibroblasts. Required for the localization of ACTN1 and PALLD to stress fibers. Required for cell migration and in maintaining cell polarity of fibroblasts (By similarity).

**Summary**, from NCBI Gene [9124](https://www.ncbi.nlm.nih.gov/gene/9124):

> This gene encodes a member of the enigma protein family. The protein contains two protein interacting domains, a PDZ domain at the amino terminal end and one to three LIM domains at the carboxyl terminal. It is a cytoplasmic protein associated with the cytoskeleton. The protein may function as an adapter to bring other LIM-interacting proteins to the cytoskeleton. Pseudogenes associated with this gene are located on chromosomes 3, 14 and 17. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:2067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2067) · Entrez [9124](https://www.ncbi.nlm.nih.gov/gene/9124) · UniProt [O00151](https://www.uniprot.org/uniprotkb/O00151) · Ensembl [ENSG00000107438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107438)

## Data

Gene col 2851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2851); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2851]; `tensor/DDL_lfc|DDL_z.npy` [2851]; `embed/gene_vectors.npy` [2851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2851 or target_col == 2851). Every well: [[PDLIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDLIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
