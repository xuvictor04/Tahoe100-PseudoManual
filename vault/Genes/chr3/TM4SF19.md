---
symbol: "TM4SF19"
type: "gene"
col: 6958
ensembl_id: "ENSG00000145107"
name: "transmembrane 4 L six family member 19"
location: "3q29"
module: 229
arm: "+"
pooled_cpm: 31.37
n_lines_expressing: 30
n_dd_up: 32
n_dd_down: 54
n_dd_up_clean: 27
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 9
direction_downstream: 18
tags: ["gene", "module/229"]
generated_by: "tahoemap"
---

# TM4SF19

*transmembrane 4 L six family member 19* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.66× (z +13.2, q 3e-37, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.334× (z -20.8, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM4SF19-DYNLT2B]] (+0.92, fdr 7e-06, ⚠ same locus), [[ARHGAP22]] (+0.67, fdr 7e-06), [[LINC01705]] (+0.65, fdr 7e-06), [[GSTO1]] (+0.62, fdr 7e-06); moves opposite to [[ZNF608]] (-0.55, fdr 1e-05), [[TNS3]] (-0.53, fdr 3e-05), [[ARHGEF12]] (-0.53, fdr 4e-05).
> It is in [[Module 229]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[S100A16]] → it (grade B ⚠); 18 go from it, the strongest it → [[LUCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.66×** | +13.2 | 3e-37 | 24/28 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.93×** | +8.9 | 2e-16 | 22/28 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +6.6 | 7e-09 | 17/28 (A498, NCI-H1573, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.72×** | +5.2 | 2e-05 | 16/28 (SW480, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.50×** | +5.2 | 2e-05 | 15/28 (NCI-H460, A549, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 1e-04 | 13/28 (HOP62, CFPAC-1, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 2e-04 | 13/28 (HCT15, RKO, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.16×** | +4.5 | 4e-04 | 15/28 (HOP62, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.12×** | +4.4 | 6e-04 | 13/28 (A-172, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.40×** | +4.4 | 6e-04 | 14/29 (H4, J82, …) | top dose only | plate-row cell shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.37×** | +4.3 | 9e-04 | 12/27 (A498, CFPAC-1, …) | two highest doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.002 | 11/28 (CFPAC-1, SW480, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.96×** | +4.0 | 0.003 | 10/27 (A-172, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 12/28 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 15/28 (NCI-H1573, A-172, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.003 | 14/28 (J82, RKO, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.92×** | +3.8 | 0.004 | 11/27 (A-172, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.334×** | -20.8 | 0e+00 | 26/28 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.343×** | -14.4 | 2e-44 | 26/28 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -13.9 | 6e-42 | 26/28 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -13.7 | 1e-40 | 25/28 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -10.3 | 6e-23 | 20/28 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -10.2 | 2e-22 | 24/28 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.545×** | -10.0 | 1e-21 | 26/28 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.485×** | -9.0 | 2e-17 | 22/28 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.536×** | -8.8 | 6e-17 | 22/29 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.598×** | -8.4 | 2e-15 | 20/28 (HEC-1-A, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.562×** | -8.3 | 7e-15 | 21/28 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -8.1 | 2e-14 | 16/26 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.545×** | -8.1 | 2e-14 | 23/29 (SK-MEL-2, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.553×** | -7.9 | 9e-14 | 18/26 (A-172, RKO, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.571×** | -7.5 | 2e-12 | 18/28 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.567×** | -7.3 | 1e-11 | 18/27 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 44.6 | 1 | 14 | [[Auranofin (drug)]] 5 µM 2.99× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.1) |
| [[RKO (line)]] | wt | 285 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -19.6) |
| [[A-172 (line)]] | wt | 152 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 25.2 | 1 | 8 | [[Auranofin (drug)]] 5 µM 6.65× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.8) |
| [[A549 (line)]] | wt | 29.4 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 49.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -21.1) |
| [[H4 (line)]] | wt | 78.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -21.0) |
| [[J82 (line)]] | alt | 44.4 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 138 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 59.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -22.8) |
| [[NCI-H460 (line)]] | wt | 32.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.7) |
| [[SNU-423 (line)]] | alt | 27.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.2) |
| [[HOP62 (line)]] | alt | 38.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.0) |
| [[SW480 (line)]] | alt | 15.1 | 1 | 3 | [[Auranofin (drug)]] 5 µM 4.75× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.8) |
| [[A498 (line)]] | wt | 46.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.534× (z -10.0) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.05 µM 0.207× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.3) |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.00× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 11.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.99× (z +10.4) | — |
| [[A-427 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF19-DYNLT2B]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ARHGAP22]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[LINC01705]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DYNLT2B]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 | STRING 519; ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[GSTO1]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SHANK1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LAT]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ZNF83]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[LINC02970]] | +0.59 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[NBPF8]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RABGEF1P3]] | +0.58 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SH2D2A]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 | STRING 429 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.55 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TNS3]] | -0.53 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ARHGEF12]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[NFIB]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MXRA8]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[SHROOM3]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[HOPX]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CAND1]] | -0.49 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[RBM33]] | -0.49 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[RARRES1]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP17]] | -0.49 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[PLAC8]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A16]] | B | S100A16 activity raises TM4SF19's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 3.33× lower at baseline in the lines without S100A16 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[PLAUR]] | B | PLAUR activity raises TM4SF19's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 4.11× lower at baseline in the lines without PLAUR | 0.009 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[ARAP3]] | B | ARAP3 activity raises TM4SF19's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 4.12× lower at baseline in the lines without ARAP3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[RFX8]] | B | RFX8 activity raises TM4SF19's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.52× lower at baseline in the lines without RFX8 | 0.065 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[CRYM]] | B | CRYM activity raises TM4SF19's level | lines that do not express CRYM (12) vs lines expressing it (38) | 3.61× lower at baseline in the lines without CRYM | 0.077 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[RABGEF1P3]] | B | RABGEF1P3 activity raises TM4SF19's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 4.91× lower at baseline in the lines without RABGEF1P3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent; its own permutation p |
| [[TMEM158]] | B | TMEM158 activity raises TM4SF19's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without TMEM158 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[ZFPM2-AS1]] | C | ZFPM2-AS1 activity raises TM4SF19's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 3.29× lower at baseline in the lines without ZFPM2-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises TM4SF19's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without LINC01705 | 0.082 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUCAT1]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises LUCAT1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.79× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[MAP2K1]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises MAP2K1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.52× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[GPATCH2L]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises GPATCH2L's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.32× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[SPOCD1]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises SPOCD1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.26× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.035 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[SHC3]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises SHC3's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 2.13× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[RABGEF1P3]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises RABGEF1P3's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.70× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[S100A16]] | B | TM4SF19 activity raises S100A16's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without TM4SF19 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[ABHD16A]] | B | TM4SF19 activity lowers ABHD16A's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 1.28× higher at baseline in the lines without TM4SF19 | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[EFL1]] | B | TM4SF19 activity raises EFL1's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without TM4SF19 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[DYNLT2B]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity raises DYNLT2B's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.45× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[DGKG]] | B | TM4SF19 activity raises DGKG's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without TM4SF19 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[CORO2B]] | B | TM4SF19, [[TM4SF19-DYNLT2B]] activity strengthens CORO2B's drug response | lines that do not express TM4SF19, TM4SF19-DYNLT2B (11) vs lines expressing them (23) | the lines without TM4SF19, TM4SF19-DYNLT2B respond 0.55× as strongly (z diff +1.63); strongest at Homoharringtonine 5 µM: 0.72x vs 0.37x (z diff +3.6) | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; target measured in part of the lines; artifact flags; co-absent genes |

