---
symbol: "LASP1"
type: "gene"
col: 25
ensembl_id: "ENSG00000002834"
name: "LIM and SH3 protein 1"
location: "17q12"
module: 4
arm: "-"
pooled_cpm: 171.33
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LASP1

*LIM and SH3 protein 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +10.5, q 6e-23, up in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (LoVo 2.16×, A549 2.14×, NCI-H460 2.07×, C-33 A 2.95×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A549 2.90×, SNU-423 2.58×, J82 2.47×, A498 2.24×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 2.92×, SNU-423 2.75×, A498 2.19×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.587× (z -12.7, q 2e-34, down in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.393× (z -11.6, q 4e-29, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM117A]] (+0.63, fdr 4e-05), [[AAMDC]] (+0.57, fdr 1e-05), [[ERO1B]] (+0.56, fdr 4e-05); moves opposite to [[PAK1IP1]] (-0.62, fdr 1e-05), [[KAT14]] (-0.62, fdr 9e-06), [[TMEM177]] (-0.61, fdr 8e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 25.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (LoVo 2.16×, A549 2.14×, NCI-H460 2.07×, C-33 A 2.95×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A549 2.90×, SNU-423 2.58×, J82 2.47×, A498 2.24×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 2.92×, SNU-423 2.75×, A498 2.19×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +10.5 | 6e-23 | 33/49 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +7.8 | 2e-12 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +7.3 | 5e-11 | 36/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.6 | 3e-06 | 25/44 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.5 | 3e-06 | 28/49 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | 1.20× | +4.2 | 0.002 | 19/48 (C32, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.033 | 22/48 (NCI-H460, SW480, …) | top dose only | composition shift; position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.095 | 9/49 (A498, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 25.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.587×** | -12.7 | 2e-34 | 37/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -12.6 | 1e-33 | 46/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.599×** | -12.2 | 5e-32 | 35/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -11.6 | 4e-29 | 41/49 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.628×** | -10.7 | 1e-24 | 38/47 (SW480, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.714×** | -8.0 | 9e-14 | 31/48 (SW480, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.577×** | -6.9 | 6e-10 | 34/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -6.5 | 5e-09 | 32/48 (HOP62, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.598×** | -6.4 | 1e-08 | 39/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.762×** | -6.3 | 2e-08 | 31/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.621×** | -5.9 | 2e-07 | 36/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.782×** | -5.8 | 3e-07 | 27/48 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.647×** | -5.4 | 2e-06 | 31/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.656×** | -5.3 | 6e-06 | 30/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.800×** | -5.1 | 1e-05 | 22/48 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.893× | -3.8 | 0.003 | 7/48 (HOP62, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.812×** | -3.6 | 0.009 | 21/49 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.813×** | -3.5 | 0.009 | 20/48 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.017 | 13/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.871× | -3.3 | 0.020 | 22/48 (SW480, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 25. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 195 | 2 (2 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.331× (z -18.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.508× (z -11.1) |
| [[A-172 (line)]] | wt | 188 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -10.5) |
| [[BT-474 (line)]] | alt | 1,070 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.420× (z -11.8) |
| [[Hs 766T (line)]] | wt | 139 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.382× (z -11.1) |
| [[SNU-423 (line)]] | alt | 205 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +14.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.414× (z -12.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 454 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.338× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -10.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 210 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -13.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.290× (z -8.8) |
| [[LoVo (line)]] | wt | 110 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -11.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.181× (z -19.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.172× (z -10.6) |
| [[A498 (line)]] | wt | 198 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.542× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 174 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.517× (z -9.5) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 205 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 195 | 0 | 4 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.247× (z -10.5) |
| [[HT-29 (line)]] | alt | 265 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.545× (z -10.6) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 155 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 233 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -14.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.326× (z -9.1) |
| [[PANC-1 (line)]] | alt | 53.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -9.5) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 170 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 63.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.159× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 105 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +13.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.508× (z -9.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 141 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.351× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 173 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.520× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 246 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.428× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 159 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.485× (z -9.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 147 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 73.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.638× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 86.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.349× (z -8.5) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 109 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.65× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 64.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.1) | — |
| [[H4 (line)]] | wt | 159 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 253 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.5) | — |
| [[SW48 (line)]] | wt | 89.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 96.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 25), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*24 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | +0.63 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[AAMDC]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ERO1B]] | +0.56 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[BAIAP2]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 | same gene group |
| [[CTDSP2]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 | same gene group |
| [[CRELD1]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[YPEL5]] | +0.53 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[TSC22D4]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[OTUD5]] | +0.52 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[OAT]] | +0.51 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[VAMP1]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[GNAS]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*76 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK1IP1]] | -0.62 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[KAT14]] | -0.62 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[TMEM177]] | -0.61 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[ORC5]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[DPH6]] | -0.60 | -0.55 / -0.64 | both halves | 1e-05 | same gene group |
| [[LTV1]] | -0.60 | -0.47 / -0.73 | both halves | 2e-05 |  |
| [[DIS3L2]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 | same gene group |
| [[AGK]] | -0.59 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[TSEN2]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[COA4]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[COA1]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[NAA25]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.7, -44.2); signed map (-11.4, 9.7). **Vector** length 139, 44.5% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.0 | -11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -7.2 | -10.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -7.0 | -6.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.4 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.3 | -6.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -5.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.4 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | LIM and SH3 protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,869,859-38,921,770 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MLN50, Lasp-1 |
| Gene groups (HGNC) | LIM domain containing; MicroRNA protein coding host genes; Nebulin family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14847](https://www.uniprot.org/uniprotkb/Q14847) (LIM and SH3 domain protein 1):

> Plays an important role in the regulation of dynamic actin-based, cytoskeletal activities. Agonist-dependent changes in LASP1 phosphorylation may also serve to regulate actin-associated ion transport activities, not only in the parietal cell but also in certain other F-actin-rich secretory epithelial cell types (By similarity).

**Summary**, from NCBI Gene [3927](https://www.ncbi.nlm.nih.gov/gene/3927):

> This gene encodes a member of a subfamily of LIM proteins, characterized by a LIM motif and a domain of Src homology region 3, and also a member of the nebulin family of actin-binding proteins. The encoded protein is a cAMP and cGMP dependent signaling protein and binds to the actin cytoskeleton at extensions of the cell membrane. The encoded protein has been linked to metastatic breast cancer, hematopoetic tumors such as B-cell lymphomas, and colorectal cancer. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:6513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6513) · Entrez [3927](https://www.ncbi.nlm.nih.gov/gene/3927) · UniProt [Q14847](https://www.uniprot.org/uniprotkb/Q14847) · Ensembl [ENSG00000002834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002834)

## Data

Gene col 25: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 25); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 25, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 25]; `tensor/DDL_lfc|DDL_z.npy` [25]; `embed/gene_vectors.npy` [25]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 25 or target_col == 25). Every well: [[LASP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LASP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
