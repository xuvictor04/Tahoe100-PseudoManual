---
symbol: SNX2
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: sorting nexin 2
locus: 5q23.2
locus_type: gene with protein product
gene_family: [Sorting nexins, PX-BAR domain containing]
family_siblings_here: [SNX31]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 76.93
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SNX2

*sorting nexin 2* — 5q23.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SNX2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | sorting nexin 2 |
| Also known as | — (no recorded alias) |
| Locus | 5q23.2 — gene with protein product |
| Gene families | Sorting nexins; PX-BAR domain containing |
| Other genes here in those families | [[SNX31]] |

**Function**, from UniProt [O60749](https://www.uniprot.org/uniprotkb/O60749) (reviewed):

> Involved in several stages of intracellular trafficking. Interacts with membranes containing phosphatidylinositol 3-phosphate (PtdIns(3P)) or phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2) (PubMed:16179610). Acts in part as component of the retromer membrane-deforming SNX-BAR subcomplex (PubMed:17101778). The SNX-BAR retromer mediates retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN) and is involved in endosome-to-plasma membrane transport for cargo protein recycling. The SNX-BAR subcomplex functions to deform the donor membrane into a tubular profile called endosome-to-TGN transport carrier (ETC) (Probable). Can sense membrane curvature and has in vitro vesicle-to-membrane remodeling activity (PubMed:23085988). Required for retrograde endosome-to-TGN transport of TGN38 (PubMed:20138391). Promotes KALRN- and RHOG-dependent but retromer-independent membrane remodeling such as lamellipodium formation; the function is dependent on GEF activity of KALRN (PubMed:20604901)

**Summary**, from NCBI Gene [6643](https://www.ncbi.nlm.nih.gov/gene/6643):

> This gene belongs to the sorting nexin family whose members contain the phosphoinositide-binding phox (PX) domain. The encoded protein is a component of the retromer complex which plays a role in protein sorting in the endocytic pathway. This protein may form oligomeric complexes with other family members. Alternate splicing results in multiple transcript variants of this gene. Pseudogenes associated with this gene are located on chromosomes 1 and 7. [provided by RefSeq, May 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11173) · Entrez [6643](https://www.ncbi.nlm.nih.gov/gene/6643) · UniProt [O60749](https://www.uniprot.org/uniprotkb/O60749) · Ensembl [ENSG00000205302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205302) · OMIM [605929](https://www.omim.org/entry/605929)

**PubMed**, as HGNC records for this gene — [9819414](https://pubmed.ncbi.nlm.nih.gov/9819414/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 76.93 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 68 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.075× |
| Wild-type minus altered | 1.038× |
| Compounds moving it up in WT lines | 75 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00824 |
| As a percentage | -0.57% |
| FDR, exposure-shuffle null | 0.0005 |
| In TP53-wild-type lines / altered lines | -0.00305 / -0.01138 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.039 raw, -0.329 with 3 PCs removed |

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
