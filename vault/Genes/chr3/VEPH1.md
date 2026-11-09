---
symbol: "VEPH1"
type: "gene"
col: 12395
ensembl_id: "ENSG00000197415"
name: "ventricular zone expressed PH domain containing 1"
location: "3q25.31-q25.32"
module: 13
arm: "+"
pooled_cpm: 19.64
n_lines_expressing: 24
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 33
direction_downstream: 33
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# VEPH1

*ventricular zone expressed PH domain containing 1* — 3q25.31-q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +18.4, q 0e+00, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.759× (z -3.9, q 0.050, down in 1 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.71, fdr 7e-06), [[RFX8]] (+0.70, fdr 7e-06), [[NLRP3]] (+0.69, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); 33 go from it, the strongest it → [[SH2B3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +18.4 | 0e+00 | 8/22 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +16.1 | 0e+00 | 3/12 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +13.8 | 7e-41 | 6/17 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +9.7 | 5e-20 | 4/16 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +9.2 | 5e-18 | 9/22 (SW480, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +7.5 | 5e-12 | 6/22 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.6 | 3e-09 | 9/21 (A-172, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +6.1 | 1e-07 | 6/22 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.7 | 6e-07 | 7/21 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +5.4 | 4e-06 | 3/19 (A-172, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +4.6 | 2e-04 | 1/20 (A-172) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +3.8 | 0.007 | 7/21 (HEC-1-A, A-172, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.28×** | +3.5 | 0.021 | 2/18 (HEC-1-A, NCI-H23) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.030 | 2/21 (C32, SK-MEL-2) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.038 | 2/21 (C32, SW480) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.039 | 0/21 | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.040 | 1/21 (COLO 205) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.759×** | -3.9 | 0.050 | 1/22 (SW 1088) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.779×** | -3.5 | 0.084 | 8/21 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.084 | 8/21 (H4, LOX-IMVI, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.720× | -3.3 | 0.13 | 0/22 | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.653× | -3.1 | 0.16 | 4/22 (J82, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.789× | -3.1 | 0.16 | 8/21 (RKO, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.804× | -3.1 | 0.16 | 9/21 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.807× | -3.0 | 0.16 | 3/21 (H4, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 187 | 0 | 18 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0597× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 163 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 112 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.1) |
| [[H4 (line)]] | wt | 23.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0362× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0617× (z -9.5) |
| [[HOP62 (line)]] | alt | 68.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.7) |
| [[A-172 (line)]] | wt | 6.64 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0707× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.564× (z -9.3) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 47.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.71 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RFX8]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[NLRP3]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[TMEM200A]] | +0.67 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[RDUR]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[FGF5]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTS12]] | +0.63 | +0.65 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[INSYN2B]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ADAMTS18]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[AK5]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 5, C 28. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises VEPH1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without BCL2A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[ADAMTS6]] | B | ADAMTS6 activity raises VEPH1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.59× lower at baseline in the lines without ADAMTS6 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[RPSAP52]] | B | RPSAP52 activity raises VEPH1's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without RPSAP52 | 0.082 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[ARHGAP22]] | B | ARHGAP22 activity raises VEPH1's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.35× lower at baseline in the lines without ARHGAP22 | 0.089 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[GDNF-AS1]] | B | GDNF-AS1 activity raises VEPH1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without GDNF-AS1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[ROBO4]] | C | ROBO4 activity raises VEPH1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 4.77× lower at baseline in the lines without ROBO4 | 7e-04 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01812]] | C | LINC01812 activity raises VEPH1's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 5.00× lower at baseline in the lines without LINC01812 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises VEPH1's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 4.09× lower at baseline in the lines without FGF5 | 0.003 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[CCDC190]] | C | CCDC190 activity raises VEPH1's level | lines that do not express CCDC190 (38) vs lines expressing it (12) | 4.69× lower at baseline in the lines without CCDC190 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SIM1, RGS4, ENSG00000254337; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises VEPH1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 4.46× lower at baseline in the lines without LNCOG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises VEPH1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 3.61× lower at baseline in the lines without ADTRP | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises VEPH1's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 3.10× lower at baseline in the lines without RGS4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 9, C 24. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH2B3]] | B | VEPH1 activity raises SH2B3's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without VEPH1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[IQCJ-SCHIP1]] | B | VEPH1 activity raises IQCJ-SCHIP1's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.88× lower at baseline in the lines without VEPH1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[GDNF-AS1]] | B | VEPH1 activity raises GDNF-AS1's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without VEPH1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[APCDD1L-DT]] | B | VEPH1 activity raises APCDD1L-DT's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without VEPH1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[LINC02454]] | B | VEPH1 activity raises LINC02454's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without VEPH1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[ARHGAP22]] | B | VEPH1 activity raises ARHGAP22's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 3.39× lower at baseline in the lines without VEPH1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[RPSAP52]] | B | VEPH1 activity raises RPSAP52's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.41× lower at baseline in the lines without VEPH1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| cells under [[Daptomycin (drug)]] 0.5 µM | B | VEPH1 activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express VEPH1 (26) vs lines expressing it (22) | the lines without VEPH1: 1.35× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; cell counts less trustworthy |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | B | VEPH1 activity lowers the cells' numbers under Doxorubicin (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express VEPH1 (26) vs lines expressing it (22) | the lines without VEPH1: 1.64× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[FGF5]] | C | VEPH1 activity raises FGF5's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without VEPH1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[COL6A3]] | C | VEPH1 activity raises COL6A3's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 4.87× lower at baseline in the lines without VEPH1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[ROBO4]] | C | VEPH1 activity raises ROBO4's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without VEPH1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, 13.4); signed map (18.9, 47.2). **Vector** length 77.1, 21.4% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ventricular zone expressed PH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31-q25.32 — chr3:157,259,742-157,533,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12604, KIAA1692 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14D04](https://www.uniprot.org/uniprotkb/Q14D04) (Ventricular zone-expressed PH domain-containing protein homolog 1):

> Interacts with TGF-beta receptor type-1 (TGFBR1) and inhibits dissociation of activated SMAD2 from TGFBR1, impeding its nuclear accumulation and resulting in impaired TGF-beta signaling. May also affect FOXO, Hippo and Wnt signaling.

**Summary**, from NCBI Gene [79674](https://www.ncbi.nlm.nih.gov/gene/79674):

> Predicted to enable phosphatidylinositol-5-phosphate binding activity. Involved in negative regulation of SMAD protein signal transduction and negative regulation of transforming growth factor beta receptor signaling pathway. Predicted to be located in endomembrane system. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:25735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25735) · Entrez [79674](https://www.ncbi.nlm.nih.gov/gene/79674) · UniProt [Q14D04](https://www.uniprot.org/uniprotkb/Q14D04) · Ensembl [ENSG00000197415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197415)

## Data

Gene col 12395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12395); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12395]; `tensor/DDL_lfc|DDL_z.npy` [12395]; `embed/gene_vectors.npy` [12395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12395 or target_col == 12395). Every well: [[VEPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
