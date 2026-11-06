---
symbol: GRIN2C
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [NMDAR2C]
gene_name: glutamate ionotropic receptor NMDA type subunit 2C
locus: 17q25.1
locus_type: gene with protein product
gene_family: [Glutamate ionotropic receptor NMDA type subunits]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 2.08
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# GRIN2C

*glutamate ionotropic receptor NMDA type subunit 2C* — 17q25.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/GRIN2C.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | glutamate ionotropic receptor NMDA type subunit 2C |
| Also known as | GluN2C, NR2C |
| Locus | 17q25.1 — gene with protein product |
| Gene families | Glutamate ionotropic receptor NMDA type subunits |
| Previously named | glutamate receptor, ionotropic, N-methyl D-aspartate 2C |

**Function**, from UniProt [Q14957](https://www.uniprot.org/uniprotkb/Q14957) (reviewed):

> Component of N-methyl-D-aspartate (NMDA) receptors (NMDARs) that function as heterotetrameric, ligand-gated cation channels with high calcium permeability and voltage-dependent block by Mg(2+) (PubMed:26875626, PubMed:36309015). Participates in synaptic plasticity for learning and memory formation by contributing to the slow phase of excitatory postsynaptic current and long-term synaptic potentiation (By similarity). Channel activation requires binding of the neurotransmitter L-glutamate to the GluN2 subunit, glycine or D-serine binding to the GluN1 subunit, plus membrane depolarization to eliminate channel inhibition by Mg(2+) (PubMed:26875626, PubMed:36309015). NMDARs mediate simultaneously the potassium efflux and the influx of calcium and sodium (By similarity). Each GluN2 subunit confers differential attributes to channel properties, including activation, deactivation and desensitization kinetics, pH sensitivity, Ca2(+) permeability, and binding to allosteric modulators (PubMed:26875626)

**Summary**, from NCBI Gene [2905](https://www.ncbi.nlm.nih.gov/gene/2905):

> This gene encodes a subunit of the N-methyl-D-aspartate (NMDA) receptor, which is a subtype of ionotropic glutamate receptor. NMDA receptors are found in the central nervous system, are permeable to cations and have an important role in physiological processes such as learning, memory, and synaptic development. The receptor is a tetramer of different subunits (typically heterodimer of subunit 1 with one or more of subunits 2A-D), forming a channel that is permeable to calcium, potassium, and sodium, and whose properties are determined by subunit composition. Alterations in the subunit composition of the receptor are associated with pathophysiological conditions such as Parkinson's disease, Alzheimer's disease, depression, and schizophrenia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4587) · Entrez [2905](https://www.ncbi.nlm.nih.gov/gene/2905) · UniProt [Q14957](https://www.uniprot.org/uniprotkb/Q14957) · Ensembl [ENSG00000161509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161509) · OMIM [138254](https://www.omim.org/entry/138254)

**PubMed**, as HGNC records for this gene — [9480759](https://pubmed.ncbi.nlm.nih.gov/9480759/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 2.08 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 24 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.244× |
| Wild-type minus altered | 1.331× |
| Compounds moving it up in WT lines | 78 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.05109 |
| As a percentage | +3.61% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.05602 / 0.04795 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.489 raw, 0.345 with 3 PCs removed |

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
