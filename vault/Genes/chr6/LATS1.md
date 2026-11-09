---
symbol: "LATS1"
type: "gene"
col: 5160
ensembl_id: "ENSG00000131023"
name: "large tumor suppressor kinase 1"
location: "6q25.1"
module: 68
arm: "+"
pooled_cpm: 91.39
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# LATS1

*large tumor suppressor kinase 1* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +26.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.508× (z -17.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFYC]] (+0.78, fdr 7e-06), [[WDR33]] (+0.77, fdr 7e-06), [[RNF146]] (+0.76, fdr 1e-05); moves opposite to [[TPST2]] (-0.70, fdr 7e-06), [[MBOAT2]] (-0.67, fdr 2e-05), [[PIP4K2A]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HNF1A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +26.2 | 0e+00 | 47/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +16.9 | 0e+00 | 47/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +15.5 | 0e+00 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +12.8 | 2e-35 | 43/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +12.1 | 9e-32 | 45/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +11.8 | 4e-30 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +11.0 | 2e-26 | 41/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +10.6 | 3e-24 | 44/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +9.6 | 7e-20 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +8.0 | 7e-14 | 37/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +7.3 | 2e-11 | 32/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.20× | +6.4 | 7e-09 | 24/48 (PANC-1, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +5.3 | 5e-06 | 25/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +5.3 | 5e-06 | 27/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.8 | 6e-05 | 26/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -17.0 | 0e+00 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.527×** | -16.1 | 0e+00 | 47/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.551×** | -15.0 | 0e+00 | 46/49 (LS 180, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.593×** | -13.1 | 3e-37 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -12.4 | 3e-33 | 37/44 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.667×** | -9.4 | 5e-19 | 31/45 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -9.4 | 5e-19 | 36/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -8.9 | 3e-17 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.770×** | -6.6 | 3e-09 | 35/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -5.6 | 2e-06 | 26/48 (SNU-423, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.826×** | -4.8 | 8e-05 | 22/49 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.730×** | -3.5 | 0.022 | 16/49 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | 0.886× | -3.0 | 0.10 | 10/48 (CFPAC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 149 | 8 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 111 | 7 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 77.0 | 6 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -13.1) |
| [[LoVo (line)]] | wt | 94.9 | 8 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +18.5) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -9.8) |
| [[PANC-1 (line)]] | alt | 110 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +29.6) | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.515× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 115 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.476× (z -11.7) |
| [[LS 180 (line)]] | wt | 83.8 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 137 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.478× (z -10.2) |
| [[HOP62 (line)]] | alt | 89.4 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.6) | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 62.2 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.469× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 201 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.579× (z -8.7) |
| [[HS-578T (line)]] | alt | 84.3 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.9) | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 98.7 | 4 | 2 | [[Harringtonine (drug)]] 5 µM 2.40× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 102 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.451× (z -9.6) |
| [[SW1417 (line)]] | alt | 107 | 2 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.357× (z -14.5) |
| [[A549 (line)]] | wt | 62.9 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 66.7 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.406× (z -11.8) |
| [[SW48 (line)]] | wt | 93.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.9) | — |
| [[HepG2_C3A (line)]] | wt | 127 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.421× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 81.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -8.8) |
| [[RKO (line)]] | wt | 109 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -14.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 76.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 53.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.378× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 54.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.9) |
| [[HT-29 (line)]] | alt | 85.4 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.488× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 84.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -22.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 59.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 155 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0970× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 64.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 77.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -13.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +10.8) | — |
| [[KATO III (line)]] | alt | 27.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 85.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 85.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.0) | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -23.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 71.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 83.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.4) | — |
| [[J82 (line)]] | alt | 77.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 64.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 92.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.444× (z -9.1) |
| [[H4 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYC]] | +0.78 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[WDR33]] | +0.77 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[RNF146]] | +0.76 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[POLR3C]] | +0.76 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[INO80D]] | +0.76 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.74 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[UQCRFS1]] | +0.74 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZFY]] | +0.73 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.73 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.73 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RC3H2]] | +0.73 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[ZNF253]] | +0.72 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.70 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[MBOAT2]] | -0.67 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PIP4K2A]] | -0.65 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.65 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[TMEM41B]] | -0.64 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.63 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1A]] | B | HNF1A activity lowers LATS1's level | lines that do not express HNF1A (30) vs lines expressing it (20) | 1.11× higher at baseline in the lines without HNF1A | 0.083 | ⚠ within organs, on part of the lines; also absent: HNF1A-AS1, GPX2, HNF4A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises LATS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises LATS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (0.8, 10.1); signed map (21.6, -18.8). **Vector** length 101, 30.3% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +8.7 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +12.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +8.1 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +16.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.0 | -13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.4 | -16.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -17.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.0 | -8.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | large tumor suppressor kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,658,153-149,718,105 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WARTS |
| Gene groups (HGNC) | Large tumor suppressor kinase family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [O95835](https://www.uniprot.org/uniprotkb/O95835) (Serine/threonine-protein kinase LATS1):

> Negative regulator of YAP1 in the Hippo signaling pathway that plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Phosphorylation of YAP1 …

**Summary**, from NCBI Gene [9113](https://www.ncbi.nlm.nih.gov/gene/9113):

> The protein encoded by this gene is a putative serine/threonine kinase that localizes to the mitotic apparatus and complexes with cell cycle controller CDC2 kinase in early mitosis. The protein is phosphorylated in a cell-cycle dependent manner, with late prophase phosphorylation remaining through metaphase. The N-terminal region of the protein binds CDC2 to form a complex showing reduced H1 histone kinase activity, indicating a role as a negative regulator of CDC2/cyclin A. In addition, the …

**Accessions** — [HGNC:6514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6514) · Entrez [9113](https://www.ncbi.nlm.nih.gov/gene/9113) · UniProt [O95835](https://www.uniprot.org/uniprotkb/O95835) · Ensembl [ENSG00000131023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131023)

## Data

Gene col 5160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5160); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5160]; `tensor/DDL_lfc|DDL_z.npy` [5160]; `embed/gene_vectors.npy` [5160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5160 or target_col == 5160). Every well: [[LATS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LATS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
