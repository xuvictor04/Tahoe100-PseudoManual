---
symbol: "HIPK2"
type: "gene"
col: 745
ensembl_id: "ENSG00000064393"
name: "homeodomain interacting protein kinase 2"
location: "7q34"
module: 98
arm: "+"
pooled_cpm: 243.6
n_lines_expressing: 45
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 21
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 10
direction_downstream: 19
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# HIPK2

*homeodomain interacting protein kinase 2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.64× (z +13.0, q 4e-36, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.260× (z -35.5, q 0e+00, down in 43 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STXBP5]] (+0.66, fdr 7e-06), [[DNER]] (+0.64, fdr 1e-05), [[IL1R1]] (+0.64, fdr 1e-05); moves opposite to [[CNNM4]] (-0.49, fdr 3e-04), [[CCDC85B]] (-0.48, fdr 3e-04), [[NR3C2]] (-0.48, fdr 4e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TBXAS1]] → it (grade B ⚠); 19 go from it, the strongest it → [[PLXNA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +13.0 | 4e-36 | 33/43 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +7.9 | 6e-13 | 28/43 (A-172, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +7.9 | 6e-13 | 28/43 (A498, A-172, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +7.4 | 3e-11 | 29/44 (HS-578T, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +7.1 | 2e-10 | 24/44 (A498, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.30×** | +6.9 | 7e-10 | 22/43 (A498, A-172, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.29×** | +6.7 | 1e-09 | 24/43 (A498, A-172, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +6.6 | 2e-09 | 24/43 (A-172, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +6.6 | 3e-09 | 21/39 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +6.2 | 4e-08 | 22/43 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +6.2 | 4e-08 | 22/43 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.25×** | +5.9 | 2e-07 | 22/43 (A-172, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.24×** | +5.6 | 9e-07 | 24/43 (A498, A-172, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.5 | 1e-06 | 23/43 (HEC-1-A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +5.3 | 4e-06 | 23/43 (A498, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.23×** | +5.3 | 4e-06 | 21/44 (A-172, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +5.2 | 6e-06 | 25/43 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.260×** | -35.5 | 0e+00 | 43/43 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.284×** | -33.2 | 0e+00 | 42/43 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.380×** | -25.5 | 0e+00 | 42/43 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -14.5 | 1e-45 | 30/44 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.636×** | -12.0 | 6e-31 | 34/43 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -11.8 | 6e-30 | 34/43 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -11.4 | 3e-28 | 33/42 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -11.4 | 3e-28 | 34/43 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -9.6 | 4e-20 | 33/45 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.574×** | -7.7 | 1e-12 | 37/43 (A549, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.755×** | -7.4 | 6e-12 | 32/44 (HOP62, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.587×** | -7.4 | 9e-12 | 32/44 (A549, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.765×** | -7.1 | 5e-11 | 28/44 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.797×** | -6.0 | 8e-08 | 26/43 (A549, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.814×** | -5.4 | 2e-06 | 24/43 (A549, J82, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.885× | -4.6 | 1e-04 | 12/43 (AsPC-1, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.867× | -3.8 | 0.004 | 14/43 (LoVo, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 497 | 31 (5 ⚠) | 7 | [[Clobetasol propionate (drug)]] 0.05 µM 2.65× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -24.8) |
| [[HS-578T (line)]] | alt | 473 | 24 | 9 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.87× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.110× (z -27.1) |
| [[LOX-IMVI (line)]] | wt | 468 | 19 (1 ⚠) | 9 (3 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.91× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.146× (z -28.3) |
| [[A-172 (line)]] | wt | 174 | 19 | 8 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.81× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.140× (z -26.9) |
| [[H4 (line)]] | wt | 483 | 18 | 9 (1 ⚠) | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 2.80× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -21.4) |
| [[NCI-H1792 (line)]] | alt | 567 | 19 | 6 (2 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.43× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.132× (z -24.7) |
| [[RPMI-7951 (line)]] | alt | 232 | 19 | 6 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 3.02× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -16.5) |
| [[hTERT-HPNE (line)]] | wt | 791 | 15 | 7 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.82× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.0826× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 259 | 14 | 7 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.08× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.181× (z -27.0) |
| [[SNU-423 (line)]] | alt | 258 | 17 (2 ⚠) | 3 | [[Triamcinolone (drug)]] 5 µM 1.84× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -18.0) |
| [[Hs 766T (line)]] | wt | 121 | 16 | 2 | [[Triamcinolone (drug)]] 5 µM 2.38× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.290× (z -12.4) |
| [[A549 (line)]] | wt | 415 | 0 | 15 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0761× (z -35.3) |
| [[HOP62 (line)]] | alt | 373 | 4 | 11 (2 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 2.16× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.156× (z -24.4) |
| [[J82 (line)]] | alt | 166 | 7 | 8 (2 ⚠) | [[Econazole (drug)]] 5 µM 2.04× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.236× (z -20.4) |
| [[SW 900 (line)]] | alt | 849 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0932× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 121 | 6 (2 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.75× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.370× (z -14.5) |
| [[RKO (line)]] | wt | 294 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -20.1) |
| [[BT-474 (line)]] | alt | 353 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.2) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.48× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -24.0) |
| [[LoVo (line)]] | wt | 182 | 2 | 6 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.90× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.297× (z -20.4) |
| [[C32 (line)]] | wt | 315 | 5 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.92× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.456× (z -9.7) |
| [[HT-29 (line)]] | alt | 83.1 | 4 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 3.59× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -12.3) |
| [[LS 180 (line)]] | wt | 215 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.269× (z -23.4) |
| [[PANC-1 (line)]] | alt | 209 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -20.3) |
| [[SK-MEL-2 (line)]] | alt | 311 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.17× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 217 | 3 (2 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.02× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 203 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.0) ⚠ cell-cycle shift, explains ~90% of this change | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -11.5) |
| [[KATO III (line)]] | alt | 141 | 3 (1 ⚠) | 3 | [[Bortezomib (drug)]] 0.05 µM 2.34× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.230× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 212 | 1 | 4 | [[Auranofin (drug)]] 5 µM 3.15× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.174× (z -18.9) |
| [[NCI-H2347 (line)]] | alt | 194 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.13× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -17.6) |
| [[C-33 A (line)]] | alt | 116 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.284× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 120 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -19.4) |
| [[Panc 03.27 (line)]] | alt | 87.0 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.73× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -12.6) |
| [[SW480 (line)]] | alt | 225 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -23.8) |
| [[SHP-77 (line)]] | alt | 194 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -18.3) |
| [[SNU-1 (line)]] | wt | 158 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -13.7) |
| [[SW 1088 (line)]] | alt | 586 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -11.4) |
| [[SW48 (line)]] | wt | 208 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -14.2) |
| [[AN3 CA (line)]] | alt | 295 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -10.4) |
| [[CHP-212 (line)]] | wt | 154 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.6) ⚠ cell-cycle shift, explains ~90% of this change | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -9.7) |
| [[COLO 205 (line)]] | alt | 177 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -12.0) |
| [[HCT15 (line)]] | alt | 110 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.67× (z +9.6) | — |
| [[A-427 (line)]] | wt | 51.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DNER]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[IL1R1]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ADPRHL1]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PID1]] | +0.61 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[TBXAS1]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ABLIM3]] | +0.59 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TRMT6]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ITGA10]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[FKBP5]] | +0.58 | +0.62 / +0.44 | both halves | 3e-05 | pathway: Transcriptional Regulation by MECP2 |
| [[MAOA]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[VSTM2L]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TMTC1]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM4]] | -0.49 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[CCDC85B]] | -0.48 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[NR3C2]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[TNFRSF11A]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ANKRD37]] | -0.47 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[AFTPH]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PPP1R14B]] | -0.46 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CDS1]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[C1QL1]] | -0.45 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[NPTX1]] | -0.45 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[FRMD5]] | -0.44 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[FBXO34]] | -0.44 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBXAS1]] | B | TBXAS1 activity raises HIPK2's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 3.24× lower at baseline in the lines without TBXAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[PLXNA2]] | B | PLXNA2 activity raises HIPK2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without PLXNA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[HS3ST3B1]] | B | HS3ST3B1 activity raises HIPK2's level | lines that do not express HS3ST3B1 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without HS3ST3B1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ADAMTS9]] | B | ADAMTS9 activity raises HIPK2's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without ADAMTS9 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[NR3C1]] | B | NR3C1 activity raises HIPK2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TLR2]] | B | TLR2 activity raises HIPK2's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.63× lower at baseline in the lines without TLR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[MYO1B]] | B | MYO1B activity raises HIPK2's level | lines that do not express MYO1B (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without MYO1B | 0.091 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| [[PID1]] | B | PID1 activity raises HIPK2's level | lines that do not express PID1 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without PID1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[TOP2A]] | B | TOP2A activity raises HIPK2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TBXAS1]] | C | TBXAS1 activity strengthens HIPK2's drug response | lines that do not express TBXAS1 (4) vs lines expressing it (41) | the lines without TBXAS1 respond 0.57× as strongly (z diff +2.94); strongest at Topotecan (hydrochloride) 5 µM: 0.97x vs 0.59x (z diff +5.7) | 0.020 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | HIPK2 activity raises PLXNA2's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 4.84× lower at baseline in the lines without HIPK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[LAMB1]] | B | HIPK2 activity raises LAMB1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.37× lower at baseline in the lines without HIPK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[MYO1B]] | B | HIPK2 activity raises MYO1B's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without HIPK2 | 0.020 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[MGST1]] | B | HIPK2 activity raises MGST1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.66× lower at baseline in the lines without HIPK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 0.05 µM | B | HIPK2 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.36× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[ABLIM3]] | B | HIPK2 activity raises ABLIM3's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.37× lower at baseline in the lines without HIPK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[TBXAS1]] | B | HIPK2 activity raises TBXAS1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 2.86× lower at baseline in the lines without HIPK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[DUSP1]] | B | HIPK2 activity raises DUSP1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without HIPK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | HIPK2 activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.34× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| cells under [[Futibatinib (drug)]] 0.5 µM | B | HIPK2 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.29× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| cells under [[AZD1390 (drug)]] 5 µM | B | HIPK2 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.46× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 5 µM | B | HIPK2 activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 5 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.18× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 16.1); signed map (18.4, 32.5). **Vector** length 138, 45.4% of its response variance represented; |z| ≥ 3 in 1,994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +13.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +9.9 | +7.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +8.3 | +7.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +8.1 | +6.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +7.9 | +4.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -11.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -11.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.0 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | homeodomain interacting protein kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,561,570-139,777,998 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Homeodomain interacting protein kinase family |
| Hallmark sets | TGF_BETA_SIGNALING, IL2_STAT5_SIGNALING |
| Reactome | 14 pathways, smallest: Physiological factors; YAP1- and WWTR1 (TAZ)-stimulated gene expression; Regulation of MECP2 expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2X6](https://www.uniprot.org/uniprotkb/Q9H2X6) (Homeodomain-interacting protein kinase 2):

> Serine/threonine-protein kinase involved in transcription regulation, p53/TP53-mediated cellular apoptosis and regulation of the cell cycle. Acts as a corepressor of several transcription factors, including SMAD1 and POU4F1/Brn3a and probably NK homeodomain transcription factors. Phosphorylates PDX1, ATF1, PML, p53/TP53, CREB1, CTBP1, CBX4, RUNX1, EP300, CTNNB1, HMGA1, ZBTB4 and DAZAP2. Inhibits cell growth and promotes apoptosis through the activation of p53/TP53 both at the transcription …

**Summary**, from NCBI Gene [28996](https://www.ncbi.nlm.nih.gov/gene/28996):

> This gene encodes a conserved serine/threonine kinase that is a member of the homeodomain-interacting protein kinase family. The encoded protein interacts with homeodomain transcription factors and many other transcription factors such as p53, and can function as both a corepressor and a coactivator depending on the transcription factor and its subcellular localization. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:14402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14402) · Entrez [28996](https://www.ncbi.nlm.nih.gov/gene/28996) · UniProt [Q9H2X6](https://www.uniprot.org/uniprotkb/Q9H2X6) · Ensembl [ENSG00000064393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064393)

## Data

Gene col 745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 745); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 745]; `tensor/DDL_lfc|DDL_z.npy` [745]; `embed/gene_vectors.npy` [745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 745 or target_col == 745). Every well: [[HIPK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIPK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
