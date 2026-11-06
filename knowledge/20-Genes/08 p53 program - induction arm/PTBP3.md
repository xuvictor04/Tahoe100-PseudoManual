---
symbol: PTBP3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DKFZp781I1117]
gene_name: polypyrimidine tract binding protein 3
locus: 9q32
locus_type: gene with protein product
gene_family: [RNA binding motif containing]
family_siblings_here: [FUS]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 261.56
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PTBP3

*polypyrimidine tract binding protein 3* — 9q32

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PTBP3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | polypyrimidine tract binding protein 3 |
| Also known as | DKFZp781I1117 |
| Locus | 9q32 — gene with protein product |
| Gene families | RNA binding motif containing |
| Other genes here in those families | [[FUS]] |
| Previously named | regulator of differentiation (in S. pombe) 1; ROD1 regulator of differentiation 1 (S. pombe) |

**Function**, from UniProt [O95758](https://www.uniprot.org/uniprotkb/O95758) (reviewed):

> RNA-binding protein that mediates pre-mRNA alternative splicing regulation. Plays a role in the regulation of cell proliferation, differentiation and migration. Positive regulator of EPO-dependent erythropoiesis. Participates in cell differentiation regulation by repressing tissue-specific exons. Promotes FAS exon 6 skipping. Binds RNA, preferentially to both poly(G) and poly(U)

**Summary**, from NCBI Gene [9991](https://www.ncbi.nlm.nih.gov/gene/9991):

> The protein encoded by this gene binds RNA and is a regulator of cell differentiation. The encoded protein preferentially binds to poly(G) and poly(U) sequences in vitro. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:10253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10253) · Entrez [9991](https://www.ncbi.nlm.nih.gov/gene/9991) · UniProt [O95758](https://www.uniprot.org/uniprotkb/O95758) · Ensembl [ENSG00000119314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119314) · OMIM [607527](https://www.omim.org/entry/607527)

**PubMed**, as HGNC records for this gene — [10207106](https://pubmed.ncbi.nlm.nih.gov/10207106/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 261.56 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 154 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.017× |
| Wild-type minus altered | 1.030× |
| Compounds moving it up in WT lines | 57 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00042 |
| As a percentage | +0.03% |
| FDR, exposure-shuffle null | 0.8978 |
| In TP53-wild-type lines / altered lines | 0.00283 / -0.00104 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.303 raw, -0.115 with 3 PCs removed |

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
