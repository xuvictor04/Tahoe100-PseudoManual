---
symbol: "SYNJ1"
type: "gene"
col: 8214
ensembl_id: "ENSG00000159082"
name: "synaptojanin 1"
location: "21q22.11"
module: 1
arm: "-"
pooled_cpm: 43.8
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SYNJ1

*synaptojanin 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.84× (z +20.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.434× (z -11.6, q 2e-28, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.268×, A498 0.271×, SHP-77 0.244×, PANC-1 0.320×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2347 0.232×, LOX-IMVI 0.236×, AsPC-1 0.207×, HepG2/C3A 0.122×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (H4 0.118×, HS-578T 0.281×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 0.5 µM in 1 line (NCI-H1792 0.337×); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0581×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUMB]] (+0.60, fdr 3e-05), [[HNRNPLL]] (+0.54, fdr 3e-05), [[COX8A]] (+0.53, fdr 1e-04); moves opposite to [[ACBD6]] (-0.58, fdr 2e-05), [[RRP15]] (-0.57, fdr 1e-04), [[MCM3AP-AS1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[INTS6L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.84×** | +20.3 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +17.6 | 0e+00 | 48/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.94×** | +14.8 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.49×** | +12.5 | 9e-34 | 46/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.45×** | +12.3 | 9e-33 | 47/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.38×** | +11.9 | 1e-30 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +11.4 | 3e-28 | 46/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +9.4 | 6e-19 | 42/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +8.9 | 3e-17 | 42/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +8.2 | 1e-14 | 45/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +8.1 | 2e-14 | 35/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +8.1 | 3e-14 | 34/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +6.9 | 2e-10 | 39/48 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +6.8 | 4e-10 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +6.7 | 8e-10 | 39/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +5.4 | 2e-06 | 39/48 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 6e-06 | 28/48 (SW48, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.4 | 3e-04 | 28/48 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.003 | 23/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 0.268×, A498 0.271×, SHP-77 0.244×, PANC-1 0.320×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2347 0.232×, LOX-IMVI 0.236×, AsPC-1 0.207×, HepG2/C3A 0.122×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (H4 0.118×, HS-578T 0.281×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 0.5 µM in 1 line (NCI-H1792 0.337×); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0581×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.434×** | -11.6 | 2e-28 | 37/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -10.9 | 4e-25 | 30/38 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -7.1 | 2e-10 | 32/42 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.765× | -3.3 | 0.14 | 18/47 (C32, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.25 | 19/48 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.1 | 12 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +17.4) | — |
| [[SW480 (line)]] | alt | 61.0 | 9 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -13.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.5 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +19.9) | — |
| [[PANC-1 (line)]] | alt | 34.7 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.8) | — |
| [[LoVo (line)]] | wt | 25.1 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.62× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.5) | — |
| [[A-172 (line)]] | wt | 50.7 | 5 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 46.2 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -11.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 36.5 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 45.2 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 40.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 54.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 33.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 69.5 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 36.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +17.1) | — |
| [[SW48 (line)]] | wt | 25.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +11.2) | — |
| [[A498 (line)]] | wt | 64.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -12.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 35.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 27.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 37.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 38.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 56.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 91.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 54.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 35.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +10.9) | — |
| [[H4 (line)]] | wt | 45.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 46.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 66.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 41.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 37.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 30.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[A-427 (line)]] | wt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 33.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.4) | — |
| [[KATO III (line)]] | alt | 29.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 48.4 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.337× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0603× (z -10.3) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 54.6 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM 0.0581× (z -8.8) |
| [[A549 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUMB]] | +0.60 | +0.54 / +0.43 | both halves | 3e-05 | STRING 582 |
| [[HNRNPLL]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[COX8A]] | +0.53 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[TAF5]] | +0.52 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[DONSON]] | +0.52 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[WDR91]] | +0.51 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[OST4]] | +0.51 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[WDR20]] | +0.50 | +0.38 / +0.35 | both halves | 1e-04 |  |
| [[DYRK4]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[INTS6L]] | +0.49 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[SSR4]] | +0.49 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[STX5]] | +0.48 | +0.43 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD6]] | -0.58 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[RRP15]] | -0.57 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[MCM3AP-AS1]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CCT2]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ZP3]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[FKTN]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[AIMP2]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[DCAF4]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF485]] | -0.52 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[EMSLR]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RABGGTB]] | -0.50 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MRRF]] | -0.50 | -0.37 / -0.50 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INTS6L]] | B | INTS6L activity raises SYNJ1's level | lines that do not express INTS6L (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without INTS6L | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02454, FRMD6, CHST11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.2, -49.5); signed map (-52.3, -31.5). **Vector** length 75.0, 21.1% of its response variance represented; |z| ≥ 3 in 1,323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +17.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +1.7 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.1 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.0 | +2.7 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.0 | +0.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.0 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -1.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | synaptojanin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,628,759-32,728,040 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INPP5G, PARK20 |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 10 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Synthesis of IP3 and IP4 in the cytosol; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O43426](https://www.uniprot.org/uniprotkb/O43426) (Polyphosphatidylinositol phosphatase SYNJ1):

> Phosphatase that hydrolyzes phosphate groups from the inositol ring of phosphoinositides and inositol phosphates, in a domain-specific manner. The 5-PPase domain catalyzes removal of the 5-phosphate from substrates such as phosphatidylinositol-4,5-bisphosphate (PtdIns(4,5)P2), phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3), inositol-1,4,5-trisphosphate (Ins(1,4,5)P3) and inositol-1,3,4,5-tetrakisphosphate (Ins(1,3,4,5)P4). The SAC domain hydrolyzes phosphates at the 3- and …

**Summary**, from NCBI Gene [8867](https://www.ncbi.nlm.nih.gov/gene/8867):

> This gene encodes a phosphoinositide phosphatase that regulates levels of membrane phosphatidylinositol-4,5-bisphosphate. As such, expression of this enzyme may affect synaptic transmission and membrane trafficking. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:11503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11503) · Entrez [8867](https://www.ncbi.nlm.nih.gov/gene/8867) · UniProt [O43426](https://www.uniprot.org/uniprotkb/O43426) · Ensembl [ENSG00000159082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159082)

## Data

Gene col 8214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8214); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8214]; `tensor/DDL_lfc|DDL_z.npy` [8214]; `embed/gene_vectors.npy` [8214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8214 or target_col == 8214). Every well: [[SYNJ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNJ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
