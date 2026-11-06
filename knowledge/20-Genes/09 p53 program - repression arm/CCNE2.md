---
symbol: CCNE2
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [cyclin E2]
gene_name: cyclin E2
locus: 8q22.1
locus_type: gene with protein product
gene_family: [Cyclins]
family_siblings_here: [CCNG1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 7.5
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# CCNE2

*cyclin E2* — 8q22.1

> [!summary] In one line
> CCNE2 encodes cyclin E2, a CDK2 partner that accumulates at the G1/S transition and licenses entry into S phase.

## What it is

Cyclin E2 is the second E-type cyclin, sharing CDK2 and its late-G1 window with cyclin E1, and phosphorylating RB and p27. Its transcription is an E2F output, and the protein is degraded by SCF-[[FBXW7]] after autophosphorylation, so both message and protein are sharply cell-cycle periodic. Mice lacking both E cyclins develop surprisingly far: E cyclins are dispensable for ordinary mitotic cycles and needed for endoreplication and re-entry from quiescence, making cyclin E2 a reinforcer rather than the gatekeeper of S phase. It is frequently amplified in cancer, notably breast cancer, where high cyclin E tracks resistance to endocrine and CDK4/6 therapy.

## Why it appears in this work

CCNE2 sits in the repression arm of [[p53 program P]], and is about as canonical a member as that arm has: a textbook E2F and DREAM target whose fall under p53 activators is what [[The p21-DREAM axis]] predicts. Because it is repressed, the sign of any MG53 association must be flipped before it says anything about p53 output; see [[Signing genes by p53 direction]].

## What is uncertain

Cyclin E2 mRNA is partly a readout of what fraction of cells are in late G1 or S, so "repressed by p53" here may mean no more than arrest; for this class of gene the direct-versus-indirect question resolves as indirect. Redundancy with CCNE1 also means transcript changes do not map cleanly onto CDK2 activity. The circularity warning below applies with full force.

## References

- Lauper et al., 1998, Oncogene — identified cyclin E2 as a CDK2 partner acting in late G1 and S phase.
- Gudas et al., 1999, Molecular and Cellular Biology — characterised cyclin E2 and its aberrant expression in human cancers.
- Geng et al., 2003, Cell — cyclin E1/E2 double-knockout mice show E cyclins are dispensable for normal cycles but needed for endoreplication.
- Litovchick et al., 2007, Molecular Cell — described the DREAM complex repressing cell-cycle-dependent genes.
- Fischer et al., 2016, Nucleic Acids Research — integrated TP53, DREAM and RB-E2F target analyses into cell-cycle gene regulatory networks.

## What is on record

| | |
|---|---|
| Official name | cyclin E2 |
| Also known as | CYCE2 |
| Locus | 8q22.1 — gene with protein product |
| Gene families | Cyclins |
| Other genes here in those families | [[CCNG1]] |

**Function**, from UniProt [O96020](https://www.uniprot.org/uniprotkb/O96020) (reviewed):

> Essential for the control of the cell cycle at the late G1 and early S phase

**Summary**, from NCBI Gene [9134](https://www.ncbi.nlm.nih.gov/gene/9134):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with and functions as a regulatory subunit of CDK2. This cyclin has been shown to specifically interact with CIP/KIP family of CDK inhibitors, and plays a role in cell cycle G1/S transition. The expression of this gene peaks at the G1-S phase and exhibits a pattern of tissue specificity distinct from that of cyclin E1. A significantly increased expression level of this gene was observed in tumor-derived cells. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:1590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1590) · Entrez [9134](https://www.ncbi.nlm.nih.gov/gene/9134) · UniProt [O96020](https://www.uniprot.org/uniprotkb/O96020) · Ensembl [ENSG00000175305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175305) · OMIM [603775](https://www.omim.org/entry/603775)

**PubMed**, as HGNC records for this gene — [9840927](https://pubmed.ncbi.nlm.nih.gov/9840927/), [9840943](https://pubmed.ncbi.nlm.nih.gov/9840943/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 7.50 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.931× |
| Wild-type minus altered | 0.913× |
| Compounds moving it up in WT lines | 23 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01206 |
| As a percentage | +0.84% |
| FDR, exposure-shuffle null | 0.0677 |
| In TP53-wild-type lines / altered lines | 0.01768 / 0.00865 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.448 raw, 0.135 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[The p21-DREAM axis]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, repression arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
