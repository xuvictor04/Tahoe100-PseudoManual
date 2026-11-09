# Direction: which gene probably acts on which

The relations stage links genes that respond alike. That link has no direction: CDKN1A and MDM2 rise together, but
the cosine does not say that both follow TP53. The **direction** stage adds arrows **SOURCE → TARGET**, computed by
code from the run's own tables (nothing is edited by hand). Every arrow:

- comes from a statistical test, with a p-value and a Benjamini–Hochberg q. A pair without such a result (q < 0.10
  in its family of tests) is not an edge;
- carries a **grade** (A, B or C) and its **alerts**, each doubt in plain words. Nothing that passes is dropped
  because of doubt: a doubtful arrow keeps its place, with '⚠' and the reason, and a lower grade.

```
python -m tahoemap.direction --out OUT [--data TAHOE_FOLDER]
```

It reads the finished tensor, tables and relations stages, and the cell lines' genetics from the Tahoe metadata
(`--data`; by default the files the build indexed). It writes `OUT/direction/`: `edges.parquet`, `groups.parquet`,
`controls.json`, `info.json`, and a `README.md` that lists every column. At full scale (16,643 genes × 1,132
drug-doses × 50 lines) it streams the per-line tensor in gene chunks; on a generated output of that size it needed
1.75 GB of memory and 5.7 minutes on 4 CPUs. Options: `--mem-gb` (memory for one chunk, default 1), `--perms`
(label permutations, default 200), `--pseudo` (negative-control groups, default 60).

## What "direction" means here

The source is what the test **conditions on**. The target is what **differs with it**. The source can be:

- **A recorded mutation of the source gene.** The mutation was there before the experiment: it cannot be a
  consequence of the target.
- **The source gene's absence from some lines.** The lines that lack it are a natural knockout.
- **Compounds that target the source's protein.** The drug acts on the source; the target's mRNA follows.
- **The source gene's natural level.** A weak hint only: its level is not set by the experiment.

The target can be another gene (its level at baseline, or its response to the drugs) or the cells themselves (how
many cells of the line remain under a drug-dose, relative to the other lines in the same well).

What an arrow does **not** say:

- It is **not proof of direct regulation**. A → B → C looks like A → C. Another alteration carried by the same lines
  can be the real cause (the co-occurrence alerts name the ones the metadata records).
- **"Not recorded" is not "wild type"**: the metadata lists driver alterations, and a line may carry one that is not
  listed.
- There is **one time point** (~24 h): fast and slow effects are mixed; compensation and feedback are not seen.
- **Drugs act on proteins**, not on mRNA, and a compound can act on other proteins than its listed target.
- An arrow from a gene's **level** comes from natural differences between lines. Tissue and other differences can
  produce the same pattern, and a stronger correlation one way can come from one gene's level being measured more
  precisely, not from it acting first.

## How many tests, and which q

Thousands of genes are tested against every group, so a few false arrows are expected. Two q-values are reported:

- `q`: over the **whole table** of the kind (for example every gene against every genotype group). Grades A and B
  need it below 0.10.
- `q_group`: within the arrow's **own group** (one genotype, or one drug-dose for `level_sensitivity`). Genotype
  and `level_sensitivity` arrows are written when it is below 0.10. When `q` is not, the arrow is grade C, and its
  alert says so and gives the number of such arrows that random groups produce.

So grade A/B arrows are significant both in their group and over the whole table. Grade C arrows of these kinds are
leads: they hold up within their group, and the controls tell you how many of them to expect by chance.

## The kinds of evidence, from strongest to weakest

### 1. Recorded genotype (`genotype_response`, `genotype_baseline`, `genotype_sensitivity`; grade A, B or C)

For each driver gene recorded as altered in at least 3 screened lines, three groups are formed: loss of function,
gain of function, and "altered (any record)" when some records carry no mechanism. Each group is compared with the
lines that have no record of that gene (at least 3).

