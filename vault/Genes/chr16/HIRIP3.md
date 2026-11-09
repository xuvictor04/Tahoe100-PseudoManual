---
symbol: "HIRIP3"
type: "gene"
col: 7418
ensembl_id: "ENSG00000149929"
name: "HIRA interacting protein 3"
location: "16p11.2"
module: 91
arm: "+"
pooled_cpm: 12.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# HIRIP3

*HIRA interacting protein 3* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.58× (z +8.0, q 7e-13, up in 31 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +6.6, q 5e-09, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.411× (z -7.5, q 3e-11, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REXO5]] (+0.70, fdr 7e-06), [[USP1]] (+0.66, fdr 9e-06), [[PAGR1]] (+0.65, fdr 9e-06); moves opposite to [[FTL]] (-0.56, fdr 1e-05), [[TXN]] (-0.53, fdr 1e-05), [[RPL27A]] (-0.52, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF724]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.58×** | +8.0 | 7e-13 | 31/35 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.65×** | +7.9 | 7e-13 | 16/19 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +7.1 | 2e-10 | 37/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +6.6 | 5e-09 | 31/45 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.91×** | +5.3 | 2e-05 | 31/46 (NCI-H1573, LoVo, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.94×** | +5.2 | 2e-05 | 19/28 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.92×** | +5.1 | 3e-05 | 29/44 (SW480, PANC-1, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +4.9 | 8e-05 | 29/46 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.78×** | +4.8 | 8e-05 | 27/47 (PANC-1, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.63×** | +4.1 | 0.002 | 22/40 (HS-578T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.036 | 14/47 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.3 | 0.053 | 17/45 (LoVo, NCI-H1573, …) | all doses, flat | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.31×** | +3.1 | 0.076 | 15/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.092 | 14/47 (KATO III, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.411×** | -7.5 | 3e-11 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.443×** | -6.9 | 2e-09 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.460×** | -6.6 | 9e-09 | 38/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -5.4 | 8e-06 | 30/45 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.510×** | -5.4 | 8e-06 | 33/47 (LS 180, SW480, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.559×** | -4.9 | 8e-05 | 24/47 (LoVo, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.613×** | -4.1 | 0.003 | 26/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -3.7 | 0.018 | 19/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.557×** | -3.5 | 0.025 | 19/48 (HEC-1-A, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.667×** | -3.4 | 0.035 | 18/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.692×** | -3.1 | 0.095 | 17/47 (SW1417, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.8) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[HepG2_C3A (line)]] | wt | 8.28 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0716× (z -8.6) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 6.70 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0492× (z -11.4) |
| [[LS 180 (line)]] | wt | 9.03 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.193× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 9.20 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.139× (z -10.1) |
| [[SW480 (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.5) | — |
| [[A-172 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REXO5]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[USP1]] | +0.66 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[PAGR1]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 | STRING 704 |
| [[SMC2]] | +0.65 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[MDC1]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[SPDL1]] | +0.62 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[XRCC1]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[DCLRE1A]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[EME1]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZNF724]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CETN3]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTL]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TXN]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RPL27A]] | -0.52 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[RPL39]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SNX3]] | -0.50 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[LSP1P5-1]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF724]] | B | ZNF724 activity raises HIRIP3's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without ZNF724 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.3, -44.7); signed map (-45.3, -49.6). **Vector** length 89.0, 20.6% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.53 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.53 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.5 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +5.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -6.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HIRA interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,992,330-29,996,074 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW71](https://www.uniprot.org/uniprotkb/Q9BW71) (HIRA-interacting protein 3):

> Histone chaperone that carries a H2A-H2B histone complex and facilitates its deposition onto chromatin.

**Summary**, from NCBI Gene [8479](https://www.ncbi.nlm.nih.gov/gene/8479):

> The HIRA protein shares sequence similarity with Hir1p and Hir2p, the two corepressors of histone gene transcription characterized in the yeast, Saccharomyces cerevisiae. The structural features of the HIRA protein suggest that it may function as part of a multiprotein complex. Several cDNAs encoding HIRA-interacting proteins, or HIRIPs, have been identified. In vitro, the protein encoded by this gene binds HIRA, as well as H2B and H3 core histones, indicating that a complex containing …

**Accessions** — [HGNC:4917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4917) · Entrez [8479](https://www.ncbi.nlm.nih.gov/gene/8479) · UniProt [Q9BW71](https://www.uniprot.org/uniprotkb/Q9BW71) · Ensembl [ENSG00000149929](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149929)

## Data

Gene col 7418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7418); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7418]; `tensor/DDL_lfc|DDL_z.npy` [7418]; `embed/gene_vectors.npy` [7418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7418 or target_col == 7418). Every well: [[HIRIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIRIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
