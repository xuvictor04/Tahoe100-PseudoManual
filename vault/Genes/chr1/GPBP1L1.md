---
symbol: "GPBP1L1"
type: "gene"
col: 8262
ensembl_id: "ENSG00000159592"
name: "GC-rich promoter binding protein 1 like 1"
location: "1p34.1"
module: 234
arm: "+"
pooled_cpm: 171.72
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/234"]
generated_by: "tahoemap"
---

# GPBP1L1

*GC-rich promoter binding protein 1 like 1* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +14.4, q 3e-44, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.598× (z -13.6, q 2e-39, down in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.642× (z -11.7, q 3e-29, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR20]] (+0.71, fdr 1e-05), [[TMEM59]] (+0.69, fdr 7e-06), [[LEMD3]] (+0.68, fdr 1e-05); moves opposite to [[BMS1]] (-0.61, fdr 1e-05), [[CSRP1]] (-0.59, fdr 3e-05), [[MPHOSPH6]] (-0.59, fdr 1e-05).
> It is in [[Module 234]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +14.4 | 3e-44 | 46/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +10.7 | 3e-24 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +9.0 | 5e-17 | 40/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +8.7 | 7e-16 | 37/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +8.0 | 2e-13 | 34/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +7.9 | 2e-13 | 38/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.9 | 3e-13 | 31/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.8 | 4e-07 | 29/48 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.6 | 1e-06 | 19/49 (AsPC-1, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.18× | +4.1 | 0.002 | 20/48 (A498, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.007 | 19/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 25/49 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.2 | 0.062 | 19/50 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.13× | +3.2 | 0.062 | 9/47 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.079 | 15/48 (NCI-H1573, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.598×** | -13.6 | 2e-39 | 49/49 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -11.7 | 3e-29 | 36/48 (SNU-423, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.648×** | -11.1 | 4e-26 | 34/44 (Hs 766T, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.710×** | -9.1 | 1e-17 | 37/48 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.693×** | -9.0 | 3e-17 | 35/45 (SNU-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -7.6 | 3e-12 | 38/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.754×** | -7.5 | 6e-12 | 32/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -7.1 | 1e-10 | 30/48 (HT-29, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -6.9 | 2e-10 | 33/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.790×** | -6.2 | 2e-08 | 27/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -5.9 | 2e-07 | 27/48 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.829×** | -5.0 | 3e-05 | 24/48 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.701×** | -4.9 | 4e-05 | 30/48 (Panc 03.27, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.704×** | -4.9 | 5e-05 | 30/48 (SW1417, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.712×** | -4.7 | 1e-04 | 25/48 (LoVo, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -4.3 | 6e-04 | 27/48 (LoVo, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -4.2 | 8e-04 | 18/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.901× | -3.9 | 0.003 | 8/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.864× | -3.9 | 0.003 | 11/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.864× | -3.9 | 0.003 | 15/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.871× | -3.7 | 0.007 | 14/49 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.876× | -3.2 | 0.030 | 19/47 (LS 180, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.887× | -3.2 | 0.036 | 8/48 (A-172, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 189 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +17.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.532× (z -10.8) |
| [[HT-29 (line)]] | alt | 212 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.82× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 227 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.531× (z -9.3) |
| [[LS 180 (line)]] | wt | 238 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 196 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.477× (z -9.3) |
| [[HOP62 (line)]] | alt | 166 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.521× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 240 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.545× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 195 | 2 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.526× (z -8.8) |
| [[HS-578T (line)]] | alt | 185 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.506× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 207 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.479× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 205 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 170 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 163 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 182 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.16× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 148 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.445× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.499× (z -8.5) |
| [[A-172 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 169 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 186 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.314× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 165 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 118 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 209 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.622× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-423 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -11.7) |
| [[SW 900 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 198 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 165 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR20]] | +0.71 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[LEMD3]] | +0.68 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[PAN3]] | +0.67 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[CDK19]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[KANSL1]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[APTR]] | +0.66 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.65 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SOS1]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[HERPUD2]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[HINFP]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[MPHOSPH6]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.58 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[PCNX2]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[GTF2H3]] | -0.56 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[HUS1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[EIF2B3]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.55 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PSMG1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NAA15]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 234]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-0.7, -42.3); signed map (-14.3, 11.8). **Vector** length 107, 33.0% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.6 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.8 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.3 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.2 | +14.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.7 | -11.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -5.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | GC-rich promoter binding protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,627,304-45,688,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SP192 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC44](https://www.uniprot.org/uniprotkb/Q9HC44) (Vasculin-like protein 1):

> Possible transcription factor.

**Summary**, from NCBI Gene [60313](https://www.ncbi.nlm.nih.gov/gene/60313):

> Predicted to enable DNA-binding transcription factor activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28843) · Entrez [60313](https://www.ncbi.nlm.nih.gov/gene/60313) · UniProt [Q9HC44](https://www.uniprot.org/uniprotkb/Q9HC44) · Ensembl [ENSG00000159592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159592)

## Data

Gene col 8262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8262); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8262]; `tensor/DDL_lfc|DDL_z.npy` [8262]; `embed/gene_vectors.npy` [8262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8262 or target_col == 8262). Every well: [[GPBP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPBP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
