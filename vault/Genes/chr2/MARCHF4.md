---
symbol: "MARCHF4"
type: "gene"
col: 6899
ensembl_id: "ENSG00000144583"
name: "membrane associated ring-CH-type finger 4"
location: "2q35"
module: 116
arm: "+"
pooled_cpm: 51.41
n_lines_expressing: 22
n_dd_up: 27
n_dd_down: 37
n_dd_up_clean: 19
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# MARCHF4

*membrane associated ring-CH-type finger 4* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.60× (z +9.7, q 1e-19, up in 16 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (1 with an alert ⚠); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.551× (z -7.2, q 3e-10, down in 11 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAV3]] (+0.73, fdr 7e-06), [[SRGAP1]] (+0.69, fdr 7e-06), [[ITGB1-DT]] (+0.69, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.51, fdr 2e-05), [[B4GALT1]] (-0.51, fdr 2e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LRRC8C]] → it (grade B ⚠); 2 go from it, the strongest it → [[FJX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.60×** | +9.7 | 1e-19 | 16/20 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +7.0 | 6e-10 | 15/19 (HOP62, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.81×** | +7.0 | 6e-10 | 16/19 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.72×** | +6.6 | 4e-09 | 14/19 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.46×** | +6.6 | 6e-09 | 12/20 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.70×** | +6.5 | 9e-09 | 14/20 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.62×** | +5.9 | 3e-07 | 2/19 (SW480, H4) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 7/20 (SW480, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.57×** | +5.5 | 2e-06 | 12/19 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **2.35×** | +5.5 | 3e-06 | 12/18 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.33×** | +5.4 | 3e-06 | 6/16 (A549, H4, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.84×** | +5.3 | 5e-06 | 13/20 (SW480, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.54×** | +5.3 | 6e-06 | 12/19 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.9 | 3e-05 | 2/20 (hTERT-HPNE, C32) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.8 | 5e-05 | 8/20 (hTERT-HPNE, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.8 | 6e-05 | 11/20 (NCI-H460, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 2e-04 | 11/20 (A549, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.42×** | +4.2 | 9e-04 | 1/19 (C32) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.004 | 5/19 (A549, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 2 with an alert ⚠; shown: the 15 strongest. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6899.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.551×** | -7.2 | 3e-10 | 11/19 (NCI-H460, H4, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.537×** | -7.0 | 9e-10 | 12/19 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.560×** | -6.8 | 3e-09 | 16/19 (NCI-H23, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.586×** | -6.5 | 1e-08 | 16/20 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.595×** | -6.3 | 3e-08 | 13/19 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.671×** | -6.0 | 2e-07 | 16/20 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.598×** | -5.8 | 7e-07 | 13/19 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.641×** | -5.4 | 6e-06 | 13/19 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.655×** | -5.1 | 2e-05 | 13/20 (J82, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.750×** | -4.8 | 7e-05 | 11/20 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.671×** | -4.8 | 7e-05 | 13/20 (NCI-H23, J82, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.676×** | -4.7 | 1e-04 | 15/19 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.669×** | -4.7 | 1e-04 | 13/19 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.717×** | -4.6 | 2e-04 | 9/20 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.689×** | -4.5 | 3e-04 | 13/20 (NCI-H1573, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 362 | 1 | 23 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +10.4) | [[Adagrasib (drug)]] 0.05 µM 0.526× (z -19.7) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.170× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 41.6 | 6 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.5× (z +10.3) | [[Clobetasol propionate (drug)]] 0.05 µM 0.225× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 438 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.05× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -13.9) |
| [[A-427 (line)]] | wt | 387 | 0 | 7 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -13.1) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.304× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 202 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -16.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -13.1) |
| [[A549 (line)]] | wt | 73.7 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +8.9) | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 4 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0547× (z -12.5) |
| [[J82 (line)]] | alt | 33.6 | 0 | 4 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.107× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 22.4 | 4 (2 ⚠) | 0 | [[Peretinoin (drug)]] 5 µM 13.4× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 1271 (line)]] | alt | 122 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -9.7) |
| [[PANC-1 (line)]] | alt | 62.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 17.7 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.66× (z +9.5) | — |
| [[A-172 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.44 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAV3]] | +0.73 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[SRGAP1]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SLC35F3]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ROBO4]] | +0.68 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[BCL2A1]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RGS4]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SCHIP1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[DSCAM]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SFTA1P]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ADTRP]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[B4GALT1]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8C]] | B | LRRC8C activity raises MARCHF4's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 3.03× lower at baseline in the lines without LRRC8C | 0.059 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers MARCHF4's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[CDH4]] | C | CDH4 activity raises MARCHF4's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 4.12× lower at baseline in the lines without CDH4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT; co-absent with the target |
| [[DAW1]] | C | DAW1 activity raises MARCHF4's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 4.80× lower at baseline in the lines without DAW1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FJX1]] | B | MARCHF4 activity raises FJX1's level | lines that do not express MARCHF4 (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without MARCHF4 | 0.033 | ⚠ within organs, on part of the lines; also absent: PAMR1, BASP1-AS1, ENSG00000282849 |
| [[KIAA1549L]] | C | MARCHF4 activity raises KIAA1549L's level | lines that do not express MARCHF4 (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without MARCHF4 | 0.019 | ⚠ within organs, on part of the lines; also absent: PAMR1, BASP1-AS1, ENSG00000282849; co-absent with the target |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.5, 11.4); signed map (14.7, 44.7). **Vector** length 106, 33.9% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.0 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +6.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.8 | -6.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.5 | -6.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -4.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:216,257,865-216,372,483 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1399, MARCH-IV, RNF174; previously MARCH4 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2E8](https://www.uniprot.org/uniprotkb/Q9P2E8) (E3 ubiquitin-protein ligase MARCHF4):

> E3 ubiquitin-protein ligase that may mediate ubiquitination of MHC-I and CD4, and promote their subsequent endocytosis and sorting to lysosomes via multivesicular bodies. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer the ubiquitin to targeted substrates.

**Summary**, from NCBI Gene [57574](https://www.ncbi.nlm.nih.gov/gene/57574):

> MARCH4 is a member of the MARCH family of membrane-bound E3 ubiquitin ligases (EC 6.3.2.19). MARCH enzymes add ubiquitin (see MIM 191339) to target lysines in substrate proteins, thereby signaling their vesicular transport between membrane compartments. MARCH4 reduces surface accumulation of several membrane glycoproteins by directing them to the endosomal compartment (Bartee et al., 2004 [PubMed 14722266]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:29269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29269) · Entrez [57574](https://www.ncbi.nlm.nih.gov/gene/57574) · UniProt [Q9P2E8](https://www.uniprot.org/uniprotkb/Q9P2E8) · Ensembl [ENSG00000144583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144583)

## Data

Gene col 6899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6899); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6899]; `tensor/DDL_lfc|DDL_z.npy` [6899]; `embed/gene_vectors.npy` [6899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6899 or target_col == 6899). Every well: [[MARCHF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
