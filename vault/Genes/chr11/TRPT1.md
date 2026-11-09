---
symbol: "TRPT1"
type: "gene"
col: 7405
ensembl_id: "ENSG00000149743"
name: "tRNA phosphotransferase 1"
location: "11q13.1"
module: 3
arm: "+"
pooled_cpm: 9.88
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TRPT1

*tRNA phosphotransferase 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.65× (z +4.0, q 0.030, up in 21 of 42 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change.
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.358× (z -11.7, q 5e-29, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT22]] (+0.81, fdr 7e-06, ⚠ same locus), [[MPG]] (+0.80, fdr 7e-06), [[CIB1]] (+0.77, fdr 7e-06), [[MEA1]] (+0.74, fdr 7e-06); moves opposite to [[EWSR1]] (-0.72, fdr 2e-05), [[FUBP1]] (-0.70, fdr 3e-05), [[ZMYND11]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IL1RAP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.65×** | +4.0 | 0.030 | 21/42 (RPMI-7951, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.54× | +3.5 | 0.13 | 21/46 (LOX-IMVI, SW1417, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.358×** | -11.7 | 5e-29 | 41/46 (RPMI-7951, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.322×** | -9.2 | 1e-17 | 40/43 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.391×** | -7.6 | 7e-12 | 43/47 (H4, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.398×** | -7.4 | 1e-11 | 40/47 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -5.8 | 7e-07 | 36/45 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -5.1 | 4e-05 | 28/46 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.251×** | -4.5 | 5e-04 | 34/46 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.275×** | -4.2 | 0.002 | 26/41 (NCI-H23, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -4.1 | 0.003 | 25/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.594×** | -4.0 | 0.004 | 25/43 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -3.7 | 0.011 | 19/43 (HS-578T, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.629×** | -3.5 | 0.019 | 20/47 (BT-474, RPMI-7951, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.633×** | -3.4 | 0.028 | 18/47 (HEC-1-A, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -3.3 | 0.036 | 18/46 (NCI-H2030, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.750×** | -3.2 | 0.051 | 14/47 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.664×** | -3.1 | 0.075 | 10/47 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 16.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0214× (z -17.8) |
| [[A-427 (line)]] | wt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -8.7) |
| [[C-33 A (line)]] | alt | 7.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -8.5) |
| [[COLO 205 (line)]] | alt | 7.36 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0497× (z -9.9) |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -10.8) |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 8.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -9.9) |
| [[LoVo (line)]] | wt | 7.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 9.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.130× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 9.20 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 8.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 5.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0840× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 6.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0536× (z -10.5) |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM 0.0581× (z -9.4) |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0550× (z -11.9) |
| [[A-172 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT22]] | +0.81 | +0.67 / +0.85 | both halves | 7e-06 | STRING 862; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MPG]] | +0.80 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[CIB1]] | +0.77 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MEA1]] | +0.74 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.72 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[DDT]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[OCEL1]] | +0.71 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[FAM89B]] | +0.71 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 | STRING 434 |
| [[SH3GL1]] | +0.71 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CIAO2B]] | +0.70 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[METTL26]] | +0.69 | +0.70 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | -0.72 | -0.47 / -0.74 | both halves | 2e-05 |  |
| [[FUBP1]] | -0.70 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[ZMYND11]] | -0.66 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.64 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SRSF10]] | -0.64 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.64 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.63 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[SFPQ]] | -0.63 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[IQCH-AS1]] | -0.63 | -0.62 / -0.37 | both halves | 9e-05 |  |
| [[FGF2]] | -0.63 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RAP]] | B | IL1RAP activity raises TRPT1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without IL1RAP | 0.036 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[TSTD1]] | B | TSTD1 activity raises TRPT1's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without TSTD1 | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.0, -12.9); signed map (-30.9, 14.1). **Vector** length 71.3, 16.3% of its response variance represented; |z| ≥ 3 in 716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.8 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +0.9 | +1.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +0.9 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -11.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | tRNA phosphotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,223,799-64,226,254 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11134 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TN4](https://www.uniprot.org/uniprotkb/Q86TN4) (tRNA 2'-phosphotransferase 1):

> Catalyzes the last step of tRNA splicing, the transfer of the splice junction 2'-phosphate from ligated tRNA to NAD to produce ADP-ribose 1''-2'' cyclic phosphate.

**Summary**, from NCBI Gene [83707](https://www.ncbi.nlm.nih.gov/gene/83707):

> Predicted to enable tRNA 2'-phosphotransferase activity. Predicted to be involved in tRNA splicing, via endonucleolytic cleavage and ligation. Predicted to act upstream of or within regulation of protein kinase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20316) · Entrez [83707](https://www.ncbi.nlm.nih.gov/gene/83707) · UniProt [Q86TN4](https://www.uniprot.org/uniprotkb/Q86TN4) · Ensembl [ENSG00000149743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149743)

## Data

Gene col 7405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7405); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7405]; `tensor/DDL_lfc|DDL_z.npy` [7405]; `embed/gene_vectors.npy` [7405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7405 or target_col == 7405). Every well: [[TRPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
