---
symbol: ROPN1L
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [ASP, FLJ25776, RSPH11, RP11-1C1.7, TCONS_00009352]
gene_name: rhophilin associated tail protein 1 like
locus: 5p15.2
locus_type: gene with protein product
gene_family: [MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# ROPN1L

*rhophilin associated tail protein 1 like* — 5p15.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ROPN1L.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | rhophilin associated tail protein 1 like |
| Also known as | ASP, FLJ25776, RSPH11, RP11-1C1.7, TCONS_00009352, AKAP-associated sperm protein, radial spoke head 11 homolog (Chlamydomonas) |
| Locus | 5p15.2 — gene with protein product |
| Gene families | MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]] |
| Previously named | ropporin 1-like; rhophilin associated tail protein 1-like; long intergenic non-protein coding RNA 1513 |

**Function**, from UniProt [Q96C74](https://www.uniprot.org/uniprotkb/Q96C74) (reviewed):

> Functions as part of axonemal radial spoke complexes that play an important part in the motility of sperm and cilia. Important for male fertility. With ROPN1, involved in fibrous sheath integrity and sperm motility, plays a role in PKA-dependent signaling processes required for spermatozoa capacitation

**Summary**, from NCBI Gene [83853](https://www.ncbi.nlm.nih.gov/gene/83853):

> This gene encodes a member of the ropporin family. The encoded protein is present in sperm and interacts with A-kinase anchoring protein, AKAP3, through the amphipathic helix region of AKAP3. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Oct 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24060) · Entrez [83853](https://www.ncbi.nlm.nih.gov/gene/83853) · UniProt [Q96C74](https://www.uniprot.org/uniprotkb/Q96C74) · Ensembl [ENSG00000145491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145491) · OMIM [611756](https://www.omim.org/entry/611756)

**PubMed**, as HGNC records for this gene — [11278869](https://pubmed.ncbi.nlm.nih.gov/11278869/), [35003358](https://pubmed.ncbi.nlm.nih.gov/35003358/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06253 |
| As a percentage | +4.43% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07117 / 0.05641 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.688 raw, 0.565 with 3 PCs removed |

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
