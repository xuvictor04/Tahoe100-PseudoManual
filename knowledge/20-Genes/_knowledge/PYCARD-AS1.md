> [!summary] In one line
> PYCARD-AS1 is a long non-coding RNA transcribed from the plus strand across almost exactly the span PYCARD occupies on the minus strand; it is in this vault for where it sits relative to TRIM72, not for what is known about it.

## What it is

Not much is established. PYCARD-AS1 (also catalogued as C16orf98) is annotated as a polyadenylated, Pol II-transcribed non-coding RNA at 16p11.2, running antisense to [[PYCARD]] and overlapping it at the 5′ end. General gene databases list no function for it. There is no mouse model, no structure, and no disease association.

One study has investigated it functionally. Working mainly in a single breast cancer line, it reported a transcript distributed between nucleus and cytoplasm with two activities, both directed at PYCARD: in the nucleus, localising to the PYCARD promoter and helping recruit DNMT1 and the histone methyltransferase G9a, promoting DNA methylation and H3K9me2 and so silencing transcription; in the cytoplasm, base-pairing with PYCARD mRNA through their overlapping 5′ regions and interfering with ribosome assembly. Knockdown raised PYCARD and increased sensitivity to paclitaxel, and that sensitisation was reduced when PYCARD was knocked down as well. The repression of PYCARD was reproduced in a few additional breast lines; the mechanistic and apoptosis work was not.

That is the literature. Beyond it, nothing is established — including whether the transcript does anything in the cell types studied here.

## Why it appears in this work

Position. PYCARD-AS1 lies on the plus strand roughly 10.6 kb 5′ of TRIM72 — the nearer of the two same-strand genes on the path into the region annotated as MG53, with [[FUS]] the larger donor further 5′. Polymerase that fails to terminate at its 3′ end runs directly into TRIM72, and a 3′-biased short-read assay counts those reads as MG53. It is therefore the proximal term in the readthrough geometry described in [[The TRIM72 locus]], and the flux accounting in [[Readthrough spillover]] is calibrated in terms of transcription delivered through it. Its second contribution is the coincidence with PYCARD: two genes at the same coordinates on opposite strands provide a built-in test of whether the quantification is strand-aware, which is what licenses the claim that the plus-strand co-movement is transcription rather than misalignment. See also [[Why MG53 is hard to measure here]].

## What is uncertain

Almost everything about the RNA itself. Whether PYCARD-AS1 is a functional transcript or a by-product of antisense and divergent transcription at an active promoter is open, and for this gene the single mechanistic study — largely one cell line, no independent replication I am aware of — does not settle it. That caveat applies broadly to "-AS1" annotations and should not be assumed away here.

Its measurement has a specific awkwardness that deserves stating. Because it overlaps PYCARD on the opposite strand, any reported level for PYCARD-AS1 depends entirely on correct strand assignment; and because it sits 3′ of a far more highly expressed same-strand neighbour, it is exposed to exactly the spillover it is invoked to explain. PYCARD-AS1 is simultaneously a donor of readthrough into TRIM72 and a recipient of readthrough from FUS, so its own quantification is not a clean independent variable. Finally, the distances quoted in this vault depend on annotation boundaries: a revised 3′ end would change the 10.6 kb figure, though not the direction of the argument.

## References

- Miao et al., 2019, PLoS Genetics — the only functional study of PYCARD-AS1: a dual nuclear/cytoplasmic lncRNA that represses PYCARD both epigenetically, via DNMT1 and G9a at its promoter, and translationally, via 5′ base-pairing with its mRNA.
