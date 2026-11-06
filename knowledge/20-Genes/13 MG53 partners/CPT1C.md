---
symbol: CPT1C
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [FLJ23809, CPTIC, CPT1P, CATL1]
gene_name: carnitine palmitoyltransferase 1C
locus: 19q13.33
locus_type: gene with protein product
gene_family: [Carnitine palmitoyltransferase family, Thioester hydrolases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CPT1C

*carnitine palmitoyltransferase 1C* — 19q13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CPT1C.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | carnitine palmitoyltransferase 1C |
| Also known as | FLJ23809, CPTIC, CPT1P, CATL1 |
| Locus | 19q13.33 — gene with protein product |
| Gene families | Carnitine palmitoyltransferase family; Thioester hydrolases |

**Function**, from UniProt [Q8TCG5](https://www.uniprot.org/uniprotkb/Q8TCG5) (reviewed):

> Palmitoyl thioesterase specifically expressed in the endoplasmic reticulum of neurons. Modulates the trafficking of the glutamate receptor, AMPAR, to plasma membrane through depalmitoylation of GRIA1 (PubMed:30135643). Also regulates AMPR trafficking through the regulation of SACM1L phosphatidylinositol-3-phosphatase activity by interaction in a malonyl-CoA dependent manner (By similarity). Binds malonyl-CoA and couples malonyl-CoA to ceramide levels, necessary for proper spine maturation and contributing to systemic energy homeostasis and appetite control (PubMed:16651524). Binds to palmitoyl-CoA, but does not have carnitine palmitoyltransferase 1 catalytic activity or at very low levels (PubMed:25751282, PubMed:30135643)

**Summary**, from NCBI Gene [126129](https://www.ncbi.nlm.nih.gov/gene/126129):

> This gene encodes a member of the carnitine/choline acetyltransferase family. The encoded protein regulates the beta-oxidation and transport of long-chain fatty acids into mitochondria, and may play a role in the regulation of feeding behavior and whole-body energy homeostasis. Alternatively spliced transcript variants encoding multiple protein isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18540) · Entrez [126129](https://www.ncbi.nlm.nih.gov/gene/126129) · UniProt [Q8TCG5](https://www.uniprot.org/uniprotkb/Q8TCG5) · Ensembl [ENSG00000169169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169169) · OMIM [608846](https://www.omim.org/entry/608846)

**PubMed**, as HGNC records for this gene — [12376098](https://pubmed.ncbi.nlm.nih.gov/12376098/), [11001805](https://pubmed.ncbi.nlm.nih.gov/11001805/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08277 |
| As a percentage | +5.90% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08934 / 0.07878 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.609 raw, 0.376 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
