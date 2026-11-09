---
symbol: "GPRIN2"
type: "gene"
col: 12824
ensembl_id: "ENSG00000204175"
name: "G protein regulated inducer of neurite outgrowth 2"
location: "10q11.22"
module: 8
arm: "+"
pooled_cpm: 3.94
n_lines_expressing: 19
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GPRIN2

*G protein regulated inducer of neurite outgrowth 2* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.26× (z +11.7, q 4e-29, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.75× (z +5.3, q 2e-05, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.478× (z -5.5, q 3e-05, down in 14 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A549 0.0255×, LoVo 0.101×, PANC-1 0.136×, Hs 766T 0.0617×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (LoVo 0.0250×, A549 0.0786×, PANC-1 0.122×, Hs 766T 0.0572×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.0344×, A498 0.132×; ⚠ cell-cycle shift, explains ~55% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.0793×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.139×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC16]] (+0.65, fdr 1e-05), [[DAPK1]] (+0.65, fdr 1e-05), [[PLA2R1]] (+0.58, fdr 2e-05); moves opposite to [[NPAS2]] (-0.53, fdr 1e-04), [[SHC4]] (-0.47, fdr 9e-05), [[PHC2]] (-0.47, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[GALM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.26×** | +11.7 | 4e-29 | 3/6 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.99×** | +9.4 | 1e-18 | 2/8 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +9.2 | 9e-18 | 2/12 (PANC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.75×** | +5.3 | 2e-05 | 2/10 (NCI-H23, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +4.7 | 3e-04 | 2/11 (NCI-H2347, Hs 766T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.55×** | +4.4 | 9e-04 | 10/16 (LS 180, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.68×** | +4.3 | 0.001 | 10/16 (LoVo, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.25×** | +4.3 | 0.001 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.51×** | +4.2 | 0.001 | 11/16 (Hs 766T, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.003 | 9/16 (LoVo, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.15×** | +4.0 | 0.003 | 6/16 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.0 | 0.003 | 2/16 (SW48, J82) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.75×** | +3.9 | 0.004 | 10/16 (A498, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.005 | 5/16 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.8 | 0.006 | 1/14 (HT-29) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.012 | 2/15 (Panc 03.27, NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.022 | 0/16 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +3.3 | 0.024 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.035 | 3/16 (LoVo, PANC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.038 | 9/16 (LoVo, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.51×** | +3.0 | 0.058 | 8/16 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +2.9 | 0.078 | 9/16 (A549, PANC-1, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12824.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A549 0.0255×, LoVo 0.101×, PANC-1 0.136×, Hs 766T 0.0617×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (LoVo 0.0250×, A549 0.0786×, PANC-1 0.122×, Hs 766T 0.0572×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.0344×, A498 0.132×; ⚠ cell-cycle shift, explains ~55% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.0793×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -5.5 | 3e-05 | 14/16 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.543×** | -4.5 | 0.002 | 15/16 (LoVo, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.555×** | -4.4 | 0.002 | 14/16 (LoVo, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.559×** | -4.3 | 0.002 | 15/16 (LoVo, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.51 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0250× (z -18.3) |
| [[A549 (line)]] | wt | 18.1 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0255× (z -27.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0786× (z -13.5) |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -8.6) |
| [[PANC-1 (line)]] | alt | 5.74 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -9.5) |
| [[A498 (line)]] | wt | 35.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -13.3) ⚠ cell-cycle shift, explains ~91% of this change |
| [[J82 (line)]] | alt | 2.60 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 6.23 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0617× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0572× (z -9.2) |
| [[HT-29 (line)]] | alt | 3.25 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0414× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 3.44 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0620× (z -9.0) |
| [[LS 180 (line)]] | wt | 1.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0678× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 4.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.865 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC16]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 | STRING 472 |
| [[DAPK1]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[PLA2R1]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[ALDH3B1]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PLAC8]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MUC4]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[ASS1]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[LINC01133]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[LMNTD2]] | +0.50 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[GABRP]] | +0.49 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[LY75]] | +0.49 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[SIDT1]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPAS2]] | -0.53 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[SHC4]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[PHC2]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SHC3]] | -0.45 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[RNF144A]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[ETV1]] | -0.43 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[CHD1L]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[SPRY4]] | -0.43 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[WWTR1]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ACSS3]] | -0.42 | -0.45 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[DCBLD2]] | -0.42 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[LOXL3]] | -0.42 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[LINC01844]] | -0.41 | -0.29 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GPRIN2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00842]] | C | LINC00842 activity raises GPRIN2's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without LINC00842 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises GPRIN2's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 2.84× lower at baseline in the lines without HAVCR1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises GPRIN2's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.78× lower at baseline in the lines without TIMD4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |
| [[MUC16]] | C | MUC16 activity raises GPRIN2's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 2.67× lower at baseline in the lines without MUC16 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALM]] | B | GPRIN2 activity raises GALM's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without GPRIN2 | 0.062 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7 |
| [[JDP2]] | B | GPRIN2 activity raises JDP2's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without GPRIN2 | 0.075 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7 |
| [[LINC00842]] | C | GPRIN2 activity raises LINC00842's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without GPRIN2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |
| [[B3GNT7]] | C | GPRIN2 activity raises B3GNT7's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without GPRIN2 | 0.017 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |
| [[MUC16]] | C | GPRIN2 activity raises MUC16's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 5.15× lower at baseline in the lines without GPRIN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |
| [[LINC02086]] | C | GPRIN2 activity raises LINC02086's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 4.01× lower at baseline in the lines without GPRIN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |
| [[PLAC8]] | C | GPRIN2 activity raises PLAC8's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 2.88× lower at baseline in the lines without GPRIN2 | 0.065 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |
| [[CLIC5]] | C | GPRIN2 activity raises CLIC5's level | lines that do not express GPRIN2 (31) vs lines expressing it (19) | 3.19× lower at baseline in the lines without GPRIN2 | 0.096 | ⚠ within organs, on part of the lines; also absent: MUC16, KRT6A, ACP7; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 56.5); signed map (62.5, 0.8). **Vector** length 45.2, 11.2% of its response variance represented; |z| ≥ 3 in 518 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.7 | +4.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.0 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | G protein regulated inducer of neurite outgrowth 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22 — chr10:46,541,736-46,556,658 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15171; previously KIAA0514 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60269](https://www.uniprot.org/uniprotkb/O60269) (G protein-regulated inducer of neurite outgrowth 2):

> May be involved in neurite outgrowth.

**Summary**, from NCBI Gene [9721](https://www.ncbi.nlm.nih.gov/gene/9721):

> Predicted to be involved in neuron projection development. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23730) · Entrez [9721](https://www.ncbi.nlm.nih.gov/gene/9721) · UniProt [O60269](https://www.uniprot.org/uniprotkb/O60269) · Ensembl [ENSG00000204175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204175)

## Data

Gene col 12824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12824); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12824]; `tensor/DDL_lfc|DDL_z.npy` [12824]; `embed/gene_vectors.npy` [12824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12824 or target_col == 12824). Every well: [[GPRIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
