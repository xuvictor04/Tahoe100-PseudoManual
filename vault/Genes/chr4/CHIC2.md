---
symbol: "CHIC2"
type: "gene"
col: 3038
ensembl_id: "ENSG00000109220"
name: "cysteine rich hydrophobic domain 2"
location: "4q12"
module: 147
arm: "+"
pooled_cpm: 100.73
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# CHIC2

*cysteine rich hydrophobic domain 2* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.74× (z +10.0, q 6e-21, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.264× (z -18.6, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.325× (z -8.5, q 2e-15, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELL]] (+0.54, fdr 1e-05), [[ELK3]] (+0.54, fdr 1e-05), [[PAIP2]] (+0.53, fdr 5e-05); moves opposite to [[SLC4A2]] (-0.50, fdr 3e-05), [[ILVBL]] (-0.44, fdr 8e-04, ⚠ one half only (not replicated)), [[PER3]] (-0.43, fdr 3e-05), [[BLTP3A]] (-0.43, fdr 5e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.74×** | +10.0 | 6e-21 | 46/49 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +9.8 | 2e-20 | 45/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +7.4 | 2e-11 | 42/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +7.1 | 3e-10 | 44/48 (SW480, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.8 | 1e-09 | 39/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +6.0 | 2e-07 | 36/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.5 | 6e-04 | 27/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.7 | 0.018 | 18/37 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +3.5 | 0.025 | 25/48 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.029 | 24/47 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.086 | 19/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.086 | 23/48 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Baicalin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.11 | 7/49 (LOX-IMVI, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.264×** | -18.6 | 0e+00 | 42/44 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.371×** | -14.4 | 7e-45 | 46/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.391×** | -13.7 | 3e-40 | 46/49 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.325×** | -8.5 | 2e-15 | 47/48 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.388×** | -7.2 | 6e-11 | 40/48 (NCI-H2347, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.391×** | -7.1 | 9e-11 | 41/48 (NCI-H1792, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.404×** | -6.9 | 4e-10 | 42/48 (H4, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.627×** | -6.8 | 8e-10 | 41/48 (SW 1271, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.411×** | -6.8 | 8e-10 | 40/48 (NCI-H2347, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.707×** | -5.0 | 3e-05 | 30/48 (NCI-H1792, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.750×** | -4.2 | 0.002 | 27/48 (NCI-H1792, RKO, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.756×** | -4.1 | 0.002 | 26/48 (J82, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.830×** | -3.7 | 0.009 | 22/49 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.786×** | -3.4 | 0.031 | 21/48 (NCI-H1573, SHP-77, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.787×** | -3.3 | 0.031 | 24/47 (C32, HCT15, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.680×** | -3.2 | 0.046 | 27/49 (H4, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.794×** | -3.2 | 0.053 | 23/48 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.059 | 22/48 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.839× | -3.0 | 0.067 | 20/49 (RKO, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.816×** | -3.0 | 0.081 | 21/48 (SHP-77, SW 1271, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.814×** | -2.9 | 0.098 | 21/48 (NCI-H23, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 185 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.137× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 141 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0186× (z -33.8) ⚠ toxic; transcription drop · without an alert: [[venetoclax (drug)]] 5 µM 0.128× (z -9.5) |
| [[BT-474 (line)]] | alt | 43.6 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +11.6) | — |
| [[J82 (line)]] | alt | 113 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[venetoclax (drug)]] 5 µM 0.188× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.191× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 88.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -16.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 80.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +10.4) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.3× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 141 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 91.3 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -14.3) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 41.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -8.7) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 110 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.97× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 130 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.156× (z -9.3) |
| [[A498 (line)]] | wt | 70.3 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -13.0) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 175 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 134 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -13.0) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0575× (z -11.3) |
| [[Hs 766T (line)]] | wt | 146 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.50× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0589× (z -24.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 98.2 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 63.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -12.0) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 223 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -12.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.192× (z -8.5) |
| [[SHP-77 (line)]] | alt | 114 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 84.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HCT15 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[OTS514 (drug)]] 5 µM 0.0759× (z -11.0) |
| [[HOP62 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -11.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -9.5) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 78.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 77.9 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.14× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 83.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -16.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -16.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 49.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW48 (line)]] | wt | 84.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -14.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 91.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -10.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -11.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -11.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -9.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 94.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.372× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 99.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 85.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -16.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0894× (z -10.5) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELL]] | +0.54 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ELK3]] | +0.54 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PAIP2]] | +0.53 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[CNST]] | +0.53 | +0.43 / +0.56 | both halves | 4e-05 |  |
| [[LTB4R]] | +0.52 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[TFPI]] | +0.51 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SERINC1]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PTPN12]] | +0.50 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[GLRX]] | +0.49 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[CD59]] | +0.49 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PTPN1]] | +0.49 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[EVI2B]] | +0.49 | +0.48 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A2]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ILVBL]] | -0.44 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PER3]] | -0.43 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[BLTP3A]] | -0.43 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TRIM16]] | -0.42 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SLC25A22]] | -0.42 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[TRIM16L-1]] | -0.41 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF639]] | -0.40 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[NUP62]] | -0.40 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CHIC2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, 9.2); signed map (0.9, 28.6). **Vector** length 109, 38.8% of its response variance represented; |z| ≥ 3 in 1,448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +4.5 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.1 | -14.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.7 | -8.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.7 | -6.9 |
|  | [[EX229 (drug)]] 5 µM |  | -7.1 | -7.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.1 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.5 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich hydrophobic domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:54,009,789-54,064,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BTL |
| Gene groups (HGNC) | Cysteine rich hydrophobic domain family |
| Matched by | ensembl_id |

UniProt [Q9UKJ5](https://www.uniprot.org/uniprotkb/Q9UKJ5) carries no function annotation.

**Summary**, from NCBI Gene [26511](https://www.ncbi.nlm.nih.gov/gene/26511):

> This gene encodes a member of the CHIC family of proteins. The encoded protein contains a cysteine-rich hydrophobic (CHIC) motif, and is localized to vesicular structures and the plasma membrane. This gene is associated with some cases of acute myeloid leukemia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1935) · Entrez [26511](https://www.ncbi.nlm.nih.gov/gene/26511) · UniProt [Q9UKJ5](https://www.uniprot.org/uniprotkb/Q9UKJ5) · Ensembl [ENSG00000109220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109220)

## Data

Gene col 3038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3038); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3038]; `tensor/DDL_lfc|DDL_z.npy` [3038]; `embed/gene_vectors.npy` [3038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3038 or target_col == 3038). Every well: [[CHIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
