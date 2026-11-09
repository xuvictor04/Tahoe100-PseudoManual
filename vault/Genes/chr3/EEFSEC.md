---
symbol: "EEFSEC"
type: "gene"
col: 5313
ensembl_id: "ENSG00000132394"
name: "eukaryotic elongation factor, selenocysteine-tRNA specific"
location: "3q21.3"
module: 1
arm: "+"
pooled_cpm: 66.99
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EEFSEC

*eukaryotic elongation factor, selenocysteine-tRNA specific* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.79× (z +7.5, q 3e-11, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.484× (z -9.3, q 7e-18, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.625× (z -8.5, q 3e-15, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMSS1]] (+0.70, fdr 7e-06), [[EIF2B3]] (+0.69, fdr 7e-06), [[MPHOSPH6]] (+0.67, fdr 7e-06); moves opposite to [[TMEM59]] (-0.69, fdr 8e-06), [[ATOSA]] (-0.65, fdr 1e-05), [[ZNF821]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +7.5 | 3e-11 | 44/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.8 | 3e-04 | 34/48 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 3e-04 | 34/48 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.5 | 9e-04 | 35/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -9.3 | 7e-18 | 42/48 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -8.6 | 2e-15 | 39/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -8.5 | 3e-15 | 42/48 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.284×** | -8.5 | 4e-15 | 44/49 (PANC-1, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.532×** | -8.1 | 6e-14 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -8.1 | 6e-14 | 38/47 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -7.7 | 1e-12 | 29/41 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -7.4 | 7e-12 | 41/48 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.577×** | -6.8 | 7e-10 | 30/48 (A498, NCI-H460, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.373×** | -6.6 | 2e-09 | 34/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.407×** | -6.0 | 8e-08 | 29/45 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.665×** | -5.2 | 8e-06 | 36/48 (J82, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.652×** | -5.1 | 2e-05 | 29/44 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.676×** | -5.0 | 2e-05 | 29/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.694×** | -4.7 | 1e-04 | 28/48 (HOP62, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.685×** | -4.6 | 2e-04 | 33/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -4.2 | 8e-04 | 29/48 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.671×** | -3.6 | 0.008 | 28/48 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.010 | 22/48 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.051 | 22/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 190 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 50.3 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.254× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.309× (z -11.0) |
| [[PANC-1 (line)]] | alt | 79.0 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.123× (z -11.2) |
| [[HOP62 (line)]] | alt | 63.3 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 125 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -17.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 6 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 96.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0836× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -17.9) |
| [[A-172 (line)]] | wt | 62.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -18.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 39.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0981× (z -15.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 82.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.5) |
| [[LS 180 (line)]] | wt | 55.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 56.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.7) |
| [[A498 (line)]] | wt | 41.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 55.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0660× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 48.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 54.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 63.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.2) |
| [[SW480 (line)]] | alt | 86.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.409× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 93.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -15.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 78.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.309× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 67.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.6) |
| [[Hs 766T (line)]] | wt | 40.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.108× (z -8.6) |
| [[KATO III (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 71.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.411× (z -9.1) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 35.8 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0392× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 47.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 43.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.9) |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.206× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.235× (z -9.0) |
| [[SW48 (line)]] | wt | 58.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMSS1]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 | STRING 416 |
| [[MPHOSPH6]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PINX1]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[HLCS]] | +0.63 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZBED4]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[LYAR]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[ACSF3]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PGAM5]] | +0.62 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[FARSB]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 | STRING 490 |
| [[MTG1]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | -0.69 | -0.58 / -0.73 | both halves | 8e-06 |  |
| [[ATOSA]] | -0.65 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[ZNF821]] | -0.63 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[IST1]] | -0.62 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[GNAS]] | -0.62 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[TSC22D4]] | -0.61 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[ARL6IP5]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.61 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[GIPC2]] | -0.59 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[RARG]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PRRT1]] | -0.59 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers EEFSEC's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.2, -42.0); signed map (-7.0, -48.4). **Vector** length 96.8, 29.6% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.8 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -7.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic elongation factor, selenocysteine-tRNA specific |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,153,481-128,408,646 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SELB, EFSEC |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 3 pathways, smallest: Selenocysteine synthesis; Selenoamino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P57772](https://www.uniprot.org/uniprotkb/P57772) (Selenocysteine-specific elongation factor):

> Translation factor required for the incorporation of the rare amino acid selenocysteine encoded by UGA codons. Replaces the eRF1-eRF3-GTP ternary complex for the insertion of selenocysteine directed by the UGA codon. Insertion of selenocysteine at UGA codons is mediated by SECISBP2 and EEFSEC: SECISBP2 (1) specifically binds the SECIS sequence once the 80S ribosome encounters an in-frame UGA codon and (2) contacts the RPS27A/eS31 of the 40S ribosome before ribosome stalling. (3) GTP-bound …

**Summary**, from NCBI Gene [60678](https://www.ncbi.nlm.nih.gov/gene/60678):

> Enables GTPase activity. Involved in selenocysteine incorporation. Predicted to be located in cytoplasm and nucleus. Predicted to be part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24614) · Entrez [60678](https://www.ncbi.nlm.nih.gov/gene/60678) · UniProt [P57772](https://www.uniprot.org/uniprotkb/P57772) · Ensembl [ENSG00000132394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132394)

## Data

Gene col 5313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5313); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5313]; `tensor/DDL_lfc|DDL_z.npy` [5313]; `embed/gene_vectors.npy` [5313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5313 or target_col == 5313). Every well: [[EEFSEC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEFSEC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
