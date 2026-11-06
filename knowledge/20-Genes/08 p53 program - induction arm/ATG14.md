---
symbol: ATG14
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [ATG14L]
gene_name: autophagy related 14
locus: 14q22.3
locus_type: gene with protein product
gene_family: [Autophagy related, PIK3C3 complex subunits]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 68.04
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ATG14

*autophagy related 14* — 14q22.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ATG14.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | autophagy related 14 |
| Also known as | ATG14L, Barkor, beclin 1-associated autophagy-related key regulator |
| Locus | 14q22.3 — gene with protein product |
| Gene families | Autophagy related; PIK3C3 complex subunits |
| Previously named | KIAA0831; ATG14 autophagy related 14 homolog (S. cerevisiae) |

**Function**, from UniProt [Q6ZNE5](https://www.uniprot.org/uniprotkb/Q6ZNE5) (reviewed):

> Required for both basal and inducible autophagy. Determines the localization of the autophagy-specific PI3-kinase complex PI3KC3-C1 (PubMed:18843052, PubMed:19050071). Plays a role in autophagosome formation and MAP1LC3/LC3 conjugation to phosphatidylethanolamine (PubMed:19270696, PubMed:20713597). Promotes BECN1 translocation from the trans-Golgi network to autophagosomes (PubMed:20713597). Enhances PIK3C3 activity in a BECN1-dependent manner. Essential for the autophagy-dependent phosphorylation of BECN1 (PubMed:23878393). Stimulates the phosphorylation of BECN1, but suppresses the phosphorylation PIK3C3 by AMPK (PubMed:23878393). Binds to STX17-SNAP29 binary t-SNARE complex on autophagosomes and primes it for VAMP8 interaction to promote autophagosome-endolysosome fusion (PubMed:25686604, PubMed:37632749). Modulates the hepatic lipid metabolism (By similarity)

**Summary**, from NCBI Gene [22863](https://www.ncbi.nlm.nih.gov/gene/22863):

> Enables GTPase binding activity; phosphatidylinositol 3-kinase inhibitor activity; and protein-membrane adaptor activity. Involved in several processes, including early endosome to late endosome transport; macroautophagy; and phosphatidylinositol 3-kinase/protein kinase B signal transduction. Acts upstream of or within endosome to lysosome transport. Located in autophagosome and phagophore assembly site membrane. Is extrinsic component of omegasome membrane and extrinsic component of phagophore assembly site membrane. Is active in phagophore assembly site. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19962) · Entrez [22863](https://www.ncbi.nlm.nih.gov/gene/22863) · UniProt [Q6ZNE5](https://www.uniprot.org/uniprotkb/Q6ZNE5) · Ensembl [ENSG00000126775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126775) · OMIM [613515](https://www.omim.org/entry/613515)

**PubMed**, as HGNC records for this gene — [18843052](https://pubmed.ncbi.nlm.nih.gov/18843052/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 68.04 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 79 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.047× |
| Wild-type minus altered | 1.017× |
| Compounds moving it up in WT lines | 67 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00599 |
| As a percentage | -0.41% |
| FDR, exposure-shuffle null | 0.0367 |
| In TP53-wild-type lines / altered lines | -0.00840 / -0.00453 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.071 raw, -0.202 with 3 PCs removed |

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
