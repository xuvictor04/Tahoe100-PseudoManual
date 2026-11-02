---
symbol: CHEK2
type: gene
tier: 1
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CHEK2

> [!summary] In one line
> CHEK2 encodes CHK2, the checkpoint kinase that ATM activates after DNA double-strand breaks and that phosphorylates p53 and the CDC25 phosphatases to enforce arrest.

## What it is

CHK2 is a serine/threonine kinase built from an N-terminal SQ/TQ cluster, a forkhead-associated (FHA) domain and a C-terminal kinase domain. Its activation is the canonical double-strand-break cascade: ATM phosphorylates T68 in the SQ/TQ cluster, the phosphothreonine is read by the FHA domain of a partner molecule so CHK2 transiently dimerises, autophosphorylation in the activation loop follows, and the kinase disperses as an active monomer. That mechanism makes CHK2 a signal amplifier — a localised ATM signal at a break becomes a diffusible, nucleus-wide kinase activity.

Its substrates define two parallel outputs. CHK2 phosphorylates p53 at S20, which sits in the MDM2-binding surface, and the standard model is that this contributes to p53 stabilisation — placing CHK2 upstream of everything in [[The p53 pathway]]. Independently, CHK2 phosphorylates CDC25A, driving its degradation, and CDC25C, promoting 14-3-3 sequestration; either way CDK-activating phosphatase activity falls and the cell cycle halts without any transcription being required. CHK2 also acts on BRCA1, E2F1 and PML. It is the DSB-responsive counterpart to CHK1, which is activated by ATR and handles replication stress; the two are often conflated and should not be.

Clinically, CHEK2 matters mainly through germline variation. The truncating allele 1100delC and other loss-of-function variants confer moderately increased risk of breast cancer and, less strongly, prostate and colorectal cancer. Truncating CHEK2 variants were originally reported in families with a Li-Fraumeni-like presentation, which is where the gene's reputation as a p53-pathway tumour suppressor began.

## Why it appears in this work

CHEK2 sits upstream of p53, not downstream of it, which is the whole reason it belongs in this vault alongside ATM, MDM2 and USP7. Many of the 379 compounds in [[Tahoe-100M]] are genotoxic, and CHK2 is part of the machinery that decides whether a given line converts that damage into p53 transcriptional output at all. It should therefore not be read as a member of [[p53 program P]] — its own transcript is not a strongly p53-inducible one — but as part of the explanation for why two TP53-wild-type lines can differ in how much p53 output an exposure produces.

## What is uncertain

How much p53 activation actually requires CHK2 is contested, and the two best experiments disagree. Chk2-deficient mice are radioresistant with defective p53-mediated transcription, implying CHK2 is important; somatic knockout of CHEK2 in human colorectal cancer cells left p53 responses intact, implying it is not. The S20 phosphorylation model is drawn in nearly every pathway diagram, but whether that site is necessary for stabilisation is disputed, and ATM phosphorylates p53 at S15 without CHK2's help. The germline story has also shifted: the Li-Fraumeni attribution has largely not held up, CHEK2 is now classed as a moderate-penetrance gene, and the effect of many missense variants remains uncertain. For this study the practical caveat is that CHK2 activity is set by phosphorylation and dimerisation, so an mRNA level is a weak proxy for how much of the kinase is actually working.

## References

- Matsuoka, Huang & Elledge, 1998, Science — linked ATM to cell-cycle regulation through the CHK2 kinase.
- Bell et al., 1999, Science — reported heterozygous germline CHEK2 mutations in Li-Fraumeni syndrome.
- Hirao et al., 2000, Science — DNA-damage-induced activation of p53 by the checkpoint kinase Chk2.
- Takai et al., 2002, The EMBO Journal — Chk2-deficient mice are radioresistant and show defective p53-mediated transcription.
- Jallepalli et al., 2003, Journal of Biological Chemistry — CHEK2 knockout in human cancer cells left p53 responses intact, the main counterweight to the mouse result.
- Meijers-Heijboer et al., 2002, Nature Genetics — established CHEK2*1100delC as a low-penetrance breast cancer susceptibility allele.
- Zannini, Delia & Buscemi, 2014, Journal of Molecular Cell Biology — review of CHK2 in the DNA damage response.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00131 |
| As a percentage | -0.09% |
| FDR, exposure-shuffle null | 0.7114 |
| In TP53-wild-type lines / altered lines | -0.00033 / -0.00191 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.061 raw, -0.188 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
