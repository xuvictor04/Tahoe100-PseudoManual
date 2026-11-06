---
symbol: SMAD5
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [Dwfc, JV5-1]
gene_name: SMAD family member 5
locus: 5q31.1
locus_type: gene with protein product
gene_family: [SMAD family]
family_siblings_here: [SMAD4, SMAD6]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 135.21
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SMAD5

*SMAD family member 5* — 5q31.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SMAD5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | SMAD family member 5 |
| Also known as | Dwfc, JV5-1 |
| Locus | 5q31.1 — gene with protein product |
| Gene families | SMAD family |
| Other genes here in those families | [[SMAD4]], [[SMAD6]] |
| Previously named | MAD, mothers against decapentaplegic homolog 5 (Drosophila); SMAD, mothers against DPP homolog 5 (Drosophila) |

**Function**, from UniProt [Q99717](https://www.uniprot.org/uniprotkb/Q99717) (reviewed):

> Transcriptional regulator that plays a role in various cellular processes including embryonic development, cell differentiation, angiogenesis and tissue homeostasis (PubMed:12064918, PubMed:16516194). Upon BMP ligand binding to their receptors at the cell surface, is phosphorylated by activated type I BMP receptors (BMPRIs) and associates with SMAD4 to form a heteromeric complex which translocates into the nucleus acting as transcription factor (PubMed:9442019). In turn, the hetero-trimeric complex recognizes cis-regulatory elements containing Smad Binding Elements (SBEs) to modulate the outcome of the signaling network (PubMed:33510867). Non-phosphorylated SMAD5 has a cytoplasmic role in energy metabolism regulation by promoting mitochondrial respiration and glycolysis in response to cytoplasmic pH changes (PubMed:28675158). Mechanistically, interacts with hexokinase 1/HK1 and thereby accelerates glycolysis (PubMed:28675158)

**Summary**, from NCBI Gene [4090](https://www.ncbi.nlm.nih.gov/gene/4090):

> The protein encoded by this gene is involved in the transforming growth factor beta signaling pathway that results in an inhibition of the proliferation of hematopoietic progenitor cells. The encoded protein is activated by bone morphogenetic proteins type 1 receptor kinase, and may be involved in cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6771) · Entrez [4090](https://www.ncbi.nlm.nih.gov/gene/4090) · UniProt [Q99717](https://www.uniprot.org/uniprotkb/Q99717) · Ensembl [ENSG00000113658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113658) · OMIM [603110](https://www.omim.org/entry/603110)

**PubMed**, as HGNC records for this gene — [8673135](https://pubmed.ncbi.nlm.nih.gov/8673135/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 135.21 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 149 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.041× |
| Wild-type minus altered | 1.024× |
| Compounds moving it up in WT lines | 64 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00404 |
| As a percentage | -0.28% |
| FDR, exposure-shuffle null | 0.0176 |
| In TP53-wild-type lines / altered lines | -0.00438 / -0.00383 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.166 raw, -0.265 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 27 targets |
| Activity vs MG53 across exposures (r) | -0.041 (q 0.256) |
| With 3 principal components removed | -0.047 (q 0.176) |
| Within line, across exposures (r) | -0.015 (q 0.272) |
| Percentile against all genes | 45.8 |

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
