---
symbol: "SLC22A3"
type: "gene"
col: 7100
ensembl_id: "ENSG00000146477"
name: "solute carrier family 22 member 3"
location: "6q25.3"
module: 73
arm: "+"
pooled_cpm: 28.97
n_lines_expressing: 20
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 32
direction_downstream: 58
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SLC22A3

*solute carrier family 22 member 3* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +15.0, q 0e+00, up in 10 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.412× (z -11.6, q 3e-28, down in 17 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL2RG]] (+0.66, fdr 1e-05), [[SEPTIN9-DT]] (+0.63, fdr 1e-05), [[BAIAP2L2]] (+0.61, fdr 1e-05); moves opposite to [[UBAC1]] (-0.51, fdr 5e-05), [[HACE1]] (-0.50, fdr 9e-05), [[ARRB2]] (-0.50, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); 58 go from it, the strongest it → [[HACE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +15.0 | 0e+00 | 10/18 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +14.8 | 0e+00 | 5/18 (HepG2/C3A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +11.2 | 4e-27 | 3/18 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +9.9 | 7e-21 | 5/17 (HepG2/C3A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +8.7 | 4e-16 | 11/18 (COLO 205, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +8.4 | 4e-15 | 13/18 (RPMI-7951, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.8 | 6e-10 | 2/15 (A498, HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.2 | 5e-08 | 2/18 (RPMI-7951, HepG2/C3A) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.0 | 4e-05 | 4/18 (SW480, AsPC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 0/18 | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 5/18 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.005 | 5/18 (NCI-H1792, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.006 | 4/18 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.5 | 0.018 | 0/18 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.046 | 1/18 (Panc 03.27) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.046 | 0/18 | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.054 | 5/18 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.071 | 6/18 (J82, NCI-H1573, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.071 | 1/18 (HT-29) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.412×** | -11.6 | 3e-28 | 17/18 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -8.9 | 1e-16 | 18/18 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.544×** | -8.0 | 3e-13 | 17/18 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -5.4 | 1e-05 | 14/18 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.700×** | -4.3 | 0.002 | 7/18 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.776×** | -3.8 | 0.012 | 8/18 (LS 180, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.756×** | -3.7 | 0.020 | 11/18 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.767×** | -3.5 | 0.037 | 9/18 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.773×** | -3.4 | 0.047 | 0/18 | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.793× | -3.1 | 0.12 | 9/18 (AsPC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 85.2 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0656× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0828× (z -17.3) |
| [[LS 180 (line)]] | wt | 76.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -15.2) |
| [[SW480 (line)]] | alt | 64.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -20.1) |
| [[KATO III (line)]] | alt | 37.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -13.0) |
| [[LoVo (line)]] | wt | 41.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -13.4) |
| [[A498 (line)]] | wt | 94.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -13.9) |
| [[A549 (line)]] | wt | 89.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0755× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 205 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 61.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -12.6) |
| [[COLO 205 (line)]] | alt | 68.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0936× (z -15.5) |
| [[HT-29 (line)]] | alt | 48.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 80.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 17.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.131× (z -9.8) |
| [[SW1417 (line)]] | alt | 29.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 16.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 9.23× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL2RG]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN9-DT]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BAIAP2L2]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ACSL5]] | +0.61 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[INPP1]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GPR39]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TNS4]] | +0.60 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CFAP46]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[LINC02582]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[NEMP2-DT]] | +0.59 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[TRABD2A]] | +0.58 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[NOSTRIN]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBAC1]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[HACE1]] | -0.50 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[ARRB2]] | -0.50 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[HSDL1]] | -0.49 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[FAM234B]] | -0.48 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[WDR54]] | -0.47 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[VKORC1]] | -0.47 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[CRYZL1]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[ARMC2]] | -0.46 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 4, C 28. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity raises SLC22A3's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 4.23× lower at baseline in the lines without PLEKHA6 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises SLC22A3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises SLC22A3's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[GPR39]] | B | GPR39 activity raises SLC22A3's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 3.83× lower at baseline in the lines without GPR39 | 0.089 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[IL2RG]] | C | IL2RG activity raises SLC22A3's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 4.18× lower at baseline in the lines without IL2RG | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises SLC22A3's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 4.83× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises SLC22A3's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 7.52× lower at baseline in the lines without HNF4A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[MYO7B]] | C | MYO7B activity raises SLC22A3's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 4.40× lower at baseline in the lines without MYO7B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises SLC22A3's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 4.83× lower at baseline in the lines without HSD17B2 | 0.003 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises SLC22A3's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 5.12× lower at baseline in the lines without FOXQ1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |
| [[IL20RA]] | C | IL20RA activity raises SLC22A3's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 5.53× lower at baseline in the lines without IL20RA | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10; co-absent with the target |
| [[PPARG]] | C | PPARG activity raises SLC22A3's level | lines that do not express PPARG (20) vs lines expressing it (30) | 4.80× lower at baseline in the lines without PPARG | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL; co-absent with the target |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 21, C 37. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | B | SLC22A3 activity lowers HACE1's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.15× higher at baseline in the lines without SLC22A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[BAIAP2L2]] | B | SLC22A3 activity raises BAIAP2L2's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without SLC22A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[KLF3]] | B | SLC22A3 activity raises KLF3's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without SLC22A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[PLEKHA6]] | B | SLC22A3 activity raises PLEKHA6's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 3.15× lower at baseline in the lines without SLC22A3 | 0.014 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[SH2D4A]] | B | SLC22A3 activity raises SH2D4A's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without SLC22A3 | 0.018 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[MFSD6]] | B | SLC22A3 activity raises MFSD6's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SLC22A3 | 0.019 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[PSD4]] | B | SLC22A3 activity raises PSD4's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without SLC22A3 | 0.026 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[HAS3]] | B | SLC22A3 activity raises HAS3's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without SLC22A3 | 0.029 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[ADAP1]] | B | SLC22A3 activity raises ADAP1's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without SLC22A3 | 0.034 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[NAB1]] | B | SLC22A3 activity raises NAB1's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without SLC22A3 | 0.045 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[WDR54]] | B | SLC22A3 activity lowers WDR54's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 1.86× higher at baseline in the lines without SLC22A3 | 0.048 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[EFNB2]] | B | SLC22A3 activity raises EFNB2's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without SLC22A3 | 0.050 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.4, 48.5); signed map (5.1, 35.5). **Vector** length 69.3, 22.0% of its response variance represented; |z| ≥ 3 in 536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +15.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.0 | -11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.5 | -8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 22 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:160,348,378-160,452,577 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCT3, EMT |
| Gene groups (HGNC) | Solute carrier family 22 |
| Reactome | 6 pathways, smallest: Abacavir transmembrane transport; Abacavir ADME; SLC-mediated transport of organic cations |
| Matched by | ensembl_id |

