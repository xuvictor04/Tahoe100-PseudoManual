---
symbol: USP7
type: gene
tier: 1
pathway_role: p53 itself and what controls it
gene_name: ubiquitin specific peptidase 7
locus: 16p13.2
locus_type: gene with protein product
gene_family: [Ubiquitin specific peptidases]
family_siblings_here: [USP1, USP15]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# USP7

*ubiquitin specific peptidase 7* — 16p13.2

> [!summary] In one line
> USP7 is the deubiquitinase that removes ubiquitin from both p53 and MDM2, which means its net effect on p53 depends on how much USP7 there is — the clearest case in the pathway of a regulator whose direction is not a fixed property.

## What it is

USP7, long known as HAUSP (herpesvirus-associated ubiquitin-specific protease), has an N-terminal TRAF-like domain, a catalytic USP domain, and C-terminal ubiquitin-like domains that fold back to activate it. The TRAF-like domain carries the substrate-binding pocket, which p53 and MDM2 bind through similar short motifs — as does EBNA1 of Epstein–Barr virus, which is how the enzyme got its name.

Its relationship to p53 is the textbook case of a non-monotonic regulator. USP7 deubiquitinates p53 and stabilises it, even against excess MDM2, which predicts that losing USP7 should destabilise p53. Disrupting the gene in human cells did the opposite: p53 was stabilised and functionally activated. The resolution is that MDM2 is also a USP7 substrate and the more sensitive one — it needs deubiquitination to survive long enough to act as a ligase — so partial loss of USP7 lowers p53 while near-complete loss removes MDM2 first and raises it. Both behaviours have been reported in the same system at different knockdown depths.

Beyond p53 the substrate list is long — MDMX/[[MDM4]], PTEN, Claspin, FOXO4, Tip60, UHRF1 — and germline variants cause Hao-Fountain syndrome. Selective inhibitors reported in 2017 act through the MDM2 arm: they destabilise MDM2, raise p53 and induce targets including [[CDKN1A]].

## Why it appears in this work

USP7 is here as an upstream regulator of p53 stability, not a p53 target: it has no programme arm and no induction to report. Its value is as the cleanest illustration of what this study's design cannot see. USP7 is a decisive controller of p53 output, and almost none of that control appears in mRNA — it operates on protein half-life, through a pocket shared between two substrates, with a direction that depends on its own abundance. That is the same category of mechanism as [[MG53 (TRIM72)]]'s known biology, which is also E3-ligase activity on protein substrates. The asymmetry stated in [[What this study found]] — that absence of an mRNA-level association does not rule out a protein-level link — is therefore not special pleading for MG53. See [[The p53 pathway]].

## What is uncertain

"USP7 stabilises p53" is an incomplete statement, and any experiment reading out p53 after changing USP7 must report the depth of the perturbation before its sign can be interpreted. How much of the inhibitors' anti-tumour effect runs through p53 rather than other substrates is actively argued, and it matters clinically: the non-p53 substrates would predict activity in TP53-mutant tumours. Much of the substrate list derives from overexpression or immunoprecipitation work, and the weight of individual entries is uneven. For this dataset, USP7 mRNA is close to uninformative about USP7 activity — the enzyme is allosterically activated by its own C-terminal tail, competed for by abundant substrates, and present in excess of what the p53 axis consumes.

## References

- Li et al., 2002, *Nature* — showed HAUSP deubiquitinates p53 and stabilises it even in the presence of excess MDM2.
- Cummins et al., 2004, *Nature* — disrupting the HAUSP gene in human cells stabilised and activated p53, the opposite of the predicted result.
- Li et al., 2004, *Molecular Cell* — partial reduction of HAUSP destabilised p53 while near-complete loss stabilised it, giving the dose-dependent model.
- Saridakis et al., 2005, *Molecular Cell* — structural basis for EBNA1 and p53 competing for the same USP7 binding site.
- Turnbull et al., 2017, *Nature* — FT671 and FT827 inhibit USP7 selectively, destabilising MDM2, raising p53 and inducing p21.
- Kategaya et al., 2017, *Nature* — independent small-molecule USP7 inhibitors acting by interfering with ubiquitin binding.

## What is on record

| | |
|---|---|
| Official name | ubiquitin specific peptidase 7 |
| Also known as | — (no recorded alias) |
| Locus | 16p13.2 — gene with protein product |
| Gene families | Ubiquitin specific peptidases |
| Other genes here in those families | [[USP1]], [[USP15]] |
| Previously named | ubiquitin specific peptidase 7 (herpes virus-associated) |

