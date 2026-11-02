---
symbol: STK11
type: gene
tier: 1
aliases: [LKB1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# STK11

> [!summary] In one line
> STK11 encodes LKB1, the master upstream kinase that activates AMPK and twelve related kinases, and the tumour suppressor whose germline loss causes Peutz-Jeghers syndrome.

## What it is

LKB1 is a serine/threonine kinase that does not work alone: it is an obligate heterotrimer with the pseudokinase STRADα and the scaffold MO25/CAB39, which together activate it and set its localisation. In that form it is largely constitutively active — the always-on upstream element, the regulation sitting in its substrates.

LKB1 phosphorylates the activation-loop threonine of AMPKα, and the equivalent residue in twelve other AMPK-family kinases: the salt-inducible kinases, the MARK/PAR-1 polarity kinases, the BRSKs, the NUAKs and SNRK. The AMPK arm is the best known: as AMP rises relative to ATP, AMPK becomes sensitive to LKB1 phosphorylation, and its activation shuts down anabolic ATP consumption and restrains mTORC1 via TSC2 and raptor. Cells lacking LKB1 fail to activate AMPK under energy stress and lose the associated checkpoint — the core of LKB1's metabolic tumour-suppressor account. The MARK and SIK arms carry polarity and CRTC/HDAC-dependent transcriptional functions.

Germline loss-of-function causes Peutz-Jeghers syndrome: hamartomatous gastrointestinal polyposis, mucocutaneous pigmentation and markedly elevated cancer risk. Somatically it is among the more frequently inactivated genes in lung adenocarcinoma, often co-mutant with KRAS, and in cervical and pancreatic cancers; the STK11/KRAS double-mutant subgroup is immunotherapy-resistant and immune-cold.

## Why it appears in this work

STK11 is here as an upstream, contextual gene, not a p53 target: one of the routes by which p53 output can be lowered in a line that is TP53-wild-type by sequence. The link runs through AMPK, which on energy stress engages a p53-dependent metabolic checkpoint; losing LKB1 removes that input. Several of this panel's nominally wild-type lines carry truncating STK11 alleles — exactly the problem in [[p53 nullification in cancer cell lines]]: a wild-type-versus-altered split defined on TP53 does not make the wild-type group homogeneous. STK11 belongs with [[CDKN2A]], [[MDM4]], [[PPM1D]] and [[ATM]] in that annotation layer rather than with [[p53 program P]].

## What is uncertain

The attenuation argument is narrower than it appears. The AMPK-to-p53 checkpoint was characterised under energy stress; most compounds here act through DNA damage, replication stress or MDM2 inhibition, and whether LKB1 loss blunts p53's response to those is not established. LKB1 loss plausibly lowers basal and metabolic-stress p53 tone; it has not been shown to damp the responses measured here.

Whether AMPK is the relevant effector for LKB1's tumour suppression is contested: LKB1 has twelve other substrates, in several models the SIK branch accounts for more of the phenotype, and AMPK itself can support or restrain tumour growth by context. "LKB1 loss removes a tumour-suppressive AMPK signal" simplifies an unsettled question. The p53 step is also open: AMPK-dependent p53 serine-15 phosphorylation is reported, but its contribution relative to ATM and ATR at endogenous levels is not well quantified.

One measurement caveat: STK11 transcript level is an unreliable proxy for LKB1 function. Truncating alleles may or may not reduce mRNA through nonsense-mediated decay, and a kinase-impairing missense allele leaves the transcript intact, so an mRNA panel cannot distinguish an LKB1-null line from a functional one.

## References

- Hemminki et al., 1998, Nature — identified a serine/threonine kinase gene defective in Peutz-Jeghers syndrome.
- Jenne et al., 1998, Nature Genetics — independently showed Peutz-Jeghers syndrome is caused by mutations in this novel serine/threonine kinase.
- Lizcano et al., 2004, EMBO Journal — LKB1 is a master kinase activating thirteen AMPK-subfamily kinases, including MARK/PAR-1.
- Shaw et al., 2004, PNAS — LKB1 directly activates AMPK and is required for the apoptotic response to energy stress.
- Jones et al., 2005, Molecular Cell — AMPK activation induces a p53-dependent metabolic checkpoint.
- Skoulidis et al., 2018, Cancer Discovery — STK11/LKB1 loss associates with resistance to PD-1 blockade in KRAS-mutant lung adenocarcinoma.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00350 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.2827 |
| In TP53-wild-type lines / altered lines | -0.00277 / 0.00717 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.435 raw, 0.047 with 3 PCs removed |

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
