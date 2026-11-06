---
symbol: STK11
type: gene
tier: 1
pathway_role: p53 itself and what controls it
aliases: [LKB1]
gene_name: serine/threonine kinase 11
locus: 19p13.3
locus_type: gene with protein product
gene_family: [STK11 family kinases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# STK11

*serine/threonine kinase 11* — 19p13.3

> [!summary] In one line
> STK11 encodes LKB1, the master upstream kinase that activates AMPK and twelve related kinases, and the tumour suppressor whose germline loss causes Peutz-Jeghers syndrome.

## What it is

LKB1 is a serine/threonine kinase that does not work alone: it is an obligate heterotrimer with the pseudokinase STRADα and the scaffold MO25/CAB39, which together activate it and set its localisation. In that form it is largely constitutively active — the always-on upstream element, the regulation sitting in its substrates.

LKB1 phosphorylates the activation-loop threonine of AMPKα, and the equivalent residue in twelve other AMPK-family kinases: the salt-inducible kinases, the MARK/PAR-1 polarity kinases, the BRSKs, the NUAKs and SNRK. The AMPK arm is the best known: as AMP rises relative to ATP, AMPK becomes sensitive to LKB1 phosphorylation, and its activation shuts down anabolic ATP consumption and restrains mTORC1 via TSC2 and raptor. Cells lacking LKB1 fail to activate AMPK under energy stress and lose the associated checkpoint — the core of LKB1's metabolic tumour-suppressor account. The MARK and SIK arms carry polarity and CRTC/HDAC-dependent transcriptional functions.

Germline loss-of-function causes Peutz-Jeghers syndrome: hamartomatous gastrointestinal polyposis, mucocutaneous pigmentation and markedly elevated cancer risk. Somatically it is among the more frequently inactivated genes in lung adenocarcinoma, often co-mutant with KRAS, and in cervical and pancreatic cancers; the STK11/KRAS double-mutant subgroup is immunotherapy-resistant and immune-cold.

## Why it appears in this work

STK11 is here as an upstream, contextual gene, not a p53 target: one of the routes by which p53 output can be lowered in a line that is TP53-wild-type by sequence. The link runs through AMPK, which on energy stress engages a p53-dependent metabolic checkpoint; losing LKB1 removes that input. Several of this panel's nominally wild-type lines carry truncating STK11 alleles — exactly the problem in [[p53 nullification in cancer cell lines]]: a wild-type-versus-altered split defined on TP53 does not make the wild-type group homogeneous. STK11 belongs with [[CDKN2A]], [[MDM4]], [[PPM1D]] and [[ATM]] in that annotation layer rather than with [[p53 program P]].

## What is uncertain

The attenuation argument is narrower than it appears. The AMPK-to-p53 checkpoint was characterised under energy stress; most compounds here act through DNA damage, replication stress or MDM2 inhibition, and whether LKB1 loss blunts p53's response to those is not established. LKB1 loss plausibly lowers basal and metabolic-stress p53 tone; it has not been shown to damp the responses measured here.

Whether AMPK is the relevant effector for LKB1's tumour suppression is contested: LKB1 has twelve other substrates, in several models the SIK branch accounts for more of the phenotype, and AMPK itself can support or restrain tumour growth by context. "LKB1 loss removes a tumour-suppressive AMPK signal" simplifies an unsettled question. The p53 step is also open: AMPK-dependent p53 serine-15 phosphorylation is reported, but its contribution relative to ATM and ATR at endogenous levels is not well quantified.

One measurement caveat: STK11 transcript level is an unreliable proxy for LKB1 function. Truncating alleles may or may not reduce mRNA through nonsense-mediated decay, and a kinase-impairing missense allele leaves the transcript intact, so an mRNA panel cannot distinguish an LKB1-null line from a functional one.

## References

- Hemminki et al., 1998, Nature — identified a serine/threonine kinase gene defective in Peutz-Jeghers syndrome.
- Jenne et al., 1998, Nature Genetics — independently showed Peutz-Jeghers syndrome is caused by mutations in this novel serine/threonine kinase.
- Lizcano et al., 2004, EMBO Journal — LKB1 is a master kinase activating thirteen AMPK-subfamily kinases, including MARK/PAR-1.
- Shaw et al., 2004, PNAS — LKB1 directly activates AMPK and is required for the apoptotic response to energy stress.
- Jones et al., 2005, Molecular Cell — AMPK activation induces a p53-dependent metabolic checkpoint.
- Skoulidis et al., 2018, Cancer Discovery — STK11/LKB1 loss associates with resistance to PD-1 blockade in KRAS-mutant lung adenocarcinoma.

## What is on record

| | |
|---|---|
| Official name | serine/threonine kinase 11 |
| Also known as | PJS, LKB1, polarization-related protein LKB1 |
| Locus | 19p13.3 — gene with protein product |
| Gene families | STK11 family kinases |
| Previously named | serine/threonine kinase 11 (Peutz-Jeghers syndrome) |

**Function**, from UniProt [Q15831](https://www.uniprot.org/uniprotkb/Q15831) (reviewed):

> Tumor suppressor serine/threonine-protein kinase that controls the activity of AMP-activated protein kinase (AMPK) family members, thereby playing a role in various processes such as cell metabolism, cell polarity, apoptosis and DNA damage response (PubMed:12805220, PubMed:14517248, PubMed:14976552, PubMed:15016379, PubMed:15733851). Acts by phosphorylating the T-loop of AMPK family proteins, thus promoting their activity: phosphorylates PRKAA1, PRKAA2, BRSK1, BRSK2, MARK1, MARK2, MARK3, MARK4, NUAK1, NUAK2, SIK1, SIK2, SIK3 and SNRK but not MELK (PubMed:12805220, PubMed:14517248, PubMed:14976552, PubMed:15016379, PubMed:15733851). Also phosphorylates non-AMPK family proteins such as STRADA, PTEN and possibly p53/TP53 (PubMed:11430832, PubMed:15987703). Acts as a key upstream regulator of AMPK by mediating phosphorylation and activation of AMPK catalytic subunits PRKAA1 and PRKAA2 and thereby regulates processes including: inhibition of signaling pathways that promote cell growth and proliferation when energy levels are low, glucose homeostasis in liver, activation of autophagy when cells undergo nutrient deprivation, and B-cell differentiation in the germinal center in response to DNA damage (PubMed:14976552). Also acts as a regulator of cellular polarity by remodeling the actin cytoskeleton (PubMed:15016379). Required for cortical neuron polarization by mediating phosphorylation and activation of BRSK1 and BRSK2, leading to axon initiation and specification (PubMed:14976552). Involved in DNA damage response: interacts with p53/TP53 and recruited to the CDKN1A/WAF1 promoter to participate in transcription activation (PubMed:11430832, PubMed:17108107, PubMed:21317932). Able to phosphorylate p53/TP53; the relevance of such result in vivo is however unclear and phosphorylation may be indirect and mediated by downstream STK11/LKB1 kinase NUAK1 (PubMed:11430832, PubMed:17108107, PubMed:21317932). Also acts as a mediator of p53/TP53-dependent apoptosis via interaction with p53/TP53: translocates to the mitochondrion during apoptosis and regulates p53/TP53-dependent apoptosis pathways (PubMed:11430832, PubMed:17108107, PubMed:21317932). Regulates UV radiation-induced DNA damage response mediated by CDKN1A (PubMed:25329316). In association with NUAK1, phosphorylates CDKN1A in response to UV radiation and contributes to its degradation which is necessary for optimal DNA repair (PubMed:25329316)

**Summary**, from NCBI Gene [6794](https://www.ncbi.nlm.nih.gov/gene/6794):

> The protein encoded by this gene is a serine/threonine kinase that regulates cell polarity and energy metabolism and functions as a tumor suppressor. Mutations in this gene have been associated with the autosomal dominant Peutz-Jeghers syndrome, as well as with skin, pancreatic, and testicular cancers. [provided by RefSeq, May 2022]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11389) · Entrez [6794](https://www.ncbi.nlm.nih.gov/gene/6794) · UniProt [Q15831](https://www.uniprot.org/uniprotkb/Q15831) · Ensembl [ENSG00000118046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118046) · OMIM [602216](https://www.omim.org/entry/602216)

**PubMed**, as HGNC records for this gene — [9425897](https://pubmed.ncbi.nlm.nih.gov/9425897/), [34479873](https://pubmed.ncbi.nlm.nih.gov/34479873/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00350 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.2827 |
| In TP53-wild-type lines / altered lines | -0.00277 / 0.00717 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.435 raw, 0.047 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
