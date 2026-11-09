---
symbol: "ABCC10"
type: "gene"
col: 4544
ensembl_id: "ENSG00000124574"
name: "ATP binding cassette subfamily C member 10"
location: "6p21.1"
module: 2
arm: "+"
pooled_cpm: 9.71
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ABCC10

*ATP binding cassette subfamily C member 10* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.25× (z +12.7, q 5e-34, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -11.2, q 2e-26, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MON1A]] (+0.69, fdr 7e-06), [[ZBED4]] (+0.64, fdr 9e-06), [[CRLF3]] (+0.63, fdr 1e-05); moves opposite to [[DLEU7]] (-0.62, fdr 2e-05), [[CREB3L4]] (-0.61, fdr 3e-05), [[NDUFV2-AS1]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +12.7 | 5e-34 | 42/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +12.1 | 2e-31 | 36/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +11.7 | 4e-29 | 35/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.46×** | +5.9 | 6e-07 | 15/47 (NCI-H460, A-172, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.6 | 2e-06 | 17/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.41×** | +5.1 | 3e-05 | 13/38 (LoVo, HT-29, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.8 | 1e-04 | 11/47 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.6 | 4e-04 | 14/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.5 | 4e-04 | 6/47 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.010 | 11/47 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.034 | 3/43 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.063 | 5/48 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.22×** | +3.1 | 0.073 | 5/47 (A-172, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.089 | 4/47 (C32, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -11.2 | 2e-26 | 31/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.662×** | -9.2 | 1e-17 | 26/46 (PANC-1, HS-578T, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -7.5 | 2e-11 | 24/47 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.645×** | -6.9 | 8e-10 | 24/45 (C32, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -6.7 | 2e-09 | 20/40 (SNU-423, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -6.2 | 6e-08 | 25/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.696×** | -5.7 | 1e-06 | 19/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -4.5 | 4e-04 | 14/47 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.745×** | -4.3 | 0.001 | 13/26 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -4.3 | 0.001 | 17/43 (RPMI-7951, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.830×** | -4.2 | 0.002 | 15/46 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.793×** | -3.5 | 0.020 | 17/46 (PANC-1, A-427, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.821×** | -3.1 | 0.080 | 12/34 (Panc 03.27, PANC-1, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -15.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -10.0) |
| [[C32 (line)]] | wt | 8.15 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0754× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.103× (z -8.5) |
| [[HCT15 (line)]] | alt | 7.75 | 0 | 2 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0808× (z -8.8) |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -8.7) |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0766× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 8.96 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.0) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -10.0) |
| [[RKO (line)]] | wt | 11.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -10.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -9.4) |
| [[A498 (line)]] | wt | 4.22 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0781× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H460 (line)]] | wt | 7.30 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.217× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -8.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.05 µM 0.0397× (z -11.5) |
| [[A-172 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MON1A]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZBED4]] | +0.64 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CRLF3]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TEX2]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[STK25]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MTG1]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[EIF2B3]] | +0.62 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[PACC1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.61 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[SPRYD3]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[RPS6KA4]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 | same gene group |
| [[HERC2P2]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU7]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CREB3L4]] | -0.61 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NDUFV2-AS1]] | -0.58 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[STAG2]] | -0.58 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SATB1]] | -0.57 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[STX17-DT]] | -0.57 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[N4BP2L1]] | -0.57 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ATOSA]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[BDH2]] | -0.56 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[DNAH7]] | -0.56 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[LINC02694]] | -0.56 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[C11orf71]] | -0.56 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises ABCC10's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without GNAZ | 0.012 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[HNMT]] | B | HNMT activity lowers ABCC10's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.42× higher at baseline in the lines without HNMT | 0.055 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[BSN]] | B | BSN activity raises ABCC10's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without BSN | 0.068 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[SATB1]] | B | SATB1 activity lowers ABCC10's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.31× higher at baseline in the lines without SATB1 | 0.084 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[CDYL2]] | B | CDYL2 activity lowers ABCC10's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 1.21× higher at baseline in the lines without CDYL2 | 0.093 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.3, -27.2); signed map (-45.1, -14.7). **Vector** length 62.9, 9.37% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | +2.7 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +12.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.6 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -6.1 | -9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -2.7 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.1 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +3.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,427,366-43,450,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EST182763, MRP7, SIMRP7 |
| Gene groups (HGNC) | ATP binding cassette subfamily C; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T3U5](https://www.uniprot.org/uniprotkb/Q5T3U5) (ATP-binding cassette sub-family C member 10):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that actively extrudes physiological compounds, and xenobiotics from cells. Lipophilic anion transporter that mediates ATP-dependent transport of glucuronide conjugates such as estradiol-17-beta-o-glucuronide and GSH conjugates such as leukotriene C4 (LTC4). May regulate the transport of organic compounds in testes across the blood-testis-barrier (Probable). Mediates intercellular propagation of antiviral immune signaling in …

**Summary**, from NCBI Gene [89845](https://www.ncbi.nlm.nih.gov/gene/89845):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, and White). This ABC full-transporter is a member of the MRP subfamily which is involved in multi-drug resistance. Multiple transcript variants encoding different isoforms have been found for this gene.[provided …

**Accessions** — [HGNC:52](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52) · Entrez [89845](https://www.ncbi.nlm.nih.gov/gene/89845) · UniProt [Q5T3U5](https://www.uniprot.org/uniprotkb/Q5T3U5) · Ensembl [ENSG00000124574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124574)

## Data

Gene col 4544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4544); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4544]; `tensor/DDL_lfc|DDL_z.npy` [4544]; `embed/gene_vectors.npy` [4544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4544 or target_col == 4544). Every well: [[ABCC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
