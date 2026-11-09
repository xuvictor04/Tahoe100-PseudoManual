---
symbol: "CYS1"
type: "gene"
col: 13012
ensembl_id: "ENSG00000205795"
name: "cystin 1"
location: "2p25.1"
module: 128
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 28
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 13
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# CYS1

*cystin 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.27× (z +10.5, q 5e-23, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.37× (z +9.1, q 2e-17, up in 3 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.0901×, PANC-1 0.215×, A549 0.108×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 3 lines (A-427 0.151×, A549 0.0817×, A-172 0.172×); [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.0586×, PANC-1 0.226×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.137×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC36]] (+0.70, fdr 7e-06), [[TBX1]] (+0.64, fdr 7e-06), [[PDZD4]] (+0.62, fdr 1e-05); moves opposite to [[SNTB1]] (-0.43, fdr 2e-04), [[SLC12A8]] (-0.43, fdr 2e-04), [[CFAP44]] (-0.42, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 13 go from it, the strongest it → [[L1CAM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.27×** | +10.5 | 5e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +9.1 | 2e-17 | 3/14 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.33×** | +8.4 | 1e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +7.9 | 6e-13 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +6.5 | 9e-09 | 5/19 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +5.3 | 1e-05 | 4/14 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 2/22 (HOP62, C-33 A) | rises with dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +4.8 | 1e-04 | 4/9 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.002 | 1/11 (A-172) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.16×** | +4.1 | 0.002 | 1/7 (A549) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.006 | 1/12 (MIA PaCa-2) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.98×** | +3.7 | 0.012 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.92×** | +3.5 | 0.021 | 3/12 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.029 | 0/11 | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.56×** | +3.3 | 0.030 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.55×** | +3.3 | 0.034 | 3/19 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.038 | 1/12 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.047 | 1/11 (PANC-1) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.061 | 1/14 (AsPC-1) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.47×** | +2.9 | 0.097 | 0/12 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13012.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.0901×, PANC-1 0.215×, A549 0.108×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 3 lines (A-427 0.151×, A549 0.0817×, A-172 0.172×); [[Digitoxin (drug)]] 5 µM in 2 lines (HOP62 0.0586×, PANC-1 0.226×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.137×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -3.7 | 0.11 | 8/24 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.640× | -3.2 | 0.23 | 9/21 (A-172, MIA PaCa-2, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.643× | -3.2 | 0.23 | 6/19 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.659× | -3.2 | 0.23 | 5/21 (NCI-H460, RPMI-7951, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.75 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.172× (z -8.7) |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.9 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.137× (z -11.4) |
| [[A549 (line)]] | wt | 6.17 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0817× (z -10.0) |
| [[HOP62 (line)]] | alt | 5.31 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -12.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.774 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.796 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.205 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.902 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC36]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[TBX1]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[PDZD4]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS10]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[GBX1]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[DLK2]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[MAP6]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MIR493HG]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[KNDC1]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CECR2]] | +0.57 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[PAOX]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[MCF2L2]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB1]] | -0.43 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[SLC12A8]] | -0.43 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[CFAP44]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 14, C 5. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises CYS1's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without ELFN1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[FAM124A]] | B | FAM124A activity raises CYS1's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without FAM124A | 0.029 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[LRRC4B]] | B | LRRC4B activity raises CYS1's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without LRRC4B | 0.032 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[L1CAM]] | B | L1CAM activity raises CYS1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without L1CAM | 0.033 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[MAP3K15]] | B | MAP3K15 activity raises CYS1's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without MAP3K15 | 0.033 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[PAX2]] | B | PAX2 activity raises CYS1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.92× lower at baseline in the lines without PAX2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[CHD5]] | B | CHD5 activity raises CYS1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.84× lower at baseline in the lines without CHD5 | 0.061 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[MRC2]] | B | MRC2 activity raises CYS1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without MRC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[LINC00466]] | B | LINC00466 activity raises CYS1's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without LINC00466 | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[LIMCH1]] | B | LIMCH1 activity lowers CYS1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.53× higher at baseline in the lines without LIMCH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[DUSP9]] | B | DUSP9 activity raises CYS1's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 1.61× lower at baseline in the lines without DUSP9 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3 |
| [[CACNG7]] | B | CACNG7 activity raises CYS1's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.55× lower at baseline in the lines without CACNG7 | 0.089 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[L1CAM]] | B | CYS1 activity raises L1CAM's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without CYS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[CFAP298-TCP10L]] | B | CYS1 activity raises CFAP298-TCP10L's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without CYS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[FAM124A]] | B | CYS1 activity raises FAM124A's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without CYS1 | 0.030 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[SLC4A3]] | B | CYS1 activity raises SLC4A3's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.56× lower at baseline in the lines without CYS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[DNAAF9]] | B | CYS1 activity raises DNAAF9's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without CYS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[CDH23]] | B | CYS1 activity raises CDH23's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without CYS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[KIF3C]] | B | CYS1 activity raises KIF3C's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without CYS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[CIB2]] | B | CYS1 activity raises CIB2's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without CYS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[LIMCH1]] | B | CYS1 activity lowers LIMCH1's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.79× higher at baseline in the lines without CYS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[PDZD4]] | C | CYS1 activity raises PDZD4's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without CYS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4; co-absent with the target |
| [[DLK2]] | C | CYS1 activity raises DLK2's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without CYS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4; co-absent with the target |
| [[PALM]] | C | CYS1 activity raises PALM's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.42× lower at baseline in the lines without CYS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.5, 38.8); signed map (23.8, 25.2). **Vector** length 45.1, 10.9% of its response variance represented; |z| ≥ 3 in 479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +7.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | cystin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,056,473-10,080,944 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 5 pathways, smallest: Trafficking of myristoylated proteins to the cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

UniProt [Q717R9](https://www.uniprot.org/uniprotkb/Q717R9) carries no function annotation.

**Summary**, from NCBI Gene [192668](https://www.ncbi.nlm.nih.gov/gene/192668):

> Predicted to enable chromatin binding activity and transcription corepressor activity. Predicted to act upstream of or within inner ear development; kidney development; and regulation of DNA-templated transcription. Predicted to be located in ciliary basal body; membrane; and nucleus. Biomarker of stomach cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18525) · Entrez [192668](https://www.ncbi.nlm.nih.gov/gene/192668) · UniProt [Q717R9](https://www.uniprot.org/uniprotkb/Q717R9) · Ensembl [ENSG00000205795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205795)

## Data

Gene col 13012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13012); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13012]; `tensor/DDL_lfc|DDL_z.npy` [13012]; `embed/gene_vectors.npy` [13012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13012 or target_col == 13012). Every well: [[CYS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
