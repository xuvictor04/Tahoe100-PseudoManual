---
symbol: "FBXW4"
type: "gene"
col: 2886
ensembl_id: "ENSG00000107829"
name: "F-box and WD repeat domain containing 4"
location: "10q24.32"
module: 46
arm: "+"
pooled_cpm: 52.26
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# FBXW4

*F-box and WD repeat domain containing 4* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.29× (z +6.8, q 5e-09, up in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.39× (z +6.2, q 2e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.138× (z -36.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF146]] (+0.79, fdr 7e-06), [[DDX59]] (+0.76, fdr 7e-06), [[TSTD3]] (+0.72, fdr 1e-05); moves opposite to [[TNIK]] (-0.66, fdr 1e-05), [[EDA]] (-0.63, fdr 6e-05), [[DCUN1D3]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HYI]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +6.8 | 5e-09 | 30/48 (CFPAC-1, LoVo, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +6.2 | 2e-07 | 29/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 2e-04 | 22/48 (RKO, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 6e-04 | 23/48 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 8e-04 | 23/48 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.29×** | +4.3 | 0.001 | 24/49 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.1 | 0.003 | 10/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 20/48 (NCI-H23, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.006 | 17/49 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.25×** | +3.9 | 0.006 | 13/48 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.008 | 23/47 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.030 | 19/47 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.041 | 18/47 (A498, HepG2/C3A, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.20× | +3.3 | 0.045 | 14/47 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.082 | 11/48 (KATO III, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.138×** | -36.8 | 0e+00 | 48/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.143×** | -36.1 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.185×** | -31.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.382×** | -17.9 | 0e+00 | 46/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.383×** | -17.8 | 0e+00 | 46/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.267×** | -12.9 | 8e-36 | 46/49 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.614×** | -12.8 | 8e-36 | 44/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -10.8 | 2e-25 | 43/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.350×** | -10.2 | 1e-22 | 46/49 (Panc 03.27, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -9.2 | 1e-18 | 34/48 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -9.0 | 1e-17 | 37/48 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.650×** | -7.7 | 6e-13 | 24/40 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -7.4 | 8e-12 | 38/48 (SW48, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.688×** | -6.9 | 2e-10 | 37/48 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.701×** | -6.1 | 4e-08 | 24/44 (C32, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -5.6 | 8e-07 | 31/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.782×** | -4.6 | 1e-04 | 29/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.4 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -28.2) |
| [[C32 (line)]] | wt | 74.6 | 0 | 10 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0772× (z -22.5) |
| [[SNU-423 (line)]] | alt | 61.5 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -22.1) |
| [[NCI-H2030 (line)]] | alt | 80.9 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.185× (z -16.8) |
| [[HOP62 (line)]] | alt | 51.5 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -22.6) |
| [[Panc 03.27 (line)]] | alt | 54.8 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0992× (z -24.0) |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -17.9) |
| [[A-172 (line)]] | wt | 83.6 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -20.7) |
| [[A549 (line)]] | wt | 71.1 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0963× (z -26.2) |
| [[LS 180 (line)]] | wt | 57.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -20.0) |
| [[KATO III (line)]] | alt | 36.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -19.2) |
| [[LoVo (line)]] | wt | 61.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -25.2) |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.0828× (z -21.5) |
| [[NCI-H1573 (line)]] | alt | 96.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -24.7) |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0844× (z -22.5) |
| [[PANC-1 (line)]] | alt | 66.2 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -24.8) |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -16.0) |
| [[SW480 (line)]] | alt | 43.0 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0976× (z -27.2) |
| [[HEC-1-A (line)]] | alt | 69.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -18.7) |
| [[Hs 766T (line)]] | wt | 43.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -18.2) |
| [[HT-29 (line)]] | alt | 42.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -17.8) |
| [[hTERT-HPNE (line)]] | wt | 40.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -15.3) |
| [[J82 (line)]] | alt | 24.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 56.7 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0974× (z -21.4) |
| [[RKO (line)]] | wt | 39.9 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -16.1) |
| [[SW1417 (line)]] | alt | 53.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -19.0) |
| [[A-427 (line)]] | wt | 40.7 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.208× (z -13.9) |
| [[AN3 CA (line)]] | alt | 94.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.138× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 30.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -15.5) |
| [[C-33 A (line)]] | alt | 41.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -13.3) |
| [[H4 (line)]] | wt | 51.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0468× (z -21.7) |
| [[HCT15 (line)]] | alt | 73.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -16.0) |
| [[SNU-1 (line)]] | wt | 54.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0978× (z -15.9) |
| [[SW48 (line)]] | wt | 62.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0976× (z -17.2) |
| [[A498 (line)]] | wt | 46.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -20.1) |
| [[CHP-212 (line)]] | wt | 62.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -10.7) |
| [[COLO 205 (line)]] | alt | 51.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0774× (z -20.2) |
| [[HS-578T (line)]] | alt | 28.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 31.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0968× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -16.1) |
| [[RPMI-7951 (line)]] | alt | 30.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.5) |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.165× (z -13.4) |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -12.0) |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | +0.79 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[DDX59]] | +0.76 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[TSTD3]] | +0.72 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[FAIM]] | +0.71 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[DNAI4]] | +0.70 | +0.53 / +0.37 | both halves | 8e-05 | same gene group |
| [[CCAR1]] | +0.69 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RC3H2]] | +0.68 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RPAP2]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[UNK]] | +0.67 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[KRBOX5]] | +0.66 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[ITPA]] | +0.66 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ATAD2B]] | +0.65 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNIK]] | -0.66 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[EDA]] | -0.63 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[DCUN1D3]] | -0.62 | -0.62 / -0.38 | both halves | 7e-05 | pathway: Neddylation; STRING 499 |
| [[SLC27A1]] | -0.61 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[CALU]] | -0.61 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[FCHO1]] | -0.61 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[KHDRBS1]] | -0.60 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SIPA1]] | -0.60 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[GPRIN1]] | -0.60 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[GNB1L]] | -0.60 | -0.44 / -0.47 | both halves | 3e-05 | same gene group |
| [[ASMTL]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CAMK2G]] | -0.58 | -0.43 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYI]] | B | HYI activity lowers FBXW4's level | lines that do not express HYI (9) vs lines expressing it (41) | 1.42× higher at baseline in the lines without HYI | 0.046 | ⚠ within organs, on part of the lines; also absent: HEIH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.9, 15.6); signed map (24.2, -22.1). **Vector** length 119, 36.9% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +8.6 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.4 | +6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -10.6 | -17.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -10.4 | -12.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -10.1 | -17.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.6 | -6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.6 | -12.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.6 | -9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.9 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,610,664-101,695,295 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fbw4, dactylin; previously SHFM3 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Reactome | 7 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [P57775](https://www.uniprot.org/uniprotkb/P57775) (F-box/WD repeat-containing protein 4):

> Probably recognizes and binds to some phosphorylated proteins and promotes their ubiquitination and degradation. Likely to be involved in key signaling pathways crucial for normal limb development. May participate in Wnt signaling.

**Summary**, from NCBI Gene [6468](https://www.ncbi.nlm.nih.gov/gene/6468):

> This gene is a member of the F-box/WD-40 gene family, which recruit specific target proteins through their WD-40 protein-protein binding domains for ubiquitin mediated degradation. In mouse, a highly similar protein is thought to be responsible for maintaining the apical ectodermal ridge of developing limb buds; disruption of the mouse gene results in the absence of central digits, underdeveloped or absent metacarpal/metatarsal bones and syndactyly. This phenotype is remarkably similar to split …

**Accessions** — [HGNC:10847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10847) · Entrez [6468](https://www.ncbi.nlm.nih.gov/gene/6468) · UniProt [P57775](https://www.uniprot.org/uniprotkb/P57775) · Ensembl [ENSG00000107829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107829)

## Data

Gene col 2886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2886); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2886]; `tensor/DDL_lfc|DDL_z.npy` [2886]; `embed/gene_vectors.npy` [2886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2886 or target_col == 2886). Every well: [[FBXW4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
