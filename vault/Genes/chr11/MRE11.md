---
symbol: "MRE11"
type: "gene"
col: 324
ensembl_id: "ENSG00000020922"
name: "MRE11 double strand break repair nuclease"
location: "11q21"
module: 6
arm: "+"
pooled_cpm: 59.34
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MRE11

*MRE11 double strand break repair nuclease* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.81× (z +14.3, q 2e-43, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.49× (z +4.4, q 4e-04, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.622× (z -11.4, q 3e-27, down in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.756× (z -6.7, q 3e-09, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBBP4]] (+0.72, fdr 7e-06), [[MSH2]] (+0.70, fdr 7e-06), [[DDX12P]] (+0.70, fdr 7e-06); moves opposite to [[ALG2]] (-0.60, fdr 1e-05), [[ACAP1]] (-0.59, fdr 1e-05), [[MTHFR]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.81×** | +14.3 | 2e-43 | 44/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +13.6 | 7e-40 | 41/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.72×** | +13.1 | 9e-37 | 41/48 (HT-29, HS-578T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +11.7 | 2e-29 | 35/48 (SW1417, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.59×** | +10.8 | 5e-25 | 33/42 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.55×** | +10.5 | 8e-24 | 38/49 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +7.3 | 2e-11 | 31/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.36×** | +6.9 | 5e-10 | 26/45 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.30×** | +6.2 | 4e-08 | 29/49 (LS 180, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +5.9 | 2e-07 | 23/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +5.3 | 6e-06 | 21/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.22×** | +4.9 | 6e-05 | 21/48 (J82, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.4 | 4e-04 | 17/48 (HT-29, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 18/48 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.17× | +3.9 | 0.004 | 14/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.005 | 8/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.010 | 15/47 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.10× | +3.3 | 0.034 | 6/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.037 | 5/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.060 | 8/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.073 | 8/48 (KATO III, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.622×** | -11.4 | 3e-27 | 41/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.744×** | -10.0 | 3e-21 | 32/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.712×** | -8.2 | 6e-14 | 30/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -6.7 | 3e-09 | 32/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.569×** | -6.3 | 3e-08 | 27/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.574×** | -6.2 | 5e-08 | 26/48 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -5.7 | 8e-07 | 22/47 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.791×** | -5.4 | 4e-06 | 26/48 (MIA PaCa-2, SW480, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.805×** | -5.2 | 1e-05 | 22/48 (AN3 CA, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.735×** | -5.2 | 1e-05 | 22/48 (SW480, LoVo, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.736×** | -5.2 | 1e-05 | 23/47 (NCI-H1573, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.632×** | -5.1 | 1e-05 | 23/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 3e-05 | 21/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.654×** | -4.8 | 8e-05 | 21/48 (SW480, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.6 | 2e-04 | 0/49 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.774×** | -4.3 | 5e-04 | 19/48 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.844× | -4.1 | 0.001 | 16/48 (RKO, SW48, …) | two highest doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.840× | -3.9 | 0.002 | 16/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -3.6 | 0.008 | 9/48 (SW480, SNU-423, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.726×** | -3.6 | 0.008 | 12/48 (Hs 766T, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.010 | 14/48 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.019 | 15/48 (SW1417, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 116 | 1 (1 ⚠) | 8 (7 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.34× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -18.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.299× (z -8.9) |
| [[HT-29 (line)]] | alt | 62.1 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 81.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0984× (z -25.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.440× (z -9.2) |
| [[A498 (line)]] | wt | 43.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.483× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 26.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[H4 (line)]] | wt | 49.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[Hs 766T (line)]] | wt | 61.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H1573 (line)]] | alt | 34.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 83.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.5) ⚠ cell-cycle shift, explains ~27% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.390× (z -11.3) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AN3 CA (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.177× (z -9.7) ⚠ cell-cycle shift, explains ~14% of this change |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.270× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.441× (z -10.1) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HS-578T (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 97.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -9.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 56.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 54.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 53.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 77.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 67.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -9.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP4]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[MSH2]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 847 |
| [[DDX12P]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.66 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[FANCI]] | +0.66 | +0.73 / +0.59 | both halves | 7e-06 | STRING 542 |
| [[KNTC1]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[RAD51AP1]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 664 |
| [[TIMELESS]] | +0.65 | +0.72 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[RBBP7]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPU]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[RRM1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RPA1]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 953 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG2]] | -0.60 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[ACAP1]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[MTHFR]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[OSGIN1]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TUBB2A]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[GSPT2]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[EID2]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[LRRC8E]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[C14orf119]] | -0.55 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRE11's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.1, -44.1); signed map (-35.9, -42.7). **Vector** length 114, 31.3% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of the pre-replicative complex* (reactome, mean cos +0.50 to 22); *Activation of ATR in response to replication stress* (reactome, mean cos +0.50 to 23); *Unwinding of DNA* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.6 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.7 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.4 | +6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -8.1 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.4 | -8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.1 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | MRE11 double strand break repair nuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,415,570-94,493,885 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATLD; previously MRE11A |
| Gene groups (HGNC) | BRCA1 C complex; MRN complex; MicroRNA protein coding host genes |
| Hallmark sets | E2F_TARGETS |
| Reactome | 44 pathways, smallest: Sensing of DNA Double Strand Breaks; IRF3-mediated induction of type I IFN; HDR through MMEJ (alt-NHEJ) |
| Matched by | ensembl_id |

**Function**, from UniProt [P49959](https://www.uniprot.org/uniprotkb/P49959) (Double-strand break repair protein MRE11):

> Core component of the MRN complex, which plays a central role in double-strand break (DSB) repair, DNA recombination, maintenance of telomere integrity and meiosis. The MRN complex is involved in the repair of DNA double-strand breaks (DSBs) via homologous recombination (HR), an error-free mechanism which primarily occurs during S and G2 phases. The complex (1) mediates the end resection of damaged DNA, which generates proper single-stranded DNA, a key initial steps in HR, and is (2) required …

**Summary**, from NCBI Gene [4361](https://www.ncbi.nlm.nih.gov/gene/4361):

> This gene encodes a nuclear protein involved in homologous recombination, telomere length maintenance, and DNA double-strand break repair. By itself, the protein has 3' to 5' exonuclease activity and endonuclease activity. The protein forms a complex with the RAD50 homolog; this complex is required for nonhomologous joining of DNA ends and possesses increased single-stranded DNA endonuclease and 3' to 5' exonuclease activities. In conjunction with a DNA ligase, this protein promotes the joining …

**Accessions** — [HGNC:7230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7230) · Entrez [4361](https://www.ncbi.nlm.nih.gov/gene/4361) · UniProt [P49959](https://www.uniprot.org/uniprotkb/P49959) · Ensembl [ENSG00000020922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020922)

## Data

Gene col 324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 324); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 324]; `tensor/DDL_lfc|DDL_z.npy` [324]; `embed/gene_vectors.npy` [324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 324 or target_col == 324). Every well: [[MRE11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRE11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
