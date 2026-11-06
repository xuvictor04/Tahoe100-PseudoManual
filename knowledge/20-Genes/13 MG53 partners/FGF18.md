---
symbol: FGF18
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [FGF-18, ZFGF5]
gene_name: fibroblast growth factor 18
locus: 5q35.1
locus_type: gene with protein product
gene_family: [Fibroblast growth factor family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# FGF18

*fibroblast growth factor 18* — 5q35.1

> [!summary] In one line
> FGF18 is a secreted fibroblast growth factor of the FGF8 subfamily, signalling through FGFR3 and FGFR4 to coordinate cartilage and bone development.

## What it is

FGF18 is a paracrine, heparin-binding ligand grouped with FGF8 and FGF17. Its best-established role is skeletal: mice lacking Fgf18 show delayed ossification, a disorganised growth plate and defective osteoblast differentiation, a phenotype overlapping Fgfr3 loss that makes FGF18 a physiological restraint on chondrocyte proliferation and a driver of osteogenesis. In adult cartilage it promotes matrix production, the rationale behind sprifermin, a recombinant FGF18 injected into knee joints in osteoarthritis trials; those showed gains in cartilage thickness on MRI without clear symptomatic benefit. In cancer it is reported as a Wnt/β-catenin-responsive gene upregulated in colorectal tumours, read as a paracrine rather than cell-autonomous signal.

## Why it appears in this work

FGF18 is not a curated p53 effector and not a transcription factor. It is here because the genome-wide screen ranked it as tracking measured [[MG53 (TRIM72)]]. It sits far from the TRIM72 locus, so [[Readthrough spillover]] offers no explanation, and a secreted developmental ligand co-moving with a membrane-repair gene has no prior mechanism.

## What is uncertain

Whether the association means anything. Paracrine FGF ligands are expressed in only a subset of lines here, so a genome-wide slope can be carried by a few lines rather than a consistent relationship, and nothing here distinguishes the two. The slope's direction carries no interpretation either: FGF18 has no assigned p53 direction to sign it against. Its cancer biology is receptor-dependent, so even a real correlation would not point to a consequence.

## References

- Ohbayashi et al., 1998, Journal of Biological Chemistry — cloned FGF-18 and described its expression pattern.
- Liu et al., 2002, Genes & Development — Fgf18-null mice show coordinated defects in chondrogenesis and osteogenesis.
- Ohbayashi et al., 2002, Genes & Development — FGF18 is required for proliferation and differentiation during skeletal development, with phenotypes overlapping Fgfr3 loss.
- Shimokawa et al., 2003, Cancer Research — FGF18 identified as a β-catenin/TCF-responsive gene upregulated in colorectal cancer.
- Hochberg et al., 2019, JAMA — sprifermin increased cartilage thickness in knee osteoarthritis without clear symptomatic benefit.

## What is on record

| | |
|---|---|
| Official name | fibroblast growth factor 18 |
| Also known as | FGF-18, ZFGF5 |
| Locus | 5q35.1 — gene with protein product |
| Gene families | Fibroblast growth factor family |

**Function**, from UniProt [O76093](https://www.uniprot.org/uniprotkb/O76093) (reviewed):

> Plays an important role in the regulation of cell proliferation, cell differentiation and cell migration. Required for normal ossification and bone development. Stimulates hepatic and intestinal proliferation

**Summary**, from NCBI Gene [8817](https://www.ncbi.nlm.nih.gov/gene/8817):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members possess broad mitogenic and cell survival activities, and are involved in a variety of biological processes, including embryonic development, cell growth, morphogenesis, tissue repair, tumor growth, and invasion. It has been shown in vitro that this protein is able to induce neurite outgrowth in PC12 cells. Studies of the similar proteins in mouse and chick suggested that this protein is a pleiotropic growth factor that stimulates proliferation in a number of tissues, most notably the liver and small intestine. Knockout studies of the similar gene in mice implied the role of this protein in regulating proliferation and differentiation of midline cerebellar structures. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:3674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3674) · Entrez [8817](https://www.ncbi.nlm.nih.gov/gene/8817) · UniProt [O76093](https://www.uniprot.org/uniprotkb/O76093) · Ensembl [ENSG00000156427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156427) · OMIM [603726](https://www.omim.org/entry/603726)

**PubMed**, as HGNC records for this gene — [9660775](https://pubmed.ncbi.nlm.nih.gov/9660775/), [9742123](https://pubmed.ncbi.nlm.nih.gov/9742123/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.09927 |
| As a percentage | +7.12% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09711 / 0.10062 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.763 raw, 0.674 with 3 PCs removed |

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
