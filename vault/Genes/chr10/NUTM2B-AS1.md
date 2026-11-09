---
symbol: "NUTM2B-AS1"
type: "gene"
col: 13461
ensembl_id: "ENSG00000225484"
name: "NUTM2B antisense RNA 1"
location: "10q22.3"
module: 5
arm: "+"
pooled_cpm: 95.98
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NUTM2B-AS1

*NUTM2B antisense RNA 1* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.80× (z +15.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.626× (z -12.3, q 4e-32, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2A-AS1]] (+0.84, fdr 7e-06), [[MFSD14CP-1]] (+0.70, fdr 7e-06), [[ATXN10]] (+0.67, fdr 1e-05); moves opposite to [[RAB3A]] (-0.65, fdr 7e-06), [[SMAP2]] (-0.62, fdr 1e-05), [[ORC4]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MARK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +15.3 | 0e+00 | 47/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +14.3 | 1e-43 | 44/48 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +11.1 | 3e-26 | 42/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +10.6 | 5e-24 | 40/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +10.3 | 9e-23 | 29/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +9.9 | 2e-21 | 35/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +8.0 | 1e-13 | 36/48 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +6.9 | 3e-10 | 30/48 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +6.9 | 4e-10 | 30/47 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +6.7 | 1e-09 | 35/48 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +6.5 | 3e-09 | 31/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +6.0 | 9e-08 | 22/49 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 1e-07 | 27/48 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +5.9 | 1e-07 | 23/47 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.7 | 5e-07 | 31/45 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +5.2 | 7e-06 | 23/48 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 3e-05 | 22/48 (KATO III, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.9 | 3e-05 | 12/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.20×** | +4.8 | 5e-05 | 22/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.626×** | -12.3 | 4e-32 | 32/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.626×** | -12.3 | 4e-32 | 38/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.688×** | -9.8 | 2e-20 | 35/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.744×** | -7.8 | 1e-12 | 33/47 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.876× | -4.9 | 1e-04 | 15/49 (SW480, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -4.8 | 1e-04 | 15/48 (CHP-212, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.5 | 6e-04 | 19/49 (SW480, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.854× | -4.2 | 0.002 | 20/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.755×** | -3.9 | 0.007 | 21/47 (SNU-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 0.881× | -3.2 | 0.075 | 6/49 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 135 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.427× (z -9.7) |
| [[PANC-1 (line)]] | alt | 100 | 3 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +16.2) | [[Docetaxel (drug)]] 0.05 µM 0.533× (z -10.9) ⚠ transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.548× (z -10.4) |
| [[SW480 (line)]] | alt | 149 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.563× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 140 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.446× (z -11.0) |
| [[LoVo (line)]] | wt | 139 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 216 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.2) |
| [[HOP62 (line)]] | alt | 84.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 155 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.476× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 89.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 134 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.543× (z -8.7) |
| [[KATO III (line)]] | alt | 62.6 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.00× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 63.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +11.5) | — |
| [[A-427 (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.530× (z -9.1) |
| [[A549 (line)]] | wt | 93.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.528× (z -8.9) |
| [[C-33 A (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 84.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +11.5) | — |
| [[H4 (line)]] | wt | 81.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 54.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.456× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 58.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 42.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 88.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[SK-MEL-2 (line)]] | alt | 74.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 210 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.189× (z -9.5) |
| [[BT-474 (line)]] | alt | 120 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.375× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 58.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 104 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 45.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.1) | — |
| [[J82 (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 88.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0736× (z -8.7) |
| [[A498 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2A-AS1]] | +0.84 | +0.73 / +0.85 | both halves | 7e-06 | same gene group |
| [[MFSD14CP-1]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[ATXN10]] | +0.67 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[NPIPB4]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CUEDC1]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TRAPPC8]] | +0.65 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[ENOX2]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CDC42BPA]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[RUFY3]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.65 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[SMAP2]] | -0.62 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ORC4]] | -0.61 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.60 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[LINC00888]] | -0.60 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[APAF1]] | -0.60 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[PJA2]] | -0.59 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[MMUT]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[POT1]] | -0.56 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[GNAI3]] | -0.56 | -0.62 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARK1]] | B | MARK1 activity raises NUTM2B-AS1's level | lines that do not express MARK1 (24) vs lines expressing it (26) | 1.24× lower at baseline in the lines without MARK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: FXYD6, COL4A4, ENSG00000283982 |
| [[HDAC6]] | B | HDAC6 activity raises NUTM2B-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CAPN5]] | C | CAPN5 activity lowers NUTM2B-AS1's level | lines that do not express CAPN5 (4) vs lines expressing it (46) | 2.16× higher at baseline in the lines without CAPN5 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF22, PLEKHF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (6.9, -11.5); signed map (10.1, -7.1). **Vector** length 130, 39.3% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +8.8 | +14.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.5 | +15.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.7 | +11.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +6.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.5 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +6.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -12.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.5 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | NUTM2B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q22.3 — chr10:79,661,394-79,826,594 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51204) · Entrez [101060691](https://www.ncbi.nlm.nih.gov/gene/101060691) · Ensembl [ENSG00000225484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225484)

## Data

Gene col 13461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13461); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13461]; `tensor/DDL_lfc|DDL_z.npy` [13461]; `embed/gene_vectors.npy` [13461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13461 or target_col == 13461). Every well: [[NUTM2B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUTM2B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