**Function**, from UniProt [O75751](https://www.uniprot.org/uniprotkb/O75751) (Solute carrier family 22 member 3):

> Electrogenic voltage-dependent uniporter that mediates the transport of a variety of organic cations such as endogenous bioactive amines, cationic drugs and xenobiotics. Cation cellular uptake or release is driven by the electrochemical potential, i.e. membrane potential and concentration gradient. Functions as a Na(+)- and Cl(-)-independent, bidirectional uniporter. Implicated in monoamine neurotransmitters uptake such as dopamine, adrenaline/epinephrine, noradrenaline/norepinephrine, …

**Summary**, from NCBI Gene [6581](https://www.ncbi.nlm.nih.gov/gene/6581):

> Polyspecific organic cation transporters in the liver, kidney, intestine, and other organs are critical for elimination of many endogenous small organic cations as well as a wide array of drugs and environmental toxins. This gene is one of three similar cation transporter genes located in a cluster on chromosome 6. The encoded protein contains twelve putative transmembrane domains and is a plasma integral membrane protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10967) · Entrez [6581](https://www.ncbi.nlm.nih.gov/gene/6581) · UniProt [O75751](https://www.uniprot.org/uniprotkb/O75751) · Ensembl [ENSG00000146477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146477)

## Data

Gene col 7100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7100); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7100]; `tensor/DDL_lfc|DDL_z.npy` [7100]; `embed/gene_vectors.npy` [7100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7100 or target_col == 7100). Every well: [[SLC22A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC22A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
