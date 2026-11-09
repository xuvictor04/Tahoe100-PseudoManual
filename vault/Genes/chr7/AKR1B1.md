---
symbol: "AKR1B1"
type: "gene"
col: 1435
ensembl_id: "ENSG00000085662"
name: "aldo-keto reductase family 1 member B"
location: "7q33"
module: 66
arm: "+"
pooled_cpm: 56.54
n_lines_expressing: 34
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# AKR1B1

*aldo-keto reductase family 1 member B* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.55× (z +14.5, q 7e-45, up in 27 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +5.7, q 2e-06, up in 21 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLR1]] (+0.69, fdr 7e-06), [[LUM]] (+0.68, fdr 1e-05), [[CCDC80]] (+0.64, fdr 1e-05); moves opposite to [[ZNF549]] (-0.61, fdr 1e-05), [[DNAAF9]] (-0.55, fdr 1e-05), [[DPY19L3]] (-0.54, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RRAD]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **4.55×** | +14.5 | 7e-45 | 27/28 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.89×** | +12.5 | 2e-33 | 22/23 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.35×** | +8.9 | 8e-17 | 24/25 (J82, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.7 | 2e-06 | 21/31 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +5.6 | 2e-06 | 23/32 (J82, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.49×** | +5.3 | 1e-05 | 15/31 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.73×** | +5.0 | 4e-05 | 19/30 (HOP62, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.69×** | +5.0 | 4e-05 | 19/29 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.66×** | +4.7 | 2e-04 | 19/32 (J82, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.60×** | +4.5 | 4e-04 | 19/32 (J82, SK-MEL-2, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.001 | 16/32 (HOP62, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.1 | 0.002 | 16/29 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.52×** | +4.0 | 0.003 | 13/32 (J82, HEC-1-A, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.52×** | +4.0 | 0.003 | 17/32 (A498, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.51×** | +3.9 | 0.003 | 13/32 (HEC-1-A, J82, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.004 | 18/30 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.006 | 18/32 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.008 | 13/32 (LS 180, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.016 | 12/32 (J82, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.035 | 11/32 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.044 | 13/29 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.070 | 12/32 (SW 900, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.071 | 8/32 (A498, A549, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +2.9 | 0.071 | 12/32 (Panc 03.27, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.082 | 12/32 (NCI-H2030, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.688× | -3.6 | 0.17 | 15/32 (A498, NCI-H1792, …) | rises with dose | position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.617× | -3.3 | 0.17 | 14/32 (A498, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.697× | -3.3 | 0.17 | 13/32 (A498, SHP-77, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.703× | -3.2 | 0.17 | 12/32 (C-33 A, A-172, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 102 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +17.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +9.9) | — |
| [[A498 (line)]] | wt | 627 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +14.5) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +11.2) | — |
| [[A549 (line)]] | wt | 197 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +11.6) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 19.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +17.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.2) | — |
| [[C32 (line)]] | wt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.73× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +11.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.29× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 24.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[RPMI-7951 (line)]] | alt | 70.7 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.15× (z +8.8) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[A-172 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.24× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.64× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[Hs 766T (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.95× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2347 (line)]] | alt | 51.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 73.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-423 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +11.5) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A-427 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLR1]] | +0.69 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LUM]] | +0.68 | +0.52 / +0.66 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[CCDC80]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[VCAM1]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TNFRSF9]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.60 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SLC2A6]] | +0.59 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CDH2]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TMEM47]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TMEM52B]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF549]] | -0.61 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[DNAAF9]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[DPY19L3]] | -0.54 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CLMP]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[BCL7C]] | -0.52 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[ZNF595]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[C19orf25]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[OGG1]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SPOUT1]] | -0.51 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[CROCCP3]] | -0.50 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[ING5]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZMYND19]] | -0.49 | -0.55 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAD]] | B | RRAD activity raises AKR1B1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 3.88× lower at baseline in the lines without RRAD | 0.039 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[CCDC80]] | B | CCDC80 activity raises AKR1B1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.05× lower at baseline in the lines without CCDC80 | 0.074 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[SYNM]] | C | SYNM activity raises AKR1B1's level | lines that do not express SYNM (14) vs lines expressing it (36) | 5.06× lower at baseline in the lines without SYNM | 0.082 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent; co-absent with the target |
| [[SSTR2]] | C | SSTR2 activity raises AKR1B1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.84× lower at baseline in the lines without SSTR2 | 0.090 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCN3]] | B | AKR1B1 activity raises CCN3's level | lines that do not express AKR1B1 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without AKR1B1 | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPRM, EHD3, SYNM |
| [[FLI1]] | B | AKR1B1 activity raises FLI1's level | lines that do not express AKR1B1 (16) vs lines expressing it (34) | 3.46× lower at baseline in the lines without AKR1B1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PTPRM, EHD3, SYNM |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 22.5); signed map (45.7, 21.2). **Vector** length 67.9, 17.8% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.1 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,442,356-134,459,284 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AR; previously ALDR1 |
| Gene groups (HGNC) | Aldo-keto reductases |
| Reactome | 7 pathways, smallest: Fructose metabolism; Galactose catabolism; Pregnenolone biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P15121](https://www.uniprot.org/uniprotkb/P15121) (Aldo-keto reductase family 1 member B1):

> Catalyzes the NADPH-dependent reduction of a wide variety of carbonyl-containing compounds to their corresponding alcohols. Displays enzymatic activity towards endogenous metabolites such as aromatic and aliphatic aldehydes, ketones, monosaccharides, bile acids and xenobiotics substrates. It catalyzes the reduction of glucose to sorbitol, the first step of the polyol pathway, an alternative route of glucose metabolism that converts glucose to fructose. This pathway becomes highly active under …

**Summary**, from NCBI Gene [231](https://www.ncbi.nlm.nih.gov/gene/231):

> This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. This member catalyzes the reduction of a number of aldehydes, including the aldehyde form of glucose, and is thereby implicated in the development of diabetic complications by catalyzing the reduction of glucose to sorbitol. Multiple pseudogenes have been identified for this gene. The nomenclature system used by the HUGO Gene Nomenclature Committee to define human …

**Accessions** — [HGNC:381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:381) · Entrez [231](https://www.ncbi.nlm.nih.gov/gene/231) · UniProt [P15121](https://www.uniprot.org/uniprotkb/P15121) · Ensembl [ENSG00000085662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085662)

## Data

Gene col 1435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1435); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1435]; `tensor/DDL_lfc|DDL_z.npy` [1435]; `embed/gene_vectors.npy` [1435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1435 or target_col == 1435). Every well: [[AKR1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