**Function**, from UniProt [Q93009](https://www.uniprot.org/uniprotkb/Q93009) (reviewed):

> Hydrolase that deubiquitinates target proteins such as ARMC5, FOXO4, DEPTOR, KAT5, p53/TP53, MDM2, ERCC6, DNMT1, UHRF1, PTEN, KMT2E/MLL5 and DAXX (PubMed:11923872, PubMed:15053880, PubMed:16964248, PubMed:18716620, PubMed:25283148, PubMed:25865756, PubMed:26678539, PubMed:28655758, PubMed:33544460, PubMed:35216969). Together with DAXX, prevents MDM2 self-ubiquitination and enhances the E3 ligase activity of MDM2 towards p53/TP53, thereby promoting p53/TP53 ubiquitination and proteasomal degradation (PubMed:15053880, PubMed:16845383, PubMed:18566590, PubMed:20153724). Deubiquitinates p53/TP53, preventing degradation of p53/TP53, and enhances p53/TP53-dependent transcription regulation, cell growth repression and apoptosis (PubMed:25283148). Deubiquitinates p53/TP53 and MDM2 and strongly stabilizes p53/TP53 even in the presence of excess MDM2, and also induces p53/TP53-dependent cell growth repression and apoptosis (PubMed:11923872, PubMed:26786098). Deubiquitination of FOXO4 in presence of hydrogen peroxide is not dependent on p53/TP53 and inhibits FOXO4-induced transcriptional activity (PubMed:16964248). In association with DAXX, is involved in the deubiquitination and translocation of PTEN from the nucleus to the cytoplasm, both processes that are counteracted by PML (PubMed:18716620). Deubiquitinates KMT2E/MLL5 preventing KMT2E/MLL5 proteasomal-mediated degradation (PubMed:26678539). Involved in cell proliferation during early embryonic development. Involved in transcription-coupled nucleotide excision repair (TC-NER) in response to UV damage: recruited to DNA damage sites following interaction with KIAA1530/UVSSA and promotes deubiquitination of ERCC6, preventing UV-induced degradation of ERCC6 (PubMed:22466611, PubMed:22466612). Involved in maintenance of DNA methylation via its interaction with UHRF1 and DNMT1: acts by mediating deubiquitination of UHRF1 and DNMT1, preventing their degradation and promoting DNA methylation by DNMT1 (PubMed:21745816, PubMed:22411829). Deubiquitinates alkylation repair enzyme ALKBH3. OTUD4 recruits USP7 and USP9X to stabilize ALKBH3, thereby promoting the repair of alkylated DNA lesions (PubMed:25944111). Acts as a chromatin regulator via its association with the Polycomb group (PcG) multiprotein PRC1-like complex; may act by deubiquitinating components of the PRC1-like complex (PubMed:20601937). Able to mediate deubiquitination of histone H2B; it is however unsure whether this activity takes place in vivo (PubMed:20601937). Exhibits a preference towards 'Lys-48'-linked ubiquitin chains (PubMed:22689415). Increases regulatory T-cells (Treg) suppressive capacity by deubiquitinating and stabilizing the transcription factor FOXP3 which is crucial for Treg cell function (PubMed:23973222). Plays a role in the maintenance of the circadian clock periodicity via deubiquitination and stabilization of the CRY1 and CRY2 proteins (PubMed:27123980). Deubiquitinates REST, thereby stabilizing REST and promoting the maintenance of neural progenitor cells (PubMed:21258371). Deubiquitinates SIRT7, inhibiting SIRT7 histone deacetylase activity and regulating gluconeogenesis (PubMed:28655758). Involved in the regulation of WASH-dependent actin polymerization at the surface of endosomes and the regulation of endosomal protein recycling (PubMed:26365382). It maintains optimal WASH complex activity and precise F-actin levels via deubiquitination of TRIM27 and WASHC1 (PubMed:26365382). Mediates the deubiquitination of phosphorylated DEPTOR, promoting its stability and leading to decreased mTORC1 signaling (PubMed:35216969). Deubiquitinates H2AB1, H2BC4 and H2BC22 (By similarity)

**Summary**, from NCBI Gene [7874](https://www.ncbi.nlm.nih.gov/gene/7874):

> The protein encoded by this gene belongs to the peptidase C19 family, which includes ubiquitinyl hydrolases. This protein deubiquitinates target proteins such as p53 (a tumor suppressor protein) and WASH (essential for endosomal protein recycling), and regulates their activities by counteracting the opposing ubiquitin ligase activity of proteins such as HDM2 and TRIM27, involved in the respective process. Mutations in this gene have been implicated in a neurodevelopmental disorder. [provided by RefSeq, Mar 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12630) · Entrez [7874](https://www.ncbi.nlm.nih.gov/gene/7874) · UniProt [Q93009](https://www.uniprot.org/uniprotkb/Q93009) · Ensembl [ENSG00000187555](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187555) · OMIM [602519](https://www.omim.org/entry/602519)

**PubMed**, as HGNC records for this gene — [12838346](https://pubmed.ncbi.nlm.nih.gov/12838346/), [9925944](https://pubmed.ncbi.nlm.nih.gov/9925944/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00028 |
| As a percentage | +0.02% |
| FDR, exposure-shuffle null | 0.9209 |
| In TP53-wild-type lines / altered lines | 0.00150 / -0.00046 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.232 raw, 0.253 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
