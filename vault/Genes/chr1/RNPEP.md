---
symbol: "RNPEP"
type: "gene"
col: 10710
ensembl_id: "ENSG00000176393"
name: "arginyl aminopeptidase"
location: "1q32.1"
module: 190
arm: "+"
pooled_cpm: 31.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# RNPEP

*arginyl aminopeptidase* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.34× (z +21.0, q 0e+00, up in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.23× (z +4.9, q 1e-04, up in 17 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.388× (z -33.0, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERMP1]] (+0.70, fdr 7e-06), [[GLB1]] (+0.70, fdr 7e-06), [[RPA1]] (+0.69, fdr 7e-06); moves opposite to [[NSRP1]] (-0.68, fdr 7e-06), [[HELQ]] (-0.65, fdr 7e-06), [[ZNF75A]] (-0.63, fdr 1e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CD163L1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +21.0 | 0e+00 | 38/43 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +17.9 | 0e+00 | 28/36 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +9.0 | 5e-17 | 27/41 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +4.9 | 1e-04 | 17/47 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.3 | 0.002 | 14/46 (A498, SW48, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +4.2 | 0.003 | 16/48 (LS 180, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +4.1 | 0.003 | 20/48 (A498, A-172, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.1 | 0.003 | 15/37 (A498, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.8 | 0.010 | 8/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.015 | 4/45 (LS 180, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.068 | 9/45 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | 1.13× | +3.1 | 0.083 | 14/46 (H4, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Quinestrol (drug)]] 5 µM |  | 1.09× | +3.1 | 0.096 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -33.0 | 0e+00 | 44/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -19.8 | 0e+00 | 39/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.501×** | -16.4 | 0e+00 | 41/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -9.6 | 1e-19 | 31/47 (LoVo, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -8.6 | 1e-15 | 28/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -7.9 | 2e-13 | 28/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.805×** | -5.4 | 7e-06 | 17/46 (AsPC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.821×** | -4.9 | 8e-05 | 21/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -4.6 | 2e-04 | 18/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.823×** | -4.6 | 2e-04 | 16/47 (SK-MEL-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.3 | 8e-04 | 18/47 (SW 1271, SNU-1, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.867× | -3.5 | 0.022 | 15/47 (RKO, SW 1271, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.855× | -3.2 | 0.057 | 8/46 (LS 180, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.05 µM |  | 0.868× | -3.2 | 0.057 | 4/48 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.057 | 6/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 0.880× | -3.2 | 0.057 | 5/48 (A-172, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.6 | 2 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -28.6) |
| [[A498 (line)]] | wt | 48.1 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -20.0) |
| [[PANC-1 (line)]] | alt | 28.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -26.0) |
| [[A549 (line)]] | wt | 28.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.9) |
| [[HT-29 (line)]] | alt | 36.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -16.5) |
| [[C32 (line)]] | wt | 80.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.5) |
| [[CFPAC-1 (line)]] | alt | 24.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.5) |
| [[HOP62 (line)]] | alt | 20.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.9) |
| [[KATO III (line)]] | alt | 28.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.8) |
| [[LoVo (line)]] | wt | 48.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -33.4) |
| [[NCI-H1573 (line)]] | alt | 25.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 33.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 49.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.8) |
| [[Hs 766T (line)]] | wt | 39.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.0) |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -15.1) |
| [[LS 180 (line)]] | wt | 35.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -15.1) |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.1) |
| [[A-172 (line)]] | wt | 36.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -11.6) |
| [[A-427 (line)]] | wt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -17.3) |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.107× (z -9.4) |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.0) |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.3) |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -9.0) |
| [[H4 (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0876× (z -9.7) |
| [[HCT15 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -8.7) |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.285× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.3) |
| [[RKO (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.2) |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.0) |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.0) |
| [[SW48 (line)]] | wt | 58.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.4) |
| [[SW480 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.9) |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERMP1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[GLB1]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[RPA1]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[EI24]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CNPY3]] | +0.67 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[KDM1A]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 | same gene group |
| [[NAPB]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RCN2]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ABCB10]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[LAPTM4B]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.68 | -0.66 / -0.68 | both halves | 7e-06 | same gene group |
| [[HELQ]] | -0.65 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[ZNF75A]] | -0.63 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[SURF6]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | -0.60 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[ZNF274]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[BPTF]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[TUT7]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ZNF829]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.58 | -0.58 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD163L1]] | B | CD163L1 activity lowers RNPEP's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 1.39× higher at baseline in the lines without CD163L1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.4, -14.7); signed map (-37.8, -14.2). **Vector** length 90.2, 19.2% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +21.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +4.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.5 | +1.1 |
|  | [[Asciminib (drug)]] 0.05 µM |  | +1.4 | +0.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -19.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -33.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -4.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.6 | -0.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | arginyl aminopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,982,372-202,006,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APB |
| Gene groups (HGNC) | Aminopeptidases; M1 metallopeptidases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4A4](https://www.uniprot.org/uniprotkb/Q9H4A4) (Aminopeptidase B):

> Exopeptidase which selectively removes arginine and/or lysine residues from the N-terminus of several peptide substrates including Arg(0)-Leu-enkephalin, Arg(0)-Met-enkephalin and Arg(-1)-Lys(0)-somatostatin-14. Can hydrolyze leukotriene A4 (LTA-4) into leukotriene B4 (LTB-4) (By similarity).

**Summary**, from NCBI Gene [6051](https://www.ncbi.nlm.nih.gov/gene/6051):

> Predicted to enable metalloaminopeptidase activity. Predicted to be involved in proteolysis. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10078) · Entrez [6051](https://www.ncbi.nlm.nih.gov/gene/6051) · UniProt [Q9H4A4](https://www.uniprot.org/uniprotkb/Q9H4A4) · Ensembl [ENSG00000176393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176393)

## Data

Gene col 10710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10710); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10710]; `tensor/DDL_lfc|DDL_z.npy` [10710]; `embed/gene_vectors.npy` [10710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10710 or target_col == 10710). Every well: [[RNPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
