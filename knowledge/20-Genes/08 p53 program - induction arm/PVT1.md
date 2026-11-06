---
symbol: PVT1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FFX, HNB, NCRNA00079, LINC00079, onco-lncRNA-100, MIR1204HG]
gene_name: Pvt1 oncogene
locus: 8q24.21
locus_type: RNA, long non-coding
gene_family: [MicroRNA non-coding host genes, Long non-coding RNAs with non-systematic symbols]
family_siblings_here: [ENSG00000251095, LMO7DN, MIR34AHG, MIR3659HG, MIR9-1HG, MIR924HG, PINCR, PURPL, RFPL3S]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 470.01
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PVT1

*Pvt1 oncogene* — 8q24.21

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PVT1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | Pvt1 oncogene |
| Also known as | FFX, HNB, NCRNA00079, LINC00079, onco-lncRNA-100, MIR1204HG, TP53LC09, Firefox, Honeybadger, non-protein coding RNA 79, long intergenic non-protein coding RNA 79, MIR1204, MIR1205, MIR1206 and MIR1207 host gene, plasmacytoma variant translocation 1, HLA-A24 ligand (HWNDTRPAHF, HF10) |
| Locus | 8q24.21 — RNA, long non-coding |
| Gene families | MicroRNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Other genes here in those families | [[ENSG00000251095]], [[LMO7DN]], [[MIR34AHG]], [[MIR3659HG]], [[MIR9-1HG]], [[MIR924HG]], [[PINCR]], [[PURPL]], [[RFPL3S]] |
| Previously named | pvt-1 (murine) oncogene homolog, MYC activator; Pvt1 oncogene homolog (mouse); Pvt1 oncogene (non-protein coding) |

**Summary**, from NCBI Gene [5820](https://www.ncbi.nlm.nih.gov/gene/5820):

> This gene represents a long non-coding RNA locus that has been identified as a candidate oncogene. Increased copy number and overexpression of this gene are associated with many types of cancers including breast and ovarian cancers, acute myeloid leukemia and Hodgkin lymphoma. Allelic variants of this gene are also associated with end-stage renal disease attributed to type 1 diabetes. Consistent with its association with various types of cancer, transcription of this gene is regulated by the tumor suppressor p53 through a canonical p53-binding site, and it has been implicated in regulating levels of the proto-oncogene MYC to promote tumorigenesis. [provided by RefSeq, Sep 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9709) · Entrez [5820](https://www.ncbi.nlm.nih.gov/gene/5820) · Ensembl [ENSG00000249859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249859) · OMIM [165140](https://www.omim.org/entry/165140)

**PubMed**, as HGNC records for this gene — [42618323](https://pubmed.ncbi.nlm.nih.gov/42618323/), [42618324](https://pubmed.ncbi.nlm.nih.gov/42618324/), [17503467](https://pubmed.ncbi.nlm.nih.gov/17503467/), [23801869](https://pubmed.ncbi.nlm.nih.gov/23801869/), [40035876](https://pubmed.ncbi.nlm.nih.gov/40035876/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 470.01 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 34 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.102× |
| Wild-type minus altered | 1.085× |
| Compounds moving it up in WT lines | 83 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00136 |
| As a percentage | +0.09% |
| FDR, exposure-shuffle null | 0.7298 |
| In TP53-wild-type lines / altered lines | -0.00108 / 0.00284 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.215 raw, 0.022 with 3 PCs removed |

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
