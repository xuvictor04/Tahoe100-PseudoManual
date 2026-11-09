---
symbol: "CENPJ"
type: "gene"
col: 7572
ensembl_id: "ENSG00000151849"
name: "centrosome assembly and centriole elongation protein"
location: "13q12.12-q12.13"
module: 71
arm: "+"
pooled_cpm: 53.59
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# CENPJ

*centrosome assembly and centriole elongation protein* — 13q12.12-q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.50× (z +8.5, q 8e-15, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 3.04×, C32 2.52×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 1.64×; ⚠ cell-cycle shift, explains ~56% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.410× (z -9.8, q 5e-20, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA5]] (+0.79, fdr 7e-06), [[DSN1]] (+0.78, fdr 7e-06), [[POC1A]] (+0.78, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 3.04×, C32 2.52×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 1.64×; ⚠ cell-cycle shift, explains ~56% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.50×** | +8.5 | 8e-15 | 30/47 (COLO 205, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.49×** | +8.4 | 8e-15 | 30/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.37×** | +6.6 | 7e-09 | 24/47 (RKO, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +5.1 | 4e-05 | 26/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.18× | +4.9 | 1e-04 | 21/47 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +4.8 | 1e-04 | 19/46 (J82, LoVo, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.21×** | +3.9 | 0.009 | 20/46 (HOP62, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.19× | +3.6 | 0.019 | 13/47 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.039 | 11/47 (J82, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.17× | +3.4 | 0.039 | 12/47 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.079 | 9/47 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.16× | +3.1 | 0.086 | 15/47 (HT-29, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.089 | 9/47 (SW480, NCI-H23, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -9.8 | 5e-20 | 42/47 (A498, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -9.5 | 8e-19 | 32/47 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.738×** | -9.1 | 2e-17 | 29/47 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.739×** | -9.0 | 3e-17 | 29/47 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.680×** | -8.1 | 5e-14 | 32/47 (A498, A-172, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -8.0 | 1e-13 | 6/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -7.4 | 9e-12 | 28/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -7.4 | 9e-12 | 27/43 (H4, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -7.2 | 4e-11 | 28/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.687×** | -7.1 | 6e-11 | 29/47 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.749×** | -5.5 | 2e-06 | 25/47 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -5.2 | 1e-05 | 21/47 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.816×** | -4.0 | 0.003 | 19/46 (A-172, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -3.9 | 0.004 | 17/47 (A-172, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.833×** | -3.9 | 0.004 | 11/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | 0.836× | -3.5 | 0.017 | 16/47 (HT-29, CHP-212, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.742×** | -3.3 | 0.032 | 13/47 (SW 1088, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.035 | 15/47 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.040 | 10/46 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.750×** | -3.2 | 0.042 | 19/46 (A-172, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.816×** | -3.1 | 0.056 | 10/47 (J82, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 198 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.4) |
| [[A-172 (line)]] | wt | 71.5 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.3) |
| [[H4 (line)]] | wt | 76.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0534× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.1) |
| [[HOP62 (line)]] | alt | 67.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.5) |
| [[HS-578T (line)]] | alt | 54.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.5) |
| [[J82 (line)]] | alt | 129 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.492× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 37.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.9) |
| [[Hs 766T (line)]] | wt | 68.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 56.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.401× (z -9.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[RKO (line)]] | wt | 46.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 63.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -9.5) |
| [[HT-29 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.426× (z -10.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.467× (z -9.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H1792 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.155× (z -8.8) |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.383× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.0 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0759× (z -8.7) |
| [[SW480 (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.8) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A549 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA5]] | +0.79 | +0.74 / +0.81 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[DSN1]] | +0.78 | +0.72 / +0.79 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[POC1A]] | +0.78 | +0.75 / +0.77 | both halves | 7e-06 | STRING 545 |
| [[RAD51]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[RECQL4]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[RFC4]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 | STRING 400 |
| [[TOP3A]] | +0.72 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[HAUS8]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 | pathway: AURKA Activation by TPX2; STRING 691 |
| [[FANCI]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[MELK]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SPC25]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 | pathway: Mitotic Prometaphase |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CENPJ's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PKMYT1]] | C | PKMYT1 activity raises CENPJ's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without PKMYT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | CENPJ's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | CENPJ's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.447 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.1, -48.8); signed map (-41.6, -41.2). **Vector** length 135, 39.4% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.64 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.0 | +4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.6 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.6 | +8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | +3.1 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +2.9 | +8.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -7.9 | -9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.1 | -9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.4 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -2.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | centrosome assembly and centriole elongation protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.12-q12.13 — chr13:24,882,279-24,922,889 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAP, LIP1, BM032, SASS4, SCKL4, Sas-4; previously CENPJ, MCPH6 |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; TP53 Regulates Transcription of Cell Cycle Genes; Loss of Nlp from mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC77](https://www.uniprot.org/uniprotkb/Q9HC77) (Centrosomal P4.1-associated protein):

> Plays an important role in cell division and centrosome function by participating in centriole duplication. Inhibits microtubule nucleation from the centrosome. Involved in the regulation of slow processive growth of centriolar microtubules. Acts as a microtubule plus-end tracking protein that stabilizes centriolar microtubules and inhibits microtubule polymerization and extension from the distal ends of centrioles. Required for centriole elongation and for STIL-mediated centriole …

**Summary**, from NCBI Gene [55835](https://www.ncbi.nlm.nih.gov/gene/55835):

> This gene encodes a protein that belongs to the centromere protein family. During cell division, this protein plays a structural role in the maintenance of centrosome integrity and normal spindle morphology, and it is involved in microtubule disassembly at the centrosome. This protein can function as a transcriptional coactivator in the Stat5 signaling pathway, and also as a coactivator of NF-kappaB-mediated transcription, likely via its interaction with the coactivator p300/CREB-binding …

**Accessions** — [HGNC:17272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17272) · Entrez [55835](https://www.ncbi.nlm.nih.gov/gene/55835) · UniProt [Q9HC77](https://www.uniprot.org/uniprotkb/Q9HC77) · Ensembl [ENSG00000151849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151849)

## Data

Gene col 7572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7572); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7572]; `tensor/DDL_lfc|DDL_z.npy` [7572]; `embed/gene_vectors.npy` [7572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7572 or target_col == 7572). Every well: [[CENPJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
