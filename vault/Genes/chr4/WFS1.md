---
symbol: "WFS1"
type: "gene"
col: 3056
ensembl_id: "ENSG00000109501"
name: "wolframin ER transmembrane glycoprotein"
location: "4p16.1"
module: 159
arm: "+"
pooled_cpm: 10.76
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# WFS1

*wolframin ER transmembrane glycoprotein* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.20× (z +16.8, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.492× (z -10.3, q 4e-22, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMK2G]] (+0.62, fdr 2e-05), [[UBE2Q2P2-1]] (+0.62, fdr 5e-05), [[LDLRAP1]] (+0.60, fdr 1e-05); moves opposite to [[PCNX4-DT]] (-0.56, fdr 1e-04), [[PATL2]] (-0.56, fdr 2e-04), [[ZNF610]] (-0.56, fdr 4e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.20×** | +16.8 | 0e+00 | 45/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +15.8 | 0e+00 | 42/45 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +13.3 | 8e-38 | 41/46 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.9 | 5e-21 | 12/17 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +9.2 | 3e-18 | 30/43 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +9.0 | 1e-17 | 29/46 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.71×** | +7.8 | 6e-13 | 16/29 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +7.2 | 5e-11 | 24/46 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +6.8 | 7e-10 | 23/45 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.6 | 1e-06 | 20/42 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.8 | 9e-05 | 10/22 (NCI-H23, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 12/46 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.3 | 7e-04 | 9/44 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.005 | 14/46 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.31×** | +3.4 | 0.023 | 9/23 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.025 | 7/43 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.026 | 6/43 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.041 | 3/39 (LoVo, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.072 | 8/41 (A-172, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.492×** | -10.3 | 4e-22 | 31/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -9.6 | 3e-19 | 26/42 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.635×** | -9.3 | 2e-18 | 25/41 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -7.0 | 3e-10 | 18/39 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.619×** | -7.0 | 3e-10 | 19/44 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -7.0 | 3e-10 | 20/44 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -6.3 | 2e-08 | 21/45 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -5.0 | 3e-05 | 15/42 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -5.0 | 4e-05 | 20/37 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.768×** | -3.8 | 0.007 | 14/44 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.609×** | -3.8 | 0.009 | 9/45 (A-172, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.799×** | -3.3 | 0.051 | 5/47 (CHP-212, BT-474, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.668×** | -3.1 | 0.097 | 9/40 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.813× | -3.0 | 0.11 | 9/43 (SW480, AN3 CA, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0968× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.133× (z -8.8) |
| [[A-172 (line)]] | wt | 30.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -19.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -12.5) |
| [[HOP62 (line)]] | alt | 7.67 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.03× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -9.6) |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0868× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0687× (z -10.4) |
| [[SW480 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -10.0) |
| [[A498 (line)]] | wt | 8.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -9.2) |
| [[C-33 A (line)]] | alt | 8.43 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0732× (z -9.3) |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -9.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 6.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0756× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.128× (z -11.1) |
| [[A-427 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | +0.62 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[UBE2Q2P2-1]] | +0.62 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[LDLRAP1]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HDAC11]] | +0.59 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[USP35]] | +0.58 | +0.54 / +0.27 | both halves | 3e-04 |  |
| [[MKRN2]] | +0.56 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[HTT]] | +0.56 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[PRR5]] | +0.55 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[HSPA5]] | +0.55 | +0.53 / +0.35 | both halves | 1e-04 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 429 |
| [[ST6GALNAC4]] | +0.54 | +0.42 / +0.26 | both halves | 4e-04 |  |
| [[EVI5L]] | +0.54 | +0.37 / +0.37 | both halves | 8e-05 |  |
| [[RIMS3]] | +0.54 | +0.42 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | -0.56 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PATL2]] | -0.56 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ZNF610]] | -0.56 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[WAC-AS1]] | -0.55 | -0.42 / -0.20 | both halves | 7e-04 |  |
| [[MAD2L1-DT]] | -0.55 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | -0.54 | -0.42 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[DNAI4]] | -0.54 | -0.44 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[RIPK2-DT]] | -0.54 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | -0.54 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[GTF2H1]] | -0.53 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[DPH6-DT]] | -0.53 | -0.41 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[TBCE-1]] | -0.52 | -0.42 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[PGBD4]] | -0.52 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.52 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.52 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[INO80D]] | -0.52 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.5, 4.5); signed map (-39.4, -6.2). **Vector** length 84.0, 16.3% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +16.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +15.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.1 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[AZD-8055 (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | wolframin ER transmembrane glycoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,269,849-6,303,265 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIDMOAD, WFS; previously DFNA6, DFNA14, DFNA38 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 7 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O76024](https://www.uniprot.org/uniprotkb/O76024) (Wolframin):

> Participates in the regulation of cellular Ca(2+) homeostasis, at least partly, by modulating the filling state of the endoplasmic reticulum Ca(2+) store. Negatively regulates the ER stress response and positively regulates the stability of V-ATPase subunits ATP6V1A and ATP1B1 by preventing their degradation through an unknown proteasome-independent mechanism.

**Summary**, from NCBI Gene [7466](https://www.ncbi.nlm.nih.gov/gene/7466):

> This gene encodes a transmembrane protein, which is located primarily in the endoplasmic reticulum and ubiquitously expressed with highest levels in brain, pancreas, heart, and insulinoma beta-cell lines. Mutations in this gene are associated with Wolfram syndrome, also called DIDMOAD (Diabetes Insipidus, Diabetes Mellitus, Optic Atrophy, and Deafness), an autosomal recessive disorder. The disease affects the brain and central nervous system. Mutations in this gene can also cause autosomal …

**Accessions** — [HGNC:12762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12762) · Entrez [7466](https://www.ncbi.nlm.nih.gov/gene/7466) · UniProt [O76024](https://www.uniprot.org/uniprotkb/O76024) · Ensembl [ENSG00000109501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109501)

## Data

Gene col 3056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3056); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3056]; `tensor/DDL_lfc|DDL_z.npy` [3056]; `embed/gene_vectors.npy` [3056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3056 or target_col == 3056). Every well: [[WFS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WFS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
