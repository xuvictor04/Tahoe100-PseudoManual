---
symbol: "FGF9"
type: "gene"
col: 2261
ensembl_id: "ENSG00000102678"
name: "fibroblast growth factor 9"
location: "13q12.11"
module: 9
arm: "+"
pooled_cpm: 6.43
n_lines_expressing: 19
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 20
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FGF9

*fibroblast growth factor 9* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.36× (z +19.7, q 0e+00, up in 10 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.262×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02223]] (+0.53, fdr 2e-05), [[SLC7A8]] (+0.52, fdr 3e-05), [[PPARGC1A]] (+0.48, fdr 2e-05); moves opposite to [[SDCBP2]] (-0.45, fdr 2e-04), [[CALB1]] (-0.42, fdr 2e-04), [[GJB3]] (-0.41, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[PKHD1]] → it (grade B ⚠); 20 go from it, the strongest it → [[RASGEF1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.36×** | +19.7 | 0e+00 | 10/14 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.01×** | +18.9 | 0e+00 | 10/14 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.49×** | +17.6 | 0e+00 | 14/15 (LoVo, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **7.03×** | +16.2 | 0e+00 | 13/15 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.29×** | +15.2 | 0e+00 | 12/15 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.05×** | +11.6 | 5e-29 | 12/15 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.47×** | +10.3 | 6e-23 | 14/15 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.43×** | +10.2 | 1e-22 | 13/15 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +9.0 | 1e-17 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.92×** | +8.5 | 8e-16 | 5/10 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.77×** | +8.4 | 2e-15 | 4/10 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +6.1 | 5e-08 | 3/14 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +5.8 | 3e-07 | 3/8 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.5 | 1e-06 | 9/13 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +4.9 | 4e-05 | 6/15 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +4.5 | 2e-04 | 6/15 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.001 | 0/15 | top dose only |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.94×** | +3.9 | 0.003 | 7/14 (COLO 205, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.89×** | +3.8 | 0.005 | 2/11 (LoVo, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2261.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.262×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.649× | -3.3 | 0.48 | 2/15 (NCI-H1573, SW1417) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.262× (z -11.0) |
| [[COLO 205 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 10.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.71× (z +9.7) | — |
| [[SW480 (line)]] | alt | 15.9 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 3.63× (z +8.7) | — |
| [[A-172 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02223]] | +0.53 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[SLC7A8]] | +0.52 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[PPARGC1A]] | +0.48 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TSPAN12]] | +0.48 | +0.33 / +0.68 | both halves | 1e-04 |  |
| [[AGMO]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ASCL1]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[RUNX1T1]] | +0.47 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[SOX2]] | +0.47 | +0.38 / +0.50 | both halves | 6e-05 | STRING 607 |
| [[SCIN]] | +0.47 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[LRFN2]] | +0.47 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[SPTB]] | +0.47 | +0.39 / +0.54 | both halves | 5e-05 | pathway: MAPK family signaling cascades |
| [[SLAIN1]] | +0.46 | +0.33 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2]] | -0.45 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[CALB1]] | -0.42 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[GJB3]] | -0.41 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[KRT6A]] | -0.40 | -0.47 / -0.26 | both halves | 3e-04 |  |
| [[MUC17]] | -0.39 | -0.47 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[ARHGEF5]] | -0.39 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[ZDHHC3]] | -0.38 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ITGB4]] | -0.37 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[INAVA]] | -0.37 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[FAM83B]] | -0.37 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[LINC02474]] | -0.36 | -0.46 / -0.21 | both halves | 6e-04 |  |
| [[NPSR1]] | -0.36 | -0.45 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[EPS8L1]] | -0.36 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[PITPNM3]] | -0.36 | -0.37 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 2, C 18. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKHD1]] | B | PKHD1 activity raises FGF9's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without PKHD1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[LFNG]] | B | LFNG activity raises FGF9's level | lines that do not express LFNG (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without LFNG | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent |
| [[CALCA]] | C | CALCA activity raises FGF9's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.46× lower at baseline in the lines without CALCA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises FGF9's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.52× lower at baseline in the lines without KCNB2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | ST18 activity raises FGF9's level | lines that do not express ST18 (39) vs lines expressing it (11) | 4.86× lower at baseline in the lines without ST18 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises FGF9's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.56× lower at baseline in the lines without RIT2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises FGF9's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.71× lower at baseline in the lines without SYT4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises FGF9's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.44× lower at baseline in the lines without SRRM4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises FGF9's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 1.72× lower at baseline in the lines without ASCL1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[RMST]] | C | RMST activity raises FGF9's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.21× lower at baseline in the lines without RMST | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[AGMO]] | C | AGMO activity raises FGF9's level | lines that do not express AGMO (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without AGMO | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises FGF9's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without PHYHIPL | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 12, C 8. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASGEF1B]] | B | FGF9 activity raises RASGEF1B's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.93× lower at baseline in the lines without FGF9 | 0.005 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[SERPINI1]] | B | FGF9 activity raises SERPINI1's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without FGF9 | 0.012 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[KLHL32]] | B | FGF9 activity raises KLHL32's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without FGF9 | 0.016 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[SDCBP2]] | B | FGF9 activity raises SDCBP2's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 3.02× lower at baseline in the lines without FGF9 | 0.022 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[EPS8L1]] | B | FGF9 activity raises EPS8L1's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.65× lower at baseline in the lines without FGF9 | 0.022 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[SELENOP]] | B | FGF9 activity raises SELENOP's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 1.63× lower at baseline in the lines without FGF9 | 0.048 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[PITPNM3]] | B | FGF9 activity raises PITPNM3's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 1.78× lower at baseline in the lines without FGF9 | 0.050 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[SLAIN1]] | B | FGF9 activity raises SLAIN1's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 1.71× lower at baseline in the lines without FGF9 | 0.059 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| cells under [[Omeprazole (drug)]] 5 µM | B | FGF9 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express FGF9 (31) vs lines expressing it (17) | the lines without FGF9: 1.14× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| [[MSX2]] | B | FGF9 activity strengthens MSX2's drug response | lines that do not express FGF9 (23) vs lines expressing it (13) | the lines without FGF9 respond 0.70× as strongly (z diff +1.13); strongest at Homoharringtonine 5 µM: 1.83x vs 2.50x (z diff +2.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L; target measured in part of the lines; artifact flags |
| [[ARHGEF5]] | B | FGF9 activity raises ARHGEF5's level | lines that do not express FGF9 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without FGF9 | 0.094 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | FGF9 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FGF9 (31) vs lines expressing it (17) | the lines without FGF9: 1.15× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.331). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.9, 39.5); signed map (46.2, 31.9). **Vector** length 42.6, 11.6% of its response variance represented; |z| ≥ 3 in 358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:21,671,073-21,704,498 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Receptor ligands; Fibroblast growth factor family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 66 pathways, smallest: FGFR3b ligand binding and activation; Transcriptional regulation of testis differentiation; Signaling by activated point mutants of FGFR1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P31371](https://www.uniprot.org/uniprotkb/P31371) (Fibroblast growth factor 9):

> Plays an important role in the regulation of embryonic development, cell proliferation, cell differentiation and cell migration. May have a role in glial cell growth and differentiation during development, gliosis during repair and regeneration of brain tissue after damage, differentiation and survival of neuronal cells, and growth stimulation of glial tumors.

**Summary**, from NCBI Gene [2254](https://www.ncbi.nlm.nih.gov/gene/2254):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth and invasion. This protein was isolated as a secreted factor that exhibits a growth-stimulating effect on cultured glial cells. In nervous system, this protein is produced mainly by neurons …

**Accessions** — [HGNC:3687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3687) · Entrez [2254](https://www.ncbi.nlm.nih.gov/gene/2254) · UniProt [P31371](https://www.uniprot.org/uniprotkb/P31371) · Ensembl [ENSG00000102678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102678)

## Data

Gene col 2261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2261); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2261]; `tensor/DDL_lfc|DDL_z.npy` [2261]; `embed/gene_vectors.npy` [2261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2261 or target_col == 2261). Every well: [[FGF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
