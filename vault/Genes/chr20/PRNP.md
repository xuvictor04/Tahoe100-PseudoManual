---
symbol: "PRNP"
type: "gene"
col: 10180
ensembl_id: "ENSG00000171867"
name: "prion protein (Kanno blood group)"
location: "20p13"
module: 3
arm: "-"
pooled_cpm: 74.21
n_lines_expressing: 47
n_dd_up: 32
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PRNP

*prion protein (Kanno blood group)* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.34× (z +15.2, q 0e+00, up in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.25× (z +14.5, q 1e-45, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.398× (z -16.5, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A1]] (+0.64, fdr 1e-05), [[RCC2]] (+0.59, fdr 5e-05), [[ARSB]] (+0.57, fdr 8e-05); moves opposite to [[TMEM256]] (-0.62, fdr 6e-05), [[NDUFB10]] (-0.61, fdr 2e-04), [[METTL26]] (-0.58, fdr 2e-04).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HSPA13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +15.2 | 0e+00 | 39/45 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +14.5 | 1e-45 | 44/45 (BT-474, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +13.3 | 4e-38 | 42/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +12.2 | 4e-32 | 42/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +11.5 | 2e-28 | 30/39 (A549, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +10.5 | 7e-24 | 39/44 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.74×** | +10.0 | 2e-21 | 40/45 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.5 | 1e-19 | 32/46 (A549, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +9.2 | 1e-18 | 39/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +8.8 | 7e-17 | 30/41 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +8.3 | 5e-15 | 35/45 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.5 | 3e-09 | 33/44 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.39×** | +5.8 | 2e-07 | 29/45 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.80×** | +5.5 | 2e-06 | 33/45 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.36×** | +5.5 | 2e-06 | 30/45 (SW480, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.7 | 1e-04 | 19/45 (A549, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +4.4 | 4e-04 | 22/45 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +4.3 | 6e-04 | 23/45 (PANC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.001 | 21/45 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.001 | 18/46 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.005 | 17/44 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.005 | 19/45 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.010 | 19/46 (C32, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -16.5 | 0e+00 | 44/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.402×** | -16.4 | 0e+00 | 44/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.404×** | -16.3 | 0e+00 | 45/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -7.7 | 2e-12 | 32/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.528×** | -6.0 | 2e-07 | 31/46 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.764×** | -4.7 | 2e-04 | 26/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.772×** | -4.7 | 3e-04 | 24/45 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.817×** | -4.6 | 3e-04 | 21/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.770×** | -4.5 | 4e-04 | 24/44 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.791×** | -4.2 | 0.002 | 22/46 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.862× | -3.7 | 0.011 | 21/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.026 | 23/46 (HepG2/C3A, C32, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.027 | 18/46 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.874× | -3.3 | 0.038 | 14/46 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.834× | -3.3 | 0.038 | 15/45 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.038 | 14/45 (CFPAC-1, LS 180, …) | top dose only | plate-row cell shift; position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **0.825×** | -3.2 | 0.041 | 8/45 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 279 | 0 | 15 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.360× (z -31.5) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -13.1) |
| [[SNU-423 (line)]] | alt | 62.3 | 9 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.78× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.252× (z -13.6) |
| [[HOP62 (line)]] | alt | 115 | 7 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -10.6) |
| [[SW480 (line)]] | alt | 87.7 | 5 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.24× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.248× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 84.1 | 5 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.319× (z -13.9) |
| [[A-172 (line)]] | wt | 99.7 | 6 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.16× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.360× (z -10.2) |
| [[A549 (line)]] | wt | 48.0 | 6 (5 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -8.6) |
| [[A498 (line)]] | wt | 83.4 | 1 | 5 | [[Auranofin (drug)]] 5 µM 2.04× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 105 | 4 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -9.7) |
| [[HS-578T (line)]] | alt | 117 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.362× (z -11.3) |
| [[PANC-1 (line)]] | alt | 61.2 | 3 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.75× (z +13.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.355× (z -13.9) |
| [[SW 900 (line)]] | alt | 78.0 | 3 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.63× (z +9.9) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.344× (z -11.0) |
| [[BT-474 (line)]] | alt | 33.7 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.41× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 36.9 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.40× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.88× (z +8.8) | [[Adagrasib (drug)]] 0.05 µM 0.661× (z -11.6) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 262 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.17× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 51.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 47.9 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.53× (z +8.6) ⚠ unreliable plate only | [[Belinostat (drug)]] 5 µM 0.213× (z -14.1) |
| [[KATO III (line)]] | alt | 75.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.298× (z -13.9) |
| [[RKO (line)]] | wt | 73.0 | 1 (1 ⚠) | 3 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.68× (z +10.2) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.205× (z -17.1) |
| [[C32 (line)]] | wt | 189 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.317× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 48.2 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.33× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -9.4) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -10.8) |
| [[J82 (line)]] | alt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.36× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -9.8) |
| [[SNU-1 (line)]] | wt | 80.8 | 2 | 1 | [[Auranofin (drug)]] 5 µM 3.77× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.336× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 39.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 65.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.3) | — |
| [[LoVo (line)]] | wt | 26.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.43× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 47.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.1) | — |
| [[H4 (line)]] | wt | 125 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -9.3) |
| [[HCT15 (line)]] | alt | 67.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.55× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.87× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 74.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -9.0) |
| [[SW 1088 (line)]] | alt | 117 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.100× (z -9.3) |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.322× (z -9.8) |
| [[SW48 (line)]] | wt | 53.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -8.7) |
| [[A-427 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 164 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A1]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[RCC2]] | +0.59 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[ARSB]] | +0.57 | +0.37 / +0.40 | both halves | 8e-05 |  |
| [[EPM2A]] | +0.56 | +0.33 / +0.36 | both halves | 1e-04 |  |
| [[MSANTD2]] | +0.56 | +0.42 / +0.32 | both halves | 2e-04 |  |
| [[ASB1]] | +0.55 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[SERPINB8]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[CYP4V2]] | +0.54 | +0.38 / +0.38 | both halves | 6e-05 |  |
| [[CRPPA]] | +0.54 | +0.37 / +0.29 | both halves | 3e-04 |  |
| [[TOR1A]] | +0.54 | +0.46 / +0.33 | both halves | 1e-04 |  |
| [[HCFC1]] | +0.54 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[VLDLR-AS1]] | +0.53 | +0.35 / +0.43 | both halves | 1e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM256]] | -0.62 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[NDUFB10]] | -0.61 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[METTL26]] | -0.58 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ATP5MJ]] | -0.57 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ATP5ME]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[HEATR5B]] | -0.56 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[POLR2I]] | -0.55 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[HDGFL2]] | -0.55 | -0.28 / -0.41 | both halves | 3e-04 |  |
| [[TARS2]] | -0.54 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ARL3]] | -0.54 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[RANBP10]] | -0.54 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[EMC2]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 | pathway: Protein localization |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PRNP's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSPA13]] | C | PRNP activity raises HSPA13's level | lines that do not express PRNP (3) vs lines expressing it (47) | 5.69× lower at baseline in the lines without PRNP | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TFAP2A, ADAMTSL5, KDELR3; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.9, -14.4); signed map (23.1, -30.1). **Vector** length 117, 37.4% of its response variance represented; |z| ≥ 3 in 1,409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.7 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.9 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.3 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.8 | -16.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.6 | -16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -16.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | prion protein (Kanno blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:4,686,350-4,701,590 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD230, PRP, AltPrP; previously PRIP, GSS, CJD |
| Gene groups (HGNC) | Blood group antigens; CD molecules |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, MYOGENESIS, IL2_STAT5_SIGNALING |
| Reactome | 6 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; NCAM1 interactions; NCAM signaling for neurite out-growth |
| Matched by | ensembl_id |

UniProt [F7VJQ1](https://www.uniprot.org/uniprotkb/F7VJQ1) carries no function annotation.

**Summary**, from NCBI Gene [5621](https://www.ncbi.nlm.nih.gov/gene/5621):

> The protein encoded by this gene is a membrane glycosylphosphatidylinositol-anchored glycoprotein that tends to aggregate into rod-like structures. The encoded protein contains a highly unstable region of five tandem octapeptide repeats. This gene is found on chromosome 20, approximately 20 kbp upstream of a gene which encodes a biochemically and structurally similar protein to the one encoded by this gene. Mutations in the repeat region as well as elsewhere in this gene have been associated …

**Accessions** — [HGNC:9449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9449) · Entrez [5621](https://www.ncbi.nlm.nih.gov/gene/5621) · UniProt [F7VJQ1](https://www.uniprot.org/uniprotkb/F7VJQ1) · Ensembl [ENSG00000171867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171867)

## Data

Gene col 10180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10180); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10180]; `tensor/DDL_lfc|DDL_z.npy` [10180]; `embed/gene_vectors.npy` [10180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10180 or target_col == 10180). Every well: [[PRNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
