---
symbol: PPM1D
type: gene
tier: 1
aliases: [WIP1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: negative feedback
median_line_cpm: 56.2
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PPM1D

> [!summary] In one line
> PPM1D encodes WIP1, a p53-induced phosphatase that switches the DNA-damage response back off by stripping the activating phosphorylations off ATM, CHK1, CHK2, p53 and MDM2.

## What it is

WIP1 — wild-type p53-induced phosphatase 1 — is a Mg²⁺/Mn²⁺-dependent serine/threonine phosphatase of the PP2C family, encoded at 17q23.2. PP2C enzymes are monomeric — no regulatory or targeting subunits — so substrate choice is built into the catalytic domain rather than supplied by a partner. It was found as a transcript induced after ionising radiation in a p53-dependent manner, still the cleanest fact about it.

Its function is to reverse the damage response. The phosphorylations that ATM and ATR install to raise the alarm — ATM's own Ser1981 autophosphorylation, CHK2 Thr68, CHK1, Ser15 on p53, Ser139 on H2AX, Ser395 on MDM2, Thr180 on p38 MAPK — are WIP1 substrates. Because p53 drives PPM1D transcription and WIP1 then dephosphorylates p53 and its upstream kinases, the arrangement is a delayed negative feedback loop built one layer below [[MDM2]]'s: MDM2 controls how much p53 protein there is, WIP1 controls how activated it is. They converge: dephosphorylated MDM2 is more stable and binds p53 more avidly, so WIP1 reinforces the brake it parallels.

Clinically PPM1D behaves as an oncogene in tumours that keep wild-type p53: it sits in a recurrent 17q23 amplicon in breast cancer, where amplification was argued to abrogate p53 function without mutating it. A second, stranger mode came later: truncating mutations in the last two exons produce a stable protein that keeps the catalytic domain and behaves as gain-of-function. Acquired somatically in blood, they drive clonal haematopoiesis that expands specifically under cytotoxic chemotherapy; arising de novo in the germline, the same class of variant causes Jansen-de Vries syndrome. An allosteric inhibitor, GSK2830371, made the enzyme a tractable target.

## Why it appears in this work

PPM1D is a strongly and consistently induced direct member of [[p53 program P]], which makes it a reliable reporter that p53 is engaged rather than that cells are merely stressed. It also carries an interpretive warning: it is an induced off-switch, so seeing it up means the response being measured has already started building the machinery that terminates it. A 24 h snapshot of a feedback component says where in the response a cell sits, not only that it happened — the same caution as for [[MDM2]] and [[CCNG1]].

## What is uncertain

The substrate list is long and mostly from overexpression and in vitro work. Which substrates WIP1 governs at endogenous levels in a given cell type is far less settled than the catalogue suggests, and papers differ on whether ATM, p53 or p38 is limiting. That PPM1D is a direct p53 target is well supported; whether its phosphatase activity is itself regulated — rather than simply set by how much protein is present — is not resolved, and no activating modification or ligand is established. The oncogenic mechanism is contested between a p53-centred route and a p38/p16-centred one. The 17q23 amplicon is broad and contains other candidate drivers, so amplification data alone do not pin a phenotype on PPM1D. Finally, the truncating variants show two distinct disease mechanisms pointing the same functional way; treating "PPM1D activity" as one quantity is a simplification.

## References

- Fiscella et al., 1997, PNAS — identified Wip1 as a human protein phosphatase induced by ionising radiation in a p53-dependent manner.
- Bulavin et al., 2002, Nature Genetics — amplification of PPM1D in human tumours abrogates p53 tumour-suppressor activity; Li et al. reported its oncogenic properties in the 17q23 breast cancer amplicon in the same journal and year.
- Shreeram et al., 2006, Molecular Cell — Wip1 modulates ATM-dependent signalling, including dephosphorylation of ATM Ser1981.
- Lu et al., 2007, Cancer Cell — Wip1 as a gatekeeper in the p53–MDM2 autoregulatory loop, acting through MDM2 stabilisation.
- Jansen et al., 2017, American Journal of Human Genetics — de novo truncating mutations in the last and penultimate exons of PPM1D cause an intellectual disability syndrome.
- Hsu et al., 2018, Cell Stem Cell — PPM1D mutations drive clonal haematopoiesis in response to cytotoxic chemotherapy.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 56.20 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 1 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.243× |
| Wild-type minus altered | 1.170× |
| Compounds moving it up in WT lines | 93 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00202 |
| As a percentage | -0.14% |
| FDR, exposure-shuffle null | 0.5791 |
| In TP53-wild-type lines / altered lines | -0.00737 / 0.00123 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.216 raw, -0.067 with 3 PCs removed |

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
