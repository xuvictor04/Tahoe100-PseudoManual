---
symbol: SMC1A
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [SMC1, SMC1L1]
gene_name: structural maintenance of chromosomes 1A
locus: Xp11.22
locus_type: gene with protein product
gene_family: [Structural maintenance of chromosomes proteins, Cohesin complex, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 126.07
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# SMC1A

*structural maintenance of chromosomes 1A* — Xp11.22

> [!summary] In one line
> SMC1A is an ATPase subunit of the cohesin ring that holds sister chromatids together, and is also a direct ATM substrate in the DNA-damage response.

## What it is

SMC1A heterodimerises with SMC3 through long coiled-coil arms joined at a hinge; RAD21 and a STAG subunit close the ring entrapping sister chromatids from replication until anaphase, and the same complex organises chromatin loops with CTCF. Beyond cohesion, SMC1A is phosphorylated by [[ATM]] on two C-terminal serines after ionising radiation, a step required for the S-phase checkpoint: cohesin is part of the damage response, not only the scaffold. The gene is X-linked: missense variants give a Cornelia de Lange phenotype, truncating variants a distinct epileptic encephalopathy. Cohesin subunits are recurrently mutated in myeloid malignancy and bladder cancer.

## Why it appears in this work

SMC1A was selected into the repressed arm of [[p53 program P]]: it falls where p53 output rises. Its value is as a reminder that a data-derived p53 programme contains genes p53 switches off, not only genes it induces. See [[Signing genes by p53 direction]].

## What is uncertain

SMC1A is not a canonical direct p53 target. No p53 repressive element at this gene is established, and indirect repression through [[The p21-DREAM axis]] explains cohesin and mitotic genes at least as well, the route that also moves [[SGO1]] and [[KIF11]]. Being essential and well expressed in every line, its dynamic range is narrow: a small coordinated fall is what cell-cycle exit alone produces. The direct-versus-indirect question is open.

## References

- Kim et al., 2002, Genes & Development — ATM-dependent and ATM-independent phosphorylation of SMC1 in response to DNA damage.
- Musio et al., 2006, Nature Genetics — SMC1A mutations cause X-linked Cornelia de Lange syndrome.
- Nasmyth & Haering, 2009, Annual Review of Genetics — review of cohesin ring architecture and its roles.

## What is on record

| | |
|---|---|
| Official name | structural maintenance of chromosomes 1A |
| Also known as | DXS423E, KIAA0178, SB1.8, Smcb |
| Locus | Xp11.22 — gene with protein product |
| Gene families | Structural maintenance of chromosomes proteins; Cohesin complex; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]] |
| Previously named | SMC1 (structural maintenance of chromosomes 1, yeast)-like 1; SMC1 structural maintenance of chromosomes 1-like 1 (yeast) |

**Function**, from UniProt [Q14683](https://www.uniprot.org/uniprotkb/Q14683) (reviewed):

> Involved in chromosome cohesion during cell cycle and in DNA repair. Central component of cohesin complex. The cohesin complex is required for the cohesion of sister chromatids after DNA replication. The cohesin complex apparently forms a large proteinaceous ring within which sister chromatids can be trapped. At anaphase, the complex is cleaved and dissociates from chromatin, allowing sister chromatids to segregate. The cohesin complex may also play a role in spindle pole assembly during mitosis. Involved in DNA repair via its interaction with BRCA1 and its related phosphorylation by ATM, or via its phosphorylation by ATR. Works as a downstream effector both in the ATM/NBS1 branch and in the ATR/MSH2 branch of S-phase checkpoint

**Summary**, from NCBI Gene [8243](https://www.ncbi.nlm.nih.gov/gene/8243):

> Proper cohesion of sister chromatids is a prerequisite for the correct segregation of chromosomes during cell division. The cohesin multiprotein complex is required for sister chromatid cohesion. This complex is composed partly of two structural maintenance of chromosomes (SMC) proteins, SMC3 and either SMC1B or the protein encoded by this gene. Most of the cohesin complexes dissociate from the chromosomes before mitosis, although those complexes at the kinetochore remain. Therefore, the encoded protein is thought to be an important part of functional kinetochores. In addition, this protein interacts with BRCA1 and is phosphorylated by ATM, indicating a potential role for this protein in DNA repair. This gene, which belongs to the SMC gene family, is located in an area of the X-chromosome that escapes X inactivation. Mutations in this gene result in Cornelia de Lange syndrome. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11111) · Entrez [8243](https://www.ncbi.nlm.nih.gov/gene/8243) · UniProt [Q14683](https://www.uniprot.org/uniprotkb/Q14683) · Ensembl [ENSG00000072501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072501) · OMIM [300040](https://www.omim.org/entry/300040)

**PubMed**, as HGNC records for this gene — [7757074](https://pubmed.ncbi.nlm.nih.gov/7757074/), [17273969](https://pubmed.ncbi.nlm.nih.gov/17273969/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 126.07 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.957× |
| Wild-type minus altered | 0.971× |
| Compounds moving it up in WT lines | 30 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00535 |
| As a percentage | +0.37% |
| FDR, exposure-shuffle null | 0.0064 |
| In TP53-wild-type lines / altered lines | 0.00547 / 0.00529 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.352 raw, 0.097 with 3 PCs removed |

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
