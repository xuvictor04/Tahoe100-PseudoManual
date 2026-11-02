---
type: finding
tags: [finding, p53, cell-lines, calibration, power, effect-size]
status: current
---

# Per-line p53 function

Each of the 50 pooled lines placed on a continuous p53-output axis against a null reference, instead of
being carried as a yes/no [[TP53]] genotype label — and what changes in the MG53 result when the finer
picture is used.

> [!summary] In one line
> p53 is off across two thirds of the panel: **33 of 50 lines carry a TP53 driver mutation**, **11 of 50**
> are called functionally responsive, and **0 of 33** altered lines reach the responsive cut
> [`mg53_p53/findings/tables/p53_nullification.csv`]. The altered lines are not quite at zero — the median
> one retains **2–4% of the wild-type-to-null gap**, and eight retain **5–31%** — but replacing the binary
> label with the graded axis moves nothing. The wild-type-minus-altered program-P slope stays at
> **−0.00183** (two-way p 0.285, TP53-label-permutation p 0.304), every graded moderator is within noise,
> and the smallest multiplicity-corrected q across roughly 24 such tests is **0.54**.

> [!note] Scope
> This note is about **downstream of MG53** — what MG53's level does to p53 and p53's output — and about the
> arm structure that question is measured in. Whether p53 regulates MG53 (**upstream of MG53**) is out of
> scope: the section of the source document that asked whether [[TRIM72]]'s induction depends on p53
> function was removed, together with the cardiac-glycoside lead that rested on it
> [`mg53_p53/findings/PER_LINE_p53_FUNCTION.md` §scope]. No number below bears on it.

## The axis, and what anchors zero

Four per-line read-outs are available, two data-defined and two list-based
[`mg53_p53/findings/tables/per_line_p53_state.csv`, 50 rows, 29 key columns; the full 216-column version is
`per_line_p53_state_FULL.csv`]:

| Column | What it is | Basis |
|---|---|---|
| `ind_P_mean` | mean induction of [[p53 program P]] across drug-doses, log2 | data-defined |
| `lf_P_on_LFP50_mean` | the same on the **label-free** 50-gene programme | data-defined |
| `ax_P_S2_b_p53` (`b_p53`) | per-line slope on the S2 p53-activating drug-dose axis | data-defined |
| `p53_responsiveness_log2` | induction of the curated 21-gene P53_ACTIVITY panel | list-based |
| `basal_p53_activity_log2` | basal panel level, within-plate z | list-based |

**Zero is anchored by the null reference, not by the panel mean.** Ten TP53 truncating / splice-disrupted /
whole-gene-deleted lines form the core reference: **AsPC-1, COLO 205, HOP62, KATO III, NCI-H1792,
Panc 03.27, RPMI-7951, SNU-423, SW 900, SW1417** [`mg53_p53/findings/tables/null_reference_lines.csv`].
KATO III is the cleanest anchor of all — homozygous TP53 deletion, no TP53 mRNA. Three further
truncating-class lines are deliberately **excluded** from the reference because their variants may leave
some functional protein:

| Excluded line | Variant | Why |
|---|---|---|
| AN3 CA | p.G389W; p.R213Q; p.S90fs | frameshift plus two missense alleles, subclonal (VAF ≤ 0.5) |
| HCT15 | splice site + p.S241F | missense at a DNA-contact hotspot alongside the splice allele; unphased |
| NCI-H2347 | p.T125T | synonymous at the exon-4 donor — splice-affecting, can leave full-length mRNA |

`ind_P_mean_minus_null` is each line's induction minus the median of the ten core lines, computed
**leave-one-out** for lines that are themselves in the reference, so no null line is scored against itself
(verified by arithmetic on the table: the subtracted anchor is 0.003706 for every non-reference line,
0.003563 for SW 900, 0.003850 for KATO III). The wild-type end of the axis is the median of the 17
genotype-wild-type lines, 0.1437 log2 — C32, as it happens — and `ind_P_mean_frac_of_WT_gap` rescales the
axis so the null sits at 0.0 and that median at 1.0.

