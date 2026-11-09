---
symbol: "TES"
type: "gene"
col: 5673
ensembl_id: "ENSG00000135269"
name: "testin LIM domain protein"
location: "7q31.2"
module: 106
arm: "+"
pooled_cpm: 206.56
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# TES

*testin LIM domain protein* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.02× (z +17.5, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.634× (z -16.1, q 0e+00, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP2]] (+0.61, fdr 3e-05), [[EZR]] (+0.59, fdr 1e-05), [[ANXA2]] (+0.58, fdr 1e-05); moves opposite to [[RABEP2]] (-0.53, fdr 2e-05), [[CDAN1]] (-0.44, fdr 3e-05), [[ZNF500]] (-0.44, fdr 1e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MYO5B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ADAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +17.5 | 0e+00 | 38/40 (LoVo, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +13.0 | 3e-36 | 32/40 (A-427, LoVo, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +11.0 | 7e-26 | 31/40 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.30×** | +9.1 | 9e-18 | 24/40 (LoVo, A549, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +8.8 | 2e-16 | 29/40 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.42×** | +8.8 | 2e-16 | 29/40 (COLO 205, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +7.4 | 8e-12 | 22/41 (COLO 205, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.33×** | +6.8 | 5e-10 | 25/40 (A549, A-427, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +6.8 | 9e-10 | 21/38 (AsPC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 4e-09 | 24/40 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.30×** | +6.5 | 6e-09 | 24/40 (COLO 205, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +6.4 | 8e-09 | 26/40 (COLO 205, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +6.2 | 3e-08 | 20/40 (A549, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +5.9 | 2e-07 | 22/41 (SW48, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.20×** | +4.6 | 1e-04 | 17/40 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +4.4 | 4e-04 | 16/40 (COLO 205, C32, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.6 | 0.009 | 14/40 (SW480, KATO III, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.012 | 16/40 (SW480, KATO III, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.4 | 0.015 | 7/40 (A-427, SHP-77, …) | two highest doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +3.1 | 0.042 | 13/40 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.064 | 11/40 (RKO, SHP-77, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.088 | 13/40 (COLO 205, BT-474, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -16.1 | 0e+00 | 31/41 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -10.7 | 2e-24 | 31/40 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.772×** | -6.2 | 1e-07 | 23/40 (HT-29, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.802×** | -5.5 | 5e-06 | 21/40 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.757×** | -5.0 | 8e-05 | 22/40 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.873× | -4.8 | 2e-04 | 14/40 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.826×** | -4.8 | 2e-04 | 20/40 (BT-474, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.842× | -4.3 | 0.001 | 18/40 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.847× | -4.2 | 0.002 | 15/40 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.866× | -3.6 | 0.020 | 16/40 (BT-474, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.874× | -3.4 | 0.037 | 17/40 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.874× | -3.4 | 0.037 | 9/40 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.879× | -3.2 | 0.060 | 10/40 (PANC-1, BT-474, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.884× | -3.1 | 0.078 | 9/40 (SW 900, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -3.1 | 0.078 | 7/40 (LoVo, SW480, …) | top dose only | plate-row cell shift |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.886× | -3.0 | 0.087 | 4/40 (LoVo, LS 180, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.887× | -3.0 | 0.087 | 9/40 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.888× | -3.0 | 0.088 | 8/40 (AsPC-1, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 306 | 7 (5 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.56× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -20.4) |
| [[HT-29 (line)]] | alt | 470 | 1 | 8 (7 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -17.5) |
| [[SW48 (line)]] | wt | 306 | 6 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.02× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 121 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 170 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -11.1) |
| [[A549 (line)]] | wt | 160 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 323 | 4 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.7) ⚠ cell-cycle shift, explains ~63% of this change | [[Panobinostat (drug)]] 5 µM 0.395× (z -11.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 128 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +16.0) | — |
| [[NCI-H1792 (line)]] | alt | 154 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.73× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 217 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +11.7) | — |
| [[A498 (line)]] | wt | 195 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.03× (z +15.2) | — |
| [[BT-474 (line)]] | alt | 196 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.35× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -17.8) |
| [[C32 (line)]] | wt | 155 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 165 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.42× (z +11.4) ⚠ toxic · without an alert: [[Peretinoin (drug)]] 5 µM 2.58× (z +8.8) | — |
| [[KATO III (line)]] | alt | 585 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 777 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.535× (z -11.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SW480 (line)]] | alt | 215 | 2 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.96× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 358 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -21.6) |
| [[LS 180 (line)]] | wt | 323 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.38× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 91.0 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.29× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.5) |
| [[HOP62 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.72× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 413 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.89× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 321 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -12.6) |
| [[HCT15 (line)]] | alt | 198 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -9.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 111 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 265 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.63× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 295 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -14.3) |
| [[RKO (line)]] | wt | 72.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 113 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 187 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +10.1) | — |
| [[A-172 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 230 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2]] | +0.61 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[EZR]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[DSEL]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[ANXA1]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[KRT80]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[AIG1]] | +0.51 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[KRT7]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PDLIM1]] | +0.49 | +0.37 / +0.51 | both halves | 8e-05 | same gene group |
| [[ZFAND5]] | +0.48 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[SLC38A4-AS1]] | +0.48 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[FGD4]] | +0.48 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABEP2]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CDAN1]] | -0.44 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ZNF500]] | -0.44 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[CEP43]] | -0.43 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[POLR2F]] | -0.43 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[SPG7]] | -0.43 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD13D]] | -0.42 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[STARD3]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DNLZ]] | -0.42 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ATPAF2]] | -0.42 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[WDR20]] | -0.41 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[LIN52]] | -0.41 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5B]] | B | MYO5B activity raises TES's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without MYO5B | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[KLF5]] | B | KLF5 activity raises TES's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 3.53× lower at baseline in the lines without KLF5 | 0.006 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[LMO7]] | B | LMO7 activity raises TES's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 2.96× lower at baseline in the lines without LMO7 | 0.022 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[PDLIM1]] | B | PDLIM1 activity raises TES's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 3.22× lower at baseline in the lines without PDLIM1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[ANXA3]] | B | ANXA3 activity raises TES's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without ANXA3 | 0.035 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[EPS8]] | B | EPS8 activity raises TES's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without EPS8 | 0.051 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[KRT7]] | B | KRT7 activity raises TES's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without KRT7 | 0.056 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[MET]] | B | MET activity raises TES's level | lines that do not express MET (9) vs lines expressing it (41) | 3.69× lower at baseline in the lines without MET | 0.087 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[IL18]] | B | IL18 activity raises TES's level | lines that do not express IL18 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without IL18 | 0.095 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[UCHL1]] | B | UCHL1 activity lowers TES's level | lines that do not express UCHL1 (29) vs lines expressing it (21) | 1.78× higher at baseline in the lines without UCHL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NEFL, ADD2, CDH4 |
| [[KRT80]] | B | KRT80 activity raises TES's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 2.59× lower at baseline in the lines without KRT80 | 0.099 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAT3]] | B | TES activity lowers ADAT3's level | lines that do not express TES (8) vs lines expressing it (42) | 1.18× higher at baseline in the lines without TES | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM241A, GPR39, TBC1D8B; its own permutation p |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.362). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, 58.3); signed map (-0.1, 24.2). **Vector** length 141, 46.3% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +17.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +13.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.0 | +6.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -16.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -10.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.8 | -4.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Ritonavir (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | testin LIM domain protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:116,210,506-116,258,783 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586B2022, TESS-2, TESTIN |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | HYPOXIA, MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGI8](https://www.uniprot.org/uniprotkb/Q9UGI8) (Testin):

> Scaffold protein that may play a role in cell adhesion, cell spreading and in the reorganization of the actin cytoskeleton. Plays a role in the regulation of cell proliferation. May act as a tumor suppressor. Inhibits tumor cell growth.

**Summary**, from NCBI Gene [26136](https://www.ncbi.nlm.nih.gov/gene/26136):

> Cancer-associated chromosomal changes often involve regions containing fragile sites. This gene maps to a common fragile site on chromosome 7q31.2 designated FRA7G. This gene is similar to mouse Testin, a testosterone-responsive gene encoding a Sertoli cell secretory protein containing three LIM domains. LIM domains are double zinc-finger motifs that mediate protein-protein interactions between transcription factors, cytoskeletal proteins and signaling proteins. This protein is a negative …

**Accessions** — [HGNC:14620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14620) · Entrez [26136](https://www.ncbi.nlm.nih.gov/gene/26136) · UniProt [Q9UGI8](https://www.uniprot.org/uniprotkb/Q9UGI8) · Ensembl [ENSG00000135269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135269)

## Data

Gene col 5673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5673); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5673]; `tensor/DDL_lfc|DDL_z.npy` [5673]; `embed/gene_vectors.npy` [5673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5673 or target_col == 5673). Every well: [[TES — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TES.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
