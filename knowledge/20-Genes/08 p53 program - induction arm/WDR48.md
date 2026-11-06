---
symbol: WDR48
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [UAF1, KIAA1449, P80, SPG60, Bun62]
gene_name: WD repeat domain 48
locus: 3p22.2
locus_type: gene with protein product
gene_family: [WD repeat domain containing]
family_siblings_here: [COP1, DDB2, DNAI3, FBXW7, RIC1, TLE4]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 73.81
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# WDR48

*WD repeat domain 48* — 3p22.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/WDR48.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | WD repeat domain 48 |
| Also known as | UAF1, KIAA1449, P80, SPG60, Bun62, USP1 associated factor 1 |
| Locus | 3p22.2 — gene with protein product |
| Gene families | WD repeat domain containing |
| Other genes here in those families | [[COP1]], [[DDB2]], [[DNAI3]], [[FBXW7]], [[RIC1]], [[TLE4]] |

**Function**, from UniProt [Q8TAF3](https://www.uniprot.org/uniprotkb/Q8TAF3) (reviewed):

> Regulator of deubiquitinating complexes, which acts as a strong activator of USP1, USP12 and USP46 (PubMed:18082604, PubMed:19075014, PubMed:26388029, PubMed:31253762). Enhances the USP1-mediated deubiquitination of FANCD2; USP1 being almost inactive by itself (PubMed:18082604, PubMed:31253762). Activates deubiquitination by increasing the catalytic turnover without increasing the affinity of deubiquitinating enzymes for the substrate (PubMed:19075014, PubMed:27373336). Also activates deubiquitinating activity of complexes containing USP12 (PubMed:19075014, PubMed:27373336, PubMed:27650958). In complex with USP12, acts as a potential tumor suppressor by positively regulating PHLPP1 stability (PubMed:24145035). Docks at the distal end of the USP12 fingers domain and induces a cascade of structural changes leading to the activation of the enzyme (PubMed:27373336, PubMed:27650958). Together with RAD51AP1, promotes DNA repair by stimulating RAD51-mediated homologous recombination (PubMed:27239033, PubMed:27463890, PubMed:32350107). Binds single-stranded DNA (ssDNA) and double-stranded DNA (dsDNA) (PubMed:27239033, PubMed:31253762, PubMed:32350107). DNA-binding is required both for USP1-mediated deubiquitination of FANCD2 and stimulation of RAD51-mediated homologous recombination: both WDR48/UAF1 and RAD51AP1 have coordinated role in DNA-binding during these processes (PubMed:31253762, PubMed:32350107). Together with ATAD5 and by regulating USP1 activity, has a role in PCNA-mediated translesion synthesis (TLS) by deubiquitinating monoubiquitinated PCNA (PubMed:20147293). Together with ATAD5, has a role in recruiting RAD51 to stalled forks during replication stress (PubMed:31844045)

**Summary**, from NCBI Gene [57599](https://www.ncbi.nlm.nih.gov/gene/57599):

> The protein encoded by this gene has been shown to interact with ubiquitin specific peptidase 1 (USP1), activating the deubiquitinating activity of USP1 and allowing it to remove the ubiquitin moiety from monoubiquitinated FANCD2. FANCD2 is ubiquitinated in response to DNA damage. [provided by RefSeq, Sep 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30914) · Entrez [57599](https://www.ncbi.nlm.nih.gov/gene/57599) · UniProt [Q8TAF3](https://www.uniprot.org/uniprotkb/Q8TAF3) · Ensembl [ENSG00000114742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114742) · OMIM [612167](https://www.omim.org/entry/612167)

**PubMed**, as HGNC records for this gene — [12196293](https://pubmed.ncbi.nlm.nih.gov/12196293/), [32587090](https://pubmed.ncbi.nlm.nih.gov/32587090/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 73.81 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 135 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.041× |
| Wild-type minus altered | 1.019× |
| Compounds moving it up in WT lines | 62 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00469 |
| As a percentage | -0.32% |
| FDR, exposure-shuffle null | 0.0240 |
| In TP53-wild-type lines / altered lines | -0.00396 / -0.00513 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.088 raw, -0.117 with 3 PCs removed |

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
