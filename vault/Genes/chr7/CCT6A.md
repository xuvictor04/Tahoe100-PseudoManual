---
symbol: "CCT6A"
type: "gene"
col: 7117
ensembl_id: "ENSG00000146731"
name: "chaperonin containing TCP1 subunit 6A"
location: "7p11.2"
module: 60
arm: "+"
pooled_cpm: 180.11
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CCT6A

*chaperonin containing TCP1 subunit 6A* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.88× (z +18.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.77× (z +13.9, q 2e-41, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.467×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (BT-474 0.383×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.0947×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT3]] (+0.87, fdr 7e-06), [[CCT5]] (+0.84, fdr 7e-06), [[CCT4]] (+0.75, fdr 7e-06); moves opposite to [[SIRT2]] (-0.67, fdr 7e-06), [[GABARAP]] (-0.66, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[VAMP2]] (-0.66, fdr 7e-06), [[YY1AP1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTGES]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.88×** | +18.5 | 0e+00 | 49/49 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.77×** | +17.4 | 0e+00 | 44/44 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.77×** | +13.9 | 2e-41 | 48/48 (C32, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.32×** | +11.5 | 3e-28 | 48/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.29×** | +11.3 | 2e-27 | 47/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.42×** | +11.2 | 7e-27 | 45/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.23×** | +10.3 | 4e-23 | 46/48 (SW1417, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.6 | 2e-12 | 35/49 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +7.0 | 2e-10 | 43/45 (SW1417, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.62×** | +6.3 | 1e-08 | 43/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.51×** | +5.4 | 3e-06 | 36/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +5.4 | 3e-06 | 39/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.9 | 5e-05 | 32/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.42×** | +4.7 | 9e-05 | 39/48 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.27×** | +4.5 | 2e-04 | 39/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.86×** | +4.4 | 3e-04 | 40/48 (MIA PaCa-2, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.001 | 35/49 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.008 | 31/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.015 | 22/48 (A-172, SNU-423, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.015 | 29/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.015 | 24/47 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.015 | 29/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.021 | 27/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.027 | 32/48 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +3.1 | 0.031 | 14/48 (A-427, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7117.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.467×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (BT-474 0.383×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.0947×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.758× | -3.4 | 0.30 | 29/50 (LoVo, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.633× | -3.3 | 0.30 | 29/50 (LoVo, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.34 | 21/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.856× | -3.0 | 0.34 | 17/48 (HCT15, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 161 | 11 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.37× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 11 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 180 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.16× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.36× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 178 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.40× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 239 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 94.0 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.2× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.0) | — |
| [[A498 (line)]] | wt | 353 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.09× (z +10.3) | — |
| [[A549 (line)]] | wt | 127 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.55× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 105 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.76× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 162 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.06× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 230 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.45× (z +12.2) | — |
| [[C32 (line)]] | wt | 88.7 | 6 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.11× (z +16.2) | — |
| [[CFPAC-1 (line)]] | alt | 69.9 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 170 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.46× (z +15.1) | — |
| [[Hs 766T (line)]] | wt | 137 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.85× (z +12.0) | — |
| [[J82 (line)]] | alt | 169 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +10.2) | — |
| [[KATO III (line)]] | alt | 202 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 125 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 159 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.74× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 157 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.50× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 134 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.35× (z +12.1) | — |
| [[SW480 (line)]] | alt | 333 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.93× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.50× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 166 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.54× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 166 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.79× (z +10.1) | — |
| [[H4 (line)]] | wt | 206 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.49× (z +11.0) | — |
| [[LoVo (line)]] | wt | 202 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.79× (z +10.9) | — |
| [[RKO (line)]] | wt | 201 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.70× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 198 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.95× (z +11.0) | — |
| [[A-427 (line)]] | wt | 381 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 238 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 57.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 225 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.37× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 204 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.87× (z +15.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 66.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 346 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.42× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 76.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 169 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0947× (z -9.0) |
| [[SHP-77 (line)]] | alt | 268 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 154 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.81× (z +12.0) | — |
| [[SW 1271 (line)]] | alt | 135 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.60× (z +8.8) | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT3]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[CCT5]] | +0.84 | +0.86 / +0.80 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[CCT4]] | +0.75 | +0.79 / +0.74 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[HSPD1]] | +0.75 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 871 |
| [[NUDC]] | +0.73 | +0.74 / +0.73 | both halves | 7e-06 | STRING 554 |
| [[CCT7]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[TCP1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[STIP1]] | +0.71 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 931 |
| [[CCT2]] | +0.68 | +0.75 / +0.67 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[HSPA8]] | +0.68 | +0.56 / +0.78 | both halves | 1e-05 | STRING 872 |
| [[HSPA4]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 761 |
| [[UTP11]] | +0.68 | +0.69 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.67 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | -0.66 | -0.67 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VAMP2]] | -0.66 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[YY1AP1]] | -0.65 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[NEU1]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[CUTA]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NPC2]] | -0.61 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[WIPF2]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.60 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[SPPL3]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTGES]] | B | PTGES activity lowers CCT6A's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.45× higher at baseline in the lines without PTGES | 0.040 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.5, -31.4); signed map (-11.9, -44.5). **Vector** length 105, 45.6% of its response variance represented; |z| ≥ 3 in 1,364 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Hh mutants are degraded by ERAD* (reactome, mean cos +0.55 to 6); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.53 to 8); *Hh mutants abrogate ligand secretion* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.1 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.3 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +13.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.1 | +7.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.1 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.9 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.0 | +4.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.7 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.7 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.7 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:56,051,685-56,063,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TTCP20, TCPZ, Cctz, HTR3, TCP20; previously CCT6 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Chaperonin containing TCP1 |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 13 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; RHOBTB2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P40227](https://www.uniprot.org/uniprotkb/P40227) (T-complex protein 1 subunit zeta):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance.

**Summary**, from NCBI Gene [908](https://www.ncbi.nlm.nih.gov/gene/908):

> The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Alternate transcriptional splice variants of this gene, encoding …

**Accessions** — [HGNC:1620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1620) · Entrez [908](https://www.ncbi.nlm.nih.gov/gene/908) · UniProt [P40227](https://www.uniprot.org/uniprotkb/P40227) · Ensembl [ENSG00000146731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146731)

## Data

Gene col 7117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7117); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7117]; `tensor/DDL_lfc|DDL_z.npy` [7117]; `embed/gene_vectors.npy` [7117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7117 or target_col == 7117). Every well: [[CCT6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
