---
symbol: "DCAF16"
type: "gene"
col: 8660
ensembl_id: "ENSG00000163257"
name: "DDB1 and CUL4 associated factor 16"
location: "4p15.31"
module: 20
arm: "+"
pooled_cpm: 34.16
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DCAF16

*DDB1 and CUL4 associated factor 16* — 4p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.43× (z +8.8, q 1e-15, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.588× (z -18.4, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF6]] (+0.68, fdr 7e-06), [[PABIR2]] (+0.65, fdr 7e-06), [[VMA21]] (+0.63, fdr 7e-06); moves opposite to [[SNRNP27]] (-0.68, fdr 1e-05), [[WASHC1]] (-0.66, fdr 1e-05), [[ZNF585A]] (-0.66, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +8.8 | 1e-15 | 36/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.39×** | +7.7 | 3e-12 | 25/41 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +7.2 | 1e-10 | 26/48 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +7.2 | 1e-10 | 25/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +6.9 | 8e-10 | 26/47 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 2e-08 | 23/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.26×** | +5.6 | 2e-06 | 22/45 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +5.5 | 3e-06 | 21/46 (NCI-H2030, HCT15, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +5.1 | 2e-05 | 21/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.25×** | +5.1 | 2e-05 | 20/45 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +4.2 | 0.001 | 16/47 (SW480, SW 900, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +4.1 | 0.002 | 14/47 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.12× | +3.9 | 0.004 | 4/48 (NCI-H1792, C-33 A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.9 | 0.005 | 16/48 (HEC-1-A, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 11/47 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.056 | 1/48 (SHP-77) | top dose only | position effect removed |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.070 | 3/47 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.09× | +2.9 | 0.094 | 4/48 (HS-578T, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.588×** | -18.4 | 0e+00 | 40/48 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -12.0 | 1e-30 | 38/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.619×** | -11.3 | 3e-27 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -9.6 | 7e-20 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -8.6 | 7e-16 | 27/48 (NCI-H2030, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -8.1 | 6e-14 | 27/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.637×** | -5.8 | 6e-07 | 23/42 (J82, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.801×** | -5.4 | 4e-06 | 19/47 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.788×** | -5.4 | 4e-06 | 19/47 (A-427, BT-474, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.813×** | -4.8 | 9e-05 | 17/48 (SK-MEL-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.839× | -4.3 | 9e-04 | 20/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.886× | -4.2 | 0.001 | 15/48 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.725×** | -4.1 | 0.002 | 10/48 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.891× | -4.0 | 0.002 | 14/48 (SW480, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.849× | -4.0 | 0.002 | 13/48 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.884× | -3.0 | 0.087 | 8/48 (SW480, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -11.2) |
| [[A-427 (line)]] | wt | 53.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -21.3) |
| [[C-33 A (line)]] | alt | 77.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -14.2) |
| [[LoVo (line)]] | wt | 44.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.0) |
| [[SW480 (line)]] | alt | 51.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -18.6) |
| [[HCT15 (line)]] | alt | 56.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -14.6) |
| [[J82 (line)]] | alt | 46.3 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0386× (z -19.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.0) |
| [[RKO (line)]] | wt | 59.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0684× (z -12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.391× (z -12.0) |
| [[A498 (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.9) |
| [[A549 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 39.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -8.7) |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 34.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.388× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0704× (z -11.4) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.6) |
| [[SW48 (line)]] | wt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.2) |
| [[A-172 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF6]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[PABIR2]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[VMA21]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CDK2]] | +0.63 | +0.74 / +0.39 | both halves | 6e-05 |  |
| [[CHID1]] | +0.62 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[EEF1AKMT2]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.61 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[FBXW2]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 | pathway: Neddylation |
| [[POFUT1]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[QSOX2]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TFDP1]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SPATA5]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP27]] | -0.68 | -0.76 / -0.50 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.66 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.66 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[CCDC174]] | -0.63 | -0.72 / -0.44 | both halves | 3e-05 |  |
| [[RSRC2]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[AMZ2P1-1]] | -0.60 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[CIRBP]] | -0.59 | -0.70 / -0.39 | both halves | 5e-05 |  |
| [[ZC3H6]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[RAD52]] | -0.58 | -0.69 / -0.32 | both halves | 2e-04 |  |
| [[SNW1]] | -0.58 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[TCEANC]] | -0.58 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[SNHG32]] | -0.58 | -0.68 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DCAF16's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises DCAF16's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.7, -27.5); signed map (-27.3, -35.2). **Vector** length 103, 23.0% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +6.0 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.7 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +6.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | +4.0 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.3 | +3.9 |
|  | [[Benztropine (mesylate) (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -18.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.31 — chr4:17,800,655-17,810,758 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20280; previously C4orf30 |
| Gene groups (HGNC) | DDB1 and CUL4 associated factors |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXF7](https://www.uniprot.org/uniprotkb/Q9NXF7) (DDB1- and CUL4-associated factor 16):

> Functions as a substrate recognition component for CUL4-DDB1 E3 ubiquitin-protein ligase complex, which mediates ubiquitination and proteasome-dependent degradation of nuclear proteins.

**Summary**, from NCBI Gene [54876](https://www.ncbi.nlm.nih.gov/gene/54876):

> Predicted to be involved in epigenetic regulation of gene expression. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25987) · Entrez [54876](https://www.ncbi.nlm.nih.gov/gene/54876) · UniProt [Q9NXF7](https://www.uniprot.org/uniprotkb/Q9NXF7) · Ensembl [ENSG00000163257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163257)

## Data

Gene col 8660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8660); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8660]; `tensor/DDL_lfc|DDL_z.npy` [8660]; `embed/gene_vectors.npy` [8660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8660 or target_col == 8660). Every well: [[DCAF16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
