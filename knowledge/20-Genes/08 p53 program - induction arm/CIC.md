---
symbol: CIC
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0306]
gene_name: capicua transcriptional repressor
locus: 19q13.2
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 27.56
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CIC

*capicua transcriptional repressor* — 19q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CIC.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | capicua transcriptional repressor |
| Also known as | KIAA0306 |
| Locus | 19q13.2 — gene with protein product |
| Previously named | capicua (Drosophila) homolog; capicua homolog (Drosophila) |

**Function**, from UniProt [Q96RK0](https://www.uniprot.org/uniprotkb/Q96RK0) (reviewed):

> Transcriptional repressor which plays a role in development of the central nervous system (CNS). In concert with ATXN1 and ATXN1L, involved in brain development

**Summary**, from NCBI Gene [23152](https://www.ncbi.nlm.nih.gov/gene/23152):

> The protein encoded by this gene is an ortholog of the Drosophila melanogaster capicua gene, and is a member of the high mobility group (HMG)-box superfamily of transcriptional repressors. This protein contains a conserved HMG domain that is involved in DNA binding and nuclear localization, and a conserved C-terminus. Studies suggest that the N-terminal region of this protein interacts with Atxn1 (GeneID:6310), to form a transcription repressor complex, and in vitro studies suggest that polyglutamine-expansion of ATXN1 may alter the repressor activity of this complex. Mutations in this gene have been associated with olidogdendrogliomas (PMID:21817013). In addition, translocation events resulting in gene fusions of this gene with both DUX4 (GeneID:100288687) and FOXO4 (GeneID:4303) have been associated with round cell sarcomas. There are multiple pseudogenes of this gene found on chromosomes 1, 4, 6, 7, 16, 20, and the Y chromosome. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Feb 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:14214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14214) · Entrez [23152](https://www.ncbi.nlm.nih.gov/gene/23152) · UniProt [Q96RK0](https://www.uniprot.org/uniprotkb/Q96RK0) · Ensembl [ENSG00000079432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079432) · OMIM [612082](https://www.omim.org/entry/612082)

**PubMed**, as HGNC records for this gene — [12393275](https://pubmed.ncbi.nlm.nih.gov/12393275/), [15981098](https://pubmed.ncbi.nlm.nih.gov/15981098/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 27.56 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 174 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.029× |
| Wild-type minus altered | 1.046× |
| Compounds moving it up in WT lines | 54 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00037 |
| As a percentage | +0.03% |
| FDR, exposure-shuffle null | 0.9247 |
| In TP53-wild-type lines / altered lines | -0.00323 / 0.00255 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.042 raw, 0.109 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
