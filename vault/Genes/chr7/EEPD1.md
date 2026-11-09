---
symbol: "EEPD1"
type: "gene"
col: 4349
ensembl_id: "ENSG00000122547"
name: "endonuclease/exonuclease/phosphatase family domain containing 1"
location: "7p14.2"
module: 162
arm: "+"
pooled_cpm: 129.57
n_lines_expressing: 36
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# EEPD1

*endonuclease/exonuclease/phosphatase family domain containing 1* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.64× (z +30.5, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.675× (z -9.3, q 1e-17, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA13]] (+0.66, fdr 1e-05), [[PRAG1]] (+0.58, fdr 1e-05), [[NOS1AP]] (+0.55, fdr 6e-05); moves opposite to [[ZSCAN30]] (-0.53, fdr 4e-04), [[BTC]] (-0.48, fdr 1e-04), [[CCDC30]] (-0.47, fdr 0.002, ⚠ not reproduced), [[PDIA3P1]] (-0.47, fdr 3e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[AZGP1]] → it (grade B ⚠); 11 go from it, the strongest it → [[RHPN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.64×** | +30.5 | 0e+00 | 30/34 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.06×** | +26.3 | 0e+00 | 31/34 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.96×** | +25.6 | 0e+00 | 30/34 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +14.9 | 0e+00 | 30/34 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +10.6 | 4e-24 | 25/35 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +10.5 | 8e-24 | 14/34 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +10.1 | 6e-22 | 25/34 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +9.6 | 4e-20 | 19/34 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +5.8 | 4e-07 | 13/34 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 13/34 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +4.6 | 3e-04 | 8/35 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.14× | +4.5 | 3e-04 | 10/35 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.14× | +4.2 | 9e-04 | 9/35 (SW480, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 9/34 (A498, Hs 766T, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.1 | 0.064 | 11/33 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -9.3 | 1e-17 | 24/34 (SW480, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -7.0 | 7e-10 | 18/34 (A498, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -6.2 | 1e-07 | 17/34 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.607×** | -6.1 | 1e-07 | 20/35 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.797×** | -5.3 | 1e-05 | 15/33 (NCI-H2030, RKO, …) | two highest doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.799×** | -5.3 | 1e-05 | 20/34 (KATO III, HT-29, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -5.1 | 2e-05 | 2/36 (NCI-H23, NCI-H2030) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.669×** | -4.9 | 5e-05 | 16/34 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.696×** | -4.5 | 5e-04 | 14/34 (A498, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -4.5 | 5e-04 | 12/34 (SW1417, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.883× | -4.1 | 0.002 | 12/34 (CFPAC-1, Panc 03.27, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.002 | 16/34 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.002 | 12/34 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.890× | -3.9 | 0.004 | 12/34 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.845× | -3.8 | 0.005 | 15/33 (NCI-H2030, RKO, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.740×** | -3.7 | 0.007 | 7/35 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.862× | -3.5 | 0.013 | 14/35 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.866× | -3.4 | 0.019 | 14/34 (A498, SW 1088, …) | top dose only |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.872× | -3.0 | 0.055 | 5/34 (LS 180, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 446 | 0 | 16 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -11.1) |
| [[LS 180 (line)]] | wt | 221 | 0 | 12 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.360× (z -9.2) |
| [[PANC-1 (line)]] | alt | 577 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -22.8) |
| [[Panc 03.27 (line)]] | alt | 94.1 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.77× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.417× (z -9.0) |
| [[LoVo (line)]] | wt | 45.3 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.94× (z +17.7) | — |
| [[A498 (line)]] | wt | 80.3 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.56× (z +13.5) | [[Homoharringtonine (drug)]] 0.05 µM 0.406× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 264 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -14.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.367× (z -8.7) |
| [[KATO III (line)]] | alt | 601 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 76.5 | 3 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.12× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 48.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +16.5) | — |
| [[SW1417 (line)]] | alt | 303 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 54.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 58.4 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.317× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.363× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 62.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.48× (z +11.8) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.382× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 42.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +14.2) | — |
| [[SW 900 (line)]] | alt | 33.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.99× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 201 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.326× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 52.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +12.4) | — |
| [[COLO 205 (line)]] | alt | 137 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +23.9) | — |
| [[HEC-1-A (line)]] | alt | 59.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 43.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 75.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +11.4) | — |
| [[A-172 (line)]] | wt | 32.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 75.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 37.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.272× (z -9.5) ⚠ transcription drop |
| [[RKO (line)]] | wt | 43.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.5) | — |
| [[SW48 (line)]] | wt | 62.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +9.7) | — |
| [[A549 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 31.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 31.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA13]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PRAG1]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NOS1AP]] | +0.55 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[CHKA]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[EPHB3]] | +0.52 | +0.28 / +0.46 | both halves | 3e-04 |  |
| [[FOXO1]] | +0.52 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PPARG]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[SOX13]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D8]] | +0.50 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[ONECUT3]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC00659]] | +0.48 | +0.38 / +0.37 | both halves | 7e-05 |  |
| [[GRAMD4]] | +0.48 | +0.40 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN30]] | -0.53 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[BTC]] | -0.48 | -0.47 / -0.34 | both halves | 1e-04 | pathway: Signaling by Nuclear Receptors |
| [[CCDC30]] | -0.47 | -0.41 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[ARRDC3-AS1]] | -0.47 | -0.36 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[PDIA3P1]] | -0.47 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[KRBA2]] | -0.47 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[ZBTB21]] | -0.47 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[MAMDC2-AS1]] | -0.46 | -0.38 / -0.24 | both halves | 5e-04 |  |
| [[CLHC1]] | -0.46 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[AP5B1]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.46 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[AEBP2]] | -0.46 | -0.34 / -0.21 | both halves | 6e-04 |  |
| [[ZNF629]] | -0.46 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ACYP2]] | -0.46 | -0.36 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AZGP1]] | B | AZGP1 activity raises EEPD1's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.25× lower at baseline in the lines without AZGP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[HNF4A]] | B | HNF4A activity raises EEPD1's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without HNF4A | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[ONECUT3]] | B | ONECUT3 activity raises EEPD1's level | lines that do not express ONECUT3 (37) vs lines expressing it (13) | 3.11× lower at baseline in the lines without ONECUT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: KLK7, KLK11, SLC6A20 |
| [[NOS1AP]] | B | NOS1AP activity raises EEPD1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.74× lower at baseline in the lines without NOS1AP | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |
| [[ARHGAP8]] | B | ARHGAP8 activity raises EEPD1's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without ARHGAP8 | 0.081 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[SLC45A4]] | B | SLC45A4 activity raises EEPD1's level | lines that do not express SLC45A4 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without SLC45A4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGEF3; maybe low, not absent; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers EEPD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers EEPD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[APOA2]] | C | APOA2 activity raises EEPD1's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 2.29× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; its own permutation p |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHPN2]] | B | EEPD1 activity raises RHPN2's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without EEPD1 | 0.016 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[SLC45A4]] | B | EEPD1 activity raises SLC45A4's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.07× lower at baseline in the lines without EEPD1 | 0.018 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[NOS1AP]] | B | EEPD1 activity raises NOS1AP's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without EEPD1 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| cells under [[ULK-101 (drug)]] 5 µM | B | EEPD1 activity raises the cells' numbers under ULK-101 5 µM (protects the cells) | lines that do not express EEPD1 (14) vs lines expressing it (34) | the lines without EEPD1: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[EML4]] | B | EEPD1 activity raises EML4's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without EEPD1 | 0.038 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[CHKA]] | B | EEPD1 activity raises CHKA's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without EEPD1 | 0.044 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[VSIR]] | B | EEPD1 activity raises VSIR's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.96× lower at baseline in the lines without EEPD1 | 0.062 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[PRAG1]] | B | EEPD1 activity raises PRAG1's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without EEPD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[ARHGAP8]] | B | EEPD1 activity raises ARHGAP8's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 3.62× lower at baseline in the lines without EEPD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[FAIM]] | B | EEPD1 activity raises FAIM's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without EEPD1 | 0.088 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[KCNK5]] | C | EEPD1 activity raises KCNK5's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 3.66× lower at baseline in the lines without EEPD1 | 0.026 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 34.8); signed map (-18.3, 35.3). **Vector** length 111, 27.7% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.5 | +26.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +30.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +25.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.5 | +14.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +5.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | endonuclease/exonuclease/phosphatase family domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:36,153,254-36,301,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1706 |
| Reactome | 3 pathways, smallest: NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux; NR1H2 and NR1H3-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

UniProt [Q7L9B9](https://www.uniprot.org/uniprotkb/Q7L9B9) carries no function annotation.

**Summary**, from NCBI Gene [80820](https://www.ncbi.nlm.nih.gov/gene/80820):

> Predicted to enable DNA binding activity and catalytic activity. Involved in positive regulation of cholesterol efflux. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22223) · Entrez [80820](https://www.ncbi.nlm.nih.gov/gene/80820) · UniProt [Q7L9B9](https://www.uniprot.org/uniprotkb/Q7L9B9) · Ensembl [ENSG00000122547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122547)

## Data

Gene col 4349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4349); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4349]; `tensor/DDL_lfc|DDL_z.npy` [4349]; `embed/gene_vectors.npy` [4349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4349 or target_col == 4349). Every well: [[EEPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
