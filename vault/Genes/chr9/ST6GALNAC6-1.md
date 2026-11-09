---
symbol: "ST6GALNAC6-1"
type: "gene"
col: 15047
ensembl_id: "ENSG00000257524"
name: ""
location: ""
module: 38
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ST6GALNAC6-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.72× (z +8.2, q 2e-13, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.60× (z +4.0, q 0.008, up in 8 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.439× (z -6.8, q 6e-09, down in 21 of 39 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.498× (z -6.0, q 4e-07, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6]] (+0.73, fdr 7e-06, ⚠ same locus), [[FPGS]] (+0.72, fdr 7e-06), [[PIP5KL1]] (+0.70, fdr 8e-06, ⚠ same locus), [[RSKR]] (+0.69, fdr 7e-06), [[TFAP2E]] (+0.67, fdr 1e-05); moves opposite to [[CGGBP1]] (-0.65, fdr 1e-05), [[CASD1]] (-0.63, fdr 1e-05), [[HMGN2]] (-0.63, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATAD3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +8.2 | 2e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.4 | 0.002 | 3/10 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.3 | 0.002 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.3 | 0.002 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.008 | 8/21 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.081 | 8/42 (HCT15, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.45× | +3.2 | 0.12 | 5/44 (RKO, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.15 | 4/23 (A549, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.439×** | -6.8 | 6e-09 | 21/39 (A498, BT-474, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.594×** | -6.3 | 7e-08 | 17/32 (BT-474, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -6.0 | 4e-07 | 20/45 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.594×** | -4.5 | 0.001 | 13/40 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.605×** | -4.3 | 0.002 | 7/18 (PANC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -4.1 | 0.004 | 15/34 (A498, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -4.0 | 0.004 | 16/40 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -4.0 | 0.004 | 16/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.645×** | -3.6 | 0.017 | 9/29 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.774×** | -3.1 | 0.094 | 5/45 (C-33 A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Eplerenone (drug)]] 0.05 µM |  | 0.681× | -3.1 | 0.10 | 5/36 (NCI-H2347, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.702× | -3.1 | 0.10 | 17/29 (SW480, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 6.11 | 0 | 1 | — | [[Celecoxib (drug)]] 0.05 µM 0.0785× (z -9.1) |
| [[SW480 (line)]] | alt | 1.36 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0647× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.590 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | +0.73 | +0.67 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[FPGS]] | +0.72 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PIP5KL1]] | +0.70 | +0.57 / +0.71 | both halves | 8e-06 | ⚠ same locus (14.9 kb, same strand: neighbours can correlate without regulation) |
| [[RSKR]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TFAP2E]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.66 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[SLC27A5]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[HYAL1]] | +0.65 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[DRD4]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SYCE1L]] | +0.63 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[KBTBD11-OT1-1]] | +0.63 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[RBAK-RBAKDN]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PFDN2]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.65 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[CASD1]] | -0.63 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[HMGN2]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.62 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ARMT1]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[DECR1]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TAF9B]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[STXBP3]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CILK1]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[STX17]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MED12]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TIA1]] | -0.54 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD3C]] | B | ATAD3C activity lowers ST6GALNAC6-1's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.27× higher at baseline in the lines without ATAD3C | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, -21.6); signed map (-45.8, -2.6). **Vector** length 50.8, 6.52% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +1.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.2 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -6.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.3 | -1.1 |

## What is on record

> [!warning] No registry record
> ST6GALNAC6-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15047); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15047]; `tensor/DDL_lfc|DDL_z.npy` [15047]; `embed/gene_vectors.npy` [15047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15047 or target_col == 15047). Every well: [[ST6GALNAC6-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GALNAC6-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
