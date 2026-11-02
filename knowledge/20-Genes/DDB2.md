---
symbol: DDB2
type: gene
tier: 1
aliases: [XPE]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: DNA repair
median_line_cpm: 54.26
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DDB2

> [!summary] In one line
> DDB2 is the damage-recognition subunit of the UV-DDB complex and the substrate receptor of a CRL4 ubiquitin ligase, it is a direct p53 target, and it is the gene mutated in xeroderma pigmentosum group E.

## What it is

DDB2 (p48) is the small subunit of UV-DDB, the heterodimer it forms with DDB1 (p127). UV-DDB binds UV photoproducts — cyclobutane pyrimidine dimers and 6-4 photoproducts — and also abasic sites and short mismatches, with the highest affinity of any known damage sensor for the poorly helix-distorting CPD lesion. Crystallography showed how: DDB2's WD40 β-propeller holds the duplex and the damaged bases are flipped out of the helix into a hydrophobic pocket on the propeller face, which is why a lesion that barely deforms DNA can still be read. UV-DDB then hands the lesion to XPC–RAD23B to initiate global-genome nucleotide excision repair.

DDB2 has a second, inseparable job. DDB1 is the adaptor of CUL4A/CUL4B–RBX1, and DDB2 is the substrate receptor of the resulting CRL4^DDB2 ligase, which ubiquitylates XPC, core histones H2A/H3/H4 at the lesion, and DDB2 itself. The histone marks loosen nucleosomes around the damage; the autoubiquitylation drives DDB2's own proteasomal turnover and so times the handoff and terminates the response. CRL4^DDB2 activity is further gated by the COP9 signalosome after damage.

The p53 connection is at the level of expression rather than activity: DDB2 mRNA depends on basal p53 and rises further after damage in a p53-dependent way. This is the accepted explanation for a long-standing species difference — rodent cells lack appreciable UV-DDB activity and repair CPDs poorly in non-transcribed DNA, because they do not express DDB2 the way human cells do. Clinically, biallelic DDB2 loss causes xeroderma pigmentosum group E: the mildest XP complementation group, with late-onset skin cancer and without the neurological degeneration of other groups. Beyond repair, DDB2 has reported roles in oncogene-induced senescence, in CRL4-dependent transcriptional repression, and in ROS control, all on narrower evidence.

## Why it appears in this work

DDB2 is the member of [[p53 program P]] that reports p53 output reaching the repair machinery rather than the arrest arm through [[The p21-DREAM axis]] or the apoptotic effectors. It is a direct target with a wild-type-selective induction, so it serves both as a reporter and as evidence that [[The p53 pathway]] is being engaged as a damage response and not only as a growth-suppressive program.

## What is uncertain

The direct-target status is secure, but what induction means functionally at 24 h is not. DDB2 protein is autoubiquitylated and short-lived at damage sites, so more mRNA does not straightforwardly mean more active UV-DDB; the limiting quantity may be CRL4 assembly or chromatin access rather than transcript abundance. The lesions DDB2 reads best are UV photoproducts, which are not what most compounds in this panel produce, so DDB2 induction here should be read as a p53 signature and not as evidence of relevant repair capacity. DDB2 also responds to inputs other than p53, and in lines with high basal replication stress its baseline may be set by those. The CRL4^DDB2-as-repressor and ROS results come from fewer systems than the repair biochemistry and should carry less weight.

## References

- Hwang et al., 1999, PNAS — showed DDB2/p48 expression depends on basal p53 and is further induced after DNA damage p53-dependently, accounting for the human/rodent difference in UV-DDB activity.
- Scrima et al., 2008, Cell — structural basis of UV DNA-damage recognition by the DDB1–DDB2 complex, with the lesion flipped into a pocket on the DDB2 β-propeller.
- Groisman et al., 2003, Cell — showed the ubiquitin ligase activity of the DDB2 and CSA complexes is differentially regulated by the COP9 signalosome in response to DNA damage.
- Sugasawa et al., 2005, Cell — UV-induced ubiquitylation of XPC mediated by the UV-DDB–ubiquitin ligase complex.
- Rapić-Otrin et al., 2003, Human Molecular Genetics — established that true xeroderma pigmentosum group E patients have a defective DDB2 component of the UV-DDB complex.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 54.26 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 10 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.139× |
| Wild-type minus altered | 1.154× |
| Compounds moving it up in WT lines | 81 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00752 |
| As a percentage | -0.52% |
| FDR, exposure-shuffle null | 0.0405 |
| In TP53-wild-type lines / altered lines | -0.00377 / -0.00980 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.173 raw, 0.028 with 3 PCs removed |

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
