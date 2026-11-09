---
symbol: "ARMC8"
type: "gene"
col: 3522
ensembl_id: "ENSG00000114098"
name: "armadillo repeat containing 8"
location: "3q22.3"
module: 229
arm: "+"
pooled_cpm: 81.72
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/229"]
generated_by: "tahoemap"
---

# ARMC8

*armadillo repeat containing 8* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 1.30× (z +5.7, q 6e-06, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.440× (z -18.0, q 0e+00, down in 48 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 15 lines (NCI-H23 0.266×, A-427 0.328×, HS-578T 0.260×, HEC-1-A 0.330×, …); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1573 0.167×, C32 0.200×, LoVo 0.276×, A-427 0.299×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.199×, SW480 0.298×, NCI-H1573 0.277×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STXBP5]] (+0.58, fdr 1e-05), [[TADA2A]] (+0.57, fdr 1e-05), [[KAT14]] (+0.55, fdr 1e-05); moves opposite to [[SLC5A3]] (-0.62, fdr 7e-06), [[POU2F2]] (-0.59, fdr 3e-05), [[NPTX1]] (-0.58, fdr 1e-05).
> It is in [[Module 229]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.30×** | +5.7 | 6e-06 | 26/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 7e-06 | 26/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.27×** | +5.3 | 3e-05 | 26/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.1 | 4e-05 | 34/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.4 | 0.001 | 24/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.064 | 13/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.10 | 4/48 (SNU-423, SNU-1, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.10 | 8/48 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.10 | 23/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.10 | 21/48 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3522.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 15 lines (NCI-H23 0.266×, A-427 0.328×, HS-578T 0.260×, HEC-1-A 0.330×, …); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1573 0.167×, C32 0.200×, LoVo 0.276×, A-427 0.299×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.199×, SW480 0.298×, NCI-H1573 0.277×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.440×** | -18.0 | 0e+00 | 48/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -14.4 | 2e-44 | 43/49 (NCI-H1573, C32, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -13.7 | 1e-40 | 35/45 (A-427, SW48, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.525×** | -13.6 | 1e-39 | 38/44 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.811×** | -4.6 | 5e-04 | 22/48 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.8 | 0.017 | 15/49 (A549, HOP62, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.896× | -3.4 | 0.052 | 7/49 (A-172, RKO, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.905× | -3.1 | 0.12 | 4/49 (SNU-1, hTERT-HPNE, …) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.12 | 13/48 (HT-29, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 69.6 | 6 | 2 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.48× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -13.7) |
| [[C32 (line)]] | wt | 80.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -15.4) |
| [[LoVo (line)]] | wt | 82.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -10.5) |
| [[PANC-1 (line)]] | alt | 114 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.426× (z -12.8) |
| [[SW480 (line)]] | alt | 107 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -14.6) |
| [[A-427 (line)]] | wt | 124 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 87.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.266× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 63.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -15.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -14.4) |
| [[SW1417 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.461× (z -9.7) |
| [[HS-578T (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.260× (z -15.6) |
| [[KATO III (line)]] | alt | 92.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -19.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -13.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 70.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.282× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 60.5 | 2 | 0 | [[Budesonide (drug)]] 5 µM 2.19× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.287× (z -11.6) |
| [[SHP-77 (line)]] | alt | 97.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 60.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.322× (z -12.9) |
| [[A498 (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.464× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.332× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 80.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0578× (z -16.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.363× (z -10.7) |
| [[J82 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.441× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 67.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.478× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.410× (z -12.2) |
| [[SNU-423 (line)]] | alt | 58.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.352× (z -11.5) |
| [[SW 900 (line)]] | alt | 62.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.421× (z -8.5) |
| [[SW48 (line)]] | wt | 85.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0897× (z -18.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TADA2A]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[KAT14]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[AHCTF1]] | +0.53 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[DICER1]] | +0.53 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[FKBP5]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ORC5]] | +0.52 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.52 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[CHPT1]] | +0.51 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FOXC2]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[MCMBP]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CCND3]] | +0.51 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A3]] | -0.62 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[POU2F2]] | -0.59 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[NPTX1]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ACVR1C]] | -0.58 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[MRPS6]] | -0.57 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[LINC01705]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GEM]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[RABGEF1P3]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NRIP3]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[FAM107B]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[CLN8]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[LINC00243]] | -0.55 | -0.40 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP1]] | B | MMP1 activity lowers ARMC8's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.22× higher at baseline in the lines without MMP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[LINC01705]] | B | LINC01705 activity lowers ARMC8's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.18× higher at baseline in the lines without LINC01705 | 0.037 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[LINC00536]] | B | LINC00536 activity lowers ARMC8's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 1.16× higher at baseline in the lines without LINC00536 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent |
| [[FAM107B]] | B | FAM107B activity lowers ARMC8's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.36× higher at baseline in the lines without FAM107B | 0.069 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[LINC01291]] | B | LINC01291 activity lowers ARMC8's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without LINC01291 | 0.071 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[TERT]] | C | TERT activity strengthens ARMC8's drug response | recorded gain-of-function mutation of TERT in 8 lines vs 38 not recorded | the TERT-altered lines respond 1.36× as strongly (z diff -0.79); strongest at Budesonide 5 µM: 1.82x vs 1.27x (z diff -2.7) | 0.260 over the table, 0.091 within its group | ⚠ within its group only (a lead); tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines; target measured in part of the lines; the reference differs |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 229]]; 6 genes; every member is in the + arm (projection on the module's main direction -0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.4, -10.5); signed map (-3.5, -39.7). **Vector** length 107, 29.5% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 5 µM |  | +5.2 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.0 | +5.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.0 | +2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.9 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.5 | -18.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,187,248-138,298,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC056, DKFZP434A043, GID5, VID28 |
| Gene groups (HGNC) | Armadillo repeat containing; CTLH complex subunits |
| Reactome | 5 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUR7](https://www.uniprot.org/uniprotkb/Q8IUR7) (Armadillo repeat-containing protein 8):

> Component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1.

**Summary**, from NCBI Gene [25852](https://www.ncbi.nlm.nih.gov/gene/25852):

> Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Located in cytosol and nucleoplasm. Part of ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24999) · Entrez [25852](https://www.ncbi.nlm.nih.gov/gene/25852) · UniProt [Q8IUR7](https://www.uniprot.org/uniprotkb/Q8IUR7) · Ensembl [ENSG00000114098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114098)

## Data

Gene col 3522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3522); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3522]; `tensor/DDL_lfc|DDL_z.npy` [3522]; `embed/gene_vectors.npy` [3522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3522 or target_col == 3522). Every well: [[ARMC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
