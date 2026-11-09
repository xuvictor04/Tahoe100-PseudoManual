---
symbol: "APLP2"
type: "gene"
col: 1398
ensembl_id: "ENSG00000084234"
name: "amyloid beta precursor like protein 2"
location: "11q24.3"
module: 11
arm: "-"
pooled_cpm: 472.06
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# APLP2

*amyloid beta precursor like protein 2* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +21.7, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +20.9, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.666× (z -8.6, q 4e-15, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMBIM6]] (+0.71, fdr 7e-06), [[CTSB]] (+0.65, fdr 7e-06), [[ITGB1]] (+0.64, fdr 1e-05); moves opposite to [[MTPAP]] (-0.62, fdr 1e-05), [[MRPL58]] (-0.62, fdr 1e-05), [[MRPL15]] (-0.62, fdr 8e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.69×** | +21.7 | 0e+00 | 49/49 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +20.9 | 0e+00 | 47/49 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.38×** | +18.3 | 0e+00 | 44/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.00×** | +15.2 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.98×** | +13.8 | 2e-41 | 44/45 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +12.6 | 4e-34 | 48/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +11.4 | 3e-28 | 47/48 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.52×** | +8.9 | 4e-17 | 37/50 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +7.2 | 3e-11 | 41/48 (NCI-H460, SW1417, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.38×** | +7.1 | 6e-11 | 41/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.0 | 1e-07 | 26/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +5.6 | 1e-06 | 32/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.5 | 2e-06 | 22/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +5.0 | 3e-05 | 29/48 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.31×** | +4.7 | 9e-05 | 32/48 (NCI-H460, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.6 | 1e-04 | 32/49 (KATO III, RKO, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 39/48 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.003 | 26/48 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.666×** | -8.6 | 4e-15 | 43/49 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.766×** | -5.9 | 1e-06 | 27/48 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.857× | -4.8 | 3e-04 | 12/48 (LoVo, A549, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -4.8 | 3e-04 | 28/48 (SW 900, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.857× | -4.7 | 3e-04 | 17/48 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.836× | -4.0 | 0.007 | 21/49 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.5 | 0.039 | 22/48 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.835× | -3.4 | 0.045 | 22/50 (A549, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.860× | -3.3 | 0.053 | 20/48 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.11 | 16/48 (HepG2/C3A, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 393 | 13 (11 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +16.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +16.4) | — |
| [[SW480 (line)]] | alt | 320 | 11 (9 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +22.3) | — |
| [[LoVo (line)]] | wt | 250 | 10 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +25.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 457 | 10 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +24.2) | — |
| [[SW48 (line)]] | wt | 278 | 10 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +14.5) | — |
| [[C32 (line)]] | wt | 532 | 8 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +22.3) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +16.5) | [[Verteporfin (drug)]] 5 µM 0.518× (z -9.1) |
| [[HOP62 (line)]] | alt | 299 | 9 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +19.5) | — |
| [[LOX-IMVI (line)]] | wt | 541 | 8 (6 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +16.8) | [[Verteporfin (drug)]] 5 µM 0.574× (z -8.6) |
| [[A498 (line)]] | wt | 303 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +10.8) | — |
| [[KATO III (line)]] | alt | 775 | 8 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +17.5) | — |
| [[NCI-H1573 (line)]] | alt | 415 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +13.8) | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.3) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 345 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 411 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +18.7) | — |
| [[HT-29 (line)]] | alt | 434 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +21.9) | — |
| [[J82 (line)]] | alt | 321 | 6 (4 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +16.0) | [[Verteporfin (drug)]] 5 µM 0.577× (z -8.8) |
| [[LS 180 (line)]] | wt | 315 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +17.8) | — |
| [[Panc 03.27 (line)]] | alt | 747 | 6 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +19.1) | [[Harringtonine (drug)]] 0.5 µM 0.621× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 718 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.7) | [[Verteporfin (drug)]] 5 µM 0.510× (z -10.4) |
| [[SW1417 (line)]] | alt | 545 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +14.1) | — |
| [[A-427 (line)]] | wt | 258 | 4 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.624× (z -10.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.562× (z -9.3) |
| [[COLO 205 (line)]] | alt | 460 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.81× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 561 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +15.4) | — |
| [[HepG2_C3A (line)]] | wt | 809 | 2 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -18.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.458× (z -11.4) |
| [[Hs 766T (line)]] | wt | 810 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +12.3) | [[Verteporfin (drug)]] 5 µM 0.528× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 350 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 755 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 582 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +12.5) | — |
| [[A-172 (line)]] | wt | 190 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +16.0) | — |
| [[AsPC-1 (line)]] | alt | 988 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 1,120 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +11.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -13.4) |
| [[HS-578T (line)]] | alt | 219 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 273 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 282 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +14.7) | — |
| [[SNU-1 (line)]] | wt | 352 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +14.6) | — |
| [[A549 (line)]] | wt | 282 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 275 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.6) | — |
| [[H4 (line)]] | wt | 322 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 425 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 856 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +16.9) | — |
| [[SHP-77 (line)]] | alt | 304 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 472 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 523 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 385 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +16.6) | — |
| [[BT-474 (line)]] | alt | 424 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +13.2) | — |
| [[NCI-H2122 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 434 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 439 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMBIM6]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[CTSB]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | STRING 642 |
| [[ITGB1]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[IQGAP1]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[BSG]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PSAP]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 523 |
| [[TPM3]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[IDS]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[QSOX1]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[NUCB1]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation |
| [[TLN1]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[ARPC2]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[MRPL58]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[MRPL15]] | -0.62 | -0.58 / -0.60 | both halves | 8e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[MRPL20]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[KAT14]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[BRIX1]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[CIAPIN1]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RPP38]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[C15orf40]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ZNF691]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[DPH5]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RDH14]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers APLP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.7, -20.6); signed map (-9.8, 38.9). **Vector** length 136, 51.7% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.0 | +7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.9 | +4.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.4 | -0.0 |
|  | [[Malotilate (drug)]] 0.05 µM |  | +3.4 | +2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.3 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -12.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.8 | -5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -9.3 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.0 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.0 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.4 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor like protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:130,068,147-130,144,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APPH; previously APPL2 |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06481](https://www.uniprot.org/uniprotkb/Q06481) (Amyloid beta precursor like protein 2):

> May play a role in the regulation of hemostasis. The soluble form may have inhibitory properties towards coagulation factors. May interact with cellular G protein signaling pathways. May bind to the DNA 5'-GTCACATG-3'(CDEI box). Inhibits trypsin, chymotrypsin, plasmin, factor XIA and plasma and glandular kallikrein. Modulates the Cu/Zn nitric oxide-catalyzed autodegradation of GPC1 heparan sulfate side chains in fibroblasts (By similarity).

**Summary**, from NCBI Gene [334](https://www.ncbi.nlm.nih.gov/gene/334):

> This gene encodes amyloid precursor- like protein 2 (APLP2), which is a member of the APP (amyloid precursor protein) family including APP, APLP1 and APLP2. This protein is ubiquitously expressed. It contains heparin-, copper- and zinc- binding domains at the N-terminus, BPTI/Kunitz inhibitor and E2 domains in the middle region, and transmembrane and intracellular domains at the C-terminus. This protein interacts with major histocompatibility complex (MHC) class I molecules. The synergy of this …

**Accessions** — [HGNC:598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:598) · Entrez [334](https://www.ncbi.nlm.nih.gov/gene/334) · UniProt [Q06481](https://www.uniprot.org/uniprotkb/Q06481) · Ensembl [ENSG00000084234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084234)

## Data

Gene col 1398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1398); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1398]; `tensor/DDL_lfc|DDL_z.npy` [1398]; `embed/gene_vectors.npy` [1398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1398 or target_col == 1398). Every well: [[APLP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APLP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
