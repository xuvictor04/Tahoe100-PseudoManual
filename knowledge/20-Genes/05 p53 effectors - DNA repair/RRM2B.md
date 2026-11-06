---
symbol: RRM2B
type: gene
tier: 1
pathway_role: p53 effector: DNA repair
aliases: [p53R2]
gene_name: ribonucleotide reductase regulatory TP53 inducible subunit M2B
locus: 8q22.3
locus_type: gene with protein product
gene_family: [Ribonucleotide reductase subunits]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: DNA repair
median_line_cpm: 47.57
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RRM2B

*ribonucleotide reductase regulatory TP53 inducible subunit M2B* — 8q22.3

> [!summary] In one line
> RRM2B encodes p53R2, the p53-inducible small subunit of ribonucleotide reductase, which supplies deoxyribonucleotides for DNA repair and for mitochondrial DNA synthesis in cells that are not in S phase.

## What it is

Ribonucleotide reductase makes the deoxyribonucleotides that DNA synthesis consumes, and it is the committed step: no dNTPs, no replication and no repair. The enzyme pairs a large catalytic subunit, RRM1, with a small subunit supplying the tyrosyl radical. Mammals have two alternative small subunits, and the difference between them is the whole point of this gene. RRM2 is the S-phase subunit: cell-cycle regulated, abundant in dividing cells, destroyed on exit from mitosis. RRM2B — p53R2 — is the damage-inducible, quiescence-competent one, transcribed from a p53-responsive promoter at 8q22.3.

It was identified as a p53 target supplying dNTPs for repair, and reported shortly afterwards as responsive to p73 as well. The consequence is that a non-dividing cell retains a route to dNTPs: RRM1 pairs with p53R2 instead of RRM2, and the pathway is switched on by damage rather than by the cell cycle.

The genetics have shifted where the emphasis sits. *Rrm2b*-null mice die early with severe renal failure and depleted dNTP pools. In humans, biallelic loss of function causes an mtDNA depletion syndrome — severe infantile encephalomyopathy with tubulopathy — and heterozygous truncating variants cause autosomal-dominant progressive external ophthalmoplegia with multiple mtDNA deletions. The unifying explanation is that mitochondrial DNA replicates on its own schedule, so it depends on the dNTP supply route that does not require S phase. RRM2B is therefore, in practice, a mitochondrial maintenance gene as much as a damage-response gene.

## Why it appears in this work

RRM2B is a direct, reliably induced member of [[p53 program P]] in the repair and metabolic arm, which makes its induction a trustworthy report that p53 is engaged rather than that cells are generically stressed. It is also among the clearest demonstrations that p53's output is not only arrest and apoptosis: the gene p53 turns on here is a biosynthetic enzyme, provisioning the raw material repair will need. For a reader tracking what [[The p53 pathway]] actually does downstream, RRM2B is the provisioning arm, sitting alongside the arrest arm of [[The p21-DREAM axis]] and the apoptotic effectors.

## What is uncertain

What p53R2 is *for* physiologically is not settled. The original framing — a p53-controlled dNTP supply dedicated to repairing damaged nuclear DNA — sits uneasily with the human and mouse genetics, which read much more like a constitutive housekeeping requirement for mitochondrial and post-mitotic dNTP pools. Both can be true, but the relative weight is genuinely open, and the field's centre of gravity has moved toward the mitochondrial role. Whether p53R2 acts inside mitochondria or supplies a cytosolic pool they import was contested; the balance of evidence favours cytosolic reduction with transport of the product, so "mitochondrial ribonucleotide reductase" is misleading shorthand. Whether RRM2B is net tumour-suppressive is also unresolved: supplying dNTPs supports repair in cancer cells too, and reported associations between RRM2B level and outcome run in both directions depending on tumour type and treatment. Finally, the disease variants are loss-of-function; nothing about them says what a modest change in RRM2B transcript level does to dNTP pools, which are buffered and allosterically controlled.

## References

