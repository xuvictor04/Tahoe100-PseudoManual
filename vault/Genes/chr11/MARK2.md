---
symbol: "MARK2"
type: "gene"
col: 1022
ensembl_id: "ENSG00000072518"
name: "microtubule affinity regulating kinase 2"
location: "11q13.1"
module: 42
arm: "+"
pooled_cpm: 74.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MARK2

*microtubule affinity regulating kinase 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.50× (z +22.4, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.678× (z -11.1, q 5e-26, down in 35 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.148×, NCI-H2030 0.280×, SW1417 0.508×, RKO 0.433×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.159×, NCI-H23 0.241×, PANC-1 0.441×, HT-29 0.491×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.215×, NCI-H2030 0.285×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX8]] (+0.64, fdr 7e-06), [[KAT6A]] (+0.64, fdr 1e-05), [[GPATCH8]] (+0.56, fdr 2e-05); moves opposite to [[LMAN1]] (-0.60, fdr 3e-05), [[UFM1]] (-0.57, fdr 2e-05), [[LINC00595]] (-0.55, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STAC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.50×** | +22.4 | 0e+00 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +21.4 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +18.6 | 0e+00 | 43/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +17.7 | 0e+00 | 46/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.07×** | +16.7 | 0e+00 | 43/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +16.0 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +14.6 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +14.6 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +10.6 | 2e-24 | 33/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +10.2 | 9e-23 | 33/47 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +8.8 | 6e-17 | 31/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +6.8 | 6e-10 | 30/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +6.0 | 1e-07 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +5.8 | 3e-07 | 22/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +5.2 | 8e-06 | 22/48 (A-427, SW480, …) | two highest doses |  |
| [[crizotinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.012 | 11/48 (HOP62, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.012 | 17/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.012 | 13/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.024 | 7/47 (HepG2/C3A, RKO, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1022.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.148×, NCI-H2030 0.280×, SW1417 0.508×, RKO 0.433×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.159×, NCI-H23 0.241×, PANC-1 0.441×, HT-29 0.491×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.215×, NCI-H2030 0.285×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.678×** | -11.1 | 5e-26 | 35/49 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -10.7 | 3e-24 | 29/42 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.721×** | -8.1 | 1e-13 | 25/45 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -5.8 | 7e-07 | 16/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.837× | -5.1 | 3e-05 | 20/49 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.908× | -3.9 | 0.008 | 13/49 (A-427, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.901× | -3.0 | 0.20 | 8/48 (J82, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 60.3 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 96.1 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -16.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 79.4 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.36× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.574× (z -9.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 81.3 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.527× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 102 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 69.8 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -21.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 53.9 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 116 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.508× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 35.6 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 100 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 61.3 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.15× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.8) | — |
| [[A-427 (line)]] | wt | 96.7 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 57.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.1) | — |
| [[KATO III (line)]] | alt | 90.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.9) | — |
| [[LoVo (line)]] | wt | 67.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 73.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 78.6 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 43.2 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +10.1) | — |
| [[RKO (line)]] | wt | 83.1 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.48× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 42.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.6) | [[Docetaxel (drug)]] 0.05 µM 0.203× (z -12.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 77.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 87.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -9.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 209 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.56× (z +12.0) | — |
| [[A498 (line)]] | wt | 58.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 83.0 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.40× (z +8.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.99× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 77.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 134 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.12× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.491× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 77.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.63× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 126 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.48× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 52.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.8) | — |
| [[SW48 (line)]] | wt | 95.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +11.2) | — |
| [[C32 (line)]] | wt | 60.6 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.32× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.6) | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -18.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 63.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.98× (z +8.7) | — |
| [[A-172 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX8]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[KAT6A]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GPATCH8]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SCAF8]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[GATAD2B]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RSBN1L]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ARID1A]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CENPB]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PAFAH2]] | +0.52 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[PPP6R2]] | +0.52 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[C2orf68]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TET3]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMAN1]] | -0.60 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[UFM1]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[LINC00595]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PGM3]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[GDI2]] | -0.52 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RBM44]] | -0.52 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[DNAJC25]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[POLR3D]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[NGLY1]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TTC3]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TVP23C]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TMEM167A]] | -0.50 | -0.33 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAC]] | B | STAC activity lowers MARK2's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.41× higher at baseline in the lines without STAC | 0.063 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[LINC01836]] | B | LINC01836 activity raises MARK2's level | lines that do not express LINC01836 (16) vs lines expressing it (34) | 1.39× lower at baseline in the lines without LINC01836 | 0.076 | ⚠ within organs, on part of the lines; also absent: ANXA3, SLC9A2, SHROOM3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction -0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, -28.0); signed map (7.7, -13.8). **Vector** length 79.0, 18.4% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +22.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +17.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +14.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +16.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.1 | -0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -3.1 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -0.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.2 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | microtubule affinity regulating kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,838,928-63,911,020 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAR-1, Par1b, PAR-1B; previously EMK1 |
| Gene groups (HGNC) | Microtubule affinity regulating kinases |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7KZI7](https://www.uniprot.org/uniprotkb/Q7KZI7) (Serine/threonine-protein kinase MARK2):

> Serine/threonine-protein kinase. Involved in cell polarity and microtubule dynamics regulation. Phosphorylates CRTC2/TORC2, DCX, HDAC7, KIF13B, MAP2, MAP4 and RAB11FIP2. Phosphorylates the microtubule-associated protein MAPT/TAU. Plays a key role in cell polarity by phosphorylating the microtubule-associated proteins MAP2, MAP4 and MAPT/TAU at KXGS motifs, causing detachment from microtubules, and their disassembly. Regulates epithelial cell polarity by phosphorylating RAB11FIP2. Involved in …

**Summary**, from NCBI Gene [2011](https://www.ncbi.nlm.nih.gov/gene/2011):

> This gene encodes a member of the Par-1 family of serine/threonine protein kinases. The protein is an important regulator of cell polarity in epithelial and neuronal cells, and also controls the stability of microtubules through phosphorylation and inactivation of several microtubule-associating proteins. The protein localizes to cell membranes. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:3332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3332) · Entrez [2011](https://www.ncbi.nlm.nih.gov/gene/2011) · UniProt [Q7KZI7](https://www.uniprot.org/uniprotkb/Q7KZI7) · Ensembl [ENSG00000072518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072518)

## Data

Gene col 1022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1022); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1022]; `tensor/DDL_lfc|DDL_z.npy` [1022]; `embed/gene_vectors.npy` [1022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1022 or target_col == 1022). Every well: [[MARK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
