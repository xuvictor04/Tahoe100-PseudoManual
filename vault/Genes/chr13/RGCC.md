---
symbol: "RGCC"
type: "gene"
col: 2268
ensembl_id: "ENSG00000102760"
name: "regulator of cell cycle"
location: "13q14.11"
module: 27
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# RGCC

*regulator of cell cycle* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.05× (z +13.8, q 8e-41, up in 12 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (SW1417 0.0827×, SW480 0.222×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW1417 0.263×, SW480 0.324×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.149×); [[c-Kit-IN-1 (drug)]] 5 µM in 1 line (SW1417 0.0325×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.201×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHACTR3]] (+0.58, fdr 1e-05), [[PELI2]] (+0.53, fdr 2e-05), [[OVOL2]] (+0.53, fdr 3e-05); moves opposite to [[IBTK]] (-0.42, fdr 9e-05), [[ZDHHC6]] (-0.41, fdr 1e-04), [[VPS33B]] (-0.40, fdr 4e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TRPV4]] → it (grade B ⚠); 6 go from it, the strongest it → [[MAN1A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.05×** | +13.8 | 8e-41 | 12/18 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.38×** | +9.9 | 9e-21 | 2/5 (CFPAC-1, SW1417) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.38×** | +9.6 | 2e-19 | 4/7 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +9.2 | 3e-18 | 2/12 (CFPAC-1, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +6.2 | 5e-08 | 8/14 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +6.0 | 2e-07 | 10/22 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.59×** | +4.6 | 3e-04 | 6/18 (CFPAC-1, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.48×** | +4.5 | 4e-04 | 4/10 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.002 | 4/22 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +4.2 | 0.002 | 6/19 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.6 | 0.015 | 1/12 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.96×** | +3.4 | 0.038 | 2/14 (SW480, SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.043 | 10/18 (Panc 03.27, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.056 | 4/18 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.1 | 0.068 | 5/15 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.53×** | +3.0 | 0.090 | 10/23 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2268.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (SW1417 0.0827×, SW480 0.222×; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW1417 0.263×, SW480 0.324×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.149×); [[c-Kit-IN-1 (drug)]] 5 µM in 1 line (SW1417 0.0325×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.201×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.613× | -3.4 | 0.37 | 5/22 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 31.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -11.4) |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0827× (z -15.3) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0325× (z -11.0) |
| [[LoVo (line)]] | wt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +9.5) | — |
| [[A-172 (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHACTR3]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[PELI2]] | +0.53 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[OVOL2]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[B3GAT1-DT]] | +0.52 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PDK4-AS1]] | +0.51 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[TMEM139]] | +0.51 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[APCDD1]] | +0.50 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[IGFL2-AS1]] | +0.50 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[F5]] | +0.50 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[AXIN2]] | +0.49 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[FOXQ1]] | +0.49 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[DIP2C-AS1]] | +0.49 | +0.34 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IBTK]] | -0.42 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[ZDHHC6]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[VPS33B]] | -0.40 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[KCTD10]] | -0.39 | -0.34 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPV4]] | B | TRPV4 activity raises RGCC's level | lines that do not express TRPV4 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without TRPV4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SHROOM4, IRAG2, ADAMTS4; maybe low, not absent |
| [[JAKMIP2-AS1]] | B | JAKMIP2-AS1 activity raises RGCC's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.58× lower at baseline in the lines without JAKMIP2-AS1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[MAN1A1]] | B | MAN1A1 activity raises RGCC's level | lines that do not express MAN1A1 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without MAN1A1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BDKRB2, TMEM200A, EVA1A |
| [[SLC40A1]] | C | SLC40A1 activity raises RGCC's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.66× lower at baseline in the lines without SLC40A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3; co-absent with the target |
| [[BMP4]] | C | BMP4 activity raises RGCC's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without BMP4 | 0.013 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises RGCC's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.63× lower at baseline in the lines without KRT23 | 0.062 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[IGFL2-AS1]] | C | IGFL2-AS1 activity raises RGCC's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.28× lower at baseline in the lines without IGFL2-AS1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559; co-absent with the target |
| [[TMEM139]] | C | TMEM139 activity raises RGCC's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without TMEM139 | 0.078 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[TRIM29]] | C | TRIM29 activity raises RGCC's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without TRIM29 | 0.079 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises RGCC's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 2.37× lower at baseline in the lines without VWA2 | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises RGCC's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.86× lower at baseline in the lines without CLRN3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAN1A1]] | B | RGCC activity raises MAN1A1's level | lines that do not express RGCC (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without RGCC | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5 |
| [[LINC00511]] | B | RGCC activity raises LINC00511's level | lines that do not express RGCC (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without RGCC | 0.035 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5 |
| [[ARID5B]] | B | RGCC activity raises ARID5B's level | lines that do not express RGCC (25) vs lines expressing it (25) | 1.25× lower at baseline in the lines without RGCC | 0.049 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5 |
| [[SLC40A1]] | C | RGCC activity raises SLC40A1's level | lines that do not express RGCC (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without RGCC | 0.016 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5; co-absent with the target |
| [[KCNE3]] | C | RGCC activity raises KCNE3's level | lines that do not express RGCC (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without RGCC | 0.052 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5; co-absent with the target |
| [[FOXQ1]] | C | RGCC activity raises FOXQ1's level | lines that do not express RGCC (25) vs lines expressing it (25) | 3.25× lower at baseline in the lines without RGCC | 0.063 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.0, 43.4); signed map (60.1, 15.3). **Vector** length 46.2, 10.6% of its response variance represented; |z| ≥ 3 in 475 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +9.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | +0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | regulator of cell cycle |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,457,550-41,470,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA157L14.2, RGC-32, RGC32; previously C13orf15 |
| Reactome | 3 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; TP53 Regulates Transcription of Cell Cycle Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4X1](https://www.uniprot.org/uniprotkb/Q9H4X1) (Regulator of cell cycle RGCC):

> Modulates the activity of cell cycle-specific kinases. Enhances CDK1 activity. May contribute to the regulation of the cell cycle. May inhibit growth of glioma cells by promoting arrest of mitotic progression at the G2/M transition. Fibrogenic factor contributing to the pathogenesis of renal fibrosis through fibroblast activation.

**Summary**, from NCBI Gene [28984](https://www.ncbi.nlm.nih.gov/gene/28984):

> This gene is thought to regulate cell cycle progression. It is induced by p53 in response to DNA damage, or by sublytic levels of complement system proteins that result in activation of the cell cycle. The encoded protein localizes to the cytoplasm during interphase and to centrosomes during mitosis. The protein forms a complex with polo-like kinase 1. The protein also translocates to the nucleus in response to treatment with complement system proteins, and can associate with and increase the …

**Accessions** — [HGNC:20369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20369) · Entrez [28984](https://www.ncbi.nlm.nih.gov/gene/28984) · UniProt [Q9H4X1](https://www.uniprot.org/uniprotkb/Q9H4X1) · Ensembl [ENSG00000102760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102760)

## Data

Gene col 2268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2268); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2268]; `tensor/DDL_lfc|DDL_z.npy` [2268]; `embed/gene_vectors.npy` [2268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2268 or target_col == 2268). Every well: [[RGCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
