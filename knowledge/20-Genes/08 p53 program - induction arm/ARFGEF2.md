---
symbol: ARFGEF2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [BIG2]
gene_name: ARF guanine nucleotide exchange factor 2
locus: 20q13.13
locus_type: gene with protein product
gene_family: [A-kinase anchoring proteins, Armadillo like helical domain containing, ArfGEF family]
family_siblings_here: [ARFGEF1, ARMH3, ATM, FANCD2, HTT, PPP4R3A, RALGAPB, TAF3]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 247.44
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ARFGEF2

*ARF guanine nucleotide exchange factor 2* — 20q13.13

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ARFGEF2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ARF guanine nucleotide exchange factor 2 |
| Also known as | BIG2, Brefeldin A-inhibited guanine nucleotide-exchange protein 2 |
| Locus | 20q13.13 — gene with protein product |
| Gene families | A-kinase anchoring proteins; Armadillo like helical domain containing; ArfGEF family |
| Other genes here in those families | [[ARFGEF1]], [[ARMH3]], [[ATM]], [[FANCD2]], [[HTT]], [[PPP4R3A]], [[RALGAPB]], [[TAF3]] |
| Previously named | ADP ribosylation factor guanine nucleotide exchange factor 2; ADP-ribosylation factor guanine nucleotide-exchange factor 2 (brefeldin A-inhibited) |

**Function**, from UniProt [Q9Y6D5](https://www.uniprot.org/uniprotkb/Q9Y6D5) (reviewed):

> Promotes guanine-nucleotide exchange on ARF1 and ARF3 and to a lower extent on ARF5 and ARF6. Promotes the activation of ARF1/ARF5/ARF6 through replacement of GDP with GTP. Involved in the regulation of Golgi vesicular transport. Required for the integrity of the endosomal compartment. Involved in trafficking from the trans-Golgi network (TGN) to endosomes and is required for membrane association of the AP-1 complex and GGA1. Seems to be involved in recycling of the transferrin receptor from recycling endosomes to the plasma membrane. Probably is involved in the exit of GABA(A) receptors from the endoplasmic reticulum. Involved in constitutive release of tumor necrosis factor receptor 1 via exosome-like vesicles; the function seems to involve PKA and specifically PRKAR2B. Proposed to act as A kinase-anchoring protein (AKAP) and may mediate crosstalk between Arf and PKA pathways

**Summary**, from NCBI Gene [10564](https://www.ncbi.nlm.nih.gov/gene/10564):

> ADP-ribosylation factors (ARFs) play an important role in intracellular vesicular trafficking. The protein encoded by this gene is involved in the activation of ARFs by accelerating replacement of bound GDP with GTP and is involved in Golgi transport. It contains a Sec7 domain, which may be responsible for its guanine-nucleotide exchange activity and also brefeldin A inhibition. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:15853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15853) · Entrez [10564](https://www.ncbi.nlm.nih.gov/gene/10564) · UniProt [Q9Y6D5](https://www.uniprot.org/uniprotkb/Q9Y6D5) · Ensembl [ENSG00000124198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124198) · OMIM [605371](https://www.omim.org/entry/605371)

**PubMed**, as HGNC records for this gene — [10212200](https://pubmed.ncbi.nlm.nih.gov/10212200/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 247.44 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 176 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.053× |
| Wild-type minus altered | 1.024× |
| Compounds moving it up in WT lines | 83 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00400 |
| As a percentage | -0.28% |
| FDR, exposure-shuffle null | 0.0301 |
| In TP53-wild-type lines / altered lines | -0.00188 / -0.00529 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.013 raw, 0.027 with 3 PCs removed |

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
