---
symbol: SCUBE2
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [Cegf1, Cegb1, FLJ16792]
gene_name: signal peptide, CUB domain and EGF like domain containing 2
locus: 11p15.4
locus_type: gene with protein product
gene_family: [MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SCUBE2

*signal peptide, CUB domain and EGF like domain containing 2* — 11p15.4

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SCUBE2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | signal peptide, CUB domain and EGF like domain containing 2 |
| Also known as | Cegf1, Cegb1, FLJ16792 |
| Locus | 11p15.4 — gene with protein product |
| Gene families | MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]] |
| Previously named | signal peptide, CUB domain, EGF-like 2 |

**Function**, from UniProt [Q9NQ36](https://www.uniprot.org/uniprotkb/Q9NQ36) (reviewed):

> Lipid-binding protein carrier required for sonic hedgehog (SHH) long-range signaling: binds to the dually lipid-modified Sonic hedgehog protein N-product (ShhN) and promotes its release from producing cells, allowing it to act as a morphogen for distant signaling (PubMed:19480626, PubMed:22677548, PubMed:22902404, PubMed:35231446). ShhN is then transferred to the CDON-BOC heterodimer and GAS1 coreceptors to reach its target, the patched receptor (PTCH1 or PTCH2), followed by activation of the smoothened signaling pathway (PubMed:35231446). May also enhance the proteolytic processing (shedding) of the lipid-modified N- and C- terminal of ShhNp at the cell surface (PubMed:24522195). Synergizes with DISP1 to increase SHH secretion (PubMed:22902404). Probable cell surface coreceptor for VEGFR2 involved in VEGFR2-mediated angiogenesis (PubMed:27834687)

**Summary**, from NCBI Gene [57758](https://www.ncbi.nlm.nih.gov/gene/57758):

> Predicted to enable hedgehog family protein binding activity. Predicted to be involved in signal transduction. Predicted to act upstream of or within several processes, including positive regulation of chondrocyte proliferation; positive regulation of osteoblast differentiation; and positive regulation of smoothened signaling pathway. Predicted to be located in extracellular region. Predicted to be active in cell surface and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30425) · Entrez [57758](https://www.ncbi.nlm.nih.gov/gene/57758) · UniProt [Q9NQ36](https://www.uniprot.org/uniprotkb/Q9NQ36) · Ensembl [ENSG00000175356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175356) · OMIM [611747](https://www.omim.org/entry/611747)

**PubMed**, as HGNC records for this gene — [12270931](https://pubmed.ncbi.nlm.nih.gov/12270931/), [11528127](https://pubmed.ncbi.nlm.nih.gov/11528127/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06310 |
| As a percentage | +4.47% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06034 / 0.06518 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.411 raw, 0.441 with 3 PCs removed |

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
