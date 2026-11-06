---
symbol: NADSYN1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ10631]
gene_name: NAD synthetase 1
locus: 11q13.4
locus_type: gene with protein product
gene_family: [MicroRNA protein coding host genes, Ligases]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NOTCH1, NUP210L, PER1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 33.56
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# NADSYN1

*NAD synthetase 1* — 11q13.4

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NADSYN1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | NAD synthetase 1 |
| Also known as | FLJ10631 |
| Locus | 11q13.4 — gene with protein product |
| Gene families | MicroRNA protein coding host genes; Ligases |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]], [[PRKD2]] |

**Function**, from UniProt [Q6IA69](https://www.uniprot.org/uniprotkb/Q6IA69) (reviewed):

> Catalyzes the final step of the nicotinamide adenine dinucleotide (NAD) de novo synthesis pathway, the ATP-dependent amidation of deamido-NAD using L-glutamine as a nitrogen source

**Summary**, from NCBI Gene [55191](https://www.ncbi.nlm.nih.gov/gene/55191):

> Nicotinamide adenine dinucleotide (NAD) is a coenzyme in metabolic redox reactions, a precursor for several cell signaling molecules, and a substrate for protein posttranslational modifications. NAD synthetase (EC 6.3.5.1) catalyzes the final step in the biosynthesis of NAD from nicotinic acid adenine dinucleotide (NaAD).[supplied by OMIM, Apr 2004]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29832) · Entrez [55191](https://www.ncbi.nlm.nih.gov/gene/55191) · UniProt [Q6IA69](https://www.uniprot.org/uniprotkb/Q6IA69) · Ensembl [ENSG00000172890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172890) · OMIM [608285](https://www.omim.org/entry/608285)

**PubMed**, as HGNC records for this gene — [12547821](https://pubmed.ncbi.nlm.nih.gov/12547821/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 33.56 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 113 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.045× |
| Wild-type minus altered | 1.054× |
| Compounds moving it up in WT lines | 63 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00162 |
| As a percentage | -0.11% |
| FDR, exposure-shuffle null | 0.5703 |
| In TP53-wild-type lines / altered lines | -0.00377 / -0.00031 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.109 raw, -0.060 with 3 PCs removed |

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
