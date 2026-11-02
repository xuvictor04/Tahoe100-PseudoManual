---
symbol: PHLDA3
type: gene
tier: 1
aliases: [TIH1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: other
median_line_cpm: 9.55
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PHLDA3

> [!summary] In one line
> PHLDA3 encodes a small PH-domain-only protein that p53 induces to compete AKT off the membrane — one of the few routes by which p53's transcriptional output reaches into PI3K signalling.

## What it is

PHLDA3 is about as minimal as a signalling protein gets: roughly 127 residues, essentially a single pleckstrin homology domain, with no catalytic activity and no other recognisable module. The proposed mechanism follows from that architecture. The PH domain binds membrane phosphoinositides and competes with AKT's own PH domain for them, blocking AKT's recruitment to the plasma membrane and so its activating phosphorylation by PDK1 and mTORC2. The consequence is reduced AKT output: less mTORC1 signalling, less FOXO inhibition, less of the survival signalling AKT normally supplies. It works by occupancy rather than catalysis, so the effect is competitive: it scales with how much PHLDA3 is present.

PHLDA3 is a direct p53 target. p53 binds a response element at the locus and the gene is induced on DNA damage, placing it among the p53 outputs that act on signalling rather than on the cycle, the mitochondrion or repair. Its best-developed disease role is in neuroendocrine tumours: the locus undergoes loss of heterozygosity at high frequency in pancreatic neuroendocrine tumours, with promoter methylation as a plausible second hit; the LOH is reported to be mutually exclusive with p53 loss, which is the argument that PHLDA3 is a principal downstream mediator of p53 in that lineage; Phlda3-deficient mice develop islet hyperplasia, and PHLDA3 loss cooperates with Men1 loss.

## Why it appears in this work

PHLDA3 is a curated p53 effector in the induction arm of [[p53 program P]], and what it contributes is breadth. Most recognisable members of that arm report arrest ([[CDKN1A]]), apoptosis ([[PMAIP1]], [[BBC3]], [[BAX]]), or repair; PHLDA3 reports that p53's output is also reaching growth-factor signalling. Its induction is therefore qualitatively informative in a way its magnitude is not — it says the programme engaged a branch the canonical readouts do not cover. It is also, unlike p21 or [[MDM2]], not an abundant transcript in most of these lines, which bears on how much a single-cell measurement can resolve.

## What is uncertain

That PHLDA3 is p53-inducible is well established. How much of the AKT inhibition attributed to it operates at endogenous expression levels, outside the overexpression and knockdown systems where it was characterised, is a weaker claim, and whether phosphoinositide competition is the whole mechanism — rather than one component alongside unmapped partners — is unsettled. The tumour-suppressor evidence is lineage-concentrated: strong for neuroendocrine tumours, an extrapolation elsewhere, and much of the functional literature comes from one group, so independent replication is thinner than the coherence of the story suggests. Two cautions apply here. PHLDA3 has reported hypoxia- and other stress-responsive inputs, so induction under a drug exposure is not by itself evidence that p53 did it; and the gene carries a mixed-direction flag in the study's own tables, meaning its behaviour across compounds is not uniform — a reason to treat it as a corroborating member of the programme rather than a readout in its own right.

## References

- Kawase et al., 2009, Cell — identified PHLDA3 as a p53-regulated PH-only protein that represses AKT by blocking its membrane translocation.
- Ohki et al., 2014, PNAS — PHLDA3 is a tumour suppressor of pancreatic neuroendocrine tumours, with frequent LOH, islet hyperplasia in deficient mice, and cooperation with Men1 loss.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 9.55 CPM |
| Lines where detected | 44 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 27 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.076× |
| Wild-type minus altered | 1.192× |
| Compounds moving it up in WT lines | 61 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00594 |
| As a percentage | -0.41% |
| FDR, exposure-shuffle null | 0.1388 |
| In TP53-wild-type lines / altered lines | -0.00691 / -0.00526 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.256 raw, -0.037 with 3 PCs removed |

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
