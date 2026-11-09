---
symbol: "RALGPS1"
type: "gene"
col: 5913
ensembl_id: "ENSG00000136828"
name: "Ral GEF with PH domain and SH3 binding motif 1"
location: "9q33.3"
module: 159
arm: "+"
pooled_cpm: 41.51
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# RALGPS1

*Ral GEF with PH domain and SH3 binding motif 1* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.39× (z +14.5, q 1e-44, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.531× (z -14.8, q 0e+00, down in 34 of 46 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.509× (z -11.2, q 1e-26, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPG2]] (+0.65, fdr 7e-06), [[CAMK2G]] (+0.65, fdr 1e-05), [[SERAC1]] (+0.64, fdr 2e-05); moves opposite to [[TRMT13]] (-0.63, fdr 3e-05), [[METTL6]] (-0.63, fdr 3e-05), [[GTF2H1]] (-0.63, fdr 1e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[RIMS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +14.5 | 1e-44 | 43/46 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +13.0 | 2e-36 | 43/46 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +11.3 | 4e-27 | 40/45 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.4 | 4e-23 | 36/46 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +10.2 | 2e-22 | 40/46 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +8.2 | 3e-14 | 34/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.11×** | +6.5 | 8e-09 | 36/46 (SW480, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 3e-05 | 27/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.004 | 20/45 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.042 | 17/45 (SW480, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.068 | 14/44 (SW480, NCI-H2347, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.068 | 16/45 (SNU-423, A498, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.11 | 18/46 (C32, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.531×** | -14.8 | 0e+00 | 34/46 (HT-29, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.417×** | -13.9 | 1e-41 | 39/46 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -11.2 | 1e-26 | 35/46 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.510×** | -10.8 | 5e-25 | 30/44 (KATO III, PANC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.580×** | -9.0 | 2e-17 | 33/45 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.587×** | -8.5 | 1e-15 | 34/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -8.4 | 4e-15 | 28/42 (NCI-H23, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.599×** | -8.2 | 2e-14 | 24/38 (LS 180, SW480, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.707×** | -8.1 | 3e-14 | 27/46 (J82, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -8.0 | 8e-14 | 35/47 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.619×** | -7.9 | 1e-13 | 29/45 (LOX-IMVI, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.673×** | -6.6 | 3e-09 | 26/46 (NCI-H1573, BT-474, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -5.1 | 2e-05 | 25/44 (SW1417, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -4.5 | 3e-04 | 21/45 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.816×** | -3.4 | 0.030 | 14/46 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.8 | 6 | 10 (7 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.31× (z +12.1) | [[Harringtonine (drug)]] 0.5 µM 0.163× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 46.5 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -16.0) |
| [[J82 (line)]] | alt | 53.5 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.399× (z -11.8) |
| [[KATO III (line)]] | alt | 80.6 | 1 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -9.9) |
| [[LS 180 (line)]] | wt | 69.8 | 1 (1 ⚠) | 7 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -11.7) |
| [[BT-474 (line)]] | alt | 153 | 0 | 7 (7 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0948× (z -12.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 66.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -20.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -19.5) |
| [[A-427 (line)]] | wt | 50.0 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -19.2) |
| [[A549 (line)]] | wt | 40.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.184× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 66.9 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.333× (z -11.4) |
| [[PANC-1 (line)]] | alt | 43.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -13.1) |
| [[SW480 (line)]] | alt | 38.1 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.372× (z -10.6) |
| [[A498 (line)]] | wt | 35.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -14.2) |
| [[HOP62 (line)]] | alt | 13.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 12.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +12.1) | — |
| [[LoVo (line)]] | wt | 65.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.1) |
| [[RKO (line)]] | wt | 52.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 12.1 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.37× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 61.7 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -15.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 25.5 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.5) | [[Harringtonine (drug)]] 0.5 µM 0.211× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 30.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 83.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 12.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 51.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 10.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 86.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -16.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 24.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -13.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.231× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 20.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.350× (z -8.7) |
| [[SW48 (line)]] | wt | 56.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.177× (z -10.6) |
| [[AN3 CA (line)]] | alt | 75.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.100× (z -14.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.252× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 16.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CAMK2G]] | +0.65 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.64 | +0.63 / +0.49 | both halves | 2e-05 |  |
| [[PACC1]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[INPP4A]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RIMS3]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ATP7B]] | +0.62 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MGAT4A]] | +0.62 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CDS1]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[BRF1]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[EIF4E3]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT13]] | -0.63 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[METTL6]] | -0.63 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.63 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.61 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ZNF764]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ABCA6]] | -0.61 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[PGBD4]] | -0.60 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[HELQ]] | -0.60 | -0.63 / -0.29 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.59 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ZNF585A]] | -0.59 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[C12orf60]] | -0.58 | -0.55 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF181]] | -0.58 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ZBTB1]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS3]] | B | RIMS3 activity raises RALGPS1's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without RIMS3 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[CYFIP2]] | B | CYFIP2 activity raises RALGPS1's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.51× lower at baseline in the lines without CYFIP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[PLAGL1]] | B | PLAGL1 activity lowers RALGPS1's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.69× higher at baseline in the lines without PLAGL1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RALGPS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RALGPS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CASZ1]] | B | CASZ1 activity raises RALGPS1's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without CASZ1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, 4.4); signed map (-38.5, -5.8). **Vector** length 111, 32.6% of its response variance represented; |z| ≥ 3 in 1,274 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +14.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +11.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -8.1 | -14.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.6 | -13.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.6 | -8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Ral GEF with PH domain and SH3 binding motif 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:126,914,774-127,223,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RALGPS1A, RALGEF2, KIAA0351 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Ral GEF with PH domain and SH3 binding motif family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JS13](https://www.uniprot.org/uniprotkb/Q5JS13) (Ras-specific guanine nucleotide-releasing factor RalGPS1):

> Guanine nucleotide exchange factor (GEF) for the small GTPase RALA. May be involved in cytoskeletal organization (By similarity). Guanine nucleotide exchange factor for.

**Summary**, from NCBI Gene [9649](https://www.ncbi.nlm.nih.gov/gene/9649):

> Enables guanyl-nucleotide exchange factor activity. Involved in regulation of Ral protein signal transduction. Predicted to be located in cytoplasm. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:16851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16851) · Entrez [9649](https://www.ncbi.nlm.nih.gov/gene/9649) · UniProt [Q5JS13](https://www.uniprot.org/uniprotkb/Q5JS13) · Ensembl [ENSG00000136828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136828)

## Data

Gene col 5913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5913); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5913]; `tensor/DDL_lfc|DDL_z.npy` [5913]; `embed/gene_vectors.npy` [5913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5913 or target_col == 5913). Every well: [[RALGPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALGPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
