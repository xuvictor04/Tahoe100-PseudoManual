---
symbol: "ILF2"
type: "gene"
col: 6780
ensembl_id: "ENSG00000143621"
name: "interleukin enhancer binding factor 2"
location: "1q21.3"
module: 20
arm: "+"
pooled_cpm: 60.06
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ILF2

*interleukin enhancer binding factor 2* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (24 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.46× (z +18.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.754× (z -4.1, q 0.024, down in 28 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (RPMI-7951 0.371×, A-427 0.536×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.0518×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.513×; ⚠ cell-cycle shift, explains ~81% of this change); [[Thymol (drug)]] 0.05 µM in 1 line (SNU-423 0.255×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BPNT2]] (+0.67, fdr 1e-05), [[TXNDC5]] (+0.65, fdr 1e-05), [[CCAR2]] (+0.65, fdr 1e-05); moves opposite to [[CROCCP2-1]] (-0.69, fdr 7e-06), [[MRPS18C]] (-0.60, fdr 9e-05), [[SMIM26]] (-0.60, fdr 3e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SAT2]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 24 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +18.3 | 0e+00 | 46/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.99×** | +14.6 | 0e+00 | 48/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.61×** | +13.8 | 7e-41 | 45/47 (KATO III, SW480, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.34×** | +12.6 | 3e-34 | 41/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.23×** | +11.5 | 2e-28 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.21×** | +11.4 | 4e-28 | 45/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.11×** | +10.8 | 5e-25 | 43/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.24×** | +10.7 | 6e-25 | 42/45 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.05×** | +10.3 | 3e-23 | 42/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **2.06×** | +10.0 | 1e-21 | 37/42 (PANC-1, HEC-1-A, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +9.7 | 1e-20 | 40/48 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.92×** | +9.4 | 4e-19 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.57×** | +9.1 | 3e-18 | 34/48 (A549, NCI-H1792, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.82×** | +8.3 | 6e-15 | 41/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.63×** | +7.0 | 9e-11 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.1 | 9e-06 | 27/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.3 | 5e-04 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.002 | 23/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.005 | 24/48 (SW480, HCT15, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.020 | 21/48 (NCI-H460, A549, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.022 | 17/48 (SNU-423, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.037 | 15/47 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.042 | 14/49 (HEC-1-A, SW48, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +2.8 | 0.091 | 17/48 (SW1417, SNU-423, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.44×** | +2.7 | 0.099 | 14/48 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6780.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (RPMI-7951 0.371×, A-427 0.536×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CHP-212 0.0518×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.513×; ⚠ cell-cycle shift, explains ~81% of this change); [[Thymol (drug)]] 0.05 µM in 1 line (SNU-423 0.255×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.754×** | -4.1 | 0.024 | 28/48 (A-427, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.782× | -3.4 | 0.16 | 21/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.857× | -3.2 | 0.21 | 18/48 (A-172, J82, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | 0.858× | -3.2 | 0.21 | 18/48 (LS 180, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.807× | -3.1 | 0.21 | 14/47 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 0.814× | -3.0 | 0.21 | 18/48 (H4, LS 180, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.1 | 13 (11 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.13× (z +15.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +13.3) | — |
| [[SW480 (line)]] | alt | 52.1 | 13 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.67× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 51.0 | 11 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 46.1 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 41.5 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 125 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.56× (z +9.0) | — |
| [[A549 (line)]] | wt | 43.2 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +15.0) | — |
| [[LoVo (line)]] | wt | 45.0 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.04× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 39.8 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 85.3 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.1) | — |
| [[KATO III (line)]] | alt | 37.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 50.0 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 39.9 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +11.5) | — |
| [[A-427 (line)]] | wt | 79.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[AsPC-1 (line)]] | alt | 42.1 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +17.2) | — |
| [[BT-474 (line)]] | alt | 72.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 35.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 43.2 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +10.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.47× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.34× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 11.0× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 23.4 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +15.3) | [[Thymol (drug)]] 0.05 µM 0.255× (z -8.5) |
| [[A-172 (line)]] | wt | 54.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 35.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.6) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 17.4× (z +8.6) | — |
| [[RKO (line)]] | wt | 73.4 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 9.02× (z +10.6) | — |
| [[A498 (line)]] | wt | 126 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.9) | — |
| [[C32 (line)]] | wt | 35.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.6) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 172 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 126 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.59× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 55.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.2) | — |
| [[SW48 (line)]] | wt | 69.2 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 11.6× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 36.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +16.7) | — |
| [[CHP-212 (line)]] | wt | 84.4 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0518× (z -14.3) ⚠ cell-cycle shift, explains ~86% of this change |
| [[HepG2_C3A (line)]] | wt | 41.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 46.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 43.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.5) | — |
| [[J82 (line)]] | alt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 92.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.371× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT2]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CCAR2]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 | STRING 414 |
| [[STT3A]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ARF3]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ACTL6A]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[HNRNPUL1]] | +0.62 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[GANAB]] | +0.62 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[PCNX3]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[UGGT1]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RPN1]] | +0.61 | +0.46 / +0.63 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.69 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.60 | -0.36 / -0.65 | both halves | 9e-05 |  |
| [[SMIM26]] ⚠ | -0.60 | -0.43 / -0.65 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAT2]] | -0.59 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[EIF1B]] | -0.59 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[YBEY]] | -0.58 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[TMEM126A]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SLC26A11]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ATF4]] | -0.57 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[FLCN]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.57 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[TBRG1]] | -0.57 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[SIRT6]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ILF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.5, -23.4); signed map (-24.5, -41.0). **Vector** length 72.3, 22.5% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +18.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +4.9 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.4 | -1.1 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.4 | -0.4 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.8 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | +4.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | interleukin enhancer binding factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,661,788-153,671,028 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NF45 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12905](https://www.uniprot.org/uniprotkb/Q12905) (Interleukin enhancer-binding factor 2):

> Chromatin-interacting protein that forms a stable heterodimer with interleukin enhancer-binding factor 3/ILF3 and plays a role in several biological processes including transcription, innate immunity or cell growth. Essential for the efficient reshuttling of ILF3 (isoform 1 and isoform 2) into the nucleus. Together with ILF3, forms an RNA-binding complex that is required for mitotic progression and cytokinesis by regulating the expression of a cluster of mitotic genes. Mechanistically, competes …

**Summary**, from NCBI Gene [3608](https://www.ncbi.nlm.nih.gov/gene/3608):

> The protein encoded by this gene is a transcription factor required for T-cell expression of the interleukin 2 gene. It also binds RNA and is an essential component for encapsidation and protein priming of hepatitis B viral polymerase. The encoded 45 kDa protein (NF45, ILF2) forms a complex with the 90 kDa interleukin enhancer-binding factor 3 (NF90, ILF3), and this complex has been shown to affect the redistribution of nuclear mRNA to the cytoplasm, to repair DNA breaks by nonhomologous end …

**Accessions** — [HGNC:6037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6037) · Entrez [3608](https://www.ncbi.nlm.nih.gov/gene/3608) · UniProt [Q12905](https://www.uniprot.org/uniprotkb/Q12905) · Ensembl [ENSG00000143621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143621)

## Data

Gene col 6780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6780); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6780]; `tensor/DDL_lfc|DDL_z.npy` [6780]; `embed/gene_vectors.npy` [6780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6780 or target_col == 6780). Every well: [[ILF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
