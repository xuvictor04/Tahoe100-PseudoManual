---
symbol: CCNG1
type: gene
tier: 1
aliases: [cyclin G1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: cell-cycle arrest
median_line_cpm: 63.21
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CCNG1

> [!summary] In one line
> CCNG1 encodes cyclin G1, an atypical cyclin that is one of p53's most reliably induced direct targets and that has been reported to feed back on p53 by recruiting PP2A to MDM2.

## What it is

Cyclin G1 carries a recognisable cyclin box but behaves very little like a cell-cycle cyclin. It has no established CDK partner that drives a cell-cycle transition, and it is not expressed with the periodicity that defines the canonical cyclins. What it does have is an unusually clean relationship to p53: cyclin G was identified as a transcriptional target of p53, and it is among the genes induced most consistently and most strongly when p53 is activated, across many cell types and many kinds of stress.

Its proposed function is as a phosphatase-targeting subunit. Cyclin G1 associates with the B′/B56 (PPP2R5) regulatory subunits of protein phosphatase 2A in a p53-dependent manner, and it also binds MDM2, where it markedly stimulates PP2A's ability to dephosphorylate MDM2 at T216 (and reduces phosphorylation at S166 of the human protein). Because dephosphorylated MDM2 binds p53 more avidly, the net effect is to lower p53. Cells lacking cyclin G have hyperphosphorylated MDM2 and higher p53 protein, which is the main genetic support for the model. The arrangement makes cyclin G1 a negative-feedback component: p53 induces it, and it damps p53 — the same topology as [[MDM2]], reached by a different mechanism. Beyond this, cyclin G1 has been implicated in hepatocyte proliferation and liver regeneration, and the gene is amplified or overexpressed in a subset of tumours.

## Why it appears in this work

Cyclin G1 is a strong, well-measured, direct member of [[p53 program P]], which makes it one of the genes whose induction can be trusted to report p53 engagement rather than a generic stress response — useful precisely because its expression level is high enough to be measured well in single cells at 24 h. Its mechanistic position adds a second reading: like MDM2, an induced feedback brake means the p53 output being measured is already attenuating itself, so a snapshot of cyclin G1 says something about where in the response a cell sits, not only that the response happened.

## What is uncertain

The PP2A–MDM2 mechanism rests essentially on one 2002 study and the reviews that summarise it; I am not aware of a clear independent replication, and the model should be held more loosely than cyclin G1's status as a p53 target. Even within that work the dose–response is paradoxical: low re-expression of cyclin G increased p53-associated MDM2 while higher levels had the opposite effect, which is hard to reconcile with a simple linear brake. Whether cyclin G1 is a cyclin in the functional sense — a subunit that activates a CDK — remains unresolved. Reports also split on whether cyclin G1 is net growth-promoting or growth-suppressing, with the direction varying by cell type and p53 status. The summary position worth holding: that p53 induces CCNG1 is well established; what CCNG1 then does is not.

## References

- Okamoto & Beach, 1994, The EMBO Journal — showed cyclin G is a transcriptional target of p53.
- Okamoto et al., 1996, Molecular and Cellular Biology — reported a p53-dependent association between cyclin G and the B′ subunit of PP2A.
- Okamoto et al., 2002, Molecular Cell — cyclin G binds MDM2 and recruits PP2A to dephosphorylate it at T216; cyclin G null cells show hyperphosphorylated MDM2 and elevated p53.
- Fischer, 2017, Oncogene — census of p53 target genes, placing CCNG1 among the consistently induced direct targets.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 63.21 CPM |
| Lines where detected | 50 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 7 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.052× |
| Wild-type minus altered | 1.077× |
| Compounds moving it up in WT lines | 76 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00170 |
| As a percentage | -0.12% |
| FDR, exposure-shuffle null | 0.4597 |
| In TP53-wild-type lines / altered lines | -0.00383 / -0.00041 |
| Verdict | none |
| **Signed into p53-output units** | **none** |

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
