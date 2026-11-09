---
symbol: "ACTN4"
type: "gene"
col: 5062
ensembl_id: "ENSG00000130402"
name: "actinin alpha 4"
location: "19q13.2"
module: 111
arm: "+"
pooled_cpm: 467.74
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# ACTN4

*actinin alpha 4* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.15× (z +15.8, q 0e+00, up in 36 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 3.39×, A549 3.42×, SNU-423 3.86×, C-33 A 4.21×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 3.58×, SNU-423 3.74×, A498 2.94×, hTERT-HPNE 4.35×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 3.45×, C-33 A 3.76×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 1.79×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.672× (z -12.1, q 5e-31, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIAPH1]] (+0.67, fdr 7e-06), [[CORO1C]] (+0.67, fdr 7e-06), [[ANXA11]] (+0.67, fdr 7e-06); moves opposite to [[CCDC59]] (-0.63, fdr 1e-05), [[COA6]] (-0.59, fdr 3e-05), [[TMEM101]] (-0.58, fdr 7e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[JUP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5062.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 3.39×, A549 3.42×, SNU-423 3.86×, C-33 A 4.21×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 3.58×, SNU-423 3.74×, A498 2.94×, hTERT-HPNE 4.35×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 3.45×, C-33 A 3.76×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 1.79×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +15.8 | 0e+00 | 36/43 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +15.8 | 0e+00 | 43/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +11.3 | 3e-27 | 40/44 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +4.3 | 0.003 | 24/47 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.20×** | +4.0 | 0.008 | 23/47 (A-427, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +3.9 | 0.009 | 23/47 (A-427, NCI-H2030, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.17× | +3.4 | 0.063 | 16/47 (SNU-423, NCI-H2030, …) | rises with dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.17 | 14/47 (NCI-H1792, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -12.1 | 5e-31 | 32/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.713×** | -10.3 | 2e-22 | 34/47 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -10.2 | 4e-22 | 42/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -6.0 | 2e-07 | 30/47 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.750×** | -6.0 | 3e-07 | 26/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -5.4 | 5e-06 | 26/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.847× | -5.1 | 3e-05 | 17/47 (SW480, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -4.7 | 2e-04 | 25/47 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.803×** | -4.5 | 5e-04 | 26/47 (HOP62, HepG2/C3A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -4.5 | 5e-04 | 25/47 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.822×** | -4.2 | 0.001 | 24/47 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.828×** | -4.1 | 0.002 | 24/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.8 | 0.005 | 13/47 (SW480, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.712×** | -3.8 | 0.005 | 28/44 (SK-MEL-2, H4, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.848× | -3.6 | 0.013 | 19/47 (HOP62, HepG2/C3A, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | 0.856× | -3.2 | 0.036 | 14/47 (HOP62, SNU-423, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 0.872× | -3.0 | 0.086 | 8/47 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.908× | -2.9 | 0.086 | 9/47 (HOP62, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 710 | 1 (1 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.73× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -24.9) |
| [[A-427 (line)]] | wt | 129 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +16.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 697 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -16.6) |
| [[HOP62 (line)]] | alt | 508 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 334 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +11.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.6) |
| [[A549 (line)]] | wt | 619 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +18.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -8.7) |
| [[C32 (line)]] | wt | 370 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +10.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 505 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +8.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 373 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.4) |
| [[HS-578T (line)]] | alt | 329 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +15.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 195 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.8) | — |
| [[LoVo (line)]] | wt | 622 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 260 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +15.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.540× (z -9.2) |
| [[LS 180 (line)]] | wt | 724 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 168 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 218 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.543× (z -9.6) |
| [[PANC-1 (line)]] | alt | 1,249 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.532× (z -9.0) |
| [[RKO (line)]] | wt | 181 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.540× (z -8.7) |
| [[SW 900 (line)]] | alt | 391 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.9) |
| [[SW48 (line)]] | wt | 712 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -18.0) |
| [[A-172 (line)]] | wt | 373 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 345 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +18.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 151 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +11.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 162 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +17.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 372 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 618 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 1.76× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -11.4) |
| [[Hs 766T (line)]] | wt | 524 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -18.3) |
| [[J82 (line)]] | alt | 309 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 144 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 279 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +15.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 323 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 189 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 220 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +18.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 846 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -18.6) |
| [[CHP-212 (line)]] | wt | 179 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +10.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 477 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.8) |
| [[HT-29 (line)]] | alt | 1,128 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -16.7) |
| [[KATO III (line)]] | alt | 688 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 239 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 291 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.490× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 518 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -12.4) |
| [[SHP-77 (line)]] | alt | 216 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.91× (z +8.8) ⚠ cell-cycle shift, explains <1% of this change | — |
| [[BT-474 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 470 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 115 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 386 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CORO1C]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 | STRING 563 |
| [[ANXA11]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CYB5R3]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[FGFRL1]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MYH9]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 926 |
| [[CDC42]] | +0.61 | +0.51 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 443 |
| [[CAPZB]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 513 |
| [[RHOA]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 | pathway: Platelet activation, signaling and aggregation; STRING 517 |
| [[ITGA6]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 | pathway: Cell-Cell communication; STRING 725 |
| [[ITGB1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 960 |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC59]] | -0.63 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[COA6]] | -0.59 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[TMEM101]] | -0.58 | -0.37 / -0.61 | both halves | 7e-05 |  |
| [[NKAP]] | -0.57 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[FDX2]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RNF135]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ZNF330]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[CCDC122]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ADPRM]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MRPS31]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[AZI2]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | JUP activity raises ACTN4's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.61× lower at baseline in the lines without JUP | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[SH3RF2]] | B | SH3RF2 activity raises ACTN4's level | lines that do not express SH3RF2 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without SH3RF2 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01564, CAPG, LINC00857; maybe low, not absent |
| [[ARHGAP23]] | B | ARHGAP23 activity raises ACTN4's level | lines that do not express ARHGAP23 (12) vs lines expressing it (38) | 1.63× lower at baseline in the lines without ARHGAP23 | 0.097 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.0, 26.2); signed map (-11.7, 36.5). **Vector** length 156, 54.9% of its response variance represented; |z| ≥ 3 in 1,433 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPase Effectors* (reactome, mean cos +0.52 to 10); *EPHB-mediated forward signaling* (reactome, mean cos +0.51 to 6); *Leishmania infection* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +6.6 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +6.0 | +3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -7.1 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -4.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | -4.2 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.7 | -2.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -3.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | actinin alpha 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,647,649-38,731,589 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FSGS1 |
| Gene groups (HGNC) | Actinins |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 6 pathways, smallest: Nephrin family interactions; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [O43707](https://www.uniprot.org/uniprotkb/O43707) (Alpha-actinin-4):

> F-actin cross-linking protein which is thought to anchor actin to a variety of intracellular structures. This is a bundling protein (Probable). Probably involved in vesicular trafficking via its association with the CART complex. The CART complex is necessary for efficient transferrin receptor recycling but not for EGFR degradation. Involved in tight junction assembly in epithelial cells probably through interaction with MICALL2. Links MICALL2 to the actin cytoskeleton and recruits it to the …

**Summary**, from NCBI Gene [81](https://www.ncbi.nlm.nih.gov/gene/81):

> Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding actin to the membrane. In contrast, skeletal, cardiac, and smooth muscle isoforms are localized to …

**Accessions** — [HGNC:166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:166) · Entrez [81](https://www.ncbi.nlm.nih.gov/gene/81) · UniProt [O43707](https://www.uniprot.org/uniprotkb/O43707) · Ensembl [ENSG00000130402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130402)

## Data

Gene col 5062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5062); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5062]; `tensor/DDL_lfc|DDL_z.npy` [5062]; `embed/gene_vectors.npy` [5062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5062 or target_col == 5062). Every well: [[ACTN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
