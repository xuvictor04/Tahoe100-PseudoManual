---
symbol: "ABCA13"
type: "gene"
col: 11060
ensembl_id: "ENSG00000179869"
name: "ATP binding cassette subfamily A member 13"
location: "7p12.3"
module: 9
arm: "+"
pooled_cpm: 7.02
n_lines_expressing: 31
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 13
direction_downstream: 6
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ABCA13

*ATP binding cassette subfamily A member 13* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.24× (z +34.3, q 0e+00, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Triamcinolone (drug)]] 5 µM: 0.781× (z -4.0, q 0.030, down in 10 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01592]] (+0.75, fdr 7e-06), [[ADAMTSL1]] (+0.74, fdr 7e-06), [[ASIC2]] (+0.68, fdr 7e-06); moves opposite to [[TTLL5]] (-0.54, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ZNF385D]] → it (grade B ⚠); 6 go from it, the strongest it → [[FRMPD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.24×** | +34.3 | 0e+00 | 20/23 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.16×** | +18.9 | 0e+00 | 18/23 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.02×** | +17.8 | 0e+00 | 5/9 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.04×** | +16.1 | 0e+00 | 8/16 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +14.6 | 0e+00 | 11/23 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +13.0 | 7e-37 | 6/12 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +11.5 | 1e-28 | 16/26 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.50×** | +10.5 | 6e-24 | 16/24 (HEC-1-A, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +10.0 | 7e-22 | 14/24 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +8.2 | 1e-14 | 7/20 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +7.3 | 1e-11 | 9/24 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.2 | 3e-08 | 6/26 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.7 | 7e-07 | 9/24 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.4 | 5e-04 | 7/24 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.2 | 8e-04 | 9/24 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.2 | 1e-03 | 3/22 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 3/26 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.005 | 5/25 (RPMI-7951, SHP-77, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.008 | 0/24 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 5 µM |  | **0.781×** | -4.0 | 0.030 | 10/25 (Hs 766T, HOP62, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.710×** | -3.7 | 0.074 | 10/23 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.736×** | -3.5 | 0.075 | 8/26 (HS-578T, SHP-77, …) | all doses, flat | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.758× | -3.2 | 0.19 | 6/24 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.826× | -3.1 | 0.19 | 1/27 (HOP62) | top dose only |  |
| [[Cilostazol (drug)]] 5 µM |  | 0.758× | -3.1 | 0.19 | 2/25 (SNU-423, AsPC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 122 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.8) |
| [[Hs 766T (line)]] | wt | 45.3 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -12.8) |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0617× (z -9.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.0728× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 8.56 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +21.4) | — |
| [[A-172 (line)]] | wt | 2.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +13.5) | — |
| [[LoVo (line)]] | wt | 2.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 66.1× (z +18.1) | — |
| [[NCI-H1573 (line)]] | alt | 3.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 13.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.0) | — |
| [[SW480 (line)]] | alt | 2.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +12.6) | — |
| [[C32 (line)]] | wt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 5.56 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.0182× (z -13.7) |
| [[KATO III (line)]] | alt | 3.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0561× (z -8.8) |
| [[SNU-423 (line)]] | alt | 6.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +13.5) | — |
| [[A-427 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01592]] | +0.75 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ADAMTSL1]] | +0.74 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ASIC2]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[UNC80]] | +0.68 | +0.73 / +0.58 | both halves | 7e-06 | STRING 417 |
| [[GRIA1]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MIR325HG]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[BAALC]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ZNF385D]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LINC01060]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CACNA1A]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[KCND2]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PECAM1]] | +0.62 | +0.73 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385D]] | B | ZNF385D activity raises ABCA13's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.21× lower at baseline in the lines without ZNF385D | 0.024 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[LINC01605]] | B | LINC01605 activity raises ABCA13's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 1.86× lower at baseline in the lines without LINC01605 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[AIM2]] | B | AIM2 activity raises ABCA13's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without AIM2 | 0.038 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[CDH6]] | B | CDH6 activity raises ABCA13's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without CDH6 | 0.039 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[SHISAL1]] | B | SHISAL1 activity raises ABCA13's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without SHISAL1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[MAGEA10]] | B | MAGEA10 activity raises ABCA13's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 2.53× lower at baseline in the lines without MAGEA10 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425 |
| [[TENM4]] | B | TENM4 activity raises ABCA13's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TENM4 | 0.075 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN |
| [[LINC01287]] | B | LINC01287 activity raises ABCA13's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.55× lower at baseline in the lines without LINC01287 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[COL22A1]] | B | COL22A1 activity raises ABCA13's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without COL22A1 | 0.085 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2 |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises ABCA13's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.93× lower at baseline in the lines without APCDD1L-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[HDAC9]] | B | HDAC9 activity raises ABCA13's level | lines that do not express HDAC9 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without HDAC9 | 0.090 | ⚠ within organs, on part of the lines; also absent: CCDC88A, ETS1, AFAP1L1 |
| [[BAALC]] | C | BAALC activity raises ABCA13's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without BAALC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMPD4]] | B | ABCA13 activity raises FRMPD4's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without ABCA13 | 0.024 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[PTHLH]] | B | ABCA13 activity raises PTHLH's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without ABCA13 | 0.032 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[LINC01500]] | B | ABCA13 activity raises LINC01500's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without ABCA13 | 0.055 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[TIMP3]] | B | ABCA13 activity raises TIMP3's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 3.05× lower at baseline in the lines without ABCA13 | 0.061 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[OFCC1]] | B | ABCA13 activity raises OFCC1's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without ABCA13 | 0.089 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |
| [[SEMA6D]] | B | ABCA13 activity raises SEMA6D's level | lines that do not express ABCA13 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without ABCA13 | 0.094 | ⚠ within organs, on part of the lines; also absent: SHC4, MIR3681HG, LINC02930; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.5, 20.6); signed map (33.7, 27.6). **Vector** length 72.1, 17.2% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +34.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +16.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +18.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +0.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:48,171,458-48,647,497 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33876, FLJ33951 |
| Gene groups (HGNC) | ATP binding cassette subfamily A |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UQ4](https://www.uniprot.org/uniprotkb/Q86UQ4) (ATP-binding cassette sub-family A member 13):

> May mediate the cholesterol and gangliosides transport from the plasma membrane to intracellular vesicles in an ATP hydrolysis dependent manner, thus playing a role in their internalization by endocytic retrograde transport and may also participate in the endocytosis of synaptic vesicle in cortical neurons.

**Summary**, from NCBI Gene [154664](https://www.ncbi.nlm.nih.gov/gene/154664):

> In human, the ATP-binding cassette (ABC) family of transmembrane transporters has at least 48 genes and 7 gene subfamilies. This gene is a member of ABC gene subfamily A (ABCA). Genes within the ABCA family typically encode several thousand amino acids. Like other ABC transmembrane transporter proteins, this protein has 12 or more transmembrane alpha-helix domains that likely arrange to form a single central chamber with multiple substrate binding sites. It is also predicted to have two large …

**Accessions** — [HGNC:14638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14638) · Entrez [154664](https://www.ncbi.nlm.nih.gov/gene/154664) · UniProt [Q86UQ4](https://www.uniprot.org/uniprotkb/Q86UQ4) · Ensembl [ENSG00000179869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179869)

## Data

Gene col 11060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11060); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11060]; `tensor/DDL_lfc|DDL_z.npy` [11060]; `embed/gene_vectors.npy` [11060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11060 or target_col == 11060). Every well: [[ABCA13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
