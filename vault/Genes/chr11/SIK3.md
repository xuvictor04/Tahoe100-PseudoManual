---
symbol: "SIK3"
type: "gene"
col: 8358
ensembl_id: "ENSG00000160584"
name: "SIK family kinase 3"
location: "11q23.3"
module: 65
arm: "-"
pooled_cpm: 270.55
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# SIK3

*SIK family kinase 3* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.63× (z +24.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.377× (z -23.6, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.686× (z -9.5, q 2e-19, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID2]] (+0.55, fdr 2e-05), [[PLEKHA5]] (+0.54, fdr 3e-05), [[CUX1]] (+0.54, fdr 3e-05); moves opposite to [[ZDHHC6]] (-0.63, fdr 1e-05), [[CDC16]] (-0.55, fdr 4e-05), [[ZNF526]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00595]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +24.3 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +17.4 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +16.7 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +16.1 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +15.1 | 0e+00 | 38/48 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +11.7 | 1e-29 | 41/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +8.1 | 7e-14 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +7.6 | 1e-12 | 35/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.3 | 1e-11 | 35/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +6.5 | 6e-09 | 28/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +5.6 | 9e-07 | 28/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +4.9 | 4e-05 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 22/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.002 | 17/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.002 | 21/48 (HT-29, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 22/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.052 | 11/48 (BT-474, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.377×** | -23.6 | 0e+00 | 43/44 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.463×** | -19.4 | 0e+00 | 48/49 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.627×** | -10.9 | 2e-25 | 33/45 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -9.5 | 2e-19 | 36/48 (SHP-77, C-33 A, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -8.1 | 7e-14 | 38/48 (KATO III, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.864× | -5.2 | 2e-05 | 15/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.815×** | -5.2 | 2e-05 | 27/48 (C-33 A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.834× | -4.6 | 3e-04 | 21/48 (SW 900, hTERT-HPNE, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.713×** | -4.5 | 5e-04 | 25/38 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.847× | -4.2 | 0.001 | 20/48 (A549, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.853× | -4.0 | 0.003 | 18/48 (SHP-77, C-33 A, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.815×** | -3.7 | 0.010 | 21/48 (Hs 766T, SW 900, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.866× | -3.7 | 0.011 | 16/48 (H4, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.879× | -3.3 | 0.043 | 13/48 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.881× | -3.2 | 0.048 | 22/48 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.791×** | -3.1 | 0.068 | 17/49 (NCI-H1573, C32, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.068 | 14/48 (LS 180, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 255 | 13 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +25.5) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -15.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 287 | 9 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -19.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 663 | 2 (1 ⚠) | 9 (6 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.08× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 207 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +28.0) | [[Dinaciclib (drug)]] 0.5 µM 0.510× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 213 | 4 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.566× (z -8.6) |
| [[KATO III (line)]] | alt | 576 | 6 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -20.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 307 | 5 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.573× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 268 | 5 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -22.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 307 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -15.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 332 | 4 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.487× (z -12.1) |
| [[HOP62 (line)]] | alt | 185 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 329 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -12.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 318 | 4 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -22.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 327 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.464× (z -9.9) |
| [[J82 (line)]] | alt | 167 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -13.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 246 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -16.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 211 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +12.1) | [[Docetaxel (drug)]] 0.05 µM 0.400× (z -11.3) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 279 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -18.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 195 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -16.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 357 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +21.0) | — |
| [[BT-474 (line)]] | alt | 135 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 253 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 342 | 2 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -19.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 305 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -17.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 98.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -15.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 372 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -11.6) |
| [[H4 (line)]] | wt | 175 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.80× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 214 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 239 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +11.3) | [[Lonafarnib (drug)]] 5 µM 0.178× (z -10.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 279 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 310 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 417 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -16.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 184 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -10.9) |
| [[C32 (line)]] | wt | 224 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -17.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 258 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -13.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 335 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.303× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 359 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 222 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 223 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.509× (z -9.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 313 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.662× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 189 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -12.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.476× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 471 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 337 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID2]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHA5]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CUX1]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[TCF12]] | +0.54 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[NCOA1]] | +0.53 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[MEMO1]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SLC6A16]] | +0.52 | +0.58 / +0.29 | both halves | 2e-04 |  |
| [[PSPC1]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[TSC22D1]] | +0.52 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[PPM1L]] | +0.51 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[DENND5B]] | +0.51 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[PIK3R3]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC6]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CDC16]] | -0.55 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZNF526]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ACP1]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[CNEP1R1]] | -0.52 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[RNF216P1]] | -0.51 | -0.23 / -0.57 | both halves | 5e-04 |  |
| [[RUSF1]] | -0.50 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[RARS1]] | -0.50 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[LONP2]] | -0.50 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[TAMM41]] | -0.50 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[RAD17]] | -0.49 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ZNF550]] | -0.49 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00595]] | B | LINC00595 activity lowers SIK3's level | lines that do not express LINC00595 (9) vs lines expressing it (41) | 1.39× higher at baseline in the lines without LINC00595 | 0.010 | ⚠ within organs, on part of the lines; also absent: SUSD4, EBF4, SLC17A7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.327). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, 12.9); signed map (10.3, -5.1). **Vector** length 108, 37.3% of its response variance represented; |z| ≥ 3 in 1,401 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +17.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.2 | +24.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.1 | +16.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +0.3 |
|  | [[Thymol (drug)]] 5 µM |  | +2.8 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SIK family kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:116,843,402-117,098,437 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12240, L19, KIAA0999, QSK |
| Gene groups (HGNC) | SIK family kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2K2](https://www.uniprot.org/uniprotkb/Q9Y2K2) (Serine/threonine-protein kinase SIK3):

> Positive regulator of mTOR signaling that functions by triggering the degradation of DEPTOR, an mTOR inhibitor. Involved in the dynamic regulation of mTOR signaling in chondrocyte differentiation during skeletogenesis. Negatively regulates cAMP signaling pathway possibly by acting on CRTC2/TORC2 and CRTC3/TORC3 (Probable). Prevents HDAC4 translocation to the nucleus (By similarity).

**Summary**, from NCBI Gene [23387](https://www.ncbi.nlm.nih.gov/gene/23387):

> Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in positive regulation of TORC1 signaling; positive regulation of TORC2 signaling; and protein phosphorylation. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29165) · Entrez [23387](https://www.ncbi.nlm.nih.gov/gene/23387) · UniProt [Q9Y2K2](https://www.uniprot.org/uniprotkb/Q9Y2K2) · Ensembl [ENSG00000160584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160584)

## Data

Gene col 8358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8358); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8358]; `tensor/DDL_lfc|DDL_z.npy` [8358]; `embed/gene_vectors.npy` [8358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8358 or target_col == 8358). Every well: [[SIK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
