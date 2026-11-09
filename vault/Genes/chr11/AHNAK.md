---
symbol: "AHNAK"
type: "gene"
col: 4582
ensembl_id: "ENSG00000124942"
name: "AHNAK nucleoprotein"
location: "11q12.3"
module: 54
arm: "-"
pooled_cpm: 590.8
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# AHNAK

*AHNAK nucleoprotein* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.25× (z +10.3, q 6e-22, up in 41 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.71× (z +7.1, q 4e-10, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.214× (z -20.6, q 0e+00, down in 46 of 46 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.259× (z -18.1, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIEZO1]] (+0.60, fdr 1e-05), [[PLEC]] (+0.59, fdr 7e-06), [[CAV1]] (+0.59, fdr 1e-05); moves opposite to [[TMEM144]] (-0.54, fdr 3e-05), [[NSFP1]] (-0.51, fdr 4e-05), [[TBK1]] (-0.51, fdr 2e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAV1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +10.3 | 6e-22 | 41/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +7.1 | 4e-10 | 39/46 (SNU-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 0.001 | 27/46 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.39×** | +4.3 | 0.002 | 26/46 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.003 | 39/46 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.003 | 31/46 (SW48, SNU-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.004 | 27/46 (NCI-H1573, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 39/45 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.017 | 29/46 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.018 | 32/45 (A549, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.029 | 27/46 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.20× | +3.3 | 0.039 | 23/46 (KATO III, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.039 | 26/45 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.039 | 29/45 (SW48, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.077 | 24/46 (NCI-H1573, Hs 766T, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.086 | 24/46 (NCI-H1573, Panc 03.27, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.088 | 26/46 (NCI-H1573, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.214×** | -20.6 | 0e+00 | 46/46 (A549, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.259×** | -18.1 | 0e+00 | 46/46 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.311×** | -15.6 | 0e+00 | 46/46 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.429×** | -10.9 | 2e-25 | 44/45 (SNU-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.565×** | -7.6 | 2e-12 | 45/46 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.599×** | -6.9 | 7e-10 | 38/46 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.698×** | -6.8 | 7e-10 | 35/47 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.592×** | -6.6 | 2e-09 | 44/46 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.398×** | -6.4 | 8e-09 | 41/43 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.638×** | -6.0 | 1e-07 | 43/46 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -5.7 | 5e-07 | 28/46 (HEC-1-A, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -5.1 | 2e-05 | 38/46 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.709×** | -4.6 | 2e-04 | 36/46 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.538×** | -4.3 | 6e-04 | 37/46 (MIA PaCa-2, SNU-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.559×** | -4.1 | 0.002 | 34/47 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.567×** | -4.0 | 0.003 | 32/47 (HOP62, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.011 | 34/45 (NCI-H661, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.012 | 23/46 (J82, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.698×** | -3.4 | 0.017 | 34/47 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.853× | -3.1 | 0.064 | 20/46 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.659×** | -2.9 | 0.088 | 25/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.809×** | -2.9 | 0.099 | 23/47 (H4, HEC-1-A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 450 | 10 | 5 (4 ⚠) | [[Betamethasone dipropionate (drug)]] 0.05 µM 2.81× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.193× (z -16.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.199× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 736 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -20.3) |
| [[A498 (line)]] | wt | 344 | 4 (3 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +12.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.47× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.9) |
| [[COLO 205 (line)]] | alt | 344 | 2 (2 ⚠) | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.97× (z +8.8) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 5 µM 0.165× (z -16.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -14.4) |
| [[SNU-1 (line)]] | wt | 1,055 | 2 | 7 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.85× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.201× (z -15.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.5) |
| [[A549 (line)]] | wt | 641 | 4 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.82× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.178× (z -20.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.203× (z -19.2) |
| [[H4 (line)]] | wt | 806 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -17.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.219× (z -14.6) |
| [[HOP62 (line)]] | alt | 754 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -17.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.168× (z -16.1) |
| [[HS-578T (line)]] | alt | 643 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.193× (z -18.2) |
| [[KATO III (line)]] | alt | 614 | 1 (1 ⚠) | 6 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.92× (z +9.8) ⚠ cell-cycle shift, explains ~9% of this change | [[Panobinostat (drug)]] 5 µM 0.169× (z -19.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.183× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 557 | 2 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.80× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -11.5) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.367× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 291 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.6) |
| [[LS 180 (line)]] | wt | 677 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -20.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.160× (z -19.3) |
| [[NCI-H1792 (line)]] | alt | 399 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.229× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.268× (z -12.8) |
| [[RKO (line)]] | wt | 469 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.2) |
| [[SW48 (line)]] | wt | 549 | 3 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.66× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.249× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -12.7) |
| [[SW480 (line)]] | alt | 528 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -19.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -18.2) |
| [[A-172 (line)]] | wt | 1,167 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -19.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.219× (z -16.7) |
| [[HCT15 (line)]] | alt | 1,576 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.3) |
| [[HT-29 (line)]] | alt | 827 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.226× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 696 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.248× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 371 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +13.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.187× (z -17.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.256× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 805 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 237 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.29× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.321× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.330× (z -11.8) |
| [[SW1417 (line)]] | alt | 500 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.09× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -12.5) |
| [[A-427 (line)]] | wt | 435 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.82× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.208× (z -15.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.261× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 778 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.225× (z -14.8) |
| [[Hs 766T (line)]] | wt | 883 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -15.2) |
| [[J82 (line)]] | alt | 743 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -18.3) |
| [[LoVo (line)]] | wt | 348 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -18.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.261× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 759 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -15.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.192× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 493 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.380× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.415× (z -10.1) |
| [[PANC-1 (line)]] | alt | 921 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 522 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.0) |
| [[SNU-423 (line)]] | alt | 581 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -17.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.237× (z -14.4) |
| [[SW 900 (line)]] | alt | 301 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.383× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 886 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -14.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 293 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.363× (z -11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -9.9) |
| [[SW 1088 (line)]] | alt | 885 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0782× (z -15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.161× (z -11.0) |
| [[C32 (line)]] | wt | 423 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.391× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 591 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -10.9) |
| [[NCI-H661 (line)]] | alt | 447 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -10.3) |
| [[SW 1271 (line)]] | alt | 591 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 322 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 391 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 350 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 561 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 477 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIEZO1]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PLEC]] | +0.59 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 730 |
| [[CAV1]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[KRT7]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[HNRNPK]] | +0.58 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TMEM43]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DSP]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[IL6ST]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SLC25A24]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SCRN1]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FLII]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[AHNAK2]] | +0.55 | +0.55 / +0.64 | both halves | 1e-05 | same gene group; STRING 944 |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM144]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[NSFP1]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[TBK1]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZNRF1]] | -0.50 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[TUBD1]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PGAP1]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[DPM1]] | -0.49 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[QPCTL]] | -0.49 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[TOMM5]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PDE8A]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[PLA2G4A]] | -0.48 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | CAV1 activity raises AHNAK's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without CAV1 | 0.004 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[NR3C1]] | B | NR3C1 activity raises AHNAK's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.2, 2.8); signed map (12.0, -8.8). **Vector** length 154, 60.9% of its response variance represented; |z| ≥ 3 in 1,838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +12.9 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +11.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +9.0 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +6.1 | +3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.9 | +4.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +5.3 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +5.3 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -7.6 | -10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.9 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.2 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -6.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.5 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.1 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.1 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | AHNAK nucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,433,542-62,556,235 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5395, AHNAK1 |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q09666](https://www.uniprot.org/uniprotkb/Q09666) (Neuroblast differentiation-associated protein AHNAK):

> May be required for neuronal cell differentiation.

**Summary**, from NCBI Gene [79026](https://www.ncbi.nlm.nih.gov/gene/79026):

> The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the shorter isoform initiates a feedback loop that regulates alternative splicing of this gene. [provided …

**Accessions** — [HGNC:347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:347) · Entrez [79026](https://www.ncbi.nlm.nih.gov/gene/79026) · UniProt [Q09666](https://www.uniprot.org/uniprotkb/Q09666) · Ensembl [ENSG00000124942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124942)

## Data

Gene col 4582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4582); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4582]; `tensor/DDL_lfc|DDL_z.npy` [4582]; `embed/gene_vectors.npy` [4582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4582 or target_col == 4582). Every well: [[AHNAK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHNAK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
