---
symbol: "CAB39L"
type: "gene"
col: 2255
ensembl_id: "ENSG00000102547"
name: "calcium binding protein 39 like"
location: "13q14.2"
module: 23
arm: "+"
pooled_cpm: 36.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CAB39L

*calcium binding protein 39 like* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.41× (z +25.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.521× (z -13.7, q 8e-40, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.719× (z -9.6, q 8e-20, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A53]] (+0.73, fdr 1e-05), [[ZNF460-AS1]] (+0.72, fdr 3e-05), [[ENTPD3-AS1]] (+0.68, fdr 3e-05); moves opposite to [[FIGNL1]] (-0.60, fdr 2e-05), [[MRPL17]] (-0.56, fdr 4e-04), [[GPRIN1]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.41×** | +25.8 | 0e+00 | 48/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +22.7 | 0e+00 | 47/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.47×** | +19.0 | 0e+00 | 47/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.42×** | +18.6 | 0e+00 | 47/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.56×** | +9.3 | 2e-18 | 37/47 (A-172, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.51×** | +8.7 | 5e-16 | 35/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +8.6 | 5e-16 | 27/47 (LoVo, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.27×** | +7.1 | 1e-10 | 23/48 (HT-29, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Infigratinib (drug)]] 5 µM |  | **1.70×** | +5.8 | 4e-07 | 23/47 (hTERT-HPNE, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 24/48 (AN3 CA, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.6 | 1e-06 | 22/47 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.32×** | +5.5 | 2e-06 | 26/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +4.9 | 4e-05 | 16/48 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.8 | 7e-05 | 18/42 (HS-578T, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.5 | 2e-04 | 18/49 (Hs 766T, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 13/47 (NCI-H1573, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.017 | 12/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.3 | 0.024 | 7/48 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 1.10× | +2.9 | 0.087 | 4/48 (A498, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.096 | 12/48 (RKO, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.521×** | -13.7 | 8e-40 | 41/48 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.524×** | -13.5 | 3e-39 | 43/48 (SW480, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.559×** | -12.2 | 8e-32 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.719×** | -9.6 | 8e-20 | 39/48 (A498, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.635×** | -9.5 | 2e-19 | 36/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -9.2 | 3e-18 | 28/47 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.664×** | -8.6 | 7e-16 | 32/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -7.2 | 4e-11 | 31/48 (RKO, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.716×** | -7.0 | 2e-10 | 25/48 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.597×** | -5.7 | 9e-07 | 23/49 (SW 900, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.778×** | -5.3 | 7e-06 | 21/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -5.2 | 9e-06 | 22/48 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.802×** | -4.6 | 2e-04 | 18/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.675×** | -4.3 | 7e-04 | 17/48 (HCT15, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.821×** | -4.1 | 0.001 | 18/49 (LS 180, A498, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.693×** | -4.0 | 0.002 | 18/48 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.697×** | -3.9 | 0.003 | 13/48 (SHP-77, A498, …) | top dose only | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.850× | -3.4 | 0.020 | 12/47 (A-172, A498, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.023 | 11/49 (A498, C32, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.852× | -3.3 | 0.023 | 15/48 (H4, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.6 | 4 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.377× (z -11.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.474× (z -8.6) |
| [[A-172 (line)]] | wt | 36.5 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +13.0) | — |
| [[H4 (line)]] | wt | 35.3 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.8× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 32.6 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.30× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 24.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.27× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 37.9 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.250× (z -11.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 60.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.7× (z +18.7) | — |
| [[HOP62 (line)]] | alt | 41.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[PANC-1 (line)]] | alt | 39.8 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.20× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 31.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.75× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.261× (z -10.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 29.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.14× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 41.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.330× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 49.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.84× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.21× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 25.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.67× (z +10.0) | — |
| [[J82 (line)]] | alt | 22.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 60.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.78× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.283× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Hs 766T (line)]] | wt | 51.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.277× (z -8.6) |
| [[SNU-1 (line)]] | wt | 65.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0878× (z -8.7) |
| [[C32 (line)]] | wt | 32.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.364× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.40× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +9.6) | — |
| [[RKO (line)]] | wt | 78.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.450× (z -9.1) |
| [[A549 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A53]] | +0.73 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.72 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[ENTPD3-AS1]] | +0.68 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[GPALPP1]] | +0.65 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CASS4]] | +0.65 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[KMT2E-AS1]] | +0.64 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[DNAI4]] | +0.63 | +0.44 / +0.23 | both halves | 6e-04 |  |
| [[RRAGC-DT]] | +0.63 | +0.57 / +0.28 | both halves | 3e-04 |  |
| [[BORCS7-ASMT]] | +0.62 | +0.62 / +0.26 | both halves | 4e-04 |  |
| [[VPS13B-DT]] | +0.62 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[DAZAP2]] | +0.61 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SWT1]] | +0.61 | +0.64 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGNL1]] | -0.60 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[MRPL17]] | -0.56 | -0.42 / -0.26 | both halves | 4e-04 |  |
| [[GPRIN1]] | -0.56 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[SAAL1]] | -0.55 | -0.47 / -0.44 | both halves | 3e-05 | same gene group |
| [[FLNB]] | -0.55 | -0.36 / -0.25 | both halves | 4e-04 |  |
| [[TTLL12]] | -0.55 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[BCKDK]] | -0.54 | -0.50 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[RIOK1]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FIBP]] | -0.54 | -0.49 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-2.6, 22.5); signed map (19.1, -3.7). **Vector** length 99.2, 24.9% of its response variance represented; |z| ≥ 3 in 1,325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.2 | +19.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.5 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.4 | +25.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.5 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -0.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -9.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.9 | -13.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -9.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | calcium binding protein 39 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,308,650-49,444,064 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA103J18.3, FLJ12577, MO2L, MLAA-34 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9S4](https://www.uniprot.org/uniprotkb/Q9H9S4) (Calcium-binding protein 39-like):

> Component of a complex that binds and activates STK11/LKB1. In the complex, required to stabilize the interaction between CAB39/MO25 (CAB39/MO25alpha or CAB39L/MO25beta) and STK11/LKB1 (By similarity).

**Summary**, from NCBI Gene [81617](https://www.ncbi.nlm.nih.gov/gene/81617):

> Predicted to enable protein serine/threonine kinase activator activity. Predicted to be involved in intracellular signal transduction. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20290) · Entrez [81617](https://www.ncbi.nlm.nih.gov/gene/81617) · UniProt [Q9H9S4](https://www.uniprot.org/uniprotkb/Q9H9S4) · Ensembl [ENSG00000102547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102547)

## Data

Gene col 2255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2255); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2255]; `tensor/DDL_lfc|DDL_z.npy` [2255]; `embed/gene_vectors.npy` [2255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2255 or target_col == 2255). Every well: [[CAB39L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAB39L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
