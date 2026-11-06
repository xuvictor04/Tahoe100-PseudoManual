---
symbol: GAL3ST1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [CST]
gene_name: galactose-3-O-sulfotransferase 1
locus: 22q12.2
locus_type: gene with protein product
gene_family: [Sulfotransferases, membrane bound]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# GAL3ST1

*galactose-3-O-sulfotransferase 1* — 22q12.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/GAL3ST1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | galactose-3-O-sulfotransferase 1 |
| Also known as | CST, cerebroside (3' phosphoadenylylsulfate:galactosylceramide 3') sulfotransferase, galactosylceramide sulfotransferase |
| Locus | 22q12.2 — gene with protein product |
| Gene families | Sulfotransferases, membrane bound |

**Function**, from UniProt [Q99999](https://www.uniprot.org/uniprotkb/Q99999) (reviewed):

> Catalyzes the transfer of a sulfate group to position 3 of non-reducing beta-galactosyl residues in glycerolipids and sphingolipids, therefore participates in the biosynthesis of sulfoglycolipids (PubMed:8830034, PubMed:9030544). Catalyzes the synthesis of galactosylceramide sulfate (sulfatide), a major lipid component of the myelin sheath and of monogalactosylalkylacylglycerol sulfate (seminolipid), present in spermatocytes (PubMed:8830034). Seems to prefer beta-glycosides at the non-reducing termini of sugar chains attached to a lipid moiety (PubMed:8830034). Also acts on lactosylceramide, galactosyl 1-alkyl-2-sn-glycerol and galactosyl diacylglycerol (in vitro) (PubMed:8830034)

**Summary**, from NCBI Gene [9514](https://www.ncbi.nlm.nih.gov/gene/9514):

> Sulfonation, an important step in the metabolism of many drugs, xenobiotics, hormones, and neurotransmitters, is catalyzed by sulfotransferases. This gene encodes galactosylceramide sulfotransferase, which catalyzes the sulfation of membrane glycolipids including the final step in the synthesis of sulfatide, a major lipid component of the myelin sheath. This gene exhibits elevated expression in ovarian epithelial carcinoma and the encoded enzyme exhibits elevated activity in renal cell carcinoma. Mutations in this gene may be associated with reduced insulin resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24240) · Entrez [9514](https://www.ncbi.nlm.nih.gov/gene/9514) · UniProt [Q99999](https://www.uniprot.org/uniprotkb/Q99999) · Ensembl [ENSG00000128242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128242) · OMIM [602300](https://www.omim.org/entry/602300)

**PubMed**, as HGNC records for this gene — [9847074](https://pubmed.ncbi.nlm.nih.gov/9847074/), [9030544](https://pubmed.ncbi.nlm.nih.gov/9030544/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06249 |
| As a percentage | +4.43% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06727 / 0.05958 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.365 raw, 0.365 with 3 PCs removed |

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
