---
symbol: "SHOC2"
type: "gene"
col: 2914
ensembl_id: "ENSG00000108061"
name: "SHOC2 leucine rich repeat scaffold protein"
location: "10q25.2"
module: 4
arm: "-"
pooled_cpm: 151.43
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SHOC2

*SHOC2 leucine rich repeat scaffold protein* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +19.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.457× (z -21.9, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.822× (z -5.5, q 6e-06, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-427 0.0673×, AN3 CA 0.109×, A498 0.340×, NCI-H1792 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 0.406×, LS 180 0.286×, KATO III 0.311×, Panc 03.27 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.328×, KATO III 0.306×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.490×); [[ULK-101 (drug)]] 5 µM in 1 line (CHP-212 0.0756×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.551×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL5]] (+0.65, fdr 7e-06), [[TNRC6C]] (+0.62, fdr 1e-05), [[BTG1]] (+0.61, fdr 1e-05); moves opposite to [[NAA25]] (-0.65, fdr 7e-06), [[FIRRE]] (-0.64, fdr 7e-06), [[MRPL3]] (-0.61, fdr 7e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +19.2 | 0e+00 | 44/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +10.7 | 3e-24 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +8.6 | 1e-15 | 35/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +8.0 | 3e-13 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +7.9 | 3e-13 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +7.4 | 1e-11 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +5.9 | 2e-07 | 26/48 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +5.7 | 1e-06 | 27/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.6 | 1e-06 | 25/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.4 | 3e-06 | 21/49 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.4 | 4e-06 | 11/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +5.2 | 8e-06 | 24/48 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | **1.20×** | +5.2 | 1e-05 | 24/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.19× | +4.7 | 8e-05 | 18/49 (RKO, HEC-1-A, …) | two highest doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.18× | +4.6 | 2e-04 | 20/48 (A-427, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.16× | +4.2 | 1e-03 | 13/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.054 | 15/47 (NCI-H2030, SW48, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.1 | 0.060 | 10/48 (RKO, SW1417, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.091 | 11/48 (NCI-H23, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-427 0.0673×, AN3 CA 0.109×, A498 0.340×, NCI-H1792 0.246×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 0.406×, LS 180 0.286×, KATO III 0.311×, Panc 03.27 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.328×, KATO III 0.306×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H1573 0.490×); [[ULK-101 (drug)]] 5 µM in 1 line (CHP-212 0.0756×); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.551×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.457×** | -21.9 | 0e+00 | 45/49 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.481×** | -18.9 | 0e+00 | 42/45 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -18.9 | 0e+00 | 39/44 (A-427, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.822×** | -5.5 | 6e-06 | 22/48 (A-427, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.845× | -4.7 | 2e-04 | 19/48 (AN3 CA, C32, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.900× | -4.2 | 0.002 | 9/48 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.863× | -4.0 | 0.005 | 20/48 (NCI-H1573, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | 0.871× | -3.7 | 0.013 | 14/47 (NCI-H2347, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.885× | -3.4 | 0.037 | 14/48 (hTERT-HPNE, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.888× | -3.3 | 0.046 | 6/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.087 | 18/48 (CFPAC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.899× | -3.0 | 0.12 | 6/48 (HT-29, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 10 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +25.7) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -16.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 117 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.550× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 157 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +22.9) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -17.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 201 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +21.8) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -18.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 110 | 4 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -15.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 143 | 4 (2 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.404× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 225 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.490× (z -10.2) |
| [[A-427 (line)]] | wt | 143 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.0673× (z -38.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.551× (z -8.8) |
| [[LS 180 (line)]] | wt | 170 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 97.7 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[RKO (line)]] | wt | 145 | 4 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 134 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 149 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.340× (z -19.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 210 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -16.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 132 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 124 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +17.5) | — |
| [[SW1417 (line)]] | alt | 167 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.481× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 193 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -15.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 269 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.94× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -15.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 221 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -17.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 220 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.225× (z -18.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -18.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 141 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -19.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 155 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 191 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 281 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -19.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[ULK-101 (drug)]] 5 µM 0.0756× (z -9.0) |
| [[COLO 205 (line)]] | alt | 174 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.5) | — |
| [[H4 (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -14.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 99.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -13.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.524× (z -9.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.0) | — |
| [[SW48 (line)]] | wt | 110 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -9.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.5) | — |
| [[SW 900 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL5]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TNRC6C]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 | pathway: MAPK family signaling cascades |
| [[BTG1]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[POLD4]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ZRANB1]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[DAAM1]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[MTHFR]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[BMAL1]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ING2]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA25]] | -0.65 | -0.67 / -0.64 | both halves | 7e-06 | same gene group |
| [[FIRRE]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[MRPL3]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[SORD]] | -0.61 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.61 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[NUP155]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SLC19A1]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[PFAS]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.58 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[CSTF2]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity strengthens SHOC2's drug response | lines that do not express DUXAP8 (7) vs lines expressing it (42) | the lines without DUXAP8 respond 0.89× as strongly (z diff +1.27); strongest at Panobinostat 5 µM: 1.07x vs 1.38x (z diff +3.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2; target measured in part of the lines; artifact flags |
| [[CRACR2A]] | B | CRACR2A activity lowers SHOC2's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 1.16× higher at baseline in the lines without CRACR2A | 0.073 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[AASS]] | B | AASS activity lowers SHOC2's level | lines that do not express AASS (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without AASS | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC00159, ZNF391, DISC1 |
| [[HDAC6]] | B | HDAC6 activity lowers SHOC2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.8, -34.1); signed map (-6.0, 9.3). **Vector** length 109, 33.0% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.2 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.9 | +5.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -18.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -18.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SHOC2 leucine rich repeat scaffold protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,919,367-111,017,307 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0862, SOC2, SUR-8, SOC-2, SUR8 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: Gain-of-function MRAS complexes activate RAF signaling; SHOC2 M1731 mutant abolishes MRAS complex function; Signaling by MRAS-complex mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ13](https://www.uniprot.org/uniprotkb/Q9UQ13) (Leucine-rich repeat protein SHOC-2):

> Core component of the SHOC2-MRAS-PP1c (SMP) holophosphatase complex that regulates activation of the MAPK pathway. Acts as a scaffolding protein in the SMP complex. The SMP complex specifically dephosphorylates the inhibitory phosphorylation at 'Ser-259' of RAF1 kinase, 'Ser-365' of BRAF kinase and 'Ser-214' of ARAF kinase, stimulating their kinase activities. The SMP complex enhances the dephosphorylation activity and substrate specificity of PP1c. Acts as an inhibitor of keratinocyte …

**Summary**, from NCBI Gene [8036](https://www.ncbi.nlm.nih.gov/gene/8036):

> This gene encodes a protein that consists almost entirely of leucine-rich repeats, a domain implicated in protein-protein interactions. The protein may function as a scaffold linking RAS to downstream signal transducers in the RAS/ERK MAP kinase signaling cascade. Mutations in this gene have been associated with Noonan-like syndrome with loose anagen hair. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:15454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15454) · Entrez [8036](https://www.ncbi.nlm.nih.gov/gene/8036) · UniProt [Q9UQ13](https://www.uniprot.org/uniprotkb/Q9UQ13) · Ensembl [ENSG00000108061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108061)

## Data

Gene col 2914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2914); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2914]; `tensor/DDL_lfc|DDL_z.npy` [2914]; `embed/gene_vectors.npy` [2914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2914 or target_col == 2914). Every well: [[SHOC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHOC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
