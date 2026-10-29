# Evaluation of Tahoe100-PseudoManual (`mg53_p53/`, `trim72_idarubicin/`)

**Goal evaluated:** use Tahoe-100M to find upstream effectors of MG53/TRIM72 and the downstream effects of TRIM72, mainly on p53 output
but also broadly, reading the data as 24 h mRNA.

**Scope.** The project works only by building and extracting from the Tahoe-100M database; no wet-lab experiments will be run. So
every recommendation here stays inside Tahoe, and the limits of Tahoe's gene-level 24 h counts are stated as limits, not as
experiments to run. Analyses should be genome-wide and data-driven at their base. Curated gene, pathway or drug lists can set
priorities, but should not define what is tested, because that preloads the answer with assumptions.

## Bottom line

**The repo largely meets the goal for p53, partly for upstream effectors, and only weakly for "downstream broadly".**

- The work is careful, internally consistent and candid about what Tahoe cannot show.
- Its central p53 conclusions reproduce on an independent source: Tahoe's own published DESeq2 table, which none of the repo's
  numbers came from.
- The weak points are mostly interpretive, not computational:
  - Much of what "raises TRIM72" travels with same-strand readthrough-type transcription from FUS, which the repo understates.
  - Several short-answer details are wrong or generalise from one compound.
  - The one replicated lowerer (radotinib) is never named.
  - The computed "broad downstream" screen is never reported.
  - The 24 h shutdown/stability effects are handled for readthrough but not for mRNA stability or for the p53 read-outs themselves.

| Part of the goal | Grade | Why |
|---|---|---|
| Downstream: TRIM72 → p53 output | **Strong** on direction; **moderate** on magnitude | TRIM72 is not a p53 target. Its induction does not need p53, though a partial p53 contribution is not excluded (as the repo says). No TP53-WT-specific association, replicated on DESeq2. The excluded effect size depends on reliability assumptions (see below). Because induced TRIM72 is largely readthrough-compatible, the null says little about MG53 protein. |
| Upstream effectors of TRIM72 mRNA | **Adequate** | Replicated raisers are right (idarubicin and homoharringtonine 5 µM). But the rise is readthrough-compatible, the class and TF claims overgeneralise, the lowerers are under-reported, and the plates 1-3 drugs were screened at about half sensitivity. |
| Downstream broadly (non-p53) | **Weak** | The within-well, genotype-controlled pathway screen (two_way D2, 27 read-outs) was computed but never reported. There is no short answer beyond p53, and per-line cell abundance is never tested as an outcome. |
| Reading it as 24 h mRNA | **Adequate** | Readthrough/DoG, ambient RNA, cell loss and the protein/time-lag caveats are handled. Not handled: stabilisation, superinduction and composition for the shutdown drugs, and the collapse of p53-target mRNA in shutdown wells. The README wrongly says the genotype contrast cancels transcription shutdown. |
| Reproducibility / engineering | **Adequate** | The summary layer rebuilds byte-identically, 33 of 34 quoted numbers trace to tables, and the core smoke test passes (196 PASS / 0 FAIL). But no test covers `mg53_p53`, the comparison tool skips the 13 `.csv.gz` tables and always exits 0, three caches are not keyed to their inputs, and nothing is pinned. |

## How this was checked

1. **Audit.** 12 independent auditors covered each workstream plus cross-cutting views (24 h kinetics, core method, literature, goal
   coverage, reproducibility). They read the code and recomputed numbers from the committed tables; the 430 GB raw data is not
   available here. This produced 73 de-duplicated issues.
2. **Adversarial verification.** Each issue went to a verifier with its own code. Of the 21 "major" issues, 5 stayed major and 16 were
   downgraded; 34 issues were only partly confirmed and 1 was refuted. A separate agent adjudicated four disagreements between auditors.
3. **Real-data check.** Tahoe's full pseudobulk DESeq2 table (1,026 files, about 92 GB) was streamed and reduced to 141 genes × all
   379 drugs (9.2M rows). It matches the repo's own idarubicin pull to 4e-7. Five analyses re-tested the claims on it:
   - upstream ranking,
   - 24 h shutdown effects,
   - locus readthrough,
   - p53 dependence and the genotype-controlled association,
   - broad downstream effects and viability.

   A separate skeptic re-derived each analysis; the numbers below are the skeptic-corrected ones.

   This check itself rests on a pre-chosen gene set (141 genes). Its results speak only to those genes. Its broad-downstream
   null, in particular, covers literature pathways, not the genome.
