---
symbol: ATM
type: gene
tier: 1
pathway_role: p53 itself and what controls it
aliases: [TEL1, TELO1]
gene_name: ATM serine/threonine kinase
locus: 11q22.3
locus_type: gene with protein product
gene_family: [Armadillo like helical domain containing, Phosphatidylinositol 3-kinase-related kinase family, BRCA1-associated genome surveillance complex]
family_siblings_here: [ARFGEF1, ARFGEF2, ARMH3, FANCD2, HTT, PPP4R3A, RALGAPB, TAF3]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# ATM

*ATM serine/threonine kinase* — 11q22.3

> [!summary] In one line
> ATM is the apical kinase of the DNA double-strand-break response and the kinase that phosphorylates p53 to begin its activation.

## What it is

ATM is a very large serine/threonine kinase of the phosphatidylinositol-3-kinase-related (PIKK) family. It is recruited to double-strand breaks by the MRE11-RAD50-NBS1 complex and, once active, phosphorylates hundreds of substrates on S/T-Q motifs: CHK2, H2AX, KAP1, SMC1, NBS1, BRCA1, 53BP1, MDM2 and p53 among them. Two of those matter directly for p53. Phosphorylation of p53 at Ser15 and phosphorylation of MDM2 and its partners together weaken the MDM2-p53 interaction and the degradation that normally keeps p53 at a low level, which is why p53 stabilises within minutes of a break rather than being newly transcribed. ATM also has a DNA-independent mode of activation by oxidative stress, which is biochemically distinct from the break-induced mode.

Biallelic loss of ATM causes ataxia-telangiectasia: progressive cerebellar degeneration, oculocutaneous telangiectasia, immunodeficiency, marked radiosensitivity and a high rate of lymphoid malignancy. Heterozygous carriers have moderately raised breast cancer risk, and ATM is a standard entry on hereditary cancer panels. Somatic ATM loss is common in chronic lymphocytic leukaemia, mantle cell lymphoma, and lung, prostate and pancreatic cancers, and is one of the better-studied contexts for ATR and PARP inhibitor sensitivity.

## Why it appears in this work

ATM is the upstream boundary of [[The p53 pathway]] as this study traces it. Most compounds in the panel that raise p53 output do so by causing DNA damage or replication stress, and ATM, with ATR, is the sensor that converts that lesion into p53 activation. It is in the vault as an interpretive anchor: it says what the induced genes of [[p53 program P]] are downstream of.

It also carries a methodological caution that applies across this work. ATM is regulated post-translationally — recruitment, conformational change, phosphorylation — and its own transcript is close to constitutive and not a p53 output. A 24 h mRNA panel therefore sees a nearly flat ATM level whether or not the kinase is firing hard. Activity has to be inferred from what ATM's substrates did, which is the logic behind [[Transcription factor activity inference]], not read off ATM itself.

## What is uncertain

The textbook activation switch is contested. Autophosphorylation at Ser1981 with dissociation of an inactive dimer is the standard model from human cell work, but knock-in mice in which the equivalent serine cannot be phosphorylated activate Atm normally, so autophosphorylation is at least dispensable in mouse and may be a consequence rather than the cause of activation. The clean division of labour between ATM for double-strand breaks and ATR for replication stress is also a simplification: the kinases share substrates and partly compensate. For p53 specifically, ATM is one route to activation among several — nucleolar stress, oncogene-driven p14ARF and ribosomal protein signalling reach p53 without it — so ATM status does not predict p53 output in a given line. Finally, nothing in this study's design lets ATM's own functional status across the panel be read out.

## References

- Savitsky et al., 1995, Science — positional cloning of ATM as the gene mutated in ataxia-telangiectasia.
- Banin et al., 1998, Science — showed ATM phosphorylates p53 on Ser15 in the damage response.
- Bakkenist and Kastan, 2003, Nature — proposed activation by intermolecular autophosphorylation and dimer dissociation.
- Pellegrini et al., 2006, Nature — showed the corresponding autophosphorylation site is dispensable for murine Atm activation in vivo.
- Matsuoka et al., 2007, Science — mapped the large ATM/ATR substrate landscape by phosphoproteomics.
- Shiloh and Ziv, 2013, Nature Reviews Molecular Cell Biology — review of ATM signalling, including its oxidative-stress mode.

## What is on record

| | |
|---|---|
| Official name | ATM serine/threonine kinase |
| Also known as | TEL1, TELO1, TEL1, telomere maintenance 1, homolog (S. cerevisiae) |
| Locus | 11q22.3 — gene with protein product |
| Gene families | Armadillo like helical domain containing; Phosphatidylinositol 3-kinase-related kinase family; BRCA1-associated genome surveillance complex |
| Other genes here in those families | [[ARFGEF1]], [[ARFGEF2]], [[ARMH3]], [[FANCD2]], [[HTT]], [[PPP4R3A]], [[RALGAPB]], [[TAF3]] |
| Previously named | ataxia telangiectasia mutated (includes complementation groups A, C and D); ataxia telangiectasia mutated |

