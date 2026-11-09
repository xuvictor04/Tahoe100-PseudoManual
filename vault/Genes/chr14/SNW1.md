---
symbol: "SNW1"
type: "gene"
col: 1999
ensembl_id: "ENSG00000100603"
name: "SNW domain containing 1"
location: "14q24.3"
module: 12
arm: "+"
pooled_cpm: 91.17
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SNW1

*SNW domain containing 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +19.6, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.24× (z +17.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.673× (z -8.6, q 4e-15, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.87, fdr 7e-06), [[C1orf131]] (+0.83, fdr 7e-06), [[SLC4A1AP]] (+0.81, fdr 7e-06); moves opposite to [[AKT1]] (-0.67, fdr 7e-06), [[COLGALT1]] (-0.66, fdr 1e-05), [[SELENON]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.89×** | +19.6 | 0e+00 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +17.6 | 0e+00 | 47/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.54×** | +17.2 | 0e+00 | 47/49 (NCI-H1573, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +14.3 | 3e-44 | 46/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.96×** | +14.1 | 5e-43 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.67×** | +11.2 | 5e-27 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +10.1 | 5e-22 | 40/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +8.9 | 5e-17 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +8.6 | 6e-16 | 44/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +8.3 | 6e-15 | 43/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +7.9 | 2e-13 | 36/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.8 | 3e-07 | 36/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.31×** | +5.6 | 9e-07 | 31/47 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.28×** | +5.4 | 2e-06 | 35/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +5.4 | 3e-06 | 27/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.5 | 0.014 | 16/48 (NCI-H2030, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.059 | 5/49 (RKO, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.064 | 11/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.673×** | -8.6 | 4e-15 | 41/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.712×** | -7.4 | 5e-11 | 40/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.738×** | -6.6 | 7e-09 | 35/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -6.2 | 1e-07 | 28/44 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.781×** | -5.4 | 9e-06 | 34/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -5.2 | 2e-05 | 20/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -3.6 | 0.022 | 22/49 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.040 | 21/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.906× | -3.0 | 0.15 | 2/48 (HEC-1-A, HCT15) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.870× | -3.0 | 0.15 | 14/48 (C32, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 90.5 | 11 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +24.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -32.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 73.9 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +24.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +19.2) | — |
| [[A549 (line)]] | wt | 100 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +19.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 167 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +19.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 79.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 123 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +12.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.564× (z -9.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 83.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +16.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +14.8) | — |
| [[LoVo (line)]] | wt | 75.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.61× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 94.5 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +17.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 114 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 79.6 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +20.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.518× (z -8.9) |
| [[COLO 205 (line)]] | alt | 85.3 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.8× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 74.9 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 75.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.03× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 103 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -12.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 108 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.37× (z +14.1) | — |
| [[BT-474 (line)]] | alt | 83.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.52× (z +8.8) | — |
| [[C32 (line)]] | wt | 75.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 128 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.63× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 83.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 85.0 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.85× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.475× (z -9.3) |
| [[SNU-1 (line)]] | wt | 83.2 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.38× (z +10.2) | — |
| [[A-427 (line)]] | wt | 81.8 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.56× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 57.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +10.8) | — |
| [[RKO (line)]] | wt | 103 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.16× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 91.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 89.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.77× (z +10.3) | — |
| [[H4 (line)]] | wt | 88.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 80.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.71× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 64.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.35× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.10× (z +11.5) | [[Lonafarnib (drug)]] 5 µM 0.112× (z -15.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 85.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +8.5) | — |
| [[A-172 (line)]] | wt | 52.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 86.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -16.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.476× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 87.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 87.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.4) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW48 (line)]] | wt | 134 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.53× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.87 | +0.87 / +0.82 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.83 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[SLC4A1AP]] | +0.81 | +0.87 / +0.72 | both halves | 7e-06 |  |
| [[PHAX]] | +0.80 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.79 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[PPIG]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 890 |
| [[ZNF830]] | +0.77 | +0.79 / +0.66 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 978 |
| [[PPCS]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ANKRD49]] | +0.75 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 | STRING 442 |
| [[COIL]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.67 | -0.64 / -0.60 | both halves | 7e-06 | pathway: Regulation of beta-cell development |
| [[COLGALT1]] | -0.66 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[SELENON]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SNW1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.4, 2.9); signed map (1.1, -16.8). **Vector** length 101, 30.7% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.9 | +11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +14.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.3 | +19.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.5 | +14.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +7.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.5 | +3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.7 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.5 | +8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -6.6 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | SNW domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,717,599-77,761,207 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NCoA-62, SKIP, Prp45, PRPF45, Bx42, SKIP1, FUN20; previously SKIIP |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 37 pathways, smallest: RUNX3 regulates NOTCH signaling; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells; NOTCH4 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13573](https://www.uniprot.org/uniprotkb/Q13573) (SNW domain-containing protein 1):

> Involved in pre-mRNA splicing as component of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). Required for the specific splicing of CDKN1A pre-mRNA; the function probably involves the recruitment of U2AF2 to the mRNA. May recruit PPIL1 to the spliceosome. May be involved in cyclin-D1/CCND1 mRNA stability through the SNARP complex which associates with both the 3'end of the CCND1 gene and its mRNA. Involved in …

**Summary**, from NCBI Gene [22938](https://www.ncbi.nlm.nih.gov/gene/22938):

> This gene, a member of the SNW gene family, encodes a coactivator that enhances transcription from some Pol II promoters. This coactivator can bind to the ligand-binding domain of the vitamin D receptor and to retinoid receptors to enhance vitamin D-, retinoic acid-, estrogen-, and glucocorticoid-mediated gene expression. It can also function as a splicing factor by interacting with poly(A)-binding protein 2 to directly control the expression of muscle-specific genes at the transcriptional …

**Accessions** — [HGNC:16696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16696) · Entrez [22938](https://www.ncbi.nlm.nih.gov/gene/22938) · UniProt [Q13573](https://www.uniprot.org/uniprotkb/Q13573) · Ensembl [ENSG00000100603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100603)

## Data

Gene col 1999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1999); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1999]; `tensor/DDL_lfc|DDL_z.npy` [1999]; `embed/gene_vectors.npy` [1999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1999 or target_col == 1999). Every well: [[SNW1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNW1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
