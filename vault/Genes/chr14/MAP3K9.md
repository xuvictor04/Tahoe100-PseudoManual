---
symbol: "MAP3K9"
type: "gene"
col: 109
ensembl_id: "ENSG00000006432"
name: "mitogen-activated protein kinase kinase kinase 9"
location: "14q24.2"
module: 3
arm: "+"
pooled_cpm: 58.16
n_lines_expressing: 42
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MAP3K9

*mitogen-activated protein kinase kinase kinase 9* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.02× (z +13.8, q 2e-40, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.384× (z -18.7, q 0e+00, down in 32 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.604× (z -9.9, q 8e-21, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM62]] (+0.70, fdr 7e-06), [[YIF1B]] (+0.68, fdr 1e-05), [[TMEM184B]] (+0.66, fdr 1e-05); moves opposite to [[BCLAF1]] (-0.66, fdr 1e-05), [[GABPB2]] (-0.64, fdr 2e-04), [[MCCC2]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP3K9-DT]] → it (grade B ⚠); 9 go from it, the strongest it → [[F11R]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +13.8 | 2e-40 | 37/40 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +11.7 | 2e-29 | 33/40 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +10.1 | 1e-21 | 35/40 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +9.8 | 1e-20 | 31/40 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +8.7 | 5e-16 | 29/40 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +8.5 | 2e-15 | 24/40 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +6.8 | 6e-10 | 19/40 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.7 | 2e-09 | 22/40 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +5.7 | 8e-07 | 21/41 (NCI-H2030, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.6 | 1e-06 | 21/40 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.3 | 5e-06 | 19/40 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +5.3 | 5e-06 | 23/41 (SW480, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 2e-05 | 21/40 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.2 | 9e-04 | 9/41 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.2 | 9e-04 | 13/40 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.2 | 9e-04 | 16/40 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.004 | 19/40 (SW480, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.004 | 9/40 (A498, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.384×** | -18.7 | 0e+00 | 32/39 (NCI-H1792, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.395×** | -16.8 | 0e+00 | 33/36 (HepG2/C3A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -14.5 | 1e-45 | 30/34 (NCI-H1573, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.604×** | -9.9 | 8e-21 | 27/40 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.706×** | -9.6 | 6e-20 | 25/40 (NCI-H2347, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.734×** | -6.0 | 1e-07 | 24/40 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -5.8 | 6e-07 | 22/40 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.750×** | -5.4 | 5e-06 | 20/40 (J82, SHP-77, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.9 | 6e-05 | 1/41 (NCI-H1792) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.849× | -4.5 | 4e-04 | 17/40 (NCI-H1792, NCI-H2347, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -4.4 | 6e-04 | 14/40 (SW 900, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -4.2 | 0.001 | 16/40 (LoVo, NCI-H2347, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.808×** | -4.0 | 0.003 | 17/40 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.865× | -4.0 | 0.003 | 9/40 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.830×** | -3.6 | 0.011 | 14/40 (SW1417, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.839× | -3.4 | 0.022 | 12/41 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.023 | 13/41 (A549, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.842× | -3.4 | 0.023 | 12/40 (A549, HT-29, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.885× | -3.4 | 0.023 | 6/40 (A549, A498, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.023 | 11/39 (C32, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.023 | 9/40 (HOP62, J82, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.851× | -3.1 | 0.043 | 11/40 (A549, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 41.3 | 0 | 14 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.130× (z -14.5) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.168× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 266 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -21.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -14.8) |
| [[SW 900 (line)]] | alt | 188 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0859× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.378× (z -12.7) |
| [[SW480 (line)]] | alt | 69.7 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.490× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 65.8 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -13.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 33.6 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 56.3 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.50× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -14.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 107 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.529× (z -9.0) |
| [[SHP-77 (line)]] | alt | 87.8 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -23.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 94.3 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -15.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 58.9 | 2 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.15× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -12.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.6 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.92× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 65.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 44.1 | 3 | 1 | [[Belinostat (drug)]] 5 µM 3.40× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -9.0) |
| [[A498 (line)]] | wt | 46.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 40.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -10.6) |
| [[BT-474 (line)]] | alt | 63.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.391× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 53.0 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -14.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 44.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 42.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 55.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 63.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0552× (z -21.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 43.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.232× (z -9.0) |
| [[AN3 CA (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -14.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 82.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM62]] | +0.70 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.68 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.66 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MPG]] | +0.66 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PEDS1]] | +0.65 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[KYAT1]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.65 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SDHAP2]] | +0.64 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[ZFYVE28]] | +0.64 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[UBE2O]] | +0.64 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[GMCL1]] | +0.63 | +0.61 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCLAF1]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.64 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[MCCC2]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[TRIM44]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[KICS2]] | -0.61 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ERMAP]] | -0.61 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[ZXDA]] | -0.61 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[RIPK2-DT]] | -0.60 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[TASOR]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RFX3-DT]] | -0.59 | -0.61 / -0.21 | both halves | 7e-04 |  |
| [[USP40]] | -0.59 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[WARS2-AS1]] | -0.59 | -0.61 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K9-DT]] | B | MAP3K9-DT activity raises MAP3K9's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 3.25× lower at baseline in the lines without MAP3K9-DT | 0.002 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[TTC9]] | B | TTC9 activity raises MAP3K9's level | lines that do not express TTC9 (23) vs lines expressing it (27) | 2.48× lower at baseline in the lines without TTC9 | 0.030 | ⚠ within organs, on part of the lines; also absent: ITGB4, AREG, SPNS2 |
| [[F11R]] | B | F11R activity raises MAP3K9's level | lines that do not express F11R (10) vs lines expressing it (40) | 2.59× lower at baseline in the lines without F11R | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000287306, LONRF3, TUBA4A |
| [[PRKCZ]] | C | PRKCZ activity raises MAP3K9's level | lines that do not express PRKCZ (10) vs lines expressing it (40) | 4.13× lower at baseline in the lines without PRKCZ | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000258593, AP1G2, CHMP4C; co-absent with the target; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11R]] | B | MAP3K9 activity raises F11R's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 4.17× lower at baseline in the lines without MAP3K9 | 0.023 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[MAP3K9-DT]] | B | MAP3K9 activity raises MAP3K9-DT's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 2.85× lower at baseline in the lines without MAP3K9 | 0.024 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[KLHL25]] | B | MAP3K9 activity raises KLHL25's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without MAP3K9 | 0.031 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[CARHSP1]] | B | MAP3K9 activity raises CARHSP1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without MAP3K9 | 0.055 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[SERINC2]] | B | MAP3K9 activity raises SERINC2's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 2.91× lower at baseline in the lines without MAP3K9 | 0.057 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[RPS6KA1]] | B | MAP3K9 activity raises RPS6KA1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.96× lower at baseline in the lines without MAP3K9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[CELSR1]] | B | MAP3K9 activity raises CELSR1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without MAP3K9 | 0.075 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[PPFIA1]] | B | MAP3K9 activity raises PPFIA1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without MAP3K9 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |
| [[PRKCZ]] | C | MAP3K9 activity raises PRKCZ's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 4.06× lower at baseline in the lines without MAP3K9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.9, 0.9); signed map (-32.0, 16.0). **Vector** length 117, 33.0% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.2 | +9.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.3 | +13.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +10.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.0 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.5 | +2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +3.8 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -16.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.8 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,722,526-70,809,534 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRKE1, MEKK9; previously MLK1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P80192](https://www.uniprot.org/uniprotkb/P80192) (Mitogen-activated protein kinase kinase kinase 9):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. Plays an important role in the cascades of cellular responses evoked by changes in the environment. Once activated, acts as an upstream activator of the MKK/JNK signal transduction cascade through the phosphorylation of MAP2K4/MKK4 and MAP2K7/MKK7 which in turn activate the JNKs. The MKK/JNK signaling pathway regulates stress response via activator protein-1 (JUN) and GATA4 transcription …

**Summary**, from NCBI Gene [4293](https://www.ncbi.nlm.nih.gov/gene/4293):

> Enables molecular function activator activity and protein serine/threonine kinase activity. Involved in protein autophosphorylation. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6861) · Entrez [4293](https://www.ncbi.nlm.nih.gov/gene/4293) · UniProt [P80192](https://www.uniprot.org/uniprotkb/P80192) · Ensembl [ENSG00000006432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006432)

## Data

Gene col 109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 109); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 109]; `tensor/DDL_lfc|DDL_z.npy` [109]; `embed/gene_vectors.npy` [109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 109 or target_col == 109). Every well: [[MAP3K9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
