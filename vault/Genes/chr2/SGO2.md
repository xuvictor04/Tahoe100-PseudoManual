---
symbol: "SGO2"
type: "gene"
col: 8712
ensembl_id: "ENSG00000163535"
name: "shugoshin 2"
location: "2q33.1"
module: 22
arm: "+"
pooled_cpm: 102.51
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SGO2

*shugoshin 2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +11.8, q 3e-29, up in 34 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +10.0, q 3e-21, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (20 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.501× (z -15.5, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Amsacrine (drug)]] 5 µM: 0.796× (z -5.1, q 2e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA8]] (+0.91, fdr 7e-06), [[FAM72D]] (+0.90, fdr 7e-06), [[GTSE1]] (+0.89, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.69×** | +11.8 | 3e-29 | 34/48 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.0 | 3e-21 | 34/48 (AsPC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.86×** | +9.8 | 1e-20 | 39/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.83×** | +9.2 | 4e-18 | 37/48 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.63×** | +7.8 | 7e-13 | 38/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **1.56×** | +7.1 | 1e-10 | 34/48 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.54×** | +6.9 | 5e-10 | 39/48 (PANC-1, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.34×** | +6.6 | 4e-09 | 39/48 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.42×** | +5.6 | 1e-06 | 27/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.41×** | +5.5 | 3e-06 | 31/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.41×** | +5.4 | 3e-06 | 33/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.37×** | +5.0 | 2e-05 | 27/48 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.82×** | +5.0 | 3e-05 | 30/47 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.9 | 5e-05 | 28/48 (NCI-H23, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.33×** | +4.5 | 2e-04 | 26/48 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.3 | 5e-04 | 23/48 (SW1417, Hs 766T, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +4.2 | 9e-04 | 21/48 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.20× | +4.1 | 0.001 | 21/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.003 | 21/48 (NCI-H23, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.003 | 24/48 (J82, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.003 | 23/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 22/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.009 | 19/47 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.020 | 18/48 (HT-29, NCI-H23, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.049 | 18/48 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.20× | +2.9 | 0.065 | 12/48 (NCI-H23, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.501×** | -15.5 | 0e+00 | 44/48 (A-427, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.406×** | -14.3 | 6e-44 | 47/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.592×** | -8.3 | 2e-14 | 37/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.627×** | -7.4 | 2e-11 | 40/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.649×** | -6.9 | 8e-10 | 30/49 (SK-MEL-2, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **0.480×** | -6.1 | 1e-07 | 31/45 (SHP-77, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.602×** | -5.9 | 3e-07 | 32/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.706×** | -5.3 | 8e-06 | 29/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.796×** | -5.1 | 2e-05 | 28/48 (A498, LS 180, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.729×** | -5.0 | 3e-05 | 29/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.735×** | -4.9 | 6e-05 | 30/48 (LOX-IMVI, C32, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.747×** | -4.4 | 4e-04 | 25/48 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.752×** | -4.3 | 6e-04 | 21/44 (C32, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.824×** | -4.3 | 6e-04 | 25/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.763×** | -4.3 | 7e-04 | 22/48 (LS 180, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.7 | 0.005 | 23/48 (HOP62, SW48, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.027 | 18/48 (HOP62, A-427, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.029 | 18/48 (Hs 766T, HOP62, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.805×** | -3.2 | 0.035 | 19/47 (LS 180, A-172, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.854× | -3.0 | 0.055 | 17/48 (A-427, HCT15, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.770×** | -3.0 | 0.065 | 15/48 (HOP62, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.880× | -2.9 | 0.082 | 15/48 (HCT15, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.99 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 188 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.274× (z -18.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.432× (z -8.7) |
| [[KATO III (line)]] | alt | 63.8 | 5 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.42× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.6) | [[Selinexor (drug)]] 0.5 µM 0.406× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[LOX-IMVI (line)]] | wt | 127 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.207× (z -18.2) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.426× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 70.2 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.488× (z -10.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[PANC-1 (line)]] | alt | 132 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +18.8) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.470× (z -9.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 101 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.330× (z -14.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.496× (z -9.2) |
| [[LS 180 (line)]] | wt | 79.1 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.240× (z -13.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.353× (z -9.9) |
| [[A498 (line)]] | wt | 86.0 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -18.4) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.468× (z -10.0) |
| [[C32 (line)]] | wt | 118 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.252× (z -16.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[CFPAC-1 (line)]] | alt | 68.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.7) | — |
| [[H4 (line)]] | wt | 142 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.239× (z -12.1) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.359× (z -8.7) |
| [[A549 (line)]] | wt | 92.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.293× (z -15.7) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.515× (z -8.5) |
| [[HS-578T (line)]] | alt | 82.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.426× (z -9.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H1573 (line)]] | alt | 83.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.4) | [[Ixazomib citrate (drug)]] 5 µM 0.320× (z -8.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 63.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 93.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +18.9) ⚠ cell-cycle shift, would explain all of this change | [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -8.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H23 (line)]] | alt | 161 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.94× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.356× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[Panc 03.27 (line)]] | alt | 62.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.4) | [[Selinexor (drug)]] 0.5 µM 0.340× (z -8.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RKO (line)]] | wt | 112 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.310× (z -10.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW1417 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.3) | — |
| [[A-427 (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.185× (z -20.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HT-29 (line)]] | alt | 69.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.290× (z -9.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[hTERT-HPNE (line)]] | wt | 78.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.285× (z -11.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[J82 (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 51.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.9) | [[Selinexor (drug)]] 5 µM 0.468× (z -9.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.356× (z -13.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[RPMI-7951 (line)]] | alt | 155 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +14.4) | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 114 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +25.5) | — |
| [[HCT15 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.323× (z -11.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HEC-1-A (line)]] | alt | 89.1 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.376× (z -9.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HepG2_C3A (line)]] | wt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 91.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 142 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.198× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[SNU-1 (line)]] | wt | 80.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.213× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW480 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.447× (z -8.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA8]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 960 |
| [[FAM72D]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[GTSE1]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[HJURP]] | +0.89 | +0.85 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[KIF2C]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 939 |
| [[KIF18A]] | +0.88 | +0.90 / +0.85 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 709 |
| [[NDC80]] | +0.87 | +0.92 / +0.86 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 669 |
| [[DLGAP5]] | +0.87 | +0.92 / +0.86 | both halves | 7e-06 | STRING 597 |
| [[TACC3]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 |  |
| [[CDCA2]] | +0.86 | +0.87 / +0.86 | both halves | 7e-06 | STRING 578 |
| [[CENPF]] | +0.86 | +0.89 / +0.85 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 665 |
| [[BUB1]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 902 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises SGO2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without PIMREG | 0.067 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[RGS3]] | B | RGS3 activity lowers SGO2's level | lines that do not express RGS3 (7) vs lines expressing it (43) | 1.44× higher at baseline in the lines without RGS3 | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises SGO2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.18× lower at baseline in the lines without NDC80 | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises SGO2's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.62× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.874). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.7, -57.0); signed map (-50.8, -42.0). **Vector** length 171, 67.7% of its response variance represented; |z| ≥ 3 in 1,534 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.69 to 60); *DREAM G2/M down* (control, mean cos +0.80 to 28); *E2F targets* (hallmark, mean cos +0.65 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +6.5 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +10.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | +5.8 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | +11.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +5.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.2 | +4.1 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.5 | +2.9 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.1 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.0 | +3.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -12.3 | -15.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -10.5 | -8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -10.2 | -14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | -9.6 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.7 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.9 | -4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.1 | -5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.3 | -3.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -4.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | shugoshin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,510,008-200,584,096 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRIPIN, FLJ25211; previously SGOL2 |
| Gene groups (HGNC) | Shugoshin family |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q562F6](https://www.uniprot.org/uniprotkb/Q562F6) (Shugoshin 2):

> Cooperates with PPP2CA to protect centromeric cohesin from separase-mediated cleavage in oocytes specifically during meiosis I. Has a crucial role in protecting REC8 at centromeres from cleavage by separase. During meiosis, protects centromeric cohesion complexes until metaphase II/anaphase II transition, preventing premature release of meiosis-specific REC8 cohesin complexes from anaphase I centromeres. Is thus essential for an accurate gametogenesis. May act by targeting PPP2CA to …

**Summary**, from NCBI Gene [151246](https://www.ncbi.nlm.nih.gov/gene/151246):

> Predicted to be involved in homologous chromosome segregation; meiotic sister chromatid cohesion; and mitotic sister chromatid cohesion, centromeric. Predicted to act upstream of or within several processes, including meiotic nuclear division; meiotic sister chromatid cohesion; and positive regulation of maintenance of meiotic sister chromatid cohesion, centromeric. Located in chromosome, centromeric region and nucleoplasm. Part of mitotic cohesin complex. [provided by Alliance of Genome …

**Accessions** — [HGNC:30812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30812) · Entrez [151246](https://www.ncbi.nlm.nih.gov/gene/151246) · UniProt [Q562F6](https://www.uniprot.org/uniprotkb/Q562F6) · Ensembl [ENSG00000163535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163535)

## Data

Gene col 8712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8712); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8712]; `tensor/DDL_lfc|DDL_z.npy` [8712]; `embed/gene_vectors.npy` [8712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8712 or target_col == 8712). Every well: [[SGO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
