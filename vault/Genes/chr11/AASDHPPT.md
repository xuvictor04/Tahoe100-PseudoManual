---
symbol: "AASDHPPT"
type: "gene"
col: 7366
ensembl_id: "ENSG00000149313"
name: "aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase"
location: "11q22.3"
module: 28
arm: "+"
pooled_cpm: 34.08
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AASDHPPT

*aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +12.6, q 1e-33, up in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.35× (z +11.1, q 2e-26, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.672× (z -5.2, q 1e-04, down in 30 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.698× (z -4.7, q 7e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX1]] (+0.81, fdr 7e-06), [[ZNF252P-1]] (+0.78, fdr 7e-06), [[DIS3L]] (+0.74, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.71, fdr 7e-06), [[UQCRH]] (-0.67, fdr 1e-05), [[IGSF8]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[S100A14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +12.6 | 1e-33 | 40/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.8 | 1e-29 | 36/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.35×** | +11.1 | 2e-26 | 46/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +10.8 | 8e-25 | 45/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.32×** | +10.5 | 6e-24 | 46/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.68×** | +9.5 | 2e-19 | 38/48 (KATO III, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +8.5 | 1e-15 | 34/44 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.9 | 3e-13 | 38/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.69×** | +6.8 | 6e-10 | 40/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +6.4 | 9e-09 | 36/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.43×** | +4.6 | 2e-04 | 29/47 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 28/48 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.005 | 25/47 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.008 | 24/48 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.33×** | +3.5 | 0.017 | 22/47 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.020 | 20/47 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.030 | 19/48 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.031 | 20/48 (HEC-1-A, SW48, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +3.0 | 0.065 | 18/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.091 | 11/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.092 | 10/48 (HOP62, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.53×** | +2.9 | 0.093 | 10/48 (CFPAC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -5.2 | 1e-04 | 30/47 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -4.7 | 7e-04 | 27/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -4.3 | 0.003 | 25/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.010 | 22/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.749×** | -3.8 | 0.017 | 25/48 (SW48, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.775× | -3.2 | 0.15 | 18/48 (SW48, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.3 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.59× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.386× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.86× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 29.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +11.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -8.8) |
| [[PANC-1 (line)]] | alt | 58.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.40× (z +8.7) | — |
| [[A498 (line)]] | wt | 23.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 38.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 52.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.00× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 52.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 34.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.26× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +11.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 32.2 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.81× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 24.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.57× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.119× (z -9.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX1]] | +0.81 | +0.89 / +0.75 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.78 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[DIS3L]] | +0.74 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[THOC7]] | +0.73 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.72 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.71 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[ZNF252P]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[SRSF8]] | +0.70 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[ZNF260]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.71 | -0.71 / -0.74 | both halves | 7e-06 |  |
| [[UQCRH]] | -0.67 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.67 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[CORO7]] | -0.67 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.66 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[INPP5A]] | -0.65 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[AZIN2]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CD81]] | -0.65 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[TPST2]] | -0.64 | -0.70 / -0.53 | both halves | 1e-05 |  |
| [[TMEM41B]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[QSOX1]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[SH3D21]] | -0.63 | -0.65 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A14]] | B | S100A14 activity lowers AASDHPPT's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.28× higher at baseline in the lines without S100A14 | 0.035 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[CFL2]] | C | CFL2 activity raises AASDHPPT's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.63× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.3, 6.2); signed map (6.5, -28.5). **Vector** length 114, 33.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.3 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +8.7 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.8 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +6.1 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:106,075,501-106,098,699 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LYS5, CGI-80, AASD-PPT, ACPS |
| Reactome | 3 pathways, smallest: Vitamin B5 (pantothenate) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRN7](https://www.uniprot.org/uniprotkb/Q9NRN7) (L-aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase):

> Catalyzes the post-translational modification of target proteins by phosphopantetheine. Can transfer the 4'-phosphopantetheine moiety from coenzyme A, regardless of whether the CoA is presented in the free thiol form or as an acetyl thioester, to a serine residue of a broad range of acceptors including the acyl carrier domain of FASN.

**Summary**, from NCBI Gene [60496](https://www.ncbi.nlm.nih.gov/gene/60496):

> The protein encoded by this gene is similar to Saccharomyces cerevisiae LYS5, which is required for the activation of the alpha-aminoadipate dehydrogenase in the biosynthetic pathway of lysine. Yeast alpha-aminoadipate dehydrogenase converts alpha-biosynthetic-aminoadipate semialdehyde to alpha-aminoadipate. It has been suggested that defects in the human gene result in pipecolic acidemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14235) · Entrez [60496](https://www.ncbi.nlm.nih.gov/gene/60496) · UniProt [Q9NRN7](https://www.uniprot.org/uniprotkb/Q9NRN7) · Ensembl [ENSG00000149313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149313)

## Data

Gene col 7366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7366); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7366]; `tensor/DDL_lfc|DDL_z.npy` [7366]; `embed/gene_vectors.npy` [7366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7366 or target_col == 7366). Every well: [[AASDHPPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AASDHPPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
