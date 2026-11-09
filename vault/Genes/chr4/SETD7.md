---
symbol: "SETD7"
type: "gene"
col: 6988
ensembl_id: "ENSG00000145391"
name: "SET domain containing 7, histone lysine methyltransferase"
location: "4q31.1"
module: 29
arm: "+"
pooled_cpm: 51.13
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 22
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SETD7

*SET domain containing 7, histone lysine methyltransferase* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +15.1, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.267× (z -26.1, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATL3]] (+0.66, fdr 1e-05), [[ZMPSTE24]] (+0.66, fdr 2e-05), [[KCTD15]] (+0.65, fdr 2e-05); moves opposite to [[TMEM191A-1]] (-0.64, fdr 3e-05), [[SIGIRR]] (-0.62, fdr 6e-05), [[ARL4C]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 22 go from it, the strongest it → cells under [[Ponatinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6988.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +15.1 | 0e+00 | 41/45 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +12.5 | 2e-33 | 31/37 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +11.4 | 1e-27 | 36/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +6.6 | 7e-09 | 26/40 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.3 | 1e-05 | 27/45 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.0 | 6e-05 | 22/45 (HOP62, A-427, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.5 | 6e-04 | 19/45 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.4 | 7e-04 | 23/45 (C-33 A, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.4 | 7e-04 | 14/45 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.3 | 7e-04 | 20/45 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 7e-04 | 22/45 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.26×** | +4.3 | 8e-04 | 21/45 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +4.2 | 0.001 | 21/46 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 17/45 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +4.0 | 0.003 | 19/44 (C32, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.004 | 19/45 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.004 | 12/45 (NCI-H460, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.8 | 0.004 | 17/45 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 21/45 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.005 | 15/45 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.006 | 13/44 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.028 | 8/45 (BT-474, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.267×** | -26.1 | 0e+00 | 43/45 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.277×** | -25.4 | 0e+00 | 45/45 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.374×** | -19.5 | 0e+00 | 42/45 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.724×** | -9.0 | 2e-17 | 31/45 (LOX-IMVI, NCI-H2030, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.635×** | -9.0 | 3e-17 | 31/45 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.656×** | -8.0 | 1e-13 | 27/45 (NCI-H460, SW 900, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.763×** | -5.4 | 7e-06 | 24/45 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.803×** | -4.3 | 1e-03 | 24/45 (SW48, LS 180, …) | top dose only |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.863× | -4.2 | 0.002 | 13/46 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.815×** | -4.0 | 0.003 | 20/45 (KATO III, LS 180, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.684×** | -3.9 | 0.004 | 23/46 (LoVo, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.850× | -3.2 | 0.057 | 8/45 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Naproxen (drug)]] 5 µM |  | 0.852× | -3.0 | 0.095 | 10/45 (C32, NCI-H1573, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.095 | 7/45 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.098 | 11/45 (J82, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.4 | 6 (1 ⚠) | 4 (1 ⚠) | [[Trametinib (drug)]] 5 µM 2.48× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Trametinib (drug)]] 0.05 µM 1.94× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.201× (z -18.4) |
| [[SW480 (line)]] | alt | 29.0 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.292× (z -13.8) |
| [[A498 (line)]] | wt | 108 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -20.5) |
| [[A549 (line)]] | wt | 50.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.192× (z -16.0) |
| [[HOP62 (line)]] | alt | 37.1 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.6) |
| [[HS-578T (line)]] | alt | 57.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -14.6) |
| [[A-172 (line)]] | wt | 58.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.267× (z -13.2) |
| [[H4 (line)]] | wt | 77.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -14.7) |
| [[Hs 766T (line)]] | wt | 57.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -14.0) |
| [[HT-29 (line)]] | alt | 71.0 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.202× (z -18.1) |
| [[J82 (line)]] | alt | 53.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -16.6) |
| [[KATO III (line)]] | alt | 68.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.153× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 52.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -19.7) |
| [[LS 180 (line)]] | wt | 88.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 60.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -11.7) |
| [[RKO (line)]] | wt | 89.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -14.7) |
| [[SW48 (line)]] | wt | 64.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.126× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 58.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.395× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 59.4 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.251× (z -11.6) |
| [[LoVo (line)]] | wt | 54.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 43.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.338× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 31.3 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.274× (z -10.3) |
| [[SNU-423 (line)]] | alt | 41.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.141× (z -16.6) |
| [[SW 900 (line)]] | alt | 68.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.244× (z -13.9) |
| [[C32 (line)]] | wt | 31.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.310× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 51.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -11.3) |
| [[HCT15 (line)]] | alt | 65.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 54.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -9.4) |
| [[PANC-1 (line)]] | alt | 39.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 43.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -8.7) |
| [[SNU-1 (line)]] | wt | 88.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -14.9) |
| [[SW1417 (line)]] | alt | 29.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -9.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-427 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.9) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[BT-474 (line)]] | alt | 56.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.162× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -8.6) |
| [[AN3 CA (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATL3]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | +0.66 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[KCTD15]] | +0.65 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[RCN1]] | +0.64 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[NAA50]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[AP5M1]] | +0.62 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[STRADB]] | +0.62 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | +0.62 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[CMPK1]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[NAXD]] | +0.60 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ARSB]] | +0.60 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[IDE]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM191A-1]] | -0.64 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SIGIRR]] | -0.62 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ARL4C]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.61 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TNFAIP8L1]] | -0.59 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.58 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[FAM89B]] | -0.58 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[SPATA2L]] | -0.58 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[CCDC85B]] | -0.57 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[BAIAP3]] | -0.57 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[INIP]] | -0.56 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[MAP1S]] | -0.56 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SETD7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ponatinib (drug)]] 5 µM | C | SETD7 activity raises the cells' numbers under Ponatinib 5 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.46× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Tirabrutinib (drug)]] 0.5 µM | C | SETD7 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.37× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | C | SETD7 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.64× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Filgotinib (drug)]] 0.05 µM | C | SETD7 activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.42× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| [[ARSB]] | C | SETD7 activity lowers ARSB's level | lines that do not express SETD7 (3) vs lines expressing it (47) | 2.86× higher at baseline in the lines without SETD7 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | C | SETD7 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.33× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Bortezomib (drug)]] 0.5 µM | C | SETD7 activity raises the cells' numbers under Bortezomib 0.5 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.73× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | C | SETD7 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.88× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | SETD7 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.75× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Entrectinib (drug)]] 5 µM | C | SETD7 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.34× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Bortezomib (drug)]] 0.05 µM | C | SETD7 activity raises the cells' numbers under Bortezomib 0.05 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.61× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| cells under [[Vortioxetine (drug)]] 0.5 µM | C | SETD7 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.36× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-11.2, 14.8); signed map (-13.1, -37.7). **Vector** length 127, 35.7% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.4 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.1 | +3.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.1 | -26.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.0 | -25.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.7 | -19.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -2.3 | -9.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Naproxen (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 7, histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,495,941-139,606,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1717, SET7, SET7/9, Set9, KMT7 |
| Gene groups (HGNC) | SET domain containing; Non-histone lysine methyltransferases; MORN repeat containing |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTS6](https://www.uniprot.org/uniprotkb/Q8WTS6) (Histone-lysine N-methyltransferase SETD7):

> Histone methyltransferase that specifically monomethylates 'Lys-4' of histone H3. H3 'Lys-4' methylation represents a specific tag for epigenetic transcriptional activation. Plays a central role in the transcriptional activation of genes such as collagenase or insulin. Recruited by IPF1/PDX-1 to the insulin promoter, leading to activate transcription. Also has methyltransferase activity toward non-histone proteins such as CGAS, GLI3, p53/TP53, TAF10, and possibly TAF7 by recognizing and binding …

**Summary**, from NCBI Gene [80854](https://www.ncbi.nlm.nih.gov/gene/80854):

> Enables histone H3 methyltransferase activity; p53 binding activity; and protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine dimethylation and peptidyl-lysine monomethylation. Acts upstream of or within DNA damage response and heterochromatin organization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30412) · Entrez [80854](https://www.ncbi.nlm.nih.gov/gene/80854) · UniProt [Q8WTS6](https://www.uniprot.org/uniprotkb/Q8WTS6) · Ensembl [ENSG00000145391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145391)

## Data

Gene col 6988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6988); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6988]; `tensor/DDL_lfc|DDL_z.npy` [6988]; `embed/gene_vectors.npy` [6988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6988 or target_col == 6988). Every well: [[SETD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
