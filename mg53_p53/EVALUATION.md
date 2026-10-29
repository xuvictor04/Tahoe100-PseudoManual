# Evaluation of Tahoe100-PseudoManual (`mg53_p53/`, `trim72_idarubicin/`)

**Goal evaluated:** use Tahoe-100M to find upstream effectors of MG53/TRIM72 and the downstream effects of TRIM72 (mainly on p53
output, but also broadly), reading the data as 24 h mRNA.

**Criteria applied.**
1. **Tahoe only.** The project builds and extracts from the Tahoe-100M database; no wet-lab experiments will be run. Limits of
   Tahoe's gene-level 24 h counts are stated as limits, not as experiments to run.
2. **Genome-wide at the base.** Analyses should be genome-wide (all genes, all drugs, all lines) and data-driven at their base.
   Curated gene, pathway, regulon or drug-class lists may set priorities or annotate results. They should not define what is tested
   (the search space), what the outcome is, or which hypotheses are asked, because that preloads the answer with assumptions.
3. The data compilation is done on a separate computer. This evaluation reads the repo's code and committed tables. Its one
   real-data check (below) used a pre-chosen gene subset and is scoped accordingly.

## Bottom line

**Under these criteria the repo meets the goal on the upstream side where it uses its genome-wide base (what raises TRIM72, the
locus, line traits), but not for "what moves with it" or "which TFs", and not yet on the downstream side.**

- **Upstream** rests mostly on genome-wide, data-driven analyses:
  - all 1,132 drug-doses are ranked;
  - all 16.6k expressed genes are scanned for co-variation across drugs;
  - all 46,775 genes are scanned across untreated lines;
  - readthrough geometry is analysed for every gene.

  Its strongest answers come from this base: the replicated raisers, the readthrough signal at the FUS-TRIM72 locus, and that the
  locus (not TP53) sets the untreated level. Two of its five short answers are list-defined, however: "what moves with TRIM72" and
  "which transcription factors track it".
- **Downstream** is list-defined at its base:
  - every p53 test uses the literature 21-gene p53 score (or named targets) as its outcome;
  - "broad downstream" is 27 pre-chosen read-outs: mostly MG53-literature pathways, plus 7 curated E2F targets and ATF3/DDIT3/PMAIP1
    picked from the repo's own co-responders;
  - the single-cell store holds only 116 hand-picked genes.

  No genome-wide, TP53-genotype-controlled downstream screen exists, although the repo's own genome-wide pseudobulk would support one
  without re-reading cells. The downstream nulls are therefore valid only for the lists tested.
- **Conclusions with TRIM72 itself as the outcome are list-free and stand.** TRIM72 induction does not need p53 (it rises in 31 of 31
  TP53-altered lines under idarubicin 5 µM), though a partial p53 contribution is not excluded.
- **Within its lists the work is careful and reproducible.** The p53 nulls reproduce on Tahoe's own DESeq2 quantification of the same
  wells (for 141 pre-chosen genes). The remaining problems are interpretive and are listed below.

| Part of the goal | Basis | Grade |
|---|---|---|
| Upstream: what raises / lowers TRIM72 mRNA | Data-driven (all drug-doses) | **Adequate.** Replicated raisers right; rise is readthrough-compatible; class claims and lowerers need correcting. |
| Upstream: locus / readthrough, line traits | Genome-wide for the locus and readthrough geometry; the trait scan is mixed (679 of 725 tests are curated regulon activities) | **Good basis, under-read.** The best-founded analyses in the repo, but the README understates the readthrough share and T1 has no readthrough column (Major 3). |
| Upstream: what moves with TRIM72, which TFs | List-defined (30 of 34 T3 rows; curated regulons) | **Not met by criterion 2.** The genome-wide tables give a different lead (readthrough-geometry genes; AP-1/IEG only in the top 1%). |
| Downstream: TRIM72 → p53 output | Outcome = curated 21-gene p53 score | **Strong for that score; not established genome-wide.** No data-derived p53 program; no genome-wide genotype-controlled screen. |
| Downstream broadly | List-defined (27 pre-chosen read-outs, mostly MG53 literature); D2 unreported | **Not met.** |
| Reading it as 24 h mRNA | — | **Adequate.** Cell loss and ambient RNA handled; readthrough raised but its share understated (Major 3); stabilisation, superinduction and composition flagged in T1 but not named as alternatives to induction for the shutdown drugs. |
| Reproducibility / engineering | — | **Adequate.** Summary layer rebuilds exactly; no test covers `mg53_p53`; the comparison tool cannot fail. |

