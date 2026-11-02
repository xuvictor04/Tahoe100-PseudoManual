---
type: concept
tags: [concept, method, statistics]
status: current
---

# FDR calibration and the inflated null

> [!summary] In one line
> The genome-wide screen's analytic test statistic is about 4.4× too large, so 4,500 genes "pass" at
> q < 0.1 — and every per-gene verdict in this study has to be read through that fact.

## What the calibration found

The pipeline checks its own statistics against nulls it constructs, and reports the inflation factor λ — the
ratio of the observed test-statistic spread to what the null says it should be. A correct statistic gives
λ = 1.

| Quantity | λ | Meaning |
|---|---|---|
| common slope, observed | **4.444** | the analytic statistic is ~4.4× too large on the test-statistic scale |
| common slope, response-matched placebo genes | 4.685 | matched placebo genes show the *same* inflation |
| common slope, expression-matched placebo genes | 5.518 | so does this family |
| common slope, exposure shuffled | 0.861 | shuffling the exposure gives a calibrated null |
| genotype difference, observed | 0.963 | the difference statistic is **fine** |

Two things follow immediately.

**The inflation is in the common slope, not the genotype difference.** `diff = b_WT − b_alt` is calibrated
(λ 0.963). So the study's repeated finding that *no gene differs by TP53 status* rests on a statistic that
needs no correction. The common slope does.

**Placebo genes inflate identically.** Matched placebo genes — genes put in MG53's place — show λ 4.7 and
5.5. So the inflation is a property of the model's treatment of line-level structure, not of MG53. "MG53 is
significantly associated with gene X" at the analytic q is therefore not evidence that MG53 is special;
whatever is inflating MG53's statistic inflates a random matched gene's just as much.

## What it does to the gene counts

At the analytic `q_common` < 0.1, **4,500 of 16,642 tested genes pass** (27.0%). At the exposure-shuffle
`q_xperm_common` < 0.1, 5,746 pass (34.5%). The p53 programme's own hit rate — 27.2% and 34.4% — is exactly
the genome-wide rate. A p53 target is no more likely than any gene to be "associated with MG53".

That is the most useful single sentence in this note: **the per-gene hit rate carries no signal about p53.**

## The three ways a per-gene verdict is read in this study

1. **Analytic `q_common`** — not used for verdicts. Recorded for continuity only.
2. **Exposure-shuffle `q_xperm_common`** — the verdict statistic. The exposure is shuffled within cell, which
   rebuilds the null empirically and gives λ 0.861. This is what `mg53_verdict_common` uses.
3. **The lone-discovery threshold** — the slope a gene would need if it were the *only* significant gene
   among the 16,642. For [[MDM2]] that is |b| ≥ 0.0102 against its actual 0.0050, so it clears BH only
   because a large mass of genes clears with it, and that mass is the inflated part. Carried in every gene
   note's bounds columns.

A fourth, most pessimistic reading: deflate the gene's own *t* by √λ. MDM2's t = −2.51 becomes −1.19,
p ≈ 0.24. Worth stating because it is the floor of what the evidence could mean.

## Why the TP53-relabelling null cannot be used on the common slope

The pipeline documents this explicitly and it is easy to get wrong. Permuting the TP53 labels tests the
*difference* between genotype groups — it destroys the group assignment while leaving each line's own
MG53–outcome relationship intact. So for `diff` it is a valid null. For the **common slope**, which is fitted
across groups, relabelling changes nothing that the statistic depends on: the within-line association
survives the permutation. Using it there would produce a meaninglessly small p.

An earlier version of the per-gene tables built verdicts on the analytic q; the fix to
`q_xperm_common` moved the verdict count among the 29 curated effectors from 6 to 8. See
[[Corrections and retractions]].

## Links

- [[Nulls and calibration]] — the mechanics of each null
- [[Placebo genes and reference families]] — why the matched-placebo result above matters so much
- [[The screen model]] · [[Cross-fitting and circularity]] · [[How the numbers are decided]]

## Sources

- `genome_wide/tables/c_calibration.csv` — λ for each statistic and null; `N_q01_common` = 4,500.
- `genome_wide/tables/c_placebos.csv` — the placebo families (200 exposures at the WT/altered split; only
  10 per family in the per-gene screen, which caps percentile resolution at 0.1).
- `genome_wide/genome_wide.py`, section C — the documented list of which null applies to which statistic.
