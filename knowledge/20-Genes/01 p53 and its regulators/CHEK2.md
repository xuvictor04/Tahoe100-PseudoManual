---
symbol: CHEK2
type: gene
tier: 1
pathway_role: p53 itself and what controls it
aliases: [CDS1, CHK2, HuCds1, PP1425, bA444G7]
gene_name: checkpoint kinase 2
locus: 22q12.1
locus_type: gene with protein product
gene_family: [Checkpoint kinase 2 family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CHEK2

*checkpoint kinase 2* — 22q12.1

> [!summary] In one line
> CHEK2 encodes CHK2, the checkpoint kinase that ATM activates after DNA double-strand breaks and that phosphorylates p53 and the CDC25 phosphatases to enforce arrest.

## What it is

CHK2 is a serine/threonine kinase built from an N-terminal SQ/TQ cluster, a forkhead-associated (FHA) domain and a C-terminal kinase domain. Its activation is the canonical double-strand-break cascade: ATM phosphorylates T68 in the SQ/TQ cluster, the phosphothreonine is read by the FHA domain of a partner molecule so CHK2 transiently dimerises, autophosphorylation in the activation loop follows, and the kinase disperses as an active monomer. That mechanism makes CHK2 a signal amplifier — a localised ATM signal at a break becomes a diffusible, nucleus-wide kinase activity.

Its substrates define two parallel outputs. CHK2 phosphorylates p53 at S20, which sits in the MDM2-binding surface, and the standard model is that this contributes to p53 stabilisation — placing CHK2 upstream of everything in [[The p53 pathway]]. Independently, CHK2 phosphorylates CDC25A, driving its degradation, and CDC25C, promoting 14-3-3 sequestration; either way CDK-activating phosphatase activity falls and the cell cycle halts without any transcription being required. CHK2 also acts on BRCA1, E2F1 and PML. It is the DSB-responsive counterpart to CHK1, which is activated by ATR and handles replication stress; the two are often conflated and should not be.

Clinically, CHEK2 matters mainly through germline variation. The truncating allele 1100delC and other loss-of-function variants confer moderately increased risk of breast cancer and, less strongly, prostate and colorectal cancer. Truncating CHEK2 variants were originally reported in families with a Li-Fraumeni-like presentation, which is where the gene's reputation as a p53-pathway tumour suppressor began.

## Why it appears in this work

CHEK2 sits upstream of p53, not downstream of it, which is the whole reason it belongs in this vault alongside ATM, MDM2 and USP7. Many of the 379 compounds in [[Tahoe-100M]] are genotoxic, and CHK2 is part of the machinery that decides whether a given line converts that damage into p53 transcriptional output at all. It should therefore not be read as a member of [[p53 program P]] — its own transcript is not a strongly p53-inducible one — but as part of the explanation for why two TP53-wild-type lines can differ in how much p53 output an exposure produces.

## What is uncertain

How much p53 activation actually requires CHK2 is contested, and the two best experiments disagree. Chk2-deficient mice are radioresistant with defective p53-mediated transcription, implying CHK2 is important; somatic knockout of CHEK2 in human colorectal cancer cells left p53 responses intact, implying it is not. The S20 phosphorylation model is drawn in nearly every pathway diagram, but whether that site is necessary for stabilisation is disputed, and ATM phosphorylates p53 at S15 without CHK2's help. The germline story has also shifted: the Li-Fraumeni attribution has largely not held up, CHEK2 is now classed as a moderate-penetrance gene, and the effect of many missense variants remains uncertain. For this study the practical caveat is that CHK2 activity is set by phosphorylation and dimerisation, so an mRNA level is a weak proxy for how much of the kinase is actually working.

## References

- Matsuoka, Huang & Elledge, 1998, Science — linked ATM to cell-cycle regulation through the CHK2 kinase.
- Bell et al., 1999, Science — reported heterozygous germline CHEK2 mutations in Li-Fraumeni syndrome.
- Hirao et al., 2000, Science — DNA-damage-induced activation of p53 by the checkpoint kinase Chk2.
- Takai et al., 2002, The EMBO Journal — Chk2-deficient mice are radioresistant and show defective p53-mediated transcription.
- Jallepalli et al., 2003, Journal of Biological Chemistry — CHEK2 knockout in human cancer cells left p53 responses intact, the main counterweight to the mouse result.
- Meijers-Heijboer et al., 2002, Nature Genetics — established CHEK2*1100delC as a low-penetrance breast cancer susceptibility allele.
- Zannini, Delia & Buscemi, 2014, Journal of Molecular Cell Biology — review of CHK2 in the DNA damage response.

## What is on record

| | |
|---|---|
| Official name | checkpoint kinase 2 |
| Also known as | CDS1, CHK2, HuCds1, PP1425, bA444G7 |
| Locus | 22q12.1 — gene with protein product |
| Gene families | Checkpoint kinase 2 family |
| Previously named | CHK2 (checkpoint, S.pombe) homolog; CHK2 checkpoint homolog (S. pombe) |

**Function**, from UniProt [O96017](https://www.uniprot.org/uniprotkb/O96017) (reviewed):

> Serine/threonine-protein kinase which is required for checkpoint-mediated cell cycle arrest, activation of DNA repair and apoptosis in response to the presence of DNA double-strand breaks. May also negatively regulate cell cycle progression during unperturbed cell cycles. Following activation, phosphorylates numerous effectors preferentially at the consensus sequence [L-X-R-X-X-S/T] (PubMed:37943659). Regulates cell cycle checkpoint arrest through phosphorylation of CDC25A, CDC25B and CDC25C, inhibiting their activity. Inhibition of CDC25 phosphatase activity leads to increased inhibitory tyrosine phosphorylation of CDK-cyclin complexes and blocks cell cycle progression. May also phosphorylate NEK6 which is involved in G2/M cell cycle arrest. Regulates DNA repair through phosphorylation of BRCA2, enhancing the association of RAD51 with chromatin which promotes DNA repair by homologous recombination. Also stimulates the transcription of genes involved in DNA repair (including BRCA2) through the phosphorylation and activation of the transcription factor FOXM1. Regulates apoptosis through the phosphorylation of p53/TP53, MDM4 and PML. Phosphorylation of p53/TP53 at 'Ser-20' by CHEK2 may alleviate inhibition by MDM2, leading to accumulation of active p53/TP53. Phosphorylation of MDM4 may also reduce degradation of p53/TP53. Also controls the transcription of pro-apoptotic genes through phosphorylation of the transcription factor E2F1. Tumor suppressor, it may also have a DNA damage-independent function in mitotic spindle assembly by phosphorylating BRCA1. Its absence may be a cause of the chromosomal instability observed in some cancer cells. Promotes the CCAR2-SIRT1 association and is required for CCAR2-mediated SIRT1 inhibition (PubMed:25361978). Under oxidative stress, promotes ATG7 ubiquitination by phosphorylating the E3 ubiquitin ligase TRIM32 at 'Ser-55' leading to positive regulation of the autophagosme assembly (PubMed:37943659)

**Summary**, from NCBI Gene [11200](https://www.ncbi.nlm.nih.gov/gene/11200):

> In response to DNA damage and replication blocks, cell cycle progression is halted through the control of critical cell cycle regulators. The protein encoded by this gene is a cell cycle checkpoint regulator and putative tumor suppressor. It contains a forkhead-associated protein interaction domain essential for activation in response to DNA damage and is rapidly phosphorylated in response to replication blocks and DNA damage. When activated, the encoded protein is known to inhibit CDC25C phosphatase, preventing entry into mitosis, and has been shown to stabilize the tumor suppressor protein p53, leading to cell cycle arrest in G1. In addition, this protein interacts with and phosphorylates BRCA1, allowing BRCA1 to restore survival after DNA damage. Mutations in this gene have been linked with Li-Fraumeni syndrome, a highly penetrant familial cancer phenotype usually associated with inherited mutations in TP53. Also, mutations in this gene are thought to confer a predisposition to sarcomas, breast cancer, and brain tumors. This nuclear protein is a member of the CDS1 subfamily of serine/threonine protein kinases. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16627) · Entrez [11200](https://www.ncbi.nlm.nih.gov/gene/11200) · UniProt [O96017](https://www.uniprot.org/uniprotkb/O96017) · Ensembl [ENSG00000183765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183765) · OMIM [604373](https://www.omim.org/entry/604373)

**PubMed**, as HGNC records for this gene — [9836640](https://pubmed.ncbi.nlm.nih.gov/9836640/), [10097108](https://pubmed.ncbi.nlm.nih.gov/10097108/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00131 |
| As a percentage | -0.09% |
| FDR, exposure-shuffle null | 0.7114 |
| In TP53-wild-type lines / altered lines | -0.00033 / -0.00191 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.061 raw, -0.188 with 3 PCs removed |

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
