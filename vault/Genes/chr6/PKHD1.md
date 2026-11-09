---
symbol: "PKHD1"
type: "gene"
col: 10029
ensembl_id: "ENSG00000170927"
name: "PKHD1 ciliary IPT domain containing fibrocystin/polyductin"
location: "6p12.3-p12.2"
module: 27
arm: "+"
pooled_cpm: 6.85
n_lines_expressing: 25
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 52
direction_downstream: 42
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PKHD1

*PKHD1 ciliary IPT domain containing fibrocystin/polyductin* — 6p12.3-p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.83× (z +20.8, q 0e+00, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.622× (z -4.4, q 0.005, down in 9 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST18]] (+0.79, fdr 7e-06), [[RMST]] (+0.78, fdr 7e-06), [[SMOC2]] (+0.77, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[SLC25A24P1]] → it (grade B ⚠); 42 go from it, the strongest it → [[LINC01091]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.83×** | +20.8 | 0e+00 | 9/16 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +10.6 | 8e-24 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +8.8 | 3e-16 | 2/8 (HEC-1-A, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +8.5 | 2e-15 | 9/21 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.45×** | +8.4 | 5e-15 | 9/19 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +6.9 | 6e-10 | 4/15 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +6.9 | 6e-10 | 2/4 (CFPAC-1, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 2e-04 | 7/17 (SW1417, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.6 | 3e-04 | 3/21 (CFPAC-1, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.3 | 0.001 | 1/10 (COLO 205) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 0.001 | 0/19 | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.75×** | +3.7 | 0.009 | 1/14 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.014 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.022 | 5/19 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.040 | 4/18 (CFPAC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.075 | 1/12 (HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.075 | 6/19 (COLO 205, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.075 | 8/20 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.077 | 0/14 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.4 | 0.005 | 9/19 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.667×** | -3.8 | 0.043 | 4/17 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.764×** | -3.6 | 0.070 | 4/21 (AN3 CA, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.689× | -3.2 | 0.18 | 4/20 (SW48, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.3 | 0 | 18 (13 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0418× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0636× (z -20.3) |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0817× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.173× (z -10.7) |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0240× (z -14.6) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0832× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 41.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.3) | — |
| [[A-172 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST18]] | +0.79 | +0.80 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SMOC2]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[DIP2C-AS1]] | +0.74 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[B3GAT1-DT]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC02466]] | +0.71 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[LINC02058]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[BANK1]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LINC01091]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LINC00299]] | +0.68 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[LINC01980]] | +0.68 | +0.62 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 11, C 41. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises PKHD1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.84× lower at baseline in the lines without SLC25A24P1 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[MAP2K6]] | B | MAP2K6 activity raises PKHD1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without MAP2K6 | 0.015 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[RASSF6]] | B | RASSF6 activity raises PKHD1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.20× lower at baseline in the lines without RASSF6 | 0.025 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[TOP2A]] | B | TOP2A activity lowers PKHD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LIPC]] | B | LIPC activity raises PKHD1's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without LIPC | 0.054 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[CSRNP3]] | B | CSRNP3 activity raises PKHD1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without CSRNP3 | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[C11orf52]] | B | C11orf52 activity raises PKHD1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without C11orf52 | 0.061 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[LINC00649]] | B | LINC00649 activity raises PKHD1's level | lines that do not express LINC00649 (25) vs lines expressing it (25) | 1.91× lower at baseline in the lines without LINC00649 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent |
| [[LINC02058]] | B | LINC02058 activity raises PKHD1's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.14× lower at baseline in the lines without LINC02058 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |
| [[ANO4]] | B | ANO4 activity raises PKHD1's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.27× lower at baseline in the lines without ANO4 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[LOXL4]] | B | LOXL4 activity raises PKHD1's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without LOXL4 | 0.098 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |
| [[DSCAML1]] | C | DSCAML1 activity raises PKHD1's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.58× lower at baseline in the lines without DSCAML1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 17, C 25. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | PKHD1 activity raises LINC01091's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without PKHD1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[FKBP9P1]] | B | PKHD1 activity raises FKBP9P1's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without PKHD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[FGF9]] | B | PKHD1 activity raises FGF9's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without PKHD1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[ATL1]] | B | PKHD1 activity raises ATL1's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without PKHD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[MYO3B]] | B | PKHD1 activity raises MYO3B's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without PKHD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[LINC02315]] | B | PKHD1 activity raises LINC02315's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without PKHD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[C11orf52]] | B | PKHD1 activity raises C11orf52's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.48× lower at baseline in the lines without PKHD1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[LINC02254]] | B | PKHD1 activity raises LINC02254's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without PKHD1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[BCL2L15]] | B | PKHD1 activity raises BCL2L15's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.63× lower at baseline in the lines without PKHD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[ENPP3]] | B | PKHD1 activity raises ENPP3's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.00× lower at baseline in the lines without PKHD1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[IGFL4]] | B | PKHD1 activity raises IGFL4's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without PKHD1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[HGD]] | B | PKHD1 activity raises HGD's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without PKHD1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.8, 43.8); signed map (60.1, 16.3). **Vector** length 55.3, 14.4% of its response variance represented; |z| ≥ 3 in 529 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +20.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +3.5 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | PKHD1 ciliary IPT domain containing fibrocystin/polyductin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3-p12.2 — chr6:51,615,299-52,087,613 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARPKD, FCYT, FPC; previously TIGM1 |
| Gene groups (HGNC) | IPT domain containing |
| Hallmark sets | APICAL_SURFACE |
| Matched by | ensembl_id |

**Function**, from UniProt [P08F94](https://www.uniprot.org/uniprotkb/P08F94) (Fibrocystin):

> Promotes ciliogenesis in renal epithelial cells and therefore participates in the tubules formation and/ or ensures the maintenance of the architecture of the lumen of the kidney (By similarity). Has an impact on cellular symmetry by ensuring correct bipolar cell division through the regulation of centrosome duplication and mitotic spindle assembly and by maintaining oriented cell division (OCD) during tubular elongation through planar cell polarity (PCP) pathway. During epithelial cell …

**Summary**, from NCBI Gene [5314](https://www.ncbi.nlm.nih.gov/gene/5314):

> The protein encoded by this gene is predicted to have a single transmembrane (TM)-spanning domain and multiple copies of an immunoglobulin-like plexin-transcription-factor domain. Alternative splicing results in two transcript variants encoding different isoforms. Other alternatively spliced transcripts have been described, but the full length sequences have not been determined. Several of these transcripts are predicted to encode truncated products which lack the TM and may be secreted. …

**Accessions** — [HGNC:9016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9016) · Entrez [5314](https://www.ncbi.nlm.nih.gov/gene/5314) · UniProt [P08F94](https://www.uniprot.org/uniprotkb/P08F94) · Ensembl [ENSG00000170927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170927)

## Data

Gene col 10029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10029); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10029]; `tensor/DDL_lfc|DDL_z.npy` [10029]; `embed/gene_vectors.npy` [10029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10029 or target_col == 10029). Every well: [[PKHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
