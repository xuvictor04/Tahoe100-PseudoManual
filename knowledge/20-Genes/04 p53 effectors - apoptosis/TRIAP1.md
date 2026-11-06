---
symbol: TRIAP1
type: gene
tier: 1
pathway_role: p53 effector: apoptosis
aliases: [p53CSV]
gene_name: TP53 regulated inhibitor of apoptosis 1
locus: 12q24.31
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis (anti-)
median_line_cpm: 9.54
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TRIAP1

*TP53 regulated inhibitor of apoptosis 1* — 12q24.31

> [!summary] In one line
> TRIAP1 is a small p53-induced protein that works inside mitochondria as half of a lipid-transfer complex, and its effect on the cell is to keep it alive — a survival output of p53, not a death one.

## What it is

TRIAP1 — TP53-regulated inhibitor of apoptosis 1, originally named p53CSV for "p53-inducible cell-survival factor" — is a 76-residue protein of the Mdm35 family. It was found as a p53-induced gene whose knockdown increased apoptosis and whose overexpression protected cells against DNA-damage-induced death, with the induction reported to be selective for *mild* genotoxic stress rather than severe damage. That conditionality places it in the arm of the p53 response that attempts survival rather than the arm that commits to death.

Its best-defined job came later and is structural. In the mitochondrial intermembrane space TRIAP1 heterodimerises with PRELID1 and with PRELID3B (SLMO2); these complexes bind and shuttle phosphatidic acid across the intermembrane space, delivering the precursor for cardiolipin synthesis at the inner membrane. Losing TRIAP1 or its PRELI partner lowers cardiolipin, which loosens cytochrome *c* from the inner membrane and leaves cells primed for apoptosis. The anti-apoptotic phenotype therefore has a lipid-level explanation that does not require TRIAP1 to touch the apoptotic machinery at all. An earlier proposal has it binding HSP70 and, through that, dampening APAF1-dependent apoptosome formation; that has much thinner support.

## Why it appears in this work

TRIAP1 is a curated p53 effector in the induction arm of [[p53 program P]], and it corrects a habit of reading that programme as a single quantity called "p53 output". The arm contains [[BAX]], [[BBC3]] and [[PMAIP1]], which push toward death, and it contains TRIAP1, which pushes the other way. A rise in the programme score means p53 is transcriptionally engaged, not that the cells are dying; the pro- and anti-apoptotic members move together because they share an upstream driver, not because their consequences agree. In the per-gene tables of [[Downstream of MG53]], the sign of a gene's slope and the sign of its effect on cell fate are different questions. See [[Signing genes by p53 direction]].

## What is uncertain

Whether TRIAP1 is a *direct* p53 target is likely but not settled: a response element has been reported within the gene rather than in an upstream promoter, and sources disagree over whether it sits in the second intron or the second exon — not a discrepancy to resolve by guessing. The two accounts of its anti-apoptotic action have not been reconciled, and the HSP70/APAF1 one rests on essentially a single study. The "mild damage only" induction pattern comes from the founding work and has not, as far as I can establish, been systematically retested across stress types. And most of the functional work is overexpression and knockdown in cultured cells; what TRIAP1 loss does in a whole animal is much less clear than its biochemistry.

## References

- Park & Nakamura, 2005, *Cancer Research* — identified p53CSV/TRIAP1 as a p53-inducible gene required for survival after low-level genotoxic stress, and proposed the HSP70/APAF1 route.
- Potting et al., 2013, *Cell Metabolism* — showed TRIAP1/PRELI complexes transport phosphatidic acid within mitochondria, and that losing them depletes cardiolipin and sensitises cells to apoptosis.

## What is on record

| | |
|---|---|
| Official name | TP53 regulated inhibitor of apoptosis 1 |
| Also known as | P53CSV, WF-1, HSPC132, p53CSV, MDM35, p53-inducible cell-survival factor, mitochondrial distribution and morphology 35 homolog (S. cerevisiae) |
| Locus | 12q24.31 — gene with protein product |

**Function**, from UniProt [O43715](https://www.uniprot.org/uniprotkb/O43715) (reviewed):

> Involved in the modulation of the mitochondrial apoptotic pathway by ensuring the accumulation of cardiolipin (CL) in mitochondrial membranes. In vitro, the TRIAP1:PRELID1 complex mediates the transfer of phosphatidic acid (PA) between liposomes and probably functions as a PA transporter across the mitochondrion intermembrane space to provide PA for CL synthesis in the inner membrane (PubMed:23931759). Likewise, the TRIAP1:PRELID3A complex mediates the transfer of phosphatidic acid (PA) between liposomes (in vitro) and probably functions as a PA transporter across the mitochondrion intermembrane space (in vivo) (PubMed:26071602). Mediates cell survival by inhibiting activation of caspase-9 which prevents induction of apoptosis (PubMed:15735003)

**Summary**, from NCBI Gene [51499](https://www.ncbi.nlm.nih.gov/gene/51499):

> Enables p53 binding activity. Contributes to phosphatidic acid transfer activity. Involved in several processes, including DNA damage response, signal transduction by p53 class mediator; negative regulation of apoptotic signaling pathway; and positive regulation of phospholipid transport. Located in mitochondrial intermembrane space. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:26937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26937) · Entrez [51499](https://www.ncbi.nlm.nih.gov/gene/51499) · UniProt [O43715](https://www.uniprot.org/uniprotkb/O43715) · Ensembl [ENSG00000170855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170855) · OMIM [614943](https://www.omim.org/entry/614943)

**PubMed**, as HGNC records for this gene — [11042152](https://pubmed.ncbi.nlm.nih.gov/11042152/), [15735003](https://pubmed.ncbi.nlm.nih.gov/15735003/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 9.54 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 6 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.078× |
| Wild-type minus altered | 1.103× |
| Compounds moving it up in WT lines | 60 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00379 |
| As a percentage | -0.26% |
| FDR, exposure-shuffle null | 0.2894 |
| In TP53-wild-type lines / altered lines | -0.00502 / -0.00303 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.231 raw, -0.218 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
