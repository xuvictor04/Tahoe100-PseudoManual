---
symbol: GDF15
type: gene
tier: 1
aliases: [MIC-1, NAG-1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: other (secreted)
median_line_cpm: 22.18
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# GDF15

> [!summary] In one line
> GDF15 encodes a secreted, divergent TGF-β superfamily cytokine that signals through a single receptor in the hindbrain to suppress appetite, and that p53 induces — along with almost every other kind of cellular stress.

## What it is

GDF15 has an unusual number of names — MIC-1, NAG-1, PLAB, PTGF-β, PDF — because several groups found it independently in unrelated screens, itself a clue to how promiscuously it is induced. It is a distant TGF-β superfamily member, secreted as a disulfide-linked dimer after pro-protein cleavage. Basal expression is low in most tissues and high in placenta; levels rise steeply with injury, inflammation, mitochondrial dysfunction, renal and cardiac disease, ageing and cancer. It is among the strongest single-protein predictors of all-cause mortality — a general distress signal, not a disease marker.

Its receptor was a long-standing puzzle, resolved in 2017 when four groups independently identified GFRAL, an orphan GDNF-family receptor that uses RET as co-receptor and is expressed essentially only in the area postrema and nucleus tractus solitarius. That anatomy explains the physiology: GDF15 acts on brainstem circuitry for nausea and aversion, suppressing food intake and causing weight loss — now understood as a principal effector arm of cancer cachexia. Metformin's weight effect runs substantially through GDF15, and GDF15 is linked to nausea and vomiting of pregnancy.

Its transcriptional control is where this gene earns its caution. GDF15 was identified as a p53 target gene and proposed as a serum biomarker of p53 pathway activation. But it is also induced strongly by the ATF4/CHOP integrated stress response, by mitochondrial dysfunction, by inflammatory cytokines, and — the original NAG-1 finding — by NSAIDs independent of cyclooxygenase. Several largely independent stress pathways converge on this one promoter.

## Why it appears in this work

GDF15 is a curated p53 effector in the induction arm of [[p53 program P]], and the one member of that set whose product leaves the cell: its induction means the p53 response is being broadcast rather than kept internal, a different output from arrest or apoptosis. It is also the set's most useful stress test for how much of program P is really p53. A panel of 379 drugs at [[Tahoe-100M]] scale contains many compounds that stress mitochondria, the ribosome and the ER without touching p53, and those should induce GDF15 regardless of genotype — so a gene whose direction across perturbations is unstable is behaving as a multiply-driven promoter should.

## What is uncertain

Whether p53 acts at the GDF15 promoter directly or through the stress machinery p53 activation itself engages is not settled in a way I would rely on: a p53 response element has been reported here, but the ATF4 route is at least as strong in many systems, and in some contexts GDF15 is induced with no p53 requirement at all. So "p53 target" is true but far from exclusive, and GDF15 induction is weak evidence that p53 specifically is on. Its direction of effect in cancer is genuinely contested, not merely unresolved: the NAG-1 literature describes it as pro-apoptotic and antitumorigenic, the cachexia literature as a driver of poor outcome; the resolution is probably that early cell-autonomous and late systemic effects differ. Its expression here is low enough that per-cell measurement is noisy, limiting what any single-cell correlation can establish.

## References

- Tan et al., 2000, PNAS — identified PTGF-β/GDF15 as a p53 target gene inhibiting tumour cell growth through TGF-β signalling.
- Baek et al., 2001, Molecular Pharmacology — cyclooxygenase inhibitors induce this TGF-β superfamily member (NAG-1), independent of COX, with proapoptotic and antitumorigenic activity.
- Yang et al., 2003, Molecular Cancer Therapeutics — proposed MIC-1/GDF15 as a biomarker of p53 pathway activation.
- Mullican et al., 2017, Nature Medicine, and Hsu et al., 2017, Nature — identified GFRAL as the GDF15 receptor and localised it to the area postrema and nucleus tractus solitarius.
- Coll et al., 2020, Nature — showed GDF15 mediates the effects of metformin on body weight and energy balance.
- Lockhart et al., 2020, Endocrine Reviews — review framing GDF15 as a hormone conveying somatic distress to the brain.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 22.18 CPM |
| Lines where detected | 47 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 96 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.075× |
| Wild-type minus altered | 1.125× |
| Compounds moving it up in WT lines | 58 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00154 |
| As a percentage | +0.11% |
| FDR, exposure-shuffle null | 0.8388 |
| In TP53-wild-type lines / altered lines | -0.00422 / 0.00544 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.159 raw, 0.035 with 3 PCs removed |

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
