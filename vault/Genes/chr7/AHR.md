---
symbol: "AHR"
type: "gene"
col: 2774
ensembl_id: "ENSG00000106546"
name: "aryl hydrocarbon receptor"
location: "7p21.1"
module: 66
arm: "+"
pooled_cpm: 195.33
n_lines_expressing: 43
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 18
direction_downstream: 37
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# AHR

*aryl hydrocarbon receptor* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +32.3, q 0e+00, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -10.7, q 4e-24, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCIM]] (+0.63, fdr 7e-06), [[SEMA3C]] (+0.62, fdr 7e-06), [[NR3C1]] (+0.62, fdr 8e-06); moves opposite to [[SLC30A6]] (-0.62, fdr 7e-06), [[GPR89A]] (-0.57, fdr 2e-05), [[RARS2]] (-0.56, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[SERPINE2]] → it (grade B ⚠); 37 go from it, the strongest it → [[ATXN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.36×** | +32.3 | 0e+00 | 34/41 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.03×** | +20.1 | 0e+00 | 37/41 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +17.2 | 0e+00 | 35/41 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +15.5 | 0e+00 | 38/41 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.05×** | +13.6 | 8e-40 | 36/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +12.0 | 4e-31 | 32/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +11.5 | 9e-29 | 36/42 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +10.6 | 1e-24 | 33/41 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +8.5 | 1e-15 | 28/41 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 2e-13 | 31/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.8 | 5e-10 | 25/41 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.7 | 9e-10 | 25/41 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.6 | 2e-09 | 25/41 (SW480, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.4 | 5e-09 | 29/42 (PANC-1, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.4 | 8e-09 | 24/41 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.2 | 3e-08 | 28/41 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -10.7 | 4e-24 | 28/42 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -7.7 | 3e-12 | 24/38 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.680×** | -7.2 | 9e-11 | 25/42 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -6.3 | 3e-08 | 0/43 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.9 | 9e-05 | 22/43 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.771×** | -4.7 | 2e-04 | 23/40 (SW 900, HepG2/C3A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.770×** | -4.6 | 3e-04 | 21/41 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.786×** | -4.5 | 4e-04 | 22/41 (HepG2/C3A, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.789×** | -4.3 | 0.001 | 20/41 (C32, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -3.8 | 0.007 | 17/42 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.011 | 19/41 (NCI-H460, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.013 | 19/41 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.770×** | -3.5 | 0.021 | 16/42 (NCI-H460, NCI-H2030, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.831×** | -3.5 | 0.022 | 17/41 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.705×** | -3.4 | 0.022 | 16/41 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.776×** | -3.4 | 0.025 | 18/41 (KATO III, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.881× | -3.4 | 0.027 | 14/41 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.029 | 18/41 (SNU-423, C32, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | 0.839× | -3.3 | 0.030 | 15/41 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.034 | 15/41 (KATO III, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.046 | 14/41 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.064 | 15/41 (HepG2/C3A, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 244 | 15 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +18.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.3) |
| [[PANC-1 (line)]] | alt | 86.3 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +40.6) | — |
| [[LoVo (line)]] | wt | 181 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +24.1) | — |
| [[SW480 (line)]] | alt | 76.2 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +21.8) | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +23.7) | — |
| [[LS 180 (line)]] | wt | 290 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 298 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +25.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.1) |
| [[SW 900 (line)]] | alt | 914 | 1 | 7 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 2.16× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -19.8) |
| [[SW1417 (line)]] | alt | 159 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +25.3) | — |
| [[C32 (line)]] | wt | 458 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 136 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +23.5) | — |
| [[Hs 766T (line)]] | wt | 78.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +16.9) | — |
| [[HS-578T (line)]] | alt | 195 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +21.2) | — |
| [[J82 (line)]] | alt | 133 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +21.4) | — |
| [[A549 (line)]] | wt | 163 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 390 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -12.2) |
| [[HT-29 (line)]] | alt | 148 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +22.4) | — |
| [[NCI-H2030 (line)]] | alt | 466 | 2 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.03× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -17.8) |
| [[RPMI-7951 (line)]] | alt | 219 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.2) | — |
| [[SK-MEL-2 (line)]] | alt | 143 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 68.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +14.5) | — |
| [[A498 (line)]] | wt | 187 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +24.7) | — |
| [[HEC-1-A (line)]] | alt | 61.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +20.1) | — |
| [[HOP62 (line)]] | alt | 84.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +18.8) | — |
| [[Panc 03.27 (line)]] | alt | 191 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.4) | — |
| [[SNU-423 (line)]] | alt | 320 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 223 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +23.5) | — |
| [[KATO III (line)]] | alt | 709 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.431× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 93.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +22.6) | — |
| [[A-427 (line)]] | wt | 232 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.7) |
| [[BT-474 (line)]] | alt | 268 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 288 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 74.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 57.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 224 | 1 | 1 | [[Cobimetinib (drug)]] 5 µM 2.54× (z +8.5) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.473× (z -10.0) |
| [[SHP-77 (line)]] | alt | 252 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.4) |
| [[CHP-212 (line)]] | wt | 396 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.2) | — |
| [[A-172 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 48.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCIM]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SEMA3C]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NR3C1]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ATP1B1]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[NCOA7]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CYP1B1]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Biological oxidations; STRING 763 |
| [[CDKN2B]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PLD1]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[KYNU]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NEDD9]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SYTL2]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[EID1]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[GPR89A]] | -0.57 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[RARS2]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[RABEPK]] | -0.54 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[EIF4ENIF1]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CWF19L1]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[DRD4]] | -0.52 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[TOP3A]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[DPH7]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PGS1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[DPY19L3]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[VPS53]] | -0.52 | -0.40 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE2]] | B | SERPINE2 activity raises AHR's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.74× lower at baseline in the lines without SERPINE2 | 0.001 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[DUSP10]] | B | DUSP10 activity raises AHR's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without DUSP10 | 0.006 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[PTGER4]] | B | PTGER4 activity raises AHR's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 3.22× lower at baseline in the lines without PTGER4 | 0.006 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[CXCL2]] | B | CXCL2 activity raises AHR's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without CXCL2 | 0.013 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[MEIS1]] | B | MEIS1 activity raises AHR's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 3.30× lower at baseline in the lines without MEIS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises AHR's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 2.81× lower at baseline in the lines without TNFRSF21 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[NR4A2]] | B | NR4A2 activity raises AHR's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 3.36× lower at baseline in the lines without NR4A2 | 0.021 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RPS6KA6]] | B | RPS6KA6 activity raises AHR's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without RPS6KA6 | 0.030 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |
| [[MEF2C]] | B | MEF2C activity raises AHR's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without MEF2C | 0.035 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[LXN]] | B | LXN activity raises AHR's level | lines that do not express LXN (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without LXN | 0.041 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[PLD1]] | B | PLD1 activity raises AHR's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.49× lower at baseline in the lines without PLD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[PLK2]] | B | PLK2 activity raises AHR's level | lines that do not express PLK2 (6) vs lines expressing it (44) | 3.92× lower at baseline in the lines without PLK2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, POLE |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 35, C 2. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1]] | B | AHR activity raises ATXN1's level | lines that do not express AHR (7) vs lines expressing it (43) | 4.48× lower at baseline in the lines without AHR | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[SMAD3]] | B | AHR activity raises SMAD3's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.02× lower at baseline in the lines without AHR | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[PTGER4]] | B | AHR activity raises PTGER4's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.35× lower at baseline in the lines without AHR | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | AHR activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | AHR activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | AHR activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[DUSP10]] | B | AHR activity raises DUSP10's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.96× lower at baseline in the lines without AHR | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ATP2B1]] | B | AHR activity raises ATP2B1's level | lines that do not express AHR (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without AHR | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[TNFRSF21]] | B | AHR activity raises TNFRSF21's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.95× lower at baseline in the lines without AHR | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| cells under [[Ralimetinib dimesylate (drug)]] 5 µM | B | AHR activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.82× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | AHR activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.77× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ARHGAP26]] | B | AHR activity raises ARHGAP26's level | lines that do not express AHR (7) vs lines expressing it (43) | 2.48× lower at baseline in the lines without AHR | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.6, 20.4); signed map (48.8, 23.2). **Vector** length 137, 45.9% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.8 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.3 | +11.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +20.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.7 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.2 | -0.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -6.5 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.7 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | aryl hydrocarbon receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:16,916,359-17,346,152 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHe76 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing |
| Hallmark sets | INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING |
| Reactome | 9 pathways, smallest: Aryl hydrocarbon receptor signalling; Xenobiotics; Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [P35869](https://www.uniprot.org/uniprotkb/P35869) (Aryl hydrocarbon receptor):

> Ligand-activated transcription factor that enables cells to adapt to changing conditions by sensing compounds from the environment, diet, microbiome and cellular metabolism, and which plays important roles in development, immunity and cancer. Upon ligand binding, translocates into the nucleus, where it heterodimerizes with ARNT and induces transcription by binding to xenobiotic response elements (XRE). Regulates a variety of biological processes, including angiogenesis, hematopoiesis, drug and …

**Summary**, from NCBI Gene [196](https://www.ncbi.nlm.nih.gov/gene/196):

> The protein encoded by this gene is a ligand-activated helix-loop-helix transcription factor involved in the regulation of biological responses to planar aromatic hydrocarbons. This receptor has been shown to regulate xenobiotic-metabolizing enzymes such as cytochrome P450. Before ligand binding, the encoded protein is sequestered in the cytoplasm; upon ligand binding, this protein moves to the nucleus and stimulates transcription of target genes. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:348) · Entrez [196](https://www.ncbi.nlm.nih.gov/gene/196) · UniProt [P35869](https://www.uniprot.org/uniprotkb/P35869) · Ensembl [ENSG00000106546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106546)

## Data

Gene col 2774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2774); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2774]; `tensor/DDL_lfc|DDL_z.npy` [2774]; `embed/gene_vectors.npy` [2774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2774 or target_col == 2774). Every well: [[AHR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
