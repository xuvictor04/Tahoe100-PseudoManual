---
symbol: "KCNC4"
type: "gene"
col: 3793
ensembl_id: "ENSG00000116396"
name: "potassium voltage-gated channel subfamily C member 4"
location: "1p13.3"
module: 110
arm: "+"
pooled_cpm: 12.81
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# KCNC4

*potassium voltage-gated channel subfamily C member 4* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.66× (z +6.3, q 2e-07, up in 23 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.315× (z -21.0, q 0e+00, down in 35 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXYD5]] (+0.68, fdr 7e-06), [[CORO2B]] (+0.68, fdr 7e-06), [[PODXL]] (+0.65, fdr 7e-06); moves opposite to [[ZNF608]] (-0.64, fdr 7e-06), [[ANAPC16]] (-0.58, fdr 1e-05), [[LINC01170]] (-0.57, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EBF4]] → it (grade B ⚠); 10 go from it, the strongest it → [[AP3M2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.66×** | +6.3 | 2e-07 | 23/40 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +5.9 | 9e-07 | 8/19 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 1e-04 | 20/40 (NCI-H23, HOP62, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.3 | 0.12 | 7/42 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | 1.29× | +3.3 | 0.12 | 8/40 (NCI-H23, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.19 | 5/39 (PANC-1, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.27× | +3.0 | 0.19 | 7/40 (H4, SW48, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.315×** | -21.0 | 0e+00 | 35/40 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.227×** | -18.3 | 0e+00 | 35/40 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.366×** | -12.9 | 9e-36 | 30/38 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.430×** | -10.8 | 3e-25 | 32/41 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.437×** | -10.6 | 3e-24 | 31/40 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -8.7 | 4e-16 | 27/40 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -7.6 | 3e-12 | 28/40 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -7.2 | 3e-11 | 25/40 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -6.6 | 3e-09 | 20/40 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.589×** | -6.6 | 3e-09 | 19/41 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.615×** | -6.2 | 2e-08 | 21/41 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.402×** | -6.1 | 5e-08 | 23/37 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.9 | 1e-07 | 20/40 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.636×** | -5.8 | 3e-07 | 19/41 (HOP62, A-427, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -5.8 | 3e-07 | 20/41 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.657×** | -5.2 | 8e-06 | 15/40 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.1 | 0 | 15 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0662× (z -17.0) |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -15.8) |
| [[LoVo (line)]] | wt | 45.2 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -20.9) |
| [[NCI-H23 (line)]] | alt | 56.7 | 0 | 7 | — | [[Harringtonine (drug)]] 5 µM 0.0179× (z -27.5) |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0651× (z -14.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.110× (z -11.8) |
| [[SW48 (line)]] | wt | 18.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0534× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 5.50 | 0 | 4 | — | [[Omeprazole (drug)]] 0.5 µM 0.0636× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 8.59 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0672× (z -13.2) |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -18.3) |
| [[A-427 (line)]] | wt | 11.4 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0739× (z -13.8) |
| [[A549 (line)]] | wt | 9.61 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0517× (z -18.7) |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -15.5) |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.1) |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0658× (z -19.7) |
| [[RKO (line)]] | wt | 11.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -10.1) |
| [[SW480 (line)]] | alt | 11.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -14.1) |
| [[C32 (line)]] | wt | 7.61 | 0 | 1 | — | [[Trametinib (drug)]] 0.05 µM 0.169× (z -9.0) |
| [[J82 (line)]] | alt | 9.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 5.24 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0889× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 7.72 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.131× (z -11.3) |
| [[SW 900 (line)]] | alt | 4.48 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0722× (z -8.6) |
| [[SW1417 (line)]] | alt | 6.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -9.1) |
| [[A498 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXYD5]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[PODXL]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[PNP]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[S100A16]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PLXNA1]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ATP13A2]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[VAV2]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CCNE1]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.64 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[ANAPC16]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[LINC01170]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PHF21A]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ZNF292]] | -0.54 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[FMC1]] | -0.53 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[RAB30]] | -0.52 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[CEP350]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CDKN1B]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SORBS2]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NIPBL]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[FIGN]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF4]] | B | EBF4 activity raises KCNC4's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without EBF4 | 0.069 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[GLI2]] | B | GLI2 activity strengthens KCNC4's drug response | lines that do not express GLI2 (10) vs lines expressing it (32) | the lines without GLI2 respond 0.54× as strongly (z diff +1.91); strongest at Ouabain (Octahydrate) 0.5 µM: 0.85x vs 0.50x (z diff +3.0) | 0.080 | ⚠ within organs, on part of the lines; also absent: HAPLN3; target measured in part of the lines; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP3M2]] | B | KCNC4 activity raises AP3M2's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without KCNC4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[SDC3]] | B | KCNC4 activity raises SDC3's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without KCNC4 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[CDR2L]] | B | KCNC4 activity raises CDR2L's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without KCNC4 | 0.035 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[PLP2]] | B | KCNC4 activity raises PLP2's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without KCNC4 | 0.045 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[GATAD2A]] | B | KCNC4 activity raises GATAD2A's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.24× lower at baseline in the lines without KCNC4 | 0.048 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[ATP13A2]] | B | KCNC4 activity raises ATP13A2's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without KCNC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[LIMK1]] | B | KCNC4 activity raises LIMK1's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without KCNC4 | 0.062 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[SLC25A19]] | B | KCNC4 activity raises SLC25A19's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without KCNC4 | 0.072 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[FMC1]] | B | KCNC4 activity raises FMC1's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without KCNC4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[EFL1]] | B | KCNC4 activity strengthens EFL1's drug response | lines that do not express KCNC4 (6) vs lines expressing it (44) | the lines without KCNC4 respond 0.54× as strongly (z diff +2.19); strongest at Idarubicin (hydrochloride) 5 µM: 0.71x vs 0.49x (z diff +4.0) | 0.090 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent; artifact flags |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.0, 3.8); signed map (4.8, 47.2). **Vector** length 97.1, 23.1% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.4 | +6.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -2.0 |
|  | [[vincristine (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -18.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -10.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily C member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,210,314-110,283,100 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv3.4, HKSHIIIC; previously C1orf30 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03721](https://www.uniprot.org/uniprotkb/Q03721) (Voltage-gated potassium channel KCNC4):

> Voltage-gated potassium channel that opens in response to the voltage difference across the membrane, forming a potassium-selective channel through which potassium ions pass in accordance with their electrochemical gradient. The channel displays rapid activation and inactivation kinetics.

**Summary**, from NCBI Gene [3749](https://www.ncbi.nlm.nih.gov/gene/3749):

> The Shaker gene family of Drosophila encodes components of voltage-gated potassium channels and is comprised of four subfamilies. Based on sequence similarity, this gene is similar to the Shaw subfamily. The protein encoded by this gene belongs to the delayed rectifier class of channel proteins and is an integral membrane protein that mediates the voltage-dependent potassium ion permeability of excitable membranes. It generates atypical voltage-dependent transient current that may be important …

**Accessions** — [HGNC:6236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6236) · Entrez [3749](https://www.ncbi.nlm.nih.gov/gene/3749) · UniProt [Q03721](https://www.uniprot.org/uniprotkb/Q03721) · Ensembl [ENSG00000116396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116396)

## Data

Gene col 3793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3793); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3793]; `tensor/DDL_lfc|DDL_z.npy` [3793]; `embed/gene_vectors.npy` [3793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3793 or target_col == 3793). Every well: [[KCNC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
