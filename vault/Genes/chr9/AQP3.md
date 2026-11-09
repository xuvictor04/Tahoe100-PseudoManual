---
symbol: "AQP3"
type: "gene"
col: 9098
ensembl_id: "ENSG00000165272"
name: "aquaporin 3 (Gill blood group)"
location: "9p13.3"
module: 155
arm: "+"
pooled_cpm: 2.73
n_lines_expressing: 31
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 37
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# AQP3

*aquaporin 3 (Gill blood group)* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.31× (z +13.0, q 5e-36, up in 14 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Binimetinib (drug)]] 0.5 µM in 1 line (BT-474 0.0426×); [[Cobimetinib (drug)]] 5 µM in 1 line (BT-474 0.0220×); [[Gefitinib (drug)]] 5 µM in 1 line (BT-474 0.0261×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLPI]] (+0.62, fdr 2e-05), [[FGB]] (+0.57, fdr 4e-05), [[SERPINA1]] (+0.56, fdr 9e-05); moves opposite to [[PGR]] (-0.42, fdr 1e-04), [[ZW10]] (-0.40, fdr 4e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[MUC5AC]] → it (grade B ⚠); 37 go from it, the strongest it → [[KLF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.31×** | +13.0 | 5e-36 | 14/22 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **7.50×** | +12.7 | 1e-34 | 7/11 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.69×** | +11.7 | 4e-29 | 10/18 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.64×** | +11.5 | 2e-28 | 23/27 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.76×** | +11.1 | 2e-26 | 13/21 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **5.83×** | +10.7 | 1e-24 | 3/4 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.34×** | +9.3 | 2e-18 | 21/24 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **4.15×** | +9.0 | 2e-17 | 22/27 (HCT15, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.84×** | +8.5 | 1e-15 | 9/14 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.05×** | +8.2 | 2e-14 | 2/6 (NCI-H2347, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.08×** | +7.1 | 7e-11 | 18/21 (Panc 03.27, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.02×** | +7.0 | 2e-10 | 16/24 (HCT15, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.79×** | +6.5 | 5e-09 | 15/28 (SW480, HepG2/C3A, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.82×** | +6.3 | 1e-08 | 5/11 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.63×** | +6.1 | 4e-08 | 11/22 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.52×** | +5.8 | 2e-07 | 17/28 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.2 | 8e-06 | 7/27 (SW480, HepG2/C3A, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +4.9 | 3e-05 | 5/23 (HCT15, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +4.8 | 4e-05 | 10/26 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.019 | 8/17 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.94×** | +3.0 | 0.069 | 1/14 (NCI-H460) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.93×** | +3.0 | 0.069 | 2/13 (Hs 766T, NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +2.9 | 0.071 | 6/27 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Binimetinib (drug)]] 0.5 µM in 1 line (BT-474 0.0426×); [[Cobimetinib (drug)]] 5 µM in 1 line (BT-474 0.0220×); [[Gefitinib (drug)]] 5 µM in 1 line (BT-474 0.0261×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 17.2 | 0 | 15 (2 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.0426× (z -12.1) |
| [[HCT15 (line)]] | alt | 6.86 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 50.7× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 42.4× (z +10.8) | — |
| [[SW480 (line)]] | alt | 2.40 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 24.2× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 8.64× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0541× (z -8.6) |
| [[KATO III (line)]] | alt | 3.10 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.2× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0833× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 8.52 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.47× (z +9.1) | — |
| [[A-172 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.783 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLPI]] | +0.62 | +0.48 / +0.66 | both halves | 2e-05 | **novel candidate** |
| [[FGB]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SERPINA1]] | +0.56 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[SERPINB4]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[S100A9]] | +0.55 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[FLRT3]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[MUC5AC]] | +0.54 | +0.49 / +0.58 | both halves | 2e-05 |  |
| [[SERPINB3]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[AREG]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[SYT12]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[LINC01440]] | +0.52 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[LINC01503]] | +0.51 | +0.39 / +0.64 | both halves | 6e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.42 | -0.35 / -0.37 | both halves | 1e-04 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ZW10]] | -0.40 | -0.46 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 16, C 7. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC5AC]] | B | MUC5AC activity raises AQP3's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.86× lower at baseline in the lines without MUC5AC | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[GSDMC]] | B | GSDMC activity raises AQP3's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 3.55× lower at baseline in the lines without GSDMC | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1 |
| [[MUC2]] | B | MUC2 activity raises AQP3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 4.36× lower at baseline in the lines without MUC2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[LRG1]] | B | LRG1 activity raises AQP3's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without LRG1 | 0.003 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[MUC5B]] | B | MUC5B activity raises AQP3's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.58× lower at baseline in the lines without MUC5B | 0.008 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[KLF5]] | B | KLF5 activity raises AQP3's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without KLF5 | 0.031 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[EPPK1]] | B | EPPK1 activity raises AQP3's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 2.17× lower at baseline in the lines without EPPK1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[TOP2A]] | B | TOP2A activity lowers AQP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYT12]] | B | SYT12 activity raises AQP3's level | lines that do not express SYT12 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without SYT12 | 0.044 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| [[P2RY6]] | B | P2RY6 activity raises AQP3's level | lines that do not express P2RY6 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without P2RY6 | 0.048 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, FGG |
| [[ATAD3C]] | B | ATAD3C activity raises AQP3's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.11× lower at baseline in the lines without ATAD3C | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[PI3]] | B | PI3 activity raises AQP3's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without PI3 | 0.064 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 30, C 7. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF5]] | B | AQP3 activity raises KLF5's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 4.68× lower at baseline in the lines without AQP3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[NCOA3]] | B | AQP3 activity raises NCOA3's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without AQP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | AQP3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | AQP3 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 1.18× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[PPL]] | B | AQP3 activity raises PPL's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without AQP3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[CYBA]] | B | AQP3 activity raises CYBA's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 3.11× lower at baseline in the lines without AQP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | AQP3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[LRG1]] | B | AQP3 activity raises LRG1's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without AQP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[CST3]] | B | AQP3 activity raises CST3's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without AQP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | AQP3 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 1.26× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[THBS3-AS1]] | B | AQP3 activity lowers THBS3-AS1's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 1.43× higher at baseline in the lines without AQP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[PLA2R1]] | B | AQP3 activity raises PLA2R1's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 2.43× lower at baseline in the lines without AQP3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, 48.9); signed map (55.2, 23.4). **Vector** length 69.2, 17.1% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.51 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.51 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.3 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.5 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -1.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | aquaporin 3 (Gill blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,441,156-33,447,596 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GIL |
| Gene groups (HGNC) | Aquaporins; Blood group antigens |
| Hallmark sets | UV_RESPONSE_UP, HEME_METABOLISM, ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Vasopressin regulates renal water homeostasis via Aquaporins; Aquaporin-mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92482](https://www.uniprot.org/uniprotkb/Q92482) (Aquaporin-3):

> Aquaglyceroporins form homotetrameric transmembrane channels, with each monomer independently mediating glycerol and water transport across the plasma membrane along their osmotic gradient. Could also be permeable to urea (By similarity). Also participates in cell permeability to H2O2 and H2O2-mediated signaling. In skin, transports glycerol to the epidermis and stratum corneum, where it maintains hydration, elasticity, and supports lipid biosynthesis for barrier repair (By similarity). In …

**Summary**, from NCBI Gene [360](https://www.ncbi.nlm.nih.gov/gene/360):

> This gene encodes the water channel protein aquaporin 3. Aquaporins are a family of small integral membrane proteins related to the major intrinsic protein, also known as aquaporin 0. Aquaporin 3 is localized at the basal lateral membranes of collecting duct cells in the kidney. In addition to its water channel function, aquaporin 3 has been found to facilitate the transport of nonionic small solutes such as urea and glycerol, but to a smaller degree. It has been suggested that water channels …

**Accessions** — [HGNC:636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:636) · Entrez [360](https://www.ncbi.nlm.nih.gov/gene/360) · UniProt [Q92482](https://www.uniprot.org/uniprotkb/Q92482) · Ensembl [ENSG00000165272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165272)

## Data

Gene col 9098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9098); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9098]; `tensor/DDL_lfc|DDL_z.npy` [9098]; `embed/gene_vectors.npy` [9098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9098 or target_col == 9098). Every well: [[AQP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AQP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
