---
symbol: EPHA2
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: EPH receptor A2
locus: 1p36.13
locus_type: gene with protein product
gene_family: [Sterile alpha motif domain containing, EPH receptors]
family_siblings_here: [TNKS]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 51.06
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# EPHA2

*EPH receptor A2* — 1p36.13

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/EPHA2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | EPH receptor A2 |
| Also known as | — (no recorded alias) |
| Locus | 1p36.13 — gene with protein product |
| Gene families | Sterile alpha motif domain containing; EPH receptors |
| Other genes here in those families | [[TNKS]] |
| Previously named | EphA2 |

**Function**, from UniProt [P29317](https://www.uniprot.org/uniprotkb/P29317) (reviewed):

> Receptor tyrosine kinase which binds promiscuously membrane-bound ephrin-A family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Activated by the ligand ephrin-A1/EFNA1 regulates migration, integrin-mediated adhesion, proliferation and differentiation of cells. Regulates cell adhesion and differentiation through DSG1/desmoglein-1 and inhibition of the ERK1/ERK2 (MAPK3/MAPK1, respectively) signaling pathway. May also participate in UV radiation-induced apoptosis and have a ligand-independent stimulatory effect on chemotactic cell migration. During development, may function in distinctive aspects of pattern formation and subsequently in development of several fetal tissues. Involved for instance in angiogenesis, in early hindbrain development and epithelial proliferation and branching morphogenesis during mammary gland development. Engaged by the ligand ephrin-A5/EFNA5 may regulate lens fiber cells shape and interactions and be important for lens transparency development and maintenance. With ephrin-A2/EFNA2 may play a role in bone remodeling through regulation of osteoclastogenesis and osteoblastogenesis

**Summary**, from NCBI Gene [1969](https://www.ncbi.nlm.nih.gov/gene/1969):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their affinities for binding ephrin-A and ephrin-B ligands. This gene encodes a protein that binds ephrin-A ligands. Mutations in this gene are the cause of certain genetically-related cataract disorders.[provided by RefSeq, May 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:3386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3386) · Entrez [1969](https://www.ncbi.nlm.nih.gov/gene/1969) · UniProt [P29317](https://www.uniprot.org/uniprotkb/P29317) · Ensembl [ENSG00000142627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142627) · OMIM [176946](https://www.omim.org/entry/176946)

**PubMed**, as HGNC records for this gene — [9119409](https://pubmed.ncbi.nlm.nih.gov/9119409/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 51.06 CPM |
| Lines where detected | 47 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 75 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.054× |
| Wild-type minus altered | 1.075× |
| Compounds moving it up in WT lines | 54 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01174 |
| As a percentage | +0.82% |
| FDR, exposure-shuffle null | 0.0125 |
| In TP53-wild-type lines / altered lines | 0.01039 / 0.01255 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.307 raw, 0.198 with 3 PCs removed |

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
