---
symbol: "FOXO3"
type: "gene"
col: 4012
ensembl_id: "ENSG00000118689"
name: "forkhead box O3"
location: "6q21"
module: 74
arm: "+"
pooled_cpm: 244.82
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# FOXO3

*forkhead box O3* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +16.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.257× (z -23.7, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.790× (z -5.8, q 4e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB10]] (+0.59, fdr 1e-05), [[PNRC1]] (+0.59, fdr 2e-05), [[PIK3IP1]] (+0.59, fdr 1e-05); moves opposite to [[PSMD1]] (-0.60, fdr 1e-05), [[TMX3]] (-0.59, fdr 1e-05), [[HERC2P9-1]] (-0.58, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +16.3 | 0e+00 | 44/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +7.0 | 8e-10 | 35/49 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 2e-05 | 32/48 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +5.3 | 2e-05 | 29/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.6 | 4e-04 | 23/49 (KATO III, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 8e-04 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +4.0 | 0.006 | 23/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.24×** | +3.9 | 0.006 | 26/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.013 | 26/48 (Panc 03.27, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.6 | 0.018 | 24/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.030 | 18/48 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.030 | 27/48 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.047 | 19/48 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.20× | +3.2 | 0.063 | 19/50 (HT-29, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.065 | 18/48 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.0 | 0.094 | 20/49 (PANC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.257×** | -23.7 | 0e+00 | 44/44 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.284×** | -22.9 | 0e+00 | 48/49 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.341×** | -18.1 | 0e+00 | 44/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.588×** | -9.7 | 6e-20 | 41/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.555×** | -9.6 | 7e-20 | 41/48 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.679×** | -6.8 | 1e-09 | 37/47 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.715×** | -5.9 | 3e-07 | 38/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -5.8 | 4e-07 | 28/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.796×** | -5.7 | 1e-06 | 28/49 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -5.1 | 2e-05 | 33/48 (LoVo, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.761×** | -5.0 | 3e-05 | 30/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.764×** | -4.9 | 4e-05 | 30/48 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.758×** | -4.9 | 5e-05 | 35/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.770×** | -4.8 | 8e-05 | 32/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.763×** | -4.7 | 8e-05 | 31/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.658×** | -4.0 | 0.002 | 26/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.660×** | -4.0 | 0.002 | 29/47 (CHP-212, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.003 | 30/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.822×** | -3.6 | 0.009 | 26/49 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.822×** | -3.6 | 0.009 | 26/48 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.015 | 23/48 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.831×** | -3.4 | 0.016 | 21/48 (NCI-H2030, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.876× | -3.3 | 0.020 | 8/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.023 | 21/49 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.023 | 21/47 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.878× | -3.2 | 0.028 | 10/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.843× | -3.1 | 0.034 | 19/49 (H4, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 226 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -16.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 186 | 2 (1 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[TAK-733 (drug)]] 5 µM 0.269× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 416 | 1 | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -23.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 246 | 4 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +16.4) | [[Auranofin (drug)]] 5 µM 0.250× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 186 | 0 | 8 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -16.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SNU-423 (line)]] | alt | 522 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -28.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 192 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -15.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 454 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -21.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 250 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.19× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -18.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 219 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -17.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 347 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -17.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 165 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.7) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.465× (z -10.1) |
| [[LS 180 (line)]] | wt | 234 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +20.0) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 272 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -17.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 360 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -26.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 143 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -17.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 382 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 104 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +18.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.381× (z -11.8) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 224 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -16.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 366 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -18.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 239 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -19.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 317 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.0880× (z -28.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 115 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +32.5) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 309 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -24.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 225 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -17.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 281 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -25.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 152 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -15.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 218 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -16.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 246 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 146 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -18.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 399 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0834× (z -26.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 280 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 293 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.2) | [[Ixazomib citrate (drug)]] 5 µM 0.379× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 271 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -13.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 223 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 166 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -21.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 226 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -15.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 286 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -15.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 341 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -20.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 149 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +15.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -9.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 252 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB10]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[PNRC1]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[PIK3IP1]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MXI1]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM; STRING 757 |
| [[UBE2B]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[GAB1]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[ZRANB1]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[HDAC5]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[CDKN1C]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA |
| [[IRS2]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA; STRING 681 |
| [[GADD45B]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD1]] | -0.60 | -0.63 / -0.54 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[TMX3]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TIMM23B-AGAP6]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PCDHGC3]] | -0.55 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[TRRAP]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[C2CD3]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[EFTUD2]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NUP155]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[UGGT1]] | -0.52 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[EMC1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FOXO3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PARD6B]] | B | PARD6B activity raises FOXO3's level | lines that do not express PARD6B (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without PARD6B | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC120, ENSG00000291079, MERTK; maybe low, not absent |
| [[CDKN1C]] | B | CDKN1C activity raises FOXO3's level | lines that do not express CDKN1C (8) vs lines expressing it (42) | 1.11× lower at baseline in the lines without CDKN1C | 0.084 | ⚠ within organs, on part of the lines; also absent: MAP3K9, CARD10, TESMIN; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, -38.9); signed map (-8.3, 11.3). **Vector** length 112, 41.0% of its response variance represented; |z| ≥ 3 in 1,490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.1 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.5 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | -0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box O3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:108,559,835-108,684,774 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF6q21, FOXO2; previously FKHRL1, FOXO3A |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | HEME_METABOLISM, HYPOXIA, P53_PATHWAY |
| Reactome | 32 pathways, smallest: RUNX3 regulates BCL2L11 (BIM) transcription; AKT phosphorylates targets in the nucleus; Regulation of FOXO transcriptional activity by acetylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43524](https://www.uniprot.org/uniprotkb/O43524) (Forkhead box protein O3):

> Transcriptional activator that recognizes and binds to the DNA sequence 5'-[AG]TAAA[TC]A-3' and regulates different processes, such as apoptosis and autophagy. Acts as a positive regulator of autophagy in skeletal muscle: in starved cells, enters the nucleus following dephosphorylation and binds the promoters of autophagy genes, such as GABARAP1L, MAP1LC3B and ATG12, thereby activating their expression, resulting in proteolysis of skeletal muscle proteins (By similarity). Triggers apoptosis in …

**Summary**, from NCBI Gene [2309](https://www.ncbi.nlm.nih.gov/gene/2309):

> This gene belongs to the forkhead family of transcription factors which are characterized by a distinct forkhead domain. This gene likely functions as a trigger for apoptosis through expression of genes necessary for cell death. Translocation of this gene with the MLL gene is associated with secondary acute leukemia. Alternatively spliced transcript variants encoding the same protein have been observed. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3821) · Entrez [2309](https://www.ncbi.nlm.nih.gov/gene/2309) · UniProt [O43524](https://www.uniprot.org/uniprotkb/O43524) · Ensembl [ENSG00000118689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118689)

## Data

Gene col 4012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4012); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4012]; `tensor/DDL_lfc|DDL_z.npy` [4012]; `embed/gene_vectors.npy` [4012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4012 or target_col == 4012). Every well: [[FOXO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
