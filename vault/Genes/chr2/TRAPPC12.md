---
symbol: "TRAPPC12"
type: "gene"
col: 10174
ensembl_id: "ENSG00000171853"
name: "trafficking protein particle complex subunit 12"
location: "2p25.3"
module: 5
arm: "+"
pooled_cpm: 66.2
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TRAPPC12

*trafficking protein particle complex subunit 12* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.29× (z +4.0, q 0.018, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (BT-474 2.67×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.444× (z -11.8, q 3e-29, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.813× (z -4.6, q 2e-04, down in 25 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 0.198×, NCI-H460 0.230×, SW480 0.317×, HepG2/C3A 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Hs 766T 0.0646×, SHP-77 0.0889×, LoVo 0.192×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.109×, SK-MEL-2 0.126×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.483×, HepG2/C3A 0.503×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.362×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGAP5]] (+0.66, fdr 7e-06), [[AGAP6]] (+0.60, fdr 1e-05), [[PRR14L]] (+0.60, fdr 1e-05); moves opposite to [[TWSG1]] (-0.60, fdr 1e-05), [[AMOT]] (-0.59, fdr 2e-05), [[CXADR]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10174.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (BT-474 2.67×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.018 | 27/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +4.0 | 0.018 | 20/48 (A-427, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.24× | +3.4 | 0.12 | 24/48 (BT-474, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.24× | +3.3 | 0.12 | 19/48 (SW48, Panc 03.27, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.21× | +3.0 | 0.26 | 15/49 (SNU-1, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10174.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 0.198×, NCI-H460 0.230×, SW480 0.317×, HepG2/C3A 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (Hs 766T 0.0646×, SHP-77 0.0889×, LoVo 0.192×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.109×, SK-MEL-2 0.126×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.483×, HepG2/C3A 0.503×); [[Ponatinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.362×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.444×** | -11.8 | 3e-29 | 34/45 (LoVo, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -10.6 | 1e-23 | 33/43 (Hs 766T, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.518×** | -10.3 | 8e-23 | 37/49 (SW480, NCI-H1573, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.518×** | -10.3 | 8e-23 | 41/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.539×** | -9.7 | 3e-20 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.700×** | -5.6 | 2e-06 | 31/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.694×** | -5.5 | 3e-06 | 29/47 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.725×** | -5.1 | 3e-05 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.6 | 2e-04 | 25/49 (SHP-77, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.747×** | -4.4 | 6e-04 | 27/48 (AN3 CA, NCI-H1792, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.002 | 26/48 (KATO III, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.773×** | -4.1 | 0.002 | 25/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.661×** | -3.4 | 0.030 | 23/49 (PANC-1, HepG2/C3A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.826× | -3.0 | 0.11 | 18/48 (LoVo, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 92.1 | 0 | 11 (11 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.208× (z -17.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 91.7 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 116 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 73.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -21.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 75.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -11.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 65.8 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 124 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0889× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.362× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 104 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 87.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 79.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 74.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.67× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.331× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 51.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0646× (z -22.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -11.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 58.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 75.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -8.9) ⚠ cell-cycle shift, explains ~77% of this change |
| [[C32 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0664× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP5]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[AGAP6]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[PRR14L]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LEMD2]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[XPNPEP3]] | +0.59 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[AGAP4]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[CKMT2-AS1]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[METTL2B]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DNAJA3]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LMF1]] | +0.55 | +0.40 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TWSG1]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[AMOT]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[CXADR]] | -0.59 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[MPP7]] | -0.58 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[FRMPD3]] | -0.57 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SLC25A23]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[GSN]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[CLSTN1]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[HPSE]] | -0.52 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[CGN]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[USP54]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.2, 0.6); signed map (-5.0, -22.0). **Vector** length 97.1, 26.7% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.2 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.6 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | -11.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.6 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:3,379,675-3,485,094 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-87, TTC-15; previously TTC15 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Trafficking protein particle complex subunits |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVT3](https://www.uniprot.org/uniprotkb/Q8WVT3) (Trafficking protein particle complex subunit 12):

> Component of the TRAPP complex, which is involved in endoplasmic reticulum to Golgi apparatus trafficking at a very early stage. Also plays a role in chromosome congression, kinetochore assembly and stability and controls the recruitment of CENPE to the kinetochores.

**Summary**, from NCBI Gene [51112](https://www.ncbi.nlm.nih.gov/gene/51112):

> Involved in several processes, including endoplasmic reticulum to Golgi vesicle-mediated transport; positive regulation of protein localization to kinetochore; and regulation of kinetochore assembly. Located in several cellular components, including endoplasmic reticulum-Golgi intermediate compartment; kinetochore; and perinuclear region of cytoplasm. Part of TRAPP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24284) · Entrez [51112](https://www.ncbi.nlm.nih.gov/gene/51112) · UniProt [Q8WVT3](https://www.uniprot.org/uniprotkb/Q8WVT3) · Ensembl [ENSG00000171853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171853)

## Data

Gene col 10174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10174); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10174]; `tensor/DDL_lfc|DDL_z.npy` [10174]; `embed/gene_vectors.npy` [10174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10174 or target_col == 10174). Every well: [[TRAPPC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
