---
symbol: PYCARD
type: gene
tier: 1
pathway_role: the MG53 locus
aliases: [TMS-1, CARD5, ASC]
gene_name: PYD and CARD domain containing
locus: 16p11.2
locus_type: gene with protein product
gene_family: [Caspase recruitment domain containing, Pyrin domain containing]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PYCARD

*PYD and CARD domain containing* — 16p11.2

> [!summary] In one line
> PYCARD encodes ASC, the two-domain adaptor that bridges inflammasome sensors to caspase-1 — and, for this study, the gene that happens to occupy exactly the same coordinates as PYCARD-AS1 on the opposite strand.

## What it is

ASC is a small bipartite adaptor: a pyrin domain (PYD) at one end, a caspase recruitment domain (CARD) at the other, and essentially nothing else. That architecture is its whole function. The PYD engages the PYD of an activated sensor — NLRP3, AIM2 and others — and the CARD engages pro-caspase-1. ASC senses nothing and cleaves nothing; it converts a sensor's activation into a platform on which caspase-1 can autoactivate.

The platform is literal. ASC polymerises into helical filaments through its PYD, and those filaments condense into the micron-scale perinuclear structure known as the ASC speck, which concentrates caspase-1 to the point where it can process its substrates. Active caspase-1 then matures IL-1β and IL-18 and cleaves gasdermin D, committing the cell to pyroptosis. Mouse knockouts showed the requirement is sensor-specific: some inflammasomes depend absolutely on ASC, while NLRC4 can engage caspase-1 through its own CARD.

The gene was found twice, under names reflecting two different interests. As ASC it was described as a protein that aggregates during apoptosis of a leukaemia line. As TMS1 — target of methylation-induced silencing — it was a pro-apoptotic CARD protein whose promoter is hypermethylated and whose expression is lost in breast cancers. That second identity matters for anyone reading this gene's level in cancer cells: PYCARD is epigenetically silenced in a substantial fraction of tumour lines, so its baseline is not a constant.

## Why it appears in this work

PYCARD is in this vault for its coordinates, not its biology. It lies at 16p11.2 on the minus strand, occupying the same span as [[PYCARD-AS1]] on the plus strand to within a couple of bases, which makes it the control that validates the readthrough argument. Transcription leaking 3′ from the plus-strand genes toward TRIM72 must raise the plus-strand genes and cannot raise PYCARD; if anything it should do the opposite. Two genes at identical coordinates moving in opposite directions is what rules out a mapping smear and shows the quantification respects strand — the load-bearing observation in [[Readthrough spillover]] and [[The TRIM72 locus]]. No inflammasome biology is required for that inference, and none should be read into it.

## What is uncertain

The inflammasome account of ASC is solid, but it was built in myeloid cells, and almost none of it transfers to the setting here. These are pooled epithelial and other non-myeloid cancer lines, many of which have PYCARD methylation-silenced and most of which lack a licensed NLRP3 inflammasome; priming signals that induce the sensors are absent in plain culture. There is therefore no basis for reading PYCARD's level in this dataset as inflammasome activity, and a change in it should not be interpreted as inflammation. Whether ASC's original pro-apoptotic (TMS1) activity is a genuine inflammasome-independent function or a downstream consequence of caspase-1-driven death has never been cleanly settled. Its usefulness as a strand control also rests on the antisense pair being correctly annotated and on the aligner assigning reads by strand — which is what the opposing movement itself tests. The argument is self-checking, but it checks the pipeline, not the biology.

## References

- Masumoto et al., 1999, Journal of Biological Chemistry — described ASC as a 22-kDa protein that aggregates during apoptosis of HL-60 cells.
- Conway et al., 2000, Cancer Research — identified TMS1 as a pro-apoptotic CARD protein silenced by promoter methylation in human breast cancers.
- Martinon et al., 2002, Molecular Cell — defined the inflammasome as a platform activating inflammatory caspases and processing pro-IL-1β.
- Mariathasan et al., 2004, Nature — showed differential requirement for the caspase-1 adaptors ASC and Ipaf across inflammasomes.
- Fernandes-Alnemri et al., 2009, Nature — AIM2 activates an ASC-dependent inflammasome in response to cytoplasmic DNA.
- Lu et al., 2014, Cell — a unified polymerisation mechanism in which ASC forms filaments that assemble the speck.

## What is on record

| | |
|---|---|
| Official name | PYD and CARD domain containing |
| Also known as | TMS-1, CARD5, ASC, apoptosis-associated speck-like, apoptosis-associated speck-like protein containing a CARD |
| Locus | 16p11.2 — gene with protein product |
| Gene families | Caspase recruitment domain containing; Pyrin domain containing |

