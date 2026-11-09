---
symbol: "IGHMBP2"
type: "gene"
col: 5365
ensembl_id: "ENSG00000132740"
name: "immunoglobulin mu DNA binding protein 2"
location: "11q13.3"
module: 64
arm: "+"
pooled_cpm: 17.12
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# IGHMBP2

*immunoglobulin mu DNA binding protein 2* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.32× (z +16.8, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.626× (z -9.4, q 3e-18, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHBDD3]] (+0.71, fdr 1e-05), [[TSSC4]] (+0.65, fdr 2e-05), [[GPATCH3]] (+0.64, fdr 9e-06); moves opposite to [[ARL6IP6]] (-0.59, fdr 6e-05), [[GOLIM4]] (-0.54, fdr 3e-05), [[PODXL2]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +16.8 | 0e+00 | 44/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.08×** | +14.7 | 0e+00 | 44/47 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +14.5 | 1e-45 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.13×** | +14.3 | 2e-44 | 42/47 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +13.9 | 7e-42 | 37/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +11.6 | 3e-29 | 34/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +11.6 | 4e-29 | 37/47 (SW480, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +10.1 | 5e-22 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.0 | 1e-21 | 29/47 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +9.7 | 1e-20 | 33/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +9.4 | 2e-19 | 32/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +8.9 | 2e-17 | 33/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +8.1 | 3e-14 | 32/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +7.3 | 1e-11 | 29/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +7.0 | 8e-11 | 25/48 (KATO III, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.0 | 6e-08 | 19/47 (SNU-1, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.626×** | -9.4 | 3e-18 | 34/47 (RPMI-7951, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -9.0 | 5e-17 | 32/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.678×** | -7.8 | 1e-12 | 26/39 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -6.4 | 2e-08 | 17/32 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -5.9 | 4e-07 | 21/47 (LoVo, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.755×** | -5.7 | 1e-06 | 19/47 (SW1417, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.766×** | -5.4 | 6e-06 | 17/47 (SW1417, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.803×** | -4.1 | 0.003 | 12/33 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.825×** | -3.9 | 0.006 | 13/47 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.734×** | -3.3 | 0.065 | 11/45 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.3 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +12.6) | — |
| [[LoVo (line)]] | wt | 18.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 18.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +10.4) | — |
| [[A498 (line)]] | wt | 9.11 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.88 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0868× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0791× (z -15.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.8) | — |
| [[J82 (line)]] | alt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.345× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.276× (z -8.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHBDD3]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.65 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[GPATCH3]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[C12orf43]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RPAP1]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.63 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[MRM3]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TIRAP]] | +0.62 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.62 | +0.64 / +0.40 | both halves | 4e-05 |  |
| [[KMT2D]] | +0.61 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[SETD1B]] | +0.60 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ALKBH6]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6IP6]] | -0.59 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[GOLIM4]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PODXL2]] | -0.54 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[RADX]] | -0.53 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[CYB5A]] | -0.53 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[MED14]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SLC44A1]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MZT1]] | -0.51 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[TWSG1]] | -0.51 | -0.34 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises IGHMBP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises IGHMBP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-42.6, 10.3); signed map (-6.8, -20.3). **Vector** length 71.0, 12.7% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +16.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +14.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +6.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +7.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Berbamine (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | immunoglobulin mu DNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:68,903,863-68,940,602 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFAND7, SMUBP2, CATF1, SMARD1, HCSA, HMN6, CMT2S |
| Gene groups (HGNC) | Zinc fingers AN1-type; UPF1 like RNA helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [P38935](https://www.uniprot.org/uniprotkb/P38935) (DNA-binding protein SMUBP-2):

> 5' to 3' helicase that unwinds both RNA and DNA duplexes in an ATP-dependent reaction (Probable). Specific to 5'-phosphorylated single-stranded guanine-rich sequences. May play a role in RNA metabolism, ribosome biogenesis or initiation of translation. May play a role in regulation of transcription (By similarity). Interacts with tRNA-Tyr. Has low processivity.

**Summary**, from NCBI Gene [3508](https://www.ncbi.nlm.nih.gov/gene/3508):

> This gene encodes a helicase superfamily member that binds a specific DNA sequence from the immunoglobulin mu chain switch region. Mutations in this gene lead to spinal muscle atrophy with respiratory distress type 1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5542) · Entrez [3508](https://www.ncbi.nlm.nih.gov/gene/3508) · UniProt [P38935](https://www.uniprot.org/uniprotkb/P38935) · Ensembl [ENSG00000132740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132740)

## Data

Gene col 5365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5365); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5365]; `tensor/DDL_lfc|DDL_z.npy` [5365]; `embed/gene_vectors.npy` [5365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5365 or target_col == 5365). Every well: [[IGHMBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGHMBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