## How far p53 is disabled across the panel

| Measure | Value | Note |
|---|---|---|
| TP53 driver mutation | **33/50** | genotype, from Tahoe cell-line metadata |
| — missense only | 20/50 | |
| — truncating / splice / deletion | 13/50 | 10 of them are the null reference |
| Functionally responsive lines | **11/50** | every responsive line is genotype-WT |
| Altered lines retaining a response | **0/33** | no TP53-altered line reaches the responsive cut |
| Genotype-WT lines not fully responsive | **6/17** | p53 damped without a TP53 mutation |
| Genotype-WT lines with CDKN2A/ARF loss | **9/17** | a second route to lowering p53 activity |
| Median responsiveness, WT vs altered | **0.948 vs 0.256** log2 (3.7×) | Mann–Whitney **p 3.1e-07**; the ranking is genotype-blind |

[`mg53_p53/findings/tables/p53_nullification.csv`]

The 11 responsive lines are NCI-H460, RKO, A549, SNU-1, A498, SW48, C32, LS 180, hTERT-HPNE, LoVo and
HepG2/C3A. The six wild-type lines that are not: H4, A-172, LOX-IMVI, A-427 and CHP-212 sit within 2 SE of
the cut and are called *uncertain*; **Hs 766T** is called outright **unresponsive**. Why a cancer panel ends
up like this, and the routes other than TP53 mutation that get it there, are in
[[p53 nullification in cancer cell lines]].

## The 50 lines, banded against the null

Each line's `ind_P_mean_minus_null` carries a 95% interval (`_lo`/`_hi`; half-widths run **1.42–2.58 ×** the
reported `ind_P_mean_se`, so these are not ±1.96 SE bands — they are resampled over drug-doses), and
`ind_P_mean_vs_null` bands the line on it. The separate `functional_call` column, which produces the
*uncertain* label, uses a ±2 SE rule against the responsiveness cut instead.

| Band | n | Lines |
|---|---|---|
| **above** | 18 | 16 WT (NCI-H460, RKO, A549, SNU-1, A498, H4, SW48, A-172, C32, LS 180, hTERT-HPNE, LoVo, LOX-IMVI, A-427, CHP-212, HepG2/C3A) + **J82, NCI-H23** |
| **above (marginal)** | 8 | HEC-1-A, HOP62, BT-474, MIA PaCa-2, SW480, HS-578T, NCI-H2030, NCI-H2347 — all altered |
| **at** | 18 | 17 altered (PANC-1, SW 900, AN3 CA, C-33 A, SK-MEL-2, SW1417, Panc 03.27, HT-29, RPMI-7951, KATO III, NCI-H1573, SNU-423, CFPAC-1, HCT15, AsPC-1, NCI-H2122, NCI-H596) + **Hs 766T** |
| **below (marginal)** | 3 | COLO 205, NCI-H1792, SHP-77 |
| **below** | 3 | SW 1271, NCI-H661, SW 1088 |

Two things to read off it. First, the **16 highest lines are all genotype-wild-type** and the band boundary
falls almost exactly on the genotype line — the only crossings are Hs 766T downward and J82/NCI-H23 upward.
Second, **no line is credibly below the null.** The six "below" calls are the panel's lowest-count lines
(SW 1088 is 54% zero-TRIM72, SW 1271 and NCI-H661 likewise sparse); SW 1088's raw mean is the lowest of the
50 but its offset-corrected value is ≈ 0, which is what a counting floor looks like rather than
dominant-negative repression. Dominant-negative repression is also structurally unavailable in most of the
panel: **30 of the 33 altered lines have sequence evidence of no remaining wild-type TP53 allele** (CCLE VAF
≈ 1.0, deleted, or compound), so there is no wild-type allele left for a mutant to poison
[`mg53_p53/findings/tables/tp53_mutation_annotation.csv`, `wt_allele_remains`; AN3 CA and NCI-H2122 may keep
a functional allele, HCT15 and Panc 03.27 are unphased].

