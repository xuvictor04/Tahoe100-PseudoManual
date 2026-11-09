---
symbol: "ERBB2"
type: "gene"
col: 6569
ensembl_id: "ENSG00000141736"
name: "erb-b2 receptor tyrosine kinase 2"
location: "17q12"
module: 27
arm: "+"
pooled_cpm: 44.04
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ERBB2

*erb-b2 receptor tyrosine kinase 2* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.49× (z +6.6, q 3e-08, up in 20 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.53× (z +3.7, q 0.044, up in 10 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.476× (z -12.1, q 5e-31, down in 39 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.658× (z -9.6, q 2e-19, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY6]] (+0.62, fdr 1e-05), [[DMTN]] (+0.59, fdr 1e-05), [[P4HTM]] (+0.55, fdr 6e-05); moves opposite to [[ST3GAL3]] (-0.52, fdr 2e-05), [[DDX50]] (-0.51, fdr 3e-05), [[HRH1]] (-0.49, fdr 6e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ERBB3]] → it (grade B ⚠); 3 go from it, the strongest it → [[CRYZL2P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.6 | 3e-08 | 20/41 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.7 | 9e-04 | 15/34 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.044 | 10/42 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.5 | 0.061 | 14/35 (HOP62, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.061 | 12/45 (SK-MEL-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.15× | +3.4 | 0.075 | 17/45 (HOP62, A-172, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.16 | 12/45 (HepG2/C3A, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.476×** | -12.1 | 5e-31 | 39/45 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.552×** | -9.7 | 1e-19 | 31/45 (LS 180, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -9.6 | 2e-19 | 29/44 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.571×** | -8.8 | 3e-16 | 31/45 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.589×** | -8.6 | 8e-16 | 33/44 (A-172, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -7.8 | 5e-13 | 29/44 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.630×** | -7.5 | 4e-12 | 33/45 (COLO 205, BT-474, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.635×** | -7.4 | 1e-11 | 28/44 (A-427, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -6.2 | 3e-08 | 27/44 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.682×** | -5.9 | 3e-07 | 23/45 (HT-29, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -5.4 | 4e-06 | 22/45 (SW1417, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.724×** | -5.2 | 8e-06 | 21/44 (NCI-H1792, J82, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.565×** | -4.9 | 5e-05 | 21/45 (HT-29, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -4.4 | 4e-04 | 3/46 (SW48, AN3 CA, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.765×** | -4.3 | 5e-04 | 22/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -4.3 | 6e-04 | 20/45 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.787×** | -3.7 | 0.007 | 14/45 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.015 | 9/45 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.772×** | -3.0 | 0.064 | 9/45 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 55.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -18.9) |
| [[LS 180 (line)]] | wt | 49.7 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.4) |
| [[A-172 (line)]] | wt | 30.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.0) |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -10.0) |
| [[BT-474 (line)]] | alt | 1,139 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.503× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 56.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 50.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -16.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 54.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 41.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -9.6) |
| [[A-427 (line)]] | wt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -14.8) |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -12.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~58% of this change |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY6]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 | same gene group; pathway: Intracellular signaling by second messengers |
| [[DMTN]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[P4HTM]] | +0.55 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[PLXNB1]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 | pathway: Sema4D in semaphorin signaling; STRING 994 |
| [[HOTAIR]] | +0.54 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[HOXB6]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TSPAN8]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[VSIG10]] | +0.53 | +0.42 / +0.37 | both halves | 7e-05 |  |
| [[GOLGA2P5]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[EVPL]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[NPEPPSP1]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SCNN1A]] | +0.51 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST3GAL3]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 | same gene group |
| [[DDX50]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[HRH1]] | -0.49 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[STK17A]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ITPR1]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers |
| [[AGPAT4]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SH3BGRL3]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 | STRING 616 |
| [[LUCAT1]] | -0.47 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[GK]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[SSH1]] | -0.46 | -0.39 / -0.37 | both halves | 7e-05 | same gene group |
| [[SLC25A51]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERBB3]] | B | ERBB3 activity raises ERBB2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without ERBB3 | 0.029 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[MUC1]] | B | MUC1 activity raises ERBB2's level | lines that do not express MUC1 (25) vs lines expressing it (25) | 2.20× lower at baseline in the lines without MUC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223 |
| [[TMC4]] | B | TMC4 activity raises ERBB2's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 1.59× lower at baseline in the lines without TMC4 | 0.049 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[SPINT1-AS1]] | B | SPINT1-AS1 activity raises ERBB2's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 2.31× lower at baseline in the lines without SPINT1-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3 |
| [[SCNN1A]] | B | SCNN1A activity raises ERBB2's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without SCNN1A | 0.052 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[TMPRSS2]] | B | TMPRSS2 activity strengthens ERBB2's drug response | lines that do not express TMPRSS2 (32) vs lines expressing it (13) | the lines without TMPRSS2 respond 0.54× as strongly (z diff +2.04); strongest at Homoharringtonine 5 µM: 0.73x vs 0.53x (z diff +3.3) | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; target measured in part of the lines; artifact flags |
| [[CRACDL]] | B | CRACDL activity raises ERBB2's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without CRACDL | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[MUC1]] | B | MUC1 activity strengthens ERBB2's drug response | lines that do not express MUC1 (22) vs lines expressing it (23) | the lines without MUC1 respond 0.58× as strongly (z diff +1.47); strongest at Ixazomib citrate 5 µM: 0.82x vs 0.61x (z diff +2.4) | 0.075 | ⚠ within organs, on part of the lines; also absent: TACSTD2, UCA1, RNF223; target measured in part of the lines; artifact flags |
| [[TMPRSS2]] | B | TMPRSS2 activity raises ERBB2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.43× lower at baseline in the lines without TMPRSS2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYZL2P]] | C | ERBB2 activity raises CRYZL2P's level | lines that do not express ERBB2 (3) vs lines expressing it (47) | 3.23× lower at baseline in the lines without ERBB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; its own permutation p |
| [[SEC16B]] | C | ERBB2 activity raises SEC16B's level | lines that do not express ERBB2 (3) vs lines expressing it (47) | 2.85× lower at baseline in the lines without ERBB2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; its own permutation p |
| [[PGAP3]] | C | ERBB2 activity raises PGAP3's level | lines that do not express ERBB2 (3) vs lines expressing it (47) | 2.21× lower at baseline in the lines without ERBB2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.306). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.5, 30.2); signed map (39.0, -14.3). **Vector** length 82.5, 16.8% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +5.7 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.9 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.8 |
| fall | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.7 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -7.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -7.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | erb-b2 receptor tyrosine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,687,914-39,730,426 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NEU, HER-2, CD340, HER2, c-ERB2, c-ERB-2, MLN-19, p185(erbB2); previously NGL |
| Gene groups (HGNC) | CD molecules; Minor histocompatibility antigens; Erb-b2 receptor tyrosine kinases; MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_DN, APOPTOSIS |
| Reactome | 46 pathways, smallest: Drug resistance in ERBB2 KD mutants; Drug resistance in ERBB2 TMD/JMD mutants; Drug-mediated inhibition of ERBB2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P04626](https://www.uniprot.org/uniprotkb/P04626) (Receptor tyrosine-protein kinase erbB-2):

> Protein tyrosine kinase that is part of several cell surface receptor complexes, but that apparently needs a coreceptor for ligand binding. Essential component of a neuregulin-receptor complex, although neuregulins do not interact with it alone. GP30 is a potential ligand for this receptor. Regulates outgrowth and stabilization of peripheral microtubules (MTs). Upon ERBB2 activation, the MEMO1-RHOA-DIAPH1 signaling pathway elicits the phosphorylation and thus the inhibition of GSK3B at cell …

**Summary**, from NCBI Gene [2064](https://www.ncbi.nlm.nih.gov/gene/2064):

> This gene encodes a member of the epidermal growth factor (EGF) receptor family of receptor tyrosine kinases. This protein has no ligand binding domain of its own and therefore cannot bind growth factors. However, it does bind tightly to other ligand-bound EGF receptor family members to form a heterodimer, stabilizing ligand binding and enhancing kinase-mediated activation of downstream signalling pathways, such as those involving mitogen-activated protein kinase and phosphatidylinositol-3 …

**Accessions** — [HGNC:3430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3430) · Entrez [2064](https://www.ncbi.nlm.nih.gov/gene/2064) · UniProt [P04626](https://www.uniprot.org/uniprotkb/P04626) · Ensembl [ENSG00000141736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141736)

## Data

Gene col 6569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6569); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6569]; `tensor/DDL_lfc|DDL_z.npy` [6569]; `embed/gene_vectors.npy` [6569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6569 or target_col == 6569). Every well: [[ERBB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERBB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
