---
symbol: TNKS
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [TIN1, TINF1, TNKS1, PARP-5a, PARP5A, pART5]
gene_name: tankyrase
locus: 8p23.1
locus_type: gene with protein product
gene_family: [Ankyrin repeat domain containing, Poly(ADP-ribose) polymerases, Sterile alpha motif domain containing, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ANKRA2, ATF5, BBC3, DNAJC5, DNMT3A, EPHA2, EZH1, FBXW7, GDF15, MGRN1, NADSYN1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 250.19
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TNKS

*tankyrase* — 8p23.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TNKS.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | tankyrase |
| Also known as | TIN1, TINF1, TNKS1, PARP-5a, PARP5A, pART5, ARTD5, TRF1-interacting ankyrin-related ADP-ribose polymerase 1 |
| Locus | 8p23.1 — gene with protein product |
| Gene families | Ankyrin repeat domain containing; Poly(ADP-ribose) polymerases; Sterile alpha motif domain containing; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ANKRA2]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EPHA2]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]] |
| Previously named | tankyrase, TRF1-interacting ankyrin-related ADP-ribose polymerase |

**Function**, from UniProt [O95271](https://www.uniprot.org/uniprotkb/O95271) (reviewed):

> Poly-ADP-ribosyltransferase involved in various processes such as Wnt signaling pathway, necroptosis, telomere length and vesicle trafficking (PubMed:9822378, PubMed:10988299, PubMed:11739745, PubMed:16076287, PubMed:19759537, PubMed:21478859, PubMed:22864114, PubMed:23622245, PubMed:25043379, PubMed:28619731). Acts as an activator of the Wnt signaling pathway by mediating poly-ADP-ribosylation (PARsylation) of AXIN1 and AXIN2, 2 key components of the beta-catenin destruction complex: poly-ADP-ribosylated target proteins are recognized by RNF146, which mediates their ubiquitination and subsequent degradation (PubMed:19759537, PubMed:21478859). Acts as an inhibitor of necroptosis by mediating PARsylation of RIPK1: following induction of necroptosis, undergoes liquid-liquid phase separation (LLPS) together with RNF146, and specifically poly-ADP-ribosylates the kinase-activated form of RIPK1, triggering RIPK1 ubiquitination by RNF146 and degradation (By similarity). Also mediates PARsylation of BLZF1 and CASC3, followed by recruitment of RNF146 and subsequent ubiquitination (PubMed:21478859). Mediates PARsylation of TERF1, thereby contributing to the regulation of telomere length (PubMed:12080061, PubMed:11739745). Involved in centrosome maturation during prometaphase by mediating PARsylation of HEPACAM2/MIKI (PubMed:22864114). May also regulate vesicle trafficking and modulate the subcellular distribution of SLC2A4/GLUT4-vesicles (PubMed:10988299). May be involved in spindle pole assembly through PARsylation of NUMA1 (PubMed:12080061, PubMed:16076287)

**Summary**, from NCBI Gene [8658](https://www.ncbi.nlm.nih.gov/gene/8658):

> Enables several functions, including pentosyltransferase activity; telomerase inhibitor activity; and zinc ion binding activity. Involved in several processes, including positive regulation of canonical Wnt signaling pathway; post-translational protein modification; and regulation of chromosome organization. Acts upstream of or within peptidyl-serine phosphorylation and peptidyl-threonine phosphorylation. Located in Golgi apparatus; chromosome, telomeric region; and mitotic spindle pole. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11941) · Entrez [8658](https://www.ncbi.nlm.nih.gov/gene/8658) · UniProt [O95271](https://www.uniprot.org/uniprotkb/O95271) · Ensembl [ENSG00000173273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173273) · OMIM [603303](https://www.omim.org/entry/603303)

**PubMed**, as HGNC records for this gene — [9822378](https://pubmed.ncbi.nlm.nih.gov/9822378/), [10198177](https://pubmed.ncbi.nlm.nih.gov/10198177/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 250.19 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 171 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.071× |
| Wild-type minus altered | 1.020× |
| Compounds moving it up in WT lines | 77 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00199 |
| As a percentage | -0.14% |
| FDR, exposure-shuffle null | 0.3419 |
| In TP53-wild-type lines / altered lines | 0.00063 / -0.00358 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.062 raw, -0.080 with 3 PCs removed |

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
