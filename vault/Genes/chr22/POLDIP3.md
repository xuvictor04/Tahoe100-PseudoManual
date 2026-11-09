---
symbol: "POLDIP3"
type: "gene"
col: 1898
ensembl_id: "ENSG00000100227"
name: "DNA polymerase delta interacting protein 3"
location: "22q13.2"
module: 130
arm: "+"
pooled_cpm: 37.48
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# POLDIP3

*DNA polymerase delta interacting protein 3* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.31× (z +13.7, q 4e-40, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.535× (z -9.9, q 2e-20, down in 27 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.717× (z -5.0, q 1e-04, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NELFA]] (+0.64, fdr 1e-05), [[GID8]] (+0.61, fdr 1e-05), [[CCDC115]] (+0.60, fdr 3e-05); moves opposite to [[ASPH]] (-0.53, fdr 1e-04), [[SLC4A7]] (-0.52, fdr 3e-05), [[DCBLD2]] (-0.52, fdr 4e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.31×** | +13.7 | 4e-40 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +12.0 | 6e-31 | 44/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +9.4 | 2e-18 | 42/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +9.2 | 5e-18 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +7.6 | 3e-12 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +7.5 | 7e-12 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.7 | 2e-09 | 37/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.0 | 1e-07 | 31/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.5 | 3e-06 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.8 | 9e-05 | 27/48 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.8 | 9e-05 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 2e-04 | 23/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.003 | 24/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.049 | 17/48 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.1 | 0.065 | 19/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -9.9 | 2e-20 | 27/40 (hTERT-HPNE, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.561×** | -9.5 | 5e-19 | 36/47 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -5.0 | 1e-04 | 29/48 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.742×** | -4.6 | 8e-04 | 23/43 (NCI-H2347, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.777×** | -4.2 | 0.003 | 23/48 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -4.1 | 0.003 | 22/48 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -4.0 | 0.006 | 24/48 (NCI-H2030, SHP-77, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.3 | 0.069 | 9/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.819× | -3.0 | 0.13 | 10/48 (HOP62, RKO, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.833× | -3.0 | 0.13 | 12/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 30.5 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +15.6) | — |
| [[SW480 (line)]] | alt | 37.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +11.9) | — |
| [[C32 (line)]] | wt | 48.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +13.4) | — |
| [[LoVo (line)]] | wt | 35.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 39.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 32.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 35.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +8.9) | — |
| [[H4 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.92× (z +9.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0709× (z -16.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.17× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -11.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.13× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NELFA]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[GID8]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.60 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[PCIF1]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[OTUB1]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[AIP]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[KBTBD4]] | +0.55 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[DNAJC27]] | +0.55 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[RAF1]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SH2B1]] | +0.54 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[COPS4]] | +0.53 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPH]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SLC4A7]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[DCBLD2]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ACTN1]] | -0.51 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[GSPT1]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ASAP2]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TPM4]] | -0.50 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[GALNT1]] | -0.49 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[OSBPL8]] | -0.49 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[SEPTIN10]] | -0.49 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[MAMLD1]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[DOCK5]] | -0.48 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises POLDIP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.8, -20.2); signed map (-11.1, 2.1). **Vector** length 61.4, 11.6% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.1 | -1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +1.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.4 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase delta interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,583,721-42,614,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDIP46, KIAA1649, SKAR, PDIP3 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY77](https://www.uniprot.org/uniprotkb/Q9BY77) (Polymerase delta-interacting protein 3):

> Is involved in regulation of translation. Is preferentially associated with CBC-bound spliced mRNA-protein complexes during the pioneer round of mRNA translation. Contributes to enhanced translational efficiency of spliced over nonspliced mRNAs. Recruits activated ribosomal protein S6 kinase beta-1 I/RPS6KB1 to newly synthesized mRNA. Involved in nuclear mRNA export; probably mediated by association with the TREX complex.

**Summary**, from NCBI Gene [84271](https://www.ncbi.nlm.nih.gov/gene/84271):

> This gene encodes an RRM (RNA recognition motif)-containing protein that participates in the regulation of translation by recruiting ribosomal protein S6 kinase beta-1 to mRNAs. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:23782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23782) · Entrez [84271](https://www.ncbi.nlm.nih.gov/gene/84271) · UniProt [Q9BY77](https://www.uniprot.org/uniprotkb/Q9BY77) · Ensembl [ENSG00000100227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100227)

## Data

Gene col 1898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1898); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1898]; `tensor/DDL_lfc|DDL_z.npy` [1898]; `embed/gene_vectors.npy` [1898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1898 or target_col == 1898). Every well: [[POLDIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLDIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
