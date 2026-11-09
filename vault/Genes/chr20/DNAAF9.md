---
symbol: "DNAAF9"
type: "gene"
col: 1549
ensembl_id: "ENSG00000088854"
name: "dynein axonemal assembly factor 9"
location: "20p13"
module: 8
arm: "+"
pooled_cpm: 130.91
n_lines_expressing: 38
n_dd_up: 2
n_dd_down: 46
n_dd_up_clean: 1
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 19
direction_downstream: 10
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DNAAF9

*dynein axonemal assembly factor 9* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.31× (z +5.2, q 1e-04, up in 21 of 35 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.28× (z +5.1, q 1e-04, up in 21 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.200× (z -45.9, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OGG1]] (+0.62, fdr 1e-05), [[CLTCL1]] (+0.58, fdr 4e-05), [[TNNT1]] (+0.57, fdr 2e-05); moves opposite to [[DENND2D]] (-0.65, fdr 1e-05), [[SH2D4A]] (-0.63, fdr 1e-05), [[PLCH1]] (-0.63, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TNFSF15]] → it (grade B ⚠); 10 go from it, the strongest it → [[TNFSF15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +5.2 | 1e-04 | 21/35 (SW 900, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +5.1 | 1e-04 | 21/35 (NCI-H2030, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.9 | 0.016 | 9/36 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.14 | 15/36 (C32, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.200×** | -45.9 | 0e+00 | 36/36 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.232×** | -28.4 | 0e+00 | 34/36 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.420×** | -24.8 | 0e+00 | 36/37 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.377×** | -19.7 | 0e+00 | 36/37 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -19.6 | 0e+00 | 33/36 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.428×** | -17.1 | 0e+00 | 35/36 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.394×** | -16.8 | 0e+00 | 29/34 (HOP62, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.208×** | -16.6 | 0e+00 | 35/37 (HOP62, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.450×** | -16.1 | 0e+00 | 29/36 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.455×** | -15.3 | 0e+00 | 35/38 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.458×** | -15.2 | 0e+00 | 31/34 (A-427, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.463×** | -15.0 | 0e+00 | 34/35 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.480×** | -14.8 | 0e+00 | 31/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.482×** | -14.6 | 0e+00 | 35/36 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.487×** | -14.5 | 0e+00 | 30/36 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.493×** | -14.3 | 1e-44 | 31/36 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.591×** | -10.6 | 8e-25 | 32/36 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.392×** | -9.9 | 1e-21 | 26/36 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -8.0 | 3e-14 | 26/36 (J82, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -7.7 | 3e-13 | 31/36 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -7.3 | 5e-12 | 27/36 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -6.7 | 6e-10 | 27/36 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -6.5 | 2e-09 | 23/36 (A-172, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -5.9 | 8e-08 | 25/36 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 214 | 0 | 24 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0589× (z -49.2) |
| [[MIA PaCa-2 (line)]] | alt | 238 | 0 | 24 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -30.1) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 24 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -34.0) |
| [[HOP62 (line)]] | alt | 396 | 0 | 23 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0840× (z -45.5) |
| [[LOX-IMVI (line)]] | wt | 209 | 0 | 23 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -37.8) |
| [[J82 (line)]] | alt | 163 | 0 | 22 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -37.8) |
| [[PANC-1 (line)]] | alt | 154 | 0 | 22 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -34.2) |
| [[HS-578T (line)]] | alt | 212 | 0 | 20 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -49.4) |
| [[hTERT-HPNE (line)]] | wt | 279 | 0 | 20 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0602× (z -38.9) |
| [[HEC-1-A (line)]] | alt | 192 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -33.2) |
| [[RPMI-7951 (line)]] | alt | 396 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -39.8) |
| [[SNU-423 (line)]] | alt | 221 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -48.4) |
| [[A549 (line)]] | wt | 249 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -29.7) |
| [[SW480 (line)]] | alt | 171 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -22.1) |
| [[CFPAC-1 (line)]] | alt | 139 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -34.1) |
| [[H4 (line)]] | wt | 130 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -24.9) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -48.2) |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -24.0) |
| [[Hs 766T (line)]] | wt | 150 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -25.8) |
| [[SK-MEL-2 (line)]] | alt | 197 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -17.3) |
| [[SW 900 (line)]] | alt | 125 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.4) |
| [[BT-474 (line)]] | alt | 117 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -20.7) |
| [[C32 (line)]] | wt | 124 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -31.4) |
| [[Panc 03.27 (line)]] | alt | 87.5 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -19.4) |
| [[A498 (line)]] | wt | 64.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -32.5) |
| [[NCI-H1573 (line)]] | alt | 34.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.4) |
| [[SW 1088 (line)]] | alt | 287 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -17.4) |
| [[NCI-H2030 (line)]] | alt | 62.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 286 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.1) |
| [[SW 1271 (line)]] | alt | 237 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.2) |
| [[A-427 (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0946× (z -26.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.600× (z -8.5) |
| [[AN3 CA (line)]] | alt | 132 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.171× (z -12.0) |
| [[C-33 A (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 31.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGG1]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CLTCL1]] | +0.58 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[TNNT1]] | +0.57 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[FAM228B]] | +0.55 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MEIS3]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[WDR44]] | +0.53 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[TRPC1]] | +0.53 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[MEX3D]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PSMD9]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CCDC112]] | +0.53 | +0.53 / +0.28 | both halves | 3e-04 |  |
| [[RHBDF2]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ASL]] | +0.52 | +0.49 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2D]] | -0.65 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[SH2D4A]] | -0.63 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[PLCH1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[PROM1]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ABO]] | -0.57 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[SLC44A3-AS1]] | -0.57 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[GPD2]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[FAT1]] | -0.56 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[LINC02474]] | -0.56 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LINC02331]] | -0.56 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[SYK]] | -0.55 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[AKR1B1]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 14, C 5. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF15]] | B | TNFSF15 activity lowers DNAAF9's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 4.75× higher at baseline in the lines without TNFSF15 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[SYK]] | B | SYK activity lowers DNAAF9's level | lines that do not express SYK (30) vs lines expressing it (20) | 4.64× higher at baseline in the lines without SYK | 0.028 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[ZNF471]] | B | ZNF471 activity raises DNAAF9's level | lines that do not express ZNF471 (28) vs lines expressing it (22) | 3.44× lower at baseline in the lines without ZNF471 | 0.029 | ⚠ within organs, on part of the lines; also absent: TRIML2, ZNF667, ZNF667-AS1 |
| [[POU5F1B]] | B | POU5F1B activity lowers DNAAF9's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.73× higher at baseline in the lines without POU5F1B | 0.029 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[PCAT1]] | B | PCAT1 activity lowers DNAAF9's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 2.41× higher at baseline in the lines without PCAT1 | 0.044 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity lowers DNAAF9's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 3.21× higher at baseline in the lines without SAMD12-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[CYS1]] | B | CYS1 activity raises DNAAF9's level | lines that do not express CYS1 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without CYS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: MT1A, FMNL1-DT, SEC14L4 |
| [[TNNT1]] | B | TNNT1 activity raises DNAAF9's level | lines that do not express TNNT1 (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without TNNT1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, HDAC9; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DNAAF9's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ACTR3C]] | B | ACTR3C activity lowers DNAAF9's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 3.14× higher at baseline in the lines without ACTR3C | 0.080 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[STAC]] | B | STAC activity raises DNAAF9's level | lines that do not express STAC (25) vs lines expressing it (25) | 3.27× lower at baseline in the lines without STAC | 0.082 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[RHBDF2]] | B | RHBDF2 activity raises DNAAF9's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without RHBDF2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF15]] | B | DNAAF9 activity lowers TNFSF15's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 5.29× higher at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[NPHP3]] | B | DNAAF9 activity raises NPHP3's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 1.51× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[ABO]] | B | DNAAF9 activity lowers ABO's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 8.90× higher at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[TSHZ3]] | B | DNAAF9 activity raises TSHZ3's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 6.61× lower at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[RHBDF2]] | B | DNAAF9 activity raises RHBDF2's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[SLC25A43]] | B | DNAAF9 activity raises SLC25A43's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without DNAAF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[FBXO17]] | C | DNAAF9 activity raises FBXO17's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 8.54× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; co-absent with the target; its own permutation p |
| [[FERMT2]] | C | DNAAF9 activity raises FERMT2's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 7.59× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; co-absent with the target; its own permutation p |
| [[WIPF1]] | C | DNAAF9 activity raises WIPF1's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 6.31× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; co-absent with the target; its own permutation p |
| [[MRC2]] | C | DNAAF9 activity raises MRC2's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 6.13× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction -0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 46.3); signed map (-24.7, 23.9). **Vector** length 95.5, 36.3% of its response variance represented; |z| ≥ 3 in 1,407 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +2.9 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.5 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.3 | -13.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.2 | -14.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +5.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -16.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -14.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.2 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.0 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,249,306-3,407,669 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434N061; previously C20orf194 |
| Gene groups (HGNC) | Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TEA3](https://www.uniprot.org/uniprotkb/Q5TEA3) (Dynein axonemal assembly factor 9):

> Dynein axonemal assembly factor that regulates the transport and activation of ciliary outer dynein arms (ODAs), which are the main force generators in cilia. Essential for cilia movement and motility. Inhibits dyneins by reducing the affinity of ODAs for microtubules and hence inactivating the dyneins in the cytoplasm; the inhibition is relieved once dyneins enter the cilia (By similarity). May act as an effector for ARL3.

**Summary**, from NCBI Gene [25943](https://www.ncbi.nlm.nih.gov/gene/25943):

> This gene encodes an uncharacterized protein with a C-terminal coiled-coil region. The gene is located on chromosome 20p13 in a 1.8 Mb region linked to a spinocerebellar ataxia phenotype, but this gene does not appear to be a disease candidate. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:17721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17721) · Entrez [25943](https://www.ncbi.nlm.nih.gov/gene/25943) · UniProt [Q5TEA3](https://www.uniprot.org/uniprotkb/Q5TEA3) · Ensembl [ENSG00000088854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088854)

## Data

Gene col 1549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1549); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1549]; `tensor/DDL_lfc|DDL_z.npy` [1549]; `embed/gene_vectors.npy` [1549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1549 or target_col == 1549). Every well: [[DNAAF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
