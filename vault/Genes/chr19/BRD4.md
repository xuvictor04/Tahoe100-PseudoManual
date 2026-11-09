---
symbol: "BRD4"
type: "gene"
col: 6577
ensembl_id: "ENSG00000141867"
name: "bromodomain containing 4"
location: "19p13.12"
module: 173
arm: "+"
pooled_cpm: 273.44
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# BRD4

*bromodomain containing 4* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.61× (z +33.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.628× (z -11.6, q 1e-28, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIRBP]] (+0.66, fdr 7e-06), [[ZSCAN29]] (+0.64, fdr 2e-05), [[WASHC1]] (+0.61, fdr 2e-05); moves opposite to [[NHP2]] (-0.56, fdr 9e-05), [[TRAPPC1]] (-0.52, fdr 2e-04), [[L2HGDH]] (-0.51, fdr 4e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +33.9 | 0e+00 | 47/48 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.73×** | +17.2 | 0e+00 | 49/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +17.0 | 0e+00 | 47/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +16.4 | 0e+00 | 44/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +14.4 | 6e-45 | 46/48 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +10.5 | 6e-24 | 42/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +9.7 | 4e-20 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +9.5 | 2e-19 | 39/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +9.3 | 1e-18 | 39/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +7.8 | 4e-13 | 39/48 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.2 | 3e-11 | 38/48 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.5 | 3e-09 | 31/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +6.1 | 5e-08 | 38/48 (SW480, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 4e-07 | 31/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.16× | +5.3 | 5e-06 | 16/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.17× | +3.8 | 0.004 | 17/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +3.7 | 0.007 | 14/48 (SW480, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.011 | 12/47 (NCI-H23, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -11.6 | 1e-28 | 45/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -10.7 | 4e-24 | 44/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -9.3 | 3e-18 | 40/47 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -9.1 | 2e-17 | 42/48 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -7.5 | 7e-12 | 39/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.800×** | -5.6 | 2e-06 | 30/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.855× | -3.9 | 0.007 | 21/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[Glasdegib (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.857× | -3.8 | 0.008 | 12/48 (AsPC-1, C32, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.860× | -3.8 | 0.010 | 9/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.869× | -3.5 | 0.024 | 7/49 (NCI-H460, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 0.865× | -3.5 | 0.024 | 20/44 (NCI-H23, SK-MEL-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | 0.871× | -3.5 | 0.025 | 17/49 (RKO, LoVo, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.908× | -3.4 | 0.027 | 8/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.877× | -3.3 | 0.042 | 4/48 (AsPC-1, NCI-H661, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.062 | 3/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.884× | -3.0 | 0.098 | 13/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 270 | 10 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.538× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 235 | 12 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +33.1) | [[Panobinostat (drug)]] 0.5 µM 0.589× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 229 | 9 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +27.6) | [[Panobinostat (drug)]] 5 µM 0.480× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 211 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +25.5) | — |
| [[LOX-IMVI (line)]] | wt | 295 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +26.4) | [[Panobinostat (drug)]] 5 µM 0.550× (z -9.8) |
| [[SW480 (line)]] | alt | 284 | 8 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.08× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.605× (z -10.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.638× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 231 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +24.7) | [[Panobinostat (drug)]] 5 µM 0.500× (z -10.9) |
| [[C32 (line)]] | wt | 203 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +25.2) | — |
| [[BT-474 (line)]] | alt | 404 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +24.3) | [[Panobinostat (drug)]] 0.5 µM 0.524× (z -11.2) |
| [[HS-578T (line)]] | alt | 301 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +33.2) | — |
| [[NCI-H2347 (line)]] | alt | 248 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +21.5) | [[Panobinostat (drug)]] 0.5 µM 0.562× (z -10.1) |
| [[PANC-1 (line)]] | alt | 274 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +24.6) | [[Panobinostat (drug)]] 5 µM 0.495× (z -13.5) |
| [[RKO (line)]] | wt | 377 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -18.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 267 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +26.4) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.517× (z -10.8) |
| [[SNU-1 (line)]] | wt | 284 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.6) | — |
| [[SW 900 (line)]] | alt | 218 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +25.2) | — |
| [[SW48 (line)]] | wt | 290 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +20.5) | — |
| [[HEC-1-A (line)]] | alt | 244 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +22.8) | — |
| [[HOP62 (line)]] | alt | 233 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +31.6) | [[Panobinostat (drug)]] 0.5 µM 0.535× (z -10.3) |
| [[LS 180 (line)]] | wt | 267 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 370 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +19.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -8.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 336 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.518× (z -11.3) |
| [[A-172 (line)]] | wt | 254 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +27.4) | [[Panobinostat (drug)]] 0.5 µM 0.505× (z -11.7) |
| [[A549 (line)]] | wt | 213 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +29.8) | — |
| [[COLO 205 (line)]] | alt | 244 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +24.2) | — |
| [[Hs 766T (line)]] | wt | 173 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +23.4) | — |
| [[NCI-H2030 (line)]] | alt | 316 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +24.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.487× (z -11.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 465 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +20.4) | [[Panobinostat (drug)]] 5 µM 0.567× (z -9.6) |
| [[A498 (line)]] | wt | 302 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +25.6) | [[Panobinostat (drug)]] 5 µM 0.554× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 214 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +29.2) | — |
| [[H4 (line)]] | wt | 340 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +24.9) | — |
| [[HepG2_C3A (line)]] | wt | 367 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.462× (z -11.5) |
| [[J82 (line)]] | alt | 285 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.516× (z -12.2) |
| [[KATO III (line)]] | alt | 215 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.457× (z -11.9) |
| [[SNU-423 (line)]] | alt | 276 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +34.3) | — |
| [[HCT15 (line)]] | alt | 367 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 215 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 267 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.3) | — |
| [[RPMI-7951 (line)]] | alt | 289 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +22.9) | — |
| [[SW1417 (line)]] | alt | 283 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.580× (z -8.8) |
| [[A-427 (line)]] | wt | 300 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.64× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 300 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.18× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 279 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 238 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 355 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 359 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIRBP]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[WASHC1]] | +0.61 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[DXO]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MYL5]] | +0.59 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SIX5]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[KRCC1]] | +0.58 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[C19orf54]] | +0.58 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[ZNF213]] | +0.57 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[GFER]] | +0.57 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[CDK3]] | +0.57 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[ZCWPW1]] | +0.57 | +0.49 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHP2]] | -0.56 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[TRAPPC1]] | -0.52 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[L2HGDH]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[BRI3BP]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ATP5MC3]] ⚠ | -0.49 | -0.49 / -0.35 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BRD4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.7, 8.2); signed map (13.0, -21.7). **Vector** length 96.0, 33.2% of its response variance represented; |z| ≥ 3 in 1,393 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +33.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +8.0 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | +7.1 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.2 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.9 | +0.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.9 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.0 | +0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.5 | +3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.4 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | +14.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | +0.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.5 | -0.9 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.4 | +0.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -2.2 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,235,519-15,332,545 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUNKI, MCAP, CAP, HUNK1, FSHRG4 |
| Gene groups (HGNC) | Bromodomain and extra-terminal domain family; Bromodomain containing |
| Reactome | 8 pathways, smallest: Regulation of PD-L1(CD274) transcription; Potential therapeutics for SARS; Regulation of PD-L1(CD274) expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O60885](https://www.uniprot.org/uniprotkb/O60885) (Bromodomain-containing protein 4):

> Chromatin reader protein that recognizes and binds acetylated histones and plays a key role in transmission of epigenetic memory across cell divisions and transcription regulation. Remains associated with acetylated chromatin throughout the entire cell cycle and provides epigenetic memory for postmitotic G1 gene transcription by preserving acetylated chromatin status and maintaining high-order chromatin structure. During interphase, plays a key role in regulating the transcription of …

**Summary**, from NCBI Gene [23476](https://www.ncbi.nlm.nih.gov/gene/23476):

> The protein encoded by this gene is homologous to the murine protein MCAP, which associates with chromosomes during mitosis, and to the human RING3 protein, a serine/threonine kinase. Each of these proteins contains two bromodomains, a conserved sequence motif which may be involved in chromatin targeting. This gene has been implicated as the chromosome 19 target of translocation t(15;19)(q13;p13.1), which defines an upper respiratory tract carcinoma in young people. Two alternatively spliced …

**Accessions** — [HGNC:13575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13575) · Entrez [23476](https://www.ncbi.nlm.nih.gov/gene/23476) · UniProt [O60885](https://www.uniprot.org/uniprotkb/O60885) · Ensembl [ENSG00000141867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141867)

## Data

Gene col 6577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6577); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6577]; `tensor/DDL_lfc|DDL_z.npy` [6577]; `embed/gene_vectors.npy` [6577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6577 or target_col == 6577). Every well: [[BRD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
