---
symbol: "YTHDF2"
type: "gene"
col: 12601
ensembl_id: "ENSG00000198492"
name: "YTH N6-methyladenosine RNA binding protein F2"
location: "1p35.3"
module: 7
arm: "+"
pooled_cpm: 84.73
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# YTHDF2

*YTH N6-methyladenosine RNA binding protein F2* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.58× (z +18.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.666× (z -7.9, q 1e-12, down in 38 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.830× (z -3.7, q 0.049, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HepG2/C3A 0.149×, PANC-1 0.319×, SNU-1 0.195×, NCI-H2347 0.345×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.112×, C-33 A 0.244×, NCI-H23 0.253×, RKO 0.298×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0970×, C-33 A 0.325×, NCI-H2030 0.452×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0886×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX28]] (+0.77, fdr 7e-06), [[ZNF629]] (+0.76, fdr 7e-06), [[HPS6]] (+0.74, fdr 7e-06); moves opposite to [[SEPTIN2]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF625]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.58×** | +18.5 | 0e+00 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.32×** | +17.1 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.82×** | +16.5 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +13.7 | 3e-40 | 46/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +13.2 | 1e-37 | 45/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +12.6 | 2e-34 | 47/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +12.3 | 1e-32 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +10.2 | 1e-22 | 43/48 (SW480, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.70×** | +10.1 | 2e-22 | 41/48 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.6 | 3e-20 | 40/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +8.2 | 1e-14 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.6 | 1e-12 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +7.6 | 1e-12 | 39/48 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +7.0 | 1e-10 | 38/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 4e-09 | 39/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.9 | 1e-07 | 32/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.3 | 4e-06 | 25/49 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.001 | 24/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.001 | 27/47 (MIA PaCa-2, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12601.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HepG2/C3A 0.149×, PANC-1 0.319×, SNU-1 0.195×, NCI-H2347 0.345×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.112×, C-33 A 0.244×, NCI-H23 0.253×, RKO 0.298×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.0970×, C-33 A 0.325×, NCI-H2030 0.452×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0886×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -7.9 | 1e-12 | 38/49 (SNU-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -6.0 | 5e-07 | 28/44 (HepG2/C3A, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.049 | 23/48 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.1 | 0.30 | 21/48 (SW480, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.1 | 12 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 73.0 | 11 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 111 | 11 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.88× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.25× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 125 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -13.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 59.0 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +14.5) | — |
| [[LoVo (line)]] | wt | 96.5 | 8 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.18× (z +13.1) | — |
| [[KATO III (line)]] | alt | 81.3 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.50× (z +12.1) | — |
| [[A549 (line)]] | wt | 51.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 122 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.39× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 85.2 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.4× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 94.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 70.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 60.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 98.6 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 115 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -16.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 207 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.67× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -17.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 81.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 58.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 55.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 78.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.96× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.492× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 99.0 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0970× (z -27.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 57.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +11.2) | — |
| [[C32 (line)]] | wt | 93.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 69.0 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.45× (z +11.3) | — |
| [[J82 (line)]] | alt | 88.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 86.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.85× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -14.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 129 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.92× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 90.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.18× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -21.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 58.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 98.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 65.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 75.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.149× (z -17.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 65.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.28× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 69.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.64× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 74.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.15× (z +9.0) | — |
| [[SW48 (line)]] | wt | 122 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.98× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +8.8) | — |
| [[H4 (line)]] | wt | 65.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 51.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 61.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0886× (z -9.0) |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX28]] | +0.77 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[HPS6]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.72 | +0.73 / +0.77 | both halves | 7e-06 | STRING 512 |
| [[RPP38]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[FEM1A]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[JAGN1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.71 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[KTI12]] | +0.71 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[SMG8]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[EID2]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN2]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF625]] | B | ZNF625 activity raises YTHDF2's level | lines that do not express ZNF625 (19) vs lines expressing it (31) | 1.02× lower at baseline in the lines without ZNF625 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF415, ZNF829, ZNF347 |
| [[MLF1]] | B | MLF1 activity lowers YTHDF2's level | lines that do not express MLF1 (5) vs lines expressing it (45) | 1.34× higher at baseline in the lines without MLF1 | 0.077 | ⚠ within organs, on part of the lines; also absent: CCDC110, MLH1, ITGA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.7, 8.8); signed map (-3.2, -25.9). **Vector** length 107, 35.3% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.4 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +18.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +17.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.8 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -0.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.5 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.3 | -0.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | YTH N6-methyladenosine RNA binding protein F2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,736,621-28,769,775 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HGRG8, NY-REN-2, CAHL |
| Gene groups (HGNC) | YTH domain containing N6-methyladenosine readers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5A9](https://www.uniprot.org/uniprotkb/Q9Y5A9) (YTH domain-containing family protein 2):

> Specifically recognizes and binds N6-methyladenosine (m6A)-containing RNAs, and regulates their stability. M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing. Acts as a regulator of mRNA stability by promoting degradation of m6A-containing mRNAs via interaction with the CCR4-NOT and ribonuclease P/MRP complexes, depending on the context. The YTHDF paralogs (YTHDF1, YTHDF2 and YTHDF3) share m6A-containing mRNAs …

**Summary**, from NCBI Gene [51441](https://www.ncbi.nlm.nih.gov/gene/51441):

> This gene encodes a member of the YTH (YT521-B homology) superfamily containing YTH domain. The YTH domain is typical for the eukaryotes and is particularly abundant in plants. The YTH domain is usually located in the middle of the protein sequence and may function in binding to RNA. In addition to a YTH domain, this protein has a proline rich region which may be involved in signal transduction. An Alu-rich domain has been identified in one of the introns of this gene, which is thought to be …

**Accessions** — [HGNC:31675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31675) · Entrez [51441](https://www.ncbi.nlm.nih.gov/gene/51441) · UniProt [Q9Y5A9](https://www.uniprot.org/uniprotkb/Q9Y5A9) · Ensembl [ENSG00000198492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198492)

## Data

Gene col 12601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12601); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12601]; `tensor/DDL_lfc|DDL_z.npy` [12601]; `embed/gene_vectors.npy` [12601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12601 or target_col == 12601). Every well: [[YTHDF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YTHDF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
