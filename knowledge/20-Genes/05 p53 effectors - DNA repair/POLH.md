---
symbol: POLH
type: gene
tier: 1
pathway_role: p53 effector: DNA repair
aliases: [pol eta, XPV]
gene_name: DNA polymerase eta
locus: 6p21.1
locus_type: gene with protein product
gene_family: [DNA polymerases, Xeroderma pigmentosum complementation groups, Zinc fingers UBZ3 CCHH-type]
family_siblings_here: [DDB2, REV3L, XPC]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: DNA repair
median_line_cpm: 59.05
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# POLH

*DNA polymerase eta* — 6p21.1

> [!summary] In one line
> POLH encodes DNA polymerase eta, the translesion polymerase that copies accurately past UV photoproducts, and whose loss causes the variant form of xeroderma pigmentosum.

## What it is

Pol eta is a Y-family DNA polymerase — one of the specialists, with pol iota, pol kappa and REV1, that replicate templates the replicative polymerases cannot accommodate. Its signature substrate is the cyclobutane pyrimidine dimer, the commonest UV photoproduct. Where pol delta stalls, pol eta's unusually open and solvent-exposed active site takes the covalently joined dimer in as though it were an ordinary base pair, holding the distorted template in a near-B-form geometry — the "molecular splint" description — and inserting the correct two adenines. The bypass is therefore largely error-free, which makes pol eta a repair-adjacent enzyme rather than simply a mutator.

On undamaged DNA the same open site makes it inaccurate and barely processive, so access is restricted. After a fork stalls, RAD6–RAD18 mono-ubiquitinates PCNA at K164; pol eta reads that mark through its PIP box and UBZ zinc finger. It synthesises a short patch and is displaced — a polymerase switch, not a replacement replicase. Translesion capacity is set mostly by that access machinery.

Biallelic loss of POLH causes xeroderma pigmentosum variant: sun sensitivity and high skin cancer incidence, but with *normal* nucleotide excision repair — the defect is in post-replication damage tolerance, which distinguishes it from the classical XP groups ([[XPC]], [[DDB2]]). Pol eta has a second job in adaptive immunity, generating the A:T mutations of immunoglobulin somatic hypermutation. It also bypasses cisplatin crosslinks, the basis for its association with platinum resistance. POLH is reported as a p53 target: induced by DNA damage p53-dependently, with a p53-binding site identified at its promoter, and its knockdown impairing p53 activation — placing it, like [[PLK3]], among p53 outputs that also feed back on p53.

## Why it appears in this work

POLH is a curated DNA-repair effector in the induction arm of [[p53 program P]], and what it adds is a third behaviour alongside arrest and death: damage *tolerance*. Its induction says part of p53's output is directed at letting replication continue through lesions rather than at stopping or killing the cell — pro-survival in the short term, mutagenic over time. Its direction of benefit is therefore genuinely ambiguous in a way [[CDKN1A]]'s is not.

## What is uncertain

The p53-target status is the soft point. The evidence is coherent but not broadly replicated, the promoter element is not one of the canonical p53 response elements, and POLH is damage-inducible by several routes — so the direct-versus-indirect question is open. The claim that pol eta is required for full p53 activation after damage has not been independently established. A more general caution: translesion synthesis is governed principally by PCNA ubiquitination and regulated access to the stalled fork, so a change in POLH mRNA need not correspond to a change in bypass activity. Finally, pol eta's role in chemoresistance is contested: higher pol eta has been associated with platinum resistance in some settings, while loss of translesion capacity sensitises cells to crosslinkers in others.

## References

- Johnson et al., 1999, Science — mutations in hRAD30/POLH underlie the variant form of xeroderma pigmentosum.
- Masutani et al., 1999, Nature — the XPV gene product is human DNA polymerase eta.
- Zeng et al., 2001, Nature Immunology — pol eta acts as an A:T mutator during somatic hypermutation of immunoglobulin variable genes.
- Liu and Chen, 2006, Molecular and Cellular Biology — POLH is a p53 target whose loss modulates the DNA damage checkpoint and p53 activation.

## What is on record

| | |
|---|---|
| Official name | DNA polymerase eta |
| Also known as | XPV, RAD30A, XP-V |
| Locus | 6p21.1 — gene with protein product |
| Gene families | DNA polymerases; Xeroderma pigmentosum complementation groups; Zinc fingers UBZ3 CCHH-type |
| Other genes here in those families | [[DDB2]], [[REV3L]], [[XPC]] |
| Previously named | polymerase (DNA directed), eta; polymerase (DNA) eta |

**Function**, from UniProt [Q9Y253](https://www.uniprot.org/uniprotkb/Q9Y253) (reviewed):

> DNA polymerase specifically involved in the DNA repair by translesion synthesis (TLS) (PubMed:10385124, PubMed:11743006, PubMed:16357261, PubMed:20388628, PubMed:24449906, PubMed:24553286, PubMed:38212351). Due to low processivity on both damaged and normal DNA, cooperates with the heterotetrameric (REV3L, REV7, POLD2 and POLD3) POLZ complex for complete bypass of DNA lesions. Inserts one or 2 nucleotide(s) opposite the lesion, the primer is further extended by the tetrameric POLZ complex. In the case of 1,2-intrastrand d(GpG)-cisplatin cross-link, inserts dCTP opposite the 3' guanine (PubMed:24449906). Particularly important for the repair of UV-induced pyrimidine dimers (PubMed:10385124, PubMed:11743006). Although inserts the correct base, may cause base transitions and transversions depending upon the context. May play a role in hypermutation at immunoglobulin genes (PubMed:11376341, PubMed:14734526). Forms a Schiff base with 5'-deoxyribose phosphate at abasic sites, but does not have any lyase activity, preventing the release of the 5'-deoxyribose phosphate (5'-dRP) residue. This covalent trapping of the enzyme by the 5'-dRP residue inhibits its DNA synthetic activity during base excision repair, thereby avoiding high incidence of mutagenesis (PubMed:14630940). Targets POLI to replication foci (PubMed:12606586)

**Summary**, from NCBI Gene [5429](https://www.ncbi.nlm.nih.gov/gene/5429):

> This gene encodes a member of the Y family of specialized DNA polymerases. It copies undamaged DNA with a lower fidelity than other DNA-directed polymerases. However, it accurately replicates UV-damaged DNA; when thymine dimers are present, this polymerase inserts the complementary nucleotides in the newly synthesized DNA, thereby bypassing the lesion and suppressing the mutagenic effect of UV-induced DNA damage. This polymerase is thought to be involved in hypermutation during immunoglobulin class switch recombination. Mutations in this gene result in XPV, a variant type of xeroderma pigmentosum. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9181) · Entrez [5429](https://www.ncbi.nlm.nih.gov/gene/5429) · UniProt [Q9Y253](https://www.uniprot.org/uniprotkb/Q9Y253) · Ensembl [ENSG00000170734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170734) · OMIM [603968](https://www.omim.org/entry/603968)

**PubMed**, as HGNC records for this gene — [20012583](https://pubmed.ncbi.nlm.nih.gov/20012583/), [10385124](https://pubmed.ncbi.nlm.nih.gov/10385124/), [10398605](https://pubmed.ncbi.nlm.nih.gov/10398605/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 59.05 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 2 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.158× |
| Wild-type minus altered | 1.136× |
| Compounds moving it up in WT lines | 86 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00213 |
| As a percentage | +0.15% |
| FDR, exposure-shuffle null | 0.5131 |
| In TP53-wild-type lines / altered lines | 0.00474 / 0.00055 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.365 raw, 0.050 with 3 PCs removed |

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
