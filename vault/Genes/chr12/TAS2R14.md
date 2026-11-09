---
symbol: "TAS2R14"
type: "gene"
col: 13068
ensembl_id: "ENSG00000212127"
name: "taste 2 receptor member 14"
location: "12p13.2"
module: 213
arm: "+"
pooled_cpm: 372.17
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# TAS2R14

*taste 2 receptor member 14* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.28× (z +4.5, q 0.004, up in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LS 180 1.72×, RKO 1.63×, HEC-1-A 1.49×, KATO III 1.57×, …; ⚠ cell-cycle shift, explains ~54% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 1.84×, HEC-1-A 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 1.79×); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 2.03×).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.488× (z -19.7, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRH1]] (+0.74, fdr 7e-06, ⚠ same locus), [[STXBP4]] (+0.61, fdr 1e-05), [[COMMD10]] (+0.59, fdr 2e-05), [[JPX]] (+0.59, fdr 1e-05); moves opposite to [[JUP]] (-0.58, fdr 1e-05), [[ABI1]] (-0.53, fdr 2e-05), [[MXD1]] (-0.53, fdr 5e-05).
> It is in [[Module 213]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); 2 go from it, the strongest it → [[PRH1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13068.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (LS 180 1.72×, RKO 1.63×, HEC-1-A 1.49×, KATO III 1.57×, …; ⚠ cell-cycle shift, explains ~54% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LoVo 1.84×, HEC-1-A 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (NCI-H1573 1.79×); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 2.03×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 0.004 | 28/47 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.21× | +3.5 | 0.12 | 24/48 (COLO 205, NCI-H2347, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 1.13× | +3.3 | 0.17 | 0/48 | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.17 | 11/48 (LoVo, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.488×** | -19.7 | 0e+00 | 49/49 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.376×** | -18.9 | 0e+00 | 46/49 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.363×** | -18.9 | 0e+00 | 43/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.506×** | -13.2 | 1e-37 | 44/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -12.9 | 5e-36 | 46/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.528×** | -12.4 | 4e-33 | 44/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.509×** | -12.1 | 9e-32 | 40/45 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -10.3 | 3e-23 | 44/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.593×** | -10.1 | 4e-22 | 44/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -9.0 | 2e-17 | 36/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -8.7 | 1e-16 | 35/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.641×** | -8.6 | 4e-16 | 43/48 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -7.1 | 6e-11 | 36/50 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.707×** | -6.7 | 9e-10 | 38/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.716×** | -6.2 | 2e-08 | 33/47 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.883× | -3.4 | 0.020 | 11/49 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.785×** | -3.3 | 0.022 | 26/48 (HOP62, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.849× | -3.2 | 0.039 | 14/48 (H4, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.041 | 14/48 (HOP62, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.740×** | -3.0 | 0.052 | 23/49 (NCI-H1792, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.859× | -2.9 | 0.067 | 18/48 (CFPAC-1, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 259 | 0 | 16 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -16.3) |
| [[HOP62 (line)]] | alt | 693 | 0 | 15 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.9) |
| [[PANC-1 (line)]] | alt | 333 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -22.3) |
| [[MIA PaCa-2 (line)]] | alt | 416 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.343× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 690 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -16.5) |
| [[SW480 (line)]] | alt | 548 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -15.0) |
| [[A-427 (line)]] | wt | 813 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.2) |
| [[C32 (line)]] | wt | 444 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -26.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 907 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -28.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -16.9) |
| [[SW 900 (line)]] | alt | 624 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -15.9) |
| [[RKO (line)]] | wt | 386 | 1 (1 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.2) ⚠ cell-cycle shift, explains ~54% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -14.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -13.6) |
| [[C-33 A (line)]] | alt | 577 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -15.2) |
| [[HCT15 (line)]] | alt | 483 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.378× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 407 | 0 | 9 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -16.2) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.332× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 500 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -19.3) |
| [[SK-MEL-2 (line)]] | alt | 352 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -15.0) |
| [[SNU-423 (line)]] | alt | 235 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -20.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -16.8) |
| [[H4 (line)]] | wt | 569 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 279 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -17.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 389 | 1 | 7 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.79× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -17.5) |
| [[A498 (line)]] | wt | 179 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 369 | 1 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.365× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -15.9) |
| [[HT-29 (line)]] | alt | 436 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -11.8) |
| [[KATO III (line)]] | alt | 262 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.4) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 5 µM 0.268× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -8.9) |
| [[LoVo (line)]] | wt | 549 | 1 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 258 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -11.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.395× (z -11.2) |
| [[SW1417 (line)]] | alt | 308 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -14.5) |
| [[A-172 (line)]] | wt | 154 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -16.6) |
| [[J82 (line)]] | alt | 290 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.9) |
| [[Hs 766T (line)]] | wt | 209 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -12.8) |
| [[SNU-1 (line)]] | wt | 480 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.416× (z -10.4) |
| [[SW48 (line)]] | wt | 334 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.8) |
| [[CHP-212 (line)]] | wt | 496 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -13.9) |
| [[SHP-77 (line)]] | alt | 255 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.78× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 783 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -10.3) |
| [[A549 (line)]] | wt | 340 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -22.6) |
| [[BT-474 (line)]] | alt | 279 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.03× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.8) |
| [[LS 180 (line)]] | wt | 349 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.7) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -13.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 329 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -10.3) |
| [[COLO 205 (line)]] | alt | 299 | 1 (1 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.03× (z +8.7) ⚠ cell-cycle shift, explains ~44% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 209 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 245 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2122 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 408 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 300 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRH1]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[STXBP4]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[COMMD10]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[JPX]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[USP34]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NMT1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 | pathway: Sensory Perception |
| [[PRR4]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MTREX]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[ACBD6]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TAS2R30]] | +0.57 | +0.70 / +0.44 | both halves | 3e-05 | same gene group; pathway: Class C/3 (Metabotropic glutamate/pheromone receptors); STRING 478; ⚠ **readthrough risk**: TAS2R30 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CLPB]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LARS2]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NF1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUP]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ABI1]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MXD1]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[RAB11A]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RNF39]] | -0.51 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[HECA]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[NATD1]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[GRB7]] | -0.49 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[FOXO4]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[CAPN1-AS1]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CACNB3]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PLCB3]] | -0.48 | -0.39 / -0.41 | both halves | 6e-05 | pathway: G alpha (i) signalling events |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity weakens TAS2R14's drug response | lines that do not express IRF6 (31) vs lines expressing it (18) | the lines without IRF6 respond 1.29× as strongly (z diff -2.00); strongest at Auranofin 5 µM: 0.56x vs 0.78x (z diff -3.8) | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; artifact flags |
| [[JUP]] | B | JUP activity weakens TAS2R14's drug response | lines that do not express JUP (16) vs lines expressing it (33) | the lines without JUP respond 1.27× as strongly (z diff -1.51); strongest at Auranofin 5 µM: 0.48x vs 0.72x (z diff -3.8) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671; target measured in part of the lines; artifact flags |
| [[JUP]] | B | JUP activity lowers TAS2R14's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.30× higher at baseline in the lines without JUP | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[PRH1]] | C | PRH1's natural level strengthens TAS2R14's drug response | PRH1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.75; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRH1]] | C | TAS2R14's natural level strengthens PRH1's drug response | TAS2R14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.64; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TAS2R30]] | C | TAS2R14's natural level strengthens TAS2R30's drug response | TAS2R14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.58; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.7, 14.6); signed map (7.6, -43.2). **Vector** length 106, 43.1% of its response variance represented; |z| ≥ 3 in 1,346 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.3 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +4.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.2 | -8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -19.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.7 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | taste 2 receptor member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,937,408-11,171,573 (-) |
| Ensembl biotype | protein_coding |
| Also known as | T2R14, TRB1 |
| Gene groups (HGNC) | Taste 2 receptors |
| Reactome | 8 pathways, smallest: Class C/3 (Metabotropic glutamate/pheromone receptors); Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYV8](https://www.uniprot.org/uniprotkb/Q9NYV8) (Taste receptor type 2 member 14):

> Gustducin-linked G protein-coupled receptor that plays a role in the perception of bitterness. The activity of this receptor stimulates GNAT3, activating the gustducin G protein pathway. Likely plays a role in sensing the chemical composition of the gastrointestinal content and other extra-oral tissues via the inhibitory G protein pathways.

**Summary**, from NCBI Gene [50840](https://www.ncbi.nlm.nih.gov/gene/50840):

> This gene product belongs to the family of candidate taste receptors that are members of the G-protein-coupled receptor superfamily. These proteins are specifically expressed in the taste receptor cells of the tongue and palate epithelia. They are organized in the genome in clusters and are genetically linked to loci that influence bitter perception in mice and humans. In functional expression studies, they respond to bitter tastants. This gene maps to the taste receptor gene cluster on …

**Accessions** — [HGNC:14920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14920) · Entrez [50840](https://www.ncbi.nlm.nih.gov/gene/50840) · UniProt [Q9NYV8](https://www.uniprot.org/uniprotkb/Q9NYV8) · Ensembl [ENSG00000212127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000212127)

## Data

Gene col 13068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13068); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13068]; `tensor/DDL_lfc|DDL_z.npy` [13068]; `embed/gene_vectors.npy` [13068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13068 or target_col == 13068). Every well: [[TAS2R14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAS2R14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
