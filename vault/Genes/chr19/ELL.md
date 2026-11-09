---
symbol: "ELL"
type: "gene"
col: 2639
ensembl_id: "ENSG00000105656"
name: "elongation factor for RNA polymerase II"
location: "19p13.11"
module: 25
arm: "-"
pooled_cpm: 69.27
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 30
n_dd_up_clean: 13
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ELL

*elongation factor for RNA polymerase II* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.09× (z +11.8, q 2e-29, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.05× (z +11.6, q 2e-28, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.335× (z -17.5, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.655× (z -6.5, q 2e-08, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R13L]] (+0.66, fdr 7e-06), [[RABGEF1]] (+0.64, fdr 7e-06), [[SH3GL1]] (+0.64, fdr 7e-06); moves opposite to [[MANEA]] (-0.67, fdr 1e-05), [[MBTPS2]] (-0.65, fdr 1e-05), [[HACD2]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +11.8 | 2e-29 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +11.6 | 2e-28 | 47/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.9 | 8e-17 | 37/49 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +8.6 | 8e-16 | 43/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +8.0 | 1e-13 | 38/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +7.9 | 4e-13 | 40/48 (RKO, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +7.7 | 1e-12 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.4 | 6e-06 | 29/48 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.31×** | +4.3 | 9e-04 | 25/48 (PANC-1, A-427, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.002 | 25/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 23/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.008 | 25/49 (PANC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.031 | 19/48 (CFPAC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +3.3 | 0.039 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.040 | 20/49 (CFPAC-1, RKO, …) | rises with dose | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.075 | 13/49 (SK-MEL-2, AN3 CA, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.097 | 19/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.335×** | -17.5 | 0e+00 | 44/49 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -14.6 | 1e-45 | 38/43 (A549, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.655×** | -6.5 | 2e-08 | 36/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.679×** | -5.9 | 4e-07 | 38/47 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -5.9 | 4e-07 | 32/47 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.690×** | -5.9 | 4e-07 | 36/48 (J82, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -5.6 | 2e-06 | 32/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.779×** | -5.2 | 1e-05 | 29/48 (NCI-H1792, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -5.0 | 4e-05 | 24/45 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.725×** | -4.7 | 1e-04 | 32/48 (HepG2/C3A, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.002 | 26/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.771×** | -4.1 | 0.002 | 27/49 (A-172, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.828×** | -4.1 | 0.002 | 21/48 (SHP-77, AsPC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.772×** | -4.1 | 0.002 | 27/49 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.774×** | -4.0 | 0.002 | 26/48 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.777×** | -4.0 | 0.002 | 23/48 (LOX-IMVI, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.805×** | -3.9 | 0.002 | 26/48 (A549, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.779×** | -3.9 | 0.002 | 28/47 (A549, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.003 | 24/50 (NCI-H596, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.782×** | -3.9 | 0.003 | 20/48 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.635×** | -3.8 | 0.004 | 26/48 (AsPC-1, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.1 | 7 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.38× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.30× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.9 | 6 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.84× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 82.1 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -19.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 111 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.24× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 82.4 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 94.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -19.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 41.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.25× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 86.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 41.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 56.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 66.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -17.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 98.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -21.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 85.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -14.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 76.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0415× (z -24.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 68.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 78.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -18.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -11.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -17.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 57.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 72.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 95.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 69.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -15.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 59.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 58.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +9.6) | — |
| [[A-427 (line)]] | wt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0797× (z -19.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 32.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.16× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 102 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.68× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 83.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R13L]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SH3GL1]] | +0.64 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[SPACDR]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TRPT1]] | +0.59 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[FAAP20]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NUDT22]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.58 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[MEIS3]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NOSIP]] | +0.57 | +0.43 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANEA]] | -0.67 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[MBTPS2]] | -0.65 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[HACD2]] | -0.64 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.62 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[DLD]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[OCRL]] | -0.60 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[EXOSC10]] | -0.60 | -0.43 / -0.58 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[ZNF280D]] | -0.59 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[AIFM1]] | -0.59 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[PROSER1]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[ATP5F1A]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[AGPS]] | -0.58 | -0.40 / -0.63 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.8, -17.3); signed map (-17.6, 17.2). **Vector** length 105, 33.3% of its response variance represented; |z| ≥ 3 in 1,284 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.7 | +8.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +5.3 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | -0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.5 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.1 | +0.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.9 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | elongation factor for RNA polymerase II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,442,663-18,522,116 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Men, ELL1, PPP1R68; previously C19orf17 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Super elongation complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 26 pathways, smallest: Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery; HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [P55199](https://www.uniprot.org/uniprotkb/P55199) (RNA polymerase II elongation factor ELL):

> Elongation factor component of the super elongation complex (SEC), a complex required to increase the catalytic rate of RNA polymerase II transcription by suppressing transient pausing by the polymerase at multiple sites along the DNA. Elongation factor component of the little elongation complex (LEC), a complex required to regulate small nuclear RNA (snRNA) gene transcription by RNA polymerase II and III. Specifically required for stimulating the elongation step of RNA polymerase II- and …

**Summary**, from NCBI Gene [8178](https://www.ncbi.nlm.nih.gov/gene/8178):

> Enables phosphatase binding activity. Involved in positive regulation of DNA-templated transcription and snRNA transcription. Located in euchromatin and nuclear ribonucleoprotein granule. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23114) · Entrez [8178](https://www.ncbi.nlm.nih.gov/gene/8178) · UniProt [P55199](https://www.uniprot.org/uniprotkb/P55199) · Ensembl [ENSG00000105656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105656)

## Data

Gene col 2639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2639); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2639]; `tensor/DDL_lfc|DDL_z.npy` [2639]; `embed/gene_vectors.npy` [2639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2639 or target_col == 2639). Every well: [[ELL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
