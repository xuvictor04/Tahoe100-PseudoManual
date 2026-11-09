---
symbol: "TMCC1-DT"
type: "gene"
col: 15680
ensembl_id: "ENSG00000271270"
name: "TMCC1 divergent transcript"
location: "3q22.1"
module: 10
arm: "+"
pooled_cpm: 3.97
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMCC1-DT

*TMCC1 divergent transcript* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.79× (z +9.2, q 2e-17, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +6.5, q 9e-09, up in 13 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.431× (z -7.9, q 2e-12, down in 24 of 44 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.495× (z -6.6, q 6e-09, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP2]] (+0.65, fdr 7e-06), [[FTCDNL1]] (+0.63, fdr 1e-05), [[ABCA17P]] (+0.62, fdr 2e-05); moves opposite to [[SHOC2]] (-0.53, fdr 3e-05), [[MYO1E]] (-0.47, fdr 1e-04), [[CDKL5]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); 8 go from it, the strongest it → [[COPS8-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +9.2 | 2e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +7.1 | 4e-10 | 7/15 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +6.6 | 9e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.5 | 9e-09 | 13/32 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +5.1 | 3e-05 | 12/42 (PANC-1, KATO III, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.77×** | +5.1 | 3e-05 | 18/36 (J82, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.40×** | +4.4 | 8e-04 | 10/43 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.4 | 8e-04 | 4/17 (A549, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.021 | 3/34 (J82, NCI-H2030, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.023 | 9/44 (HT-29, C-33 A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.027 | 7/38 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.029 | 7/36 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.058 | 8/38 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.099 | 4/44 (RKO, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.431×** | -7.9 | 2e-12 | 24/44 (PANC-1, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.593×** | -6.9 | 1e-09 | 21/36 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.495×** | -6.6 | 6e-09 | 15/24 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.495×** | -6.6 | 6e-09 | 22/41 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.540×** | -5.6 | 3e-06 | 19/41 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.590×** | -5.0 | 7e-05 | 18/39 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -4.9 | 7e-05 | 13/38 (PANC-1, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.692×** | -3.5 | 0.039 | 10/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.508×** | -3.3 | 0.056 | 11/30 (C-33 A, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.7) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.200× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0485× (z -14.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0599× (z -9.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 8.84 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -10.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 5.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.7) ⚠ cell-cycle shift, explains ~64% of this change |
| [[J82 (line)]] | alt | 4.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H23 (line)]] | alt | 7.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 5.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[RKO (line)]] | wt | 6.68 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0674× (z -9.8) |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP2]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[FTCDNL1]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ABCA17P]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[METAP1D]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 | same gene group |
| [[LINC01357]] | +0.57 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[GABPB1-AS1]] | +0.57 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[ADCK1]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[KCTD21-AS1]] | +0.57 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[EIF3E]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ZNF485]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TRIM66]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHOC2]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MYO1E]] | -0.47 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[CDKL5]] | -0.47 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises TMCC1-DT's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without MIR1915HG | 0.011 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[KLHL14]] | B | KLHL14 activity raises TMCC1-DT's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without KLHL14 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[LAMC3]] | B | LAMC3 activity raises TMCC1-DT's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without LAMC3 | 0.042 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[MYO1E]] | B | MYO1E activity lowers TMCC1-DT's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.77× higher at baseline in the lines without MYO1E | 0.055 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[KLHL14]] | B | KLHL14 activity strengthens TMCC1-DT's drug response | lines that do not express KLHL14 (33) vs lines expressing it (11) | the lines without KLHL14 respond 0.61× as strongly (z diff +1.19); strongest at Harringtonine 5 µM: 0.46x vs 0.28x (z diff +2.7) | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; target measured in part of the lines; artifact flags |
| [[LAMC3]] | B | LAMC3 activity strengthens TMCC1-DT's drug response | lines that do not express LAMC3 (22) vs lines expressing it (22) | the lines without LAMC3 respond 0.74× as strongly (z diff +1.08); strongest at Digitoxin 5 µM: 0.40x vs 0.30x (z diff +2.4) | 0.089 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COPS8-DT]] | C | TMCC1-DT activity raises COPS8-DT's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[ZNF32]] | C | TMCC1-DT activity raises ZNF32's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[PRDX6-AS1]] | C | TMCC1-DT activity raises PRDX6-AS1's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[CRTC3-AS1]] | C | TMCC1-DT activity raises CRTC3-AS1's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[LINC02728]] | C | TMCC1-DT activity raises LINC02728's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[NSMCE1-DT]] | C | TMCC1-DT activity raises NSMCE1-DT's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[CDNF]] | C | TMCC1-DT activity raises CDNF's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without TMCC1-DT | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent |
| [[PCMTD1-DT]] | C | TMCC1-DT activity raises PCMTD1-DT's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without TMCC1-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.0, 31.4); signed map (35.8, -10.0). **Vector** length 54.2, 7.55% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.5 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +5.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.0 | -5.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -1.6 | -6.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Artemether (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | TMCC1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q22.1 — chr3:129,893,811-129,918,578 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously TMCC1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49060) · Entrez [100507032](https://www.ncbi.nlm.nih.gov/gene/100507032) · Ensembl [ENSG00000271270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271270)

## Data

Gene col 15680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15680); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15680]; `tensor/DDL_lfc|DDL_z.npy` [15680]; `embed/gene_vectors.npy` [15680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15680 or target_col == 15680). Every well: [[TMCC1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCC1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
