---
symbol: TAB3
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: TGF-beta activated kinase 1 (MAP3K7) binding protein 3
locus: Xp21.2
locus_type: gene with protein product
gene_family: [Zinc fingers RANBP2-type, CUE domain containing]
family_siblings_here: [FUS, MDM2, MDM4]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 58.49
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TAB3

*TGF-beta activated kinase 1 (MAP3K7) binding protein 3* — Xp21.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TAB3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | TGF-beta activated kinase 1 (MAP3K7) binding protein 3 |
| Also known as | TAK1 binding protein 3 |
| Locus | Xp21.2 — gene with protein product |
| Gene families | Zinc fingers RANBP2-type; CUE domain containing |
| Other genes here in those families | [[FUS]], [[MDM2]], [[MDM4]] |
| Previously named | mitogen-activated protein kinase kinase kinase 7 interacting protein 3; TGF-beta activated kinase 1/MAP3K7 binding protein 3; TGF-beta activated kinase 1 and MAP3K7 binding protein 3 |

**Function**, from UniProt [Q8N5C8](https://www.uniprot.org/uniprotkb/Q8N5C8) (reviewed):

> Adapter required to activate the JNK and NF-kappa-B signaling pathways through the specific recognition of 'Lys-63'-linked polyubiquitin chains by its RanBP2-type zinc finger (NZF) (PubMed:14633987, PubMed:14766965, PubMed:15327770, PubMed:22158122). Acts as an adapter linking MAP3K7/TAK1 and TRAF6 to 'Lys-63'-linked polyubiquitin chains (PubMed:14633987, PubMed:14766965, PubMed:15327770, PubMed:22158122, PubMed:36593296). The RanBP2-type zinc finger (NZF) specifically recognizes 'Lys-63'-linked polyubiquitin chains unanchored or anchored to the substrate proteins such as RIPK1/RIP1 and RIPK2: this acts as a scaffold to organize a large signaling complex to promote autophosphorylation of MAP3K7/TAK1, and subsequent activation of I-kappa-B-kinase (IKK) core complex by MAP3K7/TAK1 (PubMed:15327770, PubMed:18079694, PubMed:22158122)

**Summary**, from NCBI Gene [257397](https://www.ncbi.nlm.nih.gov/gene/257397):

> The product of this gene functions in the NF-kappaB signal transduction pathway. The encoded protein, and the similar and functionally redundant protein MAP3K7IP2/TAB2, forms a ternary complex with the protein kinase MAP3K7/TAK1 and either TRAF2 or TRAF6 in response to stimulation with the pro-inflammatory cytokines TNF or IL-1. Subsequent MAP3K7/TAK1 kinase activity triggers a signaling cascade leading to activation of the NF-kappaB transcription factor. The human genome contains a related pseudogene. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30681) · Entrez [257397](https://www.ncbi.nlm.nih.gov/gene/257397) · UniProt [Q8N5C8](https://www.uniprot.org/uniprotkb/Q8N5C8) · Ensembl [ENSG00000157625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157625) · OMIM [300480](https://www.omim.org/entry/300480)

**PubMed**, as HGNC records for this gene — [14633987](https://pubmed.ncbi.nlm.nih.gov/14633987/), [14670075](https://pubmed.ncbi.nlm.nih.gov/14670075/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 58.49 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 125 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.069× |
| Wild-type minus altered | 1.036× |
| Compounds moving it up in WT lines | 66 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00235 |
| As a percentage | -0.16% |
| FDR, exposure-shuffle null | 0.2404 |
| In TP53-wild-type lines / altered lines | -0.00652 / 0.00018 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.173 raw, -0.066 with 3 PCs removed |

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
