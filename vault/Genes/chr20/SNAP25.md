---
symbol: "SNAP25"
type: "gene"
col: 5351
ensembl_id: "ENSG00000132639"
name: "synaptosome associated protein 25"
location: "20p12.2"
module: 152
arm: "+"
pooled_cpm: 49.6
n_lines_expressing: 24
n_dd_up: 23
n_dd_down: 23
n_dd_up_clean: 14
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 16
direction_downstream: 19
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# SNAP25

*synaptosome associated protein 25* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +15.4, q 0e+00, up in 18 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.878× (z -6.3, q 1e-07, down in 6 of 24 measured lines) ⚠ position not correctable. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.752× (z -5.6, q 8e-06, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CA8]] (+0.63, fdr 1e-05), [[MEF2C]] (+0.60, fdr 1e-05), [[MARCHF1]] (+0.59, fdr 1e-05); moves opposite to [[PTPN9]] (-0.54, fdr 1e-05), [[RNF14]] (-0.48, fdr 3e-05), [[ZFYVE9]] (-0.47, fdr 5e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 19 go from it, the strongest it → [[SNAP25-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +15.4 | 0e+00 | 18/22 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +13.0 | 3e-36 | 18/22 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +13.0 | 3e-36 | 15/22 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +10.6 | 3e-24 | 10/23 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +10.2 | 2e-22 | 19/22 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +10.0 | 2e-21 | 19/22 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +7.9 | 2e-13 | 18/22 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.71×** | +7.2 | 4e-11 | 17/22 (NCI-H460, HOP62, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +7.2 | 4e-11 | 12/23 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.55×** | +6.2 | 4e-08 | 2/22 (SW 900, SW480) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.47×** | +5.4 | 4e-06 | 7/21 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.41×** | +4.8 | 6e-05 | 7/22 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +4.5 | 3e-04 | 11/23 (HS-578T, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.35×** | +4.2 | 9e-04 | 10/22 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +4.2 | 1e-03 | 3/24 (HS-578T, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 6/22 (HS-578T, HOP62, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.004 | 0/22 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.004 | 7/22 (C32, H4, …) | two highest doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.027 | 6/22 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.51×** | +2.9 | 0.094 | 6/21 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.878× | -6.3 | 1e-07 | 6/24 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.752×** | -5.6 | 8e-06 | 16/22 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.721×** | -4.6 | 1e-03 | 4/22 (NCI-H460, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.732×** | -4.3 | 0.002 | 11/22 (C32, SW 1088, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -4.1 | 0.005 | 14/23 (C32, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.748×** | -4.0 | 0.005 | 14/22 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.753×** | -3.9 | 0.007 | 13/21 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.755×** | -3.9 | 0.007 | 11/22 (C32, SW480, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.758×** | -3.9 | 0.007 | 14/22 (NCI-H1792, C32, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.011 | 4/21 (H4, CHP-212, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.767×** | -3.7 | 0.011 | 3/22 (A498, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.768×** | -3.7 | 0.011 | 6/22 (A498, NCI-H460, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **0.768×** | -3.7 | 0.011 | 15/22 (HOP62, C32, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.015 | 6/22 (A498, NCI-H460, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.022 | 14/22 (RPMI-7951, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.039 | 8/22 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.777×** | -3.2 | 0.039 | 0/22 | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.794×** | -3.2 | 0.042 | 11/22 (H4, SHP-77, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.4 | 12 (10 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 9.37× (z +15.0) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.79× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 104 | 7 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +14.2) | [[Bortezomib (drug)]] 0.05 µM 0.241× (z -8.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[C32 (line)]] | wt | 60.9 | 0 | 7 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -10.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.268× (z -8.6) |
| [[HS-578T (line)]] | alt | 16.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 365 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SHP-77 (line)]] | alt | 1,092 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.9) |
| [[SW480 (line)]] | alt | 22.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.83× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 48.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -11.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.249× (z -9.1) |
| [[A498 (line)]] | wt | 30.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 32.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.28× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 34.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.2) | — |
| [[A549 (line)]] | wt | 81.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +10.3) | — |
| [[H4 (line)]] | wt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[NCI-H23 (line)]] | alt | 172 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.5) | — |
| [[A-172 (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.72 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.06 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA8]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MEF2C]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[NR4A3]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[OLFM1]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MEIS1]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[GABRA2]] | +0.56 | +0.45 / +0.45 | both halves | 3e-05 | pathway: Neuronal System |
| [[EPHA3]] | +0.56 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[CXXC4]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ST8SIA4]] | +0.55 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[EYA1]] | +0.55 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[EPHA7]] | +0.54 | +0.46 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN9]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RNF14]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZFYVE9]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[MICALL1]] | -0.45 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[ZNF142]] | -0.44 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[ANKAR]] | -0.44 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[METTL8]] | -0.43 | -0.30 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers SNAP25's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PDE10A]] | B | PDE10A activity raises SNAP25's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.99× lower at baseline in the lines without PDE10A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[ZMAT4]] | C | ZMAT4 activity raises SNAP25's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 6.43× lower at baseline in the lines without ZMAT4 | 0.002 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |
| [[LRP2]] | C | LRP2 activity raises SNAP25's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 4.22× lower at baseline in the lines without LRP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises SNAP25's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.45× lower at baseline in the lines without FMN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[NREP]] | C | NREP activity raises SNAP25's level | lines that do not express NREP (13) vs lines expressing it (37) | 4.96× lower at baseline in the lines without NREP | 0.020 | ⚠ within organs, on part of the lines; also absent: DMD, MAP1B, KCTD16; co-absent with the target |
| [[KCNJ6]] | C | KCNJ6 activity raises SNAP25's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 5.01× lower at baseline in the lines without KCNJ6 | 0.021 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[NCAM1]] | C | NCAM1 activity raises SNAP25's level | lines that do not express NCAM1 (34) vs lines expressing it (16) | 5.13× lower at baseline in the lines without NCAM1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, ENSG00000237268, SOX11; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises SNAP25's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 4.50× lower at baseline in the lines without PCSK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises SNAP25's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.42× lower at baseline in the lines without EPHA3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[TMPRSS15]] | C | TMPRSS15 activity raises SNAP25's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.80× lower at baseline in the lines without TMPRSS15 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[ADARB2]] | C | ADARB2 activity raises SNAP25's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.76× lower at baseline in the lines without ADARB2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 9, C 10. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAP25-AS1]] | B | SNAP25 activity raises SNAP25-AS1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without SNAP25 | 0.012 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[MEIS1]] | B | SNAP25 activity raises MEIS1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.52× lower at baseline in the lines without SNAP25 | 0.022 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[SLC6A6]] | B | SNAP25 activity raises SLC6A6's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without SNAP25 | 0.042 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[CADM1]] | B | SNAP25 activity raises CADM1's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 4.19× lower at baseline in the lines without SNAP25 | 0.051 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[MLLT3]] | B | SNAP25 activity raises MLLT3's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 1.99× lower at baseline in the lines without SNAP25 | 0.051 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | SNAP25 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express SNAP25 (26) vs lines expressing it (22) | the lines without SNAP25: 1.40× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| cells under [[Bortezomib (drug)]] 0.05 µM | B | SNAP25 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express SNAP25 (26) vs lines expressing it (22) | the lines without SNAP25: 1.30× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[RNF24]] | B | SNAP25 activity raises RNF24's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without SNAP25 | 0.079 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | SNAP25 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express SNAP25 (26) vs lines expressing it (22) | the lines without SNAP25: 1.14× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[NREP]] | C | SNAP25 activity raises NREP's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.95× lower at baseline in the lines without SNAP25 | 0.009 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |
| [[CA8]] | C | SNAP25 activity raises CA8's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.44× lower at baseline in the lines without SNAP25 | 0.019 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |
| [[PLA2G4A]] | C | SNAP25 activity raises PLA2G4A's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 3.20× lower at baseline in the lines without SNAP25 | 0.042 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.9, 32.0); signed map (37.6, 38.5). **Vector** length 83.3, 24.3% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.8 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +7.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +6.1 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.9 | -4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | -2.7 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -4.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | synaptosome associated protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.2 — chr20:10,172,395-10,308,258 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP-25, RIC-4, RIC4, SEC9, bA416N4.2, dJ1068F16.2; previously SNAP |
| Gene groups (HGNC) | SNAREs |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 22 pathways, smallest: Neurotoxicity of clostridium toxins; Acetylcholine Neurotransmitter Release Cycle; GABA synthesis, release, reuptake and degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P60880](https://www.uniprot.org/uniprotkb/P60880) (Synaptosomal-associated protein 25):

> t-SNARE involved in the molecular regulation of neurotransmitter release. May play an important role in the synaptic function of specific neuronal systems. Associates with proteins involved in vesicle docking and membrane fusion. Regulates plasma membrane recycling through its interaction with CENPF. Modulates the gating characteristics of the delayed rectifier voltage-dependent potassium channel KCNB1 in pancreatic beta cells.

**Summary**, from NCBI Gene [6616](https://www.ncbi.nlm.nih.gov/gene/6616):

> Synaptic vesicle membrane docking and fusion is mediated by SNAREs (soluble N-ethylmaleimide-sensitive factor attachment protein receptors) located on the vesicle membrane (v-SNAREs) and the target membrane (t-SNAREs). The assembled v-SNARE/t-SNARE complex consists of a bundle of four helices, one of which is supplied by v-SNARE and the other three by t-SNARE. For t-SNAREs on the plasma membrane, the protein syntaxin supplies one helix and the protein encoded by this gene contributes the other …

**Accessions** — [HGNC:11132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11132) · Entrez [6616](https://www.ncbi.nlm.nih.gov/gene/6616) · UniProt [P60880](https://www.uniprot.org/uniprotkb/P60880) · Ensembl [ENSG00000132639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132639)

## Data

Gene col 5351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5351); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5351]; `tensor/DDL_lfc|DDL_z.npy` [5351]; `embed/gene_vectors.npy` [5351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5351 or target_col == 5351). Every well: [[SNAP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAP25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
