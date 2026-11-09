---
symbol: "NLRP3"
type: "gene"
col: 8567
ensembl_id: "ENSG00000162711"
name: "NLR family pyrin domain containing 3"
location: "1q44"
module: 13
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 22
n_dd_up: 19
n_dd_down: 39
n_dd_up_clean: 11
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 11
direction_downstream: 24
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NLRP3

*NLR family pyrin domain containing 3* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.51× (z +9.5, q 8e-19, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 1.88× (z +4.6, q 4e-04, up in 7 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.333× (z -9.6, q 6e-19, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFX8]] (+0.76, fdr 7e-06), [[LINC02454]] (+0.71, fdr 7e-06), [[KIAA1549L]] (+0.71, fdr 7e-06); moves opposite to [[MBNL2]] (-0.51, fdr 3e-05), [[GULP1]] (-0.51, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CDYL2]] → it (grade B ⚠); 24 go from it, the strongest it → [[APBB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +9.5 | 8e-19 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +6.5 | 2e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +5.4 | 2e-05 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.33×** | +4.8 | 2e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.88×** | +4.6 | 4e-04 | 7/13 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 9/20 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.68×** | +4.1 | 0.003 | 6/19 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +4.0 | 0.004 | 9/18 (LOX-IMVI, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.014 | 3/15 (A-427, RPMI-7951, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.87×** | +3.5 | 0.023 | 2/14 (PANC-1, A-427) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.5 | 0.024 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +3.3 | 0.047 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.2 | 0.054 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.17×** | +3.2 | 0.054 | 3/11 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.48×** | +3.1 | 0.070 | 4/19 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.06×** | +3.0 | 0.093 | 2/8 (NCI-H1573, PANC-1) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.093 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 0.05 µM |  | **1.52×** | +3.0 | 0.094 | 0/19 | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.094 | 6/20 (PANC-1, A-427, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.333×** | -9.6 | 6e-19 | 19/20 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.294×** | -8.9 | 1e-16 | 14/19 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.379×** | -7.6 | 4e-12 | 16/19 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.379×** | -7.6 | 4e-12 | 16/19 (HOP62, J82, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.457×** | -7.4 | 1e-11 | 16/20 (HS-578T, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.499×** | -6.5 | 9e-09 | 14/20 (NCI-H1573, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.431×** | -6.3 | 2e-08 | 14/19 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.576×** | -5.8 | 4e-07 | 18/20 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.597×** | -5.5 | 2e-06 | 13/20 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.497×** | -5.5 | 2e-06 | 13/19 (PANC-1, NCI-H1573, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -5.3 | 6e-06 | 13/19 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.519×** | -5.1 | 1e-05 | 15/19 (H4, J82, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.307×** | -4.9 | 5e-05 | 8/20 (HOP62, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.847× | -4.8 | 5e-05 | 4/20 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.314×** | -4.8 | 7e-05 | 9/19 (HOP62, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -4.4 | 5e-04 | 8/14 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.5 | 0 | 24 (6 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0469× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 20 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00850× (z -22.6) |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 13 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -19.9) |
| [[J82 (line)]] | alt | 5.13 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.0440× (z -15.0) |
| [[H4 (line)]] | wt | 16.2 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0106× (z -13.9) |
| [[A-172 (line)]] | wt | 3.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0526× (z -8.5) |
| [[HS-578T (line)]] | alt | 4.44 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.0401× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 7.63 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0399× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.269× (z -9.3) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.314 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX8]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC02454]] | +0.71 | +0.68 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[KIAA1549L]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.69 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[SHANK1]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[VEPH1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LRRC8C]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DSCAM]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CLMP]] | +0.67 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[BNC1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL2]] | -0.51 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[GULP1]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDYL2]] | B | CDYL2 activity raises NLRP3's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without CDYL2 | 0.060 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330 |
| [[APCDD1L]] | C | APCDD1L activity raises NLRP3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.10× lower at baseline in the lines without APCDD1L | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises NLRP3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.26× lower at baseline in the lines without ROBO4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[MME]] | C | MME activity raises NLRP3's level | lines that do not express MME (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without MME | 0.026 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises NLRP3's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 3.05× lower at baseline in the lines without DSCAM | 0.033 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[KIAA1549L]] | C | KIAA1549L activity raises NLRP3's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without KIAA1549L | 0.034 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises NLRP3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without HS3ST3A1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises NLRP3's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without WNT5A | 0.065 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises NLRP3's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without VEPH1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[BNC1]] | C | BNC1 activity raises NLRP3's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.74× lower at baseline in the lines without BNC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |
| [[BCL2A1]] | C | BCL2A1 activity raises NLRP3's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without BCL2A1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 13, C 11. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APBB2]] | B | NLRP3 activity raises APBB2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without NLRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[MARCHF3]] | B | NLRP3 activity raises MARCHF3's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without NLRP3 | 0.025 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[MICAL2]] | B | NLRP3 activity raises MICAL2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.41× lower at baseline in the lines without NLRP3 | 0.028 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[NT5E]] | B | NLRP3 activity raises NT5E's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 3.37× lower at baseline in the lines without NLRP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[PDE4DIPP2]] | B | NLRP3 activity raises PDE4DIPP2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without NLRP3 | 0.044 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[ATP13A3]] | B | NLRP3 activity raises ATP13A3's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.80× lower at baseline in the lines without NLRP3 | 0.045 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[FXYD5]] | B | NLRP3 activity raises FXYD5's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without NLRP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[HMGA2]] | B | NLRP3 activity raises HMGA2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.29× lower at baseline in the lines without NLRP3 | 0.049 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[C13orf46]] | B | NLRP3 activity raises C13orf46's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without NLRP3 | 0.078 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[CDYL2]] | B | NLRP3 activity raises CDYL2's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without NLRP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[GRAMD1C]] | B | NLRP3 activity raises GRAMD1C's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.58× lower at baseline in the lines without NLRP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[SLC46A3]] | B | NLRP3 activity raises SLC46A3's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without NLRP3 | 0.095 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.8, 8.7); signed map (12.5, 47.7). **Vector** length 83.0, 27.0% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.1 | -7.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.8 | -9.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -8.9 |

