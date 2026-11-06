---
symbol: FBXO42
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA1332, Fbx42]
gene_name: F-box protein 42
locus: 1p36.13
locus_type: gene with protein product
gene_family: [F-boxes other]
family_siblings_here: [FBXO22]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 122.75
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FBXO42

*F-box protein 42* — 1p36.13

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FBXO42.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | F-box protein 42 |
| Also known as | KIAA1332, Fbx42 |
| Locus | 1p36.13 — gene with protein product |
| Gene families | F-boxes other |
| Other genes here in those families | [[FBXO22]] |

**Function**, from UniProt [Q6P3S6](https://www.uniprot.org/uniprotkb/Q6P3S6) (reviewed):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Required for bipolar spindle formation during mitosis (PubMed:33539788). Recognizes p53/TP53 phosphorylated by CSN-associated kinase, promoting its polyubiquitination and proteasomal degradation (PubMed:19509332, PubMed:21127074, PubMed:39134694). Positively regulates the Notch signaling pathway through 'Lys-63'-linked polyubiquitination of the transcriptional effector RBPJ, stabilizing its chromatin association and potentiating transcriptional activation of Notch target genes (PubMed:36129980). Mediates 'Lys-48'-linked polyubiquitination and proteasomal degradation of components of the PP4 phosphatase complex, including PP4C, PP4R2, PP4R3A and PP4R3B, thereby restraining PP4 phosphatase activity and ensuring proper DNA damage response signaling (PubMed:41484364). Collaborates with CCDC6 to promote polyubiquitination and proteasomal degradation of the catalytic subunit PP2AC (PubMed:41986709). Recognizes ACAA2, promoting its ubiquitination and proteasomal degradation in hepatocytes, thereby attenuating fatty acid beta-oxidation; this activity is negatively regulated by CAND1, which prevents assembly of the SCF(FBXO42)-ACAA2 degradation complex (By similarity)

**Summary**, from NCBI Gene [54455](https://www.ncbi.nlm.nih.gov/gene/54455):

> Members of the F-box protein family, such as FBXO42, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (SKP1A; MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Dec 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29249) · Entrez [54455](https://www.ncbi.nlm.nih.gov/gene/54455) · UniProt [Q6P3S6](https://www.uniprot.org/uniprotkb/Q6P3S6) · Ensembl [ENSG00000037637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037637) · OMIM [609109](https://www.omim.org/entry/609109)

**PubMed**, as HGNC records for this gene — [10718198](https://pubmed.ncbi.nlm.nih.gov/10718198/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 122.75 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 164 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.080× |
| Wild-type minus altered | 1.025× |
| Compounds moving it up in WT lines | 76 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00434 |
| As a percentage | -0.30% |
| FDR, exposure-shuffle null | 0.1075 |
| In TP53-wild-type lines / altered lines | -0.00236 / -0.00555 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.237 raw, -0.095 with 3 PCs removed |

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
