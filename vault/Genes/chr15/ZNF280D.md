---
symbol: "ZNF280D"
type: "gene"
col: 6087
ensembl_id: "ENSG00000137871"
name: "zinc finger protein 280D"
location: "15q21.3"
module: 51
arm: "+"
pooled_cpm: 40.24
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ZNF280D

*zinc finger protein 280D* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Filgotinib (drug)]] 5 µM: 1.34× (z +4.5, q 0.005, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.349× (z -16.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIS3L]] (+0.78, fdr 7e-06), [[YTHDC2]] (+0.74, fdr 7e-06), [[CC2D2A]] (+0.73, fdr 7e-06); moves opposite to [[MYO9B]] (-0.71, fdr 7e-06), [[CORO7]] (-0.67, fdr 2e-05), [[DNAJC5]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +4.5 | 0.005 | 23/48 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.064 | 15/48 (A549, PANC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.30×** | +3.5 | 0.064 | 15/49 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.064 | 21/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.064 | 15/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.070 | 20/48 (KATO III, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.090 | 22/48 (A-427, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.11 | 18/47 (A549, A-172, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.1 | 0.11 | 11/48 (NCI-H460, A549, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.47× | +3.1 | 0.11 | 10/49 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.349×** | -16.0 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -15.9 | 0e+00 | 44/48 (A498, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.365×** | -15.3 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.390×** | -14.3 | 2e-44 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.504×** | -10.4 | 2e-23 | 42/48 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.581×** | -8.2 | 2e-14 | 37/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -7.8 | 6e-13 | 32/48 (C32, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -6.9 | 3e-10 | 40/49 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.667×** | -5.9 | 2e-07 | 25/48 (HEC-1-A, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.647×** | -5.8 | 3e-07 | 35/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -5.3 | 7e-06 | 28/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.716×** | -4.9 | 5e-05 | 27/48 (SW48, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.728×** | -4.8 | 6e-05 | 25/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 1e-04 | 30/48 (C32, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.001 | 24/48 (AN3 CA, C32, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.625×** | -3.7 | 0.006 | 18/48 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.757×** | -3.7 | 0.006 | 23/48 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.6 | 0.010 | 14/48 (HT-29, C32, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.667×** | -3.2 | 0.035 | 22/48 (SW1417, J82, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.8 | 0 | 11 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 70.6 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 63.6 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 46.6 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -16.2) |
| [[C32 (line)]] | wt | 69.0 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.147× (z -12.2) |
| [[LoVo (line)]] | wt | 45.5 | 0 | 5 | — | [[Belinostat (drug)]] 0.5 µM 0.262× (z -13.9) |
| [[LS 180 (line)]] | wt | 56.7 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 39.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.256× (z -10.2) |
| [[SNU-1 (line)]] | wt | 65.8 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -14.0) |
| [[A549 (line)]] | wt | 59.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 38.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.7) |
| [[A498 (line)]] | wt | 55.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -14.5) |
| [[C-33 A (line)]] | alt | 63.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0832× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 37.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -13.8) |
| [[SW48 (line)]] | wt | 45.4 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -12.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -8.8) |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 2 | — | [[Isocorydine (drug)]] 0.5 µM 0.0462× (z -13.4) |
| [[H4 (line)]] | wt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.3) |
| [[KATO III (line)]] | alt | 34.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.308× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 42.3 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.320× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 34.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -11.1) |
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -9.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.234× (z -10.3) |
| [[SNU-423 (line)]] | alt | 33.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -10.0) |
| [[SW 900 (line)]] | alt | 38.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.5) |
| [[A-172 (line)]] | wt | 40.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.2) |
| [[A-427 (line)]] | wt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 71.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.5) |
| [[COLO 205 (line)]] | alt | 56.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.7) |
| [[HCT15 (line)]] | alt | 47.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -8.6) |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 55.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.8) |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L]] | +0.78 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[YTHDC2]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[CC2D2A]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[TIA1]] | +0.71 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[GCFC2]] | +0.68 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[NFYC]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.67 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[UBQLN2]] | +0.67 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[FUBP1]] | +0.67 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ZNF260]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 | same gene group |
| [[SREK1]] | +0.66 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.66 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | -0.71 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[CORO7]] | -0.67 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC5]] | -0.66 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[IGSF8]] | -0.66 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[MTMR14]] | -0.66 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[LRRC8A]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[TRPT1]] | -0.64 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[MED26]] | -0.64 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.64 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | -0.63 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[TPST2]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-19.1, 4.5); signed map (10.2, -33.9). **Vector** length 101, 28.0% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | -0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -16.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -15.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 280D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:56,630,176-56,734,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20086, ZNF634; previously SUHW4 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6N043](https://www.uniprot.org/uniprotkb/Q6N043) (Zinc finger protein 280D):

> May function as a transcription factor.

**Summary**, from NCBI Gene [54816](https://www.ncbi.nlm.nih.gov/gene/54816):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25953) · Entrez [54816](https://www.ncbi.nlm.nih.gov/gene/54816) · UniProt [Q6N043](https://www.uniprot.org/uniprotkb/Q6N043) · Ensembl [ENSG00000137871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137871)

## Data

Gene col 6087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6087); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6087]; `tensor/DDL_lfc|DDL_z.npy` [6087]; `embed/gene_vectors.npy` [6087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6087 or target_col == 6087). Every well: [[ZNF280D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF280D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
