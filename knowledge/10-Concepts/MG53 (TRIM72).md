---
type: concept
tags: [concept, mg53, trim72]
status: current
---

# MG53 (TRIM72)

> [!summary] In one line
> A striated-muscle TRIM-family E3 ubiquitin ligase that nucleates repair of torn plasma membrane, and the
> gene this whole study treats as its exposure variable.

## What the protein does

MG53 — "mitsugumin 53", gene symbol **TRIM72** — is a tripartite-motif protein expressed almost exclusively
in skeletal and cardiac muscle. Its domains are the TRIM signature: a RING finger (E3 ubiquitin ligase
activity), a B-box, a coiled-coil that mediates oligomerisation, and a C-terminal SPRY domain.

Its best-established job is **acute membrane repair**. When the sarcolemma tears, MG53 senses the resulting
change in redox environment, oligomerises, and nucleates a repair patch by recruiting intracellular vesicles
to the wound, working with caveolin-3, dysferlin and PTRF/cavin-1. The sensing step is oxidation-dependent —
entry of extracellular oxidants, rather than calcium, is what triggers assembly, which distinguishes it from
the calcium-triggered dysferlin pathway. `Trim72`-null mice develop progressive myopathy and are markedly
more vulnerable to ischaemia-reperfusion injury; delivering recombinant MG53 protein protects muscle, heart
and several other tissues in injury models, which is why it has been pursued as a therapeutic protein.

Two further roles matter for anyone reading an expression dataset:

- **A negative regulator of insulin signalling.** Its RING domain ubiquitinates the insulin receptor and
  IRS1, and sustained overexpression produces insulin resistance and metabolic syndrome in mice. Whether
  *circulating* MG53 does this in humans has been actively disputed, with groups reaching opposite
  conclusions about whether blood MG53 causes insulin resistance or merely marks muscle damage.
- **A brake on myogenesis.** It restrains myoblast differentiation, so its own expression is entangled with
  the muscle differentiation programme that produces it.

## Why it is the hard half of this study

Everything above happens in muscle, and at the level of protein, localisation and ubiquitination. This study
measures **mRNA, in cancer cell lines, at one time point**. That mismatch is the central limitation and it is
worth stating plainly rather than burying:

- TRIM72 is a muscle gene, and the 50 lines here are not muscle. It sits at a median of 5.89 CPM with 12.4%
  of profiles at zero — trace expression. See [[Why MG53 is hard to measure here]].
- The transcription factors that drive TRIM72 in its native tissue — the MyoD/myogenin family, MEF2, SRF —
  are silent or absent in this panel, which is why no transcription-factor account of MG53's movement here
  works. See [[Transcription factor activity inference]].
- Its locus is unlucky: it sits 10.6 kb 3′ of PYCARD-AS1 and 17 kb 3′ of FUS **on the same strand**, so
  transcription that fails to terminate at those genes is counted as TRIM72 mRNA. See
  [[The TRIM72 locus]] and [[Readthrough spillover]].
- Nothing in the dataset perturbs MG53. There is no knockdown, no overexpression, and no protein
  measurement. Every result is an association across drugs and cell lines.

So an absence of association found here constrains the *mRNA-level* association in *these* cells. It cannot
rule out a protein-level or post-translational link, which is where most of MG53's known biology lives. That
asymmetry is stated in [[What this study found]] and should be repeated wherever the nulls are quoted.

## Links

- The locus and the artefact it creates: [[The TRIM72 locus]], [[Readthrough spillover]]
- The measurement problem: [[Why MG53 is hard to measure here]], [[Plate batch effects]],
  [[Reliability and disattenuation]]
- What moves it: [[Upstream of MG53]]
- What its level does: [[Downstream of MG53]], [[The measurement with controls]]
- The gene note with this dataset's numbers: [[TRIM72]]

## References

- Cai et al., 2009, *Nature Cell Biology* — MG53 as the nucleating factor for acute membrane repair in
  striated muscle; the founding paper.
- Cai et al., 2009, *Journal of Biological Chemistry* — the oxidation-dependent, rather than
  calcium-dependent, trigger for MG53 assembly at the wound.
- Song et al., 2013, *Nature* — MG53 as an E3 ligase for the insulin receptor and IRS1, and the metabolic
  consequences of its overexpression.
- Weisleder et al., 2012, *Science Translational Medicine* — recombinant MG53 delivered as a protein
  therapeutic in muscle injury models.
- Lee et al., 2013, *Journal of Biological Chemistry* — MG53 restrains myoblast differentiation.

The insulin-resistance claim is genuinely contested in the literature; treat any single paper on circulating
MG53 and human metabolic disease as one side of an open argument.
