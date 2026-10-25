# MG53 (TRIM72): what is upstream of it, and does it act on p53? (Tahoe-100M, mRNA)

Scope: TRIM72 mRNA and p53-target mRNA, 24 h after each of 379 drugs at 3 doses, in 50 cancer cell lines (Tahoe-100M,
95.6M cells), with the repo's method-v3 corrections. Tahoe has no MG53 knockdown or overexpression and no protein data, so
every MG53-p53 relation here is an **association in mRNA**, never a causal or protein-level result. TRIM72 is low in these
lines (median line ~4 CPM; muscle is ~140 nTPM), and its untreated level is ~10x lower on plates 4-13 than on plates 1-3
and 14, which inflates fold changes on the low plates.

All tables: [SUMMARY.md](SUMMARY.md) (eight tables, T1-T8; CSVs in `summary/`). The literature evidence map, with every
citation: [literature/evidence_map.md](literature/evidence_map.md).

## Short answers

| Question | Answer | Basis | Strength |
|---|---|---|---|
| Is TRIM72 a p53 target gene? | No | Not in the p53-target census or near TP53 ChIP peaks; behaves like a non-target on 4 metrics in Tahoe (T5) | strong |
| Does TRIM72 induction need p53? | No | Rises in 31/31 TP53-altered lines under idarubicin 5 µM; selinexor activates p53 without raising TRIM72 (T5) | strong |
| Could a small p53 contribution exist? | Not excluded | WT lines lean +0.16 to +0.45 log2 across raisers, also for drugs that do not activate p53 (T5) | moderate |
| What raises TRIM72 mRNA? | Strong stress drugs | Anthracyclines/TOP2 poisons, harringtonines, auranofin, CDK9 and HDAC inhibitors; robust and replicated: idarubicin and homoharringtonine 5 µM (T1, T2) | moderate |
| What moves with it? | AP-1 / immediate-early, ATF3, PMAIP1 | Co-responders across drugs and in single cells, not shown regulators; muscle TFs (MyoD/MEF2, the known promoter TFs) are silent in these lines (T3) | moderate |
| Is it TRIM72's own promoter? | Unresolved | Part of TRIM72's reads look like readthrough from FUS (17-22 kb upstream, same strand); clean for homoharringtonine, not significant for idarubicin after level matching (T4) | moderate |
| Does more TRIM72 go with less p53 output? | No detectable association | Per line, across drugs, untreated and in single cells; only strong associations are excluded (17 WT lines) (T6, T7) | null, limited power |
| Does MG53 act on p53 protein? | Not testable here | Literature: MG53 binds p53 and drives its degradation (cardiomyocytes 2024, trophoblasts 2021); Tahoe has mRNA only and no MG53 perturbation | literature only |

## 1. What raises TRIM72 mRNA?

21 of 1,132 drug-doses raise TRIM72 (q < 0.1, >= 1.2x) and only ponatinib 5 µM lowers it. The table lists every change with
|z| >= 4 (T1 in SUMMARY.md has all 22). Only **idarubicin 5 µM and homoharringtonine 5 µM** are replicated on two plates
(and homoharringtonine also at 0.5 µM); the others are single wells, and mitoxantrone 5 µM does not replicate (plate 6 up,
plate 14 not).

