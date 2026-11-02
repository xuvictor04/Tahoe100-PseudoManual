---
symbol: MYOD1
type: gene
tier: 1
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MYOD1

> [!summary] In one line
> MYOD1 encodes MyoD, the archetypal master regulatory transcription factor: a basic helix-loop-helix protein whose expression alone is enough to convert a fibroblast into a muscle cell.

## What it is

MyoD was the founding demonstration that one transcription factor can impose a differentiation programme: a single transfected cDNA converts fibroblasts into myoblasts, the result that defined what "master regulator" means. MyoD binds the E-box consensus CANNTG as an obligate heterodimer with the ubiquitous E proteins (E12/E47, encoded by TCF3).

Its activity is gated at several levels rather than by its own abundance. Id proteins sequester E proteins and block productive heterodimers; cyclin D1–CDK4 and phosphorylation suppress activity in cycling cells; [[RB1]] interaction is required for the differentiated, cell-cycle-exited state; and the p300/CBP and SWI/SNF complexes MyoD recruits are what actually open target chromatin. MyoD occupies thousands of E-boxes genome-wide, many in non-muscle genes, so what distinguishes a productive target is cofactor availability and chromatin context rather than binding. It also feeds forward into the rest of the programme, inducing myogenin ([[MYOG]]) and partnering MEF2 factors ([[MEF2C]], [[MEF2D]]) at composite E-box/MEF2 elements.

Two further facts bear on this study: MyoD couples differentiation to cell-cycle exit by inducing [[CDKN1A]], and does so independently of p53 — a reminder that p21 induction is not by itself a p53 readout (see [[The p21-DREAM axis]]). And MYOD1 is a cancer gene in one narrow setting: a recurrent L122R substitution in the basic region acts as a neomorph with MYC-like DNA-binding preference, marking an aggressive subset of spindle cell and sclerosing rhabdomyosarcoma.

## Why it appears in this work

MyoD is the most direct candidate explanation for [[MG53 (TRIM72)]]'s expression. TRIM72's promoter is a muscle promoter: it carries E-boxes and a conserved MEF2 site beside the proximal one, mutating either element lowers promoter activity, and MyoD plus MEF2 activate it synergistically as myoblasts differentiate. If anything transcriptional drove MG53, this is where one would look first. It is in the vault because in this panel MyoD is not there to look at — it does not reach the expressed-gene list — which is much of why [[Transcription factor activity inference]] finds no factor accounting for MG53's movement, and why [[The TRIM72 locus]] carries the explanation instead.

## What is uncertain

Little about MyoD's core biology is contested; the uncertainty is about inference, not the gene. A factor absent from the expressed-gene list cannot have its activity meaningfully estimated from its regulon, so whatever a regulon method returns for MYOD1 here reflects what its annotated targets — which include cell-cycle and stress genes — do under drug exposure for unrelated reasons. The absence is a property of this panel rather than of cancer generally: rhabdomyosarcoma lines express MyoD strongly, and a panel containing them would behave differently. Finally, the TRIM72 promoter work rests on reporter assays and site mutagenesis in differentiating C2C12 myoblasts, not on demonstrated MyoD occupancy of the endogenous promoter. It establishes that MyoD can drive TRIM72 in muscle, not what sets TRIM72's trace-level transcription in cells where the muscle programme is off.

## References

- Davis, Weintraub and Lassar, 1987, Cell — expression of a single transfected cDNA converts fibroblasts to myoblasts.
- Tapscott et al., 1988, Science — identified MyoD1 as a nuclear phosphoprotein requiring a Myc-homologous region for myogenic conversion.
- Lassar et al., 1991, Cell — myogenic bHLH proteins require heterodimerisation with E12/E47-like proteins to bind DNA and function.
- Halevy et al., 1995, Science — MyoD induces p21 and couples terminal cell-cycle arrest to muscle differentiation, independently of p53.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — MyoD (or myogenin) and MEF2 synergistically activate the TRIM72 promoter via E-box and MEF2 elements.
- Kohsaka et al., 2014, Nature Genetics — a recurrent neomorphic MYOD1 mutation defines a clinically aggressive rhabdomyosarcoma subset.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 102 targets |
| Activity vs MG53 across exposures (r) | 0.086 (q 0.015) |
| With 3 principal components removed | 0.087 (q 0.014) |
| Within line, across exposures (r) | 0.004 (q 0.827) |
| Percentile against all genes | 74.0 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is absent from the expressed gene list (— CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work; muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
