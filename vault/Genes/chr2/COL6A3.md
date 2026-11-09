---
symbol: "COL6A3"
type: "gene"
col: 8675
ensembl_id: "ENSG00000163359"
name: "collagen type VI alpha 3 chain"
location: "2q37.3"
module: 13
arm: "+"
pooled_cpm: 236.3
n_lines_expressing: 11
n_dd_up: 3
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 43
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL6A3

*collagen type VI alpha 3 chain* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.33× (z +10.4, q 2e-22, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -8.8, q 6e-16, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.76, fdr 7e-06), [[THBS2]] (+0.76, fdr 7e-06), [[PDGFRB]] (+0.74, fdr 7e-06); moves opposite to [[SLC44A3]] (-0.49, fdr 6e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[PDGFRB]] → it (grade C ⚠); 19 go from it, the strongest it → [[TRIB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +10.4 | 2e-22 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +8.9 | 2e-16 | 2/8 (SK-MEL-2, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +6.8 | 1e-09 | 2/8 (SK-MEL-2, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.67× | +3.2 | 0.23 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -8.8 | 6e-16 | 9/9 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.373×** | -8.5 | 7e-15 | 9/9 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.448×** | -6.6 | 6e-09 | 9/9 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.531×** | -5.5 | 7e-06 | 7/9 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -5.2 | 2e-05 | 8/9 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.591×** | -4.5 | 6e-04 | 2/8 (H4, HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.685×** | -4.5 | 7e-04 | 2/9 (MIA PaCa-2, SK-MEL-2) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.618×** | -4.1 | 0.002 | 6/9 (MIA PaCa-2, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.598×** | -4.1 | 0.003 | 2/9 (SK-MEL-2, MIA PaCa-2) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.617×** | -3.8 | 0.007 | 0/9 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.672×** | -3.4 | 0.033 | 8/9 (HOP62, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -3.3 | 0.044 | 3/9 (HOP62, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.693×** | -3.2 | 0.070 | 0/8 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,014 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0232× (z -27.9) |
| [[H4 (line)]] | wt | 3,169 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00544× (z -38.7) |
| [[hTERT-HPNE (line)]] | wt | 3,396 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0240× (z -22.6) |
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 4 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.373× (z -19.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.112× (z -17.5) |
| [[SNU-423 (line)]] | alt | 1,280 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0275× (z -26.6) |
| [[SW 1088 (line)]] | alt | 4,270 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0400× (z -19.7) |
| [[Hs 766T (line)]] | wt | 85.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.6) |
| [[HS-578T (line)]] | alt | 3,754 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -16.5) |
| [[A-172 (line)]] | wt | 41.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 36.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 46.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 24.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 16.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 892 |
| [[THBS2]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 799 |
| [[PDGFRB]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 633 |
| [[CSPG4]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[DENND2A]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[COL6A2]] | +0.70 | +0.76 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 994 |
| [[APCDD1L]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[LINC01615]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[WNT5A]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[NAV1]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DKK3]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ANPEP]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A3]] | -0.49 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 0, C 43. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFRB]] | C | PDGFRB activity raises COL6A3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 11.80× lower at baseline in the lines without PDGFRB | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises COL6A3's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 20.31× lower at baseline in the lines without LINC01242 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[GYPC]] | C | GYPC activity raises COL6A3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 10.25× lower at baseline in the lines without GYPC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises COL6A3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 9.50× lower at baseline in the lines without APCDD1L | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises COL6A3's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 8.44× lower at baseline in the lines without ITGA4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises COL6A3's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 6.23× lower at baseline in the lines without HTR1F | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises COL6A3's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 8.23× lower at baseline in the lines without EVC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[VEPH1]] | C | VEPH1 activity raises COL6A3's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 4.87× lower at baseline in the lines without VEPH1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises COL6A3's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 5.58× lower at baseline in the lines without PTGFR | 0.016 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises COL6A3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 7.40× lower at baseline in the lines without HS3ST3A1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises COL6A3's level | lines that do not express CARMN (40) vs lines expressing it (10) | 16.73× lower at baseline in the lines without CARMN | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises COL6A3's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 5.59× lower at baseline in the lines without ADAMTS2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 3, C 16. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIB2]] | B | COL6A3 activity raises TRIB2's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without COL6A3 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474 |
| [[COL13A1]] | B | COL6A3 activity raises COL13A1's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 3.40× lower at baseline in the lines without COL6A3 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474 |
| [[SH2B3]] | B | COL6A3 activity raises SH2B3's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 2.31× lower at baseline in the lines without COL6A3 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474 |
| [[VEPH1]] | C | COL6A3 activity raises VEPH1's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 3.49× lower at baseline in the lines without COL6A3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[AK5]] | C | COL6A3 activity raises AK5's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 3.35× lower at baseline in the lines without COL6A3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[RFX8]] | C | COL6A3 activity raises RFX8's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 6.57× lower at baseline in the lines without COL6A3 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[PDGFRB]] | C | COL6A3 activity raises PDGFRB's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 5.82× lower at baseline in the lines without COL6A3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[GYPC]] | C | COL6A3 activity raises GYPC's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 5.28× lower at baseline in the lines without COL6A3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[SEMA5A]] | C | COL6A3 activity raises SEMA5A's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 5.85× lower at baseline in the lines without COL6A3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[APCDD1L]] | C | COL6A3 activity raises APCDD1L's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 4.46× lower at baseline in the lines without COL6A3 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[APCDD1L-DT]] | C | COL6A3 activity raises APCDD1L-DT's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 4.45× lower at baseline in the lines without COL6A3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |
| [[GLYATL2]] | C | COL6A3 activity raises GLYATL2's level | lines that do not express COL6A3 (39) vs lines expressing it (11) | 3.90× lower at baseline in the lines without COL6A3 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000222032, LINC01242, ENSG00000287474; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.6, 18.4); signed map (25.0, 45.7). **Vector** length 56.5, 26.8% of its response variance represented; |z| ≥ 3 in 313 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +0.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | -1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | collagen type VI alpha 3 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,324,003-237,414,328 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Collagens |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 15 pathways, smallest: NCAM1 interactions; Collagen chain trimerization; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P12111](https://www.uniprot.org/uniprotkb/P12111) (Collagen alpha-3(VI) chain):

> Collagen VI acts as a cell-binding protein.

**Summary**, from NCBI Gene [1293](https://www.ncbi.nlm.nih.gov/gene/1293):

> This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino terminal globular domain of all the alpha chains. These domains have been shown to bind extracellular …

**Accessions** — [HGNC:2213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2213) · Entrez [1293](https://www.ncbi.nlm.nih.gov/gene/1293) · UniProt [P12111](https://www.uniprot.org/uniprotkb/P12111) · Ensembl [ENSG00000163359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163359)

## Data

Gene col 8675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8675); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8675]; `tensor/DDL_lfc|DDL_z.npy` [8675]; `embed/gene_vectors.npy` [8675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8675 or target_col == 8675). Every well: [[COL6A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL6A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
