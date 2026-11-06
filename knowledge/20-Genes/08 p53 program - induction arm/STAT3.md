---
symbol: STAT3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [APRF]
gene_name: signal transducer and activator of transcription 3
locus: 17q21.2
locus_type: gene with protein product
gene_family: [SH2 domain containing, Signal transducer and activator of transcription family]
family_siblings_here: [SH2D4B, STAT4]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 251.18
mg53_verdict: none
tags: [gene, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# STAT3

*signal transducer and activator of transcription 3* — 17q21.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/STAT3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | signal transducer and activator of transcription 3 |
| Also known as | APRF |
| Locus | 17q21.2 — gene with protein product |
| Gene families | SH2 domain containing; Signal transducer and activator of transcription family |
| Other genes here in those families | [[SH2D4B]], [[STAT4]] |
| Previously named | signal transducer and activator of transcription 3 (acute-phase response factor) |

**Function**, from UniProt [P40763](https://www.uniprot.org/uniprotkb/P40763) (reviewed):

> Signal transducer and transcription activator that mediates cellular responses to interleukins, KITLG/SCF, LEP and other growth factors (PubMed:10688651, PubMed:11294841, PubMed:12359225, PubMed:12873986, PubMed:15194700, PubMed:15653507, PubMed:16285960, PubMed:17344214, PubMed:18242580, PubMed:18782771, PubMed:22306293, PubMed:23084476, PubMed:28262505, PubMed:32929201, PubMed:38404237). Once activated, recruits coactivators, such as NCOA1 or MED1, to the promoter region of the target gene (PubMed:15653507, PubMed:16285960, PubMed:17344214, PubMed:18782771, PubMed:28262505, PubMed:32929201). May mediate cellular responses to activated FGFR1, FGFR2, FGFR3 and FGFR4 (PubMed:12873986). Upon activation of IL6ST/gp130 signaling by interleukin-6 (IL6), binds to the IL6-responsive elements identified in the promoters of various acute-phase protein genes (PubMed:12359225). Activated by IL31 through IL31RA (PubMed:15194700). Acts as a regulator of inflammatory response by regulating differentiation of naive CD4(+) T-cells into T-helper Th17 or regulatory T-cells (Treg): acetylation promotes its transcription activity and cell differentiation while deacetylation and oxidation of lysine residues by LOXL3 inhibits differentiation (PubMed:28065600, PubMed:28262505). Involved in cell cycle regulation by inducing the expression of key genes for the progression from G1 to S phase, such as CCND1 (PubMed:17344214). Mediates the effects of LEP on melanocortin production, body energy homeostasis and lactation (By similarity). May play an apoptotic role by transactivating BIRC5 expression under LEP activation (PubMed:18242580). Cytoplasmic STAT3 represses macroautophagy by inhibiting EIF2AK2/PKR activity (PubMed:23084476). Plays a crucial role in basal beta cell functions, such as regulation of insulin secretion (By similarity). Following JAK/STAT signaling activation and as part of a complex with NFATC3 and NFATC4, binds to the alpha-beta E4 promoter region of CRYAB and activates transcription in cardiomyocytes (By similarity). Involved in the oncostatin-M-mediated signaling pathway through both type I OSM receptor complex (heterodimers composed of LIFR and IL6ST) and type II OSM receptor complex (heterodimers composed of OSMR and IL6ST) (PubMed:9188471)

**Summary**, from NCBI Gene [6774](https://www.ncbi.nlm.nih.gov/gene/6774):

> The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein is activated through phosphorylation in response to various cytokines and growth factors including IFNs, EGF, IL5, IL6, HGF, LIF and BMP2. This protein mediates the expression of a variety of genes in response to cell stimuli, and thus plays a key role in many cellular processes such as cell growth and apoptosis. The small GTPase Rac1 has been shown to bind and regulate the activity of this protein. PIAS3 protein is a specific inhibitor of this protein. This gene also plays a role in regulating host response to viral and bacterial infections. Mutations in this gene are associated with infantile-onset multisystem autoimmune disease and hyper-immunoglobulin E syndrome. [provided by RefSeq, Aug 2020]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11364) · Entrez [6774](https://www.ncbi.nlm.nih.gov/gene/6774) · UniProt [P40763](https://www.uniprot.org/uniprotkb/P40763) · Ensembl [ENSG00000168610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168610) · OMIM [102582](https://www.omim.org/entry/102582)

**PubMed**, as HGNC records for this gene — [7512451](https://pubmed.ncbi.nlm.nih.gov/7512451/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 251.18 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 118 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.042× |
| Wild-type minus altered | 1.036× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00112 |
| As a percentage | -0.08% |
| FDR, exposure-shuffle null | 0.7812 |
| In TP53-wild-type lines / altered lines | -0.00048 / -0.00150 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.110 raw, -0.024 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 336 targets |
| Activity vs MG53 across exposures (r) | 0.078 (q 0.027) |
| With 3 principal components removed | 0.089 (q 0.014) |
| Within line, across exposures (r) | -0.017 (q 0.374) |
| Percentile against all genes | 60.2 |

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
