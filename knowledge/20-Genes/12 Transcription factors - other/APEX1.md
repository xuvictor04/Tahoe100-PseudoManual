---
symbol: APEX1
type: gene
tier: 2
pathway_role: transcription factor
aliases: [APE, REF1, HAP1, APX, APEN, REF-1]
gene_name: apurinic/apyrimidinic endodeoxyribonuclease 1
locus: 14q11.2
locus_type: gene with protein product
gene_family: [SET complex, Endoribonucleases]
family_siblings_here: [SMG6]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# APEX1

*apurinic/apyrimidinic endodeoxyribonuclease 1* — 14q11.2

> [!summary] In one line
> APEX1 encodes APE1/Ref-1: the main AP endonuclease of base-excision repair and, separately, a redox cofactor that keeps other transcription factors able to bind DNA.

## What it is

APE1 incises the DNA backbone at abasic sites left by glycosylases, the committed step of base-excision repair. It is abundant, largely nuclear, and essential: homozygous loss is early-embryonic lethal in mice. Its second function was discovered independently, as Ref-1, an activity that restores DNA binding to oxidised AP-1, and was later extended to NF-κB, HIF-1α, STAT3 and p53 — redox chemistry, not sequence-specific DNA binding of its own. The two activities are separable: APX3330 blocks the redox function and spares the endonuclease.

## Why it appears in this work

APEX1 is in the vault because the activity-inference step scored it high as a candidate regulator upstream of [[MG53 (TRIM72)]]. It is better read as a redox reporter than a factor at a promoter: if its inferred activity moves, the likelier cause is an exposure's oxidative tone acting on its partners. Its reported stimulation of p53 DNA binding is this gene's one direct line into [[The p53 pathway]].

## What is uncertain

APE1 is not a sequence-specific transcription factor, so its assigned regulon is borrowed from the factors it reduces, and a high inferred activity may be reporting AP-1, NF-κB or HIF-1α output instead — a limitation of [[Transcription factor activity inference]] applied to a cofactor. How much of the redox function operates at endogenous protein levels, rather than in vitro on oxidised substrate, remains argued. The repair activity itself is not in doubt.

## References

- Demple et al., 1991, PNAS — cloned the major human apurinic/apyrimidinic endonuclease.
- Xanthoudakis and Curran, 1992, EMBO Journal — identified Ref-1 as a nuclear factor that restores AP-1 DNA binding.
- Xanthoudakis et al., 1996, PNAS — Apex-null mouse embryos die early, establishing the gene as essential.
- Jayaraman et al., 1997, Genes and Development — Ref-1 stimulates the DNA binding and transcriptional activity of p53 in vitro.
- Gaiddon et al., 1999, EMBO Journal — Ref-1 associates with p53 in cells, and is required for its transactivation and pro-apoptotic function.
- Tell et al., 2009, Antioxidants and Redox Signaling — review of APE1/Ref-1's dual repair and redox roles.

## What is on record

| | |
|---|---|
| Official name | apurinic/apyrimidinic endodeoxyribonuclease 1 |
| Also known as | APE, REF1, HAP1, APX, APEN, REF-1, APE-1, APE1 |
| Locus | 14q11.2 — gene with protein product |
| Gene families | SET complex; Endoribonucleases |
| Other genes here in those families | [[SMG6]] |
| Previously named | APEX nuclease (multifunctional DNA repair enzyme); APEX nuclease (multifunctional DNA repair enzyme) 1 |

