---
type: "concept"
tags: ["concept", "method", "statistics"]
status: "current"
source: "tahoemap/vault_seed/notes/FDR calibration and the inflated null.md"
generated_by: "tahoemap"
---

# FDR calibration and the inflated null

> [!summary] In one line
> An analytic test statistic can be several times too large on this data — the earlier MG53/p53 study's was
> about 4.4× too large, so 4,500 genes "passed" at q < 0.1 — and every per-gene verdict has to be read through the
> null it was tested against.

## What the calibration found

A pipeline should check its own statistics against nulls it constructs and report the inflation factor λ — the
ratio of the observed test-statistic spread to what the null says it should be. A correct statistic gives λ = 1.
The earlier study's genome-wide screen regressed every gene on measured MG53 with line-level structure:

| Quantity | λ | Meaning |
|---|---|---|
| common slope, observed | **4.444** | the analytic statistic is ~4.4× too large on the test-statistic scale |
| common slope, response-matched placebo genes | 4.685 | matched placebo genes show the *same* inflation |
| common slope, expression-matched placebo genes | 5.518 | so does this family |
| common slope, exposure shuffled | 0.861 | shuffling the exposure gives a calibrated null |
| genotype difference, observed | 0.963 | the difference statistic is **fine** |

Two lessons carry over to any analysis of this data:

**Inflation lives in some statistics and not others.** The difference between TP53-wild-type and altered lines was
calibrated (λ 0.963); the common slope was not. Check each statistic against its own null.

**Placebo genes inflate identically.** Matched placebo genes — genes put in the exposure's place — showed λ 4.7
and 5.5. So the inflation was a property of the model's treatment of line-level structure, not of the gene under
study. "Gene A is significantly associated with gene X" at an analytic q is therefore not evidence that gene A is
special; whatever inflates A's statistic inflates a random matched gene's just as much.

## What it does to gene counts

At the analytic q < 0.1, **4,500 of 16,642 tested genes passed** (27.0%); at the exposure-shuffle q < 0.1, 5,746
(34.5%). The p53 programme's own hit rate — 27.2% and 34.4% — was exactly the genome-wide rate: **a per-gene hit
rate carries no signal unless it is compared with the rate of matched genes.**

## Which null applies to which statistic

- **Permuting a label tests a difference between label groups**, not a slope fitted across groups: relabelling
  TP53 status destroys the group assignment but leaves each line's own association intact, so for a common slope it
  gives a meaninglessly small p.
- **Shuffling the exposure within a unit** rebuilds the null empirically for an association.
- **The lone-discovery threshold** — the effect a gene would need if it were the *only* significant gene — shows how
  much of a BH pass rests on the mass of genes passing with it.
- **Deflating a gene's own t by √λ** is the most pessimistic reading, and worth stating as the floor.

## How the numbers in this vault are calibrated

- **Drug effects (z, q).** z is a robust z against the spread of the *other drug wells* on reliable plates (median,
  1.4826 × MAD), widened on noisy plates; q is Benjamini–Hochberg **within each gene across drug-doses**. Most
  drug-doses do little to most genes, so the reference distribution is mostly null by construction; but a drug that
  moves thousands of genes (toxicity, transcription shutdown) moves the gene for reasons that are not specific to
  it — which is what the artifact flags are for.
- **Gene–gene relations (fdr).** The cosine between two genes has no analytic null. tahoemap estimates the false
  discovery rate empirically by **sign concordance between two halves of the compounds**: pairs are selected in one
  half's space and their sign is checked in the other half, whose noise is independent. Under no relation the sign
  agrees half the time, so FDR(t) = disagreeing / agreeing pairs with |other-half cos| ≥ t (made monotone). It is
  conservative, and it needs no distributional assumption.
- **Validation.** Gene sets are scored against random gene sets of the same size, not against an analytic null.

## Sources

- The earlier MG53/p53 study: `genome_wide/tables/c_calibration.csv` (λ for each statistic and null),
  `genome_wide/tables/c_placebos.csv` (placebo families), `genome_wide/genome_wide.py` section C.
- tahoemap: `relations/fdr_curve.csv` (the sign-concordance curve), `docs/method.md`.

---
*Written note, copied from `tahoemap/vault_seed/notes/FDR calibration and the inflated null.md` by `tahoemap vault`. Edit it there, not here: this copy is replaced on every build.*
