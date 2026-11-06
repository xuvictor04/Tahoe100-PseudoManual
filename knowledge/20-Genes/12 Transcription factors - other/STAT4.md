---
symbol: STAT4
type: gene
tier: 2
pathway_role: transcription factor
gene_name: signal transducer and activator of transcription 4
locus: 2q32.2-q32.3
locus_type: gene with protein product
gene_family: [SH2 domain containing, Signal transducer and activator of transcription family]
family_siblings_here: [SH2D4B, STAT3]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# STAT4

*signal transducer and activator of transcription 4* — 2q32.2-q32.3

> [!summary] In one line
> STAT4 is the signal transducer downstream of interleukin-12 that drives T helper 1 differentiation and interferon-gamma production.

## What it is

STAT4 is one of seven mammalian STATs. After IL-12 engages its receptor, JAK2 and TYK2 phosphorylate a single C-terminal tyrosine; STAT4 then dimerises through reciprocal SH2-phosphotyrosine contacts, enters the nucleus and binds GAS elements. Its output is the Th1 programme — IFNG induction in T and NK cells, with TBX21 as lineage partner — and Stat4-null mice lose essentially all IL-12 responses. Expression is largely confined to lymphoid and myeloid cells. STAT4 is also one of the better-replicated autoimmunity loci, with risk variants in rheumatoid arthritis, lupus and Sjogren's syndrome.

## Why it appears in this work

STAT4 sits among the positively correlated factors in the activity step. The reason to read that as a property of the method rather than of biology is the mismatch of context: STAT4's pathway is immune, these are non-haematopoietic tumour lines, and there is no IL-12 in the medium. See [[Transcription factor activity inference]].

## What is uncertain

A factor whose own transcript is near-absent across most of this panel cannot have had meaningful activity, so the score reports the regulon, not STAT4. That regulon is among the smallest scored, and its members are cytokine- and interferon-inducible genes shared with STAT1 and STAT2 — genes that move under many cytotoxic compounds through interferon responses unrelated to IL-12. The score cannot be separated from generic interferon tone, and nothing links STAT4 to TRIM72.

## References

- Thierfelder et al., 1996, Nature — Stat4-deficient mice fail to mount IL-12-mediated responses in NK and T cells.
- Kaplan et al., 1996, Nature — an independent Stat4 knockout showing impaired IL-12 responses and enhanced Th2 development.
- Remmers et al., 2007, New England Journal of Medicine — a STAT4 haplotype confers risk of rheumatoid arthritis and systemic lupus erythematosus.

## What is on record

| | |
|---|---|
| Official name | signal transducer and activator of transcription 4 |
| Also known as | — (no recorded alias) |
| Locus | 2q32.2-q32.3 — gene with protein product |
| Gene families | SH2 domain containing; Signal transducer and activator of transcription family |
| Other genes here in those families | [[SH2D4B]], [[STAT3]] |

**Function**, from UniProt [Q14765](https://www.uniprot.org/uniprotkb/Q14765) (reviewed):

> Transcriptional regulator mainly expressed in hematopoietic cells that plays a critical role in cellular growth, differentiation and immune response (PubMed:10961885, PubMed:37256972, PubMed:8943379). Plays a key role in the differentiation of T-helper 1 cells and the production of interferon-gamma (PubMed:12213961, PubMed:35614130). Also participates in multiple neutrophil functions including chemotaxis and production of the neutrophil extracellular traps (By similarity). After IL12 binding to its receptor IL12RB2, STAT4 interacts with the intracellular domain of IL12RB2 and becomes tyrosine phosphorylated (PubMed:10415122, PubMed:7638186). Phosphorylated STAT4 then homodimerizes and migrates to the nucleus where it can recognize STAT target sequences present in IL12 responsive genes. Although IL12 appears to be the predominant activating signal, STAT4 can also be phosphorylated and activated in response to IFN-gamma stimulation via JAK1 and TYK2 and in response to different interleukins including IL23, IL2 and IL35 (PubMed:11114383, PubMed:34508746). Transcription activation of IFN-gamma gene is mediated by interaction with JUN that forms a complex that efficiently interacts with the AP-1-related sequence of the IFN-gamma promoter (By similarity). In response to IFN-alpha/beta signaling, acts as a transcriptional repressor and suppresses IL5 and IL13 mRNA expression during response to T-cell receptor (TCR) activation (PubMed:26990433)

**Summary**, from NCBI Gene [6775](https://www.ncbi.nlm.nih.gov/gene/6775):

> The protein encoded by this gene is a member of the STAT family of transcription factors. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein is essential for mediating responses to IL12 in lymphocytes, and regulating the differentiation of T helper cells. Mutations in this gene may be associated with systemic lupus erythematosus and rheumatoid arthritis. Alternate splicing results in multiple transcript variants that encode the same protein. [provided by RefSeq, Aug 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11365) · Entrez [6775](https://www.ncbi.nlm.nih.gov/gene/6775) · UniProt [Q14765](https://www.uniprot.org/uniprotkb/Q14765) · Ensembl [ENSG00000138378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138378) · OMIM [600558](https://www.omim.org/entry/600558)

**PubMed**, as HGNC records for this gene — [8007943](https://pubmed.ncbi.nlm.nih.gov/8007943/), [8700208](https://pubmed.ncbi.nlm.nih.gov/8700208/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01545 |
| As a percentage | +1.08% |
| FDR, exposure-shuffle null | 0.1193 |
| In TP53-wild-type lines / altered lines | 0.00213 / 0.02286 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.203 raw, 0.048 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 14 targets |
| Activity vs MG53 across exposures (r) | 0.284 (q 4.32e-18) |
| With 3 principal components removed | 0.219 (q 1.65e-11) |
| Within line, across exposures (r) | 0.024 (q 0.033) |
| Percentile against all genes | 99.7 |

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
