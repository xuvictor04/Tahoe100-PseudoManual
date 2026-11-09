---
symbol: "ARHGEF7"
type: "gene"
col: 2260
ensembl_id: "ENSG00000102606"
name: "Rho guanine nucleotide exchange factor 7"
location: "13q34"
module: 169
arm: "+"
pooled_cpm: 115.55
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# ARHGEF7

*Rho guanine nucleotide exchange factor 7* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.65× (z +10.4, q 1e-22, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.410× (z -11.1, q 5e-26, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.814× (z -3.8, q 0.016, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 0.100×, H4 0.0672×, HCT15 0.155×, SHP-77 0.208×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.106×, NCI-H1573 0.195×, SW480 0.255×, RPMI-7951 0.186×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.257×; ⚠ toxic); [[Darinaparsin (drug)]] 0.5 µM in 1 line (SW 1271 0.0675×); [[Proglumide (drug)]] 0.05 µM in 1 line (SW 1088 0.0902×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF4]] (+0.76, fdr 7e-06), [[PHB2]] (+0.72, fdr 9e-06), [[ZDHHC7]] (+0.66, fdr 1e-05); moves opposite to [[CYP20A1]] (-0.67, fdr 7e-06), [[TIPRL]] (-0.64, fdr 7e-06), [[UPF3B]] (-0.64, fdr 7e-06).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.65×** | +10.4 | 1e-22 | 46/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.49×** | +8.4 | 8e-15 | 45/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +6.5 | 2e-08 | 41/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +6.0 | 2e-07 | 40/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.3 | 1e-05 | 32/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 0.001 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +3.7 | 0.015 | 30/48 (HS-578T, C-33 A, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.30× | +3.1 | 0.13 | 29/48 (LoVo, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2260.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (Panc 03.27 0.100×, H4 0.0672×, HCT15 0.155×, SHP-77 0.208×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.106×, NCI-H1573 0.195×, SW480 0.255×, RPMI-7951 0.186×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.257×; ⚠ toxic); [[Darinaparsin (drug)]] 0.5 µM in 1 line (SW 1271 0.0675×); [[Proglumide (drug)]] 0.05 µM in 1 line (SW 1088 0.0902×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -11.1 | 5e-26 | 43/44 (Panc 03.27, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -10.6 | 7e-24 | 47/48 (HCT15, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -6.2 | 8e-08 | 44/47 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.655×** | -5.1 | 5e-05 | 33/45 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.016 | 25/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.830×** | -3.5 | 0.053 | 23/48 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.784× | -3.2 | 0.11 | 29/47 (BT-474, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.843× | -3.2 | 0.11 | 26/48 (HCT15, A-172, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 221 | 7 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.61× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 85.2 | 4 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.51× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 165 | 1 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 8.05× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 221 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 82.7 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.84× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 125 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.23× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.257× (z -12.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 74.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -17.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 150 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 134 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.41× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 159 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.28× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 138 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.21× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -22.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 100 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.59× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.22× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 139 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.99× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 93.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 96.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.35× (z +8.6) | — |
| [[A498 (line)]] | wt | 93.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 86.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -11.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0672× (z -18.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.04× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 64.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.09× (z +8.6) | — |
| [[RKO (line)]] | wt | 143 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.16× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 273 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 90.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 88.4 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0902× (z -8.5) |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.0675× (z -8.9) |
| [[SW48 (line)]] | wt | 172 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.89× (z +9.3) | — |
| [[A549 (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | +0.76 | +0.84 / +0.64 | both halves | 7e-06 |  |
| [[PHB2]] | +0.72 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[ZDHHC7]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[PPHLN1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[ILRUN]] | +0.65 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[COPS7B]] | +0.64 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ADPGK]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.64 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[NAGA]] | +0.63 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[NDC1]] | +0.63 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[RPA1]] | +0.63 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.63 | +0.77 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP20A1]] | -0.67 | -0.72 / -0.67 | both halves | 7e-06 |  |
| [[TIPRL]] | -0.64 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[UPF3B]] | -0.64 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[GORAB]] | -0.63 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ZNF674]] | -0.62 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[RBMXL1]] | -0.61 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[HELQ]] | -0.61 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.60 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[XIAP]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 | pathway: Death Receptor Signaling |
| [[GATAD1]] | -0.58 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[MED18]] | -0.58 | -0.75 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.2, -13.6); signed map (-41.9, -12.6). **Vector** length 87.2, 28.8% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -9.2 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.4 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.6 | +0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:111,114,559-111,305,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0142, PIXB, DKFZp761K1021, Nbla10314, DKFZp686C12170, BETA-PIX, COOL1, P85SPR |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 30 pathways, smallest: Activation of RAC1 downstream of NMDARs; Ephrin signaling; EGFR downregulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14155](https://www.uniprot.org/uniprotkb/Q14155) (Rho guanine nucleotide exchange factor 7):

> Acts as a RAC1 guanine nucleotide exchange factor (GEF) and can induce membrane ruffling. Functions in cell migration, attachment and cell spreading. Promotes targeting of RAC1 to focal adhesions (By similarity). May function as a positive regulator of apoptosis. Downstream of NMDA receptors and CaMKK-CaMK1 signaling cascade, promotes the formation of spines and synapses in hippocampal neurons.

**Summary**, from NCBI Gene [8874](https://www.ncbi.nlm.nih.gov/gene/8874):

> This gene encodes a protein that belongs to a family of cytoplasmic proteins that activate the Ras-like family of Rho proteins by exchanging bound GDP for GTP. It forms a complex with the small GTP binding protein Rac1 and recruits Rac1 to membrane ruffles and to focal adhesions. Multiple alternatively spliced transcript variants encoding different isoforms have been observed for this gene. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:15607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15607) · Entrez [8874](https://www.ncbi.nlm.nih.gov/gene/8874) · UniProt [Q14155](https://www.uniprot.org/uniprotkb/Q14155) · Ensembl [ENSG00000102606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102606)

## Data

Gene col 2260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2260); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2260]; `tensor/DDL_lfc|DDL_z.npy` [2260]; `embed/gene_vectors.npy` [2260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2260 or target_col == 2260). Every well: [[ARHGEF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
