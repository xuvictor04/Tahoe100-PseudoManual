---
symbol: "MMUT"
type: "gene"
col: 7062
ensembl_id: "ENSG00000146085"
name: "methylmalonyl-CoA mutase"
location: "6p12.3"
module: 41
arm: "+"
pooled_cpm: 35.0
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 4
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MMUT

*methylmalonyl-CoA mutase* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.12× (z +7.7, q 6e-12, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.526× (z -12.6, q 1e-33, down in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.537× (z -12.2, q 9e-32, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH6A1]] (+0.75, fdr 7e-06), [[TRIM23]] (+0.70, fdr 7e-06), [[ARHGAP1]] (+0.69, fdr 7e-06); moves opposite to [[TANGO6]] (-0.60, fdr 1e-05), [[GALNT14]] (-0.58, fdr 1e-05), [[NUTM2B-AS1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +7.7 | 6e-12 | 31/48 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +7.4 | 4e-11 | 26/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +7.0 | 5e-10 | 26/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +6.8 | 2e-09 | 24/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -12.6 | 1e-33 | 41/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -12.2 | 9e-32 | 37/48 (H4, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -10.6 | 4e-24 | 37/48 (SHP-77, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.400×** | -9.4 | 8e-19 | 36/44 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.636×** | -8.9 | 8e-17 | 36/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.622×** | -8.8 | 1e-16 | 33/48 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.741×** | -8.3 | 9e-15 | 34/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -7.5 | 4e-12 | 34/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[EX229 (drug)]] 5 µM |  | **0.485×** | -7.4 | 6e-12 | 35/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -7.3 | 1e-11 | 31/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.704×** | -6.9 | 3e-10 | 32/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.719×** | -6.4 | 5e-09 | 25/44 (C32, H4, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.534×** | -6.4 | 5e-09 | 28/48 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.555×** | -6.1 | 6e-08 | 29/48 (HT-29, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.719×** | -6.0 | 8e-08 | 21/39 (SK-MEL-2, Panc 03.27, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -5.4 | 2e-06 | 24/48 (HOP62, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.610×** | -5.1 | 1e-05 | 25/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.782×** | -4.8 | 4e-05 | 24/48 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.8 | 6e-05 | 16/47 (SNU-1, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -4.7 | 6e-05 | 21/48 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 61.2 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.328× (z -10.2) |
| [[H4 (line)]] | wt | 56.4 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.165× (z -11.1) |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -11.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 66.3 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.122× (z -9.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 53.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.210× (z -12.9) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.269× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.390× (z -9.1) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.391× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 46.0 | 0 | 2 | — | [[vincristine (drug)]] 5 µM 0.0750× (z -10.4) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.2) |
| [[A498 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 24.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -10.5) |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0835× (z -10.4) |
| [[C32 (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0794× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HEC-1-A (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[HOP62 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.429× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0595× (z -14.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.314× (z -10.8) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 52.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.413× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 26.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.402× (z -9.0) |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH6A1]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 | STRING 442 |
| [[TRIM23]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ARHGAP1]] | +0.69 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[KLHL28]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SENP2]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ERCC5]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[DERL2]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZNF451]] | +0.65 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[FBXO8]] | +0.65 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PPIL4]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TANGO6]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[GALNT14]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[NUTM2B-AS1]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[CUEDC1]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G3]] | -0.58 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[MTHFD2L]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[TTC39C]] | -0.57 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TUSC3]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TULP4]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CLPB]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[PRKCE]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PVR]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MMUT's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KANK1]] | B | KANK1 activity lowers MMUT's level | lines that do not express KANK1 (12) vs lines expressing it (38) | 1.42× higher at baseline in the lines without KANK1 | 0.058 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.3, -34.2); signed map (-13.1, 2.8). **Vector** length 121, 32.8% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi traffic* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.0 | -12.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.6 | -12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.9 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -8.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | methylmalonyl-CoA mutase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:49,430,360-49,463,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCM; previously MUT |
| Reactome | 11 pathways, smallest: Propionyl-CoA catabolism; Cobalamin (Cbl) metabolism; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P22033](https://www.uniprot.org/uniprotkb/P22033) (Methylmalonyl-CoA mutase, mitochondrial):

> Catalyzes the reversible isomerization of methylmalonyl-CoA (MMCoA) (generated from branched-chain amino acid metabolism and degradation of dietary odd chain fatty acids and cholesterol) to succinyl-CoA (3-carboxypropionyl-CoA), a key intermediate of the tricarboxylic acid cycle.

**Summary**, from NCBI Gene [4594](https://www.ncbi.nlm.nih.gov/gene/4594):

> This gene encodes the mitochondrial enzyme methylmalonyl Coenzyme A mutase. In humans, the product of this gene is a vitamin B12-dependent enzyme which catalyzes the isomerization of methylmalonyl-CoA to succinyl-CoA, while in other species this enzyme may have different functions. Mutations in this gene may lead to various types of methylmalonic aciduria. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7526) · Entrez [4594](https://www.ncbi.nlm.nih.gov/gene/4594) · UniProt [P22033](https://www.uniprot.org/uniprotkb/P22033) · Ensembl [ENSG00000146085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146085)

## Data

Gene col 7062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7062); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7062]; `tensor/DDL_lfc|DDL_z.npy` [7062]; `embed/gene_vectors.npy` [7062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7062 or target_col == 7062). Every well: [[MMUT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMUT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
