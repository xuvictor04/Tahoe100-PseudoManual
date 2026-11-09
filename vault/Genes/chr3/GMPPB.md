---
symbol: "GMPPB"
type: "gene"
col: 10399
ensembl_id: "ENSG00000173540"
name: "GDP-mannose pyrophosphorylase B"
location: "3p21.31"
module: 52
arm: "+"
pooled_cpm: 7.05
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# GMPPB

*GDP-mannose pyrophosphorylase B* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +9.0, q 1e-16, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.746× (z -4.3, q 0.008, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0565×; ⚠ transcription drop); [[Ribociclib (drug)]] 0.05 µM in 1 line (AsPC-1 0.0583×; ⚠ unreliable plate only; position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A549 0.0853×; ⚠ cell-cycle shift, explains ~0% of this change); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0747×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM214]] (+0.70, fdr 7e-06), [[SYVN1]] (+0.67, fdr 7e-06), [[CRELD2]] (+0.66, fdr 7e-06); moves opposite to [[SSB]] (-0.52, fdr 1e-04), [[SMIM30]] (-0.46, fdr 6e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +9.0 | 1e-16 | 28/42 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +6.1 | 3e-07 | 12/24 (NCI-H2030, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.73×** | +5.6 | 5e-06 | 6/14 (A498, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.67×** | +5.4 | 8e-06 | 13/30 (PANC-1, A498, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.0 | 8e-05 | 20/45 (HT-29, LS 180, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.021 | 11/38 (C32, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.060 | 9/43 (NCI-H1792, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.36× | +3.2 | 0.10 | 8/40 (A-427, CFPAC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.10 | 6/36 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0565×; ⚠ transcription drop); [[Ribociclib (drug)]] 0.05 µM in 1 line (AsPC-1 0.0583×; ⚠ unreliable plate only; position not correctable); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A549 0.0853×; ⚠ cell-cycle shift, explains ~0% of this change); [[Elimusertib hydrochloride (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0747×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.746×** | -4.3 | 0.008 | 17/47 (COLO 205, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.069 | 15/46 (Hs 766T, SW48, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.93 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0853× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Ribociclib (drug)]] 0.05 µM 0.0583× (z -8.6) ⚠ unreliable plate only; position not correctable |
| [[CFPAC-1 (line)]] | alt | 3.46 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0565× (z -9.9) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 3.93 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0747× (z -8.6) |
| [[A-172 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM214]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SYVN1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CRELD2]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 | STRING 755 |
| [[LRRC59]] | +0.66 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[B4GALT7]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[CHPF2]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[SEC16A]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[GMPPA]] | +0.61 | +0.58 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 999 |
| [[SRPRA]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SEC61A1]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 | STRING 545 |
| [[FASTK]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSB]] | -0.52 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[SMIM30]] | -0.46 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.8, -29.2); signed map (-51.5, 4.2). **Vector** length 65.1, 10.9% of its response variance represented; |z| ≥ 3 in 720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.3 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | GDP-mannose pyrophosphorylase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,716,844-49,723,973 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1851 |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: Synthesis of GDP-mannose; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5P6](https://www.uniprot.org/uniprotkb/Q9Y5P6) (Mannose-1-phosphate guanylyltransferase catalytic subunit beta):

> Catalytic subunit of the GMPPA-GMPPB mannose-1-phosphate guanylyltransferase complex. Catalyzes the formation of GDP-mannose, an essential precursor of glycan moieties of glycoproteins and glycolipids. Can catalyze the reverse reaction in vitro. Together with GMPPA regulates GDP-alpha-D-mannose levels.

**Summary**, from NCBI Gene [29925](https://www.ncbi.nlm.nih.gov/gene/29925):

> This gene is thought to encode a GDP-mannose pyrophosphorylase. The encoded protein catalyzes the conversion of mannose-1-phosphate and GTP to GDP-mannose, a reaction involved in the production of N-linked oligosaccharides. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:22932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22932) · Entrez [29925](https://www.ncbi.nlm.nih.gov/gene/29925) · UniProt [Q9Y5P6](https://www.uniprot.org/uniprotkb/Q9Y5P6) · Ensembl [ENSG00000173540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173540)

## Data

Gene col 10399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10399); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10399]; `tensor/DDL_lfc|DDL_z.npy` [10399]; `embed/gene_vectors.npy` [10399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10399 or target_col == 10399). Every well: [[GMPPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMPPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
