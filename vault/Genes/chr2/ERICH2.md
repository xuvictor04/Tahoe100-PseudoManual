---
symbol: "ERICH2"
type: "gene"
col: 12853
ensembl_id: "ENSG00000204334"
name: "glutamate rich 2"
location: "2q31.1"
module: 63
arm: "+"
pooled_cpm: 5.47
n_lines_expressing: 39
n_dd_up: 20
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ERICH2

*glutamate rich 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +6.4, q 7e-08, up in 22 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.411× (z -8.7, q 2e-15, down in 23 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLGN]] (+0.67, fdr 1e-05), [[ADM2]] (+0.65, fdr 7e-06), [[ULBP1]] (+0.65, fdr 1e-05); moves opposite to [[ELAC2]] (-0.54, fdr 1e-05), [[MTAP]] (-0.52, fdr 2e-05), [[SPATA5]] (-0.50, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NIBAN1]] → it (grade B ⚠); 2 go from it, the strongest it → [[DDIT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.4 | 7e-08 | 22/36 (HT-29, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +6.3 | 8e-08 | 18/32 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.2 | 1e-07 | 15/30 (A-427, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.1 | 1e-07 | 12/21 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **1.54×** | +6.0 | 2e-07 | 16/36 (HEC-1-A, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.7 | 1e-06 | 2/9 (HOP62, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.1 | 3e-05 | 9/20 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +4.7 | 2e-04 | 15/35 (A-172, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.4 | 8e-04 | 11/21 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +4.2 | 0.002 | 7/36 (A498, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 9/33 (LoVo, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.006 | 7/36 (SW480, A-427, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 8/36 (PANC-1, A-427, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.008 | 10/35 (LoVo, C-33 A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.027 | 9/33 (SW480, C-33 A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.082 | 5/29 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.082 | 8/29 (LoVo, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.082 | 2/32 (LoVo, PANC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.411×** | -8.7 | 2e-15 | 23/33 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -8.4 | 2e-14 | 24/36 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.465×** | -7.5 | 1e-11 | 22/35 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.492×** | -6.9 | 6e-10 | 19/33 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -6.2 | 6e-08 | 18/27 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.314×** | -5.9 | 3e-07 | 20/28 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.326×** | -5.7 | 8e-07 | 16/33 (SW480, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.552×** | -5.5 | 3e-06 | 17/33 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -4.7 | 2e-04 | 16/35 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.622×** | -4.6 | 2e-04 | 14/32 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -4.4 | 5e-04 | 11/32 (HT-29, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -3.7 | 0.008 | 14/33 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -3.7 | 0.008 | 12/29 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.023 | 10/35 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 14.6 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0720× (z -13.9) |
| [[KATO III (line)]] | alt | 14.9 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0434× (z -15.9) |
| [[SW480 (line)]] | alt | 14.0 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.250× (z -10.0) |
| [[A-172 (line)]] | wt | 12.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.182× (z -8.5) |
| [[H4 (line)]] | wt | 12.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0671× (z -9.9) |
| [[HOP62 (line)]] | alt | 4.53 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0546× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.128× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 4.48 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0931× (z -8.9) |
| [[SW48 (line)]] | wt | 19.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0922× (z -9.2) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.978 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLGN]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[ADM2]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ULBP1]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[GARS1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[BEX2]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SYTL1]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TUBE1]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ASNS]] | +0.62 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[SARS1]] | +0.61 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[PCK2]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DMGDH]] | +0.60 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[EIF2S2]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELAC2]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MTAP]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SPATA5]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RBM12]] | -0.50 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[EIPR1]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[LAS1L]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[BANF1]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GRWD1]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIBAN1]] | B | NIBAN1 activity raises ERICH2's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without NIBAN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[ESRP1]] | B | ESRP1 activity raises ERICH2's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without ESRP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDIT3]] | B | ERICH2 activity raises DDIT3's level | lines that do not express ERICH2 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without ERICH2 | 0.070 | ⚠ within organs, on part of the lines; also absent: ERICH2-DT, DMBX1, GAD1 |
| [[ZFAND1]] | B | ERICH2 activity strengthens ZFAND1's drug response | lines that do not express ERICH2 (11) vs lines expressing it (37) | the lines without ERICH2 respond 0.99× as strongly (z diff +0.05); rises at some drug-doses, falls at others (57% from rises): Artesunate 5 µM: 1.11x vs 1.33x (z diff +2.0); Digitoxin 0.5 µM: 0.85x vs 0.70x (z diff +1.6); Ponatinib 5 µM: 1.30x vs 1.50x (z diff +1.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: ERICH2-DT, DMBX1, GAD1; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.6, 49.0); signed map (-11.5, 23.4). **Vector** length 61.1, 12.2% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.53 to 16); *Response of EIF2AK1 (HRI) to heme deficiency* (reactome, mean cos +0.58 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -8.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | glutamate rich 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:170,766,878-170,798,977 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A1L162](https://www.uniprot.org/uniprotkb/A1L162) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44395) · Entrez [285141](https://www.ncbi.nlm.nih.gov/gene/285141) · UniProt [A1L162](https://www.uniprot.org/uniprotkb/A1L162) · Ensembl [ENSG00000204334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204334)

## Data

Gene col 12853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12853); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12853]; `tensor/DDL_lfc|DDL_z.npy` [12853]; `embed/gene_vectors.npy` [12853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12853 or target_col == 12853). Every well: [[ERICH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERICH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