## Where it sits

- **Module**: [[Module 229]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.7, -3.5); signed map (14.3, 52.3). **Vector** length 108, 31.9% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -10.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.0 | -8.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -10.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -8.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 4 L six family member 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,319,342-196,338,503 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Transmembrane 4 L six family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DZ7](https://www.uniprot.org/uniprotkb/Q96DZ7) (Transmembrane 4 L6 family member 19):

> Negatively regulates vacuolar (H+)-ATPase (V-ATPase) activity by interacting with members of V-ATPase V0 complex and hence inhibiting V1-V0 complex assembly. Required for multinucleation during osteoclast differentiation.

**Summary**, from NCBI Gene [116211](https://www.ncbi.nlm.nih.gov/gene/116211):

> The protein encoded by this gene is a member of the four-transmembrane L6 superfamily. Members of this family function in various cellular processes including cell proliferation, motility, and adhesion via their interactions with integrins. In human brain tissue, this gene is expressed at high levels in the parietal lobe, occipital lobe, hippocampus, pons, white matter, corpus callosum, and cerebellum. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:25167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25167) · Entrez [116211](https://www.ncbi.nlm.nih.gov/gene/116211) · UniProt [Q96DZ7](https://www.uniprot.org/uniprotkb/Q96DZ7) · Ensembl [ENSG00000145107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145107)

## Data

Gene col 6958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6958); `tables/drug_effects.parquet` (90 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6958]; `tensor/DDL_lfc|DDL_z.npy` [6958]; `embed/gene_vectors.npy` [6958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6958 or target_col == 6958). Every well: [[TM4SF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM4SF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
