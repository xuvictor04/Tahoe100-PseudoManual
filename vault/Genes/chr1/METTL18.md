---
symbol: "METTL18"
type: "gene"
col: 10164
ensembl_id: "ENSG00000171806"
name: "methyltransferase 18, RPL3 N3(tau)-histidine"
location: "1q24.2"
module: 11
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# METTL18

*methyltransferase 18, RPL3 N3(tau)-histidine* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +13.3, q 7e-38, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.522× (z -5.6, q 1e-05, down in 18 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM200A]] (+0.85, fdr 7e-06), [[ARL14EP]] (+0.83, fdr 7e-06), [[ZNF620]] (+0.83, fdr 7e-06); moves opposite to [[AP2A1]] (-0.71, fdr 7e-06), [[TCF3]] (-0.68, fdr 7e-06), [[MLEC]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +13.3 | 7e-38 | 29/32 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.37×** | +10.0 | 4e-21 | 31/41 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +8.9 | 9e-17 | 25/32 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.12×** | +6.4 | 2e-08 | 25/44 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.6 | 2e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.4 | 6e-06 | 8/44 (COLO 205, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.9 | 7e-05 | 2/15 (SW1417, HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +4.7 | 2e-04 | 13/40 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.1 | 0.003 | 4/12 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +3.9 | 0.006 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +3.9 | 0.006 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.522×** | -5.6 | 1e-05 | 18/42 (LS 180, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -4.8 | 4e-04 | 17/42 (SW480, CHP-212, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.645×** | -3.8 | 0.031 | 12/43 (SHP-77, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.045 | 11/45 (NCI-H460, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Baicalin (drug)]] 5 µM |  | 0.780× | -3.0 | 0.25 | 8/45 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.704× | -3.0 | 0.25 | 10/45 (RPMI-7951, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.21 | 0 | 1 | — | [[Ataluren (drug)]] 0.5 µM 0.0679× (z -8.5) |
| [[LoVo (line)]] | wt | 1.80 | 0 | 1 | — | [[(S)-Crizotinib (drug)]] 5 µM 0.0561× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 3.38 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0990× (z -9.6) |
| [[A-172 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | +0.85 | +0.85 / +0.76 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.83 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.83 | +0.83 / +0.72 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.81 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.79 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[SDSL]] | +0.78 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PEX12]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[ZNF155]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[FUNDC1]] | +0.78 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.78 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2A1]] | -0.71 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[TCF3]] | -0.68 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[MLEC]] | -0.67 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[SETD3]] | -0.67 | -0.69 / -0.57 | both halves | 1e-05 | same gene group; STRING 577 |
| [[ADIPOR1]] | -0.67 | -0.68 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises METTL18's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF429]] | B | ZNF429 activity raises METTL18's level | lines that do not express ZNF429 (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without ZNF429 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF724, ENSG00000283201, ZNF254 |
| [[PLPP3]] | B | PLPP3 activity raises METTL18's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 1.28× lower at baseline in the lines without PLPP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.834). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.9, 7.4); signed map (3.6, -21.1). **Vector** length 52.6, 7.12% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 18, RPL3 N3(tau)-histidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,792,529-169,794,963 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9084, AsTP2, HPM1; previously C1orf156 |
| Gene groups (HGNC) | 7BS protein methyltransferases; 7BS protein histidine methyltransferases; Histidine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95568](https://www.uniprot.org/uniprotkb/O95568) (Histidine protein methyltransferase 1 homolog):

> Protein-L-histidine N-tele-methyltransferase that specifically monomethylates RPL3, thereby regulating translation elongation. Histidine methylation of RPL3 regulates translation elongation by slowing ribosome traversal on tyrosine codons: slower elongation provides enough time for proper folding of synthesized proteins and prevents cellular aggregation of tyrosine-rich proteins.

**Summary**, from NCBI Gene [92342](https://www.ncbi.nlm.nih.gov/gene/92342):

> Enables heat shock protein binding activity and protein-L-histidine N-tele-methyltransferase activity. Involved in peptidyl-lysine monomethylation; regulation of gene expression; and regulation of ribosome biogenesis. Located in cytosol and nucleolus. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28793) · Entrez [92342](https://www.ncbi.nlm.nih.gov/gene/92342) · UniProt [O95568](https://www.uniprot.org/uniprotkb/O95568) · Ensembl [ENSG00000171806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171806)

## Data

Gene col 10164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10164); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10164]; `tensor/DDL_lfc|DDL_z.npy` [10164]; `embed/gene_vectors.npy` [10164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10164 or target_col == 10164). Every well: [[METTL18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
