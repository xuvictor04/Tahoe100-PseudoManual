---
symbol: "REV1"
type: "gene"
col: 5786
ensembl_id: "ENSG00000135945"
name: "REV1 DNA directed polymerase"
location: "2q11.2"
module: 146
arm: "+"
pooled_cpm: 80.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# REV1

*REV1 DNA directed polymerase* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.83× (z +7.2, q 4e-10, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -19.2, q 0e+00, down in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (HEC-1-A 0.392×, A-172 0.371×, A498 0.444×, C32 0.374×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.108×, HCT15 0.0799×, NCI-H1573 0.107×, A549 0.128×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (H4 0.0464×, NCI-H23 0.192×, A498 0.299×, SW480 0.326×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.414×, LOX-IMVI 0.415×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.243×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf136]] (+0.66, fdr 7e-06), [[C15orf61]] (+0.62, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[ZNF592]] (+0.62, fdr 8e-06), [[FIP1L1]] (+0.62, fdr 7e-06); moves opposite to [[ATP6V1D]] (-0.56, fdr 1e-05), [[GPATCH2L]] (-0.55, fdr 1e-05), [[CCNT2-AS1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +7.2 | 4e-10 | 38/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +6.0 | 6e-07 | 23/48 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +5.5 | 7e-06 | 27/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +5.1 | 5e-05 | 25/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.8 | 2e-04 | 24/47 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.21×** | +4.3 | 0.001 | 24/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.011 | 20/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.4 | 0.054 | 15/38 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.12 | 13/48 (SW480, J82, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5786.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (HEC-1-A 0.392×, A-172 0.371×, A498 0.444×, C32 0.374×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW480 0.108×, HCT15 0.0799×, NCI-H1573 0.107×, A549 0.128×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (H4 0.0464×, NCI-H23 0.192×, A498 0.299×, SW480 0.326×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.414×, LOX-IMVI 0.415×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -19.2 | 0e+00 | 45/49 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.459×** | -17.7 | 0e+00 | 44/49 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -16.9 | 0e+00 | 38/44 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -11.4 | 4e-28 | 34/45 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -10.4 | 2e-23 | 36/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.657×** | -9.5 | 2e-19 | 34/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.744×** | -6.4 | 9e-09 | 30/50 (HEC-1-A, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.765×** | -6.1 | 8e-08 | 25/48 (SW480, J82, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -6.0 | 1e-07 | 2/50 (SW 1271, SW 1088) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.770×** | -5.7 | 6e-07 | 25/48 (C32, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -4.7 | 1e-04 | 18/48 (SNU-1, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~14% of this change | **0.825×** | -4.4 | 6e-04 | 23/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -4.2 | 0.001 | 20/48 (HS-578T, C32, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.856× | -3.5 | 0.017 | 20/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.057 | 10/48 (SW 1088, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 143 | 2 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.46× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -20.6) |
| [[SW480 (line)]] | alt | 90.0 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.47× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -32.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -13.0) |
| [[C32 (line)]] | wt | 88.1 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 85.4 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.278× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 59.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 76.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -10.3) |
| [[A498 (line)]] | wt | 95.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -16.4) |
| [[J82 (line)]] | alt | 77.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.7) |
| [[PANC-1 (line)]] | alt | 82.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.3) |
| [[SW1417 (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.4) |
| [[A-172 (line)]] | wt | 74.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -17.2) |
| [[A549 (line)]] | wt | 80.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 76.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.6) |
| [[LS 180 (line)]] | wt | 112 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 74.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -13.8) |
| [[SNU-1 (line)]] | wt | 88.7 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.243× (z -17.9) |
| [[A-427 (line)]] | wt | 62.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 96.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 67.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 50.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.5) |
| [[HT-29 (line)]] | alt | 81.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.7) |
| [[KATO III (line)]] | alt | 56.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 69.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -13.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 86.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.302× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 89.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.9) |
| [[BT-474 (line)]] | alt | 76.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.7) |
| [[C-33 A (line)]] | alt | 93.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -14.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 66.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.35× (z +8.9) | — |
| [[H4 (line)]] | wt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0464× (z -25.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 88.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0799× (z -24.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 90.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.4) | — |
| [[LoVo (line)]] | wt | 72.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 81.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -10.5) |
| [[SHP-77 (line)]] | alt | 86.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf136]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[C15orf61]] ⚠ | +0.62 | +0.59 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF592]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[FIP1L1]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MLLT10]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.57 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KAT14]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TADA1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RWDD1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PUM2]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CC2D1A]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | -0.55 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[KCTD5]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RP2]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CDC37]] | -0.52 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[NOP14-AS1]] | -0.51 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CCDC200]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[EXOC7]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[APLP2]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[MSN]] | -0.51 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.50 | -0.51 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises REV1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises REV1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.0, -3.6); signed map (-25.8, -12.7). **Vector** length 89.0, 22.5% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -19.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.8 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | REV1 DNA directed polymerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,400,475-99,490,035 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously REV1L |
| Gene groups (HGNC) | DNA polymerases |
| Reactome | 13 pathways, smallest: Translesion synthesis by REV1; Translesion synthesis by POLI; Translesion synthesis by POLK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBZ9](https://www.uniprot.org/uniprotkb/Q9UBZ9) (Translesion synthesis protein REV1):

> Bifunctional protein involved in the maintenance of genome stability through translesion DNA synthesis (TLS) and antibody diversification via somatic hypermutation. Functions as a molecular adapter protein at stalled DNA replication, coordinating polymerases recruitment, selection, and switching, in a manner independent of its deoxycytidyl transferase activity. At the site of DNA lesion, recruits and mediates the switch between low-fidelity inserter DNA polymerases, such as POLK, that …

**Summary**, from NCBI Gene [51455](https://www.ncbi.nlm.nih.gov/gene/51455):

> This gene encodes a protein with similarity to the S. cerevisiae mutagenesis protein Rev1. The Rev1 proteins contain a BRCT domain, which is important in protein-protein interactions. A suggested role for the human Rev1-like protein is as a scaffold that recruits DNA polymerases involved in translesion synthesis (TLS) of damaged DNA. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:14060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14060) · Entrez [51455](https://www.ncbi.nlm.nih.gov/gene/51455) · UniProt [Q9UBZ9](https://www.uniprot.org/uniprotkb/Q9UBZ9) · Ensembl [ENSG00000135945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135945)

## Data

Gene col 5786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5786); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5786]; `tensor/DDL_lfc|DDL_z.npy` [5786]; `embed/gene_vectors.npy` [5786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5786 or target_col == 5786). Every well: [[REV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
