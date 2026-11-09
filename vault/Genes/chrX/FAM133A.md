---
symbol: "FAM133A"
type: "gene"
col: 10994
ensembl_id: "ENSG00000179083"
name: "family with sequence similarity 133 member A"
location: "Xq21.32"
module: 9
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 21
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FAM133A

*family with sequence similarity 133 member A* — Xq21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.55× (z +9.4, q 2e-18, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.01× (z +5.4, q 8e-06, up in 10 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRXN1]] (+0.63, fdr 1e-05), [[ARHGAP25]] (+0.59, fdr 1e-05), [[CSRNP3]] (+0.59, fdr 1e-05); moves opposite to [[SMG1P6]] (-0.47, fdr 1e-04), [[SLC25A39]] (-0.47, fdr 5e-05), [[MAN2B2]] (-0.46, fdr 9e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[FSTL5]] → it (grade C ⚠); 11 go from it, the strongest it → [[TMEFF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.55×** | +9.4 | 2e-18 | 5/5 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.68×** | +9.2 | 9e-18 | 3/3 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.19×** | +7.3 | 5e-11 | 2/3 (SNU-423, RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +5.4 | 8e-06 | 10/16 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **2.19×** | +4.3 | 0.002 | 2/5 (SK-MEL-2, RPMI-7951) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.3 | 0.002 | 4/11 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.65×** | +3.9 | 0.007 | 8/11 (SK-MEL-2, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.008 | 1/16 (SHP-77) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.6 | 0.020 | 5/7 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.88×** | +3.5 | 0.027 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.86×** | +3.4 | 0.032 | 6/9 (NCI-H460, RPMI-7951, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +3.2 | 0.071 | 10/14 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.78×** | +3.1 | 0.072 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.1 | 0.077 | 1/6 (RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.73×** | +3.0 | 0.087 | 3/9 (RPMI-7951, SNU-423, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.814 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.417 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRXN1]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP25]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CSRNP3]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CDH18]] | +0.58 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[HOXD8]] | +0.57 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[UNC80]] | +0.56 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[GPM6A]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[POU3F2]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[EIF1AY]] | +0.56 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[EPHA5]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[VENTXP1]] | +0.55 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[RALYL]] | +0.55 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P6]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SLC25A39]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[MAN2B2]] | -0.46 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[RABL2B]] | -0.45 | -0.11 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[VAMP3]] | -0.45 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[RNPS1]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[EFTUD2]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[BLTP2]] | -0.44 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL5]] | C | FSTL5 activity raises FAM133A's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without FSTL5 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[DISC1FP1]] | C | DISC1FP1 activity raises FAM133A's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without DISC1FP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[PTN]] | C | PTN activity raises FAM133A's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without PTN | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[LINC02315]] | C | LINC02315 activity raises FAM133A's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without LINC02315 | 0.048 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1; co-absent with the target |
| [[LINC01611]] | C | LINC01611 activity raises FAM133A's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 2.59× lower at baseline in the lines without LINC01611 | 0.061 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises FAM133A's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without FMN2 | 0.066 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises FAM133A's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without CDH18 | 0.067 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises FAM133A's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without POU3F2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |
| [[DMD]] | C | DMD activity raises FAM133A's level | lines that do not express DMD (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without DMD | 0.087 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises FAM133A's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.64× lower at baseline in the lines without LINC01287 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEFF2]] | B | FAM133A activity raises TMEFF2's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without FAM133A | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4 |
| [[EFTUD2]] | B | FAM133A activity raises EFTUD2's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 1.26× lower at baseline in the lines without FAM133A | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4 |
| [[BCL11A]] | B | FAM133A activity raises BCL11A's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without FAM133A | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4 |
| [[FMN2]] | C | FAM133A activity raises FMN2's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 4.35× lower at baseline in the lines without FAM133A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[EPHA5]] | C | FAM133A activity raises EPHA5's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 5.35× lower at baseline in the lines without FAM133A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[FSTL5]] | C | FAM133A activity raises FSTL5's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 4.40× lower at baseline in the lines without FAM133A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[DMD]] | C | FAM133A activity raises DMD's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 4.21× lower at baseline in the lines without FAM133A | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[EPHA5-AS1]] | C | FAM133A activity raises EPHA5-AS1's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without FAM133A | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[CDH18]] | C | FAM133A activity raises CDH18's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without FAM133A | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[CRISPLD1]] | C | FAM133A activity raises CRISPLD1's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 3.37× lower at baseline in the lines without FAM133A | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[ADGRL3]] | C | FAM133A activity raises ADGRL3's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without FAM133A | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.5, 37.8); signed map (46.7, 34.7). **Vector** length 23.0, 3.94% of its response variance represented; |z| ≥ 3 in 283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +2.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.3 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +0.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 133 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.32 — chrX:93,674,013-93,712,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP1-32F7.2, FLJ37659, CT115 |
| Matched by | ensembl_id |

UniProt [Q8N9E0](https://www.uniprot.org/uniprotkb/Q8N9E0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26748) · Entrez [286499](https://www.ncbi.nlm.nih.gov/gene/286499) · UniProt [Q8N9E0](https://www.uniprot.org/uniprotkb/Q8N9E0) · Ensembl [ENSG00000179083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179083)

## Data

Gene col 10994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10994); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10994]; `tensor/DDL_lfc|DDL_z.npy` [10994]; `embed/gene_vectors.npy` [10994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10994 or target_col == 10994). Every well: [[FAM133A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM133A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
