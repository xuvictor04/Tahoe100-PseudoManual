---
symbol: LDHC
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [CT32]
gene_name: lactate dehydrogenase C
locus: 11p15.1
locus_type: gene with protein product
gene_family: [L-lactate dehydrogenase family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# LDHC

*lactate dehydrogenase C* — 11p15.1

> [!summary] In one line
> LDHC encodes the C subunit of lactate dehydrogenase, assembling into the germ-cell-restricted LDH-C4 isozyme that supports sperm energy metabolism.

## What it is

The sixth LDH isozyme was found in human testis in the 1960s and called LDH-X before the subunit got its own gene at 11p15. LDH-C4 is a homotetramer of C subunits catalysing the same pyruvate-lactate interconversion as LDH-A and LDH-B but with a distinct kinetic profile, and normally confined to spermatocytes, spermatids and mature sperm. Loss of C-subunit activity in mouse impairs sperm motility, capacitation and fertilisation, and reduced activity is associated with human male infertility. Because the promoter is silent outside the germline but de-represses in tumours, LDHC is grouped with the cancer-testis antigens, and HLA-A2-restricted peptides from it have been proposed as immunotherapy targets. Reports of a role in tumour motility come from few models.

## Why it appears in this work

LDHC is in the vault only because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector and 11p15 is far from TRIM72, so [[Readthrough spillover]] does not apply. Worth noting: its expression in these lines is an epigenetic accident of cancer-testis de-repression, not a programmed state.

## What is uncertain

The measurement is the weak point. LDHC shares substantial sequence identity with LDHA and LDHB, both abundant in essentially every cancer line, so a low LDHC count is exactly where read misassignment would show up — importing the behaviour of a major glycolytic gene into this feature. Cancer-testis expression is also strongly line-specific, so an apparent association could be carried by the few lines that de-repress the locus at all; see [[Why MG53 is hard to measure here]].

## References

- Wu et al., 2022, Frontiers in Oncology — review of LDH-C4 in germ-cell metabolism, male infertility and its reclassification as a cancer-testis antigen.
- Naik and Decock, 2023, Frontiers in Oncology — commentary on that review, noting the authors' own earlier identification of HLA-A2-restricted LDHC peptides that elicit cytotoxic T-cell responses.

## What is on record

| | |
|---|---|
| Official name | lactate dehydrogenase C |
| Also known as | CT32, cancer/testis antigen 32 |
| Locus | 11p15.1 — gene with protein product |
| Gene families | L-lactate dehydrogenase family |

**Function**, from UniProt [P07864](https://www.uniprot.org/uniprotkb/P07864) (reviewed):

> Interconverts simultaneously and stereospecifically pyruvate and L-lactate with concomitant interconversion of NADH and NAD(+) (PubMed:35646544). Predominant lactate dehydrogenase isozyme in spermatozoa and spermatogenic cells, where it is required for glycolytic ATP production, sperm motility, capacitation and fertilization (By similarity). Also acts as a regulator of chromatin during late stage of spermatogenesis by acting as a 2-oxoglutarate reductase: translocates into the nucleus and catalyzes the reduction of 2-oxoglutarate to L-2-hydroxyglutarate, thereby regulating centromere condensation and heterochromatin organization (By similarity)

**Summary**, from NCBI Gene [3948](https://www.ncbi.nlm.nih.gov/gene/3948):

> Lactate dehydrogenase C catalyzes the conversion of L-lactate and NAD to pyruvate and NADH in the final step of anaerobic glycolysis.  LDHC is testis-specific and belongs to the lactate dehydrogenase family.  Two transcript variants have been detected which differ in the 5' untranslated region. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6544](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6544) · Entrez [3948](https://www.ncbi.nlm.nih.gov/gene/3948) · UniProt [P07864](https://www.uniprot.org/uniprotkb/P07864) · Ensembl [ENSG00000166796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166796) · OMIM [150150](https://www.omim.org/entry/150150)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.11991 |
| As a percentage | +8.67% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.12646 / 0.11593 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.776 raw, 0.622 with 3 PCs removed |

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
