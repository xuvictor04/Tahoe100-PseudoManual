---
symbol: MEF2C
type: gene
tier: 1
pathway_role: transcription factor, muscle programme
gene_name: myocyte enhancer factor 2C
locus: 5q14.3
locus_type: gene with protein product
gene_family: [Myocyte enhancer factor 2 proteins, MADS box family]
family_siblings_here: [MEF2A, MEF2B, MEF2D, SRF]
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MEF2C

*myocyte enhancer factor 2C* — 5q14.3

> [!summary] In one line
> MEF2C is a MADS-box transcription factor that licenses the muscle, cardiac and neuronal differentiation programmes, acting as an amplifier of lineage master regulators rather than as a master regulator itself.

## What it is

MEF2C is one of four vertebrate MEF2 proteins ([[MEF2A]], [[MEF2B]], MEF2C, [[MEF2D]]). All share an N-terminal MADS box and adjacent MEF2 domain, which handle DNA binding at an A/T-rich consensus, dimerisation and cofactor contact; the C-terminal half carries transactivation and most regulatory sequence.

MEF2C is not a determination factor on its own — it cannot convert a fibroblast into a myoblast the way [[MYOD1]] can. Its characteristic behaviour is combinatorial: it binds adjacent to myogenic bHLH factors and the pair activate transcription far beyond additivity, through a direct MADS-to-bHLH contact. Because MEF2 sites sit in the promoters of the myogenic regulatory factors and beside E-boxes in muscle structural genes, MEF2C and MyoD form a feed-forward loop that locks the differentiated state in.

Its regulation is largely post-transcriptional, which matters for anyone inferring activity from mRNA. Class IIa histone deacetylases — HDAC4, [[HDAC5]], HDAC7, HDAC9 — bind the MADS/MEF2 surface and hold MEF2 silent; calcium-dependent kinase signalling phosphorylates them, exports them from the nucleus, and frees MEF2 to recruit p300/CBP. p38 MAPK, ERK5 and calcineurin feed into the same switch.

Among the paralogues MEF2C has the most severe loss-of-function phenotype: null embryos fail heart-tube looping and never form a right ventricle. In humans, MEF2C haploinsufficiency from 5q14.3 deletion or point mutation causes severe intellectual disability with epilepsy and absent speech. In cancer, high MEF2C marks an immature subtype of T-cell acute lymphoblastic leukaemia, arising from rearrangement of MEF2C itself or of factors upstream of it.

## Why it appears in this work

MEF2 is not a guess about [[MG53 (TRIM72)]]. The TRIM72 promoter carries a conserved MEF2 site immediately beside an E-box, and MyoD and MEF2 activate it synergistically in differentiating myoblasts. MEF2C therefore belongs to the short list of factors that would be the first explanation for MG53's behaviour if these cells were muscle. Including it tests that explanation and watches it fail: the muscle programme is not running in this panel, which is why [[Transcription factor activity inference]] reaches a negative answer and [[The TRIM72 locus]] carries the explanation instead.

## What is uncertain

Which MEF2 paralogue acts at the TRIM72 promoter is unsettled: the reporter work established a functional MEF2 site, not which of the four occupies it in a cell. MEF2C's transcript is also a poor proxy for its activity, since HDAC gating is the real switch — and unlike the myogenic bHLH factors MEF2C is expressed in this panel, so its presence is only weak evidence that the protein is doing anything. MEF2C regulons are drawn from muscle, heart, neuronal and immune contexts and overlap generic stress programmes, so an activity score here can track what those targets do for other reasons. Nothing perturbs MEF2C in this dataset in any case, so direction was never available.

## References

- Molkentin et al., 1995, Cell — showed cooperative, more-than-additive activation of muscle genes by MEF2 and myogenic bHLH factors through a direct MADS–bHLH contact.
- Lin et al., 1997, Science — Mef2c-null mouse embryos fail cardiac looping and do not form a right ventricle.
- McKinsey et al., 2000, Nature — signal-dependent nuclear export of a class II histone deacetylase releases MEF2 and permits muscle differentiation.
- Potthoff and Olson, 2007, Development — review of MEF2 as a combinatorial regulator across developmental programmes.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — the TRIM72 promoter has a conserved MEF2 site next to an E-box, and MyoD (or myogenin) plus MEF2 activate it synergistically.
- Homminga et al., 2011, Cancer Cell — high MEF2C expression defines an immature T-ALL subtype, activated by rearrangement of MEF2C or of its upstream regulators.

## What is on record

| | |
|---|---|
| Official name | myocyte enhancer factor 2C |
| Also known as | — (no recorded alias) |
| Locus | 5q14.3 — gene with protein product |
| Gene families | Myocyte enhancer factor 2 proteins; MADS box family |
| Other genes here in those families | [[MEF2A]], [[MEF2B]], [[MEF2D]], [[SRF]] |

**Function**, from UniProt [Q06413](https://www.uniprot.org/uniprotkb/Q06413) (reviewed):

> Transcription activator which binds specifically to the MEF2 element present in the regulatory regions of many muscle-specific genes. Controls cardiac morphogenesis and myogenesis, and is also involved in vascular development. Enhances transcriptional activation mediated by SOX18. Plays an essential role in hippocampal-dependent learning and memory by suppressing the number of excitatory synapses and thus regulating basal and evoked synaptic transmission. Crucial for normal neuronal development, distribution, and electrical activity in the neocortex. Necessary for proper development of megakaryocytes and platelets and for bone marrow B-lymphopoiesis. Required for B-cell survival and proliferation in response to BCR stimulation, efficient IgG1 antibody responses to T-cell-dependent antigens and for normal induction of germinal center B-cells. May also be involved in neurogenesis and in the development of cortical architecture (By similarity). Isoforms that lack the repressor domain are more active than isoform 1

**Summary**, from NCBI Gene [4208](https://www.ncbi.nlm.nih.gov/gene/4208):

> This locus encodes a member of the MADS box transcription enhancer factor 2 (MEF2) family of proteins, which play a role in myogenesis. The encoded protein, MEF2 polypeptide C, has both trans-activating and DNA binding activities. This protein may play a role in maintaining the differentiated state of muscle cells. Mutations and deletions at this locus have been associated with severe cognitive disability, stereotypic movements, epilepsy, and cerebral malformation. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jul 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6996) · Entrez [4208](https://www.ncbi.nlm.nih.gov/gene/4208) · UniProt [Q06413](https://www.uniprot.org/uniprotkb/Q06413) · Ensembl [ENSG00000081189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081189) · OMIM [600662](https://www.omim.org/entry/600662)

**PubMed**, as HGNC records for this gene — [8455629](https://pubmed.ncbi.nlm.nih.gov/8455629/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00160 |
| As a percentage | -0.11% |
| FDR, exposure-shuffle null | 0.7981 |
| In TP53-wild-type lines / altered lines | 0.00225 / -0.00371 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.094 raw, -0.134 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 43 targets |
| Activity vs MG53 across exposures (r) | 0.207 (q 1.30e-09) |
| With 3 principal components removed | 0.349 (q 6.63e-24) |
| Within line, across exposures (r) | 0.036 (q 0.023) |
| Percentile against all genes | 98.3 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is expressed at trace level (21.85 CPM), which is why the muscle programme is not what moves MG53 here.

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
