---
symbol: "APLP1"
type: "gene"
col: 2578
ensembl_id: "ENSG00000105290"
name: "amyloid beta precursor like protein 1"
location: "19q13.12"
module: 50
arm: "+"
pooled_cpm: 7.76
n_lines_expressing: 38
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 20
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# APLP1

*amyloid beta precursor like protein 1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.81× (z +12.2, q 3e-31, up in 23 of 36 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 2.41× (z +10.3, q 5e-23, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.624× (z -5.5, q 2e-05, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITM2C]] (+0.64, fdr 1e-05), [[LRPAP1]] (+0.63, fdr 1e-05), [[PRKACA]] (+0.62, fdr 1e-05); moves opposite to [[TATDN1]] (-0.60, fdr 1e-05), [[DPH5-DT]] (-0.56, fdr 2e-05), [[TTC27]] (-0.56, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ADGRB2]] → it (grade B ⚠); 20 go from it, the strongest it → [[BSG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.81×** | +12.2 | 3e-31 | 23/36 (PANC-1, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.69×** | +11.6 | 1e-28 | 20/36 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.60×** | +11.2 | 7e-27 | 23/36 (PANC-1, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.56×** | +11.1 | 3e-26 | 16/23 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.64×** | +11.0 | 5e-26 | 10/12 (A-172, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.41×** | +10.3 | 5e-23 | 23/36 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +10.0 | 1e-21 | 23/31 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.04×** | +8.4 | 3e-15 | 24/33 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.5 | 4e-09 | 14/36 (A549, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +6.0 | 1e-07 | 16/34 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.71×** | +5.8 | 3e-07 | 10/14 (HS-578T, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.52×** | +4.8 | 9e-05 | 15/31 (A498, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.23×** | +4.7 | 1e-04 | 9/36 (HOP62, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.5 | 3e-04 | 12/27 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.44×** | +4.2 | 0.001 | 6/23 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.003 | 11/36 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.011 | 6/36 (NCI-H23, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.032 | 2/35 (J82, PANC-1) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.038 | 7/35 (A498, BT-474, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.069 | 2/35 (NCI-H23, Hs 766T) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.071 | 6/36 (A-427, C-33 A, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.624×** | -5.5 | 2e-05 | 15/30 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -4.2 | 0.008 | 16/36 (hTERT-HPNE, A498, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.1 | 0.008 | 16/35 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.698×** | -4.0 | 0.010 | 16/33 (PANC-1, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.639×** | -3.7 | 0.020 | 5/36 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -3.6 | 0.032 | 16/35 (A-427, HOP62, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.755×** | -3.3 | 0.081 | 10/36 (SNU-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.097 | 9/34 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.097 | 9/35 (LoVo, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.765×** | -3.1 | 0.097 | 9/33 (A-172, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 2 | — | [[BI-3406 (drug)]] 0.05 µM 0.0567× (z -10.9) |
| [[A-172 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -12.8) |
| [[H4 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0846× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 3.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 25.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.232× (z -11.5) |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.174× (z -11.5) |
| [[RKO (line)]] | wt | 7.10 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0848× (z -9.2) |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2C]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[LRPAP1]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 | STRING 430 |
| [[BSG]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PLOD1]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TWSG1]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ADGRA2]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LRP1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ECM1]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ARSA]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FAM234A]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TATDN1]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.56 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[TTC27]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NOL8]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PHF14]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PIGL]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[NIFK]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[RBM28]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SDAD1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ESF1]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PUM3]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB2]] | B | ADGRB2 activity raises APLP1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 3.50× lower at baseline in the lines without ADGRB2 | 0.008 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[GAS6]] | B | GAS6 activity raises APLP1's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 2.62× lower at baseline in the lines without GAS6 | 0.013 | ⚠ within organs, on part of the lines |
| [[TOP2A]] | B | TOP2A activity lowers APLP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CERCAM]] | B | CERCAM activity raises APLP1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 2.66× lower at baseline in the lines without CERCAM | 0.051 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[NXPH4]] | B | NXPH4 activity raises APLP1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without NXPH4 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[NLGN2]] | C | NLGN2 activity raises APLP1's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 3.94× lower at baseline in the lines without NLGN2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSG]] | B | APLP1 activity raises BSG's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without APLP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[ADGRB2]] | B | APLP1 activity raises ADGRB2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without APLP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[RBM28]] | B | APLP1 activity raises RBM28's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without APLP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[NLGN2]] | B | APLP1 activity raises NLGN2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without APLP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[SMARCD3]] | B | APLP1 activity raises SMARCD3's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without APLP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[SEPTIN3]] | B | APLP1 activity raises SEPTIN3's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.89× lower at baseline in the lines without APLP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[NPTXR]] | B | APLP1 activity raises NPTXR's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without APLP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[CNPY4]] | B | APLP1 activity raises CNPY4's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without APLP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[LLGL1]] | B | APLP1 activity raises LLGL1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.63× lower at baseline in the lines without APLP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[PLOD1]] | B | APLP1 activity raises PLOD1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.47× lower at baseline in the lines without APLP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[ESF1]] | B | APLP1 activity raises ESF1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.15× lower at baseline in the lines without APLP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[TCF7L1]] | B | APLP1 activity raises TCF7L1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 3.02× lower at baseline in the lines without APLP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.6, -21.6); signed map (-28.0, -38.0). **Vector** length 58.5, 10.5% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +2.0 | +11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor like protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,867,899-35,879,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APLP |
| Hallmark sets | IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P51693](https://www.uniprot.org/uniprotkb/P51693) (Amyloid beta precursor like protein 1):

> May play a role in postsynaptic function. The C-terminal gamma-secretase processed fragment, ALID1, activates transcription activation through APBB1 (Fe65) binding (By similarity). Couples to JIP signal transduction through C-terminal binding. May interact with cellular G protein signaling pathways. Can regulate neurite outgrowth through binding to components of the extracellular matrix such as heparin and collagen I.; The gamma-CTF peptide, C30, is a potent enhancer of neuronal apoptosis.

**Summary**, from NCBI Gene [333](https://www.ncbi.nlm.nih.gov/gene/333):

> This gene encodes a member of the highly conserved amyloid precursor protein gene family. The encoded protein is a membrane-associated glycoprotein that is cleaved by secretases in a manner similar to amyloid beta A4 precursor protein cleavage. This cleavage liberates an intracellular cytoplasmic fragment that may act as a transcriptional activator. The encoded protein may also play a role in synaptic maturation during cortical development. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:597) · Entrez [333](https://www.ncbi.nlm.nih.gov/gene/333) · UniProt [P51693](https://www.uniprot.org/uniprotkb/P51693) · Ensembl [ENSG00000105290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105290)

## Data

Gene col 2578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2578); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2578]; `tensor/DDL_lfc|DDL_z.npy` [2578]; `embed/gene_vectors.npy` [2578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2578 or target_col == 2578). Every well: [[APLP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APLP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
