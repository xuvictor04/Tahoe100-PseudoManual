---
symbol: FBXO22
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FBX22, FISTC1]
gene_name: F-box protein 22
locus: 15q24.2
locus_type: gene with protein product
gene_family: [F-boxes other]
family_siblings_here: [FBXO42]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 65.27
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FBXO22

*F-box protein 22* — 15q24.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FBXO22.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | F-box protein 22 |
| Also known as | FBX22, FISTC1, FIST domain containing 1 |
| Locus | 15q24.2 — gene with protein product |
| Gene families | F-boxes other |
| Other genes here in those families | [[FBXO42]] |
| Previously named | F-box only protein 22 |

**Function**, from UniProt [Q8NEZ5](https://www.uniprot.org/uniprotkb/Q8NEZ5) (reviewed):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex that is implicated in the control of various cellular processes such as cell cycle control, transcriptional regulation, DNA damage repair, and apoptosis. Promotes the proteasome-dependent degradation of key sarcomeric proteins, such as alpha-actinin (ACTN2) and filamin-C (FLNC), essential for maintenance of normal contractile function. Acts as a key regulator of histone methylation marks namely H3K9 and H3K36 methylation through the regulation of histone demethylase KDM4A protein levels (PubMed:21768309). In complex with KDM4A, also regulates the abundance of TP53 by targeting methylated TP53 for degradation at the late senescent stage (PubMed:26868148). Under oxidative stress, promotes the ubiquitination and degradation of BACH1. Mechanistically, reactive oxygen species (ROS) covalently modify cysteine residues on the bZIP domain of BACH1, leading to its release from chromatin and making it accessible to FBXO22 (PubMed:39504958). Upon amino acid depletion, mediates 'Lys-27'-linked ubiquitination of MTOR and thereby inhibits substrate recruitment to mTORC1 (PubMed:37979583). Also inhibits SARS-CoV-2 replication by inducing NSP5 degradation (PubMed:39223933)

**Summary**, from NCBI Gene [26263](https://www.ncbi.nlm.nih.gov/gene/26263):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction modules or no recognizable motifs. The protein encoded by this gene belongs to the Fbxs class and, as a transcriptional target of the tumor protein p53, is thought to be involved in degradation of specific proteins in response to p53 induction. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13593) · Entrez [26263](https://www.ncbi.nlm.nih.gov/gene/26263) · UniProt [Q8NEZ5](https://www.uniprot.org/uniprotkb/Q8NEZ5) · Ensembl [ENSG00000167196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167196) · OMIM [609096](https://www.omim.org/entry/609096)

**PubMed**, as HGNC records for this gene — [10531035](https://pubmed.ncbi.nlm.nih.gov/10531035/), [10531037](https://pubmed.ncbi.nlm.nih.gov/10531037/), [17855421](https://pubmed.ncbi.nlm.nih.gov/17855421/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 65.27 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 18 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.124× |
| Wild-type minus altered | 1.106× |
| Compounds moving it up in WT lines | 83 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00426 |
| As a percentage | +0.30% |
| FDR, exposure-shuffle null | 0.0991 |
| In TP53-wild-type lines / altered lines | 0.00099 / 0.00625 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.295 raw, -0.007 with 3 PCs removed |

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
