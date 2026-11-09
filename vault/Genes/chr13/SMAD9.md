---
symbol: "SMAD9"
type: "gene"
col: 4206
ensembl_id: "ENSG00000120693"
name: "SMAD family member 9"
location: "13q13.3"
module: 103
arm: "+"
pooled_cpm: 39.44
n_lines_expressing: 39
n_dd_up: 11
n_dd_down: 47
n_dd_up_clean: 10
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# SMAD9

*SMAD family member 9* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.41× (z +5.0, q 4e-04, up in 20 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.400× (z -18.8, q 0e+00, down in 31 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM2B-DT]] (+0.64, fdr 7e-06), [[TMEM45A]] (+0.61, fdr 1e-05), [[TET1]] (+0.59, fdr 1e-05); moves opposite to [[CYP2D7]] (-0.54, fdr 3e-05), [[MYO7B]] (-0.53, fdr 5e-05), [[HNF4A]] (-0.47, fdr 6e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[USH1C]] → it (grade B ⚠); 17 go from it, the strongest it → [[KDM2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.0 | 4e-04 | 20/37 (RKO, HOP62, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 0.002 | 22/37 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 0.002 | 20/36 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.004 | 16/36 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.006 | 15/36 (A498, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.28×** | +3.9 | 0.011 | 15/37 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.034 | 14/37 (SHP-77, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.034 | 16/37 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.034 | 16/36 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.049 | 14/37 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.052 | 12/37 (SHP-77, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.068 | 12/37 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.400×** | -18.8 | 0e+00 | 31/37 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.331×** | -16.0 | 0e+00 | 31/37 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.385×** | -13.8 | 3e-41 | 32/37 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.394×** | -13.5 | 2e-39 | 30/36 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.391×** | -13.1 | 4e-37 | 33/36 (HCT15, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.416×** | -12.7 | 6e-35 | 31/37 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.451×** | -11.5 | 6e-29 | 33/37 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -11.5 | 8e-29 | 33/36 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.503×** | -10.0 | 1e-21 | 31/36 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -9.5 | 1e-19 | 32/36 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -8.9 | 3e-17 | 32/37 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.539×** | -8.5 | 1e-15 | 30/37 (C32, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.329×** | -8.4 | 2e-15 | 29/36 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -8.1 | 2e-14 | 28/38 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -8.1 | 3e-14 | 28/37 (NCI-H1792, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -7.8 | 3e-13 | 27/37 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.659×** | -6.0 | 5e-08 | 23/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 112 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -23.0) |
| [[MIA PaCa-2 (line)]] | alt | 87.6 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -26.4) |
| [[NCI-H1792 (line)]] | alt | 80.2 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.6) |
| [[HCT15 (line)]] | alt | 112 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 69.6 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -24.7) |
| [[J82 (line)]] | alt | 61.8 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -18.2) |
| [[SNU-1 (line)]] | wt | 69.1 | 0 | 10 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -14.5) |
| [[A-172 (line)]] | wt | 113 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 29.4 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 47.1 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -14.4) |
| [[SNU-423 (line)]] | alt | 42.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -24.4) |
| [[C-33 A (line)]] | alt | 183 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0505× (z -27.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.185× (z -16.8) |
| [[SHP-77 (line)]] | alt | 225 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -16.1) |
| [[HOP62 (line)]] | alt | 40.1 | 1 (1 ⚠) | 5 | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +11.6) ⚠ position not correctable | [[Panobinostat (drug)]] 5 µM 0.141× (z -13.0) |
| [[CHP-212 (line)]] | wt | 157 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -13.2) |
| [[PANC-1 (line)]] | alt | 39.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.9) |
| [[RKO (line)]] | wt | 71.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 31.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -11.1) |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.8) |
| [[H4 (line)]] | wt | 74.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -10.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.3) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.6) |
| [[LoVo (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -8.8) |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM2B-DT]] | +0.64 | +0.69 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45A]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TET1]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[PIAS2]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[GPR146]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GYS1]] | +0.58 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[WNK3]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ZNF395]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CEP250]] | +0.55 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[EPHA3]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[KDM2B]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP2D7]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[MYO7B]] | -0.53 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[HNF4A]] | -0.47 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[CLIC5]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SLC5A1]] | -0.46 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[PROM1]] | -0.45 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[DTX2P1]] | -0.45 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[EPS8L3]] | -0.45 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[ABO]] | -0.44 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[CFAP161]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[XYLT1]] | -0.43 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[GCNT3]] | -0.43 | -0.51 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USH1C]] | B | USH1C activity lowers SMAD9's level | lines that do not express USH1C (34) vs lines expressing it (16) | 3.34× higher at baseline in the lines without USH1C | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[CLIC5]] | B | CLIC5 activity lowers SMAD9's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.67× higher at baseline in the lines without CLIC5 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SMAD9's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[GCNT3]] | B | GCNT3 activity lowers SMAD9's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.73× higher at baseline in the lines without GCNT3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[MYO7B]] | B | MYO7B activity lowers SMAD9's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.56× higher at baseline in the lines without MYO7B | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[GPR155]] | B | GPR155 activity raises SMAD9's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 4.66× lower at baseline in the lines without GPR155 | 0.055 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers SMAD9's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[FAM216A]] | B | FAM216A activity raises SMAD9's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 3.43× lower at baseline in the lines without FAM216A | 0.099 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[SAMD11]] | C | SAMD11 activity raises SMAD9's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 4.08× lower at baseline in the lines without SAMD11 | 0.024 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1; co-absent with the target |
| [[KCTD16]] | C | KCTD16 activity raises SMAD9's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 3.52× lower at baseline in the lines without KCTD16 | 0.041 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B]] | B | SMAD9 activity raises KDM2B's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without SMAD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[KDM2B-DT]] | B | SMAD9 activity raises KDM2B-DT's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without SMAD9 | 0.018 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[USH1C]] | B | SMAD9 activity lowers USH1C's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 5.71× higher at baseline in the lines without SMAD9 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[SLC5A1]] | B | SMAD9 activity lowers SLC5A1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 4.21× higher at baseline in the lines without SMAD9 | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[TBC1D9B]] | B | SMAD9 activity raises TBC1D9B's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without SMAD9 | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[NDUFB8]] | B | SMAD9 activity raises NDUFB8's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without SMAD9 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[CNTNAP1]] | B | SMAD9 activity raises CNTNAP1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.57× lower at baseline in the lines without SMAD9 | 0.051 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[HNF4A]] | B | SMAD9 activity lowers HNF4A's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 6.46× higher at baseline in the lines without SMAD9 | 0.058 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[FAM216A]] | B | SMAD9 activity raises FAM216A's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without SMAD9 | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[SYDE1]] | B | SMAD9 activity strengthens SYDE1's drug response | lines that do not express SMAD9 (6) vs lines expressing it (31) | the lines without SMAD9 respond 0.80× as strongly (z diff +2.02); strongest at Homoharringtonine 0.5 µM: 0.53x vs 0.32x (z diff +2.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2; target measured in part of the lines; artifact flags |
| [[EGLN1]] | B | SMAD9 activity raises EGLN1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without SMAD9 | 0.070 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[DTX2P1]] | B | SMAD9 activity lowers DTX2P1's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.61× higher at baseline in the lines without SMAD9 | 0.077 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.4, 29.8); signed map (-30.9, 31.9). **Vector** length 95.8, 26.8% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -2.3 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.2 | -7.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.7 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | -0.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -4.1 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -3.2 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.0 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.7 | -7.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | +1.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:36,844,831-36,920,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SMAD8, SMAD8/9; previously MADH6, MADH9 |
| Gene groups (HGNC) | SMAD family |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [O15198](https://www.uniprot.org/uniprotkb/O15198) (SMAD family member 9):

> Transcriptional modulator activated by BMP (bone morphogenetic proteins) type 1 receptor kinase. SMAD9 is a receptor-regulated SMAD (R-SMAD).

**Summary**, from NCBI Gene [4093](https://www.ncbi.nlm.nih.gov/gene/4093):

> The protein encoded by this gene is a member of the SMAD family, which transduces signals from TGF-beta family members. The encoded protein is activated by bone morphogenetic proteins and interacts with SMAD4. Two transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:6774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6774) · Entrez [4093](https://www.ncbi.nlm.nih.gov/gene/4093) · UniProt [O15198](https://www.uniprot.org/uniprotkb/O15198) · Ensembl [ENSG00000120693](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120693)

## Data

Gene col 4206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4206); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4206]; `tensor/DDL_lfc|DDL_z.npy` [4206]; `embed/gene_vectors.npy` [4206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4206 or target_col == 4206). Every well: [[SMAD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
