---
symbol: "SEMA6A"
type: "gene"
col: 1698
ensembl_id: "ENSG00000092421"
name: "semaphorin 6A"
location: "5q23.1"
module: 9
arm: "+"
pooled_cpm: 11.15
n_lines_expressing: 32
n_dd_up: 44
n_dd_down: 2
n_dd_up_clean: 38
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SEMA6A

*semaphorin 6A* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.55× (z +30.2, q 0e+00, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.756× (z -4.2, q 0.007, down in 7 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AN3 CA 0.0768×, SK-MEL-2 0.366×, NCI-H460 0.322×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0570×, NCI-H1573 0.120×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (A498 0.178×, AN3 CA 0.180×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0608×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPARGC1A]] (+0.55, fdr 2e-05), [[ASXL3]] (+0.54, fdr 7e-05), [[ENPP2]] (+0.52, fdr 1e-04); moves opposite to [[LRRK1]] (-0.48, fdr 1e-04), [[ITGA9-AS1]] (-0.44, fdr 5e-04), [[RECQL5]] (-0.41, fdr 9e-04, ⚠ not reproduced), [[MOCOS]] (-0.39, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC02327]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMOD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.55×** | +30.2 | 0e+00 | 26/29 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.13×** | +30.0 | 0e+00 | 28/29 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.72×** | +28.5 | 0e+00 | 26/29 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **5.20×** | +24.6 | 0e+00 | 27/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.77×** | +23.4 | 0e+00 | 26/29 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.00×** | +16.4 | 0e+00 | 26/28 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +13.5 | 2e-39 | 15/26 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +11.4 | 2e-28 | 11/27 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.78×** | +10.4 | 2e-23 | 24/27 (LS 180, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.3 | 5e-19 | 2/22 (LoVo, LS 180) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +8.4 | 2e-15 | 2/17 (LOX-IMVI, SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.76×** | +8.1 | 2e-14 | 17/28 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +7.7 | 5e-13 | 13/26 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +6.9 | 2e-10 | 18/27 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.2 | 3e-08 | 13/29 (C32, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 2e-07 | 11/28 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.2 | 6e-06 | 4/26 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1698.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AN3 CA 0.0768×, SK-MEL-2 0.366×, NCI-H460 0.322×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0570×, NCI-H1573 0.120×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (A498 0.178×, AN3 CA 0.180×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.0608×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.756×** | -4.2 | 0.007 | 7/27 (NCI-H1573, AN3 CA, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.756×** | -4.2 | 0.007 | 8/29 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.9 | 0.016 | 5/30 (A549, LS 180, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.809× | -3.0 | 0.34 | 4/28 (SNU-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 250 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0768× (z -19.6) |
| [[A-427 (line)]] | wt | 10.00 | 6 | 1 | [[Panobinostat (drug)]] 5 µM 16.2× (z +12.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -9.1) |
| [[LoVo (line)]] | wt | 5.96 | 6 | 1 | [[Tucidinostat (drug)]] 5 µM 9.11× (z +12.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.115× (z -8.9) |
| [[LS 180 (line)]] | wt | 6.82 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 8.60× (z +10.8) | — |
| [[SW480 (line)]] | alt | 7.61 | 7 | 0 | [[Tucidinostat (drug)]] 5 µM 5.88× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 17.3× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 16.9 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 7.37× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.6) |
| [[A498 (line)]] | wt | 21.7 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.01× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.178× (z -10.6) |
| [[C32 (line)]] | wt | 20.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.99× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 4.87 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 21.1× (z +11.0) | [[Oxaprozin (drug)]] 0.5 µM 0.0640× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 47.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.98× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -13.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 63.7 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.01× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.0) |
| [[COLO 205 (line)]] | alt | 12.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +9.9) | [[Temsirolimus (drug)]] 0.5 µM 0.102× (z -8.6) |
| [[H4 (line)]] | wt | 19.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.4× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 60.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 4.39 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 20.7× (z +8.8) | — |
| [[A549 (line)]] | wt | 2.93 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.07× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 2.89 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.12× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 5.97 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.41× (z +9.0) | — |
| [[A-172 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPARGC1A]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ASXL3]] | +0.54 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[ENPP2]] | +0.52 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[TSPAN7]] | +0.52 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[MGP]] | +0.50 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[PGM2L1]] | +0.49 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[ABCB1]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[LINC02327]] | +0.49 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[SEMA6D]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 | same gene group; pathway: Other semaphorin interactions |
| [[SOX4]] | +0.48 | +0.38 / +0.37 | both halves | 7e-05 |  |
| [[PDZRN3]] | +0.48 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[DCT]] | +0.48 | +0.40 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRK1]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ITGA9-AS1]] | -0.44 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[RECQL5]] | -0.41 | -0.19 / -0.49 | ⚠ not reproduced | 9e-04 |  |
| [[ZNG1E]] | -0.40 | -0.20 / -0.42 | ⚠ not reproduced | 8e-04 |  |
| [[MORN1]] | -0.40 | -0.10 / -0.47 | ⚠ not reproduced | 0.003 |  |
| [[ACAD9]] | -0.39 | -0.09 / -0.50 | ⚠ not reproduced | 0.003 |  |
| [[MOCOS]] | -0.39 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[SP2-AS1]] | -0.38 | -0.19 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[ZNG1C]] | -0.38 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[NMNAT1]] | -0.38 | -0.11 / -0.44 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02327]] | B | LINC02327 activity raises SEMA6A's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 4.22× lower at baseline in the lines without LINC02327 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605 |
| [[CCDC144NL-AS1]] | B | CCDC144NL-AS1 activity raises SEMA6A's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.57× lower at baseline in the lines without CCDC144NL-AS1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent |
| [[ASXL3]] | B | ASXL3 activity raises SEMA6A's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without ASXL3 | 0.030 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent |
| [[CNTN1]] | B | CNTN1 activity raises SEMA6A's level | lines that do not express CNTN1 (33) vs lines expressing it (17) | 2.21× lower at baseline in the lines without CNTN1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR141, MAGEB2, S100A9 |
| [[GNAI1]] | B | GNAI1 activity lowers SEMA6A's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 1.47× higher at baseline in the lines without GNAI1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |
| [[KCNH7]] | B | KCNH7 activity raises SEMA6A's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without KCNH7 | 0.069 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[CDH7]] | B | CDH7 activity raises SEMA6A's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.42× lower at baseline in the lines without CDH7 | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9 |
| [[SOX2]] | B | SOX2 activity raises SEMA6A's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without SOX2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA |
| [[LRRK1]] | B | LRRK1 activity lowers SEMA6A's level | lines that do not express LRRK1 (10) vs lines expressing it (40) | 3.06× higher at baseline in the lines without LRRK1 | 0.094 | ⚠ within organs, on part of the lines; also absent: HRH1, ALS2CL, CTSZ; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMOD1]] | B | SEMA6A activity lowers TMOD1's level | lines that do not express SEMA6A (18) vs lines expressing it (32) | 1.78× higher at baseline in the lines without SEMA6A | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000290588, NELL2, KSR2; maybe low, not absent |
| [[LRRK1]] | B | SEMA6A activity lowers LRRK1's level | lines that do not express SEMA6A (18) vs lines expressing it (32) | 1.97× higher at baseline in the lines without SEMA6A | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000290588, NELL2, KSR2; maybe low, not absent |
| [[CNTN1]] | B | SEMA6A activity raises CNTN1's level | lines that do not express SEMA6A (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without SEMA6A | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000290588, NELL2, KSR2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.4, 29.9); signed map (36.0, 35.5). **Vector** length 65.0, 12.6% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +30.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +5.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.9 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.1 — chr5:116,443,555-116,574,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1368, SEMA6A1, SEMA, HT018; previously SEMAQ |
| Gene groups (HGNC) | Semaphorins |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2E6](https://www.uniprot.org/uniprotkb/Q9H2E6) (Semaphorin-6A):

> Cell surface receptor for PLXNA2 that plays an important role in cell-cell signaling. Required for normal granule cell migration in the developing cerebellum. Promotes reorganization of the actin cytoskeleton and plays an important role in axon guidance in the developing central nervous system. Can act as repulsive axon guidance cue. Has repulsive action towards migrating granular neurons. May play a role in channeling sympathetic axons into the sympathetic chains and controlling the temporal …

**Summary**, from NCBI Gene [57556](https://www.ncbi.nlm.nih.gov/gene/57556):

> Predicted to enable several functions, including chemorepellent activity; identical protein binding activity; and semaphorin receptor binding activity. Involved in cellular response to vascular endothelial growth factor stimulus; negative regulation of cell adhesion involved in sprouting angiogenesis; and negative regulation of signal transduction. Predicted to be located in axon and membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10738) · Entrez [57556](https://www.ncbi.nlm.nih.gov/gene/57556) · UniProt [Q9H2E6](https://www.uniprot.org/uniprotkb/Q9H2E6) · Ensembl [ENSG00000092421](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092421)

## Data

Gene col 1698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1698); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1698]; `tensor/DDL_lfc|DDL_z.npy` [1698]; `embed/gene_vectors.npy` [1698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1698 or target_col == 1698). Every well: [[SEMA6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
