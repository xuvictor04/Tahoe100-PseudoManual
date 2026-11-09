---
symbol: "PKIB"
type: "gene"
col: 5724
ensembl_id: "ENSG00000135549"
name: "cAMP-dependent protein kinase inhibitor beta"
location: "6q22.31"
module: 9
arm: "+"
pooled_cpm: 19.5
n_lines_expressing: 44
n_dd_up: 33
n_dd_down: 11
n_dd_up_clean: 30
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PKIB

*cAMP-dependent protein kinase inhibitor beta* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.20× (z +18.2, q 0e+00, up in 36 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.589× (z -8.7, q 2e-15, down in 21 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMH1]] (+0.54, fdr 3e-05), [[PACRG]] (+0.52, fdr 5e-05), [[DISC1FP1]] (+0.51, fdr 3e-05); moves opposite to [[SPOUT1]] (-0.54, fdr 3e-04), [[INTS15]] (-0.47, fdr 6e-04), [[L3MBTL2]] (-0.46, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SCIN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +18.2 | 0e+00 | 36/42 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +15.7 | 0e+00 | 27/39 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +14.1 | 7e-43 | 26/41 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +12.4 | 5e-33 | 33/40 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +12.0 | 4e-31 | 26/41 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +11.4 | 3e-28 | 24/41 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +9.8 | 6e-21 | 25/41 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +9.3 | 7e-19 | 25/40 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +7.4 | 8e-12 | 20/40 (SW480, AsPC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +6.8 | 7e-10 | 17/40 (LoVo, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.51×** | +6.7 | 1e-09 | 15/39 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +6.6 | 2e-09 | 22/42 (KATO III, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.42×** | +6.2 | 3e-08 | 17/42 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +5.9 | 1e-07 | 19/41 (BT-474, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +5.6 | 9e-07 | 17/42 (SW480, LoVo, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.41×** | +5.5 | 1e-06 | 12/40 (HOP62, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -8.7 | 2e-15 | 21/41 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.626×** | -7.7 | 4e-12 | 21/40 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.689×** | -6.1 | 2e-07 | 21/39 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -5.6 | 4e-06 | 16/39 (LS 180, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -5.1 | 4e-05 | 18/40 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.750×** | -4.7 | 2e-04 | 21/40 (A-427, KATO III, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.602×** | -4.4 | 0.001 | 17/38 (CHP-212, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.782×** | -4.1 | 0.004 | 11/41 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.036 | 8/41 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.815×** | -3.4 | 0.042 | 15/40 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.824×** | -3.2 | 0.070 | 14/42 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.833× | -3.0 | 0.12 | 5/40 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 9.73 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.143× (z -9.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.165× (z -8.9) |
| [[BT-474 (line)]] | alt | 50.3 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.70× (z +10.5) | — |
| [[SW480 (line)]] | alt | 14.4 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.96× (z +12.0) | [[Digitoxin (drug)]] 0.05 µM 0.178× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 10.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.80× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 79.5 | 2 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[KATO III (line)]] | alt | 14.2 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.45× (z +11.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -9.3) |
| [[LoVo (line)]] | wt | 20.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.27× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.01× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.4× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.97× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 92.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -10.0) |
| [[SHP-77 (line)]] | alt | 98.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0688× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 8.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.179× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 5.09 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0820× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 7.17 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.13 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0573× (z -9.4) |
| [[A-172 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMH1]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PACRG]] | +0.52 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[DISC1FP1]] | +0.51 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[LINC01748]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CDHR2]] | +0.49 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[DNAH6]] | +0.49 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[VWA5A]] | +0.49 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KSR2]] | +0.49 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[KCNH7]] | +0.49 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ENPP1]] | +0.48 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SEMA3E]] | +0.48 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[SELENOP]] | +0.48 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOUT1]] | -0.54 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[INTS15]] | -0.47 | -0.40 / -0.22 | both halves | 6e-04 |  |
| [[L3MBTL2]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[HIRA]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ZC3H18]] | -0.44 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[CNOT10]] | -0.44 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[DDX51]] | -0.43 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[PITPNA]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[DDX19A]] | -0.43 | -0.34 / -0.29 | both halves | 3e-04 |  |
| [[INO80E]] | -0.42 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCIN]] | B | SCIN activity raises PKIB's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without SCIN | 0.013 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[MPZL3]] | B | MPZL3 activity raises PKIB's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.21× lower at baseline in the lines without MPZL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[SELENOP]] | B | SELENOP activity raises PKIB's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without SELENOP | 0.018 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[LINC01226]] | B | LINC01226 activity raises PKIB's level | lines that do not express LINC01226 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without LINC01226 | 0.022 | ⚠ within organs, on part of the lines; also absent: LASTR, TRIM29, ENSG00000287003; maybe low, not absent |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises PKIB's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.30× lower at baseline in the lines without MTUS1-DT | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[SLC25A48]] | B | SLC25A48 activity lowers PKIB's level | lines that do not express SLC25A48 (8) vs lines expressing it (42) | 1.94× higher at baseline in the lines without SLC25A48 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ATL1]] | B | ATL1 activity raises PKIB's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without ATL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |
| [[SLC7A8]] | B | SLC7A8 activity raises PKIB's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without SLC7A8 | 0.083 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[MYO5B]] | B | MYO5B activity raises PKIB's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.16× lower at baseline in the lines without MYO5B | 0.086 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[FREM2]] | B | FREM2 activity raises PKIB's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without FREM2 | 0.092 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises PKIB's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.405). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.9, 27.8); signed map (54.4, 17.6). **Vector** length 74.5, 13.3% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +18.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.6 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +9.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.3 | -3.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | cAMP-dependent protein kinase inhibitor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:122,471,917-122,726,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PRKACN2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C010](https://www.uniprot.org/uniprotkb/Q9C010) (cAMP-dependent protein kinase inhibitor beta):

> Extremely potent competitive inhibitor of cAMP-dependent protein kinase activity, this protein interacts with the catalytic subunit of the enzyme after the cAMP-induced dissociation of its regulatory chains.

**Summary**, from NCBI Gene [5570](https://www.ncbi.nlm.nih.gov/gene/5570):

> This gene encodes a member of the cAMP-dependent protein kinase inhibitor family. The encoded protein may play a role in the protein kinase A (PKA) pathway by interacting with the catalytic subunit of PKA, and overexpression of this gene may play a role in prostate cancer. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:9018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9018) · Entrez [5570](https://www.ncbi.nlm.nih.gov/gene/5570) · UniProt [Q9C010](https://www.uniprot.org/uniprotkb/Q9C010) · Ensembl [ENSG00000135549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135549)

## Data

Gene col 5724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5724); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5724]; `tensor/DDL_lfc|DDL_z.npy` [5724]; `embed/gene_vectors.npy` [5724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5724 or target_col == 5724). Every well: [[PKIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
