---
symbol: MDM4
type: gene
tier: 1
pathway_role: p53 itself and what controls it
aliases: [MDMX, HDMX]
gene_name: MDM4 regulator of p53
locus: 1q32.1
locus_type: gene with protein product
gene_family: [Ring finger proteins, Zinc fingers RANBP2-type, RING finger E3 ubiquitin protein ligases]
family_siblings_here: [COP1, FUS, MDM2, MGRN1, PCGF3, RC3H1, TAB3, TRIM72]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# MDM4

*MDM4 regulator of p53* — 1q32.1

> [!summary] In one line
> MDM4 — better known in the literature as MDMX or HDMX — is MDM2's paralogue and the second brake on p53: it occludes p53's transactivation domain but, unlike MDM2, is not itself an efficient ubiquitin ligase for p53.

## What it is

MDM4 is built on the same plan as [[MDM2]]: an N-terminal pocket binding the p53 transactivation domain, a central acidic region, and a C-terminal RING. It was found as MDMX, a p53-binding protein with some of MDM2's functional properties.

The asymmetry is at the RING. MDM4's has little demonstrable intrinsic ligase activity toward p53, and instead heterodimerises with MDM2's RING to stimulate MDM2-dependent p53 ubiquitination. MDM4 therefore restrains p53 by two largely non-catalytic routes — blocking the transactivation domain, and setting how well MDM2 works.

Like *Mdm2*-null, *Mdm4*-null embryos die and are rescued by loss of *Trp53*, so MDM4's essential job is also p53 restraint — but the null phenotype differs in timing and tissue bias, read as evidence for non-overlapping control rather than redundancy.

In cancer MDM4 is amplified and overexpressed rather than mutated, concentrated as with MDM2 in tumours that retain wild-type TP53 — retinoblastoma, glioma, and cutaneous melanoma, where it was argued to be a therapeutic target. Splicing is distinctive to this gene: skipping exon 6 yields an unstable short isoform at the expense of full-length protein, and forcing that skipping with antisense oligonucleotides restrains tumour growth — a mechanism with no close MDM2 parallel.

Transcriptionally MDM4 is mostly constitutive, driven from its upstream P1 promoter, but a p53-responsive promoter in the first intron drives a longer isoform, giving MDM4 a weaker version of MDM2's feedback topology.

## Why it appears in this work

MDM4 completes the brake layer: an account of p53 output that names MDM2 and stops there describes half the restraint. Its value here is as a contrast. MDM2 is transcriptionally coupled to p53 through a strong intronic response element and behaves accordingly in [[p53 program P]]; MDM4's coupling is weak and its control is predominantly post-translational — RING partnership, splicing, protein stability. For a study that reads p53 engagement from mRNA, MDM4 is the standing reminder that a regulator can be fully engaged, or fully disengaged, with its transcript barely moving. Whatever the generated block carries here, that asymmetry is why a thin measurement is the expected result.

## What is uncertain

Whether MDM4's RING has any physiologically meaningful ligase activity toward p53 on its own has been argued both ways; the safe statement is that its contribution to p53 turnover runs mainly through MDM2. The division of labour between the paralogues is genuinely unsettled: the differing null phenotypes are compatible with distinct functions and with one function deployed at different times and places, and the literature reads them both ways. MDM4 sits at 1q32, in an arm gained in many epithelial cancers, so an "MDM4 amplification" in copy-number data is often a passenger of 1q gain; attributing a phenotype to MDM4 needs functional experiments, not copy number. The intronic p53-responsive promoter rests on limited work, and how much of total MDM4 mRNA it contributes in an ordinary cell is not established. Finally, a practical caution: most primary papers call this gene MDMX or HDMX, so a literature search on the approved symbol alone misses much of its own literature.

## References

- Shvarts et al., 1996, The EMBO Journal — identified MDMX as a p53-binding protein with some functional properties of MDM2.
- Parant et al., 2001, Nature Genetics — rescue of *Mdm4*-null embryonic lethality by loss of *Trp53*, argued to indicate a pathway not overlapping MDM2's.
- Linares et al., 2003, PNAS — HdmX stimulates Hdm2-mediated ubiquitination and degradation of p53.
- Phillips et al., 2010, Journal of Biological Chemistry — a functional p53-responsive promoter in the first intron drives the longer HDMX-L isoform.
- Gembarska et al., 2012, Nature Medicine — MDM4 as a therapeutic target in cutaneous melanoma.
- Dewaele et al., 2016, Journal of Clinical Investigation — antisense-driven MDM4 exon 6 skipping lowers full-length MDM4 and impairs tumour growth.

## What is on record

| | |
|---|---|
| Official name | MDM4 regulator of p53 |
| Also known as | MDMX, HDMX |
| Locus | 1q32.1 — gene with protein product |
| Gene families | Ring finger proteins; Zinc fingers RANBP2-type; RING finger E3 ubiquitin protein ligases |
| Other genes here in those families | [[COP1]], [[FUS]], [[MDM2]], [[MGRN1]], [[PCGF3]], [[RC3H1]], [[TAB3]], [[TRIM72]] |
| Previously named | mouse double minute 4, human homolog of; p53-binding protein; Mdm4, transformed 3T3 cell double minute 4, p53 binding protein (mouse); Mdm4 p53 binding protein homolog (mouse); MDM4, p53 regulator |

**Function**, from UniProt [O15151](https://www.uniprot.org/uniprotkb/O15151) (reviewed):

> Contributes to p53/TP53 regulation (PubMed:32300648). Inhibits p53/TP53- and p73/TP73-mediated cell cycle arrest and apoptosis by binding their transcriptional activation domains. Inhibits degradation of MDM2. Can reverse MDM2-targeted degradation of TP53 while maintaining suppression of TP53 transactivation and apoptotic functions

**Summary**, from NCBI Gene [4194](https://www.ncbi.nlm.nih.gov/gene/4194):

> This gene encodes a nuclear protein that contains a p53 binding domain at the N-terminus and a RING finger domain at the C-terminus, and shows structural similarity to p53-binding protein MDM2. Both proteins bind the p53 tumor suppressor protein and inhibit its activity, and have been shown to be overexpressed in a variety of human cancers. However, unlike MDM2 which degrades p53, this protein inhibits p53 by binding its transcriptional activation domain. This protein also interacts with MDM2 protein via the RING finger domain, and inhibits the latter's degradation. So this protein can reverse MDM2-targeted degradation of p53, while maintaining suppression of p53 transactivation and apoptotic functions. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Feb 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6974) · Entrez [4194](https://www.ncbi.nlm.nih.gov/gene/4194) · UniProt [O15151](https://www.uniprot.org/uniprotkb/O15151) · Ensembl [ENSG00000198625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198625) · OMIM [602704](https://www.omim.org/entry/602704)

**PubMed**, as HGNC records for this gene — [9226370](https://pubmed.ncbi.nlm.nih.gov/9226370/), [14660608](https://pubmed.ncbi.nlm.nih.gov/14660608/), [26798135](https://pubmed.ncbi.nlm.nih.gov/26798135/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00188 |
| As a percentage | -0.13% |
| FDR, exposure-shuffle null | 0.2411 |
| In TP53-wild-type lines / altered lines | -0.00079 / -0.00255 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.116 raw, -0.032 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
