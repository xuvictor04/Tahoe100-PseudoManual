---
symbol: "ADCY9"
type: "gene"
col: 8481
ensembl_id: "ENSG00000162104"
name: "adenylate cyclase 9"
location: "16p13.3"
module: 159
arm: "+"
pooled_cpm: 43.13
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 30
n_dd_up_clean: 22
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# ADCY9

*adenylate cyclase 9* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.51× (z +7.8, q 5e-12, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.459× (z -20.5, q 0e+00, down in 42 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.356× (z -18.5, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS15]] (+0.58, fdr 2e-05), [[FOXK2]] (+0.56, fdr 2e-05), [[BCL7A]] (+0.55, fdr 1e-05); moves opposite to [[MTRF1L]] (-0.56, fdr 1e-05), [[SMARCA1]] (-0.51, fdr 8e-05), [[PTER]] (-0.49, fdr 5e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RECK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +7.8 | 5e-12 | 37/46 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +6.7 | 6e-09 | 30/46 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.6 | 5e-06 | 23/46 (CFPAC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.4 | 8e-06 | 23/46 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +5.1 | 3e-05 | 23/47 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 3e-05 | 17/46 (NCI-H460, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.9 | 7e-05 | 16/46 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 1e-04 | 19/46 (NCI-H460, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 2e-04 | 18/46 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 3e-04 | 20/46 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 15/46 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.003 | 18/46 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 18/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.004 | 14/46 (NCI-H460, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.8 | 0.005 | 16/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 12/46 (PANC-1, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.459×** | -20.5 | 0e+00 | 42/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.356×** | -18.5 | 0e+00 | 40/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.469×** | -14.1 | 6e-43 | 37/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.519×** | -11.3 | 2e-27 | 32/41 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.549×** | -10.7 | 8e-25 | 25/38 (Hs 766T, A-427, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.571×** | -10.4 | 1e-23 | 33/45 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.603×** | -9.4 | 4e-19 | 34/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -9.2 | 3e-18 | 35/46 (A-172, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.638×** | -8.4 | 4e-15 | 32/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.628×** | -8.3 | 5e-15 | 28/45 (LoVo, SW48, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -8.1 | 3e-14 | 33/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.658×** | -7.7 | 6e-13 | 30/46 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.666×** | -7.6 | 2e-12 | 25/42 (A-427, SNU-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -7.2 | 2e-11 | 27/46 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -6.8 | 3e-10 | 27/47 (A-172, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -6.7 | 8e-10 | 27/46 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.528×** | -6.2 | 2e-08 | 28/46 (SK-MEL-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.811×** | -5.5 | 1e-06 | 21/46 (HEC-1-A, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.766×** | -4.7 | 7e-05 | 22/46 (LoVo, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.630×** | -4.5 | 2e-04 | 20/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -4.4 | 3e-04 | 19/46 (SHP-77, A498, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.652×** | -4.2 | 8e-04 | 20/45 (LOX-IMVI, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.655×** | -4.1 | 8e-04 | 16/46 (KATO III, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.806×** | -3.8 | 0.003 | 16/46 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.699×** | -3.5 | 0.010 | 16/45 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.3 | 8 (1 ⚠) | 15 (10 ⚠) | [[Trametinib (drug)]] 5 µM 3.00× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 2.43× (z +11.6) | [[Harringtonine (drug)]] 0.5 µM 0.113× (z -23.9) |
| [[HEC-1-A (line)]] | alt | 59.4 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.338× (z -11.3) |
| [[LoVo (line)]] | wt | 54.8 | 0 | 9 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.255× (z -13.8) |
| [[A-172 (line)]] | wt | 69.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -22.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.180× (z -15.8) |
| [[A498 (line)]] | wt | 99.5 | 1 (1 ⚠) | 7 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.291× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0956× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.268× (z -10.1) |
| [[PANC-1 (line)]] | alt | 50.6 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -14.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.358× (z -11.4) |
| [[HS-578T (line)]] | alt | 46.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.227× (z -12.2) |
| [[A-427 (line)]] | wt | 47.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.348× (z -10.1) |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -10.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -9.6) |
| [[KATO III (line)]] | alt | 114 | 1 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.310× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A549 (line)]] | wt | 39.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.212× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 43.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.256× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 37.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.232× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 30.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -8.6) |
| [[J82 (line)]] | alt | 42.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -11.6) |
| [[RKO (line)]] | wt | 32.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.237× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Abemaciclib (drug)]] 5 µM 0.0397× (z -10.1) |
| [[SNU-1 (line)]] | wt | 64.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.211× (z -10.7) |
| [[SW1417 (line)]] | alt | 36.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 43.8 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0537× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0841× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -10.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 39.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.213× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.141× (z -9.0) |
| [[H4 (line)]] | wt | 18.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0996× (z -9.3) |
| [[LS 180 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.253× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS15]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FOXK2]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[BCL7A]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[INPP4A]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CCZ1B]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RILPL1]] | +0.52 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[EHMT1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[CCZ1]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[SEC24B]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[PACS2]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[UIMC1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRF1L]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SMARCA1]] | -0.51 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PTER]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[MYSM1]] | -0.48 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[SUB1]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[LPXN]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[HNRNPA2B1]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[UBA6-DT]] | -0.47 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ERI2]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LINC01239]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ITPR2-AS1]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[RIPK2-DT]] | -0.46 | -0.31 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RECK]] | B | RECK activity raises ADCY9's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without RECK | 0.050 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ADCY9's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.4, -3.2); signed map (-41.9, 0.7). **Vector** length 84.0, 20.5% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.9 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.6 | -20.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.7 | -10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -9.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | adenylate cyclase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,953,387-4,116,442 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AC9 |
| Gene groups (HGNC) | Adenylate cyclases |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 42 pathways, smallest: Adenylate cyclase activating pathway; Adenylate cyclase inhibitory pathway; PKA activation in glucagon signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [O60503](https://www.uniprot.org/uniprotkb/O60503) (Adenylate cyclase type 9):

> Adenylyl cyclase that catalyzes the formation of the signaling molecule cAMP in response to activation of G protein-coupled receptors. Contributes to signaling cascades activated by CRH (corticotropin-releasing factor), corticosteroids and beta-adrenergic receptors.

**Summary**, from NCBI Gene [115](https://www.ncbi.nlm.nih.gov/gene/115):

> Adenylate cyclase is a membrane bound enzyme that catalyses the formation of cyclic AMP from ATP. It is regulated by a family of G protein-coupled receptors, protein kinases, and calcium. The type 9 adenylyl cyclase is a widely distributed adenylyl cyclase, and it is stimulated by beta-adrenergic receptor activation but is insensitive to forskolin, calcium, and somatostatin. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:240) · Entrez [115](https://www.ncbi.nlm.nih.gov/gene/115) · UniProt [O60503](https://www.uniprot.org/uniprotkb/O60503) · Ensembl [ENSG00000162104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162104)

## Data

Gene col 8481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8481); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8481]; `tensor/DDL_lfc|DDL_z.npy` [8481]; `embed/gene_vectors.npy` [8481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8481 or target_col == 8481). Every well: [[ADCY9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCY9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
