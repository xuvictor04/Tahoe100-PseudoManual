---
symbol: "GLI3"
type: "gene"
col: 2776
ensembl_id: "ENSG00000106571"
name: "GLI family zinc finger 3"
location: "7p14.1"
module: 121
arm: "+"
pooled_cpm: 50.46
n_lines_expressing: 31
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# GLI3

*GLI family zinc finger 3* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +6.9, q 2e-09, up in 18 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.568× (z -5.7, q 7e-06, down in 18 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.622× (z -5.2, q 7e-05, down in 21 of 29 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR548XHG]] (+0.59, fdr 1e-05), [[SOX5]] (+0.57, fdr 2e-05), [[FLRT2]] (+0.57, fdr 2e-05); moves opposite to [[CAPN5]] (-0.49, fdr 1e-04), [[GOLPH3L]] (-0.48, fdr 2e-04), [[CASP9]] (-0.47, fdr 2e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NPAS3]] → it (grade B ⚠); 5 go from it, the strongest it → [[NPAS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.9 | 2e-09 | 18/29 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.6 | 5e-06 | 19/29 (A498, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.027 | 15/29 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.34× | +3.2 | 0.21 | 15/29 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.22× | +3.1 | 0.23 | 12/29 (HEC-1-A, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.568×** | -5.7 | 7e-06 | 18/26 (SNU-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -5.2 | 7e-05 | 21/29 (SW480, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.416×** | -5.0 | 1e-04 | 19/28 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.637×** | -4.9 | 1e-04 | 18/29 (SW480, SNU-1, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.639×** | -4.9 | 1e-04 | 17/29 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -4.8 | 2e-04 | 18/29 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.736×** | -4.7 | 2e-04 | 21/29 (SHP-77, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.666×** | -4.4 | 7e-04 | 17/29 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.655×** | -4.4 | 8e-04 | 17/29 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -4.3 | 8e-04 | 18/29 (SW480, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -4.1 | 0.002 | 16/24 (CHP-212, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -3.9 | 0.005 | 15/30 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.703×** | -3.8 | 0.005 | 15/29 (SW1417, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.719×** | -3.6 | 0.013 | 14/28 (SW480, SW1417, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.676×** | -3.5 | 0.019 | 17/29 (LOX-IMVI, SNU-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.020 | 18/29 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.031 | 17/29 (CHP-212, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -3.3 | 0.031 | 14/29 (SW480, SNU-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.692×** | -3.3 | 0.033 | 11/28 (C32, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.045 | 16/30 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.748×** | -3.0 | 0.062 | 13/28 (BT-474, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 224 | 0 | 15 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -15.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -14.3) |
| [[SNU-1 (line)]] | wt | 446 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0384× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.147× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 22.5 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.43× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -12.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -8.8) |
| [[C32 (line)]] | wt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 86.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 75.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 42.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 247 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0546× (z -15.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 43.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -9.0) |
| [[A-427 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.73 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR548XHG]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SOX5]] | +0.57 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[FLRT2]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PCDH7]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ARHGAP24]] | +0.56 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[NPAS3]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[EGFEM1P]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CACNA2D1]] | +0.53 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[CNTLN]] | +0.52 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[FGF13]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[USP13]] | +0.52 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[TCF12]] | +0.51 | +0.49 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN5]] | -0.49 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[GOLPH3L]] | -0.48 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[CASP9]] | -0.47 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[CDA]] | -0.46 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[PIGH]] | -0.46 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[ZNF552]] | -0.46 | -0.27 / -0.36 | both halves | 3e-04 | same gene group |
| [[ZNF567-DT]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[TVP23C]] | -0.46 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[SGSM1]] | -0.46 | -0.34 / -0.32 | both halves | 1e-04 |  |
| [[PLD3]] | -0.46 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[SEC11C]] | -0.46 | -0.33 / -0.26 | both halves | 3e-04 |  |
| [[HID1]] | -0.45 | -0.33 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS3]] | B | NPAS3 activity raises GLI3's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 4.85× lower at baseline in the lines without NPAS3 | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[CSMD3]] | B | CSMD3 activity raises GLI3's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.36× lower at baseline in the lines without CSMD3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[CSMD3]] | B | CSMD3 activity strengthens GLI3's drug response | lines that do not express CSMD3 (20) vs lines expressing it (9) | the lines without CSMD3 respond 0.90× as strongly (z diff +0.73); strongest at Belinostat 5 µM: 0.77x vs 0.49x (z diff +3.2) | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; target measured in part of the lines; both ways; artifact flags |
| [[SOX5]] | B | SOX5 activity raises GLI3's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without SOX5 | 0.099 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5 |
| [[FGF13]] | C | FGF13 activity raises GLI3's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 5.23× lower at baseline in the lines without FGF13 | 0.004 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[MIR548XHG]] | C | MIR548XHG activity raises GLI3's level | lines that do not express MIR548XHG (38) vs lines expressing it (12) | 3.70× lower at baseline in the lines without MIR548XHG | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000291025, UBBP4-1, COX7B2; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS3]] | B | GLI3 activity raises NPAS3's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without GLI3 | 0.012 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2 |
| [[ATXN7]] | B | GLI3 activity raises ATXN7's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 1.16× lower at baseline in the lines without GLI3 | 0.075 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2 |
| [[FGF13]] | C | GLI3 activity raises FGF13's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 4.30× lower at baseline in the lines without GLI3 | 0.014 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2; co-absent with the target |
| [[CHSY3]] | C | GLI3 activity raises CHSY3's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 3.53× lower at baseline in the lines without GLI3 | 0.071 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2; co-absent with the target |
| [[MIR548XHG]] | C | GLI3 activity raises MIR548XHG's level | lines that do not express GLI3 (19) vs lines expressing it (31) | 2.69× lower at baseline in the lines without GLI3 | 0.077 | ⚠ within organs, on part of the lines; also absent: GPNMB, SLIT2, PRICKLE2; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, 25.2); signed map (44.2, 26.8). **Vector** length 78.9, 20.6% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.8 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.8 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.6 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +3.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.4 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | GLI family zinc finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:41,960,949-42,264,100 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP-A, PAPA, PAPA1, PAPB, ACLS, PPDIV; previously GCPS, PHS |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 8 pathways, smallest: GLI proteins bind promoters of Hh responsive genes to promote transcription; RUNX2 regulates osteoblast differentiation; RUNX2 regulates bone development |
| Matched by | ensembl_id |

