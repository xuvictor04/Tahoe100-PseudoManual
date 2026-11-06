---
symbol: TLE4
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [E(spl), ESG, GRG4]
gene_name: TLE family member 4, transcriptional corepressor
locus: 9q21.31
locus_type: gene with protein product
gene_family: [WD repeat domain containing, Wnt enhanceosome complex, TLE family]
family_siblings_here: [COP1, DDB2, DNAI3, FBXW7, RIC1, WDR48]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 67.19
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TLE4

*TLE family member 4, transcriptional corepressor* — 9q21.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TLE4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | TLE family member 4, transcriptional corepressor |
| Also known as | E(spl), ESG, GRG4 |
| Locus | 9q21.31 — gene with protein product |
| Gene families | WD repeat domain containing; Wnt enhanceosome complex; TLE family |
| Other genes here in those families | [[COP1]], [[DDB2]], [[DNAI3]], [[FBXW7]], [[RIC1]], [[WDR48]] |
| Previously named | transducin-like enhancer of split 4 (E(sp1) homolog, Drosophila); transducin like enhancer of split 4 |

**Function**, from UniProt [Q04727](https://www.uniprot.org/uniprotkb/Q04727) (reviewed):

> Transcriptional corepressor that binds to a number of transcription factors. Inhibits the transcriptional activation mediated by PAX5, and by CTNNB1 and TCF family members in Wnt signaling. The effects of full-length TLE family members may be modulated by association with dominant-negative AES. Essential for the transcriptional repressor activity of SIX3 during retina and lens development and for SIX3 transcriptional auto-repression (By similarity). Involved in transcriptional repression of GNRHR and enhances MSX1-mediated transcriptional repression of CGA/alpha-GSU (By similarity)

**Summary**, from NCBI Gene [7091](https://www.ncbi.nlm.nih.gov/gene/7091):

> Predicted to enable transcription corepressor activity. Predicted to be involved in negative regulation of canonical Wnt signaling pathway and negative regulation of transcription by RNA polymerase II. Predicted to act upstream of or within Wnt signaling pathway; cellular response to leukemia inhibitory factor; and negative regulation of DNA-templated transcription. Located in nucleoplasm. Part of beta-catenin-TCF complex. [provided by Alliance of Genome Resources, Apr 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11840) · Entrez [7091](https://www.ncbi.nlm.nih.gov/gene/7091) · UniProt [Q04727](https://www.uniprot.org/uniprotkb/Q04727) · Ensembl [ENSG00000106829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106829) · OMIM [605132](https://www.omim.org/entry/605132)

**PubMed**, as HGNC records for this gene — [8365415](https://pubmed.ncbi.nlm.nih.gov/8365415/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 67.19 CPM |
| Lines where detected | 43 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 95 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.065× |
| Wild-type minus altered | 1.064× |
| Compounds moving it up in WT lines | 75 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01643 |
| As a percentage | +1.15% |
| FDR, exposure-shuffle null | 0.0001 |
| In TP53-wild-type lines / altered lines | 0.01544 / 0.01711 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.478 raw, 0.388 with 3 PCs removed |

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
