---
symbol: "GRTP1"
type: "gene"
col: 6349
ensembl_id: "ENSG00000139835"
name: "growth hormone regulated TBC protein 1"
location: "13q34"
module: 100
arm: "+"
pooled_cpm: 9.99
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# GRTP1

*growth hormone regulated TBC protein 1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +13.9, q 3e-41, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.699× (z -7.9, q 1e-12, down in 17 of 31 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.451× (z -6.5, q 1e-08, down in 20 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF7L1]] (+0.51, fdr 5e-05), [[TEAD3]] (+0.49, fdr 7e-05), [[TMEM38A]] (+0.49, fdr 2e-05); moves opposite to [[DDX1]] (-0.50, fdr 4e-05), [[FKTN]] (-0.49, fdr 4e-05), [[SMARCE1]] (-0.49, fdr 6e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[LLGL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +13.9 | 3e-41 | 25/31 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.6 | 1e-11 | 19/37 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.1 | 2e-10 | 15/33 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.53×** | +6.6 | 4e-09 | 19/37 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +5.0 | 5e-05 | 12/37 (SW480, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 14/37 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.5 | 6e-04 | 7/37 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +4.4 | 7e-04 | 12/35 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.4 | 8e-04 | 9/36 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.2 | 0.002 | 6/15 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 9/35 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.7 | 0.010 | 5/26 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.6 | 0.015 | 10/37 (SW480, NCI-H460, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.024 | 5/36 (SW48, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 1.15× | +3.2 | 0.061 | 10/37 (NCI-H460, NCI-H1573, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.699×** | -7.9 | 1e-12 | 17/31 (NCI-H23, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.592×** | -7.9 | 1e-12 | 19/34 (RKO, A498, …) | rises with dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.451×** | -6.5 | 1e-08 | 20/32 (LS 180, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.619×** | -6.5 | 1e-08 | 18/31 (RKO, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -6.4 | 1e-08 | 19/34 (NCI-H1573, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -5.3 | 1e-05 | 17/37 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -4.9 | 6e-05 | 15/36 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -4.7 | 2e-04 | 14/37 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.752×** | -4.4 | 6e-04 | 16/37 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.742×** | -4.4 | 7e-04 | 15/36 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.005 | 9/35 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.765×** | -3.8 | 0.006 | 9/36 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.010 | 10/36 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.782×** | -3.5 | 0.017 | 13/36 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.806×** | -3.4 | 0.029 | 4/36 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.029 | 8/37 (HT-29, NCI-H2347, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.030 | 11/35 (SK-MEL-2, BT-474, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.868× | -3.1 | 0.058 | 3/37 (SW480, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.811×** | -3.0 | 0.080 | 11/36 (SNU-1, LS 180, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.697×** | -2.9 | 0.088 | 4/28 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 27.2 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.165× (z -15.0) |
| [[A498 (line)]] | wt | 13.7 | 1 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LS 180 (line)]] | wt | 41.4 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.110× (z -11.4) |
| [[RKO (line)]] | wt | 15.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0524× (z -16.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.183× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -13.5) |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -10.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HEC-1-A (line)]] | alt | 8.33 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0478× (z -15.6) |
| [[HT-29 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[LoVo (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.17 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW48 (line)]] | wt | 20.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.119× (z -9.2) |
| [[A-172 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF7L1]] | +0.51 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[TEAD3]] | +0.49 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[TMEM38A]] | +0.49 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TLE2]] | +0.49 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[SLC12A9]] | +0.48 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[AGAP3]] | +0.48 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[UBTD1]] | +0.48 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[KCNIP3]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[LGI4]] | +0.47 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[SBK1]] | +0.46 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DNAJC22]] | +0.46 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[SCAMP5]] | +0.46 | +0.30 / +0.51 | both halves | 2e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX1]] | -0.50 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[FKTN]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SMARCE1]] | -0.49 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PRMT5]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[ASNSD1]] | -0.45 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[AIMP1]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PWP1]] | -0.45 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[ZNF480]] | -0.45 | -0.26 / -0.43 | both halves | 3e-04 |  |
| [[ZNF23]] | -0.45 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[FAM114A2]] | -0.45 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[FBXO38]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[EIF6]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRTP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MLXIPL]] | C | MLXIPL activity raises GRTP1's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 3.67× lower at baseline in the lines without MLXIPL | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LLGL1]] | B | GRTP1 activity lowers LLGL1's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 1.37× higher at baseline in the lines without GRTP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |
| [[MERTK]] | B | GRTP1 activity raises MERTK's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without GRTP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |
| [[ZFPM1]] | B | GRTP1 activity lowers ZFPM1's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 1.35× higher at baseline in the lines without GRTP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |
| [[COG2]] | B | GRTP1 activity raises COG2's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without GRTP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |
| [[MLXIPL]] | C | GRTP1 activity raises MLXIPL's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 3.40× lower at baseline in the lines without GRTP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-29.7, 33.0); signed map (-17.7, 21.3). **Vector** length 56.8, 9.25% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +1.9 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.0 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.5 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.3 | -7.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -2.1 | -7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | growth hormone regulated TBC protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,324,163-113,364,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22474, TBC1D6 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TC63](https://www.uniprot.org/uniprotkb/Q5TC63) (Growth hormone-regulated TBC protein 1):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [79774](https://www.ncbi.nlm.nih.gov/gene/79774):

> Predicted to enable GTPase activator activity. Predicted to be active in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20310) · Entrez [79774](https://www.ncbi.nlm.nih.gov/gene/79774) · UniProt [Q5TC63](https://www.uniprot.org/uniprotkb/Q5TC63) · Ensembl [ENSG00000139835](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139835)

## Data

Gene col 6349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6349); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6349]; `tensor/DDL_lfc|DDL_z.npy` [6349]; `embed/gene_vectors.npy` [6349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6349 or target_col == 6349). Every well: [[GRTP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRTP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
