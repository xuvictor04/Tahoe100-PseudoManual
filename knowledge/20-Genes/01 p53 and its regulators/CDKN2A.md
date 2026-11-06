---
symbol: CDKN2A
type: gene
tier: 1
pathway_role: p53 itself and what controls it
aliases: [p16, ARF, p14ARF]
gene_name: cyclin dependent kinase inhibitor 2A
locus: 9p21.3
locus_type: gene with protein product
gene_family: [Cyclin dependent kinase inhibitor 2 family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CDKN2A

*cyclin dependent kinase inhibitor 2A* — 9p21.3

> [!summary] In one line
> CDKN2A is not one gene but one locus encoding two unrelated tumour suppressors from overlapping exons — p16^INK4a^, which holds the RB pathway on, and p14ARF, which stabilises p53 by inhibiting MDM2.

## What it is

The locus uses alternative first exons and two reading frames across shared exons 2 and 3. Transcripts beginning at exon 1α give p16^INK4a^, an INK4-family inhibitor of CDK4 and CDK6; blocking those kinases keeps RB hypophosphorylated and E2F targets off, so p16 acts entirely within the RB arm of cell-cycle control. Transcripts beginning at exon 1β are read in a different frame (hence ARF, alternative reading frame) to give p14ARF — in mouse, p19Arf — a nucleolar protein with no relationship to p16 in sequence or structure. ARF binds MDM2, sequesters and inhibits it, and so blocks MDM2-mediated ubiquitination of p53, stabilising it. Critically, ARF is induced by oncogenic signalling — E2F, MYC, RAS — which makes it the route by which hyperproliferative signals, rather than DNA damage, activate p53. One locus therefore feeds both of the two pathways most often broken in human cancer.

CDKN2A is among the most frequently inactivated regions in the cancer genome: homozygous deletion, promoter methylation and point mutation all occur, and germline mutation underlies familial melanoma. The deletions are often large, and commonly remove the neighbouring MTAP gene — the basis for the MAT2A and PRMT5 synthetic-lethality strategies now pursued in MTAP-deleted tumours. In cultured cancer cell lines the locus is lost at high frequency, which matters more here than its mutation spectrum.

## Why it appears in this work

In a panel of 50 pooled cancer cell lines, CDKN2A status is one of the main ways the p53 pathway is disabled without TP53 itself being touched. A line can be TP53-wild-type by sequence and still mount a blunted response, because the oncogene-sensing input through p14ARF has been deleted. That is directly relevant to [[p53 nullification in cancer cell lines]] and to how much weight a wild-type-versus-altered split can carry: the split is defined on TP53, and CDKN2A is a reason two wild-type lines need not behave alike. CDKN2A is not itself a p53 target, so it belongs to the upstream and contextual layer of this vault rather than to [[p53 program P]].

## What is uncertain

The most important caveat is measurement, not biology: a gene-level expression count for CDKN2A collapses p16 and p14ARF, two proteins acting on different pathways, because they share most of their exons. A CDKN2A number is ambiguous by construction unless the exon-1α and exon-1β transcripts are resolved, which short-read 3′ single-cell data generally cannot do. In lines where the locus is deleted, low counts report copy loss rather than regulation, and the deletion also removes MTAP, so neighbouring-gene signals are not independent. On the biology, how much of ARF's tumour-suppressive activity runs through p53 is genuinely contested — p53-independent ARF functions have been described in both mouse and human systems — and the mouse-to-human mapping is imperfect enough that murine p19Arf results do not transfer cleanly.

## References

- Serrano, Hannon & Beach, 1993, Nature — identified p16 as a specific inhibitor of cyclin D/CDK4.
- Kamb et al., 1994, Science — mapped the locus as a cell-cycle regulator deleted across many tumour types.
- Quelle et al., 1995, Cell — showed the alternative reading frames of INK4a encode two unrelated growth-arresting proteins.
- Pomerantz et al., 1998, Cell — ARF interacts with MDM2 and neutralises its inhibition of p53.
- Zhang, Xiong & Yarbrough, 1998, Cell — ARF promotes MDM2 degradation and stabilises p53, so locus deletion impairs both the RB and p53 pathways.
- Sherr, 2006, Nature Reviews Cancer — argued the case for p53-independent ARF functions is unsettled.

## What is on record

| | |
|---|---|
| Official name | cyclin dependent kinase inhibitor 2A |
| Also known as | CDK4I, p16, INK4a, MTS1, CMM2, ARF, p19, p14, INK4, p16INK4a, p19Arf, p14ARF, P16-INK4A, CAI2, CDKN2A/ARF Intron 2 lncRNA, multiple tumour suppressor 1, cyclin-dependent kinase 4 inhibitor A, p19 alternate open reading frame, p14 alternate open reading frame, inhibitor of cdk4 A |
| Locus | 9p21.3 — gene with protein product |
| Gene families | Cyclin dependent kinase inhibitor 2 family |
| Previously named | cyclin-dependent kinase inhibitor 2A (melanoma, p16, inhibits CDK4) |

**Function**, from UniProt [P42771](https://www.uniprot.org/uniprotkb/P42771) (reviewed):

> Acts as a negative regulator of the proliferation of normal cells by interacting strongly with CDK4 and CDK6. This inhibits their ability to interact with cyclins D and to phosphorylate the retinoblastoma protein

**Summary**, from NCBI Gene [1029](https://www.ncbi.nlm.nih.gov/gene/1029):

> This gene generates several transcript variants which differ in their first exons. At least three alternatively spliced variants encoding distinct proteins have been reported, two of which encode structurally related isoforms known to function as inhibitors of CDK4 kinase. The remaining transcript includes an alternate first exon located 20 Kb upstream of the remainder of the gene; this transcript contains an alternate open reading frame (ARF) that specifies a protein which is structurally unrelated to the products of the other variants. This ARF product functions as a stabilizer of the tumor suppressor protein p53 as it can interact with, and sequester, the E3 ubiquitin-protein ligase MDM2, a protein responsible for the degradation of p53. In spite of the structural and functional differences, the CDK inhibitor isoforms and the ARF product encoded by this gene, through the regulatory roles of CDK4 and p53 in cell cycle G1 progression, share a common functionality in cell cycle G1 control. This gene is frequently mutated or deleted in a wide variety of tumors, and is known to be an important tumor suppressor gene. [provided by RefSeq, Sep 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:1787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1787) · Entrez [1029](https://www.ncbi.nlm.nih.gov/gene/1029) · UniProt [P42771](https://www.uniprot.org/uniprotkb/P42771), [Q8N726](https://www.uniprot.org/uniprotkb/Q8N726) · Ensembl [ENSG00000147889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147889) · OMIM [600160](https://www.omim.org/entry/600160)

**PubMed**, as HGNC records for this gene — [8152487](https://pubmed.ncbi.nlm.nih.gov/8152487/), [7606716](https://pubmed.ncbi.nlm.nih.gov/7606716/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00395 |
| As a percentage | +0.27% |
| FDR, exposure-shuffle null | 0.5721 |
| In TP53-wild-type lines / altered lines | 0.00725 / 0.00266 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.264 raw, -0.054 with 3 PCs removed |

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
