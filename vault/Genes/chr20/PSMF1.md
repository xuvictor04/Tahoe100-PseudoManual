---
symbol: "PSMF1"
type: "gene"
col: 4667
ensembl_id: "ENSG00000125818"
name: "proteasome inhibitor subunit 1"
location: "20p13"
module: 30
arm: "+"
pooled_cpm: 89.5
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PSMF1

*proteasome inhibitor subunit 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.72× (z +5.7, q 6e-06, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.713× (z -9.6, q 3e-19, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H2347 0.431×, AsPC-1 0.431×, LOX-IMVI 0.480×, A549 0.553×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.447×, SNU-423 0.433×, A-172 0.462×; ⚠ cell-cycle shift, explains ~40% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 0.317×, RKO 0.254×, A-172 0.373×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.512×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK5RAP1]] (+0.75, fdr 7e-06), [[MED9]] (+0.71, fdr 7e-06), [[DNAJC24]] (+0.68, fdr 7e-06); moves opposite to [[FOSB]] (-0.60, fdr 1e-05), [[SEMA4A]] (-0.60, fdr 1e-05), [[TLE4]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +5.7 | 6e-06 | 32/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +5.0 | 1e-04 | 28/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 0.002 | 26/48 (PANC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.086 | 21/48 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +3.3 | 0.11 | 20/48 (COLO 205, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4667.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H2347 0.431×, AsPC-1 0.431×, LOX-IMVI 0.480×, A549 0.553×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.447×, SNU-423 0.433×, A-172 0.462×; ⚠ cell-cycle shift, explains ~40% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HOP62 0.317×, RKO 0.254×, A-172 0.373×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (HOP62 0.512×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -9.6 | 3e-19 | 33/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.732×** | -8.9 | 2e-16 | 31/48 (A498, SNU-423, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.654×** | -8.2 | 3e-14 | 33/44 (SNU-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.670×** | -8.1 | 1e-13 | 35/49 (COLO 205, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -6.0 | 3e-07 | 25/48 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.742×** | -5.8 | 7e-07 | 29/47 (C32, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.761×** | -5.3 | 1e-05 | 31/48 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.776×** | -4.9 | 7e-05 | 29/50 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.807×** | -4.0 | 0.004 | 24/45 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.834× | -3.6 | 0.015 | 20/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.836× | -3.6 | 0.017 | 23/48 (SW1417, A-172, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.2 | 0.069 | 1/50 (NCI-H2122) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 90.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.3) |
| [[HOP62 (line)]] | alt | 117 | 0 | 7 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -14.5) |
| [[BT-474 (line)]] | alt | 97.0 | 2 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -16.9) |
| [[A549 (line)]] | wt | 139 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -12.6) |
| [[C32 (line)]] | wt | 64.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HS-578T (line)]] | alt | 97.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 90.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 99.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 94.9 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.93× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -13.4) |
| [[A498 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -14.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 80.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 95.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.2) |
| [[CHP-212 (line)]] | wt | 75.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -8.5) |
| [[COLO 205 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HCT15 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.6) |
| [[Hs 766T (line)]] | wt | 84.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 71.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -10.0) |
| [[J82 (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 96.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 92.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.407× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H661 (line)]] | alt | 76.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0932× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SNU-1 (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SNU-423 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -14.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 78.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 60.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.568× (z -9.7) |
| [[SW480 (line)]] | alt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.03× (z +9.5) | — |
| [[A-427 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK5RAP1]] | +0.75 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[MED9]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[DNAJC24]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ZNF322]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ZNF875]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[TRIP4]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[MAFIP]] | +0.63 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[CDADC1]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[NUDCD3]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF133]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF112]] | +0.61 | +0.68 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSB]] | -0.60 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SEMA4A]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[TLE4]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CHD4]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PIK3R3]] | -0.57 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[TEX14]] | -0.55 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[HES1]] | -0.54 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PEAK1]] | -0.54 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[RFX3]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PSMF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF461]] | B | ZNF461 activity raises PSMF1's level | lines that do not express ZNF461 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without ZNF461 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF567, ZNF529-AS1, ZNF571 |
| [[NR4A3]] | B | NR4A3 activity lowers PSMF1's level | lines that do not express NR4A3 (6) vs lines expressing it (44) | 1.22× higher at baseline in the lines without NR4A3 | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC4A7, SLC16A1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-30.6, -6.3); signed map (-16.5, -19.4). **Vector** length 92.5, 22.3% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.6 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.4 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.0 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.5 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.4 | -8.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -4.3 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome inhibitor subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,113,240-1,189,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PI31 |
| Gene groups (HGNC) | Proteasome |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92530](https://www.uniprot.org/uniprotkb/Q92530) (Proteasome inhibitor PI31 subunit):

> Plays an important role in control of proteasome function. Inhibits the hydrolysis of protein and peptide substrates by the 20S proteasome. Also inhibits the activation of the proteasome by the proteasome regulatory proteins PA700 and PA28.

**Summary**, from NCBI Gene [9491](https://www.ncbi.nlm.nih.gov/gene/9491):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9571) · Entrez [9491](https://www.ncbi.nlm.nih.gov/gene/9491) · UniProt [Q92530](https://www.uniprot.org/uniprotkb/Q92530) · Ensembl [ENSG00000125818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125818)

## Data

Gene col 4667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4667); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4667]; `tensor/DDL_lfc|DDL_z.npy` [4667]; `embed/gene_vectors.npy` [4667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4667 or target_col == 4667). Every well: [[PSMF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
