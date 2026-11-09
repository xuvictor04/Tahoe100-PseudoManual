---
symbol: "NBN"
type: "gene"
col: 2438
ensembl_id: "ENSG00000104320"
name: "nibrin"
location: "8q21.3"
module: 28
arm: "+"
pooled_cpm: 71.79
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NBN

*nibrin* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.59× (z +10.3, q 5e-22, up in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.57× (z +10.1, q 3e-21, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.376× (z -30.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5]] (+0.72, fdr 7e-06), [[ZNF678]] (+0.69, fdr 7e-06), [[DCLRE1A]] (+0.69, fdr 7e-06); moves opposite to [[TPTEP2-CSNK1E]] (-0.69, fdr 7e-06), [[MARK4]] (-0.68, fdr 1e-05), [[CSNK1G2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +10.3 | 5e-22 | 38/49 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +10.1 | 3e-21 | 38/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +9.0 | 3e-17 | 30/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.4 | 7e-15 | 27/44 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.4 | 7e-15 | 36/47 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +7.6 | 3e-12 | 34/48 (A498, A-172, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.4 | 4e-06 | 25/47 (C32, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.15× | +4.3 | 0.001 | 20/48 (J82, BT-474, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.3 | 0.001 | 20/45 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 18/48 (C32, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +4.0 | 0.004 | 9/48 (AsPC-1, BT-474, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.004 | 15/48 (C32, J82, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.022 | 8/49 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.071 | 12/48 (NCI-H2347, SW1417, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.376×** | -30.7 | 0e+00 | 48/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.487×** | -15.9 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.500×** | -15.4 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -15.3 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.518×** | -14.6 | 0e+00 | 44/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.522×** | -14.4 | 3e-45 | 46/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.670×** | -12.6 | 3e-34 | 37/48 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -11.8 | 2e-30 | 39/48 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -11.4 | 2e-28 | 38/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -11.2 | 3e-27 | 42/49 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -9.7 | 2e-20 | 40/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -8.6 | 3e-16 | 37/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -8.2 | 7e-15 | 36/48 (NCI-H23, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.707×** | -7.7 | 7e-13 | 34/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.728×** | -6.7 | 8e-10 | 37/48 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.766×** | -5.7 | 4e-07 | 26/47 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 96.6 | 0 | 13 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -30.6) |
| [[A498 (line)]] | wt | 157 | 4 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 108 | 6 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -11.3) |
| [[RKO (line)]] | wt | 131 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -15.6) |
| [[LoVo (line)]] | wt | 61.7 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -21.7) |
| [[NCI-H460 (line)]] | wt | 65.9 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -25.6) |
| [[SNU-1 (line)]] | wt | 106 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0799× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -17.0) |
| [[SW480 (line)]] | alt | 57.7 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.02× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -20.8) |
| [[A549 (line)]] | wt | 116 | 1 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) ⚠ cell-cycle shift, explains ~73% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -26.8) |
| [[HS-578T (line)]] | alt | 110 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -17.4) |
| [[J82 (line)]] | alt | 53.0 | 4 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.50× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 71.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 54.1 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.3) |
| [[SW1417 (line)]] | alt | 56.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -14.9) |
| [[C-33 A (line)]] | alt | 81.0 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -18.9) |
| [[CFPAC-1 (line)]] | alt | 64.4 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.3) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -8.9) |
| [[HOP62 (line)]] | alt | 61.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 47.9 | 2 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 7.41× (z +9.8) ⚠ cell-cycle shift, explains ~20% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.8) |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.6) |
| [[SW48 (line)]] | wt | 67.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -14.8) |
| [[A-172 (line)]] | wt | 30.1 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.02× (z +11.1) | — |
| [[A-427 (line)]] | wt | 82.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.448× (z -9.8) |
| [[BT-474 (line)]] | alt | 68.2 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.6) ⚠ cell-cycle shift, explains ~73% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.3) |
| [[HT-29 (line)]] | alt | 37.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.238× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 69.9 | 1 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 10.6× (z +11.0) ⚠ cell-cycle shift, explains ~20% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 59.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 48.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.374× (z -8.6) |
| [[H4 (line)]] | wt | 58.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 61.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 60.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -17.8) |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.2) |
| [[SW 1271 (line)]] | alt | 60.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -10.7) |
| [[C32 (line)]] | wt | 52.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -12.3) |
| [[COLO 205 (line)]] | alt | 54.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.5) |
| [[HCT15 (line)]] | alt | 65.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 27.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.0) |
| [[Hs 766T (line)]] | wt | 74.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 51.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.2) |
| [[KATO III (line)]] | alt | 45.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 65.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.7) |
| [[LS 180 (line)]] | wt | 51.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.1) |
| [[SW 900 (line)]] | alt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.4) |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[ZNF678]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[DDX1]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[CCDC25]] | +0.66 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[COMMD8]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.66 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[C12orf29]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | -0.69 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[MARK4]] | -0.68 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[CSNK1G2]] | -0.68 | -0.60 / -0.69 | both halves | 7e-06 |  |
| [[RABGEF1]] | -0.64 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[ZNHIT1]] | -0.63 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[UBL5]] | -0.62 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[CDC34]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[NEDD8]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[DRD4]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[MROH1]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[FAAP20]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PITPNA]] | -0.59 | -0.66 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NBN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.3, 1.5); signed map (4.9, -35.4). **Vector** length 133, 41.8% of its response variance represented; |z| ≥ 3 in 1,483 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.4 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +12.3 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +7.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.5 | +7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.4 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -30.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.8 | -11.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.6 | -14.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -15.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.4 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.7 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -12.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | nibrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:89,924,515-90,003,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATV, AT-V2, AT-V1; previously NBS, NBS1 |
| Gene groups (HGNC) | BRCA1 C complex; MRN complex |
| Hallmark sets | FATTY_ACID_METABOLISM, E2F_TARGETS |
| Reactome | 40 pathways, smallest: Sensing of DNA Double Strand Breaks; HDR through MMEJ (alt-NHEJ); Impaired BRCA2 binding to PALB2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60934](https://www.uniprot.org/uniprotkb/O60934) (Nibrin):

> Component of the MRN complex, which plays a central role in double-strand break (DSB) repair, DNA recombination, maintenance of telomere integrity and meiosis. The MRN complex is involved in the repair of DNA double-strand breaks (DSBs) via homologous recombination (HR), an error-free mechanism which primarily occurs during S and G2 phases. The complex (1) mediates the end resection of damaged DNA, which generates proper single-stranded DNA, a key initial steps in HR, and is (2) required for …

**Summary**, from NCBI Gene [4683](https://www.ncbi.nlm.nih.gov/gene/4683):

> Mutations in this gene are associated with Nijmegen breakage syndrome, an autosomal recessive chromosomal instability syndrome characterized by microcephaly, growth retardation, immunodeficiency, and cancer predisposition. The encoded protein is a member of the MRE11/RAD50 double-strand break repair complex which consists of 5 proteins. This gene product is thought to be involved in DNA double-strand break repair and DNA damage-induced checkpoint activation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7652) · Entrez [4683](https://www.ncbi.nlm.nih.gov/gene/4683) · UniProt [O60934](https://www.uniprot.org/uniprotkb/O60934) · Ensembl [ENSG00000104320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104320)

## Data

Gene col 2438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2438); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2438]; `tensor/DDL_lfc|DDL_z.npy` [2438]; `embed/gene_vectors.npy` [2438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2438 or target_col == 2438). Every well: [[NBN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
