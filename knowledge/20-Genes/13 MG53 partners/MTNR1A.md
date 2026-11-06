---
symbol: MTNR1A
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [MEL-1A-R]
gene_name: melatonin receptor 1A
locus: 4q35.2
locus_type: gene with protein product
gene_family: [Melatonin receptors]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# MTNR1A

*melatonin receptor 1A* — 4q35.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MTNR1A.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | melatonin receptor 1A |
| Also known as | MEL-1A-R |
| Locus | 4q35.2 — gene with protein product |
| Gene families | Melatonin receptors |

**Function**, from UniProt [P48039](https://www.uniprot.org/uniprotkb/P48039) (reviewed):

> High affinity receptor for melatonin. Likely to mediate the reproductive and circadian actions of melatonin. The activity of this receptor is mediated by pertussis toxin sensitive G proteins that inhibit adenylate cyclase activity. Possibly involved in sleep induction, by melatonin activation of the potassium channel KCNMA1/BK and the dissociation of G-beta and G-gamma subunits, thereby decreasing synaptic transmission (By similarity)

**Summary**, from NCBI Gene [4543](https://www.ncbi.nlm.nih.gov/gene/4543):

> This gene encodes one of two high affinity forms of a receptor for melatonin, the primary hormone secreted by the pineal gland. This receptor is a G-protein coupled, 7-transmembrane receptor that is responsible for melatonin effects on mammalian circadian rhythm and reproductive alterations affected by day length. The receptor is an integral membrane protein that is readily detectable and localized to two specific regions of the brain. The hypothalamic suprachiasmatic nucleus appears to be involved in circadian rhythm while the hypophysial pars tuberalis may be responsible for the reproductive effects of melatonin. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7463) · Entrez [4543](https://www.ncbi.nlm.nih.gov/gene/4543) · UniProt [P48039](https://www.uniprot.org/uniprotkb/P48039) · Ensembl [ENSG00000168412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168412) · OMIM [600665](https://www.omim.org/entry/600665)

**PubMed**, as HGNC records for this gene — [7558006](https://pubmed.ncbi.nlm.nih.gov/7558006/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08239 |
| As a percentage | +5.88% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09067 / 0.07712 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.534 raw, 0.354 with 3 PCs removed |

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
