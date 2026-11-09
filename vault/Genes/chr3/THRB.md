---
symbol: "THRB"
type: "gene"
col: 7483
ensembl_id: "ENSG00000151090"
name: "thyroid hormone receptor beta"
location: "3p24.2"
module: 8
arm: "+"
pooled_cpm: 58.75
n_lines_expressing: 29
n_dd_up: 8
n_dd_down: 34
n_dd_up_clean: 8
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 19
direction_downstream: 43
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# THRB

*thyroid hormone receptor beta* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +10.8, q 3e-24, up in 16 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.232× (z -22.7, q 0e+00, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A1]] (+0.52, fdr 1e-05), [[DGKH]] (+0.51, fdr 4e-05), [[IKZF2]] (+0.50, fdr 1e-05); moves opposite to [[ACTR5]] (-0.48, fdr 1e-04), [[ZNF559]] (-0.48, fdr 1e-04), [[SPEG]] (-0.47, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[SEPTIN9-DT]] → it (grade B ⚠); 43 go from it, the strongest it → [[ZIM2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +10.8 | 3e-24 | 16/28 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 3e-04 | 11/28 (NCI-H1792, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 5e-04 | 14/27 (C32, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 0.002 | 11/26 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.003 | 11/26 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.008 | 10/27 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.042 | 11/27 (C32, SNU-423, …) | rises with dose |  |
| [[Econazole (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.045 | 9/27 (NCI-H1573, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.12 | 10/28 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 11/27 (C32, NCI-H1792, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.12 | 12/27 (NCI-H1573, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.232×** | -22.7 | 0e+00 | 26/27 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.248×** | -21.7 | 0e+00 | 26/27 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.338×** | -16.8 | 0e+00 | 26/27 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.403×** | -13.0 | 1e-36 | 19/25 (Panc 03.27, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.506×** | -10.6 | 6e-24 | 24/26 (LS 180, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.545×** | -9.4 | 5e-19 | 23/27 (LS 180, AsPC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.553×** | -9.2 | 3e-18 | 21/27 (Panc 03.27, CFPAC-1, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -8.3 | 7e-15 | 23/28 (Panc 03.27, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -7.6 | 2e-12 | 21/26 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.634×** | -7.0 | 1e-10 | 21/26 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.629×** | -6.9 | 3e-10 | 18/23 (NCI-H1792, CFPAC-1, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.654×** | -6.3 | 1e-08 | 16/26 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -5.3 | 5e-06 | 18/27 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.716×** | -5.2 | 1e-05 | 17/26 (Panc 03.27, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -4.9 | 3e-05 | 16/27 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -4.9 | 3e-05 | 15/27 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.565×** | -4.6 | 1e-04 | 18/27 (LoVo, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.597×** | -4.2 | 8e-04 | 16/26 (HT-29, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.601×** | -4.1 | 1e-03 | 16/27 (Hs 766T, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.004 | 15/27 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.840× | -3.8 | 0.004 | 14/28 (HT-29, BT-474, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.004 | 15/26 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.633×** | -3.7 | 0.005 | 13/27 (CFPAC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.644×** | -3.6 | 0.008 | 15/27 (SW 900, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 16 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 191 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0613× (z -26.3) |
| [[LoVo (line)]] | wt | 175 | 1 | 12 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.166× (z -22.0) |
| [[LS 180 (line)]] | wt | 116 | 3 | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.141× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 200 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -16.9) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0714× (z -21.9) |
| [[HEC-1-A (line)]] | alt | 108 | 3 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +24.3) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -19.6) |
| [[NCI-H1792 (line)]] | alt | 89.7 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.190× (z -14.1) |
| [[A498 (line)]] | wt | 88.0 | 2 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.3) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -20.1) |
| [[KATO III (line)]] | alt | 36.4 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.131× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 126 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.214× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 142 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -17.0) |
| [[A549 (line)]] | wt | 37.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.123× (z -13.0) |
| [[COLO 205 (line)]] | alt | 80.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0749× (z -21.2) |
| [[HT-29 (line)]] | alt | 34.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -10.4) |
| [[J82 (line)]] | alt | 105 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -16.1) |
| [[BT-474 (line)]] | alt | 157 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -12.1) |
| [[C32 (line)]] | wt | 39.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -9.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 29.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -12.2) |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.113× (z -12.1) |
| [[SW48 (line)]] | wt | 25.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.2) | [[Canagliflozin (drug)]] 0.05 µM 0.140× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.61 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A1]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DGKH]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[IKZF2]] | +0.50 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SIPA1L2]] | +0.50 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[DAPK1]] | +0.49 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[CRACDL]] | +0.48 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[INPP4B]] | +0.48 | +0.58 / +0.37 | both halves | 8e-05 |  |
| [[KIF13B]] | +0.47 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.47 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[LINC02343]] | +0.47 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[EPS8]] | +0.46 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[SATB1]] | +0.46 | +0.37 / +0.34 | both halves | 1e-04 | pathway: SUMO E3 ligases SUMOylate target proteins |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | -0.48 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[ZNF559]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[SPEG]] | -0.47 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ZNF875]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[GNAZ]] | -0.45 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[ZNF71]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[ZNF177]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[KCTD2]] | -0.45 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[LRFN3]] | -0.44 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[PLA2G12A]] | -0.44 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[TCFL5]] | -0.44 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[SARDH]] | -0.44 | -0.40 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 12, C 7. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises THRB's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 4.48× lower at baseline in the lines without SEPTIN9-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[PTPRR]] | B | PTPRR activity raises THRB's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.55× lower at baseline in the lines without PTPRR | 0.011 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[ZNF71]] | B | ZNF71 activity lowers THRB's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 2.86× higher at baseline in the lines without ZNF71 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[ZIM2-AS1]] | B | ZIM2-AS1 activity lowers THRB's level | lines that do not express ZIM2-AS1 (13) vs lines expressing it (37) | 2.45× higher at baseline in the lines without ZIM2-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF71, ZNF470, ZFP28 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises THRB's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.19× lower at baseline in the lines without SLC44A3-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[MGST2]] | B | MGST2 activity raises THRB's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 3.51× lower at baseline in the lines without MGST2 | 0.050 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[DAPK2]] | B | DAPK2 activity raises THRB's level | lines that do not express DAPK2 (10) vs lines expressing it (40) | 3.02× lower at baseline in the lines without DAPK2 | 0.063 | ⚠ within organs, on part of the lines; also absent: IL18, CXCL16, SLC44A3-AS1; maybe low, not absent |
| [[STARD9]] | B | STARD9 activity lowers THRB's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 3.89× higher at baseline in the lines without STARD9 | 0.068 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[LINC01237]] | B | LINC01237 activity lowers THRB's level | lines that do not express LINC01237 (7) vs lines expressing it (43) | 4.12× higher at baseline in the lines without LINC01237 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity raises THRB's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without SAMD12-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[L1CAM]] | B | L1CAM activity lowers THRB's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.13× higher at baseline in the lines without L1CAM | 0.075 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[GNAZ]] | B | GNAZ activity lowers THRB's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 3.21× higher at baseline in the lines without GNAZ | 0.076 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 37, C 6. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZIM2-AS1]] | B | THRB activity lowers ZIM2-AS1's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.21× higher at baseline in the lines without THRB | 0.001 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[SEPTIN9-DT]] | B | THRB activity raises SEPTIN9-DT's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without THRB | 0.002 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[ZNF71]] | B | THRB activity lowers ZNF71's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.48× higher at baseline in the lines without THRB | 0.003 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[INPP4B]] | B | THRB activity strengthens INPP4B's drug response | lines that do not express THRB (15) vs lines expressing it (24) | the lines without THRB respond 0.72× as strongly (z diff +1.15); strongest at Homoharringtonine 5 µM: 1.32x vs 0.42x (z diff +7.8) | 0.006 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2; target measured in part of the lines; both ways; artifact flags |
| [[SLC44A3-AS1]] | B | THRB activity raises SLC44A3-AS1's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.53× lower at baseline in the lines without THRB | 0.007 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[STARD9]] | B | THRB activity lowers STARD9's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.19× higher at baseline in the lines without THRB | 0.008 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[TNFAIP8L1]] | B | THRB activity lowers TNFAIP8L1's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.63× higher at baseline in the lines without THRB | 0.008 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[LRFN3]] | B | THRB activity lowers LRFN3's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.49× higher at baseline in the lines without THRB | 0.013 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[EPS8]] | B | THRB activity raises EPS8's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.26× lower at baseline in the lines without THRB | 0.013 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[SIPA1L2]] | B | THRB activity weakens SIPA1L2's drug response | lines that do not express THRB (15) vs lines expressing it (24) | the lines without THRB respond 1.72× as strongly (z diff -2.48); strongest at Idarubicin (hydrochloride) 5 µM: 2.49x vs 1.34x (z diff -3.4) | 0.014 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2; target measured in part of the lines; artifact flags |
| [[TCFL5]] | B | THRB activity lowers TCFL5's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.55× higher at baseline in the lines without THRB | 0.022 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[KLHL2P1]] | B | THRB activity raises KLHL2P1's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without THRB | 0.025 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.412). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.5, 57.6); signed map (64.1, 0.8). **Vector** length 97.4, 28.2% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.7 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -22.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -21.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -16.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.6 | -7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:24,117,153-24,495,756 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THRB1, THRB2, NR1A2, THR1, ERBA-BETA, GRTH, TRbeta, TRb; previously ERBA2, PRTH |
| Gene groups (HGNC) | Thyroid hormone receptors |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: SUMOylation of intracellular receptors; Nuclear Receptor transcription pathway; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P10828](https://www.uniprot.org/uniprotkb/P10828) (Thyroid hormone receptor beta):

> Nuclear hormone receptor that can act as a repressor or activator of transcription. High affinity receptor for thyroid hormones, including triiodothyronine and thyroxine.

**Summary**, from NCBI Gene [7068](https://www.ncbi.nlm.nih.gov/gene/7068):

> The protein encoded by this gene is a nuclear hormone receptor for triiodothyronine. It is one of the several receptors for thyroid hormone, and has been shown to mediate the biological activities of thyroid hormone. Knockout studies in mice suggest that the different receptors, while having certain extent of redundancy, may mediate different functions of thyroid hormone. Mutations in this gene are known to be a cause of generalized thyroid hormone resistance (GTHR), a syndrome characterized by …

**Accessions** — [HGNC:11799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11799) · Entrez [7068](https://www.ncbi.nlm.nih.gov/gene/7068) · UniProt [P10828](https://www.uniprot.org/uniprotkb/P10828) · Ensembl [ENSG00000151090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151090)

## Data

Gene col 7483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7483); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7483]; `tensor/DDL_lfc|DDL_z.npy` [7483]; `embed/gene_vectors.npy` [7483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7483 or target_col == 7483). Every well: [[THRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
