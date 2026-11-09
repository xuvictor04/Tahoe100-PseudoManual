---
symbol: "ENAH"
type: "gene"
col: 7804
ensembl_id: "ENSG00000154380"
name: "ENAH actin regulator"
location: "1q42.12"
module: 216
arm: "+"
pooled_cpm: 208.24
n_lines_expressing: 47
n_dd_up: 42
n_dd_down: 3
n_dd_up_clean: 33
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# ENAH

*ENAH actin regulator* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +22.8, q 0e+00, up in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +20.7, q 0e+00, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.830× (z -5.9, q 3e-06, down in 21 of 45 measured lines) ⚠ cell-cycle shift, explains ~6% of this change. The strongest without an alert is [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM: 0.871× (z -4.3, q 0.004, down in 11 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HepG2/C3A 0.405×, C-33 A 0.610×, CHP-212 0.449×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 0.430×, RKO 0.450×, SW48 0.578×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 3 lines (BT-474 0.371×, SK-MEL-2 0.528×, C-33 A 0.583×; ⚠ cell-cycle shift, explains ~6% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNN3]] (+0.60, fdr 1e-05), [[ABCC4]] (+0.60, fdr 1e-05), [[TNPO1]] (+0.59, fdr 2e-05); moves opposite to [[CCNT1]] (-0.58, fdr 1e-05), [[C16orf46]] (-0.57, fdr 5e-05), [[PPIL3]] (-0.55, fdr 1e-05).
> It is in [[Module 216]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALCAM]] → it (grade B ⚠); 3 go from it, the strongest it → [[TNPO1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 73 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +22.8 | 0e+00 | 38/46 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +20.7 | 0e+00 | 33/45 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +18.0 | 0e+00 | 35/42 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +16.3 | 0e+00 | 36/44 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +16.3 | 0e+00 | 36/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +16.3 | 0e+00 | 36/43 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +14.0 | 7e-43 | 34/45 (CFPAC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +13.9 | 3e-42 | 41/45 (RKO, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +13.8 | 2e-41 | 40/45 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +13.5 | 1e-39 | 38/45 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +13.2 | 5e-38 | 31/45 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +13.0 | 3e-37 | 39/45 (RKO, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +12.0 | 1e-31 | 33/45 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +11.9 | 6e-31 | 32/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +11.3 | 3e-28 | 30/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +11.2 | 9e-28 | 30/45 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +10.9 | 3e-26 | 33/45 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +10.5 | 3e-24 | 31/45 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.5 | 3e-24 | 28/47 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +9.0 | 7e-18 | 33/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7804.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HepG2/C3A 0.405×, C-33 A 0.610×, CHP-212 0.449×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HepG2/C3A 0.430×, RKO 0.450×, SW48 0.578×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 3 lines (BT-474 0.371×, SK-MEL-2 0.528×, C-33 A 0.583×; ⚠ cell-cycle shift, explains ~6% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.830×** | -5.9 | 3e-06 | 21/45 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.871× | -4.3 | 0.004 | 11/45 (SW 1271, A498, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.913× | -4.1 | 0.008 | 2/45 (A498, AN3 CA) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.037 | 17/46 (A498, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.891× | -3.5 | 0.055 | 7/45 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.858× | -3.4 | 0.055 | 8/45 (LoVo, A498, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.066 | 4/46 (RPMI-7951, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.863× | -3.3 | 0.066 | 6/45 (A-172, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.895× | -3.3 | 0.071 | 6/44 (AN3 CA, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 99.8 | 15 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +27.1) | — |
| [[A-172 (line)]] | wt | 227 | 14 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.89× (z +14.7) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.7) | — |
| [[PANC-1 (line)]] | alt | 285 | 14 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +16.6) | — |
| [[HT-29 (line)]] | alt | 138 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +17.5) | — |
| [[NCI-H1792 (line)]] | alt | 177 | 11 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.2) | — |
| [[SW480 (line)]] | alt | 125 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +21.9) | — |
| [[CFPAC-1 (line)]] | alt | 78.9 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +21.5) | — |
| [[Hs 766T (line)]] | wt | 101 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 389 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.44× (z +14.9) | — |
| [[A549 (line)]] | wt | 192 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 166 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.4) | — |
| [[SW 900 (line)]] | alt | 389 | 8 (1 ⚠) | 0 | [[Trametinib (drug)]] 0.05 µM 1.70× (z +10.5) | — |
| [[A498 (line)]] | wt | 261 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +20.2) | — |
| [[H4 (line)]] | wt | 169 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +16.1) | — |
| [[J82 (line)]] | alt | 284 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 274 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.05× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 89.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 175 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.2) | — |
| [[hTERT-HPNE (line)]] | wt | 95.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +17.9) | — |
| [[C32 (line)]] | wt | 242 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +22.3) | — |
| [[RPMI-7951 (line)]] | alt | 134 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 372 | 4 (3 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.15× (z +12.1) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.528× (z -10.6) ⚠ cell-cycle shift, explains ~6% of this change |
| [[LoVo (line)]] | wt | 147 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 119 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.0) | — |
| [[RKO (line)]] | wt | 62.9 | 3 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.77× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 108 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 224 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.4) | — |
| [[A-427 (line)]] | wt | 233 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 587 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -12.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HCT15 (line)]] | alt | 146 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 2.31× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 157 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 418 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -14.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.430× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 308 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 623 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.371× (z -12.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[CHP-212 (line)]] | wt | 577 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H2347 (line)]] | alt | 253 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.85× (z +8.5) ⚠ unreliable plate only | — |
| [[SNU-1 (line)]] | wt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 209 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -10.0) |
| [[AN3 CA (line)]] | alt | 437 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 38.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 739 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNN3]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ABCC4]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TNPO1]] | +0.59 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[USP25]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PAWR]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MAP2]] | +0.55 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[NFIB]] | +0.55 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LARP1]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ADAM9]] | +0.54 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[SOAT1]] | +0.54 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RHOBTB3]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LPP]] | +0.53 | +0.37 / +0.46 | both halves | 7e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT1]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[C16orf46]] | -0.57 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[PPIL3]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ZNF275]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[BLZF1]] | -0.53 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ICAM3]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ZKSCAN5]] | -0.52 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[DNTTIP1]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[MTMR14]] | -0.52 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[RIN1]] | -0.52 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ARHGAP1]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SNIP1]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALCAM]] | B | ALCAM activity lowers ENAH's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 1.65× higher at baseline in the lines without ALCAM | 0.081 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNPO1]] | C | ENAH activity raises TNPO1's level | lines that do not express ENAH (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without ENAH | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: SSBP2, DIP2C, SOX12; maybe low, not absent |
| [[RDX]] | C | ENAH activity raises RDX's level | lines that do not express ENAH (3) vs lines expressing it (47) | 4.04× lower at baseline in the lines without ENAH | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: SSBP2, DIP2C, SOX12; maybe low, not absent |
| [[KLHL5]] | C | ENAH activity raises KLHL5's level | lines that do not express ENAH (3) vs lines expressing it (47) | 4.64× lower at baseline in the lines without ENAH | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SSBP2, DIP2C, SOX12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.5, -14.5); signed map (11.1, -53.2). **Vector** length 120, 40.4% of its response variance represented; |z| ≥ 3 in 1,773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.6 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +13.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.5 | +5.3 |
|  | [[Trametinib (drug)]] 5 µM |  | +6.5 | +5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.3 | +7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +6.2 | +7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.6 | +6.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.8 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.3 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.8 | +7.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.7 | +1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.6 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ENAH actin regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,486,765-225,653,142 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10773, NDPP1, MENA |
| Gene groups (HGNC) | ENAH/VASPs |
| Reactome | 6 pathways, smallest: Generation of second messenger molecules; TCR signaling; Signaling by ROBO receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8S7](https://www.uniprot.org/uniprotkb/Q8N8S7) (Protein enabled homolog):

> Ena/VASP proteins are actin-associated proteins involved in a range of processes dependent on cytoskeleton remodeling and cell polarity such as axon guidance and lamellipodial and filopodial dynamics in migrating cells. ENAH induces the formation of F-actin rich outgrowths in fibroblasts. Acts synergistically with BAIAP2-alpha and downstream of NTN1 to promote filipodia formation (By similarity).

**Summary**, from NCBI Gene [55740](https://www.ncbi.nlm.nih.gov/gene/55740):

> This gene encodes a member of the enabled/ vasodilator-stimulated phosphoprotein. Members of this gene family are involved in actin-based motility. This protein is involved in regulating the assembly of actin filaments and modulates cell adhesion and motility. Alternate splice variants of this gene have been correlated with tumor invasiveness in certain tissues and these variants may serve as prognostic markers. A pseudogene of this gene is found on chromosome 3. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:18271](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18271) · Entrez [55740](https://www.ncbi.nlm.nih.gov/gene/55740) · UniProt [Q8N8S7](https://www.uniprot.org/uniprotkb/Q8N8S7) · Ensembl [ENSG00000154380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154380)

## Data

Gene col 7804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7804); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7804]; `tensor/DDL_lfc|DDL_z.npy` [7804]; `embed/gene_vectors.npy` [7804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7804 or target_col == 7804). Every well: [[ENAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
