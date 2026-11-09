---
symbol: "MED23"
type: "gene"
col: 3346
ensembl_id: "ENSG00000112282"
name: "mediator complex subunit 23"
location: "6q23.2"
module: 178
arm: "+"
pooled_cpm: 72.41
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# MED23

*mediator complex subunit 23* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.69× (z +8.9, q 4e-16, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.309× (z -19.3, q 0e+00, down in 42 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.646× (z -9.7, q 3e-20, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC10]] (+0.75, fdr 7e-06), [[TENT2]] (+0.75, fdr 7e-06), [[USPL1]] (+0.74, fdr 7e-06); moves opposite to [[PSMD6-AS1]] (-0.68, fdr 3e-05), [[DDX5]] (-0.66, fdr 1e-05), [[KDM6B]] (-0.65, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.69×** | +8.9 | 4e-16 | 40/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +8.2 | 8e-14 | 39/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.1 | 2e-07 | 34/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +5.3 | 2e-05 | 29/48 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.31×** | +4.7 | 4e-04 | 28/48 (Hs 766T, Panc 03.27, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 4e-04 | 30/48 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.002 | 27/47 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.6 | 0.021 | 20/48 (HT-29, SNU-1, …) | two highest doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.062 | 23/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.082 | 18/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.082 | 14/48 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.20× | +3.1 | 0.082 | 19/48 (A-427, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.309×** | -19.3 | 0e+00 | 42/42 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.338×** | -18.6 | 0e+00 | 46/49 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.429×** | -13.4 | 1e-38 | 40/45 (SHP-77, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -9.7 | 3e-20 | 39/49 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.717×** | -5.7 | 2e-06 | 33/48 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.772×** | -4.4 | 1e-03 | 27/48 (HOP62, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.2 | 0.002 | 25/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.800×** | -3.7 | 0.018 | 22/48 (LoVo, hTERT-HPNE, …) | two highest doses | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.769×** | -3.2 | 0.084 | 13/48 (NCI-H460, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.088 | 17/48 (A498, C32, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.833×** | -3.1 | 0.093 | 18/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | 0.829× | -3.1 | 0.10 | 19/47 (NCI-H2347, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 119 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.3) |
| [[A-172 (line)]] | wt | 51.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.4) |
| [[HOP62 (line)]] | alt | 68.8 | 0 | 5 (5 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.164× (z -19.4) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 98.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.0) |
| [[C32 (line)]] | wt | 81.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 79.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 84.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -19.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 71.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 49.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.6) |
| [[KATO III (line)]] | alt | 85.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -13.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 94.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0966× (z -22.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 66.0 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.67× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 94.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -16.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 76.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -14.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 87.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -12.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 88.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -19.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 89.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 99.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -21.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 96.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -16.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0750× (z -24.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 71.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 87.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -10.3) |
| [[H4 (line)]] | wt | 59.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 64.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -16.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 56.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 58.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 76.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 58.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -14.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 58.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -14.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 73.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.9) ⚠ cell-cycle shift, explains ~94% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 98.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 90.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 67.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC10]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[TENT2]] | +0.75 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[USPL1]] | +0.74 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[HEATR5B]] | +0.72 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[SDHB]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[USP30]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.71 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MALSU1]] | +0.70 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SNX1]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.70 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[CWC15]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | -0.68 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[DDX5]] | -0.66 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.65 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.64 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[PIEZO1]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SKIL]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ST7L]] | -0.61 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[HNRNPK]] | -0.61 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[NPIPB4]] | -0.61 | -0.65 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.7, -12.1); signed map (-32.4, -10.4). **Vector** length 105, 31.3% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.3 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.9 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +5.3 |
|  | [[NG25 (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +8.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.9 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -6.3 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.2 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:131,573,966-131,628,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRSP130, DRIP130, Sur2; previously CRSP3, MRT18 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULK4](https://www.uniprot.org/uniprotkb/Q9ULK4) (Mediator of RNA polymerase II transcription subunit 23):

> Required for transcriptional activation subsequent to the assembly of the pre-initiation complex (By similarity). Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a …

**Summary**, from NCBI Gene [9439](https://www.ncbi.nlm.nih.gov/gene/9439):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:2372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2372) · Entrez [9439](https://www.ncbi.nlm.nih.gov/gene/9439) · UniProt [Q9ULK4](https://www.uniprot.org/uniprotkb/Q9ULK4) · Ensembl [ENSG00000112282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112282)

## Data

Gene col 3346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3346); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3346]; `tensor/DDL_lfc|DDL_z.npy` [3346]; `embed/gene_vectors.npy` [3346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3346 or target_col == 3346). Every well: [[MED23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
