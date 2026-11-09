---
symbol: "TNFSF14"
type: "gene"
col: 4652
ensembl_id: "ENSG00000125735"
name: "TNF superfamily member 14"
location: "19p13.3"
module: 139
arm: "+"
pooled_cpm: 3.89
n_lines_expressing: 16
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 29
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# TNFSF14

*TNF superfamily member 14* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.28× (z +13.8, q 8e-41, up in 9 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0753×); [[Tofacitinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.209×); [[Thymopentin (drug)]] 5 µM in 1 line (CFPAC-1 0.0320×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[HPN]] (+0.62, fdr 7e-06), [[SLC2A14]] (+0.60, fdr 1e-05), [[LINC00958]] (+0.60, fdr 1e-05); moves opposite to [[KATNAL1]] (-0.51, fdr 2e-05), [[SLC66A3]] (-0.50, fdr 4e-05), [[ANKRD36B]] (-0.46, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[LINC01285]] → it (grade B ⚠); 29 go from it, the strongest it → [[FBXO39]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.28×** | +13.8 | 8e-41 | 9/11 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.15×** | +11.1 | 3e-26 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.22×** | +9.7 | 4e-20 | 7/10 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.73×** | +9.1 | 9e-18 | 1/8 (Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.92×** | +8.9 | 7e-17 | 11/13 (A498, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.56×** | +8.2 | 2e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.99×** | +8.1 | 3e-14 | 7/10 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.73×** | +5.9 | 2e-07 | 6/12 (HOP62, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.45×** | +5.3 | 9e-06 | 7/10 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +4.8 | 7e-05 | 6/12 (HOP62, HS-578T, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.5 | 3e-04 | 3/13 (A498, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.9 | 0.004 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.86×** | +3.6 | 0.012 | 4/11 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +3.6 | 0.012 | 7/12 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.76×** | +3.3 | 0.037 | 0/12 | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +3.2 | 0.043 | 4/12 (HOP62, A498, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +3.2 | 0.048 | 2/8 (CFPAC-1, HOP62) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +2.9 | 0.088 | 3/8 (A498, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.00×** | +2.9 | 0.097 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4652.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0753×); [[Tofacitinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.209×); [[Thymopentin (drug)]] 5 µM in 1 line (CFPAC-1 0.0320×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.572× | -3.1 | 0.64 | 2/13 (HOP62, A498) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 209 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.0753× (z -13.3) |
| [[HS-578T (line)]] | alt | 2.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0320× (z -10.0) |
| [[HOP62 (line)]] | alt | 1.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +9.6) | — |
| [[J82 (line)]] | alt | 1.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +8.5) | — |
| [[A-172 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.963 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.878 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3]] | +0.78 | +0.79 / +0.76 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 7.1 kb 3′ of C3 on the same strand (can correlate by spillover, not regulation) |
| [[HPN]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SLC2A14]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[LINC00958]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SAA2-SAA4]] | +0.59 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SAA4]] | +0.58 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CFH]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CFB]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ALDH1A2]] | +0.54 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[SOCS3]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SAA2]] | +0.53 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TNIP3]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[FGA]] | +0.52 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL1]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SLC66A3]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ANKRD36B]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GLT8D1]] | -0.46 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[STX2]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ABCB10]] | -0.45 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01285]] | B | LINC01285 activity raises TNFSF14's level | lines that do not express LINC01285 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without LINC01285 | 0.038 | ⚠ within organs, on part of the lines; also absent: HNF1A, SLC22A3, LINC01819; maybe low, not absent |
| [[C3]] | C | C3 activity raises TNFSF14's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.88× lower at baseline in the lines without C3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises TNFSF14's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 3.79× lower at baseline in the lines without ITIH2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[FGA]] | C | FGA activity raises TNFSF14's level | lines that do not express FGA (43) vs lines expressing it (7) | 4.19× lower at baseline in the lines without FGA | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[KRT17]] | C | KRT17 activity raises TNFSF14's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 1.41× lower at baseline in the lines without KRT17 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2; co-absent with the target |
| [[CP]] | C | CP activity raises TNFSF14's level | lines that do not express CP (39) vs lines expressing it (11) | 3.36× lower at baseline in the lines without CP | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |
| [[FGB]] | C | FGB activity raises TNFSF14's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.38× lower at baseline in the lines without FGB | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[AGT]] | C | AGT activity raises TNFSF14's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.23× lower at baseline in the lines without AGT | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[FGG]] | C | FGG activity raises TNFSF14's level | lines that do not express FGG (42) vs lines expressing it (8) | 3.12× lower at baseline in the lines without FGG | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises TNFSF14's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 3.23× lower at baseline in the lines without IGFBP1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |
| [[CFH]] | C | CFH activity raises TNFSF14's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without CFH | 0.050 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises TNFSF14's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 1.73× lower at baseline in the lines without FOXQ1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 16, C 13. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO39]] | B | TNFSF14 activity raises FBXO39's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without TNFSF14 | 0.002 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[DNAH17]] | B | TNFSF14 activity raises DNAH17's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without TNFSF14 | 0.005 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[CEACAM16-AS1]] | B | TNFSF14 activity raises CEACAM16-AS1's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.49× lower at baseline in the lines without TNFSF14 | 0.005 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[ZC3H12A]] | B | TNFSF14 activity raises ZC3H12A's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.60× lower at baseline in the lines without TNFSF14 | 0.007 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[UNC5CL]] | B | TNFSF14 activity raises UNC5CL's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.42× lower at baseline in the lines without TNFSF14 | 0.007 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[PTPN22]] | B | TNFSF14 activity raises PTPN22's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.11× lower at baseline in the lines without TNFSF14 | 0.036 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[PLSCR2]] | B | TNFSF14 activity raises PLSCR2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without TNFSF14 | 0.054 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[TCN2]] | B | TNFSF14 activity raises TCN2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.58× lower at baseline in the lines without TNFSF14 | 0.061 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[CEACAM22P-1]] | B | TNFSF14 activity raises CEACAM22P-1's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.40× lower at baseline in the lines without TNFSF14 | 0.062 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[LINC02068]] | B | TNFSF14 activity raises LINC02068's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.52× lower at baseline in the lines without TNFSF14 | 0.064 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[ETS2]] | B | TNFSF14 activity raises ETS2's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without TNFSF14 | 0.067 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[LINC01285]] | B | TNFSF14 activity raises LINC01285's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without TNFSF14 | 0.072 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.0, 21.9); signed map (37.2, 28.3). **Vector** length 37.7, 10.4% of its response variance represented; |z| ≥ 3 in 382 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +2.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | TNF superfamily member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,661,253-6,670,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIGHT, LTg, HVEM-L, CD258 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor superfamily |
| Reactome | 4 pathways, smallest: TNF receptor superfamily (TNFSF) members mediating non-canonical NF-kB pathway; TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O43557](https://www.uniprot.org/uniprotkb/O43557) (Tumor necrosis factor ligand superfamily member 14):

> Cytokine that binds to TNFRSF3/LTB and TNFRSF14/HVEM and plays major roles in immune system regulation. Upon binding to TNFRSF14/HVEM, delivers costimulatory signals to T cells, leading to T cell proliferation and IFNG production. Binds to the decoy receptor TNFRSF6B thereby disrupts the activation signal initiated by TNFSF14, resulting in reduced T-cell activation.

**Summary**, from NCBI Gene [8740](https://www.ncbi.nlm.nih.gov/gene/8740):

> The protein encoded by this gene is a member of the tumor necrosis factor (TNF) ligand family. This protein is a ligand for TNFRSF14, which is a member of the tumor necrosis factor receptor superfamily, and which is also known as a herpesvirus entry mediator (HVEM). This protein may function as a costimulatory factor for the activation of lymphoid cells and as a deterrent to infection by herpesvirus. This protein has been shown to stimulate the proliferation of T cells, and trigger apoptosis of …

**Accessions** — [HGNC:11930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11930) · Entrez [8740](https://www.ncbi.nlm.nih.gov/gene/8740) · UniProt [O43557](https://www.uniprot.org/uniprotkb/O43557) · Ensembl [ENSG00000125735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125735)

## Data

Gene col 4652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4652); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4652]; `tensor/DDL_lfc|DDL_z.npy` [4652]; `embed/gene_vectors.npy` [4652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4652 or target_col == 4652). Every well: [[TNFSF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFSF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
