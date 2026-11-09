---
symbol: "CAVIN4"
type: "gene"
col: 9995
ensembl_id: "ENSG00000170681"
name: "caveolae associated protein 4"
location: "9q31.1"
module: 39
arm: "+"
pooled_cpm: 7.87
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CAVIN4

*caveolae associated protein 4* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.86× (z +26.4, q 0e+00, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.420× (z -12.1, q 8e-31, down in 29 of 43 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 0.605× (z -3.7, q 0.013, down in 9 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEFF1]] (+0.86, fdr 7e-06, ⚠ same locus), [[MSANTD3-TMEFF1]] (+0.86, fdr 7e-06, ⚠ same locus), [[SLC22A1]] (+0.74, fdr 7e-06), [[GRK4]] (+0.74, fdr 7e-06), [[LINC00486]] (+0.73, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.63, fdr 1e-05), [[SLC9A6]] (-0.62, fdr 5e-05), [[BRAT1]] (-0.60, fdr 2e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[NEK10]] → it (grade B ⚠); 4 go from it, the strongest it → [[ACTR3-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.86×** | +26.4 | 0e+00 | 36/41 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.21×** | +16.2 | 0e+00 | 38/40 (A-172, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +12.5 | 9e-34 | 28/40 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.82×** | +9.7 | 4e-20 | 29/43 (NCI-H460, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.0 | 3e-10 | 6/17 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.1 | 9e-08 | 16/43 (A-172, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.6 | 2e-06 | 5/19 (NCI-H460, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.9 | 7e-05 | 19/43 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.3 | 0.001 | 6/16 (A-172, A549, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.001 | 14/40 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +4.1 | 0.003 | 5/41 (SNU-423, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.008 | 11/42 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.018 | 5/41 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.020 | 5/40 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.033 | 3/44 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.033 | 9/41 (NCI-H2030, J82, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.033 | 4/43 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.054 | 6/42 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.068 | 13/38 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.420×** | -12.1 | 8e-31 | 29/43 (HEC-1-A, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.446×** | -11.3 | 7e-27 | 33/42 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.448×** | -11.2 | 1e-26 | 30/44 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.520×** | -8.8 | 3e-16 | 21/30 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.619×** | -6.7 | 3e-09 | 21/37 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.646×** | -6.1 | 1e-07 | 20/43 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.701×** | -5.0 | 5e-05 | 17/42 (H4, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.740×** | -4.2 | 0.002 | 9/38 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.757×** | -3.8 | 0.011 | 18/35 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.766×** | -3.7 | 0.011 | 15/44 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.605×** | -3.7 | 0.013 | 9/37 (NCI-H23, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.763×** | -3.6 | 0.013 | 12/42 (AN3 CA, A549, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.022 | 13/42 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.776×** | -3.4 | 0.026 | 12/43 (NCI-H460, A-172, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.785×** | -3.4 | 0.027 | 16/44 (PANC-1, H4, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.636×** | -3.3 | 0.034 | 8/36 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.638×** | -3.3 | 0.035 | 13/42 (HEC-1-A, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.1 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0776× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -13.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0965× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.3) |
| [[HOP62 (line)]] | alt | 15.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HS-578T (line)]] | alt | 16.2 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.0951× (z -11.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 9.08 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Hs 766T (line)]] | wt | 7.22 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +11.0) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0742× (z -10.4) |
| [[J82 (line)]] | alt | 11.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.44 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.0265× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 9.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.2) | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 2.40 | 0 | 1 | — | [[Diphenhydramine (drug)]] 0.05 µM 0.0420× (z -9.2) |
| [[COLO 205 (line)]] | alt | 3.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +12.8) | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0396× (z -13.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 3.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 7.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 4.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 4.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +11.5) | — |
| [[RKO (line)]] | wt | 6.95 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.09× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 6.95 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0736× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 7.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +15.8) | — |
| [[SW480 (line)]] | alt | 4.09 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.56× (z +9.3) | — |
| [[A-427 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEFF1]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[MSANTD3-TMEFF1]] | +0.86 | +0.91 / +0.73 | both halves | 7e-06 | STRING 403; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[SLC22A1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GRK4]] | +0.74 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.73 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[ZNF382]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ESRRB]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.68 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.68 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[SCUBE2]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.67 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NEB]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.63 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.62 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[BRAT1]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[CDC42SE2]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK10]] | B | NEK10 activity raises CAVIN4's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.73× lower at baseline in the lines without NEK10 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises CAVIN4's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without CLDN14-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[LINC01505]] | B | LINC01505 activity raises CAVIN4's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without LINC01505 | 0.049 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[COL27A1]] | B | COL27A1 activity raises CAVIN4's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without COL27A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises CAVIN4's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without APCDD1L-DT | 0.062 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[SCUBE2]] | B | SCUBE2 activity raises CAVIN4's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 2.54× lower at baseline in the lines without SCUBE2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[LRIF1]] | B | LRIF1 activity raises CAVIN4's level | lines that do not express LRIF1 (5) vs lines expressing it (45) | 1.03× lower at baseline in the lines without LRIF1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RAP1GAP2, PPFIA4, AP1S3 |
| [[PLXNA4]] | B | PLXNA4 activity raises CAVIN4's level | lines that do not express PLXNA4 (9) vs lines expressing it (41) | 2.11× lower at baseline in the lines without PLXNA4 | 0.087 | ⚠ within organs, on part of the lines; also absent: ASAP3, PRDM6, PRKAR2B; maybe low, not absent |
| [[PRECSIT]] | B | PRECSIT activity raises CAVIN4's level | lines that do not express PRECSIT (9) vs lines expressing it (41) | 1.13× lower at baseline in the lines without PRECSIT | 0.095 | ⚠ within organs, on part of the lines; also absent: FAM3B, CFAP45, ENSG00000283511; maybe low, not absent |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises CAVIN4's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without ITPR2-AS1 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[TMEFF1]] | C | TMEFF1 activity raises CAVIN4's level | lines that do not express TMEFF1 (5) vs lines expressing it (45) | 3.04× lower at baseline in the lines without TMEFF1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DNAJC18, HECTD2, TBKBP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR3-AS1]] | C | CAVIN4 activity raises ACTR3-AS1's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without CAVIN4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent; its own permutation p |
| [[PRECSIT]] | C | CAVIN4 activity raises PRECSIT's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without CAVIN4 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent |
| [[LMLN]] | C | CAVIN4 activity raises LMLN's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without CAVIN4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent; its own permutation p |
| [[CDKL3]] | C | CAVIN4 activity raises CDKL3's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without CAVIN4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.0, -4.5); signed map (24.5, 8.2). **Vector** length 98.7, 21.2% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +26.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.3 | +16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.5 | -11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.4 | -12.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.0 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.9 | -11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.8 | -5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | caveolae associated protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:100,578,079-100,588,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cavin-4; previously MURC |
| Gene groups (HGNC) | Cavins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BKX8](https://www.uniprot.org/uniprotkb/Q5BKX8) (Caveolae-associated protein 4):

> Modulates the morphology of formed caveolae in cardiomyocytes, but is not required for caveolar formation. Facilitates the recruitment of MAPK1/3 to caveolae within cardiomyocytes and regulates alpha-1 adrenergic receptor-induced hypertrophic responses in cardiomyocytes through MAPK1/3 activation. Contributes to proper membrane localization and stabilization of caveolin-3 (CAV3) in cardiomyocytes (By similarity). Induces RHOA activation and activates NPPA transcription and myofibrillar …

**Summary**, from NCBI Gene [347273](https://www.ncbi.nlm.nih.gov/gene/347273):

> This gene encodes a protein containing two coiled-coil regions. The encoded protein promotes Rho/ROCK (Rho-kinase) signaling in cardiac muscles cells, and may facilitate myofibrillar organization. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:33742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33742) · Entrez [347273](https://www.ncbi.nlm.nih.gov/gene/347273) · UniProt [Q5BKX8](https://www.uniprot.org/uniprotkb/Q5BKX8) · Ensembl [ENSG00000170681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170681)

## Data

Gene col 9995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9995); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9995]; `tensor/DDL_lfc|DDL_z.npy` [9995]; `embed/gene_vectors.npy` [9995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9995 or target_col == 9995). Every well: [[CAVIN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAVIN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
