---
symbol: "ELF3-AS1"
type: "gene"
col: 13973
ensembl_id: "ENSG00000234678"
name: "ELF3 antisense RNA 1"
location: "1q32.1"
module: 8
arm: "+"
pooled_cpm: 8.31
n_lines_expressing: 35
n_dd_up: 28
n_dd_down: 7
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 95
direction_downstream: 96
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ELF3-AS1

*ELF3 antisense RNA 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.97× (z +16.0, q 0e+00, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.511× (z -7.0, q 1e-09, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RASSF6]] (+0.76, fdr 7e-06), [[ELF3]] (+0.72, fdr 7e-06, ⚠ same locus), [[ARHGEF38]] (+0.69, fdr 7e-06), [[MVP-DT]] (+0.69, fdr 7e-06); moves opposite to [[SMYD2]] (-0.59, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 95 arrows point to it, the strongest [[TMEM45B]] → it (grade B ⚠); 96 go from it, the strongest it → [[TUFT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.97×** | +16.0 | 0e+00 | 19/27 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +10.9 | 4e-25 | 26/31 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.79×** | +10.3 | 2e-22 | 23/31 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +7.6 | 5e-12 | 25/30 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.9 | 5e-10 | 11/29 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.1 | 1e-07 | 3/12 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.67×** | +5.5 | 3e-06 | 13/31 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +5.5 | 3e-06 | 15/30 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +5.5 | 3e-06 | 17/30 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +5.2 | 1e-05 | 14/30 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.61×** | +5.1 | 2e-05 | 16/31 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +4.8 | 7e-05 | 15/30 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.58×** | +4.8 | 9e-05 | 11/30 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 3e-04 | 12/30 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.002 | 11/30 (LS 180, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.004 | 8/30 (SW480, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.511×** | -7.0 | 1e-09 | 24/31 (HT-29, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -5.4 | 2e-05 | 17/30 (HT-29, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -4.4 | 0.002 | 19/30 (LS 180, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.693×** | -3.8 | 0.019 | 14/32 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -3.6 | 0.031 | 20/30 (COLO 205, HT-29, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.727×** | -3.3 | 0.083 | 13/30 (BT-474, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.083 | 7/31 (AsPC-1, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -16.0) |
| [[HT-29 (line)]] | alt | 30.6 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0641× (z -16.7) |
| [[SW480 (line)]] | alt | 9.23 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 15.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +16.5) | — |
| [[A-172 (line)]] | wt | 2.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.6× (z +13.7) | — |
| [[KATO III (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[LoVo (line)]] | wt | 12.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.146× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 23.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -10.2) |
| [[SNU-423 (line)]] | alt | 3.63 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +11.0) | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0603× (z -8.5) |
| [[A498 (line)]] | wt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +11.0) | — |
| [[A549 (line)]] | wt | 7.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.145× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 6.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 6.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[J82 (line)]] | alt | 2.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.1× (z +14.3) | — |
| [[NCI-H2347 (line)]] | alt | 5.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF6]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[ELF3]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ARHGEF38]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MVP-DT]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.69 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[KRTAP5-AS1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 | same gene group |
| [[RBM47]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[TJP3]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[HHLA2]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TMPRSS3]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ANO9]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TOX3]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD2]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*95 arrows, 95 of them with an alert ⚠; grade A 0, B 72, C 23. Shown: the 12 strongest; 83 more arrows (83 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM45B]] | B | TMEM45B activity raises ELF3-AS1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.53× lower at baseline in the lines without TMEM45B | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TOX3]] | B | TOX3 activity raises ELF3-AS1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.15× lower at baseline in the lines without TOX3 | 8e-05 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[ST14]] | B | ST14 activity raises ELF3-AS1's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.32× lower at baseline in the lines without ST14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[TRIM15]] | B | TRIM15 activity raises ELF3-AS1's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without TRIM15 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ITGB6]] | B | ITGB6 activity raises ELF3-AS1's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 4.15× lower at baseline in the lines without ITGB6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises ELF3-AS1's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.19× lower at baseline in the lines without TMPRSS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[ADGRF1]] | B | ADGRF1 activity raises ELF3-AS1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without ADGRF1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[CYP4F12]] | B | CYP4F12 activity raises ELF3-AS1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 3.76× lower at baseline in the lines without CYP4F12 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises ELF3-AS1's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.46× lower at baseline in the lines without ARHGEF38 | 5e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[LINC02967]] | B | LINC02967 activity raises ELF3-AS1's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 4.12× lower at baseline in the lines without LINC02967 | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[VNN1]] | B | VNN1 activity raises ELF3-AS1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without VNN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[PLEKHG6]] | B | PLEKHG6 activity raises ELF3-AS1's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 3.48× lower at baseline in the lines without PLEKHG6 | 0.002 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |

### Downstream of this gene

*96 arrows, 96 of them with an alert ⚠; grade A 0, B 74, C 22. Shown: the 12 strongest; 84 more arrows (84 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUFT1]] | B | ELF3-AS1 activity raises TUFT1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.04× lower at baseline in the lines without ELF3-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[BAG1]] | B | ELF3-AS1 activity raises BAG1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without ELF3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[CASP10]] | B | ELF3-AS1 activity raises CASP10's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.32× lower at baseline in the lines without ELF3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[CARD14]] | B | ELF3-AS1 activity raises CARD14's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without ELF3-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[ZSCAN16]] | B | ELF3-AS1 activity raises ZSCAN16's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without ELF3-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[PDZK1IP1]] | B | ELF3-AS1 activity raises PDZK1IP1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.02× lower at baseline in the lines without ELF3-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[DTX2]] | B | ELF3-AS1 activity raises DTX2's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without ELF3-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[DDR1]] | B | ELF3-AS1 activity raises DDR1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without ELF3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LITAF]] | B | ELF3-AS1 activity raises LITAF's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without ELF3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[RASEF]] | B | ELF3-AS1 activity raises RASEF's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.97× lower at baseline in the lines without ELF3-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[TMC5]] | B | ELF3-AS1 activity raises TMC5's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 4.15× lower at baseline in the lines without ELF3-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[ADGRG1]] | B | ELF3-AS1 activity raises ADGRG1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without ELF3-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 53.6); signed map (58.7, 3.3). **Vector** length 96.1, 27.4% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | +5.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | ELF3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.1 — chr1:201,995,696-202,010,463 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000415582, SCAT7 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40211) · Entrez [102723465](https://www.ncbi.nlm.nih.gov/gene/102723465) · Ensembl [ENSG00000234678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234678)

## Data

Gene col 13973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13973); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13973]; `tensor/DDL_lfc|DDL_z.npy` [13973]; `embed/gene_vectors.npy` [13973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13973 or target_col == 13973). Every well: [[ELF3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELF3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
