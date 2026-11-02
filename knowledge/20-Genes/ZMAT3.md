---
symbol: ZMAT3
type: gene
tier: 1
aliases: [WIG1, PAG608]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: negative feedback
median_line_cpm: 28.87
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ZMAT3

> [!summary] In one line
> ZMAT3 is a zinc-finger RNA-binding protein, induced by p53 about as reliably as any gene in the pathway, which acts on its targets' splicing and stability rather than on their transcription.

## What it is

ZMAT3 — zinc finger matrin-type 3, known in the older literature as Wig-1 and PAG608 — was found in the 1990s as a p53-inducible gene encoding a nuclear protein with three matrin-type zinc fingers. Those fingers bind RNA, including double-stranded RNA, and everything ZMAT3 is thought to do is post-transcriptional.

Two mechanistic accounts exist, and they are not the same claim. The earlier one is stability: Wig-1 was reported to bind AU-rich elements in 3′ untranslated regions and to stabilise its targets, p53 mRNA itself among them, which would make it a positive-feedback element in the pathway. The later and better-supported account is splicing. *In vivo* RNAi and CRISPR screens in Kras-driven mouse lung and liver tumours converged on Zmat3 as a tumour suppressor acting downstream of p53; ZMAT3 was then shown to bind thousands of pre-mRNAs, mostly at intronic uridine-rich sequences, and to change exon inclusion in ways frequently coupled to nonsense-mediated decay. Among the transcripts it acts on are the p53 inhibitors [[MDM2]] and [[MDM4]]. Independent work in colorectal cells found CD44 its strongest alternatively spliced target: losing ZMAT3 shifts CD44 toward the oncogenic variant isoforms, and knocking those variants down rescues the growth advantage ZMAT3 loss confers.

## Why it appears in this work

ZMAT3 is a curated p53 effector in the induction arm of [[p53 program P]], and among the better-behaved members of that arm: it moves in one direction across the reference compounds rather than going each way, unlike many of its neighbours in the signature. That makes it one of the more trustworthy single-gene readouts that p53 is transcriptionally engaged in a given well, in the same tier as [[CDKN1A]] and [[MDM2]] — and unlike MDM2 it is not simultaneously the brake, so it is easier to interpret. Its membership also helps justify treating the programme as a p53 readout rather than a generic stress readout, since ZMAT3 has few known inputs other than p53.

## What is uncertain

The vault's curated table files ZMAT3 under negative feedback, and that label does not sit comfortably with either mechanistic account: stabilising p53 mRNA would be positive feedback, and shifting MDM2 and MDM4 transcripts toward nonsense-mediated decay would also relieve inhibition of p53. Read the label as inherited annotation, not a conclusion, and do not infer the sign of ZMAT3's effect on p53 from it.

The two mechanisms are themselves unreconciled — different binding preferences, different consequences — and the later papers treat the AU-rich-element proposal as prior work, not something they confirmed. The tumour-suppressor genetics are strong but come from particular mouse models and cell lines. And in a transcript-level dataset ZMAT3 mRNA reports that p53 fired, not that ZMAT3 did anything to its RNA targets; the splicing output would need isoform-level quantification that 3′-biased single-cell data cannot supply.

## References

- Varmeh-Ziaie et al., 1997, *Oncogene* — identified Wig-1 as a p53-induced zinc-finger gene.
- Hellborg et al., 2001, *Oncogene* — characterised human Wig-1 as a p53-induced, growth-inhibitory nuclear protein with three zinc fingers.
- Méndez-Vidal et al., 2002, *Nucleic Acids Research* — showed Wig-1 binds double-stranded RNA with high affinity, the first zinc finger being required.
- Vilborg et al., 2009, *PNAS* — reported that Wig-1 binds an AU-rich element in the p53 3′ UTR and stabilises p53 mRNA.
- Bieging-Rolett et al., 2020, *Molecular Cell* — screens identified Zmat3 as a p53-dependent tumour suppressor and showed it regulates splicing, including of MDM2 and MDM4, with coupling to nonsense-mediated decay.
- Muys et al., 2021, *Genes & Development* — showed ZMAT3 binds intronic uridine-rich regions and suppresses inclusion of oncogenic CD44 variant exons, defining a p53–ZMAT3–CD44 axis.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 28.87 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 26 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.202× |
| Wild-type minus altered | 1.163× |
| Compounds moving it up in WT lines | 90 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00116 |
| As a percentage | +0.08% |
| FDR, exposure-shuffle null | 0.7745 |
| In TP53-wild-type lines / altered lines | 0.00043 / 0.00164 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.442 raw, -0.038 with 3 PCs removed |

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
