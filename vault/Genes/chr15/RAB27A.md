---
symbol: "RAB27A"
type: "gene"
col: 932
ensembl_id: "ENSG00000069974"
name: "RAB27A, member RAS oncogene family"
location: "15q21.3"
module: 29
arm: "+"
pooled_cpm: 50.49
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 34
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# RAB27A

*RAB27A, member RAS oncogene family* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +9.3, q 1e-17, up in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (PANC-1 2.90×, NCI-H2030 2.15×, SW480 2.04×, NCI-H1573 2.37×, …); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.36×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.12×; ⚠ cell-cycle shift, explains ~58% of this change).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.341× (z -17.5, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENOF]] (+0.54, fdr 5e-05), [[DYRK4]] (+0.53, fdr 4e-05), [[PI4K2B]] (+0.52, fdr 4e-05); moves opposite to [[KCTD20]] (-0.52, fdr 2e-04), [[CBX6]] (-0.51, fdr 2e-05), [[TNFAIP8L1]] (-0.50, fdr 5e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC39A8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 932.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (PANC-1 2.90×, NCI-H2030 2.15×, SW480 2.04×, NCI-H1573 2.37×, …); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.36×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.12×; ⚠ cell-cycle shift, explains ~58% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.3 | 1e-17 | 31/47 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.11 | 19/47 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.49× | +3.4 | 0.11 | 12/47 (A498, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.23× | +3.4 | 0.11 | 16/47 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.22× | +3.3 | 0.11 | 10/47 (CFPAC-1, PANC-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.23× | +3.2 | 0.13 | 16/48 (NCI-H2347, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.341×** | -17.5 | 0e+00 | 43/47 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.349×** | -17.1 | 0e+00 | 43/47 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.402×** | -14.8 | 0e+00 | 43/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.544×** | -14.0 | 3e-42 | 34/46 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.499×** | -11.3 | 2e-27 | 37/47 (HOP62, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.539×** | -10.0 | 9e-22 | 34/47 (LS 180, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.561×** | -9.4 | 5e-19 | 34/46 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.612×** | -7.7 | 1e-12 | 32/47 (COLO 205, NCI-H1792, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -7.5 | 6e-12 | 36/48 (NCI-H1792, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -7.2 | 3e-11 | 32/47 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -7.0 | 1e-10 | 31/47 (SW 900, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -6.9 | 3e-10 | 33/47 (hTERT-HPNE, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -6.8 | 6e-10 | 29/46 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.668×** | -6.6 | 2e-09 | 32/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.672×** | -6.5 | 4e-09 | 26/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.678×** | -6.0 | 9e-08 | 27/47 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.694×** | -5.9 | 1e-07 | 31/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -5.5 | 1e-06 | 26/47 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.728×** | -4.9 | 2e-05 | 25/47 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.745×** | -4.8 | 5e-05 | 21/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.821×** | -4.5 | 2e-04 | 20/47 (LoVo, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 191 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -24.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.118× (z -21.3) |
| [[A498 (line)]] | wt | 97.0 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -22.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -13.7) |
| [[HOP62 (line)]] | alt | 73.2 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -16.6) |
| [[A549 (line)]] | wt | 55.1 | 0 | 7 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.238× (z -10.5) |
| [[C32 (line)]] | wt | 63.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -15.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.330× (z -10.1) |
| [[HT-29 (line)]] | alt | 33.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -15.8) |
| [[LoVo (line)]] | wt | 40.2 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.265× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 98.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -11.8) |
| [[KATO III (line)]] | alt | 46.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.256× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.335× (z -9.2) |
| [[SW480 (line)]] | alt | 29.6 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.236× (z -14.4) |
| [[COLO 205 (line)]] | alt | 94.3 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -14.3) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.343× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 98.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -15.1) |
| [[HS-578T (line)]] | alt | 39.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 62.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -11.4) |
| [[J82 (line)]] | alt | 48.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -10.8) |
| [[SNU-423 (line)]] | alt | 85.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.6) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.253× (z -11.6) |
| [[SW 900 (line)]] | alt | 90.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -13.3) |
| [[A-172 (line)]] | wt | 50.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 84.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.379× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.6) |
| [[SW 1088 (line)]] | alt | 133 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0232× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -10.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 32.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 59.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -9.3) |
| [[PANC-1 (line)]] | alt | 22.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 25.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -9.0) |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0874× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.9) | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -10.3) |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOF]] | +0.54 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[DYRK4]] | +0.53 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[PI4K2B]] | +0.52 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[SETD7]] | +0.52 | +0.39 / +0.35 | both halves | 1e-04 |  |
| [[CMPK1]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[UGP2]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[B4GALT1]] | +0.51 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TMED5]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SLC39A8]] | +0.51 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[ERAP1]] | +0.50 | +0.29 / +0.43 | both halves | 3e-04 |  |
| [[LEPR]] | +0.50 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[FAM76B]] | +0.49 | +0.40 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD20]] | -0.52 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[CBX6]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TNFAIP8L1]] | -0.50 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[MAPKBP1]] | -0.50 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[DVL1]] | -0.49 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[SMYD3]] | -0.48 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[IFTAP]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[F2RL2]] | -0.48 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[DCAF4]] | -0.48 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[TSNARE1]] | -0.48 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[ACTG1]] | -0.48 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[TMEM177]] | -0.47 | -0.29 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A8]] | B | SLC39A8 activity raises RAB27A's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without SLC39A8 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[ABCA3]] | B | ABCA3 activity weakens RAB27A's drug response | lines that do not express ABCA3 (9) vs lines expressing it (39) | the lines without ABCA3 respond 1.46× as strongly (z diff -1.68); strongest at Homoharringtonine 5 µM: 0.36x vs 0.61x (z diff -4.3) | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ABCA3]] | B | ABCA3 activity lowers RAB27A's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.49× higher at baseline in the lines without ABCA3 | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[SOD2]] | C | SOD2 activity raises RAB27A's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without SOD2 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.313). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.5, -55.7); signed map (-21.7, -28.7). **Vector** length 98.5, 28.0% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -17.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -17.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -14.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | RAB27A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,202,966-55,319,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAB27, RAM, GS2, HsT18676 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 12 pathways, smallest: Insulin processing; Regulation of MITF-M-dependent genes involved in pigmentation; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P51159](https://www.uniprot.org/uniprotkb/P51159) (Ras-related protein Rab-27A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB27A regulates homeostasis of late endocytic pathway, including endosomal positioning, maturation and secretion. …

**Summary**, from NCBI Gene [5873](https://www.ncbi.nlm.nih.gov/gene/5873):

> The protein encoded by this gene belongs to the small GTPase superfamily, Rab family. The protein is membrane-bound and may be involved in protein transport and small GTPase mediated signal transduction. Mutations in this gene are associated with Griscelli syndrome type 2. Alternative splicing occurs at this locus and four transcript variants encoding the same protein have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9766) · Entrez [5873](https://www.ncbi.nlm.nih.gov/gene/5873) · UniProt [P51159](https://www.uniprot.org/uniprotkb/P51159) · Ensembl [ENSG00000069974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069974)

## Data

Gene col 932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 932); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 932]; `tensor/DDL_lfc|DDL_z.npy` [932]; `embed/gene_vectors.npy` [932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 932 or target_col == 932). Every well: [[RAB27A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB27A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
