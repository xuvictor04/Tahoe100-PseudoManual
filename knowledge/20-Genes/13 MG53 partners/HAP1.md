---
symbol: HAP1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [HLP, hHLP1, HIP5]
gene_name: huntingtin associated protein 1
locus: 17q21.2
locus_type: gene with protein product
gene_family: [Centriolar satellite proteins]
family_siblings_here: [HTT]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# HAP1

*huntingtin associated protein 1* — 17q21.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HAP1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | huntingtin associated protein 1 |
| Also known as | HLP, hHLP1, HIP5, neuroan 1 |
| Locus | 17q21.2 — gene with protein product |
| Gene families | Centriolar satellite proteins |
| Other genes here in those families | [[HTT]] |
| Previously named | huntingtin-associated protein 1 |

**Function**, from UniProt [P54257](https://www.uniprot.org/uniprotkb/P54257) (reviewed):

> Originally identified as neuronal protein that specifically associates with HTT/huntingtin and the binding is enhanced by an expanded polyglutamine repeat within HTT possibly affecting HAP1 interaction properties. Both HTT and HAP1 are involved in intracellular trafficking and HAP1 is proposed to link HTT to motor proteins and/or transport cargos. Seems to play a role in vesicular transport within neurons and axons such as from early endosomes to late endocytic compartments and to promote neurite outgrowth. The vesicular transport function via association with microtubule-dependent transporters can be attenuated by association with mutant HTT. Involved in the axonal transport of BDNF and its activity-dependent secretion; the function seems to involve HTT, DCTN1 and a complex with SORT1. Involved in APP trafficking and seems to facilitate APP anterograde transport and membrane insertion thereby possibly reducing processing into amyloid beta. Involved in delivery of gamma-aminobutyric acid (GABA(A)) receptors to synapses; the function is dependent on kinesin motor protein KIF5 and is disrupted by HTT with expanded polyglutamine repeat. Involved in regulation of autophagosome motility by promoting efficient retrograde axonal transport. Seems to be involved in regulation of membrane receptor recycling and degradation, and respective signal transduction, including GABA(A) receptors, tyrosine kinase receptors, EGFR, IP3 receptor and androgen receptor. Among others suggested to be involved in control of feeding behavior (involving hypothalamic GABA(A) receptors), cerebellar and brainstem development (involving AHI1 and NTRK1/TrkA), postnatal neurogenesis (involving hypothalamic NTRK2/TrkB), and ITPR1/InsP3R1-mediated Ca(2+) release (involving HTT and possibly the effect of mutant HTT). Via association with DCTN1/dynactin p150-glued and HTT/huntingtin involved in cytoplasmic retention of REST in neurons. May be involved in ciliogenesis. Involved in regulation of exocytosis. Seems to be involved in formation of cytoplasmic inclusion bodies (STBs). In case of anomalous expression of TBP, can sequester a subset of TBP into STBs; sequestration is enhanced by an expanded polyglutamine repeat within TBP. HAP1-containing STBs have been proposed to play a protective role against neurodegeneration in Huntigton disease (HD) and spinocerebellar ataxia 17 (SCA17)

**Summary**, from NCBI Gene [9001](https://www.ncbi.nlm.nih.gov/gene/9001):

> Huntington's disease (HD), a neurodegenerative disorder characterized by loss of striatal neurons, is caused by an expansion of a polyglutamine tract in the HD protein huntingtin. This gene encodes a protein that interacts with huntingtin, with two cytoskeletal proteins (dynactin and pericentriolar autoantigen protein 1), and with a hepatocyte growth factor-regulated tyrosine kinase substrate. The interactions with cytoskeletal proteins and a kinase substrate suggest a role for this protein in vesicular trafficking or organelle transport. Several alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4812) · Entrez [9001](https://www.ncbi.nlm.nih.gov/gene/9001) · UniProt [P54257](https://www.uniprot.org/uniprotkb/P54257) · Ensembl [ENSG00000173805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173805) · OMIM [600947](https://www.omim.org/entry/600947)

**PubMed**, as HGNC records for this gene — [7477378](https://pubmed.ncbi.nlm.nih.gov/7477378/), [9668110](https://pubmed.ncbi.nlm.nih.gov/9668110/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06673 |
| As a percentage | +4.73% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.05304 / 0.07342 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.599 raw, 0.372 with 3 PCs removed |

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
