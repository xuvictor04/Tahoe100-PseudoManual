---
symbol: "ADNP"
type: "gene"
col: 2073
ensembl_id: "ENSG00000101126"
name: "activity dependent neuroprotector homeobox"
location: "20q13.13"
module: 51
arm: "+"
pooled_cpm: 257.62
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ADNP

*activity dependent neuroprotector homeobox* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.83× (z +19.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.347× (z -33.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPC1]] (+0.72, fdr 7e-06), [[SCAF8]] (+0.64, fdr 2e-05), [[LYRM2]] (+0.63, fdr 7e-05); moves opposite to [[SETD3]] (-0.65, fdr 3e-05), [[NAPB]] (-0.59, fdr 1e-05), [[ENTPD4]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +19.2 | 0e+00 | 44/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +17.9 | 0e+00 | 41/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +17.5 | 0e+00 | 48/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +15.9 | 0e+00 | 44/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +15.8 | 0e+00 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +14.0 | 8e-43 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +13.0 | 8e-37 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +10.1 | 3e-22 | 30/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +6.5 | 5e-09 | 25/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.6 | 1e-06 | 21/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +4.8 | 8e-05 | 36/48 (A498, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.14× | +4.2 | 0.001 | 21/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.015 | 13/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.08× | +3.3 | 0.034 | 6/48 (SNU-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.11× | +3.2 | 0.049 | 12/48 (HT-29, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.347×** | -33.6 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.346×** | -32.4 | 0e+00 | 44/44 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.371×** | -31.6 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.398×** | -29.3 | 0e+00 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -27.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -16.3 | 0e+00 | 36/49 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.605×** | -16.0 | 0e+00 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -15.8 | 0e+00 | 48/50 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.549×** | -14.3 | 1e-44 | 40/45 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -14.0 | 1e-42 | 45/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.729×** | -10.0 | 5e-22 | 43/48 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.762×** | -8.6 | 3e-16 | 37/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.622×** | -7.7 | 8e-13 | 45/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -6.8 | 4e-10 | 18/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.801×** | -6.8 | 5e-10 | 31/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -5.7 | 4e-07 | 16/48 (SNU-1, A-427, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.865× | -4.6 | 1e-04 | 17/49 (NCI-H2347, NCI-H23, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.765×** | -4.3 | 4e-04 | 28/49 (RKO, J82, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.003 | 23/48 (HT-29, RKO, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 261 | 13 (6 ⚠) | 9 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.05× (z +22.7) | [[Panobinostat (drug)]] 5 µM 0.284× (z -25.6) |
| [[PANC-1 (line)]] | alt | 213 | 8 (1 ⚠) | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -27.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.366× (z -23.5) |
| [[SW1417 (line)]] | alt | 436 | 4 (1 ⚠) | 12 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -18.8) |
| [[SW480 (line)]] | alt | 318 | 6 (1 ⚠) | 10 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.10× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -34.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.282× (z -30.9) |
| [[RKO (line)]] | wt | 357 | 6 (1 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.345× (z -18.8) |
| [[HT-29 (line)]] | alt | 322 | 4 (1 ⚠) | 10 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.268× (z -24.7) |
| [[NCI-H1792 (line)]] | alt | 283 | 5 (1 ⚠) | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.329× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 199 | 5 (1 ⚠) | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -33.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.333× (z -18.8) |
| [[SNU-1 (line)]] | wt | 364 | 7 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -16.9) |
| [[C32 (line)]] | wt | 336 | 6 (2 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 242 | 4 (1 ⚠) | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.95× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.373× (z -20.3) |
| [[LoVo (line)]] | wt | 181 | 7 (2 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +21.3) | [[Belinostat (drug)]] 5 µM 0.399× (z -17.8) |
| [[LS 180 (line)]] | wt | 204 | 6 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +20.8) | [[Panobinostat (drug)]] 5 µM 0.380× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 233 | 4 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.315× (z -23.7) |
| [[A498 (line)]] | wt | 207 | 6 (3 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +21.1) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.412× (z -15.8) |
| [[C-33 A (line)]] | alt | 378 | 3 | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.268× (z -21.1) |
| [[HOP62 (line)]] | alt | 255 | 4 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.05× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.341× (z -18.2) |
| [[KATO III (line)]] | alt | 278 | 6 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.356× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 251 | 3 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 411 | 3 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.18× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.334× (z -19.5) |
| [[SNU-423 (line)]] | alt | 267 | 4 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.81× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -18.8) |
| [[SW48 (line)]] | wt | 294 | 6 (1 ⚠) | 6 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.69× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.272× (z -16.5) |
| [[A-172 (line)]] | wt | 244 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -23.2) |
| [[AsPC-1 (line)]] | alt | 218 | 6 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +15.9) | [[Belinostat (drug)]] 5 µM 0.326× (z -16.7) |
| [[HEC-1-A (line)]] | alt | 246 | 3 (1 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +18.6) | [[Panobinostat (drug)]] 5 µM 0.266× (z -25.0) |
| [[Hs 766T (line)]] | wt | 268 | 5 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 281 | 5 (1 ⚠) | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.25× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.331× (z -17.1) |
| [[A-427 (line)]] | wt | 215 | 3 (1 ⚠) | 7 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.73× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -35.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.464× (z -13.5) |
| [[COLO 205 (line)]] | alt | 261 | 5 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.347× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 232 | 4 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.371× (z -18.5) |
| [[A549 (line)]] | wt | 187 | 4 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.431× (z -15.1) |
| [[J82 (line)]] | alt | 343 | 1 | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.57× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.483× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 228 | 2 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.79× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.310× (z -20.0) |
| [[SW 900 (line)]] | alt | 252 | 1 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.76× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.347× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 227 | 2 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 174 | 3 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.352× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 232 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.28× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -19.0) |
| [[SK-MEL-2 (line)]] | alt | 250 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.391× (z -16.6) |
| [[BT-474 (line)]] | alt | 308 | 2 (1 ⚠) | 5 | [[Peretinoin (drug)]] 5 µM 1.77× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.269× (z -22.3) |
| [[SHP-77 (line)]] | alt | 247 | 3 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.32× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.342× (z -14.8) |
| [[HS-578T (line)]] | alt | 171 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.461× (z -11.9) |
| [[AN3 CA (line)]] | alt | 299 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.353× (z -10.0) |
| [[CHP-212 (line)]] | wt | 301 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -12.6) |
| [[H4 (line)]] | wt | 202 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -15.5) |
| [[NCI-H661 (line)]] | alt | 345 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -10.1) |
| [[HCT15 (line)]] | alt | 185 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.498× (z -8.8) |
| [[SW 1271 (line)]] | alt | 220 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0605× (z -18.4) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.210× (z -10.3) |
| [[SW 1088 (line)]] | alt | 242 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -11.5) |
| [[NCI-H2122 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 275 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPC1]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SCAF8]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 | STRING 497 |
| [[LYRM2]] | +0.63 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[STAG1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[WARS2]] | +0.62 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[ZCCHC3]] | +0.62 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[KMT5B]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 | STRING 713 |
| [[INO80]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[BRAF]] | +0.61 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[YJU2]] | +0.61 | +0.37 / +0.61 | both halves | 9e-05 |  |
| [[ZFY]] | +0.61 | +0.41 / +0.62 | both halves | 4e-05 | same gene group |
| [[RBM23]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.65 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[NAPB]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ENTPD4]] | -0.59 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.57 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[ORMDL3]] | -0.56 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GSDMB]] | -0.55 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[PIGN]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[AKTIP]] | -0.52 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[ECI2]] | -0.52 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[PLEKHA8]] | -0.52 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[BCAP31]] | -0.52 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[HYOU1]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ADNP's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.2, 12.4); signed map (12.3, -31.8). **Vector** length 105, 38.8% of its response variance represented; |z| ≥ 3 in 1,604 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +11.2 | -0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +17.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.8 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +13.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -5.4 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.0 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -16.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -3.1 | +0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -3.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | activity dependent neuroprotector homeobox |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,888,916-50,931,437 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0784, ADNP1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Reactome | 5 pathways, smallest: ChAHP complex assembly; CHD3, CHD4, CHD5 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2P0](https://www.uniprot.org/uniprotkb/Q9H2P0) (Activity-dependent neuroprotector homeobox protein):

