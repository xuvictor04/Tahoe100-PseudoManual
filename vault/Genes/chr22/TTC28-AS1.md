---
symbol: "TTC28-AS1"
type: "gene"
col: 14050
ensembl_id: "ENSG00000235954"
name: "TTC28 antisense RNA 1"
location: "22q12.1"
module: 37
arm: "+"
pooled_cpm: 45.98
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 33
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TTC28-AS1

*TTC28 antisense RNA 1* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +15.3, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (14 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.336× (z -17.0, q 0e+00, down in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.566× (z -8.9, q 3e-17, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P4-1]] (+0.70, fdr 7e-06), [[ADAM20]] (+0.68, fdr 7e-06), [[ZNF248]] (+0.67, fdr 1e-05); moves opposite to [[WDR7]] (-0.59, fdr 5e-05), [[RPAP3]] (-0.55, fdr 2e-04), [[ODC1]] (-0.55, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYCP2L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +15.3 | 0e+00 | 42/47 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.0 | 3e-13 | 30/47 (HS-578T, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 9e-04 | 20/47 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.5 | 0.001 | 24/47 (NCI-H23, HS-578T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.33×** | +4.3 | 0.002 | 22/47 (LoVo, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 0.002 | 23/47 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.006 | 22/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.017 | 20/47 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.025 | 18/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.025 | 16/47 (KATO III, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.032 | 14/47 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.062 | 18/47 (RKO, SHP-77, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.062 | 13/47 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +3.2 | 0.062 | 12/47 (H4, HOP62, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.062 | 10/47 (HOP62, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.077 | 16/46 (MIA PaCa-2, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.336×** | -17.0 | 0e+00 | 46/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -15.8 | 0e+00 | 42/47 (SHP-77, SNU-423, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.350×** | -15.8 | 0e+00 | 46/47 (NCI-H1792, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.544×** | -13.4 | 6e-39 | 40/47 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.452×** | -11.9 | 1e-30 | 33/41 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.497×** | -10.9 | 1e-25 | 41/47 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.522×** | -10.1 | 3e-22 | 35/47 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.518×** | -9.9 | 4e-21 | 39/46 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.553×** | -9.2 | 2e-18 | 39/47 (BT-474, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -8.9 | 3e-17 | 39/47 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.340×** | -8.8 | 7e-17 | 45/48 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.573×** | -8.7 | 2e-16 | 41/47 (PANC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.397×** | -7.5 | 2e-12 | 36/47 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.634×** | -7.1 | 5e-11 | 32/47 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -6.4 | 6e-09 | 26/47 (A-427, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -4.5 | 2e-04 | 25/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.756×** | -4.4 | 4e-04 | 25/47 (AN3 CA, HCT15, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.769×** | -3.9 | 0.002 | 22/47 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.9 | 0.002 | 18/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.778×** | -3.8 | 0.004 | 20/46 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.798×** | -3.5 | 0.010 | 17/47 (SW 1271, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.019 | 19/47 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.028 | 21/46 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.028 | 16/47 (AsPC-1, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.679×** | -3.2 | 0.031 | 16/45 (NCI-H1792, HCT15, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 63.1 | 0 | 12 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -8.7) |
| [[A-172 (line)]] | wt | 54.6 | 1 | 9 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.8) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.326× (z -9.8) |
| [[Hs 766T (line)]] | wt | 82.9 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0374× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 65.7 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.242× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 88.6 | 0 | 8 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -17.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 36.7 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.254× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.271× (z -13.0) |
| [[PANC-1 (line)]] | alt | 59.4 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 61.0 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.181× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 58.9 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A549 (line)]] | wt | 39.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.299× (z -10.6) |
| [[J82 (line)]] | alt | 33.8 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.329× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 34.1 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.9) | [[Digitoxin (drug)]] 0.5 µM 0.316× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.343× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 65.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 47.1 | 4 | 1 | [[Auranofin (drug)]] 5 µM 6.73× (z +15.0) | [[PH-797804 (drug)]] 5 µM 0.117× (z -8.8) |
| [[SW480 (line)]] | alt | 49.0 | 1 | 4 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.423× (z -9.5) |
| [[A-427 (line)]] | wt | 43.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -20.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.190× (z -14.9) |
| [[A498 (line)]] | wt | 36.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.6) | [[Harringtonine (drug)]] 5 µM 0.182× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.254× (z -10.7) |
| [[HCT15 (line)]] | alt | 103 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HepG2_C3A (line)]] | wt | 44.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[LS 180 (line)]] | wt | 39.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.363× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 29.8 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.1) | [[Harringtonine (drug)]] 5 µM 0.125× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.215× (z -9.2) |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0164× (z -34.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0901× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.143× (z -9.4) |
| [[BT-474 (line)]] | alt | 33.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.169× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[COLO 205 (line)]] | alt | 61.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[H4 (line)]] | wt | 41.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0486× (z -16.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +13.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.0678× (z -21.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H23 (line)]] | alt | 54.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.7) | [[Digitoxin (drug)]] 0.5 µM 0.295× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 39.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 30.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +8.6) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.217× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 37.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +16.5) | — |
| [[HT-29 (line)]] | alt | 33.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[KATO III (line)]] | alt | 51.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 23.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.6) | [[Bortezomib (drug)]] 5 µM 0.0760× (z -9.0) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 36.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.347× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.228× (z -8.6) |
| [[SW 1088 (line)]] | alt | 90.6 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0644× (z -9.2) |
| [[SW 1271 (line)]] | alt | 57.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0926× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 36.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[ADAM20]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ZNF248]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[LEPR]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[LINC00159]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ADAM20P1]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[WDR49]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TNXB]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.60 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[PLD5P1]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LINC02680]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.59 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[RPAP3]] | -0.55 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[ODC1]] | -0.55 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[PSEN2]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PCNX2]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SAYSD1]] | -0.53 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[TSPYL5]] | -0.51 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[COMMD8]] | -0.51 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[TBC1D19]] | -0.50 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[B3GALT9]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[RFK]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[ZNF780A]] | -0.49 | -0.34 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2L]] | B | SYCP2L activity raises TTC28-AS1's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without SYCP2L | 0.049 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[TOP2A]] | B | TOP2A activity lowers TTC28-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, -19.2); signed map (7.0, 3.7). **Vector** length 92.1, 26.4% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +15.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.6 | +3.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -7.3 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -6.9 | -8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.5 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.6 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TTC28 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.1 — chr22:27,919,376-28,008,581 (+) |
| Ensembl biotype | lncRNA |
| Also known as | KIAA1648; previously TTC28AS, TTC28-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29336) · Entrez [284900](https://www.ncbi.nlm.nih.gov/gene/284900) · Ensembl [ENSG00000235954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235954)

## Data

Gene col 14050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14050); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14050]; `tensor/DDL_lfc|DDL_z.npy` [14050]; `embed/gene_vectors.npy` [14050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14050 or target_col == 14050). Every well: [[TTC28-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC28-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
