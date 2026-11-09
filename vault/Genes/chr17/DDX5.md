---
symbol: "DDX5"
type: "gene"
col: 2982
ensembl_id: "ENSG00000108654"
name: "DEAD-box helicase 5"
location: "17q23.3"
module: 17
arm: "-"
pooled_cpm: 275.54
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DDX5

*DEAD-box helicase 5* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.09× (z +25.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.682× (z -6.2, q 4e-07, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC200]] (+0.66, fdr 1e-05), [[MSRA]] (+0.63, fdr 7e-06), [[KPNA4]] (+0.61, fdr 1e-05); moves opposite to [[ZFP64]] (-0.74, fdr 7e-06), [[NCK1]] (-0.70, fdr 7e-06), [[SNAPC3]] (-0.70, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +25.6 | 0e+00 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +18.0 | 0e+00 | 49/49 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +15.4 | 0e+00 | 46/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.40×** | +13.5 | 2e-39 | 46/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.16×** | +12.3 | 6e-33 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.10×** | +11.9 | 9e-31 | 49/49 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.09×** | +10.9 | 7e-26 | 44/45 (A498, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.89×** | +9.8 | 8e-21 | 43/44 (SHP-77, SW48, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +8.7 | 2e-16 | 42/48 (HOP62, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.7 | 3e-16 | 47/50 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.69×** | +8.4 | 2e-15 | 42/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +8.0 | 5e-14 | 40/48 (SW480, A-427, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.65×** | +8.0 | 7e-14 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.63×** | +7.8 | 2e-13 | 37/48 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.66×** | +7.8 | 3e-13 | 43/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.6 | 9e-13 | 36/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.6 | 1e-04 | 27/48 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 2e-04 | 34/48 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 6e-04 | 34/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.021 | 26/48 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.030 | 33/48 (SK-MEL-2, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.053 | 25/47 (Hs 766T, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.071 | 24/48 (A-427, NCI-H23, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.682×** | -6.2 | 4e-07 | 39/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.735×** | -5.0 | 2e-04 | 42/48 (KATO III, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.781×** | -4.0 | 0.011 | 37/48 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.783×** | -4.0 | 0.011 | 33/48 (KATO III, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 0.848× | -3.8 | 0.017 | 22/48 (AsPC-1, NCI-H23, …) | all doses, flat | low cells (technical?) |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.802×** | -3.6 | 0.033 | 30/48 (RPMI-7951, CHP-212, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.661×** | -3.5 | 0.038 | 26/47 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.868× | -3.3 | 0.081 | 16/48 (NCI-H23, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.095 | 25/49 (HT-29, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.095 | 18/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.816×** | -3.1 | 0.095 | 24/49 (CFPAC-1, COLO 205, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -3.1 | 0.095 | 17/48 (LoVo, HS-578T, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.828×** | -3.1 | 0.095 | 22/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.877× | -3.0 | 0.100 | 6/48 (J82, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 264 | 19 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +31.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 248 | 15 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +23.0) | — |
| [[SW480 (line)]] | alt | 345 | 15 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +20.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.1) | — |
| [[KATO III (line)]] | alt | 273 | 9 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +17.5) | [[Ponatinib (drug)]] 5 µM 0.318× (z -12.5) |
| [[A-172 (line)]] | wt | 237 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +24.5) | — |
| [[AsPC-1 (line)]] | alt | 285 | 9 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +28.2) | [[Selinexor (drug)]] 5 µM 0.525× (z -10.8) ⚠ cell-cycle shift, explains ~99% of this change |
| [[NCI-H1573 (line)]] | alt | 327 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +31.4) | — |
| [[SNU-1 (line)]] | wt | 263 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +18.8) | — |
| [[SNU-423 (line)]] | alt | 184 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +29.1) | — |
| [[SW48 (line)]] | wt | 250 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 230 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +23.5) | — |
| [[H4 (line)]] | wt | 211 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +20.1) | — |
| [[HS-578T (line)]] | alt | 195 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +24.7) | — |
| [[NCI-H1792 (line)]] | alt | 182 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +27.5) | — |
| [[PANC-1 (line)]] | alt | 138 | 9 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 278 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +30.1) | — |
| [[hTERT-HPNE (line)]] | wt | 286 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +24.5) | — |
| [[J82 (line)]] | alt | 281 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.3) | — |
| [[LS 180 (line)]] | wt | 259 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +14.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 206 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 347 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +24.6) | — |
| [[A498 (line)]] | wt | 234 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +26.2) | — |
| [[A549 (line)]] | wt | 279 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +14.5) | — |
| [[HCT15 (line)]] | alt | 258 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 311 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +19.7) | — |
| [[SW1417 (line)]] | alt | 286 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +17.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.4) | — |
| [[A-427 (line)]] | wt | 395 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.22× (z +12.6) | — |
| [[C32 (line)]] | wt | 226 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +26.7) | — |
| [[Hs 766T (line)]] | wt | 203 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +20.7) | — |
| [[LOX-IMVI (line)]] | wt | 326 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +19.3) | — |
| [[C-33 A (line)]] | alt | 381 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.75× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 395 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.5) | [[Ponatinib (drug)]] 5 µM 0.402× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 232 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +15.8) | — |
| [[SW 900 (line)]] | alt | 289 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.5) | — |
| [[COLO 205 (line)]] | alt | 329 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +23.4) | — |
| [[SHP-77 (line)]] | alt | 200 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 348 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.0) | — |
| [[LoVo (line)]] | wt | 309 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +22.2) | — |
| [[Panc 03.27 (line)]] | alt | 395 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 381 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 377 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 292 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.0) | — |
| [[RKO (line)]] | wt | 335 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 210 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +14.4) | — |
| [[CHP-212 (line)]] | wt | 371 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SW 1088 (line)]] | alt | 198 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 380 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.5) | — |
| [[NCI-H2122 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 217 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*16 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC200]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MSRA]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[KPNA4]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[NEK10]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[WDR45]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[HNRNPAB]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TUG1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[DESI1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[THOC6]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MAPRE1]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[QRICH2]] | +0.57 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[FSCN2]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*84 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP64]] | -0.74 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[NCK1]] | -0.70 | -0.66 / -0.66 | both halves | 7e-06 |  |
| [[SNAPC3]] | -0.70 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.70 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[RAD17]] | -0.69 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[MALSU1]] | -0.68 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[ARNT]] | -0.67 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[MED23]] | -0.66 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[HEATR6]] | -0.66 | -0.58 / -0.65 | both halves | 7e-06 | same gene group |
| [[USP30]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[MMS19]] | -0.65 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.64 | -0.53 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DDX5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-0.8, -12.4); signed map (16.2, -2.3). **Vector** length 127, 53.1% of its response variance represented; |z| ≥ 3 in 1,695 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.3 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +18.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.3 | +1.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -8.0 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -7.1 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,498,254-64,508,199 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p68; previously HLR1, G17P1 |
| Gene groups (HGNC) | DEAD-box helicases; MicroRNA protein coding host genes |
| Reactome | 23 pathways, smallest: Replication of the SARS-CoV-1 genome; Replication of the SARS-CoV-2 genome; SARS-CoV-1 Genome Replication and Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P17844](https://www.uniprot.org/uniprotkb/P17844) (Probable ATP-dependent RNA helicase DDX5):

> Involved in the alternative regulation of pre-mRNA splicing; its RNA helicase activity is necessary for increasing tau exon 10 inclusion and occurs in a RBM4-dependent manner. Binds to the tau pre-mRNA in the stem-loop region downstream of exon 10. The rate of ATP hydrolysis is highly stimulated by single-stranded RNA. Involved in transcriptional regulation; the function is independent of the RNA helicase activity. Transcriptional coactivator for androgen receptor AR but probably not ESR1. …

**Summary**, from NCBI Gene [1655](https://www.ncbi.nlm.nih.gov/gene/1655):

> This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the processing of small noncoding RNAs. Members of this family contain nine conserved motifs, including …

**Accessions** — [HGNC:2746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2746) · Entrez [1655](https://www.ncbi.nlm.nih.gov/gene/1655) · UniProt [P17844](https://www.uniprot.org/uniprotkb/P17844) · Ensembl [ENSG00000108654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108654)

## Data

Gene col 2982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2982); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2982]; `tensor/DDL_lfc|DDL_z.npy` [2982]; `embed/gene_vectors.npy` [2982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2982 or target_col == 2982). Every well: [[DDX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
