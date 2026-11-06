---
symbol: CENPN
type: gene
tier: 2
pathway_role: p53 program, repression arm
aliases: [CENP-N]
gene_name: centromere protein N
locus: 16q23.2
locus_type: gene with protein product
gene_family: [Constitutive centromere associated network]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 31.5
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# CENPN

*centromere protein N* — 16q23.2

> [!summary] In one line
> CENPN encodes CENP-N, the subunit of the constitutive centromere-associated network that reads the CENP-A nucleosome directly and so marks where a kinetochore is built.

## What it is

CENP-N was found in the complex that co-purifies with CENP-A chromatin, and is the component that recognises it specifically, contacting the CENP-A nucleosome through the histone's exposed RG loop. Structural work has since resolved that interface and shown how CENP-N bridges to CENP-L and sits alongside CENP-C in the inner kinetochore. Depleting it impairs kinetochore assembly and new CENP-A deposition, so cells lose chromosome segregation fidelity. Expression is proliferation-coupled rather than tissue-specific. Outside that structural role its literature is mostly correlative: raised expression in various tumours with survival associations, a weak basis for functional claims.

## Why it appears in this work

CENPN was selected into the repression arm of [[p53 program P]], declining modestly and selectively in TP53-wild-type lines under p53-activating compounds. For a mitosis gene of this kind the expected route is indirect, through p21 and the DREAM complex rather than p53 at the promoter; see [[The p21-DREAM axis]]. Its membership mainly reinforces reading that arm as a proliferation-arrest signature rather than a dedicated repression programme.

## What is uncertain

Nothing establishes CENPN as a p53 target in any direct sense, and its program membership here is only partially stable across folds, so it should be held more loosely than the core members of the arm. CENP-N's biology is executed at the protein level, so a fall in its transcript reports cells leaving the cycle, not a change in centromere function.

## References

- Foltz et al., 2006, Nature Cell Biology — defined the human CENP-A nucleosome-associated complex, including CENP-N.
- Carroll et al., 2009, Nature Cell Biology — showed CENP-N binds CENP-A nucleosomes directly and is required for centromere assembly.
- Chittori et al., 2018, Science — structural basis of centromeric nucleosome recognition by CENP-N.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle and mitosis genes.

## What is on record

| | |
|---|---|
| Official name | centromere protein N |
| Also known as | FLJ13607, FLJ22660, BM039 |
| Locus | 16q23.2 — gene with protein product |
| Gene families | Constitutive centromere associated network |
| Previously named | chromosome 16 open reading frame 60 |

**Function**, from UniProt [Q96H22](https://www.uniprot.org/uniprotkb/Q96H22) (reviewed):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres. CENPN is the first protein to bind specifically to CENPA nucleosomes and the direct binding of CENPA nucleosomes by CENPN is required for centromere assembly. Required for chromosome congression and efficiently align the chromosomes on a metaphase plate

**Summary**, from NCBI Gene [55839](https://www.ncbi.nlm.nih.gov/gene/55839):

> The protein encoded by this gene forms part of the nucleosome-associated complex and is important for kinetochore assembly. It is bound to kinetochores during S phase and G2 and recruits other proteins to the centromere. Pseudogenes of this gene are located on chromosome 2. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Jul 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30873) · Entrez [55839](https://www.ncbi.nlm.nih.gov/gene/55839) · UniProt [Q96H22](https://www.uniprot.org/uniprotkb/Q96H22) · Ensembl [ENSG00000166451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166451) · OMIM [611509](https://www.omim.org/entry/611509)

**PubMed**, as HGNC records for this gene — [16622419](https://pubmed.ncbi.nlm.nih.gov/16622419/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 31.50 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.946× |
| Wild-type minus altered | 0.943× |
| Compounds moving it up in WT lines | 28 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00349 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.3130 |
| In TP53-wild-type lines / altered lines | 0.00345 / 0.00351 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.339 raw, 0.108 with 3 PCs removed |

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
