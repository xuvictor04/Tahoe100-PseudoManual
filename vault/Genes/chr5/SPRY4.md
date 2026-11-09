---
symbol: "SPRY4"
type: "gene"
col: 11935
ensembl_id: "ENSG00000187678"
name: "sprouty RTK signaling antagonist 4"
location: "5q31.3"
module: 92
arm: "+"
pooled_cpm: 57.81
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 50
n_dd_up_clean: 5
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SPRY4

*sprouty RTK signaling antagonist 4* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.81× (z +7.5, q 3e-11, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.0967× (z -27.9, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHC2]] (+0.84, fdr 7e-06), [[SPRY4-AS1]] (+0.83, fdr 7e-06, ⚠ same locus), [[SPRED2]] (+0.80, fdr 7e-06), [[SPRY2]] (+0.79, fdr 7e-06); moves opposite to [[KIF13A]] (-0.58, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OSBPL10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +7.5 | 3e-11 | 28/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +5.9 | 1e-06 | 27/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 1e-05 | 27/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.49×** | +5.3 | 2e-05 | 25/47 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +5.2 | 3e-05 | 26/48 (A-172, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +3.8 | 0.017 | 24/48 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +3.5 | 0.045 | 18/49 (NCI-H2347, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 7 with an alert ⚠; shown: the 15 strongest. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.0967×** | -27.9 | 0e+00 | 48/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.114×** | -27.2 | 0e+00 | 47/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.199×** | -26.2 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.149×** | -24.8 | 0e+00 | 47/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.163×** | -22.7 | 0e+00 | 46/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.187×** | -20.8 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.223×** | -19.5 | 0e+00 | 46/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.349×** | -19.2 | 0e+00 | 46/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.211×** | -18.7 | 0e+00 | 47/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.340×** | -17.0 | 0e+00 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.485×** | -13.0 | 1e-36 | 44/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.372×** | -12.2 | 3e-32 | 43/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.434×** | -10.8 | 1e-25 | 41/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.478×** | -8.9 | 3e-17 | 38/47 (C32, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.127×** | -8.7 | 1e-16 | 45/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 229 | 0 | 29 (8 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.153× (z -56.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0125× (z -35.3) |
| [[HOP62 (line)]] | alt | 128 | 0 | 18 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0245× (z -20.9) |
| [[RKO (line)]] | wt | 234 | 0 | 18 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0219× (z -25.8) |
| [[SNU-1 (line)]] | wt | 197 | 0 | 17 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0536× (z -20.1) |
| [[AsPC-1 (line)]] | alt | 132 | 0 | 16 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0498× (z -19.1) |
| [[C32 (line)]] | wt | 92.4 | 0 | 16 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0450× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 32.3 | 2 (1 ⚠) | 14 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.21× (z +8.7) | [[Cobimetinib (drug)]] 5 µM 0.0751× (z -19.3) |
| [[NCI-H2347 (line)]] | alt | 58.7 | 0 | 15 (2 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.142× (z -19.4) |
| [[SK-MEL-2 (line)]] | alt | 93.5 | 0 | 15 (2 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.0997× (z -21.9) |
| [[NCI-H23 (line)]] | alt | 57.5 | 0 | 14 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.0700× (z -23.5) |
| [[SW480 (line)]] | alt | 69.2 | 0 | 14 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.103× (z -28.1) |
| [[CFPAC-1 (line)]] | alt | 47.0 | 1 (1 ⚠) | 12 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.1000× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 67.0 | 2 (1 ⚠) | 11 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.93× (z +10.0) | [[Trametinib (drug)]] 0.5 µM 0.119× (z -16.7) |
| [[Hs 766T (line)]] | wt | 68.4 | 0 | 13 | — | [[Trametinib (drug)]] 0.5 µM 0.0788× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 12 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.181× (z -13.8) |
| [[PANC-1 (line)]] | alt | 83.3 | 0 | 12 | — | [[Trametinib (drug)]] 5 µM 0.0637× (z -15.9) |
| [[J82 (line)]] | alt | 19.7 | 0 | 10 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0750× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 10 | — | [[Trametinib (drug)]] 0.5 µM 0.191× (z -15.6) |
| [[SHP-77 (line)]] | alt | 27.0 | 0 | 10 | — | [[Binimetinib (drug)]] 0.5 µM 0.0911× (z -15.2) |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 9 | — | [[Trametinib (drug)]] 5 µM 0.0368× (z -14.1) |
| [[NCI-H2030 (line)]] | alt | 35.7 | 0 | 9 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.546× (z -16.8) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.118× (z -16.2) |
| [[SW1417 (line)]] | alt | 85.0 | 0 | 9 | — | [[Trametinib (drug)]] 0.5 µM 0.187× (z -16.4) |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 8 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0827× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 0 | 8 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0825× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 1 (1 ⚠) | 7 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Trametinib (drug)]] 0.5 µM 0.153× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 8 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.406× (z -16.5) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.103× (z -12.2) |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 7 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.117× (z -10.7) |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 7 | — | [[Trametinib (drug)]] 5 µM 0.110× (z -12.6) |
| [[A498 (line)]] | wt | 20.1 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.22× (z +11.2) | [[Cobimetinib (drug)]] 5 µM 0.162× (z -12.3) |
| [[AN3 CA (line)]] | alt | 149 | 0 | 6 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0993× (z -12.2) |
| [[KATO III (line)]] | alt | 20.8 | 0 | 6 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.156× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 51.9 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.0718× (z -14.3) |
| [[SNU-423 (line)]] | alt | 22.0 | 0 | 6 | — | [[Trametinib (drug)]] 0.5 µM 0.141× (z -11.8) |
| [[A549 (line)]] | wt | 20.0 | 0 | 5 | — | [[Trametinib (drug)]] 0.5 µM 0.100× (z -16.9) |
| [[H4 (line)]] | wt | 23.8 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.0330× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 5 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0441× (z -14.0) |
| [[LoVo (line)]] | wt | 23.0 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.155× (z -13.9) |
| [[A-172 (line)]] | wt | 28.0 | 0 | 4 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0499× (z -18.1) |
| [[A-427 (line)]] | wt | 25.7 | 0 | 4 | — | [[Trametinib (drug)]] 0.5 µM 0.217× (z -14.1) |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.0628× (z -12.0) |
| [[SW 1271 (line)]] | alt | 93.5 | 0 | 4 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0328× (z -12.6) |
| [[CHP-212 (line)]] | wt | 40.8 | 0 | 3 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.0312× (z -10.9) |
| [[HT-29 (line)]] | alt | 40.8 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.115× (z -11.5) |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0735× (z -9.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.202× (z -8.7) |
| [[SW48 (line)]] | wt | 30.7 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.0900× (z -9.1) |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2]] | +0.84 | +0.86 / +0.88 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.83 | +0.82 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SPRED2]] | +0.80 | +0.80 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 709 |
| [[SPRY2]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 | same gene group; STRING 625 |
| [[DUSP6]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | STRING 752 |
| [[ITGB5]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SPRED1]] | +0.77 | +0.74 / +0.79 | both halves | 7e-06 | STRING 550 |
| [[ETV4]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 638 |
| [[LINC01844]] | +0.75 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[EGR3]] | +0.75 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.74 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.73 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[NPAS2]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13A]] | -0.58 | -0.46 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL10]] | B | OSBPL10 activity lowers SPRY4's level | lines that do not express OSBPL10 (5) vs lines expressing it (45) | 2.62× higher at baseline in the lines without OSBPL10 | 0.073 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 6.5); signed map (8.3, 47.3). **Vector** length 153, 54.2% of its response variance represented; |z| ≥ 3 in 1,914 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.58 to 7); *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.55 to 5); *MAPK family signaling cascades* (reactome, mean cos +0.64 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +5.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.1 | +1.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.8 | +2.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -15.2 | -27.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -15.1 | -26.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -14.0 | -20.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -13.5 | -24.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -13.4 | -27.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -13.0 | -22.7 |