## Roughly 5% of the response, not none

Anchored on the null and scaled to the wild-type median, the **median altered line** retains:

| Axis | Null median | WT median | Altered median | Retained |
|---|---|---|---|---|
| `ind_P_mean` | 0.0037 | 0.1474 | 0.0069 | **2.2%** |
| `lf_P_on_LFP50_mean` (label-free) | 0.0636 | 0.3255 | 0.0698 | **2.4%** |
| `ax_P_S2_b_p53` | 0.0389 | 0.9575 | 0.0741 | **3.8%** |
| `p53_responsiveness_log2` (21-gene panel) | 0.2275 | 0.9481 | 0.2562 | **4.0%** |

(Medians computed from `mg53_p53/findings/tables/per_line_p53_state.csv`; null = the ten core reference
lines.) The panel axis is the one that flatters the altered lines if read unanchored — 0.256 against 0.948
log2 looks like 21% of the wild-type induction retained — but the null reference also reads 0.2275 on that
axis, so almost all of the apparent 21% is floor. Anchored, it agrees with the other three at about 4%.

**Eight lines carry a residual worth naming**, at 5–31% of the wild-type-to-null gap on `b_p53`:

| Line | Class | `b_p53` | % of WT gap (b_p53) | % of WT gap (`ind_P`) |
|---|---|---|---|---|
| AN3 CA | truncating (flagged mixed) | 0.320 | **31%** | 4% |
| BT-474 | missense, E285K temperature-sensitive | 0.236 | **21%** | 11% |
| MIA PaCa-2 | missense, R248W hotspot | 0.179 | 15% | 11% |
| J82 | missense, E271K + K320N | 0.136 | 11% | 16% |
| HEC-1-A | missense, R248Q hotspot | 0.127 | 10% | 13% |
| HS-578T | missense, V157F | 0.100 | 7% | 9% |
| NCI-H23 | missense, M246I | 0.088 | 5% | 15% |
| HOP62 | splice c.673-2A>G | 0.088 | 5% | 11% |

**Treat this group as soft.** Its two axes disagree badly on ordering — AN3 CA leads on `b_p53` and is near
the bottom on `ind_P`; NCI-H23 is the reverse — three of the eight rest on marginal band calls, **HOP62 is
itself one of the ten null reference lines** (so about 1 in 10 null lines produces a residual this size,
which is the calibration this group has to beat), and two excluded lines outrank the bottom three on
`b_p53` anyway (NCI-H2122 0.221, SW 1088 0.186) but are set aside for low cell counts. The honest reading is
"a few percent, not zero", not a list of eight partially-functional mutants.

## Where data and literature disagree

The literature overlay in `tp53_mutation_annotation.csv` (41 variant rows over 33 lines, with Kato 2003
transactivation classes, Giacomelli 2018 DNE/LOF calls, TP53db temperature-sensitivity and GOF report
counts, Cellosaurus zygosity and CCLE 2025 VAF) expects partial canonical output above the null in only
three lines — AN3 CA, J82, NCI-H2122 — and near-null at 37 °C in one more, BT-474. Four disagreements:

1. **Hs 766T** — wild-type TP53 sequence, yet `ind_P` lands *at* the null and the panel calls it
   unresponsive. The clearest discordance in the panel, and the literature agrees the pathway is probably
   off (GDSC Nutlin-3a AUC 0.954, i.e. resistant; CDKN2A mRNA high, in the range of the TP53-mutant lines).
   It is also the single most influential line in the two-way active set ([[Two-way fixed effects]]).
2. **SNU-1, A498, C32** are flagged "attenuated" by the overlay — highest MDM4 mRNA of the 50, VHL loss,
   MDM4 amplification respectively — but score fully functional on inducibility.
