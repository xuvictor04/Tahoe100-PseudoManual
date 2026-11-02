> [!summary] In one line
> USP7 is the deubiquitinase that removes ubiquitin from both p53 and MDM2, which means its net effect on p53 depends on how much USP7 there is — the clearest case in the pathway of a regulator whose direction is not a fixed property.

## What it is

USP7, long known as HAUSP (herpesvirus-associated ubiquitin-specific protease), has an N-terminal TRAF-like domain, a catalytic USP domain, and C-terminal ubiquitin-like domains that fold back to activate it. The TRAF-like domain carries the substrate-binding pocket, which p53 and MDM2 bind through similar short motifs — as does EBNA1 of Epstein–Barr virus, which is how the enzyme got its name.

Its relationship to p53 is the textbook case of a non-monotonic regulator. USP7 deubiquitinates p53 and stabilises it, even against excess MDM2, which predicts that losing USP7 should destabilise p53. Disrupting the gene in human cells did the opposite: p53 was stabilised and functionally activated. The resolution is that MDM2 is also a USP7 substrate and the more sensitive one — it needs deubiquitination to survive long enough to act as a ligase — so partial loss of USP7 lowers p53 while near-complete loss removes MDM2 first and raises it. Both behaviours have been reported in the same system at different knockdown depths.

Beyond p53 the substrate list is long — MDMX/[[MDM4]], PTEN, Claspin, FOXO4, Tip60, UHRF1 — and germline variants cause Hao-Fountain syndrome. Selective inhibitors reported in 2017 act through the MDM2 arm: they destabilise MDM2, raise p53 and induce targets including [[CDKN1A]].

## Why it appears in this work

USP7 is here as an upstream regulator of p53 stability, not a p53 target: it has no programme arm and no induction to report. Its value is as the cleanest illustration of what this study's design cannot see. USP7 is a decisive controller of p53 output, and almost none of that control appears in mRNA — it operates on protein half-life, through a pocket shared between two substrates, with a direction that depends on its own abundance. That is the same category of mechanism as [[MG53 (TRIM72)]]'s known biology, which is also E3-ligase activity on protein substrates. The asymmetry stated in [[What this study found]] — that absence of an mRNA-level association does not rule out a protein-level link — is therefore not special pleading for MG53. See [[The p53 pathway]].

## What is uncertain

"USP7 stabilises p53" is an incomplete statement, and any experiment reading out p53 after changing USP7 must report the depth of the perturbation before its sign can be interpreted. How much of the inhibitors' anti-tumour effect runs through p53 rather than other substrates is actively argued, and it matters clinically: the non-p53 substrates would predict activity in TP53-mutant tumours. Much of the substrate list derives from overexpression or immunoprecipitation work, and the weight of individual entries is uneven. For this dataset, USP7 mRNA is close to uninformative about USP7 activity — the enzyme is allosterically activated by its own C-terminal tail, competed for by abundant substrates, and present in excess of what the p53 axis consumes.

## References

- Li et al., 2002, *Nature* — showed HAUSP deubiquitinates p53 and stabilises it even in the presence of excess MDM2.
- Cummins et al., 2004, *Nature* — disrupting the HAUSP gene in human cells stabilised and activated p53, the opposite of the predicted result.
- Li et al., 2004, *Molecular Cell* — partial reduction of HAUSP destabilised p53 while near-complete loss stabilised it, giving the dose-dependent model.
- Saridakis et al., 2005, *Molecular Cell* — structural basis for EBNA1 and p53 competing for the same USP7 binding site.
- Turnbull et al., 2017, *Nature* — FT671 and FT827 inhibit USP7 selectively, destabilising MDM2, raising p53 and inducing p21.
- Kategaya et al., 2017, *Nature* — independent small-molecule USP7 inhibitors acting by interfering with ubiquitin binding.
