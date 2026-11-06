---
symbol: ACER2
type: gene
tier: 1
pathway_role: p53 effector: metabolism / redox
aliases: [alkaline ceramidase 2]
gene_name: alkaline ceramidase 2
locus: 9p22.1
locus_type: gene with protein product
gene_family: [Alkaline ceramidases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: metabolism / redox
median_line_cpm: 13.72
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ACER2

*alkaline ceramidase 2* — 9p22.1

> [!summary] In one line
> ACER2 is a Golgi alkaline ceramidase that hydrolyses ceramide to sphingosine, and it is one of the most cleanly p53-inducible genes in sphingolipid metabolism.

## What it is

ACER2 (alkaline ceramidase 2) is one of three human alkaline ceramidases. It is a multi-pass membrane enzyme of the Golgi that hydrolyses unsaturated long-chain ceramides and dihydroceramides into a free fatty acid plus sphingosine or dihydrosphingosine; its activity is reported to depend on calcium and to have an alkaline pH optimum. Sphingosine released this way is the substrate for the sphingosine kinases, so ACER2 sits at a control point in the sphingolipid rheostat: it drains the ceramide pool, which signals toward arrest and death, and feeds the sphingosine and sphingosine-1-phosphate pools, which signal toward survival and migration. Which of those two consequences dominates depends on how much flux passes through the step.

Its regulation is what makes it interesting here. ACER2 mRNA rises sharply after DNA damage, and the induction appears to be a direct p53 effect: the dominant promoter lies inside the first intron and carries p53 consensus sites, and mutating the first conserved site abolishes p53-driven reporter activity. Downstream, doxorubicin raises ACER2 and cellular sphingosine together in a dose-dependent way, knockdown blunts both the sphingosine rise and the death response, and forced ACER2 expression drives autophagy and apoptosis in a manner blocked by antioxidants. Clinically, nothing is established: ACER2 is not a drug target and has no accepted diagnostic role.

## Why it appears in this work

ACER2 earns its place as a readout gene rather than as a mediator. Basal expression is low in most lines and the induction is steep and comparatively p53-selective, which is a good combination for a sparse single-cell readout — the opposite situation from [[MG53 (TRIM72)]] (see [[Why MG53 is hard to measure here]]). It is also a useful corrective to a cell-cycle-centric reading of [[p53 program P]]: part of p53's output runs through lipid metabolism, not only through [[The p21-DREAM axis]].

## What is uncertain

The direct-target claim rests on reporter and ChIP work in a small number of lines, and the intronic-promoter architecture has not been widely replicated; the question of whether some of the induction is indirect remains open. More importantly for reading this vault, a transcript increase is a weak proxy for ceramidase flux, which also depends on substrate supply, kinase levels and Golgi context. The cell-fate consequence is dose-dependent in the reported work — strong induction linked to death, modest induction linked to blunted arrest through S1P — and nothing in a 24 h mRNA measurement says which regime a given exposure occupied. Whether ACER2 is an effector of p53-driven death or only a bystander readout of it has been tested by knockdown in very few systems.

## References

- Wang et al., 2017, Scientific Reports — identified ACER2 as a direct p53 target with its major promoter and p53 sites in the first intron, and showed ROS-dependent autophagy and apoptosis on overexpression.
- Xu et al., 2016, Oncotarget — showed doxorubicin raises ACER2 and sphingosine dose-dependently in HCT116, and that ACER2 knockdown blunts both the sphingosine rise and the death response.

## What is on record

| | |
|---|---|
| Official name | alkaline ceramidase 2 |
| Also known as | FLJ41587, ALKCDase2 |
| Locus | 9p22.1 — gene with protein product |
| Gene families | Alkaline ceramidases |
| Previously named | N-acylsphingosine amidohydrolase 3-like |

**Function**, from UniProt [Q5QJU3](https://www.uniprot.org/uniprotkb/Q5QJU3) (reviewed):

> Golgi ceramidase that catalyzes the hydrolysis of ceramides into sphingoid bases like sphingosine and free fatty acids at alkaline pH (PubMed:16940153, PubMed:18945876, PubMed:20089856, PubMed:20207939). Ceramides, sphingosine, and its phosphorylated form sphingosine-1-phosphate are bioactive lipids that mediate cellular signaling pathways regulating several biological processes including cell proliferation, apoptosis and differentiation (PubMed:20207939). Has a better catalytic efficiency towards unsaturated long-chain ceramides, including C18:1-, C20:1- and C24:1-ceramides (PubMed:16940153, PubMed:18945876, PubMed:20089856, PubMed:20207939). Saturated long-chain ceramides and unsaturated very long-chain ceramides are also good substrates, whereas saturated very long-chain ceramides and short-chain ceramides are poor substrates (PubMed:20089856). Also hydrolyzes dihydroceramides to produce dihydrosphingosine (PubMed:20207939, PubMed:20628055). It is the ceramidase that controls the levels of circulating sphingosine-1-phosphate and dihydrosphingosine-1-phosphate in plasma through their production by hematopoietic cells (By similarity). Regulates cell proliferation, autophagy and apoptosis by the production of sphingosine and sphingosine-1-phosphate (PubMed:16940153, PubMed:26943039, PubMed:28294157, PubMed:29229990). As part of a p53/TP53-dependent pathway, promotes for instance autophagy and apoptosis in response to DNA damage (PubMed:26943039, PubMed:28294157, PubMed:29229990). Through the production of sphingosine, may also regulate the function of the Golgi complex and regulate the glycosylation of proteins (PubMed:18945876)

**Summary**, from NCBI Gene [340485](https://www.ncbi.nlm.nih.gov/gene/340485):

> The sphingolipid metabolite sphingosine-1-phosphate promotes cell proliferation and survival, whereas its precursor, sphingosine, has the opposite effect. The ceramidase ACER2 hydrolyzes very long chain ceramides to generate sphingosine (Xu et al., 2006 [PubMed 16940153]).[supplied by OMIM, Jul 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:23675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23675) · Entrez [340485](https://www.ncbi.nlm.nih.gov/gene/340485) · UniProt [Q5QJU3](https://www.uniprot.org/uniprotkb/Q5QJU3) · Ensembl [ENSG00000177076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177076) · OMIM [613492](https://www.omim.org/entry/613492)

**PubMed**, as HGNC records for this gene — [18945876](https://pubmed.ncbi.nlm.nih.gov/18945876/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 13.72 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 13 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.114× |
| Wild-type minus altered | 1.179× |
| Compounds moving it up in WT lines | 68 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01357 |
| As a percentage | +0.95% |
| FDR, exposure-shuffle null | 0.0515 |
| In TP53-wild-type lines / altered lines | 0.00590 / 0.01845 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.080 raw, 0.081 with 3 PCs removed |

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
