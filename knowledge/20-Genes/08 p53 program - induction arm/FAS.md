---
symbol: FAS
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [CD95, APO-1]
gene_name: Fas cell surface death receptor
locus: 10q23.31
locus_type: gene with protein product
gene_family: [CD molecules, Tumor necrosis factor receptor superfamily, Death inducing signaling complex]
family_siblings_here: [EDA2R, SELPLG, TNFRSF10B]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 20.98
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FAS

*Fas cell surface death receptor* — 10q23.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FAS.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | Fas cell surface death receptor |
| Also known as | CD95, APO-1, TNF receptor superfamily member 6 |
| Locus | 10q23.31 — gene with protein product |
| Gene families | CD molecules; Tumor necrosis factor receptor superfamily; Death inducing signaling complex |
| Other genes here in those families | [[EDA2R]], [[SELPLG]], [[TNFRSF10B]] |
| Previously named | tumor necrosis factor receptor superfamily, member 6; Fas (TNF receptor superfamily, member 6) |

**Function**, from UniProt [P25445](https://www.uniprot.org/uniprotkb/P25445) (reviewed):

> Receptor for TNFSF6/FASLG. The adapter molecule FADD recruits caspase CASP8 to the activated receptor. The resulting death-inducing signaling complex (DISC) performs CASP8 proteolytic activation which initiates the subsequent cascade of caspases (aspartate-specific cysteine proteases) mediating apoptosis. FAS-mediated apoptosis may have a role in the induction of peripheral tolerance, in the antigen-stimulated suicide of mature T-cells, or both. The secreted isoforms 2 to 6 block apoptosis (in vitro)

**Summary**, from NCBI Gene [355](https://www.ncbi.nlm.nih.gov/gene/355):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor contains a death domain. It has been shown to play a central role in the physiological regulation of programmed cell death, and has been implicated in the pathogenesis of various malignancies and diseases of the immune system. The interaction of this receptor with its ligand allows the formation of a death-inducing signaling complex that includes Fas-associated death domain protein (FADD), caspase 8, and caspase 10. The autoproteolytic processing of the caspases in the complex triggers a downstream caspase cascade, and leads to apoptosis. This receptor has been also shown to activate NF-kappaB, MAPK3/ERK1, and MAPK8/JNK, and is found to be involved in transducing the proliferating signals in normal diploid fibroblast and T cells. Several alternatively spliced transcript variants have been described, some of which are candidates for nonsense-mediated mRNA decay (NMD). The isoforms lacking the transmembrane domain may negatively regulate the apoptosis mediated by the full length isoform. [provided by RefSeq, Mar 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11920) · Entrez [355](https://www.ncbi.nlm.nih.gov/gene/355) · UniProt [P25445](https://www.uniprot.org/uniprotkb/P25445) · Ensembl [ENSG00000026103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026103) · OMIM [134637](https://www.omim.org/entry/134637)

**PubMed**, as HGNC records for this gene — [1385299](https://pubmed.ncbi.nlm.nih.gov/1385299/), [1385309](https://pubmed.ncbi.nlm.nih.gov/1385309/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 20.98 CPM |
| Lines where detected | 46 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 65 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.176× |
| Wild-type minus altered | 1.133× |
| Compounds moving it up in WT lines | 89 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 6.50e-06 |
| As a percentage | +0.00% |
| FDR, exposure-shuffle null | 0.9986 |
| In TP53-wild-type lines / altered lines | -0.00482 / 0.00316 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.206 raw, 0.131 with 3 PCs removed |

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
