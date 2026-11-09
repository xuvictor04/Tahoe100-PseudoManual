---
symbol: "ANKRD23"
type: "gene"
col: 8638
ensembl_id: "ENSG00000163126"
name: "ankyrin repeat domain 23"
location: "2q11.2"
module: 72
arm: "+"
pooled_cpm: 16.46
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ANKRD23

*ankyrin repeat domain 23* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.56× (z +14.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.520× (z -10.9, q 6e-25, down in 29 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.632× (z -7.2, q 1e-10, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD39]] (+0.74, fdr 7e-06, ⚠ same locus), [[PSMC1]] (+0.68, fdr 7e-06), [[SLC38A6]] (+0.67, fdr 7e-06), [[BABAM1]] (+0.66, fdr 1e-05); moves opposite to [[LCOR]] (-0.55, fdr 1e-05), [[PFN1]] (-0.52, fdr 3e-05), [[DOP1A]] (-0.51, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MINDY4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.56×** | +14.7 | 0e+00 | 42/48 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.11×** | +12.4 | 1e-32 | 38/47 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.96×** | +10.4 | 3e-23 | 38/47 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +7.0 | 4e-10 | 32/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +6.6 | 4e-09 | 28/47 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.9 | 9e-05 | 14/28 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 1e-04 | 18/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 2e-04 | 12/47 (BT-474, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 14/48 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 4e-04 | 14/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 9e-04 | 11/48 (A-172, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.006 | 14/47 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.013 | 13/47 (A498, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.17× | +3.6 | 0.015 | 18/46 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.017 | 8/47 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.066 | 4/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.520×** | -10.9 | 6e-25 | 29/46 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.545×** | -10.1 | 2e-21 | 33/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.673×** | -9.3 | 2e-18 | 27/47 (NCI-H460, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -7.2 | 1e-10 | 25/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.685×** | -5.9 | 3e-07 | 20/47 (SW480, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -5.9 | 3e-07 | 23/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.699×** | -5.7 | 8e-07 | 22/44 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.705×** | -5.6 | 1e-06 | 21/47 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -5.5 | 3e-06 | 23/48 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.750×** | -4.8 | 9e-05 | 17/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -4.5 | 4e-04 | 20/44 (hTERT-HPNE, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.832×** | -3.1 | 0.095 | 18/46 (RKO, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.2 | 1 | 6 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.90× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.187× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.218× (z -13.0) |
| [[SW480 (line)]] | alt | 22.1 | 2 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.80× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.380× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.7 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.14× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HEC-1-A (line)]] | alt | 28.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +10.5) | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.205× (z -10.0) |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 2 | — | [[Bendamustine (drug)]] 5 µM 0.168× (z -9.3) |
| [[KATO III (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 19.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.88× (z +9.1) | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 2 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0751× (z -12.9) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 12.2 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0858× (z -9.0) |
| [[C32 (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.1) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -10.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -8.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[COLO 205 (line)]] | alt | 14.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.51× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 9.54 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.156× (z -9.0) |
| [[J82 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.306× (z -10.1) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -13.3) ⚠ toxic |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -11.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0705× (z -13.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -13.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD39]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 | same gene group; STRING 773; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PSMC1]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SLC38A6]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[EPS15L1]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[UFD1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[HIBCH]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ZFAND2A]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF771]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCOR]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[PFN1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[DOP1A]] | -0.51 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[TMEM14C]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MINDY4]] | B | MINDY4 activity raises ANKRD23's level | lines that do not express MINDY4 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without MINDY4 | 0.072 | ⚠ within organs, on part of the lines; also absent: MPP4, DPH6-DT, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, -8.9); signed map (-26.2, -25.8). **Vector** length 79.1, 14.9% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA Double Strand Break Response* (reactome, mean cos +0.50 to 12); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.50 to 13); *Cellular response to chemical stress* (reactome, mean cos +0.50 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.1 | +12.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.0 | +14.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +10.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.8 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | -0.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +4.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.4 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.9 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -2.9 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +0.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,824,526-96,857,934 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DARP, FLJ32449, MARP3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SG2](https://www.uniprot.org/uniprotkb/Q86SG2) (Ankyrin repeat domain-containing protein 23):

> May be involved in the energy metabolism. Could be a molecular link between myofibrillar stretch-induced signaling pathways and muscle gene expression.

**Summary**, from NCBI Gene [200539](https://www.ncbi.nlm.nih.gov/gene/200539):

> This gene is a member of the muscle ankyrin repeat protein (MARP) family and encodes a protein with four tandem ankyrin-like repeats. The protein is localized to the nucleus, functioning as a transcriptional regulator. Expression of this protein is induced during recovery following starvation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24470) · Entrez [200539](https://www.ncbi.nlm.nih.gov/gene/200539) · UniProt [Q86SG2](https://www.uniprot.org/uniprotkb/Q86SG2) · Ensembl [ENSG00000163126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163126)

## Data

Gene col 8638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8638); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8638]; `tensor/DDL_lfc|DDL_z.npy` [8638]; `embed/gene_vectors.npy` [8638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8638 or target_col == 8638). Every well: [[ANKRD23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
