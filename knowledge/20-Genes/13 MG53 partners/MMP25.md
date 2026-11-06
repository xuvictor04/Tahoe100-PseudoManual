---
symbol: MMP25
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [MT6-MMP]
gene_name: matrix metallopeptidase 25
locus: 16p13.3
locus_type: gene with protein product
gene_family: [M10 matrix metallopeptidases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# MMP25

*matrix metallopeptidase 25* — 16p13.3

> [!summary] In one line
> MMP25 encodes MT6-MMP, or leukolysin, a GPI-anchored membrane-type matrix metalloproteinase whose expression is essentially confined to the leukocyte lineage.

## What it is

MMP25 was cloned from leukocytes and found, across a panel of tissues, in peripheral blood leukocytes and almost nowhere else. It carries the standard metalloproteinase architecture but is tethered to the outer face of the plasma membrane by a glycosylphosphatidylinositol anchor rather than a transmembrane helix, a feature it shares only with MT4-MMP (MMP17) among the membrane-type enzymes. In resting neutrophils the protein sits in specific and gelatinase granules, secretory vesicles and the plasma membrane, and is mobilised to the surface on stimulation. It degrades matrix substrates in vitro and has been reported to activate progelatinase A at the cell surface. The gene lies at 16p13.3.

## Why it appears in this work

MMP25 is here because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector and not a transcription factor, and 16p13.3 is tens of megabases from the neighbourhood in [[The TRIM72 locus]], so [[Readthrough spillover]] does not account for it.

## What is uncertain

The first problem is whether the transcript is really there. A gene this restricted to neutrophils should read near zero in pooled epithelial and mesenchymal cancer lines, so a usable signal is as plausibly ambient RNA or low-level ectopic transcription as genuine expression. Nothing links MMP25 to p53 or to membrane repair, and its reported tumour roles rest on few studies.

## References

- Pei, 1999, Cell Research — cloned leukolysin/MMP25 and showed its expression is restricted to the leukocyte lineage.
- Kang et al., 2001, Journal of Biological Chemistry — localised leukolysin to neutrophil granule compartments and showed its mobilisation on stimulation.

## What is on record

| | |
|---|---|
| Official name | matrix metallopeptidase 25 |
| Also known as | MT6-MMP |
| Locus | 16p13.3 — gene with protein product |
| Gene families | M10 matrix metallopeptidases |
| Previously named | matrix metalloproteinase 25; matrix metallopeptidase-like 1 |

**Function**, from UniProt [Q9NPA2](https://www.uniprot.org/uniprotkb/Q9NPA2) (reviewed):

> May activate progelatinase A

**Summary**, from NCBI Gene [64386](https://www.ncbi.nlm.nih.gov/gene/64386):

> Proteins of the matrix metalloproteinase (MMP) family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Most MMPs are secreted as inactive proproteins which are activated when cleaved by extracellular proteinases. However, the protein encoded by this gene is a member of the membrane-type MMP (MT-MMP) subfamily, attached to the plasma membrane via a glycosylphosphatidyl inositol anchor. In response to bacterial infection or inflammation, the encoded protein is thought to inactivate alpha-1 proteinase inhibitor, a major tissue protectant against proteolytic enzymes released by activated neutrophils, facilitating the transendothelial migration of neutrophils to inflammatory sites. The encoded protein may also play a role in tumor invasion and metastasis through activation of MMP2. The gene has previously been referred to as MMP20 but has been renamed MMP25. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:14246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14246) · Entrez [64386](https://www.ncbi.nlm.nih.gov/gene/64386) · UniProt [Q9NPA2](https://www.uniprot.org/uniprotkb/Q9NPA2) · Ensembl [ENSG00000008516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008516) · OMIM [608482](https://www.omim.org/entry/608482)

**PubMed**, as HGNC records for this gene — [10628838](https://pubmed.ncbi.nlm.nih.gov/10628838/), [10706098](https://pubmed.ncbi.nlm.nih.gov/10706098/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.11364 |
| As a percentage | +8.20% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.12876 / 0.10447 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.644 raw, 0.477 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
