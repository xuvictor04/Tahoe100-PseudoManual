---
symbol: HJURP
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [FAKTS]
gene_name: Holliday junction recognition protein
locus: 2q37.1
locus_type: gene with protein product
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 51.18
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# HJURP

*Holliday junction recognition protein* — 2q37.1

> [!summary] In one line
> HJURP is the dedicated chaperone that holds newly made CENP-A and deposits it at centromeres, so it is the gene that decides where new centromeric chromatin is built.

## What it is

HJURP was picked up twice over — once as a protein binding a Holliday-junction-like structure, once as a transcript over-expressed in lung tumours, the source of the alias URLC9. Its real job emerged from CENP-A proteomics: HJURP binds the CENP-A/H4 dimer through a conserved N-terminal domain, keeps it soluble, and loads it into centromeric chromatin in a narrow window at mitotic exit and early G1. Without it, new CENP-A is not deposited, the existing pool is diluted by replication, and kinetochores fail — placing HJURP upstream of the CENP-A reader [[CENPN]] in one assembly pathway. Beyond that the literature is largely correlative: high HJURP associates with poor outcome in several tumour series, a weak basis for functional claims.

## Why it appears in this work

HJURP was selected into the repression arm of [[p53 program P]], falling selectively in TP53-wild-type lines under p53 activators. For a replication-coupled chromatin factor the expected route is indirect, through p21 and DREAM rather than p53 at the promoter; see [[The p21-DREAM axis]]. Its presence reinforces reading that arm as cells leaving the cycle.

## What is uncertain

Nothing establishes HJURP as a p53 target in any direct sense, and its program membership here is unstable across folds, so hold it more loosely than the arm's core members. There is also a timing problem: HJURP acts in a short window at mitotic exit, so a 24 h transcript measurement in an arresting population reports cell-cycle distribution rather than centromere assembly. The prognosis literature is expression-correlation, not evidence that HJURP drives those phenotypes.

## References

- Foltz et al., 2009, Cell — showed HJURP mediates centromere-specific assembly of CENP-A nucleosomes.
- Dunleavy et al., 2009, Cell — identified HJURP as a cell-cycle-dependent CENP-A deposition and maintenance factor.
- Shuaib et al., 2010, PNAS — mapped the conserved N-terminal domain through which HJURP binds CENP-A.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle genes.

## What is on record

| | |
|---|---|
| Official name | Holliday junction recognition protein |
| Also known as | DKFZp762E1312, URLC9, hFLEG1, FAKTS |
| Locus | 2q37.1 — gene with protein product |

**Function**, from UniProt [Q8NCD3](https://www.uniprot.org/uniprotkb/Q8NCD3) (reviewed):

> Centromeric protein that plays a central role in the incorporation and maintenance of histone H3-like variant CENPA at centromeres. Acts as a specific chaperone for CENPA and is required for the incorporation of newly synthesized CENPA molecules into nucleosomes at replicated centromeres. Prevents CENPA-H4 tetramerization and prevents premature DNA binding by the CENPA-H4 tetramer. Directly binds Holliday junctions

**Summary**, from NCBI Gene [55355](https://www.ncbi.nlm.nih.gov/gene/55355):

> Enables histone binding activity and identical protein binding activity. Involved in CENP-A containing chromatin assembly; chromosome segregation; and regulation of protein-containing complex assembly. Located in kinetochore and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25444) · Entrez [55355](https://www.ncbi.nlm.nih.gov/gene/55355) · UniProt [Q8NCD3](https://www.uniprot.org/uniprotkb/Q8NCD3) · Ensembl [ENSG00000123485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123485) · OMIM [612667](https://www.omim.org/entry/612667)

**PubMed**, as HGNC records for this gene — [17823411](https://pubmed.ncbi.nlm.nih.gov/17823411/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 51.18 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.872× |
| Wild-type minus altered | 0.927× |
| Compounds moving it up in WT lines | 26 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00325 |
| As a percentage | -0.22% |
| FDR, exposure-shuffle null | 0.4626 |
| In TP53-wild-type lines / altered lines | 0.00068 / -0.00546 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.004 raw, 0.174 with 3 PCs removed |

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
