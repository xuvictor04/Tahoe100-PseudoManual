---
symbol: HPN
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [TMPRSS1]
gene_name: hepsin
locus: 19q13.11
locus_type: gene with protein product
gene_family: [Scavenger receptor cysteine rich domain containing, Type II transmembrane serine proteases]
family_siblings_here: [TMPRSS9]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# HPN

*hepsin* — 19q13.11

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HPN.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | hepsin |
| Also known as | TMPRSS1, transmembrane protease, serine 1 |
| Locus | 19q13.11 — gene with protein product |
| Gene families | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases |
| Other genes here in those families | [[TMPRSS9]] |

**Function**, from UniProt [P05981](https://www.uniprot.org/uniprotkb/P05981) (reviewed):

> Serine protease that cleaves extracellular substrates, and contributes to the proteolytic processing of growth factors, such as HGF and MST1/HGFL (PubMed:15839837, PubMed:21875933). Plays a role in cell growth and maintenance of cell morphology (PubMed:21875933, PubMed:8346233). Plays a role in the proteolytic processing of ACE2 (PubMed:24227843). Mediates the proteolytic cleavage of urinary UMOD that is required for UMOD polymerization (PubMed:26673890)

**Summary**, from NCBI Gene [3249](https://www.ncbi.nlm.nih.gov/gene/3249):

> This gene encodes a type II transmembrane serine protease that may be involved in diverse cellular functions, including blood coagulation and the maintenance of cell morphology. Expression of the encoded protein is associated with the growth and progression of cancers, particularly prostate cancer. The protein is cleaved into a catalytic serine protease chain and a non-catalytic scavenger receptor cysteine-rich chain, which associate via a single disulfide bond. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:5155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5155) · Entrez [3249](https://www.ncbi.nlm.nih.gov/gene/3249) · UniProt [P05981](https://www.uniprot.org/uniprotkb/P05981) · Ensembl [ENSG00000105707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105707) · OMIM [142440](https://www.omim.org/entry/142440)

**PubMed**, as HGNC records for this gene — [2835076](https://pubmed.ncbi.nlm.nih.gov/2835076/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07835 |
| As a percentage | +5.58% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07742 / 0.07892 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.338 raw, 0.413 with 3 PCs removed |

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
