---
type: concept
tags: [concept, method, statistics]
status: current
---

# Cross-fitting and circularity

> [!summary] In one line
> [[p53 program P]] was selected using the TP53 genotype labels, so any test of p53-specificity run on it is
> testing a hypothesis on the data that produced it — and this note is the list of which columns are infected
> and what was done about it.

## The problem, concretely

The programme was defined as "genes whose drug response differs between TP53-wild-type and TP53-altered
lines". Now ask: *is this programme's response wild-type-specific?* The answer is guaranteed to be yes,
because that is the selection rule. Any statistic built from programme membership and compared across TP53
genotype inherits that guarantee.

This is not a hypothetical failure mode. It is why the study reports a 3.07× wild-type/altered baseline
split for [[MDM2]] as a **measurement check** rather than as a finding, and why the fold-change columns in
every gene note carry a warning callout.

## Which columns are circular

| Circular — selected using TP53 labels | Not circular — never used them |
|---|---|
| programme membership (`in_P`, `in_P_down`, `arm`) | the MG53 screen slopes (`b_common`, `b_WT`, `b_alt`, `diff`) |
| `rank_in_P`, `z_program`, `q_up`, `q_down` | their standard errors, q values and placebo percentiles |
| `wt_mean_log2`, `wt_fold`, `wt_minus_alt_log2` | `median_line_cpm`, `n_lines_expressing`, `dog_class` |
| `frac_compounds_wt_up` and the mixedness flag derived from it | the per-gene detectable-effect bounds |
| the programme score `P_r2` used as an outcome | the readthrough geometry flags |

The practical rule: **circular columns describe, non-circular columns test.** A gene note may say "MDM2 is
rank 3 of the induction arm with a 1.255× fold change" as description. It may not say "therefore MDM2's
response is p53-specific".

## What was done about it

**Five-fold cross-fitting.** The programme is re-derived five times, each time leaving out a fifth of the
compounds, and `n_folds_kept` records how many of those five re-selected each gene. This does not cure
circularity with respect to the TP53 labels — the labels are used in every fold — but it does tell you
whether a gene's membership is a stable feature or a fit to a few compounds. It is frequently the latter: of
the 67 programme genes with an MG53 verdict, **20 were kept in 0 or 1 of the 5 folds**.

**Leave-one-compound-out stability.** `loco_frequency` repeats the selection 98 times, dropping one compound
each time. The induction arm averages 0.97, so most induction-arm membership is not driven by single
compounds. It is **not computed for the repression arm**, so those 15 genes read blank — a real gap, stated
wherever the repression arm is used.

**A label-free parallel programme.** The per-line p53 scoring is repeated on a programme and drug-dose set
selected *without* the TP53 labels (`lf_P_on_LFP50_*` in the per-line tables). Where the labelled and
label-free versions agree, the conclusion does not rest on the circular selection. For the per-line p53
function work they agree, which is why that note's conclusions stand; see [[Per-line p53 function]].

**A curated alternative.** The 21-gene p53-activity panel and the 29 canonical effectors are literature
sets, selected with no reference to this dataset at all. They are carried in parallel throughout precisely
so that a conclusion can be checked against a non-circular gene set. They are noisier and smaller; that is
the trade.

## The second circularity, which is easier to miss

Gene *reference families* can be selected too. The study's 4,642-gene downstream export looks like "all
genes", but **4,500 of them are in it because the screen had already called them significant against MG53**.
A percentile computed in that family is a rank inside a discovery set, not a position among genes in general
— and MG53-associated genes are over-represented in it by construction. This was published wrongly once and
corrected; see [[Placebo genes and reference families]] and [[Corrections and retractions]].

## Links

- [[p53 program P]] · [[Program P derivation]] · [[Placebo genes and reference families]]
- [[Nulls and calibration]] · [[How the numbers are decided]]
- [[Per-line p53 function]] — where the label-free repeat is used
