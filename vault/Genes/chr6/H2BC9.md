---
symbol: "H2BC9"
type: "gene"
col: 15857
ensembl_id: "ENSG00000275713"
name: "H2B clustered histone 9"
location: "6p22.2"
module: null
arm: null
pooled_cpm: 2.52
n_lines_expressing: 32
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# H2BC9

*H2B clustered histone 9* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 7.17× (z +10.2, q 1e-21, up in 24 of 28 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 3.28× (z +6.4, q 3e-08, up in 22 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 14.9×; ⚠ cell-cycle shift, explains ~56% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 8.53×; ⚠ cell-cycle shift, explains ~57% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Gemcitabine (drug)]] 0.05 µM: 0.464× (z -5.1, q 2e-04, down in 18 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0276×; ⚠ cell-cycle shift, explains ~37% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.0689×).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15857.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 14.9×; ⚠ cell-cycle shift, explains ~56% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 8.53×; ⚠ cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **7.17×** | +10.2 | 1e-21 | 24/28 (KATO III, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **3.31×** | +9.1 | 2e-17 | 24/26 (A498, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.28×** | +6.4 | 3e-08 | 22/29 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.51×** | +5.0 | 1e-04 | 17/29 (KATO III, H4, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.36×** | +4.6 | 4e-04 | 17/26 (KATO III, HS-578T, …) | rises with dose | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.82× | +3.2 | 0.12 | 5/29 (RPMI-7951, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15857.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0276×; ⚠ cell-cycle shift, explains ~37% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW480 0.0689×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.464×** | -5.1 | 2e-04 | 18/30 (RKO, SW 900, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.343×** | -5.0 | 2e-04 | 16/27 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.461×** | -4.2 | 0.005 | 14/27 (CFPAC-1, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.489×** | -3.7 | 0.028 | 14/27 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -3.4 | 0.075 | 10/26 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.541×** | -3.3 | 0.082 | 9/29 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM |  | 0.564× | -3.1 | 0.15 | 8/26 (RPMI-7951, SW 900, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.567× | -3.1 | 0.15 | 5/29 (A498, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.95 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.07 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +8.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[KATO III (line)]] | alt | 7.68 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 14.9× (z +8.8) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.12 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0276× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 5.02 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0689× (z -8.7) |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.108 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.118 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.156 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.151 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.119 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.120 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.114 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.111 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.118 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.110 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.141 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.147 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.89 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | H2B clustered histone 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,251,614-26,252,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H2B/j; previously H2BFJ, HIST1H2BH |
| Gene groups (HGNC) | H2B histones |
| Reactome | 133 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; ChAHP complex assembly; DNA methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93079](https://www.uniprot.org/uniprotkb/Q93079) (Histone H2B type 1-H):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.

**Summary**, from NCBI Gene [8345](https://www.ncbi.nlm.nih.gov/gene/8345):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of chromatin into higher order structures. This gene is intronless and encodes a …

**Accessions** — [HGNC:4755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4755) · Entrez [8345](https://www.ncbi.nlm.nih.gov/gene/8345) · UniProt [Q93079](https://www.uniprot.org/uniprotkb/Q93079) · Ensembl [ENSG00000275713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275713)

## Data

Gene col 15857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15857); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15857, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15857]; `tensor/DDL_lfc|DDL_z.npy` [15857]; `embed/gene_vectors.npy` [15857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15857 or target_col == 15857). Every well: [[H2BC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2BC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
