---
symbol: "CCDC122"
type: "gene"
col: 7564
ensembl_id: "ENSG00000151773"
name: "coiled-coil domain containing 122"
location: "13q14.11"
module: 23
arm: "+"
pooled_cpm: 29.48
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CCDC122

*coiled-coil domain containing 122* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +8.9, q 2e-16, up in 28 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.334× (z -15.5, q 0e+00, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12A-AS2]] (+0.73, fdr 1e-04), [[KRCC1]] (+0.73, fdr 1e-05), [[ATE1OSP]] (+0.73, fdr 6e-05); moves opposite to [[PODXL2]] (-0.67, fdr 1e-04), [[GNAI2]] (-0.65, fdr 5e-04), [[APMAP]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MIR583HG]] → it (grade B ⚠); 3 go from it, the strongest it → [[GABPB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.9 | 2e-16 | 28/41 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.2 | 2e-07 | 26/42 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.8 | 3e-04 | 19/43 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 4e-04 | 18/42 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.7 | 4e-04 | 20/43 (LS 180, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.004 | 22/43 (A498, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.007 | 19/42 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.043 | 13/43 (A-172, SW480, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.052 | 18/42 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.073 | 8/43 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.094 | 13/42 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.094 | 15/42 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.096 | 12/42 (SW480, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.096 | 16/42 (SW480, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.334×** | -15.5 | 0e+00 | 39/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.355×** | -14.7 | 0e+00 | 40/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.412×** | -12.5 | 1e-33 | 39/43 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.384×** | -11.8 | 9e-30 | 38/43 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -11.7 | 1e-29 | 37/42 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.444×** | -10.0 | 2e-21 | 33/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.291×** | -9.1 | 6e-18 | 36/43 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.294×** | -9.0 | 1e-17 | 33/41 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -7.8 | 4e-13 | 31/41 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.614×** | -6.0 | 1e-07 | 25/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -5.8 | 3e-07 | 28/43 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.639×** | -5.5 | 2e-06 | 23/41 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.727×** | -4.3 | 7e-04 | 19/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.766×** | -3.8 | 0.007 | 20/41 (COLO 205, NCI-H1573, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.604×** | -3.7 | 0.007 | 12/28 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.013 | 17/42 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.788×** | -3.2 | 0.038 | 12/42 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Asciminib (drug)]] 0.05 µM |  | **0.798×** | -3.1 | 0.059 | 12/42 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.805×** | -3.1 | 0.059 | 12/43 (BT-474, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 60.0 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -13.8) |
| [[PANC-1 (line)]] | alt | 45.7 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 27.8 | 2 | 8 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.210× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.256× (z -10.4) |
| [[SW480 (line)]] | alt | 37.6 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -19.8) |
| [[COLO 205 (line)]] | alt | 117 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -18.9) |
| [[HCT15 (line)]] | alt | 45.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0890× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.236× (z -10.0) |
| [[HT-29 (line)]] | alt | 42.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -14.0) |
| [[LoVo (line)]] | wt | 23.9 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.168× (z -12.9) |
| [[LS 180 (line)]] | wt | 31.6 | 2 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.0997× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 53.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -13.4) |
| [[A549 (line)]] | wt | 27.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -11.7) |
| [[J82 (line)]] | alt | 25.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 34.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 48.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.250× (z -11.5) |
| [[SNU-423 (line)]] | alt | 30.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.198× (z -11.4) |
| [[A-172 (line)]] | wt | 22.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 32.8 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -10.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -9.3) |
| [[Hs 766T (line)]] | wt | 47.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.270× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 42.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.247× (z -10.1) |
| [[RKO (line)]] | wt | 20.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.240× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.0457× (z -10.6) |
| [[BT-474 (line)]] | alt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -9.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 8.50 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0973× (z -9.4) |
| [[A-427 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12A-AS2]] | +0.73 | +0.74 / +0.36 | both halves | 1e-04 |  |
| [[KRCC1]] | +0.73 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.73 | +0.74 / +0.38 | both halves | 6e-05 |  |
| [[THAP2]] | +0.70 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[MAILR]] | +0.69 | +0.73 / +0.28 | both halves | 3e-04 |  |
| [[DNAI4]] | +0.69 | +0.70 / +0.39 | both halves | 6e-05 |  |
| [[LACC1]] | +0.67 | +0.69 / +0.45 | both halves | 3e-05 | STRING 949; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RFX3-DT]] | +0.67 | +0.70 / +0.23 | both halves | 5e-04 |  |
| [[NEPRO-AS1]] | +0.67 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.67 | +0.68 / +0.24 | both halves | 4e-04 |  |
| [[KRBOX5]] | +0.66 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[GABPB2]] | +0.66 | +0.72 / +0.26 | both halves | 4e-04 |  |
| [[CCDC59]] | +0.65 | +0.66 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL2]] | -0.67 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.65 | -0.55 / -0.23 | both halves | 5e-04 |  |
| [[APMAP]] | -0.64 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[HDAC1]] | -0.63 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[LRFN3]] | -0.63 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[NOMO1]] | -0.62 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[MATCAP1]] | -0.62 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[GTPBP3]] | -0.62 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[GGCX]] | -0.62 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[CEP131]] | -0.61 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[PCMT1]] | -0.61 | -0.55 / -0.20 | both halves | 7e-04 |  |
| [[CALM3]] | -0.60 | -0.58 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR583HG]] | B | MIR583HG activity raises CCDC122's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 2.75× lower at baseline in the lines without MIR583HG | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CCDC122's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[JHY]] | B | JHY activity raises CCDC122's level | lines that do not express JHY (15) vs lines expressing it (35) | 2.06× lower at baseline in the lines without JHY | 0.075 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[CADM4]] | B | CADM4 activity lowers CCDC122's level | lines that do not express CADM4 (5) vs lines expressing it (45) | 1.88× higher at baseline in the lines without CADM4 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LACC1]] | C | LACC1 activity raises CCDC122's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 5.46× lower at baseline in the lines without LACC1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1; co-absent with the target |
| [[DPH6-DT]] | C | DPH6-DT activity raises CCDC122's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABPB2]] | B | CCDC122 activity raises GABPB2's level | lines that do not express CCDC122 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without CCDC122 | 0.060 | ⚠ within organs, on part of the lines; also absent: LACC1, SDC4, IL1RAP; its own permutation p |
| [[MED13]] | B | CCDC122 activity raises MED13's level | lines that do not express CCDC122 (5) vs lines expressing it (45) | 1.02× lower at baseline in the lines without CCDC122 | 0.089 | ⚠ within organs, on part of the lines; also absent: LACC1, SDC4, IL1RAP; its own permutation p |
| [[LACC1]] | C | CCDC122 activity raises LACC1's level | lines that do not express CCDC122 (5) vs lines expressing it (45) | 5.21× lower at baseline in the lines without CCDC122 | 0.060 | ⚠ within organs, on part of the lines; also absent: LACC1, SDC4, IL1RAP; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.9, 13.5); signed map (25.4, -10.7). **Vector** length 108, 30.7% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +1.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.8 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.6 | -15.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.9 | -14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -9.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 122 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:43,823,909-43,879,740 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31846 |
| Matched by | ensembl_id |

UniProt [Q5T0U0](https://www.uniprot.org/uniprotkb/Q5T0U0) carries no function annotation.

**Summary**, from NCBI Gene [160857](https://www.ncbi.nlm.nih.gov/gene/160857):

> This gene encodes a protein that contains a coiled-coil domain. Naturally occurring mutations in this gene are associated with leprosy. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:26478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26478) · Entrez [160857](https://www.ncbi.nlm.nih.gov/gene/160857) · UniProt [Q5T0U0](https://www.uniprot.org/uniprotkb/Q5T0U0) · Ensembl [ENSG00000151773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151773)

## Data

Gene col 7564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7564); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7564]; `tensor/DDL_lfc|DDL_z.npy` [7564]; `embed/gene_vectors.npy` [7564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7564 or target_col == 7564). Every well: [[CCDC122 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC122.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
