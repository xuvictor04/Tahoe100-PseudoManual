---
symbol: SHOC2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0862, SOC2, SUR-8, SOC-2, SUR8]
gene_name: SHOC2 leucine rich repeat scaffold protein
locus: 10q25.2
locus_type: gene with protein product
gene_family: [MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 144.24
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SHOC2

*SHOC2 leucine rich repeat scaffold protein* — 10q25.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SHOC2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | SHOC2 leucine rich repeat scaffold protein |
| Also known as | KIAA0862, SOC2, SUR-8, SOC-2, SUR8 |
| Locus | 10q25.2 — gene with protein product |
| Gene families | MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]] |
| Previously named | soc-2 (suppressor of clear, C.elegans) homolog; soc-2 suppressor of clear homolog (C. elegans); SHOC2 leucine-rich repeat scaffold protein; SHOC2, leucine rich repeat scaffold protein |

**Function**, from UniProt [Q9UQ13](https://www.uniprot.org/uniprotkb/Q9UQ13) (reviewed):

> Core component of the SHOC2-MRAS-PP1c (SMP) holophosphatase complex that regulates activation of the MAPK pathway (PubMed:10783161, PubMed:16630891, PubMed:25137548, PubMed:35768504, PubMed:35830882, PubMed:35831509, PubMed:36175670). Acts as a scaffolding protein in the SMP complex (PubMed:35768504, PubMed:35830882, PubMed:35831509, PubMed:36175670). The SMP complex specifically dephosphorylates the inhibitory phosphorylation at 'Ser-259' of RAF1 kinase, 'Ser-365' of BRAF kinase and 'Ser-214' of ARAF kinase, stimulating their kinase activities (PubMed:10783161, PubMed:16630891, PubMed:35768504, PubMed:35830882, PubMed:35831509, PubMed:36175670). The SMP complex enhances the dephosphorylation activity and substrate specificity of PP1c (PubMed:35768504, PubMed:36175670). Acts as an inhibitor of keratinocyte differentiation via interaction with RAS protein complexes that promote ERK activation (PubMed:23524970)

**Summary**, from NCBI Gene [8036](https://www.ncbi.nlm.nih.gov/gene/8036):

> This gene encodes a protein that consists almost entirely of leucine-rich repeats, a domain implicated in protein-protein interactions. The protein may function as a scaffold linking RAS to downstream signal transducers in the RAS/ERK MAP kinase signaling cascade. Mutations in this gene have been associated with Noonan-like syndrome with loose anagen hair. [provided by RefSeq, May 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:15454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15454) · Entrez [8036](https://www.ncbi.nlm.nih.gov/gene/8036) · UniProt [Q9UQ13](https://www.uniprot.org/uniprotkb/Q9UQ13) · Ensembl [ENSG00000108061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108061) · OMIM [602775](https://www.omim.org/entry/602775)

**PubMed**, as HGNC records for this gene — [9618511](https://pubmed.ncbi.nlm.nih.gov/9618511/), [9674433](https://pubmed.ncbi.nlm.nih.gov/9674433/), [10783161](https://pubmed.ncbi.nlm.nih.gov/10783161/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 144.24 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 150 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.030× |
| Wild-type minus altered | 1.021× |
| Compounds moving it up in WT lines | 65 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00339 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.1714 |
| In TP53-wild-type lines / altered lines | 0.00587 / 0.00189 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.139 raw, 0.165 with 3 PCs removed |

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
