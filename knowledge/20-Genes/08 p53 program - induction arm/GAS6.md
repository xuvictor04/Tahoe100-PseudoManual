---
symbol: GAS6
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [AXSF, FLJ34709, DKFZp666G247]
gene_name: growth arrest specific 6
locus: 13q34
locus_type: gene with protein product
gene_family: [Gla domain containing]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 12.42
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# GAS6

*growth arrest specific 6* — 13q34

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/GAS6.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | growth arrest specific 6 |
| Also known as | AXSF, FLJ34709, DKFZp666G247, AXL stimulatory factor |
| Locus | 13q34 — gene with protein product |
| Gene families | Gla domain containing |
| Previously named | AXL receptor tyrosine kinase ligand |

**Function**, from UniProt [Q14393](https://www.uniprot.org/uniprotkb/Q14393) (reviewed):

> Ligand for tyrosine-protein kinase receptors AXL, TYRO3 and MER whose signaling is implicated in cell growth and survival, cell adhesion and cell migration (PubMed:7867073). GAS6/AXL signaling plays a role in various processes such as endothelial cell survival during acidification by preventing apoptosis, optimal cytokine signaling during human natural killer cell development, hepatic regeneration, gonadotropin-releasing hormone neuron survival and migration, platelet activation, or regulation of thrombotic responses (PubMed:12364394, PubMed:18840707)

**Summary**, from NCBI Gene [2621](https://www.ncbi.nlm.nih.gov/gene/2621):

> This gene encodes a gamma-carboxyglutamic acid (Gla)-containing protein thought to be involved in the stimulation of cell proliferation. This gene is frequently overexpressed in many cancers and has been implicated as an adverse prognostic marker. Elevated protein levels are additionally associated with a variety of disease states, including venous thromboembolic disease, systemic lupus erythematosus, chronic renal failure, and preeclampsia. [provided by RefSeq, Aug 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4168) · Entrez [2621](https://www.ncbi.nlm.nih.gov/gene/2621) · UniProt [Q14393](https://www.uniprot.org/uniprotkb/Q14393) · Ensembl [ENSG00000183087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183087) · OMIM [600441](https://www.omim.org/entry/600441)

**PubMed**, as HGNC records for this gene — [8336730](https://pubmed.ncbi.nlm.nih.gov/8336730/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 12.42 CPM |
| Lines where detected | 43 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 112 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.048× |
| Wild-type minus altered | 1.062× |
| Compounds moving it up in WT lines | 66 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00194 |
| As a percentage | -0.13% |
| FDR, exposure-shuffle null | 0.7675 |
| In TP53-wild-type lines / altered lines | -0.00506 / 0.00008 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.097 raw, -0.037 with 3 PCs removed |

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
