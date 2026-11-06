---
symbol: GRAMD2A
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
gene_name: GRAM domain containing 2A
locus: 15q23
locus_type: gene with protein product
gene_family: [GRAM domain containing]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# GRAMD2A

*GRAM domain containing 2A* — 15q23

> [!summary] In one line
> GRAMD2A encodes a tail-anchored ER protein reported to tether the endoplasmic reticulum to PI(4,5)P2-rich patches of the plasma membrane, and nearly all of what is known about it comes from one study.

## What it is

GRAMD2A, formerly GRAMD2, sits at 15q23. Its product is anchored in the ER membrane and presents a cytosolic GRAM domain that binds PI(4,5)P2, and that preference confines it to a subset of ER-plasma-membrane contact sites distinct from those held by the GRAMD1/Aster sterol transporters, alongside the extended synaptotagmins E-Syt2 and E-Syt3. The same work proposed it pre-marks the sites where STIM1 accumulates during store-operated calcium entry, making it an organiser of contact-site identity rather than a transporter. Its kinship to the yeast Lam/Ltc sterol-transfer proteins is domain homology only; no transfer activity has been shown, there is no animal knockout, and expression is low and uneven.

## Why it appears in this work

GRAMD2A is here only because the genome-wide screen ranked it as tracking measured MG53. The coincidence deserves naming — [[MG53 (TRIM72)]] acts at the injured plasma membrane and this organises plasma-membrane contact sites — but naming it is as far as this design reaches. At 15q23 it is far from TRIM72, so [[Readthrough spillover]] cannot account for it.

## What is uncertain

This is effectively a one-paper gene, and that paper's most interesting claim is its least settled: reviewers noted roughly half of STIM1 puncta formed at sites GRAMD2A did not mark. Antibody staining in the Human Protein Atlas puts the protein in nucleoli and nuclear speckles, irreconcilable with a tail-anchored ER tether; one localisation is wrong, most likely the antibody's. Nothing links the gene to p53, and at the level seen here ambient RNA stays live; see [[Why MG53 is hard to measure here]].

## References

- Besprozvannaya et al., 2018, eLife — showed GRAMD2a marks a PI(4,5)P2-dependent subset of ER-PM contact sites distinct from GRAMD1a's, and proposed a role in STIM1 recruitment.

## What is on record

| | |
|---|---|
| Official name | GRAM domain containing 2A |
| Also known as | — (no recorded alias) |
| Locus | 15q23 — gene with protein product |
| Gene families | GRAM domain containing |
| Previously named | GRAM domain containing 2 |

**Function**, from UniProt [Q8IUY3](https://www.uniprot.org/uniprotkb/Q8IUY3) (reviewed):

> Participates in the organization of endoplasmic reticulum-plasma membrane contact sites (EPCS) with pleiotropic functions including STIM1 recruitment and calcium homeostasis. Constitutive tether that co-localizes with ESYT2/3 tethers at endoplasmic reticulum-plasma membrane contact sites in a phosphatidylinositol lipid-dependent manner. Pre-marks the subset of phosphatidylinositol 4,5-biphosphate (PI(4,5)P2)-enriched EPCS destined for the store-operated calcium entry pathway (SOCE)

**Summary**, from NCBI Gene [196996](https://www.ncbi.nlm.nih.gov/gene/196996):

> Enables phosphatidylinositol binding activity and phosphatidylinositol-4,5-bisphosphate binding activity. Involved in endoplasmic reticulum-plasma membrane tethering and regulation of store-operated calcium entry. Located in endoplasmic reticulum membrane; organelle membrane contact site; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:27287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27287) · Entrez [196996](https://www.ncbi.nlm.nih.gov/gene/196996) · UniProt [Q8IUY3](https://www.uniprot.org/uniprotkb/Q8IUY3) · Ensembl [ENSG00000175318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175318) · OMIM [620181](https://www.omim.org/entry/620181)

**PubMed**, as HGNC records for this gene — [29469807](https://pubmed.ncbi.nlm.nih.gov/29469807/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.10794 |
| As a percentage | +7.77% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.11489 / 0.10373 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.723 raw, 0.520 with 3 PCs removed |

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
