---
symbol: "CELF2"
type: "gene"
col: 540
ensembl_id: "ENSG00000048740"
name: "CUGBP Elav-like family member 2"
location: "10p14"
module: 102
arm: "+"
pooled_cpm: 70.31
n_lines_expressing: 26
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# CELF2

*CUGBP Elav-like family member 2* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +16.9, q 0e+00, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.572× (z -13.0, q 6e-36, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY1]] (+0.58, fdr 1e-05), [[DOCK3]] (+0.51, fdr 7e-05), [[SRCIN1]] (+0.50, fdr 5e-05); moves opposite to [[SENP2]] (-0.42, fdr 1e-04), [[DHX8]] (-0.37, fdr 1e-04), [[NPIPB14P]] (-0.37, fdr 8e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[PVT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +16.9 | 0e+00 | 13/24 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +13.5 | 6e-39 | 13/24 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +9.8 | 2e-20 | 15/25 (LS 180, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.2 | 1e-10 | 4/16 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.2 | 7e-08 | 4/24 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +6.0 | 2e-07 | 5/21 (Panc 03.27, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.5 | 4e-06 | 7/23 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.4 | 4e-06 | 9/24 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 4e-06 | 8/24 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.0 | 3e-05 | 3/23 (C32, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.2 | 0.001 | 8/23 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 5/24 (LoVo, LS 180, …) | rises with dose |  |
| [[Verteporfin (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.004 | 0/24 | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.18× | +3.6 | 0.011 | 4/24 (LoVo, HCT15, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.014 | 9/24 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.5 | 0.019 | 2/23 (SW 900, hTERT-HPNE) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.021 | 0/25 | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.044 | 6/25 (LS 180, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.061 | 10/24 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.074 | 4/23 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.077 | 9/24 (SW1417, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.094 | 2/23 (HEC-1-A, NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.572×** | -13.0 | 6e-36 | 19/24 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -12.2 | 1e-31 | 19/24 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.642×** | -10.3 | 1e-22 | 16/24 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -8.0 | 2e-13 | 13/22 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.779×** | -5.8 | 7e-07 | 9/23 (hTERT-HPNE, SK-MEL-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.826×** | -4.4 | 8e-04 | 9/24 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.842× | -4.0 | 0.005 | 5/23 (BT-474, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.844× | -3.8 | 0.010 | 11/24 (HEC-1-A, HCT15, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 208 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -11.5) |
| [[C-33 A (line)]] | alt | 861 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0561× (z -26.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.122× (z -20.6) |
| [[J82 (line)]] | alt | 120 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.259× (z -14.7) |
| [[LoVo (line)]] | wt | 85.7 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +21.2) | [[Auranofin (drug)]] 5 µM 0.413× (z -9.7) |
| [[BT-474 (line)]] | alt | 50.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -10.3) |
| [[A-427 (line)]] | wt | 903 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -18.3) |
| [[C32 (line)]] | wt | 38.9 | 3 (2 ⚠) | 0 | [[Binimetinib (drug)]] 5 µM 3.77× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 99.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +16.6) | — |
| [[SK-MEL-2 (line)]] | alt | 271 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -14.0) |
| [[HCT15 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -16.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -11.3) |
| [[SW48 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY1]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DOCK3]] | +0.51 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[SRCIN1]] | +0.50 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[SLC6A11]] | +0.50 | +0.49 / +0.27 | both halves | 3e-04 |  |
| [[UBE2QL1]] | +0.48 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[NCS1]] | +0.47 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[NKAIN3]] | +0.46 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[SUGCT]] | +0.45 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[PVT1]] | +0.45 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[GNAL]] | +0.44 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[LINC02026]] | +0.44 | +0.39 / +0.29 | both halves | 2e-04 |  |
| [[DGCR5]] | +0.44 | +0.43 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP2]] | -0.42 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[DHX8]] | -0.37 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[NPIPB14P]] | -0.37 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[MBD4]] | -0.36 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[ABHD16A]] | -0.35 | -0.25 / -0.34 | both halves | 4e-04 |  |
| [[VCPKMT]] | -0.35 | -0.27 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CELF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01036]] | C | LINC01036 activity raises CELF2's level | lines that do not express LINC01036 (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without LINC01036 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MSR1, IHO1, ENSG00000250038; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PVT1]] | B | CELF2 activity lowers PVT1's level | lines that do not express CELF2 (24) vs lines expressing it (26) | 1.48× higher at baseline in the lines without CELF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENPP5, LMO3, GNAT3 |
| [[PDE5A]] | B | CELF2 activity raises PDE5A's level | lines that do not express CELF2 (24) vs lines expressing it (26) | 1.45× lower at baseline in the lines without CELF2 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENPP5, LMO3, GNAT3 |
| [[ZNF385B]] | B | CELF2 activity raises ZNF385B's level | lines that do not express CELF2 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without CELF2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENPP5, LMO3, GNAT3 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.481). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.1, 36.5); signed map (25.6, 23.4). **Vector** length 64.1, 15.1% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +16.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.2 | -1.8 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.1 | -8.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | +0.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[Sodium Salicylate (drug)]] 5 µM |  | -0.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CUGBP Elav-like family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:10,798,397-11,336,675 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Etr-3, NAPOR-2, BRUNOL3; previously CUGBP2 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [O95319](https://www.uniprot.org/uniprotkb/O95319) (CUGBP Elav-like family member 2):

> RNA-binding protein implicated in the regulation of several post-transcriptional events. Involved in pre-mRNA alternative splicing, mRNA translation and stability. Mediates exon inclusion and/or exclusion in pre-mRNA that are subject to tissue-specific and developmentally regulated alternative splicing. Specifically activates exon 5 inclusion of TNNT2 in embryonic, but not adult, skeletal muscle. Activates TNNT2 exon 5 inclusion by antagonizing the repressive effect of PTB. Acts both as an …

**Summary**, from NCBI Gene [10659](https://www.ncbi.nlm.nih.gov/gene/10659):

> Members of the CELF/BRUNOL protein family contain two N-terminal RNA recognition motif (RRM) domains, one C-terminal RRM domain, and a divergent segment of 160-230 aa between the second and third RRM domains. Members of this protein family regulate pre-mRNA alternative splicing and may also be involved in mRNA editing, and translation. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2550) · Entrez [10659](https://www.ncbi.nlm.nih.gov/gene/10659) · UniProt [O95319](https://www.uniprot.org/uniprotkb/O95319) · Ensembl [ENSG00000048740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048740)

## Data

Gene col 540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 540); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 540]; `tensor/DDL_lfc|DDL_z.npy` [540]; `embed/gene_vectors.npy` [540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 540 or target_col == 540). Every well: [[CELF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
