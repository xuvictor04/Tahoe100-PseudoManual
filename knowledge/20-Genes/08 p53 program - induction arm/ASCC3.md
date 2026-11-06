---
symbol: ASCC3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [RNAH, ASC1p200, dJ121G13.4, dJ467N11.1]
gene_name: activating signal cointegrator 1 complex subunit 3
locus: 6q16.3
locus_type: gene with protein product
gene_family: [Activating signal cointegrator 1 complex, DexD/H helicases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 302.75
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ASCC3

*activating signal cointegrator 1 complex subunit 3* — 6q16.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ASCC3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | activating signal cointegrator 1 complex subunit 3 |
| Also known as | RNAH, ASC1p200, dJ121G13.4, dJ467N11.1, RNA helicase family |
| Locus | 6q16.3 — gene with protein product |
| Gene families | Activating signal cointegrator 1 complex; DexD/H helicases |
| Previously named | helicase, ATP binding 1 |

**Function**, from UniProt [Q8N3C0](https://www.uniprot.org/uniprotkb/Q8N3C0) (reviewed):

> ATPase involved both in DNA repair and rescue of stalled ribosomes (PubMed:22055184, PubMed:28757607, PubMed:32099016, PubMed:32579943, PubMed:36302773). 3'-5' DNA helicase involved in repair of alkylated DNA: promotes DNA unwinding to generate single-stranded substrate needed for ALKBH3, enabling ALKBH3 to process alkylated N3-methylcytosine (3mC) within double-stranded regions (PubMed:22055184). Also involved in activation of the ribosome quality control (RQC) pathway, a pathway that degrades nascent peptide chains during problematic translation (PubMed:28757607, PubMed:32099016, PubMed:32579943, PubMed:36302773). Drives the splitting of stalled ribosomes that are ubiquitinated in a ZNF598-dependent manner, as part of the ribosome quality control trigger (RQT) complex (PubMed:28757607, PubMed:32099016, PubMed:32579943, PubMed:36302773). Part of the ASC-1 complex that enhances NF-kappa-B, SRF and AP1 transactivation (PubMed:12077347)

**Summary**, from NCBI Gene [10973](https://www.ncbi.nlm.nih.gov/gene/10973):

> This gene encodes a protein that belongs to a family of helicases that are involved in the ATP-dependent unwinding of nucleic acid duplexes. The encoded protein is the largest subunit of the activating signal cointegrator 1 complex that is involved in DNA repair and resistance to alkylation damage. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18697) · Entrez [10973](https://www.ncbi.nlm.nih.gov/gene/10973) · UniProt [Q8N3C0](https://www.uniprot.org/uniprotkb/Q8N3C0) · Ensembl [ENSG00000112249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112249) · OMIM [614217](https://www.omim.org/entry/614217)

**PubMed**, as HGNC records for this gene — [10218103](https://pubmed.ncbi.nlm.nih.gov/10218103/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 302.75 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 48 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.107× |
| Wild-type minus altered | 1.073× |
| Compounds moving it up in WT lines | 81 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00168 |
| As a percentage | +0.12% |
| FDR, exposure-shuffle null | 0.5320 |
| In TP53-wild-type lines / altered lines | -0.00025 / 0.00286 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.074 raw, 0.186 with 3 PCs removed |

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
