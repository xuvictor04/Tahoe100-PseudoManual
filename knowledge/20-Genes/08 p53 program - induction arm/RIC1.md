---
symbol: RIC1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [bA207C16.1]
gene_name: RIC1 partner of RAB6A GEF complex
locus: 9p24.1
locus_type: gene with protein product
gene_family: [WD repeat domain containing]
family_siblings_here: [COP1, DDB2, DNAI3, FBXW7, TLE4, WDR48]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 117.31
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RIC1

*RIC1 partner of RAB6A GEF complex* — 9p24.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RIC1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | RIC1 partner of RAB6A GEF complex |
| Also known as | bA207C16.1 |
| Locus | 9p24.1 — gene with protein product |
| Gene families | WD repeat domain containing |
| Other genes here in those families | [[COP1]], [[DDB2]], [[DNAI3]], [[FBXW7]], [[TLE4]], [[WDR48]] |
| Previously named | RIC1 homolog, RAB6A GEF complex partner 1; KIAA1432; RAB6A GEF complex partner 1 |

**Function**, from UniProt [Q4ADV7](https://www.uniprot.org/uniprotkb/Q4ADV7) (reviewed):

> The RIC1-RGP1 complex acts as a guanine nucleotide exchange factor (GEF), which activates RAB6A by exchanging bound GDP for free GTP, and may thereby be required for efficient fusion of endosome-derived vesicles with the Golgi compartment (PubMed:23091056). The RIC1-RGP1 complex participates in the recycling of mannose-6-phosphate receptors (PubMed:23091056). Required for phosphorylation and localization of GJA1 (PubMed:16112082). Is a regulator of procollagen transport and secretion, and is required for correct cartilage morphogenesis and development of the craniofacial skeleton (PubMed:31932796)

**Summary**, from NCBI Gene [57589](https://www.ncbi.nlm.nih.gov/gene/57589):

> Enables guanyl-nucleotide exchange factor activity and small GTPase binding activity. Involved in several processes, including positive regulation of GTPase activity; regulation of extracellular matrix constituent secretion; and retrograde transport, endosome to Golgi. Located in cytosol and membrane. Part of Ric1-Rgp1 guanyl-nucleotide exchange factor complex. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17686) · Entrez [57589](https://www.ncbi.nlm.nih.gov/gene/57589) · UniProt [Q4ADV7](https://www.uniprot.org/uniprotkb/Q4ADV7) · Ensembl [ENSG00000107036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107036) · OMIM [610354](https://www.omim.org/entry/610354)

**PubMed**, as HGNC records for this gene — [10718198](https://pubmed.ncbi.nlm.nih.gov/10718198/), [23091056](https://pubmed.ncbi.nlm.nih.gov/23091056/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 117.31 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 165 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.044× |
| Wild-type minus altered | 1.029× |
| Compounds moving it up in WT lines | 71 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00111 |
| As a percentage | -0.08% |
| FDR, exposure-shuffle null | 0.6699 |
| In TP53-wild-type lines / altered lines | 0.00044 / -0.00206 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.300 raw, -0.015 with 3 PCs removed |

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
