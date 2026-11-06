---
symbol: HELZ
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0054, HUMORF5, DHRC]
gene_name: helicase with zinc finger
locus: 17q24.2
locus_type: gene with protein product
gene_family: [Zinc fingers CCCH-type, UPF1 like RNA helicases]
family_siblings_here: [C12orf50, PAN3, RC3H1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 351.32
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# HELZ

*helicase with zinc finger* — 17q24.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HELZ.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | helicase with zinc finger |
| Also known as | KIAA0054, HUMORF5, DHRC, down-regulated in human cancers |
| Locus | 17q24.2 — gene with protein product |
| Gene families | Zinc fingers CCCH-type; UPF1 like RNA helicases |
| Other genes here in those families | [[C12orf50]], [[PAN3]], [[RC3H1]] |

**Function**, from UniProt [P42694](https://www.uniprot.org/uniprotkb/P42694) (reviewed):

> ATP-dependent RNA helicase that promotes degradation of mRNAs via its association with the CCR4-NOT deadenylase complex, leading to deadenylation, decapping, and subsequent degradation of target mRNAs (PubMed:31570513). Can repress translation independently of mRNA decay in a manner dependent on both the CCR4-NOT complex and the helicase DDX6 (PubMed:31570513). Involved in promoting cell proliferation, translation initiation, and ribosomal protein S6 (RPS6) phosphorylation (PubMed:21765940)

**Summary**, from NCBI Gene [9931](https://www.ncbi.nlm.nih.gov/gene/9931):

> HELZ is a member of the superfamily I class of RNA helicases. RNA helicases alter the conformation of RNA by unwinding double-stranded regions, thereby altering the biologic activity of the RNA molecule and regulating access to other proteins (Wagner et al., 1999 [PubMed 10471385]).[supplied by OMIM, Mar 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16878) · Entrez [9931](https://www.ncbi.nlm.nih.gov/gene/9931) · UniProt [P42694](https://www.uniprot.org/uniprotkb/P42694) · Ensembl [ENSG00000198265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198265) · OMIM [606699](https://www.omim.org/entry/606699)

**PubMed**, as HGNC records for this gene — [10471385](https://pubmed.ncbi.nlm.nih.gov/10471385/), [12691822](https://pubmed.ncbi.nlm.nih.gov/12691822/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 351.32 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 110 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.100× |
| Wild-type minus altered | 1.028× |
| Compounds moving it up in WT lines | 81 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00192 |
| As a percentage | -0.13% |
| FDR, exposure-shuffle null | 0.3928 |
| In TP53-wild-type lines / altered lines | 0.00112 / -0.00376 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.088 raw, 0.164 with 3 PCs removed |

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
