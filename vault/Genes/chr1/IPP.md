---
symbol: "IPP"
type: "gene"
col: 12397
ensembl_id: "ENSG00000197429"
name: "kelch like family member 27"
location: "1p34.1"
module: 64
arm: "+"
pooled_cpm: 19.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# IPP

*kelch like family member 27* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.68× (z +8.1, q 3e-13, up in 22 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.27× (z +4.0, q 0.011, up in 16 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.495× (z -16.1, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.435× (z -13.5, q 5e-39, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM209]] (+0.58, fdr 1e-05), [[DDX59]] (+0.56, fdr 3e-05), [[PGGT1B]] (+0.56, fdr 3e-05); moves opposite to [[LHX4]] (-0.57, fdr 6e-05), [[DNAAF3]] (-0.54, fdr 4e-05), [[TNIK]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRMT2B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.1 | 3e-13 | 22/31 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.22×** | +4.5 | 0.002 | 19/48 (A498, RKO, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.3 | 0.004 | 19/41 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.011 | 16/47 (MIA PaCa-2, A498, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.14 | 7/48 (BT-474, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.495×** | -16.1 | 0e+00 | 42/47 (H4, LOX-IMVI, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -13.5 | 5e-39 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -13.3 | 3e-38 | 43/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -13.0 | 1e-36 | 40/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.485×** | -11.1 | 2e-26 | 41/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.509×** | -11.0 | 6e-26 | 36/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -10.9 | 7e-26 | 37/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.500×** | -10.8 | 2e-25 | 33/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -10.6 | 2e-24 | 37/47 (COLO 205, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.534×** | -9.8 | 8e-21 | 33/47 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -9.1 | 5e-18 | 37/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -9.1 | 5e-18 | 35/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.605×** | -8.1 | 2e-14 | 36/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -7.9 | 8e-14 | 33/45 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.635×** | -7.4 | 7e-12 | 29/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.627×** | -7.1 | 3e-11 | 30/45 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -6.4 | 4e-09 | 28/47 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -4.5 | 2e-04 | 19/48 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.794×** | -3.7 | 0.005 | 11/48 (C32, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.8 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.200× (z -15.5) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 6 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0411× (z -15.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.221× (z -14.1) |
| [[LoVo (line)]] | wt | 21.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -9.9) |
| [[PANC-1 (line)]] | alt | 36.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.2) |
| [[A-427 (line)]] | wt | 34.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -9.7) |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.266× (z -9.5) |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -10.8) |
| [[A549 (line)]] | wt | 15.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -10.4) |
| [[H4 (line)]] | wt | 21.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0934× (z -15.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.306× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -9.7) |
| [[A-172 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0755× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0906× (z -10.6) ⚠ toxic |
| [[J82 (line)]] | alt | 11.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -8.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -10.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -12.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM209]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DDX59]] | +0.56 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[PGGT1B]] | +0.56 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[FAIM]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[NCBP3]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PIGB]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.53 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[MTHFSD]] | +0.52 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[MTA3]] | +0.52 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[BLOC1S2]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GTF3C6]] | +0.52 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[SDHC]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHX4]] | -0.57 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[DNAAF3]] | -0.54 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[TNIK]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SLC6A6]] | -0.50 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[RARA]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ASMTL]] | -0.49 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[TGFB1]] | -0.48 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ITGA7]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SUN1]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[IL1RAP]] | -0.48 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PDP1]] | -0.46 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[CFAP45]] | -0.46 | -0.27 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRMT2B]] | C | TRMT2B's natural level strengthens IPP's drug response | TRMT2B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.15; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-15.9, 13.7); signed map (9.3, -32.9). **Vector** length 68.0, 12.9% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +5.5 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +4.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Amsacrine (drug)]] 0.5 µM |  | +1.8 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -8.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -7.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,694,324-45,750,653 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously IPP |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y573](https://www.uniprot.org/uniprotkb/Q9Y573) (Actin-binding protein IPP):

> May play a role in organizing the actin cytoskeleton.

**Summary**, from NCBI Gene [3652](https://www.ncbi.nlm.nih.gov/gene/3652):

> The protein encoded by this gene is a member of the kelch family of proteins, which is characterized by a 50 amino acid repeat which interacts with actin. Transcript variants have been described but their full-length nature has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6108) · Entrez [3652](https://www.ncbi.nlm.nih.gov/gene/3652) · UniProt [Q9Y573](https://www.uniprot.org/uniprotkb/Q9Y573) · Ensembl [ENSG00000197429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197429)

## Data

Gene col 12397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12397); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12397]; `tensor/DDL_lfc|DDL_z.npy` [12397]; `embed/gene_vectors.npy` [12397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12397 or target_col == 12397). Every well: [[IPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
