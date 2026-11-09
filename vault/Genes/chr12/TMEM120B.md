---
symbol: "TMEM120B"
type: "gene"
col: 12044
ensembl_id: "ENSG00000188735"
name: "transmembrane protein 120B"
location: "12q24.31"
module: 77
arm: "+"
pooled_cpm: 49.39
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TMEM120B

*transmembrane protein 120B* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.02× (z +23.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.363× (z -27.7, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.319× (z -23.3, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.80, fdr 7e-06), [[SDHAP2]] (+0.78, fdr 7e-06), [[COG5]] (+0.77, fdr 1e-05); moves opposite to [[TIA1]] (-0.75, fdr 7e-06), [[DDX6]] (-0.75, fdr 1e-05), [[MED12]] (-0.75, fdr 7e-06).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CARD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +23.5 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +22.2 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +20.2 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +12.5 | 9e-34 | 45/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +10.7 | 7e-25 | 42/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +7.5 | 6e-12 | 37/48 (A-427, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +7.2 | 5e-11 | 29/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +6.6 | 3e-09 | 28/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +5.0 | 3e-05 | 20/48 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +4.7 | 2e-04 | 17/48 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +4.6 | 2e-04 | 22/48 (HEC-1-A, J82, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 3e-04 | 18/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 1e-03 | 16/48 (LoVo, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 15/48 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.1 | 0.002 | 18/48 (H4, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.005 | 19/48 (H4, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.363×** | -27.7 | 0e+00 | 46/48 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.319×** | -23.3 | 0e+00 | 44/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.441×** | -17.4 | 0e+00 | 44/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -14.3 | 2e-44 | 30/42 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.531×** | -13.4 | 5e-39 | 39/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.535×** | -13.3 | 4e-38 | 41/48 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.557×** | -12.4 | 2e-33 | 34/48 (LoVo, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -11.9 | 9e-31 | 33/44 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.664×** | -8.7 | 3e-16 | 27/48 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -7.9 | 1e-13 | 29/48 (RPMI-7951, hTERT-HPNE, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -7.3 | 1e-11 | 26/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -6.6 | 3e-09 | 30/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -6.5 | 4e-09 | 26/49 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.758×** | -5.4 | 2e-06 | 27/47 (HS-578T, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **0.776×** | -5.4 | 3e-06 | 21/48 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.780×** | -5.3 | 5e-06 | 24/48 (C32, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -5.2 | 7e-06 | 26/48 (J82, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -4.6 | 1e-04 | 21/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.854× | -3.3 | 0.018 | 10/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.866× | -3.0 | 0.046 | 9/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.896× | -3.0 | 0.054 | 7/48 (J82, HS-578T, …) | top dose only |  |
| [[LJI308 (drug)]] 0.5 µM |  | **0.823×** | -2.9 | 0.057 | 6/48 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 71.1 | 3 | 12 (7 ⚠) | [[Belinostat (drug)]] 5 µM 3.15× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -17.8) |
| [[HOP62 (line)]] | alt | 49.0 | 5 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 4.18× (z +13.0) | [[Harringtonine (drug)]] 5 µM 0.206× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 59.2 | 3 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.261× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 56.4 | 3 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 50.9 | 4 (1 ⚠) | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -12.3) |
| [[SNU-423 (line)]] | alt | 59.5 | 3 | 7 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.189× (z -15.5) |
| [[BT-474 (line)]] | alt | 48.7 | 3 | 5 (4 ⚠) | [[Belinostat (drug)]] 5 µM 3.46× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.235× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 56.6 | 4 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.75× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.297× (z -11.3) |
| [[PANC-1 (line)]] | alt | 53.8 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.255× (z -13.9) |
| [[SW480 (line)]] | alt | 32.6 | 5 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.98× (z +17.7) | [[Harringtonine (drug)]] 5 µM 0.253× (z -14.5) |
| [[A498 (line)]] | wt | 82.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -23.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -18.5) |
| [[A549 (line)]] | wt | 56.0 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.272× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 43.2 | 3 (1 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.311× (z -12.1) |
| [[HS-578T (line)]] | alt | 69.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -24.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.127× (z -18.3) |
| [[LoVo (line)]] | wt | 63.6 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.151× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 26.9 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -17.0) |
| [[A-172 (line)]] | wt | 52.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -11.7) |
| [[C32 (line)]] | wt | 38.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 33.0 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.17× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.320× (z -8.7) |
| [[HT-29 (line)]] | alt | 40.4 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -10.0) |
| [[KATO III (line)]] | alt | 27.1 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.66× (z +12.5) | [[Harringtonine (drug)]] 5 µM 0.223× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 37.2 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.01× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 66.6 | 2 | 4 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.74× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -32.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.7) |
| [[SW 900 (line)]] | alt | 42.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.98× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.267× (z -10.3) |
| [[SW1417 (line)]] | alt | 34.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.21× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -12.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 45.3 | 2 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.95× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -21.0) |
| [[J82 (line)]] | alt | 54.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.39× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 39.2 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -16.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 52.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.296× (z -8.8) |
| [[SHP-77 (line)]] | alt | 57.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -17.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 35.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 37.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 27.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +11.3) | — |
| [[RKO (line)]] | wt | 45.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -13.6) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.268× (z -9.3) |
| [[SNU-1 (line)]] | wt | 52.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -10.9) |
| [[C-33 A (line)]] | alt | 63.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -11.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 38.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 81.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -10.9) |
| [[HCT15 (line)]] | alt | 39.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.44× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 59.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -8.9) |
| [[LS 180 (line)]] | wt | 33.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.267× (z -9.4) |
| [[SW48 (line)]] | wt | 54.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.80 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.78 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[COG5]] | +0.77 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.75 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.75 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ANKS3]] | +0.74 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TSEN54]] | +0.73 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MMS19]] | +0.72 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[AKR1A1]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[MPG]] | +0.71 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[YIF1B]] | +0.71 | +0.59 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.75 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[DDX6]] | -0.75 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[MED12]] | -0.75 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[C11orf58]] | -0.75 | -0.69 / -0.57 | both halves | 8e-06 |  |
| [[BAZ2B]] | -0.75 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | -0.72 | -0.72 / -0.31 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.72 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.71 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.70 | -0.69 / -0.37 | both halves | 8e-05 |  |
| [[RIPK2-DT]] | -0.69 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | -0.69 | -0.65 / -0.29 | both halves | 3e-04 |  |
| [[AKT1S1]] | -0.68 | -0.67 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD6]] | B | CARD6 activity lowers TMEM120B's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.14× higher at baseline in the lines without CARD6 | 0.073 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.6, 0.6); signed map (-41.7, -3.6). **Vector** length 132, 41.6% of its response variance represented; |z| ≥ 3 in 1,314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.5 | +22.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.8 | +20.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.7 | +23.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +12.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +4.6 | +4.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.5 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -11.8 | -27.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -23.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -6.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 120B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,712,752-121,783,001 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [A0PK00](https://www.uniprot.org/uniprotkb/A0PK00) (Transmembrane protein 120B):

> Necessary for efficient adipogenesis. Does not show ion channel activity.

**Summary**, from NCBI Gene [144404](https://www.ncbi.nlm.nih.gov/gene/144404):

> Predicted to be involved in fat cell differentiation and protein heterooligomerization. Predicted to be located in membrane. Predicted to be active in nuclear inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:32008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32008) · Entrez [144404](https://www.ncbi.nlm.nih.gov/gene/144404) · UniProt [A0PK00](https://www.uniprot.org/uniprotkb/A0PK00) · Ensembl [ENSG00000188735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188735)

## Data

Gene col 12044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12044); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12044]; `tensor/DDL_lfc|DDL_z.npy` [12044]; `embed/gene_vectors.npy` [12044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12044 or target_col == 12044). Every well: [[TMEM120B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM120B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
