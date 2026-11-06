---
symbol: SLC8A2
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [NCX2, KIAA1087]
gene_name: solute carrier family 8 member A2
locus: 19q13.32
locus_type: gene with protein product
gene_family: [Solute carrier family 8]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SLC8A2

*solute carrier family 8 member A2* — 19q13.32

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SLC8A2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | solute carrier family 8 member A2 |
| Also known as | NCX2, KIAA1087 |
| Locus | 19q13.32 — gene with protein product |
| Gene families | Solute carrier family 8 |
| Previously named | solute carrier family 8 (sodium/calcium exchanger), member 2 |

**Function**, from UniProt [Q9UPR5](https://www.uniprot.org/uniprotkb/Q9UPR5) (reviewed):

> Mediates the electrogenic exchange of Ca(2+) against Na(+) ions across the cell membrane, and thereby contributes to the regulation of cytoplasmic Ca(2+) levels and Ca(2+)-dependent cellular processes. Contributes to cellular Ca(2+) homeostasis in excitable cells. Contributes to the rapid decrease of cytoplasmic Ca(2+) levels back to baseline after neuronal activation, and thereby contributes to modulate synaptic plasticity, learning and memory. Plays a role in regulating urinary Ca(2+) and Na(+) excretion

**Summary**, from NCBI Gene [6543](https://www.ncbi.nlm.nih.gov/gene/6543):

> Predicted to enable calcium:monoatomic cation antiporter activity involved in regulation of postsynaptic cytosolic calcium ion concentration and calcium:sodium antiporter activity. Predicted to be involved in several processes, including learning or memory; monoatomic cation transmembrane transport; and regulation of short-term neuronal synaptic plasticity. Predicted to act upstream of or within several processes, including modulation of chemical synaptic transmission; regulation of action potential firing pattern; and response to ischemia. Located in presynapse. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11069) · Entrez [6543](https://www.ncbi.nlm.nih.gov/gene/6543) · UniProt [Q9UPR5](https://www.uniprot.org/uniprotkb/Q9UPR5) · Ensembl [ENSG00000118160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118160) · OMIM [601901](https://www.omim.org/entry/601901)

**PubMed**, as HGNC records for this gene — [8021246](https://pubmed.ncbi.nlm.nih.gov/8021246/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08530 |
| As a percentage | +6.09% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08468 / 0.08565 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.701 raw, 0.529 with 3 PCs removed |

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
