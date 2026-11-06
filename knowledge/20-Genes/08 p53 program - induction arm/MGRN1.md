---
symbol: MGRN1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0544, RNF156]
gene_name: mahogunin ring finger 1
locus: 16p13.3
locus_type: gene with protein product
gene_family: [Ring finger proteins, MicroRNA protein coding host genes, RING finger E3 ubiquitin protein ligases]
family_siblings_here: [AEN, ATF5, BBC3, COP1, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MDM2, MDM4, NADSYN1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 63.52
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# MGRN1

*mahogunin ring finger 1* — 16p13.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MGRN1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | mahogunin ring finger 1 |
| Also known as | KIAA0544, RNF156 |
| Locus | 16p13.3 — gene with protein product |
| Gene families | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[COP1]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MDM2]], [[MDM4]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]] |
| Previously named | mahogunin, ring finger 1; mahogunin ring finger 1, E3 ubiquitin protein ligase |

**Function**, from UniProt [O60291](https://www.uniprot.org/uniprotkb/O60291) (reviewed):

> E3 ubiquitin-protein ligase, which mediates ubiquitination of target proteins, such as MC1R, MC4R, smoothened (SMO) and TSG101 (PubMed:17229889, PubMed:19703557, PubMed:24556679). Catalytic component of the MMM ubiquitin ligase complex, a multiprotein complex that acts as a negative regulator of smoothened signaling pathway by mediating the ubiquitination and degradation of SMO in primary cilia (PubMed:42190653). Catalytic component of a membrane-tethered ubiquitin ligase complex that acts as a negative regulator of melanocortin receptor signaling by mediating ubiquitination of MC1R and MC4R (By similarity). Mediates monoubiquitination at multiple sites of TSG101 in the presence of UBE2D1, thereby playing a role in the regulation of endosome-to-lysosome trafficking (PubMed:17229889, PubMed:19703557). Also acts as a regulator of transcription in aged neurons: translocates into the nucleus in response to proteotoxic stress and associates with ATF3 to potentiate the ATF3-mediated response to proteotoxic stress (PubMed:28475871). Acts as a regulator of microtubule polymerization by mediating 'Lys-6'-linked ubiquitination of alpha-tubulin (PubMed:24556679, PubMed:28902452). Involved in the degradation of misfolded protein aggregates via autophagy (PubMed:23756845)

**Summary**, from NCBI Gene [23295](https://www.ncbi.nlm.nih.gov/gene/23295):

> Enables protein sequestering activity and ubiquitin-protein transferase activity. Involved in endosome to lysosome transport; negative regulation of adenylate cyclase-activating G protein-coupled receptor signaling pathway; and protein monoubiquitination. Located in early endosome; nucleus; and plasma membrane. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:20254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20254) · Entrez [23295](https://www.ncbi.nlm.nih.gov/gene/23295) · UniProt [O60291](https://www.uniprot.org/uniprotkb/O60291) · Ensembl [ENSG00000102858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102858) · OMIM [607559](https://www.omim.org/entry/607559)

**PubMed**, as HGNC records for this gene — [9628581](https://pubmed.ncbi.nlm.nih.gov/9628581/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 63.52 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 76 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.033× |
| Wild-type minus altered | 1.033× |
| Compounds moving it up in WT lines | 76 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00095 |
| As a percentage | +0.07% |
| FDR, exposure-shuffle null | 0.6726 |
| In TP53-wild-type lines / altered lines | -0.00152 / 0.00245 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.061 raw, 0.178 with 3 PCs removed |

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
