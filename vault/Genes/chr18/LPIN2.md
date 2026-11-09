---
symbol: "LPIN2"
type: "gene"
col: 2155
ensembl_id: "ENSG00000101577"
name: "lipin 2"
location: "18p11.31"
module: 79
arm: "+"
pooled_cpm: 120.58
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# LPIN2

*lipin 2* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.27× (z +5.0, q 4e-04, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H460 2.23×, HOP62 1.97×, J82 1.89×, Hs 766T 2.07×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.61×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 1.71×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.397× (z -17.9, q 0e+00, down in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.769× (z -5.3, q 1e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HA1]] (+0.66, fdr 7e-06), [[SAP30]] (+0.60, fdr 1e-05), [[POR]] (+0.59, fdr 1e-05); moves opposite to [[ZNF839]] (-0.55, fdr 1e-05), [[ZNF239]] (-0.50, fdr 2e-05), [[NAA25]] (-0.50, fdr 2e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2155.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (NCI-H460 2.23×, HOP62 1.97×, J82 1.89×, Hs 766T 2.07×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 2.61×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 1.71×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +5.0 | 4e-04 | 24/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.16 | 19/48 (NCI-H460, HOP62, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.16 | 21/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.22× | +3.0 | 0.29 | 16/48 (NCI-H1792, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.29 | 9/48 (PANC-1, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.397×** | -17.9 | 0e+00 | 43/45 (C32, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -16.0 | 0e+00 | 43/44 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.473×** | -15.7 | 0e+00 | 44/49 (HT-29, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -9.8 | 1e-20 | 44/47 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -6.8 | 1e-09 | 35/47 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -5.3 | 1e-05 | 28/48 (C32, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.668×** | -4.4 | 8e-04 | 27/48 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -4.2 | 0.002 | 19/48 (NCI-H2347, C32, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.682×** | -4.2 | 0.002 | 23/45 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -4.1 | 0.002 | 16/48 (A-172, NCI-H661, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.698×** | -3.9 | 0.004 | 21/49 (LS 180, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.830×** | -3.9 | 0.005 | 21/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.010 | 18/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.7 | 0.010 | 22/48 (HT-29, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.841× | -3.6 | 0.010 | 22/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.857× | -3.2 | 0.033 | 18/48 (HepG2/C3A, SHP-77, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.045 | 17/48 (C-33 A, NCI-H1573, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.872× | -2.9 | 0.096 | 12/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.866× | -2.8 | 0.099 | 11/47 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 158 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0939× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.400× (z -10.4) |
| [[HT-29 (line)]] | alt | 354 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -20.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 156 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -17.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 79.1 | 0 | 6 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.331× (z -14.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 5 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.494× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 134 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -20.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 268 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -15.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 260 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 65.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -17.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 216 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -21.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.124× (z -13.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 198 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -17.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 74.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.401× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 85.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.318× (z -12.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 103 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -15.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 69.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.116× (z -10.8) |
| [[SW 900 (line)]] | alt | 145 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -15.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 126 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 124 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.323× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.105× (z -25.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -12.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -12.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 98.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.414× (z -8.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 90.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -13.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 85.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HA1]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SAP30]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[POR]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[ARFGEF3]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SNX14]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[FUT11]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[USP28]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[WDR45B]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SMAP1]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KDM4B]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF839]] | -0.55 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ZNF239]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[NAA25]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[U2SURP]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[RBM45]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SMG7]] | -0.50 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[DHX9]] | -0.50 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CNOT6]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EWSR1]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF502]] | -0.48 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[ZFP41]] | -0.48 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ALKBH8]] | -0.48 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, -17.4); signed map (-33.4, 25.5). **Vector** length 117, 33.5% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.9 | +3.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -6.8 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.2 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -9.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -17.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | lipin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:2,885,296-3,013,144 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0249 |
| Gene groups (HGNC) | Lipins |
| Hallmark sets | XENOBIOTIC_METABOLISM, HEME_METABOLISM |
| Reactome | 13 pathways, smallest: Triglyceride biosynthesis; Synthesis of PE; Depolymerization of the Nuclear Lamina |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92539](https://www.uniprot.org/uniprotkb/Q92539) (Phosphatidate phosphatase LPIN2):

> Acts as a magnesium-dependent phosphatidate phosphatase enzyme which catalyzes the conversion of phosphatidic acid to diacylglycerol during triglyceride, phosphatidylcholine and phosphatidylethanolamine biosynthesis in the endoplasmic reticulum membrane. Plays important roles in controlling the metabolism of fatty acids at different levels. Also acts as a nuclear transcriptional coactivator for PPARGC1A to modulate lipid metabolism.

**Summary**, from NCBI Gene [9663](https://www.ncbi.nlm.nih.gov/gene/9663):

> Mouse studies suggest that this gene functions during normal adipose tissue development and may play a role in human triglyceride metabolism. This gene represents a candidate gene for human lipodystrophy, characterized by loss of body fat, fatty liver, hypertriglyceridemia, and insulin resistance. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14450) · Entrez [9663](https://www.ncbi.nlm.nih.gov/gene/9663) · UniProt [Q92539](https://www.uniprot.org/uniprotkb/Q92539) · Ensembl [ENSG00000101577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101577)

## Data

Gene col 2155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2155); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2155]; `tensor/DDL_lfc|DDL_z.npy` [2155]; `embed/gene_vectors.npy` [2155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2155 or target_col == 2155). Every well: [[LPIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
