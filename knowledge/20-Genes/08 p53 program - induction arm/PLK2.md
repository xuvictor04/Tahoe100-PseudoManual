---
symbol: PLK2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [SNK]
gene_name: polo like kinase 2
locus: 5q11.2
locus_type: gene with protein product
gene_family: [Polo like kinase family]
family_siblings_here: [PLK3]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 75.01
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PLK2

*polo like kinase 2* — 5q11.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PLK2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | polo like kinase 2 |
| Also known as | SNK, serum-inducible kinase |
| Locus | 5q11.2 — gene with protein product |
| Gene families | Polo like kinase family |
| Other genes here in those families | [[PLK3]] |
| Previously named | polo-like kinase 2 (Drosophila); polo-like kinase 2 |

**Function**, from UniProt [Q9NYY3](https://www.uniprot.org/uniprotkb/Q9NYY3) (reviewed):

> Tumor suppressor serine/threonine-protein kinase involved in synaptic plasticity, centriole duplication and G1/S phase transition. Polo-like kinases act by binding and phosphorylating proteins that are already phosphorylated on a specific motif recognized by the POLO box domains. Phosphorylates CPAP, NPM1, RAPGEF2, RASGRF1, SNCA, SIPA1L1 and SYNGAP1. Plays a key role in synaptic plasticity and memory by regulating the Ras and Rap protein signaling: required for overactivity-dependent spine remodeling by phosphorylating the Ras activator RASGRF1 and the Rap inhibitor SIPA1L1 leading to their degradation by the proteasome. Conversely, phosphorylates the Rap activator RAPGEF2 and the Ras inhibitor SYNGAP1, promoting their activity. Also regulates synaptic plasticity independently of kinase activity, via its interaction with NSF that disrupts the interaction between NSF and the GRIA2 subunit of AMPARs, leading to a rapid rundown of AMPAR-mediated current that occludes long term depression. Required for procentriole formation and centriole duplication by phosphorylating CPAP and NPM1, respectively. Its induction by p53/TP53 suggests that it may participate in the mitotic checkpoint following stress

**Summary**, from NCBI Gene [10769](https://www.ncbi.nlm.nih.gov/gene/10769):

> The protein encoded by this gene is a member of the polo family of serine/threonine protein kinases that have a role in normal cell division. This gene is most abundantly expressed in testis, spleen and fetal tissues, and its expression is inducible by serum, suggesting that it may also play an important role in cells undergoing rapid cell division. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19699) · Entrez [10769](https://www.ncbi.nlm.nih.gov/gene/10769) · UniProt [Q9NYY3](https://www.uniprot.org/uniprotkb/Q9NYY3) · Ensembl [ENSG00000145632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145632) · OMIM [607023](https://www.omim.org/entry/607023)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 75.01 CPM |
| Lines where detected | 46 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 134 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.081× |
| Wild-type minus altered | 1.078× |
| Compounds moving it up in WT lines | 58 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01259 |
| As a percentage | +0.88% |
| FDR, exposure-shuffle null | 0.0233 |
| In TP53-wild-type lines / altered lines | 0.01638 / 0.01019 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.327 raw, 0.123 with 3 PCs removed |

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
