---
symbol: "SLC19A3"
type: "gene"
col: 5777
ensembl_id: "ENSG00000135917"
name: "solute carrier family 19 member 3"
location: "2q36.3"
module: 19
arm: "+"
pooled_cpm: 3.57
n_lines_expressing: 14
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLC19A3

*solute carrier family 19 member 3* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.63× (z +12.4, q 1e-32, up in 11 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.238×, A498 0.199×, NCI-H460 0.336×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.136×, KATO III 0.158×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.115×, NCI-H460 0.189×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.181×, KATO III 0.218×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GYG2]] (+0.60, fdr 6e-05), [[GDA]] (+0.58, fdr 1e-05), [[SLITRK4]] (+0.57, fdr 2e-05); moves opposite to [[LINC00310]] (-0.54, fdr 2e-05), [[CCDC90B]] (-0.49, fdr 1e-04), [[EMP3]] (-0.48, fdr 9e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AKR1B10]] → it (grade C ⚠); 3 go from it, the strongest it → cells under [[Docetaxel (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.63×** | +12.4 | 1e-32 | 11/11 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.66×** | +8.5 | 5e-15 | 1/4 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.45×** | +8.4 | 6e-15 | 9/11 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.27×** | +8.1 | 9e-14 | 9/11 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.13×** | +7.8 | 9e-13 | 9/11 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.94×** | +7.3 | 2e-11 | 7/11 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.83×** | +7.1 | 1e-10 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +6.6 | 2e-09 | 1/5 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.54×** | +6.3 | 1e-08 | 10/11 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.5 | 2e-06 | 1/10 (NCI-H1792) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.01×** | +5.3 | 5e-06 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +5.2 | 1e-05 | 2/8 (SK-MEL-2, PANC-1) | top dose only | cell-cycle shift (explains ~18% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.52×** | +4.5 | 3e-04 | 1/8 (NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.41×** | +4.4 | 5e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +4.3 | 8e-04 | 3/11 (A549, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.19×** | +4.1 | 0.001 | 8/11 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.004 | 1/9 (NCI-H23) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.006 | 5/11 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.65×** | +3.4 | 0.018 | 2/8 (SK-MEL-2, PANC-1) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.026 | 3/8 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.033 | 1/11 (A498) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5777.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.238×, A498 0.199×, NCI-H460 0.336×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.136×, KATO III 0.158×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.115×, NCI-H460 0.189×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.181×, KATO III 0.218×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -3.1 | 0.60 | 1/11 (J82) | inconsistent across doses |  |
| [[Adenosine (drug)]] 0.5 µM |  | 0.641× | -3.1 | 0.60 | 1/11 (RKO) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 40.2 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.7) |
| [[A498 (line)]] | wt | 10.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -10.4) |
| [[A549 (line)]] | wt | 7.39 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0720× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0718× (z -9.3) |
| [[A-172 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.728 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.587 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GYG2]] | +0.60 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[GDA]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SLITRK4]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GTF2I-AS1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NRCAM]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[DDIT4L]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[SCARA5]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SLC15A5]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LRRC63]] | +0.52 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SNCA]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PAX7]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ST6GALNAC3]] | +0.51 | +0.37 / +0.39 | both halves | 8e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00310]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CCDC90B]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[EMP3]] | -0.48 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[CCDC92]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[CSNK2B]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[MRPS6]] | -0.45 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[LINC02646]] | -0.44 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[CNPPD1]] | -0.44 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NMNAT1]] | -0.43 | -0.34 / -0.29 | both halves | 2e-04 | pathway: Metabolism of vitamins and cofactors |
| [[CPEB2-DT]] | -0.43 | -0.18 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[GPR161]] | -0.43 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[RNF170]] | -0.43 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[INKA2]] | -0.43 | -0.22 / -0.32 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1B10]] | C | AKR1B10 activity raises SLC19A3's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.99× lower at baseline in the lines without AKR1B10 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Docetaxel (drug)]] 0.5 µM | B | SLC19A3 activity lowers the cells' numbers under Docetaxel 0.5 µM (makes them more sensitive) | lines that do not express SLC19A3 (36) vs lines expressing it (12) | the lines without SLC19A3: 1.16× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, MTND1P23, LINC00824 |
| [[MCOLN2]] | B | SLC19A3 activity raises MCOLN2's level | lines that do not express SLC19A3 (36) vs lines expressing it (14) | 2.18× lower at baseline in the lines without SLC19A3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, MTND1P23, LINC00824 |
| [[AKR1B10]] | C | SLC19A3 activity raises AKR1B10's level | lines that do not express SLC19A3 (36) vs lines expressing it (14) | 3.44× lower at baseline in the lines without SLC19A3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, MTND1P23, LINC00824; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.460). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 38.6); signed map (45.3, 45.3). **Vector** length 36.4, 10.6% of its response variance represented; |z| ≥ 3 in 354 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +7.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.9 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | -0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.3 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -0.9 | -2.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.9 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 19 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,683,763-227,718,028 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THTR2, thTr-2, hTHTR2 |
| Gene groups (HGNC) | Solute carrier family 19 |
| Reactome | 3 pathways, smallest: Vitamin B1 (thiamin) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZV2](https://www.uniprot.org/uniprotkb/Q9BZV2) (Thiamine transporter 2):

> Mediates high affinity thiamine uptake, probably via a proton anti-port mechanism. Has no folate transport activity. Mediates H(+)-dependent pyridoxine transport.

**Summary**, from NCBI Gene [80704](https://www.ncbi.nlm.nih.gov/gene/80704):

> This gene encodes a ubiquitously expressed transmembrane thiamine transporter that lacks folate transport activity. Mutations in this gene cause biotin-responsive basal ganglia disease (BBGD); a recessive disorder manifested in childhood that progresses to chronic encephalopathy, dystonia, quadriparesis, and death if untreated. Patients with BBGD have bilateral necrosis in the head of the caudate nucleus and in the putamen. Administration of high doses of biotin in the early progression of the …

**Accessions** — [HGNC:16266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16266) · Entrez [80704](https://www.ncbi.nlm.nih.gov/gene/80704) · UniProt [Q9BZV2](https://www.uniprot.org/uniprotkb/Q9BZV2) · Ensembl [ENSG00000135917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135917)

## Data

Gene col 5777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5777); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5777]; `tensor/DDL_lfc|DDL_z.npy` [5777]; `embed/gene_vectors.npy` [5777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5777 or target_col == 5777). Every well: [[SLC19A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC19A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
