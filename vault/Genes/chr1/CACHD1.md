---
symbol: "CACHD1"
type: "gene"
col: 8206
ensembl_id: "ENSG00000158966"
name: "cache domain containing 1"
location: "1p31.3"
module: 143
arm: "+"
pooled_cpm: 41.36
n_lines_expressing: 43
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 7
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# CACHD1

*cache domain containing 1* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.05× (z +28.0, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.663× (z -7.0, q 1e-09, down in 19 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.704× (z -6.3, q 1e-07, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRA3]] (+0.64, fdr 2e-05), [[NCR3LG1]] (+0.58, fdr 2e-05), [[ISOC1]] (+0.57, fdr 9e-06); moves opposite to [[ZCCHC17]] (-0.54, fdr 5e-05), [[SZT2]] (-0.54, fdr 2e-05), [[KRBOX4]] (-0.54, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); 7 go from it, the strongest it → [[FAM169A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.05×** | +28.0 | 0e+00 | 38/41 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +13.5 | 3e-39 | 35/41 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +12.2 | 7e-32 | 34/41 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +11.0 | 4e-26 | 26/41 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +9.0 | 4e-17 | 25/41 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.4 | 3e-15 | 21/40 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +8.4 | 4e-15 | 28/41 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +7.8 | 5e-13 | 29/41 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +6.6 | 2e-09 | 24/41 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +6.3 | 2e-08 | 24/40 (J82, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 9e-07 | 25/40 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 7e-06 | 21/40 (SW48, A-427, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +5.1 | 1e-05 | 18/41 (LOX-IMVI, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 9e-05 | 20/40 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 2e-04 | 20/40 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -7.0 | 1e-09 | 19/29 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -6.3 | 1e-07 | 21/40 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -5.3 | 3e-05 | 18/41 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.779×** | -4.5 | 0.001 | 19/39 (SW480, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.764×** | -4.4 | 0.001 | 19/37 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **0.782×** | -4.4 | 0.001 | 18/37 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.011 | 13/39 (SHP-77, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.069 | 11/39 (COLO 205, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.879× | -3.3 | 0.069 | 11/41 (KATO III, SW 1271, …) | two highest doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.082 | 8/42 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.883× | -3.2 | 0.082 | 11/41 (Hs 766T, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 138 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -11.8) |
| [[LoVo (line)]] | wt | 59.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.5) | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +18.0) | — |
| [[PANC-1 (line)]] | alt | 82.6 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.4) |
| [[A-427 (line)]] | wt | 43.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 12.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.9× (z +23.0) | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.7× (z +24.3) | — |
| [[LOX-IMVI (line)]] | wt | 74.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +17.8) | — |
| [[RKO (line)]] | wt | 60.0 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW48 (line)]] | wt | 94.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -16.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 36.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.4) | — |
| [[A498 (line)]] | wt | 24.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +23.5) | — |
| [[A549 (line)]] | wt | 18.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.9) | [[Harringtonine (drug)]] 0.05 µM 0.244× (z -8.5) |
| [[C-33 A (line)]] | alt | 64.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 48.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +19.2) | — |
| [[J82 (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +16.8) | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +25.4) | — |
| [[NCI-H23 (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 21.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +13.3) | — |
| [[AN3 CA (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0685× (z -15.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.2) | — |
| [[C32 (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.8) | — |
| [[Hs 766T (line)]] | wt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.8) | — |
| [[KATO III (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 53.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +19.0) | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -13.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRA3]] | +0.64 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[NCR3LG1]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ISOC1]] | +0.57 | +0.58 / +0.57 | both halves | 9e-06 | same gene group |
| [[STOX1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[GPR63]] | +0.55 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[PPM1H]] | +0.54 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GSE1]] | +0.54 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[FAM171B]] | +0.54 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ADAM22]] | +0.54 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[POGLUT1]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[UST]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SZT2]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 | same gene group |
| [[KRBOX4]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EVI5L]] | -0.53 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[COPA]] | -0.51 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[ZNF526]] | -0.50 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[RAB18]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[RARS2]] | -0.50 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.50 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[YIPF1]] | -0.49 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[YKT6]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SLC35E1]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises CACHD1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without MIR1915HG | 0.003 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[SLC16A10]] | B | SLC16A10 activity raises CACHD1's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without SLC16A10 | 0.008 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[ADAM22]] | B | ADAM22 activity raises CACHD1's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without ADAM22 | 0.015 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[ADRA2C]] | B | ADRA2C activity raises CACHD1's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without ADRA2C | 0.029 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B |
| [[ATF7IP2]] | B | ATF7IP2 activity raises CACHD1's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 2.11× lower at baseline in the lines without ATF7IP2 | 0.038 | ⚠ within organs, on part of the lines |
| [[FAXC]] | B | FAXC activity raises CACHD1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without FAXC | 0.044 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[SOBP]] | B | SOBP activity raises CACHD1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without SOBP | 0.044 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[FAM169A]] | B | FAM169A activity raises CACHD1's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.72× lower at baseline in the lines without FAM169A | 0.077 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[KLHL14]] | B | KLHL14 activity raises CACHD1's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.55× lower at baseline in the lines without KLHL14 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55 |
| [[IL27RA]] | C | IL27RA activity raises CACHD1's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without IL27RA | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | CACHD1 activity raises FAM169A's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without CACHD1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[GPHN]] | B | CACHD1 activity raises GPHN's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without CACHD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[ARPC1A]] | B | CACHD1 activity lowers ARPC1A's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.60× higher at baseline in the lines without CACHD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[ZFHX2]] | B | CACHD1 activity raises ZFHX2's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without CACHD1 | 0.041 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[GCFC2]] | B | CACHD1 activity raises GCFC2's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without CACHD1 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[ANKRD18A]] | B | CACHD1 activity raises ANKRD18A's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without CACHD1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[BCL2]] | B | CACHD1 activity raises BCL2's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 3.14× lower at baseline in the lines without CACHD1 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.0, 6.6); signed map (23.5, -35.0). **Vector** length 103, 24.8% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +28.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +12.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +5.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.1 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.0 | +0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -4.4 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | +0.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -2.7 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cache domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:64,470,129-64,693,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1573; previously VWCD1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VU97](https://www.uniprot.org/uniprotkb/Q5VU97) (VWFA and cache domain-containing protein 1):

> Is a regulator of voltage-dependent calcium channels, modulating the activity of T-type calcium channels; it probably forms complexes with Cav3.1 at the cell surface and increases channel open probability. Is also involved in the regulation of Wnt signaling, acting within a ternary complex as scaffold component that bridges FZD5 and LRP6 (By similarity). Plays a role in the regulation of neural progenitor cells proliferation and differentiation.

**Summary**, from NCBI Gene [57685](https://www.ncbi.nlm.nih.gov/gene/57685):

> Predicted to enable voltage-gated calcium channel activity. Predicted to be involved in calcium ion transmembrane transport. Predicted to be located in membrane. Predicted to be part of voltage-gated calcium channel complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29314) · Entrez [57685](https://www.ncbi.nlm.nih.gov/gene/57685) · UniProt [Q5VU97](https://www.uniprot.org/uniprotkb/Q5VU97) · Ensembl [ENSG00000158966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158966)

## Data

Gene col 8206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8206); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8206]; `tensor/DDL_lfc|DDL_z.npy` [8206]; `embed/gene_vectors.npy` [8206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8206 or target_col == 8206). Every well: [[CACHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
