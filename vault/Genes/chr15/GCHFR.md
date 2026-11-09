---
symbol: "GCHFR"
type: "gene"
col: 6092
ensembl_id: "ENSG00000137880"
name: "GTP cyclohydrolase I feedback regulator"
location: "15q15.1"
module: 58
arm: "+"
pooled_cpm: 5.14
n_lines_expressing: 37
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# GCHFR

*GTP cyclohydrolase I feedback regulator* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.21× (z +7.5, q 3e-11, up in 17 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +3.4, q 0.049, up in 11 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.339× (z -5.9, q 2e-06, down in 20 of 28 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSTD1]] (+0.72, fdr 7e-06), [[NUDT8]] (+0.70, fdr 1e-05), [[NME3]] (+0.66, fdr 2e-05); moves opposite to [[LTO1]] (-0.59, fdr 6e-05), [[DVL3]] (-0.55, fdr 1e-04), [[PCBD2]] (-0.54, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CRIP1]] → it (grade B ⚠); 7 go from it, the strongest it → [[VWA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **4.21×** | +7.5 | 3e-11 | 17/20 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.85×** | +7.1 | 4e-10 | 8/9 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.31×** | +4.6 | 8e-04 | 19/34 (KATO III, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **2.02×** | +3.9 | 0.016 | 13/22 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.08×** | +3.7 | 0.022 | 8/11 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.57×** | +3.5 | 0.045 | 14/34 (LoVo, HCT15, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.049 | 11/34 (LS 180, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.339×** | -5.9 | 2e-06 | 20/28 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.401×** | -5.0 | 2e-04 | 23/34 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.526×** | -4.9 | 2e-04 | 21/29 (NCI-H2030, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.418×** | -4.4 | 0.002 | 23/32 (HT-29, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.453×** | -4.3 | 0.002 | 20/34 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.457×** | -4.3 | 0.002 | 21/35 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.484×** | -3.9 | 0.007 | 18/33 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.232×** | -3.8 | 0.012 | 18/30 (HT-29, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.552×** | -3.2 | 0.081 | 16/34 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.303× | -3.1 | 0.12 | 12/27 (PANC-1, J82, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.43 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.3) |
| [[A-427 (line)]] | wt | 4.14 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0509× (z -8.7) |
| [[HT-29 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0807× (z -8.6) |
| [[A-172 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 9 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSTD1]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NUDT8]] | +0.70 | +0.53 / +0.68 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[NME3]] | +0.66 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TNNI3]] | +0.64 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CYBA]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TMEM191A-1]] | +0.63 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[RNF24]] | +0.61 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[TMEM256]] | +0.61 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZDHHC12]] | +0.61 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[IGFBP2]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[VWA1]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[DPM3]] | +0.60 | +0.40 / +0.62 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTO1]] | -0.59 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[DVL3]] | -0.55 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PCBD2]] | -0.54 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[GLIPR1-AS1]] | -0.54 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[DESI1]] | -0.53 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[MAPKAPK5]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[AVEN]] | -0.53 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ACYP2]] | -0.53 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[DPH5-DT]] | -0.52 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[RNF6]] | -0.52 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[FLII]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[PSME3IP1]] | -0.51 | -0.26 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRIP1]] | B | CRIP1 activity raises GCHFR's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without CRIP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[VWA1]] | B | VWA1 activity raises GCHFR's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 2.17× lower at baseline in the lines without VWA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GCHFR's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCMAP]] | B | NCMAP activity raises GCHFR's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without NCMAP | 0.073 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises GCHFR's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ATAD3C]] | C | ATAD3C activity raises GCHFR's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.49× lower at baseline in the lines without ATAD3C | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWA1]] | B | GCHFR activity raises VWA1's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 2.70× lower at baseline in the lines without GCHFR | 0.023 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[TUBG2]] | B | GCHFR activity lowers TUBG2's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 1.61× higher at baseline in the lines without GCHFR | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[DNAJA4]] | B | GCHFR activity raises DNAJA4's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without GCHFR | 0.068 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[CRIP1]] | B | GCHFR activity raises CRIP1's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 3.34× lower at baseline in the lines without GCHFR | 0.068 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[FLII]] | B | GCHFR activity lowers FLII's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 1.18× higher at baseline in the lines without GCHFR | 0.099 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[ATAD3C]] | C | GCHFR activity raises ATAD3C's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without GCHFR | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent; co-absent with the target |
| [[TSTD1]] | C | GCHFR activity raises TSTD1's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without GCHFR | 0.024 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.3, -17.1); signed map (-31.8, 5.9). **Vector** length 57.0, 13.2% of its response variance represented; |z| ≥ 3 in 595 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.3 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | GTP cyclohydrolase I feedback regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,764,068-40,767,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GFRP, HsT16933 |
| Reactome | 3 pathways, smallest: Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P30047](https://www.uniprot.org/uniprotkb/P30047) (GTP cyclohydrolase 1 feedback regulatory protein):

> Mediates tetrahydrobiopterin inhibition of GTP cyclohydrolase 1. This inhibition is reversed by L-phenylalanine.

**Summary**, from NCBI Gene [2644](https://www.ncbi.nlm.nih.gov/gene/2644):

> GTP cyclohydrolase I feedback regulatory protein binds to and mediates tetrahydrobiopterin inhibition of GTP cyclohydrolase I. The regulatory protein, GCHFR, consists of a homodimer. It is postulated that GCHFR may play a role in regulating phenylalanine metabolism in the liver and in the production of biogenic amine neurotransmitters and nitric oxide. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4194) · Entrez [2644](https://www.ncbi.nlm.nih.gov/gene/2644) · UniProt [P30047](https://www.uniprot.org/uniprotkb/P30047) · Ensembl [ENSG00000137880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137880)

## Data

Gene col 6092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6092); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6092]; `tensor/DDL_lfc|DDL_z.npy` [6092]; `embed/gene_vectors.npy` [6092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6092 or target_col == 6092). Every well: [[GCHFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCHFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
