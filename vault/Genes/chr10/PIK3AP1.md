---
symbol: "PIK3AP1"
type: "gene"
col: 7907
ensembl_id: "ENSG00000155629"
name: "phosphoinositide-3-kinase adaptor protein 1"
location: "10q24.1"
module: 55
arm: "+"
pooled_cpm: 14.68
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 57
direction_downstream: 47
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# PIK3AP1

*phosphoinositide-3-kinase adaptor protein 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.78× (z +14.8, q 0e+00, up in 9 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.92× (z +13.9, q 9e-42, up in 14 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.425× (z -12.9, q 5e-35, down in 20 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF4A]] (+0.71, fdr 1e-05), [[LINC01819]] (+0.69, fdr 7e-06), [[GPX2]] (+0.68, fdr 7e-06); moves opposite to [[HOXA9]] (-0.56, fdr 3e-05), [[CHKB]] (-0.51, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 57 arrows point to it, the strongest [[MMP28]] → it (grade B ⚠); 47 go from it, the strongest it → [[ACOT11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +14.8 | 0e+00 | 9/13 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.92×** | +13.9 | 9e-42 | 14/20 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +13.7 | 1e-40 | 11/16 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +11.3 | 3e-27 | 8/13 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +7.9 | 5e-13 | 11/20 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.25×** | +4.8 | 2e-04 | 2/19 (A549, SW480) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.4 | 8e-04 | 1/10 (AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.6 | 0.022 | 0/20 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.5 | 0.027 | 6/16 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.052 | 3/20 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.062 | 1/20 (SW480) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.0 | 0.12 | 1/15 (HepG2/C3A) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -12.9 | 5e-35 | 20/20 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.590×** | -11.2 | 8e-27 | 19/19 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.540×** | -9.3 | 3e-18 | 19/20 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.562×** | -8.7 | 6e-16 | 17/20 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -8.6 | 1e-15 | 18/20 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -8.4 | 4e-15 | 16/20 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -8.0 | 1e-13 | 13/19 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.705×** | -5.2 | 1e-05 | 15/20 (A498, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.590×** | -4.1 | 0.002 | 7/19 (A-172, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.764×** | -4.0 | 0.003 | 4/20 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.784×** | -3.6 | 0.014 | 4/20 (HEC-1-A, HT-29, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.780×** | -3.4 | 0.026 | 3/20 (LoVo, SHP-77, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.100 | 12/20 (LoVo, LS 180, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 127 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0343× (z -30.1) |
| [[SW480 (line)]] | alt | 8.75 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.2) |
| [[SW1417 (line)]] | alt | 27.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 31.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0718× (z -19.4) |
| [[RKO (line)]] | wt | 22.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0969× (z -13.6) |
| [[SW48 (line)]] | wt | 16.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -19.0) |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -13.6) |
| [[A498 (line)]] | wt | 47.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.6) |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -15.5) |
| [[A549 (line)]] | wt | 5.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -8.9) |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.7) |
| [[KATO III (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4A]] | +0.71 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[GPX2]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.68 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CTSE]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[LINC02474]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GRIN2B]] | +0.65 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[DSG3]] | +0.64 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[VILL]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[NPSR1]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[INPP5D]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA9]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CHKB]] | -0.51 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 2, C 55. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP28]] | B | MMP28 activity raises PIK3AP1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without MMP28 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[XK]] | B | XK activity raises PIK3AP1's level | lines that do not express XK (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without XK | 0.069 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[GCNT3]] | C | GCNT3 activity raises PIK3AP1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 5.02× lower at baseline in the lines without GCNT3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[LINC02331]] | C | LINC02331 activity raises PIK3AP1's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without LINC02331 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises PIK3AP1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without FGFBP1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises PIK3AP1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 4.68× lower at baseline in the lines without TFF2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises PIK3AP1's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.67× lower at baseline in the lines without CEACAM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises PIK3AP1's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.48× lower at baseline in the lines without LAD1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises PIK3AP1's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 4.92× lower at baseline in the lines without EPS8L3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[DSG3]] | C | DSG3 activity raises PIK3AP1's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 5.23× lower at baseline in the lines without DSG3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises PIK3AP1's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.90× lower at baseline in the lines without PPP1R1B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises PIK3AP1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.75× lower at baseline in the lines without GPX2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 7, C 40. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT11]] | B | PIK3AP1 activity raises ACOT11's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without PIK3AP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[PRR5-ARHGAP8]] | B | PIK3AP1 activity raises PRR5-ARHGAP8's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without PIK3AP1 | 0.025 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[FGFR4]] | B | PIK3AP1 activity raises FGFR4's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without PIK3AP1 | 0.040 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[XK]] | B | PIK3AP1 activity raises XK's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without PIK3AP1 | 0.046 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[VILL]] | B | PIK3AP1 activity raises VILL's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 1.91× lower at baseline in the lines without PIK3AP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[NOSTRIN]] | B | PIK3AP1 activity raises NOSTRIN's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without PIK3AP1 | 0.064 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[ZNF503-AS1]] | B | PIK3AP1 activity raises ZNF503-AS1's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without PIK3AP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |
| [[B3GNT3]] | C | PIK3AP1 activity raises B3GNT3's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 5.13× lower at baseline in the lines without PIK3AP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[LINC03040]] | C | PIK3AP1 activity raises LINC03040's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without PIK3AP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[USH1C]] | C | PIK3AP1 activity raises USH1C's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 5.27× lower at baseline in the lines without PIK3AP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[HNF4A]] | C | PIK3AP1 activity raises HNF4A's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 8.18× lower at baseline in the lines without PIK3AP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[UNC5A]] | C | PIK3AP1 activity raises UNC5A's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.74× lower at baseline in the lines without PIK3AP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, 49.3); signed map (65.1, 9.3). **Vector** length 77.8, 24.6% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.9 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.2 | +3.2 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide-3-kinase adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,593,315-96,720,514 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCAP, FLJ35564 |
| Reactome | 10 pathways, smallest: Antigen activates B Cell Receptor (BCR) leading to generation of second messengers; Constitutive Signaling by Aberrant PI3K in Cancer; PI3K/AKT Signaling in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZUJ8](https://www.uniprot.org/uniprotkb/Q6ZUJ8) (Phosphoinositide 3-kinase adapter protein 1):

> Signaling adapter that contributes to B-cell development by linking B-cell receptor (BCR) signaling to the phosphoinositide 3-kinase (PI3K)-Akt signaling pathway. Has a complementary role to the BCR coreceptor CD19, coupling BCR and PI3K activation by providing a docking site for the PI3K subunit PIK3R1. Alternatively, links Toll-like receptor (TLR) signaling to PI3K activation, a process preventing excessive inflammatory cytokine production. Also involved in the activation of PI3K in natural …

**Summary**, from NCBI Gene [118788](https://www.ncbi.nlm.nih.gov/gene/118788):

> Predicted to enable phosphatidylinositol 3-kinase regulatory subunit binding activity and signaling receptor binding activity. Predicted to be involved in positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; regulation of inflammatory response; and regulation of innate immune response. Predicted to be located in membrane. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30034) · Entrez [118788](https://www.ncbi.nlm.nih.gov/gene/118788) · UniProt [Q6ZUJ8](https://www.uniprot.org/uniprotkb/Q6ZUJ8) · Ensembl [ENSG00000155629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155629)

## Data

Gene col 7907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7907); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7907]; `tensor/DDL_lfc|DDL_z.npy` [7907]; `embed/gene_vectors.npy` [7907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7907 or target_col == 7907). Every well: [[PIK3AP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3AP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
