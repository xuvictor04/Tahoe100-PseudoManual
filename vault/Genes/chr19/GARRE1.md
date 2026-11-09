---
symbol: "GARRE1"
type: "gene"
col: 9297
ensembl_id: "ENSG00000166398"
name: "granule associated Rac and RHOG effector 1"
location: "19q13.11"
module: 145
arm: "+"
pooled_cpm: 84.96
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# GARRE1

*granule associated Rac and RHOG effector 1* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.56× (z +9.8, q 5e-20, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.301× (z -26.4, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.286× (z -14.4, q 8e-45, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLU7]] (+0.71, fdr 1e-04), [[UBXN7]] (+0.70, fdr 3e-05), [[AGO4]] (+0.68, fdr 7e-06); moves opposite to [[DHX9]] (-0.51, fdr 4e-05), [[NAA15]] (-0.51, fdr 5e-05), [[CS]] (-0.51, fdr 2e-04).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.56×** | +9.8 | 5e-20 | 43/49 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +7.0 | 8e-10 | 39/48 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +6.8 | 2e-09 | 34/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.4 | 2e-08 | 25/49 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +5.5 | 3e-06 | 23/48 (LOX-IMVI, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.22×** | +4.3 | 0.002 | 24/47 (NCI-H2030, H4, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.7 | 0.020 | 16/48 (CFPAC-1, A498, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.6 | 0.023 | 18/48 (COLO 205, HepG2/C3A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.12× | +3.4 | 0.035 | 8/48 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.035 | 18/48 (KATO III, SW1417, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.035 | 19/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.035 | 12/49 (C32, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.035 | 15/47 (NCI-H2030, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.045 | 16/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.045 | 12/49 (SW480, A-172, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.10× | +3.1 | 0.073 | 3/49 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.098 | 11/48 (CFPAC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.301×** | -26.4 | 0e+00 | 48/48 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.444×** | -17.8 | 0e+00 | 44/49 (A549, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -17.5 | 0e+00 | 41/44 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.426×** | -17.3 | 0e+00 | 41/45 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.286×** | -14.4 | 8e-45 | 45/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.287×** | -14.3 | 1e-44 | 45/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.330×** | -12.7 | 4e-35 | 47/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.369×** | -11.4 | 2e-28 | 47/48 (MIA PaCa-2, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.376×** | -11.2 | 2e-27 | 43/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -8.5 | 8e-16 | 34/47 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.589×** | -8.3 | 6e-15 | 41/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -8.0 | 8e-14 | 37/49 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.613×** | -7.7 | 9e-13 | 43/49 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.695×** | -7.5 | 2e-12 | 40/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.530×** | -7.3 | 1e-11 | 36/47 (LoVo, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.646×** | -6.8 | 3e-10 | 40/48 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.832×** | -4.0 | 0.002 | 21/48 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.735×** | -3.5 | 0.012 | 16/47 (H4, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.852× | -3.5 | 0.012 | 17/48 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.019 | 20/48 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 118 | 0 | 12 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.126× (z -23.8) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.123× (z -12.6) |
| [[PANC-1 (line)]] | alt | 129 | 1 (1 ⚠) | 11 (7 ⚠) | [[Selinexor (drug)]] 0.5 µM 1.71× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.232× (z -12.3) |
| [[HT-29 (line)]] | alt | 126 | 2 (1 ⚠) | 8 (5 ⚠) | [[Selinexor (drug)]] 5 µM 1.73× (z +9.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.166× (z -11.7) |
| [[A498 (line)]] | wt | 84.3 | 1 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -19.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.236× (z -10.5) |
| [[A549 (line)]] | wt | 159 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Abemaciclib (drug)]] 5 µM 0.234× (z -10.6) |
| [[A-172 (line)]] | wt | 102 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.241× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Abemaciclib (drug)]] 5 µM 0.290× (z -10.0) |
| [[HOP62 (line)]] | alt | 119 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.297× (z -16.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.280× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 67.0 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -15.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.133× (z -11.6) |
| [[KATO III (line)]] | alt | 69.5 | 1 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.195× (z -9.3) |
| [[LoVo (line)]] | wt | 68.7 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.273× (z -15.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.198× (z -10.3) |
| [[SW1417 (line)]] | alt | 86.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.211× (z -10.4) |
| [[SW480 (line)]] | alt | 91.1 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -18.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.259× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 94.6 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -14.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.237× (z -8.8) |
| [[H4 (line)]] | wt | 114 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0431× (z -26.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 66.3 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.175× (z -16.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.131× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 63.2 | 2 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.95× (z +10.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Selinexor (drug)]] 0.05 µM 2.18× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -14.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.203× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 53.2 | 1 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.85× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -14.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.212× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 67.0 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.250× (z -15.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.217× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 95.1 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -14.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 40.3 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -15.3) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 81.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 68.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -20.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -13.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 85.6 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.265× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[HS-578T (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -13.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.256× (z -8.7) |
| [[J82 (line)]] | alt | 77.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.433× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 61.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -22.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 73.3 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -13.6) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 81.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 92.5 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -14.1) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 80.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.202× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 43.4 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -14.7) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 67.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -13.0) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 84.8 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -10.7) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.172× (z -8.9) |
| [[SHP-77 (line)]] | alt | 94.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -19.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 54.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 87.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -11.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -9.1) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 82.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.318× (z -11.0) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 64.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -8.8) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 70.8 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.101× (z -9.5) |
| [[CHP-212 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | +0.71 | +0.33 / +0.77 | both halves | 1e-04 |  |
| [[UBXN7]] | +0.70 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[AGO4]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.67 | +0.42 / +0.74 | both halves | 4e-05 |  |
| [[ATXN3]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[OGA]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[WDR48]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[TMEM50A]] | +0.62 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[PIK3CA]] | +0.62 | +0.40 / +0.70 | both halves | 5e-05 | pathway: RAC1 GTPase cycle; STRING 402 |
| [[RB1CC1]] | +0.62 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[EZH1]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.61 | +0.48 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | -0.51 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NAA15]] | -0.51 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CS]] | -0.51 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[ILF3]] | -0.50 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[INTS7]] | -0.50 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[EMC1]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[FIRRE]] | -0.50 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TUBB]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MTHFD1]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SARS2]] | -0.48 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[PSMD1]] | -0.48 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.8, -44.1); signed map (-14.9, 9.0). **Vector** length 130, 41.0% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +8.7 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.4 | +6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +3.2 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.3 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.8 | -26.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.2 | -14.3 |
|  | [[EX229 (drug)]] 5 µM |  | -10.8 | -14.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -9.8 | -12.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.5 | -11.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -9.0 | -11.2 |

## What is on record

|  |  |
|---|---|
| Name | granule associated Rac and RHOG effector 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,254,552-34,355,566 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MiniBAR; previously KIAA0355 |
| Reactome | 7 pathways, smallest: RHOG GTPase cycle; RAC2 GTPase cycle; RAC3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O15063](https://www.uniprot.org/uniprotkb/O15063) (Granule associated Rac and RHOG effector protein 1):

> Acts as an effector of RAC1. Associates with CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. May also play a role in miRNA silencing machinery.

**Summary**, from NCBI Gene [9710](https://www.ncbi.nlm.nih.gov/gene/9710):

> Enables CCR4-NOT complex binding activity and small GTPase binding activity. Involved in Rac protein signal transduction. Located in P-body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29016) · Entrez [9710](https://www.ncbi.nlm.nih.gov/gene/9710) · UniProt [O15063](https://www.uniprot.org/uniprotkb/O15063) · Ensembl [ENSG00000166398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166398)

## Data

Gene col 9297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9297); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9297]; `tensor/DDL_lfc|DDL_z.npy` [9297]; `embed/gene_vectors.npy` [9297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9297 or target_col == 9297). Every well: [[GARRE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GARRE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