3. **Ten hotspot lines** (R248Q/W, R273H/C, G245S/C, R248L), **eight of them with reported gain of
   function**, all score null-like. That is what the overlay predicts: program P measures canonical,
   wild-type-like output, and reported GOF acts through non-canonical programmes P cannot see. It is not a
   contradiction, and it is not evidence against GOF either.
4. **NCI-H2122** is "partial" by literature (a functional Q16L majority allele) but null-like in the data —
   on 19% usable wells, with a high basal panel z of 4.2, so this is a weak data call.

## Does the finer picture change the MG53 result?

No. Every version of the downstream test gives the same answer, and the graded versions are if anything
closer to zero than the binary one.

- **Primary, list-free, binary label:** wild-type minus altered program-P slope **−0.00183**, two-way
  p 0.285, TP53-label-permutation p 0.304 [`genome_wide/tables/c_program_models.csv` row 0; fit on 17 WT and
  30 altered lines, 53,084 rows]. Covariate set `none` gives **−0.00230** [row 4; 17/32, 53,331 rows].
  Rebuilt from the export's non-cross-fitted programme: **−0.00177 (95% CI −0.0054 to +0.0018)**, label
  p 0.37, 80%-detectable effect 0.0063. Three altered lines are not in the primary fit at all — NCI-H661
  (no TRIM72 detected), NCI-H2122 and NCI-H596 (no usable exposure).
- **Graded moderators, per SD of function, deconfounded within drug-dose:** responsiveness **−0.0011**
  (p_perm 0.24), inducibility **−0.0014** (0.16), basal **−0.0014** (0.19); within genotype ≈ 0. Two
  specifications that first looked positive (naive drug-dose fixed effects; genotype fixed effects plus
  moderator) were drug-dose-level confounds and vanish once each drug-dose × genotype cell gets its own
  moderator slope.
- **Functional-group contrasts:** responsive minus unresponsive **−0.0013** (CI −0.0055 to +0.0030,
  p 0.59); the clean responsive-WT versus unresponsive-altered contrast **−0.0015** (p 0.54), closer to zero
  with SW 1088 dropped.
- **Mutation class:** missense-only minus truncating **+0.0040** (p 0.14), halving to +0.0020 without
  SW 1088. Hotspot minus other-altered **+0.0070** (valid-permutation p ≈ 0.10), single-line driven by
  SW 1088.
- **Leave-one-line-out:** no single line flips the sign of the binary difference (range −0.0025 to
  −0.0008); SW 1088 pulls hardest, C32 and A549 pull the other way.
- **Multiplicity and power:** across ~24 tests the smallest corrected **q is 0.54**. What the data *exclude*
  at 80% power is function-dependent slope changes of about **0.003/SD** (genotype-free), **0.005–0.006**
  (within genotype) and **0.007–0.009** (group contrasts) — all larger than the TRIM72 slopes themselves
  (b_WT +0.0009, b_alt +0.0026). Small modifications are therefore not ruled out; no grouping reveals a
  hidden effect. This sits inside the study's standing bound: in TP53-wild-type lines, effects above roughly
  **0.4–0.6% of p53 output per doubling of measured MG53** are excluded
  ([[Downstream of MG53]], [[The measurement with controls]]).

**And the association sits in the wrong place for a p53-mediated effect.** In the primary model the slope
lives in the *altered* lines — b_alt **+0.0026** (drug-level p 3e-6) against b_WT +0.0009, not significant
[`genome_wide/tables/c_program_models.csv` row 0] — and in the repository's own activity split it is largest
in the **lowest**-activity mutants (**+0.0043**) and absent in wild-type and higher-activity mutants
[`mg53_p53/findings/tables/tableC_mutants_by_activity.csv`]. An effect routed through p53 cannot be
strongest where p53 is deadest. That pattern points at a stress-amplitude confound — the same mechanism as
[[Readthrough spillover]] and [[Plate batch effects]] — not at p53 direction.

