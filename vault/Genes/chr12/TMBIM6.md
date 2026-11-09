---
symbol: "TMBIM6"
type: "gene"
col: 6329
ensembl_id: "ENSG00000139644"
name: "transmembrane BAX inhibitor motif containing 6"
location: "12q13.12"
module: 11
arm: "-"
pooled_cpm: 246.92
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TMBIM6

*transmembrane BAX inhibitor motif containing 6* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.77× (z +19.7, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +14.6, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.690× (z -6.9, q 2e-09, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APLP2]] (+0.71, fdr 7e-06), [[TMED4]] (+0.69, fdr 7e-06), [[MTPN]] (+0.64, fdr 1e-05); moves opposite to [[MRPL58]] (-0.65, fdr 1e-05), [[NSUN5]] (-0.64, fdr 7e-06), [[RP9]] (-0.62, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.77×** | +19.7 | 0e+00 | 48/49 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +18.8 | 0e+00 | 44/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +14.6 | 0e+00 | 47/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +12.7 | 9e-35 | 43/45 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.75×** | +10.8 | 6e-25 | 46/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.58×** | +8.9 | 8e-17 | 45/48 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +7.2 | 4e-11 | 44/49 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.43×** | +6.9 | 3e-10 | 36/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.43×** | +6.9 | 3e-10 | 39/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.43×** | +6.9 | 4e-10 | 35/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.6 | 2e-09 | 39/50 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.1 | 4e-08 | 27/48 (HOP62, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.35×** | +5.7 | 5e-07 | 34/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.34×** | +5.7 | 5e-07 | 40/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.33×** | +5.5 | 1e-06 | 29/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.3 | 5e-06 | 35/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.1 | 0.052 | 12/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.059 | 27/48 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.072 | 20/47 (Hs 766T, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.690×** | -6.9 | 2e-09 | 40/49 (NCI-H23, HepG2/C3A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -5.0 | 2e-04 | 24/48 (A-427, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -4.8 | 3e-04 | 28/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.783×** | -4.6 | 7e-04 | 27/48 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -4.4 | 1e-03 | 27/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.782×** | -4.0 | 0.005 | 30/50 (NCI-H23, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.842× | -3.2 | 0.10 | 21/47 (RKO, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.847× | -3.1 | 0.12 | 18/48 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.1 | 0.12 | 0/50 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.14 | 4/48 (NCI-H23, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 386 | 6 (4 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.460× (z -11.9) |
| [[KATO III (line)]] | alt | 441 | 6 (5 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.12× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -10.8) |
| [[HOP62 (line)]] | alt | 195 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +14.1) | — |
| [[SW480 (line)]] | alt | 225 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 357 | 4 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.540× (z -9.1) |
| [[LoVo (line)]] | wt | 322 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.50× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.513× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 321 | 5 (4 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +18.2) | [[Harringtonine (drug)]] 0.5 µM 0.545× (z -10.2) |
| [[HT-29 (line)]] | alt | 277 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.08× (z +16.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.444× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 293 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 183 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +14.0) | — |
| [[A-172 (line)]] | wt | 152 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 240 | 4 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 271 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 256 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.46× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 161 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 239 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 198 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 262 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.519× (z -9.2) |
| [[PANC-1 (line)]] | alt | 251 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 214 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +13.5) | — |
| [[A-427 (line)]] | wt | 298 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.99× (z +16.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -15.2) |
| [[A498 (line)]] | wt | 283 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.3) | — |
| [[A549 (line)]] | wt | 216 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 148 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 334 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.38× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.451× (z -10.3) |
| [[Hs 766T (line)]] | wt | 173 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 154 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 266 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +8.9) | — |
| [[SW48 (line)]] | wt | 198 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +14.4) | — |
| [[C32 (line)]] | wt | 163 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 196 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 230 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 134 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 205 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 328 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +11.4) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.536× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 198 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 145 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 136 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +11.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 299 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 274 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +15.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 218 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 431 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 277 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLP2]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TMED4]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[MTPN]] | +0.64 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[BSG]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[PCYOX1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[GRN]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ITGB1]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ADAM10]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[IDS]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CAP1]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[PSAP]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL58]] | -0.65 | -0.53 / -0.73 | both halves | 1e-05 |  |
| [[NSUN5]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[RP9]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[TRMT10B]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[PHAX]] | -0.61 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[TMEM70]] | -0.59 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZNF579]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NT5C]] | -0.58 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[GFER]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ARL14EP]] | -0.58 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[NEMF]] | -0.58 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMBIM6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPINT2]] | B | SPINT2 activity raises TMBIM6's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without SPINT2 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.6, -3.5); signed map (-52.2, -7.3). **Vector** length 122, 46.3% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +14.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.5 | +10.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.6 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.4 | -0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -13.4 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane BAX inhibitor motif containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,707,725-49,764,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BI-1, BAXI1; previously TEGT |
| Gene groups (HGNC) | Transmembrane BAX inhibitor motif containing |
| Hallmark sets | UV_RESPONSE_UP, XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P55061](https://www.uniprot.org/uniprotkb/P55061) (Bax inhibitor 1):

> Endoplasmic reticulum (ER)-resident protein that confers cellular protection as an anti-apoptotic protein by limiting multiple stress-inducing pathways surrounding the endoplasmic reticulum and mitochondria. Inhibits the activities of the key sensor for the endoplasmic reticulum unfolded protein response IRE1alpha/ERN1 both directly and by blocking BAX/BAK binding. Modulates ER calcium homeostasis by acting as a calcium-leak channel. Negatively regulates autophagy and autophagosome formation, …

**Summary**, from NCBI Gene [7009](https://www.ncbi.nlm.nih.gov/gene/7009):

> Enables endoribonuclease inhibitor activity and ubiquitin protein ligase binding activity. Involved in several processes, including negative regulation of RNA splicing; negative regulation of intracellular signal transduction; and response to L-glutamate. Acts upstream of or within negative regulation of calcium ion transport into cytosol. Located in endoplasmic reticulum membrane. Biomarker of cervical squamous cell carcinoma and prostate carcinoma. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:11723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11723) · Entrez [7009](https://www.ncbi.nlm.nih.gov/gene/7009) · UniProt [P55061](https://www.uniprot.org/uniprotkb/P55061) · Ensembl [ENSG00000139644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139644)

## Data

Gene col 6329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6329); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6329]; `tensor/DDL_lfc|DDL_z.npy` [6329]; `embed/gene_vectors.npy` [6329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6329 or target_col == 6329). Every well: [[TMBIM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMBIM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
