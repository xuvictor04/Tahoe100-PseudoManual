---
symbol: "ALG6"
type: "gene"
col: 1518
ensembl_id: "ENSG00000088035"
name: "ALG6 alpha-1,3-glucosyltransferase"
location: "1p31.3"
module: 175
arm: "+"
pooled_cpm: 17.46
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ALG6

*ALG6 alpha-1,3-glucosyltransferase* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.34× (z +4.4, q 0.005, up in 17 of 47 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.31× (z +4.0, q 0.021, up in 13 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.383× (z -20.4, q 0e+00, down in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.353× (z -15.1, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP40]] (+0.72, fdr 7e-06), [[ABCB10]] (+0.69, fdr 7e-06), [[CSE1L]] (+0.68, fdr 7e-06); moves opposite to [[NBPF10]] (-0.60, fdr 1e-05), [[TUT7]] (-0.60, fdr 1e-05), [[SLC22A1]] (-0.57, fdr 2e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.34×** | +4.4 | 0.005 | 17/47 (MIA PaCa-2, NCI-H2347, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.021 | 13/47 (BT-474, CHP-212, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.035 | 10/48 (HS-578T, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.047 | 10/45 (C32, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **1.27×** | +3.4 | 0.073 | 16/43 (SW480, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +3.3 | 0.081 | 6/48 (C32, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.24× | +3.2 | 0.12 | 11/47 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.12 | 10/45 (NCI-H460, H4, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.12 | 5/47 (LoVo, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.383×** | -20.4 | 0e+00 | 40/47 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.353×** | -15.1 | 0e+00 | 38/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.379×** | -14.6 | 0e+00 | 42/45 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.382×** | -14.5 | 3e-45 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -12.0 | 6e-31 | 38/46 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -11.0 | 6e-26 | 39/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.513×** | -10.0 | 9e-22 | 32/47 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -8.1 | 3e-14 | 27/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -5.5 | 2e-06 | 23/45 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -5.2 | 9e-06 | 25/47 (NCI-H23, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -5.1 | 1e-05 | 24/47 (SW480, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.750×** | -4.3 | 7e-04 | 15/47 (hTERT-HPNE, NCI-H23, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.003 | 18/47 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.003 | 19/48 (KATO III, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.782×** | -3.7 | 0.009 | 16/48 (NCI-H460, SW 1088, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.091 | 11/47 (NCI-H2030, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.0 | 0.093 | 19/47 (LoVo, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.197× (z -13.0) |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -15.4) |
| [[LoVo (line)]] | wt | 15.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.216× (z -10.8) |
| [[A498 (line)]] | wt | 16.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.166× (z -13.6) |
| [[A549 (line)]] | wt | 12.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.176× (z -10.8) |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -11.1) |
| [[J82 (line)]] | alt | 14.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.158× (z -11.3) |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.216× (z -9.8) |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0740× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.135× (z -9.6) |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -10.5) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -14.2) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -11.1) |
| [[A-427 (line)]] | wt | 32.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -11.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -8.7) |
| [[H4 (line)]] | wt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.182× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.165× (z -11.0) |
| [[RKO (line)]] | wt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.2) |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.104× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -17.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 1 | — | [[Pasireotide (acetate) (drug)]] 0.5 µM 0.0514× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -8.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 8.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -15.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP40]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ABCB10]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SKP2]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[RPA1]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[PCCB]] | +0.67 | +0.76 / +0.52 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[COPS7B]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NDC1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[NAE1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[COPG2]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KDM1A]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF10]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TUT7]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[SLC22A1]] | -0.57 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[BOD1L1]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SPATC1]] | -0.57 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[EIF4EBP3]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[ATXN1]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[DLX2]] | -0.55 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[MTHFR]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CPEB4]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[OFD1]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP2]] | B | BMP2 activity lowers ALG6's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 1.35× higher at baseline in the lines without BMP2 | 0.063 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[C11orf96]] | B | C11orf96 activity lowers ALG6's level | lines that do not express C11orf96 (17) vs lines expressing it (33) | 1.31× higher at baseline in the lines without C11orf96 | 0.088 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, ZNF569, PPP1R3C |
| [[MVB12B]] | B | MVB12B activity raises ALG6's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without MVB12B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises ALG6's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without DSCC1 | 0.035 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, -14.7); signed map (-38.8, -15.3). **Vector** length 75.7, 14.8% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.7 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | +3.3 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | -0.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.8 | -20.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -15.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -14.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ALG6 alpha-1,3-glucosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:63,367,575-63,438,553 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Alpha-1,3-glucosyltransferases |
| Reactome | 5 pathways, smallest: Diseases associated with N-glycosylation of proteins; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y672](https://www.uniprot.org/uniprotkb/Q9Y672) (Dolichyl pyrophosphate Man9GlcNAc2 alpha-1,3-glucosyltransferase):

> Dolichyl pyrophosphate Man9GlcNAc2 alpha-1,3-glucosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, including …

**Summary**, from NCBI Gene [29929](https://www.ncbi.nlm.nih.gov/gene/29929):

> This gene encodes a member of the ALG6/ALG8 glucosyltransferase family. The encoded protein catalyzes the addition of the first glucose residue to the growing lipid-linked oligosaccharide precursor of N-linked glycosylation. Mutations in this gene are associated with congenital disorders of glycosylation type Ic. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23157) · Entrez [29929](https://www.ncbi.nlm.nih.gov/gene/29929) · UniProt [Q9Y672](https://www.uniprot.org/uniprotkb/Q9Y672) · Ensembl [ENSG00000088035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088035)

## Data

Gene col 1518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1518); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1518]; `tensor/DDL_lfc|DDL_z.npy` [1518]; `embed/gene_vectors.npy` [1518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1518 or target_col == 1518). Every well: [[ALG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
