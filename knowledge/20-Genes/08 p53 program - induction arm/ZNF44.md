---
symbol: ZNF44
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KOX7, ZNF504]
gene_name: zinc finger protein 44
locus: 19p13.2
locus_type: gene with protein product
gene_family: [Zinc fingers C2H2-type, KRAB domain containing]
family_siblings_here: [HIVEP2, ZFPM1, ZNF195, ZNF37A, ZNF423, ZNF654, ZNF79, ZNF91]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 27.1
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ZNF44

*zinc finger protein 44* — 19p13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ZNF44.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | zinc finger protein 44 |
| Also known as | KOX7, ZNF504 |
| Locus | 19p13.2 — gene with protein product |
| Gene families | Zinc fingers C2H2-type; KRAB domain containing |
| Other genes here in those families | [[HIVEP2]], [[ZFPM1]], [[ZNF195]], [[ZNF37A]], [[ZNF423]], [[ZNF654]], [[ZNF79]], [[ZNF91]] |
| Previously named | zinc finger protein 58; zinc finger protein 44 (KOX 7); zinc finger protein 55 |

**Function**, from UniProt [P15621](https://www.uniprot.org/uniprotkb/P15621) (reviewed):

> May be involved in transcriptional regulation

**Summary**, from NCBI Gene [51710](https://www.ncbi.nlm.nih.gov/gene/51710):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13110) · Entrez [51710](https://www.ncbi.nlm.nih.gov/gene/51710) · UniProt [P15621](https://www.uniprot.org/uniprotkb/P15621) · Ensembl [ENSG00000197857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197857) · OMIM [194542](https://www.omim.org/entry/194542)

**PubMed**, as HGNC records for this gene — [1946370](https://pubmed.ncbi.nlm.nih.gov/1946370/), [1505991](https://pubmed.ncbi.nlm.nih.gov/1505991/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 27.10 CPM |
| Lines where detected | 46 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 153 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.071× |
| Wild-type minus altered | 1.026× |
| Compounds moving it up in WT lines | 62 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00534 |
| As a percentage | -0.37% |
| FDR, exposure-shuffle null | 0.0915 |
| In TP53-wild-type lines / altered lines | 0.00078 / -0.00825 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.146 raw, -0.137 with 3 PCs removed |

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
