---
symbol: "UBR5"
type: "gene"
col: 2468
ensembl_id: "ENSG00000104517"
name: "ubiquitin protein ligase E3 component n-recognin 5"
location: "8q22.3"
module: 130
arm: "+"
pooled_cpm: 441.89
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# UBR5

*ubiquitin protein ligase E3 component n-recognin 5* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +13.2, q 6e-37, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.502× (z -11.4, q 3e-27, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.723× (z -5.6, q 2e-06, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.200×, SK-MEL-2 0.335×, C-33 A 0.221×, SNU-1 0.313×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.253×, CHP-212 0.202×, NCI-H1792 0.320×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.359×, A549 0.411×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.500×, C32 0.529×); [[Auranofin (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.423×, SK-MEL-2 0.528×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF21A]] (+0.66, fdr 7e-06), [[TOP2B]] (+0.62, fdr 1e-05), [[ACBD5]] (+0.60, fdr 2e-05); moves opposite to [[CUTC]] (-0.58, fdr 4e-05), [[RRP7BP-1]] (-0.58, fdr 1e-05), [[GPR89B]] (-0.54, fdr 4e-04).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +13.2 | 6e-37 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +11.8 | 7e-30 | 39/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.5 | 4e-15 | 35/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +6.3 | 4e-08 | 44/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.0 | 2e-07 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.5 | 4e-06 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.4 | 5e-06 | 34/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +5.3 | 7e-06 | 40/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.13 | 20/48 (HCT15, LoVo, …) | all doses, flat |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.0 | 0.15 | 23/49 (A-172, NCI-H1792, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2468.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (C32 0.200×, SK-MEL-2 0.335×, C-33 A 0.221×, SNU-1 0.313×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.253×, CHP-212 0.202×, NCI-H1792 0.320×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.359×, A549 0.411×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.500×, C32 0.529×); [[Auranofin (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.423×, SK-MEL-2 0.528×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.502×** | -11.4 | 3e-27 | 47/47 (C32, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -10.0 | 3e-21 | 42/44 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -9.5 | 5e-19 | 43/49 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.591×** | -9.0 | 2e-17 | 44/48 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.636×** | -7.8 | 8e-13 | 44/48 (A549, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -7.0 | 3e-10 | 39/45 (CHP-212, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.695×** | -6.3 | 3e-08 | 41/48 (AsPC-1, CHP-212, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -5.6 | 2e-06 | 36/48 (hTERT-HPNE, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.744×** | -5.1 | 2e-05 | 39/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.802×** | -3.8 | 0.008 | 29/48 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.858× | -3.7 | 0.009 | 12/48 (C32, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 305 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +22.8) | — |
| [[AsPC-1 (line)]] | alt | 521 | 5 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.53× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -12.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 1,004 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.6) |
| [[CHP-212 (line)]] | wt | 822 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 748 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -16.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.0) |
| [[PANC-1 (line)]] | alt | 345 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +21.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.556× (z -9.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 551 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.423× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 387 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -10.8) ⚠ toxic |
| [[SW 900 (line)]] | alt | 564 | 2 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.404× (z -10.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 409 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.5) | — |
| [[KATO III (line)]] | alt | 305 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +19.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -9.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 771 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -11.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 582 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.473× (z -10.4) ⚠ toxic |
| [[A549 (line)]] | wt | 501 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 286 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 256 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -9.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 588 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -9.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 288 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 347 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 609 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -10.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 287 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +19.2) | — |
| [[A498 (line)]] | wt | 361 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +26.3) | — |
| [[C-33 A (line)]] | alt | 824 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 281 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.515× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 387 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.526× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 340 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.471× (z -9.4) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 475 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -10.2) ⚠ toxic |
| [[RKO (line)]] | wt | 831 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 365 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.528× (z -8.5) |
| [[BT-474 (line)]] | alt | 470 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 353 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -9.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 801 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 235 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.2) | — |
| [[J82 (line)]] | alt | 401 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 621 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 501 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 308 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 440 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.493× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 282 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 557 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -12.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 304 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.1) | — |
| [[SW48 (line)]] | wt | 296 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[A-172 (line)]] | wt | 249 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 444 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 453 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 490 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 564 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 390 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF21A]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TOP2B]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ACBD5]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ANP32A]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | +0.57 | +0.27 / +0.49 | both halves | 3e-04 |  |
| [[PIAS2]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.56 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZHX1]] | +0.56 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[CMC4]] | +0.56 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[REV3L]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[TAPT1]] | +0.56 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[CA11]] | +0.55 | +0.42 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTC]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[RRP7BP-1]] | -0.58 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[GPR89B]] | -0.54 | -0.26 / -0.63 | both halves | 4e-04 |  |
| [[ERCC3]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[ANKS6]] | -0.53 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[RABIF]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[ARMC9]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MPP3]] | -0.52 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[TRIP4]] | -0.52 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[HERC2P3]] | -0.52 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[HERC2P2]] | -0.52 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[C19orf12]] | -0.52 | -0.36 / -0.56 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UBR5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PBX4]] | C | PBX4 activity weakens UBR5's drug response | lines that do not express PBX4 (3) vs lines expressing it (46) | the lines without PBX4 respond 0.99× as strongly (z diff -0.16); strongest at Dinaciclib 0.05 µM: 0.27x vs 0.64x (z diff -5.1) | 0.006 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561; target measured in part of the lines; both ways; artifact flags |
| [[CTNNA3]] | C | CTNNA3 activity lowers UBR5's level | lines that do not express CTNNA3 (4) vs lines expressing it (46) | 1.55× higher at baseline in the lines without CTNNA3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OSBPL10, MYO15B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.6, -26.7); signed map (12.9, -14.0). **Vector** length 100, 43.0% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.5 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +11.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -11.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.0 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin protein ligase E3 component n-recognin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:102,252,273-102,412,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DD5, HYD, EDD, KIAA0896; previously EDD1 |
| Gene groups (HGNC) | Ubiquitin protein ligase E3 component n-recognins; HECT domain E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95071](https://www.uniprot.org/uniprotkb/O95071) (E3 ubiquitin-protein ligase UBR5):

> E3 ubiquitin-protein ligase involved in different protein quality control pathways in the cytoplasm and nucleus. Mainly acts as a ubiquitin chain elongator that extends pre-ubiquitinated substrates. Component of the N-end rule pathway: ubiquitinates proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their degradation (By similarity). Recognizes type-1 N-degrons, containing positively charged amino acids (Arg, Lys and His) (By …

**Summary**, from NCBI Gene [51366](https://www.ncbi.nlm.nih.gov/gene/51366):

> This gene encodes a progestin-induced protein, which belongs to the HECT (homology to E6-AP carboxyl terminus) family. The HECT family proteins function as E3 ubiquitin-protein ligases, targeting specific proteins for ubiquitin-mediated proteolysis. This gene is localized to chromosome 8q22 which is disrupted in a variety of cancers. This gene potentially has a role in regulation of cell proliferation or differentiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16806) · Entrez [51366](https://www.ncbi.nlm.nih.gov/gene/51366) · UniProt [O95071](https://www.uniprot.org/uniprotkb/O95071) · Ensembl [ENSG00000104517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104517)

## Data

Gene col 2468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2468); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2468]; `tensor/DDL_lfc|DDL_z.npy` [2468]; `embed/gene_vectors.npy` [2468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2468 or target_col == 2468). Every well: [[UBR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
