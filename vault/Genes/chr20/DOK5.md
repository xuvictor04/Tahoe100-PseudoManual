---
symbol: "DOK5"
type: "gene"
col: 2075
ensembl_id: "ENSG00000101134"
name: "docking protein 5"
location: "20q13.2"
module: 9
arm: "+"
pooled_cpm: 8.94
n_lines_expressing: 10
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DOK5

*docking protein 5* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.31× (z +11.2, q 4e-26, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +10.1, q 2e-21, up in 2 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Citalopram (hydrobromide) (drug)]] 0.05 µM: 0.586× (z -4.1, q 0.014, down in 5 of 8 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIM1]] (+0.73, fdr 7e-06), [[CDH6]] (+0.72, fdr 7e-06), [[PTGIS]] (+0.72, fdr 7e-06); moves opposite to [[SLC26A2]] (-0.55, fdr 1e-05), [[YAP1]] (-0.50, fdr 2e-05), [[MT1A]] (-0.45, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NRXN1]] → it (grade B ⚠); 8 go from it, the strongest it → [[GRIA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.31×** | +11.2 | 4e-26 | 1/5 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +10.1 | 2e-21 | 2/7 (BT-474, A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +9.2 | 6e-18 | 4/7 (C32, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +8.9 | 8e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +7.7 | 1e-12 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +6.1 | 1e-07 | 3/7 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +6.0 | 2e-07 | 4/7 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +4.2 | 0.002 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +3.9 | 0.006 | 2/7 (C32, A-172) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.012 | 1/7 (BT-474) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.59×** | +3.6 | 0.020 | 2/6 (NCI-H1573, HS-578T) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.5 | 0.021 | 0/5 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.4 | 0.031 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.4 | 0.032 | 0/6 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.033 | 4/7 (SW 900, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.038 | 1/7 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.038 | 1/6 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.038 | 1/7 (SW 900) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.586×** | -4.1 | 0.014 | 5/8 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.588×** | -4.1 | 0.014 | 4/7 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.580×** | -3.8 | 0.022 | 2/7 (A-172, C32) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.749× | -3.1 | 0.23 | 0/8 | top dose only |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.670× | -3.1 | 0.23 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 320 | 0 | 28 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0913× (z -18.1) |
| [[A-172 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIM1]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CDH6]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PTGIS]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SLC14A1]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SOX7]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[GRIA1]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ERG]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[PTPRB]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SPOCK3]] | +0.56 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[ABCA13]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PCDH18]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CDH8]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A2]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[YAP1]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MT1A]] | -0.45 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ARRDC1]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TOP1]] | -0.42 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[HMGA2]] | -0.42 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[KRT5]] | -0.40 | -0.19 / -0.33 | ⚠ not reproduced | 8e-04 |  |
| [[TLR2]] | -0.40 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[MT1F]] | -0.40 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[RPGR]] | -0.40 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LDLRAD3]] | -0.40 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[COPS8]] | -0.39 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN1]] | B | NRXN1 activity raises DOK5's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without NRXN1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[IGFBP5]] | C | IGFBP5 activity raises DOK5's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without IGFBP5 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises DOK5's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 5.30× lower at baseline in the lines without KRT5 | 0.008 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SIM1]] | C | SIM1 activity raises DOK5's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.32× lower at baseline in the lines without SIM1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[SULF1]] | C | SULF1 activity raises DOK5's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.98× lower at baseline in the lines without SULF1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[CDH8]] | C | CDH8 activity raises DOK5's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without CDH8 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIA1]] | B | DOK5 activity raises GRIA1's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.71× lower at baseline in the lines without DOK5 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5 |
| [[IGFBP5]] | C | DOK5 activity raises IGFBP5's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 9.78× lower at baseline in the lines without DOK5 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[ECSCR]] | C | DOK5 activity raises ECSCR's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.93× lower at baseline in the lines without DOK5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[KRT5]] | C | DOK5 activity raises KRT5's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without DOK5 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[SULF1]] | C | DOK5 activity raises SULF1's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 3.49× lower at baseline in the lines without DOK5 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[LGR6]] | C | DOK5 activity raises LGR6's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.21× lower at baseline in the lines without DOK5 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[SIM1]] | C | DOK5 activity raises SIM1's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.32× lower at baseline in the lines without DOK5 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |
| [[MEOX2]] | C | DOK5 activity raises MEOX2's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.51× lower at baseline in the lines without DOK5 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.415). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.6, 20.0); signed map (35.3, 30.3). **Vector** length 34.9, 13.0% of its response variance represented; |z| ≥ 3 in 224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.7 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.8 | +0.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -4.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | docking protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:54,475,593-54,651,169 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ805C22.1; previously C20orf180 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Docking protein family |
| Reactome | 3 pathways, smallest: RET signaling; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P104](https://www.uniprot.org/uniprotkb/Q9P104) (Docking protein 5):

> DOK proteins are enzymatically inert adaptor or scaffolding proteins. They provide a docking platform for the assembly of multimolecular signaling complexes. DOK5 functions in RET-mediated neurite outgrowth and plays a positive role in activation of the MAP kinase pathway. Putative link with downstream effectors of RET in neuronal differentiation.

**Summary**, from NCBI Gene [55816](https://www.ncbi.nlm.nih.gov/gene/55816):

> The protein encoded by this gene is a member of the DOK family of membrane proteins, which are adapter proteins involved in signal transduction. The encoded protein interacts with phosphorylated receptor tyrosine kinases to mediate neurite outgrowth and activation of the MAP kinase pathway. Unlike other DOK family proteins, this protein does not interact with RASGAP. This protein is up-regulated in patients with systemic sclerosis and is associated with fibrosis induced by insulin-like growth …

**Accessions** — [HGNC:16173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16173) · Entrez [55816](https://www.ncbi.nlm.nih.gov/gene/55816) · UniProt [Q9P104](https://www.uniprot.org/uniprotkb/Q9P104) · Ensembl [ENSG00000101134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101134)

## Data

Gene col 2075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2075); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2075]; `tensor/DDL_lfc|DDL_z.npy` [2075]; `embed/gene_vectors.npy` [2075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2075 or target_col == 2075). Every well: [[DOK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
