---
symbol: "CCDC6"
type: "gene"
col: 2916
ensembl_id: "ENSG00000108091"
name: "coiled-coil domain containing 6"
location: "10q21.2"
module: 17
arm: "+"
pooled_cpm: 129.91
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CCDC6

*coiled-coil domain containing 6* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +12.0, q 2e-30, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.639× (z -18.3, q 0e+00, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX1]] (+0.62, fdr 1e-05), [[HSD17B4]] (+0.62, fdr 1e-05), [[PDLIM1]] (+0.61, fdr 1e-05); moves opposite to [[PPP1R14B-AS1]] (-0.59, fdr 2e-05), [[TPTEP2-CSNK1E]] (-0.58, fdr 1e-05), [[ADGRL1-AS1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +12.0 | 2e-30 | 28/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +10.1 | 2e-21 | 37/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +6.9 | 1e-09 | 30/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +6.7 | 3e-09 | 27/48 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +6.4 | 2e-08 | 29/48 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.25×** | +6.1 | 1e-07 | 29/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +5.6 | 1e-06 | 24/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.4 | 4e-06 | 23/49 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +4.8 | 1e-04 | 26/47 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.7 | 1e-04 | 20/48 (A498, A-172, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.18× | +4.4 | 6e-04 | 19/47 (A498, AsPC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.17× | +4.3 | 8e-04 | 19/49 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.2 | 0.001 | 18/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 18/49 (LoVo, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.002 | 18/48 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +4.0 | 0.002 | 16/48 (C32, HepG2/C3A, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.15× | +3.9 | 0.003 | 20/48 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.14× | +3.8 | 0.004 | 17/48 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.007 | 18/48 (A498, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.6 | 0.009 | 9/49 (AsPC-1, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -18.3 | 0e+00 | 38/49 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -11.4 | 7e-28 | 37/47 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.739×** | -8.7 | 4e-16 | 33/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.750×** | -8.3 | 1e-14 | 34/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.751×** | -8.3 | 1e-14 | 31/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -6.5 | 7e-09 | 30/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.809×** | -6.1 | 7e-08 | 27/48 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.808×** | -5.9 | 2e-07 | 27/50 (LS 180, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.888× | -4.9 | 7e-05 | 12/48 (SNU-1, HepG2/C3A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.8 | 1e-04 | 20/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.847× | -4.4 | 5e-04 | 18/48 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.852× | -4.3 | 9e-04 | 16/48 (J82, RPMI-7951, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.816×** | -4.2 | 0.001 | 22/48 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.024 | 12/49 (LS 180, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 99.1 | 16 (1 ⚠) | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.17× (z +11.6) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Budesonide (drug)]] 5 µM 1.98× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.489× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 233 | 13 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.66× (z +44.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.2) |
| [[HOP62 (line)]] | alt | 70.6 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -13.2) |
| [[LS 180 (line)]] | wt | 222 | 4 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.53× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.470× (z -12.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 133 | 7 | 0 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 1.85× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -19.5) |
| [[NCI-H23 (line)]] | alt | 81.2 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.419× (z -9.9) |
| [[RKO (line)]] | wt | 138 | 1 | 3 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.69× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.5) |
| [[SNU-1 (line)]] | wt | 131 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -14.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.4) |
| [[SNU-423 (line)]] | alt | 152 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.538× (z -8.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.554× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -12.1) |
| [[H4 (line)]] | wt | 94.0 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.5) |
| [[J82 (line)]] | alt | 64.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.36× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.9) | — |
| [[LoVo (line)]] | wt | 126 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 116 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.7) |
| [[PANC-1 (line)]] | alt | 106 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.63× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -13.5) |
| [[SW48 (line)]] | wt | 185 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 5.15× (z +9.4) | — |
| [[SW480 (line)]] | alt | 174 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.595× (z -9.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 156 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 168 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.26× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.550× (z -8.5) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.441× (z -10.8) |
| [[SW 900 (line)]] | alt | 132 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -9.7) |
| [[SW1417 (line)]] | alt | 240 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -11.5) |
| [[A-427 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 179 | 1 | 0 | [[Neratinib (maleate) (drug)]] 5 µM 1.88× (z +9.4) | — |
| [[C32 (line)]] | wt | 45.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 79.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.6) |
| [[KATO III (line)]] | alt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 92.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.9) |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.244× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.6) | — |
| [[SW 1088 (line)]] | alt | 86.1 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0916× (z -8.5) |
| [[A-172 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 212 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 122 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HSD17B4]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[QDPR]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DLD]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TTC5]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.58 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[THYN1]] | +0.58 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[BLTP1]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[DLAT]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RNF20]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R14B-AS1]] | -0.59 | -0.46 / -0.66 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ADGRL1-AS1]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PDE6D]] | -0.56 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[PPP1R14B]] | -0.55 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[TPBG]] | -0.55 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[OSMR-DT]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ING2-DT]] | -0.54 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[ZNF143]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[POLR2K]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[PHLDA2]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[LUCAT1]] | -0.54 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CCDC6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NEBL]] | B | NEBL activity raises CCDC6's level | lines that do not express NEBL (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without NEBL | 0.056 | ⚠ within organs, on part of the lines; also absent: NUP210, NSUN7, ENSG00000288656 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-20.3, -6.4); signed map (-25.9, -19.3). **Vector** length 141, 43.3% of its response variance represented; |z| ≥ 3 in 1,401 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +5.4 |
|  | [[NG25 (drug)]] 5 µM |  | +6.6 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +10.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.9 | +4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.7 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.6 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -18.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -8.8 | -8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.5 | -8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.6 | -4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.4 | -1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:59,788,747-59,906,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTC, TPC, H4, PTC1; previously TST1, D10S170 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16204](https://www.uniprot.org/uniprotkb/Q16204) (Coiled-coil domain-containing protein 6):

> Acts as a structural scaffold that organizes free PP2Ac into a configuration that FBXO42 can recognize and ubiquitinate, leading to its proteasomal degradation. Also interacts independently with PPP4C through a mechanism distinct from FBXO42-mediated ubiquitination.

**Summary**, from NCBI Gene [8030](https://www.ncbi.nlm.nih.gov/gene/8030):

> This gene encodes a coiled-coil domain-containing protein. The encoded protein is ubiquitously expressed and may function as a tumor suppressor. A chromosomal rearrangement resulting in the expression of a fusion gene containing a portion of this gene and the intracellular kinase-encoding domain of the ret proto-oncogene is the cause of thyroid papillary carcinoma.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:18782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18782) · Entrez [8030](https://www.ncbi.nlm.nih.gov/gene/8030) · UniProt [Q16204](https://www.uniprot.org/uniprotkb/Q16204) · Ensembl [ENSG00000108091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108091)

## Data

Gene col 2916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2916); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2916]; `tensor/DDL_lfc|DDL_z.npy` [2916]; `embed/gene_vectors.npy` [2916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2916 or target_col == 2916). Every well: [[CCDC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
