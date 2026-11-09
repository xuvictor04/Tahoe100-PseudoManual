---
symbol: "FRMD3"
type: "gene"
col: 10216
ensembl_id: "ENSG00000172159"
name: "FERM domain containing 3"
location: "9q21.32"
module: 98
arm: "+"
pooled_cpm: 40.03
n_lines_expressing: 45
n_dd_up: 21
n_dd_down: 12
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# FRMD3

*FERM domain containing 3* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.78× (z +24.5, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.565× (z -7.7, q 1e-11, down in 28 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.729× (z -4.4, q 0.001, down in 19 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (LoVo 0.213×, C32 0.322×, HS-578T 0.310×, LS 180 0.338×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.207×, A-172 0.154×, PANC-1 0.208×, AsPC-1 0.200×; ⚠ cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.136×, C32 0.139×, A-172 0.0896×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SK-MEL-2 0.169×, C32 0.252×, LS 180 0.369×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTBR]] (+0.52, fdr 2e-05), [[DIP2C]] (+0.51, fdr 2e-05), [[PRR5L]] (+0.50, fdr 2e-05); moves opposite to [[RND1]] (-0.45, fdr 4e-05), [[DENND4A]] (-0.44, fdr 2e-04), [[LTB]] (-0.44, fdr 8e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RIPOR2]] → it (grade B ⚠); 3 go from it, the strongest it → [[USP39]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.78×** | +24.5 | 0e+00 | 41/43 (HEC-1-A, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **6.59×** | +13.8 | 1e-40 | 39/44 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.32×** | +10.7 | 2e-24 | 33/41 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +5.9 | 7e-07 | 22/42 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +5.2 | 2e-05 | 17/43 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +5.1 | 2e-05 | 20/42 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.002 | 19/43 (NCI-H1573, A549, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 19/42 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.1 | 0.003 | 13/34 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.36×** | +4.0 | 0.004 | 18/42 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.005 | 21/43 (NCI-H1573, A549, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.014 | 20/43 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.016 | 13/42 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.016 | 18/43 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.19× | +3.5 | 0.017 | 17/43 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.039 | 16/43 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.051 | 13/42 (Panc 03.27, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10216.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (LoVo 0.213×, C32 0.322×, HS-578T 0.310×, LS 180 0.338×, …); [[Homoharringtonine (drug)]] 5 µM in 4 lines (C32 0.207×, A-172 0.154×, PANC-1 0.208×, AsPC-1 0.200×; ⚠ cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.136×, C32 0.139×, A-172 0.0896×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SK-MEL-2 0.169×, C32 0.252×, LS 180 0.369×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -7.7 | 1e-11 | 28/40 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.720×** | -6.5 | 3e-08 | 25/42 (C32, A-172, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.649×** | -5.8 | 1e-06 | 23/43 (LoVo, AsPC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.690×** | -5.2 | 3e-05 | 24/43 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.701×** | -4.9 | 9e-05 | 21/42 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.729×** | -4.4 | 0.001 | 19/43 (LoVo, C32, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.738×** | -4.2 | 0.002 | 20/42 (C32, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.733×** | -4.2 | 0.002 | 17/32 (LoVo, C32, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.697×** | -3.6 | 0.020 | 13/43 (A-172, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.779×** | -3.5 | 0.029 | 16/37 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.783×** | -3.4 | 0.033 | 19/42 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.787×** | -3.3 | 0.039 | 17/43 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.797× | -3.0 | 0.11 | 17/42 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 184 | 0 | 15 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -21.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -12.5) |
| [[LoVo (line)]] | wt | 196 | 0 | 14 (13 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.213× (z -15.0) |
| [[LS 180 (line)]] | wt | 148 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.247× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.6) |
| [[A-172 (line)]] | wt | 67.9 | 1 | 8 (7 ⚠) | [[Auranofin (drug)]] 5 µM 8.28× (z +15.7) | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -19.7) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.276× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -14.6) |
| [[PANC-1 (line)]] | alt | 41.0 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.2) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW1417 (line)]] | alt | 56.2 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HS-578T (line)]] | alt | 59.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 26.5 | 5 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 6.14× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 40.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 9.15× (z +19.2) | — |
| [[SW480 (line)]] | alt | 13.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +17.0) | — |
| [[AsPC-1 (line)]] | alt | 53.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -15.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 21.2 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 25.2× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 44.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 12.7 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.12× (z +14.7) | — |
| [[A498 (line)]] | wt | 10.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.28× (z +10.0) | — |
| [[A549 (line)]] | wt | 43.3 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.21× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 49.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +12.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.77× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 15.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 17.4× (z +16.9) | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 16.7× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 35.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.19× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 34.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.17× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[COLO 205 (line)]] | alt | 17.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -12.2) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 10.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.03× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.4) ⚠ cell-cycle shift, explains ~68% of this change |
| [[RPMI-7951 (line)]] | alt | 10.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.0× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 20.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +13.2) | — |
| [[SW48 (line)]] | wt | 10.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.4× (z +8.7) | — |
| [[A-427 (line)]] | wt | 7.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBR]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DIP2C]] | +0.51 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[PRR5L]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[FOXN2]] | +0.50 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[GLUL]] | +0.48 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[XKR9]] | +0.47 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[RNF175]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.47 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[PHACTR3]] | +0.47 | +0.40 / +0.43 | both halves | 4e-05 |  |
| [[SP2-AS1]] | +0.47 | +0.45 / +0.39 | both halves | 6e-05 |  |
| [[RHOBTB2]] | +0.47 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SNED1]] | +0.46 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RND1]] | -0.45 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[DENND4A]] | -0.44 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[LTB]] | -0.44 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[CD47]] | -0.41 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[NFKB2]] | -0.41 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[LCA5]] | -0.40 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[FAM110A]] | -0.40 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[IL23A]] | -0.40 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[AHI1]] | -0.40 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[SVIP]] | -0.40 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[TESK2]] | -0.39 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[TMEM63B]] | -0.39 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIPOR2]] | B | RIPOR2 activity raises FRMD3's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without RIPOR2 | 0.026 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises FRMD3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TLR2]] | B | TLR2 activity raises FRMD3's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.61× lower at baseline in the lines without TLR2 | 0.097 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP39]] | B | FRMD3 activity lowers USP39's level | lines that do not express FRMD3 (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without FRMD3 | 0.047 | ⚠ within organs, on part of the lines; also absent: SSUH2, CACNG2, ZMIZ1; maybe low, not absent |
| [[CDC123]] | B | FRMD3 activity lowers CDC123's level | lines that do not express FRMD3 (5) vs lines expressing it (45) | 1.49× higher at baseline in the lines without FRMD3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SSUH2, CACNG2, ZMIZ1; maybe low, not absent |
| [[DBNDD1]] | B | FRMD3 activity lowers DBNDD1's level | lines that do not express FRMD3 (5) vs lines expressing it (45) | 2.17× higher at baseline in the lines without FRMD3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SSUH2, CACNG2, ZMIZ1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.3, 39.4); signed map (15.7, 33.1). **Vector** length 120, 32.2% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.3 | +24.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.0 | +13.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.2 | +10.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.2 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.0 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.7 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.5 | +5.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.3 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.2 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Hexylresorcinol (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,242,990-83,538,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPB41L4O, MGC20553 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A2A2Y4](https://www.uniprot.org/uniprotkb/A2A2Y4) (FERM domain-containing protein 3):

> Putative tumor suppressor gene that may be implicated in the origin and progression of lung cancer.

**Summary**, from NCBI Gene [257019](https://www.ncbi.nlm.nih.gov/gene/257019):

> The protein encoded by this gene is a single pass membrane protein primarily found in ovaries. A similar protein in erythrocytes helps determine the shape of red blood cells, but the function of the encoded protein has not been determined. There is some evidence that this is a tumor suppressor gene, and there is also evidence linking defects in this gene to susceptibility to diabetic nephropathy in type 1 diabetes. Several transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:24125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24125) · Entrez [257019](https://www.ncbi.nlm.nih.gov/gene/257019) · UniProt [A2A2Y4](https://www.uniprot.org/uniprotkb/A2A2Y4) · Ensembl [ENSG00000172159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172159)

## Data

Gene col 10216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10216); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10216]; `tensor/DDL_lfc|DDL_z.npy` [10216]; `embed/gene_vectors.npy` [10216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10216 or target_col == 10216). Every well: [[FRMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
