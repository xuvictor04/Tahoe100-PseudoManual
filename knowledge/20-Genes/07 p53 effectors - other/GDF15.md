---
symbol: GDF15
type: gene
tier: 1
pathway_role: p53 effector: other
aliases: [MIC-1, NAG-1]
gene_name: growth differentiation factor 15
locus: 19p13.11
locus_type: gene with protein product
gene_family: [MicroRNA protein coding host genes, Transforming growth factor beta superfamily]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, MGRN1, NADSYN1, NOTCH1, NUP210L, PER1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: other (secreted)
median_line_cpm: 22.18
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# GDF15

*growth differentiation factor 15* — 19p13.11

> [!summary] In one line
> GDF15 encodes a secreted, divergent TGF-β superfamily cytokine that signals through a single receptor in the hindbrain to suppress appetite, and that p53 induces — along with almost every other kind of cellular stress.

## What it is

GDF15 has an unusual number of names — MIC-1, NAG-1, PLAB, PTGF-β, PDF — because several groups found it independently in unrelated screens, itself a clue to how promiscuously it is induced. It is a distant TGF-β superfamily member, secreted as a disulfide-linked dimer after pro-protein cleavage. Basal expression is low in most tissues and high in placenta; levels rise steeply with injury, inflammation, mitochondrial dysfunction, renal and cardiac disease, ageing and cancer. It is among the strongest single-protein predictors of all-cause mortality — a general distress signal, not a disease marker.

Its receptor was a long-standing puzzle, resolved in 2017 when four groups independently identified GFRAL, an orphan GDNF-family receptor that uses RET as co-receptor and is expressed essentially only in the area postrema and nucleus tractus solitarius. That anatomy explains the physiology: GDF15 acts on brainstem circuitry for nausea and aversion, suppressing food intake and causing weight loss — now understood as a principal effector arm of cancer cachexia. Metformin's weight effect runs substantially through GDF15, and GDF15 is linked to nausea and vomiting of pregnancy.

Its transcriptional control is where this gene earns its caution. GDF15 was identified as a p53 target gene and proposed as a serum biomarker of p53 pathway activation. But it is also induced strongly by the ATF4/CHOP integrated stress response, by mitochondrial dysfunction, by inflammatory cytokines, and — the original NAG-1 finding — by NSAIDs independent of cyclooxygenase. Several largely independent stress pathways converge on this one promoter.

## Why it appears in this work

GDF15 is a curated p53 effector in the induction arm of [[p53 program P]], and the one member of that set whose product leaves the cell: its induction means the p53 response is being broadcast rather than kept internal, a different output from arrest or apoptosis. It is also the set's most useful stress test for how much of program P is really p53. A panel of 379 drugs at [[Tahoe-100M]] scale contains many compounds that stress mitochondria, the ribosome and the ER without touching p53, and those should induce GDF15 regardless of genotype — so a gene whose direction across perturbations is unstable is behaving as a multiply-driven promoter should.

## What is uncertain

Whether p53 acts at the GDF15 promoter directly or through the stress machinery p53 activation itself engages is not settled in a way I would rely on: a p53 response element has been reported here, but the ATF4 route is at least as strong in many systems, and in some contexts GDF15 is induced with no p53 requirement at all. So "p53 target" is true but far from exclusive, and GDF15 induction is weak evidence that p53 specifically is on. Its direction of effect in cancer is genuinely contested, not merely unresolved: the NAG-1 literature describes it as pro-apoptotic and antitumorigenic, the cachexia literature as a driver of poor outcome; the resolution is probably that early cell-autonomous and late systemic effects differ. Its expression here is low enough that per-cell measurement is noisy, limiting what any single-cell correlation can establish.

## References

- Tan et al., 2000, PNAS — identified PTGF-β/GDF15 as a p53 target gene inhibiting tumour cell growth through TGF-β signalling.
- Baek et al., 2001, Molecular Pharmacology — cyclooxygenase inhibitors induce this TGF-β superfamily member (NAG-1), independent of COX, with proapoptotic and antitumorigenic activity.
- Yang et al., 2003, Molecular Cancer Therapeutics — proposed MIC-1/GDF15 as a biomarker of p53 pathway activation.
- Mullican et al., 2017, Nature Medicine, and Hsu et al., 2017, Nature — identified GFRAL as the GDF15 receptor and localised it to the area postrema and nucleus tractus solitarius.
- Coll et al., 2020, Nature — showed GDF15 mediates the effects of metformin on body weight and energy balance.
- Lockhart et al., 2020, Endocrine Reviews — review framing GDF15 as a hormone conveying somatic distress to the brain.

## What is on record

