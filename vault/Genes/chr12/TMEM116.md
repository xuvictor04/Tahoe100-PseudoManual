---
symbol: "TMEM116"
type: "gene"
col: 12564
ensembl_id: "ENSG00000198270"
name: "transmembrane protein 116"
location: "12q24.13"
module: 72
arm: "+"
pooled_cpm: 12.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# TMEM116

*transmembrane protein 116* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +5.9, q 2e-06, up in 21 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.37× (z +4.7, q 4e-04, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.474× (z -11.1, q 5e-26, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH2]] (+0.53, fdr 1e-05), [[XNDC1N-ZNF705EP-ALG1L9P]] (+0.52, fdr 3e-05), [[TIMM21]] (+0.52, fdr 5e-05); moves opposite to [[MIEN1]] (-0.49, fdr 2e-04), [[POLR2L]] (-0.47, fdr 4e-04), [[GPX4]] (-0.45, fdr 1e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPDR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12564.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +5.9 | 2e-06 | 21/46 (SW480, HT-29, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.43×** | +5.2 | 7e-05 | 13/45 (A498, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +4.8 | 3e-04 | 20/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.7 | 4e-04 | 16/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.35×** | +4.5 | 9e-04 | 18/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.37×** | +4.4 | 9e-04 | 16/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +3.8 | 0.010 | 9/30 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 1.19× | +3.6 | 0.017 | 19/48 (HS-578T, HOP62, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.017 | 7/47 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.018 | 8/47 (LS 180, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.018 | 10/45 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.022 | 13/47 (SW48, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.023 | 7/48 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.074 | 8/46 (NCI-H1573, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.074 | 3/45 (SHP-77, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12564.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.474×** | -11.1 | 5e-26 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -10.5 | 3e-23 | 33/45 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.538×** | -9.3 | 4e-18 | 28/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.541×** | -8.8 | 2e-16 | 30/47 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -7.8 | 6e-13 | 31/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -5.9 | 5e-07 | 22/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -4.4 | 9e-04 | 17/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.772×** | -3.9 | 0.008 | 13/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.015 | 14/47 (CFPAC-1, J82, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.784×** | -3.6 | 0.015 | 15/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.015 | 14/47 (A-172, SW 1088, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.021 | 11/48 (NCI-H661, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.808×** | -3.2 | 0.062 | 13/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~83% of this change | **0.810×** | -3.2 | 0.064 | 14/40 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12564. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -13.5) |
| [[SW480 (line)]] | alt | 10.4 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.178× (z -13.1) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0794× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.282× (z -8.8) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -12.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 9.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0774× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 8.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.59 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0719× (z -11.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.286× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.208× (z -10.4) |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -10.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0654× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12564), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH2]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 | STRING 512 |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.52 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[TIMM21]] | +0.52 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[NUP153]] | +0.51 | +0.29 / +0.40 | both halves | 2e-04 |  |
| [[CUL1]] | +0.50 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[PSMA1]] | +0.49 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[RPTOR]] | +0.49 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[ANKRD23]] | +0.49 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[SUPT16H]] | +0.48 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[PSPH]] | +0.48 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CTPS2]] | +0.48 | +0.42 / +0.23 | both halves | 5e-04 |  |
| [[SUPV3L1]] | +0.48 | +0.28 / +0.46 | both halves | 3e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIEN1]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[POLR2L]] | -0.47 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[GPX4]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.45 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[ZFAND6]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[BMAL1]] | -0.43 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[TMEM50A]] | -0.43 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[S100A6]] | -0.42 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SNAP29]] | -0.42 | -0.26 / -0.33 | both halves | 3e-04 |  |
| [[AMN1]] | -0.42 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[WASL]] | -0.42 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[SLC25A4]] | -0.41 | -0.25 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPDR1]] | B | EPDR1 activity raises TMEM116's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without EPDR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.387). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.7, -35.2); signed map (-28.9, -48.7). **Vector** length 57.5, 7.91% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.3 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.9 | -8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 116 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:111,931,282-112,013,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90167 |
| Matched by | ensembl_id |

UniProt [Q8NCL8](https://www.uniprot.org/uniprotkb/Q8NCL8) carries no function annotation.

**Summary**, from NCBI Gene [89894](https://www.ncbi.nlm.nih.gov/gene/89894):

> Predicted to be involved in signal transduction. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25084) · Entrez [89894](https://www.ncbi.nlm.nih.gov/gene/89894) · UniProt [Q8NCL8](https://www.uniprot.org/uniprotkb/Q8NCL8) · Ensembl [ENSG00000198270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198270)

## Data

Gene col 12564: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12564); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12564, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12564]; `tensor/DDL_lfc|DDL_z.npy` [12564]; `embed/gene_vectors.npy` [12564]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12564 or target_col == 12564). Every well: [[TMEM116 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM116.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
