---
symbol: "CST6"
type: "gene"
col: 10593
ensembl_id: "ENSG00000175315"
name: "cystatin E/M"
location: "11q13.1"
module: 58
arm: "+"
pooled_cpm: 4.66
n_lines_expressing: 8
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CST6

*cystatin E/M* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.28× (z +9.9, q 3e-20, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +6.0, q 3e-07, up in 4 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.391× (z -4.1, q 0.029, down in 0 of 6 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (HCT15 0.0333×).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf33]] (+0.53, fdr 3e-05), [[RBP1]] (+0.44, fdr 7e-04), [[SOD3]] (+0.43, fdr 6e-04); moves opposite to [[SUGT1P3]] (-0.51, fdr 7e-05), [[CCDC6]] (-0.47, fdr 1e-04), [[TTC22]] (-0.47, fdr 8e-04, ⚠ not reproduced), [[BAG1]] (-0.42, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MUC4]] → it (grade C ⚠); 10 go from it, the strongest it → [[LNX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.28×** | +9.9 | 3e-20 | 4/4 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.39×** | +9.2 | 9e-18 | 4/4 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.10×** | +7.7 | 3e-12 | 4/4 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.89×** | +6.2 | 6e-08 | 4/5 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +6.0 | 3e-07 | 4/6 (Panc 03.27, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.26×** | +5.2 | 2e-05 | 3/5 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +5.1 | 3e-05 | 5/5 (Panc 03.27, HCT15, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.87×** | +4.1 | 0.004 | 0/6 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.0 | 0.004 | 4/5 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.35×** | +3.9 | 0.005 | 4/6 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +3.5 | 0.020 | 1/5 (Panc 03.27) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.00×** | +3.3 | 0.040 | 1/2 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 3.15× | +3.0 | 0.12 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10593.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (HCT15 0.0333×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.391×** | -4.1 | 0.029 | 0/6 | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 5 µM |  | 0.256× | -3.3 | 0.19 | 2/6 (HCT15, Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.495× | -3.3 | 0.19 | 1/6 (HT-29) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 11.4 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.0333× (z -10.0) |
| [[A-172 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.206 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 16 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf33]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[RBP1]] | +0.44 | +0.20 / +0.59 | both halves | 7e-04 |  |
| [[SOD3]] | +0.43 | +0.22 / +0.64 | both halves | 6e-04 |  |
| [[CYBA]] | +0.43 | +0.36 / +0.33 | both halves | 1e-04 |  |
| [[MYL12B]] | +0.42 | +0.45 / +0.27 | both halves | 3e-04 |  |
| [[SNX32]] | +0.42 | +0.40 / +0.30 | both halves | 2e-04 |  |
| [[LINC01322]] | +0.42 | +0.39 / +0.25 | both halves | 4e-04 |  |
| [[CASC20]] | +0.42 | +0.32 / +0.26 | both halves | 3e-04 |  |
| [[CD9]] | +0.41 | +0.39 / +0.31 | both halves | 2e-04 |  |
| [[ADGRE3]] | +0.41 | +0.32 / +0.27 | both halves | 3e-04 |  |
| [[MAGEA3-DT]] | +0.41 | +0.07 / +0.37 | ⚠ not reproduced | 0.004 |  |
| [[PRADC1]] | +0.40 | +0.27 / +0.31 | both halves | 3e-04 |  |
| [[E2F7]] | +0.40 | +0.41 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P3]] | -0.51 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CCDC6]] | -0.47 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[TTC22]] | -0.47 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[MUC4]] | -0.43 | -0.19 / -0.27 | ⚠ not reproduced | 9e-04 |  |
| [[BAG1]] | -0.42 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[SLC15A1]] | -0.40 | -0.05 / -0.49 | ⚠ not reproduced | 0.005 |  |
| [[SLC4A2]] | -0.40 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[AP1G2]] | -0.40 | -0.10 / -0.31 | ⚠ not reproduced | 0.003 |  |
| [[LNX1]] | -0.40 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[SLC34A2]] | -0.39 | -0.09 / -0.43 | ⚠ not reproduced | 0.003 |  |
| [[TPTE2P5]] | -0.38 | -0.32 / -0.27 | both halves | 3e-04 |  |
| [[ABCF3]] | -0.38 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[CUL5]] | -0.38 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[SYNJ2BP]] | -0.37 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[TTC5]] | -0.37 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ALDH3B1]] | -0.37 | -0.26 / -0.22 | both halves | 6e-04 |  |
| [[TLR3]] | -0.37 | -0.22 / -0.31 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC4]] | C | MUC4 activity raises CST6's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 4.11× lower at baseline in the lines without MUC4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6; co-absent with the target |
| [[SGPP2]] | C | SGPP2 activity raises CST6's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.49× lower at baseline in the lines without SGPP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4; co-absent with the target |
| [[FAAH2]] | C | FAAH2 activity raises CST6's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without FAAH2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent; co-absent with the target |
| [[SLC34A2]] | C | SLC34A2 activity raises CST6's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.82× lower at baseline in the lines without SLC34A2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | CST6 activity raises LNX1's level | lines that do not express CST6 (42) vs lines expressing it (8) | 5.12× lower at baseline in the lines without CST6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[RBM47]] | B | CST6 activity raises RBM47's level | lines that do not express CST6 (42) vs lines expressing it (8) | 6.05× lower at baseline in the lines without CST6 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[AP1G2]] | B | CST6 activity raises AP1G2's level | lines that do not express CST6 (42) vs lines expressing it (8) | 2.24× lower at baseline in the lines without CST6 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[S100A13]] | B | CST6 activity raises S100A13's level | lines that do not express CST6 (42) vs lines expressing it (8) | 1.82× lower at baseline in the lines without CST6 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[C19orf33]] | B | CST6 activity raises C19orf33's level | lines that do not express CST6 (42) vs lines expressing it (8) | 3.96× lower at baseline in the lines without CST6 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[SUGT1P3]] | B | CST6 activity raises SUGT1P3's level | lines that do not express CST6 (42) vs lines expressing it (8) | 1.71× lower at baseline in the lines without CST6 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546 |
| [[MUC4]] | C | CST6 activity raises MUC4's level | lines that do not express CST6 (42) vs lines expressing it (8) | 9.31× lower at baseline in the lines without CST6 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546; co-absent with the target |
| [[SGPP2]] | C | CST6 activity raises SGPP2's level | lines that do not express CST6 (42) vs lines expressing it (8) | 9.41× lower at baseline in the lines without CST6 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546; co-absent with the target |
| [[FAAH2]] | C | CST6 activity raises FAAH2's level | lines that do not express CST6 (42) vs lines expressing it (8) | 5.42× lower at baseline in the lines without CST6 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546; co-absent with the target |
| [[SLC34A2]] | C | CST6 activity raises SLC34A2's level | lines that do not express CST6 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without CST6 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546; co-absent with the target |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.189). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, 57.0); signed map (61.1, -6.4). **Vector** length 16.7, 5.00% of its response variance represented; |z| ≥ 3 in 131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.4 | +1.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.4 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | +0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.4 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | +0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -0.4 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cystatin E/M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:66,012,008-66,013,505 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cystatins, type 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15828](https://www.uniprot.org/uniprotkb/Q15828) (Cystatin-M):

> High affinity inhibitor for cathepsin L, cathepsin L2 (cathepsin V), and legumain. Involved in the regulation of epidermal cornification, and hair follicle morphogenesis and maintenance.

**Summary**, from NCBI Gene [1474](https://www.ncbi.nlm.nih.gov/gene/1474):

> The cystatin superfamily encompasses proteins that contain multiple cystatin-like sequences. Some of the members are active cysteine protease inhibitors, while others have lost or perhaps never acquired this inhibitory activity. There are three inhibitory families in the superfamily, including the type 1 cystatins (stefins), type 2 cystatins and the kininogens. The type 2 cystatin proteins are a class of cysteine proteinase inhibitors found in a variety of human fluids and secretions, where …

**Accessions** — [HGNC:2478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2478) · Entrez [1474](https://www.ncbi.nlm.nih.gov/gene/1474) · UniProt [Q15828](https://www.uniprot.org/uniprotkb/Q15828) · Ensembl [ENSG00000175315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175315)

## Data

Gene col 10593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10593); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10593]; `tensor/DDL_lfc|DDL_z.npy` [10593]; `embed/gene_vectors.npy` [10593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10593 or target_col == 10593). Every well: [[CST6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CST6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
