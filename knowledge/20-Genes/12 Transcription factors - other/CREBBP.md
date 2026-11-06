---
symbol: CREBBP
type: gene
tier: 2
pathway_role: transcription factor
aliases: [RTS, CBP, KAT3A]
gene_name: CREB binding lysine acetyltransferase 
locus: 16p13.3
locus_type: gene with protein product
gene_family: [Zinc fingers ZZ-type, Lysine acetyltransferases, Bromodomain containing]
family_siblings_here: [EP300, PBRM1]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# CREBBP

*CREB binding lysine acetyltransferase * — 16p13.3

> [!summary] In one line
> CREBBP encodes CBP, a lysine acetyltransferase and transcriptional coactivator that many DNA-binding factors — p53 among them — depend on to reach chromatin.

## What it is

CBP and its paralogue p300 share a domain layout built for brokering: TAZ1 and TAZ2 zinc-binding regions, a KIX domain, a bromodomain and a central acetyltransferase. CBP acetylates histones — H3K27 at active enhancers — and many non-histone substrates, including lysines in the p53 C-terminus, where acetylation stabilises p53 on DNA and raises target induction. Because CBP is shared among many pathways and limited in amount, competition for it is regulatory. Germline heterozygous loss causes Rubinstein-Taybi syndrome; somatic inactivating mutations are frequent in B-cell lymphoma, relapsed acute lymphoblastic leukaemia and bladder cancer. CBP and p300 are partly redundant.

## Why it appears in this work

CREBBP is scored in the regulon-based activity step and ranks near the top. The point to hold onto: CBP is not a sequence-specific factor but a coactivator, so its regulon collects whatever its partners drive. Being also a p53 coactivator, its inferred activity is not independent of p53's output. See [[Transcription factor activity inference]] and [[The p53 pathway]].

## What is uncertain

Whether "CREBBP activity" is meaningful here is the first question. Its regulon in this collection is small and heterogeneous, so a coherent rise across it may report general enhancer acetylation rather than anything CBP-specific — which is also why its score is collinear with [[TP53]] and [[EP300]]. CBP mRNA is a poor proxy for function, since the biology is competition at the protein level. No link between CBP and the TRIM72 promoter is reported.

## References

- Petrij et al., 1995, Nature — mutations in CBP cause Rubinstein-Taybi syndrome.
- Gu & Roeder, 1997, Cell — acetylation of the p53 C-terminal domain by p300 activates its sequence-specific DNA binding.
- Avantaggiati et al., 1997, Cell — p300/CBP is recruited into p53-dependent transcriptional responses.
- Pasqualucci et al., 2011, Nature — recurrent inactivating mutations of CREBBP and EP300 in B-cell lymphoma.
- Mullighan et al., 2011, Nature — CREBBP mutations are enriched at relapse in acute lymphoblastic leukaemia.

## What is on record

| | |
|---|---|
| Official name | CREB binding lysine acetyltransferase  |
| Also known as | RTS, CBP, KAT3A |
| Locus | 16p13.3 — gene with protein product |
| Gene families | Zinc fingers ZZ-type; Lysine acetyltransferases; Bromodomain containing |
| Other genes here in those families | [[EP300]], [[PBRM1]] |
| Previously named | CREB binding protein; Rubinstein-Taybi syndrome |

**Function**, from UniProt [Q92793](https://www.uniprot.org/uniprotkb/Q92793) (reviewed):

> Acetylates histones, giving a specific tag for transcriptional activation (PubMed:21131905, PubMed:24616510). Mediates acetylation of histone H3 at 'Lys-18' and 'Lys-27' (H3K18ac and H3K27ac, respectively) (PubMed:21131905). Also acetylates non-histone proteins, like DDX21, FBL, IRF2, MAFG, NCOA3, POLR1E/PAF53 and FOXO1 (PubMed:10490106, PubMed:11154691, PubMed:12738767, PubMed:12929931, PubMed:24207024, PubMed:28790157, PubMed:30540930, PubMed:35675826, PubMed:9707565). Binds specifically to phosphorylated CREB and enhances its transcriptional activity toward cAMP-responsive genes. Acts as a coactivator of ALX1. Acts as a circadian transcriptional coactivator which enhances the activity of the circadian transcriptional activators: NPAS2-BMAL1 and CLOCK-BMAL1 heterodimers (PubMed:14645221). Acetylates PCNA; acetylation promotes removal of chromatin-bound PCNA and its degradation during nucleotide excision repair (NER) (PubMed:24939902). Acetylates POLR1E/PAF53, leading to decreased association of RNA polymerase I with the rDNA promoter region and coding region (PubMed:24207024). Acetylates DDX21, thereby inhibiting DDX21 helicase activity (PubMed:28790157). Acetylates FBL, preventing methylation of 'Gln-105' of histone H2A (H2AQ104me) (PubMed:30540930). In addition to protein acetyltransferase, can use different acyl-CoA substrates, such as lactoyl-CoA and propanoyl-CoA (propionyl-CoA), and is able to mediate protein lactylation and propionylation, respectively (PubMed:38128537, PubMed:40615044). Catalyzes lactylation of MRE11 in response to DNA damage, thereby promoting DNA double-strand breaks (DSBs) via homologous recombination (HR) (PubMed:38128537). Catalyzes propionylation of histone H3 at 'Lys-18' (H3K18Pr) (PubMed:40615044). Functions as a transcriptional coactivator for SMAD4 in the TGF-beta signaling pathway (PubMed:25514493)

**Summary**, from NCBI Gene [1387](https://www.ncbi.nlm.nih.gov/gene/1387):

> This gene is ubiquitously expressed and is involved in the transcriptional coactivation of many different transcription factors. First isolated as a nuclear protein that binds to cAMP-response element binding protein (CREB), this gene is now known to play critical roles in embryonic development, growth control, and homeostasis by coupling chromatin remodeling to transcription factor recognition. The protein encoded by this gene has intrinsic histone acetyltransferase activity and also acts as a scaffold to stabilize additional protein interactions with the transcription complex. This protein acetylates both histone and non-histone proteins. This protein shares regions of very high sequence similarity with protein p300 in its bromodomain, cysteine-histidine-rich regions, and histone acetyltransferase domain. Mutations in this gene cause Rubinstein-Taybi syndrome (RTS). Chromosomal translocations involving this gene have been associated with acute myeloid leukemia. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Feb 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2348) · Entrez [1387](https://www.ncbi.nlm.nih.gov/gene/1387) · UniProt [Q92793](https://www.uniprot.org/uniprotkb/Q92793) · Ensembl [ENSG00000005339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005339) · OMIM [600140](https://www.omim.org/entry/600140)

**PubMed**, as HGNC records for this gene — [8413673](https://pubmed.ncbi.nlm.nih.gov/8413673/), [29170789](https://pubmed.ncbi.nlm.nih.gov/29170789/), [39293094](https://pubmed.ncbi.nlm.nih.gov/39293094/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00232 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.2778 |
| In TP53-wild-type lines / altered lines | 0.00072 / 0.00329 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.104 raw, 0.233 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 29 targets |
| Activity vs MG53 across exposures (r) | 0.315 (q 8.44e-20) |
| With 3 principal components removed | 0.265 (q 1.67e-14) |
| Within line, across exposures (r) | 0.010 (q 0.534) |
| Percentile against all genes | 98.8 |

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
