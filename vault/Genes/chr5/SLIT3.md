---
symbol: "SLIT3"
type: "gene"
col: 11521
ensembl_id: "ENSG00000184347"
name: "slit guidance ligand 3"
location: "5q34-q35.1"
module: 13
arm: "+"
pooled_cpm: 18.58
n_lines_expressing: 19
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 14
direction_downstream: 10
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SLIT3

*slit guidance ligand 3* — 5q34-q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +16.4, q 0e+00, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.626× (z -6.4, q 9e-08, down in 14 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLIS1]] (+0.61, fdr 1e-05), [[RNF212]] (+0.61, fdr 3e-05), [[SFRP1]] (+0.60, fdr 2e-05); moves opposite to [[CSF3]] (-0.48, fdr 5e-05), [[BTN2A1]] (-0.48, fdr 1e-04), [[RNF146]] (-0.47, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TRIM9]] → it (grade B ⚠); 10 go from it, the strongest it → [[GXYLT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +16.4 | 0e+00 | 4/17 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +15.3 | 0e+00 | 2/15 (SK-MEL-2, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +12.9 | 9e-36 | 1/10 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +12.8 | 3e-35 | 12/17 (J82, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +9.4 | 6e-19 | 2/12 (A498, SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +7.5 | 5e-12 | 3/17 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +6.9 | 5e-10 | 11/17 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.7 | 1e-09 | 7/17 (SW1417, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.8 | 6e-07 | 1/17 (BT-474) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.5 | 2e-06 | 1/14 (SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.27×** | +4.8 | 1e-04 | 8/17 (A498, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.7 | 1e-04 | 4/13 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.4 | 4e-04 | 1/17 (A498) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.33×** | +4.1 | 0.002 | 8/17 (A498, J82, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 4/16 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.003 | 11/17 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.009 | 11/17 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.019 | 3/17 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.019 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.026 | 0/17 | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.030 | 4/17 (PANC-1, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.626×** | -6.4 | 9e-08 | 14/17 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -5.0 | 2e-04 | 11/17 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.734×** | -4.4 | 0.002 | 1/17 (J82) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.808×** | -4.3 | 0.002 | 6/17 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.738×** | -4.1 | 0.005 | 0/17 | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.742×** | -4.0 | 0.006 | 13/17 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.764×** | -3.8 | 0.010 | 14/17 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.777×** | -3.6 | 0.023 | 12/17 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.099 | 2/17 (SNU-423, HOP62) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.13 | 4/17 (A498, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 54.9 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -13.4) |
| [[PANC-1 (line)]] | alt | 81.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -24.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.259× (z -10.9) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0902× (z -27.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.220× (z -11.8) |
| [[SW 900 (line)]] | alt | 38.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -23.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.151× (z -10.9) |
| [[A549 (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -18.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.205× (z -10.3) |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.245× (z -9.4) |
| [[A498 (line)]] | wt | 7.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 67.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -10.2) |
| [[J82 (line)]] | alt | 8.85 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.61× (z +9.9) | — |
| [[A-172 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.50 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIS1]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RNF212]] | +0.61 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SFRP1]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[MEG8]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PTPRS]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MIR493HG]] | +0.58 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SPANXA2-OT1]] | +0.58 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[HMCN1]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ZNF677]] | +0.55 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CACNG7]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[CCNYL2]] | +0.54 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[LAYN]] | +0.54 | +0.57 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF3]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[BTN2A1]] | -0.48 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[RNF146]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[LINC00869-1]] | -0.46 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ZNF101]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ZNF700]] | -0.45 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[FBXW4]] | -0.45 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[HOMEZ]] | -0.44 | -0.36 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 3, C 11. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM9]] | B | TRIM9 activity raises SLIT3's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.94× lower at baseline in the lines without TRIM9 | 0.040 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[OCA2]] | B | OCA2 activity raises SLIT3's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 2.87× lower at baseline in the lines without OCA2 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SLIT3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GLYATL2]] | C | GLYATL2 activity raises SLIT3's level | lines that do not express GLYATL2 (37) vs lines expressing it (13) | 4.26× lower at baseline in the lines without GLYATL2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000234426, VCAM1, LINC02476; co-absent with the target |
| [[LINC00842]] | C | LINC00842 activity raises SLIT3's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without LINC00842 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2; co-absent with the target |
| [[STAC]] | C | STAC activity raises SLIT3's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.31× lower at baseline in the lines without STAC | 0.037 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |
| [[MYLK]] | C | MYLK activity raises SLIT3's level | lines that do not express MYLK (20) vs lines expressing it (30) | 2.71× lower at baseline in the lines without MYLK | 0.041 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[RNF182]] | C | RNF182 activity raises SLIT3's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 3.24× lower at baseline in the lines without RNF182 | 0.046 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615; co-absent with the target |
| [[MEG3]] | C | MEG3 activity raises SLIT3's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 3.32× lower at baseline in the lines without MEG3 | 0.055 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises SLIT3's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 3.78× lower at baseline in the lines without MIR493HG | 0.060 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[SLC66A1L]] | C | SLC66A1L activity raises SLIT3's level | lines that do not express SLC66A1L (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without SLC66A1L | 0.062 | ⚠ within organs, on part of the lines; also absent: MIR137HG, ADAMTS12, SLC8A1; co-absent with the target |
| [[SFRP1]] | C | SFRP1 activity raises SLIT3's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 3.00× lower at baseline in the lines without SFRP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | SLIT3 activity raises GXYLT2's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.19× lower at baseline in the lines without SLIT3 | 0.069 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3 |
| [[COL18A1]] | B | SLIT3 activity raises COL18A1's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.20× lower at baseline in the lines without SLIT3 | 0.096 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3 |
| [[MYLK]] | C | SLIT3 activity raises MYLK's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 4.72× lower at baseline in the lines without SLIT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[GLYATL2]] | C | SLIT3 activity raises GLYATL2's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 4.49× lower at baseline in the lines without SLIT3 | 0.011 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[COL5A1]] | C | SLIT3 activity raises COL5A1's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 6.58× lower at baseline in the lines without SLIT3 | 0.023 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[DKK3]] | C | SLIT3 activity raises DKK3's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without SLIT3 | 0.050 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[SFRP1]] | C | SLIT3 activity raises SFRP1's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without SLIT3 | 0.050 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[RNF182]] | C | SLIT3 activity raises RNF182's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.38× lower at baseline in the lines without SLIT3 | 0.054 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[LINC00842]] | C | SLIT3 activity raises LINC00842's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without SLIT3 | 0.086 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[CCNYL2]] | C | SLIT3 activity raises CCNYL2's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 2.81× lower at baseline in the lines without SLIT3 | 0.096 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.445). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.0, 20.6); signed map (26.7, 43.7). **Vector** length 50.3, 13.7% of its response variance represented; |z| ≥ 3 in 446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | slit guidance ligand 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34-q35.1 — chr5:168,661,740-169,301,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | slit2, MEGF5, SLIT1, Slit-3; previously SLIL2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Slit guidance ligands |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 5 pathways, smallest: Regulation of commissural axon pathfinding by SLIT and ROBO; Netrin-1 signaling; Signaling by ROBO receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75094](https://www.uniprot.org/uniprotkb/O75094) (Slit homolog 3 protein):

> May act as molecular guidance cue in cellular migration, and function may be mediated by interaction with roundabout homolog receptors.

**Summary**, from NCBI Gene [6586](https://www.ncbi.nlm.nih.gov/gene/6586):

> The protein encoded by this gene is secreted, likely interacting with roundabout homolog receptors to effect cell migration. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:11087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11087) · Entrez [6586](https://www.ncbi.nlm.nih.gov/gene/6586) · UniProt [O75094](https://www.uniprot.org/uniprotkb/O75094) · Ensembl [ENSG00000184347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184347)

## Data

Gene col 11521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11521); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11521]; `tensor/DDL_lfc|DDL_z.npy` [11521]; `embed/gene_vectors.npy` [11521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11521 or target_col == 11521). Every well: [[SLIT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLIT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
