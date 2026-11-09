---
symbol: "SRR"
type: "gene"
col: 9527
ensembl_id: "ENSG00000167720"
name: "serine racemase"
location: "17p13.3"
module: 15
arm: "+"
pooled_cpm: 8.75
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SRR

*serine racemase* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +19.3, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.675× (z -6.9, q 3e-09, down in 17 of 45 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.747× (z -5.3, q 2e-05, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.193×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.228×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.158×; ⚠ toxic; cell-cycle shift, explains ~3% of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (COLO 205 0.0884×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERVK13-1]] (+0.58, fdr 1e-05), [[GATD1-DT]] (+0.56, fdr 1e-05), [[GHRLOS]] (+0.55, fdr 2e-05); moves opposite to [[PTPN13]] (-0.52, fdr 2e-04), [[MAPRE2]] (-0.51, fdr 6e-05), [[SNX2]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +19.3 | 0e+00 | 39/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +10.8 | 9e-25 | 32/47 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +9.5 | 3e-19 | 27/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.0 | 4e-17 | 8/17 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.8 | 2e-16 | 14/31 (SHP-77, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +8.5 | 2e-15 | 23/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +8.4 | 5e-15 | 14/26 (LoVo, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +6.2 | 5e-08 | 18/43 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.6 | 1e-06 | 10/47 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.31×** | +4.8 | 1e-04 | 12/38 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +4.7 | 1e-04 | 11/38 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 6e-04 | 10/44 (RPMI-7951, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +3.9 | 0.004 | 8/43 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.007 | 6/47 (H4, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.24×** | +3.7 | 0.007 | 8/43 (SW480, COLO 205, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.011 | 9/44 (J82, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.070 | 4/41 (A-172, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9527.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.193×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.228×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.158×; ⚠ toxic; cell-cycle shift, explains ~3% of this change); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (COLO 205 0.0884×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.675×** | -6.9 | 3e-09 | 17/45 (J82, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -6.8 | 3e-09 | 22/44 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.747×** | -5.3 | 2e-05 | 16/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.786×** | -4.4 | 0.002 | 13/46 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.870× | -3.6 | 0.040 | 9/48 (AN3 CA, SW 1088, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.701×** | -3.4 | 0.070 | 3/40 (C-33 A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.838× | -3.2 | 0.11 | 6/48 (A-172, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.13 | 9/45 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +11.6) | — |
| [[C32 (line)]] | wt | 6.45 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.103× (z -8.6) |
| [[COLO 205 (line)]] | alt | 7.12 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0884× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[NCI-H460 (line)]] | wt | 9.23 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.228× (z -9.4) |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK13-1]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[GATD1-DT]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GHRLOS]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[NDOR1]] | +0.55 | +0.33 / +0.58 | both halves | 1e-04 |  |
| [[CTC-338M12.4]] | +0.54 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[LENG8-AS1]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ING5]] | +0.53 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ANKUB1]] | +0.52 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[NPLOC4]] | +0.51 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[WDR53]] | +0.51 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZNF251]] | +0.51 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN13]] | -0.52 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[MAPRE2]] | -0.51 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SNX2]] | -0.50 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[CHN2]] | -0.49 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[CGN]] | -0.48 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ANO9]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[DMXL2]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[NEDD9]] | -0.46 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[CHIC1]] | -0.46 | -0.21 / -0.59 | both halves | 6e-04 |  |
| [[PPARGC1A]] | -0.46 | -0.15 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[USP2]] | -0.45 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[FRMD4B]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[FAAH2]] | -0.45 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.6, 21.3); signed map (4.6, 0.3). **Vector** length 49.4, 5.80% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.8 | +0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +3.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.7 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | +0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.2 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -1.9 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -2.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | serine racemase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,303,383-2,325,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ILV1, ISO1 |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZT4](https://www.uniprot.org/uniprotkb/Q9GZT4) (Serine racemase):

> Pyridoxal-5'-phosphate (PLP)-dependent enzyme that catalyzes the synthesis of D-serine from L-serine. D-serine is a key coagonist with glutamate at NMDA receptors. In addition to racemization, has dehydratase activity towards both L-serine and D-serine, a two-step reaction in which the hydroxyl group of serine is eliminated to produce aminoacrylate (2-aminoprop-2-enoate), and then the aminoacrylate (an unstable intermediate) is deaminated by nonenzymatic hydrolysis to produce pyruvate (By …

**Summary**, from NCBI Gene [63826](https://www.ncbi.nlm.nih.gov/gene/63826):

> Enables several functions, including L-serine ammonia-lyase activity; PDZ domain binding activity; and heterocyclic compound binding activity. Involved in oxoacid metabolic process and response to lipopolysaccharide. Located in cytoplasm and neuronal cell body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14398) · Entrez [63826](https://www.ncbi.nlm.nih.gov/gene/63826) · UniProt [Q9GZT4](https://www.uniprot.org/uniprotkb/Q9GZT4) · Ensembl [ENSG00000167720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167720)

## Data

Gene col 9527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9527); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9527]; `tensor/DDL_lfc|DDL_z.npy` [9527]; `embed/gene_vectors.npy` [9527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9527 or target_col == 9527). Every well: [[SRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
