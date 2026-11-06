---
symbol: PPM1A
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MGC9201, PP2Calpha, PP2CA]
gene_name: protein phosphatase, Mg2+/Mn2+ dependent 1A
locus: 14q23.1
locus_type: gene with protein product
gene_family: [Protein phosphatases, Mg2+/Mn2+ dependent]
family_siblings_here: [PPM1D]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 76.94
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PPM1A

*protein phosphatase, Mg2+/Mn2+ dependent 1A* — 14q23.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PPM1A.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | protein phosphatase, Mg2+/Mn2+ dependent 1A |
| Also known as | MGC9201, PP2Calpha, PP2CA, phosphatase 2C alpha, protein phosphatase 2C, alpha isoform |
| Locus | 14q23.1 — gene with protein product |
| Gene families | Protein phosphatases, Mg2+/Mn2+ dependent |
| Other genes here in those families | [[PPM1D]] |
| Previously named | protein phosphatase 1A (formerly 2C), magnesium-dependent, alpha isoform; protein phosphatase, Mg2+/Mn2+ dependent, 1A |

**Function**, from UniProt [P35813](https://www.uniprot.org/uniprotkb/P35813) (reviewed):

> Enzyme with a broad specificity. Negatively regulates TGF-beta signaling through dephosphorylating SMAD2 and SMAD3, resulting in their dissociation from SMAD4, nuclear export of the SMADs and termination of the TGF-beta-mediated signaling. Dephosphorylates PRKAA1 and PRKAA2. Plays an important role in the termination of TNF-mediated NF-kappa-B activation through dephosphorylating and inactivating IKBKB/IKKB

**Summary**, from NCBI Gene [5494](https://www.ncbi.nlm.nih.gov/gene/5494):

> The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase dephosphorylates, and negatively regulates the activities of, MAP kinases and MAP kinase kinases. It has been shown to inhibit the activation of p38 and JNK kinase cascades induced by environmental stresses. This phosphatase can also dephosphorylate cyclin-dependent kinases, and thus may be involved in cell cycle control. Overexpression of this phosphatase is reported to activate the expression of the tumor suppressor gene TP53/p53, which leads to G2/M cell cycle arrest and apoptosis. Three alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9275) · Entrez [5494](https://www.ncbi.nlm.nih.gov/gene/5494) · UniProt [P35813](https://www.uniprot.org/uniprotkb/P35813) · Ensembl [ENSG00000100614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100614) · OMIM [606108](https://www.omim.org/entry/606108)

**PubMed**, as HGNC records for this gene — [1311954](https://pubmed.ncbi.nlm.nih.gov/1311954/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 76.94 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 92 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.050× |
| Wild-type minus altered | 1.035× |
| Compounds moving it up in WT lines | 65 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00246 |
| As a percentage | -0.17% |
| FDR, exposure-shuffle null | 0.1254 |
| In TP53-wild-type lines / altered lines | -0.00529 / -0.00074 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.307 raw, -0.169 with 3 PCs removed |

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
