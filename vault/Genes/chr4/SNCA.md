---
symbol: "SNCA"
type: "gene"
col: 6976
ensembl_id: "ENSG00000145335"
name: "synuclein alpha"
location: "4q22.1"
module: 19
arm: "+"
pooled_cpm: 46.73
n_lines_expressing: 21
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SNCA

*synuclein alpha* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +12.8, q 6e-35, up in 7 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +9.8, q 4e-20, up in 15 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.648× (z -6.4, q 1e-07, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK5]] (+0.70, fdr 7e-06), [[ASXL3]] (+0.67, fdr 7e-06), [[RBM20]] (+0.67, fdr 7e-06); moves opposite to [[ZNF597]] (-0.46, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); 11 go from it, the strongest it → [[KLHL13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +12.8 | 6e-35 | 7/18 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +9.8 | 4e-20 | 15/19 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +9.2 | 5e-18 | 6/18 (J82, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +8.0 | 2e-13 | 6/17 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.6 | 5e-09 | 15/19 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.3 | 1e-05 | 7/19 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.41×** | +5.0 | 4e-05 | 4/19 (A498, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.8 | 1e-04 | 6/19 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 9/19 (J82, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.033 | 0/19 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.4 | 0.033 | 5/19 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.035 | 1/19 (HOP62) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.035 | 14/19 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.035 | 1/19 (SHP-77) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.043 | 0/19 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.059 | 0/19 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.060 | 1/19 (HOP62) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.062 | 4/19 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.064 | 7/19 (SNU-423, CHP-212, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.071 | 8/19 (NCI-H23, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.084 | 0/19 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -6.4 | 1e-07 | 12/19 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -4.7 | 9e-04 | 11/19 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.733×** | -4.4 | 0.002 | 11/19 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -4.2 | 0.003 | 8/19 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.817×** | -4.2 | 0.003 | 12/19 (NCI-H460, LOX-IMVI, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.580×** | -4.2 | 0.003 | 16/19 (NCI-H460, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -4.1 | 0.003 | 11/19 (NCI-H460, C-33 A, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.614×** | -3.8 | 0.012 | 8/19 (C32, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucatinib (drug)]] 0.5 µM |  | **0.711×** | -3.6 | 0.022 | 0/19 | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.785×** | -3.3 | 0.053 | 1/19 (LOX-IMVI) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.794×** | -3.3 | 0.054 | 2/19 (NCI-H460, NCI-H661) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.861× | -3.1 | 0.077 | 12/19 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.077 | 1/19 (PANC-1) | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | **0.749×** | -3.0 | 0.087 | 0/19 | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.674×** | -3.0 | 0.087 | 0/19 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.801×** | -3.0 | 0.087 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 323 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -12.8) |
| [[C-33 A (line)]] | alt | 290 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.81× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.46× (z +9.5) | — |
| [[A-427 (line)]] | wt | 434 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.1) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 40.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -9.5) |
| [[C32 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.28× (z +8.5) ⚠ toxic | — |
| [[J82 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 68.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.89× (z +11.0) ⚠ position not correctable | — |
| [[PANC-1 (line)]] | alt | 20.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 13.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +10.1) | — |
| [[A-172 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK5]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ASXL3]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[RBM20]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GALNT13]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NCAM2]] | +0.65 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[KLHL13]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LRRC63]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SCN9A]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[GLRB]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CDH10]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[TENM1]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CTNNA2]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF597]] | -0.46 | -0.35 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises SNCA's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without ANK2 | 0.030 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[BCHE]] | C | BCHE activity raises SNCA's level | lines that do not express BCHE (35) vs lines expressing it (15) | 5.25× lower at baseline in the lines without BCHE | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CNKSR2]] | C | CNKSR2 activity raises SNCA's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 6.56× lower at baseline in the lines without CNKSR2 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises SNCA's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 5.58× lower at baseline in the lines without EPHA5 | 0.040 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises SNCA's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 6.11× lower at baseline in the lines without MIR99AHG | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[ANO5]] | C | ANO5 activity raises SNCA's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 3.34× lower at baseline in the lines without ANO5 | 0.057 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises SNCA's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 6.43× lower at baseline in the lines without KCNH5 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[EPB41L3]] | C | EPB41L3 activity raises SNCA's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 4.49× lower at baseline in the lines without EPB41L3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[UNC5C]] | C | UNC5C activity raises SNCA's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without UNC5C | 0.089 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL13]] | B | SNCA activity raises KLHL13's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without SNCA | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10 |
| [[ANK2]] | B | SNCA activity raises ANK2's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.82× lower at baseline in the lines without SNCA | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10 |
| [[SLC6A15]] | C | SNCA activity raises SLC6A15's level | lines that do not express SNCA (29) vs lines expressing it (21) | 6.20× lower at baseline in the lines without SNCA | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[BMP5]] | C | SNCA activity raises BMP5's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.73× lower at baseline in the lines without SNCA | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[ZFHX4]] | C | SNCA activity raises ZFHX4's level | lines that do not express SNCA (29) vs lines expressing it (21) | 6.37× lower at baseline in the lines without SNCA | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[KCNH5]] | C | SNCA activity raises KCNH5's level | lines that do not express SNCA (29) vs lines expressing it (21) | 4.35× lower at baseline in the lines without SNCA | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[MARCHF1]] | C | SNCA activity raises MARCHF1's level | lines that do not express SNCA (29) vs lines expressing it (21) | 3.22× lower at baseline in the lines without SNCA | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[CARD18]] | C | SNCA activity raises CARD18's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.16× lower at baseline in the lines without SNCA | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[EPHA5]] | C | SNCA activity raises EPHA5's level | lines that do not express SNCA (29) vs lines expressing it (21) | 4.30× lower at baseline in the lines without SNCA | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[ARHGAP28]] | C | SNCA activity raises ARHGAP28's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without SNCA | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |
| [[CTNNA2]] | C | SNCA activity raises CTNNA2's level | lines that do not express SNCA (29) vs lines expressing it (21) | 3.44× lower at baseline in the lines without SNCA | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.4, 35.2); signed map (40.3, 37.7). **Vector** length 71.8, 22.5% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -4.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | synuclein alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:89,700,345-89,838,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NACP, PD1; previously PARK1, PARK4 |
| Gene groups (HGNC) | Synuclein family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Amyloid fiber formation; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P37840](https://www.uniprot.org/uniprotkb/P37840) (Alpha-synuclein):

> Neuronal protein that plays several roles in synaptic activity such as regulation of synaptic vesicle trafficking and subsequent neurotransmitter release. Participates as a monomer in synaptic vesicle exocytosis by enhancing vesicle priming, fusion and dilation of exocytotic fusion pores. Mechanistically, acts by increasing local Ca(2+) release from microdomains which is essential for the enhancement of ATP-induced exocytosis. Also acts as a molecular chaperone in its multimeric membrane-bound …

**Summary**, from NCBI Gene [6622](https://www.ncbi.nlm.nih.gov/gene/6622):

> Alpha-synuclein is a member of the synuclein family, which also includes beta- and gamma-synuclein. Synucleins are abundantly expressed in the brain and alpha- and beta-synuclein inhibit phospholipase D2 selectively. SNCA may serve to integrate presynaptic signaling and membrane trafficking. Defects in SNCA have been implicated in the pathogenesis of Parkinson disease. SNCA peptides are a major component of amyloid plaques in the brains of patients with Alzheimer's disease. Alternatively …

**Accessions** — [HGNC:11138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11138) · Entrez [6622](https://www.ncbi.nlm.nih.gov/gene/6622) · UniProt [P37840](https://www.uniprot.org/uniprotkb/P37840) · Ensembl [ENSG00000145335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145335)

## Data

Gene col 6976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6976); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6976]; `tensor/DDL_lfc|DDL_z.npy` [6976]; `embed/gene_vectors.npy` [6976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6976 or target_col == 6976). Every well: [[SNCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
