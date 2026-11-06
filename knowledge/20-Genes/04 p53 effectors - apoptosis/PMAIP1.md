---
symbol: PMAIP1
type: gene
tier: 1
pathway_role: p53 effector: apoptosis
aliases: [NOXA]
gene_name: phorbol-12-myristate-13-acetate-induced protein 1
locus: 18q21.32
locus_type: gene with protein product
gene_family: [BCL2 homology region 3 (BH3) only]
family_siblings_here: [BBC3]
p53_direction: induced by p53
curated_effector: true
effector_role: apoptosis
mg53_verdict: positive
mg53_effect_on_p53_output: toward MORE p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced]
generated_by: knowledge/_build/build_vault.py
---

# PMAIP1

*phorbol-12-myristate-13-acetate-induced protein 1* — 18q21.32

> [!summary] In one line
> PMAIP1 encodes NOXA, the BH3-only protein p53 induces to neutralise MCL1 and so lower the threshold for mitochondrial apoptosis.

## What it is

NOXA is a very small BH3-only protein — a BH3 motif and a C-terminal mitochondrial-targeting segment, little else. In the BCL2 family's division of labour it is a *sensitiser*: it does not itself permeabilise the outer mitochondrial membrane, but occupies prosurvival relatives so that the direct activators can. Its defining property is selectivity. Unlike PUMA ([[BBC3]]), which engages the whole prosurvival set, NOXA binds MCL1 and A1/BFL1 and essentially ignores BCL2 and BCL-XL. Binding MCL1 also accelerates MCL1's proteasomal degradation, so NOXA removes its target rather than merely sequestering it. With MCL1 depleted, BAK and [[BAX]] are free to oligomerise, the membrane permeabilises, and the apoptosome commits the cell.

PMAIP1 is a direct p53 target with a p53 response element; mouse work combining Noxa and Puma loss showed the two together account for much of p53-dependent apoptosis, with PUMA generally the more consequential. But NOXA is not a p53-exclusive gene, and that matters more for NOXA than for most p53 targets. It is strongly induced by proteasome inhibition, by ER stress through the ATF4 ([[ATF4]]) arm of the integrated stress response, by E2F1 and deregulated MYC, and under hypoxia. The protein is short-lived and proteasome-degraded, so steady-state NOXA reflects turnover as much as transcription. Clinically the NOXA-to-MCL1 balance helps determine whether a cell depends on BCL2 or on MCL1 for survival — MCL1 dependence is a principal route to venetoclax resistance, and bortezomib's cytotoxicity runs substantially through NOXA induction.

## Why it appears in this work

NOXA is where p53's output stops being reversible. Most members of the induction arm of [[p53 program P]] report engagement — arrest, repair, signalling — but NOXA, with PUMA, [[BAX]] and [[TNFRSF10B]], reports commitment to death. For a reader trying to tell whether p53 activity in a line is cytostatic or cytotoxic, the apoptotic members are the relevant subset, and NOXA is the most lineage-agnostic of them. Because it is an induced gene, its slope against anything must be converted into p53-output units before it can be compared with a repressed gene's — see [[Signing genes by p53 direction]].

## What is uncertain

The largest problem is structural rather than biological. A transcriptome measured at 24 h in cells still present is a survivorship-filtered sample: cells that acted on a NOXA induction are gone, so what is measured is NOXA in the survivors, and its relation to the apoptotic response actually mounted is not simple. Second, NOXA's p53-independent inducers are strong and this screen contains compounds that hit several of them — proteasome inhibitors, CDK and transcription inhibitors, ER stressors — so NOXA induction under drug exposure is weak evidence of p53 engagement on its own. Third, this is a case where mRNA is a poor proxy for function: what decides outcome is NOXA protein against MCL1 protein at the mitochondrion, and both are short-lived. Fourth, the mouse genetics do not transfer cleanly — the relative weight of Noxa and Puma differs by cell type.

## References

- Oda et al., 2000, Science — identified Noxa as a BH3-only p53 target and candidate mediator of p53-induced apoptosis.
- Villunger et al., 2003, Science — Puma and Noxa together mediate much of the p53- and drug-induced apoptotic response in mouse cells.
- Chen et al., 2005, Molecular Cell — Noxa selectively targets Mcl-1 while Puma engages all prosurvival relatives, giving the BH3-only proteins complementary function.

## What is on record

| | |
|---|---|
| Official name | phorbol-12-myristate-13-acetate-induced protein 1 |
| Also known as | APR, NOXA |
| Locus | 18q21.32 — gene with protein product |
| Gene families | BCL2 homology region 3 (BH3) only |
| Other genes here in those families | [[BBC3]] |

**Function**, from UniProt [Q13794](https://www.uniprot.org/uniprotkb/Q13794) (reviewed):

> Promotes activation of caspases and apoptosis. Promotes mitochondrial membrane changes and efflux of apoptogenic proteins from the mitochondria. Contributes to p53/TP53-dependent apoptosis after radiation exposure. Promotes proteasomal degradation of MCL1. Competes with BAK1 for binding to MCL1 and can displace BAK1 from its binding site on MCL1 (By similarity). Competes with BIM/BCL2L11 for binding to MCL1 and can displace BIM/BCL2L11 from its binding site on MCL1

**Summary**, from NCBI Gene [5366](https://www.ncbi.nlm.nih.gov/gene/5366):

> This gene belongs to a pro-apoptotic subfamily within the BCL-2 protein family, referred to as the BCL-2 homology domain 3 (BH3)-only subfamily, which determine whether a cell commits to apoptosis. In response to death-inducing stimuli, BH3-only members inhibit the anti-apoptotic BCL-2 family members, which under steady-state conditions keep the multi-BH domain proteins BAX and BAK, in an inactive state. [provided by RefSeq, Aug 2020]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9108) · Entrez [5366](https://www.ncbi.nlm.nih.gov/gene/5366) · UniProt [Q13794](https://www.uniprot.org/uniprotkb/Q13794) · Ensembl [ENSG00000141682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141682) · OMIM [604959](https://www.omim.org/entry/604959)

**PubMed**, as HGNC records for this gene — [2398525](https://pubmed.ncbi.nlm.nih.gov/2398525/), [12879012](https://pubmed.ncbi.nlm.nih.gov/12879012/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00813 |
| As a percentage | +0.57% |
| FDR, exposure-shuffle null | 0.0313 |
| In TP53-wild-type lines / altered lines | 0.00963 / 0.00713 |
| Verdict | positive |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.599 raw, 0.316 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
