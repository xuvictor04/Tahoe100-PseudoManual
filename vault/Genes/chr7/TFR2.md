---
symbol: "TFR2"
type: "gene"
col: 2743
ensembl_id: "ENSG00000106327"
name: "transferrin receptor 2"
location: "7q22.1"
module: 132
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 40
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# TFR2

*transferrin receptor 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +9.4, q 3e-18, up in 3 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.55× (z +5.0, q 6e-05, up in 13 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.568× (z -6.3, q 2e-07, down in 14 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO7]] (+0.55, fdr 1e-05), [[VASH2]] (+0.54, fdr 4e-05), [[RNF125]] (+0.52, fdr 3e-05); moves opposite to [[RO60]] (-0.54, fdr 2e-05), [[LYST]] (-0.46, fdr 3e-05), [[TMEM14C]] (-0.46, fdr 5e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNX10]] → it (grade B ⚠); 3 go from it, the strongest it → [[BUD23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +9.4 | 3e-18 | 3/13 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.4 | 1e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +7.1 | 3e-10 | 9/18 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.3 | 1e-05 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +5.0 | 6e-05 | 13/31 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +4.6 | 5e-04 | 7/27 (A-427, A498, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.011 | 4/23 (SW48, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.7 | 0.015 | 4/22 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.6 | 0.019 | 1/9 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.021 | 5/30 (SW480, HT-29, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.037 | 3/23 (SK-MEL-2, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.037 | 2/31 (HOP62, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.044 | 0/30 | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.063 | 0/24 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.1 | 0.063 | 0/12 | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -6.3 | 2e-07 | 14/32 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -5.9 | 1e-06 | 11/30 (KATO III, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -5.8 | 1e-06 | 20/35 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.6 | 5e-04 | 18/27 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.773×** | -4.2 | 0.003 | 15/29 (NCI-H23, SW48, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.0 | 0.007 | 10/33 (RKO, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.759× | -3.2 | 0.13 | 6/32 (HT-29, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0669× (z -13.1) |
| [[SW48 (line)]] | wt | 11.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0517× (z -10.8) |
| [[RKO (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0781× (z -11.9) |
| [[LS 180 (line)]] | wt | 4.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0573× (z -9.3) |
| [[A-172 (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.971 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO7]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[VASH2]] | +0.54 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[RNF125]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SHANK3]] | +0.52 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[BRSK2]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[NMRAL1]] | +0.52 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[KCNAB2]] | +0.51 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[CHRNA5]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[C2orf72]] | +0.51 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[WNK2]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ADCY3]] | +0.50 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[UCK2]] | +0.50 | +0.38 / +0.53 | both halves | 7e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[LYST]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TMEM14C]] | -0.46 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[WASL]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[SMIM14]] | -0.45 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[SLC38A4-AS1]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TNRC6C]] | -0.43 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[PHF20L1]] | -0.42 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[GABARAP]] ⚠ | -0.42 | -0.48 / -0.32 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MPC1]] | -0.42 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX10]] | B | SNX10 activity raises TFR2's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without SNX10 | 0.070 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BUD23]] | B | TFR2 activity raises BUD23's level | lines that do not express TFR2 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without TFR2 | 0.031 | ⚠ within organs, on part of the lines; also absent: KRTAP5-AS1, EFNA2, AP1G2; maybe low, not absent |
| [[SNX10]] | B | TFR2 activity raises SNX10's level | lines that do not express TFR2 (10) vs lines expressing it (40) | 2.87× lower at baseline in the lines without TFR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: KRTAP5-AS1, EFNA2, AP1G2; maybe low, not absent |
| [[SMIM14]] | B | TFR2 activity raises SMIM14's level | lines that do not express TFR2 (10) vs lines expressing it (40) | 1.41× lower at baseline in the lines without TFR2 | 0.097 | ⚠ within organs, on part of the lines; also absent: KRTAP5-AS1, EFNA2, AP1G2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.4, 44.2); signed map (-24.3, 38.0). **Vector** length 44.7, 6.73% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.0 | +4.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.9 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +3.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -4.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transferrin receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,620,416-100,642,779 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HFE3, TFRC2 |
| Gene groups (HGNC) | M28 metallopeptidases |
| Reactome | 5 pathways, smallest: Transferrin endocytosis and recycling; Iron uptake and transport; Cotranslational targeting of proteins to the endoplasmic reticulum |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UP52](https://www.uniprot.org/uniprotkb/Q9UP52) (Transferrin receptor protein 2):

> Mediates cellular uptake of transferrin-bound iron in a non-iron dependent manner. May be involved in iron metabolism, hepatocyte function and erythrocyte differentiation.

**Summary**, from NCBI Gene [7036](https://www.ncbi.nlm.nih.gov/gene/7036):

> This gene encodes a single-pass type II membrane protein, which is a member of the transferrin receptor-like family. This protein mediates cellular uptake of transferrin-bound iron, and may be involved in iron metabolism, hepatocyte function and erythrocyte differentiation. Mutations in this gene have been associated with hereditary hemochromatosis type III. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:11762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11762) · Entrez [7036](https://www.ncbi.nlm.nih.gov/gene/7036) · UniProt [Q9UP52](https://www.uniprot.org/uniprotkb/Q9UP52) · Ensembl [ENSG00000106327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106327)

## Data

Gene col 2743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2743); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2743]; `tensor/DDL_lfc|DDL_z.npy` [2743]; `embed/gene_vectors.npy` [2743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2743 or target_col == 2743). Every well: [[TFR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
