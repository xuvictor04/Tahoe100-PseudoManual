---
symbol: "MYO9A"
type: "gene"
col: 844
ensembl_id: "ENSG00000066933"
name: "myosin IXA"
location: "15q23"
module: 20
arm: "-"
pooled_cpm: 238.86
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 32
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MYO9A

*myosin IXA* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.41× (z +6.4, q 1e-07, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.446× (z -15.5, q 0e+00, down in 44 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.527× (z -12.3, q 8e-33, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FER]] (+0.62, fdr 1e-05), [[SCAPER]] (+0.59, fdr 3e-05), [[RSPH3]] (+0.55, fdr 1e-05); moves opposite to [[TMSB15B]] (-0.57, fdr 2e-05), [[LINC03009]] (-0.55, fdr 3e-05), [[DTX2P1]] (-0.49, fdr 5e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-07 | 41/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +5.4 | 2e-05 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.009 | 26/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.24×** | +4.0 | 0.009 | 25/50 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.053 | 15/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.077 | 28/50 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.077 | 18/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.11 | 17/48 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.11 | 13/48 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 844.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.446×** | -15.5 | 0e+00 | 44/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.588×** | -14.4 | 2e-44 | 38/48 (SNU-423, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.445×** | -14.4 | 2e-44 | 42/45 (NCI-H23, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.480×** | -14.1 | 7e-43 | 45/49 (HCT15, A-172, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.500×** | -13.3 | 4e-38 | 43/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.489×** | -13.2 | 1e-37 | 45/47 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.509×** | -12.5 | 1e-33 | 39/44 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -12.3 | 8e-33 | 42/48 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.297×** | -12.2 | 3e-32 | 49/49 (RPMI-7951, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.548×** | -11.1 | 8e-27 | 37/48 (SNU-423, RPMI-7951, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.553×** | -10.9 | 6e-26 | 41/47 (LoVo, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.594×** | -10.0 | 8e-22 | 40/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.599×** | -9.8 | 4e-21 | 46/48 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -7.9 | 1e-13 | 42/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **0.693×** | -7.0 | 9e-11 | 39/48 (PANC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -6.9 | 2e-10 | 40/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.697×** | -6.9 | 2e-10 | 30/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.704×** | -6.7 | 5e-10 | 42/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.718×** | -6.0 | 6e-08 | 38/48 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -5.3 | 3e-06 | 25/48 (J82, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.772×** | -3.5 | 0.008 | 25/49 (HOP62, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.035 | 14/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.739×** | -3.0 | 0.043 | 23/48 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.750×** | -2.9 | 0.068 | 20/49 (PANC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.855× | -2.8 | 0.077 | 18/47 (BT-474, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 304 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -15.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -13.0) |
| [[SNU-423 (line)]] | alt | 303 | 0 | 17 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -26.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.193× (z -10.6) |
| [[HOP62 (line)]] | alt | 297 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -23.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 369 | 1 (1 ⚠) | 14 (13 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +22.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.262× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 234 | 0 | 15 (13 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.312× (z -9.2) |
| [[PANC-1 (line)]] | alt | 299 | 0 | 15 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.254× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 280 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -17.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 399 | 0 | 14 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.273× (z -15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.302× (z -14.4) |
| [[Hs 766T (line)]] | wt | 246 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -15.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 398 | 0 | 13 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -12.2) |
| [[J82 (line)]] | alt | 223 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -18.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -14.4) |
| [[SW480 (line)]] | alt | 200 | 0 | 13 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -13.2) |
| [[A-172 (line)]] | wt | 287 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -21.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -12.1) |
| [[KATO III (line)]] | alt | 202 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.470× (z -9.6) |
| [[LoVo (line)]] | wt | 240 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.269× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 254 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -19.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 257 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -12.3) |
| [[H4 (line)]] | wt | 346 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -10.3) |
| [[HCT15 (line)]] | alt | 503 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.476× (z -10.2) |
| [[A549 (line)]] | wt | 386 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -21.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.206× (z -9.9) |
| [[BT-474 (line)]] | alt | 252 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -14.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.346× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 219 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -14.3) |
| [[HS-578T (line)]] | alt | 238 | 0 | 8 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.327× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -10.2) |
| [[HT-29 (line)]] | alt | 224 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.301× (z -16.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 233 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.499× (z -9.1) |
| [[C32 (line)]] | wt | 238 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.7) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -10.6) |
| [[LS 180 (line)]] | wt | 198 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.271× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 254 | 0 | 7 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.156× (z -12.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -12.1) |
| [[SW 900 (line)]] | alt | 187 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -14.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW1417 (line)]] | alt | 170 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.340× (z -12.2) ⚠ toxic |
| [[A498 (line)]] | wt | 185 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.441× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.236× (z -9.5) |
| [[AN3 CA (line)]] | alt | 272 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.388× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 288 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.508× (z -8.5) |
| [[CHP-212 (line)]] | wt | 284 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -10.0) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 340 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -8.6) |
| [[SW 1271 (line)]] | alt | 358 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 149 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.490× (z -9.2) |
| [[RKO (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 216 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[COLO 205 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 179 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FER]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SCAPER]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RSPH3]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[NBEAL1]] | +0.55 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ERC1]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ANKRD12]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TRPC1]] | +0.52 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NPHP3]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[AK6]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[CEP350]] | +0.51 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[DNAAF9]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CCDC18-AS1]] | +0.51 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMSB15B]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[LINC03009]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DTX2P1]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[COPS7B]] | -0.48 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[PTGFRN]] | -0.47 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[KCTD14]] | -0.47 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[PGAP3]] | -0.46 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ZNF618]] | -0.46 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[LRP5]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[EPHX4]] | -0.46 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[TIGD1]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[KAT2A]] | -0.45 | -0.38 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.7, 30.3); signed map (-2.0, 9.8). **Vector** length 96.7, 41.7% of its response variance represented; |z| ≥ 3 in 1,727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.7 | -13.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | -1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.9 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.4 | -14.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -6.3 | -12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.7 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -7.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | myosin IXA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:71,822,291-72,118,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11061, FLJ13244, MGC71859 |
| Gene groups (HGNC) | Myosin heavy chains, class IX |
| Reactome | 6 pathways, smallest: RHOV GTPase cycle; RHOB GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [B2RTY4](https://www.uniprot.org/uniprotkb/B2RTY4) (Unconventional myosin-IXa):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Regulates Rho by stimulating its GTPase activity in neurons. Required for the regulation of neurite branching and motor neuron axon guidance (By similarity).

**Summary**, from NCBI Gene [4649](https://www.ncbi.nlm.nih.gov/gene/4649):

> This gene encodes a member of the myosin superfamily. The protein represents an unconventional myosin; it should not be confused with the conventional non-muscle myosin-9 (MYH9). Unconventional myosins contain the basic domains of conventional myosins and are further distinguished from class members by their tail domains. They function as actin-based molecular motors. Mutations in this gene have been associated with Bardet-Biedl Syndrome. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:7608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7608) · Entrez [4649](https://www.ncbi.nlm.nih.gov/gene/4649) · UniProt [B2RTY4](https://www.uniprot.org/uniprotkb/B2RTY4) · Ensembl [ENSG00000066933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066933)

## Data

Gene col 844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 844); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 844]; `tensor/DDL_lfc|DDL_z.npy` [844]; `embed/gene_vectors.npy` [844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 844 or target_col == 844). Every well: [[MYO9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
