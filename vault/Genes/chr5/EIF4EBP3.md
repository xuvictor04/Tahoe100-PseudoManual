---
symbol: "EIF4EBP3"
type: "gene"
col: 14338
ensembl_id: "ENSG00000243056"
name: "eukaryotic translation initiation factor 4E binding protein 3"
location: "5q31.3"
module: 68
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# EIF4EBP3

*eukaryotic translation initiation factor 4E binding protein 3* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +8.8, q 1e-15, up in 26 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.515× (z -4.1, q 0.024, down in 16 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 5 µM in 1 line (KATO III 0.0498×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKHD1-EIF4EBP3]] (+0.78, fdr 7e-06, ⚠ same locus), [[LINC02307]] (+0.75, fdr 7e-06), [[WASHC1]] (+0.75, fdr 7e-06), [[CDK3]] (+0.74, fdr 7e-06); moves opposite to [[NOMO2]] (-0.66, fdr 7e-06), [[RPA1]] (-0.66, fdr 1e-05), [[SKP2]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +8.8 | 1e-15 | 26/30 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.3 | 1e-07 | 20/28 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +5.6 | 3e-06 | 12/25 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +5.3 | 2e-05 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +5.2 | 2e-05 | 7/13 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.13×** | +4.9 | 9e-05 | 5/8 (NCI-H2030, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +4.7 | 2e-04 | 19/37 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +3.9 | 0.007 | 11/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.007 | 10/31 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.62×** | +3.1 | 0.097 | 6/42 (HOP62, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +3.1 | 0.097 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14338.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 5 µM in 1 line (KATO III 0.0498×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -4.1 | 0.024 | 16/39 (NCI-H1573, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.358× | -3.5 | 0.13 | 8/26 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 5.78 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0498× (z -10.5) |
| [[A-172 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.592 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKHD1-EIF4EBP3]] | +0.78 | +0.82 / +0.65 | both halves | 7e-06 | STRING 914; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02307]] | +0.75 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[CDK3]] | +0.74 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[RSF1]] | +0.72 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[BOLA1]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[GUCY2C-AS1]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[SPATC1]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[C11orf71]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[NKAPD1]] | +0.68 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[N4BP2L1]] | +0.67 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[BPTF]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | -0.66 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RPA1]] | -0.66 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[SKP2]] | -0.66 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.66 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.66 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[NUDT21]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.65 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[SDHA]] | -0.64 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[STRAP]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TMED7]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[STIMATE]] | -0.63 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[COLGALT1]] | -0.63 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EIF4EBP3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (23.4, -8.6); signed map (2.7, -11.2). **Vector** length 48.4, 6.78% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,547,662-140,549,576 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 4E-BP3 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60516](https://www.uniprot.org/uniprotkb/O60516) (Eukaryotic translation initiation factor 4E-binding protein 3):

> Repressor of translation initiation that regulates EIF4E activity by preventing its assembly into the eIF4F complex: the hypophosphorylated form competes with EIF4G1/EIF4G3 and strongly binds to EIF4E, leading to repression of translation. In contrast, the hyperphosphorylated form dissociates from EIF4E, allowing interaction between EIF4G1/EIF4G3 and EIF4E, leading to initiation of translation (By similarity). Inhibits EIF4E-mediated mRNA nuclear export.

**Summary**, from NCBI Gene [8637](https://www.ncbi.nlm.nih.gov/gene/8637):

> This gene encodes a member of the EIF4EBP family, which consists of proteins that bind to eukaryotic translation initiation factor 4E and regulate its assembly into EIF4F, the multi-subunit translation initiation factor that recognizes the mRNA cap structure. Read-through transcription from the neighboring upstream gene (MASK or ANKHD1) generates a transcript (MASK-BP3) that encodes a protein comprised of the MASK protein sequence for the majority of the protein and a different C-terminus due …

**Accessions** — [HGNC:3290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3290) · Entrez [8637](https://www.ncbi.nlm.nih.gov/gene/8637) · UniProt [O60516](https://www.uniprot.org/uniprotkb/O60516) · Ensembl [ENSG00000243056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243056)

## Data

Gene col 14338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14338); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14338]; `tensor/DDL_lfc|DDL_z.npy` [14338]; `embed/gene_vectors.npy` [14338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14338 or target_col == 14338). Every well: [[EIF4EBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4EBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
