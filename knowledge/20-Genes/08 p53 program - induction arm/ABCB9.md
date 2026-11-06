---
symbol: ABCB9
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [EST122234]
gene_name: ATP binding cassette subfamily B member 9
locus: 12q24.31
locus_type: gene with protein product
gene_family: [ATP binding cassette subfamily B]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 23.89
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ABCB9

*ATP binding cassette subfamily B member 9* — 12q24.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ABCB9.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ATP binding cassette subfamily B member 9 |
| Also known as | EST122234 |
| Locus | 12q24.31 — gene with protein product |
| Gene families | ATP binding cassette subfamily B |
| Previously named | ATP-binding cassette, sub-family B (MDR/TAP), member 9 |

**Function**, from UniProt [Q9NP78](https://www.uniprot.org/uniprotkb/Q9NP78) (reviewed):

> ATP-dependent low-affinity peptide transporter which translocates a broad spectrum of peptides from the cytosol to the lysosomal lumen for degradation (PubMed:15863492, PubMed:17977821, PubMed:18434309, PubMed:22641697, PubMed:25646430, PubMed:30353140, PubMed:30877195, PubMed:31417173). Displays a broad peptide length specificity from 6-mer up to at least 59-mer peptides with an optimum of 23-mers (PubMed:15863492, PubMed:25646430). Binds and transports smaller and larger peptides with the same affinity (PubMed:31417173). Favors positively charged, aromatic or hydrophobic residues in the N- and C-terminal positions whereas negatively charged residues as well as asparagine and methionine are not favored (PubMed:15863492, PubMed:17977821, PubMed:18434309)

**Summary**, from NCBI Gene [23457](https://www.ncbi.nlm.nih.gov/gene/23457):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance as well as antigen presentation. This family member functions in the translocation of peptides from the cytosol into the lysosomal lumen. Alternative splicing of this gene results in distinct isoforms which are likely to have different substrate specificities. [provided by RefSeq, Jul 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:50](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50) · Entrez [23457](https://www.ncbi.nlm.nih.gov/gene/23457) · UniProt [Q9NP78](https://www.uniprot.org/uniprotkb/Q9NP78) · Ensembl [ENSG00000150967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150967) · OMIM [605453](https://www.omim.org/entry/605453)

**PubMed**, as HGNC records for this gene — [8894702](https://pubmed.ncbi.nlm.nih.gov/8894702/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 23.89 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 166 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.011× |
| Wild-type minus altered | 1.047× |
| Compounds moving it up in WT lines | 60 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00718 |
| As a percentage | +0.50% |
| FDR, exposure-shuffle null | 0.0154 |
| In TP53-wild-type lines / altered lines | 0.01058 / 0.00502 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.021 raw, -0.051 with 3 PCs removed |

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
