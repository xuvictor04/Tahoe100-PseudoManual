---
symbol: XPC
type: gene
tier: 1
aliases: [xeroderma pigmentosum C]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: DNA repair
median_line_cpm: 60.01
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# XPC

> [!summary] In one line
> XPC is the sensor that finds bulky DNA lesions anywhere in the genome and starts nucleotide-excision repair there, and it is one of the repair genes p53 induces.

## What it is

Nucleotide-excision repair comes in two flavours that differ only in how the lesion is found. In transcription-coupled repair, a stalled RNA polymerase is the detector. In global-genome repair — the rest of the genome, including the strand nobody is transcribing — the detector is XPC, working as a heterotrimer with RAD23B and centrin-2. XPC does not read the lesion's chemistry; it recognises the single-stranded character of the undamaged strand opposite a helix-distorting adduct, which is why its substrates range from UV photoproducts to bulky chemical adducts. It then recruits TFIIH and hands off to the shared verification and incision machinery.

Because XPC serves only the global-genome branch, losing it gives a distinctive clinical picture: xeroderma pigmentosum group C patients have extreme photosensitivity and hugely raised skin-cancer risk, but usually lack the neurodegeneration seen in groups whose defects also cripple transcription-coupled repair.

Its connection to p53 is transcriptional. XPC mRNA and protein rise after UV damage in a p53-dependent manner, with little induction in p53-deficient cells, and a p53 response element has been mapped to the gene — located, in follow-up work, within the first exon near the translation start rather than in the upstream promoter. [[DDB2]], the other dedicated global-genome sensor, is likewise p53-inducible — the basis for describing p53 as raising global-genome repair capacity as a whole rather than one gene at a time.

## Why it appears in this work

XPC is a curated p53 effector in the induction arm of [[p53 program P]], sitting with [[DDB2]], [[POLH]] and [[RRM2B]] in the DNA-repair group of [[The p53 pathway]]. Its presence shapes how the programme reads: the signature is not only arrest and apoptosis genes, and a rise in it is consistent with p53 attempting repair rather than only elimination. In a panel dominated by genotoxic compounds that distinction is worth keeping explicit, because the same drug that activates p53 also makes the lesions XPC is induced to clear.

## What is uncertain

The p53-dependence of XPC induction was established largely in UV-irradiated fibroblast systems, and how far it carries to the chemical classes in this panel is not something that work addressed. The induction is modest even where it is clean, and in this dataset XPC's direction is mixed across the reference compounds — it is in the induction arm on balance, not because it reliably goes up. Whether the mapped exon-1 element is the operative one in all contexts is unresolved.

More fundamentally, XPC mRNA is a poor proxy for repair capacity. XPC acts stoichiometrically as a sensor, its protein is regulated by damage-induced ubiquitination, and DDB2 modulates its recruitment — so a change in transcript need not become a change in lesion clearance. Treat XPC here as a reporter that p53 engaged its repair arm, not as a measure of how much repair happened.

## References

- Sugasawa et al., 1998, *Molecular Cell* — identified the XPC complex as the initiator of global-genome nucleotide-excision repair.
- Araki et al., 2001, *Journal of Biological Chemistry* — identified centrin-2 as the third subunit of the XPC–RAD23B complex.
- Adimoolam & Ford, 2002, *PNAS* — showed XPC mRNA and protein are induced after UV in a p53-dependent manner, and reported a putative p53 response element upstream of the transcription start site.
- Hastak et al., 2012, *Genes & Cancer* — mapped p53 binding at the XPC locus to the first exon at the translation start, and did not reproduce binding at the earlier upstream element in cells.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 60.01 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 19 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.088× |
| Wild-type minus altered | 1.122× |
| Compounds moving it up in WT lines | 56 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00044 |
| As a percentage | +0.03% |
| FDR, exposure-shuffle null | 0.9060 |
| In TP53-wild-type lines / altered lines | 0.00351 / -0.00142 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.291 raw, 0.043 with 3 PCs removed |

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
