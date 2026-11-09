---
symbol: "MICU1"
type: "gene"
col: 2875
ensembl_id: "ENSG00000107745"
name: "mitochondrial calcium uptake 1"
location: "10q22.1"
module: 24
arm: "+"
pooled_cpm: 168.06
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MICU1

*mitochondrial calcium uptake 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.39× (z +24.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.545× (z -16.1, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.665× (z -5.3, q 9e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPC2]] (+0.72, fdr 7e-06), [[ZFYVE1]] (+0.69, fdr 7e-06), [[CERT1]] (+0.67, fdr 7e-06); moves opposite to [[PGAM5]] (-0.64, fdr 1e-05), [[NSUN2]] (-0.63, fdr 7e-06), [[MRPL3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CSTB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.39×** | +24.1 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +19.3 | 0e+00 | 38/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +17.8 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +13.3 | 4e-38 | 39/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +12.1 | 2e-31 | 38/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +9.5 | 3e-19 | 38/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +9.4 | 6e-19 | 35/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +8.9 | 3e-17 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +8.7 | 3e-16 | 25/49 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +8.5 | 1e-15 | 35/48 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +8.3 | 4e-15 | 34/48 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.33×** | +7.5 | 4e-12 | 35/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.3 | 1e-08 | 25/48 (SW 900, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.2 | 6e-06 | 25/50 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +5.2 | 9e-06 | 24/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 21/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.3 | 6e-04 | 24/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -16.1 | 0e+00 | 36/44 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.616×** | -13.3 | 7e-38 | 37/49 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -13.0 | 3e-36 | 40/45 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -10.0 | 1e-21 | 36/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.781×** | -6.8 | 1e-09 | 31/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.665×** | -5.3 | 9e-06 | 26/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.667×** | -5.3 | 1e-05 | 30/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | 0.846× | -4.4 | 8e-04 | 22/47 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | 0.850× | -4.3 | 0.001 | 22/47 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.729×** | -4.1 | 0.002 | 21/48 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.881× | -3.5 | 0.028 | 7/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.058 | 19/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.884× | -3.1 | 0.078 | 14/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.893× | -3.1 | 0.083 | 10/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.794×** | -3.0 | 0.099 | 16/38 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 179 | 15 (5 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +40.6) | [[Dinaciclib (drug)]] 5 µM 0.482× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 189 | 12 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +23.2) | [[Dinaciclib (drug)]] 0.5 µM 0.541× (z -12.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 375 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -14.1) |
| [[A-427 (line)]] | wt | 168 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -19.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 215 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +25.0) | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 206 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -12.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 174 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -18.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 116 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 145 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +15.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -14.6) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 189 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +20.7) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -12.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 199 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 140 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +30.2) | — |
| [[SW 900 (line)]] | alt | 182 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 182 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 176 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.484× (z -10.1) |
| [[BT-474 (line)]] | alt | 121 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.10× (z +19.5) | — |
| [[COLO 205 (line)]] | alt | 232 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +23.3) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -17.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 167 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -15.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 203 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -12.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 207 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -14.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 186 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +26.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.562× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 127 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +33.1) | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 199 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 141 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 117 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 98.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.1) | — |
| [[J82 (line)]] | alt | 99.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.4) | — |
| [[NCI-H2347 (line)]] | alt | 190 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 269 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 129 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +22.6) | — |
| [[RPMI-7951 (line)]] | alt | 146 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 94.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 142 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.552× (z -8.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 156 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 347 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -14.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +17.5) | — |
| [[LoVo (line)]] | wt | 90.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.3) | — |
| [[A549 (line)]] | wt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.2) |
| [[C32 (line)]] | wt | 120 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.0) | — |
| [[H4 (line)]] | wt | 136 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 196 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 118 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.91× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPC2]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ZFYVE1]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[CERT1]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[UMAD1]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | +0.65 | +0.58 / +0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SYNRG]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[RNASEK]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[GABARAPL2]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[UXT]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ATP5PD]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SIRT2]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAM5]] | -0.64 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.63 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[MRPL3]] | -0.63 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[EHD3]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 | same gene group |
| [[PRPF19]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[HEATR3]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RIOX2]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[POLR1B]] | -0.58 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[NAA15]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ATIC]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TXLNA]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSTB]] | B | CSTB activity raises MICU1's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without CSTB | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-8.5, -46.7); signed map (-10.9, 7.0). **Vector** length 119, 40.4% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.6 | +24.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +17.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.8 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.4 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -10.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | -6.7 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -13.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | -5.4 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | -5.2 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial calcium uptake 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,367,340-72,626,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CALC, EFHA3, FLJ12684; previously CBARA1 |
| Gene groups (HGNC) | EF-hand domain containing; MCU complex subunits |
| Reactome | 3 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPX6](https://www.uniprot.org/uniprotkb/Q9BPX6) (Calcium uptake protein 1, mitochondrial):

> Calcium sensor of the mitochondrial calcium uniporter (MCU) channel, which senses calcium level via its EF-hand domains. MICU1 and MICU2 (or MICU3) form a disulfide-linked heterodimer that stimulates and inhibits MCU activity, depending on the concentration of calcium. At low calcium levels, MICU1 occludes the pore of the MCU channel, preventing mitochondrial calcium uptake. At higher calcium levels, calcium-binding to MICU1 and MICU2 (or MICU3) induces a conformational change that weakens …

**Summary**, from NCBI Gene [10367](https://www.ncbi.nlm.nih.gov/gene/10367):

> This gene encodes an essential regulator of mitochondrial Ca2+ uptake under basal conditions. The encoded protein interacts with the mitochondrial calcium uniporter, a mitochondrial inner membrane Ca2+ channel, and is essential in preventing mitochondrial Ca2+ overload, which can cause excessive production of reactive oxygen species and cell stress. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:1530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1530) · Entrez [10367](https://www.ncbi.nlm.nih.gov/gene/10367) · UniProt [Q9BPX6](https://www.uniprot.org/uniprotkb/Q9BPX6) · Ensembl [ENSG00000107745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107745)

## Data

Gene col 2875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2875); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2875]; `tensor/DDL_lfc|DDL_z.npy` [2875]; `embed/gene_vectors.npy` [2875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2875 or target_col == 2875). Every well: [[MICU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
