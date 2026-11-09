---
symbol: "PI4KA"
type: "gene"
col: 14296
ensembl_id: "ENSG00000241973"
name: "phosphatidylinositol 4-kinase alpha"
location: "22q11.21"
module: 135
arm: "-"
pooled_cpm: 91.54
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# PI4KA

*phosphatidylinositol 4-kinase alpha* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.30× (z +20.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.554× (z -14.3, q 2e-43, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.693× (z -12.5, q 1e-33, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TECPR1]] (+0.68, fdr 2e-05), [[GGA1]] (+0.64, fdr 2e-04), [[SH3GL1]] (+0.62, fdr 3e-05); moves opposite to [[POLR2M]] (-0.62, fdr 4e-05), [[RNF6]] (-0.61, fdr 3e-05), [[EIF4G2]] (-0.60, fdr 3e-05).
> It sits in the **-** arm of [[Module 135]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +20.1 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +18.8 | 0e+00 | 46/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +16.1 | 0e+00 | 47/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +11.8 | 4e-30 | 36/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +10.4 | 3e-23 | 41/48 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.5 | 2e-15 | 33/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 3e-13 | 39/48 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +7.3 | 3e-11 | 34/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +7.0 | 1e-10 | 36/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.8 | 5e-10 | 37/48 (SHP-77, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.7 | 1e-09 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.20×** | +4.3 | 8e-04 | 22/48 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +4.3 | 8e-04 | 22/48 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.004 | 16/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 17/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 21/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.009 | 12/49 (NCI-H2347, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14296.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.554×** | -14.3 | 2e-43 | 44/49 (SNU-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -14.2 | 3e-43 | 35/43 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.693×** | -12.5 | 1e-33 | 43/48 (A498, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.608×** | -11.1 | 2e-26 | 37/45 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.714×** | -8.1 | 5e-14 | 35/48 (SW1417, SW 1088, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -6.3 | 2e-08 | 4/50 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.789×** | -5.7 | 8e-07 | 25/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.807×** | -5.2 | 2e-05 | 23/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -3.9 | 0.006 | 21/47 (H4, C32, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.805×** | -3.7 | 0.011 | 19/47 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.858× | -3.7 | 0.011 | 22/48 (C32, HS-578T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.882× | -3.6 | 0.016 | 16/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.858× | -3.5 | 0.016 | 19/47 (HepG2/C3A, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.858× | -3.5 | 0.016 | 19/48 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.904× | -3.4 | 0.023 | 3/48 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.821×** | -3.4 | 0.025 | 17/48 (RPMI-7951, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.836× | -3.1 | 0.068 | 13/48 (A-427, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.6 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -13.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 110 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.546× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 139 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.614× (z -9.4) |
| [[SW1417 (line)]] | alt | 155 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -17.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 66.7 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.18× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.557× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 118 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 161 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 110 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -11.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 93.4 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.476× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.626× (z -9.9) |
| [[C-33 A (line)]] | alt | 79.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 101 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.7) | [[Docetaxel (drug)]] 0.05 µM 0.378× (z -10.3) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 121 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.633× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 97.8 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.577× (z -9.2) |
| [[HOP62 (line)]] | alt | 75.1 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.450× (z -9.8) |
| [[KATO III (line)]] | alt | 89.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 78.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 83.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 73.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +17.8) | — |
| [[PANC-1 (line)]] | alt | 87.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 115 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -20.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 108 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.556× (z -10.3) |
| [[SW 1088 (line)]] | alt | 110 | 0 | 4 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0777× (z -10.5) ⚠ transcription drop · without an alert: [[Belumosudil (drug)]] 0.05 µM 0.0666× (z -10.3) |
| [[SW48 (line)]] | wt | 99.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -15.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 75.9 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +9.0) | [[Selinexor (drug)]] 5 µM 0.593× (z -10.4) |
| [[C32 (line)]] | wt | 99.7 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 89.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 73.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +13.9) | — |
| [[A-427 (line)]] | wt | 65.0 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.11× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.576× (z -8.9) |
| [[BT-474 (line)]] | alt | 97.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 58.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 77.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.2) | — |
| [[J82 (line)]] | alt | 71.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 67.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 95.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 77.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.434× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 84.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -12.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -10.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 112 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 81.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.400× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 141 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 102 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.03× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 98.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0736× (z -12.6) |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR1]] | +0.68 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GGA1]] | +0.64 | +0.57 / +0.32 | both halves | 2e-04 |  |
| [[SH3GL1]] | +0.62 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[ARID3B]] | +0.60 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[PIBF1]] | +0.59 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[EIF3K]] | +0.58 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[NAA10]] ⚠ | +0.58 | +0.27 / +0.43 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PI4KAP1]] | +0.57 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[FAAP20]] | +0.57 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[ANAPC11]] | +0.57 | +0.49 / +0.25 | both halves | 4e-04 |  |
| [[ATP5F1D]] ⚠ | +0.56 | +0.28 / +0.40 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ARPC1B]] | +0.55 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[SPATA2L]] | +0.55 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ETHE1]] | +0.55 | +0.27 / +0.50 | both halves | 3e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2M]] | -0.62 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RNF6]] | -0.61 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.60 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TDP2]] | -0.60 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[OTUD4]] | -0.59 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[BAG2]] | -0.58 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ZXDA]] | -0.58 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ZXDB]] | -0.57 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[C17orf75]] | -0.57 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ZNF514]] | -0.57 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[FAIM]] | -0.56 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[FKBP4]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-12.5, 13.3); signed map (-33.4, 1.8). **Vector** length 98.8, 28.8% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +18.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +20.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +16.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -13.2 | -12.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.4 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 4-kinase alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,707,691-20,859,417 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PI4K-ALPHA, pi4K230; previously PIK4CA |
| Gene groups (HGNC) | Armadillo like helical domain containing; PI4KA lipid kinase complex; Phosphatidylinositol 4-kinase type 3 family |
| Reactome | 5 pathways, smallest: Synthesis of PIPs at the ER membrane; Synthesis of PIPs at the Golgi membrane; PI Metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P42356](https://www.uniprot.org/uniprotkb/P42356) (Phosphatidylinositol 4-kinase alpha):

> Acts on phosphatidylinositol (PtdIns) in the first committed step in the production of the second messenger inositol-1,4,5,-trisphosphate.

**Summary**, from NCBI Gene [5297](https://www.ncbi.nlm.nih.gov/gene/5297):

> This gene encodes a phosphatidylinositol (PI) 4-kinase which catalyzes the first committed step in the biosynthesis of phosphatidylinositol 4,5-bisphosphate. The mammalian PI 4-kinases have been classified into two types, II and III, based on their molecular mass, and modulation by detergent and adenosine. The protein encoded by this gene is a type III enzyme that is not inhibited by adenosine. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by …

**Accessions** — [HGNC:8983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8983) · Entrez [5297](https://www.ncbi.nlm.nih.gov/gene/5297) · UniProt [P42356](https://www.uniprot.org/uniprotkb/P42356) · Ensembl [ENSG00000241973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241973)

## Data

Gene col 14296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14296); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14296]; `tensor/DDL_lfc|DDL_z.npy` [14296]; `embed/gene_vectors.npy` [14296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14296 or target_col == 14296). Every well: [[PI4KA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4KA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
