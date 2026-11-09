---
symbol: "TMEM167A"
type: "gene"
col: 10515
ensembl_id: "ENSG00000174695"
name: "transmembrane protein 167A"
location: "5q14.2"
module: 42
arm: "+"
pooled_cpm: 108.8
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMEM167A

*transmembrane protein 167A* — 5q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.91× (z +13.4, q 2e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.766× (z -5.3, q 5e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAR1A]] (+0.68, fdr 7e-06), [[SEC61A1]] (+0.68, fdr 7e-06), [[SURF4]] (+0.66, fdr 7e-06); moves opposite to [[SMC3]] (-0.59, fdr 1e-05), [[KAT6A]] (-0.57, fdr 3e-05), [[KRI1]] (-0.56, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +13.4 | 2e-38 | 44/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +12.4 | 9e-33 | 44/45 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.0 | 8e-26 | 43/49 (A-427, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +7.7 | 2e-12 | 40/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.6 | 5e-12 | 41/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.44×** | +7.3 | 2e-11 | 28/44 (A-427, A-172, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +6.2 | 5e-08 | 35/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +5.9 | 3e-07 | 27/49 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +5.9 | 3e-07 | 31/48 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.8 | 3e-07 | 34/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.5 | 2e-06 | 26/37 (LOX-IMVI, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +5.3 | 6e-06 | 27/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.0 | 2e-05 | 33/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.25×** | +4.7 | 1e-04 | 25/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.24×** | +4.3 | 6e-04 | 26/47 (RKO, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.002 | 24/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 9/49 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.008 | 20/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.013 | 19/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.039 | 15/48 (LoVo, RKO, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.049 | 20/48 (LS 180, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.766×** | -5.3 | 5e-05 | 28/48 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -4.5 | 0.002 | 24/48 (J82, NCI-H2347, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.820×** | -4.0 | 0.013 | 24/47 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.833×** | -3.8 | 0.020 | 21/48 (SW1417, KATO III, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.837× | -3.7 | 0.024 | 20/49 (NCI-H2122, NCI-H2347, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.850× | -3.4 | 0.069 | 22/48 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.891× | -3.3 | 0.076 | 7/49 (SHP-77, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 142 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.01× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 163 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.12× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 74.2 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.67× (z +11.3) | — |
| [[SW480 (line)]] | alt | 109 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.50× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 77.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.1) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.24× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 97.1 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.40× (z +12.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.31× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 119 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.21× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 166 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +11.5) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[SHP-77 (line)]] | alt | 116 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.82× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.32× (z +9.8) | — |
| [[A-172 (line)]] | wt | 83.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[COLO 205 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.93× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[J82 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.499× (z -9.3) |
| [[LS 180 (line)]] | wt | 142 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.11× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 91.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.60× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.580× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 73.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.79× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 84.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.09× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 121 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.12× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +8.7) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[NCI-H23 (line)]] | alt | 83.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.40× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 199 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.96× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.04× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 94.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.4) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[RKO (line)]] | wt | 102 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.60× (z +11.1) ⚠ toxic; cell-cycle shift, explains ~15% of this change | — |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 105 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.20× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.109× (z -11.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 96.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1A]] | +0.68 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.68 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SURF4]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[TAF13]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[COPG1]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.64 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[RPN1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.62 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TM9SF3]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ZNF587B]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PMM2]] | +0.60 | +0.68 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC3]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[KAT6A]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[KRI1]] | -0.56 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[SETD2]] | -0.55 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[SCAF11]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[ZFP36L2]] | -0.53 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[KLF11]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[KMT2A]] | -0.52 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[REPIN1]] | -0.51 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[TET3]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CMTR2]] | -0.50 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[IKBKB]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -28.9); signed map (-52.5, 7.1). **Vector** length 108, 31.4% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.4 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.3 | +5.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[EX229 (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 167A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.2 — chr5:83,052,846-83,077,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30508, MGC23909, kish; previously TMEM167 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBQ9](https://www.uniprot.org/uniprotkb/Q8TBQ9) (Protein kish-A):

> Involved in the early part of the secretory pathway.

**Summary**, from NCBI Gene [153339](https://www.ncbi.nlm.nih.gov/gene/153339):

> Involved in constitutive secretory pathway. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28330) · Entrez [153339](https://www.ncbi.nlm.nih.gov/gene/153339) · UniProt [Q8TBQ9](https://www.uniprot.org/uniprotkb/Q8TBQ9) · Ensembl [ENSG00000174695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174695)

## Data

Gene col 10515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10515); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10515]; `tensor/DDL_lfc|DDL_z.npy` [10515]; `embed/gene_vectors.npy` [10515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10515 or target_col == 10515). Every well: [[TMEM167A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM167A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
