---
symbol: "KANK1"
type: "gene"
col: 2825
ensembl_id: "ENSG00000107104"
name: "KN motif and ankyrin repeat domains 1"
location: "9p24.3"
module: 18
arm: "+"
pooled_cpm: 84.92
n_lines_expressing: 38
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# KANK1

*KN motif and ankyrin repeat domains 1* — 9p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.27× (z +4.4, q 0.007, up in 18 of 36 measured lines) ⚠ cell-cycle shift, explains ~27% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (SW1417 2.33×, NCI-H460 1.79×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.98×; ⚠ cell-cycle shift, explains ~22% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -18.4, q 0e+00, down in 32 of 36 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.400× (z -16.7, q 0e+00, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE9]] (+0.62, fdr 1e-05), [[CHD7]] (+0.61, fdr 2e-05), [[DOCK9]] (+0.60, fdr 1e-05); moves opposite to [[SENP2]] (-0.52, fdr 6e-05), [[MMUT]] (-0.48, fdr 6e-05), [[CCDC159]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[MMUT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 2 lines (SW1417 2.33×, NCI-H460 1.79×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.98×; ⚠ cell-cycle shift, explains ~22% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +4.4 | 0.007 | 18/36 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.4 | 0.16 | 12/36 (SW1417, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.3 | 0.16 | 15/36 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.18× | +3.2 | 0.16 | 13/37 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.2 | 0.16 | 0/38 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2825.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.511×** | -18.4 | 0e+00 | 32/36 (A549, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.400×** | -16.7 | 0e+00 | 31/36 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.406×** | -16.4 | 0e+00 | 27/33 (C-33 A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.513×** | -12.9 | 4e-36 | 30/36 (SNU-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.511×** | -12.0 | 3e-31 | 29/35 (LoVo, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.430×** | -11.6 | 5e-29 | 31/37 (RKO, AN3 CA, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.562×** | -11.2 | 4e-27 | 33/36 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -11.1 | 5e-27 | 30/36 (AN3 CA, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -9.7 | 3e-20 | 30/37 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.611×** | -9.5 | 9e-20 | 27/36 (LoVo, COLO 205, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.647×** | -8.4 | 2e-15 | 26/36 (C-33 A, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.648×** | -7.9 | 1e-13 | 24/36 (NCI-H460, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.724×** | -6.3 | 2e-08 | 25/36 (C-33 A, SNU-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.739×** | -5.9 | 2e-07 | 21/36 (HepG2/C3A, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.758×** | -5.4 | 3e-06 | 20/36 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.613×** | -5.0 | 2e-05 | 17/36 (LS 180, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.011 | 19/36 (SK-MEL-2, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 262 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -22.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -17.4) |
| [[A549 (line)]] | wt | 306 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0665× (z -28.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0795× (z -17.7) |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 11 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 362 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -18.9) |
| [[SW48 (line)]] | wt | 219 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.206× (z -14.9) |
| [[A498 (line)]] | wt | 197 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -18.0) |
| [[LoVo (line)]] | wt | 201 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.109× (z -16.8) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 37.9 | 2 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.79× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.326× (z -11.0) |
| [[C-33 A (line)]] | alt | 159 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -29.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 75.7 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.206× (z -11.3) |
| [[J82 (line)]] | alt | 79.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -16.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.347× (z -10.6) |
| [[PANC-1 (line)]] | alt | 49.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -19.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.277× (z -16.7) |
| [[RKO (line)]] | wt | 172 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0696× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.180× (z -16.7) |
| [[HS-578T (line)]] | alt | 127 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -17.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 46.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -13.8) |
| [[LS 180 (line)]] | wt | 201 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.156× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 93.8 | 0 | 4 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -14.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 77.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.284× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 77.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.186× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -18.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 91.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.332× (z -11.0) |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 60.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.376× (z -8.5) |
| [[SW 900 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 38.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[SW480 (line)]] | alt | 69.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE9]] | +0.62 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CHD7]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[DOCK9]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SNX24]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[GALNT14]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[LRRC8D]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[NSMAF]] | +0.56 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[NRF1]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ADCY3]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MVB12B]] | +0.55 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[SPECC1L]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP2]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[MMUT]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[CCDC159]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[YY1AP1]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[COG4]] | -0.46 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[MAP3K13]] | -0.46 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[ILK]] | -0.46 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[TYK2]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[NPHP1]] | -0.45 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[PLAG1]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SEPTIN2]] | -0.45 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMUT]] | B | KANK1 activity lowers MMUT's level | lines that do not express KANK1 (12) vs lines expressing it (38) | 1.42× higher at baseline in the lines without KANK1 | 0.058 | ⚠ within organs, on part of the lines |
| [[COG4]] | B | KANK1 activity lowers COG4's level | lines that do not express KANK1 (12) vs lines expressing it (38) | 1.19× higher at baseline in the lines without KANK1 | 0.081 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.1, -37.3); signed map (7.8, -2.5). **Vector** length 86.3, 20.3% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +0.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +0.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.8 | -18.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -5.0 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.2 | +1.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | KN motif and ankyrin repeat domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.3 — chr9:470,291-746,105 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0172, KANK; previously ANKRD15 |
| Gene groups (HGNC) | KN motif and ankyrin repeat domain containing |
| Reactome | 6 pathways, smallest: Signaling by membrane-tethered fusions of PDGFRA or PDGFRB; Signaling by PDGFR in disease; Estrogen-dependent gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14678](https://www.uniprot.org/uniprotkb/Q14678) (KN motif and ankyrin repeat domain-containing protein 1):

> Adapter protein that links structural and signaling protein complexes positioned to guide microtubule and actin cytoskeleton dynamics during cell morphogenesis. At focal adhesions (FAs) rims, organizes cortical microtubule stabilizing complexes (CMSCs) and directly interacts with major FA component TLN1, forming macromolecular assemblies positioned to control microtubule-actin crosstalk at the cell edge. Recruits KIF21A in CMSCs at axonal growth cones and regulates axon guidance by suppressing …

**Summary**, from NCBI Gene [23189](https://www.ncbi.nlm.nih.gov/gene/23189):

> The protein encoded by this gene belongs to the Kank family of proteins, which contain multiple ankyrin repeat domains. This family member functions in cytoskeleton formation by regulating actin polymerization. This gene is a candidate tumor suppressor for renal cell carcinoma. Mutations in this gene cause cerebral palsy spastic quadriplegic type 2, a central nervous system development disorder. A t(5;9) translocation results in fusion of the platelet-derived growth factor receptor beta gene …

**Accessions** — [HGNC:19309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19309) · Entrez [23189](https://www.ncbi.nlm.nih.gov/gene/23189) · UniProt [Q14678](https://www.uniprot.org/uniprotkb/Q14678) · Ensembl [ENSG00000107104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107104)

## Data

Gene col 2825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2825); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2825]; `tensor/DDL_lfc|DDL_z.npy` [2825]; `embed/gene_vectors.npy` [2825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2825 or target_col == 2825). Every well: [[KANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
