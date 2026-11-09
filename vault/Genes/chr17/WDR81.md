---
symbol: "WDR81"
type: "gene"
col: 9526
ensembl_id: "ENSG00000167716"
name: "WD repeat domain 81"
location: "17p13.3"
module: 172
arm: "+"
pooled_cpm: 9.78
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# WDR81

*WD repeat domain 81* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.63× (z +12.3, q 3e-32, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.677× (z -7.1, q 1e-09, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A7]] (+0.76, fdr 7e-06), [[TMEM199]] (+0.72, fdr 7e-06), [[GPATCH3]] (+0.68, fdr 7e-06); moves opposite to [[PLS1]] (-0.63, fdr 1e-05), [[PHF6]] (-0.58, fdr 2e-05), [[FAM102B]] (-0.58, fdr 3e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NCAM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.63×** | +12.3 | 3e-32 | 42/47 (HT-29, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +11.7 | 2e-29 | 32/44 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.9 | 5e-07 | 18/48 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.60×** | +5.7 | 2e-06 | 22/46 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.3 | 1e-05 | 18/39 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 6e-05 | 18/47 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +4.4 | 9e-04 | 15/47 (A-427, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.4 | 9e-04 | 17/43 (SNU-423, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.005 | 12/47 (LOX-IMVI, SHP-77, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.009 | 7/47 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.33×** | +3.6 | 0.013 | 15/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.6 | 0.013 | 5/26 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.016 | 15/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.023 | 13/46 (SW480, RKO, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.030 | 7/48 (PANC-1, J82, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.039 | 11/44 (SHP-77, hTERT-HPNE, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.20× | +3.2 | 0.039 | 8/48 (NCI-H460, J82, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.19× | +3.2 | 0.041 | 9/48 (SHP-77, HOP62, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.042 | 7/46 (HOP62, SW 1271, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.074 | 7/48 (A-427, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9526.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.677×** | -7.1 | 1e-09 | 28/48 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.646×** | -5.6 | 7e-06 | 18/46 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.682×** | -4.9 | 2e-04 | 16/47 (SW480, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.681×** | -4.7 | 3e-04 | 18/46 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.706×** | -4.5 | 9e-04 | 20/46 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -4.1 | 0.005 | 12/47 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.735×** | -3.8 | 0.013 | 17/40 (RKO, KATO III, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.759×** | -3.5 | 0.029 | 18/47 (NCI-H1573, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0879× (z -13.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.38 | 0 | 3 | — | [[DT-061 (drug)]] 0.05 µM 0.0546× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 9.35 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -10.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.4 | 0 | 3 (2 ⚠) | — | [[Mozavaptan (drug)]] 0.05 µM 0.0682× (z -10.5) |
| [[LoVo (line)]] | wt | 10.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.49× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 7.04 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +10.0) | [[Hydroxyurea (drug)]] 0.05 µM 0.0943× (z -9.3) |
| [[A-172 (line)]] | wt | 17.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +9.1) | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 | — | [[Posaconazole (drug)]] 0.05 µM 0.0539× (z -9.9) |
| [[HCT15 (line)]] | alt | 9.93 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0950× (z -8.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 9.07 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0838× (z -8.7) |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.135× (z -9.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 7.89 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.37× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 9.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0553× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1792 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 9.48 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.192× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0877× (z -8.9) |
| [[PANC-1 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.155× (z -8.5) |
| [[SW480 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -8.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A7]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.72 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[GPATCH3]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.67 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A17]] | +0.65 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LRRC41]] | +0.65 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[RHBDD3]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 | same gene group |
| [[DHX34]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[CELF6]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[HMGA1P4]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLS1]] | -0.63 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PHF6]] | -0.58 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FAM102B]] | -0.58 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SVIP]] | -0.57 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[SSX2IP]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TMEM106C]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[HLTF]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[FSBP]] | -0.54 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PPP1CC]] | -0.54 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[CYB5A]] | -0.53 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[HYCC1]] | -0.53 | -0.26 / -0.55 | both halves | 3e-04 |  |
| [[HMGN3]] | -0.53 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCAM1]] | B | NCAM1 activity raises WDR81's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without NCAM1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises WDR81's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises WDR81's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.0, 11.2); signed map (-7.7, -19.9). **Vector** length 85.9, 16.3% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.6 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.2 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.3 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 81 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,716,523-1,738,599 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33817, PPP1R166, CAMRQ2, SORF-2 |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 1 regulatory subunits; BEACH domain containing ; Armadillo like helical domain containing |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q562E7](https://www.uniprot.org/uniprotkb/Q562E7) (WD repeat-containing protein 81):

> Functions as a negative regulator of the PI3 kinase/PI3K activity associated with endosomal membranes via BECN1, a core subunit of the PI3K complex. By modifying the phosphatidylinositol 3-phosphate/PtdInsP3 content of endosomal membranes may regulate endosome fusion, recycling, sorting and early to late endosome transport. It is for instance, required for the delivery of cargos like BST2/tetherin from early to late endosome and thereby participates indirectly to their degradation by the …

**Summary**, from NCBI Gene [124997](https://www.ncbi.nlm.nih.gov/gene/124997):

> This gene encodes a multi-domain transmembrane protein which is predominantly expressed in the brain and is thought to play a role in endolysosomal trafficking. Mutations in this gene are associated with an autosomal recessive form of a syndrome exhibiting cerebellar ataxia, cognitive disability, and disequilibrium (CAMRQ2). Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:26600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26600) · Entrez [124997](https://www.ncbi.nlm.nih.gov/gene/124997) · UniProt [Q562E7](https://www.uniprot.org/uniprotkb/Q562E7) · Ensembl [ENSG00000167716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167716)

## Data

Gene col 9526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9526); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9526]; `tensor/DDL_lfc|DDL_z.npy` [9526]; `embed/gene_vectors.npy` [9526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9526 or target_col == 9526). Every well: [[WDR81 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR81.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
