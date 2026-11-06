---
symbol: TRIM72
type: gene
tier: 1
pathway_role: the MG53 locus
aliases: [MG53, mitsugumin 53]
gene_name: tripartite motif containing 72
locus: 16p11.2
locus_type: gene with protein product
gene_family: [Ring finger proteins, Tripartite motif family, RING finger E3 ubiquitin protein ligases]
family_siblings_here: [COP1, MDM2, MDM4, MGRN1, PCGF3, RC3H1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# TRIM72

*tripartite motif containing 72* — 16p11.2

> [!summary] In one line
> TRIM72 encodes MG53, a striated-muscle E3 ubiquitin ligase that patches torn plasma membrane — and in this study it is the exposure variable, measured as mRNA in cells that are not muscle.

## What it is

MG53 ("mitsugumin 53") is a tripartite-motif protein — a RING finger with E3 ubiquitin ligase activity, a B-box, an oligomerising coiled-coil and a C-terminal SPRY domain — expressed almost only in skeletal and cardiac muscle.

Its established job is acute membrane repair. When the sarcolemma tears, MG53 senses the change in redox environment, oligomerises, and nucleates a repair patch by drawing vesicles to the breach, alongside caveolin-3, dysferlin and PTRF/cavin-1. What brings it to the wound is the oxidative environment rather than calcium entry — calcium is still needed for the recruited vesicles to fuse — which separates its sensing step from the calcium-sensing dysferlin pathway. *Trim72*-null mice develop myopathy and tolerate ischaemia–reperfusion poorly, and recombinant MG53 protein is protective in injury models.

Two further activities matter here: the RING domain ubiquitinates the insulin receptor and IRS1, and MG53 restrains myoblast differentiation, entangling its expression with the muscle programme that produces it. The fuller account is in [[MG53 (TRIM72)]].

## Why it appears in this work

It is the exposure: every result is an association between measured TRIM72 mRNA and something else. Two structural facts shape all of it. First, it is a muscle gene read in 50 non-muscle cancer lines, where it sits at trace levels and the factors that normally drive it — MYOD1, MYOG, MEF2, SRF — are silent or absent, so no transcription-factor account of its movement here can work; see [[Transcription factor activity inference]]. Second, its locus is unlucky: it lies about 17 kb 3′ of [[FUS]] and 11 kb 3′ of [[PYCARD-AS1]] on the same strand, with FUS far higher, so transcription that fails to terminate there is counted as TRIM72 mRNA. That geometry, not any regulator, is the leading account of what appears to raise MG53 here — see [[The TRIM72 locus]] and [[Readthrough spillover]].

## What is uncertain

Nearly everything MG53 is known to do happens at the level of protein, localisation and ubiquitination, and this dataset has none of those: it measures mRNA, at one time point, with no knockdown, no overexpression and no protein readout. A null here constrains the mRNA-level association in these cells and cannot rule out a protein-level link — the asymmetry stated in [[What this study found]].

Part of the measured signal is not this gene's transcript. The strand-specific evidence that readthrough happens at this locus is solid, but the arithmetic over-predicts the observed rise, so the magnitude is unaccounted for and no clean subtraction exists. It also carries the largest plate batch gap in the dataset; see [[Why MG53 is hard to measure here]].

And two things the dataset cannot speak to: all 50 lines are TRIM72-wild-type and differ only in level, so nothing here contrasts functional with non-functional MG53; and the insulin-resistance role is genuinely disputed, groups disagreeing over whether circulating MG53 causes insulin resistance or merely marks muscle damage.

## References

- Cai et al., 2009, *Nature Cell Biology* — identified MG53 as the nucleating factor for acute membrane repair in striated muscle, with oligomerisation and recruitment driven by entry of the extracellular oxidative environment rather than by calcium.
- Song et al., 2013, *Nature* — MG53 as an E3 ligase for the insulin receptor and IRS1, with metabolic consequences on overexpression.
- Weisleder et al., 2012, *Science Translational Medicine* — recombinant MG53 delivered as a protein therapeutic in muscle injury models.

## What is on record

| | |
|---|---|
| Official name | tripartite motif containing 72 |
| Also known as | MG53, mitsugumin 53 |
| Locus | 16p11.2 — gene with protein product |
| Gene families | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Other genes here in those families | [[COP1]], [[MDM2]], [[MDM4]], [[MGRN1]], [[PCGF3]], [[RC3H1]] |
| Previously named | tripartite motif-containing 72; tripartite motif containing 72, E3 ubiquitin protein ligase |

**Function**, from UniProt [Q6ZMU5](https://www.uniprot.org/uniprotkb/Q6ZMU5) (reviewed):

> Muscle-specific E3 ubiquitin-protein ligase that plays a central role in cell membrane repair by nucleating the assembly of the repair machinery at injury sites (PubMed:36944613). Its ubiquitination activity is mediated by E2 ubiquitin-conjugating enzymes UBE2D1, UBE2D2 and UBE2D3 (By similarity). Acts as a sensor of oxidation: upon membrane damage, entry of extracellular oxidative environment results in disulfide bond formation and homooligomerization at the injury site (By similarity). This oligomerization acts as a nucleation site for recruitment of TRIM72-containing vesicles to the injury site, leading to membrane patch formation (By similarity). Probably acts upstream of the Ca(2+)-dependent membrane resealing process (By similarity). Required for transport of DYSF to sites of cell injury during repair patch formation (By similarity). Regulates membrane budding and exocytosis (By similarity). May be involved in the regulation of the mobility of KCNB1-containing endocytic vesicles (By similarity)

**Summary**, from NCBI Gene [493829](https://www.ncbi.nlm.nih.gov/gene/493829):

> Enables identical protein binding activity. Predicted to be involved in several processes, including plasma membrane repair; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein homooligomerization. Predicted to act upstream of or within negative regulation of insulin receptor signaling pathway; negative regulation of insulin-like growth factor receptor signaling pathway; and negative regulation of myotube differentiation. Predicted to be located in cytoplasmic vesicle membrane. Predicted to be active in cytoplasm and sarcolemma. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:32671](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32671) · Entrez [493829](https://www.ncbi.nlm.nih.gov/gene/493829) · UniProt [Q6ZMU5](https://www.uniprot.org/uniprotkb/Q6ZMU5) · Ensembl [ENSG00000177238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177238) · OMIM [613288](https://www.omim.org/entry/613288)

**PubMed**, as HGNC records for this gene — [20399744](https://pubmed.ncbi.nlm.nih.gov/20399744/), [23354051](https://pubmed.ncbi.nlm.nih.gov/23354051/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 1.00000 |
| As a percentage | +100.00% |
| FDR, exposure-shuffle null | — |
| In TP53-wild-type lines / altered lines | 1.00000 / 1.00000 |
| Verdict | — |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

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
