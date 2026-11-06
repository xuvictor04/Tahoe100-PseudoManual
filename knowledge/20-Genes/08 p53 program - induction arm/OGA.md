---
symbol: OGA
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MEA5, NCOAT]
gene_name: O-GlcNAcase
locus: 10q24.32
locus_type: gene with protein product
gene_family: [Hexosaminidases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 488.86
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# OGA

*O-GlcNAcase* — 10q24.32

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/OGA.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | O-GlcNAcase |
| Also known as | MEA5, NCOAT, nuclear cytoplasmic O-GlcNAcase and acetyltransferase |
| Locus | 10q24.32 — gene with protein product |
| Gene families | Hexosaminidases |
| Previously named | meningioma expressed antigen 5 (hyaluronidase) |

**Function**, from UniProt [O60502](https://www.uniprot.org/uniprotkb/O60502) (reviewed):

> Cleaves GlcNAc but not GalNAc from O-glycosylated proteins (PubMed:11148210, PubMed:11788610, PubMed:20673219, PubMed:22365600, PubMed:24088714, PubMed:28939839, PubMed:37962578). Deglycosylates a large and diverse number of proteins, such as CRYAB, ELK1, GSDMD, LMNB1 and TAB1 (PubMed:28939839, PubMed:37962578). Can use p-nitrophenyl-beta-GlcNAc and 4-methylumbelliferone-GlcNAc as substrates but not p-nitrophenyl-beta-GalNAc or p-nitrophenyl-alpha-GlcNAc (in vitro) (PubMed:20673219). Does not bind acetyl-CoA and does not have histone acetyltransferase activity (PubMed:24088714)

**Summary**, from NCBI Gene [10724](https://www.ncbi.nlm.nih.gov/gene/10724):

> The dynamic modification of cytoplasmic and nuclear proteins by O-linked N-acetylglucosamine (O-GlcNAc) addition and removal on serine and threonine residues is catalyzed by OGT (MIM 300255), which adds O-GlcNAc, and MGEA5, a glycosidase that removes O-GlcNAc modifications (Gao et al., 2001 [PubMed 11148210]).[supplied by OMIM, Mar 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7056) · Entrez [10724](https://www.ncbi.nlm.nih.gov/gene/10724) · UniProt [O60502](https://www.uniprot.org/uniprotkb/O60502) · Ensembl [ENSG00000198408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198408) · OMIM [604039](https://www.omim.org/entry/604039)

**PubMed**, as HGNC records for this gene — [9811929](https://pubmed.ncbi.nlm.nih.gov/9811929/), [16356930](https://pubmed.ncbi.nlm.nih.gov/16356930/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 488.86 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 139 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.073× |
| Wild-type minus altered | 1.026× |
| Compounds moving it up in WT lines | 71 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00534 |
| As a percentage | -0.37% |
| FDR, exposure-shuffle null | 0.0027 |
| In TP53-wild-type lines / altered lines | -0.00297 / -0.00678 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.030 raw, -0.096 with 3 PCs removed |

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
