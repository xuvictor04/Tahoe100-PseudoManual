---
symbol: "TOPBP1"
type: "gene"
col: 8775
ensembl_id: "ENSG00000163781"
name: "DNA topoisomerase II binding protein 1"
location: "3q22.1"
module: 71
arm: "+"
pooled_cpm: 100.79
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# TOPBP1

*DNA topoisomerase II binding protein 1* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.12× (z +9.2, q 2e-17, up in 0 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.25× (z +5.7, q 3e-06, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 2.38×, A549 2.68×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -22.0, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTBP]] (+0.82, fdr 7e-06), [[RRM1]] (+0.80, fdr 7e-06), [[RFC3]] (+0.80, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 2.38×, A549 2.68×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +9.2 | 2e-17 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.7 | 3e-06 | 26/48 (HS-578T, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.3 | 2e-05 | 26/49 (J82, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.19× | +4.4 | 0.001 | 20/48 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.16× | +3.7 | 0.022 | 16/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.6 | 0.034 | 13/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.16× | +3.5 | 0.034 | 13/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.16× | +3.5 | 0.034 | 19/45 (SHP-77, A549, …) | inconsistent across doses | composition shift |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.11× | +3.4 | 0.050 | 6/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.14× | +3.3 | 0.050 | 10/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.3 | 0.050 | 15/38 (NCI-H2030, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.065 | 11/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.13× | +3.0 | 0.10 | 7/48 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.31× | +3.0 | 0.10 | 13/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.528×** | -22.0 | 0e+00 | 41/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.653×** | -14.1 | 1e-42 | 46/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.594×** | -13.2 | 9e-38 | 47/49 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.644×** | -11.2 | 6e-27 | 38/48 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.633×** | -11.2 | 6e-27 | 37/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.668×** | -10.3 | 1e-22 | 37/48 (KATO III, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -9.9 | 5e-21 | 34/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.689×** | -9.5 | 1e-19 | 38/48 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -8.0 | 6e-14 | 30/48 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.789×** | -6.0 | 9e-08 | 28/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -5.5 | 2e-06 | 20/49 (A498, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.824×** | -5.0 | 3e-05 | 25/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -4.8 | 8e-05 | 24/49 (A-172, CHP-212, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.883× | -4.2 | 9e-04 | 12/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.866× | -3.7 | 0.009 | 13/48 (SW 1088, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.725×** | -3.6 | 0.010 | 19/49 (SHP-77, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 134 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -19.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 164 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -16.1) |
| [[SW480 (line)]] | alt | 138 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 72.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.8) |
| [[KATO III (line)]] | alt | 131 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -12.7) |
| [[LS 180 (line)]] | wt | 80.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.6) |
| [[A-172 (line)]] | wt | 96.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.2) |
| [[C32 (line)]] | wt | 82.6 | 0 | 4 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.332× (z -12.1) |
| [[COLO 205 (line)]] | alt | 103 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.4) |
| [[HOP62 (line)]] | alt | 72.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.3) |
| [[HS-578T (line)]] | alt | 90.0 | 0 | 3 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.418× (z -10.3) |
| [[J82 (line)]] | alt | 154 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -21.9) |
| [[NCI-H2347 (line)]] | alt | 79.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.482× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 3 | — | [[Tucidinostat (drug)]] 0.5 µM 0.463× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -13.3) |
| [[SHP-77 (line)]] | alt | 148 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.38× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.489× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -14.5) |
| [[SNU-423 (line)]] | alt | 65.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.2) |
| [[A-427 (line)]] | wt | 173 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.441× (z -13.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.7) |
| [[HCT15 (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.6) |
| [[PANC-1 (line)]] | alt | 130 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.494× (z -10.5) |
| [[SW 900 (line)]] | alt | 67.4 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.399× (z -9.3) |
| [[A549 (line)]] | wt | 54.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.68× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.9) |
| [[C-33 A (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 62.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.6) |
| [[H4 (line)]] | wt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -8.8) |
| [[Hs 766T (line)]] | wt | 59.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -8.8) |
| [[HT-29 (line)]] | alt | 65.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.8) |
| [[LoVo (line)]] | wt | 78.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 58.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 58.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -11.2) |
| [[RKO (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 86.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.1) |
| [[SW 1271 (line)]] | alt | 110 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.143× (z -9.7) |
| [[SW1417 (line)]] | alt | 107 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -9.5) |
| [[BT-474 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTBP]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | STRING 866 |
| [[RRM1]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 | STRING 455 |
| [[RFC3]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 785 |
| [[ZNF519]] | +0.79 | +0.71 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MCM8]] | +0.79 | +0.75 / +0.78 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 444 |
| [[MMS22L]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 | STRING 413 |
| [[ORC1]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[CENPO]] | +0.78 | +0.79 / +0.78 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[FANCD2]] | +0.77 | +0.73 / +0.80 | both halves | 7e-06 | STRING 765 |
| [[POLQ]] | +0.77 | +0.77 / +0.76 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 408 |
| [[ATAD5]] | +0.77 | +0.73 / +0.75 | both halves | 7e-06 | STRING 672 |
| [[FANCI]] | +0.77 | +0.79 / +0.78 | both halves | 7e-06 | STRING 752 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TOPBP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TOPBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises TOPBP1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without DSCC1 | 0.036 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ITGB3BP]] | C | ITGB3BP's natural level strengthens TOPBP1's drug response | ITGB3BP's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.13; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.7, -47.4); signed map (-40.0, -42.4). **Vector** length 138, 45.1% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metabolism of non-coding RNA* (reactome, mean cos +0.51 to 5); *snRNP Assembly* (reactome, mean cos +0.51 to 5); *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +5.2 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -0.1 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.1 | +4.4 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.0 | +3.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -0.5 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.0 | -14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.0 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -22.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -5.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase II binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:133,598,175-133,662,380 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0259, TOP2BP1, Dpb11 |
| Gene groups (HGNC) | BRCA1 B complex |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 20 pathways, smallest: Impaired BRCA2 binding to RAD51; HDR through Single Strand Annealing (SSA); Presynaptic phase of homologous DNA pairing and strand exchange |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92547](https://www.uniprot.org/uniprotkb/Q92547) (DNA topoisomerase 2-binding protein 1):

> Scaffold protein that acts as a key protein-protein adapter in DNA replication and DNA repair. Composed of multiple BRCT domains, which specifically recognize and bind phosphorylated proteins, bringing proteins together into functional combinations. Required for DNA replication initiation but not for the formation of pre-replicative complexes or the elongation stages (By similarity). Necessary for the loading of replication factors onto chromatin, including GMNC, CDC45, DNA polymerases and …

**Summary**, from NCBI Gene [11073](https://www.ncbi.nlm.nih.gov/gene/11073):

> This gene encodes a binding protein which interacts with the C-terminal region of topoisomerase II beta. This interaction suggests a supportive role for this protein in the catalytic reactions of topoisomerase II beta through transient breakages of DNA strands. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17008) · Entrez [11073](https://www.ncbi.nlm.nih.gov/gene/11073) · UniProt [Q92547](https://www.uniprot.org/uniprotkb/Q92547) · Ensembl [ENSG00000163781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163781)

## Data

Gene col 8775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8775); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8775]; `tensor/DDL_lfc|DDL_z.npy` [8775]; `embed/gene_vectors.npy` [8775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8775 or target_col == 8775). Every well: [[TOPBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOPBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
