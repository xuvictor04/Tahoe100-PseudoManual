---
symbol: NHEJ1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [Cernunnos, XLF, FLJ12610]
gene_name: non-homologous end joining factor 1
locus: 2q35
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 28.72
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# NHEJ1

*non-homologous end joining factor 1* — 2q35

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NHEJ1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | non-homologous end joining factor 1 |
| Also known as | Cernunnos, XLF, FLJ12610, XRCC4-like factor |
| Locus | 2q35 — gene with protein product |
| Previously named | nonhomologous end-joining factor 1 |

**Function**, from UniProt [Q9H9Q4](https://www.uniprot.org/uniprotkb/Q9H9Q4) (reviewed):

> DNA repair protein involved in DNA non-homologous end joining (NHEJ); it is required for double-strand break (DSB) repair and V(D)J recombination and is also involved in telomere maintenance (PubMed:16439204, PubMed:16439205, PubMed:17317666, PubMed:17470781, PubMed:17717001, PubMed:18158905, PubMed:18644470, PubMed:20558749, PubMed:26100018, PubMed:28369633). Plays a key role in NHEJ by promoting the ligation of various mismatched and non-cohesive ends (PubMed:17470781, PubMed:17717001, PubMed:19056826). Together with PAXX, collaborates with DNA polymerase lambda (POLL) to promote joining of non-cohesive DNA ends (PubMed:25670504, PubMed:30250067). May act in concert with XRCC5-XRCC6 (Ku) to stimulate XRCC4-mediated joining of blunt ends and several types of mismatched ends that are non-complementary or partially complementary (PubMed:16439204, PubMed:16439205, PubMed:17317666, PubMed:17470781). In some studies, has been shown to associate with XRCC4 to form alternating helical filaments that bridge DNA and act like a bandage, holding together the broken DNA until it is repaired (PubMed:21768349, PubMed:21775435, PubMed:22228831, PubMed:22287571, PubMed:26100018, PubMed:27437582, PubMed:28500754). Alternatively, it has also been shown that rather than forming filaments, a single NHEJ1 dimer interacts through both head domains with XRCC4 to promote the close alignment of DNA ends (By similarity). The XRCC4-NHEJ1/XLF subcomplex binds to the DNA fragments of a DSB in a highly diffusive manner and robustly bridges two independent DNA molecules, holding the broken DNA fragments in close proximity to one other (PubMed:27437582, PubMed:28500754). The mobility of the bridges ensures that the ends remain accessible for further processing by other repair factors (PubMed:27437582). Binds DNA in a length-dependent manner (PubMed:17317666, PubMed:18158905)

**Summary**, from NCBI Gene [79840](https://www.ncbi.nlm.nih.gov/gene/79840):

> Double-strand breaks in DNA result from genotoxic stresses and are among the most damaging of DNA lesions. This gene encodes a DNA repair factor essential for the nonhomologous end-joining pathway, which preferentially mediates repair of double-stranded breaks. Mutations in this gene cause different kinds of severe combined immunodeficiency disorders. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25737) · Entrez [79840](https://www.ncbi.nlm.nih.gov/gene/79840) · UniProt [Q9H9Q4](https://www.uniprot.org/uniprotkb/Q9H9Q4) · Ensembl [ENSG00000187736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187736) · OMIM [611290](https://www.omim.org/entry/611290)

**PubMed**, as HGNC records for this gene — [16439204](https://pubmed.ncbi.nlm.nih.gov/16439204/), [16439205](https://pubmed.ncbi.nlm.nih.gov/16439205/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 28.72 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 137 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.011× |
| Wild-type minus altered | 1.021× |
| Compounds moving it up in WT lines | 63 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01820 |
| As a percentage | +1.27% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.01510 / 0.02008 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.156 raw, 0.405 with 3 PCs removed |

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
