---
symbol: "CCDC71L"
type: "gene"
col: 14794
ensembl_id: "ENSG00000253276"
name: "coiled-coil domain containing 71 like"
location: "7q22.3"
module: 219
arm: "+"
pooled_cpm: 9.06
n_lines_expressing: 42
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# CCDC71L

*coiled-coil domain containing 71 like* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.18× (z +11.8, q 3e-29, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.701× (z -5.4, q 5e-05, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL4R]] (+0.67, fdr 7e-06), [[ZNF281]] (+0.62, fdr 1e-05), [[OSMR]] (+0.61, fdr 2e-05); moves opposite to [[NDRG3]] (-0.57, fdr 1e-05), [[RBL2]] (-0.56, fdr 2e-05), [[DYNC2LI1]] (-0.55, fdr 4e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CLCF1]] → it (grade B ⚠); 10 go from it, the strongest it → [[SLFN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +11.8 | 3e-29 | 29/38 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +10.3 | 2e-22 | 21/34 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +7.6 | 5e-12 | 26/37 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +7.3 | 3e-11 | 24/37 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +7.1 | 1e-10 | 18/37 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +5.8 | 6e-07 | 15/34 (AsPC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.6 | 3e-04 | 13/31 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 16/40 (Hs 766T, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.5 | 5e-04 | 12/37 (C32, HS-578T, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +4.2 | 0.001 | 10/33 (NCI-H23, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.026 | 13/33 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.028 | 8/36 (A498, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +3.4 | 0.034 | 6/19 (MIA PaCa-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.37×** | +3.3 | 0.035 | 3/38 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.043 | 11/34 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.76×** | +3.1 | 0.058 | 6/34 (AsPC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.75×** | +3.1 | 0.058 | 5/33 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.065 | 3/35 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.701×** | -5.4 | 5e-05 | 20/38 (AsPC-1, J82, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.745×** | -4.4 | 0.002 | 19/38 (J82, A498, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.752×** | -4.3 | 0.002 | 16/38 (J82, CHP-212, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.669×** | -4.3 | 0.002 | 18/39 (NCI-H1792, A498, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.648×** | -4.3 | 0.002 | 15/37 (J82, NCI-H1792, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.482×** | -4.1 | 0.005 | 17/34 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -3.9 | 0.009 | 11/39 (NCI-H1792, SW48, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -3.7 | 0.013 | 17/38 (RPMI-7951, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.698×** | -3.6 | 0.019 | 15/36 (SW48, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.716×** | -3.6 | 0.021 | 14/39 (NCI-H1792, SW48, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.5 | 0.024 | 12/31 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.088 | 5/38 (C-33 A, AN3 CA, …) | rises with dose | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 45.6 | 0 | 13 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0161× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0916× (z -11.7) |
| [[C32 (line)]] | wt | 13.0 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 9.09× (z +9.7) | — |
| [[A498 (line)]] | wt | 21.0 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.82× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 10.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.83× (z +8.9) | [[Fluvoxamine (drug)]] 5 µM 0.0512× (z -10.2) |
| [[J82 (line)]] | alt | 54.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.400× (z -17.8) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -12.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.56 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0575× (z -11.2) |
| [[HS-578T (line)]] | alt | 9.91 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 10.5× (z +8.7) | — |
| [[LoVo (line)]] | wt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 3.33 | 0 | 1 | — | [[crizotinib (drug)]] 5 µM 0.0495× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0806× (z -9.8) |
| [[SW480 (line)]] | alt | 3.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.70× (z +9.6) | — |
| [[A-427 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL4R]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ZNF281]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[OSMR]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TLNRD1]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ARL14EPL]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[UTP3]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EPOP]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ZNF274]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[S100A11]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[MAD2L1BP]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DEGS1]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[HELZ2]] | +0.54 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RBL2]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[DYNC2LI1]] | -0.55 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SEC23A]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ANAPC5]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[OPA1]] | -0.52 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[UBE4B]] | -0.52 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[SCP2]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MED23]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[AGO1]] | -0.51 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[NUDT21]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RPA1]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | CLCF1 activity raises CCDC71L's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without CLCF1 | 0.050 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[SGK1]] | B | SGK1 activity raises CCDC71L's level | lines that do not express SGK1 (12) vs lines expressing it (38) | 2.16× lower at baseline in the lines without SGK1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with WNK2, PRDM2; also absent: RNF182, FRG1DP, DPYSL3; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLFN5]] | B | CCDC71L activity raises SLFN5's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 5.68× lower at baseline in the lines without CCDC71L | 0.001 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[OSMR]] | B | CCDC71L activity raises OSMR's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 3.41× lower at baseline in the lines without CCDC71L | 0.008 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[CLCF1]] | B | CCDC71L activity raises CLCF1's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 2.17× lower at baseline in the lines without CCDC71L | 0.009 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[S100A11]] | B | CCDC71L activity raises S100A11's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without CCDC71L | 0.013 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[EID2]] | B | CCDC71L activity lowers EID2's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.80× higher at baseline in the lines without CCDC71L | 0.035 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[NABP1]] | B | CCDC71L activity raises NABP1's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 2.01× lower at baseline in the lines without CCDC71L | 0.041 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[ABL2]] | B | CCDC71L activity raises ABL2's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 2.32× lower at baseline in the lines without CCDC71L | 0.044 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[PPIF]] | B | CCDC71L activity raises PPIF's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without CCDC71L | 0.053 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[PRKCE]] | B | CCDC71L activity raises PRKCE's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CCDC71L | 0.075 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[USP48]] | B | CCDC71L activity lowers USP48's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.18× higher at baseline in the lines without CCDC71L | 0.099 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, 8.2); signed map (10.7, 24.5). **Vector** length 85.0, 17.9% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.3 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 71 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:106,654,360-106,661,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36031; previously C7orf74 |
| Matched by | ensembl_id |

UniProt [Q8N9Z2](https://www.uniprot.org/uniprotkb/Q8N9Z2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26685) · Entrez [168455](https://www.ncbi.nlm.nih.gov/gene/168455) · UniProt [Q8N9Z2](https://www.uniprot.org/uniprotkb/Q8N9Z2) · Ensembl [ENSG00000253276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253276)

## Data

Gene col 14794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14794); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14794]; `tensor/DDL_lfc|DDL_z.npy` [14794]; `embed/gene_vectors.npy` [14794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14794 or target_col == 14794). Every well: [[CCDC71L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC71L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
