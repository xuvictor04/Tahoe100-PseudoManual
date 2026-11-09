---
symbol: "SLC4A1AP"
type: "gene"
col: 8779
ensembl_id: "ENSG00000163798"
name: "solute carrier family 4 member 1 adaptor protein"
location: "2p23.3"
module: 12
arm: "+"
pooled_cpm: 49.18
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SLC4A1AP

*solute carrier family 4 member 1 adaptor protein* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +14.6, q 1e-45, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.96× (z +11.9, q 3e-30, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.716× (z -8.4, q 3e-14, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 0.165×, H4 0.149×, LS 180 0.274×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.0742×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW 900 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (H4 0.0853×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNW1]] (+0.81, fdr 7e-06), [[CCDC174]] (+0.77, fdr 7e-06), [[CCDC43]] (+0.74, fdr 7e-06); moves opposite to [[AHCY]] (-0.68, fdr 7e-06), [[SMG1P3]] (-0.65, fdr 7e-06), [[SEH1L]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.79×** | +14.6 | 1e-45 | 43/48 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +11.9 | 3e-30 | 41/48 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +11.7 | 2e-29 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.79×** | +9.9 | 5e-21 | 44/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.4 | 5e-15 | 35/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +8.0 | 9e-14 | 38/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 6e-10 | 35/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.7 | 1e-09 | 41/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.6 | 2e-09 | 34/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +6.4 | 1e-08 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 5e-06 | 30/48 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.7 | 1e-04 | 25/47 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.28×** | +4.4 | 6e-04 | 19/48 (NCI-H1573, SW480, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.3 | 7e-04 | 28/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.9 | 0.004 | 23/44 (SW1417, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.004 | 23/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8779.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 0.165×, H4 0.149×, LS 180 0.274×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.0742×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW 900 0.380×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (H4 0.0853×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -8.4 | 3e-14 | 40/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -5.5 | 1e-05 | 30/48 (CHP-212, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -4.8 | 3e-04 | 22/40 (A-427, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.876× | -3.3 | 0.13 | 6/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Baicalin (drug)]] 5 µM |  | 0.887× | -3.0 | 0.31 | 5/49 (KATO III, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 61.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.57× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -17.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +11.0) | — |
| [[SW480 (line)]] | alt | 55.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.18× (z +9.9) | — |
| [[A498 (line)]] | wt | 98.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +9.5) | — |
| [[A549 (line)]] | wt | 47.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +10.6) | — |
| [[H4 (line)]] | wt | 32.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.0853× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 39.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 40.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 42.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.38× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 44.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 50.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 78.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 58.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +9.4) | — |
| [[C32 (line)]] | wt | 42.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 49.0 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0742× (z -12.2) |
| [[HS-578T (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 33.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 43.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 45.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNW1]] | +0.81 | +0.87 / +0.72 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.77 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.74 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.74 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[SNRNP27]] | +0.74 | +0.84 / +0.60 | both halves | 7e-06 |  |
| [[SART3]] | +0.73 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[BRAP]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TTF1]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[ZMAT2]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.71 | +0.76 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCY]] | -0.68 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.65 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[SEH1L]] | -0.64 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[GLB1L2]] | -0.64 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[MED14]] | -0.61 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.6, 3.2); signed map (-0.3, -16.6). **Vector** length 106, 28.1% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.56 to 17); *mRNA Splicing* (reactome, mean cos +0.56 to 17); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.52 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.1 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.5 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 1 adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,663,426-27,695,366 (+) |
| Ensembl biotype | protein_coding |
| Also known as | kanadaptin, HLC3 |
| Matched by | ensembl_id |

UniProt [Q9BWU0](https://www.uniprot.org/uniprotkb/Q9BWU0) carries no function annotation.

**Summary**, from NCBI Gene [22950](https://www.ncbi.nlm.nih.gov/gene/22950):

> Predicted to enable mRNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13813) · Entrez [22950](https://www.ncbi.nlm.nih.gov/gene/22950) · UniProt [Q9BWU0](https://www.uniprot.org/uniprotkb/Q9BWU0) · Ensembl [ENSG00000163798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163798)

## Data

Gene col 8779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8779); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8779]; `tensor/DDL_lfc|DDL_z.npy` [8779]; `embed/gene_vectors.npy` [8779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8779 or target_col == 8779). Every well: [[SLC4A1AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A1AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
