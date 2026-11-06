---
symbol: MEF2B
type: gene
tier: 1
pathway_role: transcription factor, muscle programme
aliases: [RSRFR2]
gene_name: myocyte enhancer factor 2B
locus: 19p13.11
locus_type: gene with protein product
gene_family: [Myocyte enhancer factor 2 proteins, MADS box family]
family_siblings_here: [MEF2A, MEF2C, MEF2D, SRF]
tags: [gene, muscle-tf]
generated_by: knowledge/_build/build_vault.py
---

# MEF2B

*myocyte enhancer factor 2B* — 19p13.11

> [!summary] In one line
> MEF2B is the divergent member of the MEF2 family — named for muscle because of the DNA-binding domain it shares with its paralogues, but best established as a germinal-centre B-cell factor that activates BCL6 and is recurrently mutated in lymphoma.

## What it is

MEF2B shares the N-terminal MADS-box and MEF2 domain with [[MEF2A]], MEF2C and MEF2D, and therefore binds the same A/T-rich consensus. Outside that domain it diverges from the other three, and it was flagged as the unusual member of the family when the mouse gene was first characterised. The family name is a statement about a shared binding site, not about where each member works.

The best-supported biology for MEF2B is in B cells, not muscle. It is expressed in germinal-centre B cells, where it directly activates *BCL6*, the factor on which the germinal-centre reaction and the lymphomas derived from it depend; losing MEF2B impairs proliferation of those B cells, and raising BCL6 compensates only partly, implying targets beyond BCL6. MEF2B is recurrently mutated in diffuse large B-cell and follicular lymphoma, at roughly one case in nine. The mutations fall into two classes: N-terminal changes raise its transcriptional activity and BCL6 with it, some by disrupting binding to the corepressor CABIN1, others by altering dimerisation; C-terminal changes truncate the protein and remove regulatory phosphorylation and SUMOylation sites, raising both activity and stability. Conditional mouse work places MEF2B as an instructor of germinal-centre development and an oncogene in B-cell lymphomagenesis, and expression surveys show a germinal-centre-associated pattern, though not one restricted to germinal-centre-derived tumours.

MEF2B is expressed in the early cardiac and skeletal muscle lineages of the mouse embryo and is a potent transactivator there, so its muscle credentials are more than family membership. But a MEF2B-specific *requirement* in striated muscle, demonstrated by loss of function, is not something I can point to.

## Why it appears in this work

MEF2B is here as one of the candidate native-tissue drivers of [[MG53 (TRIM72)]]: the TRIM72 promoter carries a conserved MEF2 site next to an E-box, the family binds that site, and the family was entered as a set. That is a defensible way to build a candidate list, and MEF2B is the member to hold most loosely. The question this study can ask is whether its inferred activity tracks TRIM72 across exposures; the generated block carries that. If MEF2B is doing anything in cancer lines, the likelier routes are its B-cell programme or generic MEF2-site occupancy, not myogenesis. See [[The TRIM72 locus]] and [[Transcription factor activity inference]].

## What is uncertain

Treating MEF2B as a muscle transcription factor is the weakest link here. The name and the shared DNA-binding domain justify grouping it with its paralogues; the functional literature does not place it in the myogenic programme as it does MEF2A and MEF2C.

Nothing I can cite puts MEF2B protein at the TRIM72 promoter: the study motivating this gene set identified a MEF2 site, without resolving which paralogue occupies it in muscle, let alone elsewhere.

Paralogue-specific activity inference is intrinsically hard here because all four members read the same consensus: an inferred "MEF2B activity" may report shared MEF2-site occupancy rather than MEF2B — a property of the method applied to this family, not a defect of this dataset.

Class IIa HDACs and the HUCA corepressor complex do restrain MEF2B — the commonest lymphoma mutant, D83V, works partly by escaping both — so that much is established. What is not is whether the gating is quantitatively like MEF2A's: the family is usually described with a single regulatory model, and MEF2B's divergent C-terminus is a reason not to transfer it wholesale.

## References

- Molkentin et al., 1996, Molecular and Cellular Biology — MEF2B is a potent transactivator expressed in the early myogenic lineages.
- Morisaki et al., 1997, Journal of Biochemistry — characterised mouse *Mef2b* as the unique member of the MEF2 gene family.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — identified a conserved MEF2 site adjacent to an E-box in the TRIM72 promoter, activated by MyoD/myogenin and MEF2 together.
- Ying et al., 2013, Nature Immunology — MEF2B directly activates BCL6 in germinal-centre B cells, and MEF2B mutations in DLBCL and follicular lymphoma deregulate BCL6.
- Krenács et al., 2015, Virchows Archiv — surveyed MEF2B expression across lymphoid tissues and malignant lymphomas.
- Brescia et al., 2018, Cancer Cell — MEF2B instructs germinal-centre development and acts as an oncogene in B-cell lymphomagenesis.
- Yu et al., 2024, Nature Communications — MEF2B C-terminal mutations enhance transcriptional activity and protein stability to drive B-cell lymphomagenesis.

## What is on record

| | |
|---|---|
| Official name | myocyte enhancer factor 2B |
| Also known as | RSRFR2 |
| Locus | 19p13.11 — gene with protein product |
| Gene families | Myocyte enhancer factor 2 proteins; MADS box family |
| Other genes here in those families | [[MEF2A]], [[MEF2C]], [[MEF2D]], [[SRF]] |

**Function**, from UniProt [Q02080](https://www.uniprot.org/uniprotkb/Q02080) (reviewed):

> Transcriptional activator which binds specifically to the MEF2 element, 5'-YTA[AT](4)TAR-3', found in numerous muscle-specific genes. Activates transcription via this element. May be involved in muscle-specific and/or growth factor-related transcription

**Summary**, from NCBI Gene [100271849](https://www.ncbi.nlm.nih.gov/gene/100271849):

> The product of this gene is a member of the MADS/MEF2 family of DNA binding proteins. The protein is thought to regulate gene expression, including expression of the smooth muscle myosin heavy chain gene. This region undergoes considerable alternative splicing, with transcripts supporting two non-overlapping loci (GeneID 729991 and 100271849) as well as numerous read-through transcripts that span both loci (annotated as GeneID 4207). Several isoforms of this protein are expressed from either this locus or from some of the read-through transcripts annotated on GeneID 4207. [provided by RefSeq, Jan 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6995) · Entrez [100271849](https://www.ncbi.nlm.nih.gov/gene/100271849) · UniProt [Q02080](https://www.uniprot.org/uniprotkb/Q02080) · Ensembl [ENSG00000213999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213999) · OMIM [600661](https://www.omim.org/entry/600661)

**PubMed**, as HGNC records for this gene — [1516833](https://pubmed.ncbi.nlm.nih.gov/1516833/), [8575763](https://pubmed.ncbi.nlm.nih.gov/8575763/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00807 |
| As a percentage | +0.56% |
| FDR, exposure-shuffle null | 0.0361 |
| In TP53-wild-type lines / altered lines | 0.00713 / 0.00865 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.016 raw, -0.133 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is expressed at trace level (13.77 CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
