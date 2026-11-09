---
symbol: "PIWIL1"
type: "gene"
col: 4594
ensembl_id: "ENSG00000125207"
name: "piwi like RNA-mediated gene silencing 1"
location: "12q24.33"
module: 55
arm: "+"
pooled_cpm: 6.44
n_lines_expressing: 12
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 28
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# PIWIL1

*piwi like RNA-mediated gene silencing 1* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.71× (z +11.5, q 5e-28, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.01× (z +7.6, q 3e-12, up in 7 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.463× (z -5.5, q 2e-05, down in 5 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO1]] (+0.74, fdr 7e-06), [[LCK]] (+0.72, fdr 7e-06), [[EDAR]] (+0.65, fdr 1e-05); moves opposite to [[HOXA9]] (-0.49, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 28 go from it, the strongest it → [[CACNA1E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4594.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.71×** | +11.5 | 5e-28 | 3/5 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.48×** | +10.7 | 2e-24 | 3/5 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +8.9 | 1e-16 | 4/7 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +7.6 | 3e-12 | 7/9 (SW480, SW1417, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +4.8 | 1e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +4.6 | 3e-04 | 5/8 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +3.8 | 0.013 | 0/4 | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.97×** | +3.7 | 0.013 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.015 | 0/8 | top dose only | cell-cycle shift (explains ~3% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.93×** | +3.6 | 0.016 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.042 | 1/8 (COLO 205) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.83×** | +3.3 | 0.042 | 1/8 (SW480) | inconsistent across doses | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +3.2 | 0.064 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.1 | 0.080 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.463×** | -5.5 | 2e-05 | 5/9 (SW480, SNU-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.521×** | -5.1 | 1e-04 | 5/8 (SNU-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.533×** | -4.5 | 0.001 | 7/10 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.655×** | -4.0 | 0.009 | 6/9 (SW480, SNU-1, …) | two highest doses | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.602×** | -3.7 | 0.029 | 1/9 (LoVo) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.615×** | -3.5 | 0.038 | 0/9 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.628×** | -3.5 | 0.038 | 5/9 (SNU-1, SW480, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.427×** | -3.5 | 0.038 | 4/9 (COLO 205, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.644×** | -3.4 | 0.038 | 1/10 (Hs 766T) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.664×** | -3.2 | 0.080 | 5/9 (SNU-1, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.669×** | -3.1 | 0.088 | 4/9 (SNU-1, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -3.1 | 0.098 | 5/9 (SNU-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.660× | -3.0 | 0.12 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 253 | 0 | 18 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -17.7) |
| [[KATO III (line)]] | alt | 54.6 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -14.1) |
| [[SW480 (line)]] | alt | 7.54 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.30× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0808× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 77.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.1) |
| [[A-172 (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO1]] | +0.74 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.65 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ONECUT3]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[INPP5D]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.64 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[KCNH8]] | +0.63 | +0.58 / +0.57 | both halves | 8e-06 |  |
| [[SLC5A1]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SKAP1]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CTSE]] | +0.62 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[LINC00589]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA9]] | -0.49 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PIWIL1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TFF2]] | C | TFF2 activity raises PIWIL1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.85× lower at baseline in the lines without TFF2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[CACNA2D4]] | C | CACNA2D4 activity raises PIWIL1's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without CACNA2D4 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises PIWIL1's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without PADI1 | 0.045 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[ANO1]] | C | ANO1 activity raises PIWIL1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.21× lower at baseline in the lines without ANO1 | 0.046 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2; co-absent with the target |
| [[SH3TC2]] | C | SH3TC2 activity raises PIWIL1's level | lines that do not express SH3TC2 (20) vs lines expressing it (30) | 2.21× lower at baseline in the lines without SH3TC2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SH3TC2-DT, TNFSF10, PSORS1C1; maybe low, not absent; co-absent with the target |
| [[BMP10]] | C | BMP10 activity raises PIWIL1's level | lines that do not express BMP10 (47) vs lines expressing it (3) | 9.23× lower at baseline in the lines without BMP10 | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, APOB, TBXT; co-absent with the target; its own permutation p |
| [[GJB1]] | C | GJB1 activity raises PIWIL1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 3.30× lower at baseline in the lines without GJB1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises PIWIL1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 4.52× lower at baseline in the lines without CLRN3 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises PIWIL1's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.36× lower at baseline in the lines without EDAR | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[CALB1]] | C | CALB1 activity raises PIWIL1's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 2.85× lower at baseline in the lines without CALB1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 9, C 19. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1E]] | B | PIWIL1 activity raises CACNA1E's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 1.82× lower at baseline in the lines without PIWIL1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[CEMIP]] | B | PIWIL1 activity raises CEMIP's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 4.71× lower at baseline in the lines without PIWIL1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[ITGA6]] | B | PIWIL1 activity raises ITGA6's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 3.94× lower at baseline in the lines without PIWIL1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[LINC02320]] | B | PIWIL1 activity raises LINC02320's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 3.71× lower at baseline in the lines without PIWIL1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[PLLP]] | B | PIWIL1 activity raises PLLP's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without PIWIL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[SYNE3]] | B | PIWIL1 activity raises SYNE3's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.21× lower at baseline in the lines without PIWIL1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[PLS1]] | B | PIWIL1 activity raises PLS1's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 3.66× lower at baseline in the lines without PIWIL1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[TLDC2]] | B | PIWIL1 activity raises TLDC2's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.26× lower at baseline in the lines without PIWIL1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[PLCD3]] | B | PIWIL1 activity raises PLCD3's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.03× lower at baseline in the lines without PIWIL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[ANO1]] | C | PIWIL1 activity raises ANO1's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 8.16× lower at baseline in the lines without PIWIL1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |
| [[CALB1]] | C | PIWIL1 activity raises CALB1's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 5.30× lower at baseline in the lines without PIWIL1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |
| [[CLRN3]] | C | PIWIL1 activity raises CLRN3's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 3.64× lower at baseline in the lines without PIWIL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, 51.9); signed map (3.6, 38.7). **Vector** length 48.6, 19.6% of its response variance represented; |z| ≥ 3 in 313 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +0.7 | -1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | piwi like RNA-mediated gene silencing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:130,337,887-130,372,637 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIWI, HIWI, CT80.1 |
| Gene groups (HGNC) | Piwi like RNA-mediated gene silencing family |
| Reactome | 2 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96J94](https://www.uniprot.org/uniprotkb/Q96J94) (Piwi-like protein 1):

> Endoribonuclease that plays a central role in postnatal germ cells by repressing transposable elements and preventing their mobilization, which is essential for the germline integrity. Acts via the piRNA metabolic process, which mediates the repression of transposable elements during meiosis by forming complexes composed of piRNAs and Piwi proteins and governs the methylation and subsequent repression of transposons. Directly binds methylated piRNAs, a class of 24 to 30 nucleotide RNAs that are …

**Summary**, from NCBI Gene [9271](https://www.ncbi.nlm.nih.gov/gene/9271):

> This gene encodes a member of the PIWI subfamily of Argonaute proteins, evolutionarily conserved proteins containing both PAZ and Piwi motifs that play important roles in stem cell self-renewal, RNA silencing, and translational regulation in diverse organisms. The encoded protein may play a role as an intrinsic regulator of the self-renewal capacity of germline and hematopoietic stem cells. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:9007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9007) · Entrez [9271](https://www.ncbi.nlm.nih.gov/gene/9271) · UniProt [Q96J94](https://www.uniprot.org/uniprotkb/Q96J94) · Ensembl [ENSG00000125207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125207)

## Data

Gene col 4594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4594); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4594]; `tensor/DDL_lfc|DDL_z.npy` [4594]; `embed/gene_vectors.npy` [4594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4594 or target_col == 4594). Every well: [[PIWIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIWIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
