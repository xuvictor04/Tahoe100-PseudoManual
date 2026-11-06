---
symbol: NPHS1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [CNF, NPHN]
gene_name: NPHS1 adhesion molecule, nephrin
locus: 19q13.12
locus_type: gene with protein product
gene_family: [Fibronectin type III domain containing, V-set domain containing, C2-set domain containing]
family_siblings_here: [COL20A1, FNDC7, NECTIN4, PILRA]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# NPHS1

*NPHS1 adhesion molecule, nephrin* — 19q13.12

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NPHS1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | NPHS1 adhesion molecule, nephrin |
| Also known as | CNF, NPHN |
| Locus | 19q13.12 — gene with protein product |
| Gene families | Fibronectin type III domain containing; V-set domain containing; C2-set domain containing |
| Other genes here in those families | [[COL20A1]], [[FNDC7]], [[NECTIN4]], [[PILRA]] |
| Previously named | nephrosis 1, congenital, Finnish type (nephrin); NPHS1, nephrin |

**Function**, from UniProt [O60500](https://www.uniprot.org/uniprotkb/O60500) (reviewed):

> Seems to play a role in the development or function of the kidney glomerular filtration barrier. Regulates glomerular vascular permeability. May anchor the podocyte slit diaphragm to the actin cytoskeleton. Plays a role in skeletal muscle formation through regulation of myoblast fusion (By similarity)

**Summary**, from NCBI Gene [4868](https://www.ncbi.nlm.nih.gov/gene/4868):

> This gene encodes a member of the immunoglobulin family of cell adhesion molecules that functions in the glomerular filtration barrier in the kidney. The gene is primarily expressed in renal tissues, and the protein is a type-1 transmembrane protein found at the slit diaphragm of glomerular podocytes. The slit diaphragm is thought to function as an ultrafilter to exclude albumin and other plasma macromolecules in the formation of urine. Mutations in this gene result in Finnish-type congenital nephrosis 1, characterized by severe proteinuria and loss of the slit diaphragm and foot processes.[provided by RefSeq, Oct 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7908) · Entrez [4868](https://www.ncbi.nlm.nih.gov/gene/4868) · UniProt [O60500](https://www.uniprot.org/uniprotkb/O60500) · Ensembl [ENSG00000161270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161270) · OMIM [602716](https://www.omim.org/entry/602716)

**PubMed**, as HGNC records for this gene — [9915943](https://pubmed.ncbi.nlm.nih.gov/9915943/), [9660941](https://pubmed.ncbi.nlm.nih.gov/9660941/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06504 |
| As a percentage | +4.61% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06992 / 0.06208 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.673 raw, 0.345 with 3 PCs removed |

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
