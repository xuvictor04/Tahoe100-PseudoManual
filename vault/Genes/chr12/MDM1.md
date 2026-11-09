---
symbol: "MDM1"
type: "gene"
col: 3240
ensembl_id: "ENSG00000111554"
name: "stabilizer of axonemal microtubules 6"
location: "12q15"
module: 28
arm: "+"
pooled_cpm: 10.42
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MDM1

*stabilizer of axonemal microtubules 6* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.89× (z +22.4, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.454× (z -13.1, q 3e-36, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKS1]] (+0.69, fdr 7e-06), [[SAAL1]] (+0.69, fdr 1e-05), [[CCDC113]] (+0.64, fdr 9e-06); moves opposite to [[SNX31]] (-0.61, fdr 0.001, ⚠ not reproduced), [[IL12RB2]] (-0.60, fdr 0.002, ⚠ one half only (not replicated)), [[C9orf153]] (-0.60, fdr 4e-05), [[TPT1-AS1]] (-0.59, fdr 1e-05), [[PHKG1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMBD1P]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.89×** | +22.4 | 0e+00 | 43/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.42×** | +20.3 | 0e+00 | 44/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.11×** | +18.7 | 0e+00 | 42/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +10.6 | 4e-24 | 24/43 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.0 | 1e-13 | 8/17 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.40×** | +7.6 | 4e-12 | 23/47 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +7.3 | 2e-11 | 25/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +7.2 | 4e-11 | 22/44 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +7.2 | 5e-11 | 23/46 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +7.1 | 7e-11 | 9/24 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.1 | 9e-11 | 21/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.43×** | +5.9 | 1e-07 | 15/33 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.43×** | +5.7 | 4e-07 | 11/38 (SW480, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +5.3 | 4e-06 | 14/43 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 9e-05 | 15/45 (RKO, NCI-H1573, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +4.4 | 4e-04 | 3/46 (KATO III, LOX-IMVI, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.007 | 5/46 (A549, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.007 | 7/46 (HS-578T, SHP-77, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.008 | 7/37 (SW480, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.015 | 9/46 (LS 180, C-33 A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -13.1 | 3e-36 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.493×** | -11.7 | 3e-29 | 32/46 (C32, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -9.7 | 4e-20 | 28/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -9.6 | 9e-20 | 27/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -7.9 | 4e-13 | 24/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -5.8 | 5e-07 | 25/47 (H4, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -5.8 | 7e-07 | 18/41 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.590×** | -4.6 | 3e-04 | 17/45 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.841× | -4.1 | 0.003 | 7/47 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.637×** | -3.9 | 0.005 | 7/45 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.744×** | -3.5 | 0.024 | 8/42 (SK-MEL-2, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.816×** | -3.2 | 0.055 | 13/39 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.055 | 11/46 (H4, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.824×** | -3.2 | 0.055 | 6/46 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.074 | 8/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.075 | 12/46 (BT-474, KATO III, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.772×** | -3.1 | 0.075 | 4/46 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.1 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.86× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -11.0) |
| [[SW480 (line)]] | alt | 10.4 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 3.98× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -12.2) |
| [[LoVo (line)]] | wt | 7.32 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 7.34× (z +10.2) | [[PH-797804 (drug)]] 5 µM 0.0402× (z -8.6) |
| [[A498 (line)]] | wt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.92× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.222× (z -11.0) |
| [[A-427 (line)]] | wt | 17.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 115 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.278× (z -8.8) |
| [[C32 (line)]] | wt | 8.60 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.119× (z -9.2) |
| [[Hs 766T (line)]] | wt | 5.63 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.84× (z +8.8) | — |
| [[J82 (line)]] | alt | 11.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 6.10 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0789× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 8.19 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 5.89 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.101× (z -9.0) |
| [[RKO (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 9.16 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -9.3) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKS1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.69 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[CCDC113]] | +0.64 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[ZNF678]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[C2CD5]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SSX2IP]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MRPS31P4]] | +0.62 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[EXOSC9]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CEP57L1]] | +0.62 | +0.31 / +0.69 | both halves | 2e-04 |  |
| [[NBN]] | +0.61 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[HPF1]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 7 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX31]] | -0.61 | -0.16 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[IL12RB2]] | -0.60 | -0.12 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[C9orf153]] | -0.60 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[C2]] | -0.59 | -0.14 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[TPT1-AS1]] | -0.59 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[NUP210L]] | -0.58 | -0.09 / -0.63 | ⚠ one half (not replicated) | 0.003 |  |
| [[PHKG1]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[LINC02646]] | -0.57 | -0.04 / -0.63 | ⚠ one half (not replicated) | 0.006 |  |
| [[TTLL3]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PELO-AS1]] | -0.57 | -0.05 / -0.60 | ⚠ one half (not replicated) | 0.005 |  |
| [[LINC01588]] | -0.56 | -0.21 / -0.64 | both halves | 7e-04 |  |
| [[FER1L6]] | -0.56 | -0.09 / -0.57 | ⚠ one half (not replicated) | 0.003 |  |
| [[EHBP1-AS1]] | -0.56 | -0.21 / -0.56 | both halves | 6e-04 |  |
| [[CCDC62]] | -0.55 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[SLC23A3]] | -0.55 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[ZFC3H1]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[PLAC1]] | -0.55 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[SLC25A53]] | -0.54 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[LIPE-AS1]] | -0.54 | -0.27 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMBD1P]] | C | SMBD1P activity lowers MDM1's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 1.82× higher at baseline in the lines without SMBD1P | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.6, -1.4); signed map (-22.6, -16.3). **Vector** length 63.7, 10.2% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +20.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +22.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | stabilizer of axonemal microtubules 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:68,272,443-68,332,381 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MDM1 |
| Gene groups (HGNC) | Stabilizer of axonemal microtubules family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC05](https://www.uniprot.org/uniprotkb/Q8TC05) (Stabilizer of axonemal microtubules 6):

> Microtubule-binding protein that negatively regulates centriole duplication. Binds to and stabilizes microtubules.

**Summary**, from NCBI Gene [56890](https://www.ncbi.nlm.nih.gov/gene/56890):

> This gene encodes a microtubule-binding nuclear protein that localizes to the centrioles of dividing cells and differentiating multiciliated cells and negatively regulates centriole duplication. The encoded protein is closely associated with the centriole barrel, and resides in the centriole lumen. Naturally-occurring mutations in the orthologous mouse gene are associated with age-related retinal degeneration. [provided by RefSeq, Feb 2019]

**Accessions** — [HGNC:29917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29917) · Entrez [56890](https://www.ncbi.nlm.nih.gov/gene/56890) · UniProt [Q8TC05](https://www.uniprot.org/uniprotkb/Q8TC05) · Ensembl [ENSG00000111554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111554)

## Data

Gene col 3240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3240); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3240]; `tensor/DDL_lfc|DDL_z.npy` [3240]; `embed/gene_vectors.npy` [3240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3240 or target_col == 3240). Every well: [[MDM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MDM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
