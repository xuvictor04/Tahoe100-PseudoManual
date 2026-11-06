---
symbol: ASCL1
type: gene
tier: 2
pathway_role: transcription factor
aliases: [ASH1, HASH1, bHLHa46]
gene_name: achaete-scute family bHLH transcription factor 1
locus: 12q23.2
locus_type: gene with protein product
gene_family: [Basic helix-loop-helix proteins, Achaete-scute family bHLH transcription factors]
family_siblings_here: [MXI1, MYF5, MYF6, MYOD1, MYOG, TCF21, TWIST1, TWIST2]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ASCL1

*achaete-scute family bHLH transcription factor 1* — 12q23.2

> [!summary] In one line
> ASCL1 is a basic helix-loop-helix transcription factor that drives neuronal and neuroendocrine lineage commitment, and acts as a lineage-dependency oncogene in small-cell lung cancer.

## What it is

ASCL1 (Mash1) heterodimerises with E-proteins and binds E-boxes, and is one of the proneural factors: mice lacking it fail to make olfactory and autonomic neurons, and ASCL1 is the indispensable member of the three-factor cocktail that converts fibroblasts directly into neurons. Notch-HES signalling and rapid turnover keep it pulsatile in progenitors, and it must be extinguished for differentiation to finish. In cancer it defines a lineage state rather than a mutation: ASCL1-high small-cell lung cancer, the SCLC-A subtype, depends on it for survival, and its enhancer programme is distinct from the NEUROD1-driven alternative.

## Why it appears in this work

ASCL1 is a candidate upstream regulator of [[MG53 (TRIM72)]] from the activity-inference step, and it is on that list for a structural reason: the TRIM72 promoter's characterised element is an E-box next to a MEF2 site, read in muscle by the myogenic bHLH factors ([[MYOD1]], [[MYOG]], [[MYF5]], [[MYF6]]). ASCL1 reads the same class of E-box. See [[The TRIM72 locus]].

## What is uncertain

There is no evidence that ASCL1 regulates TRIM72; the shared E-box consensus is enough to make inferred bHLH activities overlap, so a score here may be reporting generic E-box occupancy, or the neuroendocrine lines in the panel, rather than ASCL1. The well-supported part of this gene's biology — proneural specification and SCLC lineage dependency — is largely orthogonal to the question this study asks.

## References

- Guillemot et al., 1993, Cell — Mash1-null mice lack olfactory and autonomic neurons.
- Vierbuchen et al., 2010, Nature — Ascl1 with Brn2 and Myt1l converts fibroblasts into functional neurons.
- Augustyn et al., 2014, PNAS — ASCL1 is a lineage-specific oncogene required for survival of ASCL1-high small-cell lung cancer.
- Borromeo et al., 2016, Cell Reports — ASCL1 and NEUROD1 bind distinct enhancer programmes defining SCLC subtypes.
- Rudin et al., 2019, Nature Reviews Cancer — synthesis defining SCLC subtypes, with SCLC-A keyed to ASCL1.

## What is on record

| | |
|---|---|
| Official name | achaete-scute family bHLH transcription factor 1 |
| Also known as | ASH1, HASH1, bHLHa46 |
| Locus | 12q23.2 — gene with protein product |
| Gene families | Basic helix-loop-helix proteins; Achaete-scute family bHLH transcription factors |
| Other genes here in those families | [[MXI1]], [[MYF5]], [[MYF6]], [[MYOD1]], [[MYOG]], [[TCF21]], [[TWIST1]], [[TWIST2]] |
| Previously named | achaete-scute complex (Drosophila) homolog-like 1; achaete-scute complex-like 1 (Drosophila); achaete-scute complex homolog 1 (Drosophila) |

**Function**, from UniProt [P50553](https://www.uniprot.org/uniprotkb/P50553) (reviewed):

> Transcription factor that plays a key role in neuronal differentiation: acts as a pioneer transcription factor, accessing closed chromatin to allow other factors to bind and activate neural pathways. Directly binds the E box motif (5'-CANNTG-3') on promoters and promotes transcription of neuronal genes. The combination of three transcription factors, ASCL1, POU3F2/BRN2 and MYT1L, is sufficient to reprogram fibroblasts and other somatic cells into induced neuronal (iN) cells in vitro. Plays a role at early stages of development of specific neural lineages in most regions of the CNS, and of several lineages in the PNS. Essential for the generation of olfactory and autonomic neurons. Acts synergistically with FOXN4 to specify the identity of V2b neurons rather than V2a from bipotential p2 progenitors during spinal cord neurogenesis, probably through DLL4-NOTCH signaling activation. Involved in the regulation of neuroendocrine cell development in the glandular stomach (By similarity)

**Summary**, from NCBI Gene [429](https://www.ncbi.nlm.nih.gov/gene/429):

> This gene encodes a member of the basic helix-loop-helix (BHLH) family of transcription factors. The protein activates transcription by binding to the E box (5'-CANNTG-3'). Dimerization with other BHLH proteins is required for efficient DNA binding. This protein plays a role in the neuronal commitment and differentiation and in the generation of olfactory and autonomic neurons. Mutations in this gene may contribute to the congenital central hypoventilation syndrome (CCHS) phenotype in rare cases. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:738) · Entrez [429](https://www.ncbi.nlm.nih.gov/gene/429) · UniProt [P50553](https://www.uniprot.org/uniprotkb/P50553) · Ensembl [ENSG00000139352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139352) · OMIM [100790](https://www.omim.org/entry/100790)

**PubMed**, as HGNC records for this gene — [8390674](https://pubmed.ncbi.nlm.nih.gov/8390674/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01320 |
| As a percentage | +0.92% |
| FDR, exposure-shuffle null | 0.0642 |
| In TP53-wild-type lines / altered lines | 0.00869 / 0.01594 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.196 raw, -0.073 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 47 targets |
| Activity vs MG53 across exposures (r) | 0.306 (q 1.80e-19) |
| With 3 principal components removed | 0.217 (q 4.01e-10) |
| Within line, across exposures (r) | 0.035 (q 0.008) |
| Percentile against all genes | 97.9 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
