---
symbol: "GLB1"
type: "gene"
col: 9924
ensembl_id: "ENSG00000170266"
name: "galactosidase beta 1"
location: "3p22.3"
module: 50
arm: "+"
pooled_cpm: 49.97
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GLB1

*galactosidase beta 1* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.32× (z +7.3, q 1e-10, up in 24 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.20× (z +4.9, q 1e-04, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.389× (z -36.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAN2B2]] (+0.73, fdr 7e-06), [[RNPEP]] (+0.70, fdr 7e-06), [[PLBD2]] (+0.69, fdr 7e-06); moves opposite to [[HELQ]] (-0.61, fdr 7e-06), [[CD163L1]] (-0.61, fdr 1e-05), [[METTL23]] (-0.60, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +7.3 | 1e-10 | 24/41 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +6.3 | 8e-08 | 23/48 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.20×** | +5.1 | 8e-05 | 20/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +4.9 | 1e-04 | 21/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +4.8 | 2e-04 | 16/48 (RKO, SW480, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +4.1 | 0.004 | 14/48 (J82, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.30×** | +3.7 | 0.013 | 13/44 (LS 180, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.7 | 0.013 | 7/48 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.015 | 7/49 (NCI-H2347, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.016 | 11/48 (C32, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.016 | 9/49 (RKO, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.060 | 5/47 (C32, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.12× | +3.1 | 0.084 | 5/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.08× | +3.1 | 0.084 | 13/48 (J82, LS 180, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.100 | 13/47 (SW480, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.389×** | -36.9 | 0e+00 | 46/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.409×** | -23.8 | 0e+00 | 44/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -21.6 | 0e+00 | 44/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -14.7 | 0e+00 | 42/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -8.5 | 3e-15 | 32/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.736×** | -7.9 | 4e-13 | 26/47 (A-172, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -6.7 | 2e-09 | 22/48 (CHP-212, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.794×** | -6.4 | 1e-08 | 24/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.803×** | -5.8 | 3e-07 | 24/48 (A498, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -5.0 | 4e-05 | 20/48 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 0.844× | -4.7 | 1e-04 | 19/48 (SW480, LOX-IMVI, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.868× | -4.0 | 0.004 | 17/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.876× | -3.7 | 0.010 | 13/48 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.917× | -3.4 | 0.024 | 2/49 (LoVo, SW 900) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.889× | -3.3 | 0.038 | 12/48 (SW480, NCI-H661, …) | rises with dose |  |
| [[Silodosin (drug)]] 5 µM |  | 0.890× | -3.1 | 0.066 | 10/47 (SW 1271, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 81.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -29.6) |
| [[C32 (line)]] | wt | 56.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 38.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 46.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -23.7) |
| [[PANC-1 (line)]] | alt | 29.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -24.2) |
| [[SW480 (line)]] | alt | 45.8 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.408× (z -12.0) |
| [[A498 (line)]] | wt | 40.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -25.5) |
| [[A549 (line)]] | wt | 45.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.2) |
| [[HS-578T (line)]] | alt | 46.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.4) |
| [[A-427 (line)]] | wt | 40.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -13.9) |
| [[HOP62 (line)]] | alt | 58.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -21.4) |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 40.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -21.0) |
| [[NCI-H2347 (line)]] | alt | 66.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 56.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 75.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 52.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -16.1) |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -12.8) |
| [[SW1417 (line)]] | alt | 87.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.6) |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 44.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -16.8) |
| [[J82 (line)]] | alt | 70.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -15.2) |
| [[KATO III (line)]] | alt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.4) |
| [[LoVo (line)]] | wt | 41.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.490× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 39.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -13.6) |
| [[LS 180 (line)]] | wt | 64.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.455× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 43.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -12.3) |
| [[RKO (line)]] | wt | 57.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -9.4) |
| [[SNU-423 (line)]] | alt | 71.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -21.5) |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 45.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.3) |
| [[SNU-1 (line)]] | wt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -8.5) |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN2B2]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives; STRING 434 |
| [[RNPEP]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PLBD2]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ENTREP3]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[NAGPA]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism; STRING 771 |
| [[STIM1]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.63 | +0.70 / +0.51 | both halves | 1e-05 | ⚠ same locus (16.8 kb: neighbours can correlate without regulation) |
| [[ADPGK]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PPT1]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CTSD]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.62 | +0.69 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELQ]] | -0.61 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[CD163L1]] | -0.61 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[METTL23]] | -0.60 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.59 | -0.62 / -0.57 | both halves | 8e-06 |  |
| [[NSRP1]] | -0.59 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.58 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[OFD1]] | -0.57 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[SURF6]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.57 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SFR1]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CCDC148]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers GLB1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TEAD2]] | B | TEAD2 activity raises GLB1's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without TEAD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[PPP1R1C]] | B | PPP1R1C activity lowers GLB1's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.19× higher at baseline in the lines without PPP1R1C | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[CTSZ]] | B | CTSZ activity raises GLB1's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.18× lower at baseline in the lines without CTSZ | 0.093 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[CRTAP]] | C | CRTAP activity raises GLB1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without CRTAP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.9, -14.8); signed map (-46.4, -12.0). **Vector** length 99.9, 22.8% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.5 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.8 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -21.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.7 | -23.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.1 | -14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -36.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -7.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | galactosidase beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:32,996,609-33,097,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EBP; previously ELNR1 |
| Gene groups (HGNC) | Galactosidases beta |
| Reactome | 22 pathways, smallest: Defective NEU1 causes sialidosis; Keratan sulfate degradation; Mucopolysaccharidoses |
| Matched by | ensembl_id |

**Function**, from UniProt [P16278](https://www.uniprot.org/uniprotkb/P16278) (Beta-galactosidase):

> [Isoform 1]: Cleaves beta-linked terminal galactosyl residues from gangliosides, glycoproteins, and glycosaminoglycans.; [Isoform 2]: Has no beta-galactosidase catalytic activity, but plays functional roles in the formation of extracellular elastic fibers (elastogenesis) and in the development of connective tissue. Seems to be identical to the elastin-binding protein (EBP), a major component of the non-integrin cell surface receptor expressed on fibroblasts, smooth muscle cells, chondroblasts, …

**Summary**, from NCBI Gene [2720](https://www.ncbi.nlm.nih.gov/gene/2720):

> This gene encodes a member of the glycosyl hydrolase 35 family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the mature lysosomal enzyme. This enzyme catalyzes the hydrolysis of a terminal beta-linked galactose residue from ganglioside substrates and other glycoconjugates. Mutations in this gene may result in GM1-gangliosidosis and Morquio B syndrome. [provided by RefSeq, Nov …

**Accessions** — [HGNC:4298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4298) · Entrez [2720](https://www.ncbi.nlm.nih.gov/gene/2720) · UniProt [P16278](https://www.uniprot.org/uniprotkb/P16278) · Ensembl [ENSG00000170266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170266)

## Data

Gene col 9924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9924); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9924]; `tensor/DDL_lfc|DDL_z.npy` [9924]; `embed/gene_vectors.npy` [9924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9924 or target_col == 9924). Every well: [[GLB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
