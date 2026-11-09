---
symbol: "LHX2"
type: "gene"
col: 2796
ensembl_id: "ENSG00000106689"
name: "LIM homeobox 2"
location: "9q33.3"
module: 115
arm: "+"
pooled_cpm: 3.4
n_lines_expressing: 24
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# LHX2

*LIM homeobox 2* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +13.9, q 5e-41, up in 7 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.103×, NCI-H23 0.259×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0773×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00937]] (+0.66, fdr 1e-05), [[SBK1]] (+0.63, fdr 4e-05), [[SLC16A10]] (+0.60, fdr 1e-04); moves opposite to [[COPB2-DT]] (-0.55, fdr 3e-05), [[SDCBP2-AS1]] (-0.55, fdr 4e-05), [[HDHD2]] (-0.51, fdr 8e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 13 go from it, the strongest it → [[KIF26A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +13.9 | 5e-41 | 7/16 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.42×** | +10.5 | 3e-23 | 15/21 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.12×** | +9.2 | 1e-17 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.75×** | +8.1 | 5e-14 | 10/15 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +5.3 | 1e-05 | 9/18 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.74×** | +4.6 | 3e-04 | 9/21 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.5 | 6e-04 | 3/15 (NCI-H460, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.70×** | +4.4 | 7e-04 | 10/20 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.75×** | +4.3 | 0.001 | 0/7 | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 4/21 (C32, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.27×** | +3.7 | 0.012 | 1/12 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.50×** | +3.4 | 0.030 | 0/13 | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.4 | 0.030 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.50×** | +3.3 | 0.044 | 3/17 (NCI-H23, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.064 | 5/21 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2796.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.103×, NCI-H23 0.259×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0773×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.688× | -3.2 | 0.64 | 9/17 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.7) | — |
| [[A549 (line)]] | wt | 4.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 3.67 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0773× (z -9.4) |
| [[LoVo (line)]] | wt | 4.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -14.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 9.13 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.860 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.622 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00937]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SBK1]] | +0.63 | +0.41 / +0.73 | both halves | 4e-05 |  |
| [[SLC16A10]] | +0.60 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[ARHGAP44]] | +0.60 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[ELAVL2]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[TEX15]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PARD6G]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SEMA6B]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PHF21B]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[LMX1B]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 | same gene group |
| [[ADCY1]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GNAO1]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPB2-DT]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SDCBP2-AS1]] | -0.55 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[HDHD2]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[USP40]] | -0.51 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[ACYP2]] | -0.51 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ENTPD3-AS1]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CLHC1]] | -0.50 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[ZNF655]] | -0.50 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[ZSCAN30]] | -0.49 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[NEK11]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[NEK9]] | -0.48 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.47 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises LHX2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without SEMA6B | 0.019 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises LHX2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.31× lower at baseline in the lines without E2F2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CRACD]] | B | CRACD activity raises LHX2's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.47× lower at baseline in the lines without CRACD | 0.059 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[TSPAN33]] | B | TSPAN33 activity raises LHX2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.44× lower at baseline in the lines without TSPAN33 | 0.064 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises LHX2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.59× lower at baseline in the lines without SEPTIN3 | 0.070 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[KIF26A]] | B | KIF26A activity raises LHX2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.27× lower at baseline in the lines without KIF26A | 0.075 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SLC16A10]] | B | SLC16A10 activity raises LHX2's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without SLC16A10 | 0.091 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[MED12L]] | C | MED12L activity raises LHX2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without MED12L | 0.021 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[KCNG3]] | C | KCNG3 activity raises LHX2's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 3.07× lower at baseline in the lines without KCNG3 | 0.029 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |
| [[RET]] | C | RET activity raises LHX2's level | lines that do not express RET (28) vs lines expressing it (22) | 2.91× lower at baseline in the lines without RET | 0.039 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[ADCY1]] | C | ADCY1 activity raises LHX2's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without ADCY1 | 0.043 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | LHX2 activity raises KIF26A's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without LHX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[ACYP2]] | B | LHX2 activity raises ACYP2's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without LHX2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[RASGEF1C]] | B | LHX2 activity raises RASGEF1C's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 2.51× lower at baseline in the lines without LHX2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[SBK1]] | B | LHX2 activity raises SBK1's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 2.21× lower at baseline in the lines without LHX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[SEMA6B]] | B | LHX2 activity raises SEMA6B's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without LHX2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[LINC00937]] | B | LHX2 activity raises LINC00937's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without LHX2 | 0.047 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[MAPT]] | B | LHX2 activity raises MAPT's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without LHX2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[TSPAN33]] | B | LHX2 activity raises TSPAN33's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without LHX2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[PARD6G]] | B | LHX2 activity raises PARD6G's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without LHX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[RHBDL3]] | B | LHX2 activity raises RHBDL3's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without LHX2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[E2F2]] | B | LHX2 activity raises E2F2's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without LHX2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[MED12L]] | C | LHX2 activity raises MED12L's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 3.91× lower at baseline in the lines without LHX2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.0, 37.5); signed map (29.1, 26.7). **Vector** length 37.6, 7.44% of its response variance represented; |z| ≥ 3 in 434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +13.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | LIM homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,001,670-124,033,301 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LH-2, hLhx2 |
| Gene groups (HGNC) | LIM class homeoboxes |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 7 pathways, smallest: Expression and translocation of olfactory receptors; Olfactory Signaling Pathway; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [P50458](https://www.uniprot.org/uniprotkb/P50458) (LIM/homeobox protein Lhx2):

> Acts as a transcriptional activator. Stimulates the promoter of the alpha-glycoprotein gene. Transcriptional regulatory protein involved in the control of cell differentiation in developing lymphoid and neural cell types (By similarity).

**Summary**, from NCBI Gene [9355](https://www.ncbi.nlm.nih.gov/gene/9355):

> This gene encodes a protein belonging to a large protein family, members of which carry the LIM domain, a unique cysteine-rich zinc-binding domain. The encoded protein may function as a transcriptional regulator. The protein can recapitulate or rescue phenotypes in Drosophila caused by a related protein, suggesting conservation of function during evolution. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6594) · Entrez [9355](https://www.ncbi.nlm.nih.gov/gene/9355) · UniProt [P50458](https://www.uniprot.org/uniprotkb/P50458) · Ensembl [ENSG00000106689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106689)

## Data

Gene col 2796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2796); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2796]; `tensor/DDL_lfc|DDL_z.npy` [2796]; `embed/gene_vectors.npy` [2796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2796 or target_col == 2796). Every well: [[LHX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
