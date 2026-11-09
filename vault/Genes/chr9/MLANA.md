---
symbol: "MLANA"
type: "gene"
col: 4166
ensembl_id: "ENSG00000120215"
name: "melan-A"
location: "9p24.1"
module: 21
arm: "+"
pooled_cpm: 2.2
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MLANA

*melan-A* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.20× (z +9.4, q 2e-18, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +7.7, q 2e-12, up in 14 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Diphenhydramine (drug)]] 0.05 µM: 0.536× (z -4.1, q 0.021, down in 6 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF7]] (+0.65, fdr 7e-06), [[DCT]] (+0.64, fdr 7e-06), [[SPATC1]] (+0.63, fdr 1e-05); moves opposite to [[TTLL12]] (-0.58, fdr 3e-05), [[RPE]] (-0.57, fdr 2e-05), [[PHF6]] (-0.56, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DCT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.20×** | +9.4 | 2e-18 | 2/2 (SK-MEL-2, C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +9.1 | 4e-17 | 4/4 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +8.6 | 2e-15 | 1/1 (C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +7.7 | 2e-12 | 14/21 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.68×** | +3.7 | 0.028 | 2/2 (SK-MEL-2, C32) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.4 | 0.067 | 1/4 (C32) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.3 | 0.074 | 1/10 (Hs 766T) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.097 | 2/8 (A498, Hs 766T) | inconsistent across doses | low cells (technical?) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.58× | +3.1 | 0.11 | 1/6 (SK-MEL-2) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.56× | +3.0 | 0.14 | 4/9 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.536×** | -4.1 | 0.021 | 6/39 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -3.9 | 0.031 | 15/37 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.618× | -3.2 | 0.28 | 7/44 (H4, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.656× | -3.0 | 0.36 | 6/41 (CFPAC-1, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.716 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.955 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.870 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.572 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.665 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.931 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF7]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[DCT]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 | pathway: MITF-M-dependent gene expression; STRING 921 |
| [[SPATC1]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[LINC00685]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.62 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[C3orf49]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SGCD]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.60 | +0.55 / +0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC02951]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.59 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[COL24A1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LRRN3]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL12]] | -0.58 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RPE]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PHF6]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SLC48A1]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[IDH3A]] | -0.56 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ALG10]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PGM2]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[APEH]] | -0.54 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[POLD2]] | -0.53 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ELMOD2]] | -0.53 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SIGMAR1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ICMT]] | -0.51 | -0.35 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCT]] | B | DCT activity raises MLANA's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.55× lower at baseline in the lines without DCT | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, 26.3); signed map (31.8, 6.8). **Vector** length 31.6, 3.15% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.0 | +2.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.0 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -0.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -3.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | melan-A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:5,890,889-5,910,606 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MART1, MART-1 |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in pigmentation; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16655](https://www.uniprot.org/uniprotkb/Q16655) (Melanoma antigen recognized by T-cells 1):

> Involved in melanosome biogenesis by ensuring the stability of GPR143. Plays a vital role in the expression, stability, trafficking, and processing of melanocyte protein PMEL, which is critical to the formation of stage II melanosomes.

**Summary**, from NCBI Gene [2315](https://www.ncbi.nlm.nih.gov/gene/2315):

> Located in endoplasmic reticulum membrane; melanosome; and trans-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7124) · Entrez [2315](https://www.ncbi.nlm.nih.gov/gene/2315) · UniProt [Q16655](https://www.uniprot.org/uniprotkb/Q16655) · Ensembl [ENSG00000120215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120215)

## Data

Gene col 4166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4166); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4166]; `tensor/DDL_lfc|DDL_z.npy` [4166]; `embed/gene_vectors.npy` [4166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4166 or target_col == 4166). Every well: [[MLANA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLANA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