## How this was checked

1. **Workstream audit.** 12 auditors read the code and recomputed numbers from the committed tables, producing 73 issues.
2. **Adversarial verification.** Each issue was verified against the code and tables. Of the 21 issues rated "major", 5 stayed major
   and 16 were downgraded to minor; none was refuted. Across all 73 issues, 38 were confirmed, 34 partially confirmed (narrowed) and
   1 (a note) refuted.
3. **Independent quantification.** Tahoe's published pseudobulk DESeq2 table (drug vs plate DMSO, per gene × line × drug × dose ×
   plate) was read for all 379 drugs and 50 lines, but **only for 141 pre-chosen genes**. Each of five analyses had a skeptic re-check.
   - Statements about TRIM72 itself are unaffected by the gene restriction.
   - Statements about other genes (p53 targets, pathways, selectivity) speak only to those 141.
   - This compilation step is now left to the separate build computer.
4. **List-dependence audit.** Five audits (data products, upstream, downstream, a list-free reading of the committed genome-wide
   tables, and the previous version of this evaluation) each had a verifier. They classified every analysis by whether a list defines its search space,
   outcome or hypotheses.

## Where the repo rests on lists, and where it is genome-wide

**What the build makes:**
- `atlas/pseudobulk`: every gene, per well × line, about 20 GB, no gene filter (`tahoe_atlas.py:486-488, 586`).
- `atlas/effects`: 16,643 expressed genes, but only per well and per drug-dose; the median over lines (`tahoe_atlas.py:960`).
- `gene_panel/cells` and `well_line`: the only per-cell store. It holds **116 hard-coded genes** plus 3 modules: 39 panel genes
  (`tahoe_gene_panel.py:85-128`, "the user's list"), 4 MTAP anchors and 73 curated context genes (`:144-152`). All other genes are
  dropped at extraction (`tahoe_mtap_gankyrin.py:386-416`).
- Tahoe's own genome-wide DESeq2 table ships with the download but is never read by the pipeline.

**Short answers and their basis:**

