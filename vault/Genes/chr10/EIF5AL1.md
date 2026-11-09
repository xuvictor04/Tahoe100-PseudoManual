---
symbol: "EIF5AL1"
type: "gene"
col: 14821
ensembl_id: "ENSG00000253626"
name: "eukaryotic translation initiation factor 5A like 1"
location: "10q22.3"
module: 58
arm: "+"
pooled_cpm: 3.89
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# EIF5AL1

*eukaryotic translation initiation factor 5A like 1* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.52× (z +11.1, q 6e-26, up in 6 of 6 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.97× (z +4.6, q 4e-04, up in 20 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM10]] (+0.67, fdr 1e-05), [[HMGB1P5]] (+0.64, fdr 2e-05, ⚠ HMGB1P5 in the vector space only through flagged drug-doses), [[THSD4-AS1]] (+0.58, fdr 3e-05), [[APRT]] (+0.58, fdr 1e-05); moves opposite to [[SUPT5H]] (-0.58, fdr 3e-05), [[CIZ1]] (-0.52, fdr 5e-05), [[STRA6LP]] (-0.50, fdr 3e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **6.52×** | +11.1 | 6e-26 | 6/6 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **7.20×** | +9.9 | 1e-20 | 19/20 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **4.83×** | +9.8 | 3e-20 | 8/8 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.61×** | +6.4 | 2e-08 | 26/34 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.1 | 3e-05 | 12/22 (NCI-H2030, A-427, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **2.12×** | +5.1 | 4e-05 | 11/20 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +4.6 | 4e-04 | 20/44 (SW480, C32, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.85×** | +4.1 | 0.003 | 18/46 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.013 | 16/36 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.77×** | +3.4 | 0.040 | 12/28 (SW 900, LOX-IMVI, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.64×** | +3.3 | 0.046 | 8/45 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 9 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM10]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[HMGB1P5]] ⚠ | +0.64 | +0.48 / +0.70 | both halves | 2e-05 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[THSD4-AS1]] | +0.58 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[APRT]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SNRPB]] | +0.55 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[POLR3K]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ATP5MC1]] | +0.55 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[HSD17B10]] ⚠ | +0.54 | +0.52 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MYCBP]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MRPL12]] | +0.53 | +0.53 / +0.57 | both halves | 1e-05 | STRING 522 |
| [[C9orf40]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TOMM22]] | +0.51 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[PGP]] | +0.50 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[TIMM13]] | +0.50 | +0.37 / +0.57 | both halves | 8e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT5H]] | -0.58 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[CIZ1]] | -0.52 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[STRA6LP]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[LINC00888]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[AMZ2P1]] | -0.49 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[ZNF18]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ACADSB]] | -0.46 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[CREBL2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[AAAS]] | -0.46 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TYW5]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ZNF211]] | -0.45 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[ZNF177]] | -0.45 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.1, -51.9); signed map (-43.4, -37.9). **Vector** length 35.0, 4.09% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +1.9 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +1.5 | +3.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +0.9 | +1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +0.9 | +2.0 |
|  | [[Thymol (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 5A like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:79,512,533-79,516,440 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA342M3.3; previously EIF5AP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IS14](https://www.uniprot.org/uniprotkb/Q6IS14) (Eukaryotic translation initiation factor 5A-1-like):

> Translation factor that promotes translation elongation and termination, particularly upon ribosome stalling at specific amino acid sequence contexts (By similarity). Binds between the exit (E) and peptidyl (P) site of the ribosome and promotes rescue of stalled ribosome: specifically required for efficient translation of polyproline-containing peptides as well as other motifs that stall the ribosome. Acts as a ribosome quality control (RQC) cofactor by joining the RQC complex to facilitate …

**Summary**, from NCBI Gene [143244](https://www.ncbi.nlm.nih.gov/gene/143244):

> Predicted to enable translation elongation factor activity. Predicted to be involved in translational elongation. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17419) · Entrez [143244](https://www.ncbi.nlm.nih.gov/gene/143244) · UniProt [Q6IS14](https://www.uniprot.org/uniprotkb/Q6IS14) · Ensembl [ENSG00000253626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253626)

## Data

Gene col 14821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14821); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14821]; `tensor/DDL_lfc|DDL_z.npy` [14821]; `embed/gene_vectors.npy` [14821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14821 or target_col == 14821). Every well: [[EIF5AL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF5AL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
