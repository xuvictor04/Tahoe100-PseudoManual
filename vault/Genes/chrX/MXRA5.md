---
symbol: "MXRA5"
type: "gene"
col: 2174
ensembl_id: "ENSG00000101825"
name: "matrix remodeling associated 5"
location: "Xp22.33"
module: 13
arm: "+"
pooled_cpm: 11.14
n_lines_expressing: 16
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 15
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MXRA5

*matrix remodeling associated 5* — Xp22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.99× (z +10.5, q 6e-23, up in 4 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +6.8, q 2e-09, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.408× (z -6.8, q 8e-09, down in 11 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.67, fdr 7e-06), [[B3GNT9]] (+0.63, fdr 1e-05), [[ARHGEF6]] (+0.59, fdr 1e-05); moves opposite to [[SSTR2]] (-0.46, fdr 3e-04), [[PLLP]] (-0.43, fdr 4e-05), [[ESRRA]] (-0.39, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NHS]] → it (grade B ⚠); 15 go from it, the strongest it → [[TPM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.99×** | +10.5 | 6e-23 | 4/12 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +10.2 | 8e-22 | 2/11 (BT-474, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.54×** | +8.9 | 2e-16 | 4/12 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.8 | 2e-09 | 2/13 (BT-474, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.73×** | +4.0 | 0.007 | 8/13 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.00×** | +3.7 | 0.017 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.6 | 0.031 | 0/12 | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | 1.49× | +3.0 | 0.17 | 4/13 (SNU-423, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.408×** | -6.8 | 8e-09 | 11/13 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -6.0 | 6e-07 | 11/13 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.546×** | -4.6 | 1e-03 | 11/14 (Hs 766T, A-172, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.569×** | -4.2 | 0.003 | 7/13 (SW1417, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.580×** | -4.1 | 0.004 | 12/13 (Hs 766T, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.581×** | -4.1 | 0.004 | 7/13 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.606×** | -3.8 | 0.012 | 4/13 (Hs 766T, Panc 03.27, …) | all doses, flat | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.595×** | -3.8 | 0.012 | 3/14 (Hs 766T, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -3.7 | 0.013 | 12/13 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | **0.614×** | -3.7 | 0.013 | 1/13 (SW1417) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.615×** | -3.7 | 0.013 | 5/13 (Hs 766T, HS-578T, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -3.5 | 0.022 | 9/13 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.630×** | -3.5 | 0.022 | 10/12 (A-172, Panc 03.27, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.639×** | -3.4 | 0.031 | 9/14 (CHP-212, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.642×** | -3.3 | 0.032 | 10/13 (A-172, RPMI-7951, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.662×** | -3.1 | 0.068 | 9/14 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -3.1 | 0.075 | 13/14 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.673×** | -3.0 | 0.092 | 3/13 (HS-578T, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 82.5 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0912× (z -10.9) |
| [[J82 (line)]] | alt | 45.0 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0937× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.125× (z -9.4) |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0215× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0447× (z -11.7) |
| [[Hs 766T (line)]] | wt | 137 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0942× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 5 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0662× (z -10.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0784× (z -9.6) |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0381× (z -10.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0537× (z -8.9) |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.00825× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0492× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0143× (z -17.2) |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0174× (z -13.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 4.66 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0341× (z -9.4) |
| [[A-427 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.815 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.762 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.553 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 581 |
| [[B3GNT9]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF6]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[APOBEC3G]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[SEMA5A]] | +0.57 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[LINC00842]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[DENND2A]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PDGFRB]] | +0.56 | +0.51 / +0.63 | both halves | 1e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TEK]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[SULF1]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 | STRING 496 |
| [[ANXA8]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[HTR1F]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSTR2]] | -0.46 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[PLLP]] | -0.43 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ESRRA]] | -0.39 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NHS]] | B | NHS activity raises MXRA5's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.68× lower at baseline in the lines without NHS | 0.087 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[ANXA8]] | C | ANXA8 activity raises MXRA5's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 4.77× lower at baseline in the lines without ANXA8 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises MXRA5's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.53× lower at baseline in the lines without COL5A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[LINC00842]] | C | LINC00842 activity raises MXRA5's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 2.71× lower at baseline in the lines without LINC00842 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises MXRA5's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.84× lower at baseline in the lines without DKK3 | 0.044 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises MXRA5's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 3.79× lower at baseline in the lines without GPR173 | 0.057 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[SSTR2]] | C | SSTR2 activity raises MXRA5's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 3.75× lower at baseline in the lines without SSTR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises MXRA5's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 3.35× lower at baseline in the lines without SEMA5A | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises MXRA5's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 3.11× lower at baseline in the lines without LAMA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 4, C 11. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPM1]] | B | MXRA5 activity raises TPM1's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.64× lower at baseline in the lines without MXRA5 | 0.046 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[SERPINB9P1]] | B | MXRA5 activity raises SERPINB9P1's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 1.56× lower at baseline in the lines without MXRA5 | 0.051 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[MYLK]] | B | MXRA5 activity raises MYLK's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 3.93× lower at baseline in the lines without MXRA5 | 0.093 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[SLC14A2]] | B | MXRA5 activity raises SLC14A2's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without MXRA5 | 0.095 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476 |
| [[COL5A1]] | C | MXRA5 activity raises COL5A1's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 7.42× lower at baseline in the lines without MXRA5 | 0.023 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[APCDD1L]] | C | MXRA5 activity raises APCDD1L's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 3.42× lower at baseline in the lines without MXRA5 | 0.036 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[ANXA8]] | C | MXRA5 activity raises ANXA8's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without MXRA5 | 0.042 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[LINC00842]] | C | MXRA5 activity raises LINC00842's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without MXRA5 | 0.050 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[DENND2A]] | C | MXRA5 activity raises DENND2A's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without MXRA5 | 0.057 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[DKK3]] | C | MXRA5 activity raises DKK3's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 4.18× lower at baseline in the lines without MXRA5 | 0.060 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[FLI1]] | C | MXRA5 activity raises FLI1's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 5.14× lower at baseline in the lines without MXRA5 | 0.060 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |
| [[APOBEC3G]] | C | MXRA5 activity raises APOBEC3G's level | lines that do not express MXRA5 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without MXRA5 | 0.067 | ⚠ within organs, on part of the lines; also absent: IRAG2, VCAM1, LINC02476; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.8, 20.4); signed map (26.5, 44.8). **Vector** length 67.7, 27.7% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +4.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.2 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -4.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | matrix remodeling associated 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 — chrX:3,308,565-3,346,652 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564I1922 |
| Gene groups (HGNC) | I-set domain containing |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR99](https://www.uniprot.org/uniprotkb/Q9NR99) (Matrix-remodeling-associated protein 5):

> In kidney, has anti-inflammatory and anti-fibrotic properties by limiting the induction of chemokines, fibronectin and collagen expression in response to TGB1 and pro-inflammatory stimuli.

**Summary**, from NCBI Gene [25878](https://www.ncbi.nlm.nih.gov/gene/25878):

> This gene encodes one of the matrix-remodelling associated proteins. This protein contains 7 leucine-rich repeats and 12 immunoglobulin-like C2-type domains related to perlecan. This gene has a pseudogene on chromosome Y. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:7539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7539) · Entrez [25878](https://www.ncbi.nlm.nih.gov/gene/25878) · UniProt [Q9NR99](https://www.uniprot.org/uniprotkb/Q9NR99) · Ensembl [ENSG00000101825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101825)

## Data

Gene col 2174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2174); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2174]; `tensor/DDL_lfc|DDL_z.npy` [2174]; `embed/gene_vectors.npy` [2174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2174 or target_col == 2174). Every well: [[MXRA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXRA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
