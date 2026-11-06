---
symbol: COP1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ10416, RNF200, FAP78, CFAP78]
gene_name: COP1 E3 ubiquitin ligase
locus: 1q25.1-q25.2
locus_type: gene with protein product
gene_family: [Ring finger proteins, WD repeat domain containing, Cilia and flagella associated, Small nucleolar RNA protein coding host genes, RING finger E3 ubiquitin protein ligases]
family_siblings_here: [DDB2, DNAI3, FBXW7, MDM2, MDM4, MGRN1, NAP1L4, PCGF3, RC3H1, RIC1, TLE4, TRIM72]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 264.49
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# COP1

*COP1 E3 ubiquitin ligase* — 1q25.1-q25.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/COP1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | COP1 E3 ubiquitin ligase |
| Also known as | FLJ10416, RNF200, FAP78, CFAP78, constitutive photomorphogenic protein 1 (Arabidopsis) |
| Locus | 1q25.1-q25.2 — gene with protein product |
| Gene families | Ring finger proteins; WD repeat domain containing; Cilia and flagella associated; Small nucleolar RNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Other genes here in those families | [[DDB2]], [[DNAI3]], [[FBXW7]], [[MDM2]], [[MDM4]], [[MGRN1]], [[NAP1L4]], [[PCGF3]], [[RC3H1]], [[RIC1]], [[TLE4]], [[TRIM72]], [[WDR48]] |
| Previously named | ring finger and WD repeat domain 2 |

**Function**, from UniProt [Q8NHY2](https://www.uniprot.org/uniprotkb/Q8NHY2) (reviewed):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent proteasomal degradation of target proteins. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Involved in JUN ubiquitination and degradation. Directly involved in p53 (TP53) ubiquitination and degradation, thereby abolishing p53-dependent transcription and apoptosis. Ubiquitinates p53 independently of MDM2 or RCHY1. Probably mediates E3 ubiquitin ligase activity by functioning as the essential RING domain subunit of larger E3 complexes. In contrast, it does not constitute the catalytic RING subunit in the DCX DET1-COP1 complex that negatively regulates JUN, the ubiquitin ligase activity being mediated by RBX1. Involved in 14-3-3 protein sigma/SFN ubiquitination and proteasomal degradation, leading to AKT activation and promotion of cell survival. Ubiquitinates MTA1 leading to its proteasomal degradation. Upon binding to TRIB1, ubiquitinates CEBPA, which lacks a canonical COP1-binding motif (Probable)

**Summary**, from NCBI Gene [64326](https://www.ncbi.nlm.nih.gov/gene/64326):

> Enables ubiquitin protein ligase activity. Involved in several processes, including negative regulation of fatty acid biosynthetic process; positive regulation of proteasomal ubiquitin-dependent protein catabolic process; and response to ionizing radiation. Part of Cul4A-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17440) · Entrez [64326](https://www.ncbi.nlm.nih.gov/gene/64326) · UniProt [Q8NHY2](https://www.uniprot.org/uniprotkb/Q8NHY2) · Ensembl [ENSG00000143207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143207) · OMIM [608067](https://www.omim.org/entry/608067)

**PubMed**, as HGNC records for this gene — [10395541](https://pubmed.ncbi.nlm.nih.gov/10395541/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 264.49 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 180 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.029× |
| Wild-type minus altered | 1.020× |
| Compounds moving it up in WT lines | 61 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00172 |
| As a percentage | +0.12% |
| FDR, exposure-shuffle null | 0.3725 |
| In TP53-wild-type lines / altered lines | 0.00296 / 0.00097 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.432 raw, 0.051 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
