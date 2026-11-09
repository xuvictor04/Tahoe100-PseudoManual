---
symbol: "STEAP4"
type: "gene"
col: 4848
ensembl_id: "ENSG00000127954"
name: "STEAP4 metalloreductase"
location: "7q21.12"
module: 8
arm: "+"
pooled_cpm: 13.43
n_lines_expressing: 12
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 55
direction_downstream: 94
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# STEAP4

*STEAP4 metalloreductase* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.15× (z +11.9, q 7e-30, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.88× (z +10.9, q 5e-25, up in 10 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 4 lines (HT-29 0.0536×, Panc 03.27 0.105×, NCI-H1573 0.0755×, COLO 205 0.0257×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 0.171×, Panc 03.27 0.264×, HT-29 0.251×; ⚠ cell-cycle shift, explains ~3% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 0.0549×, HT-29 0.0837×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (HT-29 0.0648×, Panc 03.27 0.143×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L15]] (+0.74, fdr 7e-06), [[PDZK1IP1]] (+0.70, fdr 7e-06), [[SAMD12-AS1]] (+0.68, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[MTUS1-DT]] → it (grade B ⚠); 94 go from it, the strongest it → [[RASGEF1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.15×** | +11.9 | 7e-30 | 1/9 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.88×** | +10.9 | 5e-25 | 10/10 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +8.6 | 2e-15 | 2/5 (SW1417, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +8.1 | 8e-14 | 4/11 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.69×** | +7.2 | 9e-11 | 10/11 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +5.9 | 5e-07 | 1/7 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.88×** | +4.6 | 4e-04 | 3/10 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.0 | 0.005 | 6/11 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.5 | 0.034 | 1/10 (KATO III) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.043 | 6/10 (CFPAC-1, KATO III, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.068 | 1/9 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.068 | 8/10 (LoVo, CFPAC-1, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.52× | +3.0 | 0.10 | 7/10 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.52× | +3.0 | 0.10 | 3/10 (NCI-H1573, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 4 lines (HT-29 0.0536×, Panc 03.27 0.105×, NCI-H1573 0.0755×, COLO 205 0.0257×); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1573 0.171×, Panc 03.27 0.264×, HT-29 0.251×; ⚠ cell-cycle shift, explains ~3% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (Panc 03.27 0.0549×, HT-29 0.0837×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (HT-29 0.0648×, Panc 03.27 0.143×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.598× | -3.5 | 0.29 | 0/10 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.655× | -3.1 | 0.55 | 1/10 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 111 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.35× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.0549× (z -15.5) |
| [[HT-29 (line)]] | alt | 81.2 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0536× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0359× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0755× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 21.2 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.89× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 6.93 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0257× (z -9.2) |
| [[KATO III (line)]] | alt | 3.47 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.58× (z +8.5) | — |
| [[LoVo (line)]] | wt | 6.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 203 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.96× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 7.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.30× (z +9.5) | — |
| [[A-172 (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.962 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.915 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L15]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PDZK1IP1]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[SAMD12-AS1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[C4orf19]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[MMP7]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SLC34A2]] | +0.65 | +0.41 / +0.68 | both halves | 4e-05 | **novel candidate** |
| [[SCIN]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.62 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[LRG1]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 3, C 52. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1-DT]] | B | MTUS1-DT activity raises STEAP4's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.54× lower at baseline in the lines without MTUS1-DT | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[TOP2A]] | B | TOP2A activity lowers STEAP4's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MTUS1]] | B | MTUS1 activity raises STEAP4's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.53× lower at baseline in the lines without MTUS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[GRHL2]] | C | GRHL2 activity raises STEAP4's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 5.88× lower at baseline in the lines without GRHL2 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises STEAP4's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.56× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises STEAP4's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 6.95× lower at baseline in the lines without WFDC2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[SIDT1]] | C | SIDT1 activity raises STEAP4's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 4.31× lower at baseline in the lines without SIDT1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises STEAP4's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.51× lower at baseline in the lines without ITGB6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |
| [[SLC28A3]] | C | SLC28A3 activity raises STEAP4's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 3.41× lower at baseline in the lines without SLC28A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14; co-absent with the target |
| [[MUC16]] | C | MUC16 activity raises STEAP4's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 7.47× lower at baseline in the lines without MUC16 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |
| [[GABRP]] | C | GABRP activity raises STEAP4's level | lines that do not express GABRP (44) vs lines expressing it (6) | 11.91× lower at baseline in the lines without GABRP | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[LRRN1]] | C | LRRN1 activity raises STEAP4's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 4.02× lower at baseline in the lines without LRRN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*94 arrows, 94 of them with an alert ⚠; grade A 0, B 27, C 67. Shown: the 12 strongest; 82 more arrows (82 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1B]] | B | STEAP4 activity raises RASGEF1B's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 4.55× lower at baseline in the lines without STEAP4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[MUC20]] | B | STEAP4 activity raises MUC20's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 4.50× lower at baseline in the lines without STEAP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[CARD14]] | B | STEAP4 activity raises CARD14's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.24× lower at baseline in the lines without STEAP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[LGALS9]] | B | STEAP4 activity raises LGALS9's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.58× lower at baseline in the lines without STEAP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[ELF3-AS1]] | B | STEAP4 activity raises ELF3-AS1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.60× lower at baseline in the lines without STEAP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[C4orf19]] | B | STEAP4 activity raises C4orf19's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.23× lower at baseline in the lines without STEAP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[ETV7]] | B | STEAP4 activity raises ETV7's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.56× lower at baseline in the lines without STEAP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[BCL2L15]] | B | STEAP4 activity raises BCL2L15's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.25× lower at baseline in the lines without STEAP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[STS]] | B | STEAP4 activity raises STS's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.91× lower at baseline in the lines without STEAP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[CFB]] | B | STEAP4 activity raises CFB's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.94× lower at baseline in the lines without STEAP4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[PCAT1]] | B | STEAP4 activity raises PCAT1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.62× lower at baseline in the lines without STEAP4 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[APOL1]] | B | STEAP4 activity raises APOL1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.45× lower at baseline in the lines without STEAP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 54.2); signed map (59.5, 1.9). **Vector** length 54.6, 21.4% of its response variance represented; |z| ≥ 3 in 398 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +11.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | STEAP4 metalloreductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:88,270,892-88,306,894 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23153, TIARP, STAMP2, SchLAH; previously TNFAIP9 |
| Gene groups (HGNC) | STEAP family; Flavoproteins |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 3 pathways, smallest: Transferrin endocytosis and recycling; Iron uptake and transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q687X5](https://www.uniprot.org/uniprotkb/Q687X5) (Metalloreductase STEAP4):

> Integral membrane protein that functions as a NADPH-dependent ferric-chelate reductase, using NADPH from one side of the membrane to reduce a Fe(3+) chelate that is bound on the other side of the membrane. Mediates sequential transmembrane electron transfer from NADPH to FAD and onto heme, and finally to the Fe(3+) chelate. Can also reduce Cu(2+) to Cu(1+) (By similarity). Plays a role in systemic metabolic homeostasis, integrating inflammatory and metabolic responses (By similarity). …

**Summary**, from NCBI Gene [79689](https://www.ncbi.nlm.nih.gov/gene/79689):

> The protein encoded by this gene belongs to the STEAP (six transmembrane epithelial antigen of prostate) family, and resides in the golgi apparatus. It functions as a metalloreductase that has the ability to reduce both Fe(3+) to Fe(2+) and Cu(2+) to Cu(1+), using NAD(+) as acceptor. Studies in mice and human suggest that this gene maybe involved in adipocyte development and metabolism, and may contribute to the normal biology of the prostate cell, as well as prostate cancer progression. …

**Accessions** — [HGNC:21923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21923) · Entrez [79689](https://www.ncbi.nlm.nih.gov/gene/79689) · UniProt [Q687X5](https://www.uniprot.org/uniprotkb/Q687X5) · Ensembl [ENSG00000127954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127954)

## Data

Gene col 4848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4848); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4848]; `tensor/DDL_lfc|DDL_z.npy` [4848]; `embed/gene_vectors.npy` [4848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4848 or target_col == 4848). Every well: [[STEAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STEAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
