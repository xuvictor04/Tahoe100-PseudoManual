---
symbol: MPP4
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: MAGUK p55 scaffold protein 4
locus: 2q33.1
locus_type: gene with protein product
gene_family: [Membrane associated guanylate kinases, PDZ domain containing, SH3 domain containing]
family_siblings_here: [CASK, EPS8L2, HCLS1, PRX, RAPGEF6]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# MPP4

*MAGUK p55 scaffold protein 4* — 2q33.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MPP4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | MAGUK p55 scaffold protein 4 |
| Also known as | — (no recorded alias) |
| Locus | 2q33.1 — gene with protein product |
| Gene families | Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Other genes here in those families | [[CASK]], [[EPS8L2]], [[HCLS1]], [[PRX]], [[RAPGEF6]] |
| Previously named | membrane protein, palmitoylated 4 (MAGUK p55 subfamily member 4); membrane protein, palmitoylated 4; membrane palmitoylated protein 4 |

**Function**, from UniProt [Q96JB8](https://www.uniprot.org/uniprotkb/Q96JB8) (reviewed):

> May play a role in retinal photoreceptors development

**Summary**, from NCBI Gene [58538](https://www.ncbi.nlm.nih.gov/gene/58538):

> This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) protein family, with an N-terminal PDZ domain, a central src homology 3 region (SH3), and a C-terminal guanylate kinase-like (GUK) domain. The protein is localized to the outer limiting membrane in the retina, and is thought to function in photoreceptor polarity and the organization of specialized intercellular junctions. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13680) · Entrez [58538](https://www.ncbi.nlm.nih.gov/gene/58538) · UniProt [Q96JB8](https://www.uniprot.org/uniprotkb/Q96JB8) · Ensembl [ENSG00000082126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082126) · OMIM [606575](https://www.omim.org/entry/606575)

**PubMed**, as HGNC records for this gene — [11414766](https://pubmed.ncbi.nlm.nih.gov/11414766/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06393 |
| As a percentage | +4.53% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.05087 / 0.07238 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.669 raw, 0.564 with 3 PCs removed |

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
