---
symbol: DHDH
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [HUM2DD]
gene_name: dihydrodiol dehydrogenase
locus: 19q13.33
locus_type: gene with protein product
gene_family: [Gfo/Idh/MocA-like oxidoreductase domain containing, Oxidoreductases]
family_siblings_here: [FDXR, RETSAT, TP53I3]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# DHDH

*dihydrodiol dehydrogenase* — 19q13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DHDH.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | dihydrodiol dehydrogenase |
| Also known as | HUM2DD, trans-1,2-dihydrobenzene-1,2-diol dehydrogenase |
| Locus | 19q13.33 — gene with protein product |
| Gene families | Gfo/Idh/MocA-like oxidoreductase domain containing; Oxidoreductases |
| Other genes here in those families | [[FDXR]], [[RETSAT]], [[TP53I3]] |

**Function**, from UniProt [Q9UQ10](https://www.uniprot.org/uniprotkb/Q9UQ10) (reviewed):

> Catalyzes the NADP(+)-linked oxidation of trans-dihydrodiols of aromatic hydrocarbons to the corresponding catechols. It also catalyzes the oxidation of several pentoses and hexoses. In the reverse reaction in the presence of NADPH, it acts as NADPH-linked reductase on a broad range of substrates including aldehydes, chetones, and alpha-dicarbonyl compounds such as 3-deoxyglucosone, camphorquinone and methylglyoxal

**Summary**, from NCBI Gene [27294](https://www.ncbi.nlm.nih.gov/gene/27294):

> This gene encodes an enzyme that belongs to the family of dihydrodiol dehydrogenases, which exist in multiple forms in mammalian tissues and are involved in the metabolism of xenobiotics and sugars. These enzymes catalyze the NADP1-linked oxidation of transdihydrodiols of aromatic hydrocarbons to corresponding catechols. This enzyme is a dimeric dihydrodiol dehydrogenase, and it differs from monomeric dihydrodiol dehydrogenases in its high substrate specificity for trans-dihydrodiols of aromatic hydrocarbons in the oxidative direction. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17887) · Entrez [27294](https://www.ncbi.nlm.nih.gov/gene/27294) · UniProt [Q9UQ10](https://www.uniprot.org/uniprotkb/Q9UQ10) · Ensembl [ENSG00000104808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104808) · OMIM [606377](https://www.omim.org/entry/606377)

**PubMed**, as HGNC records for this gene — [10477285](https://pubmed.ncbi.nlm.nih.gov/10477285/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06297 |
| As a percentage | +4.46% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07507 / 0.05563 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.623 raw, 0.408 with 3 PCs removed |

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
