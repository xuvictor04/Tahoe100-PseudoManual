---
symbol: "GRB2"
type: "gene"
col: 10873
ensembl_id: "ENSG00000177885"
name: "growth factor receptor bound protein 2"
location: "17q25.1"
module: 30
arm: "+"
pooled_cpm: 153.93
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GRB2

*growth factor receptor bound protein 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.23× (z +18.9, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.15× (z +18.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.772× (z -8.7, q 2e-15, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHA8]] (+0.74, fdr 7e-06), [[RNF4]] (+0.74, fdr 7e-06), [[GDAP2]] (+0.71, fdr 1e-05); moves opposite to [[ZNF764]] (-0.72, fdr 7e-06), [[DCAF8]] (-0.70, fdr 7e-06), [[ERCC6L2]] (-0.69, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.23×** | +18.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +18.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.01×** | +16.5 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.12×** | +14.1 | 8e-43 | 46/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +13.1 | 2e-37 | 47/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +12.3 | 5e-33 | 40/49 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +10.6 | 3e-24 | 42/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +10.0 | 1e-21 | 44/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.3 | 5e-15 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +8.2 | 1e-14 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +7.4 | 7e-12 | 38/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.30×** | +5.9 | 2e-07 | 32/50 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +5.7 | 7e-07 | 40/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +5.5 | 2e-06 | 33/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 5e-06 | 38/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.0 | 0.003 | 22/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.3 | 0.030 | 14/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.077 | 13/48 (NCI-H2030, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.088 | 13/48 (LoVo, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.772×** | -8.7 | 2e-15 | 29/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.751×** | -6.8 | 3e-09 | 30/48 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.787×** | -4.1 | 0.009 | 24/48 (LoVo, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.848× | -3.9 | 0.012 | 20/49 (A498, C-33 A, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.851× | -3.8 | 0.013 | 16/48 (SK-MEL-2, RPMI-7951, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.799×** | -3.8 | 0.013 | 22/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.8 | 0.013 | 21/48 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -3.7 | 0.017 | 21/44 (NCI-H1573, NCI-H2347, …) | top dose only | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.855× | -3.6 | 0.020 | 14/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.865× | -3.5 | 0.031 | 19/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.052 | 20/48 (NCI-H661, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.875× | -3.2 | 0.065 | 9/47 (AsPC-1, HEC-1-A, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.877× | -3.1 | 0.075 | 9/48 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.879× | -3.1 | 0.079 | 11/48 (NCI-H1573, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 145 | 10 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.72× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 163 | 9 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.14× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 146 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +15.0) | — |
| [[KATO III (line)]] | alt | 215 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.23× (z +13.2) | [[Harringtonine (drug)]] 5 µM 0.555× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 200 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.56× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 150 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 145 | 7 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.67× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 182 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 138 | 4 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.27× (z +13.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.452× (z -13.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H1573 (line)]] | alt | 95.8 | 5 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.05× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 107 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.92× (z +16.6) | — |
| [[A-172 (line)]] | wt | 118 | 3 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.20× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -17.5) |
| [[A-427 (line)]] | wt | 218 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.71× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 213 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.10× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 160 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.39× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 233 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.593× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 175 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.15× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 133 | 2 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.98× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.507× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[H4 (line)]] | wt | 138 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.78× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 173 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.02× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.60× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.4) |
| [[Hs 766T (line)]] | wt | 88.9 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.18× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 115 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.65× (z +11.4) | — |
| [[SW48 (line)]] | wt | 165 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 7.01× (z +10.5) | — |
| [[A549 (line)]] | wt | 139 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.67× (z +12.1) | — |
| [[C32 (line)]] | wt | 148 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 8.21× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.99× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 153 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.25× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -9.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 145 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.10× (z +10.6) | — |
| [[RKO (line)]] | wt | 164 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.538× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 152 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.62× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 134 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.12× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 148 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[J82 (line)]] | alt | 142 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.99× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 169 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.88× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 186 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.481× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA8]] | +0.74 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[RNF4]] | +0.74 | +0.78 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[GDAP2]] | +0.71 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[ALKBH5]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[WASF3]] | +0.70 | +0.67 / +0.58 | both halves | 7e-06 | pathway: FCGR3A-mediated phagocytosis; STRING 543 |
| [[EFCAB14]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.68 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[NFATC3]] | +0.68 | +0.73 / +0.52 | both halves | 1e-05 | pathway: FCERI mediated Ca+2 mobilization |
| [[PLEKHB2]] | +0.68 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[VDAC2]] | +0.67 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.67 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[SAP130]] | +0.67 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF764]] | -0.72 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[DCAF8]] | -0.70 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.69 | -0.72 / -0.48 | both halves | 2e-05 |  |
| [[TIA1]] | -0.69 | -0.70 / -0.49 | both halves | 1e-05 | pathway: Signaling by FGFR |
| [[ST7L]] | -0.68 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.68 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[CHMP4A]] | -0.68 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | -0.67 | -0.72 / -0.40 | both halves | 5e-05 |  |
| [[FKRP]] | -0.66 | -0.70 / -0.36 | both halves | 1e-04 |  |
| [[SLC9A8]] | -0.66 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[ZNF518A]] | -0.66 | -0.72 / -0.43 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.66 | -0.65 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRB2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-12.5, -9.0); signed map (-49.3, -4.6). **Vector** length 129, 45.4% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.5 | +8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.4 | +18.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.1 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +10.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +7.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +5.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.2 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -15.9 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -15.0 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -11.8 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.7 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.4 | -3.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.9 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | growth factor receptor bound protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,318,076-75,405,709 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NCKAP2 |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing; Growth factor receptor bound protein 2 family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, PI3K_AKT_MTOR_SIGNALING, COMPLEMENT |
| Reactome | 177 pathways, smallest: Co-inhibition by BTLA; MET activates PTPN11; Activated NTRK2 signals through PI3K |
| Matched by | ensembl_id |

**Function**, from UniProt [P62993](https://www.uniprot.org/uniprotkb/P62993) (Growth factor receptor-bound protein 2):

> Non-enzymatic adapter protein that plays a pivotal role in precisely regulated signaling cascades from cell surface receptors to cellular responses, including signaling transduction and gene expression. Thus, participates in many biological processes including regulation of innate and adaptive immunity, autophagy, DNA repair or necroptosis. Controls signaling complexes at the T-cell antigen receptor to facilitate the activation, differentiation, and function of T-cells. Mechanistically, …

**Summary**, from NCBI Gene [2885](https://www.ncbi.nlm.nih.gov/gene/2885):

> The protein encoded by this gene binds the epidermal growth factor receptor and contains one SH2 domain and two SH3 domains. Its two SH3 domains direct complex formation with proline-rich regions of other proteins, and its SH2 domain binds tyrosine phosphorylated sequences. This gene is similar to the Sem5 gene of C.elegans, which is involved in the signal transduction pathway. Two alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:4566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4566) · Entrez [2885](https://www.ncbi.nlm.nih.gov/gene/2885) · UniProt [P62993](https://www.uniprot.org/uniprotkb/P62993) · Ensembl [ENSG00000177885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177885)

## Data

Gene col 10873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10873); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10873]; `tensor/DDL_lfc|DDL_z.npy` [10873]; `embed/gene_vectors.npy` [10873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10873 or target_col == 10873). Every well: [[GRB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
