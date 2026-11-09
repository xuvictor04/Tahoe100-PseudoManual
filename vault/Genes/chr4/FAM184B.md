---
symbol: "FAM184B"
type: "gene"
col: 524
ensembl_id: "ENSG00000047662"
name: "family with sequence similarity 184 member B"
location: "4p15.32-p15.31"
module: 26
arm: "+"
pooled_cpm: 4.78
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FAM184B

*family with sequence similarity 184 member B* — 4p15.32-p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.31× (z +20.3, q 0e+00, up in 38 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (PANC-1 0.0613×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.1000×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF451-AS1]] (+0.82, fdr 7e-06), [[TBCE-1]] (+0.81, fdr 7e-06), [[PSMD7-DT]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CASC20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +20.3 | 0e+00 | 38/41 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.04×** | +12.1 | 3e-31 | 28/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +11.3 | 3e-27 | 24/39 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +10.3 | 7e-23 | 19/24 (LoVo, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +9.3 | 2e-18 | 9/12 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +8.7 | 4e-16 | 17/36 (HS-578T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +7.9 | 3e-13 | 21/38 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +7.8 | 3e-13 | 12/26 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +7.8 | 5e-13 | 25/45 (A-172, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.5 | 5e-12 | 6/8 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +5.8 | 4e-07 | 3/10 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 2e-06 | 16/40 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +5.3 | 4e-06 | 21/46 (NCI-H460, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.29×** | +4.3 | 8e-04 | 13/46 (SNU-423, A498, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.001 | 6/33 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +3.8 | 0.005 | 6/42 (NCI-H1792, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +3.6 | 0.010 | 6/38 (NCI-H2347, SK-MEL-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Pyridoxine (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.037 | 1/44 (NCI-H1573) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.093 | 9/42 (KATO III, RKO, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (PANC-1 0.0613×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.1000×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.0 | 0.037 | 14/48 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.826× | -3.3 | 0.28 | 7/47 (HEC-1-A, Hs 766T, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.753× | -3.2 | 0.28 | 13/41 (SW1417, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.774× | -3.1 | 0.28 | 6/47 (SW 1271, NCI-H460, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.05 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.6) | — |
| [[A498 (line)]] | wt | 4.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 3.80 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.1000× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 6.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 3.21 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0613× (z -11.5) |
| [[A-172 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451-AS1]] | +0.82 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.81 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.81 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.81 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.81 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.81 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.81 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[OOEP]] | +0.80 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.79 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[COLEC11]] | +0.79 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.79 | +0.74 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises FAM184B's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without CASC20 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FAM184B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LY96]] | B | LY96 activity raises FAM184B's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.25× lower at baseline in the lines without LY96 | 0.033 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[GPC5]] | B | GPC5 activity raises FAM184B's level | lines that do not express GPC5 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without GPC5 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IQCJ]] | B | IQCJ activity raises FAM184B's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without IQCJ | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.8, 23.6); signed map (29.9, -0.1). **Vector** length 58.4, 7.59% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +20.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +12.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 184 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32-p15.31 — chr4:17,629,306-17,781,621 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1276 |
| Matched by | ensembl_id |

UniProt [Q9ULE4](https://www.uniprot.org/uniprotkb/Q9ULE4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29235) · Entrez [27146](https://www.ncbi.nlm.nih.gov/gene/27146) · UniProt [Q9ULE4](https://www.uniprot.org/uniprotkb/Q9ULE4) · Ensembl [ENSG00000047662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047662)

## Data

Gene col 524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 524); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 524]; `tensor/DDL_lfc|DDL_z.npy` [524]; `embed/gene_vectors.npy` [524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 524 or target_col == 524). Every well: [[FAM184B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM184B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
