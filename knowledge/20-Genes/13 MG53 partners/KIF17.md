---
symbol: KIF17
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [KIAA1405, KIF3X, KIF17B, OSM-3, KLP-2]
gene_name: kinesin family member 17
locus: 1p36.12
locus_type: gene with protein product
gene_family: [Kinesins]
family_siblings_here: [KIF11]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# KIF17

*kinesin family member 17* — 1p36.12

> [!summary] In one line
> KIF17 is a homodimeric kinesin-2 motor that carries cargo outward along microtubules in dendrites and into cilia.

## What it is

KIF17 is the vertebrate counterpart of *C. elegans* OSM-3: a processive, plus-end-directed homodimer, unlike heterotrimeric kinesin-II. Its best-established cargo is neuronal. The KIF17 tail binds the PDZ domain of mLin-10/Mint1, linking the motor to a scaffold carrying NMDA-receptor NR2B subunits, and this is the route by which NR2B-containing vesicles move into dendrites; CaMKII phosphorylation of the same region releases the cargo. A second, largely separate literature places KIF17 in cilia, where it enters the axoneme, associates with IFT-B, and is required for building photoreceptor outer segments. Mouse knockouts are viable, with impaired NR2B transport and memory deficits. Outside neurons and ciliated cells little is described.

## Why it appears in this work

KIF17 is in the vault only because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector, not a transcription factor, and 1p36 is nowhere near TRIM72, so [[Readthrough spillover]] does not explain it. Note that it shares nothing with the kinesin-5 spindle motor [[KIF11]] beyond distant motor-domain ancestry.

## What is uncertain

Both of KIF17's established settings — dendrites and cilia — are largely absent from pooled cancer lines, so there is no known function here for a correlation to act through. The transcript is low in these lines, putting ambient RNA and mapping ambiguity across the conserved kinesin motor domain in play; see [[Why MG53 is hard to measure here]]. Nothing in the literature connects KIF17 to p53 or to membrane repair, and nothing in this design separates a real association from one driven by a few lines.

## References

- Setou et al., 2000, Science — showed KIF17 transports NR2B-containing vesicles in dendrites via mLin-10/Mint1.
- Insinna et al., 2008, Developmental Biology — showed Kif17 is required for vertebrate photoreceptor outer-segment development.

## What is on record

| | |
|---|---|
| Official name | kinesin family member 17 |
| Also known as | KIAA1405, KIF3X, KIF17B, OSM-3, KLP-2, kinesin-like protein KIF17, KIF3-related motor protein |
| Locus | 1p36.12 — gene with protein product |
| Gene families | Kinesins |
| Other genes here in those families | [[KIF11]] |

**Function**, from UniProt [Q9P2E2](https://www.uniprot.org/uniprotkb/Q9P2E2) (reviewed):

> Together with RAB23 and IFT57, it is required for the localization of specific G protein-coupled receptors, such as dopamime receptor DRD1, to primary cilia (PubMed:26182404). In association with the Apba1-containing complex (LIN-10-LIN-2-LIN-7 complex), transports vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules

**Summary**, from NCBI Gene [57576](https://www.ncbi.nlm.nih.gov/gene/57576):

> Predicted to enable ATP hydrolysis activity; microtubule binding activity; and plus-end-directed microtubule motor activity. Predicted to be involved in anterograde dendritic transport of neurotransmitter receptor complex. Predicted to act upstream of or within microtubule-based process; protein-containing complex localization; and vesicle-mediated transport. Predicted to be located in cytosol. Predicted to be part of kinesin complex. Predicted to be active in several cellular components, including cilium; microtubule cytoskeleton; and neuron projection. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19167) · Entrez [57576](https://www.ncbi.nlm.nih.gov/gene/57576) · UniProt [Q9P2E2](https://www.uniprot.org/uniprotkb/Q9P2E2) · Ensembl [ENSG00000117245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117245) · OMIM [605037](https://www.omim.org/entry/605037)

**PubMed**, as HGNC records for this gene — [10846156](https://pubmed.ncbi.nlm.nih.gov/10846156/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08870 |
| As a percentage | +6.34% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.10145 / 0.08153 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.651 raw, 0.457 with 3 PCs removed |

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
