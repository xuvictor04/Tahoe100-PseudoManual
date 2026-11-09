---
symbol: "MUC4"
type: "gene"
col: 6959
ensembl_id: "ENSG00000145113"
name: "mucin 4, cell surface associated"
location: "3q29"
module: 8
arm: "+"
pooled_cpm: 33.75
n_lines_expressing: 9
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 87
direction_downstream: 98
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# MUC4

*mucin 4, cell surface associated* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.46× (z +13.9, q 6e-41, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +8.8, q 2e-16, up in 2 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.707× (z -4.2, q 0.016, down in 6 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.310×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.313×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC16]] (+0.80, fdr 7e-06), [[MMP7]] (+0.77, fdr 7e-06), [[PDZK1IP1]] (+0.76, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 87 arrows point to it, the strongest [[SLC44A3-AS1]] → it (grade B ⚠); 98 go from it, the strongest it → [[ETV7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.46×** | +13.9 | 6e-41 | 3/6 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +12.0 | 9e-31 | 4/7 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +8.8 | 2e-16 | 1/7 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +8.8 | 2e-16 | 2/7 (AsPC-1, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +8.2 | 4e-14 | 0/7 | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +7.5 | 5e-12 | 2/7 (KATO III, NCI-H2347) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.7 | 2e-04 | 3/7 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +4.3 | 0.001 | 1/7 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.00×** | +3.9 | 0.005 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.017 | 7/7 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.4 | 0.039 | 1/7 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.47×** | +3.3 | 0.052 | 0/7 | top dose only | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.46×** | +3.2 | 0.058 | 5/7 (KATO III, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.065 | 6/7 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.069 | 1/7 (HEC-1-A) | two highest doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.069 | 0/7 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.099 | 7/7 (AsPC-1, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6959.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.310×); [[Homoharringtonine (drug)]] 5 µM in 1 line (Panc 03.27 0.313×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.707×** | -4.2 | 0.016 | 6/7 (CFPAC-1, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 996 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 27.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.98× (z +8.5) | — |
| [[A-172 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 391 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.99 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC16]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 969 |
| [[MMP7]] | +0.77 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PDZK1IP1]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 | STRING 441 |
| [[TRIM31]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ALOX5]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TMC5]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SAMD12-AS1]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RBM47]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC34A2]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[GABRP]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[MYH14]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*87 arrows, 87 of them with an alert ⚠; grade A 0, B 6, C 81. Shown: the 12 strongest; 75 more arrows (75 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises MUC4's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without SLC44A3-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[RHBDL2]] | B | RHBDL2 activity raises MUC4's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without RHBDL2 | 0.072 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MUC4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[BCL2L15]] | B | BCL2L15 activity raises MUC4's level | lines that do not express BCL2L15 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without BCL2L15 | 0.084 | ⚠ within organs, on part of the lines; also absent: SYK, NOS3, CASC8; maybe low, not absent |
| [[SAMD12]] | B | SAMD12 activity raises MUC4's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without SAMD12 | 0.088 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[CFB]] | B | CFB activity raises MUC4's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without CFB | 0.088 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[SLC44A4]] | C | SLC44A4 activity raises MUC4's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.85× lower at baseline in the lines without SLC44A4 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises MUC4's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 5.61× lower at baseline in the lines without ADGRF1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises MUC4's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 4.49× lower at baseline in the lines without GRHL2 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises MUC4's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 5.72× lower at baseline in the lines without WFDC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[CST6]] | C | CST6 activity raises MUC4's level | lines that do not express CST6 (42) vs lines expressing it (8) | 9.31× lower at baseline in the lines without CST6 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises MUC4's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 4.93× lower at baseline in the lines without LCN2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*98 arrows, 98 of them with an alert ⚠; grade A 0, B 25, C 73. Shown: the 12 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETV7]] | B | MUC4 activity raises ETV7's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 2.83× lower at baseline in the lines without MUC4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[OCLN]] | B | MUC4 activity raises OCLN's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 5.76× lower at baseline in the lines without MUC4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[RBM47]] | B | MUC4 activity raises RBM47's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 5.12× lower at baseline in the lines without MUC4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[SLC44A3-AS1]] | B | MUC4 activity raises SLC44A3-AS1's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 3.59× lower at baseline in the lines without MUC4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[BAG1]] | B | MUC4 activity raises BAG1's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 1.85× lower at baseline in the lines without MUC4 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[BCL2L14]] | B | MUC4 activity raises BCL2L14's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 1.44× lower at baseline in the lines without MUC4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[LGALS9]] | B | MUC4 activity raises LGALS9's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 3.48× lower at baseline in the lines without MUC4 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[MUC20]] | B | MUC4 activity raises MUC20's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 3.47× lower at baseline in the lines without MUC4 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[LINC01504]] | B | MUC4 activity raises LINC01504's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 1.99× lower at baseline in the lines without MUC4 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[STS]] | B | MUC4 activity raises STS's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 3.13× lower at baseline in the lines without MUC4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[PLEKHA7]] | B | MUC4 activity raises PLEKHA7's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 2.13× lower at baseline in the lines without MUC4 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | MUC4 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express MUC4 (41) vs lines expressing it (7) | the lines without MUC4: 1.25× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.808). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 55.0); signed map (59.8, 3.0). **Vector** length 40.4, 21.0% of its response variance represented; |z| ≥ 3 in 185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -1.0 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.7 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | mucin 4, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,746,765-195,811,973 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASGP, MUC-4 |
| Gene groups (HGNC) | Mucins |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99102](https://www.uniprot.org/uniprotkb/Q99102) (Mucin-4):

> Membrane-bound mucin, a family of highly glycosylated proteins that constitute the major component of the mucus, the slimy and viscous secretion covering epithelial surfaces. These glycoproteins play important roles in the protection of the epithelium and are implicated in epithelial renewal and differentiation. Regulates cellular behavior through both anti-adhesive effects on cell-cell and cell-extracellular matrix interactions and its ability to act as an intramembrane ligand for ERBB2. Plays …

**Summary**, from NCBI Gene [4585](https://www.ncbi.nlm.nih.gov/gene/4585):

> The major constituents of mucus, the viscous secretion that covers epithelial surfaces such as those in the trachea, colon, and cervix, are highly glycosylated proteins called mucins. These glycoproteins play important roles in the protection of the epithelial cells and have been implicated in epithelial renewal and differentiation. This gene encodes an integral membrane glycoprotein found on the cell surface, although secreted isoforms may exist. At least two dozen transcript variants of this …

**Accessions** — [HGNC:7514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7514) · Entrez [4585](https://www.ncbi.nlm.nih.gov/gene/4585) · UniProt [Q99102](https://www.uniprot.org/uniprotkb/Q99102) · Ensembl [ENSG00000145113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145113)

## Data

Gene col 6959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6959); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6959]; `tensor/DDL_lfc|DDL_z.npy` [6959]; `embed/gene_vectors.npy` [6959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6959 or target_col == 6959). Every well: [[MUC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
