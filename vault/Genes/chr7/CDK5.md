---
symbol: "CDK5"
type: "gene"
col: 9020
ensembl_id: "ENSG00000164885"
name: "cyclin dependent kinase 5"
location: "7q36.1"
module: 58
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CDK5

*cyclin dependent kinase 5* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.66× (z +12.6, q 2e-33, up in 8 of 9 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.62× (z +3.6, q 0.022, up in 9 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 5.01×, SW480 7.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 8.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.353× (z -7.8, q 3e-12, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THYN1]] (+0.71, fdr 7e-06), [[SNRNP25]] (+0.70, fdr 3e-05), [[POP5]] (+0.66, fdr 6e-05); moves opposite to [[ANKRD18A]] (-0.52, fdr 4e-04), [[SPON1-AS1]] (-0.51, fdr 2e-04), [[RFX3-DT]] (-0.49, fdr 0.002, ⚠ not reproduced), [[USP45]] (-0.49, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 5.01×, SW480 7.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 8.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **5.66×** | +12.6 | 2e-33 | 8/9 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.93×** | +12.0 | 8e-31 | 21/21 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.99×** | +7.6 | 4e-12 | 8/9 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.11×** | +5.6 | 3e-06 | 25/45 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.99×** | +5.2 | 2e-05 | 26/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.64×** | +3.8 | 0.016 | 12/24 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.022 | 9/37 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.62×** | +3.5 | 0.032 | 8/29 (A-172, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.57×** | +3.4 | 0.044 | 17/47 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9020.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.353×** | -7.8 | 3e-12 | 35/47 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.381×** | -7.2 | 1e-10 | 30/46 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -6.2 | 1e-07 | 28/39 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -5.6 | 3e-06 | 28/44 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -5.5 | 5e-06 | 23/37 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.342×** | -4.2 | 0.002 | 16/42 (hTERT-HPNE, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -3.6 | 0.024 | 11/33 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.669× | -3.0 | 0.19 | 12/46 (NCI-H1573, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.94 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.83× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -8.7) |
| [[A498 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 5.93 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0973× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 6.04 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -9.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Panc 03.27 (line)]] | alt | 4.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0344× (z -10.8) |
| [[PANC-1 (line)]] | alt | 3.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.31× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[RKO (line)]] | wt | 4.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0490× (z -9.2) |
| [[A-172 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THYN1]] | +0.71 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SNRNP25]] | +0.70 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[POP5]] | +0.66 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[ATP6V0E2]] | +0.65 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GAMT]] | +0.65 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[SCRN2]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ROGDI]] | +0.64 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[MFSD3]] | +0.63 | +0.40 / +0.65 | both halves | 4e-05 |  |
| [[RPUSD1]] | +0.62 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PAFAH1B3]] | +0.61 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[GPS1]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.52 | -0.34 / -0.24 | both halves | 4e-04 |  |
| [[SPON1-AS1]] | -0.51 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[RFX3-DT]] | -0.49 | -0.32 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[USP45]] | -0.49 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[RCC1]] | -0.48 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[MSTO1]] | -0.48 | -0.19 / -0.39 | ⚠ not reproduced | 8e-04 |  |
| [[CDKL1]] | -0.48 | -0.40 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CDK5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.6, -13.8); signed map (-26.7, -2.8). **Vector** length 46.6, 6.55% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +2.7 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.7 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.6 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.3 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.0 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -7.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,053,815-151,057,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSSALRE |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Reactome | 35 pathways, smallest: Phosphorylation and nuclear translocation of BMAL1 (ARNTL) and CLOCK; Activated NTRK2 signals through CDK5; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00535](https://www.uniprot.org/uniprotkb/Q00535) (Cyclin-dependent kinase 5):

> Proline-directed serine/threonine-protein kinase essential for neuronal cell cycle arrest and differentiation and may be involved in apoptotic cell death in neuronal diseases by triggering abortive cell cycle re-entry. Interacts with D1 and D3-type G1 cyclins. Phosphorylates SRC, NOS3, VIM/vimentin, p35/CDK5R1, MEF2A, SIPA1L1, SH3GLB1, PXN, PAK1, MCAM/MUC18, SEPT5, SYN1, DNM1, AMPH, SYNJ1, CDK16, RAC1, RHOA, CDC42, TONEBP/NFAT5, MAPT/TAU, MAP1B, histone H1, p53/TP53, HDAC1, APEX1, PTK2/FAK1, …

**Summary**, from NCBI Gene [1020](https://www.ncbi.nlm.nih.gov/gene/1020):

> This gene encodes a proline-directed serine/threonine kinase that is a member of the cyclin-dependent kinase family of proteins. Unlike other members of the family, the protein encoded by this gene does not directly control cell cycle regulation. Instead the protein, which is predominantly expressed at high levels in mammalian postmitotic central nervous system neurons, functions in diverse processes such as synaptic plasticity and neuronal migration through phosphorylation of proteins required …

**Accessions** — [HGNC:1774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1774) · Entrez [1020](https://www.ncbi.nlm.nih.gov/gene/1020) · UniProt [Q00535](https://www.uniprot.org/uniprotkb/Q00535) · Ensembl [ENSG00000164885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164885)

## Data

Gene col 9020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9020); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9020]; `tensor/DDL_lfc|DDL_z.npy` [9020]; `embed/gene_vectors.npy` [9020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9020 or target_col == 9020). Every well: [[CDK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