- **response**: does the target respond to its drugs less (or more) where the source is altered? The target's
  drug-doses are its 10 strongest pooled responses. The per-line response at each of them is compared between the
  two sides. The evidence of all 10 is combined, so a dependence carried by one drug class counts as much as one
  spread over all of them.
- **baseline**: is the target's level lower or higher where the source is altered?
- **sensitivity**: do the altered lines lose more or fewer cells under a drug-dose?

The null is built by shuffling which lines count as altered (200 times). When enough lines of the same organ sit on
both sides, lines are shuffled only within their organ. Every target's statistic is set against its own shuffled
values, and the shuffled values of all targets together form the null that gives the p-value. Its far tail is
fitted with a smooth curve, so a single very strong effect can still pass among millions of tests. Each target is
also checked against its own shuffles. If they disagree with the pooled null, the target's own p-value is used. This
happens for a target measured in few lines, or with few lines per organ. If a grouping shifts the whole genome (for
example, it coincides with broad differences between lines), the statistics are deflated by that inflation factor,
in the way genomic control works.

**Global sensitivity.** A line may respond less to a drug in general. TP53-mutant lines resist DNA damage, a line
with an efflux pump takes up less drug, and a line that contributes fewer cells shows weaker responses everywhere.
Every gene would then look "dependent" on whatever those lines carry. So at each of the target's drug-doses, the
line's general responsiveness is measured:

- where the drug-dose moves at least 50 other genes, from those genes (the target's own related genes are left out,
  or the correction would cancel the programme being tested);
- elsewhere, from the line's responsiveness over all drug-doses (its overall strength of response, which follows
  mostly the number of cells it contributes). This is used only when it is reliable: read from at least 20
  compounds, and reproduced by two random halves of them. A median of a few drug-doses that all carry line-dependent
  programmes of their own would follow those programmes. Without it, the arrow says that no correction was
  possible, and when most of its evidence is uncorrected it is not graded A.

A line that responds 0.3× as strongly overall is expected to show 0.3× of the gene's typical response too. Only the
difference beyond that counts. The correction has one blind spot: when most of the other genes responding at a
drug-dose are one programme that itself depends on the genotype, it mistakes that programme for general resistance.
A gene that responds the same everywhere then looks as if it responds *more* where the gene is altered. Every
response arrow therefore also reports how much of its evidence remains without the correction (`raw_share`). When
little does, the arrow is kept, says that it rests on the correction and how much the reference differs between the
two sides, and is not graded A.

**Sign.** `+1` means the source's **activity** raises the target. For a loss-of-function group, that is when the
target is higher, or responds more, where the source is intact. For gain of function the sign is reversed. For
"altered (any record)" it is not inferred (0).

**Organs.** When the lines are shuffled within organs, every shuffle keeps the organ make-up of the two sides. The
comparison is then between lines of the same organ, and no tissue alert is raised. Only lines in organs that hold
both sides carry it, and the alert says how many. When the comparison has to run across organs, the arrow says so.
It is called *tissue-confounded* when the two sides' organs differ more than chance, for example when most
KRAS-mutant lines are pancreatic.

Examples (from the synthetic test data, where they were planted):

- *TP53 loss of function (10 lines) vs not recorded (8): CDKN1A responds less in the TP53-LoF lines than in the
  other lines: 1.32x vs 3.00x at 5-Fluorouracil 5 µM; TP53 activity raises CDKN1A's drug response* (grade A, q 0.003
  over the whole table). Its alerts say that TP53 itself is not expressed in 2 of the 10 altered lines (deletions).
  They also say that at these drug-doses too few other genes respond to check for a resistance specific to the
  drugs, so only the lines' overall responsiveness was corrected.
- *XPC responds less in the TP53-LoF lines: 0.87x vs 1.74x at 5-Fluorouracil 0.5 µM* (grade C: q 0.006 within the
  TP53 group, 0.24 over the whole table; the alert adds that random groups give about 1.5 such arrows over the 38
  groups).
- *cells under Doxorubicin 5 µM: 1.15x in the TP53-LoF lines vs 0.74x in the other lines; TP53 activity makes the
  cells more sensitive* (grade B, q 0.06).
