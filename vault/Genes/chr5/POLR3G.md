---
symbol: "POLR3G"
type: "gene"
col: 3452
ensembl_id: "ENSG00000113356"
name: "RNA polymerase III subunit G"
location: "5q14.3"
module: 18
arm: "+"
pooled_cpm: 34.71
n_lines_expressing: 47
n_dd_up: 37
n_dd_down: 14
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# POLR3G

*RNA polymerase III subunit G* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.83× (z +17.5, q 0e+00, up in 36 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.71× (z +12.7, q 4e-35, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.778× (z -6.0, q 1e-06, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS7]] (+0.72, fdr 7e-06), [[FABP5]] (+0.69, fdr 7e-06), [[ANKS6]] (+0.68, fdr 7e-06); moves opposite to [[ATOSA]] (-0.65, fdr 1e-05), [[CREBRF]] (-0.59, fdr 2e-05), [[KDM5A]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLC16A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.83×** | +17.5 | 0e+00 | 36/43 (HOP62, A549, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.78×** | +17.1 | 0e+00 | 43/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.73×** | +16.9 | 0e+00 | 40/45 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.70×** | +16.6 | 0e+00 | 40/45 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.52×** | +14.9 | 0e+00 | 30/32 (J82, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.31×** | +14.1 | 5e-43 | 33/45 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +12.7 | 4e-35 | 38/45 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +11.4 | 2e-28 | 35/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.92×** | +10.5 | 6e-24 | 33/41 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.88×** | +9.8 | 5e-21 | 22/38 (J82, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.42×** | +8.3 | 7e-15 | 21/44 (NCI-H1792, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 6e-13 | 32/45 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +7.7 | 8e-13 | 29/45 (HOP62, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.58×** | +7.6 | 1e-12 | 30/44 (SW480, J82, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.63×** | +7.3 | 1e-11 | 28/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.46×** | +6.8 | 4e-10 | 26/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +6.7 | 7e-10 | 24/45 (NCI-H1792, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.30×** | +6.3 | 1e-08 | 28/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.68×** | +6.2 | 1e-08 | 27/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.15×** | +5.8 | 2e-07 | 25/42 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.57×** | +5.4 | 2e-06 | 24/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.38×** | +5.1 | 8e-06 | 23/45 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 4e-04 | 20/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.77×** | +4.3 | 4e-04 | 19/44 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.0 | 0.001 | 15/45 (LOX-IMVI, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -6.0 | 1e-06 | 21/44 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.535×** | -4.7 | 7e-04 | 20/45 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.751×** | -4.5 | 0.001 | 17/45 (C32, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.570×** | -4.2 | 0.003 | 14/43 (C32, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.591×** | -4.0 | 0.008 | 9/44 (C32, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.008 | 14/44 (AsPC-1, C32, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.749×** | -3.7 | 0.016 | 11/45 (LoVo, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.807×** | -3.5 | 0.038 | 18/44 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.809×** | -3.4 | 0.038 | 12/44 (A549, HEC-1-A, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.759×** | -3.3 | 0.054 | 7/45 (C32, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.824×** | -3.2 | 0.059 | 8/45 (C32, SW 1088, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 0.875× | -3.2 | 0.067 | 17/45 (C32, J82, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 0.875× | -3.2 | 0.067 | 8/45 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.662×** | -3.1 | 0.071 | 2/45 (C32, HEC-1-A) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.662×** | -3.1 | 0.071 | 2/45 (J82, C32) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.088 | 12/44 (SW480, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.672×** | -3.0 | 0.091 | 11/44 (C32, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.098 | 8/44 (NCI-H2030, A498, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.2 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.29× (z +10.1) | — |
| [[RKO (line)]] | wt | 84.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.1) |
| [[C32 (line)]] | wt | 184 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -16.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.6) |
| [[J82 (line)]] | alt | 76.8 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.02× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.444× (z -11.4) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 66.3 | 2 (2 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.66× (z +12.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.1) |
| [[A498 (line)]] | wt | 10.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +10.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[PANC-1 (line)]] | alt | 69.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.00× (z +9.2) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -17.6) |
| [[SW48 (line)]] | wt | 69.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 13.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +12.2) | — |
| [[LoVo (line)]] | wt | 28.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +9.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 22.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-427 (line)]] | wt | 70.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -12.0) |
| [[A549 (line)]] | wt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 8.04× (z +10.9) ⚠ unreliable plate only | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.23× (z +13.9) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 2.45× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 47.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.81× (z +9.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -10.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.3) |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.20× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[C-33 A (line)]] | alt | 88.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.1) |
| [[HCT15 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LOX-IMVI (line)]] | wt | 76.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.443× (z -9.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[NCI-H1573 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.21× (z +10.6) ⚠ toxic; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 6.00× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.70× (z +8.5) ⚠ unreliable plate only | — |
| [[A-172 (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS7]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[FABP5]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PALS2]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PACC1]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[FXN]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HEATR3]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SORD]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[UBE2G2]] | +0.64 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PPAT]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[XPO5]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSA]] | -0.65 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[CREBRF]] | -0.59 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[KDM5A]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[EFCAB6]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SLU7]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[FBXO8]] | -0.58 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NBR1]] | -0.57 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SYNRG]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZNF446]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RBM48]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[KAT6B]] | -0.55 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[ZNF490]] | -0.55 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises POLR3G's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without MCOLN2 | 0.006 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[FAM78B]] | B | FAM78B activity raises POLR3G's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.77× lower at baseline in the lines without FAM78B | 0.035 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[NT5M]] | B | NT5M activity raises POLR3G's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without NT5M | 0.039 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[PARVB]] | B | PARVB activity raises POLR3G's level | lines that do not express PARVB (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without PARVB | 0.047 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[ADCY3]] | B | ADCY3 activity raises POLR3G's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without ADCY3 | 0.064 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A1]] | C | POLR3G activity raises SLC16A1's level | lines that do not express POLR3G (3) vs lines expressing it (47) | 3.44× lower at baseline in the lines without POLR3G | 0.054 | ⚠ few lines (3 vs 47); across organs; also absent: HMGA1, PALS2, SLC35F2; maybe low, not absent; co-absent with the target |
| [[ZNF215]] | C | POLR3G activity raises ZNF215's level | lines that do not express POLR3G (3) vs lines expressing it (47) | 6.60× lower at baseline in the lines without POLR3G | 0.060 | ⚠ few lines (3 vs 47); across organs; also absent: HMGA1, PALS2, SLC35F2; maybe low, not absent |
| [[HPRT1]] | C | POLR3G activity raises HPRT1's level | lines that do not express POLR3G (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without POLR3G | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: HMGA1, PALS2, SLC35F2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.5, -39.7); signed map (-8.6, -55.8). **Vector** length 116, 33.0% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.7 | +17.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.5 | +6.3 |
|  | [[EX229 (drug)]] 5 µM |  | +5.3 | +6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.0 | +5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.0 | +7.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.0 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.7 | +0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:90,471,748-90,514,557 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPC32, RPC7, C31 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [O15318](https://www.uniprot.org/uniprotkb/O15318) (DNA-directed RNA polymerase III subunit RPC7):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Acts as a long tether that bridges POLR3C/RPC3-POLR3F/RPC6-POLR3G/RPC7 heterotrimer and the mobile stalk of Pol III, coordinating the dynamics of Pol III stalk and clamp modules …

**Summary**, from NCBI Gene [10622](https://www.ncbi.nlm.nih.gov/gene/10622):

> Enables chromatin binding activity. Involved in positive regulation of innate immune response; positive regulation of interferon-beta production; and transcription by RNA polymerase III. Acts upstream of or within cell population proliferation. Located in nuclear body. Part of RNA polymerase III complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30075) · Entrez [10622](https://www.ncbi.nlm.nih.gov/gene/10622) · UniProt [O15318](https://www.uniprot.org/uniprotkb/O15318) · Ensembl [ENSG00000113356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113356)

## Data

Gene col 3452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3452); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3452]; `tensor/DDL_lfc|DDL_z.npy` [3452]; `embed/gene_vectors.npy` [3452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3452 or target_col == 3452). Every well: [[POLR3G — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3G.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
