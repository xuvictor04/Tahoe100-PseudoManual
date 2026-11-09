---
symbol: "PRPS2"
type: "gene"
col: 2188
ensembl_id: "ENSG00000101911"
name: "phosphoribosyl pyrophosphate synthetase 2"
location: "Xp22.2"
module: 6
arm: "+"
pooled_cpm: 30.55
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PRPS2

*phosphoribosyl pyrophosphate synthetase 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.08× (z +19.5, q 0e+00, up in 40 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +5.8, q 6e-07, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.552× (z -10.3, q 3e-22, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBBP7]] (+0.78, fdr 7e-06), [[CDK2]] (+0.72, fdr 7e-06), [[GMPS]] (+0.71, fdr 7e-06); moves opposite to [[NFKBIL1]] (-0.69, fdr 7e-06), [[ANKRD49]] (-0.68, fdr 7e-06), [[CCDC174]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SCARA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.08×** | +19.5 | 0e+00 | 40/41 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.58×** | +15.8 | 0e+00 | 31/34 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.49×** | +14.6 | 0e+00 | 37/39 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +10.3 | 1e-22 | 35/46 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.8 | 6e-07 | 26/47 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +5.3 | 1e-05 | 24/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.8 | 1e-04 | 24/47 (NCI-H1792, SW1417, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.7 | 2e-04 | 0/47 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.7 | 2e-04 | 24/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.30×** | +4.5 | 4e-04 | 19/46 (Panc 03.27, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 24/47 (CFPAC-1, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +4.0 | 0.003 | 17/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.18× | +3.9 | 0.004 | 13/47 (Panc 03.27, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.7 | 0.009 | 16/47 (NCI-H1792, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.22×** | +3.5 | 0.017 | 12/47 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.075 | 8/44 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.079 | 7/45 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2188.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -10.3 | 3e-22 | 34/46 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.560×** | -9.7 | 1e-19 | 35/46 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -8.0 | 2e-13 | 35/47 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.701×** | -6.2 | 1e-07 | 24/47 (SNU-1, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.788×** | -5.9 | 5e-07 | 20/46 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.608×** | -4.5 | 6e-04 | 20/45 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -4.4 | 1e-03 | 23/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.777×** | -4.1 | 0.002 | 19/45 (HOP62, A-427, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.850× | -4.0 | 0.004 | 15/47 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -3.8 | 0.009 | 18/47 (LS 180, A-427, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.807×** | -3.6 | 0.017 | 17/45 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Baicalin (drug)]] 5 µM |  | 0.865× | -3.6 | 0.017 | 9/47 (SW480, NCI-H1792, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.874× | -3.3 | 0.040 | 13/47 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.832×** | -3.2 | 0.054 | 18/47 (SNU-1, RKO, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.885× | -3.0 | 0.10 | 13/47 (HOP62, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 54.2 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.02× (z +18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.1) | — |
| [[A-427 (line)]] | wt | 39.5 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -27.5) |
| [[CFPAC-1 (line)]] | alt | 17.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.5) | — |
| [[A498 (line)]] | wt | 17.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -11.8) |
| [[A549 (line)]] | wt | 24.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HEC-1-A (line)]] | alt | 45.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 56.7 | 1 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -13.3) |
| [[LoVo (line)]] | wt | 25.8 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Harringtonine (drug)]] 5 µM 0.320× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 70.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 42.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 15.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.6) |
| [[H4 (line)]] | wt | 57.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.4) |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.2) |
| [[Hs 766T (line)]] | wt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 63.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 48.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.11× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 50.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.241× (z -8.5) |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.9) |
| [[C32 (line)]] | wt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 42.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -25.3) |
| [[RKO (line)]] | wt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.8) |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.147× (z -9.5) |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP7]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[CDK2]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[GMPS]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | STRING 627 |
| [[GPC4]] | +0.70 | +0.58 / +0.68 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[TXNDC5]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TRIP13]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[POLE]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PTDSS1]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[RRM2]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIL1]] | -0.69 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[ANKRD49]] | -0.68 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.67 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.65 / -0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RBMX2]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | -0.66 | -0.64 / -0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PIGBOS1]] | -0.65 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.65 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[C18orf21]] | -0.65 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[ASB8]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | -0.64 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[SEC62]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[RP9]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[FRG1]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARA3]] | B | SCARA3 activity raises PRPS2's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without SCARA3 | 0.061 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[TOP2A]] | B | TOP2A activity lowers PRPS2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.8, -38.1); signed map (-31.9, -44.8). **Vector** length 103, 24.8% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.51 to 23); *S Phase* (reactome, mean cos +0.50 to 41); *Activation of the pre-replicative complex* (reactome, mean cos +0.52 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.6 | +19.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.6 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.4 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.4 | +10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Volasertib (drug)]] 0.5 µM |  | +1.6 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosyl pyrophosphate synthetase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:12,791,355-12,824,222 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoribosyl pyrophosphate synthetase family |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P11908](https://www.uniprot.org/uniprotkb/P11908) (Ribose-phosphate pyrophosphokinase 2):

> Catalyzes the transfer of the pyrophosphoryl group from ATP to the 1-hydroxyl of ribose-5-phosphate to form 5-phospho-ribosyl-1-pyrophosphate (PRPP), a key intermediate in the biosynthesis of several metabolites including nucleotides, dinucleotides and some amino acids. Involved in the production of newly synthesized ATP/GTP through the purine biosynthesis pathway.

**Summary**, from NCBI Gene [5634](https://www.ncbi.nlm.nih.gov/gene/5634):

> This gene encodes a phosphoribosyl pyrophosphate synthetase that plays a central role in the synthesis of purines and pyrimidines. The encoded protein catalyzes the synthesis of 5-phosphoribosyl 1-pyrophosphate from ATP and D-ribose 5-phosphate. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:9465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9465) · Entrez [5634](https://www.ncbi.nlm.nih.gov/gene/5634) · UniProt [P11908](https://www.uniprot.org/uniprotkb/P11908) · Ensembl [ENSG00000101911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101911)

## Data

Gene col 2188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2188); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2188]; `tensor/DDL_lfc|DDL_z.npy` [2188]; `embed/gene_vectors.npy` [2188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2188 or target_col == 2188). Every well: [[PRPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