| Short answer | Basis | Where the list enters |
|---|---|---|
| What raises TRIM72 | All 1,132 drug-doses ranked (data-driven) | Class labels in T2 are 37 author-curated classes (`summary_tables.py:84`). In the repo's own table, Tahoe's MoA annotation gives a TOP2/DNA-damage lean (p 0.012, no FDR survivor) and no CDK or HDAC support (p 0.60, 0.74). A plate-controlled scan of Tahoe's DESeq2 also finds DNA synthesis/repair, protein-synthesis and CDK-inhibitor classes leaning up (q 0.01-0.02), but not HDAC inhibitors. |
| Is it TRIM72's own promoter (readthrough) | Genome-wide co-variation and DoG geometry | — |
| Which line traits predict it | Genome-wide untreated scan (PYCARD-AS1 #1 of 46,775); all annotated drivers | 679 of 725 trait tests are curated regulon activities |
| What moves with it (AP-1/IEG, ATF3, PMAIP1) | **30 of T3's 34 rows are pre-chosen** (`trim72_upstream_landscape.py:862-868`; the other 4 are a level control and 3 QC metrics); single-cell leg uses panel genes picked from the same table | Defines the hypotheses |
| Which TFs track it | **CollecTRI regulons** (curated targets); 16 hand-picked TFs shown in T11; hand-made IEG adjustment list | Defines the exposure |
| Not a p53 target / induction does not need p53 | TRIM72 is the outcome, TP53 genotype the modifier (data-driven) | "p53 activator" drug-doses (e.g. selinexor) are picked by the 21-gene score; target-likeness is measured against that score inside the 116-gene panel |
| No association of TRIM72 with p53 output (T7, T9, T10) | **Outcome = 21-gene P53_ACTIVITY** (`tahoe_gene_panel.py:156-157`); nulls from 78 curated panel genes; single cells confined to panel genes | Defines the outcome, the reference and the search space |
| Broad downstream (two_way D2; single-cell NF-κB/ferroptosis) | **27 pre-chosen read-outs**, mostly MG53 literature, plus 7 curated E2F targets and 3 of the repo's own co-responders (`two_way.py:113-123`, `gene_modules.csv`); 3-gene single-cell scores | Defines the hypotheses. D2 unreported; single-cell rows shown in T10 without interpretation |

**Also list-defined, and less visible:**
- The "functional p53" line status and the "p53 activator" drug classes are defined by the 21-gene score
  (`tahoe_gene_panel.py:1219-1286`). They are then used as exposures or strata.
- A curated DNA-damage drug list stratifies p53_dependence and downstream_p53.
- The S/G2M (Tirosh 2016) modules and a panel-based responsiveness term (`bg_abs_r2`) are covariates in the primary two_way model
  (`two_way.py:126`). The S/G2M and proteasome modules are also partialled in the 'covariates' variant of the co-regulation and TF
  analyses. These are adjustments, which criterion 2 tolerates, but they are lists.

**The list choice can change the reading, by the repo's own tables:**
- Against the panel's own competitive null, the primary p53-score slope sits at the 1.8th percentile of 500 background modules
  (p_emp 0.04). The correlation-aware test gives p 0.31, so this is not a hidden effect. It shows the reference set matters, and a
  genome-wide reference is needed.
- With a different curated p53 list (the CollecTRI TP53 regulon, 835 targets), TRIM72 has a significant within-line negative
  association (r −0.060, q 0.005). It is present in both genotypes, if anything weaker in WT, so it is not routed through p53. The
  README prints it but never connects it to the "no association with p53 output" answer.

## What the committed genome-wide tables show when read without lists

These tables come from the repo's own genome-wide or all-drug-dose analyses; only the reading is new. Apart from the TRIM72
WT-vs-altered screen (last bullet), they are not genotype-split.

- **TRIM72's strongest partners are defined by genomic geometry, not by a pathway.** Across 1,086 drug-doses, 41-51% of its top 100
  partners are low-expressed genes just downstream of a strongly expressed same-strand gene. The genome-wide rate is 4.2%. The same
  axis runs through:
  - the untreated plate batch (TRIM72 #1 of 16,656 genes);
  - untreated line-to-line variation (PYCARD-AS1 #1 of 46,775);
  - drug response (TRIM72 vs the genome-wide readthrough index: rho 0.45).

  The upstream genes of these partners also co-vary with TRIM72 (median r 0.27 vs 0.12 genome-wide). So the data do not separate
  readthrough from co-regulation of the whole same-strand neighbourhood.
- **The repo's lists reproduce only the secondary part of "what moves".** The union of all 20 repo list definitions supplies 0 of
  TRIM72's top 50 partners.
  - On T3's own metric, FOSB ranks 18, FOS 53, HEXIM1 93 and JUN 102 of 16,643: real, but top-1% rather than top.
  - ATF3 and PMAIP1, named in the short answer, are outside the top ~118.
  - Among TF mRNAs, which is the list-free TF read-out, FOSB, FOS and ATF3 lead and ATF4 does not track TRIM72.
  - MEF2A/C/D are expressed but do not co-vary positively; MyoD/MYOG/MYF5/MYF6 are not expressed.
- **The raisers split by the data-defined readthrough index.** 8 of 21 raisers are genome-wide readthrough inducers, among them
  homoharringtonine, auranofin, panobinostat and the weak adagrasib, filgotinib and TAK-901. Idarubicin 5 and 0.5 µM,
  harringtonine, ouabain and dinaciclib raise TRIM72 without global readthrough. Idarubicin 5 µM is about zero on the level-matched
  log2 index and negative only by z; idarubicin 0.05 µM is one of the 8 inducers. Both groups show the same same-strand PYCARD-AS1
  co-rise at the FUS-TRIM72 locus, so the split concerns global readthrough, not the locus. The curated classes do not show it.
- **No genome-wide table points to TRIM72 going with less p53-target mRNA.** MDM2 and CDKN1A are mid-ranked partners, and TRIM72 sits
  at the 55th percentile of all genes for correlation with the curated 21-gene p53 score (the genes are genome-wide; the axis is a
  list). One p53-responsive lncRNA outside every repo list,
  TP53TG1, is a strong negative partner in one adjustment variant only. That is not robust, but it is the kind of gene a list-free
  screen would surface.
- **A genotype-dependent lead that the repo selected but never reported: cardiac glycosides.** The repo's all-drug-dose TRIM72
  WT-vs-altered screen gives:
  - ouabain 5 µM +1.65 log2 (line-permutation p 0.006, FDR 0.27);
  - digitoxin 0.5 µM +1.29 log2 (p 0.004);
  - 5 of 6 glycoside drug-doses leaning the same way.

  These are single wells with 2-16 TRIM72 counts per profile. For ouabain the 21-gene p53 score is also WT-selective and tracks
  TRIM72 within the well (rho 0.43), so a p53 link is ambiguous. It is a lead only.

## What holds up (with scope stated)

- **TRIM72 induction does not need p53.**
  - TRIM72 is the outcome here, so this test is list-free.
  - Under idarubicin 5 µM TRIM72 rises in 31/31 TP53-altered lines in the repo, and 33/33 in Tahoe's DESeq2 (WT − altered −0.18 log2,
    CI −1.22 to 0.60).
  - A modest WT lean across raisers (+0.3 to +0.5 log2 pooled, nominal p 0.01-0.04) means a partial p53 contribution is not excluded,
    as the repo says, though it mis-cites the numbers. The lean is as large or larger in raisers that do not activate p53 (+0.33 to
    +0.49 vs −0.08), which points to line background.
  - The literature (Fischer 2017 census; 2 of 393 ChIP-Atlas sets) is supporting annotation.
- **No TP53-WT-specific association between TRIM72 and the curated 21-gene p53 score.**
  - Repo: −0.0032 (CI −0.0085 to 0.0022).
  - Tahoe's DESeq2 (12 curated targets): WT − altered +0.0020 (CI −0.0078 to +0.0117), permutation p 0.73.
  - The repo's −0.030 in drug-doses selected partly by that same score is post hoc (smallest Holm p 0.106). Whether it replicates
    depends on the specification. On Tahoe's DESeq2 it is −0.029 (p 0.006) in an unweighted fit without covariates, but −0.004 to
    +0.044 in IVW-weighted fits on the repo's 62 drug-doses. It falls to about −0.01 to −0.02 when line effects use all drug-doses.
  - Valid for these curated targets; not a genome-wide statement.
- **The TP53 labels (17 WT / 33 altered) are correct.**
- **Idarubicin and homoharringtonine 5 µM are replicated raisers** (both plates; 45-47 of 47 lines in DESeq2). All 21 repo raisers
  point the same way in DESeq2.
- **The locus sets the untreated level.** PYCARD-AS1 is #1 of 46,775 genes (genome-wide, list-free); TP53 status shows no detectable
  effect (rho 0.07; underpowered).
  - KMT2D, the only hit among all Tahoe-annotated drivers altered in enough lines, replicates in DESeq2 (+1.5 log2, q 0.02 of 30).
  - Half of it goes with PYCARD-AS1, and the mutant lines are hypermutated, so it remains a lead.
- **Internal consistency is excellent**, and the verdict that Tahoe cannot test MG53 → p53 causally is right, though one stated reason
  is not (see Wording).

## The 24 h reading, raiser by raiser

| Raiser | What a 24 h mRNA snapshot shows |
|---|---|
| Idarubicin 5 µM (replicated) | PYCARD-AS1, the same-strand RNA between FUS and TRIM72, rises with TRIM72; opposite-strand PYCARD does not. If TRIM72 follows PYCARD-AS1 at its untreated ratio, that rise covers about half (plate 6) to all (plate 14) of TRIM72's added counts. Idarubicin is not a genome-wide readthrough inducer. Curated long-lived p53 targets rise WT-selectively, while the short-lived MDM2/CDKN1A are blunted. |
| Homoharringtonine 5 / 0.5 µM | Same near-locus signature, extending into ITGAM. A genome-wide readthrough inducer. Translation block gives a superinduction/stabilisation-like profile (FOS +3.0, JUN +3.6 log2 in Tahoe's DESeq2). |
| Epirubicin, doxorubicin 5 µM (single wells, low-count plate 9) | Partly locus-coupled; largest WT lean. |
| Auranofin 5 µM | Locus co-rise; a genome-wide readthrough inducer; curated p53 targets fall in WT lines. |
| Dinaciclib, all doses | The z and fold come mostly from the pseudocount floor (a no-change simulation reproduces 66-83%). A real 1.8-4.3x rise remains, but it is a generic low-gene rise in heavily cell-depleted wells, with no strand pattern. |
| Not raisers | AT7519 (globally near-inactive), plicamycin, 4EGI-1, MNK inhibitors. Shutdown alone is not sufficient. |

## What needs correcting

### Major
1. **Downstream answers are defined by lists, and stated as if general.** "No detectable association with p53 output" means "with the
   21-gene literature score and named targets". "Broad downstream" was asked only of 27 pre-chosen read-outs (mostly MG53 literature),
   and the D2 results are not reported. The repo should say so until a genome-wide, genotype-controlled screen exists (see the last section).
2. **"What moves with it" and "which TFs track it" are list-framed.**
   - The genome-wide base the repo already computed puts readthrough-geometry genes first and AP-1/IEG in the top 1%.
   - The TF answer rests on regulon scores. The ISR association (ATF4/ATF5/XBP1) comes from weakly active drug-doses, and ATF4 mRNA
     does not track TRIM72.
   - "Muscle TFs silent" is wrong for MEF2A/C/D, which are expressed (though they do not co-vary).
3. **The drug "induction" of TRIM72 is largely readthrough-compatible, and this is understated.**
   - Idarubicin and homoharringtonine show the same near-locus signature. The README's "clean for homoharringtonine, not significant
     for idarubicin" comes from a strand test dominated by genes 150-280 kb away.
   - The FUS distal-3' feature ENSG00000260060 rises more than FUS but was dropped from T4 by the Ensembl 116 coordinates.
   - T1 has no readthrough column.
   - Consequence: the upstream list names effectors of transcription in the FUS-TRIM72 neighbourhood, not demonstrated regulators of
     MG53 expression.
4. **"CDK9 and HDAC inhibitors raise TRIM72" generalises from one compound each.** Dinaciclib's significance comes mostly from the
   pseudocount floor; only panobinostat of three HDAC inhibitors raises TRIM72.

### Notable
- **Lowerers.**
  - The short answers have no lowering row. README section 1 names only ponatinib 5 µM, which is not significant in DESeq2
    (z −1.9, q 0.70).
  - Trametinib (lower in 9/9 wells) and the "Other TK inhibitor" class (q 0.010) appear only as hypotheses.
  - Radotinib 5 µM, the only lowerer replicated on two plates (0.48x in DESeq2; repo 0.65x, z −2.8), is never named as a lowerer; it
    appears only in T2's class member lists. It changes 824 genes genome-wide, so TRIM72-selectivity is not established.
- **Effect-size bounds (for the curated p53 score).**
  - "Up to ~0.03 per doubling" is 0.03 log2 (about 2%) and is the optimistic end.
  - With replicate-well reliability it is about 0.08 log2 (~5%) on the repo's data and 3.6-5.1% on Tahoe's DESeq2. That reliability
    is carried by the strongly replicated idarubicin/homoharringtonine wells (replicate r 0.47/0.39). In a typical drug-dose TRIM72's
    line deviations do not replicate, so the data constrain little there.
  - The single-cell ">1.2% per doubling excluded" depends on the overdispersion model and on a 0/1 detection exposure.
- **The plates 1-3 drug set was screened at about half sensitivity.** PF-06260933, HI-TOPK-032, abemaciclib and ERK5-IN-2 at 5 µM are
  unresolved candidates.
- **The cardiac-glycoside WT lean (above) is unreported.**

### Minor
- **24 h kinetics.**
  - Stabilisation, superinduction and composition are not named as alternatives for the translation- and transcription-blocking
    raisers.
  - The README wrongly says the genotype contrast cancels transcription shutdown.
  - Wells should be excluded from p53-output tests only on list-free evidence: severe cell loss, or a genome-wide
    transcription-collapse signature. Results should be reported with and without them. A mechanism label is not list-free evidence,
    and a 4-gene labile index would also flag idarubicin and epirubicin.
- **Wording.**
  - "Compare z, not folds, across plates": z carries the full plate amplification.
  - "No detectable association in any of four designs": the across-drug rho is 0.12, p 5e-5, a stress co-induction.
  - The untreated "negative lean" is illustrated with TP53 mRNA (−0.45), which a degradation mechanism would not lower. Of the valid
    read-outs only basal p53 activity leans (−0.19); MDM2, CDKN1A and responsiveness do not, and all 72 tests have q ≈ 0.99.
  - "+0.16 to +0.45 log2" cannot be traced to T5.
  - "TRIM72 only changes with drugs that act on p53" is contradicted by T1.
- **`trim72_idarubicin/README.md`.**
  - 12.2x is a per-line-median estimand against the plate's median drug well; it is about 6-7x against DMSO and plate-dependent.
  - It carries no readthrough caveat.
- **Literature.**
  - Cong 2020 is misdescribed: it does not say "no direct binding", and the cells were rat RLE-6TN, not A549.
  - The MDM2-independence of Jiang 2024 rests on a 2025 review.
- **Code.**
  - The panel's p53 WT-vs-altered contrast adds an unfiltered single-pass position correction, which creates false "suppressors"
    (erythromycin, afatinib, z −5 to −8).
  - Its pattern label ignores sign.
  - FDR uses two one-sided BH families.
- **Reproducibility.**
  - `compare_with_repo.py` skips the 13 `.csv.gz` tables and always exits 0.
  - Three caches are not keyed to their inputs.
  - No test covers `mg53_p53`.
  - The T8 short answers are hard-coded.
  - Nothing is pinned.

### Claims (from the audits and from this evaluation's own checks) that did not survive
- **"Only ~6 raisers survive batch correction": refuted.** Low-baseline plates amplify true effects.
- **"The active-set −0.030 slope is a shutdown artefact": not established.** Shutdown drug-doses contribute 59% of it, but it
  persists among drug-doses with a valid WT>altered p53 read-out (−0.034, p 0.011), and mechanism heterogeneity is not significant
  (p 0.13-0.22). Either way it is post hoc and not robust (Holm ≥ 0.106), and whether it replicates in DESeq2 depends on the
  specification.
- **"Decreases are detectable mainly on high-baseline plates": refuted.** The pattern is confounded with the plates 1-3 compound library.
- **"MUSCLE_STRUCTURAL is a readthrough false positive": not shown.** It is a weak nominal signal either way.
- **"A within-line E2F/p53-regulon axis is not reproduced": withdrawn.** This was tested only with 19 curated p53 targets and 5
  proliferation markers from the 141-gene subset, which cannot refute a regulon-wide pattern; it was not re-tested genome-wide.

## What Tahoe says so far on the question (scoped)

- **Upstream** (data-driven base).
  - At 24 h TRIM72 mRNA rises after strong cytotoxic or stress drugs:
    - replicated for idarubicin and homoharringtonine 5 µM;
    - single wells for auranofin, epirubicin, doxorubicin, harringtonine, dinaciclib, panobinostat and filgotinib.
  - It falls with radotinib (replicated) and trametinib.
  - The rise does not need p53.
  - Across drug-doses it tracks a genome-wide downstream-of-gene (readthrough) index (rho 0.45), although idarubicin, harringtonine,
    ouabain and dinaciclib raise it without global readthrough.
  - In nearly every raiser it rises with the same-strand PYCARD-AS1 at the FUS-TRIM72 locus (readthrough or neighbourhood
    co-regulation). It is not established as TRIM72-promoter activation or as more MG53 protein.
  - The locus, not TP53, sets the untreated level.
- **Downstream** (list-limited base).
  - No TP53-genotype-specific association of TRIM72 with the curated p53-target score. Falls steeper than roughly 2-5% per doubling
    are excluded, and only where TRIM72 varies reproducibly.
  - Among 28 MG53-linked pathway genes (tested against a 109-gene background), no footprint beyond a shared stress state.
  - A list-free test finds no protective link between a line's TRIM72 induction and its 24 h cell abundance (strong raisers: slope
    −0.019, p 0.70). If anything, lines that raise TRIM72 more are more depleted (17 of 18 raiser drug-doses in the repo, mean rho
    −0.26), largely a shared drug-responsiveness axis (partial rho −0.10).
  - **A genome-wide, genotype-controlled screen has not been run, so effects outside the tested lists are unknown.**
- **What Tahoe cannot settle.** These are limits of the database:
  - spliced TRIM72 mRNA vs readthrough (gene-level counts only);
  - MG53 protein or p53 protein (no protein data);
  - anything before or after 24 h (one time point).

## Building the list-free version (for the build computer)

These specs use the repo's existing products and code paths. Lists appear only as annotation after a genome-wide result.

- **Keep the per-(well × line) effect tensor for all genes.** It is already computed and discarded twice: in `upstream_tf.py`
  build_pass (`:562-707`, about 2-11 min) and in atlas effects pass 3 (`tahoe_atlas.py:1176-1187`). It is about 4.4 GB for 1,329 wells ×
  50 lines × 16,643 genes. It reproduces the panel's per-line effects exactly and needs no raw-cell pass. The genome-wide downstream
  screen and the Tahoe-derived p53 program build on it; the other items use existing atlas products, committed tables or Tahoe's
  DESeq2 table.
- **Genome-wide, genotype-controlled downstream screen.**
  - Run the two_way design (drug-dose × TP53-group and line fixed effects; `many_diffs`, `two_way.py:1051`, is already vectorised)
    with every expressed gene as the outcome and TRIM72 as the exposure. Chunk the genes; per-gene expression masks make the fitting
    take hours.
  - Report the WT-specific and common slopes for all genes, with the FDR over the genome.
  - Then test, as overlays, whether p53 targets or MG53 pathways are enriched, using a rank-based, correlation-aware test against the
    genome.
- **A p53 program derived from Tahoe.**
  - The genes whose 24 h response is TP53-WT-selective across drug-doses, genome-wide.
  - Choose the activating drug-doses by genome-wide WT-vs-altered divergence, not by the 21-gene score.
  - Use this program as the p53 outcome; keep the 21-gene list as a check.
  - The atlas already has a genotype-split, drug-level read-out of every driver feature (`angle_line_response`, `tahoe_atlas.py:2881-2911`).
- **Data-driven programs and drug groupings.**
  - Run the atlas `angles` step, which `mg53_setup.sh` skips. `angle_programs` (`tahoe_atlas.py:3042-3160`) finds gene programs
    genome-wide and gives per-line, genotype-split program responses.
  - Use these programs for "what moves with TRIM72".
  - Group drugs by signature similarity (`drug_summary.csv` `most_similar_drugs`) rather than by curated classes.
- **"What moves" and "which TFs" from the genome-wide tables already committed.**
  - Base T3/T8 on `a_coreg_genomewide.csv` (raw and PC-removed variants) and on TF mRNA across all genes.
  - Add the genome-wide readthrough index as a T1 column.
- **Single cells, genome-wide.** This needs one new pass over the raw cells (338 GB; a re-download only if the build used stream
  mode).
  - The cheapest form is a TRIM72-detection-stratified pseudobulk: add a detected flag to the (sample, line) key at
    `tahoe_atlas.py:507`. That is about 2 × 20 GB and about 1 h, and makes every gene an outcome.
  - Choose detection-matched placebo genes from the data (a few hundred via `--genes`, about 14 MB per gene).
- **Method-independent replicate.** Tahoe's own DESeq2 table for all genes × all drugs (`metadata/pseudobulk_differential_expression`,
  about 90 GB; read it whole, without the gene filter) supports the same screens with a different quantification.

## Repo content outside the project's scope (criterion 1)

These recommend wet-lab work and should be removed or reframed as limits:
- `README.md` section 4's "direct test";
- section 2's qPCR assay;
- T8's last row (`summary_tables.py:372`);
- `gene_modules.csv`, a knockdown/overexpression qPCR design with pre-written expected directions.
