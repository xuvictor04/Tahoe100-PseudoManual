---
symbol: "ARL15"
type: "gene"
col: 11659
ensembl_id: "ENSG00000185305"
name: "ARF like GTPase 15"
location: "5q11.2"
module: 16
arm: "-"
pooled_cpm: 167.74
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ARL15

*ARF like GTPase 15* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.47× (z +17.0, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.422× (z -14.9, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.373× (z -8.7, q 3e-16, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEAK1]] (+0.58, fdr 1e-05), [[PPM1L]] (+0.54, fdr 1e-05), [[MAGI3]] (+0.52, fdr 1e-05); moves opposite to [[ZNF17]] (-0.59, fdr 1e-05), [[AP1M1]] (-0.57, fdr 1e-05), [[MTERF4]] (-0.56, fdr 5e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +17.0 | 0e+00 | 43/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +16.5 | 0e+00 | 44/47 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +15.3 | 0e+00 | 41/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +14.6 | 0e+00 | 43/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +13.9 | 7e-42 | 42/47 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +12.8 | 1e-35 | 46/47 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +12.8 | 2e-35 | 43/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +11.4 | 3e-28 | 40/49 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +7.7 | 9e-13 | 36/47 (SNU-423, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 1e-12 | 39/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.50×** | +7.6 | 2e-12 | 38/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.33×** | +7.5 | 3e-12 | 43/48 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +7.4 | 8e-12 | 32/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +6.3 | 1e-08 | 36/46 (A-172, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +6.2 | 3e-08 | 24/47 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.5 | 1e-06 | 26/47 (A-172, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.422×** | -14.9 | 0e+00 | 39/44 (SHP-77, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -14.1 | 1e-42 | 37/43 (SNU-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.464×** | -11.5 | 3e-28 | 37/48 (KATO III, A-427, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.577×** | -9.9 | 8e-21 | 36/46 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -8.7 | 3e-16 | 43/48 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.649×** | -8.1 | 6e-14 | 38/47 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.499×** | -6.1 | 7e-08 | 23/37 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -6.0 | 1e-07 | 34/47 (LOX-IMVI, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.775×** | -4.8 | 1e-04 | 25/47 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -4.2 | 0.001 | 25/47 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.2 | 0.001 | 22/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.829×** | -3.2 | 0.058 | 23/46 (C32, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.807×** | -3.2 | 0.058 | 24/47 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 186 | 8 | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.468× (z -10.0) |
| [[J82 (line)]] | alt | 105 | 13 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.77× (z +19.2) | — |
| [[PANC-1 (line)]] | alt | 128 | 5 | 8 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 3.47× (z +17.0) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.231× (z -9.5) |
| [[HT-29 (line)]] | alt | 202 | 6 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -12.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 87.0 | 10 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +24.6) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 188 | 9 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -17.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 252 | 6 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 105 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +16.5) | — |
| [[NCI-H2347 (line)]] | alt | 100 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 156 | 10 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.96× (z +15.5) | — |
| [[SW1417 (line)]] | alt | 117 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +16.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -12.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 77.7 | 8 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 217 | 3 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.14× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -19.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 209 | 4 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -10.9) |
| [[SW 900 (line)]] | alt | 130 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -15.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 55.2 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.58× (z +17.3) | — |
| [[LS 180 (line)]] | wt | 361 | 4 | 4 (4 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -17.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 141 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +14.2) | — |
| [[KATO III (line)]] | alt | 216 | 1 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.67× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.519× (z -9.3) |
| [[LoVo (line)]] | wt | 294 | 2 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.170× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 87.5 | 5 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.30× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.4) |
| [[RKO (line)]] | wt | 162 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -12.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 222 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -22.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 282 | 2 | 5 (4 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -13.2) |
| [[A-172 (line)]] | wt | 215 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 276 | 2 | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -23.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 72.4 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.9) | — |
| [[H4 (line)]] | wt | 105 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 74.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +17.3) | — |
| [[A-427 (line)]] | wt | 417 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.1) |
| [[AN3 CA (line)]] | alt | 371 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 146 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 153 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -12.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.4) |
| [[COLO 205 (line)]] | alt | 281 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.2) | [[TAK-901 (drug)]] 5 µM 0.160× (z -9.8) |
| [[HCT15 (line)]] | alt | 178 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.521× (z -8.9) |
| [[SHP-77 (line)]] | alt | 175 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 224 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.0665× (z -26.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 128 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.0) | — |
| [[C32 (line)]] | wt | 239 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 301 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0281× (z -19.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 321 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PPM1L]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MAGI3]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TMEM131L]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NEO1]] | +0.51 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MAGI1]] | +0.51 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[WDFY3]] | +0.51 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[POU2F1]] | +0.51 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[EPB41L5]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[GLCE]] | +0.50 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SERINC5]] | +0.50 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[AHCYL2]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF17]] | -0.59 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[AP1M1]] | -0.57 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[MTERF4]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ASCC2]] | -0.55 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[INO80E]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SF3A2]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[MAEA]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[C19orf47]] | -0.53 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ZNF229]] | -0.53 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ZNF583]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNF408]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[ZNF568]] | -0.52 | -0.53 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.248). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-51.1, 7.9); signed map (-15.5, 28.3). **Vector** length 109, 39.8% of its response variance represented; |z| ≥ 3 in 1,724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +13.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.7 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.6 | -14.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | -14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:53,883,942-54,310,582 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20051; previously ARFRP2 |
| Gene groups (HGNC) | ARF GTPase family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q9NXU5](https://www.uniprot.org/uniprotkb/Q9NXU5) carries no function annotation.

**Summary**, from NCBI Gene [54622](https://www.ncbi.nlm.nih.gov/gene/54622):

> Predicted to enable GTP binding activity; GTPase activity; and metal ion binding activity. Predicted to act upstream of or within several processes, including bone mineralization; hard palate development; and soft palate development. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25945) · Entrez [54622](https://www.ncbi.nlm.nih.gov/gene/54622) · UniProt [Q9NXU5](https://www.uniprot.org/uniprotkb/Q9NXU5) · Ensembl [ENSG00000185305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185305)

## Data

Gene col 11659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11659); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11659]; `tensor/DDL_lfc|DDL_z.npy` [11659]; `embed/gene_vectors.npy` [11659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11659 or target_col == 11659). Every well: [[ARL15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
