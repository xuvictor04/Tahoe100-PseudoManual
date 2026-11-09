---
type: "concept"
tags: ["concept", "artefact", "measurement"]
status: "current"
source: "tahoemap/vault_seed/notes/Readthrough spillover.md"
generated_by: "tahoemap"
---

# Readthrough spillover

> [!summary] In one line
> Transcription that fails to terminate at one gene runs into the next one on the same strand and is counted as
> that gene's mRNA — so two neighbouring genes can "move together" with no regulation at all.

## The mechanism

RNA polymerase II does not stop cleanly at every annotated 3′ end. When termination fails, the polymerase
continues into whatever lies 3′ on the same strand, and a short-read assay assigns the resulting reads to the
gene they land in. The effect scales with the *donor's* expression, not the recipient's, so a gene sitting a
few kilobases 3′ of a highly expressed neighbour can register large apparent changes that are not its own
transcription at all.

Readthrough is itself regulated: it increases under stress, heat shock, osmotic shock, viral infection and
various transcription and translation inhibitors — exactly the kind of compound a drug screen contains. So the
drugs that seem to "raise" an exposed gene are often the drugs that raise readthrough.

**Naming rule.** This phenomenon is called **readthrough spillover**. Chromosomal position is written "3′ of" or
"5′ of". The words "upstream" and "downstream" are reserved for regulatory consequence and never used for
position — a distinction that matters because confusing the two is how a measurement artefact gets written up as
a pathway.

## The worked example: the TRIM72 locus

In the earlier MG53/p53 study, [[TRIM72]] lay 17.05 kb 3′ of [[FUS]] on the same strand, with FUS at roughly
**47× TRIM72's level** and PYCARD-AS1 between them. What the study found:

**Solid — the phenomenon is real and strand-aware.** In the wells where TRIM72 rose most, the plus-strand genes on
the readthrough path rose together (median excess **+0.856 log2**, 14 of 15 wells, one-sided Wilcoxon p 9×10⁻⁵,
shuffle unit = well), while **PYCARD** — co-positional with PYCARD-AS1 to the base pair but on the *minus*
strand — **fell** (median −0.495 log2, negative in 14 of 15, p 0.0013). Two genes at identical coordinates moving
in opposite directions rules out a mapping smear and establishes that the quantification respects strand.

**Not solid — the magnitude.** A flux model calibrated three independent ways (κ = 5.36 to 8.00 CPM delivered to
TRIM72 per CPM delivered to PYCARD-AS1) **over-predicted** the observed rise by about 59% at the median, and
per-well attributable fractions ran from −140% to +742%: order-of-magnitude consistent, quantitatively unaccounted
for. The honest statement was "readthrough spillover is the leading account of the apparent induction, and the
arithmetic does not close" — not "the induction is readthrough".

Restricting a comparison to genes that are structurally incapable of spillover (no expressed same-strand gene
close 5′ of them) is a useful control; in that study it did not change the conclusion.

## What tahoemap does about it

Every gene pair in `relations/gene_relations.parquet` carries genomic flags from the reference annotation
(Ensembl GRCh38 coordinates):

- `locus` — the two genes are ≤ 50 kb apart on the same chromosome;
- `readthrough_risk` — same strand, ≤ 20 kb apart, and the 5′ gene is ≥ 8× more expressed than the 3′ gene (the
  geometry in which the 3′ gene's counts can be the 5′ gene's transcription).

A gene note marks such partners in its "move with / move opposite" tables and says which gene lies 3′ of which.
Locus pairs are **never** called novel candidates. A readthrough-risk pair that "moves together" is first an
artefact candidate and only second a co-regulation candidate; a strand-aware check (does the opposite-strand gene
at the same place move the other way?) is the test that separates them.

## Sources

- The earlier MG53/p53 study: `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv` (exposure class, 5′
  same-strand neighbour), `c_locus_obs_over_exp_raiser_wells.csv` (the per-well strand contrast),
  `c_DoG_gene_exposure_classes.csv` (the exposure class of every gene).
- tahoemap: `relations/gene_relations.parquet` (`locus`, `readthrough_risk`, `distance_bp`, `same_strand`) and
  `reference/annotations.parquet` (`chrom`, `start`, `end`, `strand`).

---
*Written note, copied from `tahoemap/vault_seed/notes/Readthrough spillover.md` by `tahoemap vault`. Edit it there, not here: this copy is replaced on every build.*
