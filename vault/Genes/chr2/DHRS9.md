---
symbol: "DHRS9"
type: "gene"
col: 1058
ensembl_id: "ENSG00000073737"
name: "dehydrogenase/reductase 9"
location: "2q31.1"
module: 34
arm: "+"
pooled_cpm: 25.28
n_lines_expressing: 10
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 27
direction_downstream: 47
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# DHRS9

*dehydrogenase/reductase 9* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.54× (z +9.4, q 2e-18, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +5.6, q 2e-06, up in 3 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.561× (z -3.9, q 0.026, down in 6 of 7 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMC2]] (+0.70, fdr 7e-06), [[C6orf141]] (+0.67, fdr 7e-06), [[TMC7]] (+0.66, fdr 7e-06); moves opposite to [[MGC32805]] (-0.47, fdr 1e-04), [[RARRES1]] (-0.43, fdr 9e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[TMCC3]] → it (grade B ⚠); 47 go from it, the strongest it → [[TMC7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.54×** | +9.4 | 2e-18 | 3/5 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +8.7 | 1e-15 | 0/8 | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.70×** | +6.1 | 2e-07 | 4/4 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +5.8 | 7e-07 | 0/4 | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +5.6 | 2e-06 | 3/8 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.18×** | +5.3 | 1e-05 | 5/7 (NCI-H1573, AsPC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.98×** | +4.6 | 4e-04 | 5/7 (NCI-H1573, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.86×** | +4.2 | 0.002 | 7/7 (NCI-H1573, AsPC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.007 | 6/7 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.8 | 0.008 | 3/7 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.79×** | +3.8 | 0.008 | 5/7 (LS 180, CFPAC-1, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.72×** | +3.7 | 0.012 | 3/7 (LS 180, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.70×** | +3.6 | 0.015 | 5/7 (NCI-H1573, CFPAC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.73×** | +3.5 | 0.020 | 4/7 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.561×** | -3.9 | 0.026 | 6/7 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.545×** | -3.8 | 0.026 | 5/7 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.342×** | -3.8 | 0.026 | 4/8 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.026 | 4/8 (AsPC-1, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | 0.622× | -3.2 | 0.13 | 7/7 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.601× | -3.2 | 0.13 | 3/7 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.652× | -3.2 | 0.13 | 4/8 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.613× | -3.1 | 0.13 | 1/8 (KATO III) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 20.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 16.6× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 99.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 8.39 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 19.0× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 861 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMC2]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[C6orf141]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TMC7]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KLK11]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[FERMT1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[DENND2C]] | +0.62 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[PLEK2]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SERPINB5]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[S100A16]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[GJB3]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ATG9B]] | +0.59 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[PEAR1]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGC32805]] | -0.47 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[RARRES1]] | -0.43 | -0.37 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 2, C 25. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC3]] | B | TMCC3 activity raises DHRS9's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without TMCC3 | 0.071 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[LYPD3]] | B | LYPD3 activity raises DHRS9's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.09× lower at baseline in the lines without LYPD3 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[KLK10]] | C | KLK10 activity raises DHRS9's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without KLK10 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises DHRS9's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without SERPINB5 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[LINC01610]] | C | LINC01610 activity raises DHRS9's level | lines that do not express LINC01610 (45) vs lines expressing it (5) | 6.98× lower at baseline in the lines without LINC01610 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC00879, LINC02099; co-absent with the target |
| [[DSG3]] | C | DSG3 activity raises DHRS9's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.66× lower at baseline in the lines without DSG3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises DHRS9's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 4.62× lower at baseline in the lines without LINC02582 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[KLK11]] | C | KLK11 activity raises DHRS9's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 4.31× lower at baseline in the lines without KLK11 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises DHRS9's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 4.53× lower at baseline in the lines without TFF2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises DHRS9's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.79× lower at baseline in the lines without HS3ST1 | 0.033 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises DHRS9's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.17× lower at baseline in the lines without SLC14A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[SCEL]] | C | SCEL activity raises DHRS9's level | lines that do not express SCEL (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without SCEL | 0.036 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 18, C 29. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC7]] | B | DHRS9 activity raises TMC7's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.85× lower at baseline in the lines without DHRS9 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[LYPD3]] | B | DHRS9 activity raises LYPD3's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.40× lower at baseline in the lines without DHRS9 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[PLEK2]] | B | DHRS9 activity raises PLEK2's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 4.41× lower at baseline in the lines without DHRS9 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[KPNA7]] | B | DHRS9 activity raises KPNA7's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.62× lower at baseline in the lines without DHRS9 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[LANCL3]] | B | DHRS9 activity raises LANCL3's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.48× lower at baseline in the lines without DHRS9 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[GRB10]] | B | DHRS9 activity raises GRB10's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 3.32× lower at baseline in the lines without DHRS9 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[PLEKHM1P1]] | B | DHRS9 activity raises PLEKHM1P1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 1.56× lower at baseline in the lines without DHRS9 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | DHRS9 activity strengthens ARHGAP27P1-BPTFP1-KPNA2P3's drug response | lines that do not express DHRS9 (40) vs lines expressing it (8) | the lines without DHRS9 respond 0.48× as strongly (z diff +2.54); strongest at Harringtonine 5 µM: 0.73x vs 0.32x (z diff +4.4) | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; target measured in part of the lines; artifact flags |
| [[PLEKHM1]] | B | DHRS9 activity raises PLEKHM1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 1.58× lower at baseline in the lines without DHRS9 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[SDC1]] | B | DHRS9 activity raises SDC1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.53× lower at baseline in the lines without DHRS9 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[PLEKHM1P1]] | B | DHRS9 activity strengthens PLEKHM1P1's drug response | lines that do not express DHRS9 (40) vs lines expressing it (8) | the lines without DHRS9 respond 0.59× as strongly (z diff +2.05); strongest at Idarubicin (hydrochloride) 5 µM: 0.78x vs 0.45x (z diff +4.5) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; target measured in part of the lines; artifact flags |
| [[TMCC3]] | B | DHRS9 activity raises TMCC3's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 3.46× lower at baseline in the lines without DHRS9 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, 54.2); signed map (1.7, 39.7). **Vector** length 46.7, 23.2% of its response variance represented; |z| ≥ 3 in 265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -0.7 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,064,789-169,096,167 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RDHL, 3alpha-HSD, RETSDR8, RDH15, SDR9C4 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 6 pathways, smallest: The canonical retinoid cycle in rods (twilight vision); RA biosynthesis pathway; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPW9](https://www.uniprot.org/uniprotkb/Q9BPW9) (Dehydrogenase/reductase SDR family member 9):

> 3-alpha-hydroxysteroid dehydrogenase that converts 3-alpha-tetrahydroprogesterone (allopregnanolone) to dihydroxyprogesterone and 3-alpha-androstanediol to dihydroxyprogesterone. Also plays a role in the biosynthesis of retinoic acid from retinaldehyde. Can utilize both NADH and NADPH.

**Summary**, from NCBI Gene [10170](https://www.ncbi.nlm.nih.gov/gene/10170):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. This protein demonstrates oxidoreductase activity toward hydroxysteroids and is able to convert 3-alpha-tetrahydroprogesterone to dihydroxyprogesterone and 3-alpha-androstanediol to dihydroxyprogesterone in the cytoplasm, and may additionally function as a transcriptional …

**Accessions** — [HGNC:16888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16888) · Entrez [10170](https://www.ncbi.nlm.nih.gov/gene/10170) · UniProt [Q9BPW9](https://www.uniprot.org/uniprotkb/Q9BPW9) · Ensembl [ENSG00000073737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073737)

## Data

Gene col 1058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1058); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1058]; `tensor/DDL_lfc|DDL_z.npy` [1058]; `embed/gene_vectors.npy` [1058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1058 or target_col == 1058). Every well: [[DHRS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
