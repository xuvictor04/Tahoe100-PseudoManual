---
symbol: "SFTPA2"
type: "gene"
col: 11657
ensembl_id: "ENSG00000185303"
name: "surfactant protein A2"
location: "10q22.3"
module: 8
arm: "+"
pooled_cpm: 2.53
n_lines_expressing: 4
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 23
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SFTPA2

*surfactant protein A2* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 10.7× (z +8.7, q 1e-15, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.56× (z +5.1, q 6e-05, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.115×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WFDC2]] (+0.52, fdr 2e-04), [[MMP7]] (+0.50, fdr 4e-05), [[GABRP]] (+0.50, fdr 7e-05); moves opposite to [[IFT88]] (-0.46, fdr 1e-04), [[EIF3J]] (-0.46, fdr 1e-04), [[NT5C]] (-0.43, fdr 7e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[SLC44A4]] → it (grade C ⚠); 23 go from it, the strongest it → [[MUC4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.7×** | +8.7 | 1e-15 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.69×** | +8.3 | 3e-14 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.87×** | +7.3 | 5e-11 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.56×** | +5.1 | 6e-05 | 0/2 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +4.9 | 1e-04 | 0/1 | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.64×** | +4.7 | 2e-04 | 0/1 | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.42×** | +4.7 | 2e-04 | 1/1 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **5.47×** | +4.6 | 2e-04 | 1/1 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.23×** | +4.5 | 5e-04 | 0/1 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.36×** | +4.5 | 5e-04 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +3.8 | 0.007 | 0/1 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.61×** | +3.7 | 0.012 | 0/1 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +3.6 | 0.012 | 0/1 | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +3.6 | 0.013 | 1/1 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.93×** | +3.5 | 0.015 | 0/1 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.18×** | +3.0 | 0.095 | 0/1 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11657.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.407× | -3.5 | 0.23 | 0/1 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.422× | -3.4 | 0.23 | 0/1 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 67.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -12.4) |
| [[A-172 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.113 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.140 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.162 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.156 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.144 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.145 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.124 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.126 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.115 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.128 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.142 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.124 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.133 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.139 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WFDC2]] | +0.52 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[MMP7]] | +0.50 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[GABRP]] | +0.50 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[EOLA2]] | +0.49 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[JAK3]] | +0.49 | +0.33 / +0.21 | both halves | 6e-04 |  |
| [[SLC34A2]] | +0.49 | +0.41 / +0.36 | both halves | 9e-05 | pathway: Diseases associated with surfactant metabolism; STRING 491 |
| [[SFTA3-1]] | +0.49 | +0.37 / +0.42 | both halves | 8e-05 |  |
| [[SAR1A]] | +0.48 | +0.45 / +0.31 | both halves | 2e-04 |  |
| [[MUC4]] | +0.48 | +0.35 / +0.50 | both halves | 1e-04 | pathway: Diseases of metabolism |
| [[LGALS3BP]] | +0.48 | +0.30 / +0.40 | both halves | 2e-04 |  |
| [[MUC16]] | +0.47 | +0.35 / +0.46 | both halves | 1e-04 | pathway: Diseases of metabolism |
| [[ANKRD30BL]] | +0.46 | +0.39 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT88]] | -0.46 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[EIF3J]] | -0.46 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[NT5C]] | -0.43 | -0.41 / -0.20 | both halves | 7e-04 |  |
| [[ADGRE5]] | -0.42 | -0.41 / -0.20 | both halves | 7e-04 |  |
| [[SHLD2]] | -0.42 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[KCNK5]] | -0.42 | -0.41 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[MTMR9]] | -0.42 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[HLCS]] | -0.41 | -0.27 / -0.34 | both halves | 3e-04 | pathway: Diseases of metabolism |
| [[USP4]] | -0.41 | -0.18 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[NEPRO-AS1]] | -0.41 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[ZNF354A]] | -0.40 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[LZIC]] | -0.39 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[JPX]] | -0.39 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[CRCP]] | -0.39 | -0.25 / -0.33 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A4]] | C | SLC44A4 activity raises SFTPA2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 1.58× lower at baseline in the lines without SLC44A4 | 0.030 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[XIST]] | C | XIST activity raises SFTPA2's level | lines that do not express XIST (43) vs lines expressing it (7) | 2.25× lower at baseline in the lines without XIST | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20; co-absent with the target |
| [[MSLN]] | C | MSLN activity raises SFTPA2's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.46× lower at baseline in the lines without MSLN | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[MUC4]] | C | MUC4 activity raises SFTPA2's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 1.81× lower at baseline in the lines without MUC4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6; co-absent with the target |
| [[FUT3]] | C | FUT3 activity raises SFTPA2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without FUT3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises SFTPA2's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 1.48× lower at baseline in the lines without RAB25 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises SFTPA2's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.41× lower at baseline in the lines without MAL2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises SFTPA2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.63× lower at baseline in the lines without WFDC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC4]] | C | SFTPA2 activity raises MUC4's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 2.93× lower at baseline in the lines without SFTPA2 | 0.002 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[TACSTD2]] | C | SFTPA2 activity raises TACSTD2's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 14.76× lower at baseline in the lines without SFTPA2 | 0.003 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[FUT3]] | C | SFTPA2 activity raises FUT3's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 8.44× lower at baseline in the lines without SFTPA2 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[ERBB3]] | C | SFTPA2 activity raises ERBB3's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 6.46× lower at baseline in the lines without SFTPA2 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[KCNK5]] | C | SFTPA2 activity raises KCNK5's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 2.91× lower at baseline in the lines without SFTPA2 | 0.010 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |
| [[SLC44A4]] | C | SFTPA2 activity raises SLC44A4's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 6.58× lower at baseline in the lines without SFTPA2 | 0.013 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[NPEPPSP1]] | C | SFTPA2 activity raises NPEPPSP1's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 1.95× lower at baseline in the lines without SFTPA2 | 0.015 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |
| [[CD74]] | C | SFTPA2 activity raises CD74's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 2.82× lower at baseline in the lines without SFTPA2 | 0.026 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[ADGRF4]] | C | SFTPA2 activity raises ADGRF4's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 3.85× lower at baseline in the lines without SFTPA2 | 0.030 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SPINT1]] | C | SFTPA2 activity raises SPINT1's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 7.22× lower at baseline in the lines without SFTPA2 | 0.037 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[LGALS9]] | C | SFTPA2 activity raises LGALS9's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 2.47× lower at baseline in the lines without SFTPA2 | 0.039 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |
| [[MAL2]] | C | SFTPA2 activity raises MAL2's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 6.53× lower at baseline in the lines without SFTPA2 | 0.042 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.404). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 55.8); signed map (62.9, -1.7). **Vector** length 4.20, 1.51% of its response variance represented; |z| ≥ 3 in 18 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.3 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.2 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.2 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.1 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.1 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.1 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | +0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.1 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.1 | +0.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.1 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.1 | -3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | surfactant protein A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:79,555,852-79,560,407 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SP-A2, COLEC5 |
| Gene groups (HGNC) | Collectins; C-type lectin domain containing |
| Reactome | 11 pathways, smallest: Diseases associated with surfactant metabolism; Signal regulatory protein family interactions; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWL1](https://www.uniprot.org/uniprotkb/Q8IWL1) (Pulmonary surfactant-associated protein A2):

> In presence of calcium ions, it binds to surfactant phospholipids and contributes to lower the surface tension at the air-liquid interface in the alveoli of the mammalian lung and is essential for normal respiration.

**Summary**, from NCBI Gene [729238](https://www.ncbi.nlm.nih.gov/gene/729238):

> This gene is one of several genes encoding pulmonary-surfactant associated proteins (SFTPA) located on chromosome 10. Mutations in this gene and a highly similar gene located nearby, which affect the highly conserved carbohydrate recognition domain, are associated with idiopathic pulmonary fibrosis. The current version of the assembly displays only a single centromeric SFTPA gene pair rather than the two gene pairs shown in the previous assembly which were thought to have resulted from a …

**Accessions** — [HGNC:10799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10799) · Entrez [729238](https://www.ncbi.nlm.nih.gov/gene/729238) · UniProt [Q8IWL1](https://www.uniprot.org/uniprotkb/Q8IWL1) · Ensembl [ENSG00000185303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185303)

## Data

Gene col 11657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11657); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11657]; `tensor/DDL_lfc|DDL_z.npy` [11657]; `embed/gene_vectors.npy` [11657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11657 or target_col == 11657). Every well: [[SFTPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFTPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
