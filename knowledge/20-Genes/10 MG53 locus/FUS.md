---
symbol: FUS
type: gene
tier: 1
pathway_role: the MG53 locus
aliases: [TLS, FUS1, hnRNP-P2, HNRNPP2]
gene_name: FUS DNA/RNA binding protein
locus: 16p11.2
locus_type: gene with protein product
gene_family: [Zinc fingers RANBP2-type, RNA binding motif containing, Heterogeneous nuclear ribonucleoproteins, FET protein family]
family_siblings_here: [MDM2, MDM4, PTBP3, TAB3]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# FUS

*FUS DNA/RNA binding protein* — 16p11.2

> [!summary] In one line
> FUS is an abundant, essential RNA- and DNA-binding protein involved in transcription, splicing and the DNA damage response, mutated in familial ALS and rearranged in several sarcomas — and, in this study, the highly expressed gene lying 17.05 kb 5′ of TRIM72 on the same strand.

## What it is

FUS (fused in sarcoma, also TLS) is a member of the FET family alongside EWSR1 and TAF15. Its architecture is a list of interaction modules rather than an enzyme: an N-terminal QGSY-rich low-complexity prion-like domain, RGG repeats, an RRM, a zinc finger, and a C-terminal PY-type nuclear localisation signal read by Transportin-1/karyopherin-β2. It is predominantly nuclear but shuttles, and binds thousands of transcripts with loose specificity. Functionally it has been placed at transcription — interacting with the RNA polymerase II C-terminal domain and affecting initiation and elongation — at alternative splicing, at mRNA transport, and in paraspeckles with NEAT1. It also participates in the DNA damage response, recruited rapidly to damage sites in a PARP- and poly(ADP-ribose)-dependent manner, with reported roles in double-strand break repair and in ligation during oxidative damage repair.

The low-complexity domain makes FUS a phase-separating protein, and the property that lets it condense functionally lets it solidify pathologically: purified FUS undergoes a liquid-to-solid transition that disease mutations accelerate. Clinically it is known from two directions. Mutations cause ALS type 6 and some frontotemporal dementia; most cluster in the PY-NLS, weaken Transportin binding, and drive cytoplasmic mislocalisation and inclusion formation, so the disease is usually read as mislocalisation rather than simple loss of function. Separately, translocations fuse the FUS N-terminal low-complexity domain to DNA-binding partners — FUS–DDIT3 (CHOP) in myxoid liposarcoma, FUS–ERG in leukaemia, FUS–CREB3L2 in low-grade fibromyxoid sarcoma — where it acts as a potent transactivation module. FUS is highly expressed in essentially all proliferating cells.

## Why it appears in this work

Position, first and foremost. FUS is the dominant donor in [[The TRIM72 locus]]: same strand, 17.05 kb 5′ of TRIM72, running at roughly 47× TRIM72's level in these pools. Because [[Readthrough spillover]] scales with the donor's expression and not the recipient's, a small proportional failure of termination at FUS is a large proportional gain for the region annotated as TRIM72. That geometry is the main reason behind [[Why MG53 is hard to measure here]], and it is why FUS is read in this vault first as a measurement covariate and only second as a gene. Its own biology reinforces the concern: readthrough rises under stress and under transcription and translation inhibitors, and FUS is heavily transcribed.

## What is uncertain

Whether FUS is a quantitatively sufficient donor is not established. The strand-aware evidence that plus-strand readthrough is really occurring at this locus is solid, but the flux arithmetic calibrated on it over-predicts the observed rise, so "FUS readthrough explains the MG53 signal" overstates what has been shown — the honest form is that it is the leading account and the numbers do not yet close. Whether changes in FUS's own counts are pathway responses is also unsettled: FUS is not a known p53 target and has no established p53 response element, so movement in it more plausibly tracks global transcriptional output or termination fidelity than any specific signal. And nothing about FUS's protein-level biology — condensation state, localisation, DDR recruitment — is visible in mRNA, so a change in FUS counts says nothing about whether FUS is functioning normally in these cells.

## References

- Crozat et al., 1993, Nature — identified FUS/TLS through its fusion to CHOP in human myxoid liposarcoma.
- Kwiatkowski et al., 2009, Science — found mutations in FUS/TLS on chromosome 16 causing familial amyotrophic lateral sclerosis.
- Vance et al., 2009, Science — independently identified FUS mutations as the cause of familial ALS type 6.
- Patel et al., 2015, Cell — showed a liquid-to-solid phase transition of FUS that is accelerated by disease mutation.
- Mastrocola et al., 2013, Journal of Biological Chemistry — showed FUS acts downstream of PARP in the response to DNA damage, with recruitment dependent on poly(ADP-ribose).

## What is on record

| | |
|---|---|
| Official name | FUS DNA/RNA binding protein |
| Also known as | TLS, FUS1, hnRNP-P2, HNRNPP2, heterogeneous nuclear ribonucleoprotein P2, translocated in liposarcoma |
| Locus | 16p11.2 — gene with protein product |
| Gene families | Zinc fingers RANBP2-type; RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins; FET protein family |
| Other genes here in those families | [[MDM2]], [[MDM4]], [[PTBP3]], [[TAB3]] |
| Previously named | FUS RNA binding protein; fusion, derived from t(12;16) malignant liposarcoma; amyotrophic lateral sclerosis 6; fusion (involved in t(12;16) in malignant liposarcoma); fused in sarcoma |

**Function**, from UniProt [P35637](https://www.uniprot.org/uniprotkb/P35637) (reviewed):

> DNA/RNA-binding protein that plays a role in various cellular processes such as transcription regulation, RNA splicing, RNA transport, DNA repair and damage response (PubMed:27731383). Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3' (PubMed:21256132). Binds to nascent pre-mRNAs and acts as a molecular mediator between RNA polymerase II and U1 small nuclear ribonucleoprotein thereby coupling transcription and splicing (PubMed:26124092). Also binds its own pre-mRNA and autoregulates its expression; this autoregulation mechanism is mediated by non-sense-mediated decay (PubMed:24204307). Plays a role in DNA repair mechanisms by promoting D-loop formation and homologous recombination during DNA double-strand break repair (PubMed:10567410). In neuronal cells, plays crucial roles in dendritic spine formation and stability, RNA transport, mRNA stability and synaptic homeostasis (By similarity)

**Summary**, from NCBI Gene [2521](https://www.ncbi.nlm.nih.gov/gene/2521):

> This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of genomic integrity and mRNA/microRNA processing. Alternative splicing results in multiple transcript variants. Defects in this gene result in amyotrophic lateral sclerosis type 6. [provided by RefSeq, Sep 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4010) · Entrez [2521](https://www.ncbi.nlm.nih.gov/gene/2521) · UniProt [P35637](https://www.uniprot.org/uniprotkb/P35637) · Ensembl [ENSG00000089280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089280) · OMIM [137070](https://www.omim.org/entry/137070)

**PubMed**, as HGNC records for this gene — [2372777](https://pubmed.ncbi.nlm.nih.gov/2372777/), [7503811](https://pubmed.ncbi.nlm.nih.gov/7503811/), [19251628](https://pubmed.ncbi.nlm.nih.gov/19251628/), [19251627](https://pubmed.ncbi.nlm.nih.gov/19251627/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00955 |
| As a percentage | +0.66% |
| FDR, exposure-shuffle null | 0.0001 |
| In TP53-wild-type lines / altered lines | 0.01191 / 0.00812 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.636 raw, 0.467 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[Readthrough spillover]], [[The TRIM72 locus]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
