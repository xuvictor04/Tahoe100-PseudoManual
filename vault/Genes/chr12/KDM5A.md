---
symbol: "KDM5A"
type: "gene"
col: 1055
ensembl_id: "ENSG00000073614"
name: "lysine demethylase 5A"
location: "12p13.33"
module: 74
arm: "+"
pooled_cpm: 188.08
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# KDM5A

*lysine demethylase 5A* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.65× (z +22.9, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.598× (z -16.8, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.608× (z -8.8, q 1e-16, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLU7]] (+0.70, fdr 7e-06), [[BOD1L1]] (+0.69, fdr 7e-06), [[ZNF791]] (+0.65, fdr 7e-06); moves opposite to [[FAM20B]] (-0.60, fdr 1e-05), [[POLR3G]] (-0.59, fdr 1e-05), [[XPO5]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.65×** | +22.9 | 0e+00 | 47/49 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +20.7 | 0e+00 | 39/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +15.4 | 0e+00 | 43/48 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +13.1 | 5e-37 | 37/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +11.4 | 4e-28 | 35/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +9.8 | 1e-20 | 34/48 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +8.0 | 1e-13 | 29/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +7.5 | 6e-12 | 21/49 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.18× | +5.7 | 7e-07 | 20/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.0 | 3e-05 | 19/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.9 | 4e-05 | 19/50 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +4.7 | 1e-04 | 25/49 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.10× | +4.7 | 1e-04 | 14/48 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.3 | 6e-04 | 20/48 (LS 180, NCI-H460, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.14× | +4.1 | 0.002 | 12/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.12× | +3.6 | 0.013 | 9/49 (BT-474, J82, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.10× | +3.3 | 0.028 | 4/48 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.028 | 11/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -16.8 | 0e+00 | 36/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.614×** | -16.5 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.659×** | -14.1 | 5e-43 | 41/49 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -10.8 | 3e-25 | 35/47 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.608×** | -8.8 | 1e-16 | 41/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.616×** | -8.6 | 9e-16 | 42/48 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.638×** | -8.0 | 1e-13 | 40/48 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.644×** | -7.8 | 5e-13 | 39/48 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.692×** | -6.5 | 5e-09 | 37/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.824×** | -6.1 | 7e-08 | 26/45 (Hs 766T, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.803×** | -5.3 | 6e-06 | 29/48 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.857× | -5.2 | 7e-06 | 19/48 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.825×** | -4.6 | 1e-04 | 24/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.874× | -4.3 | 6e-04 | 15/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.836× | -4.3 | 6e-04 | 23/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.940× | -3.0 | 0.098 | 1/49 (H4) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 230 | 6 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +18.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.621× (z -10.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 356 | 5 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.24× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -21.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 292 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 317 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -17.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 114 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 253 | 5 (3 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +21.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +16.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.469× (z -13.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 199 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +17.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.500× (z -11.2) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 193 | 4 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.22× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.476× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 269 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.18× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -23.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 257 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -16.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 201 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 163 | 4 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.66× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.501× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 83.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.7) | — |
| [[NCI-H23 (line)]] | alt | 308 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -28.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 212 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -23.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 168 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.75× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 130 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.531× (z -9.4) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 175 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +23.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.525× (z -12.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 218 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 156 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.18× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.451× (z -11.8) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 160 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 233 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.506× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 151 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.6) | — |
| [[A-172 (line)]] | wt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +24.2) | — |
| [[BT-474 (line)]] | alt | 149 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +17.4) | — |
| [[COLO 205 (line)]] | alt | 231 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.14× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -16.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 216 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -17.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 160 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.448× (z -13.0) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 226 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.02× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 186 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +16.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.481× (z -17.4) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.496× (z -8.7) |
| [[PANC-1 (line)]] | alt | 121 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.02× (z +15.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.585× (z -11.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 156 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.89× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.131× (z -14.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 150 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.16× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.493× (z -10.8) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.448× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 144 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.413× (z -9.8) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.485× (z -9.6) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 155 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.18× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 228 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 236 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.85× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 185 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 195 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 292 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[BOD1L1]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[GPANK1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TOX4]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GOLGB1]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PIN4]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[USP8]] | +0.63 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[NBR1]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TBC1D15]] | +0.61 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[CRNKL1]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM20B]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[POLR3G]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[XPO5]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[CAD]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A15]] | -0.57 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[GK5]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PALS2]] | -0.56 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[SORD]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CAMKK2]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[CMTM4]] | -0.55 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[SEH1L]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PUS7]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.1, -47.5); signed map (2.9, -14.6). **Vector** length 129, 40.8% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.1 | +22.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.7 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +15.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +6.1 | +4.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +4.5 | +5.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.7 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.5 | -16.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.0 | -10.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.9 | -8.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.6 | -8.6 |
|  | [[EX229 (drug)]] 5 µM |  | -7.5 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.3 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:280,057-389,320 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RBBP2, JARID1A |
| Gene groups (HGNC) | PHD finger proteins; AT-rich interaction domain containing; EMSY complex; Lysine demethylase 5 family |
| Reactome | 6 pathways, smallest: Chromatin modifications during the maternal to zygotic transition (MZT); HDMs demethylate histones; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P29375](https://www.uniprot.org/uniprotkb/P29375) (Lysine-specific demethylase 5A):

> Histone demethylase that specifically demethylates 'Lys-4' of histone H3, thereby playing a central role in histone code. Does not demethylate histone H3 'Lys-9', H3 'Lys-27', H3 'Lys-36', H3 'Lys-79' or H4 'Lys-20'. Demethylates trimethylated and dimethylated but not monomethylated H3 'Lys-4'. Regulates specific gene transcription through DNA-binding on 5'-CCGCCC-3' motif. May stimulate transcription mediated by nuclear receptors. Involved in transcriptional regulation of Hox proteins during …

**Summary**, from NCBI Gene [5927](https://www.ncbi.nlm.nih.gov/gene/5927):

> This gene encodes a member of the Jumonji, AT-rich interactive domain 1 (JARID1) histone demethylase protein family. The encoded protein plays a role in gene regulation through the histone code by specifically demethylating lysine 4 of histone H3. The encoded protein interacts with many other proteins, including retinoblastoma protein, and is implicated in the transcriptional regulation of Hox genes and cytokines. This gene may play a role in tumor progression. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:9886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9886) · Entrez [5927](https://www.ncbi.nlm.nih.gov/gene/5927) · UniProt [P29375](https://www.uniprot.org/uniprotkb/P29375) · Ensembl [ENSG00000073614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073614)

## Data

Gene col 1055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1055); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1055]; `tensor/DDL_lfc|DDL_z.npy` [1055]; `embed/gene_vectors.npy` [1055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1055 or target_col == 1055). Every well: [[KDM5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
