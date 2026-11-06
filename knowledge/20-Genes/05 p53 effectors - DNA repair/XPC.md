---
symbol: XPC
type: gene
tier: 1
pathway_role: p53 effector: DNA repair
aliases: [xeroderma pigmentosum C]
gene_name: XPC complex subunit, DNA damage recognition and repair factor
locus: 3p25.1
locus_type: gene with protein product
gene_family: [Xeroderma pigmentosum complementation groups]
family_siblings_here: [DDB2, POLH]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: DNA repair
median_line_cpm: 60.01
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# XPC

*XPC complex subunit, DNA damage recognition and repair factor* — 3p25.1

> [!summary] In one line
> XPC is the sensor that finds bulky DNA lesions anywhere in the genome and starts nucleotide-excision repair there, and it is one of the repair genes p53 induces.

## What it is

Nucleotide-excision repair comes in two flavours that differ only in how the lesion is found. In transcription-coupled repair, a stalled RNA polymerase is the detector. In global-genome repair — the rest of the genome, including the strand nobody is transcribing — the detector is XPC, working as a heterotrimer with RAD23B and centrin-2. XPC does not read the lesion's chemistry; it recognises the single-stranded character of the undamaged strand opposite a helix-distorting adduct, which is why its substrates range from UV photoproducts to bulky chemical adducts. It then recruits TFIIH and hands off to the shared verification and incision machinery.

Because XPC serves only the global-genome branch, losing it gives a distinctive clinical picture: xeroderma pigmentosum group C patients have extreme photosensitivity and hugely raised skin-cancer risk, but usually lack the neurodegeneration seen in groups whose defects also cripple transcription-coupled repair.

Its connection to p53 is transcriptional. XPC mRNA and protein rise after UV damage in a p53-dependent manner, with little induction in p53-deficient cells, and a p53 response element has been mapped to the gene — located, in follow-up work, within the first exon near the translation start rather than in the upstream promoter. [[DDB2]], the other dedicated global-genome sensor, is likewise p53-inducible — the basis for describing p53 as raising global-genome repair capacity as a whole rather than one gene at a time.

## Why it appears in this work

XPC is a curated p53 effector in the induction arm of [[p53 program P]], sitting with [[DDB2]], [[POLH]] and [[RRM2B]] in the DNA-repair group of [[The p53 pathway]]. Its presence shapes how the programme reads: the signature is not only arrest and apoptosis genes, and a rise in it is consistent with p53 attempting repair rather than only elimination. In a panel dominated by genotoxic compounds that distinction is worth keeping explicit, because the same drug that activates p53 also makes the lesions XPC is induced to clear.

## What is uncertain

The p53-dependence of XPC induction was established largely in UV-irradiated fibroblast systems, and how far it carries to the chemical classes in this panel is not something that work addressed. The induction is modest even where it is clean, and in this dataset XPC's direction is mixed across the reference compounds — it is in the induction arm on balance, not because it reliably goes up. Whether the mapped exon-1 element is the operative one in all contexts is unresolved.

More fundamentally, XPC mRNA is a poor proxy for repair capacity. XPC acts stoichiometrically as a sensor, its protein is regulated by damage-induced ubiquitination, and DDB2 modulates its recruitment — so a change in transcript need not become a change in lesion clearance. Treat XPC here as a reporter that p53 engaged its repair arm, not as a measure of how much repair happened.

## References

- Sugasawa et al., 1998, *Molecular Cell* — identified the XPC complex as the initiator of global-genome nucleotide-excision repair.
- Araki et al., 2001, *Journal of Biological Chemistry* — identified centrin-2 as the third subunit of the XPC–RAD23B complex.
- Adimoolam & Ford, 2002, *PNAS* — showed XPC mRNA and protein are induced after UV in a p53-dependent manner, and reported a putative p53 response element upstream of the transcription start site.
- Hastak et al., 2012, *Genes & Cancer* — mapped p53 binding at the XPC locus to the first exon at the translation start, and did not reproduce binding at the earlier upstream element in cells.

## What is on record

| | |
|---|---|
| Official name | XPC complex subunit, DNA damage recognition and repair factor |
| Also known as | XPCC, RAD4, xeroderma pigmentosum group C protein |
| Locus | 3p25.1 — gene with protein product |
| Gene families | Xeroderma pigmentosum complementation groups |
| Other genes here in those families | [[DDB2]], [[POLH]] |
| Previously named | xeroderma pigmentosum, complementation group C |

