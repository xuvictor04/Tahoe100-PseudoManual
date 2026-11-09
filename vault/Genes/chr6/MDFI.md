---
symbol: "MDFI"
type: "gene"
col: 3378
ensembl_id: "ENSG00000112559"
name: "MyoD family inhibitor"
location: "6p21.1"
module: 34
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 25
n_dd_up: 28
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 11
direction_downstream: 24
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MDFI

*MyoD family inhibitor* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.31× (z +10.7, q 4e-24, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.77× (z +7.5, q 1e-11, up in 14 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.544× (z -5.7, q 6e-06, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJB3]] (+0.63, fdr 7e-06), [[SFN]] (+0.61, fdr 7e-06), [[SCEL]] (+0.59, fdr 7e-06); moves opposite to [[TRIQK]] (-0.55, fdr 3e-05), [[RNF5]] (-0.53, fdr 3e-05), [[GALM]] (-0.52, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 24 go from it, the strongest it → [[EPHA2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +10.7 | 4e-24 | 2/5 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +8.1 | 1e-13 | 1/13 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.77×** | +7.5 | 1e-11 | 14/22 (LS 180, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +7.4 | 2e-11 | 9/15 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +6.2 | 8e-08 | 1/10 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.89×** | +5.9 | 3e-07 | 12/17 (COLO 205, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.8 | 1e-04 | 6/17 (NCI-H2347, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +4.8 | 1e-04 | 12/19 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.77×** | +4.6 | 3e-04 | 2/13 (NCI-H1573, NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.64×** | +4.4 | 4e-04 | 13/21 (COLO 205, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.4 | 4e-04 | 3/15 (AsPC-1, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.61×** | +4.4 | 4e-04 | 12/23 (COLO 205, LS 180, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.89×** | +4.2 | 0.001 | 8/17 (COLO 205, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.002 | 10/22 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +4.1 | 0.002 | 2/15 (Panc 03.27, SW48) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +4.0 | 0.003 | 2/17 (KATO III, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.004 | 7/23 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.005 | 8/23 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.019 | 1/23 (HT-29) | rises with dose | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **2.02×** | +3.2 | 0.033 | 6/17 (LS 180, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.036 | 7/21 (KATO III, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.042 | 4/17 (COLO 205, RKO, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -5.7 | 6e-06 | 14/22 (LoVo, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.655×** | -4.0 | 0.019 | 14/23 (LoVo, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.670×** | -3.8 | 0.029 | 13/22 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.762×** | -3.6 | 0.039 | 6/22 (KATO III, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.666×** | -3.5 | 0.044 | 7/23 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.072 | 8/23 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.091 | 6/22 (HT-29, HCT15, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.722× | -3.1 | 0.14 | 5/23 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.718× | -3.0 | 0.16 | 9/19 (NCI-H1573, AsPC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 10.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0581× (z -11.6) |
| [[LoVo (line)]] | wt | 22.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0728× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.128× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -9.8) |
| [[RKO (line)]] | wt | 9.30 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0183× (z -16.9) |
| [[SW48 (line)]] | wt | 12.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -11.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJB3]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SFN]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SCEL]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ALS2CL]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LAMC2]] | +0.57 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[NUP50-DT]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ZNF562]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KRT6A]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[LINC01322]] | +0.52 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[MST1R]] | +0.52 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ADCY7]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[IL1R2]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIQK]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RNF5]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GALM]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ATF2]] | -0.51 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[RSPH1]] | -0.50 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PCM1]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[IFT81]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CXXC5]] | -0.46 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CFAP69]] | -0.45 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SELENOP]] | -0.45 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[IQUB]] | -0.44 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[WDPCP]] | -0.44 | -0.39 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MDFI's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM83H]] | B | FAM83H activity raises MDFI's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without FAM83H | 0.087 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN |
| [[DSG3]] | C | DSG3 activity raises MDFI's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 3.93× lower at baseline in the lines without DSG3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1; co-absent with the target |
| [[KIAA0040]] | C | KIAA0040 activity raises MDFI's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without KIAA0040 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises MDFI's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without GJB3 | 0.052 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises MDFI's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.96× lower at baseline in the lines without KRT6A | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[SH2D3A]] | C | SH2D3A activity raises MDFI's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without SH2D3A | 0.060 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[LAMA3]] | C | LAMA3 activity raises MDFI's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.30× lower at baseline in the lines without LAMA3 | 0.064 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises MDFI's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.93× lower at baseline in the lines without CEACAM1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[CRYBG2]] | C | CRYBG2 activity raises MDFI's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without CRYBG2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; co-absent with the target |
| [[ZBED2]] | C | ZBED2 activity raises MDFI's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 2.73× lower at baseline in the lines without ZBED2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 12, C 12. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2-AS1]] | B | MDFI activity raises EPHA2-AS1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without MDFI | 0.003 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[FAM83H]] | B | MDFI activity raises FAM83H's level | lines that do not express MDFI (25) vs lines expressing it (25) | 3.44× lower at baseline in the lines without MDFI | 0.005 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[RAPGEF3]] | B | MDFI activity raises RAPGEF3's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without MDFI | 0.008 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[RSPH1]] | B | MDFI activity raises RSPH1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without MDFI | 0.011 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[PRKG2-AS1]] | B | MDFI activity raises PRKG2-AS1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without MDFI | 0.014 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[SDC1]] | B | MDFI activity raises SDC1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without MDFI | 0.016 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[NUP50]] | B | MDFI activity raises NUP50's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without MDFI | 0.026 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[BLACAT1]] | B | MDFI activity raises BLACAT1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without MDFI | 0.048 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[ALS2CL]] | B | MDFI activity raises ALS2CL's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without MDFI | 0.062 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[PLEKHN1]] | B | MDFI activity raises PLEKHN1's level | lines that do not express MDFI (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without MDFI | 0.075 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| [[EPHA2]] | B | MDFI activity raises EPHA2's level | lines that do not express MDFI (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without MDFI | 0.084 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | B | MDFI activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express MDFI (25) vs lines expressing it (23) | the lines without MDFI: 0.74× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.6, 51.2); signed map (3.0, 36.7). **Vector** length 61.7, 17.4% of its response variance represented; |z| ≥ 3 in 539 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +7.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.1 | +4.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +5.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MyoD family inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,636,882-41,654,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | I-mfa |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99750](https://www.uniprot.org/uniprotkb/Q99750) (MyoD family inhibitor):

> Inhibits the transactivation activity of the Myod family of myogenic factors and represses myogenesis (By similarity). Acts by associating with Myod family members and retaining them in the cytoplasm by masking their nuclear localization signals (By similarity). Can also interfere with the DNA-binding activity of Myod family members (By similarity). Plays an important role in trophoblast and chondrogenic differentiation (By similarity). Regulates the transcriptional activity of TCF7L1/TCF3 by …

**Summary**, from NCBI Gene [4188](https://www.ncbi.nlm.nih.gov/gene/4188):

> This protein is a transcription factor that negatively regulates other myogenic family proteins. Studies of the mouse homolog, I-mf, show that it interferes with myogenic factor function by masking nuclear localization signals and preventing DNA binding. Knockout mouse studies show defects in the formation of vertebrae and ribs that also involve cartilage formation in these structures. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6967) · Entrez [4188](https://www.ncbi.nlm.nih.gov/gene/4188) · UniProt [Q99750](https://www.uniprot.org/uniprotkb/Q99750) · Ensembl [ENSG00000112559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112559)

## Data

Gene col 3378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3378); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3378]; `tensor/DDL_lfc|DDL_z.npy` [3378]; `embed/gene_vectors.npy` [3378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3378 or target_col == 3378). Every well: [[MDFI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDFI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
