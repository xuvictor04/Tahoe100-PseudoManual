---
symbol: ZFPM1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PRDM18, FOG1, FOG, ZNF89A]
gene_name: zinc finger protein, FOG family member 1
locus: 16q24.2
locus_type: gene with protein product
gene_family: [Zinc fingers C2H2-type, PR/SET domain family, MicroRNA protein coding host genes, Zinc fingers FOG C2HC-type, Putative lysine methyltransferases]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, HIVEP2, MGRN1, NADSYN1, NOTCH1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 17.97
mg53_verdict: none
tags: [gene, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ZFPM1

*zinc finger protein, FOG family member 1* — 16q24.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ZFPM1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | zinc finger protein, FOG family member 1 |
| Also known as | PRDM18, FOG1, FOG, ZNF89A, PR/SET domain 18 |
| Locus | 16q24.2 — gene with protein product |
| Gene families | Zinc fingers C2H2-type; PR/SET domain family; MicroRNA protein coding host genes; Zinc fingers FOG C2HC-type; Putative lysine methyltransferases |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[HIVEP2]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]] |
| Previously named | zinc finger protein, multitype 1 |

**Function**, from UniProt [Q8IX07](https://www.uniprot.org/uniprotkb/Q8IX07) (reviewed):

> Transcription regulator that plays an essential role in erythroid and megakaryocytic cell differentiation. Essential cofactor that acts via the formation of a heterodimer with transcription factors of the GATA family GATA1, GATA2 and GATA3. Such heterodimer can both activate or repress transcriptional activity, depending on the cell and promoter context. The heterodimer formed with GATA proteins is essential to activate expression of genes such as NFE2, ITGA2B, alpha- and beta-globin, while it represses expression of KLF1. May be involved in regulation of some genes in gonads. May also be involved in cardiac development, in a non-redundant way with ZFPM2/FOG2 (By similarity)

**Summary**, from NCBI Gene [161882](https://www.ncbi.nlm.nih.gov/gene/161882):

> Enables RNA polymerase II-specific DNA-binding transcription factor binding activity and transcription corepressor activity. Involved in platelet formation; regulation of definitive erythrocyte differentiation; and regulation of gene expression. Part of transcription repressor complex. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19762) · Entrez [161882](https://www.ncbi.nlm.nih.gov/gene/161882) · UniProt [Q8IX07](https://www.uniprot.org/uniprotkb/Q8IX07) · Ensembl [ENSG00000179588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179588) · OMIM [601950](https://www.omim.org/entry/601950)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 17.97 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 39 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.089× |
| Wild-type minus altered | 1.113× |
| Compounds moving it up in WT lines | 73 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00232 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.6061 |
| In TP53-wild-type lines / altered lines | 0.00408 / 0.00125 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.073 raw, 0.025 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 9 targets |
| Activity vs MG53 across exposures (r) | 0.021 (q 0.579) |
| With 3 principal components removed | 0.072 (q 0.035) |
| Within line, across exposures (r) | 0.011 (q 0.506) |
| Percentile against all genes | 69.3 |

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
