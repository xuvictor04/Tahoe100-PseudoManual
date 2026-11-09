---
symbol: "ZFP64"
type: "gene"
col: 320
ensembl_id: "ENSG00000020256"
name: "ZFP64 zinc finger protein"
location: "20q13.2"
module: 146
arm: "+"
pooled_cpm: 58.27
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# ZFP64

*ZFP64 zinc finger protein* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 1.18× (z +5.8, q 4e-06, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (LoVo 1.77×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.236× (z -49.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL34]] (+0.66, fdr 7e-06), [[HEATR6]] (+0.64, fdr 7e-06), [[EEF2K]] (+0.63, fdr 9e-06); moves opposite to [[DDX5]] (-0.74, fdr 7e-06), [[TRIP12]] (-0.55, fdr 3e-05), [[DBNL]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 320.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (LoVo 1.77×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +5.8 | 4e-06 | 24/48 (AsPC-1, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +5.3 | 3e-05 | 25/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.3 | 0.004 | 13/48 (J82, COLO 205, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.18× | +4.2 | 0.005 | 16/48 (J82, A549, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.18× | +4.0 | 0.008 | 16/49 (J82, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.3 | 0.079 | 15/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.080 | 10/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.080 | 12/48 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.092 | 7/48 (KATO III, PANC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.09× | +3.1 | 0.11 | 16/48 (LoVo, A498, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.236×** | -49.6 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.298×** | -29.9 | 0e+00 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.293×** | -29.1 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.380×** | -23.9 | 0e+00 | 47/48 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -23.3 | 0e+00 | 46/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -23.0 | 0e+00 | 45/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.458×** | -19.3 | 0e+00 | 48/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.491×** | -17.5 | 0e+00 | 42/47 (KATO III, SNU-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.483×** | -17.3 | 0e+00 | 43/48 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.420×** | -16.8 | 0e+00 | 46/48 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.511×** | -16.6 | 0e+00 | 38/49 (A-427, C-33 A, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -15.1 | 0e+00 | 42/49 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.521×** | -14.9 | 0e+00 | 38/45 (A-427, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.585×** | -12.7 | 2e-35 | 35/44 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -12.7 | 3e-35 | 39/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.573×** | -10.8 | 2e-25 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -10.2 | 8e-23 | 36/48 (SNU-1, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -7.4 | 3e-12 | 30/49 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.716×** | -6.5 | 3e-09 | 27/48 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.780×** | -6.1 | 2e-08 | 29/48 (J82, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -5.8 | 2e-07 | 23/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -5.7 | 2e-07 | 28/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.8 | 0 | 18 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -36.2) |
| [[MIA PaCa-2 (line)]] | alt | 59.0 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -37.6) |
| [[NCI-H2030 (line)]] | alt | 78.7 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -35.9) |
| [[SNU-423 (line)]] | alt | 48.9 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -23.9) |
| [[SW480 (line)]] | alt | 54.6 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -33.5) |
| [[A-427 (line)]] | wt | 113 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0706× (z -30.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.343× (z -18.8) |
| [[HOP62 (line)]] | alt | 78.1 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -22.4) |
| [[HEC-1-A (line)]] | alt | 66.3 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -20.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.345× (z -17.6) |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -34.2) |
| [[SW 900 (line)]] | alt | 91.5 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.7) |
| [[A-172 (line)]] | wt | 41.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -30.0) |
| [[C-33 A (line)]] | alt | 225 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0955× (z -25.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -36.5) |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 72.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -30.6) |
| [[SNU-1 (line)]] | wt | 89.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0732× (z -32.2) |
| [[Hs 766T (line)]] | wt | 81.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -35.3) |
| [[J82 (line)]] | alt | 61.4 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -18.1) |
| [[BT-474 (line)]] | alt | 71.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -14.8) |
| [[HCT15 (line)]] | alt | 72.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.7) |
| [[HS-578T (line)]] | alt | 50.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 51.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -25.1) |
| [[NCI-H1573 (line)]] | alt | 47.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -34.4) |
| [[RKO (line)]] | wt | 49.2 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -11.6) |
| [[SW1417 (line)]] | alt | 73.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -24.9) |
| [[COLO 205 (line)]] | alt | 66.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -27.7) |
| [[KATO III (line)]] | alt | 54.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0921× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -17.9) |
| [[A549 (line)]] | wt | 50.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -21.6) |
| [[HT-29 (line)]] | alt | 43.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.5) |
| [[LoVo (line)]] | wt | 40.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.77× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -19.0) |
| [[Panc 03.27 (line)]] | alt | 39.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 66.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.3) |
| [[A498 (line)]] | wt | 39.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.3) |
| [[C32 (line)]] | wt | 51.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 51.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.0) |
| [[SW48 (line)]] | wt | 51.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0665× (z -19.9) |
| [[AsPC-1 (line)]] | alt | 25.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.8) |
| [[H4 (line)]] | wt | 43.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -23.9) |
| [[LS 180 (line)]] | wt | 46.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -15.1) |
| [[SW 1271 (line)]] | alt | 69.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -14.3) |
| [[AN3 CA (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL34]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[EEF2K]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[MRPS34]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[TADA1]] | +0.63 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[GATA4]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[NOD1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[EBPL]] | +0.62 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[FLYWCH1]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[BRAT1]] | +0.61 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.74 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[TRIP12]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DBNL]] | -0.55 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[PDLIM5]] | -0.54 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[MSRA]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TUG1]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[CDKN2B-AS1]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[HIVEP2]] | -0.52 | -0.47 / -0.55 | both halves | 2e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZFP64's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.5, -7.1); signed map (-28.4, -12.6). **Vector** length 84.7, 24.1% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | +5.8 | -5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.1 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | -0.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -17.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -3.8 | -14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -12.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -0.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.2 | -0.6 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -0.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ZFP64 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:52,051,663-52,204,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10734, dJ831D17.1, FLJ12628, dJ548G19.1; previously ZNF338 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTW7](https://www.uniprot.org/uniprotkb/Q9NTW7) (Zinc finger protein 64):

> May be involved in the regulation of mesenchymal cell differentiation through transactivation of NOTCH1 target genes.

**Summary**, from NCBI Gene [55734](https://www.ncbi.nlm.nih.gov/gene/55734):

> Predicted to enable DNA-binding transcription factor activity and transcription cis-regulatory region binding activity. Involved in mesenchymal cell differentiation. Located in cytoplasm and megasporocyte nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15940) · Entrez [55734](https://www.ncbi.nlm.nih.gov/gene/55734) · UniProt [Q9NTW7](https://www.uniprot.org/uniprotkb/Q9NTW7) · Ensembl [ENSG00000020256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020256)

## Data

Gene col 320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 320); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 320]; `tensor/DDL_lfc|DDL_z.npy` [320]; `embed/gene_vectors.npy` [320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 320 or target_col == 320). Every well: [[ZFP64 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP64.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
