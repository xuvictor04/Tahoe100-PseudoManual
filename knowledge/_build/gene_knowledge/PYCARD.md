> [!summary] In one line
> PYCARD encodes ASC, the two-domain adaptor that bridges inflammasome sensors to caspase-1 — and, for this study, the gene that happens to occupy exactly the same coordinates as PYCARD-AS1 on the opposite strand.

## What it is

ASC is a small bipartite adaptor: a pyrin domain (PYD) at one end, a caspase recruitment domain (CARD) at the other, and essentially nothing else. That architecture is its whole function. The PYD engages the PYD of an activated sensor — NLRP3, AIM2 and others — and the CARD engages pro-caspase-1. ASC senses nothing and cleaves nothing; it converts a sensor's activation into a platform on which caspase-1 can autoactivate.

The platform is literal. ASC polymerises into helical filaments through its PYD, and those filaments condense into the micron-scale perinuclear structure known as the ASC speck, which concentrates caspase-1 to the point where it can process its substrates. Active caspase-1 then matures IL-1β and IL-18 and cleaves gasdermin D, committing the cell to pyroptosis. Mouse knockouts showed the requirement is sensor-specific: some inflammasomes depend absolutely on ASC, while NLRC4 can engage caspase-1 through its own CARD.

The gene was found twice, under names reflecting two different interests. As ASC it was described as a protein that aggregates during apoptosis of a leukaemia line. As TMS1 — target of methylation-induced silencing — it was a pro-apoptotic CARD protein whose promoter is hypermethylated and whose expression is lost in breast cancers. That second identity matters for anyone reading this gene's level in cancer cells: PYCARD is epigenetically silenced in a substantial fraction of tumour lines, so its baseline is not a constant.

## Why it appears in this work

PYCARD is in this vault for its coordinates, not its biology. It lies at 16p11.2 on the minus strand, occupying the same span as [[PYCARD-AS1]] on the plus strand to within a couple of bases, which makes it the control that validates the readthrough argument. Transcription leaking 3′ from the plus-strand genes toward TRIM72 must raise the plus-strand genes and cannot raise PYCARD; if anything it should do the opposite. Two genes at identical coordinates moving in opposite directions is what rules out a mapping smear and shows the quantification respects strand — the load-bearing observation in [[Readthrough spillover]] and [[The TRIM72 locus]]. No inflammasome biology is required for that inference, and none should be read into it.

## What is uncertain

The inflammasome account of ASC is solid, but it was built in myeloid cells, and almost none of it transfers to the setting here. These are pooled epithelial and other non-myeloid cancer lines, many of which have PYCARD methylation-silenced and most of which lack a licensed NLRP3 inflammasome; priming signals that induce the sensors are absent in plain culture. There is therefore no basis for reading PYCARD's level in this dataset as inflammasome activity, and a change in it should not be interpreted as inflammation. Whether ASC's original pro-apoptotic (TMS1) activity is a genuine inflammasome-independent function or a downstream consequence of caspase-1-driven death has never been cleanly settled. Its usefulness as a strand control also rests on the antisense pair being correctly annotated and on the aligner assigning reads by strand — which is what the opposing movement itself tests. The argument is self-checking, but it checks the pipeline, not the biology.

## References

- Masumoto et al., 1999, Journal of Biological Chemistry — described ASC as a 22-kDa protein that aggregates during apoptosis of HL-60 cells.
- Conway et al., 2000, Cancer Research — identified TMS1 as a pro-apoptotic CARD protein silenced by promoter methylation in human breast cancers.
- Martinon et al., 2002, Molecular Cell — defined the inflammasome as a platform activating inflammatory caspases and processing pro-IL-1β.
- Mariathasan et al., 2004, Nature — showed differential requirement for the caspase-1 adaptors ASC and Ipaf across inflammasomes.
- Fernandes-Alnemri et al., 2009, Nature — AIM2 activates an ASC-dependent inflammasome in response to cytoplasmic DNA.
- Lu et al., 2014, Cell — a unified polymerisation mechanism in which ASC forms filaments that assemble the speck.
