---
symbol: "VGF"
type: "gene"
col: 4892
ensembl_id: "ENSG00000128564"
name: "VGF nerve growth factor inducible"
location: "7q22.1"
module: 109
arm: "+"
pooled_cpm: 62.42
n_lines_expressing: 18
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# VGF

*VGF nerve growth factor inducible* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.82× (z +21.3, q 0e+00, up in 12 of 15 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 4.16× (z +11.2, q 8e-27, up in 12 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.561× (z -6.3, q 2e-07, down in 11 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER2]] (+0.61, fdr 8e-06), [[SCG3]] (+0.61, fdr 4e-05), [[EGR3]] (+0.59, fdr 1e-05); moves opposite to [[DRAM2]] (-0.53, fdr 4e-05), [[FHIP2A]] (-0.52, fdr 4e-05), [[BMPR1A]] (-0.52, fdr 1e-04).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[HRH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **6.82×** | +21.3 | 0e+00 | 12/15 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.12×** | +12.8 | 4e-35 | 12/15 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.16×** | +11.2 | 8e-27 | 12/15 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.94×** | +10.8 | 8e-25 | 14/16 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.93×** | +10.3 | 6e-23 | 11/15 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.60×** | +10.1 | 8e-22 | 15/16 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.67×** | +9.8 | 8e-21 | 9/11 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.26×** | +8.6 | 7e-16 | 8/12 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.61×** | +7.5 | 3e-12 | 11/15 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +7.3 | 2e-11 | 12/16 (SW1417, SW480, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.18×** | +6.1 | 5e-08 | 9/15 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +6.0 | 7e-08 | 13/16 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **2.01×** | +5.5 | 2e-06 | 10/15 (SW 900, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +4.9 | 3e-05 | 9/15 (SW480, SW1417, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.86×** | +4.9 | 4e-05 | 10/16 (SW1417, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +4.3 | 6e-04 | 8/16 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.007 | 6/15 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.61×** | +3.5 | 0.016 | 11/15 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.97×** | +3.4 | 0.018 | 3/15 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.020 | 6/16 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.022 | 8/17 (SW1417, CHP-212, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.033 | 7/15 (SHP-77, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4892.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.561×** | -6.3 | 2e-07 | 11/16 (SHP-77, SW480, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.499×** | -5.2 | 5e-05 | 13/18 (SHP-77, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.495×** | -5.1 | 6e-05 | 13/15 (SHP-77, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.653×** | -3.9 | 0.012 | 11/16 (SHP-77, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.613×** | -3.7 | 0.025 | 10/15 (SHP-77, H4, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.679×** | -3.6 | 0.026 | 11/16 (SHP-77, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.646×** | -3.5 | 0.033 | 11/17 (SHP-77, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.736×** | -3.3 | 0.057 | 10/17 (SHP-77, C32, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.665×** | -3.2 | 0.083 | 5/16 (LOX-IMVI, C32, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.671×** | -3.1 | 0.097 | 10/15 (SK-MEL-2, SHP-77, …) | rises with dose | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.678× | -3.1 | 0.12 | 7/16 (C32, SHP-77, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.6 | 12 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.2× (z +25.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 43.1× (z +19.0) | — |
| [[SW480 (line)]] | alt | 24.6 | 9 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 15.5× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 174 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Bortezomib (drug)]] 0.05 µM 0.103× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.170× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +17.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 10.2× (z +11.3) | — |
| [[C32 (line)]] | wt | 1,696 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.06× (z +8.7) | [[Bortezomib (drug)]] 0.05 µM 0.0992× (z -13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.187× (z -10.2) |
| [[SHP-77 (line)]] | alt | 891 | 0 | 4 | — | [[Binimetinib (drug)]] 0.05 µM 0.275× (z -10.7) |
| [[SW1417 (line)]] | alt | 118 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +12.3) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.67× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +16.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 7.04× (z +9.1) | — |
| [[A-427 (line)]] | wt | 25.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.20× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +11.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[H4 (line)]] | wt | 49.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +15.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 9.41 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.87 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.56 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SCG3]] | +0.61 | +0.55 / +0.41 | both halves | 4e-05 | same gene group; pathway: Post-translational protein phosphorylation; STRING 661 |
| [[EGR3]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 | pathway: NGF-stimulated transcription |
| [[EGR1]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 | pathway: NGF-stimulated transcription; STRING 836 |
| [[CHGB]] | +0.58 | +0.42 / +0.52 | both halves | 4e-05 | same gene group; pathway: Post-translational protein phosphorylation; STRING 698 |
| [[EGR2]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 | pathway: NGF-stimulated transcription |
| [[ARC]] | +0.57 | +0.54 / +0.45 | both halves | 3e-05 | pathway: NGF-stimulated transcription |
| [[CSRNP1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ITGA3]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MCL1]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.55 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SYN1]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAM2]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[FHIP2A]] | -0.52 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[BMPR1A]] | -0.52 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[MACROH2A2]] | -0.52 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CRYAB]] | -0.51 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[UBE4B]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ELMOD3]] | -0.49 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[SOS1]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[SMO]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[KIF13A]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ZCCHC8]] | -0.46 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[SULT1A1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises VGF's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds |
| [[NT5E]] | B | NT5E activity lowers VGF's level | lines that do not express NT5E (14) vs lines expressing it (36) | 1.89× higher at baseline in the lines without NT5E | 0.017 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[MAP2K2]] | B | MAP2K2 activity raises VGF's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SCG3]] | C | SCG3 activity raises VGF's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 5.53× lower at baseline in the lines without SCG3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[CRYAB]] | C | CRYAB activity raises VGF's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 2.77× lower at baseline in the lines without CRYAB | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP; co-absent with the target |
| [[CHGB]] | C | CHGB activity raises VGF's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without CHGB | 0.052 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HRH1]] | B | VGF activity lowers HRH1's level | lines that do not express VGF (32) vs lines expressing it (18) | 1.70× higher at baseline in the lines without VGF | 0.023 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3 |
| [[HRH1]] | B | VGF activity weakens HRH1's drug response | lines that do not express VGF (27) vs lines expressing it (12) | the lines without VGF respond 1.74× as strongly (z diff -2.52); strongest at Dinaciclib 0.05 µM: 0.41x vs 0.75x (z diff -4.5) | 0.039 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; target measured in part of the lines; artifact flags |
| [[NPTX2]] | B | VGF activity strengthens NPTX2's drug response | lines that do not express VGF (12) vs lines expressing it (7) | the lines without VGF respond 0.78× as strongly (z diff +1.31); strongest at Dinaciclib 5 µM: 1.52x vs 12x (z diff +7.4) | 0.059 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; target measured in part of the lines; artifact flags |
| [[ARC]] | B | VGF activity raises ARC's level | lines that do not express VGF (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without VGF | 0.081 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3 |
| [[MYL12A]] | B | VGF activity strengthens MYL12A's drug response | lines that do not express VGF (32) vs lines expressing it (17) | the lines without VGF respond 1.01× as strongly (z diff +0.59); strongest at Cobimetinib 5 µM: 0.67x vs 0.56x (z diff +1.5) | 0.097 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; target measured in part of the lines; artifact flags |
| [[SCG3]] | C | VGF activity raises SCG3's level | lines that do not express VGF (32) vs lines expressing it (18) | 2.74× lower at baseline in the lines without VGF | 0.010 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; co-absent with the target |
| [[CHGB]] | C | VGF activity raises CHGB's level | lines that do not express VGF (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without VGF | 0.018 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; co-absent with the target |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, 34.5); signed map (7.4, 30.2). **Vector** length 59.4, 17.3% of its response variance represented; |z| ≥ 3 in 517 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.0 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.8 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.4 | +21.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.3 | +9.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | -1.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | VGF nerve growth factor inducible |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,162,509-101,165,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCG7, SgVII |
| Gene groups (HGNC) | Granins |
| Reactome | 7 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15240](https://www.uniprot.org/uniprotkb/O15240) (Neurosecretory protein VGF):

> [Neurosecretory protein VGF]: Secreted polyprotein that is packaged and proteolytically processed by prohormone convertases PCSK1 and PCSK2 in a cell-type-specific manner (By similarity). VGF and peptides derived from its processing play many roles in neurogenesis and neuroplasticity associated with learning, memory, depression and chronic pain (By similarity).; [Neuroendocrine regulatory peptide-1]: Plays a role in the control of body fluid homeostasis by regulating vasopressin release. …

**Summary**, from NCBI Gene [7425](https://www.ncbi.nlm.nih.gov/gene/7425):

> This gene is specifically expressed in a subpopulation of neuroendocrine cells, and is upregulated by nerve growth factor. The structural organization of this gene is similar to that of the rat gene, and both the translated and the untranslated regions show a high degree of sequence similarity to the rat gene. The encoded secretory protein also shares similarities with the secretogranin/chromogranin family, however, its exact function is not known. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12684) · Entrez [7425](https://www.ncbi.nlm.nih.gov/gene/7425) · UniProt [O15240](https://www.uniprot.org/uniprotkb/O15240) · Ensembl [ENSG00000128564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128564)

## Data

Gene col 4892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4892); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4892]; `tensor/DDL_lfc|DDL_z.npy` [4892]; `embed/gene_vectors.npy` [4892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4892 or target_col == 4892). Every well: [[VGF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VGF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
