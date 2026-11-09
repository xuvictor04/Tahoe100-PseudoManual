---
symbol: "RNF17"
type: "gene"
col: 5401
ensembl_id: "ENSG00000132972"
name: "ring finger protein 17"
location: "13q12.12"
module: 177
arm: "+"
pooled_cpm: 3.22
n_lines_expressing: 8
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 21
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# RNF17

*ring finger protein 17* — 13q12.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.19× (z +15.2, q 0e+00, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CFPAC-1 0.244×, SK-MEL-2 0.336×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0584×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.135×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC152]] (+0.69, fdr 2e-05), [[COX7B2]] (+0.65, fdr 1e-05), [[NAA11]] (+0.59, fdr 1e-04); moves opposite to [[ZNF213-AS1]] (-0.39, fdr 0.001, ⚠ not reproduced), [[SELENOF]] (-0.37, fdr 6e-04), [[RNF170]] (-0.36, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NAA11]] → it (grade C ⚠); 21 go from it, the strongest it → [[NYAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.19×** | +15.2 | 0e+00 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.34×** | +11.6 | 1e-28 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +10.3 | 1e-22 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.13×** | +7.7 | 1e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.7 | 3e-04 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +4.7 | 3e-04 | 0/4 | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +4.5 | 5e-04 | 1/3 (HS-578T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.01×** | +4.5 | 5e-04 | 1/5 (hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.55×** | +4.3 | 9e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.1 | 0.002 | 0/3 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.34×** | +3.9 | 0.004 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.78×** | +3.7 | 0.010 | 0/3 | inconsistent across doses | position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.74×** | +3.6 | 0.014 | 0/4 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.85×** | +3.6 | 0.015 | 1/2 (SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.4 | 0.022 | 0/4 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.023 | 0/5 | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.041 | 0/3 | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.042 | 0/3 | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.0 | 0.079 | 0/3 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5401.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (CFPAC-1 0.244×, SK-MEL-2 0.336×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0584×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.135×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.620× | -3.2 | 0.35 | 0/6 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.573× | -3.1 | 0.35 | 0/5 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.580× | -3.0 | 0.35 | 0/6 | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.5 µM |  | 0.635× | -3.0 | 0.35 | 1/6 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 78.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0584× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 51.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -12.9) |
| [[A-172 (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.448 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC152]] | +0.69 | +0.47 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[COX7B2]] | +0.65 | +0.57 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[NAA11]] | +0.59 | +0.35 / +0.63 | both halves | 1e-04 | **novel candidate** |
| [[F11-AS1]] | +0.58 | +0.23 / +0.73 | both halves | 5e-04 | **novel candidate** |
| [[NRG3]] | +0.54 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ANKRD20A8P]] | +0.54 | +0.26 / +0.60 | both halves | 4e-04 |  |
| [[LINC02506]] | +0.51 | +0.24 / +0.51 | both halves | 4e-04 |  |
| [[LINC00383]] | +0.49 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[DHRS2]] | +0.49 | +0.20 / +0.42 | both halves | 7e-04 |  |
| [[ZNF208]] | +0.48 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[FAM230C]] | +0.47 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[LINC01205]] | +0.46 | +0.25 / +0.62 | both halves | 4e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213-AS1]] | -0.39 | -0.25 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[SELENOF]] | -0.37 | -0.22 / -0.24 | both halves | 6e-04 |  |
| [[RNF170]] | -0.36 | -0.22 / -0.17 | ⚠ not reproduced | 0.001 | same gene group |
| [[CCT6B]] | -0.36 | -0.17 / -0.11 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAA11]] | C | NAA11 activity raises RNF17's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.69× lower at baseline in the lines without NAA11 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises RNF17's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 2.58× lower at baseline in the lines without GPR141 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |
| [[NRG3]] | C | NRG3 activity raises RNF17's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 3.16× lower at baseline in the lines without NRG3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises RNF17's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.77× lower at baseline in the lines without F11-AS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[LINC00879]] | C | LINC00879 activity raises RNF17's level | lines that do not express LINC00879 (46) vs lines expressing it (4) | 5.34× lower at baseline in the lines without LINC00879 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, ENSG00000234426, APOB; co-absent with the target; its own permutation p |
| [[CHMP1B2P]] | C | CHMP1B2P activity raises RNF17's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 1.81× lower at baseline in the lines without CHMP1B2P | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises RNF17's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.65× lower at baseline in the lines without MIR3667HG | 0.069 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises RNF17's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 1.55× lower at baseline in the lines without GTSF1 | 0.086 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises RNF17's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 1.58× lower at baseline in the lines without LINC01518 | 0.0999 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 3, C 18. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | RNF17 activity raises NYAP2's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 2.43× lower at baseline in the lines without RNF17 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD |
| [[FMN1]] | B | RNF17 activity raises FMN1's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 2.27× lower at baseline in the lines without RNF17 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD |
| [[KIF20B]] | B | RNF17 activity lowers KIF20B's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 1.52× higher at baseline in the lines without RNF17 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD |
| [[LINC01518]] | C | RNF17 activity raises LINC01518's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.69× lower at baseline in the lines without RNF17 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[MIR3667HG]] | C | RNF17 activity raises MIR3667HG's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 5.47× lower at baseline in the lines without RNF17 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[CCDC152]] | C | RNF17 activity raises CCDC152's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.14× lower at baseline in the lines without RNF17 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[ZNF208]] | C | RNF17 activity raises ZNF208's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.25× lower at baseline in the lines without RNF17 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[LINC01885]] | C | RNF17 activity raises LINC01885's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 5.61× lower at baseline in the lines without RNF17 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[F11-AS1]] | C | RNF17 activity raises F11-AS1's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 4.26× lower at baseline in the lines without RNF17 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[ZMAT4]] | C | RNF17 activity raises ZMAT4's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 4.71× lower at baseline in the lines without RNF17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[LINGO2]] | C | RNF17 activity raises LINGO2's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.93× lower at baseline in the lines without RNF17 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[NAA11]] | C | RNF17 activity raises NAA11's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.93× lower at baseline in the lines without RNF17 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 27.9); signed map (32.8, 38.0). **Vector** length 9.83, 2.20% of its response variance represented; |z| ≥ 3 in 92 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.0 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.7 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.4 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.4 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.4 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.4 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.4 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.4 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.3 | -0.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12 — chr13:24,764,169-24,879,921 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Mmip-2, SPATA23, FLJ11045; previously TDRD4 |
| Gene groups (HGNC) | Ring finger proteins; Tudor domain containing; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXT8](https://www.uniprot.org/uniprotkb/Q9BXT8) (RING finger protein 17):

> Seems to be involved in regulation of transcriptional activity of MYC. In vitro, inhibits DNA-binding activity of Mad-MAX heterodimers. Can recruit Mad transcriptional repressors (MXD1, MXD3, MXD4 and MXI1) to the cytoplasm. May be involved in spermiogenesis (By similarity).

**Summary**, from NCBI Gene [56163](https://www.ncbi.nlm.nih.gov/gene/56163):

> This gene is similar to a mouse gene that encodes a testis-specific protein containing a RING finger domain. Alternatively spliced transcript variants encoding different isoforms have been found. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:10060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10060) · Entrez [56163](https://www.ncbi.nlm.nih.gov/gene/56163) · UniProt [Q9BXT8](https://www.uniprot.org/uniprotkb/Q9BXT8) · Ensembl [ENSG00000132972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132972)

## Data

Gene col 5401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5401); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5401]; `tensor/DDL_lfc|DDL_z.npy` [5401]; `embed/gene_vectors.npy` [5401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5401 or target_col == 5401). Every well: [[RNF17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