## What is on record

|  |  |
|---|---|
| Name | sprouty RTK signaling antagonist 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:142,310,427-142,326,455 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sprouty RTK signaling antagonist family |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C004](https://www.uniprot.org/uniprotkb/Q9C004) (Protein sprouty homolog 4):

> Suppresses the insulin receptor and EGFR-transduced MAPK signaling pathway, but does not inhibit MAPK activation by a constitutively active mutant Ras. Probably impairs the formation of GTP-Ras. Inhibits Ras-independent, but not Ras-dependent, activation of RAF1. Represses integrin-mediated cell spreading via inhibition of TESK1-mediated phosphorylation of cofilin.

**Summary**, from NCBI Gene [81848](https://www.ncbi.nlm.nih.gov/gene/81848):

> This gene encodes a member of a family of cysteine- and proline-rich proteins. The encoded protein is an inhibitor of the receptor-transduced mitogen-activated protein kinase (MAPK) signaling pathway. Activity of this protein impairs the formation of active GTP-RAS. Nucleotide variation in this gene has been associated with hypogonadotropic hypogonadism 17 with or without anosmia. Alternative splicing results in a multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:15533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15533) · Entrez [81848](https://www.ncbi.nlm.nih.gov/gene/81848) · UniProt [Q9C004](https://www.uniprot.org/uniprotkb/Q9C004) · Ensembl [ENSG00000187678](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187678)

## Data

Gene col 11935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11935); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11935]; `tensor/DDL_lfc|DDL_z.npy` [11935]; `embed/gene_vectors.npy` [11935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11935 or target_col == 11935). Every well: [[SPRY4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRY4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
