---
symbol: "PIGBOS1"
type: "gene"
col: 13501
ensembl_id: "ENSG00000225973"
name: "PIGB opposite strand 1"
location: "15q21.3"
module: 12
arm: "+"
pooled_cpm: 8.75
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PIGBOS1

*PIGB opposite strand 1* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.57× (z +3.9, q 0.063, up in 15 of 39 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.572× (z -4.8, q 7e-04, down in 23 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.675× (z -4.7, q 7e-04, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS18B]] (+0.79, fdr 7e-06), [[MRPS18C]] (+0.76, fdr 7e-06), [[SEC62]] (+0.76, fdr 7e-06); moves opposite to [[AKT1]] (-0.73, fdr 7e-06), [[DHFR]] (-0.70, fdr 1e-05), [[RPSA]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.57×** | +3.9 | 0.063 | 15/39 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.47× | +3.2 | 0.38 | 3/17 (NCI-H2347, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.43× | +3.1 | 0.38 | 12/46 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.572×** | -4.8 | 7e-04 | 23/47 (SW 900, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -4.7 | 7e-04 | 27/43 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.363×** | -4.5 | 0.001 | 24/45 (COLO 205, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.656×** | -3.6 | 0.047 | 23/47 (RPMI-7951, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.660×** | -3.5 | 0.047 | 20/47 (SNU-423, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.652×** | -3.4 | 0.075 | 16/26 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -3.3 | 0.087 | 18/46 (NCI-H1792, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | 0.678× | -3.2 | 0.11 | 19/45 (SNU-1, NCI-H23, …) | top dose only | position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.769× | -3.1 | 0.11 | 8/48 (HT-29, A549, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.698× | -3.1 | 0.13 | 19/47 (NCI-H460, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 6.87 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -9.0) |
| [[Hs 766T (line)]] | wt | 6.62 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0994× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18B]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[SEC62]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.75 | +0.52 / +0.81 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COIL]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[PPIG]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[NKAP]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.72 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.72 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[EID2]] | +0.71 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TMEM70]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[PHAX]] | +0.71 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.71 | +0.54 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.73 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[DHFR]] | -0.70 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[RPSA]] | -0.70 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.69 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.69 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[COLGALT1]] | -0.67 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[BPNT2]] | -0.66 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[RPL10]] | -0.66 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[CTSZ]] | -0.66 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[ARHGAP4]] | -0.66 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[PRPS2]] | -0.65 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | -0.65 | -0.61 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PIGBOS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.4, 1.6); signed map (-12.1, -5.2). **Vector** length 65.6, 12.3% of its response variance represented; |z| ≥ 3 in 622 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.3 | +1.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PIGB opposite strand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,317,184-55,319,161 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A0B4J2F0](https://www.uniprot.org/uniprotkb/A0A0B4J2F0) (Protein PIGBOS1):

> Plays a role in regulation of the unfolded protein response triggered by endoplasmic reticulum (ER) stress resulting from the presence of unfolded proteins in the ER lumen.

**Summary**, from NCBI Gene [101928527](https://www.ncbi.nlm.nih.gov/gene/101928527):

> Involved in regulation of endoplasmic reticulum unfolded protein response. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:50696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50696) · Entrez [101928527](https://www.ncbi.nlm.nih.gov/gene/101928527) · UniProt [A0A0B4J2F0](https://www.uniprot.org/uniprotkb/A0A0B4J2F0) · Ensembl [ENSG00000225973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225973)

## Data

Gene col 13501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13501); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13501]; `tensor/DDL_lfc|DDL_z.npy` [13501]; `embed/gene_vectors.npy` [13501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13501 or target_col == 13501). Every well: [[PIGBOS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGBOS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
