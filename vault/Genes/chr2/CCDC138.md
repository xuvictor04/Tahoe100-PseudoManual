---
symbol: "CCDC138"
type: "gene"
col: 8617
ensembl_id: "ENSG00000163006"
name: "coiled-coil domain containing 138"
location: "2q13"
module: 38
arm: "+"
pooled_cpm: 96.71
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CCDC138

*coiled-coil domain containing 138* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.71× (z +10.7, q 7e-24, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 1.43× (z +3.7, q 0.018, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 4 lines (CFPAC-1 3.13×, A-172 2.78×, A549 2.21×, NCI-H2347 2.43×; ⚠ cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 1.84×, NCI-H1792 2.04×; ⚠ cell-cycle shift, explains ~73% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (CFPAC-1 3.14×, A-172 2.69×; ⚠ cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.596× (z -10.4, q 1e-22, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7BP]] (+0.62, fdr 1e-05), [[FAM53A]] (+0.62, fdr 7e-06), [[RRP7BP-1]] (+0.61, fdr 9e-06); moves opposite to [[TCTA]] (-0.51, fdr 1e-04), [[WASHC3]] (-0.50, fdr 3e-05), [[WAC-AS1]] (-0.48, fdr 1e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 4 lines (CFPAC-1 3.13×, A-172 2.78×, A549 2.21×, NCI-H2347 2.43×; ⚠ cell-cycle shift, explains ~44% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 1.84×, NCI-H1792 2.04×; ⚠ cell-cycle shift, explains ~73% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (CFPAC-1 3.14×, A-172 2.69×; ⚠ cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.71×** | +10.7 | 7e-24 | 40/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +9.7 | 7e-20 | 44/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.52×** | +8.3 | 2e-14 | 34/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.51×** | +8.0 | 3e-13 | 35/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.35×** | +6.0 | 2e-07 | 29/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.018 | 23/48 (HOP62, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +3.5 | 0.031 | 18/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.031 | 17/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.5 | 0.031 | 15/48 (A-172, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8617.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -10.4 | 1e-22 | 37/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -10.0 | 6e-21 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.689×** | -7.2 | 1e-10 | 34/47 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -7.1 | 1e-10 | 30/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -6.9 | 5e-10 | 32/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -6.6 | 4e-09 | 32/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.842× | -4.9 | 7e-05 | 23/48 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.786×** | -4.9 | 8e-05 | 29/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.798×** | -4.5 | 3e-04 | 27/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.5 | 3e-04 | 23/48 (A-427, RKO, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.788×** | -4.5 | 3e-04 | 25/47 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.793×** | -4.5 | 3e-04 | 28/47 (HOP62, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.817×** | -4.1 | 0.002 | 24/48 (SW48, A-427, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.818×** | -4.1 | 0.002 | 23/47 (SNU-423, RKO, …) | rises with dose | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.723×** | -3.4 | 0.024 | 17/49 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 0.852× | -3.2 | 0.044 | 8/48 (AsPC-1, LoVo, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.858× | -3.1 | 0.062 | 10/48 (A498, A-172, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.853× | -3.0 | 0.071 | 13/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.354× (z -14.0) |
| [[PANC-1 (line)]] | alt | 87.2 | 1 (1 ⚠) | 7 (3 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 1.90× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~40% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 262 | 0 | 7 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.388× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.413× (z -10.4) |
| [[J82 (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 66.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.252× (z -13.4) |
| [[SW480 (line)]] | alt | 157 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.420× (z -14.5) |
| [[A498 (line)]] | wt | 68.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.250× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 94.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) ⚠ cell-cycle shift, explains ~73% of this change | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 129 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.406× (z -9.7) |
| [[A-172 (line)]] | wt | 80.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[AsPC-1 (line)]] | alt | 64.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.393× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 42.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +10.7) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[H4 (line)]] | wt | 102 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.337× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 74.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0985× (z -17.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.369× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 53.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.2) |
| [[SW1417 (line)]] | alt | 94.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -10.4) |
| [[SW48 (line)]] | wt | 143 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -9.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.381× (z -9.0) |
| [[A-427 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -9.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A549 (line)]] | wt | 70.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +8.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.489× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.367× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.1) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[LS 180 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +8.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[Panc 03.27 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.193× (z -8.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0951× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 99.3 | 0 | 1 | — | [[Mifepristone (drug)]] 5 µM 0.0773× (z -8.5) |
| [[SW 1271 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0797× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 122 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -9.2) |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FAM53A]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RRP7BP-1]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[EP400P1]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[IL20RB]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PYGM]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ORC2]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RFPL3S]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CHAF1B]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CUZD1]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[MRPS28]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTA]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[WASHC3]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[WAC-AS1]] | -0.48 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[CYLD]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 | same gene group |
| [[ATP6V1C1]] | -0.47 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[UPK2]] | -0.47 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[CPEB2]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TRAPPC6B]] | -0.47 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[OPTN]] | -0.47 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SGO1-AS1]] | -0.46 | -0.21 / -0.47 | both halves | 6e-04 |  |
| [[IGF2R]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ZHX1]] | -0.46 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CCDC138's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.1, -23.2); signed map (-51.2, -1.7). **Vector** length 130, 40.5% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +8.5 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.7 | +9.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.4 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | -10.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.7 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.9 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 138 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:108,786,757-108,885,477 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32745 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

UniProt [Q96M89](https://www.uniprot.org/uniprotkb/Q96M89) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26531) · Entrez [165055](https://www.ncbi.nlm.nih.gov/gene/165055) · UniProt [Q96M89](https://www.uniprot.org/uniprotkb/Q96M89) · Ensembl [ENSG00000163006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163006)

## Data

Gene col 8617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8617); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8617]; `tensor/DDL_lfc|DDL_z.npy` [8617]; `embed/gene_vectors.npy` [8617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8617 or target_col == 8617). Every well: [[CCDC138 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC138.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