4. **Critics.** A completeness critic and a calibration critic reviewed the draft of this report. The KMT2D lead was re-checked
   independently.

## What holds up

- **TRIM72 is not a p53 target, and its induction does not need p53.**
  - Under idarubicin 5 µM, TRIM72 rises in 33 of 33 TP53-altered lines (WT − altered −0.18 log2, CI −1.22 to 0.60).
  - In the same wells MDM2 is WT-selective (WT − altered +0.81, p 0.002).
  - Selinexor activates p53 WT-selectively (MDM2 WT − altered +1.10) without raising TRIM72.
  - TRIM72 is absent from the Fischer 2017 p53-target census and has TP53 ChIP peaks in only 2 of 393 data sets.
  - A modest WT lean in TRIM72 induction does reproduce (+0.3 to +0.5 log2 pooled, nominal p 0.01-0.04). It is largest for
    epirubicin and doxorubicin (+1.1 to +2.1 log2, on low-count plate 9). So a partial p53 input of about 0.5-1 log2 is not excluded.
    The repo's short answer says exactly this, though it mis-cites the numbers.
- **No TP53-WT-specific association between TRIM72 and p53 output.**
  - The repo's WT − altered slope is −0.0032 (CI −0.0085 to 0.0022). The independent DESeq2 refit gives +0.0020 (CI −0.0078 to +0.0117),
    permutation p 0.73. It stays null when shutdown drugs are dropped, in active drug-doses, with MDM2 or CDKN1A alone, and with count
    filters.
  - The repo's FDXR slope (p 0.01) does not replicate (p 0.24), and DDB2 leans the opposite way (+0.029, p 0.026). Neither survives correction.
  - The repo's −0.030 slope in its 62 active drug-doses does not replicate (−0.0035 to +0.044 by model). The repo already calls it not robust.
- **The TP53 labels (17 WT / 33 altered) are correct.** Seven WT lines are CDKN2A-null, which matters only for non-genotoxic drugs.
- **Idarubicin and homoharringtonine 5 µM are real, replicated raisers.**
  - Both rise on both plates, in 45-47 of 47 lines in DESeq2.
  - All 21 repo raisers point the same way in DESeq2, and no raiser outside them reaches significance.
  - Mitoxantrone 5 µM is correctly flagged as not replicating.
- **The locus drives the untreated TRIM72 level across lines.** PYCARD-AS1 within-plate rho is 0.82 in the repo and 0.62-0.75 in DESeq2.
  TP53 status shows no detectable effect (rho 0.07; underpowered).
  - The repo's KMT2D lead replicates in DESeq2: KMT2D-mutant lines read +1.5 log2 higher (q 0.02, the only one of 30 drivers).
  - Half of it goes with PYCARD-AS1 (+0.74, p 0.10 after adjusting), and these lines are hypermutated (median 18 vs 6 drivers).
  - It is still a lead, as the repo says.
