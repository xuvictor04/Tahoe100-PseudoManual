---
symbol: AZU1
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [AZU, CAP37, AZAMP, HBP, NAZC, HUMAZUR]
gene_name: azurocidin 1
locus: 19p13.3
locus_type: gene with protein product
gene_family: [Granule associated serine proteases of immune defence]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# AZU1

*azurocidin 1* — 19p13.3

> [!summary] In one line
> AZU1 encodes azurocidin (CAP37, heparin-binding protein), an antibacterial and chemotactic protein stored in the azurophil granules of neutrophils.

## What it is

Azurocidin is made in promyelocytes and stored in primary granules for release on activation. It folds like an elastase-family serine protease but lacks the catalytic serine and histidine, so it is not an enzyme. It binds heparin and lipopolysaccharide, kills Gram-negative bacteria, attracts monocytes, and increases endothelial permeability — the property behind its use as a sepsis marker. Expression is essentially restricted to bone marrow; the gene lies at 19p13.3 among other azurophil-granule protease genes. No function is established outside the neutrophil lineage, and no link to p53 or to membrane repair is reported.

## Why it appears in this work

AZU1 is not a curated pathway member. It is here because the genome-wide screen ranked it as tracking measured [[MG53 (TRIM72)]] across exposures — a hit with no prior reason to be one. It is not at the TRIM72 locus, so [[Readthrough spillover]] does not apply.

## What is uncertain

Essentially everything that matters here. The transcript sits close to the detection floor, and a promyelocyte-restricted gene reading as weakly present across a pooled cancer-line panel is as easily explained by ambient RNA, or by reads shared with its near-identical neighbours at 19p13.3, as by real expression. Nothing predicts an MG53 relationship, and nothing in this design separates one from a correlation driven by a few lines or by the covariates behind [[Why MG53 is hard to measure here]]. Treat it as a lead for a targeted assay, not a finding.

## References

- Pereira et al., 1990, Journal of Clinical Investigation — characterised CAP37 as a neutrophil-derived chemotactic factor with monocyte specificity.
- Gautam et al., 2001, Nature Medicine — showed heparin-binding protein released from neutrophils causes endothelial hyperpermeability.

## What is on record

| | |
|---|---|
| Official name | azurocidin 1 |
| Also known as | AZU, CAP37, AZAMP, HBP, NAZC, HUMAZUR, cationic antimicrobial protein 37, heparin-binding protein, neutrophil azurocidin |
| Locus | 19p13.3 — gene with protein product |
| Gene families | Granule associated serine proteases of immune defence |

**Function**, from UniProt [P20160](https://www.uniprot.org/uniprotkb/P20160) (reviewed):

> This is a neutrophil granule-derived antibacterial and monocyte- and fibroblast-specific chemotactic glycoprotein. Binds heparin. The cytotoxic action is limited to many species of Gram-negative bacteria; this specificity may be explained by a strong affinity of the very basic N-terminal half for the negatively charged lipopolysaccharides that are unique to the Gram-negative bacterial outer envelope. It may play a role in mediating recruitment of monocytes in the second wave of inflammation. Has antibacterial activity against the Gram-negative bacterium P.aeruginosa, this activity is inhibited by LPS from P.aeruginosa. Acting alone, it does not have antimicrobial activity against the Gram-negative bacteria A.actinomycetemcomitans ATCC 29532, A.actinomycetemcomitans NCTC 9709, A.actinomycetemcomitans FDC-Y4, H.aphrophilus ATCC 13252, E.corrodens ATCC 23834, C.sputigena ATCC 33123, Capnocytophaga sp ATCC 33124, Capnocytophaga sp ATCC 27872 or E.coli ML-35. Has antibacterial activity against C.sputigena ATCC 33123 when acting synergistically with either elastase or cathepsin G

**Summary**, from NCBI Gene [566](https://www.ncbi.nlm.nih.gov/gene/566):

> Azurophil granules, specialized lysosomes of the neutrophil, contain at least 10 proteins implicated in the killing of microorganisms. This gene encodes a preproprotein that is proteolytically processed to generate a mature azurophil granule antibiotic protein, with monocyte chemotactic and antimicrobial activity. It is also an important multifunctional inflammatory mediator. This encoded protein is a member of the serine protease gene family but it is not a serine proteinase, because the active site serine and histidine residues are replaced. The genes encoding this protein, neutrophil elastase 2, and proteinase 3 are in a cluster located at chromosome 19pter. All 3 genes are expressed coordinately and their protein products are packaged together into azurophil granules during neutrophil differentiation. [provided by RefSeq, Nov 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:913) · Entrez [566](https://www.ncbi.nlm.nih.gov/gene/566) · UniProt [P20160](https://www.uniprot.org/uniprotkb/P20160) · Ensembl [ENSG00000172232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172232) · OMIM [162815](https://www.omim.org/entry/162815)

**PubMed**, as HGNC records for this gene — [1919011](https://pubmed.ncbi.nlm.nih.gov/1919011/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.11227 |
| As a percentage | +8.09% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.12103 / 0.10695 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.673 raw, 0.606 with 3 PCs removed |

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
