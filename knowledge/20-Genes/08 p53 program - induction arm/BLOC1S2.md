---
symbol: BLOC1S2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MGC10120, FLJ30135, BLOS2, BORCS2]
gene_name: biogenesis of lysosomal organelles complex 1 subunit 2
locus: 10q24.31
locus_type: gene with protein product
gene_family: [Biogenesis of lysosomal organelles complex 1 subunits, BLOC-1 related complex subunits]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 22.15
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# BLOC1S2

*biogenesis of lysosomal organelles complex 1 subunit 2* — 10q24.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/BLOC1S2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | biogenesis of lysosomal organelles complex 1 subunit 2 |
| Also known as | MGC10120, FLJ30135, BLOS2, BORCS2, centrosome protein oncogene, Biogenesis of Lysosome-related Organelles complex-1 Subunit 2, BLOC-1 subunit 2 |
| Locus | 10q24.31 — gene with protein product |
| Gene families | Biogenesis of lysosomal organelles complex 1 subunits; BLOC-1 related complex subunits |

**Function**, from UniProt [Q6QNY1](https://www.uniprot.org/uniprotkb/Q6QNY1) (reviewed):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes (PubMed:15102850, PubMed:17182842). In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension (By similarity). As part of the BORC complex may play a role in lysosomes movement and localization at the cell periphery. Associated with the cytosolic face of lysosomes, the BORC complex may recruit ARL8B and couple lysosomes to microtubule plus-end-directed kinesin motor (PubMed:25898167). May play a role in cell proliferation (PubMed:15381421)

**Summary**, from NCBI Gene [282991](https://www.ncbi.nlm.nih.gov/gene/282991):

> This gene encodes a protein with multiple functions. The encoded protein has been found in association with the centrosome, shown to co-localize with gamma-tubulin, and also found to be one of the proteins in the BLOC-1 complex which functions in the formation of lysosome-related organelles. A pseudogene of this gene is located on the X chromosome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:20984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20984) · Entrez [282991](https://www.ncbi.nlm.nih.gov/gene/282991) · UniProt [Q6QNY1](https://www.uniprot.org/uniprotkb/Q6QNY1) · Ensembl [ENSG00000196072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196072) · OMIM [609768](https://www.omim.org/entry/609768)

**PubMed**, as HGNC records for this gene — [11483580](https://pubmed.ncbi.nlm.nih.gov/11483580/), [15102850](https://pubmed.ncbi.nlm.nih.gov/15102850/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 22.15 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 37 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.122× |
| Wild-type minus altered | 1.093× |
| Compounds moving it up in WT lines | 71 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00365 |
| As a percentage | -0.25% |
| FDR, exposure-shuffle null | 0.2350 |
| In TP53-wild-type lines / altered lines | -0.00085 / -0.00535 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.280 raw, -0.215 with 3 PCs removed |

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
