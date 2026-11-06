---
symbol: TNFRSF10B
type: gene
tier: 1
pathway_role: p53 effector: apoptosis
aliases: [DR5, TRAIL-R2, KILLER]
gene_name: TNF receptor superfamily member 10b
locus: 8p21.3
locus_type: gene with protein product
gene_family: [CD molecules, Tumor necrosis factor receptor superfamily]
family_siblings_here: [EDA2R, FAS, SELPLG]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 200.46
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TNFRSF10B

*TNF receptor superfamily member 10b* — 8p21.3

> [!summary] In one line
> TNFRSF10B encodes DR5, the principal death receptor for TRAIL and a direct p53 target, through which p53 can route killing through the cell surface rather than the mitochondrion.

## What it is

DR5 (also TRAIL-R2, KILLER, TRICK2) is a type I transmembrane protein of the TNF receptor superfamily. Its cysteine-rich ectodomain binds trimeric TRAIL (TNFSF10); its cytoplasmic death domain then recruits FADD, which brings in caspase-8 and caspase-10 to form the death-inducing signalling complex. Caspase-8 activated there cleaves caspase-3 and -7 directly in so-called type I cells, or cleaves BID and so recruits the mitochondrion in type II cells — meaning the extrinsic pathway usually converges on the same machinery as the intrinsic one. Several layers sit between receptor and death: the decoy receptors TNFRSF10C and TNFRSF10D and soluble osteoprotegerin compete for ligand, cFLIP blocks caspase-8 at the complex, and receptor clustering rather than mere abundance is what licenses signalling. Two splice isoforms differ by a short insertion in the extracellular stalk.

The gene entered the p53 field directly: it was cloned as a DNA-damage-inducible, p53-regulated death receptor, and it appears in essentially every census of p53 targets. It is not only a p53 gene, though. DR5 is a major node of the unfolded protein response, where PERK–CHOP drives its transcription while IRE1α degrades its mRNA through regulated IRE1-dependent decay — the two arms opposing each other on one gene, which turns DR5 into a timer that converts sustained ER stress into ligand-independent apoptosis. NF-κB signalling also raises it. Therapeutically, DR5 was one of oncology's most-attempted targets: recombinant TRAIL and first-generation agonist antibodies were tested widely and largely failed as single agents, which is itself informative about how much of the pathway lies downstream of the receptor.

## Why it appears in this work

DR5 is the receptor arm of p53's death output, and it is a different sort of commitment from the BCL-2-family effectors: p53 raising DR5 builds *capacity* for extrinsic killing that only becomes lethal if ligand or clustering arrives. Within [[p53 program P]] it is also one of the better-measured apoptotic members, being abundantly expressed in most lines, so it carries more usable signal per cell in [[Tahoe-100M]] than the low-abundance effectors do. Read it as evidence that p53 is engaging its apoptotic repertoire, not that cells died.

## What is uncertain

The gap between DR5 mRNA and apoptosis is wide and well documented — most cancer lines carry plenty of DR5 and remain TRAIL-resistant, because cFLIP, decoy receptors, caspase-8 silencing and the absence of ligand all intervene. The bigger caution for this study is specificity: ER stress induces DR5 strongly and entirely without p53, and in a 379-compound panel many agents stress the endoplasmic reticulum, so DR5 induction is a weaker p53-specific signal than its program membership suggests. Its p53 response element is accepted as functional, but DR5 is a multiply-regulated gene rather than a dedicated p53 readout, and the relative weight of p53, CHOP and NF-κB input in any given condition is not something a transcript level can resolve.

## References

- Wu et al., 1997, Nature Genetics — identified KILLER/DR5 as a DNA damage-inducible, p53-regulated death receptor gene.
- Sheridan et al., 1997, Science — placed TRAIL-induced apoptosis under the control of a family of signalling and decoy receptors.
- Lu et al., 2014, Science — showed opposing unfolded-protein-response signals converge on DR5 to set the timing of ER-stress apoptosis.
- Fischer, 2017, Oncogene — census of p53 target genes, in which TNFRSF10B scores as a high-confidence direct target.

## What is on record

| | |
|---|---|
| Official name | TNF receptor superfamily member 10b |
| Also known as | DR5, KILLER, TRICK2A, TRAIL-R2, TRICKB, CD262, TRAILR2 |
| Locus | 8p21.3 — gene with protein product |
| Gene families | CD molecules; Tumor necrosis factor receptor superfamily |
| Other genes here in those families | [[EDA2R]], [[FAS]], [[SELPLG]] |
| Previously named | tumor necrosis factor receptor superfamily, member 10b |

**Function**, from UniProt [O14763](https://www.uniprot.org/uniprotkb/O14763) (reviewed):

> Receptor for the cytotoxic ligand TNFSF10/TRAIL (PubMed:10549288). The adapter molecule FADD recruits caspase-8 to the activated receptor. The resulting death-inducing signaling complex (DISC) performs caspase-8 proteolytic activation which initiates the subsequent cascade of caspases (aspartate-specific cysteine proteases) mediating apoptosis. Promotes the activation of NF-kappa-B. Essential for ER stress-induced apoptosis

**Summary**, from NCBI Gene [8795](https://www.ncbi.nlm.nih.gov/gene/8795):

> The protein encoded by this gene is a member of the TNF-receptor superfamily, and contains an intracellular death domain. This receptor can be activated by tumor necrosis factor-related apoptosis inducing ligand (TNFSF10/TRAIL/APO-2L), and transduces an apoptosis signal. Studies with FADD-deficient mice suggested that FADD, a death domain containing adaptor protein, is required for the apoptosis mediated by this protein. Two transcript variants encoding different isoforms and one non-coding transcript have been found for this gene. [provided by RefSeq, Mar 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11905) · Entrez [8795](https://www.ncbi.nlm.nih.gov/gene/8795) · UniProt [O14763](https://www.uniprot.org/uniprotkb/O14763) · Ensembl [ENSG00000120889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120889) · OMIM [603612](https://www.omim.org/entry/603612)

**PubMed**, as HGNC records for this gene — [9285725](https://pubmed.ncbi.nlm.nih.gov/9285725/), [9311998](https://pubmed.ncbi.nlm.nih.gov/9311998/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 200.46 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 44 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.131× |
| Wild-type minus altered | 1.066× |
| Compounds moving it up in WT lines | 79 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00388 |
| As a percentage | +0.27% |
| FDR, exposure-shuffle null | 0.3001 |
| In TP53-wild-type lines / altered lines | -0.00034 / 0.00649 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.313 raw, 0.299 with 3 PCs removed |

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
