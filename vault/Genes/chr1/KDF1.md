---
symbol: "KDF1"
type: "gene"
col: 10640
ensembl_id: "ENSG00000175707"
name: "keratinocyte differentiation factor 1"
location: "1p36.11"
module: 119
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 20
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 26
direction_downstream: 51
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# KDF1

*keratinocyte differentiation factor 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.23× (z +11.0, q 2e-25, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +5.6, q 3e-06, up in 0 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.110×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HCT15 0.0463×); [[Entecavir (monohydrate) (drug)]] 0.05 µM in 1 line (HCT15 0.0531×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL44]] (+0.59, fdr 6e-05), [[SYK]] (+0.57, fdr 5e-05), [[PHAX]] (+0.55, fdr 6e-05); moves opposite to [[SLC6A6]] (-0.54, fdr 2e-05), [[GALNT1]] (-0.47, fdr 5e-04), [[LRP11]] (-0.46, fdr 7e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[SLC44A3]] → it (grade B ⚠); 51 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10640.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.23×** | +11.0 | 2e-25 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.89×** | +9.1 | 3e-17 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.51×** | +6.5 | 2e-08 | 2/11 (KATO III, HEC-1-A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.6 | 3e-06 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +5.3 | 1e-05 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.1 | 3e-05 | 6/13 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +5.0 | 6e-05 | 3/18 (Panc 03.27, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +4.9 | 6e-05 | 2/15 (HCT15, SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 0/17 | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.21×** | +4.1 | 0.003 | 3/13 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.9 | 0.006 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.028 | 0/18 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.3 | 0.044 | 1/16 (CFPAC-1) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.2 | 0.047 | 2/16 (LoVo, SW1417) | top dose only |  |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.2 | 0.051 | 0/17 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.053 | 2/15 (BT-474, CFPAC-1) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.110×); [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HCT15 0.0463×); [[Entecavir (monohydrate) (drug)]] 0.05 µM in 1 line (HCT15 0.0531×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10640. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.76 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -10.5) |
| [[HCT15 (line)]] | alt | 8.59 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.0463× (z -10.3) |
| [[KATO III (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 7.28 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0487× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.222 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10640), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL44]] | +0.59 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[SYK]] | +0.57 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[PHAX]] | +0.55 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[ILDR1]] | +0.54 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[TMC4]] | +0.54 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[RORC]] | +0.54 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[KCNE3]] | +0.54 | +0.58 / +0.30 | both halves | 2e-04 |  |
| [[HPS6]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[C11orf52]] | +0.54 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[KCTD14]] | +0.53 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[ZNF576]] | +0.53 | +0.28 / +0.64 | both halves | 3e-04 |  |
| [[INAVA]] | +0.53 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A6]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[GALNT1]] | -0.47 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[LRP11]] | -0.46 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[SERPINB9]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[COL4A2]] | -0.45 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 2, C 24. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SLC44A3 activity raises KDF1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without SLC44A3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[FBLIM1]] | B | FBLIM1 activity raises KDF1's level | lines that do not express FBLIM1 (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without FBLIM1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FAM83G, KITLG, DSG2 |
| [[TMEM125]] | C | TMEM125 activity raises KDF1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.27× lower at baseline in the lines without TMEM125 | 3e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises KDF1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.63× lower at baseline in the lines without INAVA | 4e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[MACC1]] | C | MACC1 activity raises KDF1's level | lines that do not express MACC1 (32) vs lines expressing it (18) | 4.75× lower at baseline in the lines without MACC1 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ENSG00000243004, GRHL2; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises KDF1's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 3.92× lower at baseline in the lines without CLDN3 | 9e-05 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises KDF1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.76× lower at baseline in the lines without FAM83B | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises KDF1's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 3.97× lower at baseline in the lines without SPINT1-AS1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |
| [[TMC4]] | C | TMC4 activity raises KDF1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.35× lower at baseline in the lines without TMC4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent; co-absent with the target |
| [[ILDR1]] | C | ILDR1 activity raises KDF1's level | lines that do not express ILDR1 (31) vs lines expressing it (19) | 3.99× lower at baseline in the lines without ILDR1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TMEM125, ESRP1, SLC5A1; co-absent with the target |
| [[HSH2D]] | C | HSH2D activity raises KDF1's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 3.44× lower at baseline in the lines without HSH2D | 4e-04 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent; co-absent with the target |
| [[RNF43]] | C | RNF43 activity raises KDF1's level | lines that do not express RNF43 (26) vs lines expressing it (24) | 3.21× lower at baseline in the lines without RNF43 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1; co-absent with the target |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 26, C 25. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | KDF1 activity raises SLC44A3's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 3.79× lower at baseline in the lines without KDF1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[MMAA]] | B | KDF1 activity raises MMAA's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.53× lower at baseline in the lines without KDF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[TST]] | B | KDF1 activity raises TST's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without KDF1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[DPH1]] | B | KDF1 activity lowers DPH1's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.22× higher at baseline in the lines without KDF1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | KDF1 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | KDF1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.18× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[ATM]] | B | KDF1 activity lowers ATM's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.49× higher at baseline in the lines without KDF1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | KDF1 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.24× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[TIMM22]] | B | KDF1 activity lowers TIMM22's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.15× higher at baseline in the lines without KDF1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | KDF1 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 0.84× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | KDF1 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| cells under [[Omeprazole (drug)]] 5 µM | B | KDF1 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.15× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 48.3); signed map (57.0, 11.2). **Vector** length 30.6, 5.78% of its response variance represented; |z| ≥ 3 in 327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.3 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.8 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -0.8 | +2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -1.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.6 | -2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | keratinocyte differentiation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,949,562-26,960,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34633, RP11-344H11.3; previously C1orf172 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAX2](https://www.uniprot.org/uniprotkb/Q8NAX2) (Keratinocyte differentiation factor 1):

> Plays a role in the regulation of the epidermis formation during early development. Required both as an inhibitor of basal cell proliferation and a promoter of differentiation of basal progenitor cell progeny (By similarity).

**Summary**, from NCBI Gene [126695](https://www.ncbi.nlm.nih.gov/gene/126695):

> Predicted to be involved in several processes, including positive regulation of epidermal cell differentiation; regulation of epidermal cell division; and skin epidermis development. Predicted to act upstream of or within several processes, including keratinocyte development; negative regulation of keratinocyte proliferation; and protein stabilization. Predicted to be located in cytoplasm. Predicted to be active in cell junction. Implicated in ectodermal dysplasia 12. [provided by Alliance of …

**Accessions** — [HGNC:26624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26624) · Entrez [126695](https://www.ncbi.nlm.nih.gov/gene/126695) · UniProt [Q8NAX2](https://www.uniprot.org/uniprotkb/Q8NAX2) · Ensembl [ENSG00000175707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175707)

## Data

Gene col 10640: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10640); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10640, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10640]; `tensor/DDL_lfc|DDL_z.npy` [10640]; `embed/gene_vectors.npy` [10640]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10640 or target_col == 10640). Every well: [[KDF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
