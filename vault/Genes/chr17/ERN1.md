---
symbol: "ERN1"
type: "gene"
col: 10942
ensembl_id: "ENSG00000178607"
name: "endoplasmic reticulum to nucleus signaling 1"
location: "17q23.3"
module: 81
arm: "+"
pooled_cpm: 93.97
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 20
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ERN1

*endoplasmic reticulum to nucleus signaling 1* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +10.3, q 6e-22, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.466× (z -10.5, q 5e-23, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.435× (z -6.5, q 1e-08, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIT1]] (+0.64, fdr 1e-05), [[SLC9A1]] (+0.63, fdr 1e-05), [[STK40]] (+0.63, fdr 7e-06); moves opposite to [[KCTD3]] (-0.58, fdr 1e-05), [[GTF2I]] (-0.54, fdr 1e-05), [[NDUFA9]] (-0.53, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DZIP1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +10.3 | 6e-22 | 34/49 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +9.3 | 3e-18 | 33/48 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +8.4 | 9e-15 | 30/48 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.64×** | +7.4 | 2e-11 | 37/48 (Panc 03.27, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.1 | 2e-10 | 28/48 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.39×** | +6.9 | 5e-10 | 38/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.54×** | +6.4 | 1e-08 | 36/47 (HCT15, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +5.9 | 2e-07 | 26/48 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.5 | 2e-06 | 26/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 2e-04 | 29/48 (KATO III, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 6e-04 | 25/48 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 9e-04 | 26/48 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.3 | 9e-04 | 23/48 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.1 | 0.002 | 26/48 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.004 | 24/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.016 | 22/48 (LoVo, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.466×** | -10.5 | 5e-23 | 35/44 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -10.0 | 5e-21 | 31/41 (HT-29, A-427, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.513×** | -9.9 | 6e-21 | 34/48 (HT-29, A-427, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -6.5 | 1e-08 | 38/49 (HT-29, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.447×** | -6.3 | 4e-08 | 33/47 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.647×** | -6.2 | 4e-08 | 30/47 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.659×** | -6.2 | 4e-08 | 30/48 (SW1417, HT-29, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -5.9 | 2e-07 | 28/48 (NCI-H1573, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.688×** | -5.6 | 2e-06 | 31/49 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.789×** | -5.0 | 4e-05 | 30/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.706×** | -4.8 | 8e-05 | 26/48 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.724×** | -4.4 | 4e-04 | 26/47 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -4.3 | 6e-04 | 22/48 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.005 | 22/47 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.624×** | -3.7 | 0.009 | 24/46 (H4, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.019 | 19/47 (SHP-77, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.852× | -3.4 | 0.027 | 21/48 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.793×** | -3.3 | 0.035 | 20/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.036 | 19/49 (HepG2/C3A, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.805×** | -3.1 | 0.051 | 18/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 303 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0918× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.113× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 6 (3 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.309× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 83.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 206 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 224 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.8) |
| [[KATO III (line)]] | alt | 159 | 1 | 3 (3 ⚠) | [[Artesunate (drug)]] 5 µM 2.30× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0768× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +18.4) | — |
| [[SW480 (line)]] | alt | 120 | 1 | 3 (3 ⚠) | [[Artesunate (drug)]] 5 µM 1.99× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 66.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 63.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +19.2) | — |
| [[C32 (line)]] | wt | 42.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 87.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 91.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -12.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 92.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 48.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -19.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +16.0) | — |
| [[hTERT-HPNE (line)]] | wt | 153 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 49.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 73.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 44.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +14.1) | — |
| [[A-172 (line)]] | wt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 56.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 380 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.8) | — |
| [[NCI-H596 (line)]] | alt | 102 | 1 | 0 | [[Methylthiouracil (drug)]] 0.05 µM 4.07× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 191 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.332× (z -8.5) |
| [[BT-474 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIT1]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[SLC9A1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[STK40]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ARG2]] | +0.62 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ADAMTSL4-AS2]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TPBG]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[UPP1]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[USE1]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PDE2A]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MCL1]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 | STRING 471 |
| [[CCNYL1]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.58 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[GTF2I]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NDUFA9]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[HADH]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[HSF2]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SMG7]] | -0.50 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[NDUFAF5]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ARHGAP17]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[KDM1A]] | -0.49 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TNRC6A]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[RFX7]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MRPL16]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DZIP1L]] | B | DZIP1L activity lowers ERN1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.18× higher at baseline in the lines without DZIP1L | 0.070 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ERN1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, -7.1); signed map (-2.0, 29.9). **Vector** length 141, 46.8% of its response variance represented; |z| ≥ 3 in 1,636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +7.6 | +6.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.8 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.4 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.3 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.3 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -6.8 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.8 | -4.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -6.2 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -6.5 |
|  | [[NG25 (drug)]] 5 µM |  | -5.9 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.8 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum to nucleus signaling 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,039,080-64,130,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRE1, IRE1P |
| Gene groups (HGNC) | Endoribonucleases; Endoplasmic reticulum to nucleus signaling family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 4 pathways, smallest: IRE1alpha activates chaperones; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O75460](https://www.uniprot.org/uniprotkb/O75460) (Serine/threonine-protein kinase/endoribonuclease IRE1):

> Serine/threonine-protein kinase and endoribonuclease that acts as a key sensor for the endoplasmic reticulum unfolded protein response (UPR). In unstressed cells, the endoplasmic reticulum luminal domain is maintained in its inactive monomeric state by binding to the endoplasmic reticulum chaperone HSPA5/BiP. Accumulation of misfolded proteins in the endoplasmic reticulum causes release of HSPA5/BiP, allowing the luminal domain to homodimerize, promoting autophosphorylation of the kinase domain …

**Summary**, from NCBI Gene [2081](https://www.ncbi.nlm.nih.gov/gene/2081):

> This gene encodes the transmembrane protein kinase inositol-requiring enzyme 1. The encoded protein contains two functional catalytic domains, a serine/threonine-protein kinase domain and an endoribonuclease domain. This protein functions as a sensor of unfolded proteins in the endoplasmic reticulum (ER) and triggers an intracellular signaling pathway termed the unfolded protein response (UPR). The UPR is an ER stress response that is conserved from yeast to mammals and activates genes involved …

**Accessions** — [HGNC:3449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3449) · Entrez [2081](https://www.ncbi.nlm.nih.gov/gene/2081) · UniProt [O75460](https://www.uniprot.org/uniprotkb/O75460) · Ensembl [ENSG00000178607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178607)

## Data

Gene col 10942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10942); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10942]; `tensor/DDL_lfc|DDL_z.npy` [10942]; `embed/gene_vectors.npy` [10942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10942 or target_col == 10942). Every well: [[ERN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
