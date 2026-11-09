---
symbol: "CNGA1"
type: "gene"
col: 12605
ensembl_id: "ENSG00000198515"
name: "cyclic nucleotide gated channel subunit alpha 1"
location: "4p12"
module: 8
arm: "+"
pooled_cpm: 3.34
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 12
n_dd_up_clean: 24
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CNGA1

*cyclic nucleotide gated channel subunit alpha 1* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.50× (z +20.2, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.486× (z -8.2, q 1e-13, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALOX5]] (+0.59, fdr 1e-05), [[SUSD4]] (+0.57, fdr 4e-05), [[C12orf75]] (+0.53, fdr 1e-04); moves opposite to [[HECTD1]] (-0.56, fdr 7e-05), [[EFCAB2]] (-0.45, fdr 0.001, ⚠ one half only (not replicated)), [[STXBP5]] (-0.44, fdr 2e-04), [[ZFHX3]] (-0.43, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[NR3C2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AFG1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.50×** | +20.2 | 0e+00 | 38/40 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.76×** | +17.8 | 0e+00 | 38/41 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.22×** | +16.4 | 0e+00 | 34/38 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.43×** | +13.9 | 6e-42 | 36/41 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +13.6 | 3e-40 | 18/29 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.24×** | +13.4 | 4e-39 | 33/38 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.04×** | +12.7 | 5e-35 | 30/34 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +12.0 | 2e-31 | 1/7 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.84×** | +9.9 | 4e-21 | 19/40 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +8.1 | 2e-14 | 6/14 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.7 | 9e-13 | 3/8 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.38×** | +7.3 | 2e-11 | 17/33 (CFPAC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +6.8 | 6e-10 | 7/16 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 9e-06 | 10/31 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.52×** | +4.8 | 6e-05 | 7/39 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.8 | 7e-05 | 9/40 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.50×** | +4.6 | 1e-04 | 10/35 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.010 | 2/26 (HOP62, NCI-H2347) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.011 | 5/34 (AsPC-1, HT-29, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.486×** | -8.2 | 1e-13 | 19/41 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.505×** | -7.5 | 2e-11 | 19/37 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -6.2 | 1e-07 | 11/40 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -5.1 | 6e-05 | 10/27 (Hs 766T, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -4.2 | 0.003 | 15/39 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -3.9 | 0.007 | 15/23 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.701×** | -3.9 | 0.008 | 11/30 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -3.8 | 0.010 | 11/35 (LS 180, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.031 | 5/39 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.041 | 13/37 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.755×** | -3.2 | 0.068 | 5/39 (A549, C-33 A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.071 | 10/41 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 3 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0459× (z -10.9) |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0613× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.35 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.20× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 5.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 2.96 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.845 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.852 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALOX5]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[C12orf75]] | +0.53 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[NR3C2]] | +0.51 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[GPR160]] | +0.50 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[ENTREP1]] | +0.49 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[TNFRSF11A]] | +0.49 | +0.29 / +0.51 | both halves | 2e-04 |  |
| [[SGSM1]] | +0.49 | +0.22 / +0.61 | both halves | 6e-04 |  |
| [[SLAIN1]] | +0.49 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[C4orf19]] | +0.48 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[LYPD5]] | +0.48 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[SGCZ]] | +0.48 | +0.38 / +0.62 | both halves | 7e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECTD1]] | -0.56 | -0.37 / -0.61 | both halves | 7e-05 |  |
| [[EFCAB2]] | -0.45 | -0.16 / -0.69 | ⚠ one half (not replicated) | 0.001 |  |
| [[STXBP5]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZFHX3]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[HIPK2]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TRMT6]] | -0.42 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[AFG1L]] | -0.42 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[PRORP]] | -0.41 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[UBTF]] | -0.41 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[ZMYND11]] | -0.41 | -0.14 / -0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[KIAA0825]] | -0.41 | -0.12 / -0.41 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C2]] | B | NR3C2 activity raises CNGA1's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without NR3C2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[KLHL32]] | B | KLHL32 activity raises CNGA1's level | lines that do not express KLHL32 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without KLHL32 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP8A1, ENSG00000270265, CHN2; maybe low, not absent |
| [[NRIP3]] | B | NRIP3 activity lowers CNGA1's level | lines that do not express NRIP3 (15) vs lines expressing it (35) | 1.81× higher at baseline in the lines without NRIP3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SDK2, DTX3, MCTP1 |
| [[CDS1]] | B | CDS1 activity raises CNGA1's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without CDS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[MGAT4A]] | B | MGAT4A activity raises CNGA1's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without MGAT4A | 0.042 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[ENPP5]] | B | ENPP5 activity raises CNGA1's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.64× lower at baseline in the lines without ENPP5 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises CNGA1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without TNFRSF11A | 0.058 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[TSPAN1]] | B | TSPAN1 activity raises CNGA1's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without TSPAN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[PTPN22]] | B | PTPN22 activity raises CNGA1's level | lines that do not express PTPN22 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without PTPN22 | 0.062 | ⚠ within organs, on part of the lines; also absent: PTPRE; maybe low, not absent |
| [[TJP3]] | B | TJP3 activity raises CNGA1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without TJP3 | 0.092 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[B3GALT5]] | B | B3GALT5 activity raises CNGA1's level | lines that do not express B3GALT5 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without B3GALT5 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000225330, IGFL2-AS1, PADI1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFG1L]] | B | CNGA1 activity lowers AFG1L's level | lines that do not express CNGA1 (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without CNGA1 | 0.072 | ⚠ within organs, on part of the lines; co-absent genes; also absent: FHIP1A, NIPAL1, RALGPS2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.357). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.5, 35.9); signed map (31.2, 28.6). **Vector** length 58.5, 9.22% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +20.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | -1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | +0.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclic nucleotide gated channel subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:47,935,977-48,016,681 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RCNC1, RCNCa, CNG1, RP49; previously CNCG1, CNCG |
| Gene groups (HGNC) | Cyclic nucleotide gated channels |
| Reactome | 5 pathways, smallest: Activation of the phototransduction cascade; Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P29973](https://www.uniprot.org/uniprotkb/P29973) (Cyclic nucleotide-gated channel alpha-1):

> Pore-forming subunit of the rod cyclic nucleotide-gated channel. Mediates rod photoresponses at dim light converting transient changes in intracellular cGMP levels into electrical signals. In the dark, cGMP levels are high and keep the channel open enabling a steady inward current carried by Na(+) and Ca(2+) ions that leads to membrane depolarization and neurotransmitter release from synaptic terminals. Upon photon absorption cGMP levels decline leading to channel closure and membrane …

**Summary**, from NCBI Gene [1259](https://www.ncbi.nlm.nih.gov/gene/1259):

> The protein encoded by this gene is involved in phototransduction. Along with another protein, the encoded protein forms a cGMP-gated cation channel in the plasma membrane, allowing depolarization of rod photoreceptors. This represents the last step in the phototransduction pathway. Defects in this gene are a cause of retinitis pigmentosa autosomal recessive (ARRP) disease. Multiple transcript variants have been found for this gene. [provided by RefSeq, Oct 2019]

**Accessions** — [HGNC:2148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2148) · Entrez [1259](https://www.ncbi.nlm.nih.gov/gene/1259) · UniProt [P29973](https://www.uniprot.org/uniprotkb/P29973) · Ensembl [ENSG00000198515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198515)

## Data

Gene col 12605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12605); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12605]; `tensor/DDL_lfc|DDL_z.npy` [12605]; `embed/gene_vectors.npy` [12605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12605 or target_col == 12605). Every well: [[CNGA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNGA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
