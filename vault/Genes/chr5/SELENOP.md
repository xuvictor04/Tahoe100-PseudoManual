---
symbol: "SELENOP"
type: "gene"
col: 14710
ensembl_id: "ENSG00000250722"
name: "selenoprotein P"
location: "5p12"
module: 8
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 32
n_dd_up: 48
n_dd_down: 2
n_dd_up_clean: 40
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 27
direction_downstream: 18
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SELENOP

*selenoprotein P* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.13× (z +14.4, q 5e-44, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.602× (z -4.6, q 0.003, down in 9 of 26 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.666× (z -3.7, q 0.071, down in 11 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0871×); [[Acetazolamide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0692×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCIN]] (+0.72, fdr 7e-06), [[RASGEF1B]] (+0.64, fdr 7e-06), [[FMO5]] (+0.61, fdr 9e-06); moves opposite to [[FERMT1]] (-0.57, fdr 1e-05), [[MST1R]] (-0.54, fdr 1e-05), [[GJB3]] (-0.53, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); 18 go from it, the strongest it → [[SH3BGRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.13×** | +14.4 | 5e-44 | 24/25 (SW1417, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +14.2 | 2e-43 | 18/23 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.77×** | +13.9 | 1e-41 | 13/15 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.68×** | +13.2 | 1e-37 | 5/6 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.72×** | +10.8 | 3e-25 | 7/10 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.03×** | +9.9 | 6e-21 | 22/25 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.71×** | +8.9 | 6e-17 | 23/26 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **2.14×** | +7.8 | 5e-13 | 19/25 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.34×** | +7.5 | 3e-12 | 20/26 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +6.7 | 8e-10 | 6/25 (LS 180, SHP-77, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +6.7 | 1e-09 | 18/26 (BT-474, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.07×** | +6.5 | 4e-09 | 20/26 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.63×** | +5.9 | 1e-07 | 16/25 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.61×** | +5.8 | 2e-07 | 14/25 (SW480, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +5.3 | 3e-06 | 11/24 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.34×** | +5.2 | 8e-06 | 9/23 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.30×** | +5.1 | 1e-05 | 9/15 (AsPC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.83×** | +5.1 | 1e-05 | 11/25 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14710.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0871×); [[Acetazolamide (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0692×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.602×** | -4.6 | 0.003 | 9/26 (AsPC-1, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.071 | 11/25 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.706× | -3.1 | 0.26 | 11/23 (H4, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 0.05 µM |  | 0.695× | -3.1 | 0.26 | 8/25 (NCI-H1792, SW48, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.611× | -3.0 | 0.26 | 6/26 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 174 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 4.95 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +10.1) | — |
| [[KATO III (line)]] | alt | 5.17 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.2× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 6.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.90× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 4.01 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0692× (z -8.7) |
| [[SHP-77 (line)]] | alt | 8.53 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0871× (z -9.5) |
| [[SW1417 (line)]] | alt | 6.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.9× (z +13.4) | — |
| [[A-172 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCIN]] | +0.72 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[RASGEF1B]] | +0.64 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[FMO5]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[SLC40A1]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ACSM3]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MPP7]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SYNPR-AS1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SLC7A8]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[GALM]] | +0.58 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | +0.57 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CXADR]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT1]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MST1R]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[GJB3]] | -0.53 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[HAS3]] | -0.52 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[LAMA3]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PALD1]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[S100A16]] | -0.52 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[LRP8]] | -0.51 | -0.54 / -0.52 | both halves | 1e-05 | STRING 837 |
| [[CASC19]] | -0.51 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[NACC1]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[EIPR1]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TGFA]] | -0.49 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 23, C 4. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises SELENOP's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without NR3C2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises SELENOP's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without SYNPR-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[FOXP2]] | B | FOXP2 activity raises SELENOP's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.53× lower at baseline in the lines without FOXP2 | 0.011 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[TGFA]] | B | TGFA activity raises SELENOP's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.15× lower at baseline in the lines without TGFA | 0.020 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises SELENOP's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without SH3BGRL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[SCIN]] | B | SCIN activity raises SELENOP's level | lines that do not express SCIN (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without SCIN | 0.021 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[MPP7]] | B | MPP7 activity raises SELENOP's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without MPP7 | 0.025 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[LINC00992]] | B | LINC00992 activity raises SELENOP's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without LINC00992 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[LNX1]] | B | LNX1 activity raises SELENOP's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without LNX1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[LAMA3]] | B | LAMA3 activity raises SELENOP's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without LAMA3 | 0.039 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[MST1R]] | B | MST1R activity raises SELENOP's level | lines that do not express MST1R (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without MST1R | 0.045 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[FGF9]] | B | FGF9 activity raises SELENOP's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 1.63× lower at baseline in the lines without FGF9 | 0.048 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 13, C 5. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3BGRL2]] | B | SELENOP activity raises SH3BGRL2's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.77× lower at baseline in the lines without SELENOP | 0.008 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[FOXP2]] | B | SELENOP activity raises FOXP2's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 3.45× lower at baseline in the lines without SELENOP | 0.017 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[PKIB]] | B | SELENOP activity raises PKIB's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without SELENOP | 0.018 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[LINC00992]] | B | SELENOP activity raises LINC00992's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without SELENOP | 0.022 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[LNX1]] | B | SELENOP activity raises LNX1's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.91× lower at baseline in the lines without SELENOP | 0.048 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[SLC7A8]] | B | SELENOP activity raises SLC7A8's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without SELENOP | 0.048 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[MST1R]] | B | SELENOP activity strengthens MST1R's drug response | lines that do not express SELENOP (5) vs lines expressing it (19) | the lines without SELENOP respond 0.33× as strongly (z diff +2.45); strongest at Panobinostat 5 µM: 1.12x vs 0.43x (z diff +5.2) | 0.057 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LAMA3]] | B | SELENOP activity raises LAMA3's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 3.48× lower at baseline in the lines without SELENOP | 0.060 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[RAB17]] | B | SELENOP activity raises RAB17's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.33× lower at baseline in the lines without SELENOP | 0.070 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[C4orf19]] | B | SELENOP activity raises C4orf19's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without SELENOP | 0.071 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[SLC40A1]] | B | SELENOP activity raises SLC40A1's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without SELENOP | 0.079 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[RASGEF1B]] | B | SELENOP activity raises RASGEF1B's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without SELENOP | 0.086 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.443). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.7, 52.0); signed map (53.4, 1.4). **Vector** length 64.8, 16.1% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +7.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein P |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:42,799,880-42,887,392 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SeP, SELP, SEPP; previously SEPP1 |
| Gene groups (HGNC) | Selenoproteins |
| Hallmark sets | ANDROGEN_RESPONSE, KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49908](https://www.uniprot.org/uniprotkb/P49908) (Selenoprotein P):

> Might be responsible for some of the extracellular antioxidant defense properties of selenium or might be involved in the transport of selenium. May supply selenium to tissues such as brain and testis.

**Summary**, from NCBI Gene [6414](https://www.ncbi.nlm.nih.gov/gene/6414):

> This gene encodes a selenoprotein that is predominantly expressed in the liver and secreted into the plasma. This selenoprotein is unique in that it contains multiple selenocysteine (Sec) residues per polypeptide (10 in human), and accounts for most of the selenium in plasma. It has been implicated as an extracellular antioxidant, and in the transport of selenium to extra-hepatic tissues via apolipoprotein E receptor-2 (apoER2). Mice lacking this gene exhibit neurological dysfunction, …

**Accessions** — [HGNC:10751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10751) · Entrez [6414](https://www.ncbi.nlm.nih.gov/gene/6414) · UniProt [P49908](https://www.uniprot.org/uniprotkb/P49908) · Ensembl [ENSG00000250722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250722)

## Data

Gene col 14710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14710); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14710]; `tensor/DDL_lfc|DDL_z.npy` [14710]; `embed/gene_vectors.npy` [14710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14710 or target_col == 14710). Every well: [[SELENOP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
