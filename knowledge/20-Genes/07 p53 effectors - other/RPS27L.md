---
symbol: RPS27L
type: gene
tier: 1
pathway_role: p53 effector: other
aliases: [ribosomal protein S27-like]
gene_name: ribosomal protein S27 like
locus: 15q22.2
locus_type: gene with protein product
gene_family: [S ribosomal proteins]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: other
median_line_cpm: 53.91
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RPS27L

*ribosomal protein S27 like* — 15q22.2

> [!summary] In one line
> RPS27L encodes a p53-induced paralogue of ribosomal protein S27 that differs from it by only three amino acids, incorporates into the 40S subunit, and binds MDM2 — placing it at the junction between p53 and the ribosome.

## What it is

RPS27L is an 84-residue small-subunit ribosomal protein at 15q22.2, very nearly a duplicate of RPS27: in human and mouse the proteins differ at just three positions. The gene's name records the resemblance, which is both why it is interesting and why it is awkward to measure.

What distinguishes RPS27L from an ordinary ribosomal protein gene is its regulation. It is a direct p53 target, with a response element demonstrated in the first intron. Which way it tips cell fate was reported in both directions in the same year: the group that identified it as a p53 target found RPS27L *promotes* etoposide-induced apoptosis, so silencing it reduces apoptosis; an independent group found that depleting it defeats the damage checkpoints and converts the p53 response from arrest to apoptosis. It also engages the p53 machinery as protein. RPS27L binds the central acidic domain of MDM2, competes with p53 for that interaction, and is itself ubiquitylated by MDM2 — target, substrate and regulator of the same axis.

The mouse genetics complicate the picture. Germline inactivation of *Rps27l* stabilises Mdm2, which degrades Mdm4 and unbalances the Mdm2–Mdm4 ligase, activating p53 strongly enough to deplete haematopoietic stem cells and kill the animals after birth. On a *Trp53*-heterozygous background the same loss instead produces lymphoma with loss of the remaining p53 allele and marked aneuploidy. Separately, work on paralogue retention found that Rps27- and Rps27l-containing ribosomes associate preferentially with different transcripts, and that the two loss-of-function alleles are lethal at different developmental stages — evidence for subfunctionalised expression rather than interchangeable proteins.

## Why it appears in this work

RPS27L is a p53 target that is not an effector in the usual sense. It does not arrest the cycle or trigger apoptosis; it is a structural component of the translation apparatus, so its induction shows p53's reach extending into ribosome composition, and it is one route by which p53 activation feeds back onto [[MDM2]]. For a vault built around [[p53 program P]], it marks the edge where "p53 output" stops meaning a discrete cellular decision. It also carries a measurement lesson that rhymes with this project's central theme: a gene can be hard to read not because of a neighbour's transcription, as in [[The TRIM72 locus]], but because an abundant near-identical paralogue sits elsewhere in the genome.

## What is uncertain

The direction of RPS27L's effect on p53 is genuinely contested. The cell-based work has it sequestering MDM2 and so stabilising p53 — an activator; the mouse knockout has p53 going *up* when RPS27L is removed — a restraint. Both come from the same laboratory and are not obviously reconcilable by one mechanism; the resolution probably involves Mdm2/Mdm4 stoichiometry and differs between acute perturbation and germline loss, but that is interpretation, not an established answer. Whether RPS27L has a function distinct from RPS27, as opposed to a different expression pattern, remains open; the paralogue-retention work favours divergent expression over divergent protein chemistry. Given a three-residue difference from a far more abundant paralogue, read assignment between RPS27L and RPS27 rests on a handful of distinguishing positions, so modest apparent changes here deserve more caution than in a gene with no close relative. Ribosomal protein transcripts are also dominated by growth- and translation-coupled regulation, so a p53 signal read off this gene competes with a much larger source of variation.

## References

- He & Sun, 2007, Oncogene — RPS27L is a direct p53 target, with a p53-binding site in its first intron; overexpression promoted and silencing inhibited etoposide-induced apoptosis.
- Li et al., 2007, Cancer Research — RPS27L as a p53-inducible modulator of cell fate: its depletion causes checkpoint deficiency and converts the damage response from arrest to apoptosis, the opposite direction to He & Sun.
- Xiong et al., 2011, Oncogene — RPS27L and RPS27 interplay with the p53–MDM2 axis as a target, a substrate and a regulator; maps binding to MDM2's central acidic domain.
- Xiong et al., 2014, eLife — germline *Rps27l* loss activates p53 via Mdm2 stabilisation and Mdm4 degradation, and promotes lymphoma with aneuploidy on a *Trp53*-heterozygous background.
- Xu et al., 2023, eLife — subfunctionalised expression, not protein divergence, accounts for retention of Rps27 and Rps27l in vertebrates.

## What is on record

| | |
|---|---|
| Official name | ribosomal protein S27 like |
| Also known as | — (no recorded alias) |
| Locus | 15q22.2 — gene with protein product |
| Gene families | S ribosomal proteins |
| Previously named | ribosomal protein S27-like |

UniProt [Q71UM5](https://www.uniprot.org/uniprotkb/Q71UM5) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [51065](https://www.ncbi.nlm.nih.gov/gene/51065):

> This gene encodes a protein sharing 96% amino acid similarity with ribosomal protein S27, which suggests the encoded protein may be a component of the 40S ribosomal subunit. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18476) · Entrez [51065](https://www.ncbi.nlm.nih.gov/gene/51065) · UniProt [Q71UM5](https://www.uniprot.org/uniprotkb/Q71UM5) · Ensembl [ENSG00000185088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185088) · OMIM [612055](https://www.omim.org/entry/612055)

**PubMed**, as HGNC records for this gene — [11042152](https://pubmed.ncbi.nlm.nih.gov/11042152/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 53.91 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 38 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.017× |
| Wild-type minus altered | 1.098× |
| Compounds moving it up in WT lines | 50 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00024 |
| As a percentage | -0.02% |
| FDR, exposure-shuffle null | 0.9407 |
| In TP53-wild-type lines / altered lines | 0.00011 / -0.00045 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.197 raw, -0.168 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
