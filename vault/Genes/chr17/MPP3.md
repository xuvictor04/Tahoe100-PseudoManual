---
symbol: "MPP3"
type: "gene"
col: 8445
ensembl_id: "ENSG00000161647"
name: "MAGUK p55 scaffold protein 3"
location: "17q21.31"
module: 18
arm: "+"
pooled_cpm: 34.19
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 35
n_dd_up_clean: 3
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MPP3

*MAGUK p55 scaffold protein 3* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 1.28× (z +4.5, q 0.002, up in 20 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.30× (z +4.4, q 0.002, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -22.5, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPSM1]] (+0.73, fdr 7e-06), [[FPGS]] (+0.72, fdr 7e-06), [[SHLD2]] (+0.69, fdr 7e-06); moves opposite to [[ITM2B]] (-0.64, fdr 1e-05), [[CDKN1B]] (-0.64, fdr 8e-06), [[EFNA1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GPR161]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +4.5 | 0.002 | 20/46 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +4.4 | 0.002 | 23/46 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 0.002 | 17/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.4 | 0.002 | 17/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +4.2 | 0.003 | 18/47 (NCI-H460, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.0 | 0.005 | 24/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.019 | 16/46 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.2 | 0.11 | 0/47 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.15 | 13/46 (hTERT-HPNE, RPMI-7951, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.417×** | -22.5 | 0e+00 | 41/46 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.421×** | -22.2 | 0e+00 | 40/46 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.338×** | -18.0 | 0e+00 | 41/47 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.378×** | -17.7 | 0e+00 | 39/47 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.361×** | -16.9 | 0e+00 | 41/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.419×** | -15.8 | 0e+00 | 36/47 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.392×** | -15.5 | 0e+00 | 43/47 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.459×** | -14.2 | 1e-43 | 37/47 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.261×** | -12.8 | 2e-35 | 42/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.570×** | -10.2 | 9e-23 | 29/44 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.576×** | -10.0 | 6e-22 | 37/47 (LoVo, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -9.6 | 5e-20 | 34/47 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -8.9 | 4e-17 | 29/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.587×** | -8.9 | 4e-17 | 23/36 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.639×** | -8.1 | 2e-14 | 30/46 (LoVo, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.647×** | -7.9 | 9e-14 | 28/47 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.486×** | -6.8 | 2e-10 | 30/46 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.727×** | -5.8 | 2e-07 | 25/47 (LoVo, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.709×** | -5.7 | 3e-07 | 24/46 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 50.7 | 0 | 17 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -18.4) |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 15 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 57.2 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -21.6) |
| [[HOP62 (line)]] | alt | 50.6 | 0 | 12 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.124× (z -19.0) |
| [[LOX-IMVI (line)]] | wt | 51.6 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -18.8) |
| [[MIA PaCa-2 (line)]] | alt | 55.4 | 0 | 12 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 39.6 | 0 | 12 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.233× (z -13.7) |
| [[LoVo (line)]] | wt | 52.6 | 0 | 11 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.217× (z -14.7) |
| [[A498 (line)]] | wt | 55.5 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -19.4) |
| [[RKO (line)]] | wt | 63.8 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0965× (z -28.0) |
| [[SW48 (line)]] | wt | 55.4 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0600× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0942× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0564× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.7) |
| [[J82 (line)]] | alt | 36.7 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -14.6) |
| [[SNU-1 (line)]] | wt | 49.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.3) |
| [[SNU-423 (line)]] | alt | 33.8 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.182× (z -12.9) |
| [[A-427 (line)]] | wt | 29.0 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -12.5) |
| [[A549 (line)]] | wt | 47.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.8) |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -18.6) |
| [[AsPC-1 (line)]] | alt | 27.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.2) |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.354× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -10.1) |
| [[SW480 (line)]] | alt | 23.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.6) |
| [[H4 (line)]] | wt | 47.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.1) |
| [[Hs 766T (line)]] | wt | 22.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 33.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -9.7) |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.3) |
| [[SW1417 (line)]] | alt | 22.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.413× (z -8.8) |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0985× (z -8.7) |
| [[C32 (line)]] | wt | 13.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.9) |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.4) |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.7) |
| [[BT-474 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPSM1]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 | STRING 409 |
| [[FPGS]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SHLD2]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[HMOX2]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[GARNL3]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MON1A]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[NLN]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[RRP7BP-1]] | +0.63 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[DCAF4]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ADCY7]] | +0.62 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[RBAK-RBAKDN]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC18]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2B]] | -0.64 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.64 | -0.62 / -0.58 | both halves | 8e-06 |  |
| [[EFNA1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[STAG2]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[MINDY1]] | -0.59 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MAT2B]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[FMR1]] | -0.57 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[DECR1]] | -0.57 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[PCM1]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[HNMT]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.57 | -0.46 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR161]] | B | GPR161 activity raises MPP3's level | lines that do not express GPR161 (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without GPR161 | 0.022 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PPP2R3A, NKAIN1 |
| [[TOP2A]] | B | TOP2A activity raises MPP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01399]] | B | LINC01399 activity raises MPP3's level | lines that do not express LINC01399 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without LINC01399 | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC02885, ENSG00000258168, PCDHB2; maybe low, not absent |
| [[CLTCL1]] | C | CLTCL1 activity raises MPP3's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.71× lower at baseline in the lines without CLTCL1 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[FSD1L]] | C | FSD1L activity raises MPP3's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without FSD1L | 0.030 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[ATG2B]] | C | ATG2B's natural level weakens MPP3's drug response | ATG2B's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.39; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MYO19]] | C | MYO19's natural level strengthens MPP3's drug response | MYO19's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.36; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RUSC2]] | C | RUSC2 activity raises MPP3's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without RUSC2 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |
| [[CAMKK2]] | C | CAMKK2's natural level strengthens MPP3's drug response | CAMKK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.25; direction not clear | 0.093 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.427). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-2.6, -27.5); signed map (-44.9, -3.3). **Vector** length 106, 31.5% of its response variance represented; |z| ≥ 3 in 1,399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.7 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.9 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.2 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.6 | -12.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -15.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -18.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | MAGUK p55 scaffold protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,800,799-43,833,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DLG3 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13368](https://www.uniprot.org/uniprotkb/Q13368) (MAGUK p55 subfamily member 3):

> Participates in cell spreading through the phosphoinositide-3-kinase (PI3K) pathway by connecting CADM1 to DLG1 and the regulatory subunit of phosphoinositide-3-kinase (PI3K). Stabilizes HTR2C at the plasma membrane and prevents its desensitization. May participates in the maintenance of adherens junctions (By similarity).

**Summary**, from NCBI Gene [4356](https://www.ncbi.nlm.nih.gov/gene/4356):

> This gene product is a member of a family of membrane-associated proteins termed MAGUKs (membrane-associated guanylate kinase homologs). MAGUKs interact with the cytoskeleton and regulate cell proliferation, signaling pathways, and intracellular junctions. This protein contains a conserved sequence, called the SH3 (src homology 3) motif, found in several other proteins that associate with the cytoskeleton and are suspected to play important roles in signal transduction. Alternatively spliced …

**Accessions** — [HGNC:7221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7221) · Entrez [4356](https://www.ncbi.nlm.nih.gov/gene/4356) · UniProt [Q13368](https://www.uniprot.org/uniprotkb/Q13368) · Ensembl [ENSG00000161647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161647)

## Data

Gene col 8445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8445); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8445]; `tensor/DDL_lfc|DDL_z.npy` [8445]; `embed/gene_vectors.npy` [8445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8445 or target_col == 8445). Every well: [[MPP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
