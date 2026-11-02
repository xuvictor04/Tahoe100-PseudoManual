> [!summary] In one line
> TRIAP1 is a small p53-induced protein that works inside mitochondria as half of a lipid-transfer complex, and its effect on the cell is to keep it alive — a survival output of p53, not a death one.

## What it is

TRIAP1 — TP53-regulated inhibitor of apoptosis 1, originally named p53CSV for "p53-inducible cell-survival factor" — is a 76-residue protein of the Mdm35 family. It was found as a gene induced by p53 whose knockdown increased apoptosis and whose overexpression protected cells against DNA-damage-induced death, and the induction was reported to be selective for *mild* genotoxic stress rather than severe damage. That conditionality is the interesting part of the original observation: it frames TRIAP1 as part of the arm of the p53 response that attempts repair and survival, rather than the arm that commits to death.

Its best-defined molecular job came later and is structural. In the mitochondrial intermembrane space TRIAP1 forms heterodimers with PRELID1 and with PRELID3B (SLMO2); these complexes bind and shuttle phosphatidic acid across the intermembrane space, delivering the precursor needed for cardiolipin synthesis at the inner membrane. Losing TRIAP1 or its PRELI partner lowers cardiolipin, which loosens cytochrome *c* from the inner membrane and leaves cells primed for apoptosis. So the anti-apoptotic phenotype has a plausible lipid-level explanation that does not require TRIAP1 to touch the apoptotic machinery at all.

A second, earlier mechanism is also in the literature: TRIAP1 co-immunoprecipitates with HSP70 and with APAF1, and was proposed to dampen apoptosome formation. This has much thinner support than the lipid-transfer work.

## Why it appears in this work

TRIAP1 is a curated p53 effector and a member of the induction arm of [[p53 program P]], which makes it a useful corrective to a habit of reading that programme as a single quantity called "p53 output". The arm contains [[BAX]], [[BBC3]] and [[PMAIP1]], which push toward death, and it also contains TRIAP1, which pushes the other way. A rise in the programme score therefore means "p53 is transcriptionally engaged", not "the cells are dying"; the pro- and anti-apoptotic members move together because they share an upstream driver, not because their consequences agree. For anyone reading the per-gene tables in [[Downstream of MG53]], TRIAP1 is a good reminder that the sign of a gene's slope and the sign of its effect on cell fate are different questions. See also [[Signing genes by p53 direction]].

## What is uncertain

Whether TRIAP1 is a *direct* p53 target is probably true but not cleanly settled: a p53 response element has been reported within the gene rather than in an upstream promoter, and secondary sources disagree over whether it sits in the second intron or the second exon — a discrepancy small enough to look like a transcription error somewhere and large enough that it should not be asserted either way here. The two mechanistic accounts of its anti-apoptotic action, cardiolipin supply and HSP70/APAF1 binding, have not been reconciled, and the second rests on essentially one study. The "mild damage only" induction pattern comes from the founding work and has not, as far as I can establish, been systematically retested across stress types. Finally, most of the functional work is overexpression and knockdown in cultured cells; what TRIAP1 loss does in a whole animal is much less clear than its biochemistry.

## References

- Park & Nakamura, 2005, *Cancer Research* — identified p53CSV/TRIAP1 as a p53-inducible gene required for survival after low-level genotoxic stress, and proposed the HSP70/APAF1 route.
- Potting et al., 2013, *Cell Metabolism* — showed TRIAP1/PRELI complexes transport phosphatidic acid within mitochondria, and that losing them depletes cardiolipin and sensitises cells to apoptosis.
