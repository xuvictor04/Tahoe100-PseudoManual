---
symbol: "FSIP2-AS1"
type: "gene"
col: 13805
ensembl_id: "ENSG00000231646"
name: "FSIP2 antisense RNA 1"
location: "2q32.1"
module: 26
arm: "+"
pooled_cpm: 12.12
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 25
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 42
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FSIP2-AS1

*FSIP2 antisense RNA 1* — 2q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +5.0, q 3e-04, up in 19 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.306× (z -10.1, q 5e-21, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAM]] (+0.77, fdr 7e-06), [[LRGUK]] (+0.76, fdr 7e-06), [[TMEM232]] (+0.73, fdr 7e-06); moves opposite to [[SEMA4F]] (-0.57, fdr 3e-05), [[LRRC20]] (-0.56, fdr 8e-05), [[L2HGDH]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02516]] → it (grade B ⚠); 42 go from it, the strongest it → [[LINC01473]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +5.0 | 3e-04 | 19/37 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 0.007 | 19/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.013 | 17/41 (KATO III, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +3.9 | 0.013 | 19/41 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.013 | 17/41 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.013 | 20/41 (LS 180, C-33 A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.018 | 16/41 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.024 | 16/41 (LoVo, HepG2/C3A, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.041 | 14/41 (A498, LS 180, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.088 | 16/41 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.092 | 7/41 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.093 | 11/40 (NCI-H460, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.093 | 12/41 (SW480, A498, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.100 | 8/41 (KATO III, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.306×** | -10.1 | 5e-21 | 31/41 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.329×** | -9.5 | 9e-19 | 31/40 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.344×** | -9.1 | 2e-17 | 34/41 (hTERT-HPNE, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.358×** | -8.7 | 4e-16 | 29/40 (NCI-H1792, HT-29, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.387×** | -8.1 | 7e-14 | 31/41 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.373×** | -8.1 | 7e-14 | 27/33 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.422×** | -7.3 | 2e-11 | 33/41 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.195×** | -7.3 | 3e-11 | 30/40 (NCI-H1573, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.457×** | -6.6 | 2e-09 | 30/41 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.504×** | -5.8 | 4e-07 | 25/41 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.503×** | -5.6 | 1e-06 | 21/33 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.548×** | -5.1 | 2e-05 | 25/41 (HCT15, SW480, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -4.6 | 2e-04 | 22/37 (SW 900, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -4.5 | 3e-04 | 22/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.582×** | -4.3 | 6e-04 | 23/40 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.722×** | -3.9 | 0.003 | 21/41 (HT-29, BT-474, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.669×** | -3.4 | 0.019 | 18/40 (HepG2/C3A, HT-29, …) | rises with dose | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.757×** | -3.3 | 0.024 | 10/42 (C-33 A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.491×** | -3.2 | 0.041 | 13/41 (HepG2/C3A, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -2.9 | 0.077 | 12/41 (HOP62, H4, …) | top dose only | plate-row cell shift |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.706×** | -2.9 | 0.077 | 10/41 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.616×** | -2.9 | 0.077 | 9/41 (C32, NCI-H460, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.66 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 39.2 | 1 | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0544× (z -19.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0873× (z -17.2) |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0412× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 0 | 7 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0729× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.132× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0581× (z -14.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0988× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0682× (z -11.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.145× (z -8.8) |
| [[A498 (line)]] | wt | 15.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.108× (z -9.4) |
| [[COLO 205 (line)]] | alt | 9.22 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0564× (z -10.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0578× (z -10.3) |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 2 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.136× (z -10.8) |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.198× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0819× (z -12.2) |
| [[C-33 A (line)]] | alt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +9.0) | — |
| [[C32 (line)]] | wt | 20.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.115× (z -9.0) |
| [[HCT15 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +8.6) | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0814× (z -10.5) ⚠ toxic |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0675× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 7.97 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0849× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.1) ⚠ cell-cycle shift, explains ~74% of this change |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAM]] | +0.77 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[LRGUK]] | +0.76 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[TMEM232]] | +0.73 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[LINC01252]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[CXCL13]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.69 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.69 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[SGO1-AS1]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 | same gene group |
| [[LINC02398]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[UBA6-DT]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.68 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[PRR4]] | +0.67 | +0.54 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4F]] | -0.57 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[LRRC20]] | -0.56 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[L2HGDH]] | -0.56 | -0.57 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02516]] | B | LINC02516 activity raises FSIP2-AS1's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without LINC02516 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |
| [[LINC01917]] | B | LINC01917 activity raises FSIP2-AS1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without LINC01917 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity raises FSIP2-AS1's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers FSIP2-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[LINC02398]] | B | LINC02398 activity raises FSIP2-AS1's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without LINC02398 | 0.081 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[PMFBP1]] | C | PMFBP1 activity raises FSIP2-AS1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 3.04× lower at baseline in the lines without PMFBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent; co-absent with the target |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises FSIP2-AS1's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 41, C 1. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01473]] | B | FSIP2-AS1 activity raises LINC01473's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without FSIP2-AS1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[DLG2]] | B | FSIP2-AS1 activity raises DLG2's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without FSIP2-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[PSMD7-DT]] | B | FSIP2-AS1 activity raises PSMD7-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FSIP2-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[C21orf62-AS1]] | B | FSIP2-AS1 activity raises C21orf62-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without FSIP2-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LRRC39]] | B | FSIP2-AS1 activity raises LRRC39's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without FSIP2-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[ITPR2-AS1]] | B | FSIP2-AS1 activity raises ITPR2-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without FSIP2-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[CCDC30]] | B | FSIP2-AS1 activity raises CCDC30's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.36× lower at baseline in the lines without FSIP2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[ALDH8A1]] | B | FSIP2-AS1 activity raises ALDH8A1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without FSIP2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[MFSD4B]] | B | FSIP2-AS1 activity raises MFSD4B's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without FSIP2-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TIAM2]] | B | FSIP2-AS1 activity raises TIAM2's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without FSIP2-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[RFX3-DT]] | B | FSIP2-AS1 activity raises RFX3-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without FSIP2-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[PRR4]] | B | FSIP2-AS1 activity raises PRR4's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without FSIP2-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.2, 15.6); signed map (23.4, 2.1). **Vector** length 96.7, 23.2% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.8 | -10.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -0.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | FSIP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q32.1 — chr2:185,653,303-185,802,323 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously FSIP2-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40978) · Entrez [107985781](https://www.ncbi.nlm.nih.gov/gene/107985781) · Ensembl [ENSG00000231646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231646)

## Data

Gene col 13805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13805); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13805]; `tensor/DDL_lfc|DDL_z.npy` [13805]; `embed/gene_vectors.npy` [13805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13805 or target_col == 13805). Every well: [[FSIP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FSIP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
