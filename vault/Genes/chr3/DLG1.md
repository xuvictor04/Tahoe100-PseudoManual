---
symbol: "DLG1"
type: "gene"
col: 1130
ensembl_id: "ENSG00000075711"
name: "discs large MAGUK scaffold protein 1"
location: "3q29"
module: 1
arm: "-"
pooled_cpm: 493.65
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DLG1

*discs large MAGUK scaffold protein 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +11.5, q 5e-28, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.470× (z -20.9, q 0e+00, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -15.3, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR6A1]] (+0.54, fdr 3e-05), [[MAP4K3]] (+0.49, fdr 7e-05), [[CASK]] (+0.48, fdr 3e-05); moves opposite to [[PCMTD2]] (-0.48, fdr 7e-05), [[ZBTB34]] (-0.46, fdr 6e-04), [[MFAP3]] (-0.44, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADAMTS16]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +11.5 | 5e-28 | 39/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +9.5 | 7e-19 | 34/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +8.9 | 1e-16 | 33/48 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +6.0 | 3e-07 | 26/48 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +5.6 | 2e-06 | 31/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +5.5 | 3e-06 | 27/47 (H4, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +4.2 | 0.002 | 23/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.8 | 0.011 | 14/49 (HepG2/C3A, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.1 | 0.12 | 14/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.0 | 0.15 | 9/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -20.9 | 0e+00 | 47/47 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.504×** | -19.7 | 0e+00 | 45/49 (SNU-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -15.3 | 0e+00 | 40/49 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -15.2 | 0e+00 | 40/45 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -15.2 | 0e+00 | 40/44 (SNU-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.615×** | -14.0 | 2e-42 | 45/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -13.3 | 2e-38 | 44/48 (SNU-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.661×** | -11.9 | 1e-30 | 43/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.698×** | -10.3 | 3e-23 | 41/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.706×** | -10.0 | 9e-22 | 40/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -9.4 | 2e-19 | 35/48 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -8.8 | 5e-17 | 36/48 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.768×** | -7.3 | 1e-11 | 32/50 (A-172, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.816×** | -5.8 | 2e-07 | 26/48 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.816×** | -5.6 | 8e-07 | 25/48 (A-172, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.824×** | -5.6 | 9e-07 | 26/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.855× | -4.5 | 2e-04 | 19/49 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.851× | -4.3 | 6e-04 | 20/47 (NCI-H1792, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.815×** | -4.2 | 7e-04 | 25/48 (LS 180, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.871× | -3.9 | 0.002 | 20/48 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.889× | -3.4 | 0.017 | 17/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.913× | -3.3 | 0.018 | 7/48 (J82, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1,230 | 0 | 19 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -23.7) |
| [[MIA PaCa-2 (line)]] | alt | 1,077 | 0 | 15 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.157× (z -23.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.243× (z -18.2) |
| [[J82 (line)]] | alt | 1,133 | 0 | 14 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -21.1) |
| [[HS-578T (line)]] | alt | 672 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -19.2) |
| [[SNU-1 (line)]] | wt | 1,217 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -28.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -19.7) |
| [[SW480 (line)]] | alt | 582 | 3 (1 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.539× (z -14.4) |
| [[HT-29 (line)]] | alt | 369 | 2 (1 ⚠) | 8 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +11.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -17.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.467× (z -15.2) |
| [[LoVo (line)]] | wt | 378 | 2 (1 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.536× (z -13.5) |
| [[A498 (line)]] | wt | 495 | 1 (1 ⚠) | 8 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.93× (z +10.8) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -21.6) |
| [[LOX-IMVI (line)]] | wt | 459 | 1 | 8 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.76× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 1,103 | 1 | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -14.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 697 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -16.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.5) |
| [[SNU-423 (line)]] | alt | 633 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 539 | 3 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.522× (z -13.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.666× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 417 | 1 (1 ⚠) | 7 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.64× (z +8.9) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -13.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -11.0) |
| [[PANC-1 (line)]] | alt | 360 | 3 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +25.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.570× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 621 | 0 | 8 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -15.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -13.8) |
| [[HCT15 (line)]] | alt | 707 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.1) |
| [[KATO III (line)]] | alt | 541 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.599× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 435 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -21.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.585× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 522 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.3) |
| [[AN3 CA (line)]] | alt | 810 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 249 | 1 | 5 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.72× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -12.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.494× (z -12.0) |
| [[H4 (line)]] | wt | 440 | 4 (1 ⚠) | 2 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.70× (z +14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.46× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -15.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 548 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -10.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.457× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 256 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.561× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.620× (z -9.2) |
| [[A-427 (line)]] | wt | 277 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -15.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 487 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.566× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 509 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.97× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.491× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 324 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.437× (z -13.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 404 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +16.5) | — |
| [[NCI-H460 (line)]] | wt | 267 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -15.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -11.8) |
| [[RKO (line)]] | wt | 372 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -14.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 189 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.39× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 403 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -11.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 356 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -12.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -9.7) |
| [[A549 (line)]] | wt | 198 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -15.2) |
| [[C32 (line)]] | wt | 211 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 282 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.83× (z +9.1) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -16.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 350 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 234 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.473× (z -12.1) |
| [[SW48 (line)]] | wt | 347 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -10.1) |
| [[BT-474 (line)]] | alt | 329 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.559× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 400 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.307× (z -10.3) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 348 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 441 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 484 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 347 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 8 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR6A1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MAP4K3]] | +0.49 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[CASK]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 | same gene group; pathway: Activation of NMDA receptors and postsynaptic events; STRING 980 |
| [[WWC2]] | +0.46 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[FRYL]] | +0.45 | +0.44 / +0.36 | both halves | 9e-05 |  |
| [[ARHGAP32]] | +0.44 | +0.48 / +0.41 | both halves | 4e-05 | same gene group |
| [[NF1]] | +0.43 | +0.44 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[CLASP2]] | +0.43 | +0.37 / +0.37 | both halves | 8e-05 |  |
| [[A2MP1]] | +0.42 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[PCSK1N]] | +0.42 | +0.45 / +0.25 | both halves | 4e-04 |  |
| [[NHS]] | +0.42 | +0.29 / +0.46 | both halves | 2e-04 | same gene group |
| [[ZFAT]] | +0.42 | +0.53 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMTD2]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ZBTB34]] | -0.46 | -0.21 / -0.49 | both halves | 6e-04 |  |
| [[MFAP3]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[FOXL1]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[DPY19L3-DT]] | -0.43 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[RRN3P1]] | -0.42 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[GLUL]] | -0.41 | -0.41 / -0.39 | both halves | 5e-05 | pathway: Neuronal System |
| [[COPS8]] | -0.41 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[PDCD6P1]] | -0.41 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[ADAMTS9]] | -0.41 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SLC26A2]] | -0.40 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SEC14L2]] | -0.40 | -0.26 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS16]] | B | ADAMTS16 activity raises DLG1's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without ADAMTS16 | 0.073 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[PKD1L1-AS1]] | B | PKD1L1-AS1 activity raises DLG1's level | lines that do not express PKD1L1-AS1 (36) vs lines expressing it (14) | 1.62× lower at baseline in the lines without PKD1L1-AS1 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000222032, TMPRSS15, COL1A2 |
| [[EML1]] | B | EML1 activity raises DLG1's level | lines that do not express EML1 (13) vs lines expressing it (37) | 1.17× lower at baseline in the lines without EML1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FGF2, PYGO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.186). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-52.6, 9.6); signed map (-16.1, 30.1). **Vector** length 108, 36.6% of its response variance represented; |z| ≥ 3 in 1,821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.9 | +11.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.7 | +8.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +1.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.3 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -20.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.0 | -10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -15.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -8.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | discs large MAGUK scaffold protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,042,560-197,299,330 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAP97, SAP-97, hdlg, DLGH1, dJ1061C18.1.1 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; Scribble complex; MicroRNA protein coding host genes; SH3 domain containing |
| Hallmark sets | UV_RESPONSE_DN, APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 25 pathways, smallest: NrCAM interactions; Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12959](https://www.uniprot.org/uniprotkb/Q12959) (MAGUK scaffold protein DLG1):

> Essential multidomain scaffolding protein required for normal development (By similarity). Recruits channels, receptors and signaling molecules to discrete plasma membrane domains in polarized cells. Promotes epithelial cell layer barrier function via maintaining cell-cell adhesion (By similarity). May also play a role in adherens junction assembly, signal transduction, cell proliferation, synaptogenesis and lymphocyte activation. Regulates the excitability of cardiac myocytes by modulating the …

**Summary**, from NCBI Gene [1739](https://www.ncbi.nlm.nih.gov/gene/1739):

> This gene encodes a multi-domain scaffolding protein that is required for normal development. This protein may have a role in septate junction formation, signal transduction, cell proliferation, synaptogenesis and lymphocyte activation. A multitude of transcript variants deriving from alternative splicing and the use of multiple alternate promoter have been observed, including some splice variants that may be specific to brain and other tissues. An upstream uORF may regulate translation at some …

**Accessions** — [HGNC:2900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2900) · Entrez [1739](https://www.ncbi.nlm.nih.gov/gene/1739) · UniProt [Q12959](https://www.uniprot.org/uniprotkb/Q12959) · Ensembl [ENSG00000075711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075711)

## Data

Gene col 1130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1130); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1130]; `tensor/DDL_lfc|DDL_z.npy` [1130]; `embed/gene_vectors.npy` [1130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1130 or target_col == 1130). Every well: [[DLG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
