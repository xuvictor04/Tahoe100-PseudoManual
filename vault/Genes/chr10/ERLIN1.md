---
symbol: "ERLIN1"
type: "gene"
col: 2860
ensembl_id: "ENSG00000107566"
name: "ER lipid raft associated 1"
location: "10q24.31"
module: 6
arm: "+"
pooled_cpm: 43.8
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ERLIN1

*ER lipid raft associated 1* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +12.8, q 2e-34, up in 36 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.35× (z +8.4, q 7e-15, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.457×, A498 0.514×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (NCI-H2030 0.411×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBGCP3]] (+0.70, fdr 7e-06), [[DCK]] (+0.69, fdr 7e-06), [[MAD2L1]] (+0.68, fdr 7e-06); moves opposite to [[IER5]] (-0.64, fdr 1e-05), [[MSX1]] (-0.56, fdr 5e-05), [[PLEKHN1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC44A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.97×** | +12.8 | 2e-34 | 36/46 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.79×** | +10.5 | 2e-23 | 29/40 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.70×** | +9.2 | 4e-18 | 32/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +8.4 | 7e-15 | 38/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.43×** | +6.5 | 8e-09 | 31/47 (NCI-H23, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +6.4 | 2e-08 | 34/48 (AsPC-1, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.8 | 1e-04 | 23/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.24×** | +4.0 | 0.004 | 20/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.6 | 0.018 | 15/34 (NCI-H2347, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.20×** | +3.5 | 0.030 | 17/47 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.3 | 0.047 | 17/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.079 | 7/48 (A-172, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.12× | +3.1 | 0.079 | 6/48 (HT-29, SNU-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.19× | +3.1 | 0.079 | 10/48 (C32, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.0 | 0.10 | 14/48 (PANC-1, NCI-H23, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2860.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.457×, A498 0.514×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (NCI-H2030 0.411×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[ULK-101 (drug)]] 0.05 µM |  | 0.821× | -3.5 | 0.28 | 16/48 (SNU-1, J82, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.2 | 0.34 | 1/48 (CHP-212) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 60.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2030 (line)]] | alt | 50.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Sunitinib (drug)]] 5 µM 0.411× (z -8.6) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 36.5 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.90× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 43.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[KATO III (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 97.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBGCP3]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[DCK]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MAD2L1]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[HADH]] | +0.67 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[SKP2]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CHEK1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[HNRNPR]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PBK]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TMEM109]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PRKDC]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.64 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[MSX1]] | -0.56 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[PLEKHN1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MAFG]] | -0.55 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[APBA3]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SRP19]] | -0.54 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[KCNK6]] | -0.54 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[RPL36AL]] ⚠ | -0.53 | -0.47 / -0.60 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A1]] | B | SLC44A1 activity lowers ERLIN1's level | lines that do not express SLC44A1 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without SLC44A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: RALGPS2, PELI1, LINC00298; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises ERLIN1's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.7, -40.1); signed map (-32.0, -42.3). **Vector** length 91.0, 20.6% of its response variance represented; |z| ≥ 3 in 810 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +5.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +5.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.5 | +9.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +2.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ER lipid raft associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,150,094-100,186,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KE04, Erlin-1, SPG62; previously C10orf69, SPFH1 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Reactome | 11 pathways, smallest: Defective CFTR causes cystic fibrosis; AMPK-induced ERAD and lysosome mediated degradation of PD-L1(CD274); ABC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [O75477](https://www.uniprot.org/uniprotkb/O75477) (Erlin-1):

> Component of the ERLIN1/ERLIN2 complex which mediates the endoplasmic reticulum-associated degradation (ERAD) of inositol 1,4,5-trisphosphate receptors (IP3Rs). Involved in regulation of cellular cholesterol homeostasis by regulation the SREBP signaling pathway. Binds cholesterol and may promote ER retention of the SCAP-SREBF complex.; (Microbial infection) Required early in hepatitis C virus (HCV) infection to initiate RNA replication, and later in the infection to support infectious virus …

**Summary**, from NCBI Gene [10613](https://www.ncbi.nlm.nih.gov/gene/10613):

> The protein encoded by this gene is part of a protein complex that mediates degradation of inositol 1,4,5-trisphosphate receptors in the endoplasmic reticulum. The encoded protein also binds cholesterol and regulates the SREBP signaling pathway, which promotes cellular cholesterol homeostasis. Defects in this gene have been associated with spastic paraplegia 62. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:16947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16947) · Entrez [10613](https://www.ncbi.nlm.nih.gov/gene/10613) · UniProt [O75477](https://www.uniprot.org/uniprotkb/O75477) · Ensembl [ENSG00000107566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107566)

## Data

Gene col 2860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2860); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2860]; `tensor/DDL_lfc|DDL_z.npy` [2860]; `embed/gene_vectors.npy` [2860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2860 or target_col == 2860). Every well: [[ERLIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERLIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
