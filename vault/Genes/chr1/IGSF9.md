---
symbol: "IGSF9"
type: "gene"
col: 1432
ensembl_id: "ENSG00000085552"
name: "immunoglobulin superfamily member 9"
location: "1q23.2"
module: 31
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 34
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 32
direction_downstream: 30
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# IGSF9

*immunoglobulin superfamily member 9* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.17× (z +8.4, q 2e-14, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.406× (z -7.0, q 2e-09, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC52A3]] (+0.68, fdr 7e-06), [[PRSS3]] (+0.68, fdr 7e-06), [[SLC5A1]] (+0.67, fdr 7e-06); moves opposite to [[KRIT1]] (-0.52, fdr 4e-05), [[PUS10]] (-0.51, fdr 2e-04), [[IFT74]] (-0.51, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); 30 go from it, the strongest it → [[CYP2S1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +8.4 | 2e-14 | 16/30 (NCI-H2347, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +8.1 | 2e-13 | 2/3 (NCI-H2347, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +6.1 | 2e-07 | 12/24 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +6.1 | 2e-07 | 15/30 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +4.8 | 2e-04 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +4.6 | 4e-04 | 12/29 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +4.5 | 5e-04 | 2/8 (NCI-H2347, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +4.2 | 0.002 | 11/31 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.004 | 12/31 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.23×** | +3.2 | 0.073 | 0/2 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.406×** | -7.0 | 2e-09 | 20/31 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -6.7 | 7e-09 | 16/23 (NCI-H2347, HT-29, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.575×** | -6.1 | 3e-07 | 16/22 (Hs 766T, HT-29, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.447×** | -6.0 | 3e-07 | 13/27 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.495×** | -5.4 | 6e-06 | 14/27 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.543×** | -4.7 | 2e-04 | 11/25 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.5 | 0.038 | 7/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Resveratrol (drug)]] 5 µM |  | **0.746×** | -3.2 | 0.091 | 4/30 (SW 900, AsPC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.096 | 11/20 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.657× | -3.1 | 0.10 | 2/23 (KATO III, BT-474) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0227× (z -22.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0706× (z -10.6) |
| [[HT-29 (line)]] | alt | 5.88 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0277× (z -19.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -11.1) |
| [[LS 180 (line)]] | wt | 4.61 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -12.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.4) |
| [[HOP62 (line)]] | alt | 2.19 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0765× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0231× (z -9.8) |
| [[LoVo (line)]] | wt | 5.77 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0636× (z -10.4) |
| [[SW480 (line)]] | alt | 3.58 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0552× (z -9.9) |
| [[BT-474 (line)]] | alt | 6.58 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0584× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 3.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0427× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 2.00 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0530× (z -8.7) |
| [[A-172 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.737 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC52A3]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP8]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ANO1]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CYP4F12]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[PRR5-ARHGAP8]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PRR5]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRIT1]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PUS10]] | -0.51 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[IFT74]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.50 | -0.48 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 31, C 1. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity raises IGSF9's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without SERPINB5 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[C1orf116]] | B | C1orf116 activity raises IGSF9's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without C1orf116 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[LINC01133]] | B | LINC01133 activity raises IGSF9's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 2.14× lower at baseline in the lines without LINC01133 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1 |
| [[LINC01819]] | B | LINC01819 activity raises IGSF9's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without LINC01819 | 0.008 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[PLEKHG6]] | B | PLEKHG6 activity raises IGSF9's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without PLEKHG6 | 0.008 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[ANO1]] | B | ANO1 activity raises IGSF9's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without ANO1 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[LINC00589]] | B | LINC00589 activity raises IGSF9's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without LINC00589 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[TINAGL1]] | B | TINAGL1 activity raises IGSF9's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.62× lower at baseline in the lines without TINAGL1 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[P2RY2]] | B | P2RY2 activity raises IGSF9's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without P2RY2 | 0.019 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[LGR6]] | B | LGR6 activity raises IGSF9's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 2.23× lower at baseline in the lines without LGR6 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2 |
| [[FA2H]] | B | FA2H activity raises IGSF9's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without FA2H | 0.022 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[KLK10]] | B | KLK10 activity raises IGSF9's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.04× lower at baseline in the lines without KLK10 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP2S1]] | B | IGSF9 activity raises CYP2S1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without IGSF9 | 0.015 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[MAPK11]] | B | IGSF9 activity lowers MAPK11's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.25× higher at baseline in the lines without IGSF9 | 0.048 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[PPARG]] | B | IGSF9 activity raises PPARG's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without IGSF9 | 0.054 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[TNS4]] | B | IGSF9 activity raises TNS4's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without IGSF9 | 0.055 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[OXSR1]] | B | IGSF9 activity raises OXSR1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without IGSF9 | 0.058 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[IL22RA1]] | B | IGSF9 activity raises IL22RA1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without IGSF9 | 0.065 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | B | IGSF9 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 1.28× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | B | IGSF9 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 0.83× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[ANO1]] | B | IGSF9 activity raises ANO1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.45× lower at baseline in the lines without IGSF9 | 0.075 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | IGSF9 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 0.89× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[DYRK2]] | B | IGSF9 activity raises DYRK2's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without IGSF9 | 0.079 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[SLC6A20]] | B | IGSF9 activity raises SLC6A20's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without IGSF9 | 0.080 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, 53.9); signed map (0.4, 39.4). **Vector** length 56.0, 11.4% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.0 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -7.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin superfamily member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:159,927,039-159,945,613 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1355, Nrt1, IGSF9A |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2J2](https://www.uniprot.org/uniprotkb/Q9P2J2) (Protein turtle homolog A):

> Functions in dendrite outgrowth and synapse maturation.

**Summary**, from NCBI Gene [57549](https://www.ncbi.nlm.nih.gov/gene/57549):

> Predicted to enable cell-cell adhesion mediator activity. Predicted to be involved in axon guidance; dendrite self-avoidance; and homophilic cell-cell adhesion. Predicted to act upstream of or within dendrite development and regulation of synapse organization. Predicted to be located in dendrite and inhibitory synapse. Predicted to be active in axon and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18132) · Entrez [57549](https://www.ncbi.nlm.nih.gov/gene/57549) · UniProt [Q9P2J2](https://www.uniprot.org/uniprotkb/Q9P2J2) · Ensembl [ENSG00000085552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085552)

## Data

Gene col 1432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1432); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1432]; `tensor/DDL_lfc|DDL_z.npy` [1432]; `embed/gene_vectors.npy` [1432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1432 or target_col == 1432). Every well: [[IGSF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGSF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
