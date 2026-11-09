---
symbol: "HHIP"
type: "gene"
col: 8884
ensembl_id: "ENSG00000164161"
name: "hedgehog interacting protein"
location: "4q31.21"
module: 13
arm: "+"
pooled_cpm: 7.79
n_lines_expressing: 17
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 18
direction_downstream: 27
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# HHIP

*hedgehog interacting protein* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.66× (z +13.8, q 9e-41, up in 4 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +9.5, q 6e-19, up in 4 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.0815×, HOP62 0.121×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.138×); [[Panobinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.0817×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (C-33 A 0.153×); [[Verteporfin (drug)]] 5 µM in 1 line (C-33 A 0.168×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS4]] (+0.64, fdr 1e-05), [[NES]] (+0.62, fdr 7e-06), [[SCUBE3]] (+0.61, fdr 1e-05); moves opposite to [[SQOR]] (-0.53, fdr 3e-05), [[C1RL]] (-0.51, fdr 1e-05), [[SAA2]] (-0.50, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[COL5A3]] → it (grade C ⚠); 27 go from it, the strongest it → [[DOCK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.66×** | +13.8 | 9e-41 | 4/6 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.62×** | +12.7 | 2e-34 | 7/8 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +9.5 | 6e-19 | 4/10 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +8.9 | 1e-16 | 3/7 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +5.3 | 1e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.044 | 1/13 (NCI-H1792) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.082 | 5/11 (HS-578T, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.2 | 0.082 | 2/11 (SW48, Panc 03.27) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.082 | 2/12 (HS-578T, SNU-423) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.0815×, HOP62 0.121×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.138×); [[Panobinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.0817×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (C-33 A 0.153×); [[Verteporfin (drug)]] 5 µM in 1 line (C-33 A 0.168×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.754× | -3.3 | 0.48 | 5/13 (Panc 03.27, A-172, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.694× | -3.0 | 0.48 | 1/12 (Panc 03.27) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.674× | -3.0 | 0.48 | 2/12 (Hs 766T, A-172) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 253 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -17.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -13.9) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0739× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS4]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[NES]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SCUBE3]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[AK5]] | +0.60 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS6]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PRSS23]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KCNQ5]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PTHLH]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 | STRING 432 |
| [[SCHIP1]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SAMD3]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CSMD2]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LAMA4]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SQOR]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[C1RL]] | -0.51 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SAA2]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[SOD2]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[IRAK3]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[AZI2]] | -0.48 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[SAA2-SAA4]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TSC22D3]] | -0.48 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[SAA4]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SAA1]] | -0.47 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TOM1]] | -0.45 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[AGTRAP]] | -0.44 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL5A3]] | C | COL5A3 activity raises HHIP's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.45× lower at baseline in the lines without COL5A3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises HHIP's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 3.31× lower at baseline in the lines without RGS4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises HHIP's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 2.31× lower at baseline in the lines without LINC01592 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises HHIP's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.81× lower at baseline in the lines without ADAMTS6 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises HHIP's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 3.55× lower at baseline in the lines without CDH6 | 0.023 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises HHIP's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without ITGA11 | 0.026 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[AK5]] | C | AK5 activity raises HHIP's level | lines that do not express AK5 (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without AK5 | 0.042 | ⚠ within organs, on part of the lines; also absent: SHISAL1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises HHIP's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without COL1A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises HHIP's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 1.41× lower at baseline in the lines without VEPH1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises HHIP's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.29× lower at baseline in the lines without DKK3 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[SIGLEC15]] | C | SIGLEC15 activity raises HHIP's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.69× lower at baseline in the lines without SIGLEC15 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises HHIP's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.05× lower at baseline in the lines without INSYN2B | 0.074 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 11, C 16. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK2]] | B | HHIP activity raises DOCK2's level | lines that do not express HHIP (33) vs lines expressing it (17) | 1.68× lower at baseline in the lines without HHIP | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[IQCJ-SCHIP1]] | B | HHIP activity strengthens IQCJ-SCHIP1's drug response | lines that do not express HHIP (27) vs lines expressing it (15) | the lines without HHIP respond 0.80× as strongly (z diff +1.40); strongest at Dinaciclib 5 µM: 0.61x vs 0.27x (z diff +3.5) | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PCDHGC3]] | B | HHIP activity raises PCDHGC3's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without HHIP | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[PODXL]] | B | HHIP activity raises PODXL's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without HHIP | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[CD44]] | B | HHIP activity raises CD44's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.73× lower at baseline in the lines without HHIP | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[EVC]] | B | HHIP activity raises EVC's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.88× lower at baseline in the lines without HHIP | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[SCHIP1]] | B | HHIP activity raises SCHIP1's level | lines that do not express HHIP (33) vs lines expressing it (17) | 1.87× lower at baseline in the lines without HHIP | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[KIAA1549L]] | B | HHIP activity raises KIAA1549L's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.39× lower at baseline in the lines without HHIP | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[PRSS23]] | B | HHIP activity raises PRSS23's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without HHIP | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[IQCJ-SCHIP1]] | B | HHIP activity raises IQCJ-SCHIP1's level | lines that do not express HHIP (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without HHIP | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[MANCR]] | B | HHIP activity raises MANCR's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without HHIP | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[DKK3]] | C | HHIP activity raises DKK3's level | lines that do not express HHIP (33) vs lines expressing it (17) | 6.24× lower at baseline in the lines without HHIP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.3, 12.1); signed map (18.8, 45.6). **Vector** length 40.4, 11.7% of its response variance represented; |z| ≥ 3 in 341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.9 | +1.4 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | hedgehog interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:144,646,156-144,745,271 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HIP, FLJ20992 |
| Reactome | 4 pathways, smallest: Ligand-receptor interactions; GLI proteins bind promoters of Hh responsive genes to promote transcription; Hedgehog 'on' state |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QV1](https://www.uniprot.org/uniprotkb/Q96QV1) (Hedgehog-interacting protein):

> Modulates hedgehog signaling in several cell types including brain and lung through direct interaction with members of the hedgehog family.

**Summary**, from NCBI Gene [64399](https://www.ncbi.nlm.nih.gov/gene/64399):

> This gene encodes a member of the hedgehog-interacting protein (HHIP) family. The hedgehog (HH) proteins are evolutionarily conserved protein, which are important morphogens for a wide range of developmental processes, including anteroposterior patterns of limbs and regulation of left-right asymmetry in embryonic development. Multiple cell-surface receptors are responsible for transducing and/or regulating HH signals. The HHIP encoded by this gene is a highly conserved, vertebrate-specific …

**Accessions** — [HGNC:14866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14866) · Entrez [64399](https://www.ncbi.nlm.nih.gov/gene/64399) · UniProt [Q96QV1](https://www.uniprot.org/uniprotkb/Q96QV1) · Ensembl [ENSG00000164161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164161)

## Data

Gene col 8884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8884); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8884]; `tensor/DDL_lfc|DDL_z.npy` [8884]; `embed/gene_vectors.npy` [8884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8884 or target_col == 8884). Every well: [[HHIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HHIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
