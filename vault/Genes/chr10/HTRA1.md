---
symbol: "HTRA1"
type: "gene"
col: 9228
ensembl_id: "ENSG00000166033"
name: "HtrA serine peptidase 1"
location: "10q26.13"
module: 11
arm: "-"
pooled_cpm: 11.37
n_lines_expressing: 31
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# HTRA1

*HtrA serine peptidase 1* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +8.5, q 9e-15, up in 9 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.63× (z +7.1, q 1e-10, up in 19 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C32 4.87×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C32 4.62×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.365× (z -14.5, q 4e-45, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUSB]] (+0.56, fdr 3e-05), [[LDOC1]] (+0.54, fdr 2e-05), [[F2R]] (+0.53, fdr 2e-05); moves opposite to [[DAXX]] (-0.55, fdr 3e-05), [[CMAS]] (-0.51, fdr 4e-05), [[GCC1]] (-0.50, fdr 6e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 12 go from it, the strongest it → cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9228.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C32 4.87×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C32 4.62×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.5 | 9e-15 | 9/15 (C32, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.9 | 1e-12 | 15/19 (C32, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +7.6 | 6e-12 | 11/18 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +7.1 | 1e-10 | 19/29 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.033 | 8/28 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.365×** | -14.5 | 4e-45 | 25/28 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.248×** | -13.7 | 5e-40 | 25/28 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.359×** | -10.4 | 3e-23 | 22/27 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.436×** | -8.5 | 4e-15 | 21/28 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.424×** | -8.3 | 2e-14 | 21/28 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.637×** | -6.5 | 9e-09 | 24/29 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -5.9 | 3e-07 | 19/28 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.589×** | -5.4 | 5e-06 | 14/28 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.599×** | -5.1 | 2e-05 | 16/28 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.610×** | -5.0 | 3e-05 | 17/27 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.623×** | -4.8 | 8e-05 | 15/28 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.682×** | -3.8 | 0.006 | 15/28 (NCI-H23, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.492×** | -3.8 | 0.007 | 12/28 (RPMI-7951, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.598×** | -3.7 | 0.008 | 6/29 (H4, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.693×** | -3.7 | 0.008 | 14/28 (A-172, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.704×** | -3.6 | 0.013 | 14/27 (RPMI-7951, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.709×** | -3.4 | 0.020 | 11/28 (KATO III, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 28.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0565× (z -20.9) |
| [[C32 (line)]] | wt | 47.5 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 9.01 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0859× (z -13.6) |
| [[HOP62 (line)]] | alt | 57.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -19.6) |
| [[RPMI-7951 (line)]] | alt | 53.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -14.3) |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0818× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.158× (z -9.3) |
| [[A498 (line)]] | wt | 5.69 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -9.7) |
| [[Hs 766T (line)]] | wt | 46.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -11.6) |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0747× (z -13.6) |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0884× (z -11.0) |
| [[KATO III (line)]] | alt | 7.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0346× (z -13.8) |
| [[PANC-1 (line)]] | alt | 4.71 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0986× (z -9.8) |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -8.9) |
| [[SW480 (line)]] | alt | 5.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -9.9) |
| [[A-172 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSB]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[LDOC1]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[F2R]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[RPN2]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[HDAC1]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[RCN2]] | +0.50 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[FKBP1A]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[DKK3]] | +0.50 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[PIGS]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[C1GALT1C1]] | +0.49 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[IGFBP7]] | +0.48 | +0.49 / +0.49 | both halves | 1e-05 | STRING 536 |
| [[TGFBI]] | +0.48 | +0.44 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 560 |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAXX]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CMAS]] | -0.51 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GCC1]] | -0.50 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[FNBP4]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZNF525]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ZNF286B]] | -0.45 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[DNAJB2]] | -0.44 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[YDJC]] | -0.44 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[GATAD1]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[CCT6P3]] | -0.43 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[ASNSD1]] | -0.43 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SMARCAL1]] | -0.43 | -0.41 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HTRA1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LDOC1]] | B | LDOC1 activity raises HTRA1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 2.36× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; its own permutation p |
| [[ECM1]] | B | ECM1 activity raises HTRA1's level | lines that do not express ECM1 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without ECM1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SEMA5A, NLRP1, MMP14; maybe low, not absent |
| [[DKK3]] | C | DKK3 activity raises HTRA1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.28× lower at baseline in the lines without DKK3 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[HTRA3]] | C | HTRA3 activity raises HTRA1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without HTRA3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; co-absent with the target |
| [[SFRP1]] | C | SFRP1 activity raises HTRA1's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 2.94× lower at baseline in the lines without SFRP1 | 0.036 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[ANTXR1]] | C | ANTXR1 activity raises HTRA1's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.71× lower at baseline in the lines without ANTXR1 | 0.076 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |
| [[FAM20C]] | C | FAM20C activity raises HTRA1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without FAM20C | 0.089 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | B | HTRA1 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.84× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[LTBP1]] | B | HTRA1 activity raises LTBP1's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without HTRA1 | 0.048 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[SLC22A4]] | B | HTRA1 activity raises SLC22A4's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without HTRA1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | HTRA1 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.88× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[PCDHGC3]] | B | HTRA1 activity raises PCDHGC3's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without HTRA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| cells under [[Tucatinib (drug)]] 5 µM | B | HTRA1 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.81× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| cells under [[Clopidogrel (drug)]] 0.05 µM | B | HTRA1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.79× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| cells under [[Malotilate (drug)]] 0.05 µM | B | HTRA1 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.83× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[OLFML2A]] | B | HTRA1 activity raises OLFML2A's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without HTRA1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[FAM20C]] | C | HTRA1 activity raises FAM20C's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 4.19× lower at baseline in the lines without HTRA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1; co-absent with the target |
| [[DKK3]] | C | HTRA1 activity raises DKK3's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 4.03× lower at baseline in the lines without HTRA1 | 0.028 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1; co-absent with the target |
| [[ANTXR1]] | C | HTRA1 activity raises ANTXR1's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without HTRA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.340). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (60.5, 18.5); signed map (22.7, 41.2). **Vector** length 68.6, 15.8% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -13.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -10.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -6.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | HtrA serine peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,458,551-122,514,907 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HtrA, IGFBP5-protease, ARMD7; previously PRSS11 |
| Gene groups (HGNC) | PDZ domain containing; HtrA serine protease family |
| Hallmark sets | COAGULATION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92743](https://www.uniprot.org/uniprotkb/Q92743) (Serine protease HTRA1):

> Serine protease with a variety of targets, including extracellular matrix proteins such as fibronectin. HTRA1-generated fibronectin fragments further induce synovial cells to up-regulate MMP1 and MMP3 production. May also degrade proteoglycans, such as aggrecan, decorin and fibromodulin. Through cleavage of proteoglycans, may release soluble FGF-glycosaminoglycan complexes that promote the range and intensity of FGF signals in the extracellular space. Regulates the availability of insulin-like …

**Summary**, from NCBI Gene [5654](https://www.ncbi.nlm.nih.gov/gene/5654):

> This gene encodes a member of the trypsin family of serine proteases. This protein is a secreted enzyme that is proposed to regulate the availability of insulin-like growth factors (IGFs) by cleaving IGF-binding proteins. It has also been suggested to be a regulator of cell growth. Variations in the promoter region of this gene are the cause of susceptibility to age-related macular degeneration type 7. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9476) · Entrez [5654](https://www.ncbi.nlm.nih.gov/gene/5654) · UniProt [Q92743](https://www.uniprot.org/uniprotkb/Q92743) · Ensembl [ENSG00000166033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166033)

## Data

Gene col 9228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9228); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9228]; `tensor/DDL_lfc|DDL_z.npy` [9228]; `embed/gene_vectors.npy` [9228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9228 or target_col == 9228). Every well: [[HTRA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTRA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
