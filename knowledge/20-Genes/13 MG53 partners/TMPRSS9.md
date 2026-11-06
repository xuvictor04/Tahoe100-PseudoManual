---
symbol: TMPRSS9
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: transmembrane serine protease 9
locus: 19p13.3
locus_type: gene with protein product
gene_family: [Type II transmembrane serine proteases]
family_siblings_here: [HPN]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# TMPRSS9

*transmembrane serine protease 9* — 19p13.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TMPRSS9.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | transmembrane serine protease 9 |
| Also known as | polyserase 1 |
| Locus | 19p13.3 — gene with protein product |
| Gene families | Type II transmembrane serine proteases |
| Other genes here in those families | [[HPN]] |
| Previously named | transmembrane protease, serine 9 |

**Function**, from UniProt [Q7Z410](https://www.uniprot.org/uniprotkb/Q7Z410) (reviewed):

> Serase-1 and serase-2 are serine proteases that hydrolyze the peptides N-t-Boc-Gln-Ala-Arg-AMC and N-t-Boc-Gln-Gly-Arg-AMC. In contrast, N-t-Boc-Ala-Phe-Lys-AMC and N-t-Boc-Ala-Pro-Ala-AMC are not significantly hydrolyzed

**Summary**, from NCBI Gene [360200](https://www.ncbi.nlm.nih.gov/gene/360200):

> The protein encoded by this gene is a membrane-bound type II serine polyprotease that is cleaved to release three different proteases. Two of the proteases are active and can be inhibited by serine protease inhibitors, and one is thought to be catalytically inactive. This gene enhances the invasive capability of pancreatic cancer cells and may be involved in cancer progression. [provided by RefSeq, Jul 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30079](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30079) · Entrez [360200](https://www.ncbi.nlm.nih.gov/gene/360200) · UniProt [Q7Z410](https://www.uniprot.org/uniprotkb/Q7Z410) · Ensembl [ENSG00000178297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178297) · OMIM [610477](https://www.omim.org/entry/610477)

**PubMed**, as HGNC records for this gene — [12886014](https://pubmed.ncbi.nlm.nih.gov/12886014/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07050 |
| As a percentage | +5.01% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06808 / 0.07197 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.659 raw, 0.340 with 3 PCs removed |

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
