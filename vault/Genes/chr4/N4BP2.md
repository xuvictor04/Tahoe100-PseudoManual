---
symbol: "N4BP2"
type: "gene"
col: 1213
ensembl_id: "ENSG00000078177"
name: "NEDD4 binding protein 2"
location: "4p14"
module: 137
arm: "+"
pooled_cpm: 57.52
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# N4BP2

*NEDD4 binding protein 2* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.47× (z +8.3, q 3e-14, up in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.22× (z +4.5, q 0.001, up in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 1 line (RKO 2.78×); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 2.47×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.18×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.324× (z -25.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAIM]] (+0.59, fdr 7e-05), [[HDGFL3]] (+0.59, fdr 5e-05), [[BRPF3]] (+0.59, fdr 5e-05); moves opposite to [[CFD]] (-0.62, fdr 3e-05), [[PHAF1]] (-0.62, fdr 9e-05), [[SLC2A1]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CREB3L1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1213.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 1 line (RKO 2.78×); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 2.47×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.18×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.3 | 3e-14 | 31/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.3 | 3e-14 | 29/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.5 | 0.001 | 18/47 (HEC-1-A, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 0.001 | 19/48 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.9 | 0.010 | 15/48 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.056 | 9/47 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.31× | +3.2 | 0.12 | 9/48 (HOP62, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.12 | 19/47 (RKO, KATO III, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.30× | +3.1 | 0.12 | 11/47 (Hs 766T, RKO, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.324×** | -25.2 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.325×** | -25.2 | 0e+00 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.370×** | -22.3 | 0e+00 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.539×** | -13.8 | 2e-41 | 44/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.558×** | -13.1 | 6e-37 | 41/47 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.351×** | -12.2 | 2e-32 | 46/49 (NCI-H1573, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.733×** | -9.8 | 7e-21 | 29/47 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -8.5 | 1e-15 | 34/48 (SW480, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.518×** | -7.7 | 9e-13 | 39/49 (A-427, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.576×** | -6.5 | 6e-09 | 29/48 (HOP62, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.590×** | -6.2 | 3e-08 | 34/47 (SW 900, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.779×** | -5.6 | 1e-06 | 25/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.798×** | -5.0 | 2e-05 | 23/47 (SW 1271, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -4.8 | 6e-05 | 19/48 (HepG2/C3A, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.828×** | -4.2 | 0.001 | 19/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.707×** | -4.1 | 0.002 | 24/47 (NCI-H460, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.712×** | -4.0 | 0.002 | 17/46 (SW 900, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.857× | -3.4 | 0.015 | 13/48 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 86.5 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 218 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -22.6) |
| [[A498 (line)]] | wt | 51.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 67.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -18.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.297× (z -15.3) |
| [[HOP62 (line)]] | alt | 70.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -15.1) |
| [[LoVo (line)]] | wt | 77.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -16.4) |
| [[NCI-H2030 (line)]] | alt | 59.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -15.7) |
| [[SW480 (line)]] | alt | 67.6 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -21.9) |
| [[A-427 (line)]] | wt | 96.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 38.5 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.329× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 84.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.8) |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.246× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 59.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -16.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -9.9) |
| [[SNU-1 (line)]] | wt | 69.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -13.6) |
| [[SW 900 (line)]] | alt | 93.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -12.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -10.7) |
| [[A549 (line)]] | wt | 64.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -13.2) |
| [[C-33 A (line)]] | alt | 84.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.256× (z -12.6) |
| [[H4 (line)]] | wt | 64.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.306× (z -10.0) |
| [[HS-578T (line)]] | alt | 34.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.187× (z -13.8) |
| [[HT-29 (line)]] | alt | 48.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -10.7) |
| [[KATO III (line)]] | alt | 41.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 77.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -12.9) |
| [[RKO (line)]] | wt | 72.3 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 2.78× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -8.9) |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.240× (z -11.5) |
| [[A-172 (line)]] | wt | 24.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -9.7) |
| [[C32 (line)]] | wt | 29.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -9.5) |
| [[COLO 205 (line)]] | alt | 82.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -10.2) |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.245× (z -11.5) |
| [[J82 (line)]] | alt | 39.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -12.0) |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 48.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.302× (z -10.8) |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 46.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.376× (z -9.0) |
| [[BT-474 (line)]] | alt | 47.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 83.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -9.2) |
| [[SW 1271 (line)]] | alt | 87.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0947× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | +0.59 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[HDGFL3]] | +0.59 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[BRPF3]] | +0.59 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[PSME3IP1]] | +0.57 | +0.23 / +0.58 | both halves | 5e-04 |  |
| [[EFCAB2]] | +0.57 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[FBXO30]] | +0.57 | +0.40 / +0.46 | both halves | 4e-05 |  |
| [[DVL3]] | +0.56 | +0.30 / +0.55 | both halves | 2e-04 |  |
| [[NDUFS1]] | +0.56 | +0.32 / +0.52 | both halves | 2e-04 | STRING 483 |
| [[ATE1]] | +0.56 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[ZMYND11]] | +0.55 | +0.26 / +0.51 | both halves | 3e-04 |  |
| [[PRDM5]] | +0.55 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[RNF6]] | +0.54 | +0.32 / +0.47 | both halves | 2e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | -0.62 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PHAF1]] | -0.62 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[SLC2A1]] | -0.60 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MRPL14]] | -0.58 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ST3GAL4]] | -0.57 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[CARHSP1]] | -0.57 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CDK18]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[KIAA2013]] | -0.56 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[RAB20]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RHPN2]] | -0.54 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[EFNA4]] | -0.54 | -0.25 / -0.44 | both halves | 4e-04 |  |
| [[TMEM160]] | -0.53 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L1]] | B | CREB3L1 activity lowers N4BP2's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.46× higher at baseline in the lines without CREB3L1 | 0.081 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-7.7, 4.3); signed map (20.7, -28.3). **Vector** length 108, 29.0% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -12.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.1 | -13.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -6.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -13.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -22.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -8.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:40,056,797-40,158,252 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B3BP |
| Gene groups (HGNC) | CUE domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UW6](https://www.uniprot.org/uniprotkb/Q86UW6) (NEDD4-binding protein 2):

> Has 5'-polynucleotide kinase and nicking endonuclease activity. May play a role in DNA repair or recombination. May play a role in the non-stop mRNA decay pathway (NSD), which specifically targets and degrades mRNAs that lack a proper stop codon.

**Summary**, from NCBI Gene [55728](https://www.ncbi.nlm.nih.gov/gene/55728):

> This gene encodes a protein containing a polynucleotide kinase domain (PNK) near the N-terminal region, and a Small MutS Related (Smr) domain near the C-terminal region. The encoded protein can bind to both B-cell leukemia/lymphoma 3 (BCL-3) and neural precursor cell expressed, developmentally downregulated 4, (Nedd4) proteins. This protein binds and hydrolyzes ATP, may function as a 5'-polynucleotide kinase, and has the capacity to be a ubiquitylation substrate. This protein may play a role in …

**Accessions** — [HGNC:29851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29851) · Entrez [55728](https://www.ncbi.nlm.nih.gov/gene/55728) · UniProt [Q86UW6](https://www.uniprot.org/uniprotkb/Q86UW6) · Ensembl [ENSG00000078177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078177)

## Data

Gene col 1213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1213); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1213]; `tensor/DDL_lfc|DDL_z.npy` [1213]; `embed/gene_vectors.npy` [1213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1213 or target_col == 1213). Every well: [[N4BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/N4BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
