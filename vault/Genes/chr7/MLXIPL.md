---
symbol: "MLXIPL"
type: "gene"
col: 194
ensembl_id: "ENSG00000009950"
name: "MLX interacting protein like"
location: "7q11.23"
module: 115
arm: "+"
pooled_cpm: 9.78
n_lines_expressing: 37
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 16
direction_downstream: 12
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# MLXIPL

*MLX interacting protein like* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.73× (z +18.1, q 0e+00, up in 28 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.599× (z -7.0, q 1e-09, down in 14 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGSM1]] (+0.67, fdr 1e-05), [[SBK1]] (+0.64, fdr 1e-05), [[LMTK3]] (+0.62, fdr 1e-05); moves opposite to [[KIAA0825]] (-0.51, fdr 4e-04), [[ZMPSTE24]] (-0.50, fdr 7e-05), [[MCTS1]] (-0.49, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[YBX2]] → it (grade B ⚠); 12 go from it, the strongest it → [[CFD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.73×** | +18.1 | 0e+00 | 28/33 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.30×** | +16.2 | 0e+00 | 25/33 (HT-29, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.04×** | +15.3 | 0e+00 | 25/33 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +14.4 | 1e-44 | 23/33 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +10.9 | 1e-25 | 23/33 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +10.3 | 7e-23 | 22/33 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.6 | 6e-16 | 5/23 (NCI-H460, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.0 | 1e-10 | 3/13 (HepG2/C3A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.0 | 2e-10 | 9/29 (A549, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.9 | 3e-10 | 3/16 (HEC-1-A, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 2e-07 | 15/30 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +5.7 | 5e-07 | 21/32 (MIA PaCa-2, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.6 | 1e-06 | 9/29 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 7e-04 | 6/30 (HT-29, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.021 | 7/34 (AsPC-1, HCT15, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.022 | 6/33 (SW480, HCT15, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.047 | 1/31 (BT-474) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.049 | 1/32 (SW 900) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -7.0 | 1e-09 | 14/26 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.608×** | -6.8 | 2e-09 | 16/33 (NCI-H1792, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -5.7 | 2e-06 | 17/30 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -5.3 | 2e-05 | 17/31 (LoVo, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -5.2 | 2e-05 | 12/33 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.746×** | -4.0 | 0.006 | 18/33 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.014 | 8/32 (SW48, SW480, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.758×** | -3.7 | 0.018 | 8/33 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.786×** | -3.3 | 0.061 | 13/33 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.846× | -3.3 | 0.061 | 7/33 (MIA PaCa-2, LS 180, …) | top dose only | position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.789×** | -3.2 | 0.061 | 2/33 (RKO, NCI-H2030) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.785×** | -3.2 | 0.067 | 13/31 (LoVo, NCI-H2030, …) | two highest doses | composition shift |
| [[Cilostazol (drug)]] 0.05 µM |  | **0.783×** | -3.1 | 0.084 | 2/32 (RKO, AsPC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.46 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.78× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.239× (z -8.9) |
| [[HT-29 (line)]] | alt | 3.94 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 12.5× (z +12.7) | — |
| [[KATO III (line)]] | alt | 36.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 5.02 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.63× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 13.2 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.36× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 3.85 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 17.7× (z +9.0) | — |
| [[LoVo (line)]] | wt | 55.7 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.121× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -13.3) |
| [[SW480 (line)]] | alt | 18.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 8.03 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0878× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 3.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.49× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0185× (z -22.3) |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.74 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.104× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0641× (z -11.3) |
| [[SW48 (line)]] | wt | 43.0 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.178× (z -9.9) |
| [[A-172 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGSM1]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SBK1]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LMTK3]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LLGL2]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[FAM118A]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SLC29A4]] | +0.59 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[SHF]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PRR5]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[CCDC88B]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CHKA]] | +0.57 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[SLC29A2]] | +0.56 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[SREBF2]] | +0.56 | +0.41 / +0.44 | both halves | 4e-05 | same gene group; STRING 688 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA0825]] | -0.51 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[ZMPSTE24]] | -0.50 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[MCTS1]] | -0.49 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | -0.49 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[WDR33]] | -0.48 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[C8orf33]] | -0.47 | -0.30 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 8, C 8. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises MLXIPL's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without YBX2 | 0.006 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[LMTK3]] | B | LMTK3 activity raises MLXIPL's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without LMTK3 | 0.024 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity raises MLXIPL's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without MCF2L | 0.042 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[SYTL1]] | B | SYTL1 activity raises MLXIPL's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without SYTL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[CBLC]] | B | CBLC activity raises MLXIPL's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without CBLC | 0.072 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[KIF1A]] | B | KIF1A activity raises MLXIPL's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.23× lower at baseline in the lines without KIF1A | 0.080 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[BTNL9]] | B | BTNL9 activity raises MLXIPL's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without BTNL9 | 0.081 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises MLXIPL's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without ZDHHC11B | 0.092 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[HES2]] | C | HES2 activity raises MLXIPL's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without HES2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2; co-absent with the target |
| [[EPHA10]] | C | EPHA10 activity raises MLXIPL's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.72× lower at baseline in the lines without EPHA10 | 0.021 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2; co-absent with the target |
| [[KCNK5]] | C | KCNK5 activity raises MLXIPL's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 3.09× lower at baseline in the lines without KCNK5 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2; co-absent with the target |
| [[LLGL2]] | C | LLGL2 activity raises MLXIPL's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without LLGL2 | 0.034 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFD]] | B | MLXIPL activity raises CFD's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without MLXIPL | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[NOXA1]] | B | MLXIPL activity raises NOXA1's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.64× lower at baseline in the lines without MLXIPL | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[SCARF2]] | B | MLXIPL activity lowers SCARF2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.77× higher at baseline in the lines without MLXIPL | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[BAIAP3]] | B | MLXIPL activity raises BAIAP3's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without MLXIPL | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[MERTK]] | B | MLXIPL activity raises MERTK's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without MLXIPL | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[RHPN1]] | B | MLXIPL activity raises RHPN1's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.37× lower at baseline in the lines without MLXIPL | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[ACSS2]] | B | MLXIPL activity raises ACSS2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without MLXIPL | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[LMTK3]] | B | MLXIPL activity raises LMTK3's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without MLXIPL | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[GRTP1]] | C | MLXIPL activity raises GRTP1's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 3.67× lower at baseline in the lines without MLXIPL | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |
| [[KCNK5]] | C | MLXIPL activity raises KCNK5's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 3.84× lower at baseline in the lines without MLXIPL | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |
| [[HES2]] | C | MLXIPL activity raises HES2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without MLXIPL | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |
| [[LLGL2]] | C | MLXIPL activity raises LLGL2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 4.06× lower at baseline in the lines without MLXIPL | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.3, 3.0); signed map (-21.0, 31.6). **Vector** length 65.2, 12.3% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.8 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MLX interacting protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,593,194-73,624,543 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WS-bHLH, MIO, CHREBP, MONDOB, bHLHd14; previously WBSCR14 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 5 pathways, smallest: PKA-mediated phosphorylation of key metabolic factors; PP2A-mediated dephosphorylation of key metabolic factors; AMPK inhibits chREBP transcriptional activation activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP71](https://www.uniprot.org/uniprotkb/Q9NP71) (Carbohydrate-responsive element-binding protein):

> Glucose-responsive transcription activator that regulates fatty acid synthesis and glycolysis. Key determinant of systemic insulin sensitivity and glucose homeostasis. Important for the expression of fatty acid synthetic enzymes, including PC/Pcx, APOC4/Acl, ACACA/Acc1 and FASN/Fas (By similarity). Important for glucose-induced expression of L-type pyruvate kinase/PKLR (By similarity). Binds to the canonical and non-canonical E box DNA sequences 5'-CACGTG-3' and 5'-CACGCG-3' (By similarity). …

**Summary**, from NCBI Gene [51085](https://www.ncbi.nlm.nih.gov/gene/51085):

> This gene encodes a basic helix-loop-helix leucine zipper transcription factor of the Myc/Max/Mad superfamily. This protein forms a heterodimeric complex and binds and activates, in a glucose-dependent manner, carbohydrate response element (ChoRE) motifs in the promoters of triglyceride synthesis genes. The gene is deleted in Williams-Beuren syndrome, a multisystem developmental disorder caused by the deletion of contiguous genes at chromosome 7q11.23. Alternative splicing results in multiple …

**Accessions** — [HGNC:12744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12744) · Entrez [51085](https://www.ncbi.nlm.nih.gov/gene/51085) · UniProt [Q9NP71](https://www.uniprot.org/uniprotkb/Q9NP71) · Ensembl [ENSG00000009950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009950)

## Data

Gene col 194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 194); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 194]; `tensor/DDL_lfc|DDL_z.npy` [194]; `embed/gene_vectors.npy` [194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 194 or target_col == 194). Every well: [[MLXIPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLXIPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
