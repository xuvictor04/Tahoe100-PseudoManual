---
symbol: "BAG1"
type: "gene"
col: 2838
ensembl_id: "ENSG00000107262"
name: "BAG cochaperone 1"
location: "9p13.3"
module: 8
arm: "+"
pooled_cpm: 34.55
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 42
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# BAG1

*BAG cochaperone 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.04× (z +13.9, q 3e-41, up in 32 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +11.3, q 1e-27, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.797× (z -6.3, q 1e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC16]] (+0.58, fdr 1e-05), [[TC2N]] (+0.56, fdr 1e-05), [[MUC4]] (+0.56, fdr 1e-05); moves opposite to [[APLN]] (-0.52, fdr 4e-05), [[CST6]] (-0.42, fdr 3e-04), [[SNX14]] (-0.42, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[TMC5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +13.9 | 3e-41 | 32/43 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +12.1 | 3e-31 | 36/45 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +11.4 | 1e-27 | 27/37 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +11.3 | 1e-27 | 31/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.6 | 1e-19 | 23/37 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +8.9 | 4e-17 | 31/47 (SW480, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +8.4 | 4e-15 | 23/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.2 | 3e-14 | 32/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +7.2 | 5e-11 | 28/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +7.1 | 9e-11 | 29/49 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +7.0 | 2e-10 | 26/45 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.7 | 9e-10 | 24/45 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 7e-08 | 19/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +6.0 | 7e-08 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +6.0 | 7e-08 | 26/48 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 1e-05 | 16/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +5.0 | 2e-05 | 23/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +5.0 | 2e-05 | 20/48 (LOX-IMVI, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 9e-05 | 16/46 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +4.6 | 1e-04 | 13/48 (Hs 766T, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -6.3 | 1e-07 | 25/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.736×** | -6.0 | 4e-07 | 25/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.839× | -4.9 | 2e-04 | 21/48 (AsPC-1, LS 180, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.781×** | -4.9 | 2e-04 | 19/48 (COLO 205, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.814×** | -3.8 | 0.019 | 16/45 (SW48, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.042 | 6/48 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | 0.835× | -3.4 | 0.048 | 9/46 (CHP-212, SW48, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.066 | 7/47 (AsPC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.9 | 8 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.90× (z +13.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 4.68× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 20.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.79× (z +9.6) | — |
| [[SW480 (line)]] | alt | 26.6 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.68× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.03× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.436× (z -10.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 15.6 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0608× (z -11.3) |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.126× (z -8.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 99.8 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.544× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.8) | — |
| [[SW48 (line)]] | wt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -8.9) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC16]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TC2N]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MUC4]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CATSPERB]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[KLF3]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MISP]] | +0.51 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PTPRR]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SPIRE2]] | +0.49 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[MYH14]] | +0.49 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TMC5]] | +0.49 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[SIDT1]] | +0.49 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLN]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[CST6]] | -0.42 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[SNX14]] | -0.42 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[VLDLR]] | -0.42 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[CSTF3-DT]] | -0.40 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[ZNF215]] | -0.40 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[FKBP3]] | -0.40 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[FASTKD1]] | -0.39 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[WDFY2]] | -0.39 | -0.39 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 42, C 0. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC5]] | B | TMC5 activity raises BAG1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without TMC5 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[TSPAN8]] | B | TSPAN8 activity raises BAG1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without TSPAN8 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises BAG1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without ELF3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[CATSPERB]] | B | CATSPERB activity raises BAG1's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without CATSPERB | 0.006 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[CYP4F12]] | B | CYP4F12 activity raises BAG1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 1.82× lower at baseline in the lines without CYP4F12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[ELF3]] | B | ELF3 activity raises BAG1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.91× lower at baseline in the lines without ELF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[MUC5B]] | B | MUC5B activity raises BAG1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.78× lower at baseline in the lines without MUC5B | 0.009 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[CD24]] | B | CD24 activity raises BAG1's level | lines that do not express CD24 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without CD24 | 0.010 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2 |
| [[CEACAM5]] | B | CEACAM5 activity raises BAG1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without CEACAM5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[SIDT1]] | B | SIDT1 activity raises BAG1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without SIDT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[PTPRR]] | B | PTPRR activity raises BAG1's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without PTPRR | 0.017 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[TOX3]] | B | TOX3 activity raises BAG1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without TOX3 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.460). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 55.4); signed map (60.1, 5.5). **Vector** length 101, 24.4% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +9.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +11.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +8.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.4 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.7 | -4.9 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | +0.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | BAG cochaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,247,820-33,264,720 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BAG cochaperones |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99933](https://www.uniprot.org/uniprotkb/Q99933) (BAG family molecular chaperone regulator 1):

> Co-chaperone for HSP70 and HSC70 chaperone proteins. Acts as a nucleotide-exchange factor (NEF) promoting the release of ADP from the HSP70 and HSC70 proteins thereby triggering client/substrate protein release. Nucleotide release is mediated via its binding to the nucleotide-binding domain (NBD) of HSPA8/HSC70 where as the substrate release is mediated via its binding to the substrate-binding domain (SBD) of HSPA8/HSC70. Inhibits the pro-apoptotic function of PPP1R15A, and has anti-apoptotic …

**Summary**, from NCBI Gene [573](https://www.ncbi.nlm.nih.gov/gene/573):

> The oncogene BCL2 is a membrane protein that blocks a step in a pathway leading to apoptosis or programmed cell death. The protein encoded by this gene binds to BCL2 and is referred to as BCL2-associated athanogene. It enhances the anti-apoptotic effects of BCL2 and represents a link between growth factor receptors and anti-apoptotic mechanisms. Multiple protein isoforms are encoded by this mRNA through the use of a non-AUG (CUG) initiation codon, and three alternative downstream AUG initiation …

**Accessions** — [HGNC:937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:937) · Entrez [573](https://www.ncbi.nlm.nih.gov/gene/573) · UniProt [Q99933](https://www.uniprot.org/uniprotkb/Q99933) · Ensembl [ENSG00000107262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107262)

## Data

Gene col 2838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2838); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2838]; `tensor/DDL_lfc|DDL_z.npy` [2838]; `embed/gene_vectors.npy` [2838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2838 or target_col == 2838). Every well: [[BAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
