---
symbol: SESN1
type: gene
tier: 1
pathway_role: p53 effector: metabolism / redox
aliases: [PA26, sestrin 1]
gene_name: sestrin 1
locus: 6q21
locus_type: gene with protein product
gene_family: [Sestrin family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: metabolism / redox
median_line_cpm: 44.64
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SESN1

*sestrin 1* — 6q21

> [!summary] In one line
> SESN1 encodes sestrin 1, a stress-inducible protein that restrains mTORC1 and lowers reactive oxygen species, and one of the most dependably p53-dependent transcripts in the human genome.

## What it is

SESN1 was cloned as PA26 — "p53-activated gene 26" — and the identification was unusually clean: a p53 response element in intron 2, induction by genotoxic agents only when p53 is present. It is one of three mammalian sestrins (SESN1, SESN2, SESN3). The sestrin fold matches no familiar enzyme class; its closest recognised relative is bacterial AhpD, which is how the original antioxidant hypothesis arose.

What sestrins are now best understood to do is inhibit mTORC1. The first mechanism proposed was indirect: sestrins 1 and 2 activate AMPK, which phosphorylates TSC2 and suppresses mTORC1, linking DNA damage to a halt in anabolic growth. A more direct route came later — sestrins bind GATOR2 in the amino-acid-sensing arm upstream of mTORC1, and for sestrin 2 that interaction is governed by direct leucine binding. Both converge on the same output: less mTORC1, less cap-dependent translation, more autophagy.

The antioxidant side is real but less mechanistically settled. Sestrin expression lowers intracellular ROS in many systems, and sestrin loss raises it; what is no longer tenable is the specific claim that sestrins act as reductases for overoxidised peroxiredoxins. Inputs besides p53 are described for the family, but they sort unevenly across the three paralogues: oxidative and hypoxic induction of SESN2 and SESN3 proceeds without p53, whereas SESN1's requires it, and the clear FOXO target is SESN3, with only a reported minor contribution to SESN1.

## Why it appears in this work

SESN1 is a curated p53 effector in the metabolic and redox arm of [[p53 program P]], and its value here is twofold. First, it reports a branch of p53's output that the canonical readouts do not cover: not arrest ([[CDKN1A]], [[The p21-DREAM axis]]) and not apoptosis ([[PMAIP1]], [[BBC3]], [[BAX]]), but growth and nutrient signalling, in the same direction as [[TIGAR]]. Second, it is well expressed across cancer lineages rather than tissue-restricted, which makes it one of the more practical p53 readouts in sparse single-cell data — the opposite situation to [[Why MG53 is hard to measure here]].

## What is uncertain

The strongest claim is the weakest-sounding one: SESN1 is p53-inducible. Almost everything downstream carries qualifications. The AMPK/TSC2 and GATOR2 routes have not been reconciled into a single accounting. More importantly for this gene specifically, the structural and leucine-sensing work was done on sestrin 2; transferring it to sestrin 1 is a paralogue inference, not a result. Much of what is written about "sestrins" rests on SESN2 experiments, so claims about SESN1's own biology are thinner than the family literature suggests.

The redox function remains mechanistically open now that the peroxiredoxin-reductase model has failed; lower ROS may be downstream of mTORC1 inhibition, autophagy or NRF2 rather than a direct catalytic activity. The standing caution that a stress gene's induction need not mean p53 caused it applies less forcefully here than to most of this panel, because the p53-independent routes in the sestrin literature are largely SESN2 and SESN3 results; a FOXO contribution to SESN1 and a HIF1 input have been reported, so it is not a pure p53 reporter, but it is a more specific one than its paralogues. Finally, SESN1 is not a recurrently mutated cancer gene; its tumour-suppressive reading is inherited from p53 rather than established on its own.

## References

- Velasco-Miguel et al., 1999, Oncogene — identified PA26/SESN1 as a p53-inducible gene with a p53 response element in intron 2.
- Budanov & Karin, 2008, Cell — sestrin1 and sestrin2 are p53 targets that activate AMPK, target it to TSC2 and inhibit mTOR.
- Woo et al., 2009, Antioxidants & Redox Signaling — sestrin 2 does not reduce the cysteine sulfinic acid of peroxiredoxins, contradicting the proposed reductase role.
- Chantranupong et al., 2014, Cell Reports — the sestrins interact with GATOR2 to negatively regulate the amino-acid-sensing pathway upstream of mTORC1.
- Wolfson et al., 2016, Science — sestrin 2 binds leucine directly and acts as a leucine sensor for mTORC1.

## What is on record

| | |
|---|---|
| Official name | sestrin 1 |
| Also known as | SEST1, PA26 |
| Locus | 6q21 — gene with protein product |
| Gene families | Sestrin family |

**Function**, from UniProt [Q9Y6P5](https://www.uniprot.org/uniprotkb/Q9Y6P5) (reviewed):

> Functions as an intracellular leucine sensor that negatively regulates the TORC1 signaling pathway through the GATOR complex. In absence of leucine, binds the GATOR subcomplex GATOR2 and prevents TORC1 signaling. Binding of leucine to SESN2 disrupts its interaction with GATOR2 thereby activating the TORC1 signaling pathway (PubMed:25263562, PubMed:26449471). This stress-inducible metabolic regulator may also play a role in protection against oxidative and genotoxic stresses (By similarity). May positively regulate the transcription by NFE2L2 of genes involved in the response to oxidative stress by facilitating the SQSTM1-mediated autophagic degradation of KEAP1 (PubMed:23274085). Moreover, may prevent the accumulation of reactive oxygen species (ROS) through the alkylhydroperoxide reductase activity born by the N-terminal domain of the protein (By similarity). Was originally reported to contribute to oxidative stress resistance by reducing PRDX1 (PubMed:15105503). However, this could not be confirmed (By similarity)

**Summary**, from NCBI Gene [27244](https://www.ncbi.nlm.nih.gov/gene/27244):

> This gene encodes a member of the sestrin family. Sestrins are induced by the p53 tumor suppressor protein and play a role in the cellular response to DNA damage and oxidative stress. The encoded protein mediates p53 inhibition of cell growth by activating AMP-activated protein kinase, which results in the inhibition of the mammalian target of rapamycin protein. The encoded protein also plays a critical role in antioxidant defense by regenerating overoxidized peroxiredoxins, and the expression of this gene is a potential marker for exposure to radiation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:21595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21595) · Entrez [27244](https://www.ncbi.nlm.nih.gov/gene/27244) · UniProt [Q9Y6P5](https://www.uniprot.org/uniprotkb/Q9Y6P5) · Ensembl [ENSG00000080546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080546) · OMIM [606103](https://www.omim.org/entry/606103)

**PubMed**, as HGNC records for this gene — [9926927](https://pubmed.ncbi.nlm.nih.gov/9926927/), [7938006](https://pubmed.ncbi.nlm.nih.gov/7938006/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 44.64 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 35 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.144× |
| Wild-type minus altered | 1.098× |
| Compounds moving it up in WT lines | 86 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00047 |
| As a percentage | +0.03% |
| FDR, exposure-shuffle null | 0.9141 |
| In TP53-wild-type lines / altered lines | -0.00603 / 0.00442 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.212 raw, -0.049 with 3 PCs removed |

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
