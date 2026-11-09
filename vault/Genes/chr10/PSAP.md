---
symbol: "PSAP"
type: "gene"
col: 12451
ensembl_id: "ENSG00000197746"
name: "prosaposin"
location: "10q22.1"
module: 50
arm: "+"
pooled_cpm: 358.26
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PSAP

*prosaposin* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +19.8, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +13.2, q 2e-37, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.574× (z -11.3, q 1e-26, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSD]] (+0.78, fdr 7e-06), [[GRN]] (+0.72, fdr 7e-06), [[IDS]] (+0.71, fdr 7e-06); moves opposite to [[BRIX1]] (-0.70, fdr 7e-06), [[CCDC137]] (-0.65, fdr 1e-05), [[MIS18A]] (-0.62, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +19.8 | 0e+00 | 49/49 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +17.6 | 0e+00 | 44/44 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +13.4 | 6e-39 | 45/45 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +13.2 | 2e-37 | 47/49 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +9.9 | 6e-21 | 45/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +8.9 | 8e-17 | 40/48 (SW480, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +8.5 | 1e-15 | 42/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.3 | 2e-11 | 39/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 2e-10 | 41/49 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +6.9 | 4e-10 | 39/48 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.8 | 5e-10 | 37/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.5 | 3e-09 | 36/48 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.2 | 3e-08 | 35/48 (HT-29, COLO 205, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.6 | 9e-07 | 35/50 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +5.1 | 1e-05 | 30/48 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 28/48 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.4 | 3e-04 | 29/49 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.003 | 36/47 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.009 | 15/48 (SW1417, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.574×** | -11.3 | 1e-26 | 44/49 (SW 900, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.757×** | -8.2 | 4e-14 | 33/48 (SHP-77, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -8.0 | 3e-13 | 40/48 (SW 900, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.702×** | -7.5 | 1e-11 | 44/48 (SW 900, LS 180, …) | all doses, flat |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.854× | -4.7 | 3e-04 | 14/48 (SK-MEL-2, RKO, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.804×** | -4.3 | 0.002 | 26/47 (LS 180, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.820×** | -4.2 | 0.002 | 25/48 (CFPAC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.822×** | -4.0 | 0.005 | 24/48 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 362 | 10 (6 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +15.1) | [[Verteporfin (drug)]] 5 µM 0.489× (z -10.7) |
| [[KATO III (line)]] | alt | 311 | 8 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.97× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -12.1) |
| [[HT-29 (line)]] | alt | 266 | 9 (4 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.42× (z +13.5) | — |
| [[HepG2_C3A (line)]] | wt | 381 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 233 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +14.1) | — |
| [[SW 900 (line)]] | alt | 868 | 4 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -18.2) |
| [[SW1417 (line)]] | alt | 247 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 215 | 5 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -10.0) |
| [[COLO 205 (line)]] | alt | 394 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 266 | 5 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 238 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.0) | — |
| [[SW480 (line)]] | alt | 162 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 421 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -14.6) |
| [[SHP-77 (line)]] | alt | 103 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 747 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -15.5) |
| [[A498 (line)]] | wt | 310 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +12.3) | [[Verteporfin (drug)]] 5 µM 0.512× (z -8.8) |
| [[A549 (line)]] | wt | 326 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.84× (z +8.8) | [[Verteporfin (drug)]] 5 µM 0.536× (z -8.7) |
| [[AN3 CA (line)]] | alt | 487 | 2 (1 ⚠) | 3 | [[Tucidinostat (drug)]] 5 µM 1.76× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -16.2) |
| [[HOP62 (line)]] | alt | 367 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +12.3) | [[Verteporfin (drug)]] 5 µM 0.400× (z -13.2) |
| [[LoVo (line)]] | wt | 166 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.38× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 345 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.6) | [[Verteporfin (drug)]] 5 µM 0.422× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 295 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +14.8) | — |
| [[C32 (line)]] | wt | 714 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +13.3) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.335× (z -15.2) |
| [[HCT15 (line)]] | alt | 230 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -11.0) |
| [[HS-578T (line)]] | alt | 287 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +14.6) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.373× (z -12.3) |
| [[J82 (line)]] | alt | 311 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +15.4) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.461× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 215 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 195 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 216 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 626 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -13.2) |
| [[PANC-1 (line)]] | alt | 814 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +17.8) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.461× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 322 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -10.7) |
| [[SNU-423 (line)]] | alt | 881 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +11.5) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.391× (z -13.9) |
| [[C-33 A (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +15.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 300 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 304 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 350 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 284 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -12.4) |
| [[A-427 (line)]] | wt | 227 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 235 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.0) |
| [[Hs 766T (line)]] | wt | 293 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 371 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +13.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 407 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 235 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 241 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSD]] | +0.78 | +0.81 / +0.67 | both halves | 7e-06 | STRING 799 |
| [[GRN]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 | STRING 856 |
| [[IDS]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 476 |
| [[NUCB1]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[OS9]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[VAT1]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LAMB2]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EEF1G]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CTSB]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | STRING 678 |
| [[MMP2]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIX1]] | -0.70 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.65 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[MIS18A]] | -0.62 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[TMA16]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ICE2]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | -0.59 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[MRM2]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[MRPL58]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[PPIL1]] | -0.55 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[RRS1]] | -0.55 | -0.46 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | GPX3 activity raises PSAP's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.29× lower at baseline in the lines without GPX3 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[CTSD]] | C | CTSD activity raises PSAP's level | lines that do not express CTSD (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without CTSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFITM10, SQOR, ST6GALNAC2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.4, -20.0); signed map (-50.9, -8.2). **Vector** length 139, 52.3% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.50 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.9 | +7.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.2 | +7.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.6 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.5 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.4 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.6 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.9 | -7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.1 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -11.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | prosaposin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:71,816,298-71,851,251 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SAP1, GLBA, SAP2 |
| Gene groups (HGNC) | Receptor ligands; Saposin B type domain containing |
| Reactome | 16 pathways, smallest: Glycosphingolipid catabolism; Glycosphingolipid metabolism; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P07602](https://www.uniprot.org/uniprotkb/P07602) (Prosaposin):

> Saposins are specific low-molecular mass non-enzymatic glycoproteins that act as activator proteins for lysosomal sphingolipid-degrading enzymes, facilitating the hydrolysis of sphingolipids by extracting lipid substrates from membranes and presenting them to their respective enzymes. They are derived from a common precursor protein, prosaposin, which is proteolytically cleaved to yield four homologous proteins (saposin A, B, C, and D), each with distinct but partially overlapping lipid and …

**Summary**, from NCBI Gene [5660](https://www.ncbi.nlm.nih.gov/gene/5660):

> This gene encodes a highly conserved preproprotein that is proteolytically processed to generate four main cleavage products including saposins A, B, C, and D. Each domain of the precursor protein is approximately 80 amino acid residues long with nearly identical placement of cysteine residues and glycosylation sites. Saposins A-D localize primarily to the lysosomal compartment where they facilitate the catabolism of glycosphingolipids with short oligosaccharide groups. The precursor protein …

**Accessions** — [HGNC:9498](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9498) · Entrez [5660](https://www.ncbi.nlm.nih.gov/gene/5660) · UniProt [P07602](https://www.uniprot.org/uniprotkb/P07602) · Ensembl [ENSG00000197746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197746)

## Data

Gene col 12451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12451); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12451]; `tensor/DDL_lfc|DDL_z.npy` [12451]; `embed/gene_vectors.npy` [12451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12451 or target_col == 12451). Every well: [[PSAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
