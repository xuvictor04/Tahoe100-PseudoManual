---
symbol: "FLYWCH1"
type: "gene"
col: 670
ensembl_id: "ENSG00000059122"
name: "FLYWCH-type zinc finger 1"
location: "16p13.3"
module: 30
arm: "+"
pooled_cpm: 21.05
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# FLYWCH1

*FLYWCH-type zinc finger 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.25× (z +11.4, q 1e-27, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.482× (z -10.8, q 1e-24, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZL1]] (+0.75, fdr 7e-06), [[CC2D1A]] (+0.71, fdr 7e-06), [[ANKRD39]] (+0.71, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.63, fdr 1e-05), [[LEKR1]] (-0.62, fdr 1e-05), [[TUG1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ITGB8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.25×** | +11.4 | 1e-27 | 43/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.02×** | +10.5 | 2e-23 | 42/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +9.0 | 4e-17 | 39/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.6 | 7e-04 | 18/48 (A-427, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 0.001 | 22/48 (COLO 205, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.4 | 0.001 | 18/37 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.002 | 18/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 16/48 (A-172, A-427, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.005 | 18/46 (SNU-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.005 | 20/48 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.9 | 0.006 | 14/44 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +3.8 | 0.008 | 13/48 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +3.1 | 0.081 | 16/46 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.084 | 14/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -10.8 | 1e-24 | 36/47 (LOX-IMVI, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -9.5 | 4e-19 | 36/47 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.659×** | -8.7 | 5e-16 | 29/47 (A-172, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.617×** | -7.2 | 1e-10 | 28/48 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -7.1 | 1e-10 | 34/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -6.4 | 1e-08 | 26/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.660×** | -5.9 | 3e-07 | 16/30 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.701×** | -5.3 | 1e-05 | 21/41 (SNU-423, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.694×** | -5.0 | 4e-05 | 22/36 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.725×** | -4.7 | 1e-04 | 21/46 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.815×** | -4.3 | 0.001 | 22/48 (A-172, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.8 | 0.006 | 19/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.802×** | -3.3 | 0.050 | 14/48 (A498, NCI-H661, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.813×** | -3.1 | 0.091 | 14/47 (NCI-H460, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 20.1 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.65× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.308× (z -8.9) |
| [[SW480 (line)]] | alt | 13.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +10.1) | — |
| [[A-172 (line)]] | wt | 41.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.411× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -8.7) |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0546× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -11.3) |
| [[LoVo (line)]] | wt | 15.2 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.08× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 27.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -10.1) |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0800× (z -8.6) |
| [[H4 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SHP-77 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.100× (z -12.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0769× (z -11.7) |
| [[A-427 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | +0.75 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[CC2D1A]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RTCA]] | +0.66 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[BLVRB]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ABCD4]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MED31]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RNF149]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[BAHD1]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[IQSEC2]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RUFY2]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TUG1]] | -0.62 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.61 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[NFKB1]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NAB1]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[THBS1]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.58 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[PARVA]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SKIL]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[HNRNPA2B1]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[CDK6]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | ITGB8 activity lowers FLYWCH1's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 1.22× higher at baseline in the lines without ITGB8 | 0.061 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[PLEKHF1]] | B | PLEKHF1 activity weakens FLYWCH1's drug response | lines that do not express PLEKHF1 (5) vs lines expressing it (43) | the lines without PLEKHF1 respond 1.62× as strongly (z diff -1.76); rises at some drug-doses, falls at others (55% from rises): Ouabain (Octahydrate) 5 µM: 0.35x vs 0.64x (z diff -3.7); Ixazomib citrate 5 µM: 3.47x vs 2.15x (z diff -2.8); Ixazomib citrate 0.5 µM: 2.49x vs 1.87x (z diff -1.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: E2F1, MCM10, DAGLA; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ALDH2]] | B | ALDH2 activity lowers FLYWCH1's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without ALDH2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[SLC26A11]] | B | SLC26A11 activity raises FLYWCH1's level | lines that do not express SLC26A11 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without SLC26A11 | 0.098 | ⚠ within organs, on part of the lines; also absent: DENND5B, SMAD4, MINAR1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.7, -12.2); signed map (-32.8, -3.1). **Vector** length 115, 28.9% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.4 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.2 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.8 | +9.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.7 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.1 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.3 | -8.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | FLYWCH-type zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,911,931-2,951,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761A132 |
| Gene groups (HGNC) | Zinc fingers; FLYWCH family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4VC44](https://www.uniprot.org/uniprotkb/Q4VC44) (FLYWCH-type zinc finger-containing protein 1):

> Transcription cofactor. Negatively regulates transcription activation by catenin beta-1 CTNNB1, perhaps acting by competing with TCF4 for CTNNB1 binding. May play a role in DNA-damage response signaling. Binds specifically to DNA sequences at peri-centromeric chromatin loci.

**Summary**, from NCBI Gene [84256](https://www.ncbi.nlm.nih.gov/gene/84256):

> Enables transcription coactivator binding activity and transcription corepressor activity. Involved in DNA damage response and negative regulation of transcription by RNA polymerase II. Located in nuclear body and pericentric heterochromatin. Part of transcription regulator complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25404) · Entrez [84256](https://www.ncbi.nlm.nih.gov/gene/84256) · UniProt [Q4VC44](https://www.uniprot.org/uniprotkb/Q4VC44) · Ensembl [ENSG00000059122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059122)

## Data

Gene col 670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 670); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 670]; `tensor/DDL_lfc|DDL_z.npy` [670]; `embed/gene_vectors.npy` [670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 670 or target_col == 670). Every well: [[FLYWCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLYWCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
