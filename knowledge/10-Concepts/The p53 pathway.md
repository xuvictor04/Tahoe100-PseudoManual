---
type: concept
tags: [concept, p53]
status: current
---

# The p53 pathway

> [!summary] In one line
> A stress-activated transcription factor that, when it works, turns a damage signal into arrest, repair or
> death — and that is broken in four fifths of the cell lines in this dataset.

## The part this study depends on

p53 (gene [[TP53]]) is a tetrameric transcription factor that binds response elements in the promoters of
several hundred genes. In an unstressed cell it is kept at a low level by continuous ubiquitination from
[[MDM2]] and degradation by the proteasome, with [[MDM4]] (MDMX) restraining its transactivation in parallel.
Stress interrupts that.

**Activation.** DNA double-strand breaks activate [[ATM]], which with [[CHEK2]] phosphorylates p53 and MDM2
and breaks the pair apart; replication stress runs the same logic through ATR and CHK1. Oncogenic signalling
induces p14ARF from the [[CDKN2A]] locus, which sequesters MDM2. Ribosomal stress releases free ribosomal
proteins that bind MDM2 directly. The result in each case is p53 that is stabilised, modified, and
transcriptionally competent.

**Output.** The programme splits by what the cell is asked to do:

| Arm | Genes | Effect |
|---|---|---|
| Cell-cycle arrest | [[CDKN1A]] (p21), [[GADD45A]], [[BTG2]], [[PLK3]], [[CCNG1]] | G1 and G2 arrest |
| Apoptosis | [[BAX]], [[PMAIP1]] (NOXA), [[BBC3]] (PUMA), [[TNFRSF10B]] (DR5), [[AEN]], [[TP53INP1]] | mitochondrial and receptor-mediated death |
| DNA repair | [[DDB2]], [[XPC]], [[POLH]], [[RRM2B]] | nucleotide-excision repair, lesion bypass, dNTP supply |
| Metabolism and redox | [[TIGAR]], [[SESN1]], [[FDXR]], [[TP53I3]], [[ACER2]] | glycolytic and ROS control |
| Negative feedback | [[MDM2]], [[PPM1D]] (WIP1), [[ZMAT3]] | shuts the response down again |

**Repression.** p53 also lowers transcription of a large set of cell-cycle genes, and it mostly does so
*indirectly*: p21 inhibits CDK activity, which keeps the DREAM complex assembled on cell-cycle promoters.
That matters for reading any per-gene table, because the "repressed" arm is a second-order consequence with a
different sign and a smaller amplitude. See [[The p21-DREAM axis]].

**Feedback is the reason MDM2 is confusing.** p53 induces MDM2 transcriptionally, and MDM2 protein then
degrades p53. So MDM2's mRNA is a p53 *readout* while MDM2's protein is a p53 *regulator*, and which one you
mean changes the direction of every inference. [[MDM2 and MG53]] turns on exactly this point.

## How it is broken in these cells

In cancer, p53 is disabled either by mutating TP53 or by disabling the route to it. Both appear here:

- **33 of the 50 lines carry a TP53 alteration.** The common missense hotspots (R175H, R248W, R273H, R282W)
  sit in the DNA-binding domain and produce protein that is stable but cannot transactivate; some are
  additionally dominant-negative over any remaining wild-type allele, and some are argued to have
  gain-of-function activities unrelated to wild-type p53.
- **Ten lines have no intact allele at all** — truncating, splice-disrupted, or whole-gene deletion. Those
  lines cannot mount a p53 response, which is what makes them usable as a knockout-like control arm; see
  [[The measurement with controls]].
- **Among the 17 genotype-wild-type lines, p53 is still often damped** by CDKN2A/ARF loss, MDM4 or MDM2
  amplification, PPM1D, or ATM lesions. Only 11 of the 50 lines are functionally responsive.

The practical consequence for every test in this study: the effective sample for anything that needs working
p53 is **11 to 17 cell lines**, not 50 and not the 53,331 line × exposure rows. See
[[p53 nullification in cancer cell lines]] and [[Per-line p53 function]].

## What "p53 activity" means operationally here

Not the protein, which is never measured. It means the mRNA output of a gene set:

- the **curated** route — a 21-gene p53-activity panel plus the classic effectors it omits, 29 genes in all;
- the **data-defined** route — [[p53 program P]], 180 induction-arm and 15 repression-arm genes selected from
  this dataset using the TP53 labels, which makes some of its columns circular. See
  [[Cross-fitting and circularity]].

Both are used throughout, deliberately, because they fail in different ways.

## Links

- [[p53 program P]] · [[The p21-DREAM axis]] · [[Signing genes by p53 direction]]
- [[p53 nullification in cancer cell lines]] · [[Per-line p53 function]]
- [[Downstream of MG53]] · [[The measurement with controls]] · [[MDM2 and MG53]]
- [[Genes — Map of Content]] for every gene note, grouped by what p53 does to it

## References

- el-Deiry et al., 1993, *Cell* — WAF1/CDKN1A as the p53-induced mediator of arrest.
- Vogelstein, Lane & Levine, 2000, *Nature* — the review that set the standard picture of the network.
- Haupt et al., 1997, *Nature* and Kubbutat et al., 1997, *Nature* — MDM2 as the ligase that degrades p53.
- Vousden & Prives, 2009, *Cell* — p53's output arms and how the choice between them is made.
- Fischer, 2017, *Oncogene* — a meta-analysis of which genes are genuinely direct p53 targets, and the case
  that most "p53-repressed" genes are indirect via p21-DREAM.
- Engeland, 2018, *Cell Death & Differentiation* — p53-dependent repression through DREAM and RB.
