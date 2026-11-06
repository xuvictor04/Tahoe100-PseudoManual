---
symbol: MIR9-1HG
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [CROC4]
gene_name: MIR9-1 host gene
locus: 1q22
locus_type: RNA, long non-coding
gene_family: [MicroRNA non-coding host genes]
family_siblings_here: [MIR34AHG, MIR3659HG, MIR924HG, PVT1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# MIR9-1HG

*MIR9-1 host gene* — 1q22

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MIR9-1HG.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | MIR9-1 host gene |
| Also known as | CROC4, contingent replication of cDNA-4, transcriptional activator of the c fos promoter |
| Locus | 1q22 — RNA, long non-coding |
| Gene families | MicroRNA non-coding host genes |
| Other genes here in those families | [[MIR34AHG]], [[MIR3659HG]], [[MIR924HG]], [[PVT1]] |
| Previously named | chromosome 1 open reading frame 61 |

**Function**, from UniProt [Q13536](https://www.uniprot.org/uniprotkb/Q13536) (reviewed):

> May play a role in FOS signaling pathways involved in development and remodeling of neurons. Promotes transcription of the FOS promoter

**Summary**, from NCBI Gene [10485](https://www.ncbi.nlm.nih.gov/gene/10485):

> Involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30780) · Entrez [10485](https://www.ncbi.nlm.nih.gov/gene/10485) · UniProt [Q13536](https://www.uniprot.org/uniprotkb/Q13536) · Ensembl [ENSG00000125462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125462) · OMIM [618747](https://www.omim.org/entry/618747)

**PubMed**, as HGNC records for this gene — [10995546](https://pubmed.ncbi.nlm.nih.gov/10995546/), [23012322](https://pubmed.ncbi.nlm.nih.gov/23012322/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07147 |
| As a percentage | +5.08% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07798 / 0.06752 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.781 raw, 0.682 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
