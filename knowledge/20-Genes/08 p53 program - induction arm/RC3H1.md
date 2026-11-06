---
symbol: RC3H1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA2025, roquin, RP5-1198E17.5, RNF198]
gene_name: ring finger and CCCH-type domains 1
locus: 1q25.1
locus_type: gene with protein product
gene_family: [Ring finger proteins, Zinc fingers CCCH-type, RING finger E3 ubiquitin protein ligases]
family_siblings_here: [C12orf50, COP1, HELZ, MDM2, MDM4, MGRN1, PAN3, PCGF3, TRIM72]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 188.29
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RC3H1

*ring finger and CCCH-type domains 1* — 1q25.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RC3H1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ring finger and CCCH-type domains 1 |
| Also known as | KIAA2025, roquin, RP5-1198E17.5, RNF198, KIAA2025 protein, roquin-1 |
| Locus | 1q25.1 — gene with protein product |
| Gene families | Ring finger proteins; Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Other genes here in those families | [[C12orf50]], [[COP1]], [[HELZ]], [[MDM2]], [[MDM4]], [[MGRN1]], [[PAN3]], [[PCGF3]], [[TRIM72]] |
| Previously named | ring finger and CCCH-type zinc finger domains 1 |

**Function**, from UniProt [Q5TC82](https://www.uniprot.org/uniprotkb/Q5TC82) (reviewed):

> Post-transcriptional repressor of mRNAs containing a conserved stem loop motif, called constitutive decay element (CDE), which is often located in the 3'-UTR, as in HMGXB3, ICOS, IER3, NFKBID, NFKBIZ, PPP1R10, TNF, TNFRSF4 and in many more mRNAs (PubMed:25026078, PubMed:31636267). Cleaves translationally inactive mRNAs harboring a stem-loop (SL), often located in their 3'-UTRs, during the early phase of inflammation in a helicase UPF1-independent manner (By similarity). Binds to CDE and promotes mRNA deadenylation and degradation. This process does not involve miRNAs (By similarity). In follicular helper T (Tfh) cells, represses of ICOS and TNFRSF4 expression, thus preventing spontaneous Tfh cell differentiation, germinal center B-cell differentiation in the absence of immunization and autoimmunity (By similarity). In resting or LPS-stimulated macrophages, controls inflammation by suppressing TNF expression (By similarity). Also recognizes CDE in its own mRNA and in that of paralogous RC3H2, possibly leading to feedback loop regulation (By similarity). Recognizes and binds mRNAs containing a hexaloop stem-loop motif, called alternative decay element (ADE) (By similarity). Together with ZC3H12A, destabilizes TNFRSF4/OX40 mRNA by binding to the conserved stem loop structure in its 3'UTR (By similarity). Able to interact with double-stranded RNA (dsRNA) (PubMed:25026078, PubMed:25504471). miRNA-binding protein that regulates microRNA homeostasis. Enhances DICER-mediated processing of pre-MIR146a but reduces mature MIR146a levels through an increase of 3' end uridylation. Both inhibits ICOS mRNA expression and they may act together to exert the suppression (PubMed:25697406, PubMed:31636267). Acts as a ubiquitin E3 ligase. Pairs with E2 enzymes UBE2A, UBE2B, UBE2D2, UBE2F, UBE2G1, UBE2G2 and UBE2L3 and produces polyubiquitin chains (PubMed:26489670). Shows the strongest activity when paired with UBE2N:UBE2V1 or UBE2N:UBE2V2 E2 complexes and generate both short and long polyubiquitin chains (PubMed:26489670)

**Summary**, from NCBI Gene [149041](https://www.ncbi.nlm.nih.gov/gene/149041):

> This gene encodes a protein containing RING-type and C3H1-type zinc finger motifs. The encoded protein recognizes and binds to a constitutive decay element (CDE) in the 3' UTR of mRNAs, leading to mRNA deadenylation and degradation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29434) · Entrez [149041](https://www.ncbi.nlm.nih.gov/gene/149041) · UniProt [Q5TC82](https://www.uniprot.org/uniprotkb/Q5TC82) · Ensembl [ENSG00000135870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135870) · OMIM [609424](https://www.omim.org/entry/609424)

**PubMed**, as HGNC records for this gene — [15917799](https://pubmed.ncbi.nlm.nih.gov/15917799/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 188.29 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 126 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.058× |
| Wild-type minus altered | 1.019× |
| Compounds moving it up in WT lines | 77 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00076 |
| As a percentage | -0.05% |
| FDR, exposure-shuffle null | 0.7179 |
| In TP53-wild-type lines / altered lines | -0.00040 / -0.00099 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.217 raw, 0.085 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
