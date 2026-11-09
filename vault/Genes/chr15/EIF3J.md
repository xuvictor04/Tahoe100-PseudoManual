---
symbol: "EIF3J"
type: "gene"
col: 2417
ensembl_id: "ENSG00000104131"
name: "eukaryotic translation initiation factor 3 subunit J"
location: "15q21.1"
module: 5
arm: "+"
pooled_cpm: 109.94
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# EIF3J

*eukaryotic translation initiation factor 3 subunit J* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.70× (z +18.6, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.01× (z +14.6, q 1e-45, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.724× (z -4.3, q 0.010, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.528×; ⚠ cell-cycle shift, explains ~20% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.706×; ⚠ position not correctable); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.558×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH4]] (+0.72, fdr 7e-06), [[METTL2B]] (+0.70, fdr 7e-06), [[DDX21]] (+0.68, fdr 7e-06); moves opposite to [[GGH]] (-0.68, fdr 7e-06), [[LAPTM4A]] (-0.65, fdr 7e-06), [[GM2A]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.70×** | +18.6 | 0e+00 | 47/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.01×** | +14.6 | 1e-45 | 47/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.51×** | +11.5 | 3e-28 | 47/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.36×** | +11.4 | 8e-28 | 46/49 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +11.3 | 9e-28 | 47/48 (SW480, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.06×** | +9.0 | 1e-17 | 42/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.94×** | +8.8 | 1e-16 | 42/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +8.5 | 1e-15 | 46/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.89×** | +8.4 | 3e-15 | 46/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +8.0 | 8e-14 | 44/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +7.9 | 2e-13 | 45/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.90×** | +7.9 | 2e-13 | 39/45 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +6.3 | 1e-08 | 41/47 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.2 | 3e-08 | 42/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +6.2 | 3e-08 | 42/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +5.9 | 9e-08 | 43/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 6e-05 | 34/49 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 4e-04 | 31/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.83×** | +4.2 | 7e-04 | 38/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.003 | 34/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.004 | 31/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.004 | 34/48 (SW1417, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.005 | 29/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.006 | 29/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2417.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.528×; ⚠ cell-cycle shift, explains ~20% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.706×; ⚠ position not correctable); [[Selinexor (drug)]] 5 µM in 1 line (RKO 0.558×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.724×** | -4.3 | 0.010 | 36/48 (LoVo, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.829×** | -3.5 | 0.095 | 25/48 (RKO, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.095 | 24/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.774× | -3.1 | 0.19 | 30/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.790× | -3.1 | 0.19 | 24/48 (A-427, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 162 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +19.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 99.5 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +23.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.23× (z +18.5) | — |
| [[NCI-H1792 (line)]] | alt | 98.1 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 147 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +17.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.35× (z +13.5) | — |
| [[SW480 (line)]] | alt | 138 | 8 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.22× (z +13.3) | — |
| [[A-172 (line)]] | wt | 73.5 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +17.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +12.1) | — |
| [[A498 (line)]] | wt | 127 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +19.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 86.8 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +19.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.56× (z +13.5) | — |
| [[A549 (line)]] | wt | 82.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 99.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 119 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.43× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 59.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +15.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 105 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 82.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.56× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 90.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +19.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.62× (z +12.7) | — |
| [[H4 (line)]] | wt | 81.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +14.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.01× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 67.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 133 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 156 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +19.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 131 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 99.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 129 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.13× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 76.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +20.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 64.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +13.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +9.0) | — |
| [[J82 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +8.9) | — |
| [[KATO III (line)]] | alt | 116 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 90.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 68.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +10.2) | — |
| [[A-427 (line)]] | wt | 103 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.33× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 116 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.66× (z +8.8) | — |
| [[C32 (line)]] | wt | 72.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 117 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 64.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 175 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 49.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +9.4) | — |
| [[RKO (line)]] | wt | 177 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[C-33 A (line)]] | alt | 140 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +12.3) | — |
| [[CHP-212 (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW1417 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | +0.72 | +0.82 / +0.66 | both halves | 7e-06 |  |
| [[METTL2B]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[DDX21]] | +0.68 | +0.63 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 412 |
| [[GTPBP4]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PUS1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SDAD1]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ZNF562]] | +0.64 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[NOP56]] | +0.63 | +0.74 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[BICD1]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[RRP7A]] | +0.63 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | -0.68 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.65 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[GM2A]] | -0.61 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ORC4]] | -0.61 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[CAT]] | -0.61 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[KLHDC3]] | -0.60 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.60 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.60 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[BAG4]] | -0.60 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[ITM2C]] | -0.60 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[APAF1]] | -0.60 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[DUSP11]] | -0.60 | -0.64 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity lowers EIF3J's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.35× higher at baseline in the lines without ADD3 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.2, -30.5); signed map (3.5, -45.9). **Vector** length 84.5, 33.3% of its response variance represented; |z| ≥ 3 in 1,461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +14.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:44,537,125-44,563,029 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-p35, eIF3-alpha; previously EIF3S1 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits |
| Hallmark sets | ALLOGRAFT_REJECTION, MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75822](https://www.uniprot.org/uniprotkb/O75822) (Eukaryotic translation initiation factor 3 subunit J):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [8669](https://www.ncbi.nlm.nih.gov/gene/8669):

> This gene encodes a core subunit of the eukaryotic initiation factor 3 complex, which participates in the initiation of translation by aiding in the recruitment of protein and mRNA components to the 40S ribosome. There are pseudogenes for this gene on chromosomes 1, 3, and 9. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:3270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3270) · Entrez [8669](https://www.ncbi.nlm.nih.gov/gene/8669) · UniProt [O75822](https://www.uniprot.org/uniprotkb/O75822) · Ensembl [ENSG00000104131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104131)

## Data

Gene col 2417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2417); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2417]; `tensor/DDL_lfc|DDL_z.npy` [2417]; `embed/gene_vectors.npy` [2417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2417 or target_col == 2417). Every well: [[EIF3J — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3J.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
