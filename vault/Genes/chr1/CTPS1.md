---
symbol: "CTPS1"
type: "gene"
col: 10162
ensembl_id: "ENSG00000171793"
name: "CTP synthase 1"
location: "1p34.2"
module: 5
arm: "+"
pooled_cpm: 38.97
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CTPS1

*CTP synthase 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.78× (z +13.3, q 7e-38, up in 33 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.60× (z +6.1, q 5e-08, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.585× (z -10.4, q 2e-22, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.702× (z -4.8, q 2e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLFNL1-AS1]] (+0.84, fdr 7e-06, ⚠ same locus), [[WDR4]] (+0.81, fdr 7e-06), [[LETM1]] (+0.81, fdr 7e-06), [[HNRNPAB]] (+0.80, fdr 7e-06); moves opposite to [[SECISBP2L]] (-0.67, fdr 7e-06), [[CCNG2]] (-0.66, fdr 7e-06), [[CFAP36]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.78×** | +13.3 | 7e-38 | 33/39 (A-427, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.35×** | +11.6 | 1e-28 | 35/44 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.09×** | +10.0 | 4e-21 | 43/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +9.6 | 1e-19 | 42/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.01×** | +8.7 | 3e-16 | 33/44 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.85×** | +8.3 | 9e-15 | 34/46 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.82×** | +8.1 | 5e-14 | 38/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.84×** | +8.0 | 1e-13 | 30/46 (C32, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.79×** | +7.9 | 2e-13 | 30/48 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.48×** | +7.4 | 6e-12 | 28/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.62×** | +6.2 | 2e-08 | 25/45 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.60×** | +6.1 | 5e-08 | 30/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +5.8 | 4e-07 | 33/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.2 | 7e-06 | 2/48 (HCT15, KATO III) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.48×** | +5.1 | 2e-05 | 23/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 2e-05 | 25/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +4.2 | 9e-04 | 27/46 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 1e-03 | 24/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 1e-03 | 19/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.005 | 19/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.007 | 19/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.035 | 14/45 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.035 | 14/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.035 | 15/47 (NCI-H661, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.035 | 16/48 (HT-29, AN3 CA, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.037 | 12/46 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.039 | 14/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +2.9 | 0.059 | 12/44 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.061 | 15/46 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.585×** | -10.4 | 2e-22 | 40/48 (A-172, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.552×** | -8.1 | 1e-13 | 34/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.757×** | -5.4 | 1e-05 | 24/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.702×** | -4.8 | 2e-04 | 24/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.693×** | -4.8 | 2e-04 | 25/46 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.721×** | -4.5 | 7e-04 | 22/47 (LS 180, HS-578T, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.717×** | -4.4 | 9e-04 | 22/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.728×** | -4.4 | 1e-03 | 23/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.728×** | -4.1 | 0.002 | 20/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.566×** | -4.1 | 0.003 | 15/45 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.755×** | -3.8 | 0.006 | 21/47 (NCI-H460, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.776×** | -3.5 | 0.022 | 17/48 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.776×** | -3.5 | 0.022 | 12/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.781×** | -3.3 | 0.033 | 19/48 (LoVo, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.053 | 18/48 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.053 | 19/47 (KATO III, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 80.1 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -8.5) |
| [[A-427 (line)]] | wt | 78.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.37× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.382× (z -12.6) |
| [[HT-29 (line)]] | alt | 18.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +11.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 3 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.40× (z +9.1) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 92.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 56.0 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.142× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 43.7 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.72× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 32.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.331× (z -9.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 12.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.32× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 24.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +15.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.13× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.256× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.245× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 19.3 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 5 µM 0.0763× (z -11.0) |
| [[LoVo (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.407× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.247× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.646× (z -9.2) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 46.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.76× (z +8.9) ⚠ unreliable plate only | — |
| [[SNU-423 (line)]] | alt | 9.83 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.27× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW1417 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 61.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -8.6) |
| [[A549 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFNL1-AS1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[WDR4]] | +0.81 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[LETM1]] | +0.81 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[URB2]] | +0.76 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[NAA15]] | +0.75 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[PUS1]] | +0.74 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 | STRING 439 |
| [[ABCE1]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 564 |
| [[POLR1A]] | +0.71 | +0.70 / +0.75 | both halves | 7e-06 | STRING 775 |
| [[WDR77]] | +0.71 | +0.72 / +0.72 | both halves | 7e-06 | STRING 407 |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SECISBP2L]] | -0.67 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[CCNG2]] | -0.66 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[CFAP36]] | -0.65 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.64 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[BAZ2A]] | -0.64 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[SIRT2]] | -0.64 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[ANG]] | -0.64 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[CDK7]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 | pathway: HALLMARK_PEROXISOME |
| [[CIR1]] | -0.63 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[MXD1]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises CTPS1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without TERT | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[YPEL3]] | B | YPEL3 activity lowers CTPS1's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 2.17× higher at baseline in the lines without YPEL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[ADCY3]] | B | ADCY3 activity raises CTPS1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without ADCY3 | 0.083 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[ME3]] | B | ME3 activity lowers CTPS1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.41× higher at baseline in the lines without ME3 | 0.099 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.9, -36.0); signed map (-2.5, -48.7). **Vector** length 138, 44.8% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.61 to 13); *rRNA processing* (reactome, mean cos +0.50 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +6.2 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +5.2 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +4.8 | +11.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +1.5 |
|  | [[Brimonidine (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.5 | -10.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.8 | -8.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.8 | -5.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.4 | -4.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | CTP synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,979,300-41,012,565 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GATD5A; previously CTPS |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing; CTP synthase family |
| Hallmark sets | PEROXISOME, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P17812](https://www.uniprot.org/uniprotkb/P17812) (CTP synthase 1):

> Cytidine triphosphate synthase involved in the de novo synthesis of CTP, a precursor of DNA, RNA and phospholipids. Catalyzes the ATP-dependent amination of UTP to CTP with either L-glutamine or ammonia as a source of nitrogen. CTPS1 CTP synthase activity plays a crucial role in the proliferation of activated lymphocytes and immunity; additional CTP being required to meet increased demand for DNA, RNA and lipid membrane biosynthesis in proliferating lymphocytes. In addition to CTP synthase …

**Summary**, from NCBI Gene [1503](https://www.ncbi.nlm.nih.gov/gene/1503):

> This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:2519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2519) · Entrez [1503](https://www.ncbi.nlm.nih.gov/gene/1503) · UniProt [P17812](https://www.uniprot.org/uniprotkb/P17812) · Ensembl [ENSG00000171793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171793)

## Data

Gene col 10162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10162); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10162]; `tensor/DDL_lfc|DDL_z.npy` [10162]; `embed/gene_vectors.npy` [10162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10162 or target_col == 10162). Every well: [[CTPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
