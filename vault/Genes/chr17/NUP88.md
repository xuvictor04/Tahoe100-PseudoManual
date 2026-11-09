---
symbol: "NUP88"
type: "gene"
col: 2966
ensembl_id: "ENSG00000108559"
name: "nucleoporin 88"
location: "17p13.2"
module: 71
arm: "+"
pooled_cpm: 74.29
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# NUP88

*nucleoporin 88* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.17× (z +20.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.793× (z -8.6, q 5e-15, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-427 0.106×, RKO 0.119×, HEC-1-A 0.266×, SW1417 0.419×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 0.153×, HEC-1-A 0.428×, LS 180 0.393×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.582×, A498 0.662×; ⚠ cell-cycle shift, explains ~43% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (KATO III 0.606×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN52]] (+0.61, fdr 1e-05), [[SNRPA]] (+0.57, fdr 1e-05), [[NUP107]] (+0.53, fdr 3e-05); moves opposite to [[TAB3]] (-0.49, fdr 2e-05), [[TP53BP2]] (-0.49, fdr 3e-05), [[BPHL]] (-0.48, fdr 5e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +20.0 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +17.1 | 0e+00 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.74×** | +14.3 | 4e-44 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +13.9 | 1e-41 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +10.1 | 4e-22 | 40/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +8.8 | 9e-17 | 33/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +8.1 | 6e-14 | 33/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +8.0 | 1e-13 | 34/49 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +7.0 | 1e-10 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +6.7 | 9e-10 | 31/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +6.0 | 9e-08 | 28/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.25×** | +5.7 | 4e-07 | 26/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +5.5 | 2e-06 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.16× | +5.5 | 2e-06 | 19/48 (LOX-IMVI, A549, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.16× | +5.4 | 2e-06 | 23/49 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 17/49 (NCI-H460, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.2 | 7e-04 | 14/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 16/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.048 | 7/49 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-427 0.106×, RKO 0.119×, HEC-1-A 0.266×, SW1417 0.419×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 0.153×, HEC-1-A 0.428×, LS 180 0.393×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 2 lines (A-427 0.582×, A498 0.662×; ⚠ cell-cycle shift, explains ~43% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (KATO III 0.606×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.793×** | -8.6 | 5e-15 | 31/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.725×** | -8.4 | 1e-14 | 33/49 (HT-29, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.808×** | -5.4 | 2e-05 | 24/43 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.813×** | -5.0 | 8e-05 | 21/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.866× | -3.8 | 0.019 | 16/47 (MIA PaCa-2, A-427, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.875× | -3.5 | 0.040 | 16/48 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.876× | -3.5 | 0.040 | 19/48 (BT-474, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.912× | -3.4 | 0.040 | 12/48 (A-427, A498, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.878× | -3.4 | 0.040 | 17/49 (SW48, HEC-1-A, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.877× | -3.3 | 0.053 | 16/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.886× | -3.2 | 0.076 | 6/47 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.883× | -3.1 | 0.081 | 15/47 (C-33 A, A-427, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.096 | 9/48 (SHP-77, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.2 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +16.8) | — |
| [[SW480 (line)]] | alt | 123 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +20.7) | — |
| [[AsPC-1 (line)]] | alt | 49.2 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 58.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +13.7) | — |
| [[SHP-77 (line)]] | alt | 133 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +13.2) | — |
| [[KATO III (line)]] | alt | 102 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.52× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.5) | [[Tucidinostat (drug)]] 5 µM 0.606× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 63.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 92.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 109 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.61× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -9.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 68.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.16× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 76.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -25.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 73.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 97.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -16.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 45.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 57.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.8) | — |
| [[A498 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.662× (z -8.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 77.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.137× (z -8.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 42.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.61× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 65.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 81.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[RKO (line)]] | wt | 93.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -22.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN52]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SNRPA]] | +0.57 | +0.53 / +0.60 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[NUP107]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 994 |
| [[TXNDC12]] | +0.51 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[METTL4]] | +0.51 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HAUS8]] | +0.49 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[DBF4B]] | +0.49 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[CENPN]] | +0.49 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CKS1B]] | +0.49 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[NBR2]] | +0.48 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[CENPO]] | +0.48 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[RFC3]] | +0.48 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB3]] | -0.49 | -0.53 / -0.47 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[TP53BP2]] | -0.49 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[BPHL]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[BHLHE40]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[CDC73]] | -0.44 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[LACTB]] | -0.43 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[MIER1]] | -0.43 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[COMMD3]] | -0.43 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[KIFAP3]] | -0.43 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[MCC]] | -0.42 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[RYBP]] | -0.42 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[TNFAIP3]] | -0.42 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.9, -41.2); signed map (-34.4, -40.5). **Vector** length 96.5, 25.1% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +20.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +3.4 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.8 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.7 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.7 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 88 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,359,668-5,420,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8530 |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 69 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99567](https://www.uniprot.org/uniprotkb/Q99567) (Nuclear pore complex protein Nup88):

> Component of nuclear pore complex.

**Summary**, from NCBI Gene [4927](https://www.ncbi.nlm.nih.gov/gene/4927):

> The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins, a family of 50 to 100 proteins, are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene belongs to the nucleoporin family and is associated with the oncogenic nucleoporin CAN/Nup214 in a dynamic subcomplex. This protein is also overexpressed in a …

**Accessions** — [HGNC:8067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8067) · Entrez [4927](https://www.ncbi.nlm.nih.gov/gene/4927) · UniProt [Q99567](https://www.uniprot.org/uniprotkb/Q99567) · Ensembl [ENSG00000108559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108559)

## Data

Gene col 2966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2966); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2966]; `tensor/DDL_lfc|DDL_z.npy` [2966]; `embed/gene_vectors.npy` [2966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2966 or target_col == 2966). Every well: [[NUP88 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP88.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
