---
symbol: "APOC1"
type: "gene"
col: 5035
ensembl_id: "ENSG00000130208"
name: "apolipoprotein C1"
location: "19q13.32"
module: 24
arm: "+"
pooled_cpm: 4.64
n_lines_expressing: 33
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# APOC1

*apolipoprotein C1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.97× (z +9.7, q 3e-19, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +7.1, q 2e-10, up in 14 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM27]] (+0.79, fdr 7e-06), [[CEP164P1]] (+0.78, fdr 1e-05), [[ZNF232-AS1]] (+0.76, fdr 1e-05); moves opposite to [[AKAP11]] (-0.65, fdr 1e-05), [[LIN7C]] (-0.64, fdr 1e-05), [[FARSB]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[RPS19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.97×** | +9.7 | 3e-19 | 11/12 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.92×** | +8.5 | 6e-15 | 7/9 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +7.1 | 2e-10 | 14/21 (NCI-H2347, A549, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.90×** | +6.3 | 6e-08 | 8/10 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +5.3 | 1e-05 | 13/19 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +3.9 | 0.008 | 9/13 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.6 | 0.022 | 7/18 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **2.00×** | +3.4 | 0.043 | 6/14 (NCI-H2030, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.3 | 0.053 | 7/20 (NCI-H23, J82, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.75× | +3.0 | 0.14 | 2/18 (MIA PaCa-2, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5035.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.488× | -3.3 | 0.50 | 12/30 (LoVo, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.9) |
| [[A-172 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 126 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | +0.79 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[CEP164P1]] | +0.78 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[ZNF232-AS1]] | +0.76 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[RN7SL2]] | +0.75 | +0.57 / +0.75 | both halves | 9e-06 |  |
| [[CTBP1-AS]] ⚠ | +0.73 | +0.46 / +0.74 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RHOQ-AS1]] | +0.73 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.73 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.73 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[APOE]] | +0.72 | +0.56 / +0.70 | both halves | 1e-05 | same gene group; pathway: NR1H2 and NR1H3-mediated signaling; STRING 999; ⚠ same locus (4.9 kb, same strand: neighbours can correlate without regulation) |
| [[EFCAB14-AS1]] | +0.72 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.72 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[NDUFA1]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[HIGD2A]] | +0.71 | +0.52 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.65 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.64 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[FARSB]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NUP188]] | -0.62 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[OCRL]] | -0.61 | -0.40 / -0.62 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS19]] | B | APOC1 activity raises RPS19's level | lines that do not express APOC1 (17) vs lines expressing it (33) | 1.33× lower at baseline in the lines without APOC1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, MAP3K15 |
| [[AKAP11]] | B | APOC1 activity lowers AKAP11's level | lines that do not express APOC1 (17) vs lines expressing it (33) | 1.28× higher at baseline in the lines without APOC1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, MAP3K15 |
| [[MED4]] | B | APOC1 activity lowers MED4's level | lines that do not express APOC1 (17) vs lines expressing it (33) | 1.19× higher at baseline in the lines without APOC1 | 0.090 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, MAP3K15 |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.4, -22.5); signed map (-29.2, 7.7). **Vector** length 37.1, 6.63% of its response variance represented; |z| ≥ 3 in 416 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,914,247-44,919,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Apo-CI, ApoC-I, apo-CIB, apoC-IB, APOC1B |
| Gene groups (HGNC) | Apolipoproteins |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Reactome | 9 pathways, smallest: VLDL assembly; VLDL clearance; Plasma lipoprotein assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P02654](https://www.uniprot.org/uniprotkb/P02654) (Apolipoprotein C-I):

> Inhibitor of lipoprotein binding to the low density lipoprotein (LDL) receptor, LDL receptor-related protein, and very low density lipoprotein (VLDL) receptor. Associates with high density lipoproteins (HDL) and the triacylglycerol-rich lipoproteins in the plasma and makes up about 10% of the protein of the VLDL and 2% of that of HDL. Appears to interfere directly with fatty acid uptake and is also the major plasma inhibitor of cholesteryl ester transfer protein (CETP). Binds free fatty acids …

**Summary**, from NCBI Gene [341](https://www.ncbi.nlm.nih.gov/gene/341):

> This gene encodes a member of the apolipoprotein C1 family. This gene is expressed primarily in the liver, and it is activated when monocytes differentiate into macrophages. The encoded protein plays a central role in high density lipoprotein (HDL) and very low density lipoprotein (VLDL) metabolism. This protein has also been shown to inhibit cholesteryl ester transfer protein in plasma. A pseudogene of this gene is located 4 kb downstream in the same orientation, on the same chromosome. This …

**Accessions** — [HGNC:607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:607) · Entrez [341](https://www.ncbi.nlm.nih.gov/gene/341) · UniProt [P02654](https://www.uniprot.org/uniprotkb/P02654) · Ensembl [ENSG00000130208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130208)

## Data

Gene col 5035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5035); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5035]; `tensor/DDL_lfc|DDL_z.npy` [5035]; `embed/gene_vectors.npy` [5035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5035 or target_col == 5035). Every well: [[APOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
