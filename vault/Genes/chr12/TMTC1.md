---
symbol: "TMTC1"
type: "gene"
col: 5465
ensembl_id: "ENSG00000133687"
name: "transmembrane O-mannosyltransferase targeting cadherins 1"
location: "12p11.22"
module: 104
arm: "+"
pooled_cpm: 25.43
n_lines_expressing: 25
n_dd_up: 51
n_dd_down: 4
n_dd_up_clean: 40
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# TMTC1

*transmembrane O-mannosyltransferase targeting cadherins 1* — 12p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.09× (z +16.3, q 0e+00, up in 18 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.732× (z -6.9, q 4e-09, down in 14 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP2]] (+0.71, fdr 7e-06), [[DCN]] (+0.64, fdr 1e-05), [[RIPOR2]] (+0.64, fdr 1e-05); moves opposite to [[TMEM158]] (-0.58, fdr 1e-05), [[BCL2A1]] (-0.58, fdr 1e-05), [[GDNF]] (-0.50, fdr 4e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SORBS2]] → it (grade B ⚠); 3 go from it, the strongest it → [[NEBL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.09×** | +16.3 | 0e+00 | 18/23 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **1.76×** | +12.4 | 5e-33 | 15/23 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +10.1 | 5e-22 | 17/23 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +10.1 | 5e-22 | 1/15 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.88×** | +9.9 | 7e-21 | 15/23 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +9.0 | 2e-17 | 1/21 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **1.74×** | +8.6 | 6e-16 | 13/23 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.46×** | +8.3 | 7e-15 | 13/23 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +8.3 | 8e-15 | 17/23 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.1 | 2e-14 | 7/23 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.68×** | +8.1 | 3e-14 | 14/23 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.65×** | +7.8 | 4e-13 | 13/23 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.57×** | +7.1 | 7e-11 | 12/23 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.56×** | +7.0 | 1e-10 | 13/24 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.59×** | +7.0 | 1e-10 | 14/23 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +6.7 | 7e-10 | 10/23 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.58×** | +6.6 | 1e-09 | 13/21 (NCI-H460, SNU-423, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.49×** | +6.2 | 2e-08 | 9/21 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.732×** | -6.9 | 4e-09 | 14/24 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.709×** | -5.4 | 2e-05 | 13/22 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Fluvoxamine (drug)]] 5 µM |  | **0.765×** | -4.0 | 0.012 | 6/23 (SW 900, SW 1088, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.8 | 0.022 | 2/24 (C-33 A, NCI-H661) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.798×** | -3.5 | 0.051 | 8/22 (C-33 A, A-172, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.803× | -3.3 | 0.10 | 5/23 (AsPC-1, A498, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.816× | -3.0 | 0.17 | 1/23 (NCI-H1573) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.05 µM | ⚠ position correction uncertain | 0.822× | -3.0 | 0.17 | 3/23 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.7 | 23 (1 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 3.07× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 30.3 | 15 (1 ⚠) | 0 | [[Budesonide (drug)]] 5 µM 6.14× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 8 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 8.58× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 246 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -18.2) |
| [[C32 (line)]] | wt | 58.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +12.8) ⚠ position correction uncertain · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 67.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.8) ⚠ position correction uncertain · without an alert: [[Triamcinolone (drug)]] 5 µM 2.83× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 9.91 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.54× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0856× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 11.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.91× (z +12.0) | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.220× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.115× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[BT-474 (line)]] | alt | 7.15 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.3) ⚠ position correction uncertain | — |
| [[J82 (line)]] | alt | 73.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +9.2) | — |
| [[A-172 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[DCN]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[RIPOR2]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[PID1]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[KLF9]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ACSL1]] | +0.62 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[AMPH]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 | **novel candidate** |
| [[IL1R1]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[TSC22D3]] | +0.60 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[STXBP5]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 | same gene group |
| [[IRAK3]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[BCL2A1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[GDNF]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SIGLEC15]] | -0.46 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[IL11]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ANTXR2]] | -0.44 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[INSYN2B]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SH2D2A]] | -0.44 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[PLAUR]] | -0.44 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORBS2]] | B | SORBS2 activity raises TMTC1's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without SORBS2 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[MTMR7]] | B | MTMR7 activity raises TMTC1's level | lines that do not express MTMR7 (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without MTMR7 | 0.024 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[RIPOR2]] | B | RIPOR2 activity raises TMTC1's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 3.89× lower at baseline in the lines without RIPOR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[LTBP1]] | B | LTBP1 activity raises TMTC1's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without LTBP1 | 0.056 | ⚠ within organs, on part of the lines |
| [[CMKLR2]] | B | CMKLR2 activity raises TMTC1's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without CMKLR2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[ENPP2]] | C | ENPP2 activity raises TMTC1's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without ENPP2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |
| [[SNAI2]] | C | SNAI2 activity raises TMTC1's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 3.74× lower at baseline in the lines without SNAI2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT; co-absent with the target |
| [[DNER]] | C | DNER activity raises TMTC1's level | lines that do not express DNER (32) vs lines expressing it (18) | 4.54× lower at baseline in the lines without DNER | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000222032, APCDD1L, GYPC; co-absent with the target |
| [[RNF175]] | C | RNF175 activity raises TMTC1's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 3.36× lower at baseline in the lines without RNF175 | 0.084 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises TMTC1's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 5.46× lower at baseline in the lines without PRR16 | 0.092 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEBL]] | B | TMTC1 activity lowers NEBL's level | lines that do not express TMTC1 (25) vs lines expressing it (25) | 1.82× higher at baseline in the lines without TMTC1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000255983, CNRIP1, ADAM23 |
| [[ABLIM3]] | B | TMTC1 activity strengthens ABLIM3's drug response | lines that do not express TMTC1 (16) vs lines expressing it (18) | the lines without TMTC1 respond 0.58× as strongly (z diff +1.97); strongest at Budesonide 5 µM: 1.37x vs 2.57x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000255983, CNRIP1, ADAM23; target measured in part of the lines; the reference differs |
| [[DAAM2]] | C | TMTC1 activity raises DAAM2's level | lines that do not express TMTC1 (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without TMTC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000255983, CNRIP1, ADAM23; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, 16.8); signed map (18.9, 32.0). **Vector** length 89.0, 25.3% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +10.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +9.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.0 | +8.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.9 | +7.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.6 | +8.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM | ⚠ position correction uncertain | -1.5 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | +1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane O-mannosyltransferase targeting cadherins 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.22 — chr12:29,500,840-29,784,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARG99, OLF, FLJ31400, FLJ41625 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Transmembrane O-mannosyltransferase targeting cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUR5](https://www.uniprot.org/uniprotkb/Q8IUR5) (Protein O-mannosyl-transferase TMTC1):

> Transfers mannosyl residues to the hydroxyl group of serine or threonine residues. The 4 members of the TMTC family are O-mannosyl-transferases dedicated primarily to the cadherin superfamily, each member seems to have a distinct role in decorating the cadherin domains with O-linked mannose glycans at specific regions. Also acts as O-mannosyl-transferase on other proteins such as PDIA3.

**Summary**, from NCBI Gene [83857](https://www.ncbi.nlm.nih.gov/gene/83857):

> Enables dolichyl-phosphate-mannose-protein mannosyltransferase activity. Involved in protein O-linked glycosylation via mannose. Predicted to be located in endoplasmic reticulum and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24099) · Entrez [83857](https://www.ncbi.nlm.nih.gov/gene/83857) · UniProt [Q8IUR5](https://www.uniprot.org/uniprotkb/Q8IUR5) · Ensembl [ENSG00000133687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133687)

## Data

Gene col 5465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5465); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5465]; `tensor/DDL_lfc|DDL_z.npy` [5465]; `embed/gene_vectors.npy` [5465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5465 or target_col == 5465). Every well: [[TMTC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMTC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
