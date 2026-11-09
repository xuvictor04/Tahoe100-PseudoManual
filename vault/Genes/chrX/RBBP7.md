---
symbol: "RBBP7"
type: "gene"
col: 2209
ensembl_id: "ENSG00000102054"
name: "RB binding protein 7, chromatin remodeling factor"
location: "Xp22.2"
module: 6
arm: "+"
pooled_cpm: 91.61
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RBBP7

*RB binding protein 7, chromatin remodeling factor* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.44× (z +23.3, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.18× (z +4.6, q 2e-04, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW480 3.56×, Panc 03.27 4.99×, NCI-H1792 5.80×, NCI-H1573 6.78×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1792 5.48×, PANC-1 3.60×, A549 4.30×, SW480 3.02×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.781× (z -4.8, q 7e-04, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HEC-1-A 0.585×, SW480 0.615×, NCI-H23 0.514×, A-427 0.593×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A-427 0.331×, RKO 0.362×, HEC-1-A 0.531×, SNU-1 0.303×); [[vincristine (drug)]] 5 µM in 1 line (H4 0.0737×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPS2]] (+0.78, fdr 7e-06), [[MCM3]] (+0.77, fdr 7e-06), [[HELLS]] (+0.77, fdr 7e-06); moves opposite to [[CCDC174]] (-0.73, fdr 7e-06), [[ADPRM]] (-0.72, fdr 7e-06), [[SMIM26]] (-0.72, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[WASHC1]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PGRMC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 19 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2209.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW480 3.56×, Panc 03.27 4.99×, NCI-H1792 5.80×, NCI-H1573 6.78×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1792 5.48×, PANC-1 3.60×, A549 4.30×, SW480 3.02×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.44×** | +23.3 | 0e+00 | 43/43 (SW480, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.12×** | +22.3 | 0e+00 | 47/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.26×** | +14.8 | 0e+00 | 43/45 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.64×** | +9.8 | 2e-20 | 37/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.62×** | +9.2 | 6e-18 | 40/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.56×** | +8.7 | 3e-16 | 38/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +7.2 | 7e-11 | 31/50 (SNU-423, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.28×** | +6.9 | 4e-10 | 28/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.9 | 2e-07 | 32/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.36×** | +5.8 | 4e-07 | 28/48 (A-172, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.34×** | +5.7 | 5e-07 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.33×** | +5.7 | 7e-07 | 26/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.6 | 2e-04 | 21/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.4 | 3e-04 | 27/48 (PANC-1, KATO III, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 24/48 (C32, CFPAC-1, …) | two highest doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.079 | 11/47 (HEC-1-A, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2209.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HEC-1-A 0.585×, SW480 0.615×, NCI-H23 0.514×, A-427 0.593×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A-427 0.331×, RKO 0.362×, HEC-1-A 0.531×, SNU-1 0.303×); [[vincristine (drug)]] 5 µM in 1 line (H4 0.0737×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -4.8 | 7e-04 | 25/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -4.3 | 0.006 | 22/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.811×** | -4.1 | 0.008 | 21/48 (A-172, Hs 766T, …) | two highest doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.867× | -3.9 | 0.011 | 14/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.878× | -3.6 | 0.036 | 9/49 (RPMI-7951, HOP62, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.880× | -3.5 | 0.039 | 13/48 (RKO, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.890× | -3.2 | 0.088 | 15/48 (A-172, A498, …) | two highest doses | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.088 | 18/47 (NCI-H661, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 0.895× | -3.1 | 0.13 | 1/48 (SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 153 | 6 (6 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.56× (z +18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 69.3 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 192 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 104 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 126 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -13.6) |
| [[A549 (line)]] | wt | 75.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 120 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[KATO III (line)]] | alt | 134 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 139 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 40.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.78× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 81.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 56.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 41.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 61.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[H4 (line)]] | wt | 65.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[vincristine (drug)]] 5 µM 0.0737× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 177 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.531× (z -8.9) |
| [[Hs 766T (line)]] | wt | 87.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 80.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 61.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 77.5 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Panc 03.27 (line)]] | alt | 90.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 39.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.0) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HCT15 (line)]] | alt | 88.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 62.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 37.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.87× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.70× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 78.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 68.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 67.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 63.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 64.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 86.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.624× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 45.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 92.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SNU-1 (line)]] | wt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.5) |
| [[C-33 A (line)]] | alt | 181 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[MCM3]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 520 |
| [[HELLS]] | +0.77 | +0.68 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 499 |
| [[TIMELESS]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDK2]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[PCLAF]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RANBP1]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM4]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 457 |
| [[MYBL2]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 431 |
| [[NCAPG2]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[CENPH]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 629 |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | -0.73 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[ADPRM]] | -0.72 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.72 | -0.76 / -0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[WASHC1]] | -0.71 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[NKAP]] | -0.70 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[SNHG8]] | -0.69 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.69 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[SNHG32]] | -0.69 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NFKBIL1]] | -0.67 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[ALG2]] | -0.67 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[ATF4]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[SAT2]] | -0.66 | -0.60 / -0.73 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises RBBP7's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without PODXL2 | 0.037 | ⚠ within organs, on part of the lines |
| [[SCARA3]] | B | SCARA3 activity raises RBBP7's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without SCARA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[TOP2A]] | B | TOP2A activity lowers RBBP7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MYBL2]] | C | MYBL2 activity raises RBBP7's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGRMC1]] | C | RBBP7's natural level strengthens PGRMC1's drug response | RBBP7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse -0.25; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.5, -41.0); signed map (-30.7, -42.8). **Vector** length 122, 38.8% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.55 to 28); *DNA Replication* (reactome, mean cos +0.54 to 40); *E2F G1/S* (control, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.3 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.0 | +22.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +4.0 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.8 | +23.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +1.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.6 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.5 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RB binding protein 7, chromatin remodeling factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:16,839,283-16,870,362 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RbAp46 |
| Gene groups (HGNC) | WD repeat domain containing; EMSY complex; NuRD complex subunits; SIN3 histone deacetylase complex subunits; Polycomb repressive complex 2; NURF complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 65 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; Defective pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16576](https://www.uniprot.org/uniprotkb/Q16576) (Histone-binding protein RBBP7):

> Core histone-binding subunit that may target chromatin remodeling factors, histone acetyltransferases and histone deacetylases to their histone substrates in a manner that is regulated by nucleosomal DNA. Component of several complexes which regulate chromatin metabolism. These include the type B histone acetyltransferase (HAT) complex, which is required for chromatin assembly following DNA replication; the core histone deacetylase (HDAC) complex, which promotes histone deacetylation and …

**Summary**, from NCBI Gene [5931](https://www.ncbi.nlm.nih.gov/gene/5931):

> This protein is a ubiquitously expressed nuclear protein and belongs to a highly conserved subfamily of WD-repeat proteins. It is found among several proteins that binds directly to retinoblastoma protein, which regulates cell proliferation. The encoded protein is found in many histone deacetylase complexes, including mSin3 co-repressor complex. It is also present in protein complexes involved in chromatin assembly. This protein can interact with BRCA1 tumor-suppressor gene and may have a role …

**Accessions** — [HGNC:9890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9890) · Entrez [5931](https://www.ncbi.nlm.nih.gov/gene/5931) · UniProt [Q16576](https://www.uniprot.org/uniprotkb/Q16576) · Ensembl [ENSG00000102054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102054)

## Data

Gene col 2209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2209); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2209]; `tensor/DDL_lfc|DDL_z.npy` [2209]; `embed/gene_vectors.npy` [2209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2209 or target_col == 2209). Every well: [[RBBP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBBP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
