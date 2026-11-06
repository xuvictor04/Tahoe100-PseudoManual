> [!summary] In one line
> BBC3 encodes PUMA, the BH3-only protein that is p53's most direct and most quantitatively important route to apoptosis.

## What it is

BBC3 (BCL-2 binding component 3) encodes PUMA, a small BH3-only member of the BCL-2 family. It is close to undetectable in unstressed cells and is induced strongly and rapidly by p53 through p53 response elements in its promoter. The protein localises to mitochondria and binds every anti-apoptotic BCL-2 family member with high affinity, which frees sequestered activators such as BIM and BID and leaves BAX and BAK unrestrained — so PUMA does not form pores itself, it removes the restraint on the proteins that do. Within the p53 response it is the component whose loss subtracts the most apoptosis: in mouse genetics, Puma deficiency accounts for the bulk of p53-dependent death after DNA damage in lymphoid cells, and combined loss of Puma and Noxa reproduces much of what p53 loss does in that setting.

PUMA is not only a p53 gene. Transcription is also driven by FOXO3A, by E2F1, by glucocorticoid receptor signalling and by growth-factor or cytokine withdrawal, giving it a substantial p53-independent induction repertoire. Clinically, basal and inducible PUMA levels contribute to chemotherapy and glucocorticoid sensitivity and to how cells respond to BH3-mimetic drugs, though PUMA itself is not a drug target.

## Why it appears in this work

PUMA is the cleanest transcript-level evidence that p53's output reached the apoptotic arm rather than stopping at arrest through [[The p21-DREAM axis]]. Its near-zero baseline gives it a large dynamic range within [[p53 program P]], which is an advantage for detecting induction and a liability for estimating it precisely in sparse single-cell data. Read next to [[CDKN1A]], it gives the arrest-versus-death split of a p53 response; read next to [[BAX]], it shows the difference between a gene whose p53 dependence lives in its transcription and one whose p53 dependence mostly does not.

## What is uncertain

Two things qualify PUMA as a readout here. First, its non-p53 inducers are real and several of them — growth-factor withdrawal, glucocorticoid signalling, FOXO3A activation — are exactly what a 24 h drug exposure can produce, so induction in a pooled, mixed-genotype panel is not by itself proof of p53 activity. That matters wherever the logic of [[p53 nullification in cancer cell lines]] is used to sign a gene by genotype. Second, apoptosis is self-censoring in single-cell data: dying cells lose mRNA and are preferentially lost at dissociation and quality filtering, so the cells carrying the strongest PUMA signal are the ones least likely to be counted. The bias runs toward understating the apoptotic arm and is hard to correct.

Mechanistically, whether PUMA is a direct activator of BAX or only a derepressor of anti-apoptotic proteins is still unresolved, with PUMA sitting awkwardly between the two models. And its necessity is lineage-dependent: the strong genetic evidence comes largely from lymphoid cells, while epithelial lines often tolerate PUMA loss with less effect on p53-driven death.

## References

- Nakano and Vousden, 2001, Molecular Cell — identified PUMA as a BH3-only gene induced by p53.
- Yu et al., 2001, Molecular Cell — identified PUMA as a p53-induced gene that triggers rapid apoptosis in colorectal cancer cells.
- Villunger et al., 2003, Science — showed Puma and Noxa mediate much of p53-dependent and drug-induced apoptosis in mouse cells.
- Jeffers et al., 2003, Cancer Cell — showed Puma is an essential mediator of both p53-dependent and p53-independent apoptotic pathways.
