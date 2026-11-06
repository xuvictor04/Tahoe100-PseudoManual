---
symbol: NAP1L4
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [NAP2]
gene_name: nucleosome assembly protein 1 like 4
locus: 11p15.4
locus_type: gene with protein product
gene_family: [Small nucleolar RNA protein coding host genes, Nucleosome assembly protein 1 like family]
family_siblings_here: [COP1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 186.06
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# NAP1L4

*nucleosome assembly protein 1 like 4* — 11p15.4

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NAP1L4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | nucleosome assembly protein 1 like 4 |
| Also known as | NAP2 |
| Locus | 11p15.4 — gene with protein product |
| Gene families | Small nucleolar RNA protein coding host genes; Nucleosome assembly protein 1 like family |
| Other genes here in those families | [[COP1]] |
| Previously named | nucleosome assembly protein 1-like 4 |

**Function**, from UniProt [Q99733](https://www.uniprot.org/uniprotkb/Q99733) (reviewed):

> Acts as a histone chaperone in nucleosome assembly

**Summary**, from NCBI Gene [4676](https://www.ncbi.nlm.nih.gov/gene/4676):

> This gene encodes a member of the nucleosome assembly protein (NAP) family which can interact with both core and linker histones. It can shuttle between the cytoplasm and nucleus, suggesting a role as a histone chaperone. This gene is one of several located near the imprinted gene domain of 11p15.5, an important tumor-suppressor gene region. Alterations in this region have been associated with the Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocortical carcinoma, and lung, ovarian, and breast cancer. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7640) · Entrez [4676](https://www.ncbi.nlm.nih.gov/gene/4676) · UniProt [Q99733](https://www.uniprot.org/uniprotkb/Q99733) · Ensembl [ENSG00000205531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205531) · OMIM [601651](https://www.omim.org/entry/601651)

**PubMed**, as HGNC records for this gene — [8923002](https://pubmed.ncbi.nlm.nih.gov/8923002/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 186.06 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 167 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.042× |
| Wild-type minus altered | 1.017× |
| Compounds moving it up in WT lines | 72 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00429 |
| As a percentage | -0.30% |
| FDR, exposure-shuffle null | 0.0133 |
| In TP53-wild-type lines / altered lines | 0.00033 / -0.00710 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.126 raw, -0.020 with 3 PCs removed |

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
