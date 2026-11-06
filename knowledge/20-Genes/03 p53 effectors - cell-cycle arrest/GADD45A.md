---
symbol: GADD45A
type: gene
tier: 1
pathway_role: p53 effector: cell-cycle arrest
aliases: [GADD45]
gene_name: growth arrest and DNA damage inducible alpha
locus: 1p31.3
locus_type: gene with protein product
gene_family: [Growth arrest and DNA damage inducible family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: cell-cycle arrest
median_line_cpm: 60.91
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# GADD45A

*growth arrest and DNA damage inducible alpha* — 1p31.3

> [!summary] In one line
> GADD45A is a small stress-inducible nuclear adaptor protein that couples DNA damage and other stresses to G2/M arrest and stress-kinase signalling, and it was one of the first genes shown to be p53-regulated.

## What it is

GADD45A (growth arrest and DNA damage-inducible 45 alpha) is an ~18 kDa acidic nuclear protein, the founding member of a three-gene family with GADD45B and GADD45G. It has no catalytic activity; everything it does, it does by binding partners. It binds PCNA, p21, and the CDK1/cyclin B1 complex, inhibition of which produces G2/M arrest. It binds core histones and has been placed at nucleotide excision repair. And it activates MEKK4/MTK1, feeding the p38 and JNK stress-kinase cascades — which is how a transcriptional stress response becomes a signalling one.

Its induction is promiscuous by design. GADD45A rises after ionising radiation, alkylating agents, UV, hypoxia, oxidative stress and nutrient deprivation. The p53 connection is old and firm: GADD45 was placed in a p53-dependent, ATM-dependent damage-response pathway in the early 1990s, and its p53 response element sits in intron 3 rather than the promoter, one of the examples that taught the field to look inside genes for p53 elements. But the gene is also strongly induced independently of p53, by BRCA1, FOXO3A, ATF4 and octamer- and NF-Y-family factors, and by demethylating agents and HDAC inhibitors. Gadd45a-null mice phenocopy part of p53 loss — genomic instability with aneuploidy and centrosome amplification, increased radiation-induced carcinogenesis, occasional exencephaly — which is the main evidence that it is a real effector rather than a bystander transcript.

GADD45A has a well-developed second life in muscle: it is the ATF4-induced effector required for skeletal muscle atrophy from fasting, immobilisation and denervation, and forcing its expression atrophies myofibres with no upstream stress at all. It has also been proposed to participate in active DNA demethylation with TET and TDG, a claim that has remained contested.

## Why it appears in this work

GADD45A is the member of [[p53 program P]] that reports the checkpoint and arrest arm rather than the apoptotic effectors, and it is the clearest case in this panel of a p53 target that is not a p53-exclusive gene. That makes it informative in two directions at once: where p53 is intact it tracks pathway output, and where p53 is not it keeps tracking general stress. That dual behaviour makes it a useful internal control on [[Signing genes by p53 direction]] and on what residual induction means under [[p53 nullification in cancer cell lines]]. Its muscle-atrophy function is a thematic adjacency to [[MG53 (TRIM72)]] rather than a mechanistic link, and should not be read as one.

## What is uncertain

The intron 3 response element makes the direct-target status secure, but attributing any particular induction to p53 is less secure here than for any other canonical target in the panel, because the p53-independent inputs are strong and a 379-compound library supplies exactly those inputs — ATF4-driven integrated stress response, oxidative stress, HDAC and methyltransferase inhibition. Whether GADD45A is pro-apoptotic or protective is context-dependent and both have been reported in reputable systems; the arrest function is the better-supported one. The DNA demethylation role should not be assumed. And the muscle work, solid as it is in muscle, says nothing about pooled cancer lines.

## References

- Kastan et al., 1992, Cell — placed GADD45 in a mammalian cell-cycle checkpoint pathway using p53, and showed the pathway is defective in ataxia-telangiectasia.
- Hollander et al., 1999, Nature Genetics — showed Gadd45a-deficient mice have genomic instability, centrosome amplification and increased radiation-induced tumorigenesis, phenocopying parts of p53 loss.
- Ebert et al., 2012, Journal of Biological Chemistry — showed stress-induced Gadd45a is the ATF4 effector required for muscle atrophy from fasting, immobilisation and denervation, and sufficient to cause it alone.
- Tamura et al., 2012, Current Molecular Medicine — review of the GADD45 family in DNA repair, cell-cycle control, senescence and genotoxic stress, including the argument that GADD45 induction is required for the activity of several chemotherapeutic drugs.

## What is on record

| | |
|---|---|
| Official name | growth arrest and DNA damage inducible alpha |
| Also known as | GADD45 |
| Locus | 1p31.3 — gene with protein product |
| Gene families | Growth arrest and DNA damage inducible family |
| Previously named | growth arrest and DNA-damage-inducible, alpha |

**Function**, from UniProt [P24522](https://www.uniprot.org/uniprotkb/P24522) (reviewed):

> In T-cells, functions as a regulator of p38 MAPKs by inhibiting p88 phosphorylation and activity (By similarity). Might affect PCNA interaction with some CDK (cell division protein kinase) complexes; stimulates DNA excision repair in vitro and inhibits entry of cells into S phase

**Summary**, from NCBI Gene [1647](https://www.ncbi.nlm.nih.gov/gene/1647):

> This gene is a member of a group of genes whose transcript levels are increased following stressful growth arrest conditions and treatment with DNA-damaging agents. The protein encoded by this gene responds to environmental stresses by mediating activation of the p38/JNK pathway via MTK1/MEKK4 kinase. The DNA damage-induced transcription of this gene is mediated by both p53-dependent and -independent mechanisms. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene.[provided by RefSeq, Dec 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4095) · Entrez [1647](https://www.ncbi.nlm.nih.gov/gene/1647) · UniProt [P24522](https://www.uniprot.org/uniprotkb/P24522) · Ensembl [ENSG00000116717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116717) · OMIM [126335](https://www.omim.org/entry/126335)

**PubMed**, as HGNC records for this gene — [1990262](https://pubmed.ncbi.nlm.nih.gov/1990262/), [8226988](https://pubmed.ncbi.nlm.nih.gov/8226988/), [30617255](https://pubmed.ncbi.nlm.nih.gov/30617255/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 60.91 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 23 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.111× |
| Wild-type minus altered | 1.091× |
| Compounds moving it up in WT lines | 62 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00650 |
| As a percentage | +0.45% |
| FDR, exposure-shuffle null | 0.2867 |
| In TP53-wild-type lines / altered lines | 0.00547 / 0.00713 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.485 raw, -0.080 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
