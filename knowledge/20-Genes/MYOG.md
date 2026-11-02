---
symbol: MYOG
type: gene
tier: 1
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MYOG

> [!summary] In one line
> MYOG encodes myogenin, the bHLH factor that executes terminal muscle differentiation downstream of MyoD, and one of two myogenic factors shown to switch on the TRIM72 promoter.

## What it is

Myogenin is one of the four myogenic regulatory factors, with MyoD ([[MYOD1]]), Myf5 ([[MYF5]]) and MRF4 ([[MYF6]]). The family splits by stage: MyoD and Myf5 commit a cell to the myoblast lineage, while myogenin acts in differentiation, where committed myoblasts exit the cycle, fuse, and switch on contractile genes. Mouse genetics drew that line sharply. Single MyoD or Myf5 nulls have essentially normal muscle because each covers for the other, whereas myogenin nulls die perinatally with a severe deficit of myofibres despite having myoblasts present and correctly positioned.

Mechanically myogenin resembles MyoD closely. It binds the E-box consensus CANNTG only as a heterodimer with the ubiquitous E proteins (E12/E47, from TCF3) — a consensus it shares with every other MRF, so what distinguishes a myogenin target is cofactor availability and chromatin state, not sequence preference. It acts combinatorially with MEF2 factors ([[MEF2C]], [[MEF2D]]) at composite E-box/MEF2 elements, and is itself a direct MyoD target: the feed-forward step from determination to execution. Id proteins and class II HDACs gate its output.

Conditional deletion after embryonic development leaves skeletal muscle largely normal — the mice are smaller, the muscle is not broken — so the embryonic requirement is not a standing adult one. In adult muscle myogenin instead acquires a pathological role, working with class II HDACs to induce the E3 ligases of denervation atrophy. Clinically it is a diagnostic marker for rhabdomyosarcoma, strongly positive in the fusion-positive alveolar subtype.

## Why it appears in this work

[[MG53 (TRIM72)]]'s promoter is a muscle promoter, and myogenin is one of two factors directly implicated in driving it: myogenin (or MyoD) with MEF2 activates the TRIM72 promoter synergistically through adjacent E-box and MEF2 elements. If a transcription factor set MG53's level here, myogenin would be a first-line candidate. It is in the vault because the answer is negative in an instructive way — the muscle programme is silent or absent across this panel, so the candidate regulator is not available to act. That is much of why [[Transcription factor activity inference]] finds no factor explaining MG53's movement, and why [[The TRIM72 locus]] and [[Readthrough spillover]] carry the explanation instead.

## What is uncertain

The central caution is methodological. Regulon-based inference needs a factor's targets to be informative about the factor; for a factor that is not expressed, whatever score a regulon method returns reflects what its annotated targets did for unrelated reasons. Second, the TRIM72 promoter evidence comes from reporter and chromatin work in differentiating mouse C2C12 myoblasts: it establishes that myogenin *can* drive TRIM72 in muscle, not what sets trace-level transcription where the muscle programme is off. Third, "myogenin drives muscle differentiation" is more stage-restricted than it sounds given the postnatal deletion result, and its division of labour with MRF4 in late differentiation remains unresolved. Finally, whether high myogenin in rhabdomyosarcoma reflects a functioning differentiation programme or an arrested one is debated.

## References

- Hasty et al., 1993, Nature — targeted myogenin mutation causes perinatal death with severe skeletal muscle deficiency.
- Nabeshima et al., 1993, Nature — independent myogenin disruption, same conclusion: perinatal lethality from a severe muscle defect.
- Edmondson and Olson, 1989, Genes & Development — myogenin cDNA, able to activate the muscle differentiation programme in fibroblasts.
- Knapp et al., 2006, Development — deletion of myogenin in postnatal life leaves skeletal muscle normal but reduces body size.
- Moresi et al., 2010, Cell — myogenin and class II HDACs control neurogenic muscle atrophy by inducing E3 ubiquitin ligases.
- Jung and Ko, 2010, Biochemical and Biophysical Research Communications — myogenin (or MyoD) and MEF2 synergistically activate the TRIM72 promoter.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 36 targets |
| Activity vs MG53 across exposures (r) | -0.072 (q 0.038) |
| With 3 principal components removed | -0.133 (q 7.33e-05) |
| Within line, across exposures (r) | -0.019 (q 0.045) |
| Percentile against all genes | 25.3 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is absent from the expressed gene list (— CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work; muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
