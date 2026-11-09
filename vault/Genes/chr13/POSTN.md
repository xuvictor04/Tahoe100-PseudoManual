---
symbol: "POSTN"
type: "gene"
col: 5417
ensembl_id: "ENSG00000133110"
name: "periostin"
location: "13q13.3"
module: 66
arm: "+"
pooled_cpm: 22.99
n_lines_expressing: 12
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 14
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# POSTN

*periostin* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.20× (z +14.3, q 2e-43, up in 8 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +6.8, q 2e-09, up in 8 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.190×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL3A1]] (+0.77, fdr 7e-06), [[CHRDL1]] (+0.71, fdr 7e-06), [[EFEMP1]] (+0.68, fdr 1e-05); moves opposite to [[DCLRE1C]] (-0.47, fdr 8e-05), [[NDUFB9]] (-0.45, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[COL1A1]] → it (grade C ⚠); 14 go from it, the strongest it → [[BACE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.20×** | +14.3 | 2e-43 | 8/9 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.47×** | +12.8 | 6e-35 | 8/9 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.20×** | +10.4 | 6e-23 | 7/9 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.8 | 2e-09 | 8/9 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +4.7 | 3e-04 | 4/10 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.12×** | +4.7 | 3e-04 | 3/5 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.5 | 6e-04 | 2/9 (LOX-IMVI, HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.16×** | +4.3 | 0.001 | 2/8 (RPMI-7951, LOX-IMVI) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.61×** | +3.7 | 0.013 | 2/9 (HOP62, HS-578T) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.7 | 0.014 | 4/9 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +3.6 | 0.017 | 3/9 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.046 | 4/10 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.47× | +3.0 | 0.12 | 5/10 (NCI-H1792, LOX-IMVI, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5417.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.190×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.874× | -3.7 | 0.13 | 0/10 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.736× | -3.4 | 0.17 | 9/10 (A-172, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.642× | -3.2 | 0.23 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 533 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.190× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 90.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL3A1]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_ANGIOGENESIS; STRING 976 |
| [[CHRDL1]] | +0.71 | +0.59 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EFEMP1]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 | STRING 508 |
| [[FSTL1]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ANGIOGENESIS; STRING 450 |
| [[MXRA8]] | +0.64 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[LUM]] | +0.63 | +0.43 / +0.68 | both halves | 3e-05 | pathway: HALLMARK_ANGIOGENESIS; STRING 913 |
| [[COL12A1]] | +0.63 | +0.40 / +0.65 | both halves | 5e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 669 |
| [[MYL9]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TGFBI]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 643 |
| [[MMP2]] | +0.61 | +0.50 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 787 |
| [[THY1]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 551 |
| [[OLFML2A]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1C]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[NDUFB9]] | -0.45 | -0.38 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL1A1]] | C | COL1A1 activity raises POSTN's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.47× lower at baseline in the lines without COL1A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[THY1]] | C | THY1 activity raises POSTN's level | lines that do not express THY1 (38) vs lines expressing it (12) | 4.62× lower at baseline in the lines without THY1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises POSTN's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.73× lower at baseline in the lines without FBN1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises POSTN's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 4.73× lower at baseline in the lines without COL1A2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[BCAT1]] | C | BCAT1 activity raises POSTN's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 3.13× lower at baseline in the lines without BCAT1 | 0.085 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |
| [[LUM]] | C | LUM activity raises POSTN's level | lines that do not express LUM (34) vs lines expressing it (16) | 4.40× lower at baseline in the lines without LUM | 0.087 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises POSTN's level | lines that do not express SPARC (34) vs lines expressing it (16) | 3.36× lower at baseline in the lines without SPARC | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 1, C 13. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACE1]] | B | POSTN activity raises BACE1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 1.48× lower at baseline in the lines without POSTN | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1 |
| [[ITGA4]] | C | POSTN activity raises ITGA4's level | lines that do not express POSTN (38) vs lines expressing it (12) | 6.92× lower at baseline in the lines without POSTN | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[MMP2]] | C | POSTN activity raises MMP2's level | lines that do not express POSTN (38) vs lines expressing it (12) | 7.09× lower at baseline in the lines without POSTN | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[SPARC]] | C | POSTN activity raises SPARC's level | lines that do not express POSTN (38) vs lines expressing it (12) | 10.14× lower at baseline in the lines without POSTN | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[FSTL1]] | C | POSTN activity raises FSTL1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 5.14× lower at baseline in the lines without POSTN | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[BCAT1]] | C | POSTN activity raises BCAT1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 6.51× lower at baseline in the lines without POSTN | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[FBN1]] | C | POSTN activity raises FBN1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 5.11× lower at baseline in the lines without POSTN | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[THY1]] | C | POSTN activity raises THY1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 5.15× lower at baseline in the lines without POSTN | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[CDH2]] | C | POSTN activity raises CDH2's level | lines that do not express POSTN (38) vs lines expressing it (12) | 7.64× lower at baseline in the lines without POSTN | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[COL3A1]] | C | POSTN activity raises COL3A1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 8.52× lower at baseline in the lines without POSTN | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[CCDC80]] | C | POSTN activity raises CCDC80's level | lines that do not express POSTN (38) vs lines expressing it (12) | 4.70× lower at baseline in the lines without POSTN | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[COL1A1]] | C | POSTN activity raises COL1A1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 5.94× lower at baseline in the lines without POSTN | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (57.3, 22.9); signed map (43.8, 21.7). **Vector** length 26.4, 7.30% of its response variance represented; |z| ≥ 3 in 186 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.53 to 16); *Integrin cell surface interactions* (reactome, mean cos +0.53 to 10); *ECM proteoglycans* (reactome, mean cos +0.55 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.6 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.5 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | periostin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:37,562,583-37,598,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OSF-2, PN, periostin |
| Gene groups (HGNC) | Gla domain containing |
| Hallmark sets | ANGIOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15063](https://www.uniprot.org/uniprotkb/Q15063) (Periostin):

> Induces cell attachment and spreading and plays a role in cell adhesion. Enhances incorporation of BMP1 in the fibronectin matrix of connective tissues, and subsequent proteolytic activation of lysyl oxidase LOX (By similarity).

**Summary**, from NCBI Gene [10631](https://www.ncbi.nlm.nih.gov/gene/10631):

> This gene encodes a secreted extracellular matrix protein that functions in tissue development and regeneration, including wound healing, and ventricular remodeling following myocardial infarction. The encoded protein binds to integrins to support adhesion and migration of epithelial cells. This protein plays a role in cancer stem cell maintenance and metastasis. Mice lacking this gene exhibit cardiac valve disease, and skeletal and dental defects. Alternative splicing results in multiple …

**Accessions** — [HGNC:16953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16953) · Entrez [10631](https://www.ncbi.nlm.nih.gov/gene/10631) · UniProt [Q15063](https://www.uniprot.org/uniprotkb/Q15063) · Ensembl [ENSG00000133110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133110)

## Data

Gene col 5417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5417); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5417]; `tensor/DDL_lfc|DDL_z.npy` [5417]; `embed/gene_vectors.npy` [5417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5417 or target_col == 5417). Every well: [[POSTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POSTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
