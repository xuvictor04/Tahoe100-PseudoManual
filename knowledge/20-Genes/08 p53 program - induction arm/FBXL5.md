---
symbol: FBXL5
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FBL4, FBL5, FLR1]
gene_name: F-box and leucine rich repeat protein 5
locus: 4p15.32
locus_type: gene with protein product
gene_family: [F-box and leucine rich repeat proteins]
family_siblings_here: [FBXL20]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 81.27
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FBXL5

*F-box and leucine rich repeat protein 5* — 4p15.32

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FBXL5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | F-box and leucine rich repeat protein 5 |
| Also known as | FBL4, FBL5, FLR1 |
| Locus | 4p15.32 — gene with protein product |
| Gene families | F-box and leucine rich repeat proteins |
| Other genes here in those families | [[FBXL20]] |
| Previously named | CC2D2A antisense RNA 1 |

**Function**, from UniProt [Q9UKA1](https://www.uniprot.org/uniprotkb/Q9UKA1) (reviewed):

> Component of some SCF (SKP1-cullin-F-box) protein ligase complex that plays a central role in iron homeostasis by promoting the ubiquitination and subsequent degradation of IREB2/IRP2 (PubMed:19762596, PubMed:19762597). The C-terminal domain of FBXL5 contains a redox-sensitive [2Fe-2S] cluster that, upon oxidation, promotes binding to IRP2 to effect its oxygen-dependent degradation (PubMed:32126207). Under iron deficiency conditions, the N-terminal hemerythrin-like (Hr) region, which contains a diiron metal center, cannot bind iron and undergoes conformational changes that destabilize the FBXL5 protein and cause its ubiquitination and degradation (PubMed:19762596, PubMed:19762597). When intracellular iron levels start rising, the Hr region is stabilized (PubMed:19762596, PubMed:19762597). Additional increases in iron levels facilitate the assembly and incorporation of a redox active [2Fe-2S] cluster in the C-terminal domain (PubMed:32126207). Only when oxygen level is high enough to maintain the cluster in its oxidized state can FBXL5 recruit IRP2 as a substrate for polyubiquitination and degradation (PubMed:32126207). Promotes ubiquitination and subsequent degradation of the dynactin complex component DCTN1 (PubMed:17532294). Within the nucleus, promotes the ubiquitination of SNAI1; preventing its interaction with DNA and promoting its degradation (PubMed:24157836). Negatively regulates DNA damage response by mediating the ubiquitin-proteasome degradation of the DNA repair protein NABP2 (PubMed:25249620)

**Summary**, from NCBI Gene [26234](https://www.ncbi.nlm.nih.gov/gene/26234):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction modules or no recognizable motifs. The protein encoded by this gene belongs to the Fbls class and, in addition to an F-box, contains several tandem leucine-rich repeats. Alternatively spliced transcript variants have been described for this locus. [provided by RefSeq, Aug 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13602) · Entrez [26234](https://www.ncbi.nlm.nih.gov/gene/26234) · UniProt [Q9UKA1](https://www.uniprot.org/uniprotkb/Q9UKA1) · Ensembl [ENSG00000118564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118564) · OMIM [605655](https://www.omim.org/entry/605655)

**PubMed**, as HGNC records for this gene — [10531035](https://pubmed.ncbi.nlm.nih.gov/10531035/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 81.27 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 42 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.056× |
| Wild-type minus altered | 1.048× |
| Compounds moving it up in WT lines | 75 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00828 |
| As a percentage | -0.57% |
| FDR, exposure-shuffle null | 0.0002 |
| In TP53-wild-type lines / altered lines | -0.00709 / -0.00899 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.452 raw, -0.306 with 3 PCs removed |

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
