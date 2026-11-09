---
symbol: "SCFD2"
type: "gene"
col: 11498
ensembl_id: "ENSG00000184178"
name: "sec1 family domain containing 2"
location: "4q12"
module: 33
arm: "+"
pooled_cpm: 102.44
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 25
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SCFD2

*sec1 family domain containing 2* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +10.2, q 1e-21, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.82× (z +9.1, q 2e-17, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.595× (z -7.7, q 1e-11, down in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Cyclosporin A (drug)]] 5 µM: 0.640× (z -6.9, q 2e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL6]] (+0.67, fdr 7e-06), [[GNL2]] (+0.64, fdr 7e-06), [[DCAF13]] (+0.63, fdr 1e-05); moves opposite to [[GABARAPL1]] (-0.54, fdr 3e-05), [[KANSL1L]] (-0.50, fdr 5e-05), [[SLC49A4]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.95×** | +10.2 | 1e-21 | 40/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.82×** | +9.2 | 1e-17 | 43/48 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.1 | 2e-17 | 35/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.73×** | +8.4 | 8e-15 | 37/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 1e-05 | 26/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.40×** | +5.2 | 2e-05 | 29/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 5e-04 | 24/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +4.4 | 7e-04 | 28/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +4.4 | 8e-04 | 28/49 (NCI-H1792, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 25/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.001 | 27/48 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.002 | 24/48 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.002 | 23/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.008 | 20/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.012 | 22/48 (NCI-H1573, SHP-77, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.014 | 22/48 (LoVo, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.033 | 14/49 (NCI-H460, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.033 | 20/48 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.038 | 17/48 (SW 900, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -7.7 | 1e-11 | 38/47 (HCT15, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.640×** | -6.9 | 2e-09 | 36/48 (AsPC-1, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -6.8 | 2e-09 | 33/48 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -6.4 | 2e-08 | 34/48 (CFPAC-1, LoVo, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.659×** | -6.4 | 2e-08 | 34/49 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.709×** | -5.3 | 1e-05 | 30/48 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -5.0 | 4e-05 | 30/48 (CFPAC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.715×** | -5.0 | 5e-05 | 30/48 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.727×** | -4.9 | 6e-05 | 26/48 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.736×** | -4.7 | 1e-04 | 27/48 (CHP-212, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -4.6 | 2e-04 | 26/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -4.6 | 2e-04 | 24/44 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -4.5 | 3e-04 | 27/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.752×** | -4.4 | 5e-04 | 25/47 (C32, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.741×** | -4.3 | 8e-04 | 25/45 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.787×** | -3.7 | 0.008 | 21/49 (C32, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.774×** | -3.6 | 0.009 | 24/47 (SNU-1, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **0.792×** | -3.6 | 0.010 | 20/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.796×** | -3.5 | 0.012 | 24/48 (AsPC-1, J82, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.811×** | -3.5 | 0.014 | 19/48 (AsPC-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.025 | 21/48 (RPMI-7951, Panc 03.27, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.680×** | -3.1 | 0.049 | 19/48 (KATO III, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.827×** | -2.9 | 0.077 | 18/47 (LS 180, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 363 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.171× (z -12.5) |
| [[A498 (line)]] | wt | 328 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.258× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 69.4 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.71× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +8.5) | — |
| [[A-172 (line)]] | wt | 49.1 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 0.5 µM 4.59× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cyclosporin A (drug)]] 5 µM 0.301× (z -8.6) |
| [[J82 (line)]] | alt | 151 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -14.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 112 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +8.8) | [[Ixazomib citrate (drug)]] 0.5 µM 0.361× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 150 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -20.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 53.8 | 3 (3 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.08× (z +10.7) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.415× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 88.0 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.300× (z -11.1) |
| [[HCT15 (line)]] | alt | 176 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.122× (z -15.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 99.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.42× (z +9.9) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +11.8) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 142 | 1 | 2 (1 ⚠) | [[Penfluridol (drug)]] 5 µM 2.89× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.259× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.288× (z -10.4) |
| [[LS 180 (line)]] | wt | 65.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.304× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 47.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 76.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[C-33 A (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -12.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 224 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.247× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 62.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.10× (z +8.8) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 79.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 60.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.82× (z +8.5) ⚠ unreliable plate only | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.07× (z +12.3) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL6]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[GNL2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DCAF13]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RPGRIP1L]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PNO1]] | +0.62 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[GAR1]] | +0.62 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[UTP6]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[DDX18]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PUM3]] | +0.61 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[URB1]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TTLL11]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAPL1]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[SLC49A4]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[GKAP1]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PRRG4]] | -0.49 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (5.3, -32.1); signed map (-15.1, -58.6). **Vector** length 148, 51.5% of its response variance represented; |z| ≥ 3 in 1,439 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.1 | +9.2 |
|  | [[EX229 (drug)]] 5 µM |  | +6.4 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +6.2 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.5 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.4 | +3.3 |
|  | [[EX229 (drug)]] 0.05 µM |  | +4.1 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.5 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.2 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.4 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.9 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.0 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | sec1 family domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:52,872,982-53,366,066 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STXBP1L1, FLJ39514 |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU76](https://www.uniprot.org/uniprotkb/Q8WU76) (Sec1 family domain-containing protein 2):

> May be involved in protein transport.

**Summary**, from NCBI Gene [152579](https://www.ncbi.nlm.nih.gov/gene/152579):

> Predicted to be involved in intracellular protein transport and vesicle-mediated transport. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30676) · Entrez [152579](https://www.ncbi.nlm.nih.gov/gene/152579) · UniProt [Q8WU76](https://www.uniprot.org/uniprotkb/Q8WU76) · Ensembl [ENSG00000184178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184178)

## Data

Gene col 11498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11498); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11498]; `tensor/DDL_lfc|DDL_z.npy` [11498]; `embed/gene_vectors.npy` [11498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11498 or target_col == 11498). Every well: [[SCFD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCFD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
