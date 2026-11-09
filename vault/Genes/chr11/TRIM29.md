---
symbol: "TRIM29"
type: "gene"
col: 6050
ensembl_id: "ENSG00000137699"
name: "tripartite motif containing 29"
location: "11q23.3"
module: 106
arm: "+"
pooled_cpm: 6.76
n_lines_expressing: 22
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 28
direction_downstream: 63
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TRIM29

*tripartite motif containing 29* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.14× (z +17.4, q 0e+00, up in 12 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.0941×, SW480 0.371×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.462×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGPP2]] (+0.66, fdr 1e-05), [[RHOU]] (+0.62, fdr 1e-05), [[BATF]] (+0.59, fdr 1e-05); moves opposite to [[ANTXR2]] (-0.44, fdr 4e-05), [[ARPC5L]] (-0.44, fdr 1e-04), [[FAM3C2P]] (-0.44, fdr 2e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[COL16A1]] → it (grade B ⚠); 63 go from it, the strongest it → [[KLF3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.14×** | +17.4 | 0e+00 | 12/18 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +11.8 | 1e-29 | 11/13 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.48×** | +10.4 | 5e-23 | 7/9 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.41×** | +10.2 | 2e-22 | 14/19 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +9.0 | 2e-17 | 2/18 (A-172, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +8.7 | 3e-16 | 5/12 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +8.3 | 8e-15 | 8/17 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +7.4 | 8e-12 | 12/19 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +5.4 | 4e-06 | 9/17 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.26×** | +5.4 | 5e-06 | 4/5 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.67×** | +5.2 | 9e-06 | 10/19 (NCI-H1573, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.83×** | +5.2 | 9e-06 | 7/18 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.8 | 8e-05 | 3/14 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.70×** | +4.6 | 2e-04 | 6/19 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +4.3 | 6e-04 | 1/12 (Hs 766T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.002 | 7/19 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.003 | 8/17 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.003 | 10/19 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.008 | 6/16 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.009 | 5/17 (Hs 766T, A-172, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.016 | 6/17 (NCI-H1573, AsPC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.0941×, SW480 0.371×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.462×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.672× | -3.5 | 0.27 | 1/18 (Hs 766T) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 5 µM |  | 0.496× | -3.2 | 0.27 | 0/19 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.694× | -3.2 | 0.27 | 2/19 (CFPAC-1, HepG2/C3A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 33.2 | 2 | 0 | [[Triamcinolone (drug)]] 5 µM 4.18× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 49.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +15.2) | — |
| [[A-172 (line)]] | wt | 3.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 9.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.37× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 3.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +10.8) | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0941× (z -15.3) |
| [[A-427 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.825 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPP2]] | +0.66 | +0.72 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[RHOU]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BATF]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[FLVCR2]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[PLEKHG6]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PHACTR3]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[DNAJC15]] | +0.55 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[PLEKHA7]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MAOA]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[PPA1]] | +0.54 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PELI1]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR2]] | -0.44 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ARPC5L]] | -0.44 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[FAM3C2P]] | -0.44 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[KIAA0753]] | -0.41 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 5, C 23. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL16A1]] | B | COL16A1 activity raises TRIM29's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without COL16A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises TRIM29's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.98× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.042 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[LGALS3]] | B | LGALS3 activity raises TRIM29's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without LGALS3 | 0.068 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[SAA2]] | B | SAA2 activity raises TRIM29's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without SAA2 | 0.088 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[PHACTR3]] | B | PHACTR3 activity raises TRIM29's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without PHACTR3 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[C6orf132]] | C | C6orf132 activity raises TRIM29's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 4.13× lower at baseline in the lines without C6orf132 | 2e-04 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises TRIM29's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 4.41× lower at baseline in the lines without LAD1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[KRT16]] | C | KRT16 activity raises TRIM29's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 3.93× lower at baseline in the lines without KRT16 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises TRIM29's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 5.94× lower at baseline in the lines without KRT6A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises TRIM29's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 4.19× lower at baseline in the lines without FOXQ1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |
| [[PLEKHG6]] | C | PLEKHG6 activity raises TRIM29's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.93× lower at baseline in the lines without PLEKHG6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent; co-absent with the target |
| [[SCNN1A]] | C | SCNN1A activity raises TRIM29's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 4.03× lower at baseline in the lines without SCNN1A | 0.002 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1; co-absent with the target |

### Downstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 36, C 27. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF3]] | B | TRIM29 activity raises KLF3's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.28× lower at baseline in the lines without TRIM29 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[LINC00592]] | B | TRIM29 activity raises LINC00592's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without TRIM29 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[PLEKHA7]] | B | TRIM29 activity raises PLEKHA7's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.79× lower at baseline in the lines without TRIM29 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[LGALS3]] | B | TRIM29 activity raises LGALS3's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without TRIM29 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[GAREM1]] | B | TRIM29 activity raises GAREM1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.70× lower at baseline in the lines without TRIM29 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[EPS8]] | B | TRIM29 activity raises EPS8's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without TRIM29 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[SH3TC1]] | B | TRIM29 activity raises SH3TC1's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without TRIM29 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | TRIM29 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.17× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[NOD2]] | B | TRIM29 activity raises NOD2's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without TRIM29 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[RHOU]] | B | TRIM29 activity raises RHOU's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without TRIM29 | 0.031 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | TRIM29 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.19× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| cells under [[Afatinib (drug)]] 0.05 µM | B | TRIM29 activity lowers the cells' numbers under Afatinib 0.05 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.14× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 13.8); signed map (50.0, 11.4). **Vector** length 58.1, 16.3% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | +1.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:120,111,286-120,185,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATDC, FLJ36085 |
| Gene groups (HGNC) | Tripartite motif family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14134](https://www.uniprot.org/uniprotkb/Q14134) (Tripartite motif-containing protein 29):

> Plays a crucial role in the regulation of macrophage activation in response to viral or bacterial infections within the respiratory tract. Mechanistically, TRIM29 interacts with IKBKG/NEMO in the lysosome where it induces its 'Lys-48' ubiquitination and subsequent degradation. In turn, the expression of type I interferons and the production of pro-inflammatory cytokines are inhibited. Additionally, induces the 'Lys-48' ubiquitination of STING1 in a similar way, leading to its degradation.

**Summary**, from NCBI Gene [23650](https://www.ncbi.nlm.nih.gov/gene/23650):

> The protein encoded by this gene belongs to the TRIM protein family. It has multiple zinc finger motifs and a leucine zipper motif. It has been proposed to form homo- or heterodimers which are involved in nucleic acid binding. Thus, it may act as a transcriptional regulatory factor involved in carcinogenesis and/or differentiation. It may also function in the suppression of radiosensitivity since it is associated with ataxia telangiectasia phenotype. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17274) · Entrez [23650](https://www.ncbi.nlm.nih.gov/gene/23650) · UniProt [Q14134](https://www.uniprot.org/uniprotkb/Q14134) · Ensembl [ENSG00000137699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137699)

## Data

Gene col 6050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6050); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6050]; `tensor/DDL_lfc|DDL_z.npy` [6050]; `embed/gene_vectors.npy` [6050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6050 or target_col == 6050). Every well: [[TRIM29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
