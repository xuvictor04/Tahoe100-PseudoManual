> [!summary] In one line
> USP7 is the deubiquitinase that removes ubiquitin from both p53 and MDM2, which means its net effect on p53 depends on how much USP7 there is — the clearest example in the pathway of a regulator whose direction is not a fixed property.

## What it is

USP7, long known as HAUSP (herpesvirus-associated ubiquitin-specific protease), is a large ubiquitin-specific protease built from an N-terminal TRAF-like domain, a catalytic USP domain, and a C-terminal stretch of ubiquitin-like domains that folds back to activate the catalytic domain. The TRAF-like domain carries the substrate-binding pocket, and p53 and MDM2 bind that same pocket through similar short peptide motifs — as does EBNA1 of Epstein–Barr virus, which is how the enzyme got its name.

Its relationship to p53 is the textbook case of a non-monotonic regulator. USP7 deubiquitinates p53 and stabilises it, even against excess MDM2, which predicts that losing USP7 should destabilise p53. Disrupting the gene in human cells did the opposite: p53 was stabilised and functionally activated. The resolution is that MDM2 is also a USP7 substrate and the more sensitive one — MDM2 needs USP7-mediated deubiquitination to survive long enough to act as a ligase — so partial loss of USP7 lowers p53 while near-complete loss removes MDM2 first and raises it. Both behaviours have been reported in the same system at different knockdown depths.

Beyond p53, the substrate list is long: MDMX/[[MDM4]], PTEN, Claspin, FOXO4, Tip60, UHRF1 and DNMT1 among others, plus a structural role in polycomb complexes. Germline USP7 variants cause Hao-Fountain syndrome, a neurodevelopmental disorder. Pharmacologically, selective USP7 inhibitors reported in 2017 work through the MDM2 arm: inhibiting USP7 destabilises MDM2, raises p53 and induces p53 target genes including [[CDKN1A]], giving a route to p53 reactivation that is distinct from the nutlins.

## Why it appears in this work

USP7 is in the vault as an upstream regulator of p53 stability, not as a p53 target — it has no programme arm and no induction to report. Its value here is as the cleanest illustration of what this study's design cannot see. USP7 is a decisive controller of p53 output, and almost nothing about that control appears in mRNA: it operates on protein half-life, through a pocket shared between two substrates, with a direction that depends on its own abundance. That is the same category of mechanism as [[MG53 (TRIM72)]]'s known biology, which is also E3-ligase activity on protein substrates. The asymmetry stated in [[What this study found]] — that an absence of mRNA-level association does not rule out a protein-level link — is not special pleading for MG53; USP7 shows that the pathway genuinely contains important regulation of exactly that invisible kind. See [[The p53 pathway]] and [[Why MG53 is hard to measure here]].

## What is uncertain

The direction question is not merely historical; it means "USP7 stabilises p53" is an incomplete statement, and any experiment reading out p53 after changing USP7 has to report the depth of the perturbation before the sign is interpretable. How much of the anti-tumour effect of USP7 inhibitors runs through p53 as opposed to the other substrates is actively argued, and it matters clinically because the non-p53 substrates would predict activity in TP53-mutant tumours. Much of the substrate list derives from overexpression or immunoprecipitation work and the physiological weight of individual entries is uneven. For this dataset specifically, USP7 mRNA is close to uninformative about USP7 activity: the enzyme is allosterically activated by its own C-terminal tail, competed for by abundant substrates, and present well in excess of what the p53 axis consumes, so expression-level reasoning about it should not be attempted.

## References

- Li et al., 2002, *Nature* — showed HAUSP deubiquitinates p53 and stabilises it even in the presence of excess MDM2.
- Cummins et al., 2004, *Nature* — disrupting the HAUSP gene in human cells stabilised and activated p53, the opposite of the predicted result.
- Li et al., 2004, *Molecular Cell* — partial reduction of HAUSP destabilised p53 while near-complete loss stabilised it, giving the dose-dependent model.
- Saridakis et al., 2005, *Molecular Cell* — structural basis for EBNA1 and p53 competing for the same USP7 binding site.
- Turnbull et al., 2017, *Nature* — FT671 and FT827 inhibit USP7 selectively, destabilising MDM2, raising p53 and inducing p21.
- Kategaya et al., 2017, *Nature* — independent small-molecule USP7 inhibitors acting through interference with ubiquitin binding.
