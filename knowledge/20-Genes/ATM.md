---
symbol: ATM
type: gene
tier: 1
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# ATM

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

## In this dataset

*Generated from the study's tables — do not edit by hand.*


## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
