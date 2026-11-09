---
symbol: "YWHAH"
type: "gene"
col: 4866
ensembl_id: "ENSG00000128245"
name: "tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein eta"
location: "22q12.3"
module: 123
arm: "+"
pooled_cpm: 54.79
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# YWHAH

*tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein eta* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.61× (z +12.2, q 3e-31, up in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 2.29× (z +10.9, q 2e-25, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.676× (z -7.3, q 2e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHTN1]] (+0.60, fdr 7e-06), [[SPTAN1]] (+0.58, fdr 1e-05), [[DUSP8]] (+0.57, fdr 1e-05); moves opposite to [[ECD]] (-0.54, fdr 1e-05), [[PPIL3]] (-0.50, fdr 4e-05), [[RILPL2]] (-0.50, fdr 2e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SACS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +12.2 | 3e-31 | 31/42 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **2.29×** | +10.9 | 2e-25 | 42/47 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **2.36×** | +10.9 | 2e-25 | 44/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.93×** | +8.7 | 7e-16 | 44/47 (A498, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.80×** | +7.7 | 1e-12 | 44/48 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.51×** | +7.7 | 2e-12 | 33/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +6.4 | 2e-08 | 34/47 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.62×** | +6.3 | 2e-08 | 41/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.61×** | +6.2 | 3e-08 | 36/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 2e-06 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 2e-06 | 36/48 (CFPAC-1, HT-29, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.3 | 5e-06 | 31/47 (COLO 205, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +5.3 | 5e-06 | 32/48 (SW480, LoVo, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.0 | 3e-05 | 28/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.48×** | +4.9 | 3e-05 | 29/47 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +4.8 | 4e-05 | 30/48 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 2e-04 | 26/49 (NCI-H1573, HS-578T, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 8e-04 | 25/48 (HS-578T, NCI-H1573, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.001 | 28/47 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 23/48 (MIA PaCa-2, CFPAC-1, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.018 | 17/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.025 | 18/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.027 | 21/48 (C-33 A, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -7.3 | 2e-10 | 36/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -4.5 | 0.002 | 34/49 (MIA PaCa-2, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -3.8 | 0.033 | 24/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.776× | -3.2 | 0.19 | 20/48 (A-172, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.788× | -3.1 | 0.19 | 18/48 (LS 180, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 82.4 | 6 (2 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.67× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 32.6 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +13.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 3.61× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.7) |
| [[C32 (line)]] | wt | 60.1 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 3.41× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.1) |
| [[LoVo (line)]] | wt | 62.3 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.51× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 54.1 | 2 | 2 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.93× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.3) |
| [[SW480 (line)]] | alt | 52.6 | 4 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.98× (z +10.8) ⚠ toxic · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.82× (z +10.7) | — |
| [[A498 (line)]] | wt | 64.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[CFPAC-1 (line)]] | alt | 44.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.1) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[HT-29 (line)]] | alt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +11.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 41.1 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 6.44× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 84.3 | 1 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.92× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 69.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.17× (z +8.7) | — |
| [[A-427 (line)]] | wt | 63.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.5) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[COLO 205 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +13.3) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.7) |
| [[HOP62 (line)]] | alt | 18.2 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.64× (z +9.4) | — |
| [[KATO III (line)]] | alt | 60.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H1792 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 77.0 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.55× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 51.3 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.23× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.1) |
| [[SNU-1 (line)]] | wt | 89.9 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0996× (z -8.5) |
| [[SNU-423 (line)]] | alt | 40.5 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.63× (z +8.5) | — |
| [[A-172 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHTN1]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SPTAN1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 | pathway: Apoptosis |
| [[DUSP8]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[RHOB]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 | pathway: RHO GTPase Effectors; STRING 531 |
| [[FLII]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PNMA1]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[CD151]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[KLF11]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TUBA1A]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 | pathway: RHO GTPase Effectors; STRING 413 |
| [[L1CAM]] | +0.53 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[ANKRD36C]] | +0.52 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[SNX15]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECD]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PPIL3]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[RILPL2]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[KCNAB2]] | -0.46 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[POM121]] | -0.46 | -0.46 / -0.40 | both halves | 4e-05 | pathway: SARS-CoV-2 Infection |
| [[PDSS2]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TAF11]] | -0.44 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[DISC1]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[EVI2B]] | -0.44 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[MBTD1]] | -0.44 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[SELENOH]] | -0.44 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[TXN2]] | -0.44 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises YWHAH's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without SACS | 0.053 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.425). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.9, -2.3); signed map (-8.6, 28.0). **Vector** length 132, 40.3% of its response variance represented; |z| ≥ 3 in 1,238 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +7.9 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +7.3 | +7.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.1 | +5.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +6.9 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.8 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.7 | +4.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +6.6 | +10.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.4 | +4.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +6.1 | +5.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein eta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:31,944,522-31,957,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously YWHA1 |
| Gene groups (HGNC) | 14-3-3 phospho-serine/phospho-threonine binding proteins |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM, APICAL_JUNCTION |
| Reactome | 29 pathways, smallest: SARS-CoV-2 targets host intracellular signalling and regulatory pathways; Chk1/Chk2(Cds1) mediated inactivation of Cyclin B:Cdk1 complex; Activation of BAD and translocation to mitochondria |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04917](https://www.uniprot.org/uniprotkb/Q04917) (14-3-3 protein eta):

> Adapter protein implicated in the regulation of a large spectrum of both general and specialized signaling pathways. Binds to a large number of partners, usually by recognition of a phosphoserine or phosphothreonine motif. Binding generally results in the modulation of the activity of the binding partner. Negatively regulates the kinase activity of PDPK1.

**Summary**, from NCBI Gene [7533](https://www.ncbi.nlm.nih.gov/gene/7533):

> This gene product belongs to the 14-3-3 family of proteins which mediate signal transduction by binding to phosphoserine-containing proteins. This highly conserved protein family is found in both plants and mammals, and this protein is 99% identical to the mouse, rat and bovine orthologs. This gene contains a 7 bp repeat sequence in its 5' UTR, and changes in the number of this repeat have been associated with early-onset schizophrenia and psychotic bipolar disorder. [provided by RefSeq, Jun …

**Accessions** — [HGNC:12853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12853) · Entrez [7533](https://www.ncbi.nlm.nih.gov/gene/7533) · UniProt [Q04917](https://www.uniprot.org/uniprotkb/Q04917) · Ensembl [ENSG00000128245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128245)

## Data

Gene col 4866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4866); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4866]; `tensor/DDL_lfc|DDL_z.npy` [4866]; `embed/gene_vectors.npy` [4866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4866 or target_col == 4866). Every well: [[YWHAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
