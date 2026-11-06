---
symbol: RETSAT
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ20296]
gene_name: retinol saturase
locus: 2p11.2
locus_type: gene with protein product
gene_family: [Flavoproteins, Oxidoreductases]
family_siblings_here: [DHDH, FDXR, SDHA, TP53I3]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 18.45
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RETSAT

*retinol saturase* — 2p11.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RETSAT.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | retinol saturase |
| Also known as | FLJ20296, all-trans-retinol 13,14-reductase |
| Locus | 2p11.2 — gene with protein product |
| Gene families | Flavoproteins; Oxidoreductases |
| Other genes here in those families | [[DHDH]], [[FDXR]], [[SDHA]], [[TP53I3]] |

**Function**, from UniProt [Q6NUM9](https://www.uniprot.org/uniprotkb/Q6NUM9) (reviewed):

> Catalyzes the saturation of all-trans-retinol to all-trans-13,14-dihydroretinol. Does not exhibit any activity toward all-trans-retinoic acid, nor 9-cis, 11-cis or 13-cis-retinol isomers. May play a role in the metabolism of vitamin A. Independently of retinol conversion, may regulate liver metabolism upstream of MLXIPL/ChREBP. May play a role in adipocyte differentiation

**Summary**, from NCBI Gene [54884](https://www.ncbi.nlm.nih.gov/gene/54884):

> Predicted to enable all-trans-retinol 13,14-reductase activity. Predicted to be involved in retinol metabolic process. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25991) · Entrez [54884](https://www.ncbi.nlm.nih.gov/gene/54884) · UniProt [Q6NUM9](https://www.uniprot.org/uniprotkb/Q6NUM9) · Ensembl [ENSG00000042445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042445) · OMIM [617597](https://www.omim.org/entry/617597)

**PubMed**, as HGNC records for this gene — [12975309](https://pubmed.ncbi.nlm.nih.gov/12975309/), [15358783](https://pubmed.ncbi.nlm.nih.gov/15358783/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 18.45 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 86 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.032× |
| Wild-type minus altered | 1.049× |
| Compounds moving it up in WT lines | 55 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00196 |
| As a percentage | -0.14% |
| FDR, exposure-shuffle null | 0.4510 |
| In TP53-wild-type lines / altered lines | 0.00120 / -0.00388 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.082 raw, -0.114 with 3 PCs removed |

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
