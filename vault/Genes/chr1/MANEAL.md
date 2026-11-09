---
symbol: "MANEAL"
type: "gene"
col: 11623
ensembl_id: "ENSG00000185090"
name: "mannosidase endo-alpha like"
location: "1p34.3"
module: 33
arm: "+"
pooled_cpm: 3.23
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MANEAL

*mannosidase endo-alpha like* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.42× (z +7.1, q 5e-10, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.48× (z +4.7, q 4e-04, up in 9 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -7.7, q 9e-12, down in 22 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD6]] (+0.64, fdr 1e-05), [[ZNF496]] (+0.64, fdr 2e-05), [[PCGF6]] (+0.64, fdr 1e-05); moves opposite to [[LINC00910]] (-0.60, fdr 1e-05), [[THAP9]] (-0.58, fdr 1e-05), [[PRKAR1A]] (-0.55, fdr 8e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[HMBS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.1 | 5e-10 | 4/7 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.5 | 2e-08 | 6/15 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.1 | 6e-05 | 6/17 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.7 | 4e-04 | 9/40 (A-427, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +3.8 | 0.016 | 5/9 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.025 | 7/39 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.082 | 4/27 (SW480, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -7.7 | 9e-12 | 22/30 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -3.8 | 0.032 | 17/40 (SNU-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tadalafil (drug)]] 5 µM |  | **0.629×** | -3.8 | 0.032 | 10/35 (LoVo, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.641×** | -3.6 | 0.044 | 17/37 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.670×** | -3.4 | 0.070 | 12/41 (NCI-H2030, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.070 | 12/40 (HCT15, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.764× | -3.2 | 0.10 | 13/29 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.695× | -3.1 | 0.15 | 11/27 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 2.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 5.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.8) |
| [[J82 (line)]] | alt | 5.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.3) |
| [[PANC-1 (line)]] | alt | 3.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -16.5) |
| [[SW1417 (line)]] | alt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.6) |
| [[A-427 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.881 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.996 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD6]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PCGF6]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MCAT]] | +0.62 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[TMEM177]] | +0.62 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[STARD7]] | +0.62 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[IPO11]] | +0.61 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[DCTPP1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SIMC1]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TMCO6]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00910]] | -0.60 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[THAP9]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.55 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[SUB1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PAN2]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PPP1R11]] | -0.52 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[MED29]] | -0.52 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[SMIM14]] | -0.52 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[TEX14]] | -0.51 | -0.32 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMBS]] | B | MANEAL activity raises HMBS's level | lines that do not express MANEAL (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without MANEAL | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[POLR1B]] | B | MANEAL activity raises POLR1B's level | lines that do not express MANEAL (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without MANEAL | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[MRPL34]] | B | MANEAL activity raises MRPL34's level | lines that do not express MANEAL (5) vs lines expressing it (45) | 1.15× lower at baseline in the lines without MANEAL | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.4, -41.9); signed map (-11.2, -52.2). **Vector** length 40.0, 4.76% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.0 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase endo-alpha like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,793,847-37,801,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31434 |
| Gene groups (HGNC) | Mannosidases endo-alpha |
| Matched by | ensembl_id |

UniProt [Q5VSG8](https://www.uniprot.org/uniprotkb/Q5VSG8) carries no function annotation.

**Summary**, from NCBI Gene [149175](https://www.ncbi.nlm.nih.gov/gene/149175):

> Predicted to enable alpha-mannosidase activity. Predicted to be located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26452) · Entrez [149175](https://www.ncbi.nlm.nih.gov/gene/149175) · UniProt [Q5VSG8](https://www.uniprot.org/uniprotkb/Q5VSG8) · Ensembl [ENSG00000185090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185090)

## Data

Gene col 11623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11623); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11623]; `tensor/DDL_lfc|DDL_z.npy` [11623]; `embed/gene_vectors.npy` [11623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11623 or target_col == 11623). Every well: [[MANEAL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MANEAL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
