---
symbol: KDM4C
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [GASC1, KIAA0780, TDRD14C]
gene_name: lysine demethylase 4C
locus: 9p24.1
locus_type: gene with protein product
gene_family: [PHD finger proteins, Tudor domain containing, Lysine demethylase 4 family]
family_siblings_here: [KDM4B, TAF3, TP53BP1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 320.73
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# KDM4C

*lysine demethylase 4C* — 9p24.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/KDM4C.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | lysine demethylase 4C |
| Also known as | GASC1, KIAA0780, TDRD14C, tudor domain containing 14C |
| Locus | 9p24.1 — gene with protein product |
| Gene families | PHD finger proteins; Tudor domain containing; Lysine demethylase 4 family |
| Other genes here in those families | [[KDM4B]], [[TAF3]], [[TP53BP1]] |
| Previously named | jumonji domain containing 2C; lysine (K)-specific demethylase 4C |

**Function**, from UniProt [Q9H3R0](https://www.uniprot.org/uniprotkb/Q9H3R0) (reviewed):

> Histone demethylase that specifically demethylates 'Lys-9' and 'Lys-36' residues of histone H3, thereby acting as a key regulator of nascent transcription (PubMed:16603238, PubMed:21914792, PubMed:28262558). Does not demethylate histone H3 'Lys-4', H3 'Lys-27' nor H4 'Lys-20' (PubMed:16603238, PubMed:28262558). Demethylates trimethylated H3 'Lys-9' and H3 'Lys-36' residue, while it has no activity on mono- and dimethylated residues (PubMed:16603238, PubMed:21914792, PubMed:28262558)

**Summary**, from NCBI Gene [23081](https://www.ncbi.nlm.nih.gov/gene/23081):

> This gene is a member of the Jumonji domain 2 (JMJD2) family. The encoded protein is a trimethylation-specific demethylase, and converts specific trimethylated histone residues to the dimethylated form. This enzymatic action regulates gene expression and chromosome segregation. Chromosomal aberrations and changes in expression of this gene may be found in tumor cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17071) · Entrez [23081](https://www.ncbi.nlm.nih.gov/gene/23081) · UniProt [Q9H3R0](https://www.uniprot.org/uniprotkb/Q9H3R0) · Ensembl [ENSG00000107077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107077) · OMIM [605469](https://www.omim.org/entry/605469)

**PubMed**, as HGNC records for this gene — [9872452](https://pubmed.ncbi.nlm.nih.gov/9872452/), [15138608](https://pubmed.ncbi.nlm.nih.gov/15138608/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 320.73 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 101 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.030× |
| Wild-type minus altered | 1.025× |
| Compounds moving it up in WT lines | 62 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00440 |
| As a percentage | +0.31% |
| FDR, exposure-shuffle null | 0.0277 |
| In TP53-wild-type lines / altered lines | 0.00599 / 0.00340 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.182 raw, 0.317 with 3 PCs removed |

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
