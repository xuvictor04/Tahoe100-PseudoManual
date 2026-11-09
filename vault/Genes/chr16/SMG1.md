---
symbol: "SMG1"
type: "gene"
col: 8041
ensembl_id: "ENSG00000157106"
name: "SMG1 nonsense mediated mRNA decay associated PI3K related kinase"
location: "16p12.3"
module: 111
arm: "+"
pooled_cpm: 364.26
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# SMG1

*SMG1 nonsense mediated mRNA decay associated PI3K related kinase* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +11.6, q 3e-28, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.611× (z -10.2, q 1e-21, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.767× (z -5.7, q 2e-06, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H1573 0.387×, Panc 03.27 0.517×, A-427 0.551×, A-172 0.466×, …; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 0.388×, A-172 0.385×, C-33 A 0.422×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.408×, NCI-H1573 0.410×, SK-MEL-2 0.454×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.404×, C32 0.513×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPAG9]] (+0.60, fdr 1e-05), [[UBR4]] (+0.53, fdr 3e-05), [[IQGAP1]] (+0.52, fdr 2e-05); moves opposite to [[ZNF16]] (-0.53, fdr 2e-05), [[RPRD1B]] (-0.50, fdr 2e-04), [[SLC35D1]] (-0.49, fdr 4e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +11.6 | 3e-28 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +10.7 | 2e-24 | 42/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.8 | 1e-20 | 37/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.8 | 1e-12 | 34/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +7.6 | 2e-12 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +7.1 | 1e-10 | 43/48 (HT-29, H4, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 1e-10 | 31/48 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 2e-10 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +6.9 | 2e-10 | 37/48 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.0 | 1e-07 | 34/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.7 | 7e-07 | 34/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 9e-07 | 32/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.5 | 1e-06 | 38/48 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.5 | 2e-06 | 30/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 7e-06 | 32/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +5.0 | 2e-05 | 31/48 (LoVo, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 42/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 3e-05 | 28/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H1573 0.387×, Panc 03.27 0.517×, A-427 0.551×, A-172 0.466×, …; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 0.388×, A-172 0.385×, C-33 A 0.422×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.408×, NCI-H1573 0.410×, SK-MEL-2 0.454×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.404×, C32 0.513×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -10.2 | 1e-21 | 45/47 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.759×** | -5.9 | 8e-07 | 31/49 (A-172, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.767×** | -5.7 | 2e-06 | 37/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.758×** | -5.5 | 5e-06 | 30/45 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -4.7 | 3e-04 | 20/48 (A549, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.838× | -3.8 | 0.014 | 23/48 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.890× | -3.6 | 0.027 | 3/48 (SW 900, CHP-212, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.852× | -3.5 | 0.033 | 16/48 (HT-29, LoVo, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.852× | -3.5 | 0.033 | 19/48 (LoVo, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.853× | -3.4 | 0.034 | 17/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.862× | -3.2 | 0.063 | 15/49 (LoVo, PANC-1, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.901× | -3.2 | 0.063 | 4/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.863× | -3.2 | 0.063 | 16/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 279 | 15 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +19.6) | — |
| [[LoVo (line)]] | wt | 355 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +17.5) | — |
| [[A498 (line)]] | wt | 408 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.571× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 507 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[H4 (line)]] | wt | 333 | 5 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 387 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.1) | — |
| [[KATO III (line)]] | alt | 320 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.576× (z -8.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 274 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.13× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 621 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +18.0) | — |
| [[A-172 (line)]] | wt | 403 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[BT-474 (line)]] | alt | 418 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -9.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 251 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 248 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 198 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +19.3) | — |
| [[SW 900 (line)]] | alt | 226 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.3) | — |
| [[SW1417 (line)]] | alt | 331 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.1) | — |
| [[SW480 (line)]] | alt | 264 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.11× (z +13.1) | — |
| [[A549 (line)]] | wt | 413 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -15.8) ⚠ cell-cycle shift, explains ~16% of this change |
| [[SK-MEL-2 (line)]] | alt | 488 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 319 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.8) | — |
| [[SW48 (line)]] | wt | 299 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.4) | — |
| [[A-427 (line)]] | wt | 354 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -10.0) ⚠ toxic |
| [[C32 (line)]] | wt | 391 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.513× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 311 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.551× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 299 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 307 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.549× (z -8.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 555 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.404× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 577 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -11.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 307 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 288 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -11.0) ⚠ toxic |
| [[RKO (line)]] | wt | 349 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 406 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.422× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[HCT15 (line)]] | alt | 542 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -9.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 325 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.572× (z -9.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 343 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.80× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 479 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.509× (z -9.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 283 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.7) | — |
| [[J82 (line)]] | alt | 393 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.68× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 128 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 445 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.496× (z -8.7) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 327 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 300 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 359 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 493 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 265 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[UBR4]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 | same gene group |
| [[IQGAP1]] | +0.52 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SQSTM1]] | +0.52 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SPTAN1]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[CAST]] | +0.50 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[NBEAL1]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 | same gene group |
| [[VPS35]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 | same gene group |
| [[DYNC1H1]] | +0.50 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[KTN1]] | +0.48 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[TKT]] | +0.48 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[CTNNA1]] | +0.48 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF16]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RPRD1B]] | -0.50 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[SLC35D1]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[UQCRFS1]] | -0.48 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ZNF865]] | -0.47 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[TOE1]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GMEB1]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[BMS1P1]] | -0.47 | -0.23 / -0.64 | both halves | 5e-04 |  |
| [[MOSMO]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ZNF79]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[DTWD1]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[MTMR1]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.324). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.9, 8.9); signed map (-10.0, 32.3). **Vector** length 105, 40.4% of its response variance represented; |z| ≥ 3 in 1,409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.2 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +5.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.6 | -10.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.6 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.6 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 nonsense mediated mRNA decay associated PI3K related kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:18,804,860-18,926,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIP, KIAA0421, ATX |
| Gene groups (HGNC) | Armadillo like helical domain containing; SMG1 complex; DECID complex; Phosphatidylinositol 3-kinase-related kinase family |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q15](https://www.uniprot.org/uniprotkb/Q96Q15) (Serine/threonine-protein kinase SMG1):

> Serine/threonine protein kinase involved in both mRNA surveillance and genotoxic stress response pathways. Recognizes the substrate consensus sequence [ST]-Q. Plays a central role in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons by phosphorylating UPF1/RENT1. Recruited by release factors to stalled ribosomes together with SMG8 and SMG9 (forming the SMG1C protein kinase complex), and UPF1 to form the transient SURF (SMG1-UPF1-eRF1-eRF3) complex. In EJC-dependent NMD, …

**Summary**, from NCBI Gene [23049](https://www.ncbi.nlm.nih.gov/gene/23049):

> This gene encodes a protein involved in nonsense-mediated mRNA decay (NMD) as part of the mRNA surveillance complex. The protein has kinase activity and is thought to function in NMD by phosphorylating the regulator of nonsense transcripts 1 protein. Alternatively spliced transcript variants have been described, but their full-length nature has yet to be determined. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:30045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30045) · Entrez [23049](https://www.ncbi.nlm.nih.gov/gene/23049) · UniProt [Q96Q15](https://www.uniprot.org/uniprotkb/Q96Q15) · Ensembl [ENSG00000157106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157106)

## Data

Gene col 8041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8041); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8041]; `tensor/DDL_lfc|DDL_z.npy` [8041]; `embed/gene_vectors.npy` [8041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8041 or target_col == 8041). Every well: [[SMG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
