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

## Per-gene tables

`tables/p53_effectors_per_gene.csv` — **the focused per-gene table**: the 29 canonical p53 effectors (the
curated 21-gene panel plus the classic effectors it omits), each with its fold change under a strong
activator, its wild-type-minus-altered difference, and MG53's slope on it. Grouped by what each gene does
once p53 is active. Start here.

`tables/tableD_p53_target_genes_RAW.csv` — the full set: one row per gene in the data-defined p53 program (195: 180 up
arm, 15 down arm), joining the program columns to the MG53 screen columns. A plain extraction of pipeline
columns, no derived verdicts. Per gene it carries the p53-activation fold change (`wt_mean_log2`,
`p53_fold_WT`), the WT-minus-altered difference (`wt_minus_alt_log2`), how many of the 5 cross-fitted folds
keep the gene (`n_folds_kept`), and MG53's slope on that gene (`b_common`, `q_common`, `b_WT`, `b_alt`,
`diff`, `q_diff`, `q_label_diff`).

Read `wt_mean_log2` with care: it is averaged over a broad set of drug-doses, most of which do not activate
p53, so the median program gene reads only 1.06x. It is not the fold change under a strong p53 activator.

## Per-line p53 function

`PER_LINE_p53_FUNCTION.md` and `tables/per_line_p53_state.csv` — each of the 50 lines placed on a p53-output
axis against a null reference (the TP53-deletion and truncating lines), so a mutant can be read as retaining
activity, sitting at the null, or falling below it. Plus whether using that finer picture instead of the
yes/no genotype label changes what MG53's level does to p53. It does not.

Both a circularity-prone and a label-free version of each line's inducibility are given: program P and the
p53-activating drug-doses were selected using the TP53 labels, so `lf_P_on_LFP50_*` repeats the scoring on a
label-free program and drug-dose set. `ind_P_mean_frac_of_WT_gap` is the readable one: 1.0 means a line
reaches the wild-type median, 0.0 means it sits at the null.

| File | Contents |
|---|---|
| `tables/per_line_p53_state.csv` | 50 lines, 29 key columns: inducibility, distance from null with CI, the label-free repeat, panel responsiveness, literature-expected direction, GDSC Nutlin-3a AUC |
| `tables/per_line_p53_state_FULL.csv` | the same 50 lines with all 216 computed columns |
| `tables/tp53_mutation_annotation.csv` | per-variant annotation for the 33 mutant lines (41 rows): domain, hotspot, zygosity, reported transactivation class, dominant-negative and gain-of-function evidence |
| `tables/tp53db_variant_function.csv` | NCI/IARC TP53-database function reports per variant (25 rows) |
| `tables/wt_lines_annotation.csv` | the 17 genotype-WT lines: other routes that lower p53 (CDKN2A/ARF, MDM4, PPM1D, ATM, LKB1) |
| `tables/null_reference_lines.csv` | the lines used as the zero-p53-output anchor |

## The measurement: change in p53 activity per change in MG53, with a knockout-like control

`mg53_to_p53_effect.py` and `tables/mg53_to_p53_effect.csv`.

Tahoe has no engineered p53 knockout, but it has the next best thing: **10 lines whose only TP53 allele is
truncated, splice-disrupted or deleted outright** (KATO III is a whole-gene deletion). Those cannot mount a
p53 response, so any MG53 -> p53-activity slope measured in them is being produced by something other than
p53. That makes them the control arm. A second, softer control is the 21 mutant lines retaining <= 15% of
the wild-type-minus-null gap.

Headline, over all drug-doses: in the 11 lines with functional p53, a **doubling of MG53 changes p53 activity
by +0.095% (95% CI -0.11% to +0.30%)**. The knockout-controlled contrast (functional minus p53-null) is
+0.050% (-0.163 to +0.264). Both are indistinguishable from zero, and the arm could have detected 0.29%.

The control does not merely come out null — it comes out **as large or larger than the functional arm**.
Restricted to p53-activating drug-doses the p53-null control reads +0.225% (CI +0.007 to +0.443) while the
functional arm reads -0.123%, and the low-activity mutants read +0.430% (CI +0.048 to +0.814). A slope that
is biggest where there is no p53 to act on is not a p53-mediated effect; it is MG53 tracking overall
transcriptional response amplitude.

Not computable from a run's output alone: per-arm placebo-gene pseudo-controls (a matched gene put in MG53's
place inside each arm) need per-line values for arbitrary genes, which only `export/all_genes` on the full
data provides. `genome_wide/tables/c_placebos.csv` has 200 placebo exposures at the wild-type / altered split
only.