**Function**, from UniProt [Q9ULZ3](https://www.uniprot.org/uniprotkb/Q9ULZ3) (reviewed):

> Functions as a key mediator in apoptosis and inflammation (PubMed:11103777, PubMed:12646168, PubMed:15030775, PubMed:17349957, PubMed:17599095, PubMed:19158675, PubMed:19158676, PubMed:19234215, PubMed:19494289, PubMed:21487011, PubMed:24630722, PubMed:25847972, PubMed:30674671, PubMed:34678144, PubMed:36050480). Promotes caspase-mediated apoptosis involving predominantly caspase-8 and also caspase-9 in a probable cell type-specific manner (PubMed:11103777, PubMed:12646168). Involved in activation of the mitochondrial apoptotic pathway, promotes caspase-8-dependent proteolytic maturation of BID independently of FADD in certain cell types and also mediates mitochondrial translocation of BAX and activates BAX-dependent apoptosis coupled to activation of caspase-9, -2 and -3 (PubMed:14730312, PubMed:16964285). Involved in innate immune response by acting as an integral adapter in the assembly of various inflammasomes (NLRP1, NLRP2, NLRP3, NLRP6, AIM2 and probably IFI16) which recruit and activate caspase-1 leading to processing and secretion of pro-inflammatory cytokines (PubMed:15030775, PubMed:16982856, PubMed:17349957, PubMed:17599095, PubMed:19158675, PubMed:19158676, PubMed:19234215, PubMed:21487011, PubMed:23530044, PubMed:24630722, PubMed:25847972, PubMed:29440442, PubMed:30674671, PubMed:33980849, PubMed:34678144, PubMed:34706239). Caspase-1-dependent inflammation leads to macrophage pyroptosis, a form of cell death (PubMed:24630722). The function as activating adapter in different types of inflammasomes is mediated by the pyrin and CARD domains and their homotypic interactions (PubMed:14499617, PubMed:19234215, PubMed:24630722). Clustered PYCARD nucleates the formation of caspase-1 filaments through the interaction of their respective CARD domains, acting as a platform for of caspase-1 polymerization (PubMed:24630722). In the NLRP1 and NLRC4 inflammasomes seems not be required but facilitates the processing of procaspase-1 (PubMed:17349957). In cooperation with NOD2 involved in an inflammasome activated by bacterial muramyl dipeptide leading to caspase-1 activation (PubMed:16964285). May be involved in RIGI-triggered pro-inflammatory responses and inflammasome activation (PubMed:19915568). In collaboration with AIM2 which detects cytosolic double-stranded DNA may also be involved in a caspase-1-independent cell death that involves caspase-8 (PubMed:19158675, PubMed:19158676). In adaptive immunity may be involved in maturation of dendritic cells to stimulate T-cell immunity and in cytoskeletal rearrangements coupled to chemotaxis and antigen uptake may be involved in post-transcriptional regulation of the guanine nucleotide exchange factor DOCK2; the latter function is proposed to involve the nuclear form (PubMed:22732093). Also involved in transcriptional activation of cytokines and chemokines independent of the inflammasome; this function may involve AP-1, NF-kappa-B, MAPK and caspase-8 signaling pathways (PubMed:12486103, PubMed:16585594). For regulation of NF-kappa-B activating and inhibiting functions have been reported (PubMed:12486103). Modulates NF-kappa-B induction at the level of the IKK complex by inhibiting kinase activity of CHUK and IKBK (PubMed:12486103, PubMed:16585594). Proposed to compete with RIPK2 for association with CASP1 thereby down-regulating CASP1-mediated RIPK2-dependent NF-kappa-B activation and activating interleukin-1 beta processing (PubMed:16585594). Modulates host resistance to DNA virus infection, probably by inducing the cleavage of and inactivating CGAS in presence of cytoplasmic double-stranded DNA (PubMed:28314590)

**Summary**, from NCBI Gene [29108](https://www.ncbi.nlm.nih.gov/gene/29108):

> This gene encodes an adaptor protein that is composed of two protein-protein interaction domains: a N-terminal PYRIN-PAAD-DAPIN domain (PYD) and a C-terminal caspase-recruitment domain (CARD). The PYD and CARD domains are members of the six-helix bundle death domain-fold superfamily that mediates assembly of large signaling complexes in the inflammatory and apoptotic signaling pathways via the activation of caspase. In normal cells, this protein is localized to the cytoplasm; however, in cells undergoing apoptosis, it forms ball-like aggregates near the nuclear periphery. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16608) · Entrez [29108](https://www.ncbi.nlm.nih.gov/gene/29108) · UniProt [Q9ULZ3](https://www.uniprot.org/uniprotkb/Q9ULZ3) · Ensembl [ENSG00000103490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103490) · OMIM [606838](https://www.omim.org/entry/606838)

**PubMed**, as HGNC records for this gene — [11250163](https://pubmed.ncbi.nlm.nih.gov/11250163/), [10567338](https://pubmed.ncbi.nlm.nih.gov/10567338/), [11103776](https://pubmed.ncbi.nlm.nih.gov/11103776/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*


## Links

- **Concepts:** [[Readthrough spillover]], [[The TRIM72 locus]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
