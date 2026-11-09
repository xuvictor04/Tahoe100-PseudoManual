---
symbol: "LCN2"
type: "gene"
col: 7272
ensembl_id: "ENSG00000148346"
name: "lipocalin 2"
location: "9q34.11"
module: 8
arm: "+"
pooled_cpm: 45.82
n_lines_expressing: 17
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 52
direction_downstream: 74
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# LCN2

*lipocalin 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.96× (z +10.2, q 1e-21, up in 10 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.05× (z +6.5, q 2e-08, up in 13 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HepG2/C3A 0.104×, KATO III 0.195×, COLO 205 0.199×, NCI-H2347 0.199×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.101×, KATO III 0.190×); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.237×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZK1IP1]] (+0.67, fdr 7e-06), [[WFDC2]] (+0.64, fdr 2e-05), [[SLPI]] (+0.61, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[CFB]] → it (grade B ⚠); 74 go from it, the strongest it → [[PRRG4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.96×** | +10.2 | 1e-21 | 10/16 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.30×** | +8.9 | 1e-16 | 7/11 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +6.5 | 2e-08 | 13/15 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +6.2 | 8e-08 | 6/13 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.8 | 6e-07 | 8/16 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +3.9 | 0.009 | 11/15 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.023 | 7/15 (LoVo, KATO III, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.053 | 10/16 (HT-29, Panc 03.27, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HepG2/C3A 0.104×, KATO III 0.195×, COLO 205 0.199×, NCI-H2347 0.199×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (COLO 205 0.101×, KATO III 0.190×); [[Tofacitinib (drug)]] 5 µM in 1 line (COLO 205 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | 0.683× | -3.5 | 0.12 | 4/15 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.583× | -3.5 | 0.12 | 2/15 (LS 180, KATO III) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.688× | -3.4 | 0.12 | 13/15 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.380× | -3.2 | 0.17 | 9/16 (HepG2/C3A, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 1,020 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 153 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -16.9) |
| [[HT-29 (line)]] | alt | 128 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.91× (z +13.6) | — |
| [[KATO III (line)]] | alt | 364 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 357 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 97.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.09× (z +9.9) | — |
| [[A-172 (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZK1IP1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 | STRING 677 |
| [[WFDC2]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SLPI]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 | STRING 896 |
| [[HLA-DRB1]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[LRG1]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 | STRING 414 |
| [[HLA-DRA]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[FGB]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CASP4]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CD74]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SECTM1]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[RNF183]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SAT1]] | +0.55 | +0.37 / +0.55 | both halves | 7e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 4, C 48. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFB]] | B | CFB activity raises LCN2's level | lines that do not express CFB (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without CFB | 0.021 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[PRRG4]] | B | PRRG4 activity raises LCN2's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 3.50× lower at baseline in the lines without PRRG4 | 0.044 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises LCN2's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.02× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.054 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[LGALS9]] | B | LGALS9 activity raises LCN2's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 3.41× lower at baseline in the lines without LGALS9 | 0.079 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[SLC44A4]] | C | SLC44A4 activity raises LCN2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 12.40× lower at baseline in the lines without SLC44A4 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises LCN2's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 7.00× lower at baseline in the lines without MMP7 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises LCN2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 9.72× lower at baseline in the lines without WFDC2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[CYP4F3]] | C | CYP4F3 activity raises LCN2's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 6.37× lower at baseline in the lines without CYP4F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises LCN2's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 11.38× lower at baseline in the lines without KRT23 | 0.001 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises LCN2's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 6.75× lower at baseline in the lines without EPCAM | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises LCN2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 4.99× lower at baseline in the lines without ALOX5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |
| [[FGB]] | C | FGB activity raises LCN2's level | lines that do not express FGB (42) vs lines expressing it (8) | 6.73× lower at baseline in the lines without FGB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |

### Downstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 23, C 51. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG4]] | B | LCN2 activity raises PRRG4's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 4.75× lower at baseline in the lines without LCN2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CARD14]] | B | LCN2 activity raises CARD14's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without LCN2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[ETV7]] | B | LCN2 activity raises ETV7's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.84× lower at baseline in the lines without LCN2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[LGALS9]] | B | LCN2 activity raises LGALS9's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without LCN2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SECTM1]] | B | LCN2 activity raises SECTM1's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 1.99× lower at baseline in the lines without LCN2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | LCN2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express LCN2 (33) vs lines expressing it (15) | the lines without LCN2: 0.74× the cells of the other lines | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CFB]] | B | LCN2 activity raises CFB's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.68× lower at baseline in the lines without LCN2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[IFI27]] | B | LCN2 activity raises IFI27's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without LCN2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | LCN2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express LCN2 (33) vs lines expressing it (15) | the lines without LCN2: 1.18× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| cells under [[Trifluridine (drug)]] 5 µM | B | LCN2 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express LCN2 (33) vs lines expressing it (15) | the lines without LCN2: 0.88× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CCDC69]] | B | LCN2 activity raises CCDC69's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without LCN2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CASP10]] | B | LCN2 activity raises CASP10's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.97× lower at baseline in the lines without LCN2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.7, 54.9); signed map (61.3, -2.4). **Vector** length 50.8, 17.3% of its response variance represented; |z| ≥ 3 in 328 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | lipocalin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,149,071-128,153,453 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NGAL, 24p3 |
| Gene groups (HGNC) | Lipocalins |
| Reactome | 9 pathways, smallest: Metal sequestration by antimicrobial proteins; Antimicrobial peptides; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P80188](https://www.uniprot.org/uniprotkb/P80188) (Neutrophil gelatinase-associated lipocalin):

> Iron-trafficking protein involved in multiple processes such as apoptosis, innate immunity and renal development. Binds iron through association with 2,3-dihydroxybenzoic acid (2,3-DHBA), a siderophore that shares structural similarities with bacterial enterobactin, and delivers or removes iron from the cell, depending on the context. Iron-bound form (holo-24p3) is internalized following binding to the SLC22A17 (24p3R) receptor, leading to release of iron and subsequent increase of …

**Summary**, from NCBI Gene [3934](https://www.ncbi.nlm.nih.gov/gene/3934):

> This gene encodes a protein that belongs to the lipocalin family. Members of this family transport small hydrophobic molecules such as lipids, steroid hormones and retinoids. The protein encoded by this gene is a neutrophil gelatinase-associated lipocalin and plays a role in innate immunity by limiting bacterial growth as a result of sequestering iron-containing siderophores. The presence of this protein in blood and urine is an early biomarker of acute kidney injury. This protein is thought to …

**Accessions** — [HGNC:6526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6526) · Entrez [3934](https://www.ncbi.nlm.nih.gov/gene/3934) · UniProt [P80188](https://www.uniprot.org/uniprotkb/P80188) · Ensembl [ENSG00000148346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148346)

## Data

Gene col 7272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7272); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7272]; `tensor/DDL_lfc|DDL_z.npy` [7272]; `embed/gene_vectors.npy` [7272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7272 or target_col == 7272). Every well: [[LCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
