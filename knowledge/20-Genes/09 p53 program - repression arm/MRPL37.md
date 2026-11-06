---
symbol: MRPL37
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [mitochondrial ribosomal protein L37]
gene_name: mitochondrial ribosomal protein L37
locus: 1p32.3
locus_type: gene with protein product
gene_family: [Mitochondrial ribosomal proteins, Large subunit mitochondrial ribosomal proteins]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 30.13
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# MRPL37

*mitochondrial ribosomal protein L37* — 1p32.3

> [!summary] In one line
> MRPL37 encodes mL37, a nuclear-encoded structural protein of the large subunit of the mitochondrial ribosome.

## What it is

The mitoribosome translates the thirteen OXPHOS subunits encoded by mitochondrial DNA; all of its own protein components are encoded in the nucleus and imported. MRPL37 is one of them, a constituent of the large (39S) subunit, placed in the structure by the cryo-EM work that resolved the human mitoribosome and associated with the inner membrane where translation is coupled to membrane insertion. It belongs to the mL37/mL65 family, proteins with no bacterial counterpart. Beyond structural placement and RNA binding its individual contribution is not separately characterised, and vendor claims of mitochondrial-disease association are not backed by a primary study I can cite. The gene is at 1p32.3.

## Why it appears in this work

It is carried as a member of the repression arm of [[p53 program P]], so its slope has to be read through the sign convention in [[Signing genes by p53 direction]] before it says anything about p53 output.

## What is uncertain

Whether MRPL37 carries information of its own is doubtful. Mitoribosome subunits move as one tightly co-regulated module, so a slope on MRPL37 is effectively a slope on mitochondrial biogenesis, nearly collinear with dozens of other MRPL and MRPS genes — which is also the most economical explanation for its repression-arm membership, since arrest lowers biosynthetic capacity generally. No p53 response element at the locus has been reported, and p53's reported effects on mitochondrial biogenesis run in both directions, so even the expected sign is not secure.

## References

- Brown et al., 2014, Science — structure of the large subunit of the human mitochondrial ribosome, resolving its protein complement.
- Amunts et al., 2015, Science — structure of the complete human mitoribosome.

## What is on record

| | |
|---|---|
| Official name | mitochondrial ribosomal protein L37 |
| Also known as | RPML2, MRP-L2, mL37 |
| Locus | 1p32.3 — gene with protein product |
| Gene families | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |

UniProt [Q9BZE1](https://www.uniprot.org/uniprotkb/Q9BZE1) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [51253](https://www.ncbi.nlm.nih.gov/gene/51253):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins comprising the mitoribosome differ greatly in sequence, and sometimes in biochemical properties, which prevents easy recognition by sequence homology. This gene encodes a 39S subunit protein. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:14034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14034) · Entrez [51253](https://www.ncbi.nlm.nih.gov/gene/51253) · UniProt [Q9BZE1](https://www.uniprot.org/uniprotkb/Q9BZE1) · Ensembl [ENSG00000116221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116221) · OMIM [611843](https://www.omim.org/entry/611843)

**PubMed**, as HGNC records for this gene — [10600119](https://pubmed.ncbi.nlm.nih.gov/10600119/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 30.13 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.926× |
| Wild-type minus altered | 0.964× |
| Compounds moving it up in WT lines | 25 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00758 |
| As a percentage | -0.52% |
| FDR, exposure-shuffle null | 0.0009 |
| In TP53-wild-type lines / altered lines | -0.00552 / -0.00884 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.233 raw, -0.139 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[The p21-DREAM axis]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, repression arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
