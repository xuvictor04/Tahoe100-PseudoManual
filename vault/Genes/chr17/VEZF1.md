---
symbol: "VEZF1"
type: "gene"
col: 5866
ensembl_id: "ENSG00000136451"
name: "vascular endothelial zinc finger 1"
location: "17q22"
module: 16
arm: "+"
pooled_cpm: 58.98
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# VEZF1

*vascular endothelial zinc finger 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.24× (z +28.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.673× (z -9.7, q 2e-19, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIG4]] (+0.77, fdr 7e-06), [[ZNF260]] (+0.76, fdr 7e-06), [[ZNF776]] (+0.76, fdr 7e-06); moves opposite to [[UQCRH]] (-0.75, fdr 7e-06), [[NDUFAF7]] (-0.74, fdr 7e-06), [[RARS2]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.24×** | +28.8 | 0e+00 | 47/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.19×** | +19.4 | 0e+00 | 48/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +11.4 | 7e-28 | 46/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +11.2 | 8e-27 | 45/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +10.0 | 3e-21 | 44/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +8.0 | 2e-13 | 41/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 3e-08 | 31/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +6.1 | 8e-08 | 30/48 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.7 | 9e-07 | 33/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.6 | 3e-04 | 29/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.29×** | +4.4 | 6e-04 | 26/47 (COLO 205, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.26×** | +4.0 | 0.003 | 26/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.23×** | +3.4 | 0.029 | 23/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.064 | 13/48 (J82, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -9.7 | 2e-19 | 39/48 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -8.1 | 2e-13 | 37/48 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.660×** | -7.2 | 1e-10 | 38/48 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.5 | 7e-09 | 36/49 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -6.5 | 7e-09 | 35/48 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.697×** | -5.9 | 3e-07 | 36/48 (NCI-H1573, HT-29, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.661×** | -5.1 | 3e-05 | 38/48 (SNU-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.791×** | -4.0 | 0.004 | 24/48 (HepG2/C3A, A-172, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.806×** | -3.7 | 0.012 | 23/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.758×** | -3.4 | 0.036 | 22/48 (LS 180, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.043 | 19/48 (SW 1088, NCI-H460, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.063 | 16/48 (LS 180, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.704×** | -3.2 | 0.063 | 21/44 (Hs 766T, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 0.837× | -3.1 | 0.083 | 19/47 (A-172, HepG2/C3A, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.782×** | -3.0 | 0.092 | 15/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 62.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +27.8) | — |
| [[C32 (line)]] | wt | 54.3 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 71.6 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +20.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 38.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +23.1) | — |
| [[PANC-1 (line)]] | alt | 68.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +25.2) | — |
| [[SW480 (line)]] | alt | 76.8 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -13.1) |
| [[A498 (line)]] | wt | 64.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +21.5) | — |
| [[BT-474 (line)]] | alt | 82.7 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 49.9 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +19.6) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -9.2) |
| [[A-427 (line)]] | wt | 44.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[AsPC-1 (line)]] | alt | 33.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 63.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.2) |
| [[HCT15 (line)]] | alt | 68.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.6) | [[NG25 (drug)]] 5 µM 0.0424× (z -13.2) |
| [[HOP62 (line)]] | alt | 67.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +18.8) | — |
| [[HS-578T (line)]] | alt | 68.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.4) |
| [[HT-29 (line)]] | alt | 57.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +14.7) | — |
| [[KATO III (line)]] | alt | 67.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +20.0) | — |
| [[LoVo (line)]] | wt | 35.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +19.6) | — |
| [[LOX-IMVI (line)]] | wt | 53.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 45.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 45.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +17.8) | — |
| [[NCI-H23 (line)]] | alt | 42.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 75.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.5) |
| [[SW 900 (line)]] | alt | 73.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.0) |
| [[A-172 (line)]] | wt | 66.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.0) | — |
| [[H4 (line)]] | wt | 58.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 87.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.0) |
| [[Hs 766T (line)]] | wt | 35.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.6) | [[Bortezomib (drug)]] 5 µM 0.0658× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 63.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.10× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 48.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 61.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.0) | — |
| [[RKO (line)]] | wt | 66.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.6) | — |
| [[RPMI-7951 (line)]] | alt | 53.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 67.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.2) | [[Ipatasertib (drug)]] 0.5 µM 0.190× (z -8.5) |
| [[SNU-423 (line)]] | alt | 57.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +16.5) | — |
| [[C-33 A (line)]] | alt | 58.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 61.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 75.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.5) | — |
| [[SW48 (line)]] | wt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +13.1) | — |
| [[AN3 CA (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIG4]] | +0.77 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.76 | +0.65 / +0.76 | both halves | 7e-06 | same gene group |
| [[ZNF776]] | +0.76 | +0.67 / +0.72 | both halves | 7e-06 | same gene group |
| [[BBS10]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[ZBTB33]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 | same gene group |
| [[BMI1]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SKIL]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 | same gene group |
| [[UBQLN2]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TIGD2]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ANAPC13]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CGGBP1]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.75 | -0.65 / -0.79 | both halves | 7e-06 |  |
| [[NDUFAF7]] | -0.74 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[RARS2]] | -0.71 | -0.64 / -0.68 | both halves | 7e-06 |  |
| [[DRD4]] | -0.69 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.69 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[SLC37A3]] | -0.67 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[ZCCHC17]] | -0.67 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[RAB6A]] | -0.67 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[DPM1]] | -0.66 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[TNPO3]] | -0.65 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[RPS24]] | -0.65 | -0.59 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VEZF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZFHX2]] | C | ZFHX2 activity raises VEZF1's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without ZFHX2 | 0.063 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.6, -2.4); signed map (3.2, -29.3). **Vector** length 120, 34.8% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.4 | +19.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +10.4 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +28.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.1 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.3 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -1.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -7.9 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.3 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.7 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -5.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.2 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | vascular endothelial zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:57,971,547-57,988,259 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DB1; previously ZNF161 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14119](https://www.uniprot.org/uniprotkb/Q14119) (Vascular endothelial zinc finger 1):

> Possible transcription factor. Specifically binds to the CT/GC-rich region of the interleukin-3 promoter and mediates tax transactivation of IL-3.

**Summary**, from NCBI Gene [7716](https://www.ncbi.nlm.nih.gov/gene/7716):

> Transcriptional regulatory proteins containing tandemly repeated zinc finger domains are thought to be involved in both normal and abnormal cellular proliferation and differentiation. ZNF161 is a C2H2-type zinc finger protein (Koyano-Nakagawa et al., 1994 [PubMed 8035792]). See MIM 603971 for general information on zinc finger proteins.[supplied by OMIM, Sep 2008]

**Accessions** — [HGNC:12949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12949) · Entrez [7716](https://www.ncbi.nlm.nih.gov/gene/7716) · UniProt [Q14119](https://www.uniprot.org/uniprotkb/Q14119) · Ensembl [ENSG00000136451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136451)

## Data

Gene col 5866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5866); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5866]; `tensor/DDL_lfc|DDL_z.npy` [5866]; `embed/gene_vectors.npy` [5866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5866 or target_col == 5866). Every well: [[VEZF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEZF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
