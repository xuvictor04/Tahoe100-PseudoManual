---
symbol: "RASGRP3"
type: "gene"
col: 7651
ensembl_id: "ENSG00000152689"
name: "RAS guanyl releasing protein 3"
location: "2p22.3"
module: 32
arm: "+"
pooled_cpm: 12.2
n_lines_expressing: 34
n_dd_up: 28
n_dd_down: 32
n_dd_up_clean: 22
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 28
direction_downstream: 77
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# RASGRP3

*RAS guanyl releasing protein 3* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +11.5, q 8e-28, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.531× (z -7.7, q 1e-11, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSAD2]] (+0.71, fdr 7e-06), [[NLRC5]] (+0.69, fdr 7e-06), [[DDX60L]] (+0.68, fdr 7e-06); moves opposite to [[ERGIC1]] (-0.56, fdr 1e-05), [[MAOA]] (-0.55, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 77 go from it, the strongest it → [[CMPK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +11.5 | 8e-28 | 13/29 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +9.4 | 1e-18 | 17/29 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.96×** | +8.2 | 5e-14 | 25/31 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +7.7 | 2e-12 | 12/25 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.7 | 2e-12 | 4/15 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +6.2 | 4e-08 | 19/31 (A498, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +6.0 | 2e-07 | 4/18 (HepG2/C3A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.7 | 7e-07 | 15/30 (A549, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 8e-07 | 11/32 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +5.4 | 3e-06 | 15/31 (A498, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.0 | 3e-05 | 16/31 (Panc 03.27, SNU-423, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +4.2 | 0.001 | 8/31 (RPMI-7951, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.0 | 0.002 | 5/26 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.005 | 11/31 (A549, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.006 | 7/31 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.007 | 5/31 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 9/31 (A549, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.014 | 9/31 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.021 | 12/31 (C-33 A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.027 | 7/30 (Panc 03.27, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, none with an alert; shown: the 15 strongest. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -7.7 | 1e-11 | 21/31 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.545×** | -7.3 | 6e-11 | 20/31 (KATO III, SHP-77, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.559×** | -7.0 | 3e-10 | 19/31 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -6.5 | 1e-08 | 22/31 (KATO III, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.719×** | -5.6 | 2e-06 | 19/31 (COLO 205, LoVo, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.643×** | -5.3 | 8e-06 | 15/31 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.651×** | -5.2 | 2e-05 | 15/31 (SW 900, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.740×** | -5.2 | 2e-05 | 15/31 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.655×** | -5.1 | 2e-05 | 18/31 (COLO 205, LoVo, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.667×** | -4.9 | 5e-05 | 15/31 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.754×** | -4.8 | 6e-05 | 15/31 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.673×** | -4.8 | 8e-05 | 12/31 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.679×** | -4.7 | 1e-04 | 17/31 (CFPAC-1, A498, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.699×** | -4.3 | 6e-04 | 13/31 (BT-474, A-172, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.700×** | -4.3 | 6e-04 | 16/31 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 14 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0819× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 10 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 5 µM 0.234× (z -10.1) |
| [[SHP-77 (line)]] | alt | 36.2 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0709× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.6) |
| [[KATO III (line)]] | alt | 56.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0870× (z -14.7) |
| [[A-172 (line)]] | wt | 72.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.167× (z -8.7) |
| [[A498 (line)]] | wt | 9.63 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 2 | — | [[Budesonide (drug)]] 0.05 µM 0.123× (z -11.2) |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -11.2) |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.121× (z -10.1) |
| [[A549 (line)]] | wt | 14.8 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.110× (z -9.5) |
| [[BT-474 (line)]] | alt | 5.87 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0444× (z -9.2) |
| [[COLO 205 (line)]] | alt | 42.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0168× (z -17.4) |
| [[HS-578T (line)]] | alt | 6.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -8.6) |
| [[SW480 (line)]] | alt | 3.85 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD2]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[NLRC5]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[SAMD9]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CTSS]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[PARP14]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SAMD9L]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[HDX]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[IFIT5]] | +0.65 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[HERC6]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[TDRD7]] | +0.64 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ISG20]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MAOA]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 22, C 6. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises RASGRP3's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.51× lower at baseline in the lines without SAMD9L | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[MMP13]] | B | MMP13 activity raises RASGRP3's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.27× lower at baseline in the lines without MMP13 | 0.010 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[IFI27]] | B | IFI27 activity raises RASGRP3's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.75× lower at baseline in the lines without IFI27 | 0.012 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[FBXO39]] | B | FBXO39 activity raises RASGRP3's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without FBXO39 | 0.013 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[ETV7]] | B | ETV7 activity raises RASGRP3's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without ETV7 | 0.016 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises RASGRP3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.79× lower at baseline in the lines without RSAD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[ENKUR]] | B | ENKUR activity raises RASGRP3's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without ENKUR | 0.018 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises RASGRP3's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without OAS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises RASGRP3's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.79× lower at baseline in the lines without PLSCR1 | 0.030 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises RASGRP3's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.57× lower at baseline in the lines without EPSTI1 | 0.031 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CMPK2]] | B | CMPK2 activity raises RASGRP3's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without CMPK2 | 0.033 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI44]] | B | IFI44 activity raises RASGRP3's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without IFI44 | 0.036 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 72, C 5. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMPK2]] | B | RASGRP3 activity raises CMPK2's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 3.51× lower at baseline in the lines without RASGRP3 | 7e-04 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[PARP10]] | B | RASGRP3 activity raises PARP10's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RASGRP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[SAMD9L]] | B | RASGRP3 activity raises SAMD9L's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 3.86× lower at baseline in the lines without RASGRP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[PARP9]] | B | RASGRP3 activity raises PARP9's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without RASGRP3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[LAP3]] | B | RASGRP3 activity raises LAP3's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[MX1]] | B | RASGRP3 activity raises MX1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 4.11× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[PLSCR1]] | B | RASGRP3 activity raises PLSCR1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[OAS3]] | B | RASGRP3 activity raises OAS3's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[PARP14]] | B | RASGRP3 activity raises PARP14's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[PML]] | B | RASGRP3 activity raises PML's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[USP18]] | B | RASGRP3 activity raises USP18's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without RASGRP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[TMEM140]] | B | RASGRP3 activity raises TMEM140's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.69× lower at baseline in the lines without RASGRP3 | 0.006 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.2, 55.0); signed map (63.5, 33.1). **Vector** length 102, 27.3% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.53 to 56); *interferon gamma response* (hallmark, mean cos +0.54 to 60); *interferon* (control, mean cos +0.59 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.7 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.0 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +1.8 | +1.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.4 | -7.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.0 | -5.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | RAS guanyl releasing protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:33,436,324-33,564,750 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0846, GRP3, CalDAG-GEFIII |
| Gene groups (HGNC) | EF-hand domain containing; RAS guanyl releasing proteins |
| Reactome | 7 pathways, smallest: Activation of RAS in B cells; Downstream signaling events of B Cell Receptor (BCR); Signaling by the B Cell Receptor (BCR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV61](https://www.uniprot.org/uniprotkb/Q8IV61) (Ras guanyl-releasing protein 3):

> Guanine nucleotide exchange factor (GEF) for Ras and Rap1.

**Summary**, from NCBI Gene [25780](https://www.ncbi.nlm.nih.gov/gene/25780):

> The protein encoded by this gene is a guanine nucleotide exchange factor that activates the oncogenes HRAS and RAP1A. Defects in this gene have been associated with systemic lupus erythematosus and several cancers. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:14545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14545) · Entrez [25780](https://www.ncbi.nlm.nih.gov/gene/25780) · UniProt [Q8IV61](https://www.uniprot.org/uniprotkb/Q8IV61) · Ensembl [ENSG00000152689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152689)

## Data

Gene col 7651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7651); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7651]; `tensor/DDL_lfc|DDL_z.npy` [7651]; `embed/gene_vectors.npy` [7651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7651 or target_col == 7651). Every well: [[RASGRP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGRP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
