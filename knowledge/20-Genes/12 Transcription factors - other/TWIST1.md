---
symbol: TWIST1
type: gene
tier: 2
pathway_role: transcription factor
aliases: [SCS, H-twist, BPES2, bHLHa38, CRS1]
gene_name: twist family bHLH transcription factor 1
locus: 7p21.1
locus_type: gene with protein product
gene_family: [Basic helix-loop-helix proteins]
family_siblings_here: [ASCL1, MXI1, MYF5, MYF6, MYOD1, MYOG, TCF21, TWIST2]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TWIST1

*twist family bHLH transcription factor 1* — 7p21.1

> [!summary] In one line
> TWIST1 is a basic helix-loop-helix factor that patterns cranial and limb mesenchyme and, when reactivated in tumours, drives epithelial-mesenchymal transition while blunting the ARF-p53 apoptotic response.

## What it is

TWIST1 binds E-boxes as a heterodimer with E proteins such as E12/E2A, or as a homodimer; dimer choice, HLH-domain phosphorylation and competition with HAND2 set which targets it occupies, so its output follows protein-level context, not its own abundance. It patterns cranial mesenchyme; haploinsufficiency causes Saethre-Chotzen syndrome. In cancer it is the canonical EMT factor, repressing E-cadherin and required for metastasis in mouse models. A conserved C-terminal "Twist box" binds p53 and promotes its MDM2-dependent degradation; TWIST1 also lowers ARF, blunting Myc-driven apoptosis. Both routes act on protein, not transcript. Separately, Twist is a classical antagonist of myogenesis, inhibiting MyoD-family bHLH factors and MEF2-dependent transcription.

## Why it appears in this work

TWIST1 ranks third in the transcription-factor activity step, behind [[ATF5]] and [[ATF4]], and is one of few high-ranking factors with any mechanism that could touch [[MG53 (TRIM72)]]: the one characterised element at TRIM72 is a MEF2 site beside an E-box, and TWIST1 antagonises both — as a repressor, in muscle, which is not the setting here. Its p53 connection acts on protein, invisible to this design. See [[Transcription factor activity inference]].

## What is uncertain

TWIST1 and [[TWIST2]] share a nearly identical bHLH domain and bind the same motif, so their regulons overlap by construction and the two near-top ranks are largely one observation. Activity read off target mRNA is doubly indirect for a factor governed by dimer partners and phosphorylation. The Twist-box/p53 mechanism was established mainly in mesenchymal and sarcoma systems, not the epithelial lines dominating this panel. TWIST1 is also broadly stress- and hypoxia-responsive, so a high rank across 379 compounds may report generic stress.

## References

- Spicer et al., 1996, Science — showed Twist inhibits myogenic bHLH factors and MEF2-dependent transcription.
- el Ghouzzi et al., 1997, Nature Genetics — TWIST mutations cause Saethre-Chotzen syndrome.
- Maestro et al., 1999, Genes & Development — Twist blocks Myc-induced apoptosis and lowers ARF, acting on the ARF/MDM2/p53 axis.
- Yang et al., 2004, Cell — Twist1 is required for metastatic dissemination in a breast cancer model.
- Piccinin et al., 2012, Cancer Cell — the Twist box binds the p53 C-terminus and promotes its MDM2-mediated degradation.

## What is on record

| | |
|---|---|
| Official name | twist family bHLH transcription factor 1 |
| Also known as | SCS, H-twist, BPES2, bHLHa38, CRS1, Saethre-Chotzen syndrome |
| Locus | 7p21.1 — gene with protein product |
| Gene families | Basic helix-loop-helix proteins |
| Other genes here in those families | [[ASCL1]], [[MXI1]], [[MYF5]], [[MYF6]], [[MYOD1]], [[MYOG]], [[TCF21]], [[TWIST2]] |
| Previously named | blepharophimosis, epicanthus inversus and ptosis 3; acrocephalosyndactyly 3; twist homolog 1 (Drosophila); twist basic helix-loop-helix transcription factor 1; craniosynostosis |

**Function**, from UniProt [Q15672](https://www.uniprot.org/uniprotkb/Q15672) (reviewed):

> Acts as a transcriptional regulator. Inhibits myogenesis by sequestrating E proteins, inhibiting trans-activation by MEF2, and inhibiting DNA-binding by MYOD1 through physical interaction. This interaction probably involves the basic domains of both proteins. Also represses expression of pro-inflammatory cytokines such as TNFA and IL1B. Regulates cranial suture patterning and fusion. Activates transcription as a heterodimer with E proteins. Regulates gene expression differentially, depending on dimer composition. Homodimers induce expression of FGFR2 and POSTN while heterodimers repress FGFR2 and POSTN expression and induce THBS1 expression. Heterodimerization is also required for osteoblast differentiation. Represses the activity of the circadian transcriptional activator: NPAS2-BMAL1 heterodimer (By similarity)

**Summary**, from NCBI Gene [7291](https://www.ncbi.nlm.nih.gov/gene/7291):

> This gene encodes a basic helix-loop-helix (bHLH) transcription factor that plays an important role in embryonic development. The encoded protein forms both homodimers and heterodimers that bind to DNA E box sequences and regulate the transcription of genes involved in cranial suture closure during skull development. This protein may also regulate neural tube closure, limb development and brown fat metabolism. This gene is hypermethylated and overexpressed in multiple human cancers, and the encoded protein promotes tumor cell invasion and metastasis, as well as metastatic recurrence. Mutations in this gene cause Saethre-Chotzen syndrome in human patients, which is characterized by craniosynostosis, ptosis and hypertelorism. [provided by RefSeq, Jul 2020]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12428) · Entrez [7291](https://www.ncbi.nlm.nih.gov/gene/7291) · UniProt [Q15672](https://www.uniprot.org/uniprotkb/Q15672) · Ensembl [ENSG00000122691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122691) · OMIM [601622](https://www.omim.org/entry/601622)

**PubMed**, as HGNC records for this gene — [8995765](https://pubmed.ncbi.nlm.nih.gov/8995765/), [11474656](https://pubmed.ncbi.nlm.nih.gov/11474656/), [17343269](https://pubmed.ncbi.nlm.nih.gov/17343269/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00202 |
| As a percentage | +0.14% |
| FDR, exposure-shuffle null | 0.8169 |
| In TP53-wild-type lines / altered lines | 0.00127 / 0.00247 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.222 raw, -0.038 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 64 targets |
| Activity vs MG53 across exposures (r) | 0.354 (q 9.10e-27) |
| With 3 principal components removed | 0.335 (q 7.88e-24) |
| Within line, across exposures (r) | 0.013 (q 0.483) |
| Percentile against all genes | 99.8 |

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
