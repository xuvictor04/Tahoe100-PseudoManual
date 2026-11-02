> [!summary] In one line
> PMAIP1 encodes NOXA, the BH3-only protein p53 induces to neutralise MCL1 and so lower the threshold for mitochondrial apoptosis.

## What it is

NOXA is a very small BH3-only protein — a BH3 motif and a C-terminal mitochondrial-targeting segment, little else. In the BCL2 family's division of labour it is a *sensitiser*: it does not itself permeabilise the outer mitochondrial membrane, but occupies prosurvival relatives so that the direct activators can. Its defining property is selectivity. Unlike PUMA ([[BBC3]]), which engages the whole prosurvival set, NOXA binds MCL1 and A1/BFL1 and essentially ignores BCL2 and BCL-XL. Binding MCL1 also accelerates MCL1's proteasomal degradation, so NOXA removes its target rather than merely sequestering it. With MCL1 depleted, BAK and [[BAX]] are free to oligomerise, the membrane permeabilises, and the apoptosome commits the cell.

PMAIP1 is a direct p53 target with a p53 response element; mouse work combining Noxa and Puma loss showed the two together account for much of p53-dependent apoptosis, with PUMA generally the more consequential. But NOXA is not a p53-exclusive gene, and that matters more for NOXA than for most p53 targets. It is strongly induced by proteasome inhibition, by ER stress through the ATF4 ([[ATF4]]) arm of the integrated stress response, by E2F1 and deregulated MYC, and under hypoxia. The protein is short-lived and proteasome-degraded, so steady-state NOXA reflects turnover as much as transcription. Clinically the NOXA-to-MCL1 balance helps determine whether a cell depends on BCL2 or on MCL1 for survival — MCL1 dependence is a principal route to venetoclax resistance, and bortezomib's cytotoxicity runs substantially through NOXA induction.

## Why it appears in this work

NOXA is where p53's output stops being reversible. Most members of the induction arm of [[p53 program P]] report engagement — arrest, repair, signalling — but NOXA, with PUMA, [[BAX]] and [[TNFRSF10B]], reports commitment to death. For a reader trying to tell whether p53 activity in a line is cytostatic or cytotoxic, the apoptotic members are the relevant subset, and NOXA is the most lineage-agnostic of them. Because it is an induced gene, its slope against anything must be converted into p53-output units before it can be compared with a repressed gene's — see [[Signing genes by p53 direction]].

## What is uncertain

The largest problem is structural rather than biological. A transcriptome measured at 24 h in cells still present is a survivorship-filtered sample: cells that acted on a NOXA induction are gone, so what is measured is NOXA in the survivors, and its relation to the apoptotic response actually mounted is not simple. Second, NOXA's p53-independent inducers are strong and this screen contains compounds that hit several of them — proteasome inhibitors, CDK and transcription inhibitors, ER stressors — so NOXA induction under drug exposure is weak evidence of p53 engagement on its own. Third, this is a case where mRNA is a poor proxy for function: what decides outcome is NOXA protein against MCL1 protein at the mitochondrion, and both are short-lived. Fourth, the mouse genetics do not transfer cleanly — the relative weight of Noxa and Puma differs by cell type.

## References

- Oda et al., 2000, Science — identified Noxa as a BH3-only p53 target and candidate mediator of p53-induced apoptosis.
- Villunger et al., 2003, Science — Puma and Noxa together mediate much of the p53- and drug-induced apoptotic response in mouse cells.
- Chen et al., 2005, Molecular Cell — Noxa selectively targets Mcl-1 while Puma engages all prosurvival relatives, giving the BH3-only proteins complementary function.
