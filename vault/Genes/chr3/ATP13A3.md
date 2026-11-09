---
symbol: "ATP13A3"
type: "gene"
col: 5463
ensembl_id: "ENSG00000133657"
name: "ATPase 13A3"
location: "3q29"
module: 78
arm: "+"
pooled_cpm: 352.08
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 17
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ATP13A3

*ATPase 13A3* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.62× (z +14.3, q 1e-43, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.657× (z -6.2, q 3e-07, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NT5E]] (+0.67, fdr 7e-06), [[SEPTIN10]] (+0.61, fdr 1e-05), [[SHB]] (+0.61, fdr 1e-05); moves opposite to [[SLC4A1AP]] (-0.57, fdr 1e-05), [[DNAJB4]] (-0.56, fdr 3e-05), [[CMKLR2]] (-0.56, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[MME]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.62×** | +14.3 | 1e-43 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +10.7 | 2e-24 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.87×** | +10.5 | 2e-23 | 47/49 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +10.1 | 7e-22 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +9.8 | 2e-20 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +6.4 | 2e-08 | 43/48 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.2 | 6e-08 | 34/47 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +5.0 | 5e-05 | 27/48 (A-172, A498, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 8e-05 | 32/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.8 | 9e-05 | 35/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.5 | 4e-04 | 29/38 (A-172, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.4 | 5e-04 | 31/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 27/48 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.0 | 0.003 | 32/48 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.013 | 34/48 (Hs 766T, PANC-1, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.657×** | -6.2 | 3e-07 | 38/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -5.7 | 3e-06 | 26/44 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -5.5 | 6e-06 | 35/47 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.744×** | -5.2 | 4e-05 | 36/48 (NCI-H23, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.734×** | -4.4 | 0.001 | 32/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.749×** | -4.3 | 0.002 | 28/49 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.813×** | -4.2 | 0.002 | 26/49 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.753×** | -4.2 | 0.002 | 36/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 0.002 | 34/48 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.762×** | -4.0 | 0.004 | 28/49 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.773×** | -3.8 | 0.008 | 27/47 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.030 | 28/48 (KATO III, CHP-212, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.826×** | -3.4 | 0.030 | 23/50 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.031 | 25/47 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.3 | 0.031 | 21/49 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.814×** | -3.3 | 0.035 | 27/49 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.815×** | -3.0 | 0.076 | 22/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.076 | 28/49 (NCI-H1792, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 450 | 11 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +21.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.4× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -11.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 321 | 7 (3 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.32× (z +13.0) | [[Trametinib (drug)]] 5 µM 0.393× (z -9.0) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.381× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 291 | 0 | 11 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.633× (z -18.1) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 0.445× (z -10.8) |
| [[BT-474 (line)]] | alt | 179 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 339 | 5 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.03× (z +13.2) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.296× (z -9.6) |
| [[SW480 (line)]] | alt | 256 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +21.5) | — |
| [[HepG2_C3A (line)]] | wt | 187 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +15.2) | — |
| [[Hs 766T (line)]] | wt | 189 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 36.7× (z +17.3) | — |
| [[HS-578T (line)]] | alt | 1,036 | 2 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.93× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.383× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 554 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 314 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 1,076 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 186 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 477 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.95× (z +18.5) | — |
| [[SNU-1 (line)]] | wt | 231 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 932 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 312 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +15.7) | — |
| [[A498 (line)]] | wt | 616 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.6) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.84× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 160 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 247 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +14.7) | — |
| [[KATO III (line)]] | alt | 205 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 551 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 370 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.76× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 311 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.28× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 510 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.400× (z -8.5) |
| [[SW1417 (line)]] | alt | 241 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 198 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.7) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.4× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 157 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.03× (z +15.2) | — |
| [[H4 (line)]] | wt | 425 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.52× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -8.7) ⚠ toxic |
| [[LS 180 (line)]] | wt | 200 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.8) | — |
| [[RKO (line)]] | wt | 467 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 307 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.8) | — |
| [[A549 (line)]] | wt | 287 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 212 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 171 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 110 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 427 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 211 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 232 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 282 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 513 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 556 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 215 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5E]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SHB]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PLGRKT]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[CD44]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LIF]] | +0.57 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[UXS1]] | +0.56 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[RUNX1]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MICAL2]] | +0.56 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[DNAJB4]] | -0.56 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[CMKLR2]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[THAP3]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[UBR2]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[FNBP4]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[DCTN6]] | -0.52 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[CCDC43]] | -0.51 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RPRD2]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MTRFR]] | -0.50 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SNW1]] | -0.50 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ERCC5]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MME]] | B | MME activity raises ATP13A3's level | lines that do not express MME (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without MME | 0.008 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[KCNMA1]] | B | KCNMA1 activity raises ATP13A3's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 1.72× lower at baseline in the lines without KCNMA1 | 0.011 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ETS1]] | B | ETS1 activity raises ATP13A3's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ETS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[VEGFC]] | B | VEGFC activity raises ATP13A3's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 1.69× lower at baseline in the lines without VEGFC | 0.031 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises ATP13A3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[NLRP3]] | B | NLRP3 activity raises ATP13A3's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 1.80× lower at baseline in the lines without NLRP3 | 0.045 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[KIRREL3]] | B | KIRREL3 activity raises ATP13A3's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 1.74× lower at baseline in the lines without KIRREL3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[KIAA1549L]] | B | KIAA1549L activity raises ATP13A3's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without KIAA1549L | 0.070 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[FHOD3]] | B | FHOD3 activity raises ATP13A3's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without FHOD3 | 0.082 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| [[CD59]] | B | CD59 activity raises ATP13A3's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without CD59 | 0.087 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[SPOCK1]] | B | SPOCK1 activity raises ATP13A3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without SPOCK1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[KIRREL1]] | B | KIRREL1 activity raises ATP13A3's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without KIRREL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.3, 6.7); signed map (5.3, 44.7). **Vector** length 113, 47.0% of its response variance represented; |z| ≥ 3 in 1,683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | +0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.5 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | +0.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.1 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase 13A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:194,402,672-194,498,364 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AFURS1 |
| Gene groups (HGNC) | ATPase orphan transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7F0](https://www.uniprot.org/uniprotkb/Q9H7F0) (Polyamine-transporting ATPase 13A3):

> ATP-driven pump involved in endocytosis-dependent polyamine transport. Uses ATP as an energy source to transfer polyamine precursor putrescine from the endosomal compartment to the cytosol.

**Summary**, from NCBI Gene [79572](https://www.ncbi.nlm.nih.gov/gene/79572):

> ATP13A3 is a member of the P-type ATPase family of proteins that transport a variety of cations across membranes. Other P-type ATPases include ATP7B (MIM 606882) and ATP7A (MIM 300011).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:24113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24113) · Entrez [79572](https://www.ncbi.nlm.nih.gov/gene/79572) · UniProt [Q9H7F0](https://www.uniprot.org/uniprotkb/Q9H7F0) · Ensembl [ENSG00000133657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133657)

## Data

Gene col 5463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5463); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5463]; `tensor/DDL_lfc|DDL_z.npy` [5463]; `embed/gene_vectors.npy` [5463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5463 or target_col == 5463). Every well: [[ATP13A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP13A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
