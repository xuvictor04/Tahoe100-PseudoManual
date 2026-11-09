---
symbol: "MPP7"
type: "gene"
col: 7425
ensembl_id: "ENSG00000150054"
name: "MAGUK p55 scaffold protein 7"
location: "10p12.1"
module: 27
arm: "+"
pooled_cpm: 21.54
n_lines_expressing: 31
n_dd_up: 36
n_dd_down: 10
n_dd_up_clean: 32
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 28
direction_downstream: 35
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MPP7

*MAGUK p55 scaffold protein 7* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.53× (z +34.8, q 0e+00, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.655× (z -7.9, q 2e-12, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXADR]] (+0.69, fdr 1e-05), [[SORL1]] (+0.63, fdr 3e-05), [[ATP8A1]] (+0.62, fdr 1e-05); moves opposite to [[TRAPPC12]] (-0.58, fdr 5e-05), [[GPATCH2L]] (-0.58, fdr 2e-05), [[ZNF621]] (-0.57, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[PRR36]] → it (grade B ⚠); 35 go from it, the strongest it → [[PPM1H]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.53×** | +34.8 | 0e+00 | 26/28 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.92×** | +33.0 | 0e+00 | 27/28 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.43×** | +27.6 | 0e+00 | 26/28 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +27.4 | 0e+00 | 22/29 (NCI-H2030, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.45×** | +23.0 | 0e+00 | 27/28 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +15.2 | 0e+00 | 8/18 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +14.6 | 0e+00 | 10/28 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +14.0 | 2e-42 | 10/24 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +12.8 | 1e-35 | 7/20 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.77×** | +12.2 | 1e-32 | 26/29 (NCI-H23, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +11.9 | 1e-30 | 22/28 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +10.2 | 7e-23 | 22/28 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +9.2 | 2e-18 | 22/28 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +9.2 | 2e-18 | 11/27 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +6.7 | 1e-09 | 14/29 (SW480, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +6.2 | 2e-08 | 16/28 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.39×** | +6.2 | 2e-08 | 15/29 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 2e-08 | 13/29 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7425.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -7.9 | 2e-12 | 21/28 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -6.2 | 1e-07 | 17/28 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -5.8 | 1e-06 | 20/28 (SW480, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.745×** | -5.5 | 6e-06 | 14/28 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.724×** | -4.9 | 1e-04 | 15/28 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.642×** | -4.1 | 0.004 | 8/26 (NCI-H2347, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.646×** | -4.0 | 0.004 | 14/29 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -4.0 | 0.004 | 13/28 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.809×** | -4.0 | 0.005 | 13/28 (SW 900, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.810×** | -3.9 | 0.005 | 8/28 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -3.8 | 0.007 | 11/28 (COLO 205, A-427, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.839× | -3.3 | 0.049 | 3/26 (NCI-H23, SHP-77, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.847× | -3.1 | 0.083 | 8/28 (SW480, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 177 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 6.46 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 14.7× (z +11.1) | — |
| [[SW480 (line)]] | alt | 52.2 | 0 | 5 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0692× (z -11.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.295× (z -10.5) |
| [[A498 (line)]] | wt | 5.96 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +12.6) | — |
| [[KATO III (line)]] | alt | 9.17 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.99× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 7.64 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.4× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0964× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 10.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.11× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 33.2 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.33× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 33.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.359× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 20.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0982× (z -10.4) |
| [[LoVo (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.253× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 54.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0903× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 90.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.0) |
| [[A-172 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXADR]] | +0.69 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SORL1]] | +0.63 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[ATP8A1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PPFIBP2]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[AMOT]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 | same gene group; STRING 570 |
| [[TJP3]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 | same gene group |
| [[ATP8B1]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MAP2K6]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MYRIP]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[NR3C2]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SELENOP]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[MGAT4A]] | +0.59 | +0.41 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC12]] | -0.58 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[GPATCH2L]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ZNF621]] | -0.57 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[RECQL5]] | -0.57 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[C10orf88]] | -0.55 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[RPAP1]] | -0.55 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PRR14L]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EMG1]] | -0.54 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PEX6]] | -0.54 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[BMS1P4-1]] | -0.53 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[AGAP6]] | -0.53 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[EXOSC3]] | -0.53 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 13, C 15. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR36]] | B | PRR36 activity raises MPP7's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 3.60× lower at baseline in the lines without PRR36 | 0.005 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[NR3C2]] | B | NR3C2 activity raises MPP7's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.46× lower at baseline in the lines without NR3C2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[ERBB3]] | B | ERBB3 activity raises MPP7's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.10× lower at baseline in the lines without ERBB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises MPP7's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without SH3BGRL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises MPP7's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.74× lower at baseline in the lines without ATP8B1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[CXADR]] | B | CXADR activity raises MPP7's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.54× lower at baseline in the lines without CXADR | 0.034 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[VIPR1]] | B | VIPR1 activity raises MPP7's level | lines that do not express VIPR1 (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without VIPR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[ENPP4]] | B | ENPP4 activity raises MPP7's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 2.95× lower at baseline in the lines without ENPP4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[SCN9A]] | B | SCN9A activity raises MPP7's level | lines that do not express SCN9A (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without SCN9A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRM, RPS6KA6, UCHL1 |
| [[KLHL32]] | B | KLHL32 activity raises MPP7's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 2.87× lower at baseline in the lines without KLHL32 | 0.064 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[ATP8A1]] | B | ATP8A1 activity raises MPP7's level | lines that do not express ATP8A1 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without ATP8A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENPP4, TSPAN12, KLHL32; maybe low, not absent |
| [[PPARGC1A]] | B | PPARGC1A activity raises MPP7's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 1.93× lower at baseline in the lines without PPARGC1A | 0.092 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2 |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 21, C 14. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1H]] | B | MPP7 activity raises PPM1H's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.54× lower at baseline in the lines without MPP7 | 0.006 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[SH3BGRL2]] | B | MPP7 activity raises SH3BGRL2's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.83× lower at baseline in the lines without MPP7 | 0.007 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[ERBB3]] | B | MPP7 activity raises ERBB3's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 3.07× lower at baseline in the lines without MPP7 | 0.019 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[KLHL32]] | B | MPP7 activity raises KLHL32's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without MPP7 | 0.022 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[ATP8B1]] | B | MPP7 activity raises ATP8B1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without MPP7 | 0.023 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[SELENOP]] | B | MPP7 activity raises SELENOP's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.05× lower at baseline in the lines without MPP7 | 0.025 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[SLAIN1]] | B | MPP7 activity raises SLAIN1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without MPP7 | 0.027 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[CXADR]] | B | MPP7 activity raises CXADR's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.68× lower at baseline in the lines without MPP7 | 0.031 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[SFN]] | B | MPP7 activity raises SFN's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.85× lower at baseline in the lines without MPP7 | 0.031 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[CD24]] | B | MPP7 activity raises CD24's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without MPP7 | 0.032 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[ENPP4]] | B | MPP7 activity raises ENPP4's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without MPP7 | 0.048 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[TSPAN15]] | B | MPP7 activity raises TSPAN15's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without MPP7 | 0.051 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.7, 46.8); signed map (52.2, 3.1). **Vector** length 75.7, 18.0% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +27.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +15.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +12.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +5.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | MAGUK p55 scaffold protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:28,050,993-28,334,486 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32798 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 9 pathways, smallest: RHOJ GTPase cycle; RHOQ GTPase cycle; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T2T1](https://www.uniprot.org/uniprotkb/Q5T2T1) (MAGUK p55 subfamily member 7):

> Acts as an important adapter that promotes epithelial cell polarity and tight junction formation via its interaction with DLG1. Involved in the assembly of protein complexes at sites of cell-cell contact.

**Summary**, from NCBI Gene [143098](https://www.ncbi.nlm.nih.gov/gene/143098):

> The protein encoded by this gene is a member of the p55 Stardust family of membrane-associated guanylate kinase (MAGUK) proteins, which function in the establishment of epithelial cell polarity. This family member forms a complex with the polarity protein DLG1 (discs, large homolog 1) and facilitates epithelial cell polarity and tight junction formation. Polymorphisms in this gene are associated with variations in site-specific bone mineral density (BMD). Alternative splicing results in …

**Accessions** — [HGNC:26542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26542) · Entrez [143098](https://www.ncbi.nlm.nih.gov/gene/143098) · UniProt [Q5T2T1](https://www.uniprot.org/uniprotkb/Q5T2T1) · Ensembl [ENSG00000150054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150054)

## Data

Gene col 7425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7425); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7425]; `tensor/DDL_lfc|DDL_z.npy` [7425]; `embed/gene_vectors.npy` [7425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7425 or target_col == 7425). Every well: [[MPP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
