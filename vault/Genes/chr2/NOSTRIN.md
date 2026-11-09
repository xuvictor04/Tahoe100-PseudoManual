---
symbol: "NOSTRIN"
type: "gene"
col: 8628
ensembl_id: "ENSG00000163072"
name: "nitric oxide synthase trafficking"
location: "2q24.3"
module: 73
arm: "+"
pooled_cpm: 20.29
n_lines_expressing: 34
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 67
direction_downstream: 33
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# NOSTRIN

*nitric oxide synthase trafficking* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.96× (z +9.0, q 2e-16, up in 2 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.36× (z +6.0, q 3e-07, up in 7 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.665× (z -5.7, q 8e-06, down in 18 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEPH]] (+0.75, fdr 7e-06), [[LINC02582]] (+0.75, fdr 7e-06), [[CALB1]] (+0.72, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[NPSR1]] → it (grade B ⚠); 33 go from it, the strongest it → [[PDE9A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.0 | 2e-16 | 2/14 (J82, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +6.6 | 1e-08 | 5/16 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.0 | 3e-07 | 7/31 (HEC-1-A, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.2 | 3e-05 | 4/20 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +4.5 | 7e-04 | 12/31 (SW48, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.016 | 7/31 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.027 | 5/27 (NCI-H2030, SW1417, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.032 | 4/29 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.032 | 11/28 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.032 | 0/27 | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +3.4 | 0.034 | 8/27 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.665×** | -5.7 | 8e-06 | 18/31 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.670×** | -5.6 | 8e-06 | 18/30 (SW1417, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.734×** | -4.3 | 0.003 | 15/31 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.752×** | -4.0 | 0.011 | 16/30 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.756×** | -3.6 | 0.037 | 9/31 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.636×** | -3.3 | 0.093 | 9/30 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | 0.819× | -3.1 | 0.15 | 4/31 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.802× | -3.1 | 0.15 | 7/31 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.804× | -3.0 | 0.15 | 11/30 (SNU-1, COLO 205, …) | all doses, flat | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.799× | -3.0 | 0.15 | 10/28 (C-33 A, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 181 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.291× (z -8.8) |
| [[LoVo (line)]] | wt | 121 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.127× (z -15.0) |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0746× (z -9.6) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0835× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 137 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 48.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -18.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.138× (z -9.4) |
| [[A549 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0743× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0636× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 7.63 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.117× (z -9.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 6.46 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEPH]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[LINC02582]] | +0.75 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.72 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DSG4]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.71 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CYP3A5]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[VILL]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[B3GNT3]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[DSG3]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 64, C 3. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPSR1]] | B | NPSR1 activity raises NOSTRIN's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 6.28× lower at baseline in the lines without NPSR1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[GCNT3]] | B | GCNT3 activity raises NOSTRIN's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 4.28× lower at baseline in the lines without GCNT3 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[GDA]] | B | GDA activity raises NOSTRIN's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.89× lower at baseline in the lines without GDA | 6e-04 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[CDH17]] | B | CDH17 activity raises NOSTRIN's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.91× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[MUC17]] | B | MUC17 activity raises NOSTRIN's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 5.86× lower at baseline in the lines without MUC17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1 |
| [[GPA33]] | B | GPA33 activity raises NOSTRIN's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 4.64× lower at baseline in the lines without GPA33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[LINC02582]] | B | LINC02582 activity raises NOSTRIN's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 4.79× lower at baseline in the lines without LINC02582 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[B3GNT3]] | B | B3GNT3 activity raises NOSTRIN's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without B3GNT3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[HNF4A]] | B | HNF4A activity raises NOSTRIN's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without HNF4A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[NPSR1-AS1]] | B | NPSR1-AS1 activity raises NOSTRIN's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without NPSR1-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises NOSTRIN's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without MROH3P | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[LGALS4]] | B | LGALS4 activity raises NOSTRIN's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 4.34× lower at baseline in the lines without LGALS4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 29, C 4. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE9A]] | B | NOSTRIN activity raises PDE9A's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without NOSTRIN | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[HNF4A]] | B | NOSTRIN activity raises HNF4A's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.64× lower at baseline in the lines without NOSTRIN | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[KLK10]] | B | NOSTRIN activity raises KLK10's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.71× lower at baseline in the lines without NOSTRIN | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[LIPH]] | B | NOSTRIN activity raises LIPH's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.71× lower at baseline in the lines without NOSTRIN | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[SULF2]] | B | NOSTRIN activity raises SULF2's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without NOSTRIN | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[EPS8L3]] | B | NOSTRIN activity raises EPS8L3's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without NOSTRIN | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[XDH]] | B | NOSTRIN activity raises XDH's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without NOSTRIN | 0.028 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[MROH3P]] | B | NOSTRIN activity raises MROH3P's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without NOSTRIN | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[CATSPERB]] | B | NOSTRIN activity raises CATSPERB's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.98× lower at baseline in the lines without NOSTRIN | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[VILL]] | B | NOSTRIN activity raises VILL's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 1.53× lower at baseline in the lines without NOSTRIN | 0.045 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[TC2N]] | B | NOSTRIN activity raises TC2N's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 4.07× lower at baseline in the lines without NOSTRIN | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[ARHGEF38]] | B | NOSTRIN activity raises ARHGEF38's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.73× lower at baseline in the lines without NOSTRIN | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.2, 50.6); signed map (66.0, 8.2). **Vector** length 72.8, 16.5% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | nitric oxide synthase trafficking |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:168,786,539-168,865,514 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20702 |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Reactome | 2 pathways, smallest: NOSTRIN mediated eNOS trafficking; Metabolism of nitric oxide: NOS3 activation and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVI9](https://www.uniprot.org/uniprotkb/Q8IVI9) (Nostrin):

> Multivalent adapter protein which may decrease NOS3 activity by inducing its translocation away from the plasma membrane.

**Summary**, from NCBI Gene [115677](https://www.ncbi.nlm.nih.gov/gene/115677):

> Nitric oxide (NO) is a potent mediator in biologic processes such as neurotransmission, inflammatory response, and vascular homeostasis. NOSTRIN binds the enzyme responsible for NO production, endothelial NO synthase (ENOS; MIM 163729), and triggers the translocation of ENOS from the plasma membrane to vesicle-like subcellular structures, thereby attenuating ENOS-dependent NO production.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:20203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20203) · Entrez [115677](https://www.ncbi.nlm.nih.gov/gene/115677) · UniProt [Q8IVI9](https://www.uniprot.org/uniprotkb/Q8IVI9) · Ensembl [ENSG00000163072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163072)

## Data

Gene col 8628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8628); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8628]; `tensor/DDL_lfc|DDL_z.npy` [8628]; `embed/gene_vectors.npy` [8628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8628 or target_col == 8628). Every well: [[NOSTRIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOSTRIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
