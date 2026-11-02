---
symbol: CDKN2A
type: gene
tier: 1
aliases: [p16, ARF, p14ARF]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CDKN2A

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

## In this dataset

*Generated from the study's tables — do not edit by hand.*


## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
