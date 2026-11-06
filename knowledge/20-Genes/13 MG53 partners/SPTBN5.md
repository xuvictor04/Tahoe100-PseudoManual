---
symbol: SPTBN5
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [HUSPECV, BSPECV, HUBSPECV]
gene_name: spectrin beta, non-erythrocytic 5
locus: 15q21
locus_type: gene with protein product
gene_family: [Spectrins, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SPTBN5

*spectrin beta, non-erythrocytic 5* — 15q21

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SPTBN5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | spectrin beta, non-erythrocytic 5 |
| Also known as | HUSPECV, BSPECV, HUBSPECV, beta V spectrin |
| Locus | 15q21 — gene with protein product |
| Gene families | Spectrins; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]] |

UniProt [Q9NRC6](https://www.uniprot.org/uniprotkb/Q9NRC6) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [51332](https://www.ncbi.nlm.nih.gov/gene/51332):

> Enables cytoskeletal protein binding activity; dynein intermediate chain binding activity; and identical protein binding activity. Acts upstream of or within Golgi organization and lysosomal transport. Located in cytoplasm; photoreceptor connecting cilium; and photoreceptor disc membrane. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:15680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15680) · Entrez [51332](https://www.ncbi.nlm.nih.gov/gene/51332) · UniProt [Q9NRC6](https://www.uniprot.org/uniprotkb/Q9NRC6) · Ensembl [ENSG00000137877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137877) · OMIM [605916](https://www.omim.org/entry/605916)

**PubMed**, as HGNC records for this gene — [10764729](https://pubmed.ncbi.nlm.nih.gov/10764729/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07018 |
| As a percentage | +4.98% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08204 / 0.06383 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.469 raw, 0.488 with 3 PCs removed |

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
