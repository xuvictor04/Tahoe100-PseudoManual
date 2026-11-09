---
symbol: "MAGEA4"
type: "gene"
col: 7174
ensembl_id: "ENSG00000147381"
name: "MAGE family member A4"
location: "Xq28"
module: 158
arm: "+"
pooled_cpm: 14.47
n_lines_expressing: 9
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 14
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# MAGEA4

*MAGE family member A4* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +9.3, q 7e-18, up in 6 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.44× (z +3.7, q 0.031, up in 0 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGEA10]] (+0.53, fdr 3e-05), [[ACP7]] (+0.51, fdr 4e-05), [[SCG2]] (+0.50, fdr 3e-05); moves opposite to [[ADD1]] (-0.40, fdr 2e-04), [[USP33]] (-0.40, fdr 3e-04), [[ARL6IP5]] (-0.38, fdr 0.001, ⚠ not reproduced), [[SEC61A2]] (-0.37, fdr 2e-04).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 14 go from it, the strongest it → [[RBMXL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +9.3 | 7e-18 | 6/7 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +6.8 | 2e-09 | 1/6 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +6.7 | 3e-09 | 2/6 (SHP-77, NCI-H1573) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.44×** | +3.7 | 0.031 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.69×** | +3.6 | 0.031 | 2/7 (A-427, AN3 CA) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 0.5 µM |  | 1.59× | +3.2 | 0.11 | 0/7 | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.59× | +3.2 | 0.11 | 0/7 | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 2.15× | +3.1 | 0.11 | 7/7 (SHP-77, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | 1.57× | +3.1 | 0.11 | 0/7 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Futibatinib (drug)]] 0.05 µM |  | 0.589× | -3.5 | 0.22 | 0/7 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.591× | -3.4 | 0.22 | 0/7 | inconsistent across doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.613× | -3.1 | 0.22 | 0/7 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.636× | -3.1 | 0.22 | 0/7 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.618× | -3.1 | 0.22 | 3/7 (NCI-H23, SW 1271, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.605× | -3.0 | 0.22 | 3/7 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 183 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEA10]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 | same gene group; STRING 863 |
| [[ACP7]] | +0.51 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[SCG2]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[MAGEB2]] | +0.49 | +0.42 / +0.56 | both halves | 4e-05 | same gene group |
| [[TAFA5]] | +0.49 | +0.34 / +0.35 | both halves | 1e-04 |  |
| [[GCG]] | +0.49 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[MAGEA4-AS1]] | +0.47 | +0.45 / +0.51 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MARCHF4]] | +0.47 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[ASTL]] | +0.47 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[RBMXL1]] | +0.46 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[DAW1]] | +0.46 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PWP2]] | +0.45 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[LINC01010]] | +0.45 | +0.48 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADD1]] | -0.40 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[USP33]] | -0.40 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[ARL6IP5]] | -0.38 | -0.38 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[SEC61A2]] | -0.37 | -0.30 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBMXL1]] | B | MAGEA4 activity raises RBMXL1's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.15× lower at baseline in the lines without MAGEA4 | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[ZNF121]] | B | MAGEA4 activity raises ZNF121's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.23× lower at baseline in the lines without MAGEA4 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[UTP3]] | B | MAGEA4 activity raises UTP3's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.22× lower at baseline in the lines without MAGEA4 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[COA4]] | B | MAGEA4 activity raises COA4's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.35× lower at baseline in the lines without MAGEA4 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[WDR55]] | B | MAGEA4 activity raises WDR55's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.12× lower at baseline in the lines without MAGEA4 | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[RAPGEF6]] | B | MAGEA4 activity raises RAPGEF6's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.22× lower at baseline in the lines without MAGEA4 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[MYOM1]] | B | MAGEA4, [[MAGEA4-AS1]] activity raises MYOM1's level | lines that do not express MAGEA4, MAGEA4-AS1 (41) vs lines expressing them (9) | 2.69× lower at baseline in the lines without MAGEA4, MAGEA4-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, GCG; co-absent genes |
| [[ARL6IP5]] | B | MAGEA4 activity lowers ARL6IP5's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.77× higher at baseline in the lines without MAGEA4 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[TRMT10C]] | B | MAGEA4 activity raises TRMT10C's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.29× lower at baseline in the lines without MAGEA4 | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[GNG4]] | B | MAGEA4 activity raises GNG4's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 3.41× lower at baseline in the lines without MAGEA4 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[SLC6A17]] | C | MAGEA4 activity raises SLC6A17's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 3.45× lower at baseline in the lines without MAGEA4 | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG; co-absent with the target |
| [[LINC01010]] | C | MAGEA4 activity raises LINC01010's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 2.01× lower at baseline in the lines without MAGEA4 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.5, 16.9); signed map (30.1, 34.3). **Vector** length 19.1, 6.51% of its response variance represented; |z| ≥ 3 in 75 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.1 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +6.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.5 | +3.1 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +0.4 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.4 | +3.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | +0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.5 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.5 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:151,912,495-151,925,171 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAGE4A, MAGE4B, MAGE-41, MAGE-X2, MGC21336, CT1.4; previously MAGE4 |
| Gene groups (HGNC) | MAGE family |
| Matched by | ensembl_id |

**Function**, from UniProt [P43358](https://www.uniprot.org/uniprotkb/P43358) (Melanoma-associated antigen 4):

> Regulates cell proliferation through the inhibition of cell cycle arrest at the G1 phase. Also negatively regulates p53-mediated apoptosis.

**Summary**, from NCBI Gene [4103](https://www.ncbi.nlm.nih.gov/gene/4103):

> This gene is a member of the MAGEA gene family. The members of this family encode proteins with 50 to 80% sequence identity to each other. The promoters and first exons of the MAGEA genes show considerable variability, suggesting that the existence of this gene family enables the same function to be expressed under different transcriptional controls. The MAGEA genes are clustered at chromosomal location Xq28. They have been implicated in some hereditary disorders, such as dyskeratosis …

**Accessions** — [HGNC:6802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6802) · Entrez [4103](https://www.ncbi.nlm.nih.gov/gene/4103) · UniProt [P43358](https://www.uniprot.org/uniprotkb/P43358) · Ensembl [ENSG00000147381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147381)

## Data

Gene col 7174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7174); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7174]; `tensor/DDL_lfc|DDL_z.npy` [7174]; `embed/gene_vectors.npy` [7174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7174 or target_col == 7174). Every well: [[MAGEA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
