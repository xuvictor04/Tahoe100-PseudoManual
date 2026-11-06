---
symbol: SDHA
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FP, SDHF]
gene_name: succinate dehydrogenase complex flavoprotein subunit A
locus: 5p15.33
locus_type: gene with protein product
gene_family: [Mitochondrial complex II: succinate dehydrogenase subunits, Flavoproteins]
family_siblings_here: [FDXR, RETSAT]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 73.71
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SDHA

*succinate dehydrogenase complex flavoprotein subunit A* — 5p15.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SDHA.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | succinate dehydrogenase complex flavoprotein subunit A |
| Also known as | FP, SDHF, succinate dehydrogenase [ubiquinone] flavoprotein subunit, flavoprotein subunit of complex II |
| Locus | 5p15.33 — gene with protein product |
| Gene families | Mitochondrial complex II: succinate dehydrogenase subunits; Flavoproteins |
| Other genes here in those families | [[FDXR]], [[RETSAT]] |
| Previously named | succinate dehydrogenase complex, subunit A, flavoprotein (Fp); succinate dehydrogenase complex subunit A, flavoprotein (Fp) |

**Function**, from UniProt [P31040](https://www.uniprot.org/uniprotkb/P31040) (reviewed):

> Flavoprotein (FP) subunit of succinate dehydrogenase (SDH) that is involved in complex II of the mitochondrial electron transport chain and is responsible for transferring electrons from succinate to ubiquinone (coenzyme Q) (PubMed:10746566, PubMed:24781757). SDH also oxidizes malate to the non-canonical enol form of oxaloacetate, enol-oxaloacetate (By similarity). Enol-oxaloacetate, which is a potent inhibitor of the succinate dehydrogenase activity, is further isomerized into keto-oxaloacetate (By similarity). Can act as a tumor suppressor (PubMed:20484225)

**Summary**, from NCBI Gene [6389](https://www.ncbi.nlm.nih.gov/gene/6389):

> This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identified on chromosome 3q29. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:10680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10680) · Entrez [6389](https://www.ncbi.nlm.nih.gov/gene/6389) · UniProt [P31040](https://www.uniprot.org/uniprotkb/P31040) · Ensembl [ENSG00000073578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073578) · OMIM [600857](https://www.omim.org/entry/600857)

**PubMed**, as HGNC records for this gene — [7798181](https://pubmed.ncbi.nlm.nih.gov/7798181/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 73.71 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 91 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.046× |
| Wild-type minus altered | 1.042× |
| Compounds moving it up in WT lines | 77 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00319 |
| As a percentage | -0.22% |
| FDR, exposure-shuffle null | 0.3120 |
| In TP53-wild-type lines / altered lines | -0.00217 / -0.00382 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.232 raw, -0.169 with 3 PCs removed |

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
