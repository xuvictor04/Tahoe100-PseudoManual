---
symbol: "FGF13"
type: "gene"
col: 4998
ensembl_id: "ENSG00000129682"
name: "fibroblast growth factor 13"
location: "Xq26.3-q27.1"
module: 121
arm: "+"
pooled_cpm: 42.68
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 12
direction_downstream: 15
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# FGF13

*fibroblast growth factor 13* — Xq26.3-q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.57× (z +25.8, q 0e+00, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.759× (z -4.0, q 0.043, down in 0 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 0.179×, SHP-77 0.169×, CHP-212 0.0700×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.200×, CHP-212 0.0696×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A498 0.272×, BT-474 0.266×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.239×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD8]] (+0.60, fdr 1e-05), [[FBXL7]] (+0.60, fdr 1e-05), [[LINC02438]] (+0.58, fdr 2e-05); moves opposite to [[CNEP1R1]] (-0.45, fdr 3e-04), [[ALAD]] (-0.44, fdr 2e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[LSAMP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +25.8 | 0e+00 | 12/18 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +17.1 | 0e+00 | 11/17 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +13.4 | 1e-38 | 1/18 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +12.6 | 5e-34 | 9/17 (NCI-H1573, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +8.7 | 3e-16 | 1/15 (SW1417) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +8.7 | 4e-16 | 10/17 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +7.9 | 3e-13 | 10/17 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.8 | 4e-13 | 1/16 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.7 | 1e-12 | 7/18 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.4 | 6e-12 | 9/17 (J82, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.1 | 5e-11 | 4/18 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +5.7 | 5e-07 | 6/16 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 2e-05 | 6/17 (A498, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.019 | 7/17 (NCI-H1573, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.048 | 2/17 (SK-MEL-2, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.052 | 4/18 (BT-474, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.052 | 4/17 (C32, BT-474, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.058 | 1/18 (J82) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.091 | 5/17 (NCI-H460, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A498 0.179×, SHP-77 0.169×, CHP-212 0.0700×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.200×, CHP-212 0.0696×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A498 0.272×, BT-474 0.266×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.239×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.759×** | -4.0 | 0.043 | 0/17 | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.837× | -3.6 | 0.078 | 1/17 (HS-578T) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.767×** | -3.5 | 0.078 | 2/17 (SW 1088, SW1417) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.780× | -3.3 | 0.14 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 182 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 12.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.34× (z +13.8) | — |
| [[SW480 (line)]] | alt | 58.0 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 384 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.239× (z -9.2) |
| [[CHP-212 (line)]] | wt | 174 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0700× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 87.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +17.8) | — |
| [[BT-474 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.179× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +14.7) | — |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.6) | — |
| [[A-172 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.36 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.74 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD8]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[FBXL7]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 | same gene group |
| [[LINC02438]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NRG3]] | +0.57 | +0.46 / +0.66 | both halves | 2e-05 | STRING 442 |
| [[TSHZ2]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[CD96]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ARNT2-DT]] | +0.54 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[ADAMTS3]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[LINC00383]] | +0.53 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[CSMD3]] | +0.53 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[SAMMSON]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SOX5]] | +0.52 | +0.46 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNEP1R1]] | -0.45 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[ALAD]] | -0.44 | -0.29 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FGF13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPAS3]] | B | NPAS3 activity raises FGF13's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without NPAS3 | 0.065 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[RALYL]] | B | RALYL activity raises FGF13's level | lines that do not express RALYL (17) vs lines expressing it (33) | 3.23× lower at baseline in the lines without RALYL | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[GLI3]] | C | GLI3 activity raises FGF13's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 4.30× lower at baseline in the lines without GLI3 | 0.014 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises FGF13's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 4.75× lower at baseline in the lines without LINC01320 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises FGF13's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without TSHZ2 | 0.033 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[VIPR2]] | C | VIPR2 activity raises FGF13's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without VIPR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[CACNB2]] | C | CACNB2 activity raises FGF13's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without CACNB2 | 0.070 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[LINGO2]] | C | LINGO2 activity raises FGF13's level | lines that do not express LINGO2 (27) vs lines expressing it (23) | 3.67× lower at baseline in the lines without LINGO2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PTH2R, ADGRB3, PAEP; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises FGF13's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 4.27× lower at baseline in the lines without LEF1-AS1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[PGR]] | C | PGR activity raises FGF13's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.92× lower at baseline in the lines without PGR | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[L3MBTL4]] | C | L3MBTL4 activity raises FGF13's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 3.39× lower at baseline in the lines without L3MBTL4 | 0.098 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LSAMP]] | B | FGF13 activity raises LSAMP's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 3.32× lower at baseline in the lines without FGF13 | 0.008 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[LINC02284]] | B | FGF13 activity raises LINC02284's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.73× lower at baseline in the lines without FGF13 | 0.018 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[TRPM3]] | B | FGF13 activity raises TRPM3's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.17× lower at baseline in the lines without FGF13 | 0.032 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[NPAS3]] | B | FGF13 activity raises NPAS3's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.57× lower at baseline in the lines without FGF13 | 0.049 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[LINC02306]] | B | FGF13 activity raises LINC02306's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.51× lower at baseline in the lines without FGF13 | 0.062 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[ERC2]] | B | FGF13 activity raises ERC2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.96× lower at baseline in the lines without FGF13 | 0.073 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[ADAMTS19]] | B | FGF13 activity raises ADAMTS19's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without FGF13 | 0.089 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[TSHZ2]] | C | FGF13 activity raises TSHZ2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without FGF13 | 0.003 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[GLI3]] | C | FGF13 activity raises GLI3's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 5.23× lower at baseline in the lines without FGF13 | 0.004 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[LINGO2]] | C | FGF13 activity raises LINGO2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 4.50× lower at baseline in the lines without FGF13 | 0.009 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[VIPR2]] | C | FGF13 activity raises VIPR2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without FGF13 | 0.033 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[LINC01320]] | C | FGF13 activity raises LINC01320's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without FGF13 | 0.050 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.3, 28.9); signed map (34.1, 39.0). **Vector** length 58.2, 17.6% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +25.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +0.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.2 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.1 | -1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3-q27.1 — chrX:138,614,727-139,222,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FHF2, FGF2, FLJ30672; previously LINC00889 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Fibroblast growth factor family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: Phase 0 - rapid depolarisation; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92913](https://www.uniprot.org/uniprotkb/Q92913) (Fibroblast growth factor 13):

> Microtubule-binding protein which directly binds tubulin and is involved in both polymerization and stabilization of microtubules (By similarity). Through its action on microtubules, may participate in the refinement of axons by negatively regulating axonal and leading processes branching (By similarity). Plays a crucial role in neuron polarization and migration in the cerebral cortex and the hippocampus (By similarity). Regulates voltage-gated sodium channel transport and function. May also …

**Summary**, from NCBI Gene [2258](https://www.ncbi.nlm.nih.gov/gene/2258):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth, and invasion. This gene is located in a region on chromosome X, which is associated with Borjeson-Forssman-Lehmann syndrome (BFLS), making it a possible candidate gene for familial cases of …

**Accessions** — [HGNC:3670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3670) · Entrez [2258](https://www.ncbi.nlm.nih.gov/gene/2258) · UniProt [Q92913](https://www.uniprot.org/uniprotkb/Q92913) · Ensembl [ENSG00000129682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129682)

## Data

Gene col 4998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4998); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4998]; `tensor/DDL_lfc|DDL_z.npy` [4998]; `embed/gene_vectors.npy` [4998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4998 or target_col == 4998). Every well: [[FGF13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
