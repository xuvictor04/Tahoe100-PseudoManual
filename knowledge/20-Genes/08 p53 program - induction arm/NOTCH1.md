---
symbol: NOTCH1
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: notch receptor 1
locus: 9q34.3
locus_type: gene with protein product
gene_family: [Notch receptors, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NUP210L, PER1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 21.66
mg53_verdict: none
tags: [gene, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# NOTCH1

*notch receptor 1* — 9q34.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NOTCH1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | notch receptor 1 |
| Also known as | — (no recorded alias) |
| Locus | 9q34.3 — gene with protein product |
| Gene families | Notch receptors; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NUP210L]], [[PER1]], [[PLCL2]], [[PRKD2]] |
| Previously named | Notch (Drosophila) homolog 1 (translocation-associated); Notch homolog 1, translocation-associated (Drosophila); notch 1 |

**Function**, from UniProt [P46531](https://www.uniprot.org/uniprotkb/P46531) (reviewed):

> Functions as a receptor for membrane-bound ligands Jagged-1 (JAG1), Jagged-2 (JAG2) and Delta-1 (DLL1) to regulate cell-fate determination. Upon ligand activation through the released notch intracellular domain (NICD) it forms a transcriptional activator complex with RBPJ/RBPSUH and activates genes of the enhancer of split locus. Affects the implementation of differentiation, proliferation and apoptotic programs. Involved in angiogenesis; negatively regulates endothelial cell proliferation and migration and angiogenic sprouting. Involved in the maturation of both CD4(+) and CD8(+) cells in the thymus. Important for follicular differentiation and possibly cell fate selection within the follicle. During cerebellar development, functions as a receptor for neuronal DNER and is involved in the differentiation of Bergmann glia. Represses neuronal and myogenic differentiation. May play an essential role in postimplantation development, probably in some aspect of cell specification and/or differentiation. May be involved in mesoderm development, somite formation and neurogenesis. May enhance HIF1A function by sequestering HIF1AN away from HIF1A. Required for the THBS4 function in regulating protective astrogenesis from the subventricular zone (SVZ) niche after injury. Involved in determination of left/right symmetry by modulating the balance between motile and immotile (sensory) cilia at the left-right organiser (LRO)

**Summary**, from NCBI Gene [4851](https://www.ncbi.nlm.nih.gov/gene/4851):

> This gene encodes a member of the NOTCH family of proteins. Members of this Type I transmembrane protein family share structural characteristics including an extracellular domain consisting of multiple epidermal growth factor-like (EGF) repeats, and an intracellular domain consisting of multiple different domain types. Notch signaling is an evolutionarily conserved intercellular signaling pathway that regulates interactions between physically adjacent cells through binding of Notch family receptors to their cognate ligands. The encoded preproprotein is proteolytically processed in the trans-Golgi network to generate two polypeptide chains that heterodimerize to form the mature cell-surface receptor. This receptor plays a role in the development of numerous cell and tissue types. Mutations in this gene are associated with aortic valve disease, Adams-Oliver syndrome, T-cell acute lymphoblastic leukemia, chronic lymphocytic leukemia, and head and neck squamous cell carcinoma. [provided by RefSeq, Jan 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7881) · Entrez [4851](https://www.ncbi.nlm.nih.gov/gene/4851) · UniProt [P46531](https://www.uniprot.org/uniprotkb/P46531) · Ensembl [ENSG00000148400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148400) · OMIM [190198](https://www.omim.org/entry/190198)

**PubMed**, as HGNC records for this gene — [1831692](https://pubmed.ncbi.nlm.nih.gov/1831692/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 21.66 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 53 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.041× |
| Wild-type minus altered | 1.086× |
| Compounds moving it up in WT lines | 64 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00218 |
| As a percentage | +0.15% |
| FDR, exposure-shuffle null | 0.6120 |
| In TP53-wild-type lines / altered lines | -0.00196 / 0.00474 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.290 raw, 0.099 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 53 targets |
| Activity vs MG53 across exposures (r) | 0.222 (q 5.72e-11) |
| With 3 principal components removed | 0.214 (q 4.67e-10) |
| Within line, across exposures (r) | 0.016 (q 0.243) |
| Percentile against all genes | 94.8 |

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
