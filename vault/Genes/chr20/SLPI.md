---
symbol: "SLPI"
type: "gene"
col: 4480
ensembl_id: "ENSG00000124107"
name: "secretory leukocyte peptidase inhibitor"
location: "20q13.12"
module: 139
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 25
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 25
direction_downstream: 21
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SLPI

*secretory leukocyte peptidase inhibitor* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.43× (z +9.3, q 1e-17, up in 22 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -6.9, q 3e-09, down in 21 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (KATO III 0.0934×, CFPAC-1 0.122×, BT-474 0.0356×, NCI-H1573 0.153×, …); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 0.162×; ⚠ cell-cycle shift, explains ~85% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HT-29 0.0684×; ⚠ toxic; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA4]] (+0.72, fdr 7e-06), [[SAA1]] (+0.71, fdr 7e-06), [[S100P]] (+0.71, fdr 7e-06); moves opposite to [[WNT7A]] (-0.43, fdr 1e-04).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); 21 go from it, the strongest it → [[SQOR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4480.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.43×** | +9.3 | 1e-17 | 22/23 (Panc 03.27, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.66×** | +6.9 | 1e-09 | 13/23 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +6.3 | 5e-08 | 6/15 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **3.03×** | +5.9 | 5e-07 | 14/23 (A498, H4, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +5.7 | 1e-06 | 14/24 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.72×** | +5.1 | 3e-05 | 13/21 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +5.1 | 3e-05 | 17/24 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **2.50×** | +4.9 | 8e-05 | 12/23 (A498, H4, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.84×** | +4.6 | 3e-04 | 11/23 (A498, H4, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.32×** | +4.5 | 4e-04 | 11/23 (A498, H4, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.30×** | +4.4 | 4e-04 | 12/23 (A498, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.30×** | +4.4 | 4e-04 | 13/23 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.35×** | +4.4 | 6e-04 | 15/24 (A498, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.22×** | +4.2 | 9e-04 | 11/23 (A498, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.08×** | +3.9 | 0.004 | 12/23 (A498, H4, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.02×** | +3.5 | 0.018 | 9/21 (A498, H4, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +3.4 | 0.024 | 9/23 (A498, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4480.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (KATO III 0.0934×, CFPAC-1 0.122×, BT-474 0.0356×, NCI-H1573 0.153×, …); [[Selinexor (drug)]] 5 µM in 1 line (AsPC-1 0.162×; ⚠ cell-cycle shift, explains ~85% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HT-29 0.0684×; ⚠ toxic; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.400×** | -6.9 | 3e-09 | 21/23 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.406×** | -4.8 | 4e-04 | 18/23 (H4, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.459×** | -4.2 | 0.006 | 15/23 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.551× | -3.2 | 0.20 | 14/23 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.556× | -3.1 | 0.20 | 13/22 (BT-474, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.5 | 7 | 1 | [[Betamethasone dipropionate (drug)]] 0.5 µM 14.9× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -8.5) |
| [[HT-29 (line)]] | alt | 10.8 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.36× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +8.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0356× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -12.9) |
| [[H4 (line)]] | wt | 23.2 | 1 | 0 | [[Betamethasone dipropionate (drug)]] 0.5 µM 20.6× (z +9.3) | — |
| [[J82 (line)]] | alt | 8.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.92× (z +8.8) | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0934× (z -13.3) |
| [[LS 180 (line)]] | wt | 10.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.19× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 20.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.04× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.808 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA4]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[S100P]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 | STRING 416 |
| [[SAA2]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PI3]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 | same gene group; STRING 700 |
| [[SAA2-SAA4]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[FGB]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 | STRING 489 |
| [[SERPINA1]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 | STRING 621 |
| [[AQP3]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 | **novel candidate** |
| [[BCL6]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[LCN2]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 | STRING 896 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT7A]] | -0.43 | -0.33 / -0.41 | both halves | 1e-04 | pathway: HALLMARK_KRAS_SIGNALING_UP |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises SLPI's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without CCL20 | 0.008 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[NR3C1]] | B | NR3C1 activity raises SLPI's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[MT1F]] | B | MT1F activity raises SLPI's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without MT1F | 0.033 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[IGFBP4]] | B | IGFBP4 activity raises SLPI's level | lines that do not express IGFBP4 (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without IGFBP4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SDR16C5, TNFRSF1B, TSPAN15 |
| [[TSC22D3]] | B | TSC22D3 activity raises SLPI's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without TSC22D3 | 0.088 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[PI3]] | C | PI3 activity raises SLPI's level | lines that do not express PI3 (27) vs lines expressing it (23) | 4.58× lower at baseline in the lines without PI3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A; co-absent with the target |
| [[S100P]] | C | S100P activity raises SLPI's level | lines that do not express S100P (34) vs lines expressing it (16) | 4.57× lower at baseline in the lines without S100P | 0.003 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; co-absent with the target |
| [[PRSS8]] | C | PRSS8 activity raises SLPI's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.52× lower at baseline in the lines without PRSS8 | 0.006 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises SLPI's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.90× lower at baseline in the lines without LCN2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[AQP3]] | C | AQP3 activity raises SLPI's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 4.72× lower at baseline in the lines without AQP3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent; co-absent with the target |
| [[FAM83A]] | C | FAM83A activity raises SLPI's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 4.81× lower at baseline in the lines without FAM83A | 0.008 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises SLPI's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.63× lower at baseline in the lines without FXYD3 | 0.012 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 10, C 11. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SQOR]] | B | SLPI activity raises SQOR's level | lines that do not express SLPI (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without SLPI | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[CCL20]] | B | SLPI activity raises CCL20's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without SLPI | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[NCOA3]] | B | SLPI activity raises NCOA3's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without SLPI | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[B4GALT1]] | B | SLPI activity raises B4GALT1's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without SLPI | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[ADGRG2]] | B | SLPI activity raises ADGRG2's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without SLPI | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[MT1F]] | B | SLPI activity raises MT1F's level | lines that do not express SLPI (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without SLPI | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[IGFBP4]] | B | SLPI activity raises IGFBP4's level | lines that do not express SLPI (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without SLPI | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | SLPI activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express SLPI (25) vs lines expressing it (23) | the lines without SLPI: 0.75× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| cells under [[Methylprednisolone succinate (drug)]] 5 µM | B | SLPI activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express SLPI (25) vs lines expressing it (23) | the lines without SLPI: 1.22× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | SLPI activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express SLPI (25) vs lines expressing it (23) | the lines without SLPI: 0.82× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[PI3]] | C | SLPI activity raises PI3's level | lines that do not express SLPI (25) vs lines expressing it (25) | 3.13× lower at baseline in the lines without SLPI | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2; co-absent with the target |
| [[S100P]] | C | SLPI activity raises S100P's level | lines that do not express SLPI (25) vs lines expressing it (25) | 5.41× lower at baseline in the lines without SLPI | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2; co-absent with the target |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, 49.2); signed map (55.5, 24.4). **Vector** length 78.9, 28.0% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.8 | +4.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | secretory leukocyte peptidase inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,252,239-45,254,564 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUSI-I, ALK1, ALP, BLPI, HUSI, WAP4, WFDC4 |
| Gene groups (HGNC) | WAP four-disulfide core domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P03973](https://www.uniprot.org/uniprotkb/P03973) (Antileukoproteinase):

> Acid-stable proteinase inhibitor with strong affinities for trypsin, chymotrypsin, elastase, and cathepsin G. Modulates the inflammatory and immune responses after bacterial infection, and after infection by the intracellular parasite L.major. Down-regulates responses to bacterial lipopolysaccharide (LPS) (By similarity). Plays a role in regulating the activation of NF-kappa-B and inflammatory responses. Has antimicrobial activity against mycobacteria, but not against salmonella. Contributes to …

**Summary**, from NCBI Gene [6590](https://www.ncbi.nlm.nih.gov/gene/6590):

> This gene encodes a secreted inhibitor which protects epithelial tissues from serine proteases. It is found in various secretions including seminal plasma, cervical mucus, and bronchial secretions, and has affinity for trypsin, leukocyte elastase, and cathepsin G. Its inhibitory effect contributes to the immune response by protecting epithelial surfaces from attack by endogenous proteolytic enzymes. This antimicrobial protein has antibacterial, antifungal and antiviral activity. [provided by …

**Accessions** — [HGNC:11092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11092) · Entrez [6590](https://www.ncbi.nlm.nih.gov/gene/6590) · UniProt [P03973](https://www.uniprot.org/uniprotkb/P03973) · Ensembl [ENSG00000124107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124107)

## Data

Gene col 4480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4480); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4480]; `tensor/DDL_lfc|DDL_z.npy` [4480]; `embed/gene_vectors.npy` [4480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4480 or target_col == 4480). Every well: [[SLPI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLPI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
