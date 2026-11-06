---
symbol: ARFGEF1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DKFZP434L057, BIG1, ARFGEP1, p200]
gene_name: ARF guanine nucleotide exchange factor 1
locus: 8q13.2
locus_type: gene with protein product
gene_family: [Armadillo like helical domain containing, ArfGEF family]
family_siblings_here: [ARFGEF2, ARMH3, ATM, FANCD2, HTT, PPP4R3A, RALGAPB, TAF3]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 240.17
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ARFGEF1

*ARF guanine nucleotide exchange factor 1* — 8q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ARFGEF1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ARF guanine nucleotide exchange factor 1 |
| Also known as | DKFZP434L057, BIG1, ARFGEP1, p200, Brefeldin A-inhibited guanine nucleotide-exchange protein 1 |
| Locus | 8q13.2 — gene with protein product |
| Gene families | Armadillo like helical domain containing; ArfGEF family |
| Other genes here in those families | [[ARFGEF2]], [[ARMH3]], [[ATM]], [[FANCD2]], [[HTT]], [[PPP4R3A]], [[RALGAPB]], [[TAF3]] |
| Previously named | ADP ribosylation factor guanine nucleotide exchange factor 1; ADP-ribosylation factor guanine nucleotide-exchange factor 1 (brefeldin A-inhibited) |

**Function**, from UniProt [Q9Y6D6](https://www.uniprot.org/uniprotkb/Q9Y6D6) (reviewed):

> Promotes guanine-nucleotide exchange on ARF1 and ARF3. Promotes the activation of ARF1/ARF3 through replacement of GDP with GTP. Involved in vesicular trafficking. Required for the maintenance of Golgi structure; the function may be independent of its GEF activity. Required for the maturation of integrin beta-1 in the Golgi. Involved in the establishment and persistence of cell polarity during directed cell movement in wound healing. Proposed to act as A kinase-anchoring protein (AKAP) and may mediate crosstalk between Arf and PKA pathways. Inhibits GAP activity of MYO9B probably through competitive RhoA binding. The function in the nucleus remains to be determined

**Summary**, from NCBI Gene [10565](https://www.ncbi.nlm.nih.gov/gene/10565):

> ADP-ribosylation factors (ARFs) play an important role in intracellular vesicular trafficking. The protein encoded by this gene is involved in the activation of ARFs by accelerating replacement of bound GDP with GTP. It contains a Sec7 domain, which may be responsible for guanine-nucleotide exchange activity and also brefeldin A inhibition. [provided by RefSeq, Aug 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:15772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15772) · Entrez [10565](https://www.ncbi.nlm.nih.gov/gene/10565) · UniProt [Q9Y6D6](https://www.uniprot.org/uniprotkb/Q9Y6D6) · Ensembl [ENSG00000066777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066777) · OMIM [604141](https://www.omim.org/entry/604141)

**PubMed**, as HGNC records for this gene — [10212200](https://pubmed.ncbi.nlm.nih.gov/10212200/), [8917509](https://pubmed.ncbi.nlm.nih.gov/8917509/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 240.17 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 90 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.022× |
| Wild-type minus altered | 1.023× |
| Compounds moving it up in WT lines | 65 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00113 |
| As a percentage | -0.08% |
| FDR, exposure-shuffle null | 0.5551 |
| In TP53-wild-type lines / altered lines | 0.00110 / -0.00249 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.424 raw, 0.145 with 3 PCs removed |

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
