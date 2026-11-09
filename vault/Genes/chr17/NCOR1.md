---
symbol: "NCOR1"
type: "gene"
col: 6482
ensembl_id: "ENSG00000141027"
name: "nuclear receptor corepressor 1"
location: "17p12-p11.2"
module: 51
arm: "+"
pooled_cpm: 349.58
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NCOR1

*nuclear receptor corepressor 1* — 17p12-p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.73× (z +22.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.563× (z -23.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLK1]] (+0.59, fdr 1e-05), [[SETD2]] (+0.59, fdr 5e-05), [[USP24]] (+0.57, fdr 1e-05); moves opposite to [[SRA1]] (-0.50, fdr 1e-04), [[ENTPD7]] (-0.49, fdr 8e-04, ⚠ not reproduced), [[ZNF841]] (-0.49, fdr 5e-04), [[ZNF417]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +22.3 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +18.3 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +13.4 | 2e-38 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +12.5 | 1e-33 | 39/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +10.9 | 1e-25 | 42/49 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +7.6 | 2e-12 | 26/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +7.3 | 2e-11 | 34/48 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +6.0 | 1e-07 | 14/48 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +5.7 | 8e-07 | 20/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +5.5 | 3e-06 | 16/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.10× | +5.4 | 3e-06 | 3/48 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +5.3 | 6e-06 | 13/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.14× | +5.0 | 2e-05 | 16/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +5.0 | 2e-05 | 17/48 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +4.0 | 0.003 | 7/48 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.10× | +3.8 | 0.004 | 4/47 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | 1.19× | +3.7 | 0.008 | 15/48 (NCI-H1573, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.09× | +3.5 | 0.014 | 4/48 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.16× | +3.2 | 0.038 | 5/49 (A549, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.08× | +3.1 | 0.048 | 4/49 (HepG2/C3A, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.563×** | -23.4 | 0e+00 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.560×** | -22.7 | 0e+00 | 47/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -20.3 | 0e+00 | 48/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -16.6 | 0e+00 | 33/49 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.681×** | -15.7 | 0e+00 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.688×** | -15.3 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -13.6 | 2e-40 | 43/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -10.9 | 1e-25 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -9.6 | 4e-20 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.890× | -6.7 | 9e-10 | 7/48 (SHP-77, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.851× | -6.6 | 2e-09 | 19/48 (RKO, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | 0.854× | -6.0 | 1e-07 | 20/45 (A-427, SNU-1, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -5.6 | 1e-06 | 11/49 (SHP-77, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.872× | -5.6 | 1e-06 | 19/48 (A549, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.787×** | -5.1 | 1e-05 | 28/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.925× | -3.2 | 0.046 | 0/48 | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.926× | -3.1 | 0.049 | 2/48 (SW48, SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 426 | 5 (2 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.457× (z -17.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 357 | 8 (3 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +18.1) | [[Auranofin (drug)]] 5 µM 0.584× (z -15.0) |
| [[SW480 (line)]] | alt | 428 | 4 (1 ⚠) | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.36× (z +20.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -24.6) |
| [[A549 (line)]] | wt | 417 | 5 (3 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.77× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -29.1) |
| [[HOP62 (line)]] | alt | 359 | 4 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -18.3) |
| [[COLO 205 (line)]] | alt | 445 | 4 (2 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +13.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -13.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.606× (z -9.8) |
| [[LoVo (line)]] | wt | 379 | 3 (2 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.512× (z -19.0) |
| [[LS 180 (line)]] | wt | 693 | 2 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -20.0) |
| [[BT-474 (line)]] | alt | 281 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.553× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 464 | 2 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.511× (z -13.7) |
| [[HT-29 (line)]] | alt | 301 | 2 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.415× (z -18.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.442× (z -18.1) |
| [[KATO III (line)]] | alt | 454 | 2 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -22.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 520 | 4 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +15.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.560× (z -12.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.601× (z -11.7) |
| [[RKO (line)]] | wt | 322 | 4 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.80× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.426× (z -11.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.505× (z -9.6) |
| [[SNU-423 (line)]] | alt | 239 | 2 (1 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.66× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.562× (z -10.9) |
| [[SW1417 (line)]] | alt | 326 | 1 (1 ⚠) | 6 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.51× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -16.4) |
| [[A-172 (line)]] | wt | 336 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 2.27× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -15.5) |
| [[A-427 (line)]] | wt | 413 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -20.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.561× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 368 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.486× (z -13.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -12.9) |
| [[C-33 A (line)]] | alt | 611 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.505× (z -13.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.537× (z -12.5) |
| [[Hs 766T (line)]] | wt | 238 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.477× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 389 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.482× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 436 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.36× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.463× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 289 | 3 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.90× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.644× (z -9.4) |
| [[SNU-1 (line)]] | wt | 400 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.504× (z -8.7) |
| [[HS-578T (line)]] | alt | 273 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.556× (z -11.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.609× (z -10.1) |
| [[J82 (line)]] | alt | 249 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 234 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.540× (z -12.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.564× (z -11.8) |
| [[PANC-1 (line)]] | alt | 293 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +16.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.565× (z -14.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.610× (z -13.3) |
| [[SHP-77 (line)]] | alt | 829 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.534× (z -14.6) |
| [[SW48 (line)]] | wt | 436 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 311 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 167 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.548× (z -11.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.595× (z -10.6) |
| [[H4 (line)]] | wt | 256 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 250 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.531× (z -10.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.552× (z -9.8) |
| [[A498 (line)]] | wt | 293 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 2.89× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.632× (z -11.0) |
| [[AN3 CA (line)]] | alt | 431 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.507× (z -11.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 229 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 403 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.580× (z -9.3) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 264 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.591× (z -8.8) ⚠ toxic |
| [[C32 (line)]] | wt | 277 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 350 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 531 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 601 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK1]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[SETD2]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 | pathway: Chromatin modifying enzymes; STRING 534 |
| [[USP24]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ITFG1]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ATRX]] | +0.55 | +0.22 / +0.64 | both halves | 6e-04 | STRING 485 |
| [[MAP2K5]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ROCK1]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PUM2]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MED13L]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Adipogenesis; STRING 644 |
| [[PAIP1]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[WDFY3]] | +0.53 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[ARID1B]] | +0.52 | +0.39 / +0.60 | both halves | 5e-05 | pathway: Chromatin modifying enzymes; STRING 518 |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRA1]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 | STRING 457 |
| [[ENTPD7]] | -0.49 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[ZNF841]] | -0.49 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[ZNF417]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ZNF275]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[TAF13]] | -0.47 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[BLZF1]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[LINC01128]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SPSB1]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[BET1L]] | -0.45 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[ATG101]] | -0.45 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[RP2]] | -0.44 | -0.44 / -0.32 | both halves | 2e-04 | pathway: Organelle biogenesis and maintenance |
| [[AP1M1]] | -0.43 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NCOR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.315). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.6, 4.7); signed map (6.2, -13.9). **Vector** length 96.0, 31.5% of its response variance represented; |z| ≥ 3 in 1,456 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +8.4 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +8.1 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.5 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.8 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -13.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -22.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -15.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.3 | +1.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.3 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -0.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.9 | -0.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor corepressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12-p11.2 — chr17:16,029,065-16,218,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | N-CoR, hCIT529I10, TRAC1, hN-CoR, KIAA1047, MGC104216, PPP1R109 |
| Gene groups (HGNC) | Myb/SANT domain containing; Protein phosphatase 1 regulatory subunits; NCoR/SMRT transcriptional repression complex subunits |
| Reactome | 62 pathways, smallest: Loss of MECP2 binding ability to the NCoR/SMRT complex; NR1H2 & NR1H3 regulate gene expression to control bile acid homeostasis; Disorders of Nervous System Development |
| Matched by | ensembl_id |

**Function**, from UniProt [O75376](https://www.uniprot.org/uniprotkb/O75376) (Nuclear receptor corepressor 1):

> Mediates transcriptional repression by certain nuclear receptors. Part of a complex which promotes histone deacetylation and the formation of repressive chromatin structures which may impede the access of basal transcription factors. Participates in the transcriptional repressor activity produced by BCL6. Recruited by ZBTB7A to the androgen response elements/ARE on target genes, negatively regulates androgen receptor signaling and androgen-induced cell proliferation. Mediates the …

**Summary**, from NCBI Gene [9611](https://www.ncbi.nlm.nih.gov/gene/9611):

> This gene encodes a protein that mediates ligand-independent transcription repression of thyroid-hormone and retinoic-acid receptors by promoting chromatin condensation and preventing access of the transcription machinery. It is part of a complex which also includes histone deacetylases and transcriptional regulators similar to the yeast protein Sin3p. This gene is located between the Charcot-Marie-Tooth and Smith-Magenis syndrome critical regions on chromosome 17. Alternate splicing results in …

**Accessions** — [HGNC:7672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7672) · Entrez [9611](https://www.ncbi.nlm.nih.gov/gene/9611) · UniProt [O75376](https://www.uniprot.org/uniprotkb/O75376) · Ensembl [ENSG00000141027](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141027)

## Data

Gene col 6482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6482); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6482]; `tensor/DDL_lfc|DDL_z.npy` [6482]; `embed/gene_vectors.npy` [6482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6482 or target_col == 6482). Every well: [[NCOR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
