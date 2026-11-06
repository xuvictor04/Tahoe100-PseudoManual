---
symbol: SRF
type: gene
tier: 1
pathway_role: transcription factor, muscle programme
aliases: [MCM1]
gene_name: serum response factor
locus: 6p21.1
locus_type: gene with protein product
gene_family: [MADS box family]
family_siblings_here: [MEF2A, MEF2B, MEF2C, MEF2D]
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SRF

*serum response factor* — 6p21.1

> [!summary] In one line
> SRF is a MADS-box transcription factor that sits on CArG-box promoters and delivers two different programmes — immediate-early genes or contractile and cytoskeletal genes — depending on which family of coactivators reaches it.

## What it is

SRF binds the CArG box, CC(A/T)₆GG, the core of the serum response element, through an N-terminal MADS box that also handles dimerisation. The factor is broadly expressed and largely constitutively bound at its targets; essentially all regulation happens one level up, at the coactivators. SRF is best understood as a switchboard with two incoming lines.

The first line is the ternary complex factors — ELK1, ELK4/SAP-1, ELK3/NET — recruited to SRF and activated by ERK phosphorylation. This is the growth-factor, immediate-early route: FOS, EGR1, JUNB. The second is the myocardin family — MRTFA/MKL1, MRTFB and MYOCD. These carry RPEL motifs that bind monomeric G-actin, which holds them cytoplasmic; Rho-driven actin polymerisation depletes the free G-actin pool, releases them into the nucleus and switches SRF onto cytoskeletal and contractile targets: ACTA2, ACTB, CNN1, TAGLN, vinculin. The two families compete for the same surface, so one factor reads either mitogenic signalling or the mechanical state of the cytoskeleton.

Srf-null mouse embryos fail gastrulation and never form mesoderm, with SRF-dependent immediate-early and α-actin genes unexpressed. Conditional deletion shows requirements across cardiac, smooth and skeletal muscle, and in neurons for activity-dependent transcription; in muscle it works alongside, not instead of, the myogenic bHLH and MEF2 machinery.

## Why it appears in this work

SRF is in this vault as a candidate native-tissue driver of [[MG53 (TRIM72)]], part of the muscle and promoter transcription-factor panel assembled alongside [[MEF2A]] and [[MYOD1]]. The question is upstream: if something sets TRIM72 transcription in these non-muscle lines, is it a recognisable myogenic regulator? SRF is also entangled with [[ELK4]], which appears prominently elsewhere in this analysis: ELK4 is one of SRF's own ternary complex factors, so the two share CArG-box targets and their inferred activities are not independent. A ranking placing both high reports overlapping evidence, not two converging lines. See [[Transcription factor activity inference]].

## What is uncertain

The reported myogenic control of the TRIM72 promoter runs through a MEF2 site and an adjacent E-box; no CArG element there has been characterised, and SRF is not listed as a TRIM72 regulator in the curated network used here. Its presence in this panel is a candidate choice justified by lineage logic, not a documented regulatory link; nothing here should be read as establishing one.

Two cautions matter. Because SRF is controlled at the coactivator level, its mRNA is a poor proxy for its activity — the argument for regulon-based inference, which has its own problem here: SRF's regulon is dominated by immediate-early genes, and those respond to almost any perturbation. An inferred "SRF activity" rising across a drug panel may be reporting generic stress rather than anything SRF-specific. Worse, the MRTF arm is driven by actin dynamics, so cytoskeleton-disrupting compounds activate SRF through a route unrelated to the biology under study — a real confound in a several-hundred-compound screen. Finally, SRF's role in cancer is context-dependent, so its activity carries no fixed directional meaning.

## References

- Arsenian et al., 1998, EMBO Journal — Srf-null mouse embryos show a severe gastrulation defect with impaired Egr-1, c-fos and α-actin expression, identifying SRF as essential for mesoderm formation.
- Miralles et al., 2003, Cell — actin dynamics control SRF activity through G-actin binding and nuclear accumulation of the coactivator MAL/MRTFA.
- Olson & Nordheim, 2010, Nature Reviews Molecular Cell Biology — review linking actin dynamics and SRF-dependent transcription to cell motility.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by synergism of MyoD (or myogenin) and MEF2 at a conserved MEF2 site adjacent to an E-box.

## What is on record

| | |
|---|---|
| Official name | serum response factor |
| Also known as | MCM1, minichromosome maintenance 1 homolog (S. cerevisiae), c-fos serum response element-binding transcription factor |
| Locus | 6p21.1 — gene with protein product |
| Gene families | MADS box family |
| Other genes here in those families | [[MEF2A]], [[MEF2B]], [[MEF2C]], [[MEF2D]] |

**Function**, from UniProt [P11831](https://www.uniprot.org/uniprotkb/P11831) (reviewed):

> SRF is a transcription factor that binds to the serum response element (SRE), a short sequence of dyad symmetry located 300 bp to the 5' of the site of transcription initiation of some genes (such as FOS). Together with MRTFA transcription coactivator, controls expression of genes regulating the cytoskeleton during development, morphogenesis and cell migration. The SRF-MRTFA complex activity responds to Rho GTPase-induced changes in cellular globular actin (G-actin) concentration, thereby coupling cytoskeletal gene expression to cytoskeletal dynamics. Required for cardiac differentiation and maturation

**Summary**, from NCBI Gene [6722](https://www.ncbi.nlm.nih.gov/gene/6722):

> This gene encodes a ubiquitous nuclear protein that stimulates both cell proliferation and differentiation. It is a member of the MADS (MCM1, Agamous, Deficiens, and SRF) box superfamily of transcription factors. This protein binds to the serum response element (SRE) in the promoter region of target genes. This protein regulates the activity of many immediate-early genes, for example c-fos, and thereby participates in cell cycle regulation, apoptosis, cell growth, and cell differentiation. This gene is the downstream target of many pathways; for example, the mitogen-activated protein kinase pathway (MAPK) that acts through the ternary complex factors (TCFs). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11291) · Entrez [6722](https://www.ncbi.nlm.nih.gov/gene/6722) · UniProt [P11831](https://www.uniprot.org/uniprotkb/P11831) · Ensembl [ENSG00000112658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112658) · OMIM [600589](https://www.omim.org/entry/600589)

**PubMed**, as HGNC records for this gene — [3203386](https://pubmed.ncbi.nlm.nih.gov/3203386/), [7744019](https://pubmed.ncbi.nlm.nih.gov/7744019/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00917 |
| As a percentage | +0.64% |
| FDR, exposure-shuffle null | 0.0086 |
| In TP53-wild-type lines / altered lines | 0.00626 / 0.01094 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.371 raw, 0.124 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 81 targets |
| Activity vs MG53 across exposures (r) | 0.307 (q 1.15e-19) |
| With 3 principal components removed | 0.364 (q 6.08e-26) |
| Within line, across exposures (r) | 0.030 (q 0.134) |
| Percentile against all genes | 99.2 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is expressed at trace level (23.90 CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work; muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
