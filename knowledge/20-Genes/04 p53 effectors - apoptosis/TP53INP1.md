---
symbol: TP53INP1
type: gene
tier: 1
pathway_role: p53 effector: apoptosis
aliases: [TP53INP1, SIP]
gene_name: tumor protein p53 inducible nuclear protein 1
locus: 8q22.1
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 9.2
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TP53INP1

*tumor protein p53 inducible nuclear protein 1* — 8q22.1

> [!summary] In one line
> TP53INP1 encodes a p53-induced nuclear protein that feeds back on p53 itself, helping license the apoptotic arm of the response while also restraining reactive oxygen and promoting autophagy.

## What it is

TP53INP1 (also p53DINP1, SIP, TEAP) is a small nuclear protein with no enzymatic domain, expressed as two splice isoforms. It was found as a p53-inducible gene whose own product alters p53-dependent apoptosis — that is, as a feedback component rather than a terminal effector. The mechanism reported for it is partnership with the kinase HIPK2: in complex with HIPK2, TP53INP1 promotes phosphorylation of p53 at Ser46, the modification most associated with shifting p53's output away from arrest and toward apoptosis. On that account, TP53INP1 is part of how an activated p53 biases its own program.

Two further activities complicate the simple pro-death picture. TP53INP1 is a substantial mediator of p53's antioxidant function, lowering intracellular reactive oxygen species — the opposite polarity to the redox arm represented by [[TP53I3]], and a reminder that p53 both raises and suppresses oxidative stress depending on the level of activation. It also carries an LC3-interacting region through which it binds LC3 and other ATG8-family proteins, driving autophagy and an autophagy-dependent form of cell death; so the "apoptosis" label attached to it in effector catalogues is narrower than the biology. In vivo, mice lacking Tp53inp1 show exacerbated colitis and colitis-associated cancer, which supports a genuine tumour-suppressive role, and the gene is responsive to p73 as well as p53.

## Why it appears in this work

TP53INP1 is a feedback element inside [[p53 program P]], not just an output of it, and it sits high in the induction arm — which makes it one of the more informative members for the question of whether a compound engages p53 strongly enough to bias its program rather than merely switch it on. Reading its induction as "p53 is reinforcing its own apoptotic setting" is defensible; reading it as a measure of how many cells died is not. Its low abundance is the practical caveat, and the data block below is where that shows up for [[Tahoe-100M]].

## What is uncertain

The HIPK2/Ser46 mechanism rests on a small body of work, much of it using overexpressed protein, and how much of p53's Ser46 phosphorylation in an ordinary drug response depends on TP53INP1 is not established. The antioxidant and pro-autophagic-death roles are in tension: suppressing reactive oxygen is cytoprotective, promoting autophagic death is not, and which dominates appears to depend on the degree and duration of p53 activation in ways that have not been mapped. Whether its contribution to killing is apoptotic, autophagic, or both in different proportions by cell type remains open, so the effector annotation should be read as a label of convenience. Finally, because the transcript is not abundant, single-cell estimates for it are noisier than the headline program rank might suggest.

## References

- Okamura et al., 2001, Molecular Cell — identified p53DINP1/TP53INP1 as a p53-inducible gene regulating p53-dependent apoptosis.
- Tomasini et al., 2003, Journal of Biological Chemistry — showed TP53INP1 and HIPK2 act as partners in regulating p53 activity.
- Gommeaux et al., 2007, Molecular and Cellular Biology — colitis and colitis-associated cancer are exacerbated in TP53INP1-deficient mice.
- Cano et al., 2009, Cancer Research — TP53INP1 is a major mediator of p53's antioxidant function.
- Seillier et al., 2012, Cell Death and Differentiation — TP53INP1 binds LC3 and ATG8-family proteins through an LIR motif and promotes autophagy-dependent cell death.

## What is on record

| | |
|---|---|
| Official name | tumor protein p53 inducible nuclear protein 1 |
| Also known as | DKFZp434M1317, FLJ22139, P53DINP1, SIP, TP53INP1A, TP53INP1B, Teap |
| Locus | 8q22.1 — gene with protein product |

**Function**, from UniProt [Q96A56](https://www.uniprot.org/uniprotkb/Q96A56) (reviewed):

> Antiproliferative and pro-apoptotic protein involved in cell stress response which acts as a dual regulator of transcription and autophagy. Acts as a positive regulator of autophagy. In response to cellular stress or activation of autophagy, relocates to autophagosomes where it interacts with autophagosome-associated proteins GABARAP, GABARAPL1/L2, MAP1LC3A/B/C and regulates autophagy. Acts as an antioxidant and plays a major role in p53/TP53-driven oxidative stress response. Possesses both a p53/TP53-independent intracellular reactive oxygen species (ROS) regulatory function and a p53/TP53-dependent transcription regulatory function. Positively regulates p53/TP53 and p73/TP73 and stimulates their capacity to induce apoptosis and regulate cell cycle. In response to double-strand DNA breaks, promotes p53/TP53 phosphorylation on 'Ser-46' and subsequent apoptosis. Acts as a tumor suppressor by inducing cell death by an autophagy and caspase-dependent mechanism. Can reduce cell migration by regulating the expression of SPARC

**Summary**, from NCBI Gene [94241](https://www.ncbi.nlm.nih.gov/gene/94241):

> Predicted to enable antioxidant activity. Involved in autophagic cell death; positive regulation of DNA-templated transcription; and positive regulation of autophagy. Located in autophagosome; cytosol; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18022) · Entrez [94241](https://www.ncbi.nlm.nih.gov/gene/94241) · UniProt [Q96A56](https://www.uniprot.org/uniprotkb/Q96A56) · Ensembl [ENSG00000164938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164938) · OMIM [606185](https://www.omim.org/entry/606185)

**PubMed**, as HGNC records for this gene — [11511362](https://pubmed.ncbi.nlm.nih.gov/11511362/), [12438758](https://pubmed.ncbi.nlm.nih.gov/12438758/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 9.20 CPM |
| Lines where detected | 46 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 14 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.180× |
| Wild-type minus altered | 1.212× |
| Compounds moving it up in WT lines | 78 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00581 |
| As a percentage | -0.40% |
| FDR, exposure-shuffle null | 0.3532 |
| In TP53-wild-type lines / altered lines | -0.00646 / -0.00538 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.143 raw, -0.219 with 3 PCs removed |

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
