---
symbol: PRX
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [KIAA1620]
gene_name: periaxin
locus: 19q13.2
locus_type: gene with protein product
gene_family: [PDZ domain containing]
family_siblings_here: [CASK, MPP4, RAPGEF6]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PRX

*periaxin* — 19q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PRX.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | periaxin |
| Also known as | KIAA1620 |
| Locus | 19q13.2 — gene with protein product |
| Gene families | PDZ domain containing |
| Other genes here in those families | [[CASK]], [[MPP4]], [[RAPGEF6]] |

**Function**, from UniProt [Q9BXM0](https://www.uniprot.org/uniprotkb/Q9BXM0) (reviewed):

> Scaffolding protein that functions as part of a dystroglycan complex in Schwann cells, and as part of EZR and AHNAK-containing complexes in eye lens fiber cells. Required for the maintenance of the peripheral myelin sheath that is essential for normal transmission of nerve impulses and normal perception of sensory stimuli. Required for normal transport of MBP mRNA from the perinuclear to the paranodal regions. Required for normal remyelination after nerve injury. Required for normal elongation of Schwann cells and normal length of the internodes between the nodes of Ranvier. The demyelinated nodes of Ranvier permit saltatory transmission of nerve impulses; shorter internodes cause slower transmission of nerve impulses. Required for the formation of appositions between the abaxonal surface of the myelin sheath and the Schwann cell plasma membrane; the Schwann cell cytoplasm is restricted to regions between these appositions. Required for the formation of Cajal bands and of Schmidt-Lanterman incisures that correspond to short, cytoplasm-filled regions on myelinated nerves. Recruits DRP2 to the Schwann cell plasma membrane. Required for normal protein composition of the eye lens fiber cell plasma membrane and normal eye lens fiber cell morphology

**Summary**, from NCBI Gene [57716](https://www.ncbi.nlm.nih.gov/gene/57716):

> This gene encodes a protein involved in peripheral nerve myelin upkeep. The encoded protein contains 2 PDZ domains which were named after PSD95 (post synaptic density protein), DlgA (Drosophila disc large tumor suppressor), and ZO1 (a mammalian tight junction protein). Two alternatively spliced transcript variants have been described for this gene which encode different protein isoforms and which are targeted differently in the Schwann cell. Mutations in this gene cause Charcot-Marie-Tooth neuoropathy, type 4F and Dejerine-Sottas neuropathy. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13797) · Entrez [57716](https://www.ncbi.nlm.nih.gov/gene/57716) · UniProt [Q9BXM0](https://www.uniprot.org/uniprotkb/Q9BXM0) · Ensembl [ENSG00000105227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105227) · OMIM [605725](https://www.omim.org/entry/605725)

**PubMed**, as HGNC records for this gene — [10839370](https://pubmed.ncbi.nlm.nih.gov/10839370/), [9143514](https://pubmed.ncbi.nlm.nih.gov/9143514/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06404 |
| As a percentage | +4.54% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06266 / 0.06487 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.608 raw, 0.317 with 3 PCs removed |

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
