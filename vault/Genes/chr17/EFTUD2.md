---
symbol: "EFTUD2"
type: "gene"
col: 3008
ensembl_id: "ENSG00000108883"
name: "elongation factor Tu GTP binding domain containing 2"
location: "17q21.31"
module: 4
arm: "+"
pooled_cpm: 58.84
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EFTUD2

*elongation factor Tu GTP binding domain containing 2* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +17.6, q 0e+00, up in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.20× (z +11.6, q 4e-29, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.779× (z -7.7, q 6e-12, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1A]] (+0.80, fdr 7e-06), [[NUP155]] (+0.79, fdr 7e-06), [[MRPS27]] (+0.77, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.73, fdr 7e-06), [[TERF2IP]] (-0.72, fdr 7e-06), [[ING2]] (-0.71, fdr 8e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VAMP5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +17.6 | 0e+00 | 34/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +15.7 | 0e+00 | 42/49 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +13.4 | 2e-38 | 38/45 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +11.8 | 5e-30 | 44/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.20×** | +11.6 | 4e-29 | 44/49 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +11.3 | 2e-27 | 42/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +10.9 | 1e-25 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +10.2 | 2e-22 | 42/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +9.1 | 9e-18 | 38/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +8.9 | 2e-17 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +8.9 | 4e-17 | 37/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.48×** | +8.5 | 1e-15 | 35/48 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +8.2 | 8e-15 | 38/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.44×** | +8.0 | 7e-14 | 35/48 (Hs 766T, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.36×** | +6.7 | 1e-09 | 37/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 3e-05 | 21/47 (NCI-H460, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 7e-05 | 21/48 (NCI-H1792, A498, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +4.7 | 8e-05 | 20/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +4.5 | 2e-04 | 22/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.004 | 16/48 (MIA PaCa-2, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.005 | 17/48 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.015 | 14/48 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -7.7 | 6e-12 | 30/48 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -5.6 | 8e-06 | 24/48 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.786×** | -5.3 | 3e-05 | 27/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.820×** | -4.3 | 0.002 | 20/49 (NCI-H23, LoVo, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.846× | -4.1 | 0.005 | 18/48 (SK-MEL-2, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.840× | -3.8 | 0.013 | 17/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.860× | -3.6 | 0.024 | 18/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.844× | -3.6 | 0.024 | 16/47 (LoVo, SK-MEL-2, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.858× | -3.4 | 0.047 | 15/48 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.883× | -3.2 | 0.082 | 12/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **0.818×** | -3.1 | 0.095 | 12/48 (SK-MEL-2, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.903× | -3.1 | 0.097 | 8/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.821×** | -3.1 | 0.097 | 13/48 (SW 900, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.9 | 11 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.03× (z +20.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 3.20× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 50.1 | 5 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.01× (z +9.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.1) | — |
| [[A498 (line)]] | wt | 68.3 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 50.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.99× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 69.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.03× (z +21.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 30.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.17× (z +14.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 69.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +14.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 46.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +15.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 55.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +16.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 33.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 72.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +19.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +13.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 52.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 38.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 36.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +9.2) | — |
| [[RKO (line)]] | wt | 82.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.63× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 69.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 58.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.53× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -8.6) |
| [[A-427 (line)]] | wt | 73.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.1) |
| [[A549 (line)]] | wt | 82.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 68.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.66× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 69.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +10.0) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 98.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 69.2 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0572× (z -12.1) |
| [[SNU-1 (line)]] | wt | 58.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 61.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1A]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | STRING 798 |
| [[NUP155]] | +0.79 | +0.73 / +0.81 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MRPS27]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[CHID1]] | +0.76 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[FARSB]] | +0.76 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[NOC2L]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 | STRING 496 |
| [[EIF2S1]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 | STRING 484 |
| [[LAS1L]] | +0.75 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[GFM1]] | +0.74 | +0.56 / +0.76 | both halves | 1e-05 | same gene group |
| [[TMEM33]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.73 | -0.71 / -0.71 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.72 | -0.67 / -0.74 | both halves | 7e-06 |  |
| [[ING2]] | -0.71 | -0.58 / -0.76 | both halves | 8e-06 |  |
| [[ARID4B]] | -0.70 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[ARID4A]] | -0.70 | -0.73 / -0.68 | both halves | 7e-06 |  |
| [[ZFAND2B]] | -0.69 | -0.61 / -0.76 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.68 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[KDM5B]] | -0.67 | -0.59 / -0.67 | both halves | 7e-06 | STRING 447 |
| [[AFTPH]] | -0.67 | -0.53 / -0.71 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | -0.66 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[FBXL15]] | -0.65 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[SELENOM]] | -0.65 | -0.56 / -0.69 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP5]] | B | VAMP5 activity lowers EFTUD2's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.33× higher at baseline in the lines without VAMP5 | 0.008 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |
| [[FAM133A]] | B | FAM133A activity raises EFTUD2's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 1.26× lower at baseline in the lines without FAM133A | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4 |
| [[GOLGA8N]] | B | GOLGA8N activity raises EFTUD2's level | lines that do not express GOLGA8N (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without GOLGA8N | 0.082 | ⚠ within organs, on part of the lines; also absent: HECTD2, TBKBP1, TMEFF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.8, -33.2); signed map (-9.0, -45.8). **Vector** length 119, 35.1% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.51 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.55 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +15.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +11.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +9.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | elongation factor Tu GTP binding domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,849,948-44,899,445 (-) |
| Ensembl biotype | protein_coding |
| Also known as | U5-116KD, Snrp116, Snu114, SNRNP116 |
| Gene groups (HGNC) | U5 small nuclear ribonucleoprotein; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex; Translational GTPases |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15029](https://www.uniprot.org/uniprotkb/Q15029) (116 kDa U5 small nuclear ribonucleoprotein component):

> Required for pre-mRNA splicing as component of the spliceosome, including pre-catalytic, catalytic and post-catalytic spliceosomal complexes. Component of the U5 snRNP and the U4/U6-U5 tri-snRNP complex, a building block of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [9343](https://www.ncbi.nlm.nih.gov/gene/9343):

> This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:30858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30858) · Entrez [9343](https://www.ncbi.nlm.nih.gov/gene/9343) · UniProt [Q15029](https://www.uniprot.org/uniprotkb/Q15029) · Ensembl [ENSG00000108883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108883)

## Data

Gene col 3008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3008); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3008]; `tensor/DDL_lfc|DDL_z.npy` [3008]; `embed/gene_vectors.npy` [3008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3008 or target_col == 3008). Every well: [[EFTUD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFTUD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
