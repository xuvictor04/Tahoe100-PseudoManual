---
symbol: "PDXP"
type: "gene"
col: 14270
ensembl_id: "ENSG00000241360"
name: "pyridoxal phosphatase"
location: "22q13.1"
module: 134
arm: "+"
pooled_cpm: 5.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# PDXP

*pyridoxal phosphatase* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.17× (z +10.1, q 5e-21, up in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +7.2, q 1e-10, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.578× (z -4.6, q 0.002, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.219×, NCI-H2030 0.259×); [[Adenosine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0454×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0976×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC3]] (+0.77, fdr 7e-06), [[STK32C]] (+0.76, fdr 7e-06), [[CABIN1]] (+0.76, fdr 7e-06); moves opposite to [[C11orf58]] (-0.71, fdr 7e-06), [[GTF2H1]] (-0.68, fdr 8e-06), [[UTP20]] (-0.67, fdr 7e-06).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTXN1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UNC119]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.17×** | +10.1 | 5e-21 | 42/47 (SW480, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.13×** | +9.9 | 8e-21 | 38/47 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.75×** | +8.8 | 2e-16 | 39/47 (SW480, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.2 | 1e-10 | 25/42 (A549, A498, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.2 | 8e-08 | 19/29 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.94×** | +5.8 | 7e-07 | 24/42 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +5.3 | 1e-05 | 26/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.82×** | +5.2 | 1e-05 | 19/35 (NCI-H2347, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.64×** | +4.3 | 1e-03 | 18/41 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.57×** | +3.8 | 0.009 | 1/11 (SNU-423) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.52×** | +3.6 | 0.014 | 8/27 (SHP-77, HEC-1-A, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.14×** | +3.5 | 0.024 | 12/44 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.029 | 15/46 (A498, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.46×** | +3.3 | 0.039 | 14/47 (SW480, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.48×** | +3.2 | 0.057 | 7/17 (SW480, PANC-1, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14270.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.219×, NCI-H2030 0.259×); [[Adenosine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0454×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SHP-77 0.0976×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.578×** | -4.6 | 0.002 | 21/45 (HCT15, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.376×** | -4.4 | 0.002 | 18/43 (MIA PaCa-2, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.656× | -3.4 | 0.11 | 13/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0976× (z -9.4) |
| [[C32 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.314× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 8.62 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0775× (z -8.8) |
| [[Hs 766T (line)]] | wt | 6.66 | 0 | 1 | — | [[Adenosine (drug)]] 0.5 µM 0.0454× (z -10.6) |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 4.81 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0615× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 9.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -8.8) |
| [[SW480 (line)]] | alt | 4.37 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 5.61× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | +0.77 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[STK32C]] | +0.76 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.76 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[PDK3]] | +0.75 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[TENT4A]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[UBTD1]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[KIAA1958]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.71 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[GTF2H1]] | -0.68 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[UTP20]] | -0.67 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[CHM]] | -0.66 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ARMCX4]] | -0.66 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.66 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[TTC27]] | -0.65 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[ZNF655]] | -0.64 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.64 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.64 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[DNAJC8]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[TRIP12]] | -0.63 | -0.47 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTXN1]] | B | CTXN1 activity raises PDXP's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without CTXN1 | 0.026 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC119]] | C | PDXP's natural level weakens UNC119's drug response | PDXP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.33; direction not clear | 0.093 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.9, -16.4); signed map (-36.7, 22.8). **Vector** length 78.4, 15.5% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.2 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.4 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.4 | +8.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.5 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | pyridoxal phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,658,723-37,666,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ37E16.5, FLJ32703, CIN |
| Gene groups (HGNC) | HAD Asp-based protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GD0](https://www.uniprot.org/uniprotkb/Q96GD0) (Chronophin):

> Functions as a pyridoxal phosphate (PLP) phosphatase, which also catalyzes the dephosphorylation of pyridoxine 5'-phosphate (PNP) and pyridoxamine 5'-phosphate (PMP), with order of substrate preference PLP > PNP > PMP and therefore plays a role in vitamin B6 metabolism. Also functions as a protein serine phosphatase that specifically dephosphorylates 'Ser-3' in proteins of the actin-depolymerizing factor (ADF)/cofilin family like CFL1 and DSTN. Thereby, regulates cofilin-dependent actin …

**Summary**, from NCBI Gene [57026](https://www.ncbi.nlm.nih.gov/gene/57026):

> Pyridoxal 5-prime-phosphate (PLP) is the active form of vitamin B6 that acts as a coenzyme in maintaining biochemical homeostasis. The preferred degradation route from PLP to 4-pyridoxic acid involves the dephosphorylation of PLP by PDXP (Jang et al., 2003 [PubMed 14522954]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30259) · Entrez [57026](https://www.ncbi.nlm.nih.gov/gene/57026) · UniProt [Q96GD0](https://www.uniprot.org/uniprotkb/Q96GD0) · Ensembl [ENSG00000241360](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241360)

## Data

Gene col 14270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14270); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14270]; `tensor/DDL_lfc|DDL_z.npy` [14270]; `embed/gene_vectors.npy` [14270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14270 or target_col == 14270). Every well: [[PDXP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDXP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
