---
symbol: "ANAPC13"
type: "gene"
col: 4944
ensembl_id: "ENSG00000129055"
name: "anaphase promoting complex subunit 13"
location: "3q22.2"
module: 16
arm: "+"
pooled_cpm: 12.33
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ANAPC13

*anaphase promoting complex subunit 13* — 3q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.32× (z +17.8, q 0e+00, up in 33 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +17.3, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.713× (z -5.0, q 3e-04, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEZF1]] (+0.69, fdr 7e-06), [[MCTS1]] (+0.68, fdr 1e-05), [[NEK9]] (+0.68, fdr 1e-05); moves opposite to [[CAMLG]] (-0.65, fdr 1e-05), [[PBX4]] (-0.64, fdr 1e-05), [[RPS21]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.32×** | +17.8 | 0e+00 | 33/35 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +17.3 | 0e+00 | 37/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +17.0 | 0e+00 | 19/21 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +13.4 | 2e-38 | 37/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +12.8 | 1e-35 | 29/32 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.2 | 3e-27 | 30/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.0 | 5e-26 | 35/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.95×** | +10.6 | 2e-24 | 37/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.0 | 2e-10 | 30/46 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.56×** | +6.6 | 3e-09 | 22/41 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.6 | 3e-09 | 24/48 (PANC-1, A498, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.8 | 3e-07 | 21/41 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +5.7 | 6e-07 | 22/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +5.0 | 2e-05 | 17/43 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 5e-04 | 14/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 17/47 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.010 | 10/43 (SHP-77, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.036 | 6/46 (LS 180, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -5.0 | 3e-04 | 21/47 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.572×** | -4.3 | 0.004 | 13/46 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.794×** | -3.4 | 0.071 | 12/45 (PANC-1, NCI-H1792, …) | two highest doses |  |
| [[Trimetrexate (drug)]] 0.05 µM |  | **0.795×** | -3.4 | 0.071 | 4/47 (SHP-77, LS 180, …) | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.071 | 5/47 (SW480, RPMI-7951, …) | rises with dose | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.090 | 12/45 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.798× | -3.2 | 0.12 | 10/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.816× | -3.0 | 0.17 | 9/47 (SW 900, SW48, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +16.4) | — |
| [[PANC-1 (line)]] | alt | 17.8 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 14.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +13.8) | — |
| [[A498 (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 7.19 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.44× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 9.45 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +13.5) | — |
| [[A-427 (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.93× (z +9.0) | — |
| [[A549 (line)]] | wt | 7.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 5.42 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0592× (z -11.0) |
| [[BT-474 (line)]] | alt | 9.71 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.104× (z -9.2) |
| [[H4 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.225× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 6.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 5.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0812× (z -10.0) |
| [[KATO III (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 8.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MCTS1]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[NEK9]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.67 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[GSS]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[LIG4]] | +0.67 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TASOR]] | +0.66 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ZFP91]] | +0.66 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ARCN1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[TUG1]] | +0.66 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[ZNF460]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | -0.65 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PBX4]] | -0.64 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RPS21]] | -0.64 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.63 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RNF149]] | -0.63 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[PI4KAP2]] | -0.63 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.63 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[MED31]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[SCAI]] | -0.62 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[GNRH1]] | -0.61 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[SDHAP2]] | -0.61 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[AZIN2]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-7.0, 1.7); signed map (15.1, -28.5). **Vector** length 82.8, 16.1% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +17.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +13.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.6 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.2 — chr3:134,477,706-134,486,716 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SWM1, APC13, DKFZP566D193 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BS18](https://www.uniprot.org/uniprotkb/Q9BS18) (Anaphase-promoting complex subunit 13):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [25847](https://www.ncbi.nlm.nih.gov/gene/25847):

> This gene encodes a component of the anaphase promoting complex, a large ubiquitin-protein ligase that controls cell cycle progression by regulating the degradation of cell cycle regulators such as B-type cyclins. The encoded protein is evolutionarily conserved and is required for the integrity and ubiquitin ligase activity of the anaphase promoting complex. Pseudogenes and splice variants have been found for this gene; however, the biological validity of some of the splice variants has not …

**Accessions** — [HGNC:24540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24540) · Entrez [25847](https://www.ncbi.nlm.nih.gov/gene/25847) · UniProt [Q9BS18](https://www.uniprot.org/uniprotkb/Q9BS18) · Ensembl [ENSG00000129055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129055)

## Data

Gene col 4944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4944); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4944]; `tensor/DDL_lfc|DDL_z.npy` [4944]; `embed/gene_vectors.npy` [4944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4944 or target_col == 4944). Every well: [[ANAPC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
