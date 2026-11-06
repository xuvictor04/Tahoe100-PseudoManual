---
symbol: ELL
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [Men, ELL1, PPP1R68]
gene_name: elongation factor for RNA polymerase II
locus: 19p13.11
locus_type: gene with protein product
gene_family: [Protein phosphatase 1 regulatory subunits, Super elongation complex]
family_siblings_here: [PPP1R36]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 68.75
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ELL

*elongation factor for RNA polymerase II* — 19p13.11

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ELL.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | elongation factor for RNA polymerase II |
| Also known as | Men, ELL1, PPP1R68, protein phosphatase 1, regulatory subunit 68, eleven-nineteen lysine-rich leukemia gene |
| Locus | 19p13.11 — gene with protein product |
| Gene families | Protein phosphatase 1 regulatory subunits; Super elongation complex |
| Other genes here in those families | [[PPP1R36]] |
| Previously named | chromosome 19 open reading frame 17; elongation factor RNA polymerase II |

**Function**, from UniProt [P55199](https://www.uniprot.org/uniprotkb/P55199) (reviewed):

> Elongation factor component of the super elongation complex (SEC), a complex required to increase the catalytic rate of RNA polymerase II transcription by suppressing transient pausing by the polymerase at multiple sites along the DNA. Elongation factor component of the little elongation complex (LEC), a complex required to regulate small nuclear RNA (snRNA) gene transcription by RNA polymerase II and III (PubMed:22195968, PubMed:23932780). Specifically required for stimulating the elongation step of RNA polymerase II- and III-dependent snRNA gene transcription (PubMed:23932780). ELL also plays an early role before its assembly into in the SEC complex by stabilizing RNA polymerase II recruitment/initiation and entry into the pause site. Required to stabilize the pre-initiation complex and early elongation

**Summary**, from NCBI Gene [8178](https://www.ncbi.nlm.nih.gov/gene/8178):

> Enables phosphatase binding activity. Involved in positive regulation of DNA-templated transcription and snRNA transcription. Located in euchromatin and nuclear ribonucleoprotein granule. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:23114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23114) · Entrez [8178](https://www.ncbi.nlm.nih.gov/gene/8178) · UniProt [P55199](https://www.uniprot.org/uniprotkb/P55199) · Ensembl [ENSG00000105656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105656) · OMIM [600284](https://www.omim.org/entry/600284)

**PubMed**, as HGNC records for this gene — [7991593](https://pubmed.ncbi.nlm.nih.gov/7991593/), [8596958](https://pubmed.ncbi.nlm.nih.gov/8596958/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 68.75 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 115 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.063× |
| Wild-type minus altered | 1.039× |
| Compounds moving it up in WT lines | 68 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00320 |
| As a percentage | +0.22% |
| FDR, exposure-shuffle null | 0.2749 |
| In TP53-wild-type lines / altered lines | 0.00390 / 0.00277 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.164 raw, 0.170 with 3 PCs removed |

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
