---
symbol: ZNF91
type: gene
tier: 2
pathway_role: transcription factor
aliases: [HPF7, HTF10]
gene_name: zinc finger protein 91
locus: 19p12
locus_type: gene with protein product
gene_family: [Zinc fingers C2H2-type, KRAB domain containing]
family_siblings_here: [HIVEP2, ZFPM1, ZNF195, ZNF37A, ZNF423, ZNF44, ZNF654, ZNF79]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ZNF91

*zinc finger protein 91* — 19p12

> [!summary] In one line
> ZNF91 is a primate-specific KRAB zinc-finger protein whose one well-established function is heterochromatic silencing of SVA retrotransposons.

## What it is

ZNF91 sits in the large KRAB zinc-finger cluster on chromosome 19, with the family's standard architecture: a KRAB domain that recruits TRIM28/SETDB1 to deposit H3K9me3, and a tandem zinc-finger array supplying specificity. Its array changed structurally in the hominid lineage roughly eight to twelve million years ago, including duplication of consecutive fingers, and the resulting protein recognises the VNTR of SVA elements — a retrotransposon family that expanded over the same period. Deleting ZNF91 in human embryonic stem cells reactivates SVAs, mainly young ones, together with a communal rise in other KZFP clusters. Outside transposon silencing and early development essentially nothing is established, and ZNF91 has no characterised protein-coding target promoters.

## Why it appears in this work

ZNF91 is here only because the regulon step ranked it highly. It is not a curated p53 effector, nothing connects it to [[MG53 (TRIM72)]], and chromosome 19 is unrelated to [[The TRIM72 locus]], so [[Readthrough spillover]] does not explain it. See [[Transcription factor activity inference]].

## What is uncertain

The inferred regulon is unlikely to be ZNF91's real target set: KZFPs act on repeat families through heterochromatin, not on individual protein-coding promoters, and a co-expression-derived regulon has no established relationship to that mechanism. ZNF91 also lies in a dense KZFP cluster whose members are co-expressed as a block — and whose coordinate upregulation is a documented consequence of SVA derepression — so both its measured level and its inferred activity partly report cluster-level transcription. The silencing work comes from embryonic stem cells; whether ZNF91 does anything comparable in differentiated cancer lines at 24 h is unknown.

## References

- Jacobs et al., 2014, Nature — identified ZNF91 and ZNF93 as KRAB zinc-finger repressors of SVA and L1 retrotransposons, and dated ZNF91's zinc-finger changes to the hominid lineage.
- Haring et al., 2021, Genome Research — CRISPR deletion of ZNF91 in human embryonic stem cells reactivated SVAs, chiefly young elements, and upregulated KRAB zinc-finger gene clusters.

## What is on record

| | |
|---|---|
| Official name | zinc finger protein 91 |
| Also known as | HPF7, HTF10 |
| Locus | 19p12 — gene with protein product |
| Gene families | Zinc fingers C2H2-type; KRAB domain containing |
| Other genes here in those families | [[HIVEP2]], [[ZFPM1]], [[ZNF195]], [[ZNF37A]], [[ZNF423]], [[ZNF44]], [[ZNF654]], [[ZNF79]] |
| Previously named | zinc finger protein 91 (HPF7, HTF10) |

**Function**, from UniProt [Q05481](https://www.uniprot.org/uniprotkb/Q05481) (reviewed):

> Transcription factor specifically required to repress SINE-VNTR-Alu (SVA) retrotransposons: recognizes and binds SVA sequences and represses their expression by recruiting a repressive complex containing TRIM28/KAP1 (PubMed:25274305). May also bind the promoter of the FCGR2B gene, leading to repress its expression; however, additional evidence is required to confirm this result in vivo (PubMed:11470777)

**Summary**, from NCBI Gene [7644](https://www.ncbi.nlm.nih.gov/gene/7644):

> The ZNF91 gene encodes a zinc finger protein of the KRAB (Kruppel-associated box) subfamily (Bellefroid et al., 1991, 1993 [PubMed 2023909] [PubMed 8467795]).[supplied by OMIM, May 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13166) · Entrez [7644](https://www.ncbi.nlm.nih.gov/gene/7644) · UniProt [Q05481](https://www.uniprot.org/uniprotkb/Q05481) · Ensembl [ENSG00000167232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167232) · OMIM [603971](https://www.omim.org/entry/603971)

**PubMed**, as HGNC records for this gene — [2023909](https://pubmed.ncbi.nlm.nih.gov/2023909/), [2505992](https://pubmed.ncbi.nlm.nih.gov/2505992/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00176 |
| As a percentage | -0.12% |
| FDR, exposure-shuffle null | 0.5914 |
| In TP53-wild-type lines / altered lines | -0.00242 / -0.00146 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.138 raw, -0.081 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 32 targets |
| Activity vs MG53 across exposures (r) | 0.290 (q 1.18e-17) |
| With 3 principal components removed | 0.237 (q 1.26e-12) |
| Within line, across exposures (r) | 0.034 (q 0.013) |
| Percentile against all genes | 93.9 |

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
