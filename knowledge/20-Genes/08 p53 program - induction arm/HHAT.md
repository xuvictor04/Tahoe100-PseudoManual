---
symbol: HHAT
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ10724, MART-2, MART2, Skn, ski, rasp]
gene_name: hedgehog acyltransferase
locus: 1q32.2
locus_type: gene with protein product
gene_family: [Membrane bound O-acyltransferase family]
family_siblings_here: [MBOAT1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 19.85
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# HHAT

*hedgehog acyltransferase* — 1q32.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HHAT.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | hedgehog acyltransferase |
| Also known as | FLJ10724, MART-2, MART2, Skn, ski, rasp, sit, GUP2, protein-cysteine N-palmitoyltransferase HHAT |
| Locus | 1q32.2 — gene with protein product |
| Gene families | Membrane bound O-acyltransferase family |
| Other genes here in those families | [[MBOAT1]] |

**Function**, from UniProt [Q5VTY9](https://www.uniprot.org/uniprotkb/Q5VTY9) (reviewed):

> Palmitoyl acyltransferase that catalyzes N-terminal palmitoylation of hedgehog (DHH, IHH or SHH) morphogens, promoting their maturation (PubMed:11486055, PubMed:18534984, PubMed:24784881, PubMed:31875564, PubMed:34112694, PubMed:34890564). Promotes the transfer of palmitoyl-CoA from the cytoplasmic to the luminal side of the endoplasmic reticulum membrane, where hedgehog palmitoylation occurs (PubMed:31875564, PubMed:34112694, PubMed:34890564). Required for hedgehog signaling during limb development (By similarity). Plays a role in proper testis cord formation and the differentiation of Leydig cells (PubMed:24784881)

**Summary**, from NCBI Gene [55733](https://www.ncbi.nlm.nih.gov/gene/55733):

> 'Skinny hedgehog' (SKI1) encodes an enzyme that acts within the secretory pathway to catalyze amino-terminal palmitoylation of 'hedgehog' (see MIM 600725).[supplied by OMIM, Jul 2002]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18270) · Entrez [55733](https://www.ncbi.nlm.nih.gov/gene/55733) · UniProt [Q5VTY9](https://www.uniprot.org/uniprotkb/Q5VTY9) · Ensembl [ENSG00000054392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054392) · OMIM [605743](https://www.omim.org/entry/605743)

**PubMed**, as HGNC records for this gene — [11160356](https://pubmed.ncbi.nlm.nih.gov/11160356/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 19.85 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 179 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.003× |
| Wild-type minus altered | 1.064× |
| Compounds moving it up in WT lines | 49 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00174 |
| As a percentage | -0.12% |
| FDR, exposure-shuffle null | 0.8140 |
| In TP53-wild-type lines / altered lines | -0.00783 / 0.00229 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.225 raw, 0.166 with 3 PCs removed |

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
