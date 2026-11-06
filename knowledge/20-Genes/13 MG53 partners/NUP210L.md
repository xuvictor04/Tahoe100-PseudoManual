---
symbol: NUP210L
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: nucleoporin 210 like
locus: 1q21.3
locus_type: gene with protein product
gene_family: [MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, PER1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# NUP210L

*nucleoporin 210 like* — 1q21.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NUP210L.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | nucleoporin 210 like |
| Also known as | — (no recorded alias) |
| Locus | 1q21.3 — gene with protein product |
| Gene families | MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[PER1]], [[PLCL2]], [[PRKD2]] |
| Previously named | nucleoporin 210kDa like |

UniProt [Q5VU65](https://www.uniprot.org/uniprotkb/Q5VU65) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [91181](https://www.ncbi.nlm.nih.gov/gene/91181):

> Predicted to act upstream of or within Sertoli cell development and spermatid development. Predicted to be located in nuclear membrane. Predicted to be part of nuclear pore. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29915) · Entrez [91181](https://www.ncbi.nlm.nih.gov/gene/91181) · UniProt [Q5VU65](https://www.uniprot.org/uniprotkb/Q5VU65) · Ensembl [ENSG00000143552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143552) · OMIM [621033](https://www.omim.org/entry/621033)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06816 |
| As a percentage | +4.84% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06057 / 0.07276 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.731 raw, 0.524 with 3 PCs removed |

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
