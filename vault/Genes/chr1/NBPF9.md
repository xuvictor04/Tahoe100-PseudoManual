---
symbol: "NBPF9"
type: "gene"
col: 15629
ensembl_id: "ENSG00000269713"
name: "NBPF member 9"
location: "1q21.2"
module: 110
arm: "+"
pooled_cpm: 18.3
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# NBPF9

*NBPF member 9* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.84× (z +12.7, q 3e-34, up in 31 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.60× (z +9.7, q 8e-20, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.797× (z -6.7, q 1e-08, down in 20 of 47 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Trametinib (drug)]] 5 µM: 0.750× (z -6.2, q 2e-07, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF8]] (+0.81, fdr 7e-06), [[NBPF20]] (+0.75, fdr 7e-06), [[NBPF15]] (+0.73, fdr 7e-06); moves opposite to [[RBM7]] (-0.53, fdr 1e-05), [[ZNF33A]] (-0.51, fdr 4e-05), [[CDKN1B]] (-0.49, fdr 2e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZEB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +12.7 | 3e-34 | 31/46 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +9.7 | 8e-20 | 28/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +9.6 | 2e-19 | 27/48 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.8 | 1e-12 | 26/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +6.8 | 9e-10 | 26/47 (A498, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +6.4 | 2e-08 | 20/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +6.2 | 5e-08 | 19/47 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 9e-08 | 19/46 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +6.1 | 9e-08 | 23/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +6.0 | 1e-07 | 16/45 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.9 | 2e-07 | 8/26 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +5.7 | 7e-07 | 18/47 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.1 | 1e-05 | 18/48 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 7e-05 | 14/45 (NCI-H23, SW480, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.7 | 9e-05 | 17/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 1e-04 | 12/43 (NCI-H460, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 1e-04 | 13/47 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 14/47 (LoVo, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.007 | 6/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.007 | 9/41 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.6 | 0.008 | 15/48 (LoVo, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.797×** | -6.7 | 1e-08 | 20/47 (J82, SK-MEL-2, …) | top dose only | composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.750×** | -6.2 | 2e-07 | 18/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.738×** | -6.1 | 2e-07 | 22/47 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.767×** | -5.6 | 3e-06 | 18/47 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.769×** | -5.2 | 2e-05 | 18/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.818×** | -5.1 | 4e-05 | 19/48 (HOP62, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.843× | -5.0 | 5e-05 | 15/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.780×** | -4.8 | 1e-04 | 17/47 (HOP62, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.814×** | -4.3 | 1e-03 | 19/48 (RKO, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.002 | 12/48 (HOP62, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.849× | -4.0 | 0.003 | 13/48 (HOP62, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.840× | -3.7 | 0.011 | 14/47 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.5 | 0.018 | 17/48 (J82, RKO, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.037 | 13/43 (RPMI-7951, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (mesylate) (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.069 | 9/48 (J82, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 35.6 | 0 | 4 | — | [[Trametinib (drug)]] 0.5 µM 0.417× (z -9.7) |
| [[A-427 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 9.61 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.129× (z -8.5) ⚠ transcription drop |
| [[J82 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H460 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF8]] | +0.81 | +0.81 / +0.78 | both halves | 7e-06 | same gene group |
| [[NBPF20]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | same gene group |
| [[NBPF15]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | same gene group |
| [[RUSC2]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[GSTO1]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.60 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SMAGP]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CRYL1]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RGMB]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CUTC]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM7]] | -0.53 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ZNF33A]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CDKN1B]] | -0.49 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[CHASERR]] | -0.49 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[BTN3A1]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[AKR1B1]] | -0.47 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EFNA1]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[COQ7]] | -0.45 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[CNOT1]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[LCOR]] | -0.45 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[MYOF]] | -0.45 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CTNND1]] | -0.44 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZEB1]] | B | ZEB1 activity raises NBPF9's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without ZEB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[ITPRIP]] | B | ITPRIP activity raises NBPF9's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without ITPRIP | 0.040 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[IL13RA2]] | B | IL13RA2 activity raises NBPF9's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 1.58× lower at baseline in the lines without IL13RA2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3 |
| [[PARVB]] | B | PARVB activity raises NBPF9's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without PARVB | 0.049 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[KLHL29]] | B | KLHL29 activity raises NBPF9's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without KLHL29 | 0.056 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[EFNA1]] | B | EFNA1 activity lowers NBPF9's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.48× higher at baseline in the lines without EFNA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[FLI1]] | B | FLI1 activity raises NBPF9's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 1.50× lower at baseline in the lines without FLI1 | 0.061 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[KCNG1]] | B | KCNG1 activity raises NBPF9's level | lines that do not express KCNG1 (18) vs lines expressing it (32) | 1.59× lower at baseline in the lines without KCNG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: AOX1, RASSF8, MSRB3 |
| [[MAP2K2]] | B | MAP2K2 activity raises NBPF9's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PALS2]] | C | PALS2 activity strengthens NBPF9's drug response | lines that do not express PALS2 (3) vs lines expressing it (45) | the lines without PALS2 respond the other way (z diff +2.34); strongest at Ouabain (Octahydrate) 5 µM: 0.71x vs 1.54x (z diff +4.7) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.9, -25.1); signed map (-17.3, 47.1). **Vector** length 98.9, 21.4% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.5 | +9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +6.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.5 | -6.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -5.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -6.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,052,186-149,103,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AE01 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [P0DPF3](https://www.uniprot.org/uniprotkb/P0DPF3) carries no function annotation.

**Summary**, from NCBI Gene [400818](https://www.ncbi.nlm.nih.gov/gene/400818):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:31991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31991) · Entrez [400818](https://www.ncbi.nlm.nih.gov/gene/400818) · UniProt [P0DPF3](https://www.uniprot.org/uniprotkb/P0DPF3) · Ensembl [ENSG00000269713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269713)

## Data

Gene col 15629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15629); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15629]; `tensor/DDL_lfc|DDL_z.npy` [15629]; `embed/gene_vectors.npy` [15629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15629 or target_col == 15629). Every well: [[NBPF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
