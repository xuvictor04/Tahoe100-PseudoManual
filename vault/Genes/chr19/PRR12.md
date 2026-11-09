---
symbol: "PRR12"
type: "gene"
col: 4740
ensembl_id: "ENSG00000126464"
name: "proline rich 12"
location: "19q13.33"
module: 36
arm: "+"
pooled_cpm: 34.02
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PRR12

*proline rich 12* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.80× (z +5.5, q 2e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.506× (z -12.1, q 8e-31, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.613× (z -8.7, q 6e-16, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM2B]] (+0.56, fdr 1e-05), [[SETD1A]] (+0.55, fdr 1e-05), [[PATZ1]] (+0.54, fdr 1e-05); moves opposite to [[ETNK1]] (-0.49, fdr 1e-05), [[GLS]] (-0.48, fdr 4e-05), [[RAB22A]] (-0.46, fdr 7e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +5.5 | 2e-05 | 24/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.9 | 3e-04 | 22/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.6 | 1e-03 | 22/49 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 0.001 | 22/48 (PANC-1, HepG2/C3A, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.002 | 18/48 (MIA PaCa-2, SHP-77, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.015 | 12/48 (PANC-1, J82, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.018 | 19/48 (PANC-1, RKO, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.047 | 7/46 (PANC-1, SK-MEL-2, …) | all doses, flat | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.066 | 8/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.11 | 13/47 (PANC-1, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.506×** | -12.1 | 8e-31 | 36/45 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -12.0 | 2e-30 | 29/40 (HCT15, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.530×** | -10.4 | 3e-23 | 28/43 (RPMI-7951, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -8.7 | 6e-16 | 34/48 (SNU-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.646×** | -7.8 | 1e-12 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -7.4 | 1e-11 | 29/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -7.4 | 1e-11 | 31/47 (A-427, AN3 CA, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.662×** | -7.3 | 2e-11 | 28/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.680×** | -6.8 | 5e-10 | 28/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -6.7 | 1e-09 | 27/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -6.6 | 2e-09 | 30/48 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.776×** | -6.4 | 1e-08 | 25/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -6.3 | 2e-08 | 27/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.709×** | -6.1 | 5e-08 | 26/48 (A-172, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.4 | 2e-06 | 26/48 (NCI-H460, NCI-H2030, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.7 | 1e-04 | 23/48 (SW1417, C32, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.789×** | -4.2 | 8e-04 | 19/48 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.859× | -3.8 | 0.004 | 18/48 (H4, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.811×** | -3.7 | 0.005 | 17/47 (CHP-212, A-427, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.024 | 12/47 (A-427, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.820×** | -3.2 | 0.024 | 16/48 (A-427, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.845× | -3.0 | 0.055 | 10/48 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -2.9 | 0.077 | 14/48 (MIA PaCa-2, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 20.3 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.205× (z -13.3) |
| [[A-172 (line)]] | wt | 41.6 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 80.4 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 24.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -9.0) |
| [[A-427 (line)]] | wt | 58.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.4) |
| [[COLO 205 (line)]] | alt | 37.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0573× (z -19.6) |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -11.0) |
| [[SW480 (line)]] | alt | 38.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -8.5) |
| [[C32 (line)]] | wt | 37.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.297× (z -9.2) |
| [[H4 (line)]] | wt | 29.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.7) |
| [[HCT15 (line)]] | alt | 63.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -15.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.0856× (z -8.9) |
| [[A549 (line)]] | wt | 33.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -9.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0952× (z -17.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0797× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0922× (z -11.8) |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -9.0) |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0661× (z -18.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0831× (z -16.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM2B]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SETD1A]] | +0.55 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PATZ1]] | +0.54 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CHERP]] | +0.54 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ZFP64]] | +0.52 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CBX8]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[RAVER1]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PHF12]] | +0.51 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[AKAP8]] | +0.51 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[GTF3C2]] | +0.50 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ZNF668]] | +0.50 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETNK1]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[GLS]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RAB22A]] | -0.46 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[PDLIM5]] | -0.45 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PEAK1]] | -0.45 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[MALAT1]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[GNG5]] | -0.44 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[PHF20L1]] | -0.43 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[CTNNA1]] | -0.42 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[SELENOI]] | -0.42 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[SLC35F5]] | -0.42 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[EFR3A]] | -0.41 | -0.45 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.244). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.9, -10.1); signed map (-13.8, -25.9). **Vector** length 96.8, 23.2% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.8 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +3.2 | +4.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.9 | -12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -12.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,591,182-49,626,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1205 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULL5](https://www.uniprot.org/uniprotkb/Q9ULL5) (Proline-rich protein 12):

> May play a role in the regulation of cohesin complex loading onto chromatin, probably acting in coordination with NIPBL and MAU2.

**Summary**, from NCBI Gene [57479](https://www.ncbi.nlm.nih.gov/gene/57479):

> This gene encodes a proline-rich protein that contains two A-T hook DNA binding domains. A chromosomal translocation and gene fusion between this gene and zinc finger, MIZ-type containing 1 (Gene ID: 57178) may underlie intellectual disability and neuropsychiatric problems in a human patient. Enriched expression of this gene in embryonic mouse brain suggests that this gene may play a role in nervous system development. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:29217](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29217) · Entrez [57479](https://www.ncbi.nlm.nih.gov/gene/57479) · UniProt [Q9ULL5](https://www.uniprot.org/uniprotkb/Q9ULL5) · Ensembl [ENSG00000126464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126464)

## Data

Gene col 4740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4740); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4740]; `tensor/DDL_lfc|DDL_z.npy` [4740]; `embed/gene_vectors.npy` [4740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4740 or target_col == 4740). Every well: [[PRR12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
