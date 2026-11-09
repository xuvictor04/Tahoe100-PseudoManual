---
symbol: "CDC45"
type: "gene"
col: 1718
ensembl_id: "ENSG00000093009"
name: "cell division cycle 45"
location: "22q11.21"
module: 6
arm: "+"
pooled_cpm: 13.42
n_lines_expressing: 47
n_dd_up: 42
n_dd_down: 43
n_dd_up_clean: 12
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 11
direction_downstream: 35
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDC45

*cell division cycle 45* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (30 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.14× (z +14.8, q 0e+00, up in 39 of 44 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.49× (z +5.1, q 1e-05, up in 18 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.573× (z -10.2, q 9e-22, down in 31 of 44 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.713× (z -6.2, q 6e-08, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR76]] (+0.95, fdr 7e-06), [[EXO1]] (+0.94, fdr 7e-06), [[DTL]] (+0.94, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 35 go from it, the strongest it → [[CLSPN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 30 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 30 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **3.14×** | +14.8 | 0e+00 | 39/44 (LoVo, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **2.92×** | +13.8 | 5e-41 | 36/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.65×** | +12.5 | 8e-34 | 35/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.27×** | +10.5 | 8e-24 | 33/44 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.06×** | +9.3 | 2e-18 | 26/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.08×** | +9.1 | 1e-17 | 9/17 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.01×** | +9.0 | 2e-17 | 22/35 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.93×** | +8.4 | 2e-15 | 25/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.93×** | +8.4 | 2e-15 | 29/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.92×** | +8.4 | 2e-15 | 29/42 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~84% of this change | **1.96×** | +8.3 | 4e-15 | 20/37 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.83×** | +7.2 | 3e-11 | 16/27 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.41×** | +6.2 | 2e-08 | 18/45 (SW480, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.59×** | +6.0 | 8e-08 | 21/44 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 1e-05 | 18/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +4.0 | 0.001 | 6/45 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.006 | 9/44 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.013 | 7/44 (A-427, LoVo, …) | all doses, flat |  |
| [[Olanzapine (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.014 | 4/45 (SHP-77, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.017 | 8/40 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.019 | 5/42 (SW480, HT-29, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.028 | 8/43 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.034 | 5/40 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.0 | 0.040 | 4/45 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Oxaliplatin (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.046 | 3/45 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Methotrexate (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.047 | 3/45 (SW480, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +2.8 | 0.074 | 9/44 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +2.7 | 0.091 | 12/44 (SW480, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.573×** | -10.2 | 9e-22 | 31/44 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.488×** | -9.3 | 4e-18 | 28/42 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.683×** | -7.0 | 4e-10 | 26/45 (COLO 205, SHP-77, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.619×** | -6.2 | 6e-08 | 22/42 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.713×** | -6.2 | 6e-08 | 26/45 (SW1417, SW480, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.524×** | -6.0 | 2e-07 | 21/45 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.627×** | -5.8 | 5e-07 | 22/42 (SK-MEL-2, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.443×** | -5.4 | 4e-06 | 19/41 (HEC-1-A, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.665×** | -5.3 | 7e-06 | 22/42 (HOP62, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.699×** | -5.3 | 7e-06 | 20/44 (HEC-1-A, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.678×** | -5.0 | 2e-05 | 16/45 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.686×** | -4.9 | 4e-05 | 12/44 (HEC-1-A, HOP62, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.590×** | -4.9 | 4e-05 | 13/45 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.685×** | -4.9 | 4e-05 | 18/45 (A-427, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.706×** | -4.5 | 2e-04 | 14/42 (HCT15, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.793×** | -4.3 | 6e-04 | 17/45 (LoVo, SW 1088, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.797×** | -4.2 | 9e-04 | 11/45 (NCI-H2030, SW 1088, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.799×** | -4.1 | 0.001 | 21/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.005 | 14/45 (PANC-1, SW 1271, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.007 | 18/45 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -3.6 | 0.009 | 14/42 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.763×** | -3.5 | 0.010 | 15/44 (A-172, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.014 | 11/42 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.770×** | -3.4 | 0.014 | 13/43 (RKO, LS 180, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.75 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.7 | 0 | 7 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0660× (z -22.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.271× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -10.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.6) |
| [[PANC-1 (line)]] | alt | 10.7 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.34× (z +9.2) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SW480 (line)]] | alt | 23.6 | 2 (2 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.68× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~84% of this change | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.8) |
| [[A-172 (line)]] | wt | 7.73 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.121× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 21.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.4) |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0668× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.199× (z -8.8) |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0966× (z -9.0) |
| [[COLO 205 (line)]] | alt | 7.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -9.1) |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.7) |
| [[J82 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +8.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.7) |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR76]] | +0.95 | +0.95 / +0.94 | both halves | 7e-06 | STRING 462 |
| [[EXO1]] | +0.94 | +0.94 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 963 |
| [[DTL]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | STRING 938 |
| [[FANCA]] | +0.93 | +0.93 / +0.91 | both halves | 7e-06 | STRING 539 |
| [[MCM10]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 999 |
| [[CHAF1A]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 595 |
| [[GINS2]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[CLSPN]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 995 |
| [[E2F1]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 813 |
| [[MCM8]] | +0.89 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 951 |
| [[CDC25A]] | +0.89 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 949 |
| [[CENPM]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 842 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises CDC45's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.75× lower at baseline in the lines without CDC25A | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises CDC45's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.19× lower at baseline in the lines without E2F2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CDC45's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without E2F8 | 0.057 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises CDC45's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without FAM111B | 0.065 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers CDC45's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDCA7]] | B | CDCA7 activity raises CDC45's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without CDCA7 | 0.087 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises CDC45's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without DSCC1 | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[TCF19]] | C | TCF19 activity raises CDC45's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.82× lower at baseline in the lines without TCF19 | 0.043 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[SHMT1]] | C | SHMT1 activity raises CDC45's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.89× lower at baseline in the lines without SHMT1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target |
| [[BRME1]] | C | BRME1 activity raises CDC45's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without BRME1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[PXMP2]] | C | PXMP2's natural level weakens CDC45's drug response | PXMP2's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.26; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 0, C 35. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLSPN]] | C | CDC45, [[CENPM]], [[SKA3]] activity raises CLSPN's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.82× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[GINS1]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises GINS1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.31× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[SPC25]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises SPC25's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[TK1]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises TK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CENPH]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises CENPH's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PCLAF]] | C | [[C21orf58]], CDC45, [[CENPM]] activity raises PCLAF's level | lines that do not express C21orf58, CDC45, CENPM (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without C21orf58, CDC45, CENPM | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MND1]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises MND1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.69× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[VRK1]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises VRK1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.64× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[BRCA1]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises BRCA1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[NCAPD3]] | C | [[C21orf58]], CDC45, [[CENPM]], [[SKA3]] activity raises NCAPD3's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.38× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDCA4]] | C | CDC45, [[CENPM]], [[SKA3]] activity raises CDCA4's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.37× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[NASP]] | C | [[C21orf58]], CDC45 activity raises NASP's level | lines that do not express C21orf58, CDC45 (3) vs lines expressing them (47) | 1.82× lower at baseline in the lines without C21orf58, CDC45 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.944). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.8, -45.0); signed map (-38.0, -44.8). **Vector** length 134, 41.4% of its response variance represented; |z| ≥ 3 in 1,332 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.71 to 65); *Homology Directed Repair* (reactome, mean cos +0.75 to 32); *Chromosome Maintenance* (reactome, mean cos +0.75 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.3 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +14.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +4.8 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +4.0 | +4.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +3.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.2 | +3.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.3 | +2.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -8.4 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -7.1 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -6.2 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.2 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,479,457-19,520,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CDC45L2, CDC45L |
| Gene groups (HGNC) | CMG helicase complex |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 15 pathways, smallest: Unwinding of DNA; G1/S-Specific Transcription; Activation of the pre-replicative complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O75419](https://www.uniprot.org/uniprotkb/O75419) (Cell division control protein 45 homolog):

> Required for initiation of chromosomal DNA replication. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built.

**Summary**, from NCBI Gene [8318](https://www.ncbi.nlm.nih.gov/gene/8318):

> The protein encoded by this gene was identified by its strong similarity with Saccharomyces cerevisiae Cdc45, an essential protein required to the initiation of DNA replication. Cdc45 is a member of the highly conserved multiprotein complex including Cdc6/Cdc18, the minichromosome maintenance proteins (MCMs) and DNA polymerase, which is important for early steps of DNA replication in eukaryotes. This protein has been shown to interact with MCM7 and DNA polymerase alpha. Studies of the similar …

**Accessions** — [HGNC:1739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1739) · Entrez [8318](https://www.ncbi.nlm.nih.gov/gene/8318) · UniProt [O75419](https://www.uniprot.org/uniprotkb/O75419) · Ensembl [ENSG00000093009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000093009)

## Data

Gene col 1718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1718); `tables/drug_effects.parquet` (90 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1718]; `tensor/DDL_lfc|DDL_z.npy` [1718]; `embed/gene_vectors.npy` [1718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1718 or target_col == 1718). Every well: [[CDC45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