> May be involved in transcriptional regulation. May mediate some of the neuroprotective peptide VIP-associated effects involving normal growth and cancer proliferation. Positively modulates WNT-beta-catenin/CTNN1B signaling, acting by regulating phosphorylation of, and thereby stabilizing, CTNNB1. May be required for neural induction and neuronal differentiation. May be involved in erythroid differentiation (By similarity).

**Summary**, from NCBI Gene [23394](https://www.ncbi.nlm.nih.gov/gene/23394):

> Vasoactive intestinal peptide is a neuroprotective factor that has a stimulatory effect on the growth of some tumor cells and an inhibitory effect on others. This gene encodes a protein that is upregulated by vasoactive intestinal peptide and may be involved in its stimulatory effect on certain tumor cells. The encoded protein contains one homeobox and nine zinc finger domains, suggesting that it functions as a transcription factor. This gene is also upregulated in normal proliferative tissues. …

**Accessions** — [HGNC:15766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15766) · Entrez [23394](https://www.ncbi.nlm.nih.gov/gene/23394) · UniProt [Q9H2P0](https://www.uniprot.org/uniprotkb/Q9H2P0) · Ensembl [ENSG00000101126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101126)

## Data

Gene col 2073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2073); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2073]; `tensor/DDL_lfc|DDL_z.npy` [2073]; `embed/gene_vectors.npy` [2073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2073 or target_col == 2073). Every well: [[ADNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
