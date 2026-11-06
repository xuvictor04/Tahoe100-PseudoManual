---
symbol: PRKCG
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [PKCC, MGC57564, PKCγ]
gene_name: protein kinase C gamma
locus: 19q13.42
locus_type: gene with protein product
gene_family: [C2 domain containing protein kinases, Protein kinase C family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PRKCG

*protein kinase C gamma* — 19q13.42

> [!summary] In one line
> PRKCG encodes PKCγ, a calcium- and diacylglycerol-dependent protein kinase C isoform expressed almost exclusively in neurons and most abundant in cerebellar Purkinje cells.

## What it is

A conventional PKC: tandem C1 domains that bind diacylglycerol, a C2 domain that binds calcium, and a kinase domain held off by a pseudosubstrate clamp until both second messengers arrive. Activation downstream of Gq–PLCβ signalling, including mGluR1 in Purkinje cells, drives membrane translocation. Unlike the other conventional isoforms its expression is confined to the central nervous system, so most of what is known comes from cerebellar physiology: long-term depression and developmental synapse elimination. Clinically, dominant missense mutations, concentrated in the regulatory C1 domains but also found in the catalytic half, cause spinocerebellar ataxia type 14, a slowly progressive and largely pure cerebellar ataxia.

## Why it appears in this work

PRKCG surfaces twice: among genes whose expression tracks measured [[MG53 (TRIM72)]] across the panel, and carrying a p53-activated label inherited from a curated regulon rather than earned in this study's data. It is a neuronal gene in a panel of non-neuronal lines, so it sits near the expression floor throughout.

## What is uncertain

Whether PRKCG is a p53 target at all. The label is curation; I know of no primary work showing p53 occupancy at this gene or clean induction by p53, and the data-defined [[p53 program P]] does not contain it. The mechanism of SCA14 is also unsettled — increased, unchanged and mislocalisation-driven phenotypes have all been reported for different mutants. And PRKCG carries this study's readthrough-geometry flag — it sits within 20 kb 3′ of a much higher-expressed same-strand gene, so some reads credited to it may not be its own ([[Readthrough spillover]], the same failure mode as [[Why MG53 is hard to measure here]]).

## References

- Chen et al., 2003, American Journal of Human Genetics — missense mutations in the PKCγ regulatory domain cause dominant non-episodic cerebellar ataxia (SCA14).
- Abeliovich et al., 1993, Cell — hippocampal long-term potentiation is modified in PKCγ-mutant mice.

## What is on record

| | |
|---|---|
| Official name | protein kinase C gamma |
| Also known as | PKCC, MGC57564, PKCγ, PKC-gamma |
| Locus | 19q13.42 — gene with protein product |
| Gene families | C2 domain containing protein kinases; Protein kinase C family |
| Previously named | protein kinase C, gamma |

**Function**, from UniProt [P05129](https://www.uniprot.org/uniprotkb/P05129) (reviewed):

> Calcium-activated, phospholipid- and diacylglycerol (DAG)-dependent serine/threonine-protein kinase that plays diverse roles in neuronal cells and eye tissues, such as regulation of the neuronal receptors GRIA4/GLUR4 and GRIN1/NMDAR1, modulation of receptors and neuronal functions related to sensitivity to opiates, pain and alcohol, mediation of synaptic function and cell survival after ischemia, and inhibition of gap junction activity after oxidative stress. Binds and phosphorylates GRIA4/GLUR4 glutamate receptor and regulates its function by increasing plasma membrane-associated GRIA4 expression. In primary cerebellar neurons treated with the agonist 3,5-dihyidroxyphenylglycine, functions downstream of the metabotropic glutamate receptor GRM5/MGLUR5 and phosphorylates GRIN1/NMDAR1 receptor which plays a key role in synaptic plasticity, synaptogenesis, excitotoxicity, memory acquisition and learning. May be involved in the regulation of hippocampal long-term potentiation (LTP), but may be not necessary for the process of synaptic plasticity. May be involved in desensitization of mu-type opioid receptor-mediated G protein activation in the spinal cord, and may be critical for the development and/or maintenance of morphine-induced reinforcing effects in the limbic forebrain. May modulate the functionality of mu-type-opioid receptors by participating in a signaling pathway which leads to the phosphorylation and degradation of opioid receptors. May also contributes to chronic morphine-induced changes in nociceptive processing. Plays a role in neuropathic pain mechanisms and contributes to the maintenance of the allodynia pain produced by peripheral inflammation. Plays an important role in initial sensitivity and tolerance to ethanol, by mediating the behavioral effects of ethanol as well as the effects of this drug on the GABA(A) receptors. During and after cerebral ischemia modulate neurotransmission and cell survival in synaptic membranes, and is involved in insulin-induced inhibition of necrosis, an important mechanism for minimizing ischemic injury. Required for the elimination of multiple climbing fibers during innervation of Purkinje cells in developing cerebellum. Is activated in lens epithelial cells upon hydrogen peroxide treatment, and phosphorylates connexin-43 (GJA1/CX43), resulting in disassembly of GJA1 gap junction plaques and inhibition of gap junction activity which could provide a protective effect against oxidative stress (By similarity). Phosphorylates p53/TP53 and promotes p53/TP53-dependent apoptosis in response to DNA damage. Involved in the phase resetting of the cerebral cortex circadian clock during temporally restricted feeding. Stabilizes the core clock component BMAL1 by interfering with its ubiquitination, thus suppressing its degradation, resulting in phase resetting of the cerebral cortex clock (By similarity). Phosphorylates and activates LRRK1, which phosphorylates RAB proteins involved in intracellular trafficking (PubMed:36040231). Acts as a regulator of dopamine signaling by mediating constitutive phosphorylation of dopamine receptor DRD1, inhibiting G protein-coupled receptor signaling (PubMed:20969574)

**Summary**, from NCBI Gene [5582](https://www.ncbi.nlm.nih.gov/gene/5582):

> Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC also serve as major receptors for phorbol esters, a class of tumor promoters. Each member of the PKC family has a specific expression profile and is believed to play distinct roles in cells. The protein encoded by this gene is one of the PKC family members. This protein kinase is expressed solely in the brain and spinal cord and its localization is restricted to neurons. It has been demonstrated that several neuronal functions, including long term potentiation (LTP) and long term depression (LTD), specifically require this kinase. Knockout studies in mice also suggest that this kinase may be involved in neuropathic pain development. Defects in this protein have been associated with neurodegenerative disorder spinocerebellar ataxia-14 (SCA14). Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9402) · Entrez [5582](https://www.ncbi.nlm.nih.gov/gene/5582) · UniProt [P05129](https://www.uniprot.org/uniprotkb/P05129) · Ensembl [ENSG00000126583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126583) · OMIM [176980](https://www.omim.org/entry/176980)

**PubMed**, as HGNC records for this gene — [8432525](https://pubmed.ncbi.nlm.nih.gov/8432525/), [3755548](https://pubmed.ncbi.nlm.nih.gov/3755548/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08796 |
| As a percentage | +6.29% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07779 / 0.09373 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.614 raw, 0.549 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
