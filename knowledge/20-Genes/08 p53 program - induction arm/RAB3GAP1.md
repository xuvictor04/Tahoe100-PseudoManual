---
symbol: RAB3GAP1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [RAB3GAP, KIAA0066, RAB3GAP130, WARBM1]
gene_name: RAB3 GTPase activating protein catalytic subunit 1
locus: 2q21.3
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 234.31
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RAB3GAP1

*RAB3 GTPase activating protein catalytic subunit 1* — 2q21.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RAB3GAP1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | RAB3 GTPase activating protein catalytic subunit 1 |
| Also known as | RAB3GAP, KIAA0066, RAB3GAP130, WARBM1 |
| Locus | 2q21.3 — gene with protein product |
| Previously named | RAB3 GTPase activating protein subunit 1 (catalytic) |

**Function**, from UniProt [Q15042](https://www.uniprot.org/uniprotkb/Q15042) (reviewed):

> Catalytic subunit of the Rab3 GTPase-activating (Rab3GAP) complex composed of RAB3GAP1 and RAB3GAP2, which accelerates the otherwise slow GTP hydrolysis catalyzed by Rab proteins (PubMed:9030515, PubMed:10859313, PubMed:39779760). Has GTPase-activating protein (GAP) activity towards various Rab3 subfamily members (RAB3A, RAB3B, RAB3C and RAB3D), RAB5A and RAB43 (PubMed:10859313, PubMed:9030515, PubMed:39779760). Additionally, it has guanine nucleotide exchange factor (GEF) activity towards RAB18, promoting GDP release from RAB18 and the conversion of inactive RAB18-GDP to the active form RAB18-GTP (PubMed:24891604, PubMed:39779760). Recruits and stabilizes RAB18 at the cis-Golgi membrane in fibroblasts where RAB18 is most likely activated (PubMed:26063829). Also involved in RAB18 recruitment at the endoplasmic reticulum (ER) membrane where it maintains proper ER structure (PubMed:24891604). Required for normal eye and brain development (PubMed:15696165, PubMed:23420520). May participate in neurodevelopmental processes such as cell proliferation, migration and differentiation before synapse formation, and is involved in regulating non-synaptic vesicular release of neurotransmitters (PubMed:9030515, PubMed:9852129)

**Summary**, from NCBI Gene [22930](https://www.ncbi.nlm.nih.gov/gene/22930):

> This gene encodes the catalytic subunit of a Rab GTPase activating protein. The encoded protein forms a heterodimer with a non-catalytic subunit to specifically regulate the activity of members of the Rab3 subfamily of small G proteins. This protein mediates the hydrolysis of GTP bound Rab3 to the GDP bound form. Mutations in this gene are associated with Warburg micro syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Feb 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17063) · Entrez [22930](https://www.ncbi.nlm.nih.gov/gene/22930) · UniProt [Q15042](https://www.uniprot.org/uniprotkb/Q15042) · Ensembl [ENSG00000115839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115839) · OMIM [602536](https://www.omim.org/entry/602536)

**PubMed**, as HGNC records for this gene — [9030515](https://pubmed.ncbi.nlm.nih.gov/9030515/), [15696165](https://pubmed.ncbi.nlm.nih.gov/15696165/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 234.31 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 151 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.076× |
| Wild-type minus altered | 1.021× |
| Compounds moving it up in WT lines | 79 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00028 |
| As a percentage | -0.02% |
| FDR, exposure-shuffle null | 0.9201 |
| In TP53-wild-type lines / altered lines | 0.00453 / -0.00320 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.008 raw, -0.122 with 3 PCs removed |

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
