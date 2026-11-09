---
symbol: "HNRNPM"
type: "gene"
col: 1808
ensembl_id: "ENSG00000099783"
name: "heterogeneous nuclear ribonucleoprotein M"
location: "19p13.2"
module: 3
arm: "-"
pooled_cpm: 169.67
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPM

*heterogeneous nuclear ribonucleoprotein M* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +18.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.26× (z +17.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.851× (z -4.6, q 0.002, down in 17 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Lactate (calcium) (drug)]] 0.5 µM: 0.829× (z -3.8, q 0.028, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EWSR1]] (+0.79, fdr 7e-06), [[DHX9]] (+0.73, fdr 7e-06), [[YWHAE]] (+0.72, fdr 7e-06); moves opposite to [[CIAO2B]] (-0.70, fdr 1e-05), [[COMMD6]] (-0.68, fdr 1e-05), [[RPP21]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SFT2D2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +18.8 | 0e+00 | 49/49 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.95×** | +18.7 | 0e+00 | 46/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.26×** | +17.3 | 0e+00 | 48/49 (COLO 205, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +16.0 | 0e+00 | 45/45 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.22×** | +15.9 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +15.7 | 0e+00 | 41/44 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +14.4 | 3e-45 | 47/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.68×** | +13.6 | 6e-40 | 48/48 (COLO 205, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.74×** | +11.0 | 2e-26 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +10.5 | 4e-24 | 47/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.73×** | +10.4 | 9e-24 | 42/48 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +10.3 | 3e-23 | 46/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +8.2 | 1e-14 | 38/48 (A-172, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.49×** | +7.9 | 2e-13 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +7.3 | 1e-11 | 38/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +6.9 | 1e-10 | 41/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 8e-05 | 26/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 6e-04 | 29/48 (A498, A549, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.3 | 0.021 | 18/48 (H4, HS-578T, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.023 | 18/47 (HOP62, NCI-H23, …) | two highest doses |  |
| [[LJI308 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.030 | 18/48 (HCT15, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.059 | 16/48 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +2.9 | 0.073 | 17/48 (PANC-1, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.851× | -4.6 | 0.002 | 17/48 (RKO, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.809×** | -4.3 | 0.005 | 26/49 (SK-MEL-2, NCI-H2122, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.829×** | -3.8 | 0.028 | 25/48 (C32, SNU-423, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.893× | -3.3 | 0.14 | 9/48 (SK-MEL-2, SW 900, …) | two highest doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.14 | 16/48 (SW 900, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.14 | 9/48 (BT-474, A-427, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.857× | -3.1 | 0.14 | 20/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.746× | -3.1 | 0.14 | 21/49 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.860× | -3.1 | 0.14 | 10/49 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 158 | 14 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +20.9) | — |
| [[NCI-H460 (line)]] | wt | 156 | 13 (10 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.16× (z +18.5) | — |
| [[PANC-1 (line)]] | alt | 142 | 13 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +22.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +20.4) | — |
| [[A-172 (line)]] | wt | 141 | 11 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 191 | 11 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.5) | — |
| [[H4 (line)]] | wt | 181 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 116 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +19.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 125 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 150 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 195 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.48× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 128 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 174 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.2) | — |
| [[SW480 (line)]] | alt | 223 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +13.6) | — |
| [[A-427 (line)]] | wt | 196 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.88× (z +11.6) | — |
| [[A498 (line)]] | wt | 187 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +19.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +11.8) | — |
| [[A549 (line)]] | wt | 135 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +18.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.40× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 120 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +17.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 20.6× (z +17.4) | — |
| [[HS-578T (line)]] | alt | 182 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 130 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 149 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 120 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.33× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 169 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 103 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 218 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.16× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 176 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +11.7) | — |
| [[SW48 (line)]] | wt | 203 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.61× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 151 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +18.2) | — |
| [[HEC-1-A (line)]] | alt | 179 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.40× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 170 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.66× (z +10.5) | — |
| [[KATO III (line)]] | alt | 146 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 164 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.02× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 150 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.79× (z +9.4) | — |
| [[C32 (line)]] | wt | 188 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 10.9× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.30× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.65× (z +9.2) | — |
| [[J82 (line)]] | alt | 171 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 242 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 198 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 239 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 159 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.80× (z +10.2) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.85× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 230 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 231 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.80× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 273 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 226 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | same gene group; STRING 901 |
| [[DHX9]] | +0.73 | +0.78 / +0.75 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 974 |
| [[YWHAE]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[HNRNPH3]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 | same gene group; STRING 945 |
| [[HNRNPU]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 985 |
| [[HNRNPD]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 962 |
| [[SFPQ]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | same gene group; STRING 968 |
| [[HNRNPA3]] | +0.69 | +0.48 / +0.78 | both halves | 2e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 935 |
| [[U2SURP]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 635 |
| [[FUBP1]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 | STRING 725 |
| [[ILF3]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 | STRING 970 |
| [[BCLAF1]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 | STRING 548 |

## Genes that move opposite

*54 of its nearest partners move opposite, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | -0.70 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.68 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[RPP21]] | -0.65 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[MPG]] | -0.65 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[GUK1]] | -0.64 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[CAMLG]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[B3GAT3]] | -0.63 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[ARID3A]] | -0.63 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[INAFM1]] | -0.62 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[CIB1]] | -0.61 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MIEN1]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[RNF181]] | -0.61 | -0.39 / -0.62 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFT2D2]] | C | HNRNPM's natural level weakens SFT2D2's drug response | HNRNPM's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.14; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.1, -24.7); signed map (14.6, -37.9). **Vector** length 95.5, 35.5% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 10); *MYC targets v1* (hallmark, mean cos +0.65 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +18.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.4 | +16.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.5 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +13.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +2.1 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.7 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:8,444,767-8,489,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HTGR1, HNRNPM4, HNRPM4, CEAR; previously NAGR1, HNRPM |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 13 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [P52272](https://www.uniprot.org/uniprotkb/P52272) (Heterogeneous nuclear ribonucleoprotein M):

> Pre-mRNA binding protein in vivo, binds avidly to poly(G) and poly(U) RNA homopolymers in vitro. Involved in splicing. Acts as a receptor for carcinoembryonic antigen in Kupffer cells, may initiate a series of signaling events leading to tyrosine phosphorylation of proteins and induction of IL-1 alpha, IL-6, IL-10 and tumor necrosis factor alpha cytokines.

**Summary**, from NCBI Gene [4670](https://www.ncbi.nlm.nih.gov/gene/4670):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:5046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5046) · Entrez [4670](https://www.ncbi.nlm.nih.gov/gene/4670) · UniProt [P52272](https://www.uniprot.org/uniprotkb/P52272) · Ensembl [ENSG00000099783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099783)

## Data

Gene col 1808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1808); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1808]; `tensor/DDL_lfc|DDL_z.npy` [1808]; `embed/gene_vectors.npy` [1808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1808 or target_col == 1808). Every well: [[HNRNPM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