**Function**, from UniProt [P10071](https://www.uniprot.org/uniprotkb/P10071) (Transcription activator GLI3):

> Transcription factor that acts as a key effector of the smoothened signaling pathway, and which plays a role in the development and patterning of various body structures, including the brain and limbs. Specifically binds to the minimal GLI-consensus sequence 5'-GACCACCCA-3' to activate or repress the expression of target genes. Functions both as a transcriptional activator and repressor: the full-length GLI3 form (Transcription activator GLI3) acts as a transcription activator following …

**Summary**, from NCBI Gene [2737](https://www.ncbi.nlm.nih.gov/gene/2737):

> This gene encodes a protein which belongs to the C2H2-type zinc finger proteins subclass of the Gli family. They are characterized as DNA-binding transcription factors and are mediators of Sonic hedgehog (Shh) signaling. The protein encoded by this gene localizes in the cytoplasm and activates patched Drosophila homolog (PTCH) gene expression. It is also thought to play a role during embryogenesis. Mutations in this gene have been associated with several diseases, including Greig …

**Accessions** — [HGNC:4319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4319) · Entrez [2737](https://www.ncbi.nlm.nih.gov/gene/2737) · UniProt [P10071](https://www.uniprot.org/uniprotkb/P10071) · Ensembl [ENSG00000106571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106571)

## Data

Gene col 2776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2776); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2776]; `tensor/DDL_lfc|DDL_z.npy` [2776]; `embed/gene_vectors.npy` [2776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2776 or target_col == 2776). Every well: [[GLI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
