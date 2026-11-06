---
symbol: BAX
type: gene
tier: 1
pathway_role: p53 effector: apoptosis
aliases: [bcl-2-associated X]
gene_name: BCL2 associated X, apoptosis regulator
locus: 19q13.33
locus_type: gene with protein product
gene_family: [BCL2 family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 10.52
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# BAX

*BCL2 associated X, apoptosis regulator* — 19q13.33

> [!summary] In one line
> BAX is the pore-forming BCL-2-family effector that permeabilises the outer mitochondrial membrane, and it was the first component of the apoptotic machinery identified as a direct p53 transcriptional target.

## What it is

BAX is a multidomain pro-apoptotic member of the BCL-2 family. In healthy cells most of it is a soluble cytosolic monomer, cycling on and off mitochondria and being retrotranslocated back to the cytosol by anti-apoptotic relatives. On activation it undergoes a large conformational change, inserts into the outer mitochondrial membrane and oligomerises, with BAK, into macropores. That permeabilisation releases cytochrome c and SMAC, which assemble the APAF1 apoptosome and activate caspase-9 and then caspase-3. It is the commitment step of the intrinsic pathway: cells lacking both BAX and BAK are broadly resistant to mitochondrial apoptosis regardless of upstream signalling.

BAX is controlled at two levels. Transcriptionally, p53 binds its promoter and raises its expression, the finding that first put a p53 target inside the death machinery itself. Post-translationally — and this is where the decision is actually made — its activity depends on the balance between BH3-only activators such as BID, BIM and PUMA and the anti-apoptotic proteins BCL-2, BCL-xL and MCL-1 that sequester both activators and BAX. That stoichiometry is what BH3-mimetic drugs such as venetoclax exploit; they kill through BAX and BAK rather than around them. Frameshift mutations in the BAX coding repeat are recurrent in microsatellite-unstable colorectal cancer.

## Why it appears in this work

BAX marks the apoptotic arm of p53's output. Its induction is the transcript-level signal that p53 reached the death machinery rather than stopping at arrest through [[The p21-DREAM axis]]. It is also the clearest example in this gene set of why mRNA is a lossy readout of apoptotic commitment: whether BAX kills is set by protein stoichiometry at the mitochondrion, and BAX protein is abundant and comparatively long-lived on the timescale of the 24 h window used in [[Tahoe-100M]]. A modest transcript move here can mean much less, or much more, than the same move in a gene with near-zero baseline such as [[BBC3]].

## What is uncertain

How much of a p53 transcriptional target BAX really is remains contested. The promoter work was done in a small number of systems, and across cell types BAX induction after p53 activation is usually modest and inconsistent, with PUMA and NOXA responding far more strongly; in several lineages BAX mRNA barely moves while apoptosis proceeds. So for this vault the direct-versus-indirect question is less interesting than the magnitude question: BAX is a genuine target whose transcriptional arm is probably not where its p53 dependence mostly lives. Mechanistically, whether PUMA and BID activate BAX directly or only by displacing it from anti-apoptotic partners is still argued, with evidence for both. The transcription-independent mechanism in which cytoplasmic p53 activates BAX directly is accepted by some groups and disputed by others. And Bax-null mice have a mild phenotype, which says BAK covers for it in most tissues.

## References

- Oltvai, Milliman and Korsmeyer, 1993, Cell — identified BAX as a BCL-2-interacting protein that promotes apoptosis.
- Miyashita and Reed, 1995, Cell — showed p53 is a direct transcriptional activator of the human BAX promoter.
- Wei et al., 2001, Science — showed BAX and BAK are jointly required for mitochondrial apoptosis.
- Chipuk et al., 2004, Science — reported direct activation of BAX by cytoplasmic p53, independent of transcription.
- Knudson et al., 1995, Science — characterised Bax-deficient mice, showing a limited phenotype consistent with redundancy.

## What is on record

| | |
|---|---|
| Official name | BCL2 associated X, apoptosis regulator |
| Also known as | BCL2L4 |
| Locus | 19q13.33 — gene with protein product |
| Gene families | BCL2 family |
| Previously named | BCL2-associated X protein; BCL2 associated X protein |

**Function**, from UniProt [Q07812](https://www.uniprot.org/uniprotkb/Q07812) (reviewed):

> Plays a role in the mitochondrial apoptotic process (PubMed:10772918, PubMed:11060313, PubMed:16113678, PubMed:16199525, PubMed:18948948, PubMed:21199865, PubMed:21458670, PubMed:25609812, PubMed:36361894, PubMed:8358790, PubMed:8521816). Under normal conditions, BAX is largely cytosolic via constant retrotranslocation from mitochondria to the cytosol mediated by BCL2L1/Bcl-xL, which avoids accumulation of toxic BAX levels at the mitochondrial outer membrane (MOM) (PubMed:21458670). Under stress conditions, undergoes a conformation change that causes translocation to the mitochondrion membrane, leading to the release of cytochrome c that then triggers apoptosis (PubMed:10772918, PubMed:11060313, PubMed:16113678, PubMed:16199525, PubMed:18948948, PubMed:21199865, PubMed:21458670, PubMed:25609812, PubMed:8358790, PubMed:8521816). Promotes activation of CASP3, and thereby apoptosis (PubMed:10772918, PubMed:11060313, PubMed:16113678, PubMed:16199525, PubMed:18948948, PubMed:21199865, PubMed:21458670, PubMed:25609812, PubMed:8358790, PubMed:8521816)

**Summary**, from NCBI Gene [581](https://www.ncbi.nlm.nih.gov/gene/581):

> The protein encoded by this gene belongs to the BCL2 protein family. BCL2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. This protein forms a heterodimer with BCL2, and functions as an apoptotic activator. The association and the ratio of BAX to BCL2 also determines survival or death of a cell following an apoptotic stimulus. This protein is reported to interact with, and increase the opening of, the mitochondrial voltage-dependent anion channel (VDAC), which leads to the loss in membrane potential and the release of cytochrome c. The expression of this gene is regulated by the tumor suppressor P53 and has been shown to be involved in P53-mediated apoptosis. Multiple alternatively spliced transcript variants, which encode different isoforms, have been reported for this gene. [provided by RefSeq, Dec 2019]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:959) · Entrez [581](https://www.ncbi.nlm.nih.gov/gene/581) · UniProt [Q07812](https://www.uniprot.org/uniprotkb/Q07812) · Ensembl [ENSG00000087088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087088) · OMIM [600040](https://www.omim.org/entry/600040)

**PubMed**, as HGNC records for this gene — [8358790](https://pubmed.ncbi.nlm.nih.gov/8358790/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 10.52 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 47 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.060× |
| Wild-type minus altered | 1.104× |
| Compounds moving it up in WT lines | 53 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00018 |
| As a percentage | -0.01% |
| FDR, exposure-shuffle null | 0.9720 |
| In TP53-wild-type lines / altered lines | -0.00692 / 0.00390 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.327 raw, -0.036 with 3 PCs removed |

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
