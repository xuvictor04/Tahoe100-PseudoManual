---
symbol: MBOAT1
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [OACT1]
gene_name: membrane bound glycerophospholipid O-acyltransferase 1
locus: 6p22.3
locus_type: gene with protein product
gene_family: [Membrane bound O-acyltransferase family, Lysophospholipid acyltransferases, 1-acylglycerophosphoethanolamine O-acyltransferases]
family_siblings_here: [HHAT]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 21.93
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# MBOAT1

*membrane bound glycerophospholipid O-acyltransferase 1* — 6p22.3

> [!summary] In one line
> MBOAT1 encodes an endoplasmic-reticulum lysophospholipid acyltransferase that re-acylates lyso-phosphatidylethanolamine and lyso-phosphatidylserine, setting the fatty-acid composition of membrane phospholipids.

## What it is

MBOAT1 runs the re-acylation half of the Lands cycle: a phospholipase strips the sn-2 acyl chain from a membrane phospholipid, and a membrane-bound O-acyltransferase puts a new one back. Also called LPEAT1 or LPSAT, it is a multipass ER membrane enzyme preferring lyso-phosphatidylethanolamine and lyso-phosphatidylserine as acceptors and oleoyl-CoA as donor, so its activity shifts membranes toward monounsaturated chains. That specificity gave it a second life in redox biology: MBOAT1 and its paralogue MBOAT2 were identified as ferroptosis suppressors acting independently of GPX4 and FSP1, depleting the polyunsaturated phospholipids that lipid peroxidation requires. In the same work MBOAT1 was reported to be driven transcriptionally by the oestrogen receptor.

## Why it appears in this work

It is carried here as a member of the repression arm of [[p53 program P]], which makes the sign of its slope matter more than the size — a positive coefficient on measured MG53 reads as *less* p53 output, not more. That inversion is the argument of [[Signing genes by p53 direction]].

## What is uncertain

Nothing establishes MBOAT1 as a direct p53 target: no response element at the locus has been reported, and a repression arm derived from expression behaviour collects genes that fall simply because growth and lipid synthesis fall under arrest. The ferroptosis role rests substantially on gain-of-function overexpression. And since its level tracks oestrogen-receptor status, a hormone-receptor covariate across these pooled lines could generate an association unrelated to p53.

## References

- Hishikawa et al., 2008, PNAS — defined the MBOAT lysophospholipid acyltransferase family, assigning MBOAT1 lyso-PE/lyso-PS acceptor preference.
- Liang et al., 2023, Cell — MBOAT1 and MBOAT2 suppress ferroptosis independently of GPX4 and FSP1, and are induced by oestrogen and androgen receptor respectively.

## What is on record

| | |
|---|---|
| Official name | membrane bound glycerophospholipid O-acyltransferase 1 |
| Also known as | MGC44669, dJ434O11.1, LPEAT1, LPLAT14, lysophosphatidylethanolamine acyltransferase 1, lysophospholipid acyltransferase 14, lysophospholipid acyltransferase 1 |
| Locus | 6p22.3 — gene with protein product |
| Gene families | Membrane bound O-acyltransferase family; Lysophospholipid acyltransferases; 1-acylglycerophosphoethanolamine O-acyltransferases |
| Other genes here in those families | [[HHAT]] |
| Previously named | membrane bound O-acyltransferase domain containing 1; O-acyltransferase (membrane bound) domain containing 1 |

**Function**, from UniProt [Q6ZNC8](https://www.uniprot.org/uniprotkb/Q6ZNC8) (reviewed):

> Acyltransferase which catalyzes the transfer of an acyl group from an acyl-CoA towards a lysophospholipid producing a phospholipid and participates in the reacylation step of the phospholipid remodeling pathway also known as the Lands cycle (PubMed:18772128). Acts on lysophosphatidylserine (1-acyl-2-hydroxy-sn-glycero-3-phospho-L-serine or LPS) and lysophosphatidylethanolamine (1-acyl-sn-glycero-3-phosphoethanolamine or LPE), and to a lesser extend lysophosphatidylcholine (PubMed:18772128). Prefers oleoyl-CoA as the acyl donor and 1-oleoyl-LPE as acceptor (PubMed:18772128). May play a role in neurite outgrowth during neuronal differentiation (By similarity)

**Summary**, from NCBI Gene [154141](https://www.ncbi.nlm.nih.gov/gene/154141):

> This gene belongs to the membrane-bound O-acetyltransferase superfamily. The encoded transmembrane protein is an enzyme that transfers organic compounds, preferably from oleoyl-CoA, to hydroxyl groups of protein targets in membranes. A translocation disrupting this gene may be associated with brachydactyly syndactyly syndrome. Alternately spliced transcript variants have been described for this gene. [provided by RefSeq, Nov 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:21579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21579) · Entrez [154141](https://www.ncbi.nlm.nih.gov/gene/154141) · UniProt [Q6ZNC8](https://www.uniprot.org/uniprotkb/Q6ZNC8) · Ensembl [ENSG00000172197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172197) · OMIM [611732](https://www.omim.org/entry/611732)

**PubMed**, as HGNC records for this gene — [18287005](https://pubmed.ncbi.nlm.nih.gov/18287005/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 21.93 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.935× |
| Wild-type minus altered | 0.961× |
| Compounds moving it up in WT lines | 30 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.01093 |
| As a percentage | -0.75% |
| FDR, exposure-shuffle null | 0.0218 |
| In TP53-wild-type lines / altered lines | -0.01012 / -0.01139 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.519 raw, -0.097 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[The p21-DREAM axis]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, repression arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