**Function**, from UniProt [P27695](https://www.uniprot.org/uniprotkb/P27695) (reviewed):

> Multifunctional protein that plays a central role in the cellular response to oxidative stress. The two major activities of APEX1 are DNA repair and redox regulation of transcriptional factors (PubMed:11118054, PubMed:11452037, PubMed:15831793, PubMed:18439621, PubMed:18579163, PubMed:21762700, PubMed:24079850, PubMed:8355688, PubMed:9108029, PubMed:9560228). Functions as an apurinic/apyrimidinic (AP) endodeoxyribonuclease in the base excision repair (BER) pathway of DNA lesions induced by oxidative and alkylating agents. Initiates repair of AP sites in DNA by catalyzing hydrolytic incision of the phosphodiester backbone immediately adjacent to the damage, generating a single-strand break with 5'-deoxyribose phosphate and 3'-hydroxyl ends. Also incises at AP sites in the DNA strand of DNA/RNA hybrids, single-stranded DNA regions of R-loop structures, and single-stranded RNA molecules (PubMed:15380100, PubMed:16617147, PubMed:18439621, PubMed:19123919, PubMed:19188445, PubMed:19934257, PubMed:20699270, PubMed:21762700, PubMed:24079850, PubMed:8932375, PubMed:8995436, PubMed:9804799). Operates at switch sites of immunoglobulin (Ig) constant regions where it mediates Ig isotype class switch recombination. Processes AP sites induced by successive action of AICDA and UNG. Generates staggered nicks in opposite DNA strands resulting in the formation of double-strand DNA breaks that are finally resolved via non-homologous end joining repair pathway (By similarity). Has 3'-5' exodeoxyribonuclease activity on mismatched deoxyribonucleotides at the 3' termini of nicked or gapped DNA molecules during short-patch BER (PubMed:11832948, PubMed:1719477). Possesses DNA 3' phosphodiesterase activity capable of removing lesions (such as phosphoglycolate and 8-oxoguanine) blocking the 3' side of DNA strand breaks (PubMed:15831793, PubMed:7516064). Also acts as an endoribonuclease involved in the control of single-stranded RNA metabolism. Plays a role in regulating MYC mRNA turnover by preferentially cleaving in between UA and CA dinucleotides of the MYC coding region determinant (CRD). In association with NMD1, plays a role in the rRNA quality control process during cell cycle progression (PubMed:19188445, PubMed:19401441, PubMed:21762700). Acts as a loading factor for POLB onto non-incised AP sites in DNA and stimulates the 5'-terminal deoxyribose 5'-phosphate (dRp) excision activity of POLB (PubMed:9207062). Exerts reversible nuclear redox activity to regulate DNA binding affinity and transcriptional activity of transcriptional factors by controlling the redox status of their DNA-binding domain, such as the FOS/JUN AP-1 complex after exposure to IR (PubMed:10023679, PubMed:11118054, PubMed:11452037, PubMed:18579163, PubMed:8355688, PubMed:9108029). Involved in calcium-dependent down-regulation of parathyroid hormone (PTH) expression by binding to negative calcium response elements (nCaREs). Together with HNRNPL or the dimer XRCC5/XRCC6, associates with nCaRE, acting as an activator of transcriptional repression (PubMed:11809897, PubMed:14633989, PubMed:8621488). May also play a role in the epigenetic regulation of gene expression by participating in DNA demethylation (PubMed:21496894). Stimulates the YBX1-mediated MDR1 promoter activity, when acetylated at Lys-6 and Lys-7, leading to drug resistance (PubMed:18809583). Plays a role in protection from granzyme-mediated cellular repair leading to cell death (PubMed:18179823). Binds DNA and RNA. Associates, together with YBX1, on the MDR1 promoter. Together with NPM1, associates with rRNA (PubMed:19188445, PubMed:19401441, PubMed:20699270)

**Summary**, from NCBI Gene [328](https://www.ncbi.nlm.nih.gov/gene/328):

> The APEX gene encodes the major AP endonuclease in human cells. It encodes the APEX endonuclease, a DNA repair enzyme with apurinic/apyrimidinic (AP) activity. Such AP activity sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. The AP sites are the most frequent pre-mutagenic lesions that can prevent normal DNA replication. Splice variants have been found for this gene; all encode the same protein. Disruptions in the biological functions related to APEX are associated with many various malignancies and neurodegenerative diseases.[provided by RefSeq, Dec 2019]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:587) · Entrez [328](https://www.ncbi.nlm.nih.gov/gene/328) · UniProt [P27695](https://www.uniprot.org/uniprotkb/P27695) · Ensembl [ENSG00000100823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100823) · OMIM [107748](https://www.omim.org/entry/107748)

**PubMed**, as HGNC records for this gene — [1719477](https://pubmed.ncbi.nlm.nih.gov/1719477/), [1627644](https://pubmed.ncbi.nlm.nih.gov/1627644/), [9786884](https://pubmed.ncbi.nlm.nih.gov/9786884/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00182 |
| As a percentage | -0.13% |
| FDR, exposure-shuffle null | 0.5924 |
| In TP53-wild-type lines / altered lines | -0.00413 / -0.00041 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.111 raw, -0.134 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 33 targets |
| Activity vs MG53 across exposures (r) | 0.314 (q 2.20e-23) |
| With 3 principal components removed | 0.262 (q 9.42e-16) |
| Within line, across exposures (r) | 0.020 (q 0.113) |
| Percentile against all genes | 99.5 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
