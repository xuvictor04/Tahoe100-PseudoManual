---
symbol: "ANKFY1"
type: "gene"
col: 11721
ensembl_id: "ENSG00000185722"
name: "ankyrin repeat and FYVE domain containing 1"
location: "17p13.2"
module: 32
arm: "+"
pooled_cpm: 84.31
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ANKFY1

*ankyrin repeat and FYVE domain containing 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +9.5, q 9e-19, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.79× (z +6.3, q 2e-08, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.552× (z -12.4, q 1e-32, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.605× (z -10.5, q 2e-23, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A28]] (+0.67, fdr 7e-06), [[TRIM14]] (+0.67, fdr 7e-06), [[PNPT1]] (+0.66, fdr 7e-06); moves opposite to [[GNG7]] (-0.50, fdr 3e-05), [[CD72]] (-0.48, fdr 4e-05), [[TDRP]] (-0.46, fdr 5e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.57×** | +9.5 | 9e-19 | 44/48 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.57×** | +9.5 | 9e-19 | 41/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +9.0 | 4e-17 | 30/49 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.47×** | +7.7 | 2e-12 | 40/48 (C32, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +6.3 | 2e-08 | 34/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +5.7 | 1e-06 | 27/49 (RPMI-7951, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.32×** | +5.6 | 1e-06 | 31/50 (C32, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.4 | 5e-06 | 18/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.25×** | +4.7 | 1e-04 | 24/48 (SW480, HCT15, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 23/47 (A549, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.22×** | +4.1 | 0.002 | 25/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.21×** | +3.9 | 0.004 | 21/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.19× | +3.6 | 0.015 | 14/49 (A-172, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.044 | 13/47 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +3.2 | 0.045 | 15/48 (A-172, HS-578T, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.056 | 7/48 (AsPC-1, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.552×** | -12.4 | 1e-32 | 40/49 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -12.2 | 1e-31 | 37/43 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.605×** | -10.5 | 2e-23 | 43/48 (RKO, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.621×** | -9.2 | 6e-18 | 40/45 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -7.7 | 1e-12 | 33/47 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.819×** | -5.9 | 4e-07 | 23/48 (A549, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.841× | -5.1 | 3e-05 | 24/49 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.842× | -5.0 | 3e-05 | 22/49 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 0.843× | -5.0 | 3e-05 | 22/48 (SW1417, A-172, …) | rises with dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.794×** | -4.8 | 9e-05 | 28/48 (A549, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.829×** | -3.9 | 0.005 | 23/49 (RPMI-7951, SK-MEL-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.006 | 23/48 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.006 | 24/49 (A-172, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.887× | -3.5 | 0.018 | 11/49 (RKO, SNU-1, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.733×** | -3.4 | 0.027 | 18/48 (COLO 205, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.057 | 18/49 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.865× | -3.0 | 0.081 | 10/48 (A-172, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 98.2 | 3 (3 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +12.8) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -11.0) |
| [[A549 (line)]] | wt | 162 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.590× (z -9.6) |
| [[LoVo (line)]] | wt | 97.2 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.365× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 92.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -17.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 117 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.4) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -9.0) |
| [[HT-29 (line)]] | alt | 50.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -8.9) |
| [[HS-578T (line)]] | alt | 85.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.271× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 94.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -20.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 78.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -12.7) |
| [[A498 (line)]] | wt | 114 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.1) ⚠ cell-cycle shift, explains ~97% of this change |
| [[C-33 A (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -14.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 81.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -12.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 93.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.364× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 57.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -11.4) |
| [[RKO (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.310× (z -12.8) |
| [[SNU-423 (line)]] | alt | 75.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.352× (z -11.0) |
| [[SW1417 (line)]] | alt | 72.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -14.2) ⚠ cell-cycle shift, explains ~97% of this change |
| [[AsPC-1 (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.323× (z -10.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 64.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.306× (z -8.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 69.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.369× (z -9.2) |
| [[SHP-77 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -18.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -10.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A28]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TRIM14]] | +0.67 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[PNPT1]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PML]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[TAP2]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[UBE2L6]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SAMHD1]] | +0.63 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[OAS3]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[PARP9]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[OAS2]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[CMPK2]] | +0.62 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[USP18]] | +0.61 | +0.47 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG7]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CD72]] | -0.48 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[TDRP]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity weakens ANKFY1's drug response | lines that do not express OAS1 (13) vs lines expressing it (36) | the lines without OAS1 respond 0.85× as strongly (z diff +0.65); strongest at Panobinostat 0.5 µM: 1.77x vs 1.45x (z diff -2.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ANKFY1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.5, 55.2); signed map (65.7, 33.3). **Vector** length 120, 37.1% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.51 to 56); *interferon gamma response* (hallmark, mean cos +0.52 to 60); *interferon* (control, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.9 | +7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +4.4 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -9.6 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.4 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.9 | -10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.2 | -5.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and FYVE domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,163,821-4,263,995 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ANKHZN, KIAA1255, ZFYVE14, BTBD23, RANK-5 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Ankyrin repeat domain containing; BTB domain containing |
| Reactome | 4 pathways, smallest: RHOD GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2R3](https://www.uniprot.org/uniprotkb/Q9P2R3) (Ankyrin repeat and FYVE domain-containing protein 1):

> Proposed effector of Rab5. Binds to phosphatidylinositol 3-phosphate (PI[3]P). Involved in homotypic early endosome fusion and to a lesser extent in heterotypic fusion of clathrin-coated vesicles with early endosomes. Involved in macropinocytosis; the function is dependent on Rab5-GTP. Required for correct endosomal localization. Involved in the internalization and trafficking of activated tyrosine kinase receptors such as PDGFRB. Regulates the subcellular localization of the retromer complex …

**Summary**, from NCBI Gene [51479](https://www.ncbi.nlm.nih.gov/gene/51479):

> This gene encodes a cytoplasmic protein that contains a coiled-coil structure and a BTB/POZ domain at its N-terminus, ankyrin repeats in the middle portion, and a FYVE-finger motif at its C-terminus. This protein belongs to a subgroup of double zinc finger proteins which may be involved in vesicle or protein transport. Alternate splicing results in multiple transcript variants of this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:20763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20763) · Entrez [51479](https://www.ncbi.nlm.nih.gov/gene/51479) · UniProt [Q9P2R3](https://www.uniprot.org/uniprotkb/Q9P2R3) · Ensembl [ENSG00000185722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185722)

## Data

Gene col 11721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11721); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11721]; `tensor/DDL_lfc|DDL_z.npy` [11721]; `embed/gene_vectors.npy` [11721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11721 or target_col == 11721). Every well: [[ANKFY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKFY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
