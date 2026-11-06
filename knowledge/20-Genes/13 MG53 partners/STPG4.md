---
symbol: STPG4
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [FLJ40172]
gene_name: sperm-tail PG-rich repeat containing 4
locus: 2p21
locus_type: gene with protein product
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# STPG4

*sperm-tail PG-rich repeat containing 4* — 2p21

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/STPG4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | sperm-tail PG-rich repeat containing 4 |
| Also known as | FLJ40172 |
| Locus | 2p21 — gene with protein product |
| Previously named | chromosome 2 open reading frame 61 |

**Function**, from UniProt [Q8N801](https://www.uniprot.org/uniprotkb/Q8N801) (reviewed):

> Maternal factor that plays a role in epigenetic chromatin reprogramming during early development of the zygote. Involved in the regulation of gametic DNA demethylation by inducing the conversion of the modified genomic base 5-methylcytosine (5mC) into 5-hydroxymethylcytosine (5hmC)

**Summary**, from NCBI Gene [285051](https://www.ncbi.nlm.nih.gov/gene/285051):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in epigenetic programing of male pronucleus. Predicted to act upstream of or within pyrimidine-containing compound catabolic process. Predicted to be located in cytoplasm and nucleus. Predicted to be active in female pronucleus; germinal vesicle; and male pronucleus. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:26850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26850) · Entrez [285051](https://www.ncbi.nlm.nih.gov/gene/285051) · UniProt [Q8N801](https://www.uniprot.org/uniprotkb/Q8N801) · Ensembl [ENSG00000239605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239605)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06320 |
| As a percentage | +4.48% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07485 / 0.05614 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.705 raw, 0.558 with 3 PCs removed |

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
