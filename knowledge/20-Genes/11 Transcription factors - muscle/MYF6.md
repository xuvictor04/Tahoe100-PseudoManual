---
symbol: MYF6
type: gene
tier: 1
pathway_role: transcription factor, muscle programme
aliases: [MRF4, bHLHc4]
gene_name: myogenic factor 6
locus: 12q21.31
locus_type: gene with protein product
gene_family: [Basic helix-loop-helix proteins, Myogenic regulatory family]
family_siblings_here: [ASCL1, MXI1, MYF5, MYOD1, MYOG, TCF21, TWIST1, TWIST2]
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MYF6

*myogenic factor 6* — 12q21.31

> [!summary] In one line
> MYF6 encodes MRF4, the myogenic regulatory factor of adult muscle, which contributes to lineage determination in the embryo and then acts as a brake on MEF2-driven growth in mature fibres.

## What it is

MYF6/MRF4 is the fourth myogenic regulatory factor, alongside [[MYOD1]], [[MYF5]] and [[MYOG]]. It shares their architecture — a basic helix-loop-helix domain binding the E-box consensus CANNTG as a heterodimer with E proteins. What sets it apart is timing: MRF4 appears transiently in the early somite, falls, then rises again to become the dominant MRF transcript in mature, innervated skeletal muscle. It is the family's adult member.

MRF4's genetics are entangled with [[MYF5]]'s, because the two genes sit a few kilobases apart on chromosome 12 and share regulatory sequence. Different MRF4-targeted alleles give mild, intermediate and severe phenotypes according to how much they perturb Myf5 in cis. Untangling it changed the field's conclusions: muscle forms in Myf5:MyoD double-null mice provided MRF4 is preserved, identifying MRF4 as a determination gene and not only a differentiation one.

Its adult function points the opposite way from the rest of the family. Knocking MRF4 down in adult mouse muscle causes hypertrophy rather than loss, by de-repressing MEF2-dependent transcription; MRF4 appears to stabilise a repressive complex and support nuclear localisation of the MEF2 corepressor HDAC4, so removing it releases MEF2 and raises protein synthesis. MRF4 loss also protects against denervation atrophy, which is why it is discussed as a target in sarcopenia and cachexia.

## Why it appears in this work

MRF4 is here as one of the muscle factors that would drive [[MG53 (TRIM72)]] in its native tissue, and it is the one whose native context best matches MG53's. MG53 is a protein of mature striated muscle and MRF4 is the MRF of mature striated muscle, so if TRIM72's muscle expression has a dominant adult driver, this is it. That makes its absence from this panel of cancer lines a more pointed negative than the absence of the embryonic factors: see [[Transcription factor activity inference]] and [[Why MG53 is hard to measure here]].

## What is uncertain

Whether MRF4 acts at the TRIM72 promoter is not established. The reporter and site-mutagenesis work on that promoter used MyoD and myogenin; MRF4 binds the same E-boxes and would be expected to engage them, but the inference is by family and should be labelled as such. MRF4's dual character is genuinely unresolved rather than merely complicated: the same protein activates muscle genes through E-boxes and represses MEF2 output, and how a cell sets which role dominates is not mapped. That matters for any regulon-based activity score here: a regulon signed from differentiation work and one signed from the adult hypertrophy work would point opposite ways for the same factor, so sign alone carries little meaning. In this dataset MRF4 is absent from the expressed-gene list, nothing perturbs it, and its targets overlap generic growth programmes — three reasons to treat any correlation it shows as uninformative about MG53.

## References

- Zhang, Behringer and Olson, 1995, Genes & Development — MRF4 inactivation gives myogenin up-regulation and rib anomalies.
- Olson, Arnold, Rigby and Wold, 1996, Cell — the three distinct phenotypes of MRF4-null alleles reflect cis effects on the neighbouring Myf5 gene.
- Kassar-Duchossoy et al., 2004, Nature — muscle forms in Myf5:Myod double mutants when Mrf4 is intact, establishing MRF4 as a determination gene.
- Moretti et al., 2016, Nature Communications — MRF4 knockdown in adult muscle causes hypertrophy by de-repressing MEF2, and prevents denervation atrophy.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — the TRIM72 promoter is driven by E-box and MEF2 elements in differentiating myoblasts (tested with MyoD and myogenin, not MRF4).

## What is on record

| | |
|---|---|
| Official name | myogenic factor 6 |
| Also known as | MRF4, bHLHc4, muscle-specific regulatory factor 4, herculin |
| Locus | 12q21.31 — gene with protein product |
| Gene families | Basic helix-loop-helix proteins; Myogenic regulatory family |
| Other genes here in those families | [[ASCL1]], [[MXI1]], [[MYF5]], [[MYOD1]], [[MYOG]], [[TCF21]], [[TWIST1]], [[TWIST2]] |
| Previously named | myogenic factor 6 (herculin) |

**Function**, from UniProt [P23409](https://www.uniprot.org/uniprotkb/P23409) (reviewed):

> Involved in muscle differentiation (myogenic factor). Induces fibroblasts to differentiate into myoblasts. Probable sequence specific DNA-binding protein

**Summary**, from NCBI Gene [4618](https://www.ncbi.nlm.nih.gov/gene/4618):

> The protein encoded by this gene is a probable basic helix-loop-helix (bHLH) DNA binding protein involved in muscle differentiation. The encoded protein likely acts as a heterodimer with another bHLH protein. Defects in this gene are a cause of autosomal dominant centronuclear myopathy (ADCNM). [provided by RefSeq, May 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7566) · Entrez [4618](https://www.ncbi.nlm.nih.gov/gene/4618) · UniProt [P23409](https://www.uniprot.org/uniprotkb/P23409) · Ensembl [ENSG00000111046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111046) · OMIM [159991](https://www.omim.org/entry/159991)

**PubMed**, as HGNC records for this gene — [8978788](https://pubmed.ncbi.nlm.nih.gov/8978788/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 8 targets |
| Activity vs MG53 across exposures (r) | -0.268 (q 1.07e-14) |
| With 3 principal components removed | -0.169 (q 1.37e-06) |
| Within line, across exposures (r) | -0.035 (q 0.004) |
| Percentile against all genes | 6.8 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is absent from the expressed gene list (— CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** muscle promoter TF (TRIM72's native drivers); transcription factor, negative rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
