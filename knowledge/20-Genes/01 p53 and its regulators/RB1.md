---
symbol: RB1
type: gene
tier: 2
pathway_role: p53 itself and what controls it
aliases: [RB, PPP1R130]
gene_name: RB transcriptional corepressor 1
locus: 13q14.2
locus_type: gene with protein product
gene_family: [Receptor ligands]
family_siblings_here: [HTT, SELPLG]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# RB1

*RB transcriptional corepressor 1* — 13q14.2

> [!summary] In one line
> RB1 encodes the retinoblastoma protein, the pocket protein that holds E2F transcription factors inactive until CDK phosphorylation releases them and licenses S-phase entry.

## What it is

The first tumour suppressor cloned. Its pocket domain binds the E2F transactivation domain while a separate LxCxE surface recruits histone deacetylases and chromatin modifiers, so RB does not merely block E2F but actively represses its target promoters. RB is hypophosphorylated in G0 and early G1, then progressively phosphorylated by cyclin D–CDK4/6 and cyclin E–CDK2, releasing E2F. The [[CDKN2A]]–CDK4–RB–E2F axis is disabled in most cancers, by RB1 loss in retinoblastoma and small-cell lung cancer or by p16 deletion and cyclin D amplification — and intact RB is what CDK4/6 inhibitors require. p53 reaches RB indirectly, through [[CDKN1A]]: p21 inhibits the CDKs, RB stays hypophosphorylated, E2F targets stay off.

## Why it appears in this work

RB1 is scored in the regulon-based activity step and is among the strongest negative associations with measured [[MG53 (TRIM72)]]. The caveat is structural: RB1 is a corepressor, not a sequence-specific activator, so a regulon of "RB1 targets" is really a set of E2F-driven proliferation genes, and inferred RB1 activity is a proliferation readout with its sign flipped ([[Transcription factor activity inference]]).

## What is uncertain

Whether this is about RB1 at all. Its regulon overlaps the E2F and DREAM target set that dominates any arrest response, so an association of this shape would appear wherever some conditions slow the cycle, and it cannot be separated from p21 induction ([[The p21-DREAM axis]]). RB function is set by phosphorylation, not transcript level, so target-based inference and RB1 mRNA answer different questions. No link between RB1 and the TRIM72 promoter is reported, and TRIM72 is not a known E2F target.

## References

- Friend et al., 1986, Nature — identified the retinoblastoma susceptibility gene.
- Buchkovich, Duffy & Harlow, 1989, Cell — showed that the RB protein is phosphorylated in a cell-cycle-dependent manner.
- Litovchick et al., 2007, Molecular Cell — characterised the p130–E2F4 DREAM complex repressing cell-cycle-dependent genes in quiescence.
- Dyson, 2016, Genes & Development — review reassessing RB1 as prototype tumour suppressor and the gaps in the E2F-only account.

## What is on record

| | |
|---|---|
| Official name | RB transcriptional corepressor 1 |
| Also known as | RB, PPP1R130, prepro-retinoblastoma-associated protein, protein phosphatase 1, regulatory subunit 130 |
| Locus | 13q14.2 — gene with protein product |
| Gene families | Receptor ligands |
| Other genes here in those families | [[HTT]], [[SELPLG]] |
| Previously named | osteosarcoma; retinoblastoma 1 |

**Function**, from UniProt [P06400](https://www.uniprot.org/uniprotkb/P06400) (reviewed):

> Tumor suppressor that is a key regulator of the G1/S transition of the cell cycle (PubMed:10499802, PubMed:39441926). The hypophosphorylated form binds transcription regulators of the E2F family, preventing transcription of E2F-responsive genes (PubMed:10499802). Both physically blocks E2Fs transactivating domain and recruits chromatin-modifying enzymes that actively repress transcription (PubMed:10499802). Cyclin and CDK-dependent phosphorylation of RB1 induces its dissociation from E2Fs, thereby activating transcription of E2F responsive genes and triggering entry into S phase (PubMed:10499802). RB1 also promotes the G0-G1 transition upon phosphorylation and activation by CDK3/cyclin-C (PubMed:15084261). Directly involved in heterochromatin formation by maintaining overall chromatin structure and, in particular, that of constitutive heterochromatin by stabilizing histone methylation. Recruits and targets histone methyltransferases SUV39H1, KMT5B and KMT5C, leading to epigenetic transcriptional repression. Controls histone H4 'Lys-20' trimethylation. Inhibits the intrinsic kinase activity of TAF1. Mediates transcriptional repression by SMARCA4/BRG1 by recruiting a histone deacetylase (HDAC) complex to the c-FOS promoter. In resting neurons, transcription of the c-FOS promoter is inhibited by BRG1-dependent recruitment of a phospho-RB1-HDAC1 repressor complex. Upon calcium influx, RB1 is dephosphorylated by calcineurin, which leads to release of the repressor complex (By similarity)

**Summary**, from NCBI Gene [5925](https://www.ncbi.nlm.nih.gov/gene/5925):

> The protein encoded by this gene is a negative regulator of the cell cycle and was the first tumor suppressor gene found. The encoded protein also stabilizes constitutive heterochromatin to maintain the overall chromatin structure. The active, hypophosphorylated form of the protein binds transcription factor E2F1. Defects in this gene are a cause of childhood cancer retinoblastoma (RB), bladder cancer, and osteogenic sarcoma. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9884) · Entrez [5925](https://www.ncbi.nlm.nih.gov/gene/5925) · UniProt [P06400](https://www.uniprot.org/uniprotkb/P06400) · Ensembl [ENSG00000139687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139687) · OMIM [614041](https://www.omim.org/entry/614041)

**PubMed**, as HGNC records for this gene — [1857421](https://pubmed.ncbi.nlm.nih.gov/1857421/), [15057823](https://pubmed.ncbi.nlm.nih.gov/15057823/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00298 |
| As a percentage | +0.21% |
| FDR, exposure-shuffle null | 0.0808 |
| In TP53-wild-type lines / altered lines | 0.00314 / 0.00288 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.266 raw, 0.325 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 31 targets |
| Activity vs MG53 across exposures (r) | -0.268 (q 6.18e-14) |
| With 3 principal components removed | -0.266 (q 5.66e-14) |
| Within line, across exposures (r) | 0.014 (q 0.468) |
| Percentile against all genes | 0.5 |

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
