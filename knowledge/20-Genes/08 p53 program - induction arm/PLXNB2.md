---
symbol: PLXNB2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MM1, KIAA0315, PLEXB2, lncFAL]
gene_name: plexin B2
locus: 22q13.33
locus_type: gene with protein product
gene_family: [Plexins, IPT domain containing]
family_siblings_here: [RBPJ]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 55.33
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PLXNB2

*plexin B2* — 22q13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PLXNB2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | plexin B2 |
| Also known as | MM1, KIAA0315, PLEXB2, lncFAL, ferroptosis-associated lncRNA |
| Locus | 22q13.33 — gene with protein product |
| Gene families | Plexins; IPT domain containing |
| Other genes here in those families | [[RBPJ]] |

**Function**, from UniProt [O15031](https://www.uniprot.org/uniprotkb/O15031) (reviewed):

> Cell surface receptor for SEMA4C, SEMA4D and SEMA4G that plays an important role in cell-cell signaling (By similarity). Plays a role in glutamatergic synapse development and is required for SEMA4A-mediated excitatory synapse development (By similarity). Binding to class 4 semaphorins promotes downstream activation of RHOA and phosphorylation of ERBB2 at 'Tyr-1248' (By similarity). Also acts as a cell surface receptor for angiogenin (ANG); promoting ANG endocytosis and translocation to the cytoplasm or nucleus (PubMed:29100074, PubMed:32510170). Required for normal differentiation and migration of neuronal cells during brain corticogenesis and for normal embryonic brain development (By similarity). Regulates the migration of cerebellar granule cells in the developing brain (By similarity). Plays a role in RHOA activation and subsequent changes of the actin cytoskeleton (PubMed:12183458). Plays a role in axon guidance, invasive growth and cell migration (PubMed:15184888). May modulate the activity of RAC1 and CDC42 (By similarity)

**Summary**, from NCBI Gene [23654](https://www.ncbi.nlm.nih.gov/gene/23654):

> Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9104) · Entrez [23654](https://www.ncbi.nlm.nih.gov/gene/23654) · UniProt [O15031](https://www.uniprot.org/uniprotkb/O15031) · Ensembl [ENSG00000196576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196576) · OMIM [604293](https://www.omim.org/entry/604293)

**PubMed**, as HGNC records for this gene — [10520995](https://pubmed.ncbi.nlm.nih.gov/10520995/), [12183458](https://pubmed.ncbi.nlm.nih.gov/12183458/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 55.33 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 30 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.060× |
| Wild-type minus altered | 1.082× |
| Compounds moving it up in WT lines | 63 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00011 |
| As a percentage | -0.01% |
| FDR, exposure-shuffle null | 0.9741 |
| In TP53-wild-type lines / altered lines | -0.00134 / 0.00064 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.079 raw, 0.003 with 3 PCs removed |

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
