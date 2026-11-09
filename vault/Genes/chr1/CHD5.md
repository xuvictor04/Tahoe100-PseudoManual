---
symbol: "CHD5"
type: "gene"
col: 3782
ensembl_id: "ENSG00000116254"
name: "chromodomain helicase DNA binding protein 5"
location: "1p36.31"
module: 128
arm: "+"
pooled_cpm: 13.21
n_lines_expressing: 20
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 40
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# CHD5

*chromodomain helicase DNA binding protein 5* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +13.1, q 1e-36, up in 6 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (PANC-1 0.241×, MIA PaCa-2 0.318×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.300×, PANC-1 0.444×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.402×, MIA PaCa-2 0.430×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRSK2]] (+0.66, fdr 1e-05), [[ELFN1]] (+0.65, fdr 7e-06), [[PDZD4]] (+0.62, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 40 go from it, the strongest it → [[MEGF11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +13.1 | 1e-36 | 6/16 (A549, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +12.8 | 4e-35 | 7/13 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +11.1 | 2e-26 | 4/7 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +10.5 | 2e-23 | 7/18 (LS 180, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +7.7 | 2e-12 | 4/18 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +7.5 | 5e-12 | 7/17 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.1 | 1e-10 | 1/8 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.8 | 4e-07 | 3/17 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.4 | 4e-06 | 3/15 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 2/16 (NCI-H23, SHP-77) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.0 | 0.004 | 4/16 (LS 180, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 1/18 (SW480) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 12/18 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.5 | 0.017 | 5/17 (LS 180, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.4 | 0.029 | 1/14 (A549) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.034 | 3/17 (NCI-H23, SW 900, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.034 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3782.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (PANC-1 0.241×, MIA PaCa-2 0.318×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.300×, PANC-1 0.444×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.402×, MIA PaCa-2 0.430×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.743× | -3.3 | 0.32 | 8/17 (C-33 A, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.753× | -3.2 | 0.32 | 6/17 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.731× | -3.1 | 0.32 | 3/18 (BT-474, PANC-1, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.733× | -3.1 | 0.32 | 1/17 (A549) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 48.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0527× (z -22.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.8) |
| [[PANC-1 (line)]] | alt | 126 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -14.6) |
| [[A-427 (line)]] | wt | 41.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.402× (z -10.4) |
| [[LS 180 (line)]] | wt | 4.00 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0726× (z -9.0) |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRSK2]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ELFN1]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PDZD4]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[KCNQ2]] | +0.60 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[CECR2]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PALM]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[KIF26A]] | +0.57 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TBX1]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[CYS1]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SEPTIN5]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[B4GALNT4]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CBFA2T3]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises CHD5's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without ELFN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[GNAZ]] | B | GNAZ activity raises CHD5's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.10× lower at baseline in the lines without GNAZ | 0.041 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[FSD1]] | B | FSD1 activity raises CHD5's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without FSD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[KIF26A]] | B | KIF26A activity raises CHD5's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without KIF26A | 0.070 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[KIF1A]] | C | KIF1A activity raises CHD5's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.81× lower at baseline in the lines without KIF1A | 0.005 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises CHD5's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without MYT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[CECR2]] | C | CECR2 activity raises CHD5's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.50× lower at baseline in the lines without CECR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises CHD5's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without DPYSL5 | 0.022 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[BEGAIN]] | C | BEGAIN activity raises CHD5's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.57× lower at baseline in the lines without BEGAIN | 0.034 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises CHD5's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without JPH3 | 0.050 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[B4GALNT4]] | C | B4GALNT4 activity raises CHD5's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without B4GALNT4 | 0.087 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |
| [[CBFA2T3]] | C | CBFA2T3 activity raises CHD5's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.30× lower at baseline in the lines without CBFA2T3 | 0.093 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 28, C 12. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEGF11]] | B | CHD5 activity raises MEGF11's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without CHD5 | 0.006 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[ADGRB1]] | B | CHD5 activity raises ADGRB1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without CHD5 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[KIF26A]] | B | CHD5 activity raises KIF26A's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without CHD5 | 0.011 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[APC2]] | B | CHD5 activity raises APC2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.59× lower at baseline in the lines without CHD5 | 0.017 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[AZU1]] | B | CHD5 activity raises AZU1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without CHD5 | 0.018 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[RASGEF1C]] | B | CHD5 activity raises RASGEF1C's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without CHD5 | 0.018 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[NKAIN1]] | B | CHD5 activity raises NKAIN1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without CHD5 | 0.020 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[CAMK2B]] | B | CHD5 activity raises CAMK2B's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without CHD5 | 0.029 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[TTC7B]] | B | CHD5 activity raises TTC7B's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without CHD5 | 0.030 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[SSBP4]] | B | CHD5 activity raises SSBP4's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.24× lower at baseline in the lines without CHD5 | 0.030 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[PALM]] | B | CHD5 activity raises PALM's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without CHD5 | 0.031 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[PDZD4]] | B | CHD5 activity raises PDZD4's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without CHD5 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.5, 38.2); signed map (24.6, 24.4). **Vector** length 37.4, 7.95% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.1 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,101,787-6,180,321 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PHD finger proteins; SNF2 related family; NuRD complex subunits |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDI0](https://www.uniprot.org/uniprotkb/Q8TDI0) (ATP-dependent chromatin remodeler CHD5):

> ATP-dependent chromatin-remodeling factor that binds DNA through histones and regulates gene transcription. May specifically recognize and bind trimethylated 'Lys-27' (H3K27me3) and non-methylated 'Lys-4' of histone H3. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Plays a role in the development of the nervous system by activating the expression of genes promoting neuron terminal differentiation. In parallel, it may also …

**Summary**, from NCBI Gene [26038](https://www.ncbi.nlm.nih.gov/gene/26038):

> This gene encodes a member of the chromodomain helicase DNA-binding protein family. Members of this family are characterized by a chromodomain, a helicase ATP-binding domain and an additional functional domain. This gene encodes a neuron-specific protein that may function in chromatin remodeling and gene transcription. This gene is a potential tumor suppressor gene that may play a role in the development of neuroblastoma. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:16816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16816) · Entrez [26038](https://www.ncbi.nlm.nih.gov/gene/26038) · UniProt [Q8TDI0](https://www.uniprot.org/uniprotkb/Q8TDI0) · Ensembl [ENSG00000116254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116254)

## Data

Gene col 3782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3782); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3782]; `tensor/DDL_lfc|DDL_z.npy` [3782]; `embed/gene_vectors.npy` [3782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3782 or target_col == 3782). Every well: [[CHD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
