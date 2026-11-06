---
symbol: DNMT3A
type: gene
tier: 2
pathway_role: transcription factor
gene_name: DNA methyltransferase 3 alpha
locus: 2p23.3
locus_type: gene with protein product
gene_family: [PWWP domain containing, MicroRNA protein coding host genes, 7BS C5-cytosine DNA/RNA methyltransferases, DNA/RNA methyltransferases]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L, PER1]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# DNMT3A

*DNA methyltransferase 3 alpha* — 2p23.3

> [!summary] In one line
> DNMT3A is a de novo DNA methyltransferase that writes new CpG methylation, and one of the most frequently mutated genes in myeloid disease.

## What it is

With DNMT3B, DNMT3A methylates CpGs that were previously unmethylated; DNMT1 then copies the pattern through replication. Two reader domains aim it: an ADD domain that binds histone H3 only when K4 is unmethylated, autoinhibiting catalysis until it does, and a PWWP domain that reads H3K36 methylation and aims the enzyme at gene bodies and heterochromatin. Loss in mouse stem cells expands the stem compartment and impairs differentiation; the human R882H hotspot acts dominant-negatively by disrupting tetramer formation; and DNMT3A is the most common lesion in age-related clonal haematopoiesis. Germline mutation causes an overgrowth and intellectual-disability syndrome.

## Why it appears in this work

DNMT3A is scored in the regulon-based activity step and sits at the bottom of that ranking. TRIM72 is a muscle gene silent in these non-muscle lines, and promoter methylation is an obvious candidate for that silence; a strong negative rank for a methyltransferase is at least a coherent direction. See [[Transcription factor activity inference]] and [[The TRIM72 locus]].

## What is uncertain

Calling DNMT3A a transcription factor is a stretch: it has no sequence specificity of its own, and its curated regulon is assembled from genes whose expression tracks methylation, so the sign attached to it is hard to read. Nothing shows DNMT3A methylates the TRIM72 promoter, here or anywhere. Two confounds: the compound panel includes DNA methyltransferase inhibitors, which move this pathway directly, and methylation changes slowly relative to a 24 h readout.

## References

- Okano et al., 1999, Cell — Dnmt3a and Dnmt3b are required for de novo methylation and mammalian development.
- Ley et al., 2010, New England Journal of Medicine — identified recurrent DNMT3A mutations in acute myeloid leukaemia.
- Challen et al., 2011, Nature Genetics — Dnmt3a loss expands haematopoietic stem cells and blocks differentiation.
- Jaiswal et al., 2014, New England Journal of Medicine — age-related clonal haematopoiesis, with DNMT3A the most common driver.
- Tatton-Brown et al., 2014, Nature Genetics — germline DNMT3A mutations cause an overgrowth syndrome with intellectual disability.

## What is on record

| | |
|---|---|
| Official name | DNA methyltransferase 3 alpha |
| Also known as | — (no recorded alias) |
| Locus | 2p23.3 — gene with protein product |
| Gene families | PWWP domain containing; MicroRNA protein coding host genes; 7BS C5-cytosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]], [[PRKD2]] |
| Previously named | DNA (cytosine-5-)-methyltransferase 3 alpha |

**Function**, from UniProt [Q9Y6K1](https://www.uniprot.org/uniprotkb/Q9Y6K1) (reviewed):

> DNA (cytosine-5)-methyltransferase that mediates genome-wide de novo methylation and which is essential for the establishment of DNA methylation patterns during development (PubMed:12138111, PubMed:16357870, PubMed:20838592, PubMed:29414941, PubMed:30478443, PubMed:31485078). It modifies DNA in a non-processive manner and methylates both CpG and non-CpG sites (PubMed:12138111, PubMed:16357870, PubMed:30478443). Modifies DNA at CpG sites with selectivity for residues flanking the target CpG site at positions -2 and +2 (PubMed:20838592). Preferentially methylates DNA linker regions between two nucleosomal cores and is inhibited by histone H1 (By similarity). DNA methylation is coordinated with methylation of histones (PubMed:12138111, PubMed:16357870, PubMed:30478443, PubMed:31485078). Recruited to dimethylated 'Lys-36' of histone H3 (H3K36me2) at intergenic regions and trimethylated 'Lys-36' of histone H3 (H3K36me3) sites on gene bodies to mediate de novo DNA methylation (PubMed:31485078). Plays a role in paternal and maternal imprinting: required for methylation of most imprinted loci in germ cells (By similarity). Also has weak auto-methylation activity on Cys-706 in absence of DNA (By similarity). Acts as a transcriptional corepressor for ZBTB18; can actively repress transcription through the recruitment of HDAC activity (By similarity)

**Summary**, from NCBI Gene [1788](https://www.ncbi.nlm.nih.gov/gene/1788):

> CpG methylation is an epigenetic modification that is important for embryonic development, imprinting, and X-chromosome inactivation. Studies in mice have demonstrated that DNA methylation is required for mammalian development. This gene encodes a DNA methyltransferase that is thought to function in de novo methylation, rather than maintenance methylation. The protein localizes to the cytoplasm and nucleus and its expression is developmentally regulated. [provided by RefSeq, Mar 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2978) · Entrez [1788](https://www.ncbi.nlm.nih.gov/gene/1788) · UniProt [Q9Y6K1](https://www.uniprot.org/uniprotkb/Q9Y6K1) · Ensembl [ENSG00000119772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119772) · OMIM [602769](https://www.omim.org/entry/602769)

**PubMed**, as HGNC records for this gene — [9662389](https://pubmed.ncbi.nlm.nih.gov/9662389/), [10433969](https://pubmed.ncbi.nlm.nih.gov/10433969/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00142 |
| As a percentage | +0.10% |
| FDR, exposure-shuffle null | 0.7483 |
| In TP53-wild-type lines / altered lines | -0.00709 / 0.00679 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.130 raw, 0.276 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 50 targets |
| Activity vs MG53 across exposures (r) | -0.235 (q 3.73e-12) |
| With 3 principal components removed | -0.186 (q 3.27e-08) |
| Within line, across exposures (r) | -0.034 (q 0.007) |
| Percentile against all genes | 1.7 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, negative rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
