---
symbol: ELK4
type: gene
tier: 2
pathway_role: transcription factor
aliases: [SAP1]
gene_name: ETS transcription factor ELK4
locus: 1q32.1
locus_type: gene with protein product
gene_family: [ETS transcription factor family]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ELK4

*ETS transcription factor ELK4* — 1q32.1

> [!summary] In one line
> ELK4 (SAP-1) is a ternary complex factor: an ETS-domain protein that docks onto DNA-bound SRF to carry growth-factor signals to serum response elements.

## What it is

ELK4 is one of three ternary complex factors, with ELK1 and ELK3, and was isolated as a protein recruited by serum response factor to the c-fos SRE; it cannot occupy its site unless SRF is bound: its B-box contacts the SRF dimer while its ETS domain contacts a GGA(A/T) motif beside the CArG box. ERK phosphorylation of C-terminal sites converts it into an activator, carrying mitogen signalling to immediate-early genes such as FOS and EGR1. The TCFs compete with the myocardin/MRTF family for the same surface on [[SRF]], switching it between mitogenic and cytoskeletal programmes. A recurrent SLC45A3-ELK4 chimeric transcript occurs in prostate cancer.

## Why it appears in this work

ELK4 ranks at the top of the regulon-based activity step, and is entangled with [[SRF]], a candidate native-tissue regulator of [[MG53 (TRIM72)]] in this vault. They share CArG-box targets by construction, so a ranking placing both high reports one body of overlapping evidence. See [[Transcription factor activity inference]].

## What is uncertain

ELK4's regulon here is among the smallest of any factor scored, making its activity close to an average over a handful of immediate-early transcripts — and those move under nearly any perturbation, so a high rank across this compound panel may report generic stress. The score is not separable from ELK1 or SRF. Nothing links ELK4 to TRIM72: the one characterised element there is a MEF2 site beside an E-box, with no CArG or Ets element described.

## References

- Dalton & Treisman, 1992, Cell — characterised SAP-1 as a protein recruited by serum response factor to the c-fos serum response element.
- Mo et al., 2001, Journal of Molecular Biology — crystal structure of a ternary SAP-1/SRF/c-fos SRE DNA complex.
- Rickman et al., 2009, Cancer Research — identified SLC45A3-ELK4 as a recurrent chimeric transcript in prostate cancer.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by the synergism of MyoD (or myogenin) with MEF2.

## What is on record

| | |
|---|---|
| Official name | ETS transcription factor ELK4 |
| Also known as | SAP1, SRF accessory protein 1 |
| Locus | 1q32.1 — gene with protein product |
| Gene families | ETS transcription factor family |
| Previously named | ELK4, ETS-domain protein (SRF accessory protein 1) |

**Function**, from UniProt [P28324](https://www.uniprot.org/uniprotkb/P28324) (reviewed):

> Involved in both transcriptional activation and repression. Interaction with SIRT7 leads to recruitment and stabilization of SIRT7 at promoters, followed by deacetylation of histone H3 at 'Lys-18' (H3K18Ac) and subsequent transcription repression. Forms a ternary complex with the serum response factor (SRF). Requires DNA-bound SRF for ternary complex formation and makes extensive DNA contacts to the 5'side of SRF, but does not bind DNA autonomously

**Summary**, from NCBI Gene [2005](https://www.ncbi.nlm.nih.gov/gene/2005):

> This gene is a member of the Ets family of transcription factors and of the ternary complex factor (TCF) subfamily. Proteins of the TCF subfamily form a ternary complex by binding to the the serum response factor and the serum reponse element in the promoter of the c-fos proto-oncogene. The protein encoded by this gene is phosphorylated by the kinases, MAPK1 and MAPK8. Several transcript variants have been described for this gene. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:3326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3326) · Entrez [2005](https://www.ncbi.nlm.nih.gov/gene/2005) · UniProt [P28324](https://www.uniprot.org/uniprotkb/P28324) · Ensembl [ENSG00000158711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158711) · OMIM [600246](https://www.omim.org/entry/600246)

**PubMed**, as HGNC records for this gene — [7851904](https://pubmed.ncbi.nlm.nih.gov/7851904/), [8575773](https://pubmed.ncbi.nlm.nih.gov/8575773/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00229 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.2251 |
| In TP53-wild-type lines / altered lines | 0.00303 / 0.00184 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.018 raw, 0.156 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 6 targets |
| Activity vs MG53 across exposures (r) | 0.346 (q 2.63e-22) |
| With 3 principal components removed | 0.461 (q 3.71e-38) |
| Within line, across exposures (r) | 0.046 (q 0.193) |
| Percentile against all genes | 99.1 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
