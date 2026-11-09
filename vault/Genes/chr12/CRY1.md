---
symbol: "CRY1"
type: "gene"
col: 173
ensembl_id: "ENSG00000008405"
name: "cryptochrome circadian regulator 1"
location: "12q23.3"
module: 89
arm: "+"
pooled_cpm: 123.25
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# CRY1

*cryptochrome circadian regulator 1* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 5.25× (z +17.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM: 0.327× (z -11.9, q 9e-30, down in 46 of 49 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Megestrol (drug)]] 5 µM: 0.489× (z -10.7, q 2e-24, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARIH1]] (+0.60, fdr 1e-05), [[FOSB]] (+0.53, fdr 3e-05), [[LMCD1]] (+0.51, fdr 4e-05); moves opposite to [[ZSCAN25]] (-0.61, fdr 8e-06), [[METTL22]] (-0.54, fdr 7e-05), [[GRSF1]] (-0.53, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 173.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **5.25×** | +17.5 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.05×** | +16.7 | 0e+00 | 44/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.20×** | +15.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **3.16×** | +11.4 | 8e-28 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.97×** | +10.8 | 5e-25 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +10.7 | 1e-24 | 45/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.69×** | +10.1 | 7e-22 | 43/48 (AsPC-1, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.74×** | +8.6 | 6e-16 | 47/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.15×** | +8.1 | 4e-14 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.76×** | +5.9 | 2e-07 | 41/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.85×** | +5.8 | 4e-07 | 38/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 6e-07 | 36/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +5.6 | 9e-07 | 38/48 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.66×** | +5.4 | 3e-06 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.66×** | +5.3 | 3e-06 | 35/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.008 | 31/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.012 | 31/49 (PANC-1, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.32×** | +2.9 | 0.090 | 23/48 (A-427, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 173.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.327×** | -11.9 | 9e-30 | 46/49 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[Megestrol (drug)]] 5 µM |  | **0.489×** | -10.7 | 2e-24 | 45/49 (HS-578T, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -7.3 | 5e-11 | 35/44 (AN3 CA, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.664×** | -6.2 | 9e-08 | 40/48 (AsPC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.653×** | -4.5 | 6e-04 | 32/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.680×** | -3.9 | 0.007 | 30/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.693×** | -3.9 | 0.007 | 29/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -3.6 | 0.019 | 28/48 (NCI-H1573, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.703×** | -3.6 | 0.019 | 27/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.702×** | -3.5 | 0.023 | 32/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.723×** | -3.2 | 0.060 | 26/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.746×** | -3.1 | 0.081 | 25/49 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.748×** | -3.1 | 0.084 | 27/48 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.752×** | -3.1 | 0.092 | 24/48 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **0.755×** | -3.0 | 0.100 | 25/48 (RKO, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 173. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 119 | 15 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 21.8× (z +22.5) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.252× (z -10.1) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 90.1 | 13 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +17.1) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.386× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 132 | 8 (3 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.82× (z +17.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.199× (z -16.5) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.513× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 201 | 6 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +17.8) | [[Selinexor (drug)]] 5 µM 0.297× (z -14.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Megestrol (drug)]] 5 µM 0.439× (z -9.7) |
| [[PANC-1 (line)]] | alt | 119 | 9 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.63× (z +20.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.308× (z -11.6) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.510× (z -9.4) |
| [[SW1417 (line)]] | alt | 152 | 7 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Megestrol (drug)]] 5 µM 0.404× (z -10.7) |
| [[HS-578T (line)]] | alt | 78.3 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +11.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.158× (z -15.0) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.367× (z -11.5) |
| [[A-427 (line)]] | wt | 148 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Megestrol (drug)]] 5 µM 0.541× (z -9.1) |
| [[C32 (line)]] | wt | 63.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 105 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.86× (z +13.3) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.256× (z -9.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 142 | 7 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.28× (z +16.3) | [[Megestrol (drug)]] 5 µM 0.518× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 92.1 | 5 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +18.5) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.201× (z -12.6) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.457× (z -8.7) |
| [[SW48 (line)]] | wt | 91.2 | 5 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 5.45× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.92× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Megestrol (drug)]] 5 µM 0.400× (z -9.1) |
| [[BT-474 (line)]] | alt | 99.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +10.7) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.311× (z -8.6) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 77.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +16.2) | — |
| [[Hs 766T (line)]] | wt | 109 | 5 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.92× (z +12.7) | [[Selinexor (drug)]] 5 µM 0.312× (z -11.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 46.3 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +16.5) | [[Ponatinib (drug)]] 5 µM 0.313× (z -8.8) |
| [[SNU-1 (line)]] | wt | 246 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0945× (z -17.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 144 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.33× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 161 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.41× (z +13.7) | [[Selinexor (drug)]] 5 µM 0.354× (z -9.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 99.5 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +18.1) | [[Megestrol (drug)]] 5 µM 0.456× (z -8.9) |
| [[J82 (line)]] | alt | 163 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.42× (z +15.6) | — |
| [[LOX-IMVI (line)]] | wt | 191 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +11.4) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.253× (z -12.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 82.4 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +19.7) | [[Megestrol (drug)]] 5 µM 0.315× (z -11.0) |
| [[COLO 205 (line)]] | alt | 64.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 169 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 60.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.7) | — |
| [[RPMI-7951 (line)]] | alt | 102 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.235× (z -9.1) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 134 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.39× (z +11.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.182× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 103 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.82× (z +12.0) | [[Selinexor (drug)]] 5 µM 0.304× (z -9.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H2347 (line)]] | alt | 73.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +19.1) | — |
| [[RKO (line)]] | wt | 252 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 211 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.7) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.219× (z -10.7) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.358× (z -10.2) |
| [[A549 (line)]] | wt | 150 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.2) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.205× (z -10.7) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.351× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 53.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 140 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +16.3) | — |
| [[NCI-H2030 (line)]] | alt | 156 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +10.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.344× (z -8.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 42.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 69.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +13.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.284× (z -8.6) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 249 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 106 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.33× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.278× (z -10.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0432× (z -20.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 197 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.166× (z -8.5) |
| [[C-33 A (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 173), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARIH1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FOSB]] | +0.53 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[LMCD1]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[JUN]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DENND4A]] | +0.50 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SIK3]] | +0.49 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CFAP210]] | +0.49 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[CYSTM1]] | +0.48 | +0.50 / +0.40 | both halves | 4e-05 |  |
| [[NR4A3]] | +0.48 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TLE4]] | +0.47 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[EXT1]] | +0.46 | +0.47 / +0.37 | both halves | 7e-05 |  |
| [[NR4A1]] | +0.45 | +0.41 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN25]] | -0.61 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[METTL22]] | -0.54 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[GRSF1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RNF25]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ZNF133]] | -0.51 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[PAAF1]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ABRAXAS2]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[TEFM]] | -0.49 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ALKBH1]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MIX23]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ALKBH3]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZNF225]] | -0.48 | -0.43 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction -0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.5, -6.4); signed map (3.6, 19.6). **Vector** length 98.2, 38.0% of its response variance represented; |z| ≥ 3 in 1,513 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +6.1 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | -3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.6 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | -7.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Pyridoxine (drug)]] 0.05 µM |  | +2.0 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -7.5 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.9 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | +5.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | cryptochrome circadian regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,991,364-107,093,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PHLL1 |
| Gene groups (HGNC) | Flavoproteins; Cryptochrome circadian regulator family |
| Reactome | 9 pathways, smallest: AMP and AMPK regulate the circadian clock; Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16526](https://www.uniprot.org/uniprotkb/Q16526) (Cryptochrome-1):

> Transcriptional repressor which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [1407](https://www.ncbi.nlm.nih.gov/gene/1407):

> This gene encodes a flavin adenine dinucleotide-binding protein that is a key component of the circadian core oscillator complex, which regulates the circadian clock. This gene is upregulated by CLOCK/ARNTL heterodimers but then represses this upregulation in a feedback loop using PER/CRY heterodimers to interact with CLOCK/ARNTL. Polymorphisms in this gene have been associated with altered sleep patterns. The encoded protein is widely conserved across plants and animals. Loss of the related …

**Accessions** — [HGNC:2384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2384) · Entrez [1407](https://www.ncbi.nlm.nih.gov/gene/1407) · UniProt [Q16526](https://www.uniprot.org/uniprotkb/Q16526) · Ensembl [ENSG00000008405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008405)

## Data

Gene col 173: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 173); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 173, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 173]; `tensor/DDL_lfc|DDL_z.npy` [173]; `embed/gene_vectors.npy` [173]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 173 or target_col == 173). Every well: [[CRY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