**Function**, from UniProt [Q13315](https://www.uniprot.org/uniprotkb/Q13315) (reviewed):

> Serine/threonine protein kinase which activates checkpoint signaling upon double strand breaks (DSBs), apoptosis and genotoxic stresses such as ionizing ultraviolet A light (UVA), thereby acting as a DNA damage sensor (PubMed:10550055, PubMed:10839545, PubMed:10910365, PubMed:12556884, PubMed:14871926, PubMed:15064416, PubMed:15448695, PubMed:15456891, PubMed:15790808, PubMed:15916964, PubMed:17923702, PubMed:21757780, PubMed:24534091, PubMed:27941124, PubMed:35076389, PubMed:9733514). Recognizes the substrate consensus sequence [ST]-Q (PubMed:10550055, PubMed:10839545, PubMed:10910365, PubMed:12556884, PubMed:14871926, PubMed:15448695, PubMed:15456891, PubMed:15916964, PubMed:17923702, PubMed:24534091, PubMed:27941124, PubMed:9733514). Phosphorylates 'Ser-139' of histone variant H2AX at double strand breaks (DSBs), thereby regulating DNA damage response mechanism (By similarity). Also plays a role in pre-B cell allelic exclusion, a process leading to expression of a single immunoglobulin heavy chain allele to enforce clonality and monospecific recognition by the B-cell antigen receptor (BCR) expressed on individual B-lymphocytes. After the introduction of DNA breaks by the RAG complex on one immunoglobulin allele, acts by mediating a repositioning of the second allele to pericentromeric heterochromatin, preventing accessibility to the RAG complex and recombination of the second allele. Also involved in signal transduction and cell cycle control. May function as a tumor suppressor. Necessary for activation of ABL1 and SAPK. Phosphorylates DYRK2, CHEK2, p53/TP53, FBXW7, FANCD2, NFKBIA, BRCA1, CREBBP/CBP, RBBP8/CTIP, FBXO46, MRE11, nibrin (NBN), RAD50, RAD17, PELI1, TERF1, UFL1, RAD9, UBQLN4, UCHL3 and DCLRE1C (PubMed:10550055, PubMed:10766245, PubMed:10802669, PubMed:10839545, PubMed:10910365, PubMed:10973490, PubMed:11375976, PubMed:12086603, PubMed:15456891, PubMed:19965871, PubMed:21757780, PubMed:24534091, PubMed:26240375, PubMed:26774286, PubMed:27941124, PubMed:30171069, PubMed:30612738, PubMed:30886146, PubMed:30952868, PubMed:38128537, PubMed:9733515, PubMed:9843217). May play a role in vesicle and/or protein transport. Could play a role in T-cell development, gonad and neurological function. Plays a role in replication-dependent histone mRNA degradation. Binds DNA ends. Phosphorylation of DYRK2 in nucleus in response to genotoxic stress prevents its MDM2-mediated ubiquitination and subsequent proteasome degradation (PubMed:19965871). Phosphorylates ATF2 which stimulates its function in DNA damage response (PubMed:15916964). Phosphorylates ERCC6 which is essential for its chromatin remodeling activity at DNA double-strand breaks (PubMed:29203878). Phosphorylates TTC5/STRAP at 'Ser-203' in the cytoplasm in response to DNA damage, which promotes TTC5/STRAP nuclear localization (PubMed:15448695). Also involved in pexophagy by mediating phosphorylation of PEX5: translocated to peroxisomes in response to reactive oxygen species (ROS), and catalyzes phosphorylation of PEX5, promoting PEX5 ubiquitination and induction of pexophagy (PubMed:26344566)

**Summary**, from NCBI Gene [472](https://www.ncbi.nlm.nih.gov/gene/472):

> The protein encoded by this gene belongs to the PI3/PI4-kinase family. This protein is an important cell cycle checkpoint kinase that phosphorylates; thus, it functions as a regulator of a wide variety of downstream proteins, including tumor suppressor proteins p53 and BRCA1, checkpoint kinase CHK2, checkpoint proteins RAD17 and RAD9, and DNA repair protein NBS1. This protein and the closely related kinase ATR are thought to be master controllers of cell cycle checkpoint signaling pathways that are required for cell response to DNA damage and for genome stability. Mutations in this gene are associated with ataxia telangiectasia, an autosomal recessive disorder. [provided by RefSeq, Aug 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:795) · Entrez [472](https://www.ncbi.nlm.nih.gov/gene/472) · UniProt [Q13315](https://www.uniprot.org/uniprotkb/Q13315) · Ensembl [ENSG00000149311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149311) · OMIM [607585](https://www.omim.org/entry/607585)

**PubMed**, as HGNC records for this gene — [7792600](https://pubmed.ncbi.nlm.nih.gov/7792600/), [7545545](https://pubmed.ncbi.nlm.nih.gov/7545545/), [8589678](https://pubmed.ncbi.nlm.nih.gov/8589678/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00299 |
| As a percentage | +0.21% |
| FDR, exposure-shuffle null | 0.2477 |
| In TP53-wild-type lines / altered lines | 0.00546 / 0.00149 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.357 raw, 0.427 with 3 PCs removed |

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
