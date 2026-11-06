---
symbol: RALGAPB
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DKFZp781M2411, RalGAPbeta]
gene_name: Ral GTPase activating protein non-catalytic subunit beta
locus: 20q11.23
locus_type: gene with protein product
gene_family: [Armadillo like helical domain containing, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ARFGEF1, ARFGEF2, ARMH3, ATF5, ATM, BBC3, DNAJC5, DNMT3A, EZH1, FANCD2, FBXW7]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 128.62
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RALGAPB

*Ral GTPase activating protein non-catalytic subunit beta* — 20q11.23

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RALGAPB.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | Ral GTPase activating protein non-catalytic subunit beta |
| Also known as | DKFZp781M2411, RalGAPbeta |
| Locus | 20q11.23 — gene with protein product |
| Gene families | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ARFGEF1]], [[ARFGEF2]], [[ARMH3]], [[ATF5]], [[ATM]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FANCD2]], [[FBXW7]], [[GDF15]], [[HTT]] |
| Previously named | KIAA1219 |

**Function**, from UniProt [Q86X10](https://www.uniprot.org/uniprotkb/Q86X10) (reviewed):

> Non-catalytic subunit of the heterodimeric RalGAP1 and RalGAP2 complexes which act as GTPase activators for the Ras-like small GTPases RALA and RALB

**Summary**, from NCBI Gene [57148](https://www.ncbi.nlm.nih.gov/gene/57148):

> Enables protein heterodimerization activity. Predicted to be involved in Ral protein signal transduction and activation of GTPase activity. Predicted to act upstream of or within regulation of exocyst localization and regulation of protein localization. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29221) · Entrez [57148](https://www.ncbi.nlm.nih.gov/gene/57148) · UniProt [Q86X10](https://www.uniprot.org/uniprotkb/Q86X10) · Ensembl [ENSG00000170471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170471) · OMIM [618833](https://www.omim.org/entry/618833)

**PubMed**, as HGNC records for this gene — [19520869](https://pubmed.ncbi.nlm.nih.gov/19520869/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 128.62 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 15 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.090× |
| Wild-type minus altered | 1.051× |
| Compounds moving it up in WT lines | 80 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00415 |
| As a percentage | -0.29% |
| FDR, exposure-shuffle null | 0.0078 |
| In TP53-wild-type lines / altered lines | -0.00385 / -0.00433 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.259 raw, -0.181 with 3 PCs removed |

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
