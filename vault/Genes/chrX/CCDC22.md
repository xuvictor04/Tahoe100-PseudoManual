---
symbol: "CCDC22"
type: "gene"
col: 2200
ensembl_id: "ENSG00000101997"
name: "CCC complex scaffolding subunit CCDC22"
location: "Xp11.23"
module: 170
arm: "+"
pooled_cpm: 5.64
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# CCDC22

*CCC complex scaffolding subunit CCDC22* — Xp11.23

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.461× (z -9.4, q 2e-18, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL12]] (+0.74, fdr 7e-06), [[ADPRM]] (+0.65, fdr 1e-05), [[PRPSAP2]] (+0.57, fdr 3e-05); moves opposite to [[PPP3CA]] (-0.57, fdr 2e-05), [[PLPP2]] (-0.52, fdr 4e-05), [[MBNL1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.461×** | -9.4 | 2e-18 | 31/45 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.519×** | -8.0 | 4e-13 | 26/45 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.560×** | -7.1 | 3e-10 | 24/47 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -5.4 | 1e-05 | 19/42 (RKO, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -5.4 | 1e-05 | 18/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.651×** | -5.3 | 1e-05 | 19/40 (SNU-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -4.0 | 0.006 | 12/34 (C32, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.575×** | -3.5 | 0.029 | 9/43 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 7.05 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0787× (z -9.3) ⚠ toxic · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0997× (z -8.8) |
| [[RKO (line)]] | wt | 8.17 | 0 | 2 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0620× (z -10.9) |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -9.3) |
| [[A-172 (line)]] | wt | 5.01 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0656× (z -10.9) |
| [[A498 (line)]] | wt | 3.05 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0867× (z -9.8) |
| [[LS 180 (line)]] | wt | 4.57 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0565× (z -9.6) |
| [[A-427 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL12]] | +0.74 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[ADPRM]] | +0.65 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PRPSAP2]] | +0.57 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TATDN3]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF7]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PEX16]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NDUFB9]] | +0.56 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PARL]] | +0.56 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[TJAP1]] | +0.56 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[MRPS31]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[YJU2B]] | +0.55 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[AARSD1]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CA]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PLPP2]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MBNL1]] | -0.51 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ADAM10]] | -0.50 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[LRP11]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LBR]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[LAMP2]] | -0.47 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[TGOLN2]] | -0.47 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[WWC2]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TMEM30A]] | -0.46 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[MMGT1]] | -0.46 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[WWC3]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CCDC22's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-39.2, -11.5); signed map (-14.9, -3.6). **Vector** length 43.6, 4.67% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +0.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.9 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Busulfan (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | CCC complex scaffolding subunit CCDC22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,235,470-49,250,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JM1; previously CXorf37 |
| Gene groups (HGNC) | CCC complex; Centriolar satellite proteins |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60826](https://www.uniprot.org/uniprotkb/O60826) (Coiled-coil domain-containing protein 22):

> Component of the commander complex that is essential for endosomal recycling of transmembrane cargos; the Commander complex is composed of composed of the CCC subcomplex and the retriever subcomplex. Component of the CCC complex, which is involved in the regulation of endosomal recycling of surface proteins, including integrins, signaling receptor and channels. Involved in regulation of NF-kappa-B signaling. Promotes ubiquitination of I-kappa-B-kinase subunit IKBKB and its subsequent …

**Summary**, from NCBI Gene [28952](https://www.ncbi.nlm.nih.gov/gene/28952):

> This gene encodes a protein containing a coiled-coil domain. The encoded protein functions in the regulation of NF-kB (nuclear factor kappa-light-chain-enhancer of activated B cells) by interacting with COMMD (copper metabolism Murr1 domain-containing) proteins. The mouse orthologous protein has been shown to bind copines, which are calcium-dependent, membrane-binding proteins that may function in calcium signaling. This human gene has been identified as a novel candidate gene for syndromic …

**Accessions** — [HGNC:28909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28909) · Entrez [28952](https://www.ncbi.nlm.nih.gov/gene/28952) · UniProt [O60826](https://www.uniprot.org/uniprotkb/O60826) · Ensembl [ENSG00000101997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101997)

## Data

Gene col 2200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2200); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2200]; `tensor/DDL_lfc|DDL_z.npy` [2200]; `embed/gene_vectors.npy` [2200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2200 or target_col == 2200). Every well: [[CCDC22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
