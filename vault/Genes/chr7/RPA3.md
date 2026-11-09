---
symbol: "RPA3"
type: "gene"
col: 2756
ensembl_id: "ENSG00000106399"
name: "replication protein A3"
location: "7p21.3"
module: 48
arm: "+"
pooled_cpm: 19.02
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# RPA3

*replication protein A3* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.50× (z +9.8, q 4e-20, up in 37 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 8.87×, PANC-1 4.60×, NCI-H1792 5.97×, A-172 5.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 4.71×, SK-MEL-2 7.01×, A549 6.19×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.566× (z -4.5, q 0.004, down in 31 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A498 0.353×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPN3]] (+0.74, fdr 1e-05), [[NUDT1]] (+0.74, fdr 7e-06), [[CENPW]] (+0.69, fdr 7e-06); moves opposite to [[ZNF783]] (-0.60, fdr 1e-05, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[HDDC2]] (-0.57, fdr 4e-05), [[MATR3-1]] (-0.56, fdr 4e-05), [[SNHG26]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[ETFB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2756.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A549 8.87×, PANC-1 4.60×, NCI-H1792 5.97×, A-172 5.57×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 4.71×, SK-MEL-2 7.01×, A549 6.19×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.50×** | +9.8 | 4e-20 | 37/39 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.06×** | +8.5 | 8e-15 | 28/28 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.19×** | +6.1 | 1e-07 | 36/43 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.04×** | +5.1 | 4e-05 | 25/33 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.91×** | +5.1 | 4e-05 | 38/48 (A549, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +4.5 | 5e-04 | 32/46 (A549, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.74×** | +4.3 | 0.001 | 32/48 (A549, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.67×** | +4.1 | 0.004 | 30/47 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.31× | +3.0 | 0.16 | 22/48 (HEC-1-A, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2756.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A498 0.353×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.566×** | -4.5 | 0.004 | 31/46 (A498, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.576×** | -4.3 | 0.004 | 28/48 (KATO III, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -4.2 | 0.004 | 33/48 (SW 1088, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.436× | -3.3 | 0.13 | 25/45 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.671× | -3.1 | 0.21 | 24/48 (HCT15, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 14.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.87× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A498 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.353× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.97× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[PANC-1 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.01× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-427 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN3]] | +0.74 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[NUDT1]] | +0.74 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[CENPW]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[DHTKD1]] | +0.67 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[NDUFA2]] | +0.67 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[PRADC1]] | +0.66 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[LSM3]] ⚠ | +0.64 | +0.64 / +0.61 | both halves | 7e-06 | STRING 514; ⚠ in the vector space only through flagged drug-doses |
| [[BLOC1S1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[DSN1]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[ANAPC11]] | +0.62 | +0.43 / +0.62 | both halves | 3e-05 | pathway: Cell Cycle Checkpoints |
| [[NPAT]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IDH2]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[SIVA1]] | +0.61 | +0.31 / +0.65 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF783]] ⚠ | -0.60 | -0.51 / -0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HDDC2]] | -0.57 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MATR3-1]] | -0.56 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[SNHG26]] | -0.55 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ADCK1]] | -0.53 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ZNF195]] | -0.53 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[KICS2]] | -0.53 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[FBXO30]] | -0.53 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CDV3]] | -0.52 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[DPH5-DT]] | -0.52 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[DPH5]] | -0.51 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[DDX21]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TBKBP1]] | -0.51 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RPA3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TK1]] | C | TK1 activity raises RPA3's level | lines that do not express TK1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without TK1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETFB]] | C | RPA3's natural level strengthens ETFB's drug response | RPA3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.29; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ALDH6A1]] | C | RPA3's natural level strengthens ALDH6A1's drug response | RPA3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.19; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-31.1, -50.9); signed map (-42.9, -38.6). **Vector** length 60.2, 14.0% of its response variance represented; |z| ≥ 3 in 573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +2.5 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +2.1 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.1 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -1.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Gemcitabine (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.9 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | replication protein A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:7,636,518-7,718,607 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REPA3 |
| Gene groups (HGNC) | Nucleotide excision repair |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 71 pathways, smallest: Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha); Removal of the Flap Intermediate |
| Matched by | ensembl_id |

**Function**, from UniProt [P35244](https://www.uniprot.org/uniprotkb/P35244) (Replication protein A 14 kDa subunit):

> As part of the heterotrimeric replication protein A complex (RPA/RP-A), binds and stabilizes single-stranded DNA intermediates that form during DNA replication or upon DNA stress. It prevents their reannealing and in parallel, recruits and activates different proteins and complexes involved in DNA metabolism. Thereby, it plays an essential role both in DNA replication and the cellular response to DNA damage. In the cellular response to DNA damage, the RPA complex controls DNA repair and DNA …

**Summary**, from NCBI Gene [6119](https://www.ncbi.nlm.nih.gov/gene/6119):

> Enables damaged DNA binding activity and single-stranded DNA binding activity. Involved in DNA metabolic process. Part of DNA replication factor A complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10291) · Entrez [6119](https://www.ncbi.nlm.nih.gov/gene/6119) · UniProt [P35244](https://www.uniprot.org/uniprotkb/P35244) · Ensembl [ENSG00000106399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106399)

## Data

Gene col 2756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2756); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2756]; `tensor/DDL_lfc|DDL_z.npy` [2756]; `embed/gene_vectors.npy` [2756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2756 or target_col == 2756). Every well: [[RPA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
