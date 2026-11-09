---
symbol: "ANKRD30A"
type: "gene"
col: 7293
ensembl_id: "ENSG00000148513"
name: "ankyrin repeat domain 30A"
location: "10p11.21"
module: 108
arm: "+"
pooled_cpm: 3.01
n_lines_expressing: 13
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# ANKRD30A

*ankyrin repeat domain 30A* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.43× (z +12.8, q 8e-35, up in 3 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00993]] (+0.91, fdr 7e-06, ⚠ same locus), [[TENM2]] (+0.61, fdr 1e-05), [[MGAT4C]] (+0.58, fdr 1e-05), [[LINC02267]] (+0.56, fdr 1e-05); moves opposite to [[CES1]] (-0.51, fdr 3e-05), [[CD68]] (-0.50, fdr 3e-05), [[GSDMC]] (-0.47, fdr 1e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CLMN]] → it (grade B ⚠); 9 go from it, the strongest it → [[MAP3K7CL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.43×** | +12.8 | 8e-35 | 3/4 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.49×** | +10.8 | 1e-24 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.48×** | +9.4 | 8e-19 | 2/4 (BT-474, A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.26×** | +8.5 | 2e-15 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +6.1 | 1e-07 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +5.2 | 2e-05 | 2/4 (NCI-H661, A549) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +4.5 | 5e-04 | 2/5 (BT-474, NCI-H661) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +4.4 | 8e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.05×** | +4.3 | 0.001 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.020 | 0/7 | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.020 | 1/8 (LOX-IMVI) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.061 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.82×** | +3.2 | 0.061 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.065 | 1/7 (NCI-H1792) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7293.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.842× | -3.4 | 0.41 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.534 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00993]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | ⚠ same locus (15.6 kb, same strand: neighbours can correlate without regulation) |
| [[TENM2]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[MGAT4C]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[LINC02267]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NOL4]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[MIR3171HG]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[LINC02211]] | +0.52 | +0.46 / +0.43 | both halves | 4e-05 |  |
| [[NETO1]] | +0.52 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[KCNH5]] | +0.51 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[MAPK10]] | +0.50 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[PGR]] | +0.49 | +0.29 / +0.60 | both halves | 2e-04 |  |
| [[PRKG1]] | +0.49 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[MSC-AS1]] | +0.49 | +0.39 / +0.43 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CES1]] | -0.51 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CD68]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GSDMC]] | -0.47 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[S100A9]] | -0.46 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[SERPINA1]] | -0.45 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[BEAN1]] | -0.42 | -0.46 / -0.32 | both halves | 1e-04 |  |
| [[SERPINB4]] | -0.42 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[FAM3C]] | -0.41 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[LINC01440]] | -0.40 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[SERPINA3]] | -0.40 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[CLMN]] | -0.39 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[SERPINB3]] | -0.39 | -0.26 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLMN]] | B | CLMN activity lowers ANKRD30A's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.58× higher at baseline in the lines without CLMN | 0.015 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[TBC1D8]] | B | TBC1D8 activity lowers ANKRD30A's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.41× higher at baseline in the lines without TBC1D8 | 0.017 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[LINC00993]] | C | LINC00993 activity raises ANKRD30A's level | lines that do not express LINC00993 (35) vs lines expressing it (15) | 3.92× lower at baseline in the lines without LINC00993 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANKRD30A, KCNH5, KCNB2; maybe low, not absent; co-absent with the target |
| [[ROBO2]] | C | ROBO2 activity raises ANKRD30A's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.70× lower at baseline in the lines without ROBO2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises ANKRD30A's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 2.43× lower at baseline in the lines without MIR99AHG | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises ANKRD30A's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.41× lower at baseline in the lines without BRINP3 | 0.093 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises ANKRD30A's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 3.29× lower at baseline in the lines without FUT9 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises ANKRD30A's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.45× lower at baseline in the lines without KCNH5 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K7CL]] | B | ANKRD30A activity strengthens MAP3K7CL's drug response | lines that do not express ANKRD30A (27) vs lines expressing it (9) | the lines without ANKRD30A respond 1.09× as strongly (z diff +0.32); strongest at Digitoxin 0.5 µM: 0.56x vs 0.28x (z diff +3.5) | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; target measured in part of the lines; both ways; artifact flags |
| [[MAPK10]] | B | ANKRD30A activity raises MAPK10's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.03× lower at baseline in the lines without ANKRD30A | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1 |
| [[LINC00993]] | C | ANKRD30A activity raises LINC00993's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.78× lower at baseline in the lines without ANKRD30A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[LINC02377]] | C | ANKRD30A activity raises LINC02377's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.70× lower at baseline in the lines without ANKRD30A | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[ZFHX4-AS1]] | C | ANKRD30A activity raises ZFHX4-AS1's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 2.52× lower at baseline in the lines without ANKRD30A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[ERBB4]] | C | ANKRD30A activity raises ERBB4's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without ANKRD30A | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[NETO1]] | C | ANKRD30A activity raises NETO1's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.59× lower at baseline in the lines without ANKRD30A | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[IGSF1]] | C | ANKRD30A activity raises IGSF1's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.80× lower at baseline in the lines without ANKRD30A | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |
| [[FUT9]] | C | ANKRD30A activity raises FUT9's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.45× lower at baseline in the lines without ANKRD30A | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.1, 22.7); signed map (35.1, 43.2). **Vector** length 20.7, 5.70% of its response variance represented; |z| ≥ 3 in 159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +1.1 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.7 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.6 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.4 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.4 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -0.4 | +2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.4 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 30A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.21 — chr10:37,125,598-37,232,567 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-BR-1 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [Q9BXX3](https://www.uniprot.org/uniprotkb/Q9BXX3) carries no function annotation.

**Summary**, from NCBI Gene [91074](https://www.ncbi.nlm.nih.gov/gene/91074):

> This gene encodes a DNA-binding transcription factor that is uniquely expressed in mammary epithelium and the testis. Altered expression levels have been associated with breast cancer progression. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:17234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17234) · Entrez [91074](https://www.ncbi.nlm.nih.gov/gene/91074) · UniProt [Q9BXX3](https://www.uniprot.org/uniprotkb/Q9BXX3) · Ensembl [ENSG00000148513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148513)

## Data

Gene col 7293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7293); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7293]; `tensor/DDL_lfc|DDL_z.npy` [7293]; `embed/gene_vectors.npy` [7293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7293 or target_col == 7293). Every well: [[ANKRD30A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD30A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
