---
symbol: SMG6
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0732, SMG-6, EST1A]
gene_name: SMG6 nonsense mediated mRNA decay factor
locus: 17p13.3
locus_type: gene with protein product
gene_family: [Endoribonucleases, PIN-like domain superfamily]
family_siblings_here: [APEX1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 173.28
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SMG6

*SMG6 nonsense mediated mRNA decay factor* — 17p13.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SMG6.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | SMG6 nonsense mediated mRNA decay factor |
| Also known as | KIAA0732, SMG-6, EST1A, EST1 telomerase component homolog A (S. cerevisiae) |
| Locus | 17p13.3 — gene with protein product |
| Gene families | Endoribonucleases; PIN-like domain superfamily |
| Other genes here in those families | [[APEX1]] |
| Previously named | chromosome 17 open reading frame 31; smg-6 homolog, nonsense mediated mRNA decay factor (C. elegans); SMG6 nonsense mediated mRNA decay factor; SMG6, nonsense mediated mRNA decay factor |

**Function**, from UniProt [Q86US8](https://www.uniprot.org/uniprotkb/Q86US8) (reviewed):

> Component of the telomerase ribonucleoprotein (RNP) complex that is essential for the replication of chromosome termini (PubMed:19179534). May have a general role in telomere regulation (PubMed:12676087, PubMed:12699629). Promotes in vitro the ability of TERT to elongate telomeres (PubMed:12676087, PubMed:12699629). Overexpression induces telomere uncapping, chromosomal end-to-end fusions (telomeric DNA persists at the fusion points) and did not perturb TRF2 telomeric localization (PubMed:12676087, PubMed:12699629). Binds to the single-stranded 5'-(GTGTGG)(4)GTGT-3' telomeric DNA, but not to a telomerase RNA template component (TER) (PubMed:12676087, PubMed:12699629)

**Summary**, from NCBI Gene [23293](https://www.ncbi.nlm.nih.gov/gene/23293):

> This gene encodes a component of the telomerase ribonucleoprotein complex responsible for the replication and maintenance of chromosome ends. The encoded protein also plays a role in the nonsense-mediated mRNA decay (NMD) pathway, providing the endonuclease activity near the premature translation termination codon that is needed to initiate NMD. Alternatively spliced transcript variants encoding distinct protein isoforms have been described. [provided by RefSeq, Feb 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17809) · Entrez [23293](https://www.ncbi.nlm.nih.gov/gene/23293) · UniProt [Q86US8](https://www.uniprot.org/uniprotkb/Q86US8) · Ensembl [ENSG00000070366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070366) · OMIM [610963](https://www.omim.org/entry/610963)

**PubMed**, as HGNC records for this gene — [12676087](https://pubmed.ncbi.nlm.nih.gov/12676087/), [12699629](https://pubmed.ncbi.nlm.nih.gov/12699629/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 173.28 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 136 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.016× |
| Wild-type minus altered | 1.025× |
| Compounds moving it up in WT lines | 61 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00134 |
| As a percentage | +0.09% |
| FDR, exposure-shuffle null | 0.5266 |
| In TP53-wild-type lines / altered lines | 0.00286 / 0.00041 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.315 raw, -0.026 with 3 PCs removed |

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
