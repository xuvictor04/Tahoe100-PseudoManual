---
symbol: "ATL1"
type: "gene"
col: 12604
ensembl_id: "ENSG00000198513"
name: "atlastin GTPase 1"
location: "14q22.1"
module: 90
arm: "+"
pooled_cpm: 14.76
n_lines_expressing: 43
n_dd_up: 34
n_dd_down: 9
n_dd_up_clean: 24
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# ATL1

*atlastin GTPase 1* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +15.6, q 0e+00, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.588× (z -7.9, q 1e-12, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN12]] (+0.57, fdr 3e-05), [[C11orf52]] (+0.54, fdr 6e-05), [[LCA5]] (+0.54, fdr 1e-05); moves opposite to [[EEFSEC]] (-0.51, fdr 5e-05), [[RNF123]] (-0.49, fdr 5e-05), [[CCDC57]] (-0.49, fdr 2e-04).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC7A8]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC7A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +15.6 | 0e+00 | 23/38 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.2 | 2e-17 | 22/41 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +8.3 | 1e-14 | 12/23 (A549, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +6.9 | 9e-10 | 18/39 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.3 | 4e-08 | 17/41 (J82, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.0 | 2e-07 | 6/16 (J82, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +5.8 | 5e-07 | 18/41 (J82, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +5.3 | 7e-06 | 20/41 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 11/40 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 2e-05 | 15/41 (hTERT-HPNE, HOP62, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +5.0 | 4e-05 | 13/41 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 4e-05 | 17/40 (SW480, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.9 | 4e-05 | 13/39 (SW480, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 1e-04 | 11/41 (SW480, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 5e-04 | 13/41 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +4.3 | 5e-04 | 13/41 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.002 | 9/41 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.002 | 12/35 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.588×** | -7.9 | 1e-12 | 22/41 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -6.1 | 3e-07 | 20/41 (COLO 205, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.684×** | -5.7 | 3e-06 | 15/40 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -5.0 | 7e-05 | 7/41 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -4.7 | 3e-04 | 16/41 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.747×** | -4.4 | 0.001 | 18/41 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.773×** | -3.9 | 0.009 | 18/38 (A-172, COLO 205, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.051 | 9/40 (C32, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -3.3 | 0.051 | 15/41 (SK-MEL-2, CHP-212, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.804×** | -3.3 | 0.060 | 12/41 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.072 | 11/39 (SNU-423, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 55.5 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -16.2) |
| [[SHP-77 (line)]] | alt | 97.2 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -13.8) |
| [[SW480 (line)]] | alt | 46.6 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -16.9) |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0761× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.8) |
| [[H4 (line)]] | wt | 13.9 | 0 | 2 (1 ⚠) | — | [[Triamcinolone (drug)]] 0.5 µM 0.0654× (z -10.2) |
| [[A-427 (line)]] | wt | 7.92 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -9.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A498 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 4.76 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0713× (z -9.3) |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.121× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 6.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 9.32 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.51× (z +10.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 33.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -8.7) |
| [[A549 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN12]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[C11orf52]] | +0.54 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[LCA5]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FXYD6]] | +0.52 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[LINC01605]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SLC7A8]] | +0.52 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SGCE]] | +0.52 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[PHYHIPL]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SH3BP5]] | +0.51 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CXXC5]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ZNF711]] | +0.51 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[LINC02223]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[RNF123]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[CCDC57]] | -0.49 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[CTDSP1]] | -0.48 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TRAPPC9]] | -0.48 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[ATG7]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[R3HDM4]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[E2F4]] | -0.46 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[RHBDD1]] | -0.46 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[EP400P1]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[GNL3L]] | -0.46 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[THSD4]] | -0.45 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A8]] | B | SLC7A8 activity raises ATL1's level | lines that do not express SLC7A8 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without SLC7A8 | 0.024 | ⚠ within organs, on part of the lines; also absent: RAB17, LINC00698, RGS6 |
| [[SPINK5]] | B | SPINK5 activity raises ATL1's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without SPINK5 | 0.026 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[PKHD1]] | B | PKHD1 activity raises ATL1's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without PKHD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[PHYHIPL]] | B | PHYHIPL activity raises ATL1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 1.92× lower at baseline in the lines without PHYHIPL | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[CGNL1]] | B | CGNL1 activity raises ATL1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without CGNL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[CXXC5]] | B | CXXC5 activity raises ATL1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.37× lower at baseline in the lines without CXXC5 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A8]] | B | ATL1 activity raises SLC7A8's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 2.47× lower at baseline in the lines without ATL1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |
| [[PKIB]] | B | ATL1 activity raises PKIB's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without ATL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |
| [[SRPK1]] | B | ATL1 activity lowers SRPK1's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 1.44× higher at baseline in the lines without ATL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |
| [[CDC40]] | B | ATL1 activity lowers CDC40's level | lines that do not express ATL1 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without ATL1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000236283, LSMEM2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.3, 48.1); signed map (52.6, 0.5). **Vector** length 83.1, 16.4% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.3 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +5.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -6.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.8 | -5.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | atlastin GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,532,509-50,634,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FSP1, AD-FSP; previously SPG3, SPG3A |
| Gene groups (HGNC) | Atlastins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXF7](https://www.uniprot.org/uniprotkb/Q8WXF7) (Atlastin-1):

> Atlastin-1 (ATL1) is a membrane-anchored GTPase that mediates the GTP-dependent fusion of endoplasmic reticulum (ER) membranes, maintaining the continuous ER network. It facilitates the formation of three-way junctions where ER tubules intersect. Two atlastin-1 on neighboring ER tubules bind GTP and form loose homodimers through the GB1/RHD3-type G domains and 3HB regions. Upon GTP hydrolysis, the 3HB regions tighten, pulling the membranes together to drive their fusion. After fusion, the …

**Summary**, from NCBI Gene [51062](https://www.ncbi.nlm.nih.gov/gene/51062):

> The protein encoded by this gene is a GTPase and a Golgi body transmembrane protein. The encoded protein can form a homotetramer and has been shown to interact with spastin and with mitogen-activated protein kinase kinase kinase kinase 4. This protein may be involved in axonal maintenance as evidenced by the fact that defects in this gene are a cause of spastic paraplegia type 3. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Jul …

**Accessions** — [HGNC:11231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11231) · Entrez [51062](https://www.ncbi.nlm.nih.gov/gene/51062) · UniProt [Q8WXF7](https://www.uniprot.org/uniprotkb/Q8WXF7) · Ensembl [ENSG00000198513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198513)

## Data

Gene col 12604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12604); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12604]; `tensor/DDL_lfc|DDL_z.npy` [12604]; `embed/gene_vectors.npy` [12604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12604 or target_col == 12604). Every well: [[ATL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
