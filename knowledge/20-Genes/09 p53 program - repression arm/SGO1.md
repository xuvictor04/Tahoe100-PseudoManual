---
symbol: SGO1
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [shugoshin 1]
gene_name: shugoshin 1
locus: 3p24.3
locus_type: gene with protein product
gene_family: [Shugoshin family]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 25.07
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# SGO1

*shugoshin 1* — 3p24.3

> [!summary] In one line
> SGO1 encodes shugoshin 1, the mitotic protein that shields centromeric cohesin from premature removal so sister chromatids stay paired until anaphase.

## What it is

Shugoshin is recruited to centromeres by the Bub1-phosphorylated H2A-T120 mark and by contacts near CENP-A, and brings the phosphatase PP2A-B56 to the right place. PP2A dephosphorylates sororin and the cohesin subunit SA2, blocking the Wapl- and separase-driven cohesin release that strips cohesin from chromosome arms in prophase; Cdk1 phosphorylation of Sgo1 in mitosis switches on its direct cohesin binding, making the protection mitosis-specific. Loss produces premature sister-chromatid separation, missegregation and aneuploidy, and Sgo1 also participates in kinetochore tension sensing. Clinically, a homozygous founder variant causes CAID syndrome — chronic atrial and intestinal dysrhythmia — a cohesinopathy of sinus-node and gut pacemaker tissue, with accelerated cycling and increased senescence in patient fibroblasts.

## Why it appears in this work

SGO1 is a data-defined member of the repressed arm of [[p53 program P]]: it declines in TP53-wild-type lines under p53-activating compounds. That is the expected behaviour of a mitotic gene when p53 arrests cells — [[CDKN1A]] induction, CDK inhibition, and E2F/DREAM-mediated shutdown of the mitotic module. See [[The p21-DREAM axis]].

## What is uncertain

Whether "p53 target" means anything direct here. I know of no evidence for p53 occupancy at the SGO1 promoter, and the whole mitotic module — [[KIF11]], [[HJURP]], [[CENPN]] and this gene together — moves as a block, the signature of indirect repression through the cell cycle rather than gene-specific regulation. Its program membership is also only partially stable across cross-fitting folds, so it sits nearer the selection threshold than the strongly repressed cell-cycle genes. Treating its decline as evidence about p53's direct output would be over-reading ([[Signing genes by p53 direction]]).

## References

- Kitajima et al., 2006, Nature — showed that shugoshin collaborates with PP2A to protect centromeric cohesin.
- Liu, Rankin & Yu, 2013, Nature Cell Biology — Cdk-mediated mitotic phosphorylation of Sgo1 activates its direct cohesin binding.
- Chetaille et al., 2014, Nature Genetics — a homozygous SGO1 founder mutation causes CAID syndrome, a cohesinopathy of heart and gut rhythm.

## What is on record

| | |
|---|---|
| Official name | shugoshin 1 |
| Also known as | NY-BR-85 |
| Locus | 3p24.3 — gene with protein product |
| Gene families | Shugoshin family |
| Previously named | shugoshin-like 1 (S. pombe) |

**Function**, from UniProt [Q5FBB7](https://www.uniprot.org/uniprotkb/Q5FBB7) (reviewed):

> Plays a central role in chromosome cohesion during mitosis by preventing premature dissociation of cohesin complex from centromeres after prophase, when most of cohesin complex dissociates from chromosomes arms. May act by preventing phosphorylation of the STAG2 subunit of cohesin complex at the centromere, ensuring cohesin persistence at centromere until cohesin cleavage by ESPL1/separase at anaphase. Essential for proper chromosome segregation during mitosis and this function requires interaction with PPP2R1A. Its phosphorylated form is necessary for chromosome congression and for the proper attachment of spindle microtubule to the kinetochore. Necessary for kinetochore localization of PLK1 and CENPF. May play a role in the tension sensing mechanism of the spindle-assembly checkpoint by regulating PLK1 kinetochore affinity. Isoform 3 plays a role in maintaining centriole cohesion involved in controlling spindle pole integrity. Involved in centromeric enrichment of AUKRB in prometaphase

**Summary**, from NCBI Gene [151648](https://www.ncbi.nlm.nih.gov/gene/151648):

> The protein encoded by this gene is a member of the shugoshin family of proteins. This protein is thought to protect centromeric cohesin from cleavage during mitotic prophase by preventing phosphorylation of a cohesin subunit. Reduced expression of this gene leads to the premature loss of centromeric cohesion, mis-segregation of sister chromatids, and mitotic arrest. Evidence suggests that this protein also protects a small subset of cohesin found along the length of the chromosome arms during mitotic prophase. An isoform lacking exon 6 has been shown to play a role in the cohesion of centrioles (PMID: 16582621 and PMID:18331714). Mutations in this gene have been associated with Chronic Atrial and Intestinal Dysrhythmia (CAID) syndrome, characterized by the co-occurrence of Sick Sinus Syndrome (SSS) and Chronic Intestinal Pseudo-obstruction (CIPO) within the first four decades of life (PMID:25282101). Fibroblast cells from CAID patients exhibited both increased cell proliferation and higher rates of senescence. Pseudogenes of this gene have been found on chromosomes 1 and 7. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25088) · Entrez [151648](https://www.ncbi.nlm.nih.gov/gene/151648) · UniProt [Q5FBB7](https://www.uniprot.org/uniprotkb/Q5FBB7) · Ensembl [ENSG00000129810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129810) · OMIM [609168](https://www.omim.org/entry/609168)

**PubMed**, as HGNC records for this gene — [12747765](https://pubmed.ncbi.nlm.nih.gov/12747765/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 25.07 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.896× |
| Wild-type minus altered | 0.945× |
| Compounds moving it up in WT lines | 20 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00213 |
| As a percentage | +0.15% |
| FDR, exposure-shuffle null | 0.5251 |
| In TP53-wild-type lines / altered lines | -0.00236 / 0.00466 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.247 raw, 0.056 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[The p21-DREAM axis]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, repression arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
