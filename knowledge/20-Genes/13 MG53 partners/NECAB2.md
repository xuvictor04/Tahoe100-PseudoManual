---
symbol: NECAB2
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
gene_name: N-terminal EF-hand calcium binding protein 2
locus: 16q23.3
locus_type: gene with protein product
gene_family: [N-terminal EF-hand calcium binding proteins, EF-hand domain containing]
family_siblings_here: [DGKA]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# NECAB2

*N-terminal EF-hand calcium binding protein 2* — 16q23.3

> [!summary] In one line
> NECAB2 encodes a neuronal EF-hand calcium-binding protein studied almost exclusively as a modulator of striatal G-protein-coupled receptors.

## What it is

NECAB2 is a roughly 43 kDa cytosolic protein with two EF-hand calcium-binding motifs, a NECAB homology region and a C-terminal antibiotic-monooxygenase (ABM) domain of unknown function — an odd pairing, since the ABM fold is otherwise a bacterial oxidoreductase module. Expression is narrow, enriched in striatum and hippocampal CA2. What functional work exists concerns receptor trafficking. A yeast two-hybrid screen identified NECAB2 as a partner of the adenosine A2A receptor C-terminus, and the interaction was reported to alter the receptor's surface expression, internalisation and downstream MAPK activation; an interaction with mGluR5 has also been described. The evidence is from transfected cells and rodent brain. The gene lies at 16q23.3.

## Why it appears in this work

NECAB2 is here because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector and not a transcription factor, and 16q23.3 is far from the neighbourhood in [[The TRIM72 locus]], so [[Readthrough spillover]] does not explain it.

## What is uncertain

A neuron-restricted transcript in pooled cancer cell lines should sit close to the detection floor, and at that abundance an apparent correlation is as readily produced by ambient RNA or a few lines of unusual lineage as by regulated expression. No link between NECAB2 and p53, calcium-dependent membrane repair or [[MG53 (TRIM72)]] has been reported, so there is no mechanism against which the ranking can be judged. The receptor-modulation findings come from a small literature and, as far as I can establish, are unreplicated.

## References

- Canela et al., 2007 — a yeast two-hybrid screen identified NECAB2 as an adenosine A2A receptor interactor and showed it modulates receptor surface expression and internalisation (journal not verified).

## What is on record

| | |
|---|---|
| Official name | N-terminal EF-hand calcium binding protein 2 |
| Also known as | — (no recorded alias) |
| Locus | 16q23.3 — gene with protein product |
| Gene families | N-terminal EF-hand calcium binding proteins; EF-hand domain containing |
| Other genes here in those families | [[DGKA]] |
| Previously named | EF-hand calcium binding protein 2 |

**Function**, from UniProt [Q7Z6G3](https://www.uniprot.org/uniprotkb/Q7Z6G3) (reviewed):

> May act as a signaling scaffold protein that senses intracellular calcium. Can modulate ligand-induced internalization of ADORA2A and coupling efficiency of mGluR5/GRM5; for both receptors may regulate signaling activity such as promoting MAPK1/3 (ERK1/2) activation

**Summary**, from NCBI Gene [54550](https://www.ncbi.nlm.nih.gov/gene/54550):

> The protein encoded by this gene is a neuronal calcium-binding protein that binds to and modulates the function of at least two receptors, adenosine A(2A) receptor and metabotropic glutamate receptor type 5. [provided by RefSeq, Jul 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:23746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23746) · Entrez [54550](https://www.ncbi.nlm.nih.gov/gene/54550) · UniProt [Q7Z6G3](https://www.uniprot.org/uniprotkb/Q7Z6G3) · Ensembl [ENSG00000103154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103154) · OMIM [618130](https://www.omim.org/entry/618130)

**PubMed**, as HGNC records for this gene — [12044471](https://pubmed.ncbi.nlm.nih.gov/12044471/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.09552 |
| As a percentage | +6.85% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09464 / 0.09602 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.521 raw, 0.305 with 3 PCs removed |

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
