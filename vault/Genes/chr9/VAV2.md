---
symbol: "VAV2"
type: "gene"
col: 8333
ensembl_id: "ENSG00000160293"
name: "vav guanine nucleotide exchange factor 2"
location: "9q34.2"
module: 195
arm: "+"
pooled_cpm: 83.11
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# VAV2

*vav guanine nucleotide exchange factor 2* — 9q34.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.82×, RKO 2.24×; ⚠ cell-cycle shift, explains ~0% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 2.74×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.553× (z -14.3, q 1e-43, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.519× (z -11.2, q 9e-27, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAD1L1]] (+0.71, fdr 7e-06), [[IQSEC1]] (+0.69, fdr 7e-06), [[PAQR4]] (+0.64, fdr 1e-05); moves opposite to [[CHURC1]] (-0.63, fdr 1e-05), [[THAP6]] (-0.62, fdr 1e-05), [[ZNF226]] (-0.60, fdr 1e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FARP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 2.82×, RKO 2.24×; ⚠ cell-cycle shift, explains ~0% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 2.74×; ⚠ unreliable plate only).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8333.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.553×** | -14.3 | 1e-43 | 35/47 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.519×** | -11.2 | 9e-27 | 39/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.519×** | -10.1 | 1e-21 | 41/46 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.520×** | -10.1 | 1e-21 | 34/47 (A-427, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.369×** | -8.9 | 5e-17 | 37/48 (HOP62, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -7.5 | 8e-12 | 32/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.663×** | -7.0 | 2e-10 | 33/47 (LoVo, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.717×** | -5.6 | 2e-06 | 34/48 (SK-MEL-2, A498, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.724×** | -5.5 | 2e-06 | 29/47 (LoVo, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -5.4 | 3e-06 | 25/49 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.708×** | -5.3 | 6e-06 | 28/43 (A-172, A498, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -5.3 | 7e-06 | 30/48 (COLO 205, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.751×** | -4.5 | 3e-04 | 25/44 (HS-578T, SK-MEL-2, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.614×** | -4.4 | 5e-04 | 28/46 (BT-474, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.780×** | -4.2 | 9e-04 | 25/47 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.783×** | -4.2 | 0.001 | 21/47 (SHP-77, LoVo, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.850× | -3.9 | 0.003 | 17/47 (HOP62, A549, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.006 | 24/48 (PANC-1, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -3.6 | 0.009 | 20/47 (SHP-77, A498, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.075 | 19/47 (HOP62, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 105 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.8) |
| [[HOP62 (line)]] | alt | 162 | 0 | 8 (5 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0826× (z -12.6) |
| [[A498 (line)]] | wt | 148 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -10.0) |
| [[LoVo (line)]] | wt | 79.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 53.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -28.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -19.2) |
| [[A-172 (line)]] | wt | 149 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[HS-578T (line)]] | alt | 99.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 37.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -21.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 74.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.113× (z -10.9) |
| [[RKO (line)]] | wt | 140 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 92.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -11.0) |
| [[A549 (line)]] | wt | 86.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.411× (z -9.3) |
| [[C32 (line)]] | wt | 85.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.305× (z -10.0) |
| [[COLO 205 (line)]] | alt | 93.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.359× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 32.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 46.9 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.5 µM 0.307× (z -12.2) |
| [[PANC-1 (line)]] | alt | 51.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -19.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -10.5) |
| [[SHP-77 (line)]] | alt | 179 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -8.5) |
| [[SNU-423 (line)]] | alt | 70.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.161× (z -8.6) |
| [[SW480 (line)]] | alt | 72.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -12.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.518× (z -8.9) |
| [[A-427 (line)]] | wt | 37.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0673× (z -22.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 82.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -9.8) |
| [[KATO III (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -16.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[AsPC-1 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 98.4 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.373× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -8.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.182× (z -12.8) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.406× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD1L1]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[IQSEC1]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[PAQR4]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.64 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PLXNA1]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ACOT7]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[TCF3]] | +0.63 | +0.75 / +0.52 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[TELO2]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLCO4A1]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[AKT1]] | +0.61 | +0.68 / +0.60 | both halves | 7e-06 | same gene group; pathway: Platelet activation, signaling and aggregation; STRING 769 |
| [[IGSF9B]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHURC1]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[THAP6]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.60 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PIGP]] | -0.60 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.59 | -0.65 / -0.54 | both halves | 1e-05 | pathway: RHOG GTPase cycle |
| [[ETFRF1]] | -0.58 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[COPS5]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[HHLA3]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PAXIP1-AS2]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ANAPC16]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TAB2]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 | pathway: Death Receptor Signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FARP1]] | B | FARP1 activity raises VAV2's level | lines that do not express FARP1 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without FARP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: C5AR1, SPECC1, IGSF3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.0, 2.7); signed map (-13.9, 42.2). **Vector** length 116, 34.3% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | -0.9 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | +1.7 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -11.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.4 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -5.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | vav guanine nucleotide exchange factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,761,894-133,992,604 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH2 domain containing; SH3 domain containing |
| Hallmark sets | ANGIOGENESIS, UV_RESPONSE_DN, APICAL_JUNCTION |
| Reactome | 52 pathways, smallest: Azathioprine ADME; Signal transduction by L1; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST) |
| Matched by | ensembl_id |

**Function**, from UniProt [P52735](https://www.uniprot.org/uniprotkb/P52735) (Guanine nucleotide exchange factor VAV2):

> Guanine nucleotide exchange factor for the Rho family of Ras-related GTPases. Plays an important role in angiogenesis. Its recruitment by phosphorylated EPHA2 is critical for EFNA1-induced RAC1 GTPase activation and vascular endothelial cell migration and assembly (By similarity).

**Summary**, from NCBI Gene [7410](https://www.ncbi.nlm.nih.gov/gene/7410):

> VAV2 is the second member of the VAV guanine nucleotide exchange factor family of oncogenes. Unlike VAV1, which is expressed exclusively in hematopoietic cells, VAV2 transcripts were found in most tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:12658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12658) · Entrez [7410](https://www.ncbi.nlm.nih.gov/gene/7410) · UniProt [P52735](https://www.uniprot.org/uniprotkb/P52735) · Ensembl [ENSG00000160293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160293)

## Data

Gene col 8333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8333); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8333]; `tensor/DDL_lfc|DDL_z.npy` [8333]; `embed/gene_vectors.npy` [8333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8333 or target_col == 8333). Every well: [[VAV2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAV2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
