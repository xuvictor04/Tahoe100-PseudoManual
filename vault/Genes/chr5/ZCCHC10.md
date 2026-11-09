---
symbol: "ZCCHC10"
type: "gene"
col: 7888
ensembl_id: "ENSG00000155329"
name: "zinc finger CCHC-type containing 10"
location: "5q31.1"
module: 114
arm: "+"
pooled_cpm: 33.59
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZCCHC10

*zinc finger CCHC-type containing 10* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.16× (z +15.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.607× (z -7.8, q 2e-12, down in 28 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.753× (z -5.6, q 4e-06, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3HC1]] (+0.75, fdr 7e-06), [[MTG2]] (+0.71, fdr 7e-06), [[RBM5]] (+0.71, fdr 1e-05); moves opposite to [[CORO1C]] (-0.68, fdr 7e-06), [[PABIR2]] (-0.65, fdr 1e-05), [[TTLL12]] (-0.63, fdr 3e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +15.2 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +15.0 | 0e+00 | 33/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +13.3 | 3e-38 | 43/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +12.3 | 1e-32 | 43/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +11.0 | 3e-26 | 43/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.7 | 3e-20 | 36/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +9.4 | 7e-19 | 40/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +8.9 | 4e-17 | 42/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +8.3 | 7e-15 | 41/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +7.5 | 4e-12 | 31/48 (LoVo, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.0 | 1e-10 | 30/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.0 | 1e-10 | 32/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +6.7 | 8e-10 | 30/48 (CFPAC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 3e-06 | 24/48 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 4e-05 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.002 | 19/48 (SNU-423, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.004 | 18/47 (NCI-H460, SW1417, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7888.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.607×** | -7.8 | 2e-12 | 28/47 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -7.3 | 8e-11 | 23/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.753×** | -5.6 | 4e-06 | 22/48 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.772×** | -5.1 | 4e-05 | 23/48 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.763×** | -4.9 | 1e-04 | 21/43 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.802×** | -4.4 | 0.001 | 15/48 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.812×** | -4.1 | 0.003 | 16/48 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | 0.880× | -3.6 | 0.026 | 10/48 (A-427, SW 1271, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.4 | 0.036 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.732×** | -3.2 | 0.073 | 8/48 (SW48, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 37.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.9) | — |
| [[NCI-H460 (line)]] | wt | 41.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.0) | — |
| [[LoVo (line)]] | wt | 31.8 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.34× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +11.4) | — |
| [[A-172 (line)]] | wt | 32.4 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.92× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 40.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.456× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0874× (z -21.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 41.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.219× (z -10.3) |
| [[HOP62 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.143× (z -9.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 38.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[RKO (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.5) | — |
| [[SW48 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HC1]] | +0.75 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[MTG2]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RBM5]] | +0.71 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[FDX2]] | +0.70 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[DOHH]] | +0.70 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SETDB1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RBX1]] | +0.69 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TEFM]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.69 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[GTF2IRD2B]] | +0.68 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[COIL]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | -0.68 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[PABIR2]] | -0.65 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TTLL12]] | -0.63 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TMED7]] | -0.63 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.62 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PDHA1]] | -0.61 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ITGB1]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[APEH]] | -0.61 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[RPL3]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.60 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[AGO1]] | -0.60 | -0.37 / -0.60 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZCCHC10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.7, 7.3); signed map (-3.3, -9.2). **Vector** length 93.5, 22.2% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.7 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.9 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +15.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +7.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.0 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,996,985-133,026,604 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20094 |
| Gene groups (HGNC) | Zinc fingers CCHC-type |
| Matched by | ensembl_id |

UniProt [Q8TBK6](https://www.uniprot.org/uniprotkb/Q8TBK6) carries no function annotation.

**Summary**, from NCBI Gene [54819](https://www.ncbi.nlm.nih.gov/gene/54819):

> Predicted to enable nucleic acid binding activity and zinc ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25954) · Entrez [54819](https://www.ncbi.nlm.nih.gov/gene/54819) · UniProt [Q8TBK6](https://www.uniprot.org/uniprotkb/Q8TBK6) · Ensembl [ENSG00000155329](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155329)

## Data

Gene col 7888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7888); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7888]; `tensor/DDL_lfc|DDL_z.npy` [7888]; `embed/gene_vectors.npy` [7888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7888 or target_col == 7888). Every well: [[ZCCHC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
