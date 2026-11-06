---
symbol: ZFYVE1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DFCP1, KIAA1589, TAFF1, PPP1R172]
gene_name: zinc finger FYVE-type containing 1
locus: 14q24.2
locus_type: gene with protein product
gene_family: [Zinc fingers FYVE-type]
family_siblings_here: [PIKFYVE]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 40.67
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ZFYVE1

*zinc finger FYVE-type containing 1* — 14q24.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ZFYVE1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | zinc finger FYVE-type containing 1 |
| Also known as | DFCP1, KIAA1589, TAFF1, PPP1R172, protein phosphatase 1, regulatory subunit 172 |
| Locus | 14q24.2 — gene with protein product |
| Gene families | Zinc fingers FYVE-type |
| Other genes here in those families | [[PIKFYVE]] |
| Previously named | zinc finger protein, subfamily 2A (FYVE domain containing), 1; zinc finger, FYVE domain containing 1 |

**Function**, from UniProt [Q9HBF4](https://www.uniprot.org/uniprotkb/Q9HBF4) (reviewed):

> Plays a role in the formation of lipid droplets (LDs) which are storage organelles at the center of lipid and energy homeostasis (PubMed:30970241). Regulates the morphology, size and distribution of LDs (PubMed:30970241, PubMed:31293035). Mediates the formation of endoplasmic reticulum-lipid droplets (ER-LD) contacts by forming a complex with RAB18 and ZW10 (PubMed:30970241). Binds to phosphatidylinositol 3-phosphate (PtdIns3P) through FYVE-type zinc finger (PubMed:11256955, PubMed:11739631)

**Summary**, from NCBI Gene [53349](https://www.ncbi.nlm.nih.gov/gene/53349):

> The FYVE domain mediates the recruitment of proteins involved in membrane trafficking and cell signaling to phosphatidylinositol 3-phosphate-containing membranes. This protein contains two zinc-binding FYVE domains in tandem and is reported to localize to the Golgi apparatus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13180) · Entrez [53349](https://www.ncbi.nlm.nih.gov/gene/53349) · UniProt [Q9HBF4](https://www.uniprot.org/uniprotkb/Q9HBF4) · Ensembl [ENSG00000165861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165861) · OMIM [605471](https://www.omim.org/entry/605471)

**PubMed**, as HGNC records for this gene — [11024279](https://pubmed.ncbi.nlm.nih.gov/11024279/), [11256955](https://pubmed.ncbi.nlm.nih.gov/11256955/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 40.67 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 46 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.090× |
| Wild-type minus altered | 1.049× |
| Compounds moving it up in WT lines | 85 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00383 |
| As a percentage | -0.27% |
| FDR, exposure-shuffle null | 0.2150 |
| In TP53-wild-type lines / altered lines | 0.00024 / -0.00630 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.068 raw, -0.098 with 3 PCs removed |

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
