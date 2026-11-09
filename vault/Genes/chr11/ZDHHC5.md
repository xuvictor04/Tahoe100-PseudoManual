---
symbol: "ZDHHC5"
type: "gene"
col: 7999
ensembl_id: "ENSG00000156599"
name: "zDHHC palmitoyltransferase 5"
location: "11q12.1"
module: 36
arm: "+"
pooled_cpm: 54.42
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ZDHHC5

*zDHHC palmitoyltransferase 5* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.16× (z +13.0, q 1e-35, up in 6 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.74× (z +12.7, q 1e-34, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.610× (z -10.8, q 2e-24, down in 28 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.722× (z -7.9, q 3e-13, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPF1]] (+0.61, fdr 1e-05), [[AREL1]] (+0.61, fdr 1e-05), [[TBRG4]] (+0.61, fdr 7e-06); moves opposite to [[GADD45B]] (-0.53, fdr 1e-05), [[ABI1]] (-0.52, fdr 9e-05), [[CHMP2B]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +13.0 | 1e-35 | 6/49 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +12.7 | 1e-34 | 40/49 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +10.5 | 2e-23 | 40/48 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +6.9 | 5e-10 | 31/48 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.6 | 4e-09 | 31/48 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.9 | 4e-07 | 26/47 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +5.4 | 4e-06 | 26/48 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.0 | 0.004 | 17/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.009 | 13/47 (PANC-1, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.610×** | -10.8 | 2e-24 | 28/45 (A549, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.661×** | -10.0 | 3e-21 | 30/49 (HCT15, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -9.9 | 6e-21 | 29/40 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.762×** | -9.3 | 1e-18 | 25/48 (NCI-H1792, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.722×** | -7.9 | 3e-13 | 33/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.747×** | -6.8 | 1e-09 | 28/48 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.767×** | -6.4 | 1e-08 | 26/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.800×** | -5.4 | 4e-06 | 27/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.816×** | -4.9 | 5e-05 | 19/48 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -4.9 | 5e-05 | 18/47 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -4.8 | 8e-05 | 12/48 (SW 1088, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.824×** | -4.7 | 1e-04 | 22/48 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.822×** | -4.6 | 2e-04 | 18/49 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.843× | -4.1 | 0.001 | 14/48 (COLO 205, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | 0.845× | -3.9 | 0.003 | 19/47 (NCI-H460, SW48, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.845× | -3.9 | 0.003 | 17/48 (AN3 CA, SW480, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.895× | -3.8 | 0.004 | 5/48 (AsPC-1, SHP-77, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.857× | -3.8 | 0.006 | 16/48 (C32, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.3 | 1 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.16× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.536× (z -9.3) |
| [[SW480 (line)]] | alt | 75.9 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.26× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -14.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 48.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 53.8 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.49× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 65.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 68.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 49.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.82× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 42.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.9) |
| [[SW 900 (line)]] | alt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-427 (line)]] | wt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.606× (z -9.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A549 (line)]] | wt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -13.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 50.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -8.9) |
| [[H4 (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0790× (z -20.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[J82 (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -11.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[KATO III (line)]] | alt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 93.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[RKO (line)]] | wt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -14.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0796× (z -11.9) |
| [[SNU-1 (line)]] | wt | 49.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPF1]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 | STRING 663 |
| [[AREL1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SETD1A]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ZBED4]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TTI1]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PRCC]] | +0.60 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HIRA]] | +0.60 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[FAM118B]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[DGCR8]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[MCM9]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NLK]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GADD45B]] | -0.53 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ABI1]] | -0.52 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[CHMP2B]] | -0.50 | -0.56 / -0.48 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[SGO1-AS1]] | -0.49 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[LGALS3]] | -0.49 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.0, -16.9); signed map (-47.0, -21.7). **Vector** length 91.5, 19.8% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.6 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +12.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -5.1 | -9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.6 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | -3.4 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,667,747-57,701,182 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1748, ZNF375, DHHC5 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 6 pathways, smallest: Maturation of spike protein_9694548; Translation of Structural Proteins_9694635; Late SARS-CoV-2 Infection Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0B5](https://www.uniprot.org/uniprotkb/Q9C0B5) (Palmitoyltransferase ZDHHC5):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates such as CTNND2, CD36, GSDMD, NLRP3, NOD1, NOD2, RIPK1, STAT3 and S1PR1 thus plays a role in various biological processes including cell adhesion, inflammation, fatty acid uptake, bacterial sensing or cardiac functions. Plays an important role in the regulation of synapse efficacy by mediating palmitoylation of delta-catenin/CTNND2, thereby increasing synaptic delivery and surface stabilization of …

**Summary**, from NCBI Gene [25921](https://www.ncbi.nlm.nih.gov/gene/25921):

> Enables protein-cysteine S-palmitoyltransferase activity. Involved in positive regulation of defense response; positive regulation of protein localization to plasma membrane; and protein localization to plasma membrane. Acts upstream of or within protein palmitoylation. Located in phagocytic vesicle and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18472) · Entrez [25921](https://www.ncbi.nlm.nih.gov/gene/25921) · UniProt [Q9C0B5](https://www.uniprot.org/uniprotkb/Q9C0B5) · Ensembl [ENSG00000156599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156599)

## Data

Gene col 7999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7999); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7999]; `tensor/DDL_lfc|DDL_z.npy` [7999]; `embed/gene_vectors.npy` [7999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7999 or target_col == 7999). Every well: [[ZDHHC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
