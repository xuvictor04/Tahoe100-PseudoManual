---
symbol: "MUC20-OT1"
type: "gene"
col: 14301
ensembl_id: "ENSG00000242086"
name: "MUC20 overlapping transcript"
location: "3q29"
module: 38
arm: "+"
pooled_cpm: 75.24
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# MUC20-OT1

*MUC20 overlapping transcript* — 3q29

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 2.75×, NCI-H23 2.32×, RKO 3.03×, PANC-1 2.03×, …; ⚠ cell-cycle shift, explains ~2% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 4.14×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 2.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -11.6, q 4e-28, down in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.500× (z -9.6, q 9e-20, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMBD1P]] (+0.88, fdr 7e-06, ⚠ same locus), [[SLC23A3]] (+0.67, fdr 7e-06), [[TNXB]] (+0.67, fdr 7e-06), [[APRG1]] (+0.66, fdr 7e-06); moves opposite to [[LANCL1]] (-0.55, fdr 1e-05), [[COMMD8]] (-0.55, fdr 2e-05), [[DUSP19]] (-0.55, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14301.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 2.75×, NCI-H23 2.32×, RKO 3.03×, PANC-1 2.03×, …; ⚠ cell-cycle shift, explains ~2% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 4.14×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 2.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +3.6 | 0.15 | 22/49 (NCI-H460, NCI-H23, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.27× | +3.3 | 0.21 | 23/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.26× | +3.2 | 0.21 | 18/48 (A498, Panc 03.27, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.55× | +3.2 | 0.21 | 20/49 (HCT15, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.21 | 19/48 (HT-29, SNU-423, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.21 | 19/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.554×** | -11.6 | 4e-28 | 38/47 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.459×** | -10.8 | 1e-24 | 38/47 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.478×** | -9.8 | 1e-20 | 43/48 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.500×** | -9.6 | 9e-20 | 38/48 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.268×** | -9.5 | 2e-19 | 44/49 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.513×** | -9.2 | 2e-18 | 39/48 (NCI-H1573, BT-474, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.576×** | -7.3 | 2e-11 | 35/47 (COLO 205, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.391×** | -6.8 | 7e-10 | 36/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.632×** | -6.3 | 1e-08 | 31/47 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -4.8 | 8e-05 | 31/48 (COLO 205, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -4.5 | 3e-04 | 32/48 (RPMI-7951, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.750×** | -4.0 | 0.003 | 27/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.004 | 24/48 (C32, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **0.766×** | -3.7 | 0.009 | 22/48 (COLO 205, J82, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -3.4 | 0.027 | 23/48 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.073 | 22/49 (SW 1088, RKO, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 606 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.432× (z -9.4) |
| [[LS 180 (line)]] | wt | 80.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -14.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.333× (z -10.8) |
| [[BT-474 (line)]] | alt | 129 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -14.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 223 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -19.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.170× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 120 | 1 (1 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -21.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.158× (z -9.4) |
| [[SW480 (line)]] | alt | 78.8 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.324× (z -13.4) |
| [[A549 (line)]] | wt | 57.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.143× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 63.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.322× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 131 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -25.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.139× (z -9.7) |
| [[J82 (line)]] | alt | 115 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 64.3 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 55.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.7) ⚠ cell-cycle shift, explains ~2% of this change | [[Harringtonine (drug)]] 0.5 µM 0.264× (z -10.3) |
| [[H4 (line)]] | wt | 69.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.196× (z -10.8) |
| [[A-427 (line)]] | wt | 37.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.326× (z -9.5) |
| [[A498 (line)]] | wt | 63.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.277× (z -9.0) |
| [[HOP62 (line)]] | alt | 86.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H1792 (line)]] | alt | 73.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 22.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.4) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 25.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.5) ⚠ cell-cycle shift, explains ~2% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -12.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 69.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HCT15 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.104× (z -8.6) |
| [[HT-29 (line)]] | alt | 43.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.8) ⚠ cell-cycle shift, explains ~58% of this change |
| [[KATO III (line)]] | alt | 71.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.134× (z -9.5) |
| [[LoVo (line)]] | wt | 100 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.333× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 50.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.8) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[RKO (line)]] | wt | 24.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +9.8) ⚠ cell-cycle shift, explains ~2% of this change | [[Harringtonine (drug)]] 5 µM 0.201× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 76.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 61.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.4) ⚠ cell-cycle shift, explains ~58% of this change |
| [[hTERT-HPNE (line)]] | wt | 62.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 33.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.247× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 72.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SNU-423 (line)]] | alt | 67.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0960× (z -9.1) |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMBD1P]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SLC23A3]] | +0.67 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[TNXB]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[APRG1]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[UBE2CP5]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[EOLA2-DT]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SLC22A20P]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ZNF586]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DNHD1]] | +0.64 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[TRPV1]] | +0.62 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[GABRR2]] | +0.61 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TMEM236]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1]] | -0.55 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[COMMD8]] | -0.55 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[DUSP19]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[DIXDC1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[C2CD5]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TRAPPC11]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NBN]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PRTG]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[AADAT]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A30]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[HPF1]] | -0.51 | -0.51 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.2, -19.8); signed map (10.6, 7.6). **Vector** length 96.7, 28.5% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.9 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +0.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | -0.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.4 | -9.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MUC20 overlapping transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q29 — chr3:195,658,062-195,739,964 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MUCP1 |
| Gene groups (HGNC) | Overlapping transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53807) · Entrez [111753249](https://www.ncbi.nlm.nih.gov/gene/111753249) · Ensembl [ENSG00000242086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242086)

## Data

Gene col 14301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14301); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14301]; `tensor/DDL_lfc|DDL_z.npy` [14301]; `embed/gene_vectors.npy` [14301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14301 or target_col == 14301). Every well: [[MUC20-OT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC20-OT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
