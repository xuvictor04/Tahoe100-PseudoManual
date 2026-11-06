---
symbol: ISCU
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [ISU2, hnifU]
gene_name: iron-sulfur cluster assembly enzyme
locus: 12q23.3
locus_type: gene with protein product
gene_family: [Mitochondrial iron-sulfur assembly components]
family_siblings_here: [FDXR]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 24.48
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ISCU

*iron-sulfur cluster assembly enzyme* — 12q23.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ISCU.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | iron-sulfur cluster assembly enzyme |
| Also known as | ISU2, hnifU |
| Locus | 12q23.3 — gene with protein product |
| Gene families | Mitochondrial iron-sulfur assembly components |
| Other genes here in those families | [[FDXR]] |
| Previously named | NifU-like N-terminal domain containing; IscU iron-sulfur cluster scaffold homolog (E. coli); iron-sulfur cluster scaffold homolog (E. coli) |

**Function**, from UniProt [Q9H1K1](https://www.uniprot.org/uniprotkb/Q9H1K1) (reviewed):

> Mitochondrial scaffold protein, of the core iron-sulfur cluster (ISC) assembly complex, that provides the structural architecture on which the [2Fe-2S] clusters are assembled (PubMed:34824239). The core iron-sulfur cluster (ISC) assembly complex is involved in the de novo synthesis of a [2Fe-2S] cluster, the first step of the mitochondrial iron-sulfur protein biogenesis. This process is initiated by the cysteine desulfurase complex (NFS1:LYRM4:NDUFAB1) that produces persulfide which is delivered on the scaffold protein ISCU in a FXN-dependent manner. Then this complex is stabilized by FDX2 which provides reducing equivalents to accomplish the [2Fe-2S] cluster assembly. Finally, the [2Fe-2S] cluster is transferred from ISCU to chaperone proteins, including HSCB, HSPA9 and GLRX5 (Probable) (PubMed:24971490, PubMed:29576242, PubMed:30031876, PubMed:34824239). Exists as two slow interchanging conformational states, a structured (S) and disordered (D) form (PubMed:23940031). May modulate NFS1 desulfurase activity in a zinc-dependent manner (PubMed:30031876). Modulates the interaction between FXN and the cysteine desulfurase complex (PubMed:29576242)

**Summary**, from NCBI Gene [23479](https://www.ncbi.nlm.nih.gov/gene/23479):

> This gene encodes a component of the iron-sulfur (Fe-S) cluster scaffold. Fe-S clusters are cofactors that play a role in the function of a diverse set of enzymes, including those that regulate metabolism, iron homeostasis, and oxidative stress response. Alternative splicing results in transcript variants encoding different protein isoforms that localize either to the cytosol or to the mitochondrion. Mutations in this gene have been found in patients with hereditary myopathy with lactic acidosis. A disease-associated mutation in an intron may activate a cryptic splice site, resulting in the production of a splice variant encoding a putatively non-functional protein. A pseudogene of this gene is present on chromosome 1. [provided by RefSeq, Feb 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29882) · Entrez [23479](https://www.ncbi.nlm.nih.gov/gene/23479) · UniProt [Q9H1K1](https://www.uniprot.org/uniprotkb/Q9H1K1) · Ensembl [ENSG00000136003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136003) · OMIM [611911](https://www.omim.org/entry/611911)

**PubMed**, as HGNC records for this gene — [8875867](https://pubmed.ncbi.nlm.nih.gov/8875867/), [11060020](https://pubmed.ncbi.nlm.nih.gov/11060020/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 24.48 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 138 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.004× |
| Wild-type minus altered | 1.044× |
| Compounds moving it up in WT lines | 51 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00027 |
| As a percentage | -0.02% |
| FDR, exposure-shuffle null | 0.9253 |
| In TP53-wild-type lines / altered lines | -0.00092 / 0.00013 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.271 raw, -0.190 with 3 PCs removed |

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