- Tanaka et al., 2000, Nature — identified RRM2B/p53R2 as a ribonucleotide reductase subunit gene in a p53-dependent checkpoint response to DNA damage.
- Nakano et al., 2000, Oncogene — showed the gene is a transcriptional target of both p53 and p73.
- Kimura et al., 2003, Nature Genetics — *Rrm2b*-null mice develop severe renal failure with attenuated dNTP pools.
- Bourdon et al., 2007, Nature Genetics — RRM2B mutation causes severe mitochondrial DNA depletion in humans.
- Tyynismaa et al., 2009, American Journal of Human Genetics — a heterozygous truncating RRM2B mutation causes autosomal-dominant progressive external ophthalmoplegia with multiple mtDNA deletions.

## What is on record

| | |
|---|---|
| Official name | ribonucleotide reductase regulatory TP53 inducible subunit M2B |
| Also known as | p53R2 |
| Locus | 8q22.3 — gene with protein product |
| Gene families | Ribonucleotide reductase subunits |
| Previously named | ribonucleotide reductase M2 B (TP53 inducible) |

**Function**, from UniProt [Q7LG56](https://www.uniprot.org/uniprotkb/Q7LG56) (reviewed):

> Part of the ribonucleotide reductase (RNR) complex composed of a catalytic large alpha subunit (RRM1/RR1) and a small beta subunit (RRM2B/RR2B) required for DNA synthesis (PubMed:12615712, PubMed:16376858). The active form is an alpha2beta2 heterotetramer in which the RR1-containing subunits (alpha2) catalyze reduction of ribonucleotides to deoxyribonucleotides, while the RRM2B-containing subunits (beta2) provide the diferric-tyrosyl radical cofactor required for catalysis and radical transfer (PubMed:11517226, PubMed:12615712, PubMed:16376858, PubMed:19728742, Ref.18). Mechanistically, RRM2B-containing subunits (beta2) initiates a long-distance radical transfer (RT) to the RRM1 subunits (alpha2) by generating a transient active site thiyl radical in alpha2 that catalyzes ribonucleotides reduction and, reverse radical transfer from alpha2 to beta2 regenerates the tyrosyl-radical in beta2 on every turnover (By similarity). Supplies deoxyribonucleotides for DNA repair in cells arrested at G1 or G2 in a p53/TP53-dependent manner (PubMed:10716435, PubMed:11719458, PubMed:12615712)

**Summary**, from NCBI Gene [50484](https://www.ncbi.nlm.nih.gov/gene/50484):

> This gene encodes the small subunit of a p53-inducible ribonucleotide reductase. This heterotetrameric enzyme catalyzes the conversion of ribonucleoside diphosphates to deoxyribonucleoside diphosphates. The product of this reaction is necessary for DNA synthesis. Mutations in this gene have been associated with autosomal recessive mitochondrial DNA depletion syndrome, autosomal dominant progressive external ophthalmoplegia-5, and mitochondrial neurogastrointestinal encephalopathy. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17296) · Entrez [50484](https://www.ncbi.nlm.nih.gov/gene/50484) · UniProt [Q7LG56](https://www.uniprot.org/uniprotkb/Q7LG56) · Ensembl [ENSG00000048392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048392) · OMIM [604712](https://www.omim.org/entry/604712)

**PubMed**, as HGNC records for this gene — [10716435](https://pubmed.ncbi.nlm.nih.gov/10716435/), [10980602](https://pubmed.ncbi.nlm.nih.gov/10980602/), [17486094](https://pubmed.ncbi.nlm.nih.gov/17486094/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 47.57 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | **readthrough-exposed** — sits ≤ 20 kb 3′ of a much higher same-strand gene, so transcription running past that neighbour is counted as this gene ([[Readthrough spillover]]) |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 25 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.127× |
| Wild-type minus altered | 1.113× |
| Compounds moving it up in WT lines | 86 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00104 |
| As a percentage | +0.07% |
| FDR, exposure-shuffle null | 0.7719 |
| In TP53-wild-type lines / altered lines | -0.00040 / 0.00191 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.374 raw, 0.056 with 3 PCs removed |

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
