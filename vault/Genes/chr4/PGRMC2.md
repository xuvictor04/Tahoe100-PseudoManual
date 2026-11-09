---
symbol: "PGRMC2"
type: "gene"
col: 8842
ensembl_id: "ENSG00000164040"
name: "progesterone receptor membrane component 2"
location: "4q28.2"
module: 164
arm: "+"
pooled_cpm: 72.7
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# PGRMC2

*progesterone receptor membrane component 2* — 4q28.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.26× (z +4.9, q 4e-04, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -27.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VKORC1]] (+0.66, fdr 1e-05), [[SLC35E1]] (+0.62, fdr 9e-06), [[SDHAF1]] (+0.61, fdr 2e-05); moves opposite to [[PRDM11]] (-0.54, fdr 3e-05), [[GCFC2]] (-0.53, fdr 4e-05), [[SMCO2]] (-0.51, fdr 4e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CA12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 4e-04 | 26/48 (A-427, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.004 | 22/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.022 | 16/48 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~14% of this change | 1.19× | +3.8 | 0.022 | 21/48 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.022 | 14/48 (HOP62, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.18× | +3.6 | 0.027 | 18/48 (NCI-H2030, SW48, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.027 | 17/47 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.044 | 19/47 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.086 | 20/48 (SW480, RKO, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.11 | 15/49 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.11 | 13/48 (HOP62, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.395×** | -27.6 | 0e+00 | 48/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.493×** | -14.3 | 6e-44 | 46/48 (MIA PaCa-2, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -12.7 | 1e-34 | 32/42 (HCT15, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -11.6 | 8e-29 | 44/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -9.7 | 3e-20 | 39/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.634×** | -8.8 | 9e-17 | 32/45 (C-33 A, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.684×** | -8.0 | 1e-13 | 32/49 (RKO, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -7.9 | 2e-13 | 36/48 (SW 900, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.676×** | -7.8 | 6e-13 | 39/48 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -7.7 | 6e-13 | 32/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -6.9 | 2e-10 | 31/48 (HCT15, LS 180, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.719×** | -6.9 | 2e-10 | 33/48 (SW 900, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.579×** | -5.6 | 1e-06 | 25/36 (HT-29, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.596×** | -5.3 | 5e-06 | 29/45 (H4, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.821×** | -4.1 | 0.001 | 24/48 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.776×** | -3.8 | 0.005 | 19/49 (C32, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.006 | 19/48 (COLO 205, HCT15, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -3.2 | 0.047 | 19/48 (NCI-H460, C32, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.859× | -3.0 | 0.068 | 16/47 (SNU-423, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 96.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -27.1) |
| [[SW 900 (line)]] | alt | 102 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -23.9) |
| [[A498 (line)]] | wt | 170 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -17.8) |
| [[HOP62 (line)]] | alt | 79.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -26.9) |
| [[A-172 (line)]] | wt | 131 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -22.8) |
| [[C32 (line)]] | wt | 75.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.8) |
| [[H4 (line)]] | wt | 109 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 65.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 96.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -17.5) |
| [[PANC-1 (line)]] | alt | 69.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -18.6) |
| [[AsPC-1 (line)]] | alt | 50.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -17.4) |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.7) |
| [[C-33 A (line)]] | alt | 96.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -15.2) |
| [[HCT15 (line)]] | alt | 99.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0719× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.2) |
| [[HS-578T (line)]] | alt | 75.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -16.9) |
| [[HT-29 (line)]] | alt | 68.4 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0787× (z -13.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.447× (z -12.5) |
| [[LoVo (line)]] | wt | 43.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.9) |
| [[LS 180 (line)]] | wt | 73.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 69.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 83.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 92.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -15.1) |
| [[A-427 (line)]] | wt | 54.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 66.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -15.6) |
| [[Hs 766T (line)]] | wt | 65.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.1) |
| [[J82 (line)]] | alt | 87.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -17.7) |
| [[KATO III (line)]] | alt | 64.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 59.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 83.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -40.0) |
| [[NCI-H2030 (line)]] | alt | 55.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 50.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.9) |
| [[RKO (line)]] | wt | 56.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.2) |
| [[A549 (line)]] | wt | 61.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 78.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -20.6) |
| [[CHP-212 (line)]] | wt | 95.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -12.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 61.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 63.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 52.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.1) |
| [[SNU-1 (line)]] | wt | 62.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -13.6) |
| [[SNU-423 (line)]] | alt | 88.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.0) |
| [[SW 1271 (line)]] | alt | 80.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -9.3) |
| [[SW48 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -9.1) |
| [[AN3 CA (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1]] | +0.66 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SLC35E1]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[SDHAF1]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TTC9C]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[AKR7A2]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.59 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[RNASE4]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MLLT3]] | +0.58 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[USP37]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TBC1D20]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TMUB1]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM11]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GCFC2]] | -0.53 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[SMCO2]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SFPQ]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[EWSR1]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MUTYH]] | -0.50 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[SLC4A3]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[DLG5]] | -0.49 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[MAP4K4]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA12]] | B | CA12 activity raises PGRMC2's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without CA12 | 0.016 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[PLOD2]] | B | PLOD2 activity raises PGRMC2's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without PLOD2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.1, -20.2); signed map (-38.6, 18.2). **Vector** length 114, 32.5% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +3.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.1 | -12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.3 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.9 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.3 | -27.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | +0.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | progesterone receptor membrane component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.2 — chr4:128,269,237-128,288,829 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMBP, DG6 |
| Gene groups (HGNC) | Membrane associated progesterone receptor family; Cytochrome b5 domain containing |
| Reactome | 11 pathways, smallest: Heme signaling; RHOD GTPase cycle; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O15173](https://www.uniprot.org/uniprotkb/O15173) (Membrane-associated progesterone receptor component 2):

> Required for the maintenance of uterine histoarchitecture and normal female reproductive lifespan (By similarity). May serve as a universal non-classical progesterone receptor in the uterus (Probable). Intracellular heme chaperone required for delivery of labile, or signaling heme, to the nucleus (By similarity). Plays a role in adipocyte function and systemic glucose homeostasis. In brown fat, which has a high demand for heme, delivery of labile heme in the nucleus regulates the activity of …

**Summary**, from NCBI Gene [10424](https://www.ncbi.nlm.nih.gov/gene/10424):

> Enables heme binding activity. Involved in adipose tissue development. Located in endoplasmic reticulum and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16089) · Entrez [10424](https://www.ncbi.nlm.nih.gov/gene/10424) · UniProt [O15173](https://www.uniprot.org/uniprotkb/O15173) · Ensembl [ENSG00000164040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164040)

## Data

Gene col 8842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8842); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8842]; `tensor/DDL_lfc|DDL_z.npy` [8842]; `embed/gene_vectors.npy` [8842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8842 or target_col == 8842). Every well: [[PGRMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGRMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
