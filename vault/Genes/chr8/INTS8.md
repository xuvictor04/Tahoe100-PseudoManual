---
symbol: "INTS8"
type: "gene"
col: 9038
ensembl_id: "ENSG00000164941"
name: "integrator complex subunit 8"
location: "8q22.1"
module: 15
arm: "+"
pooled_cpm: 51.36
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# INTS8

*integrator complex subunit 8* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +17.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.578× (z -14.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD8]] (+0.65, fdr 1e-05), [[PRPSAP2]] (+0.61, fdr 1e-05), [[ASH2L]] (+0.61, fdr 3e-05); moves opposite to [[ADNP2]] (-0.56, fdr 7e-05), [[C16orf95]] (-0.53, fdr 3e-05), [[PITPNB]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +17.1 | 0e+00 | 43/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.9 | 3e-30 | 40/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +9.1 | 2e-17 | 24/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.0 | 4e-17 | 34/49 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +8.0 | 1e-13 | 33/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +7.2 | 5e-11 | 29/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +6.8 | 7e-10 | 29/48 (A498, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +6.4 | 1e-08 | 26/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +5.2 | 1e-05 | 20/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +5.2 | 1e-05 | 22/48 (J82, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 22/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.21×** | +5.0 | 3e-05 | 15/47 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +4.2 | 0.001 | 15/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.004 | 8/48 (A-172, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | 1.17× | +3.8 | 0.005 | 20/47 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 15/47 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.017 | 8/48 (RKO, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.031 | 7/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.033 | 8/48 (A-172, SW48, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.082 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.578×** | -14.7 | 0e+00 | 45/48 (SW480, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -8.8 | 3e-16 | 34/47 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.757×** | -7.0 | 7e-10 | 25/44 (NCI-H23, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.625×** | -6.6 | 6e-09 | 27/49 (CHP-212, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.629×** | -6.5 | 8e-09 | 20/38 (NCI-H1573, C32, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | **0.801×** | -6.0 | 2e-07 | 23/47 (NCI-H460, SW48, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.863× | -5.7 | 1e-06 | 14/48 (A549, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.834× | -4.3 | 0.002 | 19/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.849× | -4.2 | 0.002 | 14/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.004 | 19/48 (C32, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.040 | 9/48 (H4, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.876× | -3.3 | 0.052 | 11/47 (NCI-H460, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.2 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.471× (z -9.6) |
| [[SW480 (line)]] | alt | 53.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.3) | [[Auranofin (drug)]] 5 µM 0.272× (z -18.7) |
| [[A498 (line)]] | wt | 68.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.351× (z -11.8) ⚠ toxic |
| [[C32 (line)]] | wt | 43.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.340× (z -9.0) |
| [[HOP62 (line)]] | alt | 42.7 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.398× (z -10.0) |
| [[A-427 (line)]] | wt | 46.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.64× (z +9.3) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.201× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 58.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.413× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 67.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.0) | [[TAK-901 (drug)]] 0.05 µM 0.442× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 79.1 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.163× (z -11.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 64.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -8.8) |
| [[SNU-423 (line)]] | alt | 34.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.389× (z -8.6) |
| [[SW48 (line)]] | wt | 43.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.188× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[A-172 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 40.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 62.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.6) | — |
| [[J82 (line)]] | alt | 48.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 104 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.9) | — |
| [[SW 1271 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.383× (z -9.0) |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD8]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PRPSAP2]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ASH2L]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[DRAM2]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[TAF15]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TMED8]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[UQCRC2]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[B4GALT4]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TRAPPC13]] | +0.55 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[ARMC1]] | +0.54 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TGDS]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADNP2]] | -0.56 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[C16orf95]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PITPNB]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[RABGAP1L]] | -0.49 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CDK14]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[KLRG1]] | -0.48 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[RASAL2]] | -0.48 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[FMN1]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[HERPUD2-AS1]] | -0.48 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[DUSP2]] | -0.47 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[BAIAP2-DT]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[LINC00205]] | -0.47 | -0.29 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INTS8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.288). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.2, 17.9); signed map (-2.3, 3.8). **Vector** length 86.6, 18.9% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +17.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.4 | +5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.4 | -14.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -7.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.8 | +8.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,813,311-94,881,746 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20530, INT8, MGC131633; previously C8orf52 |
| Gene groups (HGNC) | Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q75QN2](https://www.uniprot.org/uniprotkb/Q75QN2) (Integrator complex subunit 8):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [55656](https://www.ncbi.nlm.nih.gov/gene/55656):

> This gene encodes a subunit of the Integrator complex which is involved in the cleavage of small nuclear RNAs U1 and U2 within the nucleus. The encoded protein associates with RNA polymerase II and is recruited to the U1 and U2 small nuclear RNA genes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:26048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26048) · Entrez [55656](https://www.ncbi.nlm.nih.gov/gene/55656) · UniProt [Q75QN2](https://www.uniprot.org/uniprotkb/Q75QN2) · Ensembl [ENSG00000164941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164941)

## Data

Gene col 9038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9038); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9038]; `tensor/DDL_lfc|DDL_z.npy` [9038]; `embed/gene_vectors.npy` [9038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9038 or target_col == 9038). Every well: [[INTS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
