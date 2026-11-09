---
symbol: "TECPR1"
type: "gene"
col: 12971
ensembl_id: "ENSG00000205356"
name: "tectonin beta-propeller repeat containing 1"
location: "7q21.3"
module: 85
arm: "+"
pooled_cpm: 22.35
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# TECPR1

*tectonin beta-propeller repeat containing 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.38× (z +18.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.363× (z -15.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EVI5L]] (+0.70, fdr 1e-05), [[GIPC1]] (+0.69, fdr 2e-05), [[WRAP73]] (+0.68, fdr 4e-05); moves opposite to [[SNX5]] (-0.75, fdr 1e-05), [[EIF4G2]] (-0.68, fdr 3e-05), [[PNISR-AS1]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.38×** | +18.6 | 0e+00 | 47/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +17.5 | 0e+00 | 46/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.74×** | +15.4 | 0e+00 | 45/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +9.8 | 2e-20 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +7.2 | 7e-11 | 33/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +5.2 | 2e-05 | 30/48 (AsPC-1, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.4 | 7e-04 | 22/48 (KATO III, SW 900, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 17/45 (NCI-H1573, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.020 | 11/48 (A-427, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.054 | 8/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -15.5 | 0e+00 | 44/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -11.1 | 4e-26 | 34/47 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -10.7 | 1e-24 | 41/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -10.4 | 2e-23 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.683×** | -8.3 | 2e-14 | 36/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.584×** | -8.2 | 2e-14 | 34/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -8.1 | 5e-14 | 34/48 (A498, HT-29, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -7.8 | 4e-13 | 27/47 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -7.2 | 3e-11 | 29/46 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -7.0 | 1e-10 | 29/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -6.1 | 4e-08 | 27/48 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -4.6 | 2e-04 | 25/48 (A-427, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.744×** | -4.5 | 2e-04 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.762×** | -4.2 | 0.001 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -3.9 | 0.004 | 18/48 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -3.2 | 0.049 | 16/48 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.753×** | -3.1 | 0.063 | 6/48 (SW1417, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.759×** | -3.0 | 0.077 | 1/48 (NCI-H460) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.8 | 1 | 8 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 20.3 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.241× (z -12.0) |
| [[PANC-1 (line)]] | alt | 23.3 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.24× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 55.5 | 4 | 2 | [[Panobinostat (drug)]] 5 µM 7.26× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.5) |
| [[RKO (line)]] | wt | 30.5 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.82× (z +11.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0793× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.3) |
| [[SW480 (line)]] | alt | 21.1 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.56× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -11.4) |
| [[A549 (line)]] | wt | 21.4 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.8) |
| [[HT-29 (line)]] | alt | 31.6 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.267× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.5) |
| [[KATO III (line)]] | alt | 18.4 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 6.24× (z +11.7) | [[Digitoxin (drug)]] 0.5 µM 0.231× (z -9.4) |
| [[C32 (line)]] | wt | 51.5 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.00× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.30× (z +10.7) | — |
| [[J82 (line)]] | alt | 25.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.75× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -10.5) |
| [[A-427 (line)]] | wt | 21.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.6) |
| [[A498 (line)]] | wt | 22.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.72× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.38× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.368× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 20.7 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.89× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.244× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -13.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.248× (z -10.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 17.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0581× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.261× (z -9.5) |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -8.9) |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EVI5L]] | +0.70 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GIPC1]] | +0.69 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[WRAP73]] | +0.68 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[PI4KA]] | +0.68 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RNF41]] | +0.68 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MARCHF2]] | +0.67 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.67 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[PSMD9]] | +0.66 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TRIM11]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.65 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[ANKRD27]] | +0.65 | +0.47 / +0.30 | both halves | 2e-04 |  |
| [[TMEM184B]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX5]] | -0.75 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.68 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PNISR-AS1]] | -0.68 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[MBNL3]] | -0.65 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | -0.63 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.63 | -0.41 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[C5orf15]] | -0.63 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[GALNT7-DT]] | -0.63 | -0.44 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[EFCAB5]] | -0.63 | -0.49 / -0.03 | ⚠ not reproduced | 0.006 |  |
| [[ANKRD18B]] | -0.63 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[PBLD]] | -0.62 | -0.38 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[LSMEM1]] | -0.62 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[UBAP2L]] | -0.62 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[HMGN2]] | -0.62 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TAF9B]] | -0.61 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[DDX39B]] | -0.61 | -0.36 / -0.45 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TECPR1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TECPR1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.7, 0.9); signed map (-34.0, 1.9). **Vector** length 101, 26.3% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.5 | +18.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.9 | +15.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +17.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +9.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | -0.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.1 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | tectonin beta-propeller repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:98,214,624-98,252,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434B0335, FLJ23419, FLJ90593, KIAA1358 |
| Gene groups (HGNC) | Tectonin beta-propeller repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6L1](https://www.uniprot.org/uniprotkb/Q7Z6L1) (Tectonin beta-propeller repeat-containing protein 1):

> Tethering factor involved in autophagy. Involved in autophagosome maturation by promoting the autophagosome fusion with lysosomes: acts by associating with both the ATG5-ATG12 conjugate and phosphatidylinositol-3-phosphate (PtdIns(3)P) present at the surface of autophagosomes. Also involved in selective autophagy against bacterial pathogens, by being required for phagophore/preautophagosomal structure biogenesis and maturation.

**Summary**, from NCBI Gene [25851](https://www.ncbi.nlm.nih.gov/gene/25851):

> This gene encodes a tethering factor involved in autophagy. The encoded protein is found at autolysosomes, and is involved in targeting protein aggregates, damaged mitochondria, and bacterial pathogens for autophagy [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:22214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22214) · Entrez [25851](https://www.ncbi.nlm.nih.gov/gene/25851) · UniProt [Q7Z6L1](https://www.uniprot.org/uniprotkb/Q7Z6L1) · Ensembl [ENSG00000205356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205356)

## Data

Gene col 12971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12971); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12971]; `tensor/DDL_lfc|DDL_z.npy` [12971]; `embed/gene_vectors.npy` [12971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12971 or target_col == 12971). Every well: [[TECPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TECPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
