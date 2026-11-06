---
symbol: PLA2G12B
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: phospholipase A2 group XIIB
locus: 10q22.1
locus_type: gene with protein product
gene_family: [Phospholipases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PLA2G12B

*phospholipase A2 group XIIB* — 10q22.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PLA2G12B.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | phospholipase A2 group XIIB |
| Also known as | — (no recorded alias) |
| Locus | 10q22.1 — gene with protein product |
| Gene families | Phospholipases |
| Previously named | phospholipase A2, group XIII; phospholipase A2, group XIIB |

**Function**, from UniProt [Q9BX93](https://www.uniprot.org/uniprotkb/Q9BX93) (reviewed):

> Not known; does not seem to have catalytic activity

**Summary**, from NCBI Gene [84647](https://www.ncbi.nlm.nih.gov/gene/84647):

> The protein encoded by this gene belongs to the phospholipase A2 (PLA2) group of enzymes, which function in glycolipid hydrolysis with the release of free fatty acids and lysophospholipids. This family member has altered phospholipid-binding properties and is catalytically inactive. The protein is secreted, and together with microsomal triglyceride transfer protein, it functions to regulate HNF4alpha-induced hepatitis C virus infectivity. The expression of this gene is down-regulated in various tumors, suggesting that it may function as a negative regulator of tumor progression. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Dec 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18555) · Entrez [84647](https://www.ncbi.nlm.nih.gov/gene/84647) · UniProt [Q9BX93](https://www.uniprot.org/uniprotkb/Q9BX93) · Ensembl [ENSG00000138308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138308) · OMIM [611653](https://www.omim.org/entry/611653)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06649 |
| As a percentage | +4.72% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.05592 / 0.07290 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.620 raw, 0.399 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
