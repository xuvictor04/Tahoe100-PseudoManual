---
symbol: "TMED10"
type: "gene"
col: 9939
ensembl_id: "ENSG00000170348"
name: "transmembrane p24 trafficking protein 10"
location: "14q24.3"
module: 42
arm: "+"
pooled_cpm: 108.96
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMED10

*transmembrane p24 trafficking protein 10* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.85× (z +13.3, q 1e-37, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.33× (z +3.2, q 0.073, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A549 3.29×, KATO III 2.28×, NCI-H1792 2.45×, SK-MEL-2 2.59×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C32 3.24×, NCI-H460 2.36×, A498 2.47×, SW480 1.92×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (SW480 1.21×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.488× (z -22.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDOST]] (+0.80, fdr 7e-06), [[PDIA6]] (+0.75, fdr 7e-06), [[LMAN2]] (+0.74, fdr 7e-06); moves opposite to [[CCDC137]] (-0.63, fdr 7e-06), [[PLEKHN1]] (-0.60, fdr 2e-05), [[CLCF1]] (-0.56, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9939.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A549 3.29×, KATO III 2.28×, NCI-H1792 2.45×, SK-MEL-2 2.59×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C32 3.24×, NCI-H460 2.36×, A498 2.47×, SW480 1.92×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (SW480 1.21×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +13.3 | 1e-37 | 41/49 (A549, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +12.3 | 4e-32 | 12/50 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +12.0 | 6e-31 | 37/44 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +11.1 | 1e-26 | 38/45 (SHP-77, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.4 | 7e-06 | 24/38 (HT-29, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +4.5 | 6e-04 | 20/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.22×** | +4.4 | 9e-04 | 26/48 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.22×** | +4.3 | 0.001 | 27/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.073 | 18/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lipoic acid (drug)]] 5 µM |  | 1.11× | +3.2 | 0.073 | 8/48 (PANC-1, HT-29, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.16× | +3.2 | 0.073 | 13/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.16× | +3.0 | 0.11 | 13/49 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | 1.15× | +3.0 | 0.11 | 17/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +3.0 | 0.11 | 15/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.488×** | -22.0 | 0e+00 | 47/48 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -9.5 | 9e-19 | 37/48 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.684×** | -7.9 | 4e-13 | 39/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.697×** | -7.8 | 6e-13 | 42/48 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.712×** | -7.4 | 2e-11 | 35/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.724×** | -7.0 | 2e-10 | 34/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.731×** | -6.8 | 8e-10 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.745×** | -6.4 | 1e-08 | 36/48 (LS 180, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -5.6 | 1e-06 | 30/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -5.4 | 4e-06 | 23/48 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.7 | 1e-04 | 30/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.808×** | -4.6 | 2e-04 | 26/48 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.811×** | -4.4 | 5e-04 | 23/47 (LoVo, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.823×** | -4.2 | 9e-04 | 22/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.831×** | -4.0 | 0.002 | 23/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.847× | -3.5 | 0.017 | 14/47 (LS 180, hTERT-HPNE, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.066 | 12/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 162 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -17.3) |
| [[LS 180 (line)]] | wt | 168 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -19.1) |
| [[SW480 (line)]] | alt | 114 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -17.8) |
| [[A549 (line)]] | wt | 82.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.4) |
| [[LoVo (line)]] | wt | 99.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.427× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 95.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.41× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 139 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -8.8) |
| [[HOP62 (line)]] | alt | 112 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -15.0) |
| [[HT-29 (line)]] | alt | 96.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -21.6) |
| [[J82 (line)]] | alt | 74.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 148 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -28.2) |
| [[NCI-H2347 (line)]] | alt | 187 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 91.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 114 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.1) |
| [[SW1417 (line)]] | alt | 104 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.05× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -14.1) |
| [[A498 (line)]] | wt | 69.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 154 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 93.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 93.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 128 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 52.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 122 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -13.3) |
| [[PANC-1 (line)]] | alt | 70.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -10.8) |
| [[SHP-77 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.59× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 152 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -22.7) |
| [[SW48 (line)]] | wt | 153 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -8.5) |
| [[A-172 (line)]] | wt | 61.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 54.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.7) |
| [[C-33 A (line)]] | alt | 79.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.3) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 218 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.8) |
| [[RKO (line)]] | wt | 82.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 98.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.2) |
| [[SNU-1 (line)]] | wt | 84.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.9) |
| [[SW 1088 (line)]] | alt | 140 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0792× (z -11.0) |
| [[A-427 (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDOST]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 646 |
| [[PDIA6]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | STRING 642 |
| [[LMAN2]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 839 |
| [[RPN1]] | +0.72 | +0.74 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 607 |
| [[PDIA3]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[ATP6AP2]] | +0.70 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[STT3A]] | +0.70 | +0.69 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 464 |
| [[TMED2]] | +0.68 | +0.71 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_PROTEIN_SECRETION; STRING 999 |
| [[PDIA4]] | +0.66 | +0.74 / +0.63 | both halves | 7e-06 | STRING 487 |
| [[SSR1]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 | STRING 693 |
| [[ATP5F1B]] | +0.65 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.64 | +0.67 / +0.68 | both halves | 7e-06 | STRING 922 |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC137]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[PLEKHN1]] | -0.60 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CLCF1]] | -0.56 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RBMXL1]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SURF6]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[DNTTIP2]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZNF611]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[DAXX]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PWP2]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[LLPH]] | -0.53 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[RFFL]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TNIP2]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TMED10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TMED10's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.2, -21.8); signed map (-55.9, 6.5). **Vector** length 121, 37.6% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.57 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.59 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.59 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.5 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.0 | -7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,131,469-75,176,612 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMP21, P24(DELTA), p24d1, p24delta1, p23 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 11 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P49755](https://www.uniprot.org/uniprotkb/P49755) (Transmembrane emp24 domain-containing protein 10):

> Cargo receptor involved in protein vesicular trafficking and quality control in the endoplasmic reticulum (ER) and Golgi. The p24 protein family is a group of transmembrane proteins that bind coat protein complex I/COPI and coat protein complex II/COPII involved in vesicular trafficking between the membranes. Acts at the lumenal side for incorporation of secretory cargo molecules into transport vesicles and involved in vesicle coat formation at the cytoplasmic side. Mainly functions in the …

**Summary**, from NCBI Gene [10972](https://www.ncbi.nlm.nih.gov/gene/10972):

> This gene is a member of the EMP24/GP25L/p24 family and encodes a protein with a GOLD domain. This type I membrane protein is localized to the plasma membrane and golgi cisternae and is involved in vesicular protein trafficking. The protein is also a member of a heteromeric secretase complex and regulates the complex's gamma-secretase activity without affecting its epsilon-secretase activity. Mutations in this gene have been associated with early-onset familial Alzheimer's disease. This gene …

**Accessions** — [HGNC:16998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16998) · Entrez [10972](https://www.ncbi.nlm.nih.gov/gene/10972) · UniProt [P49755](https://www.uniprot.org/uniprotkb/P49755) · Ensembl [ENSG00000170348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170348)

## Data

Gene col 9939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9939); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9939]; `tensor/DDL_lfc|DDL_z.npy` [9939]; `embed/gene_vectors.npy` [9939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9939 or target_col == 9939). Every well: [[TMED10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