| Drug | Dose (µM) | TRIM72 fold (corrected) | z | Fold without pseudocount | Wells | Plates | p53 activity z | Genes changed |
|---|---|---|---|---|---|---|---|---|
| Idarubicin | 5 | 12.2× | 15.9 | 6.0× | replicated (2 wells) | 6, 14 | 18.1 | 11,472 |
| Homoharringtonine | 5 | 10.3× | 14.8 | 5.4× | replicated (2 wells) | 6, 14 | 20.6 | 11,993 |
| Auranofin | 5 | 6.6× | 8.4 | 4.1× | single well | 12 | -7.8 | 8,581 |
| Homoharringtonine | 0.5 | 5.9× | 7.9 | 5.9× | single well | 5 | 17.4 | 10,075 |
| Dinaciclib | 5 | 5.6× | 7.4 | 3.7× | single well | 9 | 0.6 | 13,164 |
| Epirubicin | 5 | 4.5× | 6.5 | 4.8× | single well | 9 | 8.1 | 6,752 |
| Dinaciclib | 0.5 | 3.7× | 5.9 | 2.0× | single well | 8 | 1.6 | 12,822 |
| Dinaciclib | 0.05 | 3.8× | 5.5 | 2.5× | single well | 7 | 7.0 | 11,885 |
| Harringtonine | 5 | 3.6× | 5.5 | 3.2× | single well | 9 | 6.2 | 9,773 |
| Doxorubicin | 5 | 3.0× | 4.7 | 3.2× | single well | 9 | 10.0 | 7,317 |
| Mitoxantrone | 5 | 2.0× | 4.5 | 1.1× | not replicated (1/2 wells) | 6, 14 | 11.3 | 4,951 |
| Panobinostat | 5 | 2.7× | 4.4 | 2.5× | single well | 12 | 1.1 | 10,622 |
| Topotecan | 5 | 2.6× | 4.0 | 2.6× | single well | 9 | 18.3 | 8,958 |
| Ponatinib | 5 | 0.39× | -4.2 | 0.43× | single well | 12 | 3.9 | 3,510 |

- **Drug classes** (T2): anthracyclines / TOP2 poisons and the harringtonines have the highest activity-adjusted TRIM72
  response, but no class survives multiple testing (classes have 2-5 compounds, and plate layout confounds the strata:
  strong drugs on plates 1-3 rarely raise TRIM72). Several tyrosine-kinase inhibitors lean towards lowering it (moa class
  'Other TK inhibitor', q 0.010); trametinib lowers it in all 9 wells. Treat both as hypotheses.
- **Not specific**: the raisers move thousands of genes (idarubicin 5 µM: 11,472). TRIM72 ranks in the top 0.24% (idarubicin)
  to 8.6% (dinaciclib) of genes by fold change, inside programs of ~800-5,900 genes up >= 2x.
- **Fold sizes are inflated on low-baseline plates**: idarubicin 5 µM is 25.7x on plate 6 but 5.8x on plate 14 (12.9x and 4.0x
  without a pseudocount). Compare z or replicated wells, not folds across plates.

## 2. What moves with it, and is it TRIM72's own promoter?

- **Co-responders, not regulators** (T3): across drug-doses (activity and cell loss partialled out) TRIM72 tracks FOS 0.51,
  HEXIM1 0.47, JUN 0.47, heat shock 0.47, ATF3 0.44, PMAIP1 0.40; the 21-gene p53 score only 0.11 (and ~0 among the strongly
  active drug-doses). The known promoter regulators of TRIM72, MyoD/myogenin + MEF2 (muscle; literature), are not expressed
  or do not co-vary in these lines.
- **Readthrough from FUS is a real possibility.** TRIM72 lies 17 kb (Ensembl 116; 22.5 kb in Ensembl 110, the annotation
  Tahoe used) downstream of FUS, a highly expressed gene on the same strand. About half of TRIM72's top co-varying genes
  genome-wide sit in the same geometry (a low gene just downstream of a strong same-strand gene; 4% expected), and this is
  specific to that geometry (57 of the top 100 vs 7, 4 and 1 in the other neighbour geometries). Untreated, TRIM72's best
  partner across the 50 lines is PYCARD-AS1, the lncRNA between FUS and TRIM72 (rho 0.82, 13 of 13 plates), and TRIM72's
  plate batch is shared with readthrough-exposed genes.
- **For idarubicin specifically, unresolved.** The same-strand neighbours rise with TRIM72, but once each gene is compared with
  genes of its own expression level the strand contrast is not significant for idarubicin (p 0.17-0.27); it is for
  homoharringtonine (p 0.04). Idarubicin does not raise readthrough-exposed genes more than other low genes on average, and
  dinaciclib raises TRIM72 without the locus pattern. Tahoe's 3' gene counts cannot separate readthrough from promoter
  activity: that needs read coverage across the FUS-TRIM72 interval, nascent RNA, or a **qPCR assay that spans a TRIM72
  exon-exon junction** (spliced TRIM72 mRNA) next to one placed in the FUS-TRIM72 intergenic region.

