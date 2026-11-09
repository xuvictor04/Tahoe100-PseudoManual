---
symbol: "CREG2"
type: "gene"
col: 10658
ensembl_id: "ENSG00000175874"
name: "cellular repressor of E1A stimulated genes 2"
location: "2q11.2"
module: 81
arm: "+"
pooled_cpm: 10.15
n_lines_expressing: 31
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 13
direction_downstream: 24
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# CREG2

*cellular repressor of E1A stimulated genes 2* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +8.7, q 2e-15, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.369× (z -17.9, q 0e+00, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC46A3]] (+0.55, fdr 3e-05), [[PTGS1]] (+0.55, fdr 3e-05), [[SERPIND1]] (+0.54, fdr 5e-05); moves opposite to [[SENP6]] (-0.47, fdr 6e-05), [[ZFX]] (-0.47, fdr 6e-05), [[ZMYND11]] (-0.47, fdr 7e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC02725]] → it (grade B ⚠); 24 go from it, the strongest it → [[ZNF684]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +8.7 | 2e-15 | 13/29 (SW480, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 0.002 | 9/27 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.098 | 5/28 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.098 | 12/28 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.42× | +3.2 | 0.17 | 3/26 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.20 | 5/29 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.27× | +3.0 | 0.20 | 4/28 (A498, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.369×** | -17.9 | 0e+00 | 25/27 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -12.3 | 2e-32 | 20/25 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.386×** | -11.6 | 6e-29 | 22/27 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.424×** | -10.9 | 2e-25 | 22/28 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.265×** | -8.8 | 1e-16 | 23/27 (NCI-H1573, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.540×** | -7.8 | 6e-13 | 23/28 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -7.3 | 2e-11 | 18/28 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.332×** | -7.3 | 2e-11 | 18/25 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -6.5 | 5e-09 | 22/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.664×** | -4.9 | 6e-05 | 17/28 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.716×** | -4.2 | 0.001 | 9/28 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.721×** | -4.1 | 0.002 | 10/26 (hTERT-HPNE, NCI-H1573, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.685×** | -4.1 | 0.002 | 12/29 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.725×** | -4.1 | 0.002 | 9/29 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -3.6 | 0.013 | 16/29 (A-172, HCT15, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.601×** | -3.4 | 0.027 | 8/28 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 41.3 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -28.1) |
| [[LoVo (line)]] | wt | 15.9 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0762× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 9.35 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.8) |
| [[A498 (line)]] | wt | 9.91 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.9) |
| [[A549 (line)]] | wt | 12.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0449× (z -22.3) |
| [[AsPC-1 (line)]] | alt | 78.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -30.2) |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -24.8) |
| [[COLO 205 (line)]] | alt | 61.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0523× (z -27.1) |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0901× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.176× (z -8.9) |
| [[SW 900 (line)]] | alt | 8.65 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0423× (z -13.4) |
| [[A-172 (line)]] | wt | 4.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0485× (z -11.1) |
| [[HOP62 (line)]] | alt | 7.58 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0744× (z -8.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.7) |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 5.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 8.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0457× (z -14.1) |
| [[SW480 (line)]] | alt | 4.89 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.55× (z +8.6) | — |
| [[A-427 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC46A3]] | +0.55 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[PTGS1]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SERPIND1]] | +0.54 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[RAC2]] | +0.54 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[OTUB2]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[NRIP3]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ETHE1]] | +0.52 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[ATP2C2]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[GTF2IP7]] | +0.52 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[ZNF511]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[RGS9]] | +0.50 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[CIB1]] | +0.50 | +0.47 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP6]] | -0.47 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ZFX]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[ZMYND11]] | -0.47 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[PIEZO1]] | -0.46 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[MRRF]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[COMT]] | -0.46 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[ZNF747]] | -0.46 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[MYOF]] | -0.45 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PRRC2B]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[CACNA2D1]] | -0.45 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[MLLT6]] | -0.45 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ATXN7]] | -0.45 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 10, C 3. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02725]] | B | LINC02725 activity raises CREG2's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 2.43× lower at baseline in the lines without LINC02725 | 0.008 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[FA2H]] | B | FA2H activity raises CREG2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.85× lower at baseline in the lines without FA2H | 0.009 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[TMCC3]] | B | TMCC3 activity raises CREG2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without TMCC3 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[THBD]] | B | THBD activity raises CREG2's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without THBD | 0.024 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[LYPD3]] | B | LYPD3 activity raises CREG2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without LYPD3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CREG2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DCLK2]] | B | DCLK2 activity lowers CREG2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 1.91× higher at baseline in the lines without DCLK2 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[SERPIND1]] | B | SERPIND1 activity raises CREG2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.24× lower at baseline in the lines without SERPIND1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises CREG2's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without PLEK2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[GTF2IP7]] | B | GTF2IP7 activity raises CREG2's level | lines that do not express GTF2IP7 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without GTF2IP7 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000290729, FRMD4B, TMEM92 |
| [[TMEM154]] | C | TMEM154 activity raises CREG2's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.63× lower at baseline in the lines without TMEM154 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13; co-absent with the target |
| [[TMEM92]] | C | TMEM92 activity raises CREG2's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.98× lower at baseline in the lines without TMEM92 | 0.008 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 20, C 4. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF684]] | B | CREG2 activity lowers ZNF684's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.48× higher at baseline in the lines without CREG2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[UBA6]] | B | CREG2 activity raises UBA6's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without CREG2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[SAMD11]] | B | CREG2 activity lowers SAMD11's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.93× higher at baseline in the lines without CREG2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[FA2H]] | B | CREG2 activity raises FA2H's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without CREG2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[TMEM178A]] | B | CREG2 activity raises TMEM178A's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.47× lower at baseline in the lines without CREG2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[THBD]] | B | CREG2 activity raises THBD's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without CREG2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[MYOF]] | B | CREG2 activity raises MYOF's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without CREG2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[RAC2]] | B | CREG2 activity raises RAC2's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.74× lower at baseline in the lines without CREG2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[GNAI3]] | B | CREG2 activity strengthens GNAI3's drug response | lines that do not express CREG2 (19) vs lines expressing it (30) | the lines without CREG2 respond 0.65× as strongly (z diff +1.54); strongest at Idarubicin (hydrochloride) 5 µM: 0.87x vs 0.66x (z diff +3.7) | 0.039 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A; target measured in part of the lines; artifact flags |
| [[ACBD3]] | B | CREG2 activity raises ACBD3's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without CREG2 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[PRRC2B]] | B | CREG2 activity lowers PRRC2B's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.36× higher at baseline in the lines without CREG2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[GTF2IP7]] | B | CREG2 activity raises GTF2IP7's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without CREG2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 0.4); signed map (0.6, 47.9). **Vector** length 70.6, 16.0% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +3.0 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -12.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -1.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cellular repressor of E1A stimulated genes 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:101,345,550-101,387,503 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q8IUH2](https://www.uniprot.org/uniprotkb/Q8IUH2) carries no function annotation.

**Summary**, from NCBI Gene [200407](https://www.ncbi.nlm.nih.gov/gene/200407):

> Predicted to be located in Golgi apparatus; endoplasmic reticulum; and extracellular region. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14272) · Entrez [200407](https://www.ncbi.nlm.nih.gov/gene/200407) · UniProt [Q8IUH2](https://www.uniprot.org/uniprotkb/Q8IUH2) · Ensembl [ENSG00000175874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175874)

## Data

Gene col 10658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10658); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10658]; `tensor/DDL_lfc|DDL_z.npy` [10658]; `embed/gene_vectors.npy` [10658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10658 or target_col == 10658). Every well: [[CREG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
