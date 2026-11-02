---
symbol: CDKN1A
type: gene
tier: 1
aliases: [p21, WAF1, CIP1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: cell-cycle arrest
median_line_cpm: 56.41
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CDKN1A

> [!summary] In one line
> CDKN1A encodes p21, the cyclin-dependent kinase inhibitor through which p53 converts transcription into a stalled cell cycle, and the most reliable mRNA readout that p53 is active.

## What it is

p21 (p21^WAF1/CIP1^) is a small, largely disordered CDK inhibitor. Its N-terminal domain grips the cyclin groove and the CDK active site, inhibiting cyclin E–CDK2 and cyclin A–CDK2 and, at higher stoichiometry, cyclin D–CDK4/6; at low levels it instead acts as an assembly factor for cyclin D–CDK4, which is why its dose matters as much as its presence. Losing CDK2 activity leaves RB hypophosphorylated and E2F targets off, producing G1/S arrest. A separate C-terminal PIP box binds PCNA and blocks processive replication, giving p21 a direct role at the fork as well as at the kinase.

The gene is the archetypal direct p53 target: two canonical p53 response elements sit roughly 1.3 kb and 2.3 kb upstream, and they were the elements that established what a p53 response element looks like. p21 is also the executor of the repression arm of the p53 program — sustained CDK inhibition keeps the DREAM complex assembled on CDE/CHR promoters, so a large block of cell-cycle genes falls without p53 ever binding them. See [[The p21-DREAM axis]].

Regulation runs in both directions. CDKN1A is induced by many p53-independent inputs — TGF-β/SMAD, BRCA1, Sp1/AP-2, differentiation signals, HDAC inhibitors. The protein is short-lived, degraded by CRL4–CDT2 and SCF–SKP2, and AKT phosphorylation at T145 can move it to the cytoplasm, where it restrains apoptotic signalling instead of the cell cycle. That cytoplasmic activity is the origin of the substantial literature arguing p21 is sometimes oncogenic. Notably, CDKN1A is almost never mutated in human cancer; the pathway is bypassed upstream rather than at p21.

## Why it appears in this work

p21 is the anchor of the p53 readout. It is highly expressed, cleanly induced, and induced wild-type-selectively, so it sets the scale against which other members of [[p53 program P]] are judged — if a 24 h single-cell measurement in [[Tahoe-100M]] detects p53 activity anywhere, it detects it here. It also carries two meanings at once: its own arrest function, and, through [[The p21-DREAM axis]], the indirect repression of the cell-cycle genes that make up the program's down arm. Reading p21 induction as "p53 is engaged" is the least contestable inference available in this study.

## What is uncertain

p21 mRNA reports p53 transcriptional activity, not outcome. Arrest, senescence, apoptosis resistance, or nothing follows depending on context, and the induction alone cannot distinguish them. Because the p53-independent inputs are real and strong, p21 up is necessary but not sufficient evidence that p53 is on — residual induction in a TP53-altered line more likely reflects those other inputs than residual p53. The cytoplasmic anti-apoptotic role means more p21 is not monotonically more tumour suppression. And p21 expression is pulsatile and bimodal at single-cell resolution; a pooled 24 h average smooths over pulse structure that is part of how the signal actually works.

## References

- el-Deiry et al., 1993, Cell — identified WAF1/CDKN1A as a p53-inducible gene and candidate mediator of p53 growth suppression.
- Harper et al., 1993, Cell — characterised p21/Cip1 as a potent inhibitor of G1 cyclin-dependent kinases.
- Waldman, Kinzler & Vogelstein, 1995, Cancer Research — showed p21 is required for p53-mediated G1 arrest in human cancer cells.
- Brugarolas et al., 1995, Nature — radiation-induced cell-cycle arrest is compromised in p21-deficient cells.
- Abbas & Dutta, 2009, Nature Reviews Cancer — review of p21's multiple, partly opposing activities in cancer.
- Engeland, 2018, Cell Death & Differentiation — set out the p53–p21–DREAM route for indirect transcriptional repression.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 56.41 CPM |
| Lines where detected | 47 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 29 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.117× |
| Wild-type minus altered | 1.161× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01040 |
| As a percentage | +0.72% |
| FDR, exposure-shuffle null | 0.0089 |
| In TP53-wild-type lines / altered lines | 0.00796 / 0.01205 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.418 raw, 0.174 with 3 PCs removed |

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
