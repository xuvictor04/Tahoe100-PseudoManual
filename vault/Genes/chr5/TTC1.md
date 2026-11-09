---
symbol: "TTC1"
type: "gene"
col: 3447
ensembl_id: "ENSG00000113312"
name: "tetratricopeptide repeat domain 1"
location: "5q33.3"
module: 64
arm: "+"
pooled_cpm: 88.72
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# TTC1

*tetratricopeptide repeat domain 1* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.26× (z +20.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.740× (z -10.7, q 9e-24, down in 30 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (RKO 0.468×, HepG2/C3A 0.408×, NCI-H460 0.627×, SNU-1 0.458×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.355×, NCI-H23 0.436×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.369×; ⚠ toxic; cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOOL]] (+0.64, fdr 7e-06), [[RPAP3]] (+0.63, fdr 1e-05), [[MOCS2]] (+0.63, fdr 1e-05); moves opposite to [[SP3]] (-0.54, fdr 8e-05), [[NFKBID]] (-0.53, fdr 4e-05), [[TAPT1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TBC1D19]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.26×** | +20.6 | 0e+00 | 47/48 (HEC-1-A, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.14×** | +19.2 | 0e+00 | 46/48 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +17.7 | 0e+00 | 48/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.10×** | +17.7 | 0e+00 | 44/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +17.7 | 0e+00 | 47/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +17.3 | 0e+00 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +13.8 | 4e-41 | 46/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.8 | 6e-21 | 26/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +9.6 | 7e-20 | 34/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.46×** | +9.5 | 1e-19 | 34/49 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +7.1 | 8e-11 | 31/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +6.4 | 1e-08 | 28/49 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.29×** | +6.0 | 7e-08 | 23/45 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +5.9 | 1e-07 | 26/48 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +5.9 | 1e-07 | 30/49 (PANC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.0 | 2e-05 | 16/48 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.6 | 9e-05 | 23/49 (A-172, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.001 | 14/48 (NCI-H2347, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.002 | 19/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3447.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (RKO 0.468×, HepG2/C3A 0.408×, NCI-H460 0.627×, SNU-1 0.458×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.355×, NCI-H23 0.436×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.369×; ⚠ toxic; cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -10.7 | 9e-24 | 30/49 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 0.893× | -4.0 | 0.019 | 6/48 (Hs 766T, SW 1271, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.871× | -3.3 | 0.17 | 16/47 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.878× | -3.2 | 0.17 | 12/47 (HOP62, SW480, …) | rises with dose | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.913× | -3.2 | 0.17 | 5/48 (HT-29, SNU-1, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.915× | -3.1 | 0.17 | 6/48 (LOX-IMVI, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 84.5 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 103 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +16.5) | — |
| [[A498 (line)]] | wt | 81.2 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 58.7 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.42× (z +13.5) | — |
| [[LoVo (line)]] | wt | 90.7 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 81.8 | 6 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.54× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -10.0) |
| [[SW480 (line)]] | alt | 102 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +14.3) | — |
| [[A549 (line)]] | wt | 70.6 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 120 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 90.9 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.34× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.27× (z +13.2) | — |
| [[Hs 766T (line)]] | wt | 109 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 79.1 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 96.3 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.63× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.449× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 69.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 89.7 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 91.7 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 107 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.14× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 89.7 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.61× (z +10.5) | — |
| [[A-427 (line)]] | wt | 127 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.01× (z +9.5) | — |
| [[C32 (line)]] | wt | 51.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 100 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.11× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 88.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +13.2) | — |
| [[KATO III (line)]] | alt | 79.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.68× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 76.4 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[RKO (line)]] | wt | 111 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 52.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.02× (z +10.5) | — |
| [[J82 (line)]] | alt | 76.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 71.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.25× (z +10.9) | — |
| [[SW48 (line)]] | wt | 74.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 70.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.36× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 65.5 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.60× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.3) |
| [[SNU-1 (line)]] | wt | 91.7 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.74× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.8) |
| [[BT-474 (line)]] | alt | 57.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.77× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 71.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 78.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.5) |
| [[SW1417 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -10.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOOL]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[RPAP3]] | +0.63 | +0.50 / +0.67 | both halves | 1e-05 | same gene group; STRING 487 |
| [[MOCS2]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CCNC]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[GTF3C3]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 | same gene group |
| [[COX19]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[LYPLAL1]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[UBE4A]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CWC27]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP3]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[NFKBID]] | -0.53 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[TAPT1]] | -0.52 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[CFL1]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[INAFM2]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PTPN18]] | -0.51 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PTBP1]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[C4orf46]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[LHFPL6]] | -0.50 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ARID1A]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[UBTF]] | -0.49 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[HIVEP1]] | -0.49 | -0.36 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D19]] | C | TBC1D19 activity raises TTC1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without TBC1D19 | 0.0996 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-21.5, -0.4); signed map (-22.6, -20.1). **Vector** length 116, 35.1% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.5 | +17.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.0 | +19.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +20.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.7 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +13.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.7 | -10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -3.1 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | +3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:160,009,113-160,065,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TPR1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99614](https://www.uniprot.org/uniprotkb/Q99614) (Tetratricopeptide repeat protein 1):

> Adapter protein that plays a role downstream of GNA15 to stimulate Ras activation and subsequent phosphorylation of ERK1/2 independently of phospholipase Cbeta signaling. Mechanistically, interacts with GNA15 and SOS2 to form a macromolecular signaling complex which has a high affinity for HRAS. Additionally, participates in signaling via other G-alpha proteins like GNA14, activating NF-kappa-B through Ras and ERK pathways. Beyond signaling, supports protein homeostasis by cooperating with …

**Summary**, from NCBI Gene [7265](https://www.ncbi.nlm.nih.gov/gene/7265):

> This gene encodes a protein that belongs to the tetratrico peptide repeat superfamily of proteins. The encoded protein plays a role in protein-protein interactions, and binds to the Galpha subunit of G protein-coupled receptors to activate the Ras signaling pathway. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:12391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12391) · Entrez [7265](https://www.ncbi.nlm.nih.gov/gene/7265) · UniProt [Q99614](https://www.uniprot.org/uniprotkb/Q99614) · Ensembl [ENSG00000113312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113312)

## Data

Gene col 3447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3447); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3447]; `tensor/DDL_lfc|DDL_z.npy` [3447]; `embed/gene_vectors.npy` [3447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3447 or target_col == 3447). Every well: [[TTC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