- **The documentation and reasoning are sound.**
  - Internal consistency is excellent.
  - The key citations (Jiang 2024 FRBM, Li 2021, Fischer 2017) are accurate.
  - The explanation of why Tahoe cannot test MG53 → p53 causally is right. (The README's proposed wet-lab experiment is outside
    this project's scope.)

## The 24 h reading, raiser by raiser (verified)

| Raiser | What a 24 h mRNA snapshot shows |
|---|---|
| Idarubicin 5 µM (replicated) | The same-strand PYCARD-AS1 co-rise covers about half (plate 6) to all (plate 14) of TRIM72's added counts. Opposite-strand PYCARD does not rise. Idarubicin is not a readthrough inducer genome-wide, so the signal is locus-specific: readthrough or co-regulation of the + strand domain, which 3' counts cannot separate. p53 output is real but read better by FDXR/DDB2 than by MDM2/CDKN1A, which are blunted at 24 h. |
| Homoharringtonine 5 / 0.5 µM (5 µM replicated) | Same near-locus signature as idarubicin. It extends further (ITGAM), and HHT is also a genome-wide readthrough inducer. Translation block gives a superinduction/stabilisation profile (FOS +3.1, JUN +3.7 log2). |
| Epirubicin, doxorubicin 5 µM (single wells, low-count plate 9) | Partly locus-coupled (about 0.5). Largest WT lean. Genuine DNA-damage p53 output. |
| Auranofin 5 µM | Locus co-rise. p53 output is suppressed in WT lines (p53 index −0.76), so these wells cannot be used for p53 read-outs. |
| Dinaciclib, all doses | The z and corrected fold come mostly from the pseudocount floor (a no-change simulation reproduces 66-83% of the effect). A real 1.8-4.3x rise remains (DESeq2 medians), but it is a generic low-gene/composition rise in heavily cell-depleted wells, with no strand pattern. Every p53 target falls, FDXR/DDB2 included, so these wells should be excluded. |
| Panobinostat 5 µM | The only one of three HDAC inhibitors to raise TRIM72. Mixed shutdown profile. |
| Not raisers | AT7519 (globally near-inactive, so the CDK9 class cannot be tested), plicamycin, 4EGI-1 and the MNK inhibitors. Shutdown alone is not sufficient. |

## What needs correcting

### Major: kept as major by the verifiers
1. **TRIM72's drug "induction" is largely readthrough-compatible, and the repo understates this** (M-4, M-5, M-6).
   - Almost every raiser co-raises PYCARD-AS1 strand-specifically.
   - If TRIM72 follows PYCARD-AS1 at its untreated ratio, that rise accounts for half to all of TRIM72's added counts.
   - The FUS distal-3' feature ENSG00000260060 rises more than FUS itself. It was dropped from the locus table (T4) by the Ensembl
     116 coordinates.
   - The README contrasts "clean for homoharringtonine" with "not significant for idarubicin". That contrast comes from a strand test
     dominated by genes 150-280 kb away. Near the locus, both drugs show the same signature.
   - Consequence: the upstream list names effectors of transcription past FUS at 16p11.2, not demonstrated regulators of TRIM72/MG53
     expression. "Unresolved" is the right verdict, but it applies to both drugs, and the TRIM72-mRNA ≈ MG53 premise is weaker than stated.
2. **"CDK9 and HDAC inhibitors raise TRIM72" generalises from single compounds** (M-1).
   - Dinaciclib is the only testable CDK9 compound, and its signal is floor-inflated and not TRIM72-specific.
   - Belinostat and tucidinostat do not raise TRIM72; only panobinostat does.
3. **The transcription-factor short answer is misleading** (M-8).
   - The ATF4/ATF5/XBP1 (integrated stress response) association comes from weakly active drug-doses.
   - At the raisers, ISR targets are repressed, in the repo's data and in DESeq2.
   - MEF2A/C/D are expressed, not "silent", though they do not explain the rise.
4. **"Downstream broadly" was computed but not delivered** (M-17).
   - The D2 screen is absent from README, SUMMARY and the short answers. Only the across-drug rows (T3) and the single-cell NF-κB and
     ferroptosis rows (T10) reach the deliverable, and they are not interpreted.
   - The independent re-analysis gives the answer the repo should state:
     - no mRNA footprint beyond a shared stress state (largest within-well |partial r| 0.027);
     - no TP53-WT-specific pathway association (minimum q 0.85);
     - no protective link to 24 h cell abundance. If anything there is a weak, non-specific negative lean: lines that raise TRIM72
       more are slightly more depleted, as stress genes are too.
   - The D2 hits (ATF3, MCL1, PTK2) are technical or stress co-variation; TRIM72's line deviations do not replicate in ordinary wells.
   - MG53's known non-p53 targets (IRS1, FAK and others) are regulated at the protein level, so mRNA cannot test them.

### Notable (the verifiers graded these minor; the real-data check sharpened them)
- **Lowerers.**
  - The short answers name only ponatinib 5 µM, which is only nominal in DESeq2.
  - The README mentions trametinib (lower in 9/9 wells, compound level q 4e-6 in DESeq2) and the "Other TK inhibitor" class only as
    hypotheses.
  - It never names radotinib 5 µM, the only lowerer replicated on two plates (0.48x). Radotinib is TRIM72-selective and barely
    moves EGR1/CCND1.
  - Trametinib's fall comes with MAPK/IEG loss and, per a critic's check, a parallel PYCARD-AS1 fall, i.e. it also looks locus-level.
- **Effect-size bounds.**
  - The README's "up to ~0.03 per doubling" is 0.03 log2, about 2%, and is the optimistic end.
  - With replicate-well reliability, the DESeq2 bound is 3.6-5.1% per doubling. That reliability is carried by the strongly
    replicated idarubicin/HHT wells. In a typical drug-dose, TRIM72's line deviations do not replicate (r ≈ 0.01), so the null
    constrains little there.
  - The single-cell ">1.2% per doubling excluded" depends on the overdispersion model (1.8% if half of it is technical). It also
    rests on a 0/1 detection exposure (about 1.7% of cells, mostly 1 UMI), and the README itself says a few-percent fall could be
    masked. That figure should be dropped from the short answer or labelled conditional.
- **Plates 1-3 were screened at about half sensitivity.** PF-06260933, HI-TOPK-032, abemaciclib and ERK5-IN-2 at 5 µM are unresolved
  candidates: 2.2-2.6x, nearly all lines up, with the same PYCARD-AS1 co-rise.

### Minor (verified)
- **24 h kinetics.**
  - Stabilisation, superinduction and composition are never named as alternatives for the translation- and transcription-blocking raisers.
  - The README wrongly lists transcription shutdown among the factors the genotype contrast cancels.
  - 7 of the 13 pooled raisers show no WT-selective p53 output at 24 h. Shutdown and cytotoxic wells (dinaciclib, auranofin)
    should be excluded from the p53-output tests, and FDXR/DDB2 should be preferred over MDM2/CDKN1A for the DNA-damage raisers.
  - The temporally cleaner design (untreated TRIM72 vs induced p53 responsiveness; WT rho 0.12, p 0.65) is in SUMMARY T7 but not
    in the README.
- **Wording.**
  - "Compare z, not folds, across plates": z carries the full 1.84x plate amplification.
  - "No detectable association in any of four designs": its own across-drug rho is 0.12, p 5e-5, a stress co-induction.
  - The untreated "negative lean" rests on TP53 mRNA, which a degradation mechanism would not lower.
  - "+0.16 to +0.45 log2" is not traceable to T5.
  - "TRIM72 only changes with drugs that act on p53" is contradicted by T1.
  - "None within lines / noise ceiling" for the TFs.
  - The AP-1-arm partial over-adjusts (ATF4 0.09 vs 0.22).
  - The AP-1/IEG co-response is equally present in inert wells, i.e. a well-level stress axis.
- **`trim72_idarubicin/README.md`.**
  - It calls 12.2x "the strongest TRIM72 increase" with no readthrough caveat.
  - 12.2x is a per-line-median estimand measured against the plate's median drug well. Against DMSO it is about 6-7x
    (pooled reads, DESeq2), and it ranges about 3-19x depending on the plate.
- **Literature.**
  - Cong 2020 is misdescribed: it does not say "no direct binding", and the cells were rat RLE-6TN, not A549.
  - The MDM2-independence of Jiang 2024 rests on a 2025 review, not the primary paper.
  - No citation for stress-induced (DoG) readthrough.
- **Code.**
  - The panel's p53 WT-vs-altered contrast adds an unfiltered single-pass position correction. It makes erythromycin and afatinib
    look like strong WT-selective p53 "suppressors" (z −5 to −8), which DESeq2 does not support.
  - Its "pattern" label ignores sign.
  - FDR uses two one-sided BH families; a single two-sided family gives 16 up / 3 down instead of 21 / 1.
  - None of these changes a headline.
- **Reproducibility.**
  - `compare_with_repo.py` skips the 13 `.csv.gz` step tables and always exits 0.
  - The p53_dependence, downstream_p53 and upstream_coregulation caches are reused regardless of input.
  - No test exercises `mg53_p53` (the synthetic data plants TRIM72 = 0).
  - The T8 short answers are hard-coded.
  - Nothing is pinned.
  - "Reproduced all 168 tables exactly" has no committed evidence.

### Claims that did not survive verification
- **"Only ~6 raisers survive batch correction" (auditor): refuted.** Low-baseline plates amplify true effects; the null spread is the same.
- **"The active-set −0.030 slope is a shutdown artefact" (auditor): contested, and moot.** It does not replicate in DESeq2.
- **"Decreases are detectable mainly on high-baseline plates" (real-data analysis): refuted by its own skeptic.** The pattern is
  confounded with the plates 1-3 compound library.
- **"The pseudocount causes the scarcity of decreases" (auditor): not supported.** DESeq2 shows the same scarcity; low counts limit power.
- **A within-line E2F/p53-regulon "axis": not reproduced.** Curated p53 targets give r 0.000.

## What Tahoe actually says on the user's question (after verification)

- **Upstream.**
  - At 24 h, TRIM72 mRNA rises after strong cytotoxic or stress drugs:
    - replicated for idarubicin and homoharringtonine 5 µM;
    - supported as a class for anthracyclines/TOP2 poisons;
    - single wells for auranofin, epirubicin, doxorubicin, harringtonine, dinaciclib, panobinostat and filgotinib.
  - It falls with radotinib (replicated) and trametinib.
  - The rise does not need p53, though a modest contribution is not excluded.
  - For idarubicin, homoharringtonine, auranofin and the anthracyclines it travels with a strand-specific rise of the FUS-downstream
    lncRNA PYCARD-AS1 (readthrough or + strand co-regulation). For dinaciclib it is a generic low-gene shift in dying wells, and the
    harringtonines add a translation-block superinduction profile.
  - None of this establishes TRIM72-promoter activation or more MG53 protein.
  - Among line traits, the locus dominates the untreated level. KMT2D is a confounded lead. The muscle promoter TFs MyoD/myogenin are
    not expressed, and the AKT and glucocorticoid routes do not raise TRIM72 mRNA here.
- **Downstream.**
  - There is no TP53-genotype-specific association of TRIM72 with p53-target output. Falls steeper than roughly 2-5% per doubling
    are excluded where TRIM72 varies reproducibly (essentially the idarubicin/HHT wells); elsewhere the data constrain little.
  - There is no broad mRNA pathway or viability footprint beyond a shared stress state.
  - The literature's MG53 → p53 effect is protein-level degradation and cannot be tested in Tahoe.
- **What Tahoe cannot settle.** These are limits of the database, not tasks:
  - Whether the TRIM72 counts are spliced TRIM72 mRNA or readthrough: Tahoe ships gene-level counts, not read coverage.
  - Whether MG53 protein changes, or acts on p53 protein: Tahoe has no protein data.
  - Anything before or after 24 h: Tahoe has one time point.

## Priority fixes for the repo
1. Rewrite the upstream short answer and section 2 around the locus signal.
   - State that idarubicin and HHT show the same near-locus signature.
   - Report the PYCARD-AS1 co-rise for each raiser in T1, and restore ENSG00000260060 to T4.
   - Add the readthrough caveat and the estimand/reference of the 12.2x to `trim72_idarubicin/README.md`.
2. Name compounds, not classes (dinaciclib, panobinostat), and carry the pseudocount-floor flag into T1/T5.
   - Add a lowering row: trametinib and radotinib 5 µM.
   - Flag plates 1-3 as low-sensitivity.
3. Build the "beyond p53" answer from a genome-wide, genotype-controlled screen of all genes, not from the 27 pre-chosen D2
   read-outs. Use the D2 pathways only as a priority overlay. Add a per-line abundance analysis.
4. Add a 24 h paragraph.
   - Name stabilisation, superinduction and composition as alternatives for the shutdown raisers.
   - Remove the claim that the genotype contrast cancels shutdown.
   - Exclude shutdown and cytotoxic wells from the p53-output tests, and use FDXR/DDB2 for the DNA-damage raisers.
5. Fix the remaining short-answer errors.
   - TF row: the ISR association holds only among weak drug-doses, and MEF2 is expressed.
   - Bounds: state 2% (split-half) to 5% (replicate wells), say where they apply, and mark the single-cell 1.2% as conditional.
   - Cite the WT lean correctly (+0.3 to +0.5 log2 pooled).
   - Correct the Cong 2020 description.
6. Engineering.
   - Make `compare_with_repo.py` include `.csv.gz` and exit non-zero on a mismatch.
   - Key all caches to their inputs.
   - Pin dependencies and data revisions.
   - Add a minimal synthetic test for `mg53_p53`.
   - Fix the panel's p53 contrast (two-pass correction, sign-aware label).
