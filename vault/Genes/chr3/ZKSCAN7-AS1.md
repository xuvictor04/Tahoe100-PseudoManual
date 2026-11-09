---
symbol: "ZKSCAN7-AS1"
type: "gene"
col: 14107
ensembl_id: "ENSG00000236869"
name: "ZKSCAN7 ZNF cluster antisense RNA 1"
location: "3p21.31"
module: 35
arm: "+"
pooled_cpm: 6.35
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ZKSCAN7-AS1

*ZKSCAN7 ZNF cluster antisense RNA 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.71× (z +8.5, q 1e-14, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +8.4, q 2e-14, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.541× (z -6.9, q 3e-09, down in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.600× (z -5.7, q 3e-06, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 3 lines (HCT15 0.0514×, HOP62 0.190×, NCI-H2347 0.195×; ⚠ cell-cycle shift, explains ~26% of this change); [[Sonidegib (drug)]] 0.5 µM in 1 line (LoVo 0.0498×); [[Rosiglitazone (drug)]] 5 µM in 1 line (A-172 0.0805×); [[Auranofin (drug)]] 0.5 µM in 1 line (HCT15 0.0648×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF236-DT]] (+0.68, fdr 1e-05), [[THBS4]] (+0.67, fdr 1e-05), [[PPP1R42]] (+0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZNF91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.71×** | +8.5 | 1e-14 | 29/48 (LS 180, KATO III, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.4 | 2e-14 | 27/43 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.4 | 2e-11 | 14/31 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.5 | 4e-06 | 7/17 (SW 900, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.8 | 2e-04 | 19/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.2 | 0.002 | 3/10 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.004 | 8/46 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.023 | 14/48 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.023 | 8/48 (BT-474, SW1417, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.023 | 10/46 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.071 | 3/47 (SW480, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.074 | 13/44 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.074 | 9/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.33×** | +3.1 | 0.091 | 9/34 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +3.0 | 0.092 | 6/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.092 | 10/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14107.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 3 lines (HCT15 0.0514×, HOP62 0.190×, NCI-H2347 0.195×; ⚠ cell-cycle shift, explains ~26% of this change); [[Sonidegib (drug)]] 0.5 µM in 1 line (LoVo 0.0498×); [[Rosiglitazone (drug)]] 5 µM in 1 line (A-172 0.0805×); [[Auranofin (drug)]] 0.5 µM in 1 line (HCT15 0.0648×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.541×** | -6.9 | 3e-09 | 26/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.600×** | -5.7 | 3e-06 | 22/46 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.641×** | -5.0 | 1e-04 | 19/46 (HCT15, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.697×** | -4.0 | 0.008 | 16/43 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.741× | -3.2 | 0.12 | 7/48 (SW48, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Allopurinol (drug)]] 0.05 µM |  | 0.750× | -3.2 | 0.12 | 11/48 (AN3 CA, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.753× | -3.2 | 0.12 | 11/48 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 8.63 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0514× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 0.5 µM 0.0648× (z -8.8) |
| [[A-172 (line)]] | wt | 5.54 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0805× (z -9.4) |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 4.76 | 0 | 1 | — | [[Sonidegib (drug)]] 0.5 µM 0.0498× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.195× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF236-DT]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[THBS4]] | +0.67 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[PPP1R42]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ANKHD1-DT]] | +0.63 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[APPBP2-DT]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF561-AS1]] | +0.63 | +0.71 / +0.42 | both halves | 4e-05 | same gene group |
| [[ZNF721]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ZNF529-AS1]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 | same gene group |
| [[MAIP1]] | +0.61 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[AHI1-DT]] | +0.61 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[LINC02951]] | +0.61 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF91]] | B | ZNF91 activity raises ZKSCAN7-AS1's level | lines that do not express ZNF91 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without ZNF91 | 0.077 | ⚠ within organs, on part of the lines; also absent: ZNF493 |
| [[HECTD2]] | B | HECTD2 activity raises ZKSCAN7-AS1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without HECTD2 | 0.077 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[ZNF528-AS1]] | B | ZNF528-AS1 activity raises ZKSCAN7-AS1's level | lines that do not express ZNF528-AS1 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without ZNF528-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF528, ZNF625, ZNF880 |
| [[MIR137HG]] | B | MIR137HG activity raises ZKSCAN7-AS1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without MIR137HG | 0.090 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2 |
| [[TOP2A]] | B | TOP2A activity lowers ZKSCAN7-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.1, 23.7); signed map (33.3, -2.7). **Vector** length 50.4, 6.10% of its response variance represented; |z| ≥ 3 in 855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.4 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +4.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +0.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ZKSCAN7 ZNF cluster antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p21.31 — chr3:44,553,148-44,685,665 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-944L7.4; previously ZNF197-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53964) · Entrez [112840933](https://www.ncbi.nlm.nih.gov/gene/112840933) · Ensembl [ENSG00000236869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236869)

## Data

Gene col 14107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14107); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14107]; `tensor/DDL_lfc|DDL_z.npy` [14107]; `embed/gene_vectors.npy` [14107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14107 or target_col == 14107). Every well: [[ZKSCAN7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
