---
symbol: "AVPI1"
type: "gene"
col: 4148
ensembl_id: "ENSG00000119986"
name: "arginine vasopressin induced 1"
location: "10q24.2"
module: 79
arm: "+"
pooled_cpm: 22.46
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# AVPI1

*arginine vasopressin induced 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.88× (z +6.2, q 3e-07, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.549× (z -5.9, q 2e-06, down in 23 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.0684×, NCI-H1792 0.0575×, RPMI-7951 0.0483×, HEC-1-A 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1792 0.0961×, SW 900 0.119×, A549 0.151×, SW48 0.164×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RPMI-7951 0.0740×, HT-29 0.115×, SNU-423 0.133×; ⚠ toxic; transcription drop); [[Adenosine (drug)]] 0.05 µM in 1 line (SHP-77 0.0702×); [[Trifluridine (drug)]] 0.05 µM in 1 line (SHP-77 0.0838×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFIL3]] (+0.68, fdr 7e-06), [[PTGES]] (+0.63, fdr 7e-06), [[EFNA4]] (+0.62, fdr 1e-05); moves opposite to [[ARHGAP31]] (-0.56, fdr 1e-05), [[MAPKAP1]] (-0.54, fdr 6e-05), [[XRCC5]] (-0.54, fdr 4e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MT1F]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +6.2 | 3e-07 | 29/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +6.0 | 4e-07 | 30/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +5.7 | 3e-06 | 32/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.008 | 16/46 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.0 | 0.008 | 20/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +3.4 | 0.074 | 16/46 (NCI-H460, LS 180, …) | all doses, flat | composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.074 | 17/47 (NCI-H460, SK-MEL-2, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | 1.84× | +3.1 | 0.12 | 12/41 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 1.30× | +3.0 | 0.17 | 13/47 (NCI-H460, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.0684×, NCI-H1792 0.0575×, RPMI-7951 0.0483×, HEC-1-A 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1792 0.0961×, SW 900 0.119×, A549 0.151×, SW48 0.164×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RPMI-7951 0.0740×, HT-29 0.115×, SNU-423 0.133×; ⚠ toxic; transcription drop); [[Adenosine (drug)]] 0.05 µM in 1 line (SHP-77 0.0702×); [[Trifluridine (drug)]] 0.05 µM in 1 line (SHP-77 0.0838×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -5.9 | 2e-06 | 23/37 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -5.0 | 2e-04 | 20/32 (RPMI-7951, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -4.5 | 0.001 | 21/30 (NCI-H1792, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.538× | -3.2 | 0.17 | 11/45 (HS-578T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.796× | -3.2 | 0.17 | 19/46 (CHP-212, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 59.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.76× (z +10.5) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -8.7) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0575× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 35.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.8) ⚠ cell-cycle shift, explains ~16% of this change |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0483× (z -14.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 5.80 | 0 | 2 | — | [[Adenosine (drug)]] 0.05 µM 0.0702× (z -9.1) |
| [[A549 (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0684× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFIL3]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[PTGES]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[EFNA4]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ARL4D]] | +0.61 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[EFNA3]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[SAP30]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[DEPP1]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[LAGE3]] | +0.57 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[DDIT4]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.56 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP31]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[MAPKAP1]] | -0.54 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[XRCC5]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MACROH2A1]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[DCTD]] | -0.53 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[MSANTD2]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MSN]] | -0.52 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[KRR1]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PRDM5]] | -0.52 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PDAP1]] | -0.52 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.51 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ELK4]] | -0.51 | -0.32 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1F]] | B | MT1F activity raises AVPI1's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without MT1F | 0.026 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[PTGES]] | B | PTGES activity raises AVPI1's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without PTGES | 0.070 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AVPI1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers AVPI1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAB20]] | B | RAB20 activity raises AVPI1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without RAB20 | 0.078 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[FLVCR2]] | B | FLVCR2 activity raises AVPI1's level | lines that do not express FLVCR2 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without FLVCR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: AIFM2, CTSD, ERAP2; maybe low, not absent; its own permutation p |
| [[DDIT4]] | C | DDIT4 activity raises AVPI1's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without DDIT4 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, -12.2); signed map (-7.8, 16.2). **Vector** length 108, 27.1% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +6.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.0 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Dapagliflozin (drug)]] 0.05 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | arginine vasopressin induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,677,424-97,687,241 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VIP32, PP5395, VIT32 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T686](https://www.uniprot.org/uniprotkb/Q5T686) (Arginine vasopressin-induced protein 1):

> May be involved in MAP kinase activation, epithelial sodium channel (ENaC) down-regulation and cell cycling.

**Summary**, from NCBI Gene [60370](https://www.ncbi.nlm.nih.gov/gene/60370):

> Predicted to be involved in positive regulation of MAPK cascade. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30898) · Entrez [60370](https://www.ncbi.nlm.nih.gov/gene/60370) · UniProt [Q5T686](https://www.uniprot.org/uniprotkb/Q5T686) · Ensembl [ENSG00000119986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119986)

## Data

Gene col 4148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4148); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4148]; `tensor/DDL_lfc|DDL_z.npy` [4148]; `embed/gene_vectors.npy` [4148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4148 or target_col == 4148). Every well: [[AVPI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AVPI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
