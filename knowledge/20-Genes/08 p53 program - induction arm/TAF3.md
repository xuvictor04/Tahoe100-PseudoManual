---
symbol: TAF3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [TAF140, TAFII140]
gene_name: TATA-box binding protein associated factor 3
locus: 10p14
locus_type: gene with protein product
gene_family: [PHD finger proteins, Armadillo like helical domain containing, General transcription factor IID complex subunits]
family_siblings_here: [ARFGEF1, ARFGEF2, ARMH3, ATM, FANCD2, HTT, KDM4B, KDM4C, PPP4R3A, RALGAPB]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 101.76
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TAF3

*TATA-box binding protein associated factor 3* — 10p14

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TAF3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | TATA-box binding protein associated factor 3 |
| Also known as | TAF140, TAFII140 |
| Locus | 10p14 — gene with protein product |
| Gene families | PHD finger proteins; Armadillo like helical domain containing; General transcription factor IID complex subunits |
| Other genes here in those families | [[ARFGEF1]], [[ARFGEF2]], [[ARMH3]], [[ATM]], [[FANCD2]], [[HTT]], [[KDM4B]], [[KDM4C]], [[PPP4R3A]], [[RALGAPB]] |
| Previously named | TAF3 RNA polymerase II, TATA box binding protein (TBP)-associated factor, 140 kD; TAF3 RNA polymerase II, TATA box binding protein (TBP)-associated factor, 140kDa |

**Function**, from UniProt [Q5VWG9](https://www.uniprot.org/uniprotkb/Q5VWG9) (reviewed):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription (PubMed:33795473). TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC) (PubMed:33795473). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13 (PubMed:33795473). The TFIID complex structure can be divided into 3 modules TFIID-A, TFIID-B, and TFIID-C (PubMed:33795473). TAF3 forms the TFIID-A module together with TAF5 and TBP (PubMed:33795473). Required in complex with TBPL2 for the differentiation of myoblasts into myocytes (PubMed:11438666). The TAF3-TBPL2 complex replaces TFIID at specific promoters at an early stage in the differentiation process (PubMed:11438666)

**Summary**, from NCBI Gene [83860](https://www.ncbi.nlm.nih.gov/gene/83860):

> The highly conserved RNA polymerase II transcription factor TFIID (see TAF1; MIM 313650) comprises the TATA box-binding protein (TBP; MIM 600075) and a set of TBP-associated factors (TAFs), including TAF3. TAFs contribute to promoter recognition and selectivity and act as antiapoptotic factors (Gangloff et al., 2001 [PubMed 11438666]).[supplied by OMIM, May 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17303) · Entrez [83860](https://www.ncbi.nlm.nih.gov/gene/83860) · UniProt [Q5VWG9](https://www.uniprot.org/uniprotkb/Q5VWG9) · Ensembl [ENSG00000165632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165632) · OMIM [606576](https://www.omim.org/entry/606576)

**PubMed**, as HGNC records for this gene — [11438666](https://pubmed.ncbi.nlm.nih.gov/11438666/), [18549481](https://pubmed.ncbi.nlm.nih.gov/18549481/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 101.76 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 124 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.081× |
| Wild-type minus altered | 1.048× |
| Compounds moving it up in WT lines | 77 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00170 |
| As a percentage | -0.12% |
| FDR, exposure-shuffle null | 0.4853 |
| In TP53-wild-type lines / altered lines | -0.00236 / -0.00130 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.274 raw, -0.184 with 3 PCs removed |

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
