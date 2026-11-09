---
symbol: "B3GLCT"
type: "gene"
col: 11934
ensembl_id: "ENSG00000187676"
name: "beta 3-glucosyltransferase"
location: "13q12.3"
module: 3
arm: "-"
pooled_cpm: 20.09
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# B3GLCT

*beta 3-glucosyltransferase* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.60× (z +8.6, q 4e-15, up in 16 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.32× (z +7.5, q 1e-11, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 4 lines (C32 10.4×, SW480 3.11×, HT-29 3.40×, NCI-H460 3.17×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.611× (z -13.3, q 2e-37, down in 28 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.525× (z -12.3, q 4e-32, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REEP3]] (+0.57, fdr 2e-05), [[HDGFL3]] (+0.57, fdr 2e-04), [[SLC35G1]] (+0.56, fdr 6e-05); moves opposite to [[RANBP10]] (-0.55, fdr 1e-04), [[EMC2]] (-0.53, fdr 6e-05), [[TBC1D17]] (-0.53, fdr 6e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11934.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 4 lines (C32 10.4×, SW480 3.11×, HT-29 3.40×, NCI-H460 3.17×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.6 | 4e-15 | 16/32 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +7.5 | 1e-11 | 25/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +6.4 | 4e-08 | 23/47 (C32, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.16× | +4.1 | 0.006 | 14/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +3.6 | 0.030 | 14/47 (SHP-77, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.6 | 0.030 | 17/41 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.2 | 0.12 | 8/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.14 | 3/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.611×** | -13.3 | 2e-37 | 28/46 (RPMI-7951, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.525×** | -12.3 | 4e-32 | 36/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -11.4 | 1e-27 | 34/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -9.9 | 4e-21 | 33/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -6.8 | 9e-10 | 25/48 (C-33 A, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -6.1 | 1e-07 | 21/46 (SNU-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.743×** | -5.6 | 1e-06 | 22/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.748×** | -5.5 | 2e-06 | 21/47 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.760×** | -5.2 | 1e-05 | 20/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -4.8 | 8e-05 | 17/47 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.789×** | -4.3 | 0.001 | 20/48 (H4, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.801×** | -4.1 | 0.002 | 17/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.809×** | -4.0 | 0.002 | 20/46 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.013 | 13/46 (SHP-77, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.829×** | -3.6 | 0.014 | 15/48 (SW480, LS 180, …) | top dose only | composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.842× | -3.2 | 0.048 | 8/47 (HepG2/C3A, A498, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 0.842× | -3.1 | 0.048 | 8/47 (A498, SHP-77, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.823×** | -3.0 | 0.077 | 9/48 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.745×** | -2.9 | 0.087 | 4/48 (LOX-IMVI, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.898× | -2.9 | 0.094 | 9/48 (NCI-H661, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.4 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.11× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.354× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.204× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.2 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.17× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.264× (z -10.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 47.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 20.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -9.9) |
| [[PANC-1 (line)]] | alt | 24.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0564× (z -8.5) |
| [[C32 (line)]] | wt | 17.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.4× (z +14.7) | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0950× (z -9.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -10.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HT-29 (line)]] | alt | 38.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.40× (z +9.8) | — |
| [[J82 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.120× (z -12.5) |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[HDGFL3]] | +0.57 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[SLC35G1]] | +0.56 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[EMB]] | +0.56 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[ZNF124]] | +0.54 | +0.28 / +0.47 | both halves | 3e-04 |  |
| [[EPM2A]] | +0.53 | +0.46 / +0.35 | both halves | 1e-04 | pathway: Diseases of metabolism |
| [[NETO2]] | +0.53 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ARSB]] | +0.53 | +0.32 / +0.40 | both halves | 2e-04 | pathway: Diseases of metabolism |
| [[PRNP]] | +0.53 | +0.40 / +0.38 | both halves | 6e-05 |  |
| [[CCND1]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PRDM5]] | +0.52 | +0.33 / +0.34 | both halves | 1e-04 |  |
| [[PRDM11]] | +0.51 | +0.26 / +0.43 | both halves | 4e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP10]] | -0.55 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[EMC2]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TBC1D17]] | -0.53 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[NDUFB10]] | -0.52 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[DNAL4]] | -0.52 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[PMM1]] | -0.51 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[COX14]] | -0.51 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[DPCD]] | -0.50 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[ASB8]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CFAP36]] | -0.50 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SF3B2]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[RNASE4]] | -0.49 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.385). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.3, 11.9); signed map (22.4, -29.6). **Vector** length 86.2, 16.9% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +4.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -6.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -5.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -9.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.2 | -12.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | beta 3-glucosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:31,199,975-31,332,276 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B3GTL, B3Glc-T; previously B3GALTL |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Y288](https://www.uniprot.org/uniprotkb/Q6Y288) (Beta-1,3-glucosyltransferase):

> Beta-1,3-glucosyltransferase involved in one of the two pathways responsible for protein O-linked fucosylation, a unique post-translational modification of cysteine-knotted proteins that regulates various biological processes. This pathway targets proteins with Thrombospondin type-1 (TSP1) repeats (TSR) in the endoplasmic reticulum. It starts with POFUT2, which attaches fucose via an O-glycosidic bond to a conserved serine or threonine residue. B3GLCT extends this modification by transferring a …

**Summary**, from NCBI Gene [145173](https://www.ncbi.nlm.nih.gov/gene/145173):

> The protein encoded by this gene is a beta-1,3-glucosyltransferase that transfers glucose to O-linked fucosylglycans on thrombospondin type-1 repeats (TSRs) of several proteins. The encoded protein is a type II membrane protein. Defects in this gene are a cause of Peters-plus syndrome (PPS).[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:20207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20207) · Entrez [145173](https://www.ncbi.nlm.nih.gov/gene/145173) · UniProt [Q6Y288](https://www.uniprot.org/uniprotkb/Q6Y288) · Ensembl [ENSG00000187676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187676)

## Data

Gene col 11934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11934); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11934]; `tensor/DDL_lfc|DDL_z.npy` [11934]; `embed/gene_vectors.npy` [11934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11934 or target_col == 11934). Every well: [[B3GLCT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GLCT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
