---
symbol: "RUBCNL"
type: "gene"
col: 2248
ensembl_id: "ENSG00000102445"
name: "rubicon like autophagy enhancer"
location: "13q14.13"
module: 196
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 20
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# RUBCNL

*rubicon like autophagy enhancer* — 13q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.86× (z +13.2, q 7e-37, up in 11 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.607× (z -4.1, q 0.013, down in 4 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (C32 0.0242×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0366×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0836×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARAP3]] (+0.53, fdr 3e-05), [[HTR7]] (+0.52, fdr 3e-05), [[IL19]] (+0.50, fdr 2e-05); moves opposite to [[RAB14]] (-0.45, fdr 1e-04), [[DCT]] (-0.44, fdr 1e-04), [[ATRAID]] (-0.43, fdr 1e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[IL19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.86×** | +13.2 | 7e-37 | 11/17 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +12.3 | 2e-32 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +10.2 | 3e-22 | 5/12 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +10.0 | 4e-21 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.53×** | +8.2 | 3e-14 | 7/12 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.1 | 7e-14 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.3 | 1e-05 | 1/10 (SNU-423) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +5.1 | 3e-05 | 5/15 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +4.7 | 2e-04 | 4/14 (BT-474, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.07×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.5 | 3e-04 | 0/7 | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.55×** | +4.3 | 7e-04 | 2/4 (C32, SW480) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +4.2 | 0.001 | 6/14 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.57×** | +4.0 | 0.003 | 1/11 (C32) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.008 | 1/11 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.6 | 0.010 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.024 | 7/17 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.024 | 0/17 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.024 | 0/9 | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.026 | 0/11 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.039 | 2/11 (NCI-H460, SW480) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.051 | 0/17 | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.38×** | +2.9 | 0.085 | 0/13 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2248.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (C32 0.0242×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0366×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0836×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.607×** | -4.1 | 0.013 | 4/17 (C32, HCT15, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.632×** | -4.1 | 0.013 | 2/17 (NCI-H1573, J82) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.788× | -3.0 | 0.46 | 3/15 (SW1417, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 6.16 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0242× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 8.00 | 0 | 2 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0366× (z -12.7) |
| [[BT-474 (line)]] | alt | 0.985 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 5.84 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0767× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.880 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAP3]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[HTR7]] | +0.52 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[IL19]] | +0.50 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[ARHGEF2]] | +0.49 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[CD58]] | +0.48 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[GCKR]] | +0.48 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[ZNF697]] | +0.47 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[TMEM163]] | +0.46 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[ATP13A3-DT]] | +0.46 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[SLC5A1]] | +0.46 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[MILR1]] | +0.46 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[LINC02970]] | +0.45 | +0.32 / +0.42 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB14]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[DCT]] | -0.44 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ATRAID]] | -0.43 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[GTF2I]] | -0.41 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ATP5F1A]] | -0.40 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[ZHX1]] | -0.40 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[MIRLET7BHG]] | -0.40 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[MARVELD1]] | -0.40 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[TMEM245]] | -0.40 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[PEBP1]] | -0.40 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PRDX6-AS1]] | -0.39 | -0.27 / -0.29 | both halves | 3e-04 |  |
| [[TBC1D5]] | -0.39 | -0.28 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL19]] | B | RUBCNL activity raises IL19's level | lines that do not express RUBCNL (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without RUBCNL | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01967, LRRN1, CADPS |
| [[TMEM154]] | C | RUBCNL activity raises TMEM154's level | lines that do not express RUBCNL (30) vs lines expressing it (20) | 1.64× lower at baseline in the lines without RUBCNL | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC01967, LRRN1, CADPS; co-absent with the target |
| [[CRTAC1]] | C | RUBCNL activity raises CRTAC1's level | lines that do not express RUBCNL (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without RUBCNL | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC01967, LRRN1, CADPS; co-absent with the target |
| [[DCT]] | C | RUBCNL activity raises DCT's level | lines that do not express RUBCNL (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without RUBCNL | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC01967, LRRN1, CADPS; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.1, 7.4); signed map (11.2, 53.6). **Vector** length 32.7, 6.62% of its response variance represented; |z| ≥ 3 in 413 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.9 | +2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.7 | -0.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | rubicon like autophagy enhancer |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.13 — chr13:46,334,681-46,438,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21562, PACER; previously C13orf18, KIAA0226L |
| Gene groups (HGNC) | PIK3C3 complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H714](https://www.uniprot.org/uniprotkb/Q9H714) (Protein associated with UVRAG as autophagy enhancer):

> Regulator of autophagy that promotes autophagosome maturation by facilitating the biogenesis of phosphatidylinositol 3-phosphate (PtdIns(3)P) in late steps of autophagy. Acts by antagonizing RUBCN, thereby stimulating phosphatidylinositol 3-kinase activity of the PI3K/PI3KC3 complex. Following anchorage to the autophagosomal SNARE STX17, promotes the recruitment of PI3K/PI3KC3 and HOPS complexes to the autophagosome to regulate the fusion specificity of autophagosomes with late …

**Summary**, from NCBI Gene [80183](https://www.ncbi.nlm.nih.gov/gene/80183):

> This gene encodes a cysteine-rich protein that contains a putative zinc-RING and/or ribbon domain. The encoded protein is related to Run domain Beclin-1-interacting and cysteine-rich domain-containing protein, which plays a role in endocytic trafficking and autophagy. In cervical cancer cell lines, this gene is expressed at low levels and may function as a tumor suppressor. Promoter hypermethylation of this gene is observed in cervical cancer cell lines and tissue derived from human patients. …

**Accessions** — [HGNC:20420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20420) · Entrez [80183](https://www.ncbi.nlm.nih.gov/gene/80183) · UniProt [Q9H714](https://www.uniprot.org/uniprotkb/Q9H714) · Ensembl [ENSG00000102445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102445)

## Data

Gene col 2248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2248); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2248]; `tensor/DDL_lfc|DDL_z.npy` [2248]; `embed/gene_vectors.npy` [2248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2248 or target_col == 2248). Every well: [[RUBCNL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUBCNL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
