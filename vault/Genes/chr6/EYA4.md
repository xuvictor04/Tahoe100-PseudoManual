---
symbol: "EYA4"
type: "gene"
col: 3357
ensembl_id: "ENSG00000112319"
name: "EYA transcriptional coactivator and phosphatase 4"
location: "6q23.2"
module: 66
arm: "+"
pooled_cpm: 41.57
n_lines_expressing: 20
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# EYA4

*EYA transcriptional coactivator and phosphatase 4* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +19.7, q 0e+00, up in 6 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.636× (z -6.6, q 2e-08, down in 14 of 16 measured lines) ⚠ toxic. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.755× (z -4.3, q 0.004, down in 7 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 0.285×, A549 0.293×, C32 0.250×, A498 0.343×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.294×, NCI-H2030 0.294×, SW 900 0.283×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.361×, A549 0.367×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A549 0.304×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSGALNACT1]] (+0.66, fdr 1e-05), [[KYNU]] (+0.65, fdr 7e-06), [[NOVA1]] (+0.61, fdr 3e-05); moves opposite to [[WDR37]] (-0.50, fdr 4e-05), [[ATG16L2]] (-0.50, fdr 7e-05), [[BCL7C]] (-0.50, fdr 6e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SLC39A8]] → it (grade B ⚠); 7 go from it, the strongest it → [[SLC39A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +19.7 | 0e+00 | 6/18 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +15.3 | 0e+00 | 0/15 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +10.1 | 1e-21 | 5/18 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +9.3 | 1e-18 | 9/18 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +7.6 | 3e-12 | 9/17 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.6 | 4e-12 | 0/15 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +7.4 | 2e-11 | 1/15 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +7.1 | 1e-10 | 11/18 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.6 | 3e-09 | 6/17 (C32, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 1e-08 | 8/17 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.2 | 4e-08 | 8/16 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 13/18 (NCI-H1792, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 1e-03 | 14/17 (HOP62, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 1e-03 | 2/18 (HOP62, SNU-423) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 1e-03 | 6/17 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.001 | 12/18 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.8 | 0.005 | 8/18 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 7/18 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.006 | 1/17 (A549) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 5/16 (SNU-423, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 0.285×, A549 0.293×, C32 0.250×, A498 0.343×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.294×, NCI-H2030 0.294×, SW 900 0.283×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.361×, A549 0.367×); [[Panobinostat (drug)]] 0.5 µM in 1 line (A549 0.304×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -6.6 | 2e-08 | 14/16 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.710×** | -5.2 | 5e-05 | 11/17 (SW 900, C32, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.755×** | -4.3 | 0.004 | 7/16 (C32, CFPAC-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.761×** | -4.1 | 0.005 | 12/18 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.801× | -3.1 | 0.20 | 0/18 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 164 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 198 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.17× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 196 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 82.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 248 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 21.1 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.01× (z +8.6) | — |
| [[A498 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 42.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 90.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -9.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSGALNACT1]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[KYNU]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NOVA1]] | +0.61 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TGFB2]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SOX5]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[VCAM1]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[EBF1]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[ROS1]] | +0.57 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[AHR]] | +0.56 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[LRMDA]] | +0.56 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[OLR1]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[RSPO3]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR37]] | -0.50 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ATG16L2]] | -0.50 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[BCL7C]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ARHGAP1]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ATAT1]] | -0.49 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[FAM131A]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[OGG1]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[TMCC3]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[HMOX2]] | -0.47 | -0.32 / -0.35 | both halves | 1e-04 |  |
| [[COL6A2]] | -0.46 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[BLCAP]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.46 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A8]] | B | SLC39A8 activity raises EYA4's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 3.83× lower at baseline in the lines without SLC39A8 | 0.051 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[BICC1]] | C | BICC1 activity raises EYA4's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 5.31× lower at baseline in the lines without BICC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |
| [[LRRK2]] | C | LRRK2 activity raises EYA4's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 4.37× lower at baseline in the lines without LRRK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[CYP1B1]] | C | CYP1B1 activity raises EYA4's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 3.48× lower at baseline in the lines without CYP1B1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises EYA4's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 5.45× lower at baseline in the lines without EBF1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[CACNA2D1]] | C | CACNA2D1 activity raises EYA4's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 4.75× lower at baseline in the lines without CACNA2D1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises EYA4's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 3.74× lower at baseline in the lines without GPRIN3 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[CSGALNACT1]] | C | CSGALNACT1 activity raises EYA4's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.49× lower at baseline in the lines without CSGALNACT1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises EYA4's level | lines that do not express KYNU (29) vs lines expressing it (21) | 4.03× lower at baseline in the lines without KYNU | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A8]] | B | EYA4 activity raises SLC39A8's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without EYA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA |
| [[PTGR1]] | B | EYA4 activity raises PTGR1's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without EYA4 | 0.063 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA |
| [[ARID5B]] | B | EYA4 activity raises ARID5B's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without EYA4 | 0.077 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA |
| [[BICC1]] | C | EYA4 activity raises BICC1's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 5.14× lower at baseline in the lines without EYA4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |
| [[KYNU]] | C | EYA4 activity raises KYNU's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 6.37× lower at baseline in the lines without EYA4 | 0.025 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |
| [[ADAMTS3]] | C | EYA4 activity raises ADAMTS3's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without EYA4 | 0.055 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |
| [[CYP1B1]] | C | EYA4 activity raises CYP1B1's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 3.38× lower at baseline in the lines without EYA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.6, 22.4); signed map (47.9, 23.9). **Vector** length 67.3, 22.1% of its response variance represented; |z| ≥ 3 in 520 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +15.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.9 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | EYA transcriptional coactivator and phosphatase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:133,240,514-133,532,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNA10, CMD1J |
| Gene groups (HGNC) | EYA transcriptional coactivator and phosphatases |
| Reactome | 4 pathways, smallest: Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; DNA Double Strand Break Response; DNA Double-Strand Break Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [O95677](https://www.uniprot.org/uniprotkb/O95677) (Protein phosphatase EYA4):

> Tyrosine phosphatase that specifically dephosphorylates 'Tyr-142' of histone H2AX (H2AXY142ph). 'Tyr-142' phosphorylation of histone H2AX plays a central role in DNA repair and acts as a mark that distinguishes between apoptotic and repair responses to genotoxic stress. Promotes efficient DNA repair by dephosphorylating H2AX, promoting the recruitment of DNA repair complexes containing MDC1. Its function as histone phosphatase probably explains its role in transcription regulation during …

**Summary**, from NCBI Gene [2070](https://www.ncbi.nlm.nih.gov/gene/2070):

> This gene encodes a member of the eyes absent (EYA) family of proteins. The encoded protein may act as a transcriptional activator through its protein phosphatase activity, and it may be important for eye development, and for continued function of the mature organ of Corti. Mutations in this gene are associated with postlingual, progressive, autosomal dominant hearing loss at the deafness, autosomal dominant non-syndromic sensorineural 10 locus. The encoded protein is also a putative oncogene …

**Accessions** — [HGNC:3522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3522) · Entrez [2070](https://www.ncbi.nlm.nih.gov/gene/2070) · UniProt [O95677](https://www.uniprot.org/uniprotkb/O95677) · Ensembl [ENSG00000112319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112319)

## Data

Gene col 3357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3357); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3357]; `tensor/DDL_lfc|DDL_z.npy` [3357]; `embed/gene_vectors.npy` [3357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3357 or target_col == 3357). Every well: [[EYA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EYA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
