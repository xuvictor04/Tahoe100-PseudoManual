---
symbol: "ARC"
type: "gene"
col: 12620
ensembl_id: "ENSG00000198576"
name: "activity regulated cytoskeleton associated protein"
location: "8q24.3"
module: 109
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 31
n_dd_up: 45
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# ARC

*activity regulated cytoskeleton associated protein* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 142× (z +29.4, q 0e+00, up in 11 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 24.0× (z +26.7, q 0e+00, up in 21 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.358× (z -6.0, q 1e-06, down in 17 of 27 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[RMC-6236 (drug)]] 5 µM: 0.292× (z -3.8, q 0.024, down in 5 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR1]] (+0.67, fdr 7e-06), [[SYN1]] (+0.64, fdr 7e-06), [[EGR2]] (+0.63, fdr 8e-06); moves opposite to [[TRAPPC13]] (-0.55, fdr 3e-05), [[SPATA5L1]] (-0.52, fdr 7e-05), [[ASB7]] (-0.51, fdr 2e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K2]] → it (grade B ⚠); 8 go from it, the strongest it → [[IER3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **142×** | +29.4 | 0e+00 | 11/11 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **24.0×** | +26.7 | 0e+00 | 21/21 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **78.2×** | +24.9 | 0e+00 | 5/5 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **48.0×** | +21.2 | 0e+00 | 5/5 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **29.8×** | +20.1 | 0e+00 | 26/26 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **23.9×** | +18.8 | 0e+00 | 23/23 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **21.2×** | +17.4 | 0e+00 | 22/24 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **18.5×** | +17.3 | 0e+00 | 19/20 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **16.9×** | +16.8 | 0e+00 | 17/20 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **9.05×** | +13.1 | 3e-37 | 20/23 (SW480, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **4.70×** | +13.0 | 1e-36 | 24/26 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **6.82×** | +11.4 | 3e-28 | 20/25 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **6.77×** | +11.3 | 4e-28 | 10/13 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.81×** | +11.2 | 1e-27 | 9/18 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **5.59×** | +10.2 | 8e-23 | 21/27 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.54×** | +7.5 | 2e-12 | 18/26 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +4.8 | 4e-05 | 9/18 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.17×** | +4.6 | 1e-04 | 6/24 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.10×** | +4.4 | 3e-04 | 7/17 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.00×** | +4.1 | 9e-04 | 10/24 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.93×** | +3.6 | 0.007 | 3/13 (C32, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.358×** | -6.0 | 1e-06 | 17/27 (HT-29, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.292×** | -3.8 | 0.024 | 5/25 (HT-29, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.500×** | -3.8 | 0.024 | 6/25 (HT-29, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.588×** | -3.7 | 0.032 | 12/25 (SHP-77, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.613×** | -3.6 | 0.034 | 10/25 (SHP-77, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.373× | -3.1 | 0.20 | 6/24 (C32, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Perindopril (erbumine) (drug)]] 5 µM |  | 0.604× | -3.0 | 0.20 | 6/27 (CHP-212, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 20.7 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 33.1× (z +21.6) | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 372× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 40.6× (z +12.3) | — |
| [[C32 (line)]] | wt | 10.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 152× (z +15.5) | — |
| [[HT-29 (line)]] | alt | 11.6 | 2 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 5.87× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0363× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0372× (z -10.9) |
| [[SW480 (line)]] | alt | 2.80 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 105× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 32.0× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 2.88 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 94.8× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 14.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 17.4× (z +8.9) ⚠ toxic; transcription drop | [[Cobimetinib (drug)]] 5 µM 0.0479× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 2.42 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 40.4× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 2.17 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 96.3× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 | 2 | 0 | [[Auranofin (drug)]] 5 µM 153× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 1.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 125× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 2.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 45.3× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.0× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +11.6) | — |
| [[A-172 (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.689 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.635 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR1]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 | pathway: NGF-stimulated transcription; STRING 851 |
| [[SYN1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 | STRING 410 |
| [[EGR2]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 | pathway: NGF-stimulated transcription; STRING 697 |
| [[IER2]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[EGR3]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 | pathway: NGF-stimulated transcription; STRING 722 |
| [[CSRNP1]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NPTX2]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SOWAHC]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ERCC1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ASTL]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SPATA5L1]] | -0.52 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[ASB7]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[EIF4ENIF1]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DRAM2]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MFSD8]] | -0.51 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[SUPV3L1]] | -0.50 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[KLHDC10]] | -0.50 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[RNPC3]] | -0.49 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[ELMOD3]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[RWDD3]] | -0.48 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ZNF738]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K2]] | B | MAP2K2 activity raises ARC's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SCG3]] | B | SCG3 activity raises ARC's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 1.90× lower at baseline in the lines without SCG3 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[VGF]] | B | VGF activity raises ARC's level | lines that do not express VGF (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without VGF | 0.081 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3 |
| [[RASD1]] | B | RASD1 activity raises ARC's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without RASD1 | 0.083 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[MAP2K1]] | B | MAP2K1 activity raises ARC's level | compounds that target MAP2K1: 2 of 4 lower it (Binimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[NBEAP1]] | C | NBEAP1 activity raises ARC's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without NBEAP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IER3]] | B | ARC activity raises IER3's level | lines that do not express ARC (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without ARC | 0.018 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[FOS]] | B | ARC activity raises FOS's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.52× lower at baseline in the lines without ARC | 0.026 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[CD163L1]] | B | ARC activity raises CD163L1's level | lines that do not express ARC (19) vs lines expressing it (31) | 2.99× lower at baseline in the lines without ARC | 0.048 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[TRIB1]] | B | ARC activity raises TRIB1's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without ARC | 0.058 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[ASB7]] | B | ARC activity raises ASB7's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.16× lower at baseline in the lines without ARC | 0.059 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[MAP2K3]] | B | ARC activity raises MAP2K3's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.25× lower at baseline in the lines without ARC | 0.064 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[SH3GL2]] | B | ARC activity lowers SH3GL2's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.65× higher at baseline in the lines without ARC | 0.069 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[LIF]] | B | ARC activity raises LIF's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.26× lower at baseline in the lines without ARC | 0.086 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -0.7); signed map (6.7, 29.6). **Vector** length 61.8, 14.4% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.57 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.53 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +24.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +29.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +21.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +16.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | activity regulated cytoskeleton associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:142,611,049-142,614,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0278, Arg3.1 |
| Gene groups (HGNC) | Retrotransposon Gag derived ARC |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LC44](https://www.uniprot.org/uniprotkb/Q7LC44) (Activity-regulated cytoskeleton-associated protein):

> Master regulator of synaptic plasticity that self-assembles into virion-like capsids that encapsulate RNAs and mediate intercellular RNA transfer in the nervous system. ARC protein is released from neurons in extracellular vesicles that mediate the transfer of ARC mRNA into new target cells, where ARC mRNA can undergo activity-dependent translation. ARC capsids are endocytosed and are able to transfer ARC mRNA into the cytoplasm of neurons. Acts as a key regulator of synaptic plasticity: …

**Summary**, from NCBI Gene [23237](https://www.ncbi.nlm.nih.gov/gene/23237):

> Enables mRNA binding activity and structural molecule activity. Predicted to be involved in several processes, including long-term memory; positive regulation of AMPA receptor activity; and regulation of synaptic plasticity. Predicted to act upstream of or within anterior/posterior pattern specification and endoderm development. Located in cytoplasm and plasma membrane. Is active in virus-like capsid. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:648) · Entrez [23237](https://www.ncbi.nlm.nih.gov/gene/23237) · UniProt [Q7LC44](https://www.uniprot.org/uniprotkb/Q7LC44) · Ensembl [ENSG00000198576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198576)

## Data

Gene col 12620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12620); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12620]; `tensor/DDL_lfc|DDL_z.npy` [12620]; `embed/gene_vectors.npy` [12620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12620 or target_col == 12620). Every well: [[ARC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
