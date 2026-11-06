---
symbol: UBA6
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ10808]
gene_name: ubiquitin like modifier activating enzyme 6
locus: 4q13.2
locus_type: gene with protein product
gene_family: [Ubiquitin like modifier activating enzymes]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 318.24
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# UBA6

*ubiquitin like modifier activating enzyme 6* — 4q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/UBA6.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ubiquitin like modifier activating enzyme 6 |
| Also known as | FLJ10808, UBA6, ubiquitin-activating enzyme E1 |
| Locus | 4q13.2 — gene with protein product |
| Gene families | Ubiquitin like modifier activating enzymes |
| Previously named | ubiquitin-activating enzyme E1-like 2; ubiquitin-like modifier activating enzyme 6 |

**Function**, from UniProt [A0AVT1](https://www.uniprot.org/uniprotkb/A0AVT1) (reviewed):

> Activates ubiquitin by first adenylating its C-terminal glycine residue with ATP, and thereafter linking this residue to the side chain of a cysteine residue in E1, yielding a ubiquitin-E1 thioester and free AMP (PubMed:35970836, PubMed:35986001). Specific for ubiquitin, does not activate ubiquitin-like peptides. Also activates UBD/FAT10 conjugation via adenylation of its C-terminal glycine (PubMed:17889673, PubMed:35970836, PubMed:35986001). Differs from UBE1 in its specificity for substrate E2 charging. Does not charge cell cycle E2s, such as CDC34. Essential for embryonic development. Isoform 2 may play a key role in ubiquitin system and may influence spermatogenesis and male fertility

**Summary**, from NCBI Gene [55236](https://www.ncbi.nlm.nih.gov/gene/55236):

> Modification of proteins with ubiquitin (UBB; MIM 191339) or ubiquitin-like proteins controls many signaling networks and requires a ubiquitin-activating enzyme (E1), a ubiquitin conjugating enzyme (E2), and a ubiquitin protein ligase (E3). UBE1L2 is an E1 enzyme that initiates the activation and conjugation of ubiquitin-like proteins (Jin et al., 2007 [PubMed 17597759]).[supplied by OMIM, Mar 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25581) · Entrez [55236](https://www.ncbi.nlm.nih.gov/gene/55236) · UniProt [A0AVT1](https://www.uniprot.org/uniprotkb/A0AVT1) · Ensembl [ENSG00000033178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033178) · OMIM [611361](https://www.omim.org/entry/611361)

**PubMed**, as HGNC records for this gene — [17580310](https://pubmed.ncbi.nlm.nih.gov/17580310/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 318.24 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 161 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.031× |
| Wild-type minus altered | 1.017× |
| Compounds moving it up in WT lines | 61 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00122 |
| As a percentage | -0.08% |
| FDR, exposure-shuffle null | 0.6629 |
| In TP53-wild-type lines / altered lines | 0.00234 / -0.00339 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.142 raw, 0.069 with 3 PCs removed |

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
