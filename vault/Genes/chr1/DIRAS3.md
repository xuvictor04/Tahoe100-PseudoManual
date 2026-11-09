---
symbol: "DIRAS3"
type: "gene"
col: 8536
ensembl_id: "ENSG00000162595"
name: "DIRAS family GTPase 3"
location: "1p31.3"
module: 13
arm: "+"
pooled_cpm: 7.04
n_lines_expressing: 6
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 33
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# DIRAS3

*DIRAS family GTPase 3* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.64× (z +9.0, q 9e-17, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.29× (z +5.8, q 8e-07, up in 1 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0260×); [[Panobinostat (drug)]] 5 µM in 1 line (A-172 0.112×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.120×; ⚠ cell-cycle shift, explains ~70% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUCNR1]] (+0.68, fdr 7e-06), [[SCUBE3]] (+0.66, fdr 1e-05), [[THBS2]] (+0.62, fdr 1e-05); moves opposite to [[MIR3936HG]] (-0.44, fdr 9e-05), [[ZNF33B]] (-0.44, fdr 1e-04), [[ROS1]] (-0.41, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ITGA11]] → it (grade C ⚠); 33 go from it, the strongest it → [[GDNF-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8536.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.64×** | +9.0 | 9e-17 | 1/2 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.42×** | +8.4 | 1e-14 | 1/2 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.39×** | +6.8 | 2e-09 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.29×** | +5.8 | 8e-07 | 1/3 (RKO) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +5.2 | 2e-05 | 1/3 (SW 1088) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +4.3 | 0.002 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.10×** | +3.7 | 0.018 | 0/2 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +3.6 | 0.020 | 0/3 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.06×** | +3.6 | 0.020 | 1/3 (RKO) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.5 | 0.026 | 0/2 | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.039 | 0/4 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8536.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0260×); [[Panobinostat (drug)]] 5 µM in 1 line (A-172 0.112×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-172 0.120×; ⚠ cell-cycle shift, explains ~70% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.459× | -3.5 | 0.23 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8536. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 227 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 5 µM 0.0260× (z -10.2) |
| [[A-427 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.708 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8536), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCNR1]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SCUBE3]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[THBS2]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LINC01615]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[VSTM4]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TEK]] | +0.60 | +0.70 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[PRSS23]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS6]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SEMA5A]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PGF]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR3936HG]] | -0.44 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[ZNF33B]] | -0.44 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[ROS1]] | -0.41 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[LINC02241]] | -0.40 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[TNFAIP6]] | -0.40 | -0.48 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA11]] | C | ITGA11 activity raises DIRAS3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.10× lower at baseline in the lines without ITGA11 | 0.014 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises DIRAS3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without APCDD1L | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises DIRAS3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without SPOCK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises DIRAS3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without PDGFRB | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises DIRAS3's level | lines that do not express SPARC (34) vs lines expressing it (16) | 1.94× lower at baseline in the lines without SPARC | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises DIRAS3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 2.58× lower at baseline in the lines without LINC01411 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[ROS1]] | C | ROS1 activity raises DIRAS3's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without ROS1 | 0.045 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent; co-absent with the target |
| [[LRRC17]] | C | LRRC17 activity raises DIRAS3's level | lines that do not express LRRC17 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without LRRC17 | 0.050 | ⚠ within organs, on part of the lines; also absent: AEBP1, ARHGAP6, LINC02240; maybe low, not absent; co-absent with the target |
| [[THBS2]] | C | THBS2 activity raises DIRAS3's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without THBS2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises DIRAS3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without HS3ST3A1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises DIRAS3's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without PRRX1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises DIRAS3's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.32× lower at baseline in the lines without COL1A2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 5, C 28. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDNF-AS1]] | B | DIRAS3 activity raises GDNF-AS1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 1.60× lower at baseline in the lines without DIRAS3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[CLEC11A]] | B | DIRAS3 activity raises CLEC11A's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.52× lower at baseline in the lines without DIRAS3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[RNF152]] | B | DIRAS3 activity raises RNF152's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 4.00× lower at baseline in the lines without DIRAS3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[SLCO1C1]] | B | DIRAS3 activity raises SLCO1C1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 2.07× lower at baseline in the lines without DIRAS3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[DENND2A]] | B | DIRAS3 activity raises DENND2A's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 2.78× lower at baseline in the lines without DIRAS3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[PAMR1]] | C | DIRAS3 activity raises PAMR1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 6.06× lower at baseline in the lines without DIRAS3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[GDNF]] | C | DIRAS3 activity raises GDNF's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 2.47× lower at baseline in the lines without DIRAS3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[LOXL3]] | C | DIRAS3 activity raises LOXL3's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.49× lower at baseline in the lines without DIRAS3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[CARMN]] | C | DIRAS3 activity raises CARMN's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.48× lower at baseline in the lines without DIRAS3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[COL1A2]] | C | DIRAS3 activity raises COL1A2's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 11.22× lower at baseline in the lines without DIRAS3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[BAALC]] | C | DIRAS3 activity raises BAALC's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 4.45× lower at baseline in the lines without DIRAS3 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[PRRX1]] | C | DIRAS3 activity raises PRRX1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 6.83× lower at baseline in the lines without DIRAS3 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.0, 17.8); signed map (23.4, 45.1). **Vector** length 21.7, 11.2% of its response variance represented; |z| ≥ 3 in 122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.6 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +0.5 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.5 | +8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.5 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +0.5 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.4 | +0.9 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.3 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.3 | +3.6 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | +0.3 | +1.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -0.6 | -0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.5 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.4 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DIRAS family GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:68,045,886-68,051,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOEY2; previously ARHI |
| Gene groups (HGNC) | RAS type GTPase family |
| Matched by | ensembl_id |

UniProt [O95661](https://www.uniprot.org/uniprotkb/O95661) carries no function annotation.

**Summary**, from NCBI Gene [9077](https://www.ncbi.nlm.nih.gov/gene/9077):

> This gene encodes a member of the ras superfamily. This gene is imprinted gene with monoallelic expression of the paternal allele which is associated with growth suppression. The encoded protein acts as a tumor suppressor whose function is abrogated in many ovarian and breast cancers. This protein may also play a role autophagy in certain cancer cells by regulating the autophagosome initiation complex. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:687) · Entrez [9077](https://www.ncbi.nlm.nih.gov/gene/9077) · UniProt [O95661](https://www.uniprot.org/uniprotkb/O95661) · Ensembl [ENSG00000162595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162595)

## Data

Gene col 8536: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8536); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8536, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8536]; `tensor/DDL_lfc|DDL_z.npy` [8536]; `embed/gene_vectors.npy` [8536]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8536 or target_col == 8536). Every well: [[DIRAS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIRAS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
