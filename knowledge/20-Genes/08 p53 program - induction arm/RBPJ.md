---
symbol: RBPJ
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [SUH, IGKJRB, RBPJK, KBF2, RBP-J, CBF1]
gene_name: recombination signal binding protein for immunoglobulin kappa J region
locus: 4p15.2
locus_type: gene with protein product
gene_family: [PTF1 complex, IPT domain containing]
family_siblings_here: [PLXNB2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 411.23
mg53_verdict: none
tags: [gene, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# RBPJ

*recombination signal binding protein for immunoglobulin kappa J region* — 4p15.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RBPJ.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | recombination signal binding protein for immunoglobulin kappa J region |
| Also known as | SUH, IGKJRB, RBPJK, KBF2, RBP-J, CBF1, suppressor of hairless homolog (Drosophila), CSL family DNA binding factor 1 |
| Locus | 4p15.2 — gene with protein product |
| Gene families | PTF1 complex; IPT domain containing |
| Other genes here in those families | [[PLXNB2]] |
| Previously named | recombining binding protein suppressor of hairless (Drosophila) |

**Function**, from UniProt [Q06330](https://www.uniprot.org/uniprotkb/Q06330) (reviewed):

> Transcriptional regulator that plays a central role in Notch signaling, a signaling pathway involved in cell-cell communication that regulates a broad spectrum of cell-fate determinations (PubMed:41086914, PubMed:36129980). Acts as a transcriptional repressor when it is not associated with Notch proteins. When associated with some NICD product of Notch proteins (Notch intracellular domain), it acts as a transcriptional activator that activates transcription of Notch target genes. Probably represses or activates transcription via the recruitment of chromatin remodeling complexes containing histone deacetylase or histone acetylase proteins, respectively. Specifically binds to the immunoglobulin kappa-type J segment recombination signal sequence. Binds specifically to methylated DNA (PubMed:21991380). Binds to the oxygen responsive element of COX4I2 and activates its transcription under hypoxia conditions (4% oxygen) (PubMed:23303788). Negatively regulates the phagocyte oxidative burst in response to bacterial infection by repressing transcription of NADPH oxidase subunits (By similarity)

**Summary**, from NCBI Gene [3516](https://www.ncbi.nlm.nih.gov/gene/3516):

> The protein encoded by this gene is a transcriptional regulator important in the Notch signaling pathway. The encoded protein acts as a repressor when not bound to Notch proteins and an activator when bound to Notch proteins. It is thought to function by recruiting chromatin remodeling complexes containing histone deacetylase or histone acetylase proteins to Notch signaling pathway genes. Several transcript variants encoding different isoforms have been found for this gene, and several pseudogenes of this gene exist on chromosome 9. [provided by RefSeq, Oct 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:5724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5724) · Entrez [3516](https://www.ncbi.nlm.nih.gov/gene/3516) · UniProt [Q06330](https://www.uniprot.org/uniprotkb/Q06330) · Ensembl [ENSG00000168214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168214) · OMIM [147183](https://www.omim.org/entry/147183)

**PubMed**, as HGNC records for this gene — [8406481](https://pubmed.ncbi.nlm.nih.gov/8406481/), [9290259](https://pubmed.ncbi.nlm.nih.gov/9290259/), [16354684](https://pubmed.ncbi.nlm.nih.gov/16354684/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 411.23 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 168 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.054× |
| Wild-type minus altered | 1.023× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00226 |
| As a percentage | -0.16% |
| FDR, exposure-shuffle null | 0.2854 |
| In TP53-wild-type lines / altered lines | -0.00291 / -0.00187 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.144 raw, 0.102 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 104 targets |
| Activity vs MG53 across exposures (r) | 0.038 (q 0.333) |
| With 3 principal components removed | 0.096 (q 0.010) |
| Within line, across exposures (r) | -0.013 (q 0.054) |
| Percentile against all genes | 72.2 |

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
