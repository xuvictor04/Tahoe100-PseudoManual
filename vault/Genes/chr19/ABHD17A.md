---
symbol: "ABHD17A"
type: "gene"
col: 5010
ensembl_id: "ENSG00000129968"
name: "abhydrolase domain containing 17A, depalmitoylase"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ABHD17A

*abhydrolase domain containing 17A, depalmitoylase* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.95× (z +8.8, q 9e-16, up in 38 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS11]] (+0.78, fdr 7e-06), [[SDHAP4]] (+0.74, fdr 7e-06), [[CCDC61]] (+0.73, fdr 1e-05); moves opposite to [[ANKRD26]] (-0.66, fdr 1e-05), [[BPTF]] (-0.64, fdr 1e-05), [[LITAF]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPP1R12C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +8.8 | 9e-16 | 38/45 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.65×** | +7.9 | 8e-13 | 30/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +6.0 | 3e-07 | 20/42 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.70×** | +4.2 | 0.003 | 1/4 (PANC-1) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.009 | 10/46 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.4 | 0.054 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.054 | 5/33 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.47× | +3.1 | 0.13 | 0/45 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.687× | -3.1 | 0.46 | 7/45 (SW1417, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.688× | -3.1 | 0.46 | 10/44 (SNU-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS11]] | +0.78 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[CCDC61]] | +0.73 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[FCHSD1]] | +0.72 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[MSTO2P]] | +0.71 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GPAT4]] | +0.70 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[TUBGCP6]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 | STRING 458 |
| [[PCNX3]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[FBXW2]] | +0.68 | +0.73 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD26]] | -0.66 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[BPTF]] | -0.64 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[LITAF]] | -0.63 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[LINC02307]] | -0.62 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[LZIC]] | -0.62 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.60 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ASH1L]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[LACTB2]] | -0.60 | -0.67 / -0.33 | both halves | 1e-04 |  |
| [[NNT-AS1]] | -0.59 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[TRIP11]] | -0.58 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[MED13]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF638]] | -0.58 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ABHD17A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R12C]] | C | ABHD17A's natural level weakens PPP1R12C's drug response | ABHD17A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.34; direction not clear | 0.088 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.1, -23.8); signed map (-44.4, -10.9). **Vector** length 43.1, 4.33% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +7.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +0.8 | +1.3 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +0.8 | +1.9 |
|  | [[Adenine (drug)]] 0.05 µM |  | +0.8 | +2.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.8 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.5 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 17A, depalmitoylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,876,810-1,885,496 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5244; previously C19orf27, FAM108A1 |
| Gene groups (HGNC) | Abhydrolase domain containing; Depalmitoylases; Thioester hydrolases |
| Reactome | 4 pathways, smallest: RAS processing; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GS6](https://www.uniprot.org/uniprotkb/Q96GS6) (Alpha/beta hydrolase domain-containing protein 17A):

> Hydrolyzes fatty acids from S-acylated cysteine residues in proteins. Has depalmitoylating activity towards NRAS. Has depalmitoylating activity towards DLG4/PSD95. May have depalmitoylating activity towards MAP6 (By similarity).

**Summary**, from NCBI Gene [81926](https://www.ncbi.nlm.nih.gov/gene/81926):

> Enables palmitoyl-(protein) hydrolase activity. Involved in negative regulation of NLRP3 inflammasome complex assembly; protein depalmitoylation; and protein localization to membrane. Located in endosome membrane and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28756) · Entrez [81926](https://www.ncbi.nlm.nih.gov/gene/81926) · UniProt [Q96GS6](https://www.uniprot.org/uniprotkb/Q96GS6) · Ensembl [ENSG00000129968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129968)

## Data

Gene col 5010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5010); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5010]; `tensor/DDL_lfc|DDL_z.npy` [5010]; `embed/gene_vectors.npy` [5010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5010 or target_col == 5010). Every well: [[ABHD17A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD17A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