- *CDKN2A is 8.78x lower at baseline in the CDKN2B-LoF lines; CDKN2B activity raises CDKN2A's level* (grade C). The
  alerts say why not to believe it as written. It is significant only within its group. It is tissue-confounded (3
  of the 6 CDKN2B-altered lines are pancreatic, 0 of the 12 others). And the two genes are deleted together
  (co-occurs with CDKN2A-altered lines).

### 2. Natural knockouts (`null_response`, `null_baseline`, `null_sensitivity`; grade B or C)

No mutation needed. Lines where a gene is not expressed at all, reading only the ambient RNA of the well, are
natural knockouts of it. A gene qualifies when at least 3 lines lack it and at least 3 express it. The same tests
as above are run, but only towards the gene's related partners (relations), not genome-wide. When the lines lacking
the gene cannot be compared with lines of the same organs, they are compared across organs, as a separate family of
tests, provided they are not concentrated in a few organs. A gene absent from whole organs would only restate the
tissue (related genes share tissue programmes). For such a gene, its partners' baseline and response are not
tested, but its effect on cell numbers is (tissue alert, grade C). The README of the run gives how many genes this
concerns, and `groups.parquet` says why for each. Genes absent from exactly the same lines share one test: any of them
could be the cause, and the alert names them. When the lines lacking the gene carry a recorded deletion of it, the
alert says so (genotype evidence too).

Example (synthetic data): *cells under Pemetrexed 5 µM: 0.64x in the lines without MTAP vs 1.17x in lines
expressing MTAP; MTAP activity protects the cells* (grade C). The alerts say it is tissue-confounded (3 of the 5
MTAP-null lines are pancreatic, 0 of the 13 others) and that it co-occurs with the CDKN2A / CDKN2B deletions (MTAP is
deleted together with them).

### 3. Drug targets (`drug_target`; grade B)

A target annotated for at least 2 distinct compounds of one mechanism (salt forms merged; inhibitor, activator, or
unclear). If a gene moves the same way under at least 2 of them, more often than under compounds in general (Fisher's
exact test), the arrow reads "inhibiting X raises / lowers Y". The sign is relative to X's activity: an inhibitor
that raises Y means X's activity lowers Y. Alerts name the compounds and any other targets they share.

