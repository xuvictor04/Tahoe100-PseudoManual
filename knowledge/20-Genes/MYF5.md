---
symbol: MYF5
type: gene
tier: 1
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MYF5

> [!summary] In one line
> MYF5 encodes the earliest-expressed myogenic regulatory factor, a basic helix-loop-helix protein that commits progenitor cells to the skeletal muscle lineage largely redundantly with MyoD.

## What it is

MYF5 is one of the four myogenic regulatory factors (MRFs), with [[MYOD1]], [[MYOG]] and [[MYF6]]. Like the others it binds the E-box consensus CANNTG as a heterodimer with E proteins. Functionally the MRFs divide into determination factors — Myf5 and MyoD — and differentiation factors — myogenin and MRF4. Myf5 is usually the first of the four to come on in the developing somite, downstream of Pax3, and its transcription is controlled by an unusually large array of distant enhancers.

Its loss-of-function genetics are the interesting part. Myf5-null mice have muscle, because MyoD compensates; MyoD-null mice have muscle, because Myf5 compensates; the double mutant was long thought to have none, which made the pair the textbook example of redundant determination genes. That picture was revised once it became clear that the targeted alleles at the Myf5 locus also disturb the neighbouring [[MYF6]] gene in cis — the two sit a few kilobases apart and share regulatory sequence — and that muscle does form in Myf5:MyoD double nulls when MRF4 expression is left intact. The rib malformations and perinatal lethality of the original Myf5 knockout are now read the same way, as a locus effect rather than a clean Myf5 phenotype.

In adult muscle Myf5 marks committed satellite cells: the compartment splits into Myf5-negative stem cells and Myf5-positive progenitors maintained by asymmetric division, and Myf5 is widely used as a lineage-tracing driver.

## Why it appears in this work

Myf5 is in the vault as one of the factors that drives [[MG53 (TRIM72)]] in its native tissue. TRIM72's promoter is an E-box-and-MEF2 muscle promoter, so the MRFs as a class are the principled first hypothesis for what sets MG53's transcription — and the point of checking them in [[Tahoe-100M]] is that none is present in a panel of non-muscle cancer lines. Myf5 is the most extreme case: it is a transiently expressed developmental commitment factor rather than a maintained adult one, so there is no reason to expect it here, and it is not found. See [[Transcription factor activity inference]].

## What is uncertain

The evidence tying Myf5 specifically to TRIM72 is weaker than for [[MYOD1]]. The promoter work tested MyoD and myogenin; Myf5 binds the same E-box consensus and would be expected to act there, but that is family inference rather than demonstrated occupancy and should not be stated as established. Myf5's own biology carries a structural caveat worth remembering whenever its knockouts are quoted: because Myf5 and MRF4 share a regulatory region, several published "Myf5" and "MRF4" phenotypes reflect the allele used rather than the gene named, and literature predating that realisation must be read with the allele in hand. For this dataset the consequence is simple: an activity score for a factor absent from the expressed-gene list reports its regulon's response to something else, and nothing here perturbs Myf5 anyway.

## References

- Braun et al., 1992, Cell — targeted inactivation of Myf-5 gives abnormal rib development and perinatal death, with muscle still forming.
- Rudnicki et al., 1993, Cell — MyoD or Myf-5 is required for skeletal muscle formation; either alone suffices, establishing the redundancy.
- Olson, Arnold, Rigby and Wold, 1996, Cell — "Know your neighbors": the three distinct phenotypes of MRF4-null alleles reflect cis effects on the neighbouring Myf5 gene, establishing that a phenotype at this locus cannot be assigned to the targeted gene alone.
- Kassar-Duchossoy et al., 2004, Nature — muscle forms in Myf5:Myod double mutants when Mrf4 expression is intact, identifying MRF4 as a determination gene.
- Kuang et al., 2007, Cell — Myf5-negative satellite stem cells generate Myf5-positive committed progenitors by asymmetric division.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — E-box and MEF2 elements drive the TRIM72 promoter in differentiating myoblasts (tested with MyoD and myogenin).

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 14 targets |
| Activity vs MG53 across exposures (r) | -0.020 (q 0.618) |
| With 3 principal components removed | 0.048 (q 0.184) |
| Within line, across exposures (r) | -0.026 (q 0.045) |
| Percentile against all genes | 45.6 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is absent from the expressed gene list (— CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
