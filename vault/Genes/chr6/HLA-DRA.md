---
symbol: "HLA-DRA"
type: "gene"
col: 12844
ensembl_id: "ENSG00000204287"
name: "major histocompatibility complex, class II, DR alpha"
location: "6p21.32"
module: 8
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 11
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 27
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HLA-DRA

*major histocompatibility complex, class II, DR alpha* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 11.7× (z +11.8, q 1e-29, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.24× (z +8.0, q 3e-13, up in 7 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 0.209×, SW1417 0.225×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD74]] (+0.78, fdr 7e-06), [[HLA-DRB1]] (+0.71, fdr 7e-06), [[AGT]] (+0.64, fdr 1e-05); moves opposite to [[INO80E]] (-0.50, fdr 5e-05), [[GTF2H3]] (-0.42, fdr 2e-04), [[GTF2A1]] (-0.41, fdr 7e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[AGT]] → it (grade C ⚠); 27 go from it, the strongest it → [[B2M]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **11.7×** | +11.8 | 1e-29 | 3/4 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.2×** | +11.2 | 1e-26 | 2/3 (C32, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.24×** | +8.0 | 3e-13 | 7/8 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.37×** | +7.5 | 1e-11 | 3/3 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +5.9 | 5e-07 | 1/4 (C32) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +5.8 | 6e-07 | 4/6 (CFPAC-1, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.83×** | +4.8 | 1e-04 | 2/4 (C32, CFPAC-1) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.57×** | +4.5 | 4e-04 | 4/6 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.012 | 0/8 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +3.6 | 0.017 | 2/6 (C32, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.17×** | +3.6 | 0.017 | 1/3 (C32) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +3.6 | 0.017 | 2/4 (CFPAC-1, C32) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.74×** | +3.5 | 0.024 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.4 | 0.025 | 1/5 (C32) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.3 | 0.037 | 0/5 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.43×** | +3.0 | 0.076 | 3/4 (SW1417, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12844.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 0.209×, SW1417 0.225×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.478× | -3.3 | 0.41 | 1/8 (hTERT-HPNE) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.493× | -3.2 | 0.41 | 1/8 (C32) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.303 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD74]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[HLA-DRB1]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 999 |
| [[AGT]] | +0.64 | +0.50 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[STEAP4]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LRG1]] | +0.58 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[LCN2]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[PLAAT4]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[C4orf19]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[LYPD5]] | +0.52 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[APOE]] | +0.51 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[CST3]] | +0.51 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[SAA4]] | +0.50 | +0.40 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80E]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[GTF2H3]] | -0.42 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[GTF2A1]] | -0.41 | -0.42 / -0.21 | both halves | 7e-04 |  |
| [[ZNF696]] | -0.40 | -0.36 / -0.24 | both halves | 5e-04 |  |
| [[ZNF23]] | -0.39 | -0.33 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[CCT6P3]] | -0.39 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[GAS8]] | -0.39 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[SLC9A3R2]] | -0.39 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGT]] | C | AGT activity raises HLA-DRA's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.64× lower at baseline in the lines without AGT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises HLA-DRA's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 3.74× lower at baseline in the lines without HLA-DRB1 | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |
| [[APOA1]] | C | APOA1 activity raises HLA-DRA's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 1.68× lower at baseline in the lines without APOA1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB; co-absent with the target |
| [[CD74]] | C | CD74 activity raises HLA-DRA's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without CD74 | 0.020 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises HLA-DRA's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.16× lower at baseline in the lines without STEAP4 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises HLA-DRA's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.16× lower at baseline in the lines without WFDC2 | 0.027 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[FGG]] | C | FGG activity raises HLA-DRA's level | lines that do not express FGG (42) vs lines expressing it (8) | 1.63× lower at baseline in the lines without FGG | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[CFI]] | C | CFI activity raises HLA-DRA's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without CFI | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[FGB]] | C | FGB activity raises HLA-DRA's level | lines that do not express FGB (42) vs lines expressing it (8) | 1.77× lower at baseline in the lines without FGB | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[FGA]] | C | FGA activity raises HLA-DRA's level | lines that do not express FGA (43) vs lines expressing it (7) | 2.00× lower at baseline in the lines without FGA | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[SPINK1]] | C | SPINK1 activity raises HLA-DRA's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without SPINK1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3; co-absent with the target |
| [[IDO1]] | C | IDO1 activity raises HLA-DRA's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without IDO1 | 0.086 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 12, C 15. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B2M]] | B | HLA-DRA activity raises B2M's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without HLA-DRA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[BCL2L15]] | B | HLA-DRA activity raises BCL2L15's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without HLA-DRA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[CST3]] | B | HLA-DRA activity raises CST3's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.87× lower at baseline in the lines without HLA-DRA | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[SEC16B]] | B | HLA-DRA activity raises SEC16B's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without HLA-DRA | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[RASGEF1B]] | B | HLA-DRA activity raises RASGEF1B's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.88× lower at baseline in the lines without HLA-DRA | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[SLC7A7]] | B | HLA-DRA activity raises SLC7A7's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.40× lower at baseline in the lines without HLA-DRA | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[SGMS1]] | B | HLA-DRA activity weakens SGMS1's drug response | lines that do not express HLA-DRA (39) vs lines expressing it (10) | the lines without HLA-DRA respond 1.26× as strongly (z diff -0.55); strongest at Dinaciclib 0.5 µM: 0.41x vs 0.77x (z diff -4.5) | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; target measured in part of the lines; both ways; artifact flags |
| [[LGALS3BP]] | B | HLA-DRA activity raises LGALS3BP's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.04× lower at baseline in the lines without HLA-DRA | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[SELENOP]] | B | HLA-DRA activity raises SELENOP's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.35× lower at baseline in the lines without HLA-DRA | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[EGFL7]] | B | HLA-DRA activity lowers EGFL7's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.55× higher at baseline in the lines without HLA-DRA | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[CFB]] | B | HLA-DRA activity raises CFB's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.84× lower at baseline in the lines without HLA-DRA | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[C4orf19]] | B | HLA-DRA activity raises C4orf19's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.95× lower at baseline in the lines without HLA-DRA | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.2, 54.9); signed map (61.4, -2.8). **Vector** length 17.6, 4.37% of its response variance represented; |z| ≥ 3 in 158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -0.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.6 | -1.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.5 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.4 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class II, DR alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,439,878-32,445,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HLA-DRA1 |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 15 pathways, smallest: Translocation of ZAP-70 to Immunological synapse; Phosphorylation of CD3 and TCR zeta chains; Generation of second messenger molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P01903](https://www.uniprot.org/uniprotkb/P01903) (HLA class II histocompatibility antigen, DR alpha chain):

