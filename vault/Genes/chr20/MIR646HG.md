---
symbol: "MIR646HG"
type: "gene"
col: 13637
ensembl_id: "ENSG00000228340"
name: "MIR646 host gene"
location: "20q13.33"
module: 108
arm: "+"
pooled_cpm: 22.31
n_lines_expressing: 16
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 22
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MIR646HG

*MIR646 host gene* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +14.8, q 0e+00, up in 0 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Hs 766T 0.0615×, HS-578T 0.301×, NCI-H1573 0.422×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 0.271×, NCI-H23 0.0731×, NCI-H1573 0.249×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HS-578T 0.251×, Hs 766T 0.145×, RPMI-7951 0.369×); [[Binimetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0612×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01446]] (+0.66, fdr 7e-06), [[TENM4]] (+0.61, fdr 1e-05), [[KHDRBS2]] (+0.55, fdr 1e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 22 go from it, the strongest it → [[RNF152]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +14.8 | 0e+00 | 0/13 | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.4 | 9e-23 | 1/8 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.4 | 7e-15 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +8.2 | 4e-14 | 6/14 (HS-578T, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +7.0 | 4e-10 | 1/11 (SHP-77) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +6.8 | 9e-10 | 8/12 (LOX-IMVI, SW 1271, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.1 | 3e-05 | 0/12 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.0 | 3e-05 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.54×** | +4.6 | 3e-04 | 7/13 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.3 | 0.001 | 1/13 (NCI-H23) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.008 | 0/14 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.027 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13637.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Hs 766T 0.0615×, HS-578T 0.301×, NCI-H1573 0.422×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 0.271×, NCI-H23 0.0731×, NCI-H1573 0.249×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HS-578T 0.251×, Hs 766T 0.145×, RPMI-7951 0.369×); [[Binimetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0612×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.688× | -3.6 | 0.15 | 2/13 (Hs 766T, LOX-IMVI) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.715× | -3.3 | 0.23 | 0/13 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.735× | -3.2 | 0.23 | 10/13 (NCI-H23, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[MK-8353 (drug)]] 0.5 µM |  | 0.662× | -3.1 | 0.27 | 1/14 (AN3 CA) | inconsistent across doses | noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.734× | -3.0 | 0.28 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 129 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0615× (z -15.3) |
| [[SHP-77 (line)]] | alt | 598 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 32.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 77.9 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0731× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.109× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -10.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 18.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.50× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.0) |
| [[SW 1271 (line)]] | alt | 182 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.150× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~10% of this change |
| [[SW1417 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A-172 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.94 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01446]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TENM4]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[KHDRBS2]] | +0.55 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[ZNF208]] | +0.52 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[GABRA3]] | +0.52 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LRFN2]] | +0.51 | +0.22 / +0.67 | both halves | 6e-04 |  |
| [[LINC01194]] | +0.50 | +0.29 / +0.55 | both halves | 3e-04 |  |
| [[MAGEA3-DT]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[GRIA2]] | +0.50 | +0.25 / +0.49 | both halves | 4e-04 |  |
| [[TMEM108]] | +0.49 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[ELMO1]] | +0.49 | +0.24 / +0.48 | both halves | 4e-04 |  |
| [[PPP1R14C]] | +0.49 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIR646HG's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TENM4]] | C | TENM4 activity raises MIR646HG's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 4.58× lower at baseline in the lines without TENM4 | 0.003 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[LINC01194]] | C | LINC01194 activity raises MIR646HG's level | lines that do not express LINC01194 (31) vs lines expressing it (19) | 3.41× lower at baseline in the lines without LINC01194 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC00470, ENSG00000259929, ENSG00000249174; co-absent with the target |
| [[SNTG2]] | C | SNTG2 activity raises MIR646HG's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 3.10× lower at baseline in the lines without SNTG2 | 0.025 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent; co-absent with the target |
| [[KC6]] | C | KC6 activity raises MIR646HG's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.99× lower at baseline in the lines without KC6 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises MIR646HG's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 4.82× lower at baseline in the lines without ZNF208 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |
| [[SLITRK6]] | C | SLITRK6 activity raises MIR646HG's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 3.10× lower at baseline in the lines without SLITRK6 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[LINC01266]] | C | LINC01266 activity raises MIR646HG's level | lines that do not express LINC01266 (35) vs lines expressing it (15) | 3.13× lower at baseline in the lines without LINC01266 | 0.049 | ⚠ within organs, on part of the lines; also absent: UNC5D, KHDRBS2, ENSG00000260958; maybe low, not absent; co-absent with the target |
| [[LINC00540]] | C | LINC00540 activity raises MIR646HG's level | lines that do not express LINC00540 (33) vs lines expressing it (17) | 2.99× lower at baseline in the lines without LINC00540 | 0.056 | ⚠ within organs, on part of the lines; also absent: CPLX2, SLC24A3, CHGB; co-absent with the target |
| [[LINC02109]] | C | LINC02109 activity raises MIR646HG's level | lines that do not express LINC02109 (40) vs lines expressing it (10) | 5.36× lower at baseline in the lines without LINC02109 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287474, ENSG00000253642, LINC00879; co-absent with the target |
| [[LINC02725]] | C | LINC02725 activity raises MIR646HG's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 3.63× lower at baseline in the lines without LINC02725 | 0.060 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises MIR646HG's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 2.93× lower at baseline in the lines without GTSF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 7, C 15. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF152]] | B | MIR646HG activity raises RNF152's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 3.22× lower at baseline in the lines without MIR646HG | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[LINC00871]] | B | MIR646HG activity raises LINC00871's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.68× lower at baseline in the lines without MIR646HG | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[LINC00871]] | B | MIR646HG activity weakens LINC00871's drug response | lines that do not express MIR646HG (22) vs lines expressing it (12) | the lines without MIR646HG respond 2.63× as strongly (z diff -1.68); strongest at Idarubicin (hydrochloride) 5 µM: 4.36x vs 0.83x (z diff -7.0) | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; target measured in part of the lines; artifact flags |
| [[EPHB1]] | B | MIR646HG activity raises EPHB1's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without MIR646HG | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[EHD3]] | B | MIR646HG activity raises EHD3's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.11× lower at baseline in the lines without MIR646HG | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[DIRC3-AS1]] | B | MIR646HG activity raises DIRC3-AS1's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.62× lower at baseline in the lines without MIR646HG | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[AGBL4]] | B | MIR646HG activity raises AGBL4's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.40× lower at baseline in the lines without MIR646HG | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211 |
| [[GABRA3]] | C | MIR646HG activity raises GABRA3's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 4.46× lower at baseline in the lines without MIR646HG | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[ERG]] | C | MIR646HG activity raises ERG's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without MIR646HG | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[MIR4527HG]] | C | MIR646HG activity raises MIR4527HG's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without MIR646HG | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[KCTD8]] | C | MIR646HG activity raises KCTD8's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 2.25× lower at baseline in the lines without MIR646HG | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |
| [[CHMP1B2P]] | C | MIR646HG activity raises CHMP1B2P's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 3.69× lower at baseline in the lines without MIR646HG | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.6, 24.1); signed map (32.8, 44.6). **Vector** length 40.0, 10.5% of its response variance represented; |z| ≥ 3 in 341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -1.4 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MIR646 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.33 — chr20:60,087,661-60,653,784 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C20orf197, LINC02910 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27659) · Entrez [284757](https://www.ncbi.nlm.nih.gov/gene/284757) · Ensembl [ENSG00000228340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228340)

## Data

Gene col 13637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13637); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13637]; `tensor/DDL_lfc|DDL_z.npy` [13637]; `embed/gene_vectors.npy` [13637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13637 or target_col == 13637). Every well: [[MIR646HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR646HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
