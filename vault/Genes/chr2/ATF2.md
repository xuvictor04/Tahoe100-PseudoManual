---
symbol: "ATF2"
type: "gene"
col: 3744
ensembl_id: "ENSG00000115966"
name: "activating transcription factor 2"
location: "2q31.1"
module: 45
arm: "+"
pooled_cpm: 180.41
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ATF2

*activating transcription factor 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +9.7, q 2e-19, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.456× (z -14.8, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.617× (z -9.1, q 1e-17, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HELZ]] (+0.64, fdr 7e-06), [[DCAF6]] (+0.62, fdr 7e-06), [[RNASE4]] (+0.61, fdr 1e-05); moves opposite to [[TNFRSF12A]] (-0.56, fdr 1e-05), [[ZNF562]] (-0.56, fdr 1e-05), [[METTL2B]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +9.7 | 2e-19 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.61×** | +9.5 | 8e-19 | 47/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +8.8 | 2e-16 | 45/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 7e-04 | 23/48 (SK-MEL-2, LoVo, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.0 | 0.008 | 26/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.057 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.12 | 18/48 (J82, HOP62, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.14 | 21/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.456×** | -14.8 | 0e+00 | 47/49 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.449×** | -14.5 | 3e-45 | 43/44 (NCI-H1573, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.563×** | -10.0 | 3e-21 | 37/45 (RKO, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.597×** | -9.3 | 1e-18 | 46/47 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -9.1 | 1e-17 | 45/48 (SW 900, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.693×** | -6.9 | 4e-10 | 36/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.695×** | -6.8 | 6e-10 | 32/48 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.731×** | -5.9 | 3e-07 | 32/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -5.7 | 9e-07 | 35/48 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.763×** | -5.1 | 2e-05 | 26/48 (H4, SW 900, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.767×** | -5.0 | 3e-05 | 37/48 (CFPAC-1, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.776×** | -4.8 | 9e-05 | 29/48 (Panc 03.27, NCI-H661, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.801×** | -4.2 | 0.001 | 26/48 (SW48, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.855× | -4.1 | 0.001 | 15/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -3.7 | 0.010 | 16/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -3.5 | 0.016 | 24/48 (SW 1088, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 199 | 7 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 183 | 6 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 229 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.63× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 192 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 197 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.449× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 145 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.307× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 202 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 117 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 372 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 135 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.382× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 170 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +23.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.82× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 214 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -8.7) |
| [[SW 900 (line)]] | alt | 293 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -8.9) |
| [[A-427 (line)]] | wt | 152 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.36× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 237 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 194 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -19.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 233 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 243 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 173 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 89.8 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 148 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 242 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 242 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 157 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.499× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 177 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.89× (z +8.9) | [[Auranofin (drug)]] 5 µM 0.581× (z -8.6) |
| [[AN3 CA (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.443× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 169 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 267 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.487× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -9.1) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 211 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELZ]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[DCAF6]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 | same gene group |
| [[RNASE4]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TFG]] | +0.59 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[COPS4]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PRCP]] | +0.56 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[PHF21A]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[DNASE2]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[SSBP2]] | +0.56 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[TRA2A]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MARCHF6]] | +0.55 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.56 | -0.57 / -0.59 | both halves | 1e-05 | same gene group |
| [[METTL2B]] | -0.55 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ZNF83]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 | same gene group |
| [[BMAL2]] | -0.53 | -0.54 / -0.38 | both halves | 6e-05 | pathway: Circadian clock |
| [[RRP7A]] | -0.53 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[FAM83H]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 | same gene group |
| [[PUS1]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.52 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ACSF3]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[MDFI]] | -0.51 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[MPHOSPH6]] | -0.51 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.3, -37.6); signed map (-24.6, 16.9). **Vector** length 101, 35.8% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.1 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | -1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -9.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:175,072,250-175,168,382 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TREB7, CRE-BP1, HB16; previously CREB2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; MicroRNA protein coding host genes; Activating transcription factor 2 family |
| Reactome | 50 pathways, smallest: Activation of the AP-1 family of transcription factors; MAPK targets/ Nuclear events mediated by MAP kinases; Expression of BMAL (ARNTL), CLOCK, and NPAS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P15336](https://www.uniprot.org/uniprotkb/P15336) (Cyclic AMP-dependent transcription factor ATF-2):

> Transcriptional activator which regulates the transcription of various genes, including those involved in anti-apoptosis, cell growth, and DNA damage response. Dependent on its binding partner, binds to CRE (cAMP response element) consensus sequences (5'-TGACGTCA-3') or to AP-1 (activator protein 1) consensus sequences (5'-TGACTCA-3'). In the nucleus, contributes to global transcription and the DNA damage response, in addition to specific transcriptional activities that are related to cell …

**Summary**, from NCBI Gene [1386](https://www.ncbi.nlm.nih.gov/gene/1386):

> This gene encodes a transcription factor that is a member of the leucine zipper family of DNA binding proteins. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions This protein binds to the cAMP-responsive element (CRE), an octameric palindrome. It forms a homodimer or a heterodimer with c-Jun and stimulates CRE-dependent transcription. This protein is also a histone acetyltransferase (HAT) that specifically …

**Accessions** — [HGNC:784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:784) · Entrez [1386](https://www.ncbi.nlm.nih.gov/gene/1386) · UniProt [P15336](https://www.uniprot.org/uniprotkb/P15336) · Ensembl [ENSG00000115966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115966)

## Data

Gene col 3744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3744); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3744]; `tensor/DDL_lfc|DDL_z.npy` [3744]; `embed/gene_vectors.npy` [3744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3744 or target_col == 3744). Every well: [[ATF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
