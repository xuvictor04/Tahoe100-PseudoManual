---
symbol: TIGAR
type: gene
tier: 1
aliases: [C12orf5]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: metabolism / redox
median_line_cpm: 35.73
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TIGAR

> [!summary] In one line
> TIGAR encodes a p53-inducible phosphatase that lowers fructose-2,6-bisphosphate, slowing glycolysis and diverting glucose into the pentose phosphate pathway — making it a p53 target that protects cells rather than killing them.

## What it is

The name is the mechanism as proposed: TP53-induced glycolysis and apoptosis regulator. Formerly C12orf5, it was found as a p53-inducible transcript resembling the bisphosphatase half of the bifunctional 6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase enzymes — only that half: histidine-phosphatase fold and catalytic histidine, no kinase domain.

Fructose-2,6-bisphosphate is the allosteric activator of phosphofructokinase-1, the committed step of glycolysis; hydrolysing it inhibits PFK-1, backs glucose-6-phosphate up into the oxidative pentose phosphate pathway and raises NADPH and so reduced glutathione. Lower ROS follows, and apoptosis resistance. This is p53's cytoprotective arm at its clearest: the factor that induces [[BAX]] and [[PMAIP1]] also induces a gene that keeps stressed cells alive and reducing. A second activity has been described: under hypoxia a fraction of TIGAR relocalises to mitochondria and complexes with hexokinase 2, raising its activity in a HIF1α-dependent manner.

The mouse genetics are awkward. Tigar-null mice develop normally; what they cannot do is regenerate intestinal epithelium after damage, a defect rescued by ROS scavengers and nucleosides. In an intestinal adenoma model, TIGAR loss reduces tumour burden and extends survival, and TIGAR is elevated in human colon tumours — on that evidence it supports rapid proliferation, malignant included.

## Why it appears in this work

TIGAR is a curated p53 effector in the metabolic and redox arm of [[p53 program P]], and the member that most usefully complicates it. Induction of TIGAR does not mean cells are dying; it means p53 has engaged its antioxidant, survival-permitting branch, as [[SESN1]] does, distinct from the arrest axis ([[CDKN1A]], [[The p21-DREAM axis]]) and the apoptotic effectors ([[BBC3]], [[PMAIP1]]). For a reader of this study it is the reminder that "more p53 output" and "more cell death" are not the same quantity, and that a signature aggregating both arms averages over opposing consequences — see [[Signing genes by p53 direction]].

## What is uncertain

Whether fructose-2,6-bisphosphate hydrolysis is the activity that matters in cells is a live question. Catalytic efficiency on that substrate is modest, the structural work shows an active site considerably more open than the specificity-restricted pocket of PFK-2/FBPase-2, and activity on 2,3-bisphosphoglycerate has also been reported. Few studies have separated phosphatase-dependent from phosphatase-independent effects with catalytically dead mutants, so much of what is credited to the enzymology could belong to protein interactions — as the hexokinase 2 result, characterised under hypoxia alone, suggests.

Two further cautions. TIGAR has p53-independent inputs, so its induction under a compound is not evidence that p53 is engaged; it corroborates a p53 reading only alongside more specific members. And its directional meaning for cancer is inverted relative to its origin: a p53 target ought to be tumour-suppressive, but the knockout mice and human tumour expression both argue it supports tumour growth — a context-dependent survival factor that p53 happens to control. The step from transcript to metabolite is also not short: fructose-2,6-bisphosphate is under layered allosteric control, and a modest change in TIGAR mRNA need not move it measurably.

## References

- Bensaad et al., 2006, Cell — identified TIGAR as a p53-inducible regulator of glycolysis and apoptosis acting through fructose-2,6-bisphosphate and the pentose phosphate pathway.
- Li & Jogl, 2009, Journal of Biological Chemistry — structural and biochemical characterisation of TIGAR, showing a histidine-phosphatase fold with a more open active site than PFK-2/FBPase-2.
- Cheung et al., 2012, PNAS — mitochondrial localisation of TIGAR under hypoxia stimulates hexokinase 2 and lowers ROS and cell death.
- Cheung et al., 2013, Developmental Cell — TIGAR is dispensable for normal development but required for efficient intestinal regeneration and for tumour growth in an intestinal adenoma model.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 35.73 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 56 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.209× |
| Wild-type minus altered | 1.132× |
| Compounds moving it up in WT lines | 83 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00431 |
| As a percentage | +0.30% |
| FDR, exposure-shuffle null | 0.2920 |
| In TP53-wild-type lines / altered lines | -0.00291 / 0.00888 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.382 raw, -0.043 with 3 PCs removed |

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

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
