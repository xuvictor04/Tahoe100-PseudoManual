---
symbol: "BSG"
type: "gene"
col: 10233
ensembl_id: "ENSG00000172270"
name: "basigin (Ok blood group)"
location: "19p13.3"
module: 50
arm: "+"
pooled_cpm: 129.67
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# BSG

*basigin (Ok blood group)* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +16.6, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +12.7, q 1e-34, up in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2347 2.32×, Panc 03.27 2.67×, AsPC-1 2.52×, LOX-IMVI 3.05×, …); [[Dinaciclib (drug)]] 0.5 µM in 8 lines (LoVo 7.40×, SW480 4.64×, HEC-1-A 4.12×, COLO 205 9.16×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 6.01×, SW480 4.78×, KATO III 4.75×, SNU-1 5.62×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.554× (z -8.2, q 1e-13, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1B]] (+0.73, fdr 7e-06), [[NAGA]] (+0.72, fdr 7e-06), [[ITM2C]] (+0.71, fdr 7e-06); moves opposite to [[DNAJC2]] (-0.72, fdr 7e-06), [[NSRP1]] (-0.66, fdr 7e-06), [[NOL8]] (-0.63, fdr 8e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[APLP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10233.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2347 2.32×, Panc 03.27 2.67×, AsPC-1 2.52×, LOX-IMVI 3.05×, …); [[Dinaciclib (drug)]] 0.5 µM in 8 lines (LoVo 7.40×, SW480 4.64×, HEC-1-A 4.12×, COLO 205 9.16×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 6.01×, SW480 4.78×, KATO III 4.75×, SNU-1 5.62×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.16×** | +16.6 | 0e+00 | 47/49 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.87×** | +14.6 | 0e+00 | 44/44 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +12.7 | 1e-34 | 45/49 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.29×** | +10.5 | 1e-23 | 45/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.95×** | +9.6 | 8e-20 | 47/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.71×** | +7.7 | 9e-13 | 47/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.60×** | +6.8 | 1e-09 | 39/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.52×** | +6.1 | 9e-08 | 44/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.51×** | +5.7 | 7e-07 | 39/50 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.2 | 1e-05 | 37/47 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.35×** | +4.1 | 0.002 | 30/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.33×** | +4.1 | 0.002 | 29/48 (LoVo, SW480, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.32×** | +4.0 | 0.002 | 30/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 23/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.9 | 0.003 | 26/38 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.6 | 0.010 | 18/48 (HT-29, HOP62, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.16× | +3.0 | 0.083 | 12/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.554×** | -8.2 | 1e-13 | 44/49 (C32, HS-578T, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.726×** | -6.6 | 2e-08 | 32/48 (SHP-77, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.739×** | -4.4 | 0.002 | 32/48 (SHP-77, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.639× | -3.4 | 0.10 | 33/49 (BT-474, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.801× | -3.0 | 0.28 | 26/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 100 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.8) | — |
| [[SW480 (line)]] | alt | 104 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 211 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.5) | [[Verteporfin (drug)]] 5 µM 0.346× (z -10.4) |
| [[KATO III (line)]] | alt | 108 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.75× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 125 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +15.1) | — |
| [[SW 900 (line)]] | alt | 162 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 129 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.5) | — |
| [[A498 (line)]] | wt | 128 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.6) | [[Verteporfin (drug)]] 5 µM 0.418× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 107 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +14.4) | — |
| [[CFPAC-1 (line)]] | alt | 74.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 51.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.16× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[H4 (line)]] | wt | 166 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.1) |
| [[HOP62 (line)]] | alt | 133 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 91.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 95.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.40× (z +20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 139 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 191 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 142 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[C32 (line)]] | wt | 183 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Verteporfin (drug)]] 5 µM 0.341× (z -11.0) |
| [[Hs 766T (line)]] | wt | 167 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 117 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 53.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 93.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 120 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.4) | — |
| [[RKO (line)]] | wt | 102 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.6) |
| [[SHP-77 (line)]] | alt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.0) |
| [[A-172 (line)]] | wt | 287 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 158 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[J82 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 200 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 151 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 168 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.62× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-427 (line)]] | wt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.6) |
| [[A549 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[BT-474 (line)]] | alt | 79.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 139 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.2) | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -8.7) |
| [[CHP-212 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | +0.73 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NAGA]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ITM2C]] | +0.71 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[LRPAP1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GANAB]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[AGPAT1]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[RTL8C]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[CALM3]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TMED4]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[FAM234A]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ADAM15]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.72 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.66 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[NOL8]] | -0.63 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[PPIG]] | -0.63 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[CRCP]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[RBM25]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[TATDN1]] | -0.61 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[C15orf40]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SLTM]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[EIF5B]] | -0.57 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[WASHC1]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PIGBOS1]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | APLP1 activity raises BSG's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.36× lower at baseline in the lines without APLP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BSG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CERCAM]] | B | CERCAM activity raises BSG's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without CERCAM | 0.031 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[L1CAM]] | B | L1CAM activity raises BSG's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without L1CAM | 0.058 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[COL1A2]] | B | COL1A2 activity raises BSG's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 1.46× lower at baseline in the lines without COL1A2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[P3H1]] | C | P3H1 activity raises BSG's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without P3H1 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |
| [[NLGN2]] | C | NLGN2 activity raises BSG's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without NLGN2 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.0, -21.9); signed map (-27.7, -38.7). **Vector** length 110, 38.8% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *epithelial mesenchymal transition* (hallmark, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +12.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.8 | +9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.7 | +5.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -4.7 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.3 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | basigin (Ok blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:571,277-583,494 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EMMPRIN, CD147, EMPRIN; previously OK |
| Gene groups (HGNC) | Blood group antigens; CD molecules; I-set domain containing; Basigin family |
| Hallmark sets | UV_RESPONSE_UP, HEME_METABOLISM |
| Reactome | 14 pathways, smallest: Proton-coupled monocarboxylate transport; Aspirin ADME; Basigin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P35613](https://www.uniprot.org/uniprotkb/P35613) (Basigin):

> [Isoform 1]: Essential for normal retinal maturation and development (By similarity). Acts as a retinal cell surface receptor for NXNL1 and plays an important role in NXNL1-mediated survival of retinal cone photoreceptors. In association with glucose transporter SLC16A1/GLUT1 and NXNL1, promotes retinal cone survival by enhancing aerobic glycolysis and accelerating the entry of glucose into photoreceptors. May act as a potent stimulator of IL6 secretion in multiple cell lines that include …

**Summary**, from NCBI Gene [682](https://www.ncbi.nlm.nih.gov/gene/682):

> The protein encoded by this gene, basigin, is a plasma membrane protein that is important in spermatogenesis, embryo implantation, neural network formation, and tumor progression. Basigin is also a member of the immunoglobulin superfamily, ubiquitously expressed in various tissues. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2020]

**Accessions** — [HGNC:1116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1116) · Entrez [682](https://www.ncbi.nlm.nih.gov/gene/682) · UniProt [P35613](https://www.uniprot.org/uniprotkb/P35613) · Ensembl [ENSG00000172270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172270)

## Data

Gene col 10233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10233); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10233]; `tensor/DDL_lfc|DDL_z.npy` [10233]; `embed/gene_vectors.npy` [10233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10233 or target_col == 10233). Every well: [[BSG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BSG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