> An alpha chain of antigen-presenting major histocompatibility complex class II (MHCII) molecule. In complex with the beta chain HLA-DRB, displays antigenic peptides on professional antigen presenting cells (APCs) for recognition by alpha-beta T cell receptor (TCR) on HLA-DR-restricted CD4-positive T cells. This guides antigen-specific T-helper effector functions, both antibody-mediated immune response and macrophage activation, to ultimately eliminate the infectious agents and transformed …

**Summary**, from NCBI Gene [3122](https://www.ncbi.nlm.nih.gov/gene/3122):

> HLA-DRA is one of the HLA class II alpha chain paralogues. This class II molecule is a heterodimer consisting of an alpha and a beta chain, both anchored in the membrane. This molecule is expressed on the surface of various antigen presenting cells such as B lymphocytes, dendritic cells, and monocytes/macrophages, and plays a central role in the immune system and response by presenting peptides derived from extracellular proteins, in particular, pathogen-derived peptides to T cells. The alpha …

**Accessions** — [HGNC:4947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4947) · Entrez [3122](https://www.ncbi.nlm.nih.gov/gene/3122) · UniProt [P01903](https://www.uniprot.org/uniprotkb/P01903) · Ensembl [ENSG00000204287](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204287)

## Data

Gene col 12844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12844); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12844]; `tensor/DDL_lfc|DDL_z.npy` [12844]; `embed/gene_vectors.npy` [12844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12844 or target_col == 12844). Every well: [[HLA-DRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-DRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