**Function**, from UniProt [Q01831](https://www.uniprot.org/uniprotkb/Q01831) (reviewed):

> Involved in global genome nucleotide excision repair (GG-NER) by acting as damage sensing and DNA-binding factor component of the XPC complex (PubMed:10734143, PubMed:10873465, PubMed:12509299, PubMed:12547395, PubMed:19609301, PubMed:19941824, PubMed:20028083, PubMed:20649465, PubMed:20798892, PubMed:9734359). Has only a low DNA repair activity by itself which is stimulated by RAD23B and RAD23A. Has a preference to bind DNA containing a short single-stranded segment but not to damaged oligonucleotides (PubMed:10734143, PubMed:19609301, PubMed:20649465). This feature is proposed to be related to a dynamic sensor function: XPC can rapidly screen duplex DNA for non-hydrogen-bonded bases by forming a transient nucleoprotein intermediate complex which matures into a stable recognition complex through an intrinsic single-stranded DNA-binding activity (PubMed:10734143, PubMed:19609301, PubMed:20649465). The XPC complex is proposed to represent the first factor bound at the sites of DNA damage and together with other core recognition factors, XPA, RPA and the TFIIH complex, is part of the pre-incision (or initial recognition) complex (PubMed:10873465, PubMed:12509299, PubMed:12547395, PubMed:19941824, PubMed:20028083, PubMed:20798892, PubMed:9734359). The XPC complex recognizes a wide spectrum of damaged DNA characterized by distortions of the DNA helix such as single-stranded loops, mismatched bubbles or single-stranded overhangs (PubMed:10873465, PubMed:12509299, PubMed:12547395, PubMed:19941824, PubMed:20028083, PubMed:20798892, PubMed:9734359). The orientation of XPC complex binding appears to be crucial for inducing a productive NER (PubMed:10873465, PubMed:12509299, PubMed:12547395, PubMed:19941824, PubMed:20028083, PubMed:20798892, PubMed:9734359). XPC complex is proposed to recognize and to interact with unpaired bases on the undamaged DNA strand which is followed by recruitment of the TFIIH complex and subsequent scanning for lesions in the opposite strand in a 5'-to-3' direction by the NER machinery (PubMed:10873465, PubMed:12509299, PubMed:12547395, PubMed:19941824, PubMed:20028083, PubMed:20798892, PubMed:9734359). Cyclobutane pyrimidine dimers (CPDs) which are formed upon UV-induced DNA damage esacpe detection by the XPC complex due to a low degree of structural perurbation. Instead they are detected by the UV-DDB complex which in turn recruits and cooperates with the XPC complex in the respective DNA repair (PubMed:10873465, PubMed:12509299, PubMed:12547395, PubMed:19941824, PubMed:20028083, PubMed:20798892, PubMed:9734359). In vitro, the XPC:RAD23B dimer is sufficient to initiate NER; it preferentially binds to cisplatin and UV-damaged double-stranded DNA and also binds to a variety of chemically and structurally diverse DNA adducts (PubMed:20028083). XPC:RAD23B contacts DNA both 5' and 3' of a cisplatin lesion with a preference for the 5' side. XPC:RAD23B induces a bend in DNA upon binding. XPC:RAD23B stimulates the activity of DNA glycosylases TDG and SMUG1 (PubMed:20028083)

**Summary**, from NCBI Gene [7508](https://www.ncbi.nlm.nih.gov/gene/7508):

> The protein encoded by this gene is a key component of the XPC complex, which plays an important role in the early steps of global genome nucleotide excision repair (NER). The encoded protein is important for damage sensing and DNA binding, and shows a preference for single-stranded DNA. Mutations in this gene or some other NER components can result in Xeroderma pigmentosum, a rare autosomal recessive disorder characterized by increased sensitivity to sunlight with the development of carcinomas at an early age. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2017]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12816) · Entrez [7508](https://www.ncbi.nlm.nih.gov/gene/7508) · UniProt [Q01831](https://www.uniprot.org/uniprotkb/Q01831) · Ensembl [ENSG00000154767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154767) · OMIM [613208](https://www.omim.org/entry/613208)

**PubMed**, as HGNC records for this gene — [1522891](https://pubmed.ncbi.nlm.nih.gov/1522891/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 60.01 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 19 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.088× |
| Wild-type minus altered | 1.122× |
| Compounds moving it up in WT lines | 56 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00044 |
| As a percentage | +0.03% |
| FDR, exposure-shuffle null | 0.9060 |
| In TP53-wild-type lines / altered lines | 0.00351 / -0.00142 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.291 raw, 0.043 with 3 PCs removed |

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
