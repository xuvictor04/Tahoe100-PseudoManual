---
symbol: "PTAFR"
type: "gene"
col: 9803
ensembl_id: "ENSG00000169403"
name: "platelet activating factor receptor"
location: "1p35.3"
module: 34
arm: "+"
pooled_cpm: 10.17
n_lines_expressing: 21
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 32
direction_downstream: 40
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PTAFR

*platelet activating factor receptor* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.98× (z +23.2, q 0e+00, up in 6 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.697× (z -4.0, q 0.033, down in 8 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLT1A]] (+0.64, fdr 1e-05), [[GDPD5]] (+0.62, fdr 1e-05), [[LYPD3]] (+0.59, fdr 1e-05); moves opposite to [[TBC1D5]] (-0.51, fdr 3e-05), [[ZMYND11]] (-0.51, fdr 6e-05), [[LARP1]] (-0.49, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[PDGFB]] → it (grade B ⚠); 40 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +23.2 | 0e+00 | 6/16 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.47×** | +20.9 | 0e+00 | 7/17 (Panc 03.27, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.95×** | +16.3 | 0e+00 | 4/17 (HT-29, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +11.1 | 1e-26 | 12/19 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +10.5 | 7e-24 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +10.5 | 7e-24 | 15/19 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +8.0 | 7e-14 | 10/18 (Panc 03.27, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +7.4 | 7e-12 | 2/16 (Panc 03.27, NCI-H23) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.81×** | +7.0 | 1e-10 | 12/18 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.79×** | +6.9 | 3e-10 | 0/13 | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +6.9 | 3e-10 | 5/14 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +6.6 | 2e-09 | 13/19 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +5.1 | 2e-05 | 4/16 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +5.0 | 3e-05 | 1/17 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.56×** | +4.8 | 5e-05 | 1/12 (SW1417) | all doses, stronger at high dose | composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +4.3 | 5e-04 | 4/19 (A549, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.1 | 0.001 | 5/18 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.003 | 0/18 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.012 | 8/18 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.76×** | +3.5 | 0.013 | 11/17 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.697×** | -4.0 | 0.033 | 8/19 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.733×** | -3.7 | 0.036 | 6/19 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.734×** | -3.7 | 0.036 | 10/19 (A549, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.805×** | -3.7 | 0.037 | 9/18 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.068 | 1/19 (AN3 CA) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.765×** | -3.3 | 0.099 | 7/19 (NCI-H1573, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.770× | -3.2 | 0.13 | 10/18 (A549, BT-474, …) | inconsistent across doses |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.839× | -3.0 | 0.18 | 1/19 (SW480) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 24.8 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 103 | 2 | 7 (5 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.49× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0220× (z -32.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -22.2) |
| [[COLO 205 (line)]] | alt | 65.2 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0612× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -12.1) |
| [[SW480 (line)]] | alt | 11.5 | 1 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.99× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -13.4) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HepG2_C3A (line)]] | wt | 67.4 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.61× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -8.9) |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0242× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 43.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[Panc 03.27 (line)]] | alt | 25.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 6.64 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.15× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 5.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLT1A]] | +0.64 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PTK6]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TNFRSF11A]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[KRT15]] | +0.58 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FA2H]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SULT2B1]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[CD68]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CIB1]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SCAT1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D5]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.51 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[LARP1]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[FBXL17]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[LMO3]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NNT]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[GTF2I]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[ANP32B]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[APEX1]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ADI1]] | -0.46 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 7, C 25. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises PTAFR's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without PDGFB | 0.013 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[LEMD1]] | B | LEMD1 activity raises PTAFR's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without LEMD1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[MMP13]] | B | MMP13 activity raises PTAFR's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.77× lower at baseline in the lines without MMP13 | 0.059 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[CREG2]] | B | CREG2 activity raises PTAFR's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without CREG2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[LMTK3]] | B | LMTK3 activity raises PTAFR's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without LMTK3 | 0.088 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[KRT15]] | B | KRT15 activity raises PTAFR's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.41× lower at baseline in the lines without KRT15 | 0.089 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[BIK]] | B | BIK activity raises PTAFR's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without BIK | 0.098 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[CEACAM1]] | C | CEACAM1 activity raises PTAFR's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 3.60× lower at baseline in the lines without CEACAM1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[IRF6]] | C | IRF6 activity raises PTAFR's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 3.53× lower at baseline in the lines without IRF6 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[SPNS2]] | C | SPNS2 activity raises PTAFR's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.93× lower at baseline in the lines without SPNS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises PTAFR's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 3.76× lower at baseline in the lines without BSPRY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[TTC9]] | C | TTC9 activity raises PTAFR's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 3.23× lower at baseline in the lines without TTC9 | 0.004 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 14, C 26. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | PTAFR activity raises LMTK3's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without PTAFR | 8e-04 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[BIK]] | B | PTAFR activity raises BIK's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without PTAFR | 0.002 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[PTK6]] | B | PTAFR activity raises PTK6's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.09× lower at baseline in the lines without PTAFR | 0.003 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[TMC6]] | B | PTAFR activity raises TMC6's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.61× lower at baseline in the lines without PTAFR | 0.003 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[PTK2B]] | B | PTAFR activity raises PTK2B's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.69× lower at baseline in the lines without PTAFR | 0.005 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[SAT1]] | B | PTAFR activity raises SAT1's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without PTAFR | 0.008 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[ATG9B]] | B | PTAFR activity raises ATG9B's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.04× lower at baseline in the lines without PTAFR | 0.031 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[KPNA7]] | B | PTAFR activity raises KPNA7's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.40× lower at baseline in the lines without PTAFR | 0.032 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[HAP1]] | B | PTAFR activity raises HAP1's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.47× lower at baseline in the lines without PTAFR | 0.033 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[CSTB]] | B | PTAFR activity raises CSTB's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.55× lower at baseline in the lines without PTAFR | 0.038 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[TLDC2]] | B | PTAFR activity raises TLDC2's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.94× lower at baseline in the lines without PTAFR | 0.048 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[DNAH17]] | B | PTAFR activity raises DNAH17's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 1.77× lower at baseline in the lines without PTAFR | 0.064 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, -1.1); signed map (-2.5, 45.3). **Vector** length 74.5, 22.6% of its response variance represented; |z| ≥ 3 in 640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +5.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~75% of this change | -3.0 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | platelet activating factor receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,147,166-28,193,936 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Platelet activating factor receptor |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 12 pathways, smallest: Interleukin-10 signaling; Interferon gamma signaling; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25105](https://www.uniprot.org/uniprotkb/P25105) (Platelet-activating factor receptor):

> Receptor for platelet activating factor, a chemotactic phospholipid mediator that possesses potent inflammatory, smooth-muscle contractile and hypotensive activity. Seems to mediate its action via a G protein that activates a phosphatidylinositol-calcium second messenger system.

**Summary**, from NCBI Gene [5724](https://www.ncbi.nlm.nih.gov/gene/5724):

> This gene encodes a seven-transmembrane G-protein-coupled receptor for platelet-activating factor (PAF) that localizes to lipid rafts and/or caveolae in the cell membrane. PAF (1-0-alkyl-2-acetyl-sn-glycero-3-phosphorylcholine) is a phospholipid that plays a significant role in oncogenic transformation, tumor growth, angiogenesis, metastasis, and pro-inflammatory processes. Binding of PAF to the PAF-receptor (PAFR) stimulates numerous signal transduction pathways including phospholipase C, D, …

**Accessions** — [HGNC:9582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9582) · Entrez [5724](https://www.ncbi.nlm.nih.gov/gene/5724) · UniProt [P25105](https://www.uniprot.org/uniprotkb/P25105) · Ensembl [ENSG00000169403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169403)

## Data

Gene col 9803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9803); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9803]; `tensor/DDL_lfc|DDL_z.npy` [9803]; `embed/gene_vectors.npy` [9803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9803 or target_col == 9803). Every well: [[PTAFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTAFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
