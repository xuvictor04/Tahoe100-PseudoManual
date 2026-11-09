---
symbol: "ANKRD54"
type: "gene"
col: 1873
ensembl_id: "ENSG00000100124"
name: "ankyrin repeat domain 54"
location: "22q13.1"
module: 30
arm: "+"
pooled_cpm: 11.99
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ANKRD54

*ankyrin repeat domain 54* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +16.9, q 0e+00, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.776× (z -3.7, q 0.099, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.5 µM in 1 line (COLO 205 0.0778×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS37D]] (+0.60, fdr 2e-05), [[FBXL15]] (+0.59, fdr 1e-05), [[GALT]] (+0.56, fdr 1e-05); moves opposite to [[XRCC5]] (-0.55, fdr 3e-05), [[EIF2S1]] (-0.53, fdr 3e-05), [[MORC2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF433]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +16.9 | 0e+00 | 40/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.32×** | +12.6 | 4e-34 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.10×** | +11.1 | 1e-26 | 37/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +10.7 | 2e-24 | 33/45 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.92×** | +9.8 | 2e-20 | 34/47 (SW480, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +9.4 | 5e-19 | 35/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.1 | 8e-18 | 29/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +8.3 | 1e-14 | 26/42 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.69×** | +7.9 | 2e-13 | 25/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +7.5 | 4e-12 | 26/48 (PANC-1, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.59×** | +7.0 | 1e-10 | 25/46 (SW480, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.45×** | +5.3 | 4e-06 | 18/46 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.43×** | +5.2 | 9e-06 | 20/42 (PANC-1, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.40×** | +5.0 | 2e-05 | 16/41 (CFPAC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +4.7 | 1e-04 | 18/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 4e-04 | 16/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 6e-04 | 13/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.005 | 13/47 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 4/47 (A-172, SNU-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.030 | 2/47 (MIA PaCa-2, H4) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.050 | 3/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.051 | 7/44 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.051 | 4/48 (SHP-77, CFPAC-1, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.053 | 6/48 (CHP-212, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.5 µM in 1 line (COLO 205 0.0778×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.776×** | -3.7 | 0.099 | 10/47 (A549, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[Auranofin (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.099 | 11/47 (J82, C32, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.807× | -3.3 | 0.19 | 5/47 (RKO, Panc 03.27, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 5 µM |  | 0.666× | -3.2 | 0.19 | 5/41 (LOX-IMVI, C32, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.805× | -3.1 | 0.21 | 4/48 (NCI-H23, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 8.90 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 7.39 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0778× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[KATO III (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +11.0) | — |
| [[LoVo (line)]] | wt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +10.4) | — |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37D]] | +0.60 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[FBXL15]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GALT]] | +0.56 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[SAT2]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[C16orf87]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[HOXA9]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZC2HC1A]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[LCA5]] | +0.55 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[DCXR]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[RCOR3]] | +0.54 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[HOXC10]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CCS]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[EIF2S1]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MORC2]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[DNAH1]] | -0.51 | -0.25 / -0.56 | both halves | 4e-04 |  |
| [[SNRPA]] | -0.50 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SERBP1]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.49 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SPCS3]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.48 | -0.14 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[PTPN11]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PRMT3]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[GART]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCT5]] | -0.48 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF433]] | B | ZNF433 activity raises ANKRD54's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 1.33× lower at baseline in the lines without ZNF433 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-38.8, -20.3); signed map (-12.5, 0.6). **Vector** length 61.7, 9.79% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +16.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.1 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | -2.2 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,830,855-37,849,327 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIAR |
| Gene groups (HGNC) | Ankyrin repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXT1](https://www.uniprot.org/uniprotkb/Q6NXT1) (Ankyrin repeat domain-containing protein 54):

> Plays an important role in regulating intracellular signaling events associated with erythroid terminal differentiation.

**Summary**, from NCBI Gene [129138](https://www.ncbi.nlm.nih.gov/gene/129138):

> Predicted to enable protein kinase regulator activity. Predicted to be involved in positive regulation of erythrocyte differentiation and regulation of intracellular signal transduction. Predicted to act upstream of or within nucleocytoplasmic transport and regulation of protein kinase activity. Predicted to be located in midbody. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:25185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25185) · Entrez [129138](https://www.ncbi.nlm.nih.gov/gene/129138) · UniProt [Q6NXT1](https://www.uniprot.org/uniprotkb/Q6NXT1) · Ensembl [ENSG00000100124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100124)

## Data

Gene col 1873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1873); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1873]; `tensor/DDL_lfc|DDL_z.npy` [1873]; `embed/gene_vectors.npy` [1873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1873 or target_col == 1873). Every well: [[ANKRD54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
