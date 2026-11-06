---
symbol: WWP1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [AIP5, DKFZP434D2111]
gene_name: WW domain containing E3 ubiquitin protein ligase 1
locus: 8q21.3
locus_type: gene with protein product
gene_family: [C2 and WW domain containing, Nedd4 family E3 ubiquitin protein ligases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 105.75
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# WWP1

*WW domain containing E3 ubiquitin protein ligase 1* — 8q21.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/WWP1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | WW domain containing E3 ubiquitin protein ligase 1 |
| Also known as | AIP5, DKFZP434D2111 |
| Locus | 8q21.3 — gene with protein product |
| Gene families | C2 and WW domain containing; Nedd4 family E3 ubiquitin protein ligases |

**Function**, from UniProt [Q9H0M0](https://www.uniprot.org/uniprotkb/Q9H0M0) (reviewed):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates (PubMed:12535537, PubMed:15221015, PubMed:15359284, PubMed:34404733). Ubiquitinates ERBB4 isoforms JM-A CYT-1 and JM-B CYT-1, KLF2, KLF5 and TP63 and promotes their proteasomal degradation (By similarity). Ubiquitinates RNF11 without targeting it for degradation (By similarity). Ubiquitinates and promotes degradation of TGFBR1; the ubiquitination is enhanced by SMAD7 (PubMed:15221015, PubMed:15359284). Ubiquitinates SMAD6 and SMAD7 (PubMed:15221015). Ubiquitinates and promotes degradation of SMAD2 in response to TGF-beta signaling, which requires interaction with TGIF (PubMed:15221015, PubMed:15359284). Activates the Hippo signaling pathway in response to cell contact inhibition and recruitment to the Crumbs complex at the cell membrane (PubMed:34404733). Monoubiquitinates AMOTL2 which facilitates its interaction with and activation of LATS2 (PubMed:34404733). LATS2 then phosphorylates YAP1, excluding it from the nucleus and therefore ultimately represses YAP1-driven transcription of target genes (PubMed:34404733). Acts as a negative regulator of smoothened signaling pathway by mediating 'Lys-63'-linked ubiquitination of smoothened (SMO) in primary cilia, leading to SMO removal from the primary cilium (By similarity)

**Summary**, from NCBI Gene [11059](https://www.ncbi.nlm.nih.gov/gene/11059):

> WW domain-containing proteins are found in all eukaryotes and play an important role in the regulation of a wide variety of cellular functions such as protein degradation, transcription, and RNA splicing. This gene encodes a protein which contains 4 tandem WW domains and a HECT (homologous to the E6-associated protein carboxyl terminus) domain. The encoded protein belongs to a family of NEDD4-like proteins, which are E3 ubiquitin-ligase molecules and regulate key trafficking decisions, including targeting of proteins to proteosomes or lysosomes. Alternative splicing of this gene generates at least 6 transcript variants; however, the full length nature of these transcripts has not been defined. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17004) · Entrez [11059](https://www.ncbi.nlm.nih.gov/gene/11059) · UniProt [Q9H0M0](https://www.uniprot.org/uniprotkb/Q9H0M0) · Ensembl [ENSG00000123124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123124) · OMIM [602307](https://www.omim.org/entry/602307)

**PubMed**, as HGNC records for this gene — [9169421](https://pubmed.ncbi.nlm.nih.gov/9169421/), [9647693](https://pubmed.ncbi.nlm.nih.gov/9647693/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 105.75 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 162 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.031× |
| Wild-type minus altered | 1.035× |
| Compounds moving it up in WT lines | 66 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00263 |
| As a percentage | -0.18% |
| FDR, exposure-shuffle null | 0.2988 |
| In TP53-wild-type lines / altered lines | -0.00372 / -0.00197 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.331 raw, -0.174 with 3 PCs removed |

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
