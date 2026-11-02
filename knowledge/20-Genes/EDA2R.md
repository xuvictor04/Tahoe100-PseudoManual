---
symbol: EDA2R
type: gene
tier: 1
aliases: [XEDAR]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 1.08
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# EDA2R

> [!summary] In one line
> EDA2R, also called XEDAR or TNFRSF27, is an X-linked TNF-receptor-family receptor for the EDA-A2 isoform of ectodysplasin A, one of the most steeply p53-inducible transcripts in the genome, and an emerging marker of muscle wasting and ageing.

## What it is

EDA2R is a membrane receptor of the TNF receptor superfamily, encoded on the X chromosome. It is the receptor for EDA-A2, one of two splice isoforms of ectodysplasin A; a two-amino-acid difference in the ligand determines whether it binds EDAR (EDA-A1) or EDA2R (EDA-A2), one of the cleanest examples of a splice-level switch between two receptors. Unlike most TNFRSF members with cytotoxic activity, EDA2R has no death domain. It couples instead to NF-κB and JNK signalling, and in overexpression systems has been reported to drive caspase-dependent apoptosis. Its developmental role is unexpectedly dispensable: loss of EDAR or of ectodysplasin itself causes hypohidrotic ectodermal dysplasia, but Eda2r-null mice have essentially normal hair, teeth and glands.

What EDA2R is actually known for now is p53. It was identified by cross-referencing p53-introduced cells against tumour tissue, and p53 drives it through two response elements in intron 1 — so this is a direct target, not an inferred one. In colorectal cancer the gene is silenced by promoter hypermethylation at high frequency, and loss of it increases cell adhesion and spreading and confers resistance to p53-induced apoptosis, which is the basis of the proposal that it mediates a p53-regulated anoikis pathway. Independent work confirmed p53-dependent transactivation across several cell types and tissues in vivo, including during chemotherapy-induced hair loss, though EDA2R is not required for that hair loss.

A separate literature has grown recently. EDA2R is among the most consistently age-upregulated transcripts across human and animal tissues, and it is elevated in denervated muscle, cancer cachexia and muscular dystrophy. The mechanism is worked out best in cachexia: EDA-A2 acting on EDA2R activates NIK and the non-canonical NF-κB pathway to atrophy myotubes, tumour-derived oncostatin M raises muscle EDA2R, and deleting either EDA2R or muscle NIK protects tumour-bearing mice from losing muscle mass. The extension of that account to ordinary ageing muscle is so far mostly associational.

## Why it appears in this work

EDA2R is a high-dynamic-range reporter for [[p53 program P]]. Its baseline in most cancer lines is very low and its p53-driven induction is large, so its fold-change is informative even where absolute counts are small — the opposite trade-off to [[CDKN1A]], and a useful complement to it. Its second life as a muscle-wasting gene is a curious adjacency to [[MG53 (TRIM72)]]'s muscle biology, but adjacency is all it is: here EDA2R is being read as a p53 reporter in pooled cancer lines, not as muscle physiology.

## What is uncertain

The direct-versus-indirect question is settled for the transcription, but whether the protein does anything in these cells is genuinely open: no ligand is supplied in this experiment, EDA-A2 is not appreciably expressed in most cancer lines, and the apoptosis-inducing activity rests largely on overexpression. Induction here may be transcription without signalling. The receptor biology is thin overall — far thinner than the p53-target literature that cites it. The low baseline that makes the fold-change large also makes single-cell detection sparse and ratios unstable. Being X-linked, its dosage may vary with donor sex and X-inactivation state across the pooled lines, a source of between-line variance unrelated to p53. The cachexia work is mouse genetics in muscle and says nothing about these lines; the ageing arm of that literature is young and largely associational.

## References

- Yan et al., 2000, Science — identified XEDAR/EDA2R as the receptor for the EDA-A2 isoform and showed a two-amino-acid switch in ectodysplasin selects between the two receptors.
- Tanikawa et al., 2009, Oncogene — identified XEDAR as a p53 target driven by two response elements in intron 1, frequently hypermethylated in colorectal cancer, and proposed it mediates p53-regulated anoikis.
- Brosh et al., 2010, FEBS Letters — showed p53-dependent transactivation of EDA2R across cell types and tissues, including in chemotherapy-induced hair loss, which nonetheless does not require EDA2R.
- Bilgic et al., 2023, Nature — showed EDA2R–NIK signalling drives muscle atrophy in cancer cachexia, with loss of EDA2R or of muscle NIK protecting tumour-bearing mice.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 1.08 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 57 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.073× |
| Wild-type minus altered | 1.183× |
| Compounds moving it up in WT lines | 53 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00513 |
| As a percentage | +0.36% |
| FDR, exposure-shuffle null | 0.5826 |
| In TP53-wild-type lines / altered lines | 0.00128 / 0.00746 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.100 raw, -0.043 with 3 PCs removed |

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
