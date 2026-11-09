---
symbol: "SBF2"
type: "gene"
col: 5477
ensembl_id: "ENSG00000133812"
name: "SET binding factor 2"
location: "11p15.4"
module: 137
arm: "-"
pooled_cpm: 557.46
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# SBF2

*SET binding factor 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.97× (z +8.8, q 7e-16, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 10 lines (PANC-1 4.81×, H4 4.80×, J82 3.68×, NCI-H23 3.06×, …); [[PH-797804 (drug)]] 5 µM in 3 lines (HS-578T 3.57×, PANC-1 2.59×, LOX-IMVI 2.62×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 1.93×, NCI-H1573 1.88×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 1.75×).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.337× (z -25.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -25.5, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (64 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 38 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM256]] (+0.64, fdr 3e-04), [[KIAA1328]] (+0.64, fdr 8e-05), [[SMYD3]] (+0.62, fdr 2e-04); moves opposite to [[BRPF3]] (-0.69, fdr 5e-05), [[MEPCE]] (-0.65, fdr 2e-04), [[SPRY3]] (-0.62, fdr 8e-04, ⚠ one half only (not replicated)), [[ANKRD18A]] (-0.62, fdr 2e-04).
> It sits in the **-** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5477.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 10 lines (PANC-1 4.81×, H4 4.80×, J82 3.68×, NCI-H23 3.06×, …); [[PH-797804 (drug)]] 5 µM in 3 lines (HS-578T 3.57×, PANC-1 2.59×, LOX-IMVI 2.62×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 1.93×, NCI-H1573 1.88×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 1.75×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +8.8 | 7e-16 | 37/49 (PANC-1, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +5.9 | 1e-06 | 33/48 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.5 | 0.077 | 15/49 (SHP-77, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.337×** | -25.9 | 0e+00 | 44/44 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -25.5 | 0e+00 | 43/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.374×** | -24.3 | 0e+00 | 49/49 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.363×** | -24.1 | 0e+00 | 47/47 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -18.7 | 0e+00 | 47/49 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.478×** | -18.3 | 0e+00 | 48/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.529×** | -15.7 | 0e+00 | 46/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -15.7 | 0e+00 | 47/48 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.505×** | -15.6 | 0e+00 | 43/45 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.533×** | -15.0 | 0e+00 | 45/50 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.628×** | -11.5 | 7e-29 | 47/48 (PANC-1, HOP62, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -10.7 | 3e-25 | 44/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -9.7 | 1e-20 | 46/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -9.6 | 3e-20 | 35/47 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.759×** | -9.5 | 1e-19 | 30/48 (J82, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.762×** | -9.2 | 1e-18 | 31/48 (HOP62, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.716×** | -8.3 | 5e-15 | 41/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.754×** | -7.0 | 1e-10 | 32/48 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.774×** | -6.3 | 8e-09 | 34/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.780×** | -5.7 | 4e-07 | 35/47 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.652×** | -5.5 | 8e-07 | 41/48 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -4.7 | 7e-05 | 24/48 (C32, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1,052 | 8 (4 ⚠) | 11 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.81× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -22.8) |
| [[HOP62 (line)]] | alt | 684 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -33.8) |
| [[C32 (line)]] | wt | 633 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -32.7) |
| [[J82 (line)]] | alt | 544 | 1 | 14 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.68× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.356× (z -16.3) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.500× (z -15.8) |
| [[A549 (line)]] | wt | 727 | 1 | 13 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.44× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -31.2) |
| [[HEC-1-A (line)]] | alt | 732 | 0 | 14 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -23.2) |
| [[HS-578T (line)]] | alt | 557 | 2 | 12 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 3.57× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -17.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -14.6) |
| [[HT-29 (line)]] | alt | 668 | 1 | 13 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.91× (z +9.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -23.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 746 | 2 | 12 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 2.62× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -27.8) |
| [[NCI-H460 (line)]] | wt | 443 | 1 | 13 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 2.59× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -31.9) |
| [[SNU-423 (line)]] | alt | 541 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -21.8) |
| [[SW1417 (line)]] | alt | 560 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.475× (z -19.9) |
| [[Hs 766T (line)]] | wt | 534 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -22.6) |
| [[hTERT-HPNE (line)]] | wt | 501 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -27.8) |
| [[NCI-H2030 (line)]] | alt | 444 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -19.7) |
| [[SK-MEL-2 (line)]] | alt | 605 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -28.3) |
| [[SNU-1 (line)]] | wt | 641 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -15.7) |
| [[A-172 (line)]] | wt | 600 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -16.5) |
| [[BT-474 (line)]] | alt | 760 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -19.3) |
| [[LS 180 (line)]] | wt | 584 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.476× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 425 | 3 (3 ⚠) | 8 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.90× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -26.9) |
| [[Panc 03.27 (line)]] | alt | 288 | 0 | 11 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -19.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.439× (z -19.5) |
| [[RPMI-7951 (line)]] | alt | 456 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -25.9) |
| [[SW480 (line)]] | alt | 578 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.411× (z -16.2) |
| [[LoVo (line)]] | wt | 449 | 2 | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.53× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -24.2) |
| [[NCI-H1792 (line)]] | alt | 459 | 1 (1 ⚠) | 9 (5 ⚠) | [[Digitoxin (drug)]] 5 µM 1.68× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -23.9) |
| [[NCI-H23 (line)]] | alt | 528 | 1 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.06× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -16.2) |
| [[C-33 A (line)]] | alt | 534 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 276 | 0 | 9 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.385× (z -17.0) |
| [[HCT15 (line)]] | alt | 643 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -23.7) |
| [[SW48 (line)]] | wt | 637 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.9) |
| [[A498 (line)]] | wt | 541 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.83× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.466× (z -19.0) |
| [[AN3 CA (line)]] | alt | 755 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -15.1) |
| [[H4 (line)]] | wt | 793 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 488 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -21.4) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -20.0) |
| [[RKO (line)]] | wt | 573 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -17.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.308× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 679 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.2) |
| [[KATO III (line)]] | alt | 300 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -15.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.420× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 418 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -17.5) |
| [[SW 900 (line)]] | alt | 266 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -17.6) |
| [[A-427 (line)]] | wt | 465 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 419 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.408× (z -12.6) |
| [[CHP-212 (line)]] | wt | 437 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -16.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.473× (z -8.6) |
| [[COLO 205 (line)]] | alt | 482 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -17.4) |
| [[SW 1088 (line)]] | alt | 506 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.2) |
| [[SHP-77 (line)]] | alt | 228 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.514× (z -9.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.554× (z -8.7) |
| [[SW 1271 (line)]] | alt | 345 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -11.2) |
| [[NCI-H2122 (line)]] | alt | 522 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 569 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 382 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 13 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM256]] | +0.64 | +0.67 / +0.28 | both halves | 3e-04 |  |
| [[KIAA1328]] | +0.64 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[SMYD3]] | +0.62 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[SLC27A1]] | +0.61 | +0.60 / +0.27 | both halves | 3e-04 |  |
| [[ATRN]] | +0.61 | +0.64 / +0.28 | both halves | 3e-04 |  |
| [[ANKRD27]] | +0.61 | +0.59 / +0.31 | both halves | 2e-04 | pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[SNRPD2]] | +0.59 | +0.65 / +0.20 | both halves | 7e-04 |  |
| [[SLC25A6]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R12B]] | +0.58 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[METRN]] | +0.58 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[RRAS]] | +0.57 | +0.57 / +0.28 | both halves | 3e-04 |  |
| [[ELOB]] | +0.57 | +0.56 / +0.24 | both halves | 4e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 25 of them with an alert (⚠; 25 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRPF3]] | -0.69 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[MEPCE]] | -0.65 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[SPRY3]] | -0.62 | -0.64 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ANKRD18A]] | -0.62 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[RCBTB2]] | -0.62 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[EIF5]] | -0.60 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[ATF5]] | -0.60 | -0.64 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[SLC25A21]] | -0.59 | -0.56 / -0.24 | both halves | 5e-04 |  |
| [[PBDC1]] | -0.59 | -0.65 / -0.30 | both halves | 2e-04 |  |
| [[ARMCX4]] | -0.58 | -0.54 / -0.21 | both halves | 6e-04 |  |
| [[FAIM]] | -0.58 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[ZNF681]] | -0.57 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[ZNF564]] | -0.56 | -0.59 / -0.24 | both halves | 4e-04 |  |
| [[CSRNP2]] | -0.55 | -0.54 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SBF2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity raises SBF2's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **-** arm (projection on the module's main direction -0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-1.3, 6.8); signed map (-34.8, 16.3). **Vector** length 117, 47.7% of its response variance represented; |z| ≥ 3 in 1,722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +8.8 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +7.9 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -10.8 | -18.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.1 | -24.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -15.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -15.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -6.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.4 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | SET binding factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,776,776-10,304,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1766, MTMR13, DENND7B; previously CMT4B2 |
| Gene groups (HGNC) | DENN domain containing; Pleckstrin homology domain containing; Myotubularins |
| Reactome | 8 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WG5](https://www.uniprot.org/uniprotkb/Q86WG5) (Myotubularin-related protein 13):

> Guanine nucleotide exchange factor (GEF) which activates RAB21 and possibly RAB28. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form. In response to starvation-induced autophagy, activates RAB21 which in turn binds to and regulates SNARE protein VAMP8 endolysosomal transport required for SNARE-mediated autophagosome-lysosome fusion. Acts as an adapter for the phosphatase MTMR2 (By similarity). Increases MTMR2 catalytic activity …

**Summary**, from NCBI Gene [81846](https://www.ncbi.nlm.nih.gov/gene/81846):

> This gene encodes a pseudophosphatase and member of the myotubularin-related protein family. This gene maps within the CMT4B2 candidate region of chromosome 11p15 and mutations in this gene have been associated with Charcot-Marie-Tooth Disease, type 4B2. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2135) · Entrez [81846](https://www.ncbi.nlm.nih.gov/gene/81846) · UniProt [Q86WG5](https://www.uniprot.org/uniprotkb/Q86WG5) · Ensembl [ENSG00000133812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133812)

## Data

Gene col 5477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5477); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5477]; `tensor/DDL_lfc|DDL_z.npy` [5477]; `embed/gene_vectors.npy` [5477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5477 or target_col == 5477). Every well: [[SBF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SBF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
