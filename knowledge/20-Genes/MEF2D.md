---
symbol: MEF2D
type: gene
tier: 1
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MEF2D

> [!summary] In one line
> MEF2D is the most broadly expressed member of the MEF2 family, a MADS-box factor that partners myogenic bHLH proteins to drive late muscle differentiation and is a recurrent fusion partner in B-cell acute lymphoblastic leukaemia.

## What it is

MEF2D shares the architecture described for [[MEF2C]]: a MADS box plus MEF2 domain for DNA binding at the A/T-rich MEF2 consensus, dimerisation and cofactor contact. It binds the same sites as its paralogues and is likewise held inactive by class IIa histone deacetylases (HDAC4, [[HDAC5]], HDAC7, HDAC9) until kinase signalling exports those repressors from the nucleus.

What distinguishes MEF2D is breadth. [[MEF2C]] is restricted to muscle, heart, brain and parts of the immune system; MEF2D is expressed in most tissues, making it the family member most likely to be present in a non-muscle cell. Within muscle it is required late rather than early, acting on differentiation and maturation alongside myogenin and [[MYF6]] rather than on determination. A muscle-specific alternatively spliced exon in its transactivation region switches it from an HDAC-bound repressive form to an activating form during differentiation, so MEF2D's identity as activator or repressor is set by splicing as well as by cofactors — one of the clearest cases in the family of a factor whose transcript abundance says little about its output.

Outside muscle, MEF2D supports neuronal survival and activity-dependent transcription, and it is a genuine oncogene in leukaemia: recurrent rearrangements fuse MEF2D to BCL9, HNRNPUL1, CSF1R, DAZAP1 or SS18, producing a high-risk B-ALL subtype with raised MEF2D activity and sensitivity to HDAC inhibition.

## Why it appears in this work

MEF2 sites are functional at the TRIM72 promoter, sitting beside an E-box and acting synergistically with MyoD, so the MEF2 family is a principled first hypothesis for what moves [[MG53 (TRIM72)]]. MEF2D is worth checking here because, like its paralogues and unlike the myogenic bHLH factors, it is expressed in this panel of non-muscle cancer lines — [[MYOD1]] and [[MYF5]] are not. It is the closest thing this dataset has to a live test of the muscle-promoter account of MG53 — a test that only means anything alongside the controls in [[Transcription factor activity inference]].

## What is uncertain

Which MEF2 paralogue occupies the TRIM72 promoter in a cell is not established; the reporter experiments demonstrated a working MEF2 site, not which family member occupies it. For MEF2D the inference problem is sharper than for its relatives: it is expressed here rather than absent, so a score can be computed, but HDAC gating plus the repressive-versus-activating splice choice leaves the transcript carrying almost no information about whether the protein is doing anything. Its regulon is drawn from muscle, neuronal and lymphoid work and overlaps generic differentiation targets, so a correlation can appear without MEF2D being involved — which is why the principal-component and overlap-removal variants matter more for this gene than for most. Nothing here perturbs MEF2D, so no causal claim is available in either direction.

## References

- Molkentin et al., 1995, Cell — established the cooperative MADS–bHLH mechanism shared by MEF2 family members with myogenic bHLH factors.
- McKinsey et al., 2000, Nature — class II HDAC nuclear export as the switch that releases MEF2 during muscle differentiation.
- Potthoff and Olson, 2007, Development — review covering MEF2 paralogue expression breadth and combinatorial control.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — functional MEF2 site juxtaposed to an E-box in the TRIM72 promoter, synergistically activated with MyoD or myogenin.
- Gu et al., 2016, Nature Communications — recurrent MEF2D fusions define a high-risk B-ALL subtype with increased MEF2D activity and HDAC inhibitor sensitivity.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00073 |
| As a percentage | -0.05% |
| FDR, exposure-shuffle null | 0.8416 |
| In TP53-wild-type lines / altered lines | 0.00080 / -0.00166 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.288 raw, 0.071 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 18 targets |
| Activity vs MG53 across exposures (r) | 0.149 (q 3.39e-05) |
| With 3 principal components removed | 0.237 (q 2.14e-11) |
| Within line, across exposures (r) | -0.014 (q 0.528) |
| Percentile against all genes | 86.2 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is expressed at trace level (86.83 CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
