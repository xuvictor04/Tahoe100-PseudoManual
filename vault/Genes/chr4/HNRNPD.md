---
symbol: "HNRNPD"
type: "gene"
col: 6208
ensembl_id: "ENSG00000138668"
name: "heterogeneous nuclear ribonucleoprotein D"
location: "4q21.22"
module: 3
arm: "-"
pooled_cpm: 230.87
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPD

*heterogeneous nuclear ribonucleoprotein D* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.06× (z +21.3, q 0e+00, up in 49 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 12 lines (NCI-H1573 11.0×, PANC-1 5.22×, LoVo 5.54×, HT-29 6.70×, …); [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 2.63×, SW480 2.94×, MIA PaCa-2 4.01×, NCI-H460 3.34×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 4.46×, J82 2.82×; ⚠ toxic; transcription drop); [[PH-797804 (drug)]] 5 µM in 2 lines (LS 180 6.29×, HEC-1-A 4.56×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.51×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.584× (z -18.9, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX9]] (+0.74, fdr 7e-06), [[SRSF10]] (+0.72, fdr 7e-06), [[SYNCRIP]] (+0.71, fdr 7e-06); moves opposite to [[CIAO2B]] (-0.65, fdr 1e-05), [[FTL]] (-0.65, fdr 7e-06), [[SWT1]] (-0.64, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6208.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 12 lines (NCI-H1573 11.0×, PANC-1 5.22×, LoVo 5.54×, HT-29 6.70×, …); [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 2.63×, SW480 2.94×, MIA PaCa-2 4.01×, NCI-H460 3.34×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (MIA PaCa-2 4.46×, J82 2.82×; ⚠ toxic; transcription drop); [[PH-797804 (drug)]] 5 µM in 2 lines (LS 180 6.29×, HEC-1-A 4.56×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.06×** | +21.3 | 0e+00 | 49/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +17.6 | 0e+00 | 46/49 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +16.3 | 0e+00 | 38/44 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +14.7 | 0e+00 | 45/48 (LS 180, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.42×** | +12.3 | 6e-33 | 42/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.63×** | +12.3 | 8e-33 | 45/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +12.3 | 9e-33 | 46/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +12.1 | 9e-32 | 38/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.51×** | +10.0 | 8e-22 | 40/48 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.42×** | +8.5 | 2e-15 | 38/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.4 | 1e-11 | 29/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +7.2 | 2e-11 | 30/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +7.0 | 8e-11 | 32/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.25×** | +5.6 | 9e-07 | 31/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.23×** | +5.1 | 1e-05 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.13× | +3.0 | 0.085 | 8/48 (C32, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -18.9 | 0e+00 | 44/49 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -16.7 | 0e+00 | 48/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.536×** | -15.6 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.602×** | -12.8 | 4e-35 | 46/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -8.1 | 5e-14 | 41/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -7.0 | 2e-10 | 32/48 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.769×** | -6.6 | 3e-09 | 31/48 (BT-474, RKO, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.776×** | -6.1 | 7e-08 | 29/47 (HT-29, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -5.3 | 6e-06 | 28/48 (LoVo, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.862× | -5.2 | 1e-05 | 20/48 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -5.1 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.8 | 7e-05 | 26/50 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.707×** | -4.6 | 2e-04 | 32/49 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.880× | -4.4 | 4e-04 | 14/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -4.4 | 4e-04 | 12/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.859× | -3.8 | 0.004 | 13/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.859× | -3.7 | 0.007 | 17/47 (A-427, C-33 A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | 0.871× | -3.4 | 0.019 | 12/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.907× | -3.3 | 0.019 | 4/48 (NCI-H23, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 167 | 13 (12 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.82× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -10.0) |
| [[LoVo (line)]] | wt | 261 | 9 (7 ⚠) | 5 | [[TAK-901 (drug)]] 5 µM 5.54× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -16.8) |
| [[A498 (line)]] | wt | 249 | 7 (6 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.01× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -18.5) |
| [[PANC-1 (line)]] | alt | 234 | 9 (7 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.22× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -17.0) |
| [[HT-29 (line)]] | alt | 238 | 7 (6 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.70× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -17.2) |
| [[KATO III (line)]] | alt | 216 | 7 (5 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.27× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 305 | 7 (5 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 11.0× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 150 | 11 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.91× (z +11.3) | — |
| [[SW480 (line)]] | alt | 303 | 7 (5 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +18.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.23× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -16.8) |
| [[J82 (line)]] | alt | 221 | 6 (5 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.76× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.482× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 216 | 8 (6 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 5.48× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.495× (z -9.7) |
| [[LS 180 (line)]] | wt | 230 | 6 (4 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +15.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.84× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -14.1) |
| [[A-427 (line)]] | wt | 291 | 4 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.13× (z +9.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.524× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 205 | 6 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +18.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.65× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -13.7) |
| [[HOP62 (line)]] | alt | 208 | 6 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.06× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -11.2) |
| [[A549 (line)]] | wt | 157 | 6 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.37× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 269 | 3 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.84× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -17.2) |
| [[SK-MEL-2 (line)]] | alt | 166 | 4 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.4) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.45× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -11.1) |
| [[SW48 (line)]] | wt | 315 | 5 (2 ⚠) | 3 | [[TAK-901 (drug)]] 0.05 µM 3.51× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -13.1) |
| [[A-172 (line)]] | wt | 184 | 6 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.83× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.567× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 272 | 3 (2 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 4.25× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 190 | 6 (4 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 5.38× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -11.0) |
| [[SHP-77 (line)]] | alt | 299 | 3 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.41× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 277 | 2 | 4 | [[PH-797804 (drug)]] 5 µM 4.56× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -16.6) |
| [[HS-578T (line)]] | alt | 150 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 209 | 3 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 10.3× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -11.5) |
| [[H4 (line)]] | wt | 239 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.60× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.0) |
| [[HCT15 (line)]] | alt | 339 | 3 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 5.30× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -14.2) |
| [[Hs 766T (line)]] | wt | 127 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.4) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.11× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 193 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.27× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.9) |
| [[RKO (line)]] | wt | 277 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.53× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 221 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.58× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 105 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +16.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 202 | 3 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 4.78× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -8.9) |
| [[BT-474 (line)]] | alt | 197 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.96× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -11.2) |
| [[C32 (line)]] | wt | 177 | 4 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.87× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 215 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 4.03× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -11.1) |
| [[C-33 A (line)]] | alt | 327 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 3.76× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 197 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.91× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 374 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 2.93× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 214 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.26× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 272 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.04× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -8.8) |
| [[CHP-212 (line)]] | wt | 246 | 0 | 1 | — | [[palbociclib (drug)]] 5 µM 0.169× (z -8.8) |
| [[AN3 CA (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 529 |
| [[SRSF10]] | +0.72 | +0.62 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 606 |
| [[SYNCRIP]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 980 |
| [[HNRNPM]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 962 |
| [[EWSR1]] | +0.70 | +0.53 / +0.77 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 677 |
| [[ARHGEF9]] | +0.68 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[C2CD5]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HNRNPR]] | +0.67 | +0.54 / +0.77 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 906 |
| [[HNRNPH3]] | +0.66 | +0.53 / +0.74 | both halves | 1e-05 | same gene group; STRING 918 |
| [[BCLAF1]] | +0.65 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[HNRNPL]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 924 |
| [[SF1]] | +0.65 | +0.44 / +0.73 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 543 |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | -0.65 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[FTL]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[SWT1]] | -0.64 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ZMAT5]] | -0.63 | -0.43 / -0.66 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TBC1D20]] | -0.63 | -0.38 / -0.74 | both halves | 7e-05 |  |
| [[CAMLG]] | -0.62 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[DUSP18]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[NQO2]] | -0.62 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[ATP6V0B]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[GID4]] | -0.61 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[RABAC1]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[GAN]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HNRNPD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.8, -25.3); signed map (13.9, -38.4). **Vector** length 112, 44.0% of its response variance represented; |z| ≥ 3 in 1,483 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.7 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.0 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +8.1 | +12.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +21.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +14.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | -1.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | -7.4 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | +0.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.6 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,352,498-82,374,503 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AUF1, HNRPD |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: AUF1 (hnRNP D0) binds and destabilizes mRNA; Regulation of mRNA stability by proteins that bind AU-rich elements; Dengue Virus Genome Translation and Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14103](https://www.uniprot.org/uniprotkb/Q14103) (Heterogeneous nuclear ribonucleoprotein D0):

> Binds with high affinity to RNA molecules that contain AU-rich elements (AREs) found within the 3'-UTR of many proto-oncogenes and cytokine mRNAs. Also binds to double- and single-stranded DNA sequences in a specific manner and functions a transcription factor. Each of the RNA-binding domains specifically can bind solely to a single-stranded non-monotonous 5'-UUAG-3' sequence and also weaker to the single-stranded 5'-TTAGGG-3' telomeric DNA repeat. Binds RNA oligonucleotides with 5'-UUAGGG-3' …

**Summary**, from NCBI Gene [3184](https://www.ncbi.nlm.nih.gov/gene/3184):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are nucleic acid binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP …

**Accessions** — [HGNC:5036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5036) · Entrez [3184](https://www.ncbi.nlm.nih.gov/gene/3184) · UniProt [Q14103](https://www.uniprot.org/uniprotkb/Q14103) · Ensembl [ENSG00000138668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138668)

## Data

Gene col 6208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6208); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6208]; `tensor/DDL_lfc|DDL_z.npy` [6208]; `embed/gene_vectors.npy` [6208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6208 or target_col == 6208). Every well: [[HNRNPD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
