---
symbol: "CENPC"
type: "gene"
col: 6966
ensembl_id: "ENSG00000145241"
name: "centromere protein C"
location: "4q13.2"
module: 69
arm: "+"
pooled_cpm: 91.92
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CENPC

*centromere protein C* — 4q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +11.8, q 3e-29, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.465× (z -15.9, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.640× (z -9.6, q 8e-20, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIS18BP1]] (+0.69, fdr 7e-06), [[CEP44]] (+0.66, fdr 7e-06), [[CCDC34]] (+0.62, fdr 1e-05); moves opposite to [[DDX21]] (-0.62, fdr 7e-06), [[PINX1]] (-0.58, fdr 1e-05), [[MORC2]] (-0.54, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +11.8 | 3e-29 | 43/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.8 | 2e-20 | 38/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +7.6 | 8e-12 | 28/48 (RKO, SW1417, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.5 | 9e-12 | 37/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **1.72×** | +6.1 | 1e-07 | 36/47 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 1e-06 | 29/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 6e-06 | 24/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +5.2 | 1e-05 | 25/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +4.9 | 6e-05 | 29/49 (KATO III, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | **1.22×** | +4.1 | 0.002 | 20/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.1 | 0.002 | 14/48 (A498, J82, …) | rises with dose | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.017 | 11/48 (AN3 CA, NCI-H460, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.048 | 17/48 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.056 | 11/49 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.056 | 10/48 (NCI-H1573, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.056 | 15/48 (LOX-IMVI, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6966.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -15.9 | 0e+00 | 40/44 (HCT15, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -15.7 | 0e+00 | 42/49 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.569×** | -12.2 | 8e-32 | 46/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.640×** | -9.6 | 8e-20 | 37/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -9.3 | 1e-18 | 33/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.732×** | -6.7 | 2e-09 | 27/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -6.6 | 2e-09 | 25/48 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -6.0 | 1e-07 | 29/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.8 | 3e-07 | 27/48 (A-172, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.618×** | -5.4 | 3e-06 | 31/48 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.849× | -5.0 | 4e-05 | 22/49 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.801×** | -4.8 | 9e-05 | 27/49 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.656×** | -4.8 | 9e-05 | 27/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.657×** | -4.7 | 9e-05 | 27/48 (Panc 03.27, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.809×** | -4.5 | 2e-04 | 25/48 (H4, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -4.3 | 6e-04 | 27/48 (A498, HCT15, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.696×** | -4.1 | 0.001 | 23/48 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.718×** | -3.7 | 0.005 | 22/48 (SW48, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.845× | -3.6 | 0.007 | 19/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.016 | 21/47 (Panc 03.27, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 144 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.439× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 78.6 | 5 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.20× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.521× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 94.2 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 83.9 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.2) | — |
| [[Panc 03.27 (line)]] | alt | 100 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.7) |
| [[SW480 (line)]] | alt | 111 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.554× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 89.0 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 74.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.96× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +15.0) | — |
| [[C-33 A (line)]] | alt | 77.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -12.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 98.5 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 80.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.326× (z -11.0) |
| [[A498 (line)]] | wt | 87.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 56.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 71.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.411× (z -11.3) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 59.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[J82 (line)]] | alt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -11.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 82.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 88.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -8.8) |
| [[PANC-1 (line)]] | alt | 58.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +13.8) | — |
| [[RKO (line)]] | wt | 130 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.0) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -12.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 102 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -9.9) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 83.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -13.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -27.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.492× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -18.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 96.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0829× (z -9.4) |
| [[SW 900 (line)]] | alt | 86.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 95.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS18BP1]] | +0.69 | +0.69 / +0.70 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 912 |
| [[CEP44]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[CCDC34]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.62 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[HMGB2]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SASS6]] | +0.59 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[ARID4A]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MBIP]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CEP152]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[RPA3]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX21]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[PINX1]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MORC2]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[EIF6]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[DNAJA3]] | -0.51 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PUS1]] | -0.50 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[TTPAL]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[EIF2S1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RRS1]] | -0.49 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[EIF4G3]] | -0.49 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[NCBP2]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-26.4, -52.6); signed map (-46.3, -35.6). **Vector** length 112, 34.5% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.4 | +4.1 |
|  | [[NG25 (drug)]] 5 µM |  | +5.6 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.0 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.4 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.3 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.2 — chr4:67,468,762-67,545,503 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CENP-C, hcp-4, MIF2; previously CENPC1 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03188](https://www.uniprot.org/uniprotkb/Q03188) (Centromere protein C):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres. CENPC recruits DNA methylation and DNMT3B to both centromeric and pericentromeric satellite repeats and regulates the histone code in these regions.

**Summary**, from NCBI Gene [1060](https://www.ncbi.nlm.nih.gov/gene/1060):

> Centromere protein C 1 is a centromere autoantigen and a component of the inner kinetochore plate. The protein is required for maintaining proper kinetochore size and a timely transition to anaphase. A putative pseudogene exists on chromosome 12. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1854) · Entrez [1060](https://www.ncbi.nlm.nih.gov/gene/1060) · UniProt [Q03188](https://www.uniprot.org/uniprotkb/Q03188) · Ensembl [ENSG00000145241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145241)

## Data

Gene col 6966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6966); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6966]; `tensor/DDL_lfc|DDL_z.npy` [6966]; `embed/gene_vectors.npy` [6966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6966 or target_col == 6966). Every well: [[CENPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
