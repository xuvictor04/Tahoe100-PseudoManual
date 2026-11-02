---
type: finding
tags: [finding, summary]
status: current
---

# What this study found

> [!summary] In one line
> In cell lines with working p53, more MG53 mRNA shows no detectable effect on p53's output, with the effect
> bounded below about a third of a percent per doubling — and what raises MG53 in this dataset is mostly
> transcription spilling into its locus from its neighbours, not any regulator of MG53.

Two questions, asked of [[Tahoe-100M]] and nothing else. Both are **regulatory**: upstream of MG53 means what
raises or lowers its expression; downstream means what its level does to p53 and p53's output.

## Downstream: what MG53's level does to p53

**Nothing detectable, and the bound is tight enough to be worth stating.** In the 11 lines with functional
p53, a doubling of measured MG53 changes the data-defined [[p53 program P]] by **+0.095%**
(95% CI −0.161% to +0.352%), against a study that could only have detected **+0.357%** at 80% power. Per
doubling of *true* MG53 — dividing by the wild-type exposure reliability of 0.301 — that is **+0.317%**
(−0.533% to +1.174%), with a detection limit of +1.194%. Nothing in those intervals is distinguishable from
zero under any inference method tried, including a whole-line permutation (p 0.387) and a restricted wild
cluster bootstrap (p 0.394).

**The control arm is what makes that a result rather than a shrug.** Ten lines have no intact TP53 allele —
truncating, splice-disrupted, or whole-gene deletion — so they cannot mount a p53 response, and any slope
measured in them is not p53-mediated. The arms are demonstrably competent to show a difference: under a
p53-activating drug-dose the programme moves **+12.54%** in the functional arm and **+1.31%** in the null
arm, and on the curated panel +24.57% against +0.21%. A p53-mediated MG53 effect of any appreciable size
would have shown up as a difference between them. The knockout-controlled contrast is **+0.050%**
(−0.194% to +0.295%). See [[The measurement with controls]].

**The raw positive correlation is drug identity.** Across drug-doses MG53 and p53 output correlate up to
r 0.495, which disappears under [[Two-way fixed effects]] — the drugs that raise MG53 are also drugs that
activate p53, and neither causes the other. What residual there is sits in the **altered** lines, not the
wild-type ones, which is the wrong arm for anything p53-mediated.

**Per gene, the association is as likely to point either way.** Signed into p53-output units, the 67
programme genes with a verdict split **35 toward more p53 output and 32 toward less**. A coherent change in
p53 output would land on one side; this lands on both. See [[Signing genes by p53 direction]] — and note
that the per-gene hit rate (27% of the programme) is exactly the genome-wide rate, so being a p53 target
confers no extra association with MG53. See [[FDR calibration and the inflated null]].

**No gene differs by TP53 status.** Zero of 195 programme genes, and zero of all 16,642 tested genes, reach
significance on the wild-type-minus-altered difference — on a statistic that, unlike the common slope, is
properly calibrated.

## Upstream: what moves MG53

**Its own genomic neighbourhood, more than any regulator.** TRIM72 sits 17 kb 3′ of [[FUS]] on the same
strand, and FUS runs ~47× higher. Transcription failing to terminate at FUS is counted as TRIM72 mRNA. The
evidence that this is really happening is strand-specific and solid; the arithmetic over-predicts the
observed rise by ~59%, so it is the leading account and not a closed case. See [[The TRIM72 locus]] and
[[Readthrough spillover]].

**The raiser list barely replicates.** Of 21 committed MG53 raisers, **two** survive a replication
requirement — idarubicin 5 µM and homoharringtonine 5 µM. Seventeen cannot be tested at all because the
design gives them one well. And the length of the list carries no information: run the same calling rule on
2,409 expression-matched genes and the median gene has 17 raisers, so MG53's 21 sits at the 67th percentile.

**The muscle programme is absent.** The factors that drive TRIM72 in striated muscle — MYOD1, MYOG, MEF2,
SRF — are silent or not expressed here. A muscle gene in non-muscle cells has no muscle regulator to
respond to. See [[Transcription factor activity inference]] and [[Upstream of MG53]].

## The honest limits

- **One time point, no perturbation, no protein.** Everything is 24 h mRNA association. Tahoe contains no
  MG53 knockdown or overexpression and no protein measurement, and most of MG53's known biology is
  post-translational. An absence here constrains the mRNA-level association in these cells; it does not rule
  out a protein-level link. See [[MG53 (TRIM72)]].
- **The effective sample is 11 to 17 lines**, not 50 and not 53,331 rows, because p53 is functionally
  disabled in about four fifths of the panel. See [[p53 nullification in cancer cell lines]].
- **MG53 is measured badly**: 5.89 CPM, 12.4% of profiles at zero, split-half reliability 0.289 to 0.705
  depending on subset, the largest plate batch gap of 16,656 genes, and two wells of the same exposure
  disagreeing by 21 percentage points at single-cell resolution. See [[Why MG53 is hard to measure here]].
- **Several published intervals were too narrow** and have been corrected, mostly by replacing an
  anti-conservative null or standard error. The ledger is [[Corrections and retractions]], and reading it is
  the fastest way to calibrate how much to trust the rest.

## Where to go next

| | |
|---|---|
| the measurement, with its control arms | [[The measurement with controls]] |
| what moves MG53 | [[Upstream of MG53]] |
| what MG53's level tracks | [[Downstream of MG53]] |
| the one gene that got its own write-up | [[MDM2 and MG53]] |
| how p53-dead each line is | [[Per-line p53 function]] |
| what was wrong and got fixed | [[Corrections and retractions]] |
| every gene | [[Genes — Map of Content]] |
| the actual CSVs | [[Tables — what the study produced]] |