| | |
|---|---|
| Official name | growth differentiation factor 15 |
| Also known as | PLAB, MIC-1, PDF, MIC1, NAG-1, PTGFB, prostate differentiation factor, non-steroidal anti-inflammatory drug-activated gene-1, macrophage inhibitory cytokine-1 |
| Locus | 19p13.11 — gene with protein product |
| Gene families | MicroRNA protein coding host genes; Transforming growth factor beta superfamily |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]], [[PRKD2]] |

**Function**, from UniProt [Q99988](https://www.uniprot.org/uniprotkb/Q99988) (reviewed):

> Hormone produced in response to various stresses to confer information about those stresses to the brain, and trigger an aversive response, characterized by nausea, vomiting, and/or loss of appetite (PubMed:23468844, PubMed:24971956, PubMed:28846097, PubMed:28846098, PubMed:28846099, PubMed:28953886, PubMed:29046435, PubMed:30639358, PubMed:31875646, PubMed:33589633, PubMed:38092039). The aversive response is both required to reduce continuing exposure to those stresses at the time of exposure and to promote avoidance behavior in the future (PubMed:30639358, PubMed:33589633, PubMed:38092039). Acts by binding to its receptor, GFRAL, activating GFRAL-expressing neurons localized in the area postrema and nucleus tractus solitarius of the brainstem (PubMed:28846097, PubMed:28846098, PubMed:28846099, PubMed:28953886, PubMed:31535977). It then triggers the activation of neurons localized within the parabrachial nucleus and central amygdala, which constitutes part of the 'emergency circuit' that shapes responses to stressful conditions (PubMed:28953886). The GDF15-GFRAL signal induces expression of genes involved in metabolism, such as lipid metabolism in adipose tissues (PubMed:31402172). Required for avoidance behavior in response to food allergens: induced downstream of mast cell activation to promote aversion and minimize harmful effects of exposure to noxious substances (By similarity). In addition to suppress appetite, also promotes weight loss by enhancing energy expenditure in muscle: acts by increasing calcium futile cycling in muscle (By similarity). Contributes to the effect of metformin, an anti-diabetic drug, on appetite reduction and weight loss: produced in the kidney in response to metformin treatment, thereby activating the GDF15-GFRAL response, leading to reduced appetite and weight (PubMed:31875646, PubMed:37060902). The contribution of GDF15 to weight loss following metformin treatment is however limited and subject to discussion (PubMed:36001956). Produced in response to anticancer drugs, such as camptothecin or cisplatin, promoting nausea, vomiting and contributing to malnutrition (By similarity). Overproduced in many cancers, promoting anorexia in cancer (cachexia) (PubMed:32661391). Responsible for the risk of nausea and vomiting during pregnancy: high levels of GDF15 during pregnancy, mostly originating from the fetus, are associated with increased nausea and vomiting (PubMed:38092039). Maternal sensitivity to nausea is probably determined by pre-pregnancy exposure to GDF15, women with naturally high level of GDF15 being less susceptible to nausea than women with low levels of GDF15 before pregnancy (PubMed:38092039). Promotes metabolic adaptation in response to systemic inflammation caused by bacterial and viral infections in order to promote tissue tolerance and prevent tissue damage (PubMed:31402172). Required for tissue tolerance in response to myocardial infarction by acting as an inhibitor of leukocyte integring activation, thereby protecting against cardiac rupture (By similarity). Inhibits growth hormone signaling on hepatocytes (By similarity)

**Summary**, from NCBI Gene [9518](https://www.ncbi.nlm.nih.gov/gene/9518):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer. The protein is expressed in a broad range of cell types, acts as a pleiotropic cytokine and is involved in the stress response program of cells after cellular injury. Increased protein levels are associated with disease states such as tissue hypoxia, inflammation, acute injury and oxidative stress. [provided by RefSeq, Aug 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30142) · Entrez [9518](https://www.ncbi.nlm.nih.gov/gene/9518) · UniProt [Q99988](https://www.uniprot.org/uniprotkb/Q99988) · Ensembl [ENSG00000130513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130513) · OMIM [605312](https://www.omim.org/entry/605312)

**PubMed**, as HGNC records for this gene — [11895857](https://pubmed.ncbi.nlm.nih.gov/11895857/), [9593718](https://pubmed.ncbi.nlm.nih.gov/9593718/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 22.18 CPM |
| Lines where detected | 47 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 96 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.075× |
| Wild-type minus altered | 1.125× |
| Compounds moving it up in WT lines | 58 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00154 |
| As a percentage | +0.11% |
| FDR, exposure-shuffle null | 0.8388 |
| In TP53-wild-type lines / altered lines | -0.00422 / 0.00544 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.159 raw, 0.035 with 3 PCs removed |

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
