---
symbol: "DTNB"
type: "gene"
col: 6126
ensembl_id: "ENSG00000138101"
name: "dystrobrevin beta"
location: "2p23.3"
module: 18
arm: "+"
pooled_cpm: 86.08
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DTNB

*dystrobrevin beta* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +10.8, q 2e-24, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.698× (z -10.7, q 5e-24, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTNBP1]] (+0.65, fdr 7e-06), [[CDIN1]] (+0.62, fdr 1e-05), [[MIPOL1]] (+0.61, fdr 1e-05); moves opposite to [[ARHGAP1]] (-0.57, fdr 1e-05), [[ZNF17]] (-0.56, fdr 3e-05), [[MAGED2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +10.8 | 2e-24 | 37/47 (LS 180, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +9.7 | 7e-20 | 32/47 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +9.7 | 9e-20 | 36/47 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +8.3 | 2e-14 | 32/48 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +8.0 | 1e-13 | 27/47 (CFPAC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.3 | 3e-11 | 32/47 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 2e-06 | 25/47 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +5.5 | 2e-06 | 29/46 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +5.0 | 4e-05 | 25/48 (HT-29, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.006 | 20/46 (NCI-H1573, SW480, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.013 | 14/47 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.042 | 13/48 (BT-474, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.049 | 15/47 (SNU-423, NCI-H2030, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.078 | 10/47 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.094 | 14/46 (NCI-H1573, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -10.7 | 5e-24 | 29/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -10.5 | 3e-23 | 40/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -9.5 | 3e-19 | 38/47 (RKO, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.647×** | -8.8 | 1e-16 | 31/47 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -7.7 | 2e-12 | 28/48 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.780×** | -7.4 | 1e-11 | 28/47 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.698×** | -7.0 | 2e-10 | 28/44 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -6.6 | 3e-09 | 24/43 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -6.5 | 5e-09 | 26/46 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.739×** | -6.4 | 1e-08 | 24/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.750×** | -6.0 | 7e-08 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.766×** | -5.6 | 9e-07 | 28/46 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.6 | 1e-06 | 25/49 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.653×** | -4.7 | 1e-04 | 19/36 (SK-MEL-2, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.828×** | -4.0 | 0.003 | 18/47 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.8 | 0.005 | 19/46 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.835× | -3.8 | 0.005 | 22/47 (SW480, LoVo, …) | rises with dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.867× | -3.0 | 0.064 | 7/48 (CFPAC-1, C32, …) | top dose only |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.908× | -2.9 | 0.088 | 5/48 (BT-474, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 120 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -27.8) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 218 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 88.8 | 0 | 10 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -17.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.253× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 9 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -11.2) |
| [[LoVo (line)]] | wt | 100 | 1 | 8 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -14.2) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.217× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 96.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -13.0) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.9) |
| [[RKO (line)]] | wt | 133 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -17.6) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.111× (z -13.8) |
| [[SW480 (line)]] | alt | 140 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -16.3) |
| [[A-427 (line)]] | wt | 236 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -12.4) |
| [[MIA PaCa-2 (line)]] | alt | 128 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 136 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 73.1 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.8) |
| [[A498 (line)]] | wt | 49.9 | 1 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.8) | [[Harringtonine (drug)]] 5 µM 0.326× (z -11.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 224 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 103 | 1 | 3 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.83× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[Panc 03.27 (line)]] | alt | 67.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.8) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0790× (z -15.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.7) |
| [[SNU-1 (line)]] | wt | 112 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0617× (z -13.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.113× (z -10.2) |
| [[A549 (line)]] | wt | 92.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -22.2) ⚠ cell-cycle shift, explains ~86% of this change |
| [[SNU-423 (line)]] | alt | 57.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -12.6) |
| [[A-172 (line)]] | wt | 56.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.02× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.9) ⚠ cell-cycle shift, explains ~86% of this change |
| [[BT-474 (line)]] | alt | 68.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.7) ⚠ cell-cycle shift, explains ~86% of this change |
| [[CFPAC-1 (line)]] | alt | 38.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -8.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 35.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.43× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 50.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.40× (z +11.3) | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 57.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.04× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNBP1]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 | STRING 919 |
| [[CDIN1]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MIPOL1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CMTM8]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PHF20]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[RNF130]] | +0.57 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CLASP2]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SNX24]] | +0.56 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SPIDR]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CAMKMT]] | +0.56 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[KPNA3]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP1]] | -0.57 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[ZNF17]] | -0.56 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MAGED2]] | -0.55 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[FBXO8]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[YME1L1]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZNF490]] | -0.52 | -0.30 / -0.29 | both halves | 2e-04 |  |
| [[ZNF550]] | -0.51 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[METTL21EP-1]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[TRAPPC6B]] | -0.51 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[ZNF408]] | -0.51 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[MMUT]] | -0.51 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[LINC00310]] | -0.50 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises DTNB's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without SLC5A4-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[CRACD]] | B | CRACD activity raises DTNB's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without CRACD | 0.019 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[DOCK3]] | B | DOCK3 activity raises DTNB's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without DOCK3 | 0.043 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[CMTM8]] | B | CMTM8 activity raises DTNB's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 2.19× lower at baseline in the lines without CMTM8 | 0.064 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[NMNAT3]] | B | NMNAT3 activity raises DTNB's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without NMNAT3 | 0.068 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers DTNB's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers DTNB's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TTC28]] | B | TTC28 activity raises DTNB's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without TTC28 | 0.098 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[AGTPBP1]] | C | AGTPBP1 activity raises DTNB's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.4, -34.6); signed map (-13.2, -51.8). **Vector** length 102, 29.2% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.0 | -10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dystrobrevin beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:25,377,198-25,673,647 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers ZZ-type |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O60941](https://www.uniprot.org/uniprotkb/O60941) (Dystrobrevin beta):

> Scaffolding protein that assembles DMD and SNTA1 molecules to the basal membrane of kidney cells and liver sinusoids (By similarity). May function as a repressor of the SYN1 promoter through the binding of repressor element-1 (RE-1), in turn regulates SYN1 expression and may be involved in cell proliferation regulation during the early phase of neural differentiation. May be required for proper maturation and function of a subset of inhibitory synapses (By similarity).

**Summary**, from NCBI Gene [1838](https://www.ncbi.nlm.nih.gov/gene/1838):

> This gene encodes dystrobrevin beta, a component of the dystrophin-associated protein complex (DPC). The DPC consists of dystrophin and several integral and peripheral membrane proteins, including dystroglycans, sarcoglycans, syntrophins and dystrobrevin alpha and beta. The DPC localizes to the sarcolemma and its disruption is associated with various forms of muscular dystrophy. Dystrobrevin beta is thought to interact with syntrophin and the DP71 short form of dystrophin. [provided by RefSeq, …

**Accessions** — [HGNC:3058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3058) · Entrez [1838](https://www.ncbi.nlm.nih.gov/gene/1838) · UniProt [O60941](https://www.uniprot.org/uniprotkb/O60941) · Ensembl [ENSG00000138101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138101)

## Data

Gene col 6126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6126); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6126]; `tensor/DDL_lfc|DDL_z.npy` [6126]; `embed/gene_vectors.npy` [6126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6126 or target_col == 6126). Every well: [[DTNB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTNB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
