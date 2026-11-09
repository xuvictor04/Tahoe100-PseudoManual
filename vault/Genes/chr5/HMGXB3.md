---
symbol: "HMGXB3"
type: "gene"
col: 3493
ensembl_id: "ENSG00000113716"
name: "HMG-box containing 3"
location: "5q32"
module: 69
arm: "+"
pooled_cpm: 62.57
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# HMGXB3

*HMG-box containing 3* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.66× (z +13.8, q 2e-40, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.379× (z -16.7, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.692× (z -9.0, q 5e-17, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF787]] (+0.56, fdr 2e-05), [[DDX55]] (+0.56, fdr 1e-04), [[DDX19A]] (+0.55, fdr 4e-05); moves opposite to [[YPEL5]] (-0.62, fdr 1e-04), [[PDCD4]] (-0.53, fdr 2e-04), [[PRDM2]] (-0.53, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.66×** | +13.8 | 2e-40 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +12.5 | 4e-33 | 46/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +11.7 | 3e-29 | 40/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.61×** | +11.5 | 2e-28 | 44/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +10.3 | 9e-23 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +9.8 | 9e-21 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +8.8 | 1e-16 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +8.3 | 1e-14 | 43/48 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.3 | 2e-11 | 34/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +7.0 | 1e-10 | 36/48 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.66×** | +4.5 | 3e-04 | 32/48 (LoVo, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 3e-04 | 38/48 (LoVo, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 3e-04 | 26/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 9e-04 | 28/48 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.0 | 0.002 | 24/47 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.009 | 23/48 (LoVo, RKO, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.022 | 19/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.028 | 19/48 (Hs 766T, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.379×** | -16.7 | 0e+00 | 44/49 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -15.2 | 0e+00 | 34/42 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -9.0 | 5e-17 | 38/49 (HS-578T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.689×** | -6.0 | 4e-07 | 30/45 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -4.6 | 5e-04 | 28/50 (AN3 CA, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.725×** | -4.0 | 0.007 | 24/48 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.797×** | -3.9 | 0.007 | 25/48 (NCI-H661, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.052 | 23/48 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.3 | 0.052 | 12/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.100 | 13/48 (AsPC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.8 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.61× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 79.0 | 5 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.37× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 60.3 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -19.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 60.8 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.64× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 76.4 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.1) |
| [[A-427 (line)]] | wt | 67.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -21.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 71.6 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.6) |
| [[SW1417 (line)]] | alt | 86.6 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 80.9 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.92× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.4 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 43.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -18.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 50.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 61.9 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0751× (z -25.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 91.4 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -10.0) |
| [[A-172 (line)]] | wt | 48.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +16.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.6) |
| [[Hs 766T (line)]] | wt | 50.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.6) | — |
| [[HS-578T (line)]] | alt | 95.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -12.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 59.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 82.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -17.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0804× (z -14.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 59.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 61.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.73× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 53.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 69.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0549× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 61.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -14.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.2) | — |
| [[A549 (line)]] | wt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -19.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.154× (z -9.0) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 86.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.67× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -12.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF787]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[DDX55]] | +0.56 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[DDX19A]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZNF865]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[MAGEF1]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[POLR3A]] | +0.54 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[ELP6]] | +0.53 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[DAGLA]] | +0.52 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[PAK1IP1]] | +0.52 | +0.32 / +0.59 | both halves | 2e-04 |  |
| [[SLC39A3]] | +0.50 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[CENPB]] | +0.49 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[P3H4]] | +0.49 | +0.42 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.62 | -0.36 / -0.66 | both halves | 1e-04 |  |
| [[PDCD4]] | -0.53 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[PRDM2]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LSMEM1]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PXDNL]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PCMTD1]] | -0.50 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[TAX1BP1]] | -0.50 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[RC3H1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TMOD3]] | -0.49 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[ATP11C]] | -0.49 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[HECA]] | -0.48 | -0.19 / -0.57 | ⚠ one half (not replicated) | 9e-04 |  |
| [[CDK19]] | -0.48 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[KLRD1]] | -0.48 | -0.37 / -0.46 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HMGXB3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity lowers HMGXB3's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.18× higher at baseline in the lines without SLC5A4-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction -0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.3, -8.1); signed map (-15.2, -22.8). **Vector** length 78.8, 20.1% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +8.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +13.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.3 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | HMG-box containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:150,000,046-150,053,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMF, KIAA0194; previously HMGX3 |
| Gene groups (HGNC) | Non-canonical high mobility group |
| Matched by | ensembl_id |

UniProt [Q12766](https://www.uniprot.org/uniprotkb/Q12766) carries no function annotation.

**Summary**, from NCBI Gene [22993](https://www.ncbi.nlm.nih.gov/gene/22993):

> This gene is one of the non-canonical high mobility group (HMG) genes. The encoded protein contains an HMG-box domain found in DNA binding proteins such as transcription factors and chromosomal proteins. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:28982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28982) · Entrez [22993](https://www.ncbi.nlm.nih.gov/gene/22993) · UniProt [Q12766](https://www.uniprot.org/uniprotkb/Q12766) · Ensembl [ENSG00000113716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113716)

## Data

Gene col 3493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3493); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3493]; `tensor/DDL_lfc|DDL_z.npy` [3493]; `embed/gene_vectors.npy` [3493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3493 or target_col == 3493). Every well: [[HMGXB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGXB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
