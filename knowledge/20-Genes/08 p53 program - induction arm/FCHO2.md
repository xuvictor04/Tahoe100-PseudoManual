---
symbol: FCHO2
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: FCH and mu domain containing endocytic adaptor 2
locus: 5q13.2
locus_type: gene with protein product
gene_family: [F-BAR domain containing]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 132.67
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FCHO2

*FCH and mu domain containing endocytic adaptor 2* — 5q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FCHO2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | FCH and mu domain containing endocytic adaptor 2 |
| Also known as | — (no recorded alias) |
| Locus | 5q13.2 — gene with protein product |
| Gene families | F-BAR domain containing |
| Previously named | FCH domain only 2 |

**Function**, from UniProt [Q0JRZ9](https://www.uniprot.org/uniprotkb/Q0JRZ9) (reviewed):

> Functions in an early step of clathrin-mediated endocytosis. Has both a membrane binding/bending activity and the ability to recruit proteins essential to the formation of functional clathrin-coated pits. Has a lipid-binding activity with a preference for membranes enriched in phosphatidylserine and phosphoinositides (Pi(4,5) biphosphate) like the plasma membrane. Its membrane-bending activity might be important for the subsequent action of clathrin and adaptors in the formation of clathrin-coated vesicles. Involved in adaptor protein complex AP-2-dependent endocytosis of the transferrin receptor, it also functions in the AP-2-independent endocytosis of the LDL receptor

**Summary**, from NCBI Gene [115548](https://www.ncbi.nlm.nih.gov/gene/115548):

> Enables identical protein binding activity. Involved in clathrin coat assembly and clathrin-dependent endocytosis. Located in clathrin-coated pit and clathrin-coated vesicle. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25180) · Entrez [115548](https://www.ncbi.nlm.nih.gov/gene/115548) · UniProt [Q0JRZ9](https://www.uniprot.org/uniprotkb/Q0JRZ9) · Ensembl [ENSG00000157107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157107) · OMIM [613438](https://www.omim.org/entry/613438)

**PubMed**, as HGNC records for this gene — [39402328](https://pubmed.ncbi.nlm.nih.gov/39402328/), [41651837](https://pubmed.ncbi.nlm.nih.gov/41651837/), [15254787](https://pubmed.ncbi.nlm.nih.gov/15254787/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 132.67 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 64 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.051× |
| Wild-type minus altered | 1.033× |
| Compounds moving it up in WT lines | 78 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00471 |
| As a percentage | -0.33% |
| FDR, exposure-shuffle null | 0.1184 |
| In TP53-wild-type lines / altered lines | -0.00414 / -0.00506 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.337 raw, 0.137 with 3 PCs removed |

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