**One post-hoc lead, not an established result.** Basal TP53 mRNA as a within-genotype moderator gives
**+0.0019/SD, p_perm 0.002**, concentrated in the altered lines (missense and high-mRNA mutants steeper than
null and truncating ones). It survives dropping SW 1088 and the low-count lines, but it is Bonferroni-
borderline across ~25–30 tests and was found after looking
[`downstream_p53/tables/b_baseline_per_line.csv`, `TP53_rel_reliable_plates`].

## What 24 h mRNA cannot decide here

- **No p53 protein.** Missense alleles typically stabilise and accumulate mutant protein; a transcript
  snapshot cannot see it. MDM2/MDM4-mediated protein destabilisation in the "attenuated" wild-type lines is
  invisible for the same reason, as is any MG53–p53 interaction at the protein level — which is where
  [[MG53 (TRIM72)]]'s known biology lives.
- **TP53 mRNA is not p53 activity.** Truncating and splice lines have low TP53 mRNA through
  nonsense-mediated decay regardless of what any protein does; COLO 205 is the counter-case, an in-frame
  deletion with normal mRNA.
- **Gain of function is off-target for program P**, which measures canonical output only (see point 3
  above).
- **Circularity.** Program P and the S2 drug-doses were selected using the binary WT/altered labels, so
  scoring lines on P biases altered lines toward unresponsive and wild-type lines toward responsive. "No
  altered line up-regulates p53" is therefore partly built in. The genotype-blind 21-gene panel corroborates
  it independently — zero altered-responsive discordants, one wild-type-unresponsive discordant
  [`p53_dependence/tables/lines_tp53_status.csv`] — and the asymmetry still favours the loss direction: an
  altered line that responded would be strong evidence of retained function, and a wild-type line that does
  not (Hs 766T) is good evidence of loss. See [[Cross-fitting and circularity]].

## Corrections carried in this note

Both are in [[Corrections and retractions]]:

- "**32 lines, all null-equivalent**" was an overstatement of the zygosity evidence. The supported statement
  is **30 of 33**, with AN3 CA and NCI-H2122 possibly retaining a functional allele and HCT15 and
  Panc 03.27 unphased.
- The hotspot-minus-other-altered contrast was published at **p 0.042**; that permutation null was invalid,
  and the corrected valid-permutation value is **p ≈ 0.10**. The effect size, +0.0070, is unchanged, and it
  is driven by one line.

## Links

- [[p53 nullification in cancer cell lines]] — why the panel looks like this, and what it costs in power
- [[The measurement with controls]] — the arms built on this table: 11 functional lines against the 10-line
  null arm
- [[Downstream of MG53]] · [[What this study found]] — the result this note tests for robustness
- [[p53 program P]] · [[Program P derivation]] · [[Signing genes by p53 direction]] — the outcome scale
- [[Nulls and calibration]] · [[Placebo genes and reference families]] — why the null reference exists
- [[The p53 pathway]] · [[The p21-DREAM axis]] · [[TP53]] · [[MDM2]] · [[MDM4]] · [[CDKN2A]]

## Sources

- `mg53_p53/findings/PER_LINE_p53_FUNCTION.md` — the analysis document; produced by a 12-agent workflow in
  which every number was independently recomputed by an adversarial verifier
- `mg53_p53/findings/tables/per_line_p53_state.csv` (50 × 29) and `per_line_p53_state_FULL.csv` (216 columns)
- `mg53_p53/findings/tables/p53_nullification.csv` — the six panel-level counts
- `mg53_p53/findings/tables/null_reference_lines.csv` — the ten core lines and the three exclusions
- `mg53_p53/findings/tables/tp53_mutation_annotation.csv` (41 rows, 33 lines) and
  `tp53db_variant_function.csv` — the literature overlay
- `genome_wide/tables/c_program_models.csv`, `two_way/tables/key_results.csv` row 42,
  `p53_dependence/tables/lines_tp53_status.csv`, `mg53_p53/findings/tables/tableC_mutants_by_activity.csv`
