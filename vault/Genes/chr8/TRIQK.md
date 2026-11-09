---
symbol: "TRIQK"
type: "gene"
col: 12950
ensembl_id: "ENSG00000205133"
name: "triple QxxK/R motif containing"
location: "8q22.1"
module: 56
arm: "+"
pooled_cpm: 54.82
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 51
n_dd_up_clean: 8
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TRIQK

*triple QxxK/R motif containing* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Rifaximin (drug)]] 5 µM: 1.29× (z +4.3, q 0.010, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.201× (z -39.9, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D23]] (+0.57, fdr 1e-05), [[SNHG18]] (+0.55, fdr 1e-05), [[ATF2]] (+0.54, fdr 3e-05); moves opposite to [[MDFI]] (-0.55, fdr 3e-05), [[ZNF562]] (-0.51, fdr 2e-05), [[PLEKHN1]] (-0.50, fdr 5e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.010 | 20/46 (A549, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.27×** | +4.1 | 0.010 | 19/46 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.023 | 20/46 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.023 | 16/46 (KATO III, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.034 | 16/45 (SW480, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.038 | 17/46 (KATO III, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.038 | 13/46 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.039 | 19/45 (SW480, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.045 | 16/46 (LS 180, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.045 | 15/46 (A-427, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.045 | 17/46 (SW480, HOP62, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.21×** | +3.3 | 0.050 | 12/45 (NCI-H1573, A549, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.2 | 0.060 | 4/46 (HOP62, SHP-77, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.072 | 12/46 (SW480, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.078 | 11/47 (SW480, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.080 | 13/46 (HOP62, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.201×** | -39.9 | 0e+00 | 42/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.253×** | -24.2 | 0e+00 | 38/45 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.239×** | -24.2 | 0e+00 | 42/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.297×** | -21.3 | 0e+00 | 43/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.318×** | -20.2 | 0e+00 | 41/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.362×** | -17.9 | 0e+00 | 42/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.406×** | -15.8 | 0e+00 | 42/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.412×** | -15.6 | 0e+00 | 42/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.412×** | -15.6 | 0e+00 | 43/46 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.437×** | -14.5 | 0e+00 | 43/46 (A-172, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.244×** | -13.0 | 1e-36 | 41/47 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.491×** | -12.5 | 5e-34 | 39/46 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.515×** | -11.6 | 1e-29 | 37/46 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -11.3 | 4e-28 | 34/46 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.533×** | -11.0 | 1e-26 | 35/46 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.522×** | -10.8 | 2e-25 | 36/46 (BT-474, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.361×** | -9.3 | 2e-19 | 37/46 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.597×** | -9.0 | 5e-18 | 34/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 88.1 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -38.0) |
| [[RPMI-7951 (line)]] | alt | 79.2 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -27.4) |
| [[PANC-1 (line)]] | alt | 51.8 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -32.6) |
| [[H4 (line)]] | wt | 84.6 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0713× (z -28.3) |
| [[HS-578T (line)]] | alt | 112 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -31.2) |
| [[A-172 (line)]] | wt | 59.0 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -25.9) |
| [[NCI-H460 (line)]] | wt | 34.5 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -26.4) |
| [[NCI-H1573 (line)]] | alt | 54.6 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -21.7) |
| [[SW480 (line)]] | alt | 46.0 | 0 | 13 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 79.8 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -30.8) |
| [[NCI-H1792 (line)]] | alt | 55.3 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0530× (z -28.4) |
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.2) |
| [[A498 (line)]] | wt | 133 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -27.6) |
| [[A549 (line)]] | wt | 47.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -26.1) |
| [[BT-474 (line)]] | alt | 93.6 | 0 | 10 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0953× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -14.2) |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.1) |
| [[LS 180 (line)]] | wt | 48.3 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.3) |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -21.9) |
| [[KATO III (line)]] | alt | 41.4 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -20.7) |
| [[Panc 03.27 (line)]] | alt | 45.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -22.5) |
| [[hTERT-HPNE (line)]] | wt | 62.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.7) |
| [[SNU-423 (line)]] | alt | 56.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -22.1) |
| [[SW 900 (line)]] | alt | 57.1 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0803× (z -20.6) |
| [[CFPAC-1 (line)]] | alt | 54.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -20.3) |
| [[J82 (line)]] | alt | 54.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 188 | 5 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.75× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 36.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -17.3) |
| [[COLO 205 (line)]] | alt | 52.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -18.1) |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0701× (z -14.4) |
| [[HepG2_C3A (line)]] | wt | 62.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 40.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -22.3) |
| [[RKO (line)]] | wt | 34.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.1) |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -12.7) |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0539× (z -11.6) |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.8) |
| [[C32 (line)]] | wt | 52.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -15.4) |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -10.1) |
| [[SHP-77 (line)]] | alt | 48.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -8.9) |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0544× (z -12.2) |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D23]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SNHG18]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ATF2]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[COPB1]] | +0.53 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TTC3]] | +0.52 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CBLB]] | +0.52 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[SGCE]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[OSTC]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RAB1A]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[NKTR]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[TMEM167B]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SEC23A]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDFI]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZNF562]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PLEKHN1]] | -0.50 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[PLEKHA6]] | -0.49 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SH3TC2]] | -0.48 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[KIAA1549]] | -0.47 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SRC]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[ZNF83]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TRAF3]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[OSBPL10]] | -0.46 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SH3TC2-DT]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NUP50]] | -0.46 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIQK's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PCSK6]] | B | PCSK6 activity lowers TRIQK's level | lines that do not express PCSK6 (21) vs lines expressing it (29) | 1.62× higher at baseline in the lines without PCSK6 | 0.071 | ⚠ within organs, on part of the lines; also absent: BTNL9, CYP4F12, LINC02964 |
| [[TOP2A]] | B | TOP2A activity raises TRIQK's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers TRIQK's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, -35.4); signed map (-48.1, 10.5). **Vector** length 74.7, 21.6% of its response variance represented; |z| ≥ 3 in 1,629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -9.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -14.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -15.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -15.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | triple QxxK/R motif containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:92,883,532-93,017,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp779L1068, PRO0845, LOC286144; previously C8orf83 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q629K1](https://www.uniprot.org/uniprotkb/Q629K1) (Triple QxxK/R motif-containing protein):

> May play a role in cell growth and maintenance of cell morphology.

**Summary**, from NCBI Gene [286144](https://www.ncbi.nlm.nih.gov/gene/286144):

> Predicted to be located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27828) · Entrez [286144](https://www.ncbi.nlm.nih.gov/gene/286144) · UniProt [Q629K1](https://www.uniprot.org/uniprotkb/Q629K1) · Ensembl [ENSG00000205133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205133)

## Data

Gene col 12950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12950); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12950]; `tensor/DDL_lfc|DDL_z.npy` [12950]; `embed/gene_vectors.npy` [12950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12950 or target_col == 12950). Every well: [[TRIQK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIQK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