| Gene | Strand | Position vs TRIM72 | Distance (kb) | Median line CPM | Idarubicin 5 µM | Homoharringtonine 5 µM | Dinaciclib 5 µM | r with TRIM72 across drug-doses |
|---|---|---|---|---|---|---|---|---|
| BCKDK | + | upstream (5') | 100.6 | 10.3 | 0.40× | 0.31× | 1.9× | -0.32 |
| KAT8 | + | upstream (5') | 82.6 | 19.3 | 1.0× | 0.79× | 1.3× | 0.09 |
| FUS | + | upstream (5') | 17.1 | 259.2 | 1.7× | 2.2× | 1.1× | 0.63 |
| PYCARD-AS1 | + | upstream (5') | 10.6 | 1.2 | 5.7× | 6.1× | 2.5× | 0.72 |
| PYCARD | − | upstream (5') | 10.6 | 0.6 | 0.55× | 0.37× | 2.2× | -0.10 |
| TRIM72 | + | overlapping | 0.0 | 4.1 | 12.2× | 10.3× | 5.6× | 1.00 |
| PYDC1 | − | overlapping | 0.0 | 0.0 | – | – | – | – |
| ITGAM | + | downstream (3') | 28.4 | 0.8 | 6.0× | 35.7× | 2.7× | 0.53 |
| ITGAX | + | downstream (3') | 123.6 | 0.9 | 0.66× | 1.4× | 1.4× | 0.06 |

## 3. Is the induction p53-dependent?

**No requirement, not sufficient, not a p53 target.** Under idarubicin 5 µM, TRIM72 rises 12.0x in TP53 wild-type and 12.1x in
TP53-altered lines of the same wells (31 of 31 altered lines up, including likely-null truncating lines), while MDM2 and the
p53 score in those wells are strongly wild-type-selective. Selinexor activates p53 as strongly and as wild-type-selectively
without raising TRIM72. TRIM72 is not in the p53-target census or near TP53 ChIP peaks (2 of 393 experiments vs CDKN1A 261),
and in Tahoe it behaves like a non-target on four metrics.

TRIM72 induction in TP53 wild-type vs altered lines in the same wells, with p53 targets as positive controls.

| Drug | Dose (µM) | TRIM72 WT lines | TRIM72 altered lines | TRIM72 WT − altered (log2) | 95% CI | p | Altered lines up | MDM2 WT − altered (log2), p | P53 score WT − altered (log2), p |
|---|---|---|---|---|---|---|---|---|---|
| Idarubicin | 5 | 12.0× | 12.1× | -0.02 | -0.60 to 0.93 | 0.89 | 100% | 1.10, 1e-04 | 0.67, 1e-04 |
| Idarubicin | 0.5 | 2.5× | 1.9× | 0.38 | -0.13 to 0.72 | 0.16 | 23% | 2.02, 1e-04 | 1.53, 1e-04 |
| Idarubicin | 0.05 | 1.7× | 2.0× | -0.21 | -0.43 to 0.47 | 0.64 | 20% | 1.07, 1e-04 | 0.78, 1e-04 |
| Homoharringtonine | 5 | 11.7× | 9.3× | 0.33 | -1.23 to 1.45 | 0.59 | 97% | 0.28, 0.43 | -0.23, 0.17 |
| Homoharringtonine | 0.5 | 8.5× | 4.8× | 0.85 | -0.07 to 2.36 | 0.066 | 73% | 0.80, 0.004 | 0.56, 4e-04 |
| Auranofin | 5 | 9.9× | 6.4× | 0.63 | -1.31 to 1.57 | 0.56 | 77% | -1.18, 1e-04 | -0.82, 1e-04 |
| Dinaciclib | 5 | 5.7× | 5.6× | 0.04 | -0.54 to 1.00 | 0.83 | 70% | -1.19, 1e-04 | -0.68, 1e-04 |
| Epirubicin | 5 | 9.8× | 3.8× | 1.35 | 0.74 to 1.77 | 0.020 | 69% | 0.30, 0.003 | 0.50, 1e-04 |
| Doxorubicin | 5 | 4.6× | 2.7× | 0.76 | 0.06 to 1.65 | 0.066 | 47% | 0.63, 1e-04 | 0.72, 1e-04 |
| Topotecan | 5 | 2.7× | 2.4× | 0.19 | -0.21 to 1.41 | 0.37 | 38% | 0.37, 3e-04 | 0.86, 1e-04 |
| Mitoxantrone | 5 | 2.2× | 1.8× | 0.28 | -0.34 to 0.88 | 0.37 | 20% | 1.02, 1e-04 | 0.71, 1e-04 |
| Selinexor | 5 | 0.78× | 0.84× | -0.11 | -0.80 to 0.37 | 0.65 | 0% | 1.19, 1e-04 | 0.72, 1e-04 |
| Selinexor | 0.5 | 1.0× | 1.0× | 0.05 | -0.97 to 0.58 | 0.90 | 3% | 0.91, 1e-04 | 0.56, 1e-04 |

**Not excluded**: a modest wild-type lean across the raisers (+0.16 to +0.45 log2, clearest for epirubicin 9.8x vs 3.8x). It
also appears for drugs that do not activate p53 (auranofin, homoharringtonine), so it may be line background rather than
p53; the test cannot exclude a contribution the size of an average p53 target's (80% power needs ~0.9 log2).

## 4. Does more TRIM72 go with less (or more) p53 output?

**No detectable association, in any of four designs** (T7): per line in the same wells (idarubicin 5 µM and 13 raisers pooled),
untreated across lines, across all drug-doses, and in single cells (cells with detected TRIM72 vs not, adjusted for depth and
cell cycle). What does co-vary with TRIM72 in single cells is ATF3 and PMAIP1, in both TP53 groups: a shared stress state.

| Test | Lines / cells | Estimate | p | n |
|---|---|---|---|---|
| Idarubicin 5 µM, per line: TRIM72 induction vs p53-score induction (drug response and cell loss out) | TP53-WT | rho -0.22 | 0.40 | 17 lines |
| Idarubicin 5 µM, per line: TRIM72 induction vs p53-score induction (drug response and cell loss out) | TP53-altered | rho -0.28 | 0.13 | 30 lines |
| 13 TRIM72 raisers pooled, per line: TRIM72 vs P53 score (drug response and cell loss out) | TP53-WT | mean rho -0.08 | 0.40 | 13 drug-doses |
| 13 TRIM72 raisers pooled, per line: TRIM72 vs P53 score (drug response and cell loss out) | TP53-altered | mean rho 0.04 | 0.53 | 13 drug-doses |
| Untreated, per line (within plates): TRIM72 level vs basal p53 activity | TP53-WT | rho -0.19 | 0.48 | 17 lines |
| Untreated, per line (within plates): TRIM72 level vs TP53 mRNA | TP53-WT | rho -0.45 | 0.071 | 17 lines |
| Untreated, per line (within plates): TRIM72 level vs basal p53 activity | TP53-altered | rho -0.16 | 0.38 | 31 lines |
| Untreated, per line (within plates): TRIM72 level vs TP53 mRNA | TP53-altered | rho 0.24 | 0.22 | 28 lines |
| Across all drug-doses: TRIM72 z vs P53_ACTIVITY z (activity out) | all lines pooled | rho 0.12 (CI 0.05 to 0.19) | 5e-05 | 1132 drug-doses |
| Across all drug-doses: TRIM72 z vs p53_WT_minus_altered z (activity out) | all lines pooled | rho 0.03 (CI -0.04 to 0.09) | 0.35 | 1132 drug-doses |
| Single cells, idarubicin 5 µM: P53 score counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-WT | rate ratio 1.020 | 0.30 | 16 lines |
| Single cells, idarubicin 5 µM: ATF3 counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-WT | rate ratio 1.117 | 0.006 | 15 lines |
| Single cells, idarubicin 5 µM: P53 score counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-altered | rate ratio 0.983 | 0.29 | 30 lines |
| Single cells, idarubicin 5 µM: ATF3 counts in TRIM72-detected vs undetected cells (depth, cycle out) | TP53-altered | rate ratio 1.195 | 1e-10 | 30 lines |

Power is limited: only strong associations (|rho| > ~0.5 in the 17 wild-type lines) are excluded, and the single-cell test
excludes more than ~7% change in p53-target counts per doubling of a cell's TRIM72. In untreated wild-type lines the point
estimates lean negative (basal p53 -0.19, TP53 mRNA -0.45, not significant), the direction an MG53-degrades-p53 mechanism
would predict.

**The literature** describes the link at the protein level: MG53 binds p53 and promotes its ubiquitination and degradation
(Jiang et al. 2024, cardiomyocytes and doxorubicin cardiotoxicity, reported MDM2-independent; Li et al. 2021, trophoblasts),
while a lung study found no direct binding and an indirect, membrane-repair route (Cong et al. 2020). Mechanisms of other TRIMs
(TRIM24, 25, 28, 32, 39, 59, 65) should not be carried over to MG53. Testing the protein link needs MG53 perturbation with p53
protein read-outs, ideally in cardiomyocytes, where MG53 is expressed (in rodents; it is scant in human heart).

## Running it on your system

Needs the computed atlas (`tahoe_atlas.py compute`, keeping `atlas/pseudobulk`) and gene panel (`tahoe_gene_panel.py all`) in
your Tahoe-100M folder; the 340 GB of cells are not read again, and nothing is written into `atlas/` or `gene_panel/`.

```bash
python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M            # ~45 min; tables in ~/Tahoe-100M/mg53_p53/
python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps summary      # rebuild SUMMARY.md only
python3 mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps literature   # optional; needs internet
```

Steps: `perturbations`, `coregulation` (one pass over `atlas/pseudobulk`, ~25 min the first time; downloads a TF list, HGNC and
Ensembl coordinates once), `p53_dependence`, `downstream`, `summary`. Each step's tables go to `<out>/<step folder>/tables`,
then `summary_tables.py` writes `<out>/SUMMARY.md` and `<out>/summary/*.csv`. The log is `<out>/run_mg53_p53.log`.
Reproducibility: a from-scratch run of `run_mg53_p53.py` into an empty folder reproduced all 26
`upstream_perturbations` tables exactly (the other steps are being checked the same way).

| Folder / file | What it holds |
|---|---|
| `run_mg53_p53.py` | Runs the steps below on a Tahoe-100M folder, then `summary_tables.py`. |
| `summary_tables.py`, `SUMMARY.md`, `summary/` | The eight summary tables (T1-T8) built from the step tables. |
| `upstream_perturbations/` | `trim72_upstream_landscape.py`: TRIM72 by drug-dose, plate batch, classes, specificity, programs. |
| `upstream_coregulation/` | `upstream_coregulation.py`: genome-wide co-regulation, untreated partners, the FUS-TRIM72 locus. |
| `p53_dependence/` | `p53_dependence.py`: TP53 wild-type vs altered induction, selinexor, target-likeness. |
| `downstream_p53/` | `downstream_p53.py`: TRIM72 vs p53 output per line, untreated, across drugs, single cells. |
| `literature/` | `evidence_map.md` plus the PubMed / Europe PMC / p53-census / ChIP-Atlas checks that back it. |
| `*/verify/` | The adversarial verifiers' independent scripts and outputs for each workstream (this run's paths). |

## How it was checked

Five workstreams (literature; drug landscape; co-regulation; p53 dependence; downstream p53) each produced findings with
scripts, and an independent verifier per workstream recomputed the key numbers with its own code and tried to break each
claim. Everything above uses the verifiers' corrected wording. What they changed: mitoxantrone dropped from the robust
raisers; class enrichments marked fragile (plate-layout confound); 'equal in WT and altered lines' softened to 'no
requirement, modest WT lean not excluded'; the readthrough claim narrowed (clean for homoharringtonine, unresolved for
idarubicin; Ensembl 110 vs 116 distance); the downstream nulls marked low-power, with the negative-leaning untreated point
estimates reported. The literature citations were all confirmed against the sources.

Limits: mRNA only, one time point, cancer lines without a muscle program; TP53 status from the annotation (17 WT / 33
altered); most drug-doses are single wells; TRIM72 counts are low (~5 per well x line profile).
