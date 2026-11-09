---
symbol: "VPS35L"
type: "gene"
col: 2382
ensembl_id: "ENSG00000103544"
name: "VPS35 endosomal protein sorting factor like"
location: "16p12.3"
module: 88
arm: "+"
pooled_cpm: 31.58
n_lines_expressing: 41
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# VPS35L

*VPS35 endosomal protein sorting factor like* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +10.0, q 9e-21, up in 23 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.407× (z -16.8, q 0e+00, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA2D1]] (+0.73, fdr 1e-05), [[ZFY]] (+0.71, fdr 1e-05), [[WARS2-AS1]] (+0.68, fdr 1e-04); moves opposite to [[MPG]] (-0.68, fdr 2e-05), [[GMCL1]] (-0.68, fdr 1e-05), [[ATP7B]] (-0.66, fdr 2e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CPEB1]] → it (grade B ⚠); 4 go from it, the strongest it → [[MRPS7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +10.0 | 9e-21 | 23/39 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 3e-06 | 19/39 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.1 | 6e-05 | 17/37 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.0 | 1e-04 | 18/39 (NCI-H1573, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.002 | 14/39 (A-427, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.004 | 10/39 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.034 | 12/39 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.035 | 14/39 (C-33 A, NCI-H1792, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.039 | 7/39 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.039 | 13/38 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.23×** | +3.4 | 0.039 | 12/39 (HEC-1-A, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.050 | 10/39 (C-33 A, PANC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.050 | 12/39 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.050 | 4/39 (RPMI-7951, CFPAC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.050 | 6/39 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.074 | 13/39 (CFPAC-1, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.407×** | -16.8 | 0e+00 | 36/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.464×** | -14.4 | 3e-44 | 34/39 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.473×** | -14.0 | 3e-42 | 34/39 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.529×** | -11.9 | 2e-30 | 34/39 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.582×** | -10.1 | 5e-22 | 32/39 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.458×** | -7.6 | 2e-12 | 30/39 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -6.7 | 1e-09 | 20/39 (HOP62, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.791×** | -6.2 | 4e-08 | 19/39 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.607×** | -4.9 | 7e-05 | 18/38 (HEC-1-A, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -4.6 | 2e-04 | 18/39 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -4.4 | 5e-04 | 14/39 (NCI-H23, A-172, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.851× | -4.3 | 9e-04 | 12/39 (NCI-H1792, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.814×** | -3.9 | 0.005 | 14/39 (C-33 A, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.005 | 12/39 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.815×** | -3.7 | 0.008 | 11/38 (A-172, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.020 | 13/39 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 71.0 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.319× (z -10.5) |
| [[PANC-1 (line)]] | alt | 88.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 52.2 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.262× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 50.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.270× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 34.0 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.413× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 71.8 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.319× (z -10.3) |
| [[C-33 A (line)]] | alt | 57.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.266× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 58.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -9.7) |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.293× (z -12.0) |
| [[A-172 (line)]] | wt | 51.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.369× (z -8.6) |
| [[A-427 (line)]] | wt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 13.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +8.6) | [[Menadione (drug)]] 5 µM 0.0617× (z -9.5) |
| [[HCT15 (line)]] | alt | 78.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -11.1) |
| [[SW480 (line)]] | alt | 8.13 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.04× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 10.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.31× (z +10.1) | — |
| [[A549 (line)]] | wt | 58.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.389× (z -8.8) |
| [[C32 (line)]] | wt | 43.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.258× (z -10.4) |
| [[H4 (line)]] | wt | 37.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.264× (z -8.5) |
| [[HS-578T (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 71.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.407× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.19 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA2D1]] | +0.73 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ZFY]] | +0.71 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.68 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | +0.68 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[FKRP]] | +0.67 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[EFCAB2]] | +0.67 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SLC9A8]] | +0.67 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.67 | +0.61 / +0.33 | both halves | 1e-04 |  |
| [[ST7L]] | +0.66 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.66 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[GTF3C6]] | +0.65 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TIA1]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.68 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.68 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[ATP7B]] | -0.66 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[MPST]] | -0.64 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[WASF3]] | -0.63 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[NBPF3]] | -0.61 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[OSTF1]] | -0.61 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[POGLUT2]] | -0.61 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.61 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SDHAP1]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RGS10]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.61 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB1]] | B | CPEB1 activity raises VPS35L's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without CPEB1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[ANKRD18B]] | B | ANKRD18B activity raises VPS35L's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without ANKRD18B | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[ATP10D]] | C | ATP10D activity raises VPS35L's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 4.75× lower at baseline in the lines without ATP10D | 0.078 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPS7]] | B | VPS35L activity raises MRPS7's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without VPS35L | 0.032 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150 |
| [[COG5]] | B | VPS35L activity lowers COG5's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without VPS35L | 0.056 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150 |
| [[ESYT3]] | B | VPS35L activity raises ESYT3's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without VPS35L | 0.077 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150 |
| [[ATP10D]] | C | VPS35L activity raises ATP10D's level | lines that do not express VPS35L (9) vs lines expressing it (41) | 3.37× lower at baseline in the lines without VPS35L | 0.061 | ⚠ within organs, on part of the lines; also absent: HDGFL3, CHST11, RNF150; co-absent with the target |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (2.6, 8.4); signed map (18.8, -24.0). **Vector** length 98.7, 23.1% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.1 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.6 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.1 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -11.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -10.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -16.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -14.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | VPS35 endosomal protein sorting factor like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,555,240-19,706,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16824; previously C16orf62 |
| Gene groups (HGNC) | Retriever complex |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3J2](https://www.uniprot.org/uniprotkb/Q7Z3J2) (VPS35 endosomal protein-sorting factor-like):

> Acts as a component of the retriever complex. The retriever complex is a heterotrimeric complex related to retromer cargo-selective complex (CSC) and essential for retromer-independent retrieval and recycling of numerous cargos such as integrin alpha-5/beta-1 (ITGA5:ITGB1). The recruitment of the retriever complex to the endosomal membrane involves CCC and WASH complexes. In the endosomes, drives the retrieval and recycling of NxxY-motif-containing cargo proteins by coupling to SNX17, a cargo …

**Summary**, from NCBI Gene [57020](https://www.ncbi.nlm.nih.gov/gene/57020):

> Involved in Golgi to plasma membrane transport and endocytic recycling. Located in endosome. Part of protein-containing complex. Implicated in Ritscher-Schinzel syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24641) · Entrez [57020](https://www.ncbi.nlm.nih.gov/gene/57020) · UniProt [Q7Z3J2](https://www.uniprot.org/uniprotkb/Q7Z3J2) · Ensembl [ENSG00000103544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103544)

## Data

Gene col 2382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2382); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2382]; `tensor/DDL_lfc|DDL_z.npy` [2382]; `embed/gene_vectors.npy` [2382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2382 or target_col == 2382). Every well: [[VPS35L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS35L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
