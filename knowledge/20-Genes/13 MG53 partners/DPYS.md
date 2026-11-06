---
symbol: DPYS
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [DHPase]
gene_name: dihydropyrimidinase
locus: 8q22.3
locus_type: gene with protein product
gene_family: [M38 metallopeptidases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# DPYS

*dihydropyrimidinase* — 8q22.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DPYS.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | dihydropyrimidinase |
| Also known as | DHPase |
| Locus | 8q22.3 — gene with protein product |
| Gene families | M38 metallopeptidases |

**Function**, from UniProt [Q14117](https://www.uniprot.org/uniprotkb/Q14117) (reviewed):

> Hydrolase that catalyzes the reversible hydrolytic ring opening of 5,6-dihydrouracil and 5,6-dihydrothymine, the second step in the reductive catabolic pathway of uracil and thymine degradation

**Summary**, from NCBI Gene [1807](https://www.ncbi.nlm.nih.gov/gene/1807):

> Dihydropyrimidinase catalyzes the conversion of 5,6-dihydrouracil to 3-ureidopropionate in pyrimidine metabolism.  Dihydropyrimidinase is expressed at a high level in liver and kidney as a major 2.5-kb transcript and a minor 3.8-kb transcript.  Defects in the DPYS gene are linked to dihydropyrimidinuria. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:3013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3013) · Entrez [1807](https://www.ncbi.nlm.nih.gov/gene/1807) · UniProt [Q14117](https://www.uniprot.org/uniprotkb/Q14117) · Ensembl [ENSG00000147647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147647) · OMIM [613326](https://www.omim.org/entry/613326)

**PubMed**, as HGNC records for this gene — [8973361](https://pubmed.ncbi.nlm.nih.gov/8973361/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06831 |
| As a percentage | +4.85% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07109 / 0.06655 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.627 raw, 0.452 with 3 PCs removed |

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
