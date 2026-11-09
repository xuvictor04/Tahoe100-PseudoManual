---
symbol: "METTL25"
type: "gene"
col: 4830
ensembl_id: "ENSG00000127720"
name: "methyltransferase like 25"
location: "12q21.31"
module: 64
arm: "+"
pooled_cpm: 23.71
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 37
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# METTL25

*methyltransferase like 25* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.35× (z +4.3, q 0.009, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.362× (z -20.6, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.431× (z -12.1, q 2e-31, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHLD1]] (+0.59, fdr 2e-05), [[CUL5]] (+0.56, fdr 1e-05), [[TRMT11]] (+0.56, fdr 3e-05); moves opposite to [[DRAP1]] (-0.52, fdr 4e-05), [[DYNLT1]] (-0.47, fdr 9e-05), [[SERINC2]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.009 | 20/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.020 | 16/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.020 | 18/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +3.4 | 0.074 | 13/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.074 | 10/47 (SW 900, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.074 | 12/47 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.074 | 14/48 (LS 180, HT-29, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.26× | +3.2 | 0.10 | 12/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.52× | +3.1 | 0.10 | 8/46 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.10 | 16/48 (HepG2/C3A, SW1417, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.10 | 8/47 (NCI-H1573, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 23 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.362×** | -20.6 | 0e+00 | 42/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.326×** | -16.1 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.335×** | -15.7 | 0e+00 | 42/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.417×** | -12.5 | 6e-34 | 44/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.431×** | -12.1 | 2e-31 | 36/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.458×** | -11.2 | 4e-27 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.457×** | -10.8 | 3e-25 | 35/47 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.477×** | -10.6 | 2e-24 | 42/47 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.491×** | -10.2 | 1e-22 | 38/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.506×** | -9.8 | 7e-21 | 34/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.495×** | -9.7 | 1e-20 | 31/46 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.544×** | -8.7 | 1e-16 | 37/48 (HCT15, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.583×** | -7.7 | 4e-13 | 33/48 (AN3 CA, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.619×** | -6.6 | 1e-09 | 26/48 (HEC-1-A, SW48, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.625×** | -6.5 | 3e-09 | 27/47 (A-427, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -4.7 | 7e-05 | 25/48 (HCT15, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.800×** | -4.5 | 1e-04 | 20/48 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.733×** | -4.5 | 2e-04 | 22/47 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.758×** | -4.0 | 0.001 | 15/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.755×** | -3.9 | 0.002 | 17/47 (NCI-H23, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.015 | 19/47 (AN3 CA, A-172, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.015 | 20/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.795×** | -3.1 | 0.031 | 14/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.805×** | -3.1 | 0.031 | 4/48 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.05 µM |  | **0.819×** | -2.9 | 0.064 | 10/47 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.815×** | -2.8 | 0.072 | 11/48 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.763×** | -2.8 | 0.084 | 16/48 (MIA PaCa-2, SW 1271, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.6 | 0 | 18 (14 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.159× (z -16.5) |
| [[PANC-1 (line)]] | alt | 25.3 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -23.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -13.9) |
| [[LoVo (line)]] | wt | 32.9 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -19.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -22.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -11.8) |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 5 (5 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -13.5) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0583× (z -14.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.225× (z -9.0) |
| [[KATO III (line)]] | alt | 16.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 33.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -9.2) |
| [[SNU-1 (line)]] | wt | 37.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 18.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 24.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -16.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 48.7 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -16.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -12.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 33.0 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 17.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0409× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.114× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[H4 (line)]] | wt | 15.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0590× (z -11.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -11.4) |
| [[J82 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.204× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 16.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.150× (z -10.0) |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0977× (z -12.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 39.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0736× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0502× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.195× (z -10.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHLD1]] | +0.59 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[CUL5]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TRMT11]] | +0.56 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[UBXN8]] | +0.55 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[AKAP8]] | +0.54 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[YTHDF3]] | +0.53 | +0.48 / +0.35 | both halves | 1e-04 |  |
| [[ZZZ3]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[MTREX]] | +0.51 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[TMEM87A]] | +0.51 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[PIGB]] | +0.50 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[RMDN2]] | +0.50 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[FAM217B]] | +0.49 | +0.56 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAP1]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[DYNLT1]] | -0.47 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[SERINC2]] | -0.45 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[HMGA1]] | -0.43 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[CARD10]] | -0.43 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[N4BP3]] | -0.43 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[AFDN]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[TINAGL1]] | -0.42 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[DOT1L]] | -0.42 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[PDLIM7]] | -0.42 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PRXL2B]] | -0.41 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[PPARD]] | -0.41 | -0.36 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.369). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-17.3, 4.0); signed map (8.1, -40.8). **Vector** length 73.2, 16.0% of its response variance represented; |z| ≥ 3 in 1,315 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.9 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.7 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.5 | -10.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.4 | -12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.3 | -6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | -3.1 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.1 | -2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.6 | -2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.3 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[vincristine (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase like 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:82,358,528-82,479,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22789; previously C12orf26 |
| Gene groups (HGNC) | 7BS orphan methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6Q8](https://www.uniprot.org/uniprotkb/Q8N6Q8) (Probable methyltransferase-like protein 25):

> Probable methyltransferase.

**Summary**, from NCBI Gene [84190](https://www.ncbi.nlm.nih.gov/gene/84190):

> Predicted to enable methyltransferase activity. Predicted to be involved in methylation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26228) · Entrez [84190](https://www.ncbi.nlm.nih.gov/gene/84190) · UniProt [Q8N6Q8](https://www.uniprot.org/uniprotkb/Q8N6Q8) · Ensembl [ENSG00000127720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127720)

## Data

Gene col 4830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4830); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4830]; `tensor/DDL_lfc|DDL_z.npy` [4830]; `embed/gene_vectors.npy` [4830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4830 or target_col == 4830). Every well: [[METTL25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
