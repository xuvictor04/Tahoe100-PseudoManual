---
symbol: "CDH3"
type: "gene"
col: 707
ensembl_id: "ENSG00000062038"
name: "cadherin 3"
location: "16q22.1"
module: 155
arm: "+"
pooled_cpm: 23.91
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 54
direction_downstream: 48
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# CDH3

*cadherin 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +13.9, q 3e-41, up in 5 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.481× (z -10.1, q 4e-21, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA1]] (+0.67, fdr 2e-05), [[SLC28A3]] (+0.66, fdr 1e-05), [[TMPRSS4]] (+0.66, fdr 7e-06); moves opposite to [[PGR]] (-0.46, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); 48 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +13.9 | 3e-41 | 5/20 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +12.4 | 7e-33 | 2/13 (HCT15, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +10.3 | 2e-22 | 16/22 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.5 | 2e-19 | 2/16 (HT-29, HCT15) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.3 | 1e-18 | 4/17 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +8.5 | 2e-15 | 13/20 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.003 | 1/20 (LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.32×** | +3.8 | 0.010 | 6/20 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.024 | 2/20 (SW480, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.024 | 3/20 (A-427, BT-474, …) | all doses, flat | position effect removed |
| [[Oxaprozin (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.076 | 2/21 (BT-474, KATO III) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.087 | 1/22 (C-33 A) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.25× | +3.0 | 0.10 | 5/21 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.0 | 0.10 | 3/20 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -10.1 | 4e-21 | 18/21 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.571×** | -7.7 | 4e-12 | 15/20 (BT-474, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -7.4 | 2e-11 | 18/21 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -6.3 | 4e-08 | 17/20 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -5.1 | 4e-05 | 12/21 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -4.8 | 2e-04 | 11/20 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.722×** | -4.5 | 6e-04 | 12/18 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.544×** | -4.4 | 8e-04 | 15/20 (BT-474, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.803×** | -4.3 | 0.001 | 16/21 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.734×** | -4.1 | 0.002 | 14/19 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.743×** | -4.1 | 0.002 | 7/21 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.763×** | -3.7 | 0.009 | 6/20 (BT-474, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.770×** | -3.6 | 0.014 | 17/20 (BT-474, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.772×** | -3.6 | 0.014 | 13/21 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.765×** | -3.6 | 0.014 | 6/20 (BT-474, NCI-H1573, …) | top dose only |  |
| [[Pimozide (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.035 | 0/21 | top dose only | position effect removed |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.066 | 3/21 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.858× | -3.0 | 0.087 | 0/21 | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.799×** | -2.9 | 0.098 | 5/19 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.803×** | -2.9 | 0.098 | 10/19 (LoVo, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 286 | 0 | 31 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -32.8) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0561× (z -21.1) |
| [[NCI-H1573 (line)]] | alt | 62.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0666× (z -23.8) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0602× (z -16.8) |
| [[KATO III (line)]] | alt | 59.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -19.5) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.8) |
| [[LoVo (line)]] | wt | 64.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -21.1) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -11.2) |
| [[LS 180 (line)]] | wt | 55.7 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -20.5) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.257× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 39.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -17.5) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.314× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.9) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HT-29 (line)]] | alt | 8.60 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.17× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SW48 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.83× (z +10.1) | — |
| [[A-172 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA1]] | +0.67 | +0.73 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[SLC28A3]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[TMPRSS4]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[S100A9]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ALOX5]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[P2RY2]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SERPINB3]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[CLDN7]] | +0.62 | +0.65 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 547 |
| [[FGB]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[LGALS9]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.46 | -0.48 / -0.36 | both halves | 1e-04 | STRING 422 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 4, C 50. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises CDH3's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without LMTK3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[ATAD3C]] | B | ATAD3C activity raises CDH3's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.28× lower at baseline in the lines without ATAD3C | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[FAM83E]] | B | FAM83E activity raises CDH3's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 3.04× lower at baseline in the lines without FAM83E | 0.070 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[ARHGAP30]] | B | ARHGAP30 activity raises CDH3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.58× lower at baseline in the lines without ARHGAP30 | 0.099 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[TMEM125]] | C | TMEM125 activity raises CDH3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 6.56× lower at baseline in the lines without TMEM125 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[ST14]] | C | ST14 activity raises CDH3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 6.17× lower at baseline in the lines without ST14 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises CDH3's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 4.96× lower at baseline in the lines without TJP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises CDH3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 6.38× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises CDH3's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 5.44× lower at baseline in the lines without CDH1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[CLDN7]] | C | CLDN7 activity raises CDH3's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 5.33× lower at baseline in the lines without CLDN7 | 0.002 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises CDH3's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 4.80× lower at baseline in the lines without BSPRY | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises CDH3's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 3.78× lower at baseline in the lines without EPHA1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 15, C 33. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | CDH3 activity raises FAM83E's level | lines that do not express CDH3 (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without CDH3 | 0.022 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[TMC6]] | B | CDH3 activity raises TMC6's level | lines that do not express CDH3 (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without CDH3 | 0.025 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| cells under [[Verteporfin (drug)]] 5 µM | B | CDH3 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 0.79× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[LMTK3]] | B | CDH3 activity raises LMTK3's level | lines that do not express CDH3 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without CDH3 | 0.045 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[MYO1D]] | B | CDH3 activity raises MYO1D's level | lines that do not express CDH3 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without CDH3 | 0.046 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | CDH3 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 1.22× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[IQANK1]] | B | CDH3 activity strengthens IQANK1's drug response | lines that do not express CDH3 (10) vs lines expressing it (20) | the lines without CDH3 respond 0.73× as strongly (z diff +1.23); strongest at Homoharringtonine 5 µM: 0.55x vs 0.35x (z diff +3.7) | 0.054 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| cells under [[Posaconazole (drug)]] 5 µM | B | CDH3 activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 1.22× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[TSC22D2]] | B | CDH3 activity raises TSC22D2's level | lines that do not express CDH3 (26) vs lines expressing it (24) | 1.43× lower at baseline in the lines without CDH3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | CDH3 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 0.83× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 5 µM | B | CDH3 activity raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | CDH3 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 1.22× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.7, 56.1); signed map (58.9, 8.7). **Vector** length 79.2, 25.5% of its response variance represented; |z| ≥ 3 in 589 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.59 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.59 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.59 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -10.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,636,189-68,727,468 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHP, PCAD |
| Gene groups (HGNC) | Type I classical cadherins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P22223](https://www.uniprot.org/uniprotkb/P22223) (Cadherin-3):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1001](https://www.ncbi.nlm.nih.gov/gene/1001):

> This gene encodes a classical cadherin of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature glycoprotein. This calcium-dependent cell-cell adhesion protein is comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cytoplasmic tail. This gene is located in a gene cluster in a region on the long arm of chromosome 16 …

**Accessions** — [HGNC:1762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1762) · Entrez [1001](https://www.ncbi.nlm.nih.gov/gene/1001) · UniProt [P22223](https://www.uniprot.org/uniprotkb/P22223) · Ensembl [ENSG00000062038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062038)

## Data

Gene col 707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 707); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 707]; `tensor/DDL_lfc|DDL_z.npy` [707]; `embed/gene_vectors.npy` [707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 707 or target_col == 707). Every well: [[CDH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
