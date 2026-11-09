---
symbol: "TADA3"
type: "gene"
col: 10060
ensembl_id: "ENSG00000171148"
name: "transcriptional adaptor 3"
location: "3p25.3"
module: 109
arm: "+"
pooled_cpm: 25.95
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# TADA3

*transcriptional adaptor 3* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +8.0, q 7e-13, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 3.70×, HEC-1-A 2.95×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.49×, NCI-H460 3.47×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.18×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.421× (z -11.8, q 2e-29, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EGR2]] (+0.69, fdr 7e-06), [[ZDHHC4]] (+0.68, fdr 7e-06), [[EGR1]] (+0.67, fdr 7e-06); moves opposite to [[HSPA1B]] (-0.59, fdr 1e-05), [[HSPA1A]] (-0.54, fdr 2e-05), [[HSPE1]] (-0.53, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10060.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 3.70×, HEC-1-A 2.95×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.49×, NCI-H460 3.47×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 3.18×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.0 | 7e-13 | 37/42 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.9 | 7e-13 | 28/35 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.5 | 7e-06 | 22/41 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.3 | 0.12 | 0/48 | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.25× | +3.0 | 0.30 | 10/47 (A-172, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -11.8 | 2e-29 | 45/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -10.9 | 4e-25 | 38/47 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.453×** | -10.8 | 5e-25 | 43/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.485×** | -9.3 | 1e-18 | 41/48 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.556×** | -8.0 | 1e-13 | 37/47 (SW 900, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.561×** | -7.9 | 3e-13 | 38/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.575×** | -7.6 | 3e-12 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.408×** | -6.4 | 1e-08 | 29/42 (SNU-423, J82, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -5.7 | 6e-07 | 27/46 (NCI-H23, HCT15, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -5.6 | 1e-06 | 27/48 (C32, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.700×** | -4.9 | 6e-05 | 24/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.718×** | -4.5 | 3e-04 | 20/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -4.4 | 5e-04 | 22/47 (NCI-H23, SW 1271, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.798×** | -4.4 | 5e-04 | 25/47 (KATO III, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -4.3 | 7e-04 | 21/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -3.8 | 0.004 | 23/46 (RKO, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.793×** | -3.2 | 0.044 | 17/48 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.068 | 15/48 (A-427, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.4 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -10.7) |
| [[SW480 (line)]] | alt | 27.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.354× (z -10.5) |
| [[J82 (line)]] | alt | 19.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.246× (z -9.1) |
| [[A498 (line)]] | wt | 13.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.177× (z -12.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 16.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.210× (z -10.1) |
| [[A-427 (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 31.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.225× (z -9.0) |
| [[H4 (line)]] | wt | 29.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -10.8) |
| [[HOP62 (line)]] | alt | 42.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.7) |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -8.9) |
| [[KATO III (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0578× (z -22.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.2) |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.248× (z -9.4) |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.266× (z -8.9) |
| [[SW 1271 (line)]] | alt | 42.3 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0747× (z -8.5) |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0404× (z -14.8) |
| [[SW48 (line)]] | wt | 24.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0829× (z -10.4) |
| [[A-172 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EGR2]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ZDHHC4]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[EGR1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[DGUOK]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[EGR3]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ARPC4]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MCL1]] | +0.59 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ERCC1]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[KBTBD2]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[IER2]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GNL1]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZNF274]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA1B]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[HSPA1A]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HSPE1]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[GSEC]] | -0.53 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[HACD3]] | -0.51 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[WWP1]] | -0.51 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[FHIP2A]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[INTS10]] | -0.50 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[HINT1]] | -0.49 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[TXN]] | -0.48 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[NAPB]] | -0.47 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[C1orf216]] | -0.46 | -0.53 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.4, 0.4); signed map (5.3, 29.0). **Vector** length 91.3, 21.7% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.7 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | +1.5 | +2.8 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.4 | +0.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.9 | -10.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -7.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.0 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional adaptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,779,967-9,793,011 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20221, FLJ21329, ADA3, hADA3, NGG1; previously TADA3L |
| Gene groups (HGNC) | ATAC complex; SAGA complex |
| Reactome | 8 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75528](https://www.uniprot.org/uniprotkb/O75528) (Transcriptional adapter 3):

> Functions as a component of the PCAF complex. The PCAF complex is capable of efficiently acetylating histones in a nucleosomal context. The PCAF complex could be considered as the human version of the yeast SAGA complex. Also known as a coactivator for p53/TP53-dependent transcriptional activation. Component of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4.

**Summary**, from NCBI Gene [10474](https://www.ncbi.nlm.nih.gov/gene/10474):

> DNA-binding transcriptional activator proteins increase the rate of transcription by interacting with the transcriptional machinery bound to the basal promoter in conjunction with adaptor proteins, possibly by acetylation and destabilization of nucleosomes. The protein encoded by this gene is a transcriptional activator adaptor and a component of the histone acetyl transferase (HAT) coactivator complex which plays a crucial role in chromatin modulation and cell cycle progression. Along with the …

**Accessions** — [HGNC:19422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19422) · Entrez [10474](https://www.ncbi.nlm.nih.gov/gene/10474) · UniProt [O75528](https://www.uniprot.org/uniprotkb/O75528) · Ensembl [ENSG00000171148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171148)

## Data

Gene col 10060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10060); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10060]; `tensor/DDL_lfc|DDL_z.npy` [10060]; `embed/gene_vectors.npy` [10060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10060 or target_col == 10060). Every well: [[TADA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TADA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
