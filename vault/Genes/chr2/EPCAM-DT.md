---
symbol: "EPCAM-DT"
type: "gene"
col: 13975
ensembl_id: "ENSG00000234690"
name: "EPCAM divergent transcript"
location: "2p21"
module: 8
arm: "+"
pooled_cpm: 13.99
n_lines_expressing: 37
n_dd_up: 20
n_dd_down: 52
n_dd_up_clean: 17
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 19
direction_downstream: 11
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# EPCAM-DT

*EPCAM divergent transcript* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.87× (z +6.0, q 1e-06, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (24 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.287× (z -17.6, q 0e+00, down in 30 of 33 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.302× (z -11.9, q 8e-31, down in 27 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC6]] (+0.68, fdr 1e-05), [[ARSL]] (+0.62, fdr 1e-05), [[SGK2]] (+0.62, fdr 2e-05); moves opposite to [[DGKD]] (-0.56, fdr 4e-05), [[ZFYVE28]] (-0.56, fdr 8e-05), [[FLNB]] (-0.54, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[HNF1B]] → it (grade B ⚠); 11 go from it, the strongest it → [[FCGRT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.87×** | +6.0 | 1e-06 | 25/33 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.77×** | +5.4 | 2e-05 | 22/35 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.1 | 6e-05 | 27/35 (KATO III, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 9e-05 | 17/34 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.8 | 1e-04 | 22/34 (SW480, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 3e-04 | 19/35 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.6 | 3e-04 | 17/34 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 3e-04 | 19/34 (A-172, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 3e-04 | 23/33 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +4.5 | 3e-04 | 16/35 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.60×** | +4.3 | 8e-04 | 16/35 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.37×** | +4.2 | 0.001 | 13/34 (A-172, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.002 | 15/33 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.58×** | +4.1 | 0.002 | 19/34 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.004 | 17/35 (KATO III, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.012 | 13/35 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 24 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.287×** | -17.6 | 0e+00 | 30/33 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.219×** | -15.1 | 0e+00 | 33/35 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.233×** | -14.5 | 1e-45 | 34/35 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.264×** | -12.8 | 4e-35 | 30/33 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.282×** | -12.6 | 2e-34 | 31/35 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.302×** | -11.9 | 8e-31 | 27/32 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.329×** | -11.1 | 2e-26 | 32/34 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.335×** | -10.9 | 1e-25 | 30/33 (HCT15, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.346×** | -10.6 | 3e-24 | 28/34 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.353×** | -10.4 | 2e-23 | 28/33 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.360×** | -9.8 | 7e-21 | 24/31 (COLO 205, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.383×** | -9.6 | 6e-20 | 31/34 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.392×** | -9.3 | 5e-19 | 24/35 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.461×** | -7.7 | 5e-13 | 24/34 (HT-29, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.505×** | -6.8 | 4e-10 | 24/32 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.518×** | -6.5 | 2e-09 | 25/34 (A-172, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.529×** | -5.7 | 4e-07 | 22/34 (HT-29, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.316×** | -5.6 | 8e-07 | 19/32 (COLO 205, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.694×** | -5.1 | 7e-06 | 22/34 (HT-29, NCI-H23, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.354×** | -5.0 | 1e-05 | 17/31 (SW1417, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.622×** | -4.7 | 5e-05 | 18/33 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.676×** | -3.9 | 0.002 | 19/33 (NCI-H23, CFPAC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.470×** | -3.6 | 0.005 | 16/34 (NCI-H1792, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.482×** | -3.5 | 0.008 | 11/34 (NCI-H23, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.613×** | -3.5 | 0.009 | 12/35 (SW1417, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.617×** | -3.4 | 0.010 | 15/33 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.2 | 0 | 15 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -19.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -12.8) |
| [[COLO 205 (line)]] | alt | 78.9 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0207× (z -35.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0894× (z -15.6) |
| [[A-172 (line)]] | wt | 35.7 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0900× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -12.4) |
| [[A549 (line)]] | wt | 19.3 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0822× (z -19.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0510× (z -16.6) |
| [[H4 (line)]] | wt | 24.2 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0761× (z -10.7) |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -15.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0936× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0767× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 9.64 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -11.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -11.4) |
| [[A498 (line)]] | wt | 37.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -25.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0594× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 18.3 | 1 (1 ⚠) | 5 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.81× (z +10.0) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.137× (z -9.7) |
| [[SW1417 (line)]] | alt | 37.6 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.106× (z -15.0) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0361× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 4 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0696× (z -12.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.179× (z -9.0) |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0562× (z -11.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 14.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0988× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0383× (z -13.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0328× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 7.91 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0632× (z -11.6) |
| [[LoVo (line)]] | wt | 8.05 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -10.9) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -12.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC6]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ARSL]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SGK2]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ERICH2-DT]] | +0.60 | +0.56 / +0.40 | both halves | 5e-05 | same gene group |
| [[A1CF]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 | same gene group |
| [[HNF1A-AS1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[HNF4G]] | +0.58 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[KLRK1-AS1]] | +0.58 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[HOTAIR]] | +0.58 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[RORA-AS1]] | +0.58 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[HNF1B]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKD]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ZFYVE28]] | -0.56 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[FLNB]] | -0.54 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[LANCL3]] | -0.52 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[RASA3]] | -0.51 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[S100A16]] | -0.51 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[GALNT1]] | -0.50 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[PHC2]] | -0.50 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MLX]] | -0.48 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[HK1]] | -0.48 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[ZBED4]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[MICAL2]] | -0.48 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1B]] | B | HNF1B activity raises EPCAM-DT's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without HNF1B | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[LINC01876]] | B | LINC01876 activity raises EPCAM-DT's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without LINC01876 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[FCGRT]] | B | FCGRT activity raises EPCAM-DT's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without FCGRT | 0.009 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[TMC4]] | B | TMC4 activity raises EPCAM-DT's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without TMC4 | 0.012 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[FAAH2]] | B | FAAH2 activity raises EPCAM-DT's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without FAAH2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises EPCAM-DT's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 2.63× lower at baseline in the lines without TMEM51-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[DCDC2]] | B | DCDC2 activity raises EPCAM-DT's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without DCDC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[ITIH2]] | B | ITIH2 activity raises EPCAM-DT's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.60× lower at baseline in the lines without ITIH2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[ACTR3C]] | B | ACTR3C activity raises EPCAM-DT's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.69× lower at baseline in the lines without ACTR3C | 0.044 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[BANK1]] | B | BANK1 activity raises EPCAM-DT's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without BANK1 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises EPCAM-DT's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without SLC44A3-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers EPCAM-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FCGRT]] | B | EPCAM-DT activity raises FCGRT's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 2.99× lower at baseline in the lines without EPCAM-DT | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[ABCC6]] | B | EPCAM-DT activity raises ABCC6's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without EPCAM-DT | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[ACTR3C]] | B | EPCAM-DT activity raises ACTR3C's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without EPCAM-DT | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[GOLGA2P5]] | B | EPCAM-DT activity raises GOLGA2P5's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without EPCAM-DT | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[TMC4]] | B | EPCAM-DT activity raises TMC4's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without EPCAM-DT | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[C11orf52]] | B | EPCAM-DT activity raises C11orf52's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without EPCAM-DT | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[SLC44A3]] | B | EPCAM-DT activity raises SLC44A3's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without EPCAM-DT | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[CHASERR]] | B | EPCAM-DT activity raises CHASERR's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without EPCAM-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[CHASERR]] | B | EPCAM-DT activity strengthens CHASERR's drug response | lines that do not express EPCAM-DT (13) vs lines expressing it (36) | the lines without EPCAM-DT respond 0.81× as strongly (z diff +1.31); strongest at Panobinostat 0.5 µM: 0.40x vs 0.27x (z diff +2.4) | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1; target measured in part of the lines; artifact flags |
| [[HNF1B]] | B | EPCAM-DT activity raises HNF1B's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without EPCAM-DT | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[SLC44A3-AS1]] | B | EPCAM-DT activity raises SLC44A3-AS1's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without EPCAM-DT | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.2, 51.3); signed map (56.7, -0.3). **Vector** length 87.9, 23.4% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.0 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.5 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.0 | -12.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -11.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.9 | -14.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | EPCAM divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p21 — chr2:47,192,405-47,345,074 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52639) · Entrez [101927043](https://www.ncbi.nlm.nih.gov/gene/101927043) · Ensembl [ENSG00000234690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234690)

## Data

Gene col 13975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13975); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13975]; `tensor/DDL_lfc|DDL_z.npy` [13975]; `embed/gene_vectors.npy` [13975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13975 or target_col == 13975). Every well: [[EPCAM-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPCAM-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
