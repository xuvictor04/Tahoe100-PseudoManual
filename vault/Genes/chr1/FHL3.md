---
symbol: "FHL3"
type: "gene"
col: 11397
ensembl_id: "ENSG00000183386"
name: "four and a half LIM domains 3"
location: "1p34.3"
module: 11
arm: "+"
pooled_cpm: 6.25
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# FHL3

*four and a half LIM domains 3* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.63× (z +10.3, q 6e-22, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.581× (z -6.3, q 2e-07, down in 26 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP27X]] (+0.59, fdr 3e-05), [[ZNF829]] (+0.58, fdr 1e-05), [[CRCP]] (+0.57, fdr 1e-05); moves opposite to [[CALM3]] (-0.55, fdr 2e-05), [[TMED4]] (-0.55, fdr 1e-05), [[CDON]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARHGAP40]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.63×** | +10.3 | 6e-22 | 38/41 (SW480, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.8 | 4e-16 | 25/36 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +8.6 | 2e-15 | 25/40 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.3 | 4e-08 | 23/41 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.9 | 1e-04 | 16/37 (CFPAC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.4 | 0.001 | 3/44 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.022 | 9/42 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.030 | 4/39 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.037 | 9/41 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.038 | 10/39 (LS 180, SW480, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.33×** | +3.3 | 0.049 | 2/42 (SW480, NCI-H1792) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.066 | 7/43 (LOX-IMVI, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | 1.30× | +3.0 | 0.11 | 6/42 (HCT15, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.581×** | -6.3 | 2e-07 | 26/42 (MIA PaCa-2, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.589×** | -5.7 | 4e-06 | 21/43 (MIA PaCa-2, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -5.2 | 4e-05 | 19/39 (HOP62, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.691×** | -4.1 | 0.005 | 14/41 (CFPAC-1, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.707×** | -3.7 | 0.023 | 15/43 (NCI-H2030, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.746×** | -3.5 | 0.041 | 8/44 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.742×** | -3.5 | 0.041 | 10/43 (C-33 A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.738×** | -3.3 | 0.078 | 10/43 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.828× | -3.1 | 0.11 | 10/43 (RKO, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.167× (z -8.7) |
| [[LoVo (line)]] | wt | 3.83 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0887× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0751× (z -9.1) |
| [[A-172 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP27X]] | +0.59 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[ZNF829]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CRCP]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TRIM47]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[RBMXL1]] | +0.54 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[FNTA]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[IRX3]] | +0.53 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[UTP3]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[GLRX2]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[SH3TC1]] | +0.53 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ANGPT2]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALM3]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TMED4]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CDON]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CBX1]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RCN2]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ATP6AP2]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PTMA]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CALR]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[TDP1]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[USP48]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[EOLA2]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CA5B]] | -0.49 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP40]] | B | ARHGAP40 activity raises FHL3's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 1.43× lower at baseline in the lines without ARHGAP40 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[MT1E]] | B | MT1E activity raises FHL3's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.41× lower at baseline in the lines without MT1E | 0.073 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[HDAC6]] | B | HDAC6 activity raises FHL3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CMTM3]] | B | CMTM3 activity raises FHL3's level | lines that do not express CMTM3 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without CMTM3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF605, C2orf74, MAP1B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.545). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.0, 8.1); signed map (1.3, -23.5). **Vector** length 70.0, 12.2% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +6.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.8 | +1.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | four and a half LIM domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,996,770-38,005,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLIM2 |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13643](https://www.uniprot.org/uniprotkb/Q13643) (Four and a half LIM domains protein 3):

> Recruited by SOX15 to FOXK1 promoters where it acts as a transcriptional coactivator of FOXK1.

**Summary**, from NCBI Gene [2275](https://www.ncbi.nlm.nih.gov/gene/2275):

> The protein encoded by this gene is a member of a family of proteins containing a four-and-a-half LIM domain, which is a highly conserved double zinc finger motif. The encoded protein has been shown to interact with the cancer developmental regulators SMAD2, SMAD3, and SMAD4, the skeletal muscle myogenesis protein MyoD, and the high-affinity IgE beta chain regulator MZF-1. This protein may be involved in tumor suppression, repression of MyoD expression, and repression of IgE receptor …

**Accessions** — [HGNC:3704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3704) · Entrez [2275](https://www.ncbi.nlm.nih.gov/gene/2275) · UniProt [Q13643](https://www.uniprot.org/uniprotkb/Q13643) · Ensembl [ENSG00000183386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183386)

## Data

Gene col 11397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11397); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11397]; `tensor/DDL_lfc|DDL_z.npy` [11397]; `embed/gene_vectors.npy` [11397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11397 or target_col == 11397). Every well: [[FHL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
