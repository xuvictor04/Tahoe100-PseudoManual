---
symbol: PLK3
type: gene
tier: 1
pathway_role: p53 effector: cell-cycle arrest
aliases: [PRK, FNK]
gene_name: polo like kinase 3
locus: 1p34.1
locus_type: gene with protein product
gene_family: [Polo like kinase family]
family_siblings_here: [PLK2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: cell-cycle arrest
median_line_cpm: 16.9
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PLK3

*polo like kinase 3* — 1p34.1

> [!summary] In one line
> PLK3 encodes a stress-activated polo-like kinase, switched on by DNA damage and oxidative stress, that has been implicated in phosphorylating p53 at serine 20.

## What it is

PLK3 (also PRK, FNK, CNK) belongs to the polo-like kinase family — an N-terminal kinase domain plus a C-terminal polo-box domain for substrate docking and localisation. Family membership is misleading if read as family resemblance. PLK1 is a mitotic kinase, overexpressed in tumours and a drug target; PLK3 behaves instead as a stress-response kinase whose transcript is an immediate-early gene and whose activity is induced rather than cell-cycle-scheduled.

The best-developed part of its biology is the damage response. PLK3 activity rises rapidly after DNA damage in an ATM-dependent manner, and PLK3 phosphorylates p53 on serine 20 in vitro — the site whose modification interferes with [[MDM2]] binding and so stabilises the protein. Hydrogen peroxide produces a comparable activation, and in cells a kinase-dead PLK3 reduces serine 20 phosphorylation after either insult, though the published effect is partial in both cases. PLK3 has also been reported to phosphorylate CHK2 ([[CHEK2]]) and CDC25C and to act on HIF-1α under hypoxia, but no single function has been pinned down as its principal one.

PLK3 is usually labelled a tumour suppressor. The basis is expression rather than mutation — the transcript is reported down-regulated in several carcinomas, lung and head and neck among them. The mouse genetics are split rather than merely weak: one study reports tumours in various organs in aged Plk3-null animals, tied to deregulated HIF-1α, while another finds no significant increase in spontaneous tumour incidence across genotypes.

## Why it appears in this work

PLK3 sits in the induction arm of [[p53 program P]] as a curated effector with an arrest role, and its interest here is that it is a candidate *feedback* component rather than a terminal output. If PLK3 is induced as part of the p53 response and also phosphorylates p53 at a stabilising site, its induction reports engagement of a loop, not merely a downstream consequence — a different kind of signal from p21's. Its presence says the stress-kinase layer moved with the canonical arrest and apoptosis arms, as one expects if [[The p53 pathway]] is genuinely active.

## What is uncertain

The serine 20 claim deserves its hedges. It rests on in vitro kinase work plus dominant-negative and knockdown experiments; CHK2 is the better-established serine 20 kinase, and how much PLK3 contributes in any particular cell type is unresolved; the two are not mutually exclusive. Whether PLK3 is a *direct* p53 target is a separate, weaker question: it is damage-inducible, but a validated p53 response element is not part of the standard account, so membership in a p53-associated induction arm may reflect a general stress induction running parallel to p53 rather than through it. The tumour-suppressor designation rests largely on reduced expression in tumour series, and the mouse data do not settle it either way. Most pointedly here, a report has PLK3 phosphorylating serine 20 of gain-of-function mutant p53 and supporting its transactivation — if that holds, PLK3's effect is conditional on p53 genotype, and this panel contains both wild-type and altered lines (see [[p53 nullification in cancer cell lines]]).

## References

- Xie et al., 2001, Journal of Biological Chemistry — Plk3 links DNA damage to arrest and apoptosis partly via p53, with ATM-dependent activation and serine 20 as a target site.
- Xie et al., 2001, Journal of Biological Chemistry — reactive-oxygen-species-induced phosphorylation of p53 on serine 20 is mediated in part by Plk3.
- Bahassi El et al., 2002, Oncogene — Plk3 as a multifunctional kinase in stress-response pathways, interacting with the damage checkpoint machinery.
- Myer et al., 2011, Mutation Research — Plk3-null mice stabilise Cdc25A after DNA damage, but show no significant increase in tumour incidence between genotypes.

## What is on record

| | |
|---|---|
| Official name | polo like kinase 3 |
| Also known as | FNK, PRK |
| Locus | 1p34.1 — gene with protein product |
| Gene families | Polo like kinase family |
| Other genes here in those families | [[PLK2]] |
| Previously named | cytokine-inducible kinase; polo-like kinase 3 (Drosophila); polo-like kinase 3 |

**Function**, from UniProt [Q9H4B4](https://www.uniprot.org/uniprotkb/Q9H4B4) (reviewed):

> Serine/threonine-protein kinase involved in cell cycle regulation, response to stress and Golgi disassembly. Polo-like kinases act by binding and phosphorylating proteins that are already phosphorylated on a specific motif recognized by the POLO box domains. Phosphorylates ATF2, BCL2L1, CDC25A, CDC25C, CHEK2, HIF1A, JUN, p53/TP53, p73/TP73, PTEN, TOP2A and VRK1. Involved in cell cycle regulation: required for entry into S phase and cytokinesis. Phosphorylates BCL2L1, leading to regulate the G2 checkpoint and progression to cytokinesis during mitosis. Plays a key role in response to stress: rapidly activated upon stress stimulation, such as ionizing radiation, reactive oxygen species (ROS), hyperosmotic stress, UV irradiation and hypoxia. Involved in DNA damage response and G1/S transition checkpoint by phosphorylating CDC25A, p53/TP53 and p73/TP73. Phosphorylates p53/TP53 in response to reactive oxygen species (ROS), thereby promoting p53/TP53-mediated apoptosis. Phosphorylates CHEK2 in response to DNA damage, promoting the G2/M transition checkpoint. Phosphorylates the transcription factor p73/TP73 in response to DNA damage, leading to inhibit p73/TP73-mediated transcriptional activation and pro-apoptotic functions. Phosphorylates HIF1A and JUN is response to hypoxia. Phosphorylates ATF2 following hyperosmotic stress in corneal epithelium. Also involved in Golgi disassembly during the cell cycle: part of a MEK1/MAP2K1-dependent pathway that induces Golgi fragmentation during mitosis by mediating phosphorylation of VRK1. May participate in endomitotic cell cycle, a form of mitosis in which both karyokinesis and cytokinesis are interrupted and is a hallmark of megakaryocyte differentiation, via its interaction with CIB1

**Summary**, from NCBI Gene [1263](https://www.ncbi.nlm.nih.gov/gene/1263):

> The protein encoded by this gene is a member of the highly conserved polo-like kinase family of serine/threonine kinases. Members of this family are characterized by an amino-terminal kinase domain and a carboxy-terminal bipartite polo box domain that functions as a substrate-binding motif and a cellular localization signal. Polo-like kinases are important regulators of cell cycle progression. This gene has also been implicated in stress responses and double-strand break repair. In human cell lines, this protein is reported to associate with centrosomes in a microtubule-dependent manner, and during mitosis, the protein becomes localized to the mitotic apparatus. Expression of a kinase-defective mutant results in abnormal cell morphology caused by changes in microtubule dynamics and mitotic arrest followed by apoptosis. [provided by RefSeq, Sep 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2154) · Entrez [1263](https://www.ncbi.nlm.nih.gov/gene/1263) · UniProt [Q9H4B4](https://www.uniprot.org/uniprotkb/Q9H4B4) · Ensembl [ENSG00000173846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173846) · OMIM [602913](https://www.omim.org/entry/602913)

**PubMed**, as HGNC records for this gene — [8702627](https://pubmed.ncbi.nlm.nih.gov/8702627/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 16.90 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 22 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.091× |
| Wild-type minus altered | 1.119× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00763 |
| As a percentage | +0.53% |
| FDR, exposure-shuffle null | 0.2280 |
| In TP53-wild-type lines / altered lines | 0.00356 / 0.01010 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.459 raw, 0.273 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
