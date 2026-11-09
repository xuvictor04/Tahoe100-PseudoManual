---
symbol: "FAR2P1"
type: "gene"
col: 11083
ensembl_id: "ENSG00000180178"
name: "fatty acyl-CoA reductase 2 pseudogene 1"
location: "2q21.1"
module: 177
arm: "+"
pooled_cpm: 7.98
n_lines_expressing: 21
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 13
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# FAR2P1

*fatty acyl-CoA reductase 2 pseudogene 1* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +13.9, q 3e-41, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.485× (z -8.2, q 1e-13, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POTEF]] (+0.68, fdr 1e-05, ⚠ same locus), [[CCDC113]] (+0.65, fdr 1e-05), [[ZMAT1]] (+0.59, fdr 1e-05), [[SPEF2]] (+0.55, fdr 4e-05); moves opposite to [[SNHG30]] (-0.60, fdr 1e-05), [[MICB]] (-0.51, fdr 2e-04), [[TMEM11-DT]] (-0.50, fdr 1e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[POTEE]] → it (grade C ⚠); 13 go from it, the strongest it → [[N6AMT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +13.9 | 3e-41 | 12/18 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +13.0 | 3e-36 | 1/8 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.01×** | +12.5 | 1e-33 | 18/19 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +10.9 | 1e-25 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +9.2 | 3e-18 | 16/19 (HepG2/C3A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +9.2 | 5e-18 | 15/19 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +7.3 | 3e-11 | 1/12 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.1 | 8e-08 | 10/17 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +5.8 | 6e-07 | 10/18 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.8 | 9e-05 | 11/19 (C-33 A, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.8 | 9e-05 | 12/19 (HepG2/C3A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +4.7 | 9e-05 | 10/19 (PANC-1, C-33 A, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.7 | 9e-05 | 4/19 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.006 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.015 | 3/19 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.029 | 0/19 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.029 | 2/18 (BT-474, HEC-1-A) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.029 | 6/19 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.485×** | -8.2 | 1e-13 | 12/19 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -4.8 | 4e-04 | 15/19 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.673×** | -4.5 | 0.001 | 7/19 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -4.4 | 0.001 | 15/19 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -4.4 | 0.001 | 15/19 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.493×** | -4.2 | 0.003 | 9/18 (LS 180, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.707×** | -3.7 | 0.020 | 6/19 (HS-578T, SW1417, …) | top dose only |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.030 | 10/19 (HepG2/C3A, A-427, …) | two highest doses | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | 0.758× | -3.1 | 0.11 | 0/19 | top dose only | position effect removed |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.765× | -3.0 | 0.14 | 2/19 (NCI-H661, SW480) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 78.1 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Decitabine (drug)]] 0.05 µM 0.209× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0357× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0825× (z -12.8) |
| [[PANC-1 (line)]] | alt | 19.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -10.6) |
| [[SNU-1 (line)]] | wt | 40.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 2 | — | [[Malotilate (drug)]] 0.5 µM 0.0407× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 32.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.217× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.88 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0725× (z -9.6) |
| [[A-427 (line)]] | wt | 14.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +10.8) | — |
| [[SW480 (line)]] | alt | 4.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.925 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POTEF]] | +0.68 | +0.53 / +0.76 | both halves | 1e-05 | ⚠ same locus (33.0 kb, same strand: neighbours can correlate without regulation) |
| [[CCDC113]] | +0.65 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.59 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SPEF2]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[MRPS33]] | +0.55 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[IFTAP]] | +0.55 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[PMFBP1]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[POTEE]] | +0.54 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[DHRS2]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[FAM95A]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[ZNF252P-1]] | +0.53 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[UROS]] | +0.51 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R9A]] | +0.51 | +0.37 / +0.62 | both halves | 8e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MICB]] | -0.51 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TMEM11-DT]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[C8orf76]] | -0.50 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[NBL1]] | -0.50 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[GLUD1P3]] | -0.50 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[PRDM10]] | -0.49 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[NFATC3]] | -0.48 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[MBOAT7]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[GUCD1]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[ZNF668]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.46 | -0.40 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POTEE]] | C | POTEE activity raises FAR2P1's level | lines that do not express POTEE (29) vs lines expressing it (21) | 8.70× lower at baseline in the lines without POTEE | 4e-06 | ⚠ within organs, on part of the lines; also absent: FAR2P1, ENSG00000286329, EPIC1; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises FAR2P1's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.92× lower at baseline in the lines without CTNNA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[N6AMT1]] | B | FAR2P1 activity raises N6AMT1's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without FAR2P1 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[DHRS2]] | B | FAR2P1, [[POTEF]] activity raises DHRS2's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 2.84× lower at baseline in the lines without FAR2P1, POTEF | 0.018 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[MLST8]] | B | FAR2P1, [[POTEF]] activity raises MLST8's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 1.19× lower at baseline in the lines without FAR2P1, POTEF | 0.037 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[PCLO]] | B | FAR2P1 activity raises PCLO's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without FAR2P1 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[AFF4]] | B | FAR2P1 activity lowers AFF4's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.15× higher at baseline in the lines without FAR2P1 | 0.047 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[CEP63]] | B | FAR2P1, [[POTEF]] activity raises CEP63's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 1.21× lower at baseline in the lines without FAR2P1, POTEF | 0.062 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |
| [[NDUFAF7]] | B | FAR2P1 activity raises NDUFAF7's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.13× lower at baseline in the lines without FAR2P1 | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[IMPACT]] | B | FAR2P1 activity raises IMPACT's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.34× lower at baseline in the lines without FAR2P1 | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[CTNNA2]] | C | FAR2P1 activity raises CTNNA2's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without FAR2P1 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[POTEE]] | C | FAR2P1, [[POTEF]] activity raises POTEE's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 3.25× lower at baseline in the lines without FAR2P1, POTEF | 0.001 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target; co-absent genes |
| [[MIR2052HG]] | C | FAR2P1 activity raises MIR2052HG's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 2.59× lower at baseline in the lines without FAR2P1 | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[MIR3667HG]] | C | FAR2P1 activity raises MIR3667HG's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 2.99× lower at baseline in the lines without FAR2P1 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.8, 27.6); signed map (0.2, -7.2). **Vector** length 44.5, 9.14% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.1 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | fatty acyl-CoA reductase 2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 2q21.1 — chr2:130,028,309-130,040,560 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | LOC440905 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49284) · Entrez [440905](https://www.ncbi.nlm.nih.gov/gene/440905) · Ensembl [ENSG00000180178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180178)

## Data

Gene col 11083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11083); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11083]; `tensor/DDL_lfc|DDL_z.npy` [11083]; `embed/gene_vectors.npy` [11083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11083 or target_col == 11083). Every well: [[FAR2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAR2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