Examples (synthetic data): *activating NR3C1 raises SYNTH0033 (3 of 3 compounds; 4% of all compounds)*;
*inhibiting MTOR lowers SYNTH0003 (3 of 6 compounds; 3% of all compounds)*, sign +1 (MTOR's activity raises it).

### 4. Natural levels (`level`, `level_sensitivity`; grade C, a glimpse)

A gene's baseline level differs between lines. The question is whether the lines with more of X also show a
stronger response of Y, or fewer cells under a drug. Both the level and the response are first adjusted for organ
and for the main axes of variation between lines. The p-value comes from the t distribution, checked against
shuffled levels. For two related genes, both directions are computed. X → Y is marked `direction_clear` only when it
is stronger than Y → X *and* a bootstrap over the lines confirms the difference (`p_direction` < 0.05). Even then,
read it with care: if X's level simply tracks the shared cause more closely than Y's (or is measured more
precisely), X → Y wins without acting first. Every level arrow carries that alert.

Examples (synthetic data): *lines with more PSMD10 (lineage-adjusted) have fewer cells under Ixazomib 5 µM (r
-0.95)*, q 0.03 over all gene × drug-dose tests. *Lines with more ACSL4 have fewer cells under Artesunate 5 µM (r
-0.91)* is significant among the genes tested for that drug-dose (q 0.05) but not over all of them (q 0.20). With 18
lines, 10 degrees of freedom remain after the adjustment, so it is shown as a lead, and its alert says so.

## How to read a grade

- **A**: a recorded genotype, at least 5 lines on each side (sharing an organ with the other side), q < 0.05 over
  the whole table, compared within organs, no tissue-confounding and no co-occurrence alert; for a response, not
  resting on the global-sensitivity correction. The strongest kind of directional evidence this data can give.
- **B**: a genotype result over the whole table with alerts or only 3–4 lines on a side; a natural knockout with at
  least 5 lines lacking the gene; a drug-target result. Worth taking seriously; read the alerts.
- **C**: a glimpse: levels; genotype results significant only within their own group; natural knockouts with 3–4
  lines, absent from whole organs, or co-absent with the target. A lead to check, not a finding.

The alerts you will meet: few lines; tissue-confounded; compared across organs; compared within organs on part of
the lines; co-occurs with another gene's altered lines; the altered lines are mostly lines without another gene's
alteration; the target is much lower at baseline in the altered lines (a lost response may be lost expression); the
source itself is not expressed in some altered lines (deletion); the target measured in only some lines; the
difference exists only relative to the other responding genes (rests on the correction); no correction, or only a
line-wide one, at the drug-doses carrying the difference; its own shuffles used; artifact flags of the supporting
drug-doses; mechanism not recorded; significant only within its group; drugs act on other proteins; direction
unclear, and the measurement-precision caveat (levels).

## Controls: how much to trust it

`controls.json` reports three kinds of control.

- **Positive.** TP53 → the p53 target genes: how many are found, with the right sign, and their ranks among all
  genes. TP53 → cells under DNA-damaging drugs (expected: TP53 activity makes the cells more sensitive). KEAP1 → the
  NRF2 target genes at baseline, when KEAP1 is recorded in enough lines.
- **Negative.** 60 random "pseudo-genotypes": random line sets with sizes spread over those of the real groups
  (small and large alike), which resemble no recorded group and no large natural-knockout line set. They are tested
  exactly like the real groups and counted at the real table's cut. Their arrows per group, times the number of
  real groups, is the number of false arrows to expect. It is reported per kind next to the real counts (also in
  `info.json`, and in the README, which warns when random groups do as well as the real ones).
- **Levels.** The same level tests with every gene's level shuffled over its lines: the arrows a run without any real
  level effect would give.

On the synthetic test data (`python tests/test_direction.py`), the planted answers come back:

- TP53 → p53 targets: 10 of 22, every one with the right sign. 3 are significant over the whole table (2 at grade A),
  7 within the TP53 group only (grade C). 17 of the 22 rank in the top 5% of all genes.
- TP53 → cells under Doxorubicin, Topotecan and 5-Fluorouracil (5 µM), grade B.
- PSMD10 → Ixazomib (q 0.03) and ACSL4 → Artesunate (a lead within its drug-dose).
- MTAP-null → Pemetrexed (grade C, tissue-confounded).
- The glucocorticoid, MTOR and statin drug classes.
- Random pseudo-groups give no arrow over the whole table, and 0.05–0.12 within-group leads per group.

With 18 lines the power is limited; with the real 50 lines it is higher. The test also builds full-dimension outputs
(1,132 drug-doses × 50 lines in 16 organs, 4,000–16,643 genes) with planted effects and checks they are found there.
These are a genotype-dependent programme, a natural knockout's partner effects, a lone natural-knockout effect on
cell numbers, and a level modulator with its direction. It checks that a line-wide resistance, a programme that
dominates its drug-doses and random driver groups give no false grade-A arrows.

At the full 16,643 genes:

- the programme comes back (39 of 40 genes, grade A);
- the knockout's partners: 30 of 30 responses and 13 of 15 baseline levels;
- the lone knockout effect on cell numbers: q 5e-5 among 6.2 million tests;
- the level modulator: 30 of 30 partners, direction clear;
- KEAP1 → 7 of 7 NRF2 targets.

The line-wide resistance gives no arrow. Random driver groups give 11 arrows over the whole table, where the
pseudo-groups predict about 6. Random pseudo-groups are never tissue-confounded with 16 organs. A weaker effect, such
as a 2.5× lower baseline in 12 knockout lines, is not enough for half a million tests (p ~1e-6 to 1e-4): it stays out
of the table. That is the price of controlling false arrows over the whole table.
