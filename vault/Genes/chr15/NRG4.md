---
symbol: "NRG4"
type: "gene"
col: 9850
ensembl_id: "ENSG00000169752"
name: "neuregulin 4"
location: "15q24.2"
module: 19
arm: "+"
pooled_cpm: 10.27
n_lines_expressing: 40
n_dd_up: 28
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 10
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NRG4

*neuregulin 4* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +13.1, q 2e-36, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.543× (z -7.2, q 5e-10, down in 22 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH15]] (+0.60, fdr 7e-06), [[KCNMB2]] (+0.57, fdr 1e-05), [[CYP39A1]] (+0.56, fdr 1e-05); moves opposite to [[WDR27]] (-0.53, fdr 3e-05), [[VKORC1L1]] (-0.47, fdr 6e-05), [[CAD]] (-0.46, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC01967]] → it (grade B ⚠); 2 go from it, the strongest it → [[EFCAB7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +13.1 | 2e-36 | 19/31 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +11.1 | 5e-26 | 17/29 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +10.1 | 1e-21 | 8/21 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +9.1 | 1e-17 | 1/9 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +7.2 | 6e-11 | 19/35 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.5 | 6e-09 | 17/35 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +6.2 | 5e-08 | 16/33 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +5.5 | 2e-06 | 13/34 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +5.4 | 5e-06 | 13/34 (AsPC-1, NCI-H1573, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.1 | 2e-05 | 14/35 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 2e-05 | 11/34 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 6e-05 | 15/35 (SW480, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.6 | 2e-04 | 2/10 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.003 | 10/35 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.003 | 6/37 (NCI-H1573, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.005 | 1/26 (HOP62) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 14/37 (KATO III, NCI-H1573, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.009 | 14/33 (NCI-H1573, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -7.2 | 5e-10 | 22/35 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.646×** | -5.1 | 6e-05 | 14/34 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.646×** | -5.1 | 6e-05 | 17/34 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -4.6 | 6e-04 | 7/35 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.670×** | -4.5 | 7e-04 | 10/34 (AN3 CA, NCI-H1792, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.708×** | -4.1 | 0.005 | 12/35 (H4, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -4.0 | 0.006 | 15/36 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.722×** | -3.8 | 0.009 | 10/35 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.724×** | -3.8 | 0.009 | 10/32 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -3.8 | 0.010 | 10/38 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.033 | 10/34 (NCI-H460, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.4 | 0 | 19 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0612× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 141 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0503× (z -22.0) |
| [[HEC-1-A (line)]] | alt | 3.02 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +15.3) | — |
| [[SW480 (line)]] | alt | 9.63 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +8.9) | [[Digitoxin (drug)]] 0.5 µM 0.208× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0884× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -8.5) |
| [[SHP-77 (line)]] | alt | 32.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0914× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.3) |
| [[LoVo (line)]] | wt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 23.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.53× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +14.5) | — |
| [[NCI-H23 (line)]] | alt | 4.82 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0634× (z -9.9) |
| [[PANC-1 (line)]] | alt | 2.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 2.63 | 0 | 1 | — | [[Pentoxifylline (drug)]] 5 µM 0.0464× (z -9.0) |
| [[A-172 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH15]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[KCNMB2]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CYP39A1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PAX7]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[GNGT1]] | +0.53 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[ARHGAP25]] | +0.53 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ISM2]] | +0.52 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[C3orf49]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[AQP4-AS1]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[NKAIN2]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PALMD]] | +0.51 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[LIN7A]] | +0.51 | +0.40 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR27]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[VKORC1L1]] | -0.47 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[CAD]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[CCM2]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[PACS2]] | -0.45 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[MIPEP]] | -0.45 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[BRD9]] | -0.44 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[KCTD13]] | -0.43 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[GART]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01967]] | B | LINC01967 activity raises NRG4's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without LINC01967 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1 |
| [[POU6F2]] | B | POU6F2 activity raises NRG4's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 3.01× lower at baseline in the lines without POU6F2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |
| [[WDR72]] | B | WDR72 activity raises NRG4's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without WDR72 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2 |
| [[LINC00649]] | B | LINC00649 activity raises NRG4's level | lines that do not express LINC00649 (25) vs lines expressing it (25) | 1.88× lower at baseline in the lines without LINC00649 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent |
| [[EPHA3]] | B | EPHA3 activity raises NRG4's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without EPHA3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491 |
| [[GLDN]] | B | GLDN activity raises NRG4's level | lines that do not express GLDN (25) vs lines expressing it (25) | 1.37× lower at baseline in the lines without GLDN | 0.067 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[PCSK5]] | B | PCSK5 activity raises NRG4's level | lines that do not express PCSK5 (24) vs lines expressing it (26) | 1.71× lower at baseline in the lines without PCSK5 | 0.073 | ⚠ within organs, on part of the lines; also absent: ALOX5, PIK3AP1, HOXA9 |
| [[PALMD]] | B | PALMD activity raises NRG4's level | lines that do not express PALMD (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without PALMD | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent |
| [[POU6F2]] | B | POU6F2 activity weakens NRG4's drug response | lines that do not express POU6F2 (26) vs lines expressing it (9) | the lines without POU6F2 respond 13.83× as strongly (z diff -1.94); strongest at Homoharringtonine 5 µM: 2.82x vs 0.58x (z diff -8.5) | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[GNGT1]] | B | GNGT1 activity raises NRG4's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without GNGT1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB7]] | B | NRG4 activity raises EFCAB7's level | lines that do not express NRG4 (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without NRG4 | 0.057 | ⚠ within organs, on part of the lines; also absent: LHFPL6, ENSG00000288583; maybe low, not absent |
| [[NME9]] | B | NRG4 activity raises NME9's level | lines that do not express NRG4 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without NRG4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LHFPL6, ENSG00000288583; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.7, 35.2); signed map (43.7, 39.5). **Vector** length 76.3, 15.6% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -5.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | neuregulin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,935,969-76,059,795 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HRG4 |
| Gene groups (HGNC) | Neuregulins |
| Reactome | 27 pathways, smallest: PI3K events in ERBB4 signaling; ERBB2 Activates PTK6 Signaling; SHC1 events in ERBB4 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWG1](https://www.uniprot.org/uniprotkb/Q8WWG1) (Pro-neuregulin-4, membrane-bound isoform):

> Low affinity ligand for the ERBB4 tyrosine kinase receptor. Concomitantly recruits ERBB1 and ERBB2 coreceptors, resulting in ligand-stimulated tyrosine phosphorylation and activation of the ERBB receptors. Does not bind to the ERBB1, ERBB2 and ERBB3 receptors (By similarity).

**Summary**, from NCBI Gene [145957](https://www.ncbi.nlm.nih.gov/gene/145957):

> The neuregulins, including NRG4, activate type-1 growth factor receptors (see EGFR; MIM 131550) to initiating cell-to-cell signaling through tyrosine phosphorylation (Harari et al., 1999 [PubMed 10348342]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29862) · Entrez [145957](https://www.ncbi.nlm.nih.gov/gene/145957) · UniProt [Q8WWG1](https://www.uniprot.org/uniprotkb/Q8WWG1) · Ensembl [ENSG00000169752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169752)

## Data

Gene col 9850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9850); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9850]; `tensor/DDL_lfc|DDL_z.npy` [9850]; `embed/gene_vectors.npy` [9850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9850 or target_col == 9850). Every well: [[NRG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
