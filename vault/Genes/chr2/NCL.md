---
symbol: "NCL"
type: "gene"
col: 3617
ensembl_id: "ENSG00000115053"
name: "nucleolin multifunctional protein"
location: "2q37.1"
module: 5
arm: "+"
pooled_cpm: 541.16
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NCL

*nucleolin multifunctional protein* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.65× (z +15.3, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +9.8, q 1e-20, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Pentagastrin (drug)]] 5 µM: 0.797× (z -3.8, q 0.071, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPU]] (+0.71, fdr 7e-06), [[EIF4G1]] (+0.71, fdr 7e-06), [[SYNCRIP]] (+0.67, fdr 1e-05); moves opposite to [[LIN7B]] (-0.58, fdr 4e-05), [[MGST3]] (-0.58, fdr 4e-05), [[PIGH]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.65×** | +15.3 | 0e+00 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.25×** | +13.4 | 2e-38 | 44/44 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.85×** | +10.3 | 2e-22 | 35/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.74×** | +10.1 | 8e-22 | 45/45 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +9.8 | 1e-20 | 43/49 (NCI-H1792, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +8.1 | 4e-14 | 39/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.79×** | +6.9 | 5e-10 | 44/48 (H4, NCI-H460, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +6.4 | 1e-08 | 45/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.75×** | +6.4 | 1e-08 | 43/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.74×** | +6.3 | 2e-08 | 45/50 (SNU-423, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.0 | 1e-07 | 36/48 (A-172, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.3 | 6e-06 | 42/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.54×** | +5.1 | 1e-05 | 43/48 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +5.1 | 2e-05 | 36/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.52×** | +4.9 | 3e-05 | 37/48 (H4, NCI-H460, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +4.6 | 1e-04 | 39/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 9e-04 | 35/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.002 | 37/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.002 | 38/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.86×** | +3.8 | 0.003 | 43/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.82×** | +3.7 | 0.006 | 39/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.71×** | +3.3 | 0.018 | 42/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.026 | 26/48 (RKO, SW480, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.044 | 30/48 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.35×** | +3.0 | 0.054 | 33/48 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.055 | 29/48 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +2.8 | 0.087 | 27/48 (HS-578T, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3617.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentagastrin (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.071 | 40/48 (NCI-H23, A549, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.085 | 34/48 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.776× | -3.0 | 0.47 | 38/49 (HT-29, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 307 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +20.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +13.5) | — |
| [[A-172 (line)]] | wt | 353 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +18.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 337 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 441 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 406 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +20.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 389 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +22.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +14.1) | — |
| [[A549 (line)]] | wt | 525 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[H4 (line)]] | wt | 458 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 403 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +12.6) | — |
| [[Panc 03.27 (line)]] | alt | 503 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 416 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.9) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 327 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 864 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 665 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 508 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 367 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 365 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.4) | — |
| [[A498 (line)]] | wt | 455 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.5) | — |
| [[C32 (line)]] | wt | 200 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +18.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.78× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 520 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 379 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.1) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.4) | — |
| [[J82 (line)]] | alt | 420 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 508 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 509 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.57× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 669 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 516 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 691 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 764 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 326 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[LoVo (line)]] | wt | 594 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 565 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.0) | — |
| [[A-427 (line)]] | wt | 641 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CHP-212 (line)]] | wt | 705 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 704 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 554 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[NCI-H23 (line)]] | alt | 954 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2347 (line)]] | alt | 489 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.5) | — |
| [[SW48 (line)]] | wt | 780 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 722 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 574 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 941 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 630 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-1 (line)]] | wt | 616 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 1088 (line)]] | alt | 412 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SW 1271 (line)]] | alt | 394 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.4) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[BT-474 (line)]] | alt | 509 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 870 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 508 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 699 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPU]] | +0.71 | +0.75 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 961 |
| [[EIF4G1]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 | same gene group; STRING 632 |
| [[SYNCRIP]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 587 |
| [[UTP20]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 554 |
| [[SET]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 | STRING 704 |
| [[NOLC1]] | +0.64 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 885 |
| [[NOP14]] | +0.63 | +0.69 / +0.59 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 543 |
| [[PRRC2B]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 | same gene group |
| [[EIF3A]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 | same gene group; STRING 879 |
| [[IPO4]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[GRWD1]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 | STRING 405 |
| [[GNL3L]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7B]] | -0.58 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[MGST3]] | -0.58 | -0.63 / -0.43 | both halves | 4e-05 |  |
| [[PIGH]] | -0.58 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[RRAS]] | -0.57 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[CARD19]] | -0.57 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[TMEM219]] | -0.55 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PIN1]] | -0.53 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[BAD]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[SNAPC3]] | -0.53 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[DDA1]] | -0.52 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[ABHD8]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[FAM229B]] | -0.51 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NCL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.4, -40.0); signed map (-6.4, -43.9). **Vector** length 95.3, 48.7% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +3.3 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.8 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.7 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.6 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +2.8 |

## What is on record

|  |  |
|---|---|
| Name | nucleolin multifunctional protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,453,531-231,483,641 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C23, Nsr1; previously NCL |
| Gene groups (HGNC) | RNA binding motif containing; Helicases; SSU processome; Small nucleolar RNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 9 pathways, smallest: Assembly and Release of Dengue Virus Virions; Respiratory syncytial virus (RSV) attachment and entry; Respiratory Syncytial Virus Infection Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P19338](https://www.uniprot.org/uniprotkb/P19338) (Nucleolin):

> Nucleolin is the major nucleolar protein of growing eukaryotic cells. It is found associated with intranucleolar chromatin and pre-ribosomal particles. It induces chromatin decondensation by binding to histone H1. It is thought to play a role in pre-rRNA transcription and ribosome assembly. May play a role in the process of transcriptional elongation. Binds RNA oligonucleotides with 5'-UUAGGG-3' repeats more tightly than the telomeric single-stranded DNA 5'-TTAGGG-3' repeats.

**Summary**, from NCBI Gene [4691](https://www.ncbi.nlm.nih.gov/gene/4691):

> Nucleolin (NCL), a eukaryotic nucleolar phosphoprotein, is involved in the synthesis and maturation of ribosomes. It is located mainly in dense fibrillar regions of the nucleolus. Human NCL gene consists of 14 exons with 13 introns and spans approximately 11kb. The intron 11 of the NCL gene encodes a small nucleolar RNA, termed U20. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7667) · Entrez [4691](https://www.ncbi.nlm.nih.gov/gene/4691) · UniProt [P19338](https://www.uniprot.org/uniprotkb/P19338) · Ensembl [ENSG00000115053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115053)

## Data

Gene col 3617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3617); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3617]; `tensor/DDL_lfc|DDL_z.npy` [3617]; `embed/gene_vectors.npy` [3617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3617 or target_col == 3617). Every well: [[NCL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
