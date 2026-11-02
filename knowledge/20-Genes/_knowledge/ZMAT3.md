> [!summary] In one line
> ZMAT3 is a zinc-finger RNA-binding protein, induced by p53 about as reliably as any gene in the pathway, which acts on its targets' splicing and stability rather than on their transcription.

## What it is

ZMAT3 — zinc finger matrin-type 3, known in the older literature as Wig-1 and PAG608 — was found in the 1990s as a p53-inducible gene encoding a nuclear protein with three zinc fingers of the matrin type. Those fingers bind RNA, including double-stranded RNA, and everything ZMAT3 is now thought to do is post-transcriptional. It is one of the most consistently p53-responsive genes known, which is why it turns up in nearly every attempt to define a p53 signature.

Two mechanistic accounts exist, and they are not the same claim. The earlier one is stability: Wig-1 was reported to bind AU-rich elements in 3′ untranslated regions and to stabilise its targets, p53 mRNA itself among them, which would make it a positive-feedback element in the pathway. The later and currently better-supported account is splicing. *In vivo* RNAi and CRISPR screens in Kras-driven mouse lung and liver tumours converged on Zmat3 as a tumour suppressor acting downstream of p53; ZMAT3 was then shown to bind thousands of pre-mRNAs, mostly at intronic uridine-rich sequences, and to change exon inclusion in ways frequently coupled to nonsense-mediated decay. Among the transcripts whose splicing it controls are the p53 inhibitors [[MDM2]] and [[MDM4]]. Independent work in colorectal cells identified CD44 as its strongest alternatively spliced target: losing ZMAT3 shifts CD44 from the standard isoform toward the oncogenic variant isoforms, and knocking the variants back down rescues the growth advantage that ZMAT3 loss confers.

## Why it appears in this work

ZMAT3 is a curated p53 effector in the induction arm of [[p53 program P]], and it is among the better-behaved members of that arm: it moves in one direction across the reference compounds rather than going each way, which is not true of many of its neighbours in the signature. That makes it one of the more trustworthy single-gene readouts that p53 is transcriptionally engaged in a given well, in the same tier as [[CDKN1A]] and [[MDM2]] — and unlike MDM2 it is not simultaneously the brake, so it is easier to interpret. Its membership also helps justify treating the programme as a p53 readout rather than a generic stress readout, since ZMAT3 has few known inputs other than p53.

## What is uncertain

The vault's curated table files ZMAT3 under negative feedback, and that label does not sit comfortably with either mechanistic account. Stabilising p53 mRNA would be positive feedback; shifting MDM2 and MDM4 transcripts toward nonsense-mediated decay would also relieve inhibition of p53. The label should be read as inherited annotation, not as a conclusion, and it is not safe to infer the sign of ZMAT3's effect on p53 from it.

The two mechanisms themselves are unreconciled. The AU-rich-element work and the intronic-U-rich splicing work describe different binding preferences and different consequences, and the later papers treat the earlier proposal as a prior claim rather than something they confirmed. Whether both happen, or the first was a partial view of the second, is open. The tumour-suppressor genetics are strong but come from specific mouse models and from cell lines; how much of p53's tumour suppression runs through ZMAT3 in human cancer is not established. And as always in a transcript-level dataset, ZMAT3 mRNA reports that p53 fired, not that ZMAT3 did anything to its RNA targets — the splicing output would need isoform-level quantification that 3′-biased single-cell data cannot supply.

## References

- Varmeh-Ziaie et al., 1997, *Oncogene* — identified Wig-1 as a p53-induced zinc-finger gene.
- Hellborg et al., 2001, *Oncogene* — characterised Wig-1 as a nuclear, double-stranded-RNA-binding zinc-finger protein.
- Vilborg et al., 2009, *PNAS* — reported that Wig-1 binds an AU-rich element in the p53 3′ UTR and stabilises p53 mRNA.
- Bieging-Rolett et al., 2020, *Molecular Cell* — screens identified Zmat3 as a p53-dependent tumour suppressor and showed it regulates splicing, including of MDM2 and MDM4, with coupling to nonsense-mediated decay.
- Muys et al., 2021, *Genes & Development* — showed ZMAT3 binds intronic uridine-rich regions and suppresses inclusion of oncogenic CD44 variant exons, defining a p53–ZMAT3–CD44 axis.
