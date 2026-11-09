---
symbol: "ECHDC3"
type: "gene"
col: 5565
ensembl_id: "ENSG00000134463"
name: "enoyl-CoA hydratase domain containing 3"
location: "10p14"
module: 221
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 27
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# ECHDC3

*enoyl-CoA hydratase domain containing 3* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.18× (z +9.4, q 3e-18, up in 15 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (NCI-H23 0.0834×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (CHP-212 0.446×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IAH1]] (+0.64, fdr 1e-05), [[CCNYL2-1]] (+0.60, fdr 4e-05), [[RBM45]] (+0.60, fdr 1e-05); moves opposite to [[RFX3]] (-0.50, fdr 4e-05), [[CFAP44]] (-0.49, fdr 4e-05), [[PIK3R3]] (-0.46, fdr 1e-04).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PIK3R3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.18×** | +9.4 | 3e-18 | 15/24 (A498, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +7.9 | 6e-13 | 2/5 (A498, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.0 | 4e-10 | 4/7 (NCI-H1792, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.68×** | +4.4 | 0.001 | 4/19 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.04×** | +4.3 | 0.002 | 3/12 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +4.2 | 0.002 | 2/7 (NCI-H2347, PANC-1) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +3.6 | 0.024 | 2/10 (NCI-H1792, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.6 | 0.026 | 1/12 (NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.3 | 0.057 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +3.2 | 0.074 | 7/19 (RPMI-7951, A498, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.10 | 1/17 (J82) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.29× | +3.0 | 0.12 | 1/19 (HS-578T) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (NCI-H23 0.0834×; ⚠ toxic); [[Panobinostat (drug)]] 5 µM in 1 line (CHP-212 0.446×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 0.975 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.446× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 7.38 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0834× (z -9.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.804 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.697 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.226 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IAH1]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CCNYL2-1]] | +0.60 | +0.43 / +0.64 | both halves | 4e-05 |  |
| [[RBM45]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[UBE2Q2P1]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[WDR11]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CAMK1]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ZNF391]] | +0.52 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[NDFIP1]] | +0.52 | +0.28 / +0.60 | both halves | 3e-04 |  |
| [[PSMF1]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PTPN20]] | +0.50 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[SVIL-AS1-1]] | +0.50 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[FAHD2CP]] | +0.50 | +0.52 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[CFAP44]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PIK3R3]] | -0.46 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[FOSB]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NASP]] | -0.45 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[TLE4]] | -0.43 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[NSUN6]] | -0.42 | -0.26 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3R3]] | B | ECHDC3 activity raises PIK3R3's level | lines that do not express ECHDC3 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without ECHDC3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: CACNA2D1, ZNF229, LRRIQ1 |

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.6, 23.4); signed map (-5.5, -33.5). **Vector** length 30.7, 4.88% of its response variance represented; |z| ≥ 3 in 444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.0 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.8 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[Rucaparib (phosphate) (drug)]] 5 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA hydratase domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:11,742,366-11,764,070 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20909 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DC8](https://www.uniprot.org/uniprotkb/Q96DC8) (Enoyl-CoA hydratase domain-containing protein 3, mitochondrial):

> May play a role in fatty acid biosynthesis and insulin sensitivity.

**Summary**, from NCBI Gene [79746](https://www.ncbi.nlm.nih.gov/gene/79746):

> Predicted to enable enoyl-CoA hydratase activity. Involved in positive regulation of cellular response to insulin stimulus. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23489) · Entrez [79746](https://www.ncbi.nlm.nih.gov/gene/79746) · UniProt [Q96DC8](https://www.uniprot.org/uniprotkb/Q96DC8) · Ensembl [ENSG00000134463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134463)

## Data

Gene col 5565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5565); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5565]; `tensor/DDL_lfc|DDL_z.npy` [5565]; `embed/gene_vectors.npy` [5565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5565 or target_col == 5565). Every well: [[ECHDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECHDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
