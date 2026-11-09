---
symbol: "ZFP91"
type: "gene"
col: 11842
ensembl_id: "ENSG00000186660"
name: "ZFP91 zinc finger protein, atypical E3 ubiquitin ligase"
location: "11q12.1"
module: 194
arm: "+"
pooled_cpm: 138.54
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# ZFP91

*ZFP91 zinc finger protein, atypical E3 ubiquitin ligase* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +23.3, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.64× (z +16.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.453× (z -19.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TASOR]] (+0.75, fdr 7e-06), [[ZC3H4]] (+0.72, fdr 1e-05), [[ST7L]] (+0.71, fdr 4e-05); moves opposite to [[MPG]] (-0.69, fdr 3e-05), [[CARHSP1]] (-0.68, fdr 1e-05), [[AFMID]] (-0.67, fdr 9e-06).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.93×** | +23.3 | 0e+00 | 48/48 (A549, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.26×** | +19.6 | 0e+00 | 47/48 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.64×** | +16.9 | 0e+00 | 48/49 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +15.6 | 0e+00 | 45/47 (NCI-H2030, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.81×** | +14.8 | 0e+00 | 46/49 (J82, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.79×** | +14.5 | 1e-45 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.01×** | +14.4 | 6e-45 | 45/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +14.1 | 5e-43 | 47/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.62×** | +11.5 | 5e-29 | 33/44 (NCI-H23, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.58×** | +11.4 | 2e-28 | 43/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +11.0 | 2e-26 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +10.9 | 7e-26 | 36/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.54×** | +10.0 | 9e-22 | 38/45 (J82, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +9.7 | 7e-21 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +7.4 | 7e-12 | 40/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +5.7 | 3e-07 | 26/48 (SW480, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.7 | 3e-07 | 26/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +5.2 | 4e-06 | 36/48 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +4.8 | 4e-05 | 22/48 (C32, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +4.5 | 1e-04 | 27/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.002 | 24/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.008 | 17/48 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.019 | 20/49 (C32, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.030 | 13/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.09× | +3.1 | 0.030 | 3/49 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.030 | 14/48 (CFPAC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.453×** | -19.8 | 0e+00 | 47/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.501×** | -17.3 | 0e+00 | 47/48 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.524×** | -16.2 | 0e+00 | 47/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.675×** | -9.9 | 9e-21 | 45/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -7.2 | 8e-11 | 30/48 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.626×** | -6.1 | 7e-08 | 38/49 (PANC-1, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.806×** | -5.4 | 4e-06 | 33/49 (CHP-212, C32, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.808×** | -5.4 | 6e-06 | 25/48 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.899× | -3.7 | 0.013 | 6/48 (NCI-H2030, NCI-H23, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.834× | -3.3 | 0.064 | 11/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.878× | -3.0 | 0.12 | 16/50 (A-427, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.882× | -3.0 | 0.13 | 12/49 (Hs 766T, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 109 | 16 (10 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +25.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +19.6) | [[Panobinostat (drug)]] 5 µM 0.426× (z -14.0) |
| [[SW480 (line)]] | alt | 131 | 16 (11 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 5.34× (z +18.3) | [[Panobinostat (drug)]] 5 µM 0.531× (z -13.2) |
| [[HOP62 (line)]] | alt | 125 | 12 (9 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.514× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 279 | 11 (7 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.68× (z +16.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.374× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 127 | 10 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.52× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.403× (z -13.0) |
| [[PANC-1 (line)]] | alt | 184 | 9 (6 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +22.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.358× (z -18.2) |
| [[LoVo (line)]] | wt | 114 | 10 (8 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +14.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.49× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.515× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 164 | 9 (6 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.01× (z +15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.96× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.428× (z -12.1) |
| [[KATO III (line)]] | alt | 152 | 8 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.14× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.426× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 101 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.59× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 154 | 7 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.60× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.439× (z -10.9) |
| [[HS-578T (line)]] | alt | 149 | 9 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +26.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.536× (z -8.6) |
| [[J82 (line)]] | alt | 184 | 7 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.478× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 151 | 7 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.04× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.428× (z -13.1) |
| [[C32 (line)]] | wt | 155 | 7 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +24.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.64× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.427× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 114 | 7 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.71× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.456× (z -12.6) |
| [[HT-29 (line)]] | alt | 189 | 5 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.76× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.380× (z -15.1) |
| [[LS 180 (line)]] | wt | 146 | 7 (5 ⚠) | 2 | [[PH-797804 (drug)]] 5 µM 6.49× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.437× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 150 | 8 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.48× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.481× (z -10.5) |
| [[SNU-423 (line)]] | alt | 151 | 7 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +25.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -9.4) |
| [[A549 (line)]] | wt | 122 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +29.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +19.3) | [[Belinostat (drug)]] 5 µM 0.549× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 161 | 5 (3 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 2.47× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.33× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.349× (z -14.8) |
| [[SW1417 (line)]] | alt | 168 | 4 (2 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 3.89× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.386× (z -16.0) |
| [[A-172 (line)]] | wt | 114 | 5 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.459× (z -10.2) |
| [[A-427 (line)]] | wt | 179 | 4 (2 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 4.80× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.446× (z -11.9) |
| [[A498 (line)]] | wt | 111 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +22.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.472× (z -10.5) |
| [[COLO 205 (line)]] | alt | 126 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.38× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 109 | 5 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.01× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.507× (z -8.9) |
| [[SW 900 (line)]] | alt | 165 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.385× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 139 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 147 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.8) ⚠ cell-cycle shift, explains ~37% of this change | [[Belinostat (drug)]] 5 µM 0.378× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 134 | 4 (3 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.99× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.444× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 105 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 74.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.68× (z +11.0) | — |
| [[RKO (line)]] | wt | 145 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.380× (z -12.6) |
| [[SNU-1 (line)]] | wt | 146 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 114 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Panobinostat (drug)]] 5 µM 0.434× (z -8.9) |
| [[HCT15 (line)]] | alt | 161 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 107 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.9) ⚠ cell-cycle shift, explains ~37% of this change | [[Panobinostat (drug)]] 5 µM 0.428× (z -9.1) |
| [[SHP-77 (line)]] | alt | 68.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.430× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 71.5 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +9.4) ⚠ toxic | — |
| [[BT-474 (line)]] | alt | 157 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.421× (z -10.4) |
| [[CHP-212 (line)]] | wt | 111 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0559× (z -17.7) |
| [[SW 1271 (line)]] | alt | 183 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.231× (z -9.2) |
| [[SW48 (line)]] | wt | 113 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.94× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TASOR]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.72 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ST7L]] | +0.71 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[ZMYND11]] | +0.70 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.70 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | +0.70 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[ZNF747]] | +0.69 | +0.66 / +0.38 | both halves | 6e-05 | same gene group |
| [[MCPH1]] | +0.69 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[DNAJC8]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[IQCH-AS1]] | +0.69 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[LZIC]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.68 | +0.67 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.69 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.68 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[AFMID]] | -0.67 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[ZDHHC9]] | -0.67 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.66 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SLC27A1]] | -0.66 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[IGSF8]] | -0.66 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RGS10]] | -0.65 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[MGST3]] | -0.64 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SPTLC2]] | -0.64 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.64 | -0.59 / -0.49 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.64 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ZFP91's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ZFP91's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-4.7, 2.8); signed map (17.1, -27.6). **Vector** length 101, 35.0% of its response variance represented; |z| ≥ 3 in 1,440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +9.4 | +23.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +9.2 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +8.6 | +14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +7.4 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +14.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +4.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.8 | -17.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -16.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -19.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | +1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.2 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | ZFP91 zinc finger protein, atypical E3 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:58,579,063-58,621,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PZF, ZNF757 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; E3 ubiquitin ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JP5](https://www.uniprot.org/uniprotkb/Q96JP5) (E3 ubiquitin-protein ligase ZFP91):

> DNA-binding transcription factor. Also acts as an atypical E3 ubiquitin-protein ligase that mediates 'Lys-63'-linked ubiquitination of MAP3K14/NIK, leading to stabilize and activate MAP3K14/NIK. It thereby acts as an activator of the non-canonical NF-kappa-B2/NFKB2 pathway. May also play an important role in cell proliferation and/or anti-apoptosis.

**Summary**, from NCBI Gene [80829](https://www.ncbi.nlm.nih.gov/gene/80829):

> The protein encoded by this gene is a member of the zinc finger family of proteins. The gene product contains C2H2-type domains, which are the classical zinc finger domains found in numerous nucleic acid-binding proteins. This protein functions as a regulator of the non-canonical NF-kappaB pathway in lymphotoxin-beta receptor signaling. Alternative splicing results in multiple transcript variants. A read-through transcript variant composed of ZFP91 and the downstream CNTF gene sequence has been …

**Accessions** — [HGNC:14983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14983) · Entrez [80829](https://www.ncbi.nlm.nih.gov/gene/80829) · UniProt [Q96JP5](https://www.uniprot.org/uniprotkb/Q96JP5) · Ensembl [ENSG00000186660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186660)

## Data

Gene col 11842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11842); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11842]; `tensor/DDL_lfc|DDL_z.npy` [11842]; `embed/gene_vectors.npy` [11842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11842 or target_col == 11842). Every well: [[ZFP91 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP91.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
