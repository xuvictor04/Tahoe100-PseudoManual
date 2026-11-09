---
symbol: "DPY19L3"
type: "gene"
col: 10970
ensembl_id: "ENSG00000178904"
name: "dpy-19 like C-mannosyltransferase 3"
location: "19q13.11"
module: 142
arm: "+"
pooled_cpm: 45.62
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# DPY19L3

*dpy-19 like C-mannosyltransferase 3* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +4.8, q 8e-04, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.412× (z -17.4, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.507× (z -9.4, q 9e-19, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPP2]] (+0.67, fdr 7e-06), [[SFXN2]] (+0.65, fdr 8e-06), [[ARHGAP1]] (+0.62, fdr 7e-06); moves opposite to [[AKR1C3]] (-0.59, fdr 1e-05), [[GBP2]] (-0.57, fdr 1e-05), [[HNRNPH2]] (-0.56, fdr 9e-06).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 8e-04 | 24/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.412×** | -17.4 | 0e+00 | 42/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.435×** | -11.1 | 5e-26 | 43/48 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.507×** | -9.4 | 9e-19 | 39/48 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.613×** | -6.5 | 1e-08 | 37/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.632×** | -6.3 | 2e-08 | 31/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.580×** | -6.1 | 9e-08 | 39/48 (HT-29, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.645×** | -6.1 | 1e-07 | 41/49 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.667×** | -5.6 | 2e-06 | 27/48 (AsPC-1, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.672×** | -5.5 | 2e-06 | 28/48 (SW1417, NCI-H460, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.684×** | -5.5 | 2e-06 | 35/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.683×** | -5.3 | 7e-06 | 29/48 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.665×** | -5.2 | 9e-06 | 23/45 (RKO, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.497×** | -5.1 | 2e-05 | 30/49 (AsPC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.688×** | -5.0 | 3e-05 | 31/47 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.705×** | -4.8 | 5e-05 | 30/48 (CFPAC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.736×** | -4.7 | 1e-04 | 33/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.770×** | -4.6 | 1e-04 | 30/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.528×** | -4.6 | 1e-04 | 29/48 (NCI-H460, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -4.3 | 5e-04 | 30/48 (RKO, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.768×** | -3.6 | 0.007 | 21/47 (AsPC-1, A549, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.764×** | -3.5 | 0.010 | 22/48 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.011 | 19/48 (SW 1088, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 78.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -21.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.352× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 32.3 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -13.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.266× (z -13.3) |
| [[HS-578T (line)]] | alt | 64.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.207× (z -13.0) |
| [[A498 (line)]] | wt | 40.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -15.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.238× (z -13.3) |
| [[A549 (line)]] | wt | 92.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.161× (z -16.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.238× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.391× (z -9.0) |
| [[A-172 (line)]] | wt | 36.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.322× (z -8.5) |
| [[J82 (line)]] | alt | 52.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 46.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -12.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.236× (z -11.1) |
| [[PANC-1 (line)]] | alt | 63.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 37.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -12.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 33.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[AN3 CA (line)]] | alt | 67.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.206× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 33.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 40.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 47.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.208× (z -11.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 60.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 58.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 59.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 73.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.245× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.265× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H2030 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0680× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW480 (line)]] | alt | 59.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPP2]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SFXN2]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ARHGAP1]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GPR89A]] | +0.62 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CERS5]] | +0.61 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[RABEPK]] | +0.61 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TMEM243]] | +0.61 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TOP3A]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[RECQL]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.59 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[NBPF15]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[DCAF13]] | +0.58 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1C3]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[GBP2]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.56 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[DUSP8]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[GNGT1]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[BCL3]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[AKR1B1]] | -0.54 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RHOB]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[FOSL2]] | -0.54 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[EFNA1]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ZSCAN31]] | -0.53 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ING3]] | -0.53 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.9, -31.3); signed map (-47.3, 4.7). **Vector** length 117, 34.8% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -7.6 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.9 | -5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.5 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.3 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | dpy-19 like C-mannosyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,405,543-32,485,895 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZPD9](https://www.uniprot.org/uniprotkb/Q6ZPD9) (Protein C-mannosyl-transferase DPY19L3):

> C-mannosyltransferase that mediates C-mannosylation of tryptophan residues on target proteins. The reaction occurs on the luminal side of the endoplasmic reticulum and involves the transfer of a mannose unit from a dolichylphosphate mannose (Dol-P-Man) donor to an acceptor protein containing a WxxW or WxxC consensus sequence. C-mannosylates RSPO1, a Wnt signaling regulator, preferentially at the first Trp residue in the sequence WxxW. C-mannosylates the netrin receptor UNC5A, preferentially at …

**Summary**, from NCBI Gene [147991](https://www.ncbi.nlm.nih.gov/gene/147991):

> Enables mannosyltransferase activity. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27120) · Entrez [147991](https://www.ncbi.nlm.nih.gov/gene/147991) · UniProt [Q6ZPD9](https://www.uniprot.org/uniprotkb/Q6ZPD9) · Ensembl [ENSG00000178904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178904)

## Data

Gene col 10970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10970); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10970]; `tensor/DDL_lfc|DDL_z.npy` [10970]; `embed/gene_vectors.npy` [10970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10970 or target_col == 10970). Every well: [[DPY19L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
