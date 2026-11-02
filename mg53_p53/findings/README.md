# Findings from the full Tahoe-100M run

Results written up from a completed `mg53_setup.sh --mode full` run. Nothing here reads Tahoe-100M itself;
everything comes from a run's output folder (`~/Tahoe-100M/mg53_p53` by default).

| File | What it holds |
|---|---|
| `MG53_p53_TABLES.md` | The three correlation tables: MG53 -> p53 targets in wild-type lines (A), what moves MG53 (B), and MG53 -> p53 split by how much p53 activity each mutant retains (C). Plus how far p53 is disabled across the panel. |
| `FINDINGS.md` | The long write-up: how the run reproduces the committed tables, upstream of MG53, downstream of MG53, how to read the 24 h snapshot, using the exported data, and what is left open. |
| `make_tables.py` | Regenerates every number in `MG53_p53_TABLES.md` into `tables/`. |
| `tables/*.csv` | The tables as CSV. |

Regenerate the tables on your own machine:

```
python3 mg53_p53/findings/make_tables.py --results ~/Tahoe-100M/mg53_p53
```

## Scope

Two questions, and only these two:

- **Upstream of MG53** — what raises or lowers MG53 expression: drugs, transcription factors, cell-line background.
- **Downstream of MG53** — what MG53's level does to p53 and to p53's output.

**Not in scope:** whether p53 regulates MG53 ("MG53 downstream of p53"). The repository's `p53_dependence`
step asks that question, so it is not drawn on here, and results that rested on it — including the
cardiac-glycoside lead — are not reported.

**A third thing, which is neither:** TRIM72 sits 10.6 kb 3' of PYCARD-AS1 and 17 kb 3' of FUS *on the same
strand*, so transcription running past those genes is counted as TRIM72 mRNA. This is called **readthrough
spillover**, never "downstream". It is a fact about position on the chromosome and about the measurement, and
it matters only because it means part of the measured MG53 signal is not MG53's own transcript.

## The short answer

- **Upstream:** MG53's expression tracks its own genomic neighbourhood far more than any transcription
  factor. Idarubicin and homoharringtonine at 5 uM raise it about 10-12x on two plates each; ponatinib and
  trametinib lower it. The muscle TFs that drive TRIM72 in its native tissue are silent or absent here.
- **Downstream:** in the TP53-wild-type lines, more MG53 shows no association with p53 target output or with
  p53-driven arrest. WT-specific effects above roughly 0.4-0.6% per doubling of measured MG53 (about 1.3-2%
  of true MG53) are excluded. The raw positive correlation is drug-driven and collapses once drug identity is
  controlled.
- **Caveat on all of it:** these are associations in 24 h mRNA. Tahoe has no MG53 perturbation and no protein
  data, every line carries wild-type MG53 at trace level, and p53 itself is functionally disabled in about
  four-fifths of the panel — so the effective sample for any MG53 -> p53 test is 11 to 17 lines.
