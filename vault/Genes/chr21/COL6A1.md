---
symbol: "COL6A1"
type: "gene"
col: 6598
ensembl_id: "ENSG00000142156"
name: "collagen type VI alpha 1 chain"
location: "21q22.3"
module: 13
arm: "+"
pooled_cpm: 110.27
n_lines_expressing: 26
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 30
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL6A1

*collagen type VI alpha 1 chain* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +12.7, q 3e-34, up in 20 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.34× (z +5.4, q 8e-06, up in 15 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 2.87×, NCI-H460 3.30×, Hs 766T 3.39×, RPMI-7951 2.66×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A498 2.85×, MIA PaCa-2 3.98×, NCI-H460 3.15×, KATO III 3.29×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW48 4.51×); [[Selinexor (drug)]] 5 µM in 1 line (KATO III 2.21×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.496× (z -9.2, q 2e-17, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A2]] (+0.86, fdr 7e-06), [[THBS2]] (+0.75, fdr 7e-06), [[ANPEP]] (+0.72, fdr 7e-06); moves opposite to [[SH2D4A]] (-0.45, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[GPR68]] → it (grade B ⚠); 19 go from it, the strongest it → [[CTSB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6598.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 2.87×, NCI-H460 3.30×, Hs 766T 3.39×, RPMI-7951 2.66×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A498 2.85×, MIA PaCa-2 3.98×, NCI-H460 3.15×, KATO III 3.29×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW48 4.51×); [[Selinexor (drug)]] 5 µM in 1 line (KATO III 2.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +12.7 | 3e-34 | 20/25 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +10.5 | 2e-23 | 18/23 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +8.0 | 2e-13 | 17/23 (RPMI-7951, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.4 | 8e-06 | 15/24 (KATO III, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.4 | 8e-06 | 10/26 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.52×** | +3.9 | 0.008 | 5/24 (AN3 CA, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.4 | 0.047 | 10/22 (Hs 766T, SW48, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -9.2 | 2e-17 | 19/24 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.630×** | -8.5 | 5e-15 | 18/24 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -4.3 | 0.003 | 13/24 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -4.0 | 0.008 | 13/24 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.794× | -3.0 | 0.25 | 8/23 (KATO III, NCI-H460, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.796× | -3.0 | 0.25 | 9/25 (CFPAC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 162 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 39.9 | 3 (3 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.54× (z +10.9) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.5 µM 0.0691× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 38.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.5) |
| [[HOP62 (line)]] | alt | 1,015 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -23.0) |
| [[KATO III (line)]] | alt | 34.9 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.83× (z +10.4) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.21× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 737 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.1) |
| [[A-172 (line)]] | wt | 176 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.0) |
| [[A498 (line)]] | wt | 61.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 75.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -21.1) |
| [[HS-578T (line)]] | alt | 525 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.4) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.326× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 1,088 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -12.6) |
| [[SW 1088 (line)]] | alt | 765 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.1) |
| [[Hs 766T (line)]] | wt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -14.0) |
| [[SW48 (line)]] | wt | 60.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +13.6) | — |
| [[A-427 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 25.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A2]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | same gene group; pathway: Assembly of collagen fibrils and other multimeric structures; STRING 998 |
| [[THBS2]] | +0.75 | +0.79 / +0.65 | both halves | 7e-06 | pathway: Signaling by PDGF; STRING 756 |
| [[ANPEP]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[IGF2]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SCUBE3]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[MMP2]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 | pathway: Collagen degradation; STRING 695 |
| [[DKK3]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PDGFRB]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 | pathway: Signaling by PDGF; STRING 460 |
| [[COL6A3]] | +0.64 | +0.71 / +0.55 | both halves | 1e-05 | same gene group; pathway: Assembly of collagen fibrils and other multimeric structures; STRING 994 |
| [[CSPG4]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 | STRING 435 |
| [[ITGA11]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 878 |
| [[COL5A1]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 879 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2D4A]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 6, C 24. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR68]] | B | GPR68 activity raises COL6A1's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without GPR68 | 0.036 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[TGFBI]] | B | TGFBI activity raises COL6A1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without TGFBI | 0.057 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[CSF1R]] | B | CSF1R activity raises COL6A1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 3.07× lower at baseline in the lines without CSF1R | 0.057 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[FAM167A]] | B | FAM167A activity raises COL6A1's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 3.22× lower at baseline in the lines without FAM167A | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[TNS1]] | B | TNS1 activity raises COL6A1's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without TNS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[LOXL1]] | B | LOXL1 activity raises COL6A1's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.80× lower at baseline in the lines without LOXL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[PDGFRB]] | C | PDGFRB activity raises COL6A1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 8.08× lower at baseline in the lines without PDGFRB | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises COL6A1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 5.29× lower at baseline in the lines without COL1A1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises COL6A1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 6.87× lower at baseline in the lines without SPARC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[COL6A2]] | C | COL6A2 activity raises COL6A1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 6.49× lower at baseline in the lines without COL6A2 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises COL6A1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.66× lower at baseline in the lines without WNT5A | 0.006 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[THBS2]] | C | THBS2 activity raises COL6A1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 5.51× lower at baseline in the lines without THBS2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 9, C 10. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSB]] | B | COL6A1 activity raises CTSB's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.37× lower at baseline in the lines without COL6A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[JARID2]] | B | COL6A1 activity raises JARID2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 1.65× lower at baseline in the lines without COL6A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[TGFB1I1]] | B | COL6A1 activity raises TGFB1I1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.35× lower at baseline in the lines without COL6A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[LAMC1]] | B | COL6A1 activity raises LAMC1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without COL6A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[JARID2]] | B | COL6A1 activity weakens JARID2's drug response | lines that do not express COL6A1 (23) vs lines expressing it (25) | the lines without COL6A1 respond 1.30× as strongly (z diff -1.12); strongest at Belinostat 5 µM: 1.98x vs 1.31x (z diff -4.3) | 0.048 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; target measured in part of the lines; artifact flags |
| [[LAMP1]] | B | COL6A1 activity raises LAMP1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without COL6A1 | 0.064 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[MMP14]] | B | COL6A1 activity raises MMP14's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 4.01× lower at baseline in the lines without COL6A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[PLOD3]] | B | COL6A1 activity raises PLOD3's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without COL6A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[BMP1]] | B | COL6A1 activity raises BMP1's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without COL6A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[COL6A2]] | C | COL6A1 activity raises COL6A2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 7.12× lower at baseline in the lines without COL6A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; co-absent with the target |
| [[THBS2]] | C | COL6A1 activity raises THBS2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 4.53× lower at baseline in the lines without COL6A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; co-absent with the target |
| [[COL1A2]] | C | COL6A1 activity raises COL1A2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 6.06× lower at baseline in the lines without COL6A1 | 0.030 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.7, 18.4); signed map (24.2, 44.5). **Vector** length 81.7, 26.6% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.9 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | collagen type VI alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:45,981,770-46,005,050 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Collagens |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 15 pathways, smallest: NCAM1 interactions; Collagen chain trimerization; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P12109](https://www.uniprot.org/uniprotkb/P12109) (Collagen alpha-1(VI) chain):

> Collagen VI acts as a cell-binding protein.

**Summary**, from NCBI Gene [1291](https://www.ncbi.nlm.nih.gov/gene/1291):

> The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The alpha2(VI) and alpha3(VI) chains are encoded by the COL6A2 and COL6A3 genes, respectively. The …

**Accessions** — [HGNC:2211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2211) · Entrez [1291](https://www.ncbi.nlm.nih.gov/gene/1291) · UniProt [P12109](https://www.uniprot.org/uniprotkb/P12109) · Ensembl [ENSG00000142156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142156)

## Data

Gene col 6598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6598); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6598]; `tensor/DDL_lfc|DDL_z.npy` [6598]; `embed/gene_vectors.npy` [6598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6598 or target_col == 6598). Every well: [[COL6A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL6A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
