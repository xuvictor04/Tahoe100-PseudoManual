---
symbol: MEF2A
type: gene
tier: 1
pathway_role: transcription factor, muscle programme
aliases: [RSRFC4, RSRFC9]
gene_name: myocyte enhancer factor 2A
locus: 15q26.3
locus_type: gene with protein product
gene_family: [Myocyte enhancer factor 2 proteins, MADS box family]
family_siblings_here: [MEF2B, MEF2C, MEF2D, SRF]
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MEF2A

*myocyte enhancer factor 2A* — 15q26.3

> [!summary] In one line
> MEF2A is a MADS-box transcription factor of the MEF2 family that drives striated-muscle and activity-dependent neuronal gene programmes, and the MEF2 site it binds is one of the two elements that switch the TRIM72 promoter on during myogenesis.

## What it is

MEF2A carries the family's N-terminal MADS-box and MEF2 domain, which together handle dimerisation and binding to an A/T-rich consensus of the form CTA(A/T)₄TAG, and a C-terminal transactivation domain where almost all of the regulation happens.

MEF2 factors are signal-responsive rather than fate-determining. They do not specify muscle by themselves; they collaborate with the myogenic bHLH factors — MyoD, myogenin — at E-boxes placed next to MEF2 sites. And MEF2 activity is set by repressor occupancy more than by MEF2 abundance: class IIa histone deacetylases (HDAC4, 5, 7, 9) bind the MEF2 domain and hold it silent, and calcium-dependent CaMK signalling phosphorylates them, drives them out of the nucleus, and releases MEF2. p38 MAPK and ERK5 phosphorylate the transactivation domain to activate it; SUMOylation and the corepressor Cabin1 add further control. The practical consequence is that MEF2A protein can be abundant and completely inert.

MEF2A-null mice die perinatally with dilated cardiomyopathy and mitochondrial deficiency, placing MEF2A in the control of cardiac mitochondrial and structural genes. MEF2A is also a central mediator of activity-dependent transcription in neurons, where the same calcium-to-class-IIa-HDAC logic runs on a different target set. Clinically, it came to attention through a reported 21-bp deletion segregating with autosomal-dominant coronary artery disease in one family — a claim that has not held up (see below).

## Why it appears in this work

MEF2A is here as one of TRIM72's native-tissue drivers. The TRIM72 promoter contains a conserved MEF2 site immediately adjacent to an E-box, and MyoD or myogenin together with MEF2 synergise there to activate TRIM72 during C2C12 differentiation; mutating either element reduces promoter activity. MEF2A is therefore where one would look first to ask what normally sets [[MG53 (TRIM72)]] levels.

Its role here is largely the negative one, and that is the point of including it: the myogenic route is the physiological route, and 50 pooled cancer lines are not muscle. If a MEF2A-shaped signal does not explain TRIM72 variation in [[Tahoe-100M]], that is the expected result, not a failure — and it leaves the field to [[The TRIM72 locus]] geometry and [[Readthrough spillover]]. See also [[Why MG53 is hard to measure here]].

## What is uncertain

The TRIM72 promoter work identified a MEF2 *site*, not a MEF2 *paralogue*. MEF2A, B, C and D share the MADS/MEF2 domain and bind the same consensus, and reporter and gel-shift experiments do not separate them, so "MEF2A drives TRIM72" is an inference from family to member.

Because MEF2 regulation is overwhelmingly post-translational, MEF2A mRNA is a poor proxy for MEF2A activity — the reason this study uses regulon-based activity inference, which carries its own assumptions ([[Transcription factor activity inference]]). A regulon built from predominantly non-muscle data may also not contain MEF2A's muscle targets, so inferred MEF2A activity here and MEF2A's myogenic function may not be the same quantity.

On the coronary-artery-disease claim, the honest position is that it failed replication: the deletion was later found in unaffected controls, case-control studies did not reproduce the association, and the original authors contested that reading. MEF2A should not be presented as an established CAD gene.

## References

- Lu et al., 2000, PNAS — signal-dependent activation of MEF2 by dissociation from histone deacetylases.
- Naya et al., 2002, Nature Medicine — MEF2A-null mice show mitochondrial deficiency and cardiac sudden death.
- Wang et al., 2003, Science — reported a MEF2A mutation in an inherited disorder with features of coronary artery disease.
- Weng et al., 2005, Journal of Clinical Investigation — found no MEF2A mutations in coronary artery disease, with the deletion present in unaffected controls.
- Potthoff & Olson, 2007, Development — review of MEF2 as a central regulator of diverse developmental programmes.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by synergism of MyoD (or myogenin) and MEF2 at a conserved MEF2 site adjacent to an E-box.

## What is on record

| | |
|---|---|
| Official name | myocyte enhancer factor 2A |
| Also known as | RSRFC4, RSRFC9 |
| Locus | 15q26.3 — gene with protein product |
| Gene families | Myocyte enhancer factor 2 proteins; MADS box family |
| Other genes here in those families | [[MEF2B]], [[MEF2C]], [[MEF2D]], [[SRF]] |

**Function**, from UniProt [Q02078](https://www.uniprot.org/uniprotkb/Q02078) (reviewed):

> Transcriptional activator which binds specifically to the MEF2 element, 5'-YTA[AT](4)TAR-3', found in numerous muscle-specific genes. Also involved in the activation of numerous growth factor- and stress-induced genes. Mediates cellular functions not only in skeletal and cardiac muscle development, but also in neuronal differentiation and survival. Plays diverse roles in the control of cell growth, survival and apoptosis via p38 MAPK signaling in muscle-specific and/or growth factor-related transcription. In cerebellar granule neurons, phosphorylated and sumoylated MEF2A represses transcription of NUR77 promoting synaptic differentiation. Associates with chromatin to the ZNF16 promoter

**Summary**, from NCBI Gene [4205](https://www.ncbi.nlm.nih.gov/gene/4205):

> The protein encoded by this gene is a DNA-binding transcription factor that activates many muscle-specific, growth factor-induced, and stress-induced genes. The encoded protein can act as a homodimer or as a heterodimer and is involved in several cellular processes, including muscle development, neuronal differentiation, cell growth control, and apoptosis. Defects in this gene could be a cause of autosomal dominant coronary artery disease 1 with myocardial infarction (ADCAD1). Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jan 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6993) · Entrez [4205](https://www.ncbi.nlm.nih.gov/gene/4205) · UniProt [Q02078](https://www.uniprot.org/uniprotkb/Q02078) · Ensembl [ENSG00000068305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068305) · OMIM [600660](https://www.omim.org/entry/600660)

**PubMed**, as HGNC records for this gene — [1516833](https://pubmed.ncbi.nlm.nih.gov/1516833/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00839 |
| As a percentage | -0.58% |
| FDR, exposure-shuffle null | 0.0009 |
| In TP53-wild-type lines / altered lines | -0.00411 / -0.01099 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.312 raw, -0.118 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 76 targets |
| Activity vs MG53 across exposures (r) | 0.125 (q 2.16e-04) |
| With 3 principal components removed | 0.184 (q 3.52e-08) |
| Within line, across exposures (r) | 0.007 (q 0.699) |
| Percentile against all genes | 84.4 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is expressed at trace level (298.50 CPM), which is why the muscle programme is not what moves MG53 here.

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
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
