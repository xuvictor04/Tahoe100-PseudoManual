---
symbol: "MYO1B"
type: "gene"
col: 4907
ensembl_id: "ENSG00000128641"
name: "myosin IB"
location: "2q32.3"
module: 113
arm: "+"
pooled_cpm: 170.35
n_lines_expressing: 43
n_dd_up: 10
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MYO1B

*myosin IB* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.82× (z +5.9, q 2e-06, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.427× (z -15.4, q 0e+00, down in 40 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.590× (z -14.0, q 4e-42, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53BP2]] (+0.53, fdr 6e-05), [[UBE2E2]] (+0.52, fdr 2e-05), [[TANC2]] (+0.51, fdr 1e-05); moves opposite to [[KLC4]] (-0.52, fdr 3e-05), [[IP6K1]] (-0.46, fdr 3e-05), [[STAG3L4-1]] (-0.45, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HIPK2]] → it (grade B ⚠); 6 go from it, the strongest it → [[FAH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +5.9 | 2e-06 | 27/42 (Hs 766T, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 3e-06 | 27/41 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.4 | 1e-05 | 22/42 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.4 | 1e-05 | 25/41 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.6 | 6e-04 | 24/41 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.002 | 21/41 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.003 | 20/41 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +3.7 | 0.017 | 19/41 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.033 | 18/41 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.4 | 0.036 | 13/41 (Panc 03.27, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.098 | 18/41 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.098 | 8/41 (SW480, KATO III, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.100 | 19/41 (SK-MEL-2, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.427×** | -15.4 | 0e+00 | 40/41 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -14.0 | 4e-42 | 35/42 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.578×** | -10.3 | 1e-22 | 32/41 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -10.1 | 8e-22 | 35/41 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -8.5 | 2e-15 | 25/41 (RKO, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.702×** | -6.6 | 3e-09 | 26/41 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.707×** | -6.5 | 7e-09 | 29/41 (SW1417, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.724×** | -6.1 | 1e-07 | 23/42 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.739×** | -5.7 | 9e-07 | 31/42 (SW1417, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -5.6 | 2e-06 | 24/41 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -5.1 | 1e-05 | 1/43 (NCI-H23) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -5.0 | 2e-05 | 25/41 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -4.9 | 5e-05 | 23/39 (CFPAC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.795×** | -4.1 | 0.001 | 22/43 (hTERT-HPNE, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.799×** | -4.0 | 0.002 | 20/38 (NCI-H1573, CFPAC-1, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.814×** | -3.9 | 0.004 | 23/41 (BT-474, HS-578T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.816×** | -3.8 | 0.005 | 20/41 (PANC-1, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.759×** | -3.7 | 0.007 | 27/41 (C32, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.766×** | -3.6 | 0.011 | 22/41 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.872× | -3.5 | 0.015 | 12/42 (SW480, RKO, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.775×** | -3.4 | 0.018 | 17/41 (SW 1271, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 226 | 17 | 2 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.30× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 307 | 0 | 9 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.220× (z -17.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 331 | 4 (1 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.20× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 331 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.378× (z -10.7) |
| [[A549 (line)]] | wt | 361 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +15.5) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.67× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -21.9) |
| [[NCI-H1573 (line)]] | alt | 298 | 1 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.12× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -17.2) |
| [[RKO (line)]] | wt | 180 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0813× (z -27.1) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.229× (z -22.5) |
| [[SNU-423 (line)]] | alt | 235 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -13.7) |
| [[SW480 (line)]] | alt | 146 | 4 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.45× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -10.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.552× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 167 | 2 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.08× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 397 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.3) |
| [[A498 (line)]] | wt | 185 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.59× (z +16.9) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.60× (z +10.6) | — |
| [[C32 (line)]] | wt | 161 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.77× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -15.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.456× (z -8.7) |
| [[HCT15 (line)]] | alt | 236 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.2) |
| [[Hs 766T (line)]] | wt | 140 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 189 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.96× (z +16.7) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.35× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -10.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 111 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.8) | — |
| [[H4 (line)]] | wt | 290 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.372× (z -9.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.2) |
| [[HOP62 (line)]] | alt | 301 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -11.5) |
| [[PANC-1 (line)]] | alt | 85.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +17.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.24× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 261 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -14.3) |
| [[BT-474 (line)]] | alt | 287 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.2) |
| [[J82 (line)]] | alt | 178 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.96× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.8) |
| [[KATO III (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 79.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.8) |
| [[SW48 (line)]] | wt | 189 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.4) |
| [[CHP-212 (line)]] | wt | 165 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 310 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -9.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 119 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.73× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 179 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.66× (z +10.1) | — |
| [[A-172 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 268 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 80.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53BP2]] | +0.53 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[UBE2E2]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TANC2]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.50 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[PGM2]] | +0.49 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[FAH]] | +0.49 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[CCBE1]] | +0.48 | +0.36 / +0.44 | both halves | 9e-05 |  |
| [[FABP5]] | +0.48 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[HPSE]] | +0.48 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[PALM2AKAP2]] | +0.47 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[PAM]] | +0.47 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[SNAI2]] | +0.46 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC4]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[IP6K1]] | -0.46 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[STAG3L4-1]] | -0.45 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[STX5]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[CWC25]] | -0.45 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SLC35D2]] | -0.44 | -0.21 / -0.48 | both halves | 6e-04 |  |
| [[ATG13]] | -0.44 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[L3MBTL1]] | -0.44 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SLC30A5]] | -0.43 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[ASPSCR1]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[OSBPL2]] | -0.43 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[TTI2]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIPK2]] | B | HIPK2 activity raises MYO1B's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 2.40× lower at baseline in the lines without HIPK2 | 0.020 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[ADAMTS9]] | B | ADAMTS9 activity raises MYO1B's level | lines that do not express ADAMTS9 (18) vs lines expressing it (32) | 2.01× lower at baseline in the lines without ADAMTS9 | 0.034 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2 |
| [[ADAMTS9]] | B | ADAMTS9 activity strengthens MYO1B's drug response | lines that do not express ADAMTS9 (14) vs lines expressing it (28) | the lines without ADAMTS9 respond 0.47× as strongly (z diff +2.60); strongest at Dinaciclib 0.5 µM: 1.10x vs 0.62x (z diff +5.5) | 0.046 | ⚠ within organs, on part of the lines; also absent: PRICKLE2, FRMPD4, ADAMTS9-AS2; target measured in part of the lines; artifact flags |
| [[SNAI2]] | B | SNAI2 activity raises MYO1B's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without SNAI2 | 0.071 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAH]] | B | MYO1B activity raises FAH's level | lines that do not express MYO1B (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without MYO1B | 0.035 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| [[DIAPH2]] | B | MYO1B activity raises DIAPH2's level | lines that do not express MYO1B (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without MYO1B | 0.065 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | MYO1B activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express MYO1B (7) vs lines expressing it (41) | the lines without MYO1B: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| [[HIPK2]] | B | MYO1B activity raises HIPK2's level | lines that do not express MYO1B (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without MYO1B | 0.091 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | MYO1B activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express MYO1B (7) vs lines expressing it (41) | the lines without MYO1B: 0.81× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | MYO1B activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express MYO1B (7) vs lines expressing it (41) | the lines without MYO1B: 0.86× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.406). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, 10.6); signed map (16.5, 36.9). **Vector** length 120, 38.6% of its response variance represented; |z| ≥ 3 in 1,342 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.3 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | -15.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -5.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -8.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | myosin IB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:191,245,185-191,425,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | myr1 |
| Gene groups (HGNC) | Myosin heavy chains, class I |
| Matched by | ensembl_id |

**Function**, from UniProt [O43795](https://www.uniprot.org/uniprotkb/O43795) (Unconventional myosin-Ib):

> Motor protein that may participate in process critical to neuronal development and function such as cell migration, neurite outgrowth and vesicular transport.

**Summary**, from NCBI Gene [4430](https://www.ncbi.nlm.nih.gov/gene/4430):

> Enables ATP binding activity; actin filament binding activity; and microfilament motor activity. Involved in actin filament organization and post-Golgi vesicle-mediated transport. Located in several cellular components, including actin filament; endosome; and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7596) · Entrez [4430](https://www.ncbi.nlm.nih.gov/gene/4430) · UniProt [O43795](https://www.uniprot.org/uniprotkb/O43795) · Ensembl [ENSG00000128641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128641)

## Data

Gene col 4907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4907); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4907]; `tensor/DDL_lfc|DDL_z.npy` [4907]; `embed/gene_vectors.npy` [4907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4907 or target_col == 4907). Every well: [[MYO1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
