---
symbol: SPATA18
type: gene
tier: 1
pathway_role: p53 effector: other
aliases: [MIEAP]
gene_name: spermatogenesis associated 18
locus: 4q12
locus_type: gene with protein product
p53_direction: induced by p53
curated_effector: true
effector_role: other
mg53_verdict: none
tags: [curated-effector, gene, p53-induced]
generated_by: knowledge/_build/build_vault.py
---

# SPATA18

*spermatogenesis associated 18* — 4q12

> [!summary] In one line
> SPATA18 encodes Mieap, a p53-inducible mitochondrial protein proposed to run a form of mitochondrial quality control distinct from canonical mitophagy — a well-supported p53 target whose mechanism rests almost entirely on one laboratory's work.

## What it is

Two names, one gene. HGNC calls it SPATA18, "spermatogenesis associated 18"; the functional literature calls it Mieap, "mitochondria-eating protein". The protein is roughly 540 residues, associates with the mitochondrial outer membrane and binds cardiolipin.

The p53 connection is the best-established part: p53 binds a response element at the locus and induces the transcript — the basis on which the gene was characterised at all. On oxidative stress it was reported to drive one of two outcomes by severity — MALM, in which lysosomal proteins are delivered into the mitochondrial interior to degrade oxidised proteins and so "repair" the organelle, requiring BNIP3 and NIX; or, when repair fails, Mieap-induced vacuoles that engulf whole mitochondria.

That model has since been substantially revised by the same group: more recent work describes Mieap forming membrane-less organelles — condensates — involved in cardiolipin metabolism, a different kind of claim from lysosome-like compartments inside mitochondria. The cancer argument is that the axis is lost in tumours: reported inactivated in a large majority of primary colorectal cancers through p53 mutation or MIEAP and BNIP3 promoter methylation; Mieap-deficient mice show increased intestinal tumour burden. Expression is tissue-enhanced rather than ubiquitous, concentrated in fallopian tube and testis; in cultured cancer lines it is generally a low-abundance transcript.

## Why it appears in this work

SPATA18 is in the vault as a curated p53 effector representing an output arm that nothing else on the list covers: organelle maintenance. The apoptotic mitochondrial effectors ([[BAX]], [[PMAIP1]], [[BBC3]]) report that p53 is permeabilising mitochondria; Mieap would report that p53 is trying to keep them serviceable. That makes its induction qualitatively informative about the breadth of [[p53 program P]]. It also carries a practical caution: unlike [[CDKN1A]] or [[MDM2]], this is not an abundant transcript in cancer lines, so a 3′-end single-cell measurement has little to work with — the problem that dominates [[Why MG53 is hard to measure here]], arising here from restricted baseline expression rather than locus geometry.

## What is uncertain

Nearly all of the mechanism comes from one group, and independent replication of the central cell-biological claims is thin. MALM and Mieap-induced vacuoles are not standard entities elsewhere in the mitochondrial quality-control field, and the originating laboratory has itself moved from that model toward cardiolipin-handling condensates, so the earlier account should not be quoted as settled. How any of this relates to PINK1/Parkin mitophagy is unmapped.

What survives best is the transcriptional fact: SPATA18 is p53-responsive. Beyond that, two tensions deserve stating. The expression pattern — ciliated epithelium and germ line — sits awkwardly with a general p53-controlled quality-control function in all tissues. And the tumour-suppressor case rests on promoter-methylation frequencies in modest cohorts plus a mouse model, which supports an association more firmly than it supports the proposed mechanism being the reason. The gene name is also a hazard: "spermatogenesis associated" reflects cataloguing history, not a demonstrated reproductive role.

## References

- Kitamura et al., 2011, PLoS ONE — identified Mieap as a p53-inducible protein controlling mitochondrial quality by repairing or eliminating unhealthy mitochondria.
- Tsuneki et al., 2015, Scientific Reports — Mieap suppresses murine intestinal tumour formation via its mitochondrial quality control function.
- Kamino et al., 2016, Oncogenesis — Mieap-regulated mitochondrial quality control is frequently inactivated in human colorectal cancer.
- Nakamura & Arakawa, 2017, Cancer Science — review framing Mieap-regulated mitochondrial quality control as a function of p53.
- Ikari et al., 2024, iScience — Mieap forms membrane-less organelles involved in cardiolipin metabolism, revising the earlier mechanistic model.

## What is on record

| | |
|---|---|
| Official name | spermatogenesis associated 18 |
| Also known as | FLJ32906 |
| Locus | 4q12 — gene with protein product |
| Previously named | spermatogenesis associated 18 homolog (rat) |

**Function**, from UniProt [Q8TC71](https://www.uniprot.org/uniprotkb/Q8TC71) (reviewed):

> Key regulator of mitochondrial quality that mediates the repairing or degradation of unhealthy mitochondria in response to mitochondrial damage (PubMed:21264221, PubMed:21264228, PubMed:22292033, PubMed:22532927). Mediator of mitochondrial protein catabolic process (also named MALM) by mediating the degradation of damaged proteins inside mitochondria by promoting the accumulation in the mitochondrial matrix of hydrolases that are characteristic of the lysosomal lumen (PubMed:21264221, PubMed:21264228, PubMed:22292033, PubMed:22532927). Also involved in mitochondrion degradation of damaged mitochondria by promoting the formation of vacuole-like structures (named MIV), which engulf and degrade unhealthy mitochondria by accumulating lysosomes (PubMed:21264228). The physical interaction of SPATA18/MIEAP, BNIP3 and BNIP3L/NIX at the mitochondrial outer membrane regulates the opening of a pore in the mitochondrial double membrane in order to mediate the translocation of lysosomal proteins from the cytoplasm to the mitochondrial matrix (PubMed:22292033). Binds cardiolipin (PubMed:38322995). May form molecular condensates (non-membrane-bounded organelles) within mitochondria that compartmentalize and promote cardiolipin metabolism (PubMed:38322995)

**Summary**, from NCBI Gene [132671](https://www.ncbi.nlm.nih.gov/gene/132671):

> This gene encodes a p53-inducible protein that is able to induce lysosome-like organelles within mitochondria that eliminate oxidized mitochondrial proteins, thereby contributing to mitochondrial quality control. Dysregulation of mitochondrial quality control is associated with cancer and degenerative diseases. The encoded protein mediates accumulation of the lysosome-like mitochondrial organelles through interaction with B cell lymphoma 2 interacting protein 3 and B cell lymphoma 2 interacting protein 3 like at the outer mitochondrial membrane, which allows translocation of lysosomal proteins to the mitochondrial matrix from the cytosol. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29579) · Entrez [132671](https://www.ncbi.nlm.nih.gov/gene/132671) · UniProt [Q8TC71](https://www.uniprot.org/uniprotkb/Q8TC71) · Ensembl [ENSG00000163071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163071) · OMIM [612814](https://www.omim.org/entry/612814)

**PubMed**, as HGNC records for this gene — [21300779](https://pubmed.ncbi.nlm.nih.gov/21300779/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01723 |
| As a percentage | +1.20% |
| FDR, exposure-shuffle null | 0.1311 |
| In TP53-wild-type lines / altered lines | 0.01164 / 0.02062 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.355 raw, -0.010 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
