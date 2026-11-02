---
type: literature
tags: [literature, p53]
status: current
---

# Key papers — p53

The p53 literature this vault leans on. The field is enormous; this is the subset that bears on how **this**
study defines and measures p53 output.

> [!warning] On citations in this vault
> No PMIDs or DOIs, deliberately — these are papers I am confident exist and showed what is stated. Verify
> before citing one in your own writing.

## The network

| Paper | What it showed |
|---|---|
| **Vogelstein, Lane & Levine, 2000, *Nature*** | "Surfing the p53 network" — the review that set the standard picture most people carry. |
| **Vousden & Prives, 2009, *Cell*** | "Blinded by the light" — p53's output arms and how the choice between arrest, senescence and death gets made. The best single entry point. |
| **Haupt et al., 1997, *Nature*** and **Kubbutat et al., 1997, *Nature*** | MDM2 as the E3 ligase that ubiquitinates p53 and sends it for degradation. The basis of the feedback loop that makes [[MDM2]] ambiguous as a readout. |

## The targets, and which ones are real

| Paper | What it showed |
|---|---|
| **el-Deiry et al., 1993, *Cell*** | WAF1/[[CDKN1A]] as a p53-inducible gene and the mediator of p53 growth suppression. The p53 response elements characterised here defined what one looks like. |
| **Harper et al., 1993, *Cell*** | p21/Cip1 as a potent inhibitor of G1 cyclin-dependent kinases — the other half of the 1993 pair. |
| **Fischer, 2017, *Oncogene*** | A meta-analysis across p53 binding and expression datasets asking which genes are *genuinely direct* p53 targets. The most useful paper for anyone building a p53 signature, and the source of the argument that p53 does not directly repress genes. |
| **Engeland, 2018, *Cell Death & Differentiation*** | p53-dependent repression through p21, DREAM and RB — the clearest statement of the indirect repression route. See [[The p21-DREAM axis]]. |

The Fischer and Engeland pair are the reason this vault treats the repression arm of [[p53 program P]] as a
second-order consequence with a smaller amplitude, rather than as a symmetric half of the programme.

## Mutant p53 and how it fails

| Paper | What it showed |
|---|---|
| **Olivier, Hollstein & Hainaut, 2010, *Cold Spring Harbor Perspectives in Biology*** | The TP53 mutation spectrum in human cancer — hotspots, their distribution, and their functional classes. The background for this study's per-variant annotation. |
| **Brosh & Rotter, 2009, *Nature Reviews Cancer*** | Gain-of-function and dominant-negative activities of mutant p53 — why "TP53-mutated" is not one phenotype. |

The IARC/NCI **TP53 database** (Hainaut and colleagues, maintained over many years) is the source of the
per-variant transactivation classes used in `tables/tp53db_variant_function.csv`. It is a curated resource
rather than a paper, and it is the right thing to cite for a specific variant's reported function.

## Why these cell lines are mostly p53-dead

The routes other than TP53 mutation — CDKN2A/ARF loss, MDM2 and MDM4 amplification, PPM1D, ATM lesions — are
standard cancer-genetics findings rather than the contribution of any one paper. The [[CDKN2A]]–ARF–MDM2 axis
in particular is textbook. What is specific to this study is the measurement of **how much** p53 output each
line retains, which is [[Per-line p53 function]] and uses no literature at all: it is anchored on the lines
that have no intact TP53 allele.

## The methodological papers worth knowing

- **DoRothEA** (Garcia-Alonso et al., 2019, *Genome Research*) and **CollecTRI** (Müller-Dott et al., 2023,
  *Nucleic Acids Research*) — the regulon collections used for [[Transcription factor activity inference]].
  Both are literature-assembled and biased toward well-studied factors, which is the limitation that note
  dwells on.
- **Benjamini & Hochberg, 1995, *JRSS-B*** — the FDR procedure whose behaviour under an inflated null is the
  subject of [[FDR calibration and the inflated null]]. Worth reading once properly: BH draws its power from
  the *mass* of signal, which is exactly why a 4.4× inflated statistic lets 4,500 genes through.

## Links

- [[The p53 pathway]] — the concept note these papers support
- [[p53 program P]] · [[The p21-DREAM axis]] · [[p53 nullification in cancer cell lines]]
- [[Key papers — MG53]]
