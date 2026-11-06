---
type: concept
tags: [concept, method, statistics]
status: current
---

# Cross-fitting and circularity

> [!summary] In one line
> A gene set selected with a label cannot then be used to test a hypothesis about that label — the test is run on
> the data that produced it — and the cure is to select on one part of the data and test on another.

## The problem, concretely

The earlier MG53/p53 study defined its p53 programme as "genes whose drug response differs between TP53-wild-type
and TP53-altered lines". Now ask: *is this programme's response wild-type-specific?* The answer is guaranteed to be
yes, because that is the selection rule. Any statistic built from programme membership and compared across TP53
genotype inherits that guarantee. It is why that study reported a 3.07× wild-type/altered baseline split for
[[MDM2]] as a **measurement check** rather than as a finding.

## Which columns are circular

The practical rule: **circular columns describe, non-circular columns test.** In that study:

| Circular — selected using TP53 labels | Not circular — never used them |
|---|---|
| programme membership, arm, rank in the programme | slopes on an independent exposure, their errors and q values |
| wild-type mean fold change, wild-type minus altered | expression level, lines expressing, readthrough geometry |
| the share of compounds raising the gene in wild-type lines | detectable-effect bounds |

A note may say "MDM2 is rank 3 of the induction arm with a 1.255× fold change" as description. It may not say
"therefore MDM2's response is p53-specific".

## What was done about it, and what tahoemap does

**Cross-fitting.** The earlier programme was re-derived five times, each time leaving out a fifth of the compounds;
how often each gene was re-selected says whether its membership is a stable feature or a fit to a few compounds.
It was frequently the latter: of 67 programme genes with a verdict, 20 were kept in 0 or 1 of the 5 folds.

**Leave-one-compound-out stability** repeats a selection dropping one compound at a time.

**A label-free parallel** repeats an analysis on a gene set selected *without* the label; where both agree, the
conclusion does not rest on the circular selection.

**A curated alternative.** Literature gene sets, selected with no reference to the dataset, are noisier and
smaller, but they cannot be circular.

tahoemap is built so that its headline numbers are not circular:

- **No labels are used to build the vector space.** Genes are placed by how they respond across every active
  drug-dose and line; modules are found without any gene annotation. Cell-line genotype (TP53 status) is shown
  next to the data, never used to select it.
- **Split halves of the compounds.** The space is fitted again on two disjoint halves of the compounds (salt forms
  kept together), and each gene–gene relation carries its cosine in both halves (`evidence`: `both halves`,
  `one half`, `not reproduced`). A relation seen in both halves was found with one set of drugs and confirmed with
  another.
- **External validation sets.** The control sets used to score the space (`tahoemap/data/control_sets.json`) and
  the Hallmark / Reactome sets were not derived from Tahoe.

## The second circularity, which is easier to miss

Reference families can be selected too. In the earlier study, a 4,642-gene export looked like "all genes", but
**4,500 of them were in it because the screen had already called them significant**. A percentile computed in
that family is a rank inside a discovery set, not a position among genes in general. When a vault table ranks a
gene "among its partners" or "in its module", the reference family is that gene's partners or that module — not
the genome.

## Sources

- The earlier MG53/p53 study: `mg53_p53/findings/tables/tableD_p53_target_genes.csv` (`n_folds_kept`,
  `loco_frequency`), the label-free per-line tables, and its corrections ledger.
- tahoemap: `embed/gene_unit_half1.npy`, `gene_unit_half2.npy`, `relations/gene_relations.parquet`
  (`cos_half1`, `cos_half2`, `evidence`), `validation/control_sets.csv`.
