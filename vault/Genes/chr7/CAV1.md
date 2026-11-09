---
symbol: "CAV1"
type: "gene"
col: 2696
ensembl_id: "ENSG00000105974"
name: "caveolin 1"
location: "7q31.2"
module: 98
arm: "+"
pooled_cpm: 135.3
n_lines_expressing: 37
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 11
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# CAV1

*caveolin 1* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +13.2, q 5e-37, up in 32 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.40× (z +11.5, q 2e-28, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.408× (z -11.7, q 6e-29, down in 31 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAV2]] (+0.71, fdr 7e-06, ⚠ same locus), [[BCL9L]] (+0.63, fdr 7e-06), [[CILK1]] (+0.62, fdr 1e-05), [[MYOF]] (+0.61, fdr 7e-06); moves opposite to [[SLC25A29]] (-0.58, fdr 1e-05), [[SS18L1]] (-0.57, fdr 2e-05), [[TRMT2B]] (-0.56, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SYNPO]] → it (grade B ⚠); 11 go from it, the strongest it → [[PTPN14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +13.2 | 5e-37 | 32/36 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +12.9 | 1e-35 | 30/33 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.40×** | +11.5 | 2e-28 | 35/36 (NCI-H460, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +9.9 | 5e-21 | 29/33 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.77×** | +7.2 | 9e-11 | 23/35 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +6.2 | 4e-08 | 25/35 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +5.7 | 1e-06 | 19/35 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.45×** | +4.8 | 1e-04 | 20/35 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.93×** | +4.5 | 5e-04 | 27/35 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 20/36 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.008 | 24/35 (C32, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.059 | 14/35 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.060 | 17/35 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.060 | 16/36 (NCI-H460, NCI-H1573, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.060 | 16/35 (A498, SW480, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.060 | 16/36 (CFPAC-1, A498, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.079 | 15/35 (NCI-H1573, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -11.7 | 6e-29 | 31/35 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.428×** | -11.1 | 3e-26 | 33/35 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.421×** | -10.7 | 2e-24 | 34/35 (C32, A-172, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.443×** | -10.6 | 3e-24 | 30/35 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -7.7 | 2e-12 | 28/35 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -7.3 | 4e-11 | 31/35 (C32, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -6.8 | 8e-10 | 28/35 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.407×** | -6.1 | 6e-08 | 25/33 (NCI-H1573, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.698×** | -4.7 | 2e-04 | 25/35 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.703×** | -4.6 | 2e-04 | 25/35 (A-172, LOX-IMVI, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.759×** | -3.6 | 0.015 | 25/36 (SW480, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.603×** | -3.5 | 0.025 | 20/35 (PANC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.668×** | -3.4 | 0.029 | 20/36 (Hs 766T, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.030 | 19/35 (PANC-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.639×** | -3.1 | 0.082 | 19/35 (SW48, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.642×** | -3.0 | 0.085 | 16/36 (Panc 03.27, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.787×** | -3.0 | 0.097 | 15/35 (SW48, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 851 | 20 | 8 (4 ⚠) | [[Budesonide (drug)]] 0.05 µM 3.64× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -11.6) |
| [[PANC-1 (line)]] | alt | 172 | 8 (7 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.80× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.311× (z -12.7) |
| [[HS-578T (line)]] | alt | 209 | 8 (7 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 12.6× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.309× (z -10.2) |
| [[A549 (line)]] | wt | 110 | 8 (7 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +21.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.6× (z +12.1) | [[Bortezomib (drug)]] 0.05 µM 0.359× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 206 | 7 (7 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +14.0) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.410× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 144 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.8) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.212× (z -13.6) |
| [[Hs 766T (line)]] | wt | 676 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.175× (z -19.7) |
| [[A-172 (line)]] | wt | 159 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.229× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 164 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 82.9 | 6 (3 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 16.8× (z +15.2) | [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 161 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.45× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 83.0 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -12.2) |
| [[J82 (line)]] | alt | 142 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 8.54× (z +10.4) | [[Ixazomib citrate (drug)]] 5 µM 0.391× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 62.1 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.91× (z +15.9) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 27.3× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 273 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +17.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -15.4) |
| [[NCI-H2347 (line)]] | alt | 98.3 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 266 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 296 | 0 | 4 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.131× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.184× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 91.6 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.6× (z +9.3) | [[Ixazomib citrate (drug)]] 5 µM 0.308× (z -8.5) |
| [[SNU-423 (line)]] | alt | 82.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +11.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 126 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 128 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 9.18× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 181 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 12.6× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -11.1) |
| [[SW48 (line)]] | wt | 119 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.202× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.312× (z -8.5) |
| [[SW480 (line)]] | alt | 58.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -11.5) |
| [[A-427 (line)]] | wt | 61.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +10.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2030 (line)]] | alt | 94.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.4× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.85× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.121× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 65.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAV2]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 | pathway: ESR-mediated signaling; STRING 999; ⚠ same locus (16.5 kb, same strand: neighbours can correlate without regulation) |
| [[BCL9L]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Signaling by WNT |
| [[CILK1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MYOF]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 488 |
| [[COL12A1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[RBMS3]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[AHNAK]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TNS2]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 | STRING 434 |
| [[CALD1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CUL4B]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[UTRN]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CFL2]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A29]] | -0.58 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[SS18L1]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TRMT2B]] | -0.56 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[C9orf72]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TANGO2]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GPR89B]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RBCK1]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PFDN2]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ASB16-AS1]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[DRD4]] | -0.51 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ANKRD39]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNPO]] | B | SYNPO activity raises CAV1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.63× lower at baseline in the lines without SYNPO | 0.007 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[SLC1A3]] | B | SLC1A3 activity raises CAV1's level | lines that do not express SLC1A3 (21) vs lines expressing it (29) | 2.13× lower at baseline in the lines without SLC1A3 | 0.012 | ⚠ within organs, on part of the lines; also absent: LRP2, SLIT2, CHSY3 |
| [[TGFBR2]] | B | TGFBR2 activity raises CAV1's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 3.55× lower at baseline in the lines without TGFBR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[MYOF]] | B | MYOF activity raises CAV1's level | lines that do not express MYOF (6) vs lines expressing it (44) | 5.43× lower at baseline in the lines without MYOF | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[MAML2]] | B | MAML2 activity raises CAV1's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 4.14× lower at baseline in the lines without MAML2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[LHFPL6]] | C | LHFPL6 activity raises CAV1's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 4.94× lower at baseline in the lines without LHFPL6 | 0.027 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B; co-absent with the target |
| [[CAV2]] | C | CAV2 activity raises CAV1's level | lines that do not express CAV2 (8) vs lines expressing it (42) | 7.52× lower at baseline in the lines without CAV2 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN14]] | B | CAV1 activity raises PTPN14's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without CAV1 | 0.001 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[AHNAK]] | B | CAV1 activity raises AHNAK's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without CAV1 | 0.004 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[ANKRD33B]] | B | CAV1 activity raises ANKRD33B's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 4.21× lower at baseline in the lines without CAV1 | 0.007 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[MYOF]] | B | CAV1 activity raises MYOF's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without CAV1 | 0.059 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[SLC1A3]] | B | CAV1 activity raises SLC1A3's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without CAV1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[UTRN]] | B | CAV1 activity raises UTRN's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without CAV1 | 0.066 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[CAPNS1]] | B | CAV1 activity raises CAPNS1's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without CAV1 | 0.070 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[LIMK1]] | B | CAV1 activity raises LIMK1's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.49× lower at baseline in the lines without CAV1 | 0.091 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[CAV2]] | C | CAV1 activity raises CAV2's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 3.53× lower at baseline in the lines without CAV1 | 0.007 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6; co-absent with the target |
| [[LHFPL6]] | C | CAV1 activity raises LHFPL6's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 4.56× lower at baseline in the lines without CAV1 | 0.037 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6; co-absent with the target |
| [[RBMS3]] | C | CAV1 activity raises RBMS3's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 4.22× lower at baseline in the lines without CAV1 | 0.066 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.489). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.3, 8.6); signed map (29.0, 8.5). **Vector** length 146, 50.8% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +10.2 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.8 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +7.0 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +1.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.3 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.1 | -11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.2 | -10.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -7.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | caveolin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:116,524,994-116,561,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CAV |
| Gene groups (HGNC) | Caveolins |
| Hallmark sets | UV_RESPONSE_DN, APOPTOSIS, ESTROGEN_RESPONSE_LATE, HYPOXIA |
| Reactome | 51 pathways, smallest: Metabolism of amine-derived hormones; NOSTRIN mediated eNOS trafficking; Thyroxine biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03135](https://www.uniprot.org/uniprotkb/Q03135) (Caveolin-1):

> May act as a scaffolding protein within caveolar membranes. Forms a stable heterooligomeric complex with CAV2 that targets to lipid rafts and drives caveolae formation. Mediates the recruitment of CAVIN proteins (CAVIN1/2/3/4) to the caveolae. Interacts directly with G protein alpha subunits and can functionally regulate their activity (By similarity). Involved in the costimulatory signal essential for T-cell receptor (TCR)-mediated T-cell activation. Its binding to DPP4 induces T-cell …

**Summary**, from NCBI Gene [857](https://www.ncbi.nlm.nih.gov/gene/857):

> The scaffolding protein encoded by this gene is the main component of the caveolae plasma membranes found in most cell types. The protein links integrin subunits to the tyrosine kinase FYN, an initiating step in coupling integrins to the Ras-ERK pathway and promoting cell cycle progression. The gene is a tumor suppressor gene candidate and a negative regulator of the Ras-p42/44 mitogen-activated kinase cascade. Caveolin 1 and caveolin 2 are located next to each other on chromosome 7 and express …

**Accessions** — [HGNC:1527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1527) · Entrez [857](https://www.ncbi.nlm.nih.gov/gene/857) · UniProt [Q03135](https://www.uniprot.org/uniprotkb/Q03135) · Ensembl [ENSG00000105974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105974)

## Data

Gene col 2696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2696); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2696]; `tensor/DDL_lfc|DDL_z.npy` [2696]; `embed/gene_vectors.npy` [2696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2696 or target_col == 2696). Every well: [[CAV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
