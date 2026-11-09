---
symbol: "EHF"
type: "gene"
col: 5693
ensembl_id: "ENSG00000135373"
name: "ETS homologous factor"
location: "11p13"
module: 73
arm: "+"
pooled_cpm: 81.85
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 53
direction_downstream: 64
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# EHF

*ETS homologous factor* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +17.2, q 0e+00, up in 5 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +8.1, q 1e-13, up in 10 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.512× (z -11.8, q 2e-29, down in 18 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP3A5]] (+0.67, fdr 7e-06), [[COL17A1]] (+0.66, fdr 2e-05), [[C4BPB]] (+0.62, fdr 1e-05); moves opposite to [[BCL7C]] (-0.47, fdr 8e-05), [[DNAAF9]] (-0.46, fdr 4e-05), [[SOCS7]] (-0.46, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[STON2]] → it (grade B ⚠); 64 go from it, the strongest it → [[ABHD11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +17.2 | 0e+00 | 5/22 (HCT15, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.9 | 1e-35 | 3/17 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +8.1 | 1e-13 | 10/21 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.37×** | +7.9 | 3e-13 | 7/21 (HT-29, BT-474, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.4 | 1e-11 | 4/21 (BT-474, SNU-423, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +6.8 | 9e-10 | 14/22 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.8 | 6e-07 | 4/20 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 9e-07 | 1/21 (SNU-423) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.34×** | +5.0 | 3e-05 | 11/21 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.31×** | +4.8 | 8e-05 | 2/21 (HEC-1-A, SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.25×** | +4.0 | 0.003 | 9/21 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.007 | 0/22 | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.017 | 0/21 | inconsistent across doses | position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.026 | 0/22 | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.20×** | +3.3 | 0.036 | 7/21 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.045 | 0/21 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.049 | 0/23 | top dose only | cell-cycle shift (explains ~0% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.092 | 2/21 (LoVo, LS 180) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.092 | 1/21 (NCI-H1573) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -11.8 | 2e-29 | 18/21 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.525×** | -11.4 | 2e-27 | 21/21 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.578×** | -9.7 | 7e-20 | 20/21 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -6.3 | 6e-08 | 14/21 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.788×** | -5.9 | 3e-07 | 14/21 (LoVo, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -5.0 | 5e-05 | 1/22 (NCI-H1792) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.754×** | -4.6 | 3e-04 | 2/21 (SK-MEL-2, NCI-H1792) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.770×** | -4.6 | 3e-04 | 1/21 (HCT15) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.795×** | -4.0 | 0.003 | 1/21 (SNU-423) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.797×** | -3.8 | 0.007 | 16/21 (SW48, Hs 766T, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.807×** | -3.8 | 0.009 | 14/22 (LoVo, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.814×** | -3.6 | 0.014 | 14/21 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.819×** | -3.5 | 0.020 | 3/21 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -3.5 | 0.020 | 8/22 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.813×** | -3.4 | 0.023 | 0/21 | inconsistent across doses |  |
| [[Bimatoprost (drug)]] 5 µM |  | 0.872× | -3.4 | 0.024 | 15/21 (CFPAC-1, NCI-H2347, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.026 | 6/21 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.030 | 0/21 | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.693×** | -3.1 | 0.054 | 0/21 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 230 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -20.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.110× (z -16.3) |
| [[LoVo (line)]] | wt | 148 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0531× (z -24.1) |
| [[BT-474 (line)]] | alt | 167 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.5) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[CFPAC-1 (line)]] | alt | 305 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[LS 180 (line)]] | wt | 387 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0767× (z -25.2) |
| [[SNU-1 (line)]] | wt | 120 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -11.8) |
| [[SW48 (line)]] | wt | 94.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -12.6) |
| [[HT-29 (line)]] | alt | 327 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.3) ⚠ cell-cycle shift, explains ~61% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -13.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.343× (z -10.2) |
| [[KATO III (line)]] | alt | 175 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0945× (z -20.5) |
| [[NCI-H1573 (line)]] | alt | 27.5 | 1 (1 ⚠) | 3 | [[Harringtonine (drug)]] 0.5 µM 3.55× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | [[Panobinostat (drug)]] 5 µM 0.194× (z -11.1) |
| [[COLO 205 (line)]] | alt | 330 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.270× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 85.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -16.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.246× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.0) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Panc 03.27 (line)]] | alt | 535 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.155× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 75.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2347 (line)]] | alt | 191 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.0) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[SNU-423 (line)]] | alt | 32.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.16× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 329 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-172 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.84 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 16.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP3A5]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[COL17A1]] | +0.66 | +0.72 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[C4BPB]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[HEPH]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CDH17]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TMPRSS2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MECOM]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[GALNT5]] | +0.58 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[CALB1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MUC17]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[DSG4]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[NOSTRIN]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL7C]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[DNAAF9]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SOCS7]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[OGG1]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 6, C 47. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STON2]] | B | STON2 activity raises EHF's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.82× lower at baseline in the lines without STON2 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[INPP4B]] | B | INPP4B activity raises EHF's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.77× lower at baseline in the lines without INPP4B | 0.032 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[HTR1D]] | B | HTR1D activity raises EHF's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without HTR1D | 0.036 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises EHF's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 4.43× lower at baseline in the lines without SHROOM3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[GRHL3]] | B | GRHL3 activity raises EHF's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without GRHL3 | 0.053 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises EHF's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without IKZF2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[COL17A1]] | C | COL17A1 activity raises EHF's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 13.40× lower at baseline in the lines without COL17A1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises EHF's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 11.55× lower at baseline in the lines without SERPINB5 | 3e-04 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[ANKRD22]] | C | ANKRD22 activity raises EHF's level | lines that do not express ANKRD22 (34) vs lines expressing it (16) | 10.09× lower at baseline in the lines without ANKRD22 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises EHF's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 7.79× lower at baseline in the lines without PKP1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |
| [[HS3ST1]] | C | HS3ST1 activity raises EHF's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 8.64× lower at baseline in the lines without HS3ST1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises EHF's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 11.77× lower at baseline in the lines without TMPRSS2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |

### Downstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 29, C 35. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD11]] | B | EHF activity raises ABHD11's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without EHF | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[INPP4B]] | B | EHF activity raises INPP4B's level | lines that do not express EHF (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without EHF | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[MET]] | B | EHF activity raises MET's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.59× lower at baseline in the lines without EHF | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[FAM228B]] | B | EHF activity lowers FAM228B's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.90× higher at baseline in the lines without EHF | 0.031 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[GRHL3]] | B | EHF activity raises GRHL3's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without EHF | 0.036 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[STON2]] | B | EHF activity raises STON2's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.14× lower at baseline in the lines without EHF | 0.038 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | EHF activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express EHF (27) vs lines expressing it (21) | the lines without EHF: 1.21× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[PLEKHG3]] | B | EHF activity raises PLEKHG3's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.10× lower at baseline in the lines without EHF | 0.039 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[SAV1]] | B | EHF activity raises SAV1's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.27× lower at baseline in the lines without EHF | 0.045 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| cells under [[Pasireotide (acetate) (drug)]] 5 µM | B | EHF activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express EHF (27) vs lines expressing it (21) | the lines without EHF: 0.89× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[IL1R2]] | B | EHF activity raises IL1R2's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.91× lower at baseline in the lines without EHF | 0.053 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[SFR1]] | B | EHF activity raises SFR1's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without EHF | 0.059 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.2, 49.3); signed map (67.8, 8.2). **Vector** length 86.1, 27.5% of its response variance represented; |z| ≥ 3 in 694 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.5 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.8 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.4 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.8 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -5.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ETS homologous factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,621,093-34,663,288 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ESE3, ESEJ |
| Gene groups (HGNC) | ETS transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZC4](https://www.uniprot.org/uniprotkb/Q9NZC4) (ETS homologous factor):

> Transcriptional activator that may play a role in regulating epithelial cell differentiation and proliferation. May act as a repressor for a specific subset of ETS/AP-1-responsive genes and as a modulator of the nuclear response to mitogen-activated protein kinase signaling cascades. Binds to DNA sequences containing the consensus nucleotide core sequence GGAA. Involved in regulation of TNFRSF10B/DR5 expression through Ets-binding sequences on the TNFRSF10B/DR5 promoter. May contribute to …

**Summary**, from NCBI Gene [26298](https://www.ncbi.nlm.nih.gov/gene/26298):

> This gene encodes a protein that belongs to an ETS transcription factor subfamily characterized by epithelial-specific expression (ESEs). The encoded protein acts as a transcriptional repressor and may be involved in epithelial differentiation and carcinogenesis. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:3246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3246) · Entrez [26298](https://www.ncbi.nlm.nih.gov/gene/26298) · UniProt [Q9NZC4](https://www.uniprot.org/uniprotkb/Q9NZC4) · Ensembl [ENSG00000135373](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135373)

## Data

Gene col 5693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5693); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5693]; `tensor/DDL_lfc|DDL_z.npy` [5693]; `embed/gene_vectors.npy` [5693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5693 or target_col == 5693). Every well: [[EHF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
