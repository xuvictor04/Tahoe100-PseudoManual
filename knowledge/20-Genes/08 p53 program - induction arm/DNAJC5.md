---
symbol: DNAJC5
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ00118, FLJ13070, DNAJC5A]
gene_name: DnaJ heat shock protein family (Hsp40) member C5
locus: 20q13.33
locus_type: gene with protein product
gene_family: [DNAJ (HSP40) heat shock proteins, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L, PER1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 101.87
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DNAJC5

*DnaJ heat shock protein family (Hsp40) member C5* — 20q13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DNAJC5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | DnaJ heat shock protein family (Hsp40) member C5 |
| Also known as | FLJ00118, FLJ13070, DNAJC5A |
| Locus | 20q13.33 — gene with protein product |
| Gene families | DNAJ (HSP40) heat shock proteins; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]], [[PRKD2]] |
| Previously named | ceroid-lipofuscinosis, neuronal 4 (Kufs disease); DnaJ (Hsp40) homolog, subfamily C, member 5 |

**Function**, from UniProt [Q9H3Z4](https://www.uniprot.org/uniprotkb/Q9H3Z4) (reviewed):

> Acts as a general chaperone in regulated exocytosis (By similarity). Acts as a co-chaperone for the SNARE protein SNAP-25 (By similarity). Involved in the calcium-mediated control of a late stage of exocytosis (By similarity). May have an important role in presynaptic function. May be involved in calcium-dependent neurotransmitter release at nerve endings (By similarity)

**Summary**, from NCBI Gene [80331](https://www.ncbi.nlm.nih.gov/gene/80331):

> This gene is a member of the J protein family. J proteins function in many cellular processes by regulating the ATPase activity of 70 kDa heat shock proteins. The encoded protein plays a role in membrane trafficking and protein folding, and has been shown to have anti-neurodegenerative properties. The encoded protein is known to play a role in cystic fibrosis and Huntington's disease. A pseudogene of this gene is located on the short arm of chromosome 8. [provided by RefSeq, Nov 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16235) · Entrez [80331](https://www.ncbi.nlm.nih.gov/gene/80331) · UniProt [Q9H3Z4](https://www.uniprot.org/uniprotkb/Q9H3Z4) · Ensembl [ENSG00000101152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101152) · OMIM [611203](https://www.omim.org/entry/611203)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 101.87 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 111 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.035× |
| Wild-type minus altered | 1.023× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00343 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.1742 |
| In TP53-wild-type lines / altered lines | 0.00852 / 0.00034 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.166 raw, 0.094 with 3 PCs removed |

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
