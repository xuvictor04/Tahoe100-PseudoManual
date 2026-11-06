---
symbol: RAB6A
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: RAB6A, member RAS oncogene family
locus: 11q13.4
locus_type: gene with protein product
gene_family: [RAB, member RAS oncogene GTPases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 296.72
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RAB6A

*RAB6A, member RAS oncogene family* — 11q13.4

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RAB6A.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | RAB6A, member RAS oncogene family |
| Also known as | — (no recorded alias) |
| Locus | 11q13.4 — gene with protein product |
| Gene families | RAB, member RAS oncogene GTPases |

**Function**, from UniProt [P20340](https://www.uniprot.org/uniprotkb/P20340) (reviewed):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes (PubMed:25962623). Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (PubMed:25962623). RAB6A acts as a regulator of COPI-independent retrograde transport from the Golgi apparatus towards the endoplasmic reticulum (ER) (PubMed:25962623). Has a low GTPase activity (PubMed:25962623). Recruits VPS13B to the Golgi membrane (PubMed:25492866). Plays a role in neuron projection development (Probable)

**Summary**, from NCBI Gene [5870](https://www.ncbi.nlm.nih.gov/gene/5870):

> This gene encodes a member of the RAB family, which belongs to the small GTPase superfamily. GTPases of the RAB family bind to various effectors to regulate the targeting and fusion of transport carriers to acceptor compartments. This protein is located at the Golgi apparatus, which regulates trafficking in both a retrograde (from early endosomes and Golgi to the endoplasmic reticulum) and an anterograde (from the Golgi to the plasma membrane) directions. Myosin II is an effector of this protein in these processes. This protein is also involved in assembly of human cytomegalovirus (HCMV) by interacting with the cellular protein Bicaudal D1, which interacts with the HCMV virion tegument protein, pp150. Multiple alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Aug 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9786) · Entrez [5870](https://www.ncbi.nlm.nih.gov/gene/5870) · UniProt [P20340](https://www.uniprot.org/uniprotkb/P20340) · Ensembl [ENSG00000175582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175582) · OMIM [179513](https://www.omim.org/entry/179513)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 296.72 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 160 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.026× |
| Wild-type minus altered | 1.019× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00555 |
| As a percentage | -0.38% |
| FDR, exposure-shuffle null | 0.0132 |
| In TP53-wild-type lines / altered lines | -0.00294 / -0.00713 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.347 raw, -0.008 with 3 PCs removed |

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
