---
symbol: "STX7"
type: "gene"
col: 1269
ensembl_id: "ENSG00000079950"
name: "syntaxin 7"
location: "6q23.2"
module: 30
arm: "+"
pooled_cpm: 63.5
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# STX7

*syntaxin 7* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +14.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.363× (z -32.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERAC1]] (+0.75, fdr 1e-05), [[TMEM185A]] (+0.75, fdr 7e-06), [[LTA4H]] (+0.73, fdr 7e-06); moves opposite to [[MZF1-AS1]] (-0.72, fdr 2e-05), [[ERCC6L2]] (-0.72, fdr 1e-05), [[MPDU1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RRAGD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +14.8 | 0e+00 | 46/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +14.2 | 1e-43 | 46/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +13.7 | 3e-40 | 45/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +9.1 | 9e-18 | 38/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +8.4 | 4e-15 | 37/48 (HT-29, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +6.9 | 4e-10 | 37/49 (SW480, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +6.5 | 8e-09 | 29/49 (SW480, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.22×** | +6.4 | 9e-09 | 26/48 (AsPC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +6.4 | 1e-08 | 34/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +6.3 | 2e-08 | 24/48 (RKO, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.25×** | +5.1 | 2e-05 | 25/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +4.5 | 3e-04 | 15/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.001 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 17/48 (BT-474, KATO III, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 17/48 (HT-29, KATO III, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.029 | 13/50 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.033 | 7/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.086 | 11/49 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +2.9 | 0.088 | 7/49 (SHP-77, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.363×** | -32.9 | 0e+00 | 47/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.471×** | -24.4 | 0e+00 | 44/49 (SNU-423, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.473×** | -16.5 | 0e+00 | 41/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.540×** | -14.2 | 2e-43 | 38/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -12.8 | 1e-35 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.637×** | -10.4 | 3e-23 | 36/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -9.5 | 1e-19 | 34/49 (MIA PaCa-2, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.660×** | -9.2 | 3e-18 | 36/50 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.676×** | -9.0 | 1e-17 | 36/48 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.677×** | -8.6 | 3e-16 | 33/48 (SNU-423, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.689×** | -8.6 | 5e-16 | 30/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -7.1 | 7e-11 | 30/48 (A-172, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -5.9 | 1e-07 | 24/48 (HOP62, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.782×** | -5.4 | 2e-06 | 26/47 (HepG2/C3A, CFPAC-1, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.808×** | -4.9 | 4e-05 | 24/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.787×** | -2.9 | 0.095 | 11/48 (Panc 03.27, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.860× | -2.9 | 0.096 | 5/49 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.6 | 3 | 8 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -21.2) |
| [[A-172 (line)]] | wt | 73.9 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -19.4) |
| [[HOP62 (line)]] | alt | 54.3 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -26.5) |
| [[LOX-IMVI (line)]] | wt | 73.1 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -28.4) |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 62.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -26.4) |
| [[NCI-H1573 (line)]] | alt | 41.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -26.5) |
| [[SW1417 (line)]] | alt | 70.5 | 3 | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.50× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.9) |
| [[A498 (line)]] | wt | 39.2 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 59.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -23.0) |
| [[BT-474 (line)]] | alt | 57.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 63.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -23.8) |
| [[HepG2_C3A (line)]] | wt | 84.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.0) |
| [[HS-578T (line)]] | alt | 55.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -17.7) |
| [[RKO (line)]] | wt | 41.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.3) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -25.1) |
| [[SW480 (line)]] | alt | 79.4 | 2 | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.95× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -14.3) |
| [[C32 (line)]] | wt | 82.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -16.0) |
| [[HT-29 (line)]] | alt | 60.8 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 59.5 | 1 | 3 | [[Belinostat (drug)]] 5 µM 2.86× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.1) |
| [[LoVo (line)]] | wt | 55.3 | 2 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.42× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 70.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -17.5) |
| [[PANC-1 (line)]] | alt | 64.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -29.0) |
| [[A549 (line)]] | wt | 61.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -18.8) |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 59.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.8) |
| [[NCI-H2030 (line)]] | alt | 55.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.8) |
| [[A-427 (line)]] | wt | 63.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.442× (z -8.5) |
| [[KATO III (line)]] | alt | 68.8 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 45.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 75.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.3) |
| [[C-33 A (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 39.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -12.2) |
| [[H4 (line)]] | wt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.6) |
| [[LS 180 (line)]] | wt | 78.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0627× (z -36.8) |
| [[SHP-77 (line)]] | alt | 67.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 83.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -13.4) |
| [[SW 1088 (line)]] | alt | 72.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0799× (z -8.7) |
| [[SW 900 (line)]] | alt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.2) |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERAC1]] | +0.75 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[LTA4H]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[MGST3]] | +0.71 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.71 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.71 | +0.72 / +0.40 | both halves | 5e-05 | STRING 430 |
| [[ARRB2]] | +0.70 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[RAB4A]] | +0.69 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[CAT]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HACE1]] | +0.69 | +0.72 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1-AS1]] | -0.72 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.72 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[MPDU1]] | -0.70 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[ZNF689]] | -0.70 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[SP2]] | -0.68 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.68 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[PCBP1-AS1]] | -0.68 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[SON]] | -0.68 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[E2F3]] | -0.66 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TSTD2]] | -0.65 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[FIZ1]] | -0.65 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PHF8]] | -0.65 | -0.57 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGD]] | B | RRAGD activity raises STX7's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.12× lower at baseline in the lines without RRAGD | 0.063 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[TOP2A]] | B | TOP2A activity raises STX7's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.1, -7.0); signed map (-33.5, -13.0). **Vector** length 131, 42.0% of its response variance represented; |z| ≥ 3 in 1,286 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +9.2 | +13.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.9 | +14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.8 | +14.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.5 | -24.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.3 | -32.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.2 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Esmolol (hydrochloride) (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.6 | -1.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:132,445,867-132,513,198 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Syntaxins |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [O15400](https://www.uniprot.org/uniprotkb/O15400) (Syntaxin-7):

> May be involved in protein trafficking from the plasma membrane to the early endosome (EE) as well as in homotypic fusion of endocytic organelles. Mediates the endocytic trafficking from early endosomes to late endosomes and lysosomes.

**Summary**, from NCBI Gene [8417](https://www.ncbi.nlm.nih.gov/gene/8417):

> The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:11442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11442) · Entrez [8417](https://www.ncbi.nlm.nih.gov/gene/8417) · UniProt [O15400](https://www.uniprot.org/uniprotkb/O15400) · Ensembl [ENSG00000079950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079950)

## Data

Gene col 1269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1269); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1269]; `tensor/DDL_lfc|DDL_z.npy` [1269]; `embed/gene_vectors.npy` [1269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1269 or target_col == 1269). Every well: [[STX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
