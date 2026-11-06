---
symbol: FANCD2
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [Fanconi anaemia D2]
gene_name: FA complementation group D2
locus: 3p25.3
locus_type: gene with protein product
gene_family: [FA complementation groups, Armadillo like helical domain containing]
family_siblings_here: [ARFGEF1, ARFGEF2, ARMH3, ATM, BRCA2, HTT, PPP4R3A, RALGAPB, TAF3]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 36.95
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# FANCD2

*FA complementation group D2* — 3p25.3

> [!summary] In one line
> FANCD2 is the Fanconi anaemia protein that, once monoubiquitinated and paired with FANCI, clamps onto DNA at stalled replication forks and licenses interstrand crosslink repair.

## What it is

FANCD2 was positionally cloned as the FA-D2 gene, and its central event was identified at the same time: the FA core complex, through its FANCL ligase, attaches a single ubiquitin to FANCD2 at K561 and to its paralogue FANCI. The modified ID2 heterodimer closes around DNA as a clamp, and that species recruits the steps that unhook a crosslink. Ubiquitination depends on ATR-driven replication-stress signalling and is reversed by USP1-UAF1 ([[USP1]]), so the pathway cycles rather than latching. FANCD2 foci are a standard readout of replication stress. It also protects nascent DNA at stalled forks, a function shared with [[BRCA2]]. Biallelic loss causes Fanconi anaemia.

## Why it appears in this work

FANCD2 sits in the repression arm of [[p53 program P]], on the same logic as [[BRCA2]] and [[EXO1]]: not a p53-bound promoter but a proliferation-coupled gene that comes down as cells leave the cycle. [[The p21-DREAM axis]] is the predicted route.

## What is uncertain

Direct repression by p53 is unlikely for this class of gene. Its program membership is also among the less stable here — the stability line in the generated block is worth reading first. More fundamentally, abundance is the wrong variable: proficiency is set by ubiquitination state, not transcript level, so a modest fall in mRNA at 24 h is not evidence that repair was impaired. The sign must be flipped ([[Signing genes by p53 direction]]); the circularity warning applies.

## References

- Timmers et al., 2001, Molecular Cell — positional cloning of FANCD2.
- Garcia-Higuera et al., 2001, Molecular Cell — FANCD2 is monoubiquitinated after damage and colocalises with BRCA1, placing the FA proteins in a common pathway.
- Nijman et al., 2005, Molecular Cell — USP1 deubiquitinates FANCD2 and regulates the FA pathway.
- Smogorzewska et al., 2007, Cell — identified FANCI as a monoubiquitinated FANCD2 paralogue required for repair.
- Schlacher et al., 2012, Cancer Cell — FA proteins protect stalled replication forks, a function distinct from crosslink repair.
- Alcón et al., 2020, Nature Structural & Molecular Biology — cryo-EM showing FANCD2-FANCI as a DNA-stabilised clamp.

## What is on record

| | |
|---|---|
| Official name | FA complementation group D2 |
| Also known as | FAD, FA-D2 |
| Locus | 3p25.3 — gene with protein product |
| Gene families | FA complementation groups; Armadillo like helical domain containing |
| Other genes here in those families | [[ARFGEF1]], [[ARFGEF2]], [[ARMH3]], [[ATM]], [[BRCA2]], [[HTT]], [[PPP4R3A]], [[RALGAPB]], [[TAF3]] |
| Previously named | Fanconi anemia complementation group D2 |

**Function**, from UniProt [Q9BXW9](https://www.uniprot.org/uniprotkb/Q9BXW9) (reviewed):

> Required for maintenance of chromosomal stability (PubMed:11239453, PubMed:14517836). Promotes accurate and efficient pairing of homologs during meiosis (PubMed:14517836). Involved in the repair of DNA double-strand breaks, both by homologous recombination and single-strand annealing (PubMed:15671039, PubMed:15650050, PubMed:30335751, PubMed:36385258). The FANCI-FANCD2 complex binds and scans double-stranded DNA (dsDNA) for DNA damage; this complex stalls at DNA junctions between double-stranded DNA and single-stranded DNA (By similarity). May participate in S phase and G2 phase checkpoint activation upon DNA damage (PubMed:15377654). Plays a role in preventing breakage and loss of missegregating chromatin at the end of cell division, particularly after replication stress (PubMed:15454491, PubMed:15661754). Required for the targeting, or stabilization, of BLM to non-centromeric abnormal structures induced by replicative stress (PubMed:15661754, PubMed:19465921). Promotes BRCA2/FANCD1 loading onto damaged chromatin (PubMed:11239454, PubMed:12239151, PubMed:12086603, PubMed:15115758, PubMed:15199141, PubMed:15671039, PubMed:18212739). May also be involved in B-cell immunoglobulin isotype switching

**Summary**, from NCBI Gene [2177](https://www.ncbi.nlm.nih.gov/gene/2177):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The members of the Fanconi anemia complementation group do not share sequence similarity; they are related by their assembly into a common nuclear protein complex. This gene encodes the protein for complementation group D2. This protein is monoubiquinated in response to DNA damage, resulting in its localization to nuclear foci with other proteins (BRCA1 AND BRCA2) involved in homology-directed DNA repair. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:3585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3585) · Entrez [2177](https://www.ncbi.nlm.nih.gov/gene/2177) · UniProt [Q9BXW9](https://www.uniprot.org/uniprotkb/Q9BXW9) · Ensembl [ENSG00000144554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144554) · OMIM [613984](https://www.omim.org/entry/613984)

**PubMed**, as HGNC records for this gene — [7581463](https://pubmed.ncbi.nlm.nih.gov/7581463/), [11239453](https://pubmed.ncbi.nlm.nih.gov/11239453/), [18475298](https://pubmed.ncbi.nlm.nih.gov/18475298/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 36.95 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.949× |
| Wild-type minus altered | 0.938× |
| Compounds moving it up in WT lines | 30 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00104 |
| As a percentage | -0.07% |
| FDR, exposure-shuffle null | 0.8124 |
| In TP53-wild-type lines / altered lines | -0.00079 / -0.00119 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.213 raw, 0.157 with 3 PCs removed |

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
