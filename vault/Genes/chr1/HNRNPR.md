---
symbol: "HNRNPR"
type: "gene"
col: 4693
ensembl_id: "ENSG00000125944"
name: "heterogeneous nuclear ribonucleoprotein R"
location: "1p36.12"
module: 4
arm: "+"
pooled_cpm: 203.04
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HNRNPR

*heterogeneous nuclear ribonucleoprotein R* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.08× (z +16.1, q 0e+00, up in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.60× (z +10.9, q 2e-25, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.632× (z -14.9, q 0e+00, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBGCP3]] (+0.72, fdr 7e-06), [[SSRP1]] (+0.71, fdr 7e-06), [[CSE1L]] (+0.68, fdr 7e-06); moves opposite to [[SIRT6]] (-0.63, fdr 1e-05), [[EIF1B]] (-0.62, fdr 7e-06), [[ZFYVE1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +16.1 | 0e+00 | 38/44 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.95×** | +15.3 | 0e+00 | 44/49 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +10.9 | 2e-25 | 45/48 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +10.1 | 1e-21 | 44/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.59×** | +9.8 | 1e-20 | 40/45 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.36×** | +6.8 | 9e-10 | 35/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.1 | 7e-08 | 28/38 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.1 | 8e-08 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.22×** | +4.6 | 3e-04 | 25/48 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.20×** | +4.2 | 0.001 | 22/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.2 | 0.001 | 23/48 (A549, RKO, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.0 | 0.003 | 23/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.18× | +3.7 | 0.009 | 20/48 (A549, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 1.16× | +3.5 | 0.022 | 20/48 (LoVo, KATO III, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.023 | 8/49 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.026 | 22/48 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.076 | 22/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -14.9 | 0e+00 | 43/49 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.647×** | -10.0 | 4e-21 | 44/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.700×** | -8.2 | 5e-14 | 36/48 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.727×** | -7.3 | 3e-11 | 40/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -6.4 | 2e-08 | 32/48 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.831×** | -6.0 | 2e-07 | 24/48 (J82, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 0.868× | -4.6 | 3e-04 | 12/48 (A498, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.818×** | -4.6 | 3e-04 | 26/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -4.4 | 5e-04 | 21/48 (AN3 CA, SNU-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.837× | -4.1 | 0.003 | 22/47 (SW48, LS 180, …) | two highest doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.898× | -3.5 | 0.022 | 10/48 (A-172, C-33 A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.854× | -3.3 | 0.042 | 19/48 (A498, SW48, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.057 | 20/48 (SW 1271, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.872× | -3.1 | 0.067 | 10/49 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.1 | 0.067 | 23/50 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.911× | -3.0 | 0.083 | 3/49 (A549, H4, …) | rises with dose |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.084 | 12/48 (KATO III, HCT15, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.915× | -2.9 | 0.095 | 10/48 (SW 900, SW1417, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.877× | -2.9 | 0.095 | 11/48 (LS 180, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 163 | 8 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.64× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -12.5) |
| [[PANC-1 (line)]] | alt | 267 | 4 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +10.4) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.12× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -15.4) |
| [[HOP62 (line)]] | alt | 241 | 3 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.46× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.32× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.5) |
| [[A549 (line)]] | wt | 156 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.52× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 199 | 5 (2 ⚠) | 1 | [[TAK-901 (drug)]] 0.05 µM 2.47× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -11.0) |
| [[LS 180 (line)]] | wt | 179 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.76× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.8) |
| [[SW480 (line)]] | alt | 255 | 2 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.82× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -17.8) |
| [[A498 (line)]] | wt | 187 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.1) |
| [[C-33 A (line)]] | alt | 507 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -19.3) |
| [[J82 (line)]] | alt | 263 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.536× (z -15.4) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 152 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.26× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -11.4) |
| [[SW 900 (line)]] | alt | 189 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 155 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 135 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.87× (z +11.1) | — |
| [[H4 (line)]] | wt | 199 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 211 | 2 (1 ⚠) | 2 | [[TAK-901 (drug)]] 0.05 µM 1.81× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -17.7) |
| [[HS-578T (line)]] | alt | 232 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -8.6) |
| [[KATO III (line)]] | alt | 170 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 172 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -16.7) |
| [[A-172 (line)]] | wt | 110 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 238 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.505× (z -10.1) |
| [[HCT15 (line)]] | alt | 225 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.5) |
| [[Hs 766T (line)]] | wt | 185 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 160 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 172 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.82× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 136 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 243 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -17.9) |
| [[RKO (line)]] | wt | 288 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.19× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -19.6) |
| [[SNU-1 (line)]] | wt | 286 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -11.5) |
| [[SNU-423 (line)]] | alt | 130 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +12.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 286 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.438× (z -11.0) |
| [[BT-474 (line)]] | alt | 177 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.05× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.4) |
| [[C32 (line)]] | wt | 171 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 136 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 191 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 190 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.6) |
| [[SW48 (line)]] | wt | 282 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.13× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 314 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.518× (z -9.2) |
| [[SHP-77 (line)]] | alt | 285 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.9) |
| [[SW1417 (line)]] | alt | 183 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.593× (z -8.6) |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBGCP3]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[SSRP1]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[HNRNPD]] | +0.67 | +0.54 / +0.77 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 906 |
| [[AGPS]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[XRCC5]] | +0.66 | +0.61 / +0.71 | both halves | 7e-06 | STRING 463 |
| [[PRKDC]] | +0.66 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[AIFM1]] | +0.66 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[SSX2IP]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[DHX9]] | +0.65 | +0.55 / +0.71 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 909 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT6]] | -0.63 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.62 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ZBTB43]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EIF1]] | -0.58 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[CSTB]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[ATG2A]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RBM38]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 | same gene group |
| [[ZMAT5]] | -0.56 | -0.39 / -0.63 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNHIT1]] | -0.56 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[CATSPERG]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.56 | -0.38 / -0.69 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HNRNPR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.7, -36.4); signed map (-17.8, -44.9). **Vector** length 119, 43.0% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.1 | +15.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.2 | +9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +10.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | -2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -14.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.9 | -4.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.7 | -1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.4 | -2.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -3.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein R |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,303,771-23,344,336 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hnRNP-R; previously HNRPR |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O43390](https://www.uniprot.org/uniprotkb/O43390) (Heterogeneous nuclear ribonucleoprotein R):

> Component of ribonucleosomes, which are complexes of at least 20 other different heterogeneous nuclear ribonucleoproteins (hnRNP). hnRNP play an important role in processing of precursor mRNA in the nucleus.

**Summary**, from NCBI Gene [10236](https://www.ncbi.nlm.nih.gov/gene/10236):

> This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:5047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5047) · Entrez [10236](https://www.ncbi.nlm.nih.gov/gene/10236) · UniProt [O43390](https://www.uniprot.org/uniprotkb/O43390) · Ensembl [ENSG00000125944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125944)

## Data

Gene col 4693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4693); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4693]; `tensor/DDL_lfc|DDL_z.npy` [4693]; `embed/gene_vectors.npy` [4693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4693 or target_col == 4693). Every well: [[HNRNPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