## What is on record

|  |  |
|---|---|
| Name | NLR family pyrin domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:247,332,331-247,449,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AGTAVPRL, AII, AVP, FCAS, FCU, NALP3, PYPAF1, MWS; previously C1orf7, CIAS1, DFNA34 |
| Gene groups (HGNC) | NLR family; Pyrin domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE |
| Reactome | 25 pathways, smallest: The NLRP3 inflammasome; Inflammasomes; Cell recruitment (pro-inflammatory response) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P20](https://www.uniprot.org/uniprotkb/Q96P20) (NACHT, LRR and PYD domains-containing protein 3):

> Sensor component of the NLRP3 inflammasome, which mediates inflammasome activation in response to defects in membrane integrity, leading to secretion of inflammatory cytokines IL1B and IL18 and pyroptosis. In response to pathogens and other damage-associated signals that affect the integrity of membranes, initiates the formation of the inflammasome polymeric complex composed of NLRP3, CASP1 and PYCARD/ASC. Recruitment of pro-caspase-1 (proCASP1) to the NLRP3 inflammasome promotes caspase-1 …

**Summary**, from NCBI Gene [114548](https://www.ncbi.nlm.nih.gov/gene/114548):

> This gene encodes a pyrin-like protein containing a pyrin domain, a nucleotide-binding site (NBS) domain, and a leucine-rich repeat (LRR) motif. This protein interacts with the apoptosis-associated speck-like protein PYCARD/ASC, which contains a caspase recruitment domain, and is a member of the NLRP3 inflammasome complex. This complex functions as an upstream activator of NF-kappaB signaling, and it plays a role in the regulation of inflammation, the immune response, and apoptosis. The …

**Accessions** — [HGNC:16400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16400) · Entrez [114548](https://www.ncbi.nlm.nih.gov/gene/114548) · UniProt [Q96P20](https://www.uniprot.org/uniprotkb/Q96P20) · Ensembl [ENSG00000162711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162711)

## Data

Gene col 8567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8567); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8567]; `tensor/DDL_lfc|DDL_z.npy` [8567]; `embed/gene_vectors.npy` [8567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8567 or target_col == 8567). Every well: [[NLRP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLRP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
