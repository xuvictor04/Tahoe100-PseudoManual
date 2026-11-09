---
symbol: "UBE2D4"
type: "gene"
col: 1238
ensembl_id: "ENSG00000078967"
name: "ubiquitin conjugating enzyme E2 D4"
location: "7p13"
module: 1
arm: "+"
pooled_cpm: 11.83
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# UBE2D4

*ubiquitin conjugating enzyme E2 D4* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.02× (z +11.2, q 3e-26, up in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +6.1, q 1e-07, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.354× (z -16.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEMT]] (+0.59, fdr 1e-05), [[RIOX2]] (+0.59, fdr 1e-05), [[BOP1]] (+0.57, fdr 1e-05); moves opposite to [[ARID4A]] (-0.53, fdr 3e-05), [[ANKRD42]] (-0.49, fdr 9e-05), [[GCC2]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TARBP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +11.2 | 3e-26 | 25/35 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +9.5 | 4e-19 | 10/24 (HEC-1-A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +9.1 | 2e-17 | 13/19 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.1 | 1e-10 | 5/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.1 | 1e-07 | 21/47 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +5.0 | 4e-05 | 18/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.002 | 11/41 (NCI-H23, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.007 | 13/47 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.8 | 0.011 | 18/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +3.5 | 0.025 | 6/47 (LoVo, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +3.4 | 0.037 | 10/48 (HOP62, AsPC-1, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.354×** | -16.6 | 0e+00 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.471×** | -12.0 | 6e-31 | 36/46 (PANC-1, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -11.5 | 4e-28 | 31/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -10.2 | 2e-22 | 34/47 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.684×** | -8.6 | 1e-15 | 26/46 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.627×** | -7.5 | 8e-12 | 25/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -6.5 | 6e-09 | 22/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -5.4 | 5e-06 | 17/44 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.740×** | -4.8 | 1e-04 | 17/46 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.777×** | -4.0 | 0.003 | 12/47 (A-427, A-172, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.785×** | -3.6 | 0.018 | 15/42 (C-33 A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.789×** | -3.5 | 0.022 | 20/47 (SK-MEL-2, SNU-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.810×** | -3.4 | 0.031 | 15/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.031 | 12/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.863× | -3.3 | 0.031 | 10/48 (COLO 205, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.061 | 13/46 (A498, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0537× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.4) |
| [[SW480 (line)]] | alt | 12.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.163× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -11.8) |
| [[LoVo (line)]] | wt | 16.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.8) |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.175× (z -9.0) |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.7) |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 7.48 | 0 | 2 | — | [[Fenofibrate (drug)]] 5 µM 0.138× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -9.4) |
| [[RKO (line)]] | wt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.0771× (z -8.6) |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0849× (z -11.5) |
| [[A-172 (line)]] | wt | 6.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -8.5) |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0468× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 18.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -9.7) |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.1) |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0822× (z -8.8) |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEMT]] | +0.59 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[RIOX2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[BOP1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DCAF17]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[FYCO1]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[COPG2]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[PDCL3]] | +0.55 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[POGK]] | +0.54 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[FXN]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ATIC]] | +0.54 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[DCAF1]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[AIMP2]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4A]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ANKRD42]] | -0.49 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[GCC2]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DLEU2]] | -0.49 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[AAMDC]] | -0.49 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[ZNF345]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.48 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[POLN]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZNHIT1]] | -0.47 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[UPF2]] | -0.46 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[CFAP53]] | -0.46 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises UBE2D4's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without GNAZ | 0.013 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises UBE2D4's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without ANK2 | 0.029 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TARBP1]] | C | UBE2D4's natural level strengthens TARBP1's drug response | UBE2D4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.34; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.2, -37.8); signed map (-1.1, -40.5). **Vector** length 61.9, 9.18% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -16.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -11.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -12.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 D4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:43,926,436-43,956,136 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HBUCE1 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2X8](https://www.uniprot.org/uniprotkb/Q9Y2X8) (Ubiquitin-conjugating enzyme E2 D4):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro able to promote polyubiquitination using all 7 ubiquitin Lys residues, but may prefer 'Lys-11' and 'Lys-48'-linked polyubiquitination.

**Summary**, from NCBI Gene [51619](https://www.ncbi.nlm.nih.gov/gene/51619):

> Enables ubiquitin conjugating enzyme activity. Involved in protein polyubiquitination. Acts upstream of or within protein ubiquitination. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21647) · Entrez [51619](https://www.ncbi.nlm.nih.gov/gene/51619) · UniProt [Q9Y2X8](https://www.uniprot.org/uniprotkb/Q9Y2X8) · Ensembl [ENSG00000078967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078967)

## Data

Gene col 1238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1238); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1238]; `tensor/DDL_lfc|DDL_z.npy` [1238]; `embed/gene_vectors.npy` [1238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1238 or target_col == 1238). Every well: [[UBE2D4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2D4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
