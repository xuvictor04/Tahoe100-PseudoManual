---
symbol: "AKAP9"
type: "gene"
col: 4840
ensembl_id: "ENSG00000127914"
name: "A-kinase anchoring protein 9"
location: "7q21.2"
module: 74
arm: "+"
pooled_cpm: 494.78
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# AKAP9

*A-kinase anchoring protein 9* — 7q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +10.5, q 3e-23, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.30× (z +4.5, q 7e-04, up in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (BT-474 2.72×, C32 2.29×, LS 180 2.30×, HT-29 2.11×, …; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (C32 2.53×, LS 180 2.50×, RKO 2.26×, HEC-1-A 2.24×; ⚠ cell-cycle shift, explains ~27% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (C32 2.41×; ⚠ cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 1.72×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 1.71×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.481× (z -24.6, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC186]] (+0.77, fdr 7e-06), [[SEC62]] (+0.77, fdr 7e-06), [[CIR1]] (+0.76, fdr 7e-06); moves opposite to [[UBE2G2]] (-0.64, fdr 8e-06), [[EIF5A]] (-0.62, fdr 1e-05), [[TATDN2]] (-0.61, fdr 9e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4840.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (BT-474 2.72×, C32 2.29×, LS 180 2.30×, HT-29 2.11×, …; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (C32 2.53×, LS 180 2.50×, RKO 2.26×, HEC-1-A 2.24×; ⚠ cell-cycle shift, explains ~27% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (C32 2.41×; ⚠ cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (C32 1.72×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 1.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +10.5 | 3e-23 | 29/48 (BT-474, C32, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.42×** | +8.4 | 1e-14 | 29/48 (C32, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +5.0 | 1e-04 | 26/48 (C32, BT-474, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.47×** | +4.8 | 2e-04 | 41/47 (BT-474, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 7e-04 | 38/48 (A498, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.29× | +3.2 | 0.13 | 22/49 (A498, NCI-H2347, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.19 | 2/49 (BT-474, KATO III) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.481×** | -24.6 | 0e+00 | 46/49 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.464×** | -18.2 | 0e+00 | 48/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.575×** | -12.6 | 3e-34 | 46/47 (KATO III, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.608×** | -10.9 | 2e-25 | 39/45 (CFPAC-1, SW48, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.692×** | -8.7 | 3e-16 | 37/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.711×** | -8.1 | 6e-14 | 32/48 (KATO III, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.523×** | -8.0 | 8e-14 | 47/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.524×** | -8.0 | 8e-14 | 48/48 (PANC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.543×** | -7.6 | 2e-12 | 47/48 (MIA PaCa-2, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -7.3 | 1e-11 | 33/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.735×** | -7.3 | 1e-11 | 34/48 (Hs 766T, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.726×** | -7.3 | 1e-11 | 34/44 (AsPC-1, HCT15, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -6.8 | 6e-10 | 34/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.753×** | -6.7 | 8e-10 | 35/48 (KATO III, SW480, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.588×** | -6.6 | 2e-09 | 43/48 (CFPAC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.603×** | -6.3 | 1e-08 | 45/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.720×** | -5.6 | 8e-07 | 43/48 (PANC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.686×** | -4.7 | 7e-05 | 32/49 (HS-578T, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.714×** | -4.2 | 7e-04 | 32/47 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.852× | -3.8 | 0.003 | 16/48 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.857× | -3.6 | 0.005 | 17/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.006 | 27/48 (RPMI-7951, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.813×** | -3.5 | 0.009 | 28/49 (PANC-1, SW48, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 685 | 2 (2 ⚠) | 11 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -21.5) |
| [[CFPAC-1 (line)]] | alt | 617 | 0 | 12 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -17.7) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 684 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -26.6) |
| [[KATO III (line)]] | alt | 803 | 1 (1 ⚠) | 10 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.212× (z -19.2) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -15.2) |
| [[C32 (line)]] | wt | 702 | 6 (4 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.72× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -23.9) |
| [[Hs 766T (line)]] | wt | 529 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -26.4) |
| [[NCI-H1792 (line)]] | alt | 635 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -21.5) |
| [[HOP62 (line)]] | alt | 370 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -17.7) |
| [[SNU-423 (line)]] | alt | 489 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -26.7) |
| [[H4 (line)]] | wt | 522 | 1 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -19.8) |
| [[HS-578T (line)]] | alt | 482 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -25.5) |
| [[BT-474 (line)]] | alt | 398 | 4 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +19.2) ⚠ cell-cycle shift, explains ~26% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -10.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.8) |
| [[HCT15 (line)]] | alt | 753 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.338× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.5) |
| [[HT-29 (line)]] | alt | 634 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +17.8) ⚠ cell-cycle shift, explains ~26% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -19.9) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 495 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.299× (z -17.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.381× (z -13.6) |
| [[PANC-1 (line)]] | alt | 309 | 0 | 6 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -20.7) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -11.6) |
| [[RKO (line)]] | wt | 530 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +13.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -20.0) |
| [[SK-MEL-2 (line)]] | alt | 547 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -22.4) |
| [[SW 900 (line)]] | alt | 592 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -21.1) |
| [[SW1417 (line)]] | alt | 552 | 2 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +14.4) ⚠ cell-cycle shift, explains ~26% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.366× (z -18.6) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -18.2) |
| [[COLO 205 (line)]] | alt | 488 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.305× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.6) |
| [[LoVo (line)]] | wt | 675 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 530 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.410× (z -16.8) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -14.4) |
| [[SW48 (line)]] | wt | 624 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -16.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -10.5) |
| [[A498 (line)]] | wt | 749 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -26.6) |
| [[HEC-1-A (line)]] | alt | 414 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.3) ⚠ cell-cycle shift, explains ~26% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.412× (z -14.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 527 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +18.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 472 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -14.7) |
| [[SNU-1 (line)]] | wt | 426 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -10.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 453 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -24.5) |
| [[AN3 CA (line)]] | alt | 548 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 350 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -19.7) |
| [[hTERT-HPNE (line)]] | wt | 432 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 289 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 478 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 322 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -20.2) |
| [[RPMI-7951 (line)]] | alt | 425 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -14.5) |
| [[A-172 (line)]] | wt | 368 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -14.1) |
| [[A-427 (line)]] | wt | 336 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.504× (z -11.1) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 361 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 488 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 321 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -21.5) |
| [[SW 1271 (line)]] | alt | 519 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -11.4) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 416 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.4) |
| [[J82 (line)]] | alt | 280 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -10.3) |
| [[NCI-H2122 (line)]] | alt | 593 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 507 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 641 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 799 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC186]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[SEC62]] | +0.77 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[CIR1]] | +0.76 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[GOLGB1]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 | STRING 515 |
| [[TMF1]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[BOD1L1]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[GCC2]] | +0.70 | +0.73 / +0.69 | both halves | 7e-06 | STRING 723 |
| [[NKAP]] | +0.69 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[RSF1]] | +0.69 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[IK]] | +0.69 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[CEP350]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 | STRING 417 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.64 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[EIF5A]] | -0.62 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[TATDN2]] | -0.61 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[RNPS1]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[VMA21]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[UBE2N]] | -0.60 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[SENP3]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[AKT1]] | -0.59 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[PSME3]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TTL]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AKAP9's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.4, -47.7); signed map (-10.9, -4.5). **Vector** length 165, 66.2% of its response variance represented; |z| ≥ 3 in 1,713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +11.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +9.8 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +9.3 | +5.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.0 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +4.4 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.9 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.8 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.1 | -18.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.1 | -7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.5 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -8.2 | -6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.1 | -8.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.8 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:91,940,840-92,110,673 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0803, AKAP350, AKAP450, CG-NAP, YOTIAO, HYPERION, PRKA9, MU-RMS-40.16A |
| Gene groups (HGNC) | A-kinase anchoring proteins; Protein phosphatase 1 regulatory subunits |
| Reactome | 24 pathways, smallest: Phase 3 - rapid repolarisation; Phase 2 - plateau phase; Signaling by BRAF and RAF1 fusions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99996](https://www.uniprot.org/uniprotkb/Q99996) (A-kinase anchor protein 9):

> Scaffolding protein that assembles several protein kinases and phosphatases on the centrosome and Golgi apparatus. Required to maintain the integrity of the Golgi apparatus. Required for microtubule nucleation at the cis-side of the Golgi apparatus. Required for association of the centrosomes with the poles of the bipolar mitotic spindle during metaphase. In complex with PDE4DIP isoform 13/MMG8/SMYLE, recruits CAMSAP2 to the Golgi apparatus and tethers non-centrosomal minus-end microtubules to …

**Summary**, from NCBI Gene [10142](https://www.ncbi.nlm.nih.gov/gene/10142):

> The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. Alternate splicing of this gene results in at least two isoforms that localize to the centrosome and the Golgi apparatus, and interact with numerous signaling proteins from multiple signal transduction …

**Accessions** — [HGNC:379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:379) · Entrez [10142](https://www.ncbi.nlm.nih.gov/gene/10142) · UniProt [Q99996](https://www.uniprot.org/uniprotkb/Q99996) · Ensembl [ENSG00000127914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127914)

## Data

Gene col 4840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4840); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4840]; `tensor/DDL_lfc|DDL_z.npy` [4840]; `embed/gene_vectors.npy` [4840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4840 or target_col == 4840). Every well: [[AKAP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
