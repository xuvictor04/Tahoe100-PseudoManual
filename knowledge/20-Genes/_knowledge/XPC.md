> [!summary] In one line
> XPC is the sensor that finds bulky DNA lesions anywhere in the genome and starts nucleotide-excision repair there, and it is one of the repair genes p53 induces.

## What it is

Nucleotide-excision repair comes in two flavours that differ only in how the lesion is found. In transcription-coupled repair, a stalled RNA polymerase is the detector. In global-genome repair — the rest of the genome, including the strand nobody is transcribing — the detector is XPC, working as a heterotrimer with RAD23B and centrin-2. XPC does not recognise the lesion's chemistry directly; it recognises the single-stranded character of the undamaged strand opposite a helix-distorting adduct, which is why it handles a chemically diverse set of substrates, UV photoproducts and bulky chemical adducts alike. Having bound, it recruits TFIIH and hands off to the verification and incision machinery; everything after that step is shared with the transcription-coupled branch.

Because XPC serves only the global-genome branch, loss of it produces a distinctive clinical picture. Xeroderma pigmentosum group C patients have extreme photosensitivity and a skin-cancer risk raised by orders of magnitude, but usually lack the progressive neurodegeneration seen in groups whose defects also cripple transcription-coupled repair. XPC is accordingly one of the strongest single-gene links between a repair deficiency and cancer incidence in humans.

Its connection to p53 is transcriptional. XPC mRNA and protein rise after UV damage in a p53-dependent manner, with little induction in p53-deficient cells, and a p53 response element has been mapped to the gene — located, in follow-up work, within the first exon near the translation start rather than in the upstream promoter. [[DDB2]], the other dedicated global-genome damage sensor, is likewise p53-inducible, which is the basis for describing p53 as a switch that raises global-genome repair capacity as a whole rather than one gene at a time.

## Why it appears in this work

XPC is a curated p53 effector and a member of the induction arm of [[p53 program P]], sitting with [[DDB2]], [[POLH]] and [[RRM2B]] in the DNA-repair group of [[The p53 pathway]]. Its presence matters for how the programme should be read: the signature is not only arrest and apoptosis genes, and a rise in it is consistent with p53 attempting to repair damage rather than only to eliminate the cell. In a panel dominated by genotoxic compounds that distinction is worth keeping explicit, because the same drug that activates p53 also creates the lesions XPC is induced to clear. XPC is also one of the better-expressed members of the programme, which makes it less vulnerable to the counting noise that dominates trace transcripts here — a contrast worth noting against [[Why MG53 is hard to measure here]].

## What is uncertain

The p53-dependence of XPC induction was established largely in UV-irradiated fibroblast systems, and how far it generalises to the chemical classes in this panel is not something the original work addressed. The induction is modest even where it is clean, and in this dataset XPC's direction is mixed across reference compounds — it is in the induction arm on balance, not because it reliably goes up. Whether the mapped exon-1 element is the operative one in all contexts is not fully resolved, and the discrepancy with the originally proposed promoter element has not been widely retested.

More fundamentally, XPC mRNA is a poor proxy for repair capacity. XPC acts stoichiometrically as a sensor, its protein is itself regulated by damage-induced ubiquitination and degradation, and DDB2 modulates its recruitment — so a change in transcript need not translate into a change in lesion clearance. Treat XPC here as a reporter that p53 engaged its repair arm, not as a measure of how much repair happened.

## References

- Sugasawa et al., 1998, *Molecular Cell* — identified the XPC complex as the initiator of global-genome nucleotide-excision repair.
- Adimoolam & Ford, 2002, *PNAS* — showed XPC mRNA and protein are induced after UV in a p53-dependent manner and identified a p53 response element in the gene.
- Araki et al., 2001, *Journal of Biological Chemistry* — identified centrin-2 as the third subunit of the XPC–RAD23B complex.
