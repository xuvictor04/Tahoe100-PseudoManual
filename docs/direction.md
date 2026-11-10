# Direction: which gene probably acts on which

The relations stage links genes that respond alike. That link has no direction: CDKN1A and MDM2 rise together, but
the cosine does not say that both follow TP53. The **direction** stage adds arrows **SOURCE → TARGET**: which gene
probably acts on which, or on how many cells of a line remain under a drug. It is computed by code from the run's own
tables and the cell lines' recorded genetics; nothing is edited by hand. Every arrow:

- comes from a statistical test, with a p-value and a Benjamini–Hochberg q. A pair without such a result (q < 0.10
  in its family of tests) is not an arrow;
- carries a **grade** (A, B or C) and every reason for doubt in plain words. Nothing that passes is dropped
  because of doubt: a doubtful arrow keeps its place, with '⚠' and the reason, and a lower grade. Every reason is
  kept, in one of four tiers: **alerts** (⚠), **notes** (below a threshold), **caveats** (the same on every arrow of
  a kind) and **support** ([how to read them](#alerts-notes-caveats-and-support));
- is a **probable** direction, from 50 cancer cell lines at one time point. It is not proof that the source regulates
  the target directly ([what an arrow does not say](#what-an-arrow-does-not-say)).

The strongest evidence is the cell lines' **recorded mutations** (loss or gain of function): a mutation was there
before the experiment, so it cannot be a consequence of the target, and that is what makes the arrow point one way.
**Without any known mutation**, three other sources give a glimpse of the direction: lines that do not express a gene
at all (natural knockouts), compounds that target a gene's protein, and a gene's natural level across the lines.

Contents: [Running it](#running-it) · [Where you see the arrows](#where-you-see-the-arrows) ·
[How to read an arrow](#how-to-read-an-arrow) · [What an arrow does not say](#what-an-arrow-does-not-say) ·
[The kinds of evidence](#the-kinds-of-evidence-from-strongest-to-weakest) · [Grades](#how-to-read-a-grade) ·
[What changed in version 5](#what-changed-in-version-5-old-rule-new-rule-why) ·
[Alerts, notes, caveats and support](#alerts-notes-caveats-and-support) ·
[How many tests, and which q](#how-many-tests-and-which-q) ·
[Controls](#controls-how-much-to-trust-it) · [Files](#the-files)

## Running it

The stage is part of the pipeline. `tahoe run` runs it after `graph`; `validate`, `vault` and `map` come after it
and show its arrows:

```
build → effects → tensor → reference → tables → embed → relations → graph → direction → validate → vault → map → explorer
```

The direction stage reads the reference stage's drug classes and ChEMBL mechanisms (`reference/drug_classes.parquet`,
`drug_mechanisms.parquet`; without ChEMBL, the classes of the code constants alone) and gene coordinates
(`reference/annotations.parquet`, `gene_coords.parquet`), and the tables stage's flags of record and each line's
response strength (`tables/drugdoses.parquet`, `tables/drug_line_response.parquet`).

- **An output made before this update** (including one that finished before this stage or the explorer existed):
  after updating the code (`tahoe update`, or `git pull` in the code folder on Windows), `tahoe run` redoes reference
  and every stage after it, because each of their methods changed: `next: reference -> tables -> embed -> relations
  -> graph -> direction -> validate -> vault -> map -> explorer` (`tahoe` alone shows the plan first, with the reason).
  That is about 45–60 minutes on the full data, plus the first ChEMBL and Compara downloads; the direction stage
  itself took 3.3 minutes on the user's PC at version 2 (about 6 minutes estimated at version 6). The build, the
  effects and the tensor are kept.
- **Alone, in the foreground**: `tahoe direction` (Windows:
  `C:\tahoe\.venv\Scripts\python.exe -m tahoemap direction --out C:\tahoe\out`). Like any stage run again, it marks
  `validate`, `vault` and `map` out of date, and the next `tahoe run` redoes them.
- **No option is needed.** The cell lines' genetics come from Tahoe-100M's `metadata/cell_line_metadata.parquet`: in
  the data folder (`--data`), in a streamed build's own copy of the metadata, or else the file the build indexed
  (`atlas/file_index.json`). Without the metadata (or without relations, drug targets or cell numbers) the kinds of
  evidence that need it have nothing to test, and the stage still finishes.
- **Time and memory** at full scale (16,643 genes × 1,132 drug-doses × 50 lines): 3.3 minutes and a 1.7 GB peak on
  the user's PC on the real data at direction version 2 (`stages/direction.json` of that run); about 6–7 minutes and
  1.3–1.8 GB of memory on 4 CPUs for version 4, measured on generated outputs of the full size
  (`tests/test_direction.py`); version 6 adds no heavy step.
  Version 5 adds the natural knockouts' random controls (an estimated 1–3 minutes; `info.json`
  `null_controls_minutes` records the time) and the selectivity kinds (seconds). `info.json` (and
  `stages/direction.json`) records the stage's own peak (`peak_rss_mb`; `peak_rss_how` says how it was measured), not
  that of the earlier stages a `tahoe run` ran in the same process. It reads the per-line tensor in
  gene chunks, so the memory stays bounded whatever the number of genes. It adds well under 0.1 GB of disk.

It writes `OUT/direction/` ([the files](#the-files)). `tahoe export` copies the folder whole, and `tahoe duplicate`
hard-links its tables like the other stages' arrays.

## Where you see the arrows

All of them read the arrows through one module (`tahoemap/direction_view.py`), so they show the same rows, in the same
order, with the same words. Every list is in one order: grade A, B, C, then q (smallest first), then the size of the
effect. A list capped at N shows the N strongest and any of the N strongest without an alert that fall beyond them;
it says how many more rows there are and how many of those carry an alert.

- **The vault.**
  - Every gene note has a section **Direction (probable)** (after the partners), with two tables. *Upstream of this
    gene* lists the arrows that point to it. *Downstream of this gene* lists the arrows that go from it, to other genes
    and to the cells under a drug-dose. Each table has the source or target, the grade, the direction in words, the
    evidence (with the lines on each side), the effect, q, and the short labels of its alerts, notes and support. It is
    capped at 12 rows, says "k of N shown" and links to the explorer for every row. When the gene has arrows, its
    *At a glance* names the strongest one each way, and the frontmatter counts them
    (`direction_upstream`, `direction_downstream`).
  - A drug note lists *the genes that set how the cells fare under it* (the arrows to the cells under its doses) and
    *its targets: what acting on them probably does* (the drug-target arrows of the compound classes it belongs to,
    and whether this compound is one of those that move the gene that way). Each list is capped at 15.
  - A cell-line note lists *its recorded alterations*: the comparison groups that count the line as altered, with the
    arrows that came out of each. It also lists *the genes it does not express (natural knockouts)* that served as a
    comparison. Each list is capped at 15.
  - The note **Concepts/Probable direction** (linked from Home, from *How to read this vault* and from every direction
    section) explains the kinds, grades, signs and alerts, with this run's counts, positive controls and the false
    arrows the controls expect. Home has a row with the arrow counts by grade.
  - Every gene note links that note, so a new vault's graph view leaves it out by default. A vault made before this
    version keeps your graph settings: there it shows as a hub until you add `-file:"Probable direction"` to the
    graph view's filter.
- **The map** (`map/gene_map.html`).
  - The side panel of the selected gene has three lists: *Upstream*, *Downstream* and *Cells under drug-doses*, each
    capped at 8 rows with *show all*. A row shows the arrow, a grade badge, the direction in words, the kind and q,
    and the alerts as short labels (hover for the full reasons). Click a row for its evidence, and a gene's name to
    select it.
  - The neighbourhood tab has a **Direction** control: *off*, *arrows* (between the genes shown), or *+ its genes*
    (the default: it also adds the selected gene's up- and downstream genes, so a gene that is not on the map, such
    as a mutated driver, can be shown with its arrows).
  - The nodal and signed maps have a **Direction arrows** box (on by default): the selected gene's arrows to and from
    the genes on the map. Hover a gene to see the rows between it and the selected gene.
  - Arrow style: grade A thick, B thin, C dashed. The head shows the sign: a filled head = raises (a level, the
    cells' numbers), a bar = lowers, an open head = strengthens a drug response, a double bar = weakens it, an open
    circle = not inferred. The key (top right of the maps) folds away with its − button.
  - A source that is not a measured gene (a drug target such as NR3C1) has no place on the map: the search finds it,
    and its panel lists its arrows. A hover over a gene shows the rows between it and the selected gene (3, by the
    cap rule); the neighbourhood view draws at most 3,000 pairs by the cap rule and says how many more there are.
  - Nothing is left out to make the page smaller (map version 7). Every arrow that touches a gene of the page is
    on it with its edge line. The rows of each gene's capped list also carry their reading. Every preview says
    "k of N shown" and links to the explorer, which has every reason in full. The stage logs the page's size and
    warns above 25 MB.
- **The validation report** (`validation/report.md`, section 10; `metrics.json`, key `direction`): the positive
  controls with their ranks, and per kind the arrows written against the false arrows the controls expect.
- **Response strength** (version 5): an arrow to *response to DRUG DOSE* is listed with the cells under that
  drug-dose (the look-ups' `dv.cells(gene)` and `dv.for_drugdose(dd)`), and `direction/selectivity.parquet` holds each
  drug-dose's selective lines and groups.

- **The look-ups.** `tahoe gene X` has a section PROBABLE DIRECTION: upstream, downstream, and the cells under drugs
  (10 rows per list by the same cap rule; `--top N` shows N, and a capped list names the `--top` that lists it all),
  each row with its evidence, its numbers, its alerts and notes as short labels, and its support. A drug target that
  the screen does not measure (such as NR3C1) has its own arrows: `tahoe gene NR3C1` lists them, and `tahoe pair
  NR3C1 GENE` gives the arrows between them with every alert, note and support reason in full. `tahoe line X` lists
  the line's recorded alterations and its natural knockouts, with the arrows that came out of each. `tahoe drug X`
  lists the arrows to the cells under its doses and its drug-target arrows. `tahoe pair A B` shows any arrow between
  the two genes, either way, with every alert, note and support reason in full, and the genes with an arrow to both. On a console that cannot show '→' or '⚠' (a Windows code page), they print as '->'
  and '!'.
- **The literature reviewers' dossiers** (`tahoe review`) end a gene's dossier with its arrows (upstream, downstream,
  cells, capped by the same rule, with the caveat), so that the reviewers can check them against the literature.

An output without this stage (made before it existed) still opens everywhere: the vault, the map, the look-ups, the
dossiers and section 10 of the validation report each say in one sentence that the direction stage has not run.

## How to read an arrow

An arrow, as the vault, the map and the look-ups write it (from the synthetic test data, where TP53 was planted; one
line, wrapped here):

```
TP53 → CDKN1A  [B]  TP53 activity strengthens CDKN1A's drug response (mutation: response; q 7e-04)  ⚠ KMT2D, CTNNB1
alterations on the other side; line-wide correction only  · notes: within organs, on part of the lines; loss of
function inferred (missense); heavily mutated comparison lines; TP53 not expressed in 2 of the 10 altered lines;
artifact flags; translation inhibitors; expected false under 1% (group)
```

- **TP53 → CDKN1A**: the source and the target. The target can be a gene, *cells under DRUG DOSE* (how many cells
  of each line remain under that drug-dose, relative to the other lines in the same wells) or *response to DRUG DOSE*
  (how strongly each line responds to it: how many genes move beyond the per-line cut, against the line's typical
  drug-dose).
- **[B]**: the [grade](#how-to-read-a-grade). It would be A (5 or more lines on each side, q < 0.05, compared within
  organs), but the lines it is compared against are largely the KMT2D- and CTNNB1-altered colon lines, so either of
  those alterations could be the cause (*KMT2D, CTNNB1 alterations on the other side*).
- **TP53 activity strengthens CDKN1A's drug response**: the **sign**, always the effect of the *source's activity*.
  For a level or the cells: *raises* or *lowers*. For a drug response or a response strength: *strengthens* or
  *weakens* - how strongly the target responds, **in its own direction**. CDKN1A rises under these drugs (2.95x), and
  less where TP53 is lost (1.32x), so TP53's activity strengthens the rise. For a target that *falls* under the drugs,
  *strengthens* means it falls further. Read which from **all** the drug-doses the arrow lists (`top_drugdoses`;
  `rise_share` is the share of the evidence from drug-doses where the target rises), not from the first. When each
  direction carries at least a quarter of the evidence the arrow is alerted *rises at some drug-doses, falls at
  others*. A natural knockout or a drug target is worded with *may*: *lines without MTAP have fewer cells under
  Pemetrexed 5 µM (MTAP may protect the cells)*, *compounds annotated to inhibit MTOR lower RPL3's level (MTOR's
  activity may raise it)* ([why](#d16-plain-non-causal-words-for-natural-knockouts-and-drug-targets)). *Not
  inferred*: the mechanism is not recorded, the drugs trap their target (a poison), the two genes lie at the same
  locus, or the gene belongs to an expression programme.
- **mutation: response**: the [kind of evidence](#the-kinds-of-evidence-from-strongest-to-weakest), here a recorded
  mutation of the source, tested against the target's drug response.
- **q 7e-04**: the Benjamini–Hochberg q over the whole table of its kind. For an arrow significant only within its own
  group, both are given: *q 0.243 over the table, 0.006 within its group* ([which q](#how-many-tests-and-which-q)).
- **⚠ ...**: the [alerts](#alerts-notes-caveats-and-support), as short labels: the reasons to doubt this arrow. The
  full reasons are in the evidence and in `direction/edges.parquet` (column `alerts`).
- **· notes: ...**: the notes, as short labels: reasons below the threshold at which they would be an alert, and
  context. Here: the comparison uses 7 of the 10 TP53-altered lines; loss of function is the metadata's inference and
  8 of the 10 lines carry a missense change; 4 of the 8 comparison lines are heavily mutated; TP53 is not expressed in
  2 of the 10; the artifact-flagged drug-doses carry 15% of the evidence; a translation inhibitor's drug-dose is among
  its 10 (carrying none of the evidence); random comparison groups give about 0.02 such arrows per group against this
  group's 9, so under 1% of them may be false. Column `notes` has them in full.
- Not on the line: the kind's **caveats**, stated once above each list (for example "every drug-target arrow: drugs
  can act on other proteins too"; for the mutation kinds: *over the whole table the controls expect 0.7 (up to 3.5) of
  the 9 arrows of this kind to be false*), and the **support** (column `support`).

The evidence behind it, in words (column `reading`): *CDKN1A responds less in the TP53-LoF lines than in the other
lines: 1.32x vs 2.95x at 5-Fluorouracil 5 µM; TP53 activity strengthens CDKN1A's drug response*. The comparison (column
`group`): *TP53 recorded as loss of function (10 lines: 8 with a missense change, 2 truncating, splice or deletion only)
vs not recorded (8)*.

**One test, several sources.** Some tests stand for several sources at once. Compounds that share several listed
targets give one result for all of those targets. Genes absent from exactly the same lines give one comparison. Every
edge carries `test_id` (one per distinct test) and `n_same_test`, and such an edge has the note *one test for 6 targets
(HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11): the same compounds give one result for each, the arrows are the same
evidence, counted once*. The vault, the map and the look-ups show such a test as one row that names every source, and
its alert says that any of them could be the cause. In the synthetic run, one class of HDAC inhibitors gives 55 rows
that each name HDAC1, HDAC2, HDAC3, HDAC8, HDAC10 and HDAC11 (330 edges), and the run's 891 edges make 409 rows.
`edges.parquet` keeps one edge per source; `info.json` `tests_written_by_kind` counts the distinct tests.

## What "direction" means here

The source is what the test **conditions on**. The target is what **differs with it**. The source can be:

- **A recorded mutation of the source gene** (by gene, or by allele: *KRAS p.G12C*, *KRAS codon G12*, a hotspot).
  The mutation was there before the experiment: it cannot be a consequence of the target.
- **The source gene's absence from some lines.** The lines that lack it are a natural knockout.
- **Compounds annotated to act on the source's protein** (by Tahoe or by ChEMBL). The drug acts on the source; the
  target's mRNA follows.
- **The source gene's natural level.** A weak hint only: its level is not set by the experiment.

The target can be another gene (its level: at baseline, or under the compounds for a drug target; or its response
to the drugs), the cells themselves (how many cells of the line remain under a drug-dose, relative to the other lines
in the same well), or the lines' **response strength** to a drug-dose (how many genes move beyond the per-line cut in
each line, against what that line's typical drug-dose moves).

## What an arrow does not say

- It is **not proof of direct regulation**. A → B → C looks like A → C: the test sees that the target follows the
  source, not how many steps lie between them. Another alteration carried by the same lines can be the real cause
  (the co-occurrence alerts name the ones the metadata records; the *heavily mutated lines* alert says when the
  altered lines carry many alterations).
- **"Not recorded" is not "wild type"**, and **"loss of function" is the metadata's inference**: a line may carry an
  unlisted variant, and a missense change can act dominant-negative or gain new functions (a note on every
  loss-of-function group where at least a third of the lines carry one).
- **Two genes at the same locus** are deleted or gained together: an arrow between them cannot tell which acts on
  which (*same locus*; sign not inferred). The same holds inside an **expression programme** (a gene absent from the
  same lines as more than 10 other line sets).
- There is **one time point** (~24 h). Fast and slow effects are mixed; compensation and feedback are not seen.
- **Drugs act on proteins**, not on mRNA, and a compound can act on other proteins than its listed target. A
  **poison** that traps its target on DNA (TOP1 / TOP2 poisons, PARP trappers) or freezes microtubules acts through
  the damage or the arrest it causes, not through less of its target: those arrows have no sign. A drug-target arrow
  says what the compounds do; it speaks of the source's activity only through the target the compounds are annotated
  for, hence *may*.
- An arrow from a gene's **natural level** comes from natural differences between lines. Tissue and other differences
  can produce the same pattern. And when one direction is stronger than the other, that can come from one gene's level
  being *measured more precisely* (or tracking a shared cause more closely), not from it acting first. Every level
  arrow carries that alert, and all of them are grade C: a glimpse.
- The **controls' counts of false arrows** are estimates from a small sample (each comes with its 95% upper bound),
  and they can be low where the real groups overlap other alterations, tissue programmes or each other.
- The lines are **cancer cell lines**: a dependence seen there need not hold in normal cells.

## The kinds of evidence, from strongest to weakest

### 1. Recorded genotype (`genotype_response`, `genotype_baseline`, `genotype_sensitivity`, `genotype_selectivity`; grade A, B or C)

For each driver gene recorded as altered in at least 3 screened lines, three groups are formed: loss of function,
gain of function, and "altered (any record)" when some records carry no mechanism. Each group is compared with the
lines that have no record of that gene (at least 3). The group's words give the altered lines' records: *TP53
recorded as loss of function (10 lines: 8 with a missense change, 2 truncating, splice or deletion only) vs not
recorded (8)*.

**Allele groups** (version 5). From the recorded protein changes (simple substitutions such as *p.G12C*; frameshifts,
deletions and synonymous changes are not alleles): every change recorded in at least 3 lines (*KRAS p.G12C*), every
codon whose line set differs from those changes (*KRAS codon G12 (6 lines: G12C 2, G12D 2, G12S 1, G12V 1)*), the
cited hotspots (PIK3CA E542K, E545K, H1047R, H1047L - Samuels Y et al. 2004, Science 304:554; TP53 missense at R175,
G245, R248, R249, R273, R282 - Baugh EH et al. 2018, Cell Death Differ 25:154) and amplifications (variant type
*Gain*, at least 3 lines; the README names those with fewer, such as *ERBB2 amplification: 1 line*). An allele group is
compared with every other recorded line, other alleles of the gene included: *KRAS p.G12C (6 lines) vs other lines
(44; 18 of them with another KRAS change)*. A group whose lines are exactly a gene group's is not added; that group's
words gain the composition (*BRAF recorded as gain of function (7 lines: 7 with a missense change; all p.V600E)*).

- **response**: does the target respond to its drugs less (or more) where the source is altered? The target's
  drug-doses are its 10 strongest pooled responses. The per-line response at each of them is compared between the
  two sides. The evidence of all 10 is combined, so a dependence carried by one drug class counts as much as one
  spread over all of them.
- **baseline**: is the target's level lower or higher where the source is altered?
- **sensitivity**: do the altered lines lose more or fewer cells under a drug-dose?
- **response strength** (`genotype_selectivity`, version 5): do the altered lines respond more or less strongly to a
  drug-dose - how many genes move beyond the per-line cut, against what the line's typical drug-dose moves
  (`tables/drug_line_response.parquet` rel_log2)? Tested at the drug-doses where at least one line responds
  selectively. The target reads *response to Adagrasib 0.5 µM*. Per compound, the other doses significant in the same
  group are support (*also at Adagrasib 5 µM (q 0.004) and 0.05 µM (q 0.03)*); a response seen at one dose only is
  alerted (*one dose only: Phenylephrine 5 µM is a single well; its other doses do not show it (p 0.6, 0.7)*) and is
  not graded A. `direction/selectivity.parquet` lists, per drug-dose, its selective lines, the organs they concentrate
  in and every group with such an arrow.

The null is built by shuffling which lines count as altered (200 times). When enough lines of the same organ sit on
both sides, lines are shuffled only within their organ. Every target's statistic is set against its own shuffled
values, and the shuffled values of all targets together form the null that gives the p-value. Its far tail is
fitted with a smooth curve, so a single very strong effect can still pass among millions of tests. Each target is
also checked against its own shuffles. If they disagree with the pooled null, the target's own p-value is used. This
happens for a target measured in few lines, or with few lines per organ. If a grouping shifts the whole genome (for
example, it coincides with broad differences between lines), the statistics are deflated by that inflation factor,
in the way genomic control works. Because the null is shared by all targets, a run where many genes differ strongly
between lines for other reasons gets a wider null, and its arrows are fewer and more conservative.

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

**Sign.** `+1` means the source's **activity** raises the target's level (or the cells' numbers), or strengthens its
drug response in the target's own direction, or the lines' response strength. For a loss-of-function group, that is
when the target is higher, or responds more strongly (rises more, or falls more), where the source is intact. For gain
of function the sign is reversed. For "altered (any record)", or an allele group whose records disagree on the
mechanism, it is not inferred (0); and it is 0 for two genes at the same locus.

**Organs.** When the lines are shuffled within organs, every shuffle keeps the organ make-up of the two sides. The
comparison is then between lines of the same organ, and no tissue alert is raised. Only lines in organs that hold
both sides carry it, and the alert says how many. When the comparison has to run across organs, the arrow says so.
It is called *tissue-confounded* when the two sides' organs differ more than chance, for example when most
KRAS-mutant lines are pancreatic; such an arrow is grade C, as for a natural knockout.

**Other alterations.** When another gene's altered lines overlap the altered side (*co-occurs with X*), or sit on the
other side (*X alterations on the other side*: the lines compared against are largely X-altered), X could be the
cause - with the same or the opposite sign. Either blocks grade A. On the synthetic data, as in real colon lines, the
TP53-intact colon lines are the KMT2D-mutant (MSI) ones. **Heavily mutated lines** (alterations recorded in 15 or
more driver genes) carry many recorded and unrecorded changes: when the altered side holds at least 2 of them at
twice their share among the other lines, every arrow of the group is alerted and none is graded A; when the
comparison side does, a note says so.

**The group's expected false share** (version 5). Random comparison groups (the pseudo-groups, below) give a number
of arrows per group of each kind. Each genotype arrow carries that number against its own group's arrows of the kind:
*random comparison groups give about 0.20 such arrows per group (up to 0.32); this comparison gives 25: about 1% of
them may be false (up to 1%)*. At 20% or more (as printed) it is an alert and the arrow is not grade A; below, a note.
Every genotype arrow also carries its kind's caveat: *over the whole table the controls expect 0.7 (up to 3.5) of the 9
arrows of this kind to be false (8%)*.

**Same locus** (version 5). Two genes within 1 Mb of each other on one chromosome are deleted or gained together. In
this screen, genes absent from the same lines are 109 times more often within 50 kb of each other than by chance, 15
times at 50-200 kb, 7.4 times at 0.2-0.5 Mb, 3.1 times at 0.5-1 Mb and 1.7 times at 1-2 Mb. A genotype or
natural-knockout arrow between two such genes (`distance_bp` <= 1,000,000: `same_locus`) has no sign and is grade C,
with the alert *same locus: CDKN2A lies 8 kb from CDKN2B (9p21.3); genes this close are deleted or gained together
...*. The same holds for a genotype group's target that is itself absent from most of the altered lines (*CDKN2A is
also absent from most of the CDKN2B-altered lines: a shared deletion can explain it*). The coordinates come from the
reference stage (Ensembl); `info.json` says for how many genes they were known.

Examples (from the synthetic test data, where TP53's effects were planted; the last one shows a doubtful arrow):

- *TP53 → CDKN1A, grade B, q 7e-04 over the whole table*: CDKN1A responds 1.32x vs 2.95x at 5-Fluorouracil 5 µM in
  the TP53-LoF lines vs the other lines ([above](#how-to-read-an-arrow)). Its alerts say that KMT2D alterations are
  in 4 of the 8 comparison lines and CTNNB1 alterations in 3, and in none of the 10 TP53-altered lines (so it is not
  grade A). They also say that at these drug-doses too few other genes respond to check for a resistance specific to
  the drugs, so only the lines' overall responsiveness was corrected.
- *TP53 → BAX, grade B, q 4e-05*: 1.14x vs 1.98x at Epirubicin 5 µM. Its extra alert: none of its drug-doses is
  significant pooled (a response only part of the lines show).
- *TP53 → PHLDA3, grade C*: 1.22x vs 2.09x at 5-Fluorouracil 5 µM; q 0.0035 within the TP53 group, 0.15 over the whole
  table. Its alert says it is a lead, not a finding.
- *TP53 → cells under Doxorubicin (hydrochloride) 5 µM, grade B, q 0.073*: 1.15x in the TP53-LoF lines vs 0.74x in
  the other lines; *TP53 activity lowers the cells' numbers (makes them more sensitive)*. The same holds at
  5-Fluorouracil and Topotecan 5 µM.
- *CDKN2B → CDKN2A, grade C, no sign*: CDKN2A is 8.78x lower at baseline in the CDKN2B-LoF lines; *CDKN2B and CDKN2A
  lie at the same locus: which acts on which cannot be told*. Version 4 read it as *CDKN2B activity raises CDKN2A's
  level* (grade C, for being tissue-confounded and significant only within its group). Version 5 adds why the
  direction itself cannot be read: CDKN2A lies 8 kb from CDKN2B (7,602 bp), CDKN2A is also absent from most of the
  CDKN2B-altered lines (one deletion takes both), and random groups give about 0.12 such within-group arrows per group
  against this group's 1 (*expected false 12%*, a note).

### 2. Natural knockouts (`null_response`, `null_baseline`, `null_sensitivity`, `null_selectivity`; grade B or C)

No mutation needed. Lines where a gene is not expressed at all, reading only the ambient RNA of the well, are
natural knockouts of it. A gene qualifies when at least 3 lines lack it and at least 3 express it. The same tests
as above are run, but only towards the gene's related partners (relations), not genome-wide. When the lines lacking
the gene cannot be compared with lines of the same organs, they are compared across organs, as a separate family of
tests, provided they are not concentrated in a few organs. A gene absent from whole organs would only restate the
tissue (related genes share tissue programmes). For such a gene, its partners' baseline and response are not
tested, but its effect on cell numbers is (tissue alert, grade C). The README of the run gives how many genes this
concerns (none when no such gene has related partners), and `groups.parquet`'s note says why for each. Genes absent
from exactly the same lines share one test: any of them could be the cause, and the alert names them all (also those
that are not a source of that row). Genes absent from most of the same lines (overlap 0.5 or more: co-deleted
neighbours such as MTAP and CDKN2A) are named too (*also absent*). When the lines lacking the gene carry a recorded
deletion of it, the alert says so (genotype evidence too).

A natural knockout is not an experiment on the gene, so the words say *may*: *lines without KRT15 have 2.05x less
SEMA4B at baseline than lines expressing KRT15 (KRT15 may raise SEMA4B's level)*. When more than 10 other line sets
overlap the lines lacking the gene (`programme_sets`), the gene belongs to an **expression programme**: its arrows
have no sign and are grade C (*an expression programme: 36 other line sets overlap the lines lacking KRT15 (overlap 0.5
or more): the direction is not identifiable*), and the reading says that the genes are co-expressed across lines.

Every natural-knockout arrow carries how much of it random genes would give (`nonspecific_share`, version 5): random
genes that are not partners of the gene, matched to its tested partners by level, are tested exactly like the partners
in 200 line sets drawn over five overlap bins, and *random genes that are not partners differ as much between these
lines in 2.1% of tests: about 2.5 of the 13 arrows of this gene would appear for any gene (19%)*. For the cells and the
response strength, 60 random line sets of the real sets' sizes give the same: *random line sets give about 0.05 such
arrows per set (up to 0.08); this set gives 3: about 2% of them would appear for any set of lines (up to 3%)*. At 20%
or more it is an alert, else a note.

Examples (synthetic data):

- *SYNTH0881 → SYNTH0313, grade B, q 8e-06*: *SYNTH0313 responds less in the lines without SYNTH0881 than in lines
  expressing SYNTH0881: 1.47x vs 3.29x at Dexamethasone 5 µM (SYNTH0881 may strengthen its drug response)*.
  SYNTH0881 was planted as a gene that 6 lines (in 4 organs) do not express, and whose 9 partners respond 0.25× as
  strongly there; all 9 come back at grade B, compared within organs, with a non-specific share under 1%.
- *SYNTH0483 → SYNTH0290, grade C, no sign*: SYNTH0290 is 7.48x lower at baseline in the lines without SYNTH0483; these
  lines also lack the genes of 11 other line sets (the planted programme): *co-expressed with SYNTH0483 across lines:
  which acts on which is not identifiable*.
- *MTAP → cells under Pemetrexed 5 µM, grade C*: 0.64x in the lines without MTAP vs 1.17x in lines expressing MTAP;
  *MTAP may protect the cells*. The alerts say it is tissue-confounded (3 of the 5 MTAP-null lines are pancreatic, 0
  of the 13 others), that it co-occurs with the CDKN2A / CDKN2B deletions (MTAP is deleted together with them), and
  that CDKN2A and CDKN2B are absent from most of these lines too (overlap 0.62 and 0.57): any of them could be the
  cause.

### 3. Drug targets (`drug_target`; grade B, C for poisons)

A target X annotated for at least 2 distinct compounds of one class. One molecule counts once, whatever its names:
salt forms, letter case and salt words are merged (the real drug list has 'Ixazomib' and 'Ixazomib citrate',
'Larotrectinib' and 'Larotrectinib sulfate', 'crizotinib' and 'Crizotinib (hydrochloride)'), and its names are joined
with ' / ' in `compounds`.

**Who is in the class** (version 5). A compound's targets and actions come from Tahoe's annotation and from ChEMBL's
curated mechanisms, side by side (`compounds_source`): one source lists the target - its action, labelled (*Clobetasol
propionate: ChEMBL (Glucocorticoid receptor agonist)*); Tahoe gives the target but no action and ChEMBL gives one -
ChEMBL's (*Triamcinolone: Tahoe target, action from ChEMBL*); both give different actions - 'unclear', alerted.
Tahoe's annotation is never changed. ChEMBL's targets count when they are a single protein, a protein family or a
chimeric protein; a protein complex (the 26S proteasome, the ribosome) lists every subunit while the drug binds one,
so it gives no membership. Every arrow of a class one of whose members has different targets in the two annotations
carries an alert (*Clobetasol propionate: Tahoe lists CYP3A5, CYP3A4 (inhibitor); ChEMBL lists NR3C1 (agonist)*).
The class is the action (inhibitor, activator, unclear), except for drugs that **trap** their target: TOP1 poisons,
TOP2 poisons, PARP trappers and microtubule stabilisers (`mechanism_class`, from `tahoemap/data/drug_classes.json`
and ChEMBL, each membership with its source in `mechanism_source`) form classes of their own, and microtubule
destabilisers are apart from the stabilisers. Without ChEMBL (offline, not cached) the classes come from the code
constants alone and `compounds_source` is empty.

**The test** (version 5: top-j). For each compound, its strongest pooled effect on Y that way over its drug-doses.
For j = 2, 3, ... up to the class's compounds significant that way (pooled q < 0.1 and >= 1.2x at any dose), m_j = how
many compounds of the screen move Y at least as strongly as the class's j-th strongest; p_j = the hypergeometric
chance that j or more of the class's N compounds are among those m_j. p = (N - 1) x the smallest p_j (a Bonferroni
over the thresholds). BH over every test where at least 2 compounds of the screen move Y that way. The arrow names
the j compounds (`n_top`, `compounds_supporting`, strongest first, then *also significant: ...*), m_j (`m_top`) and
the class (`class_size`); `contrast` is the median log2 fold of the j compounds.

The reading: *compounds annotated to activate NR3C1 raise FKBP5: 3 of 3 compounds, all 3 among the 4 of 357 compounds
that raise it most (median 10.4x; 10% of all compounds raise it) (NR3C1 activity may raise it)*. The sign is relative
to X's activity: an inhibitor that raises Y means X's activity may lower Y. A trap class has no sign and is grade C:
*compounds that trap TOP2A on DNA (TOP2 poisons: Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) raise
TP53 (3 of 5 compounds ...): an effect of the DNA damage they cause, not of less TOP2A activity*. The alerts name the
compounds, any other targets they share, compounds that also act on DNA directly, and an arrow that rests on 2
compounds only (*shared chemistry or another shared target can explain it*).

Examples (synthetic data):

- *compounds annotated to activate NR3C1 raise SYNTH0872: 4 of 4 compounds, all 4 among the 4 of 94 compounds that
  raise it most (median 6.82x; 13% of all compounds raise it)*, grade B, q 0.002. SYNTH0872 was planted as a gene that
  the glucocorticoids raise 6x and 20 other compounds raise a little: 13% of all compounds raise it, so the count test
  of version 4 (4 of 4 against 13%) is weaker than the top-j test, which sees that the 4 are the strongest. Triamcinolone
  joins the class by ChEMBL's action (Tahoe lists NR3C1 with an unclear action).
- *compounds annotated to inhibit MTOR lower SYNTH0185: 3 of 6 compounds, all 3 among the 3 of 94 compounds that lower
  it most (median 0.59x)*: *MTOR's activity may raise its level* (sign +1).
- *compounds annotated to inhibit HMGCR raise SYNTH0269: 2 of 2 compounds* (Pitavastatin, Pravastatin): *HMGCR's
  activity may lower its level* (sign -1).

### 4. Natural levels (`level`, `level_sensitivity`; grade C, a glimpse)

A gene's baseline level differs between lines. The question is whether the lines with more of X also show a
stronger response of Y, or fewer cells under a drug. Both the level and the response are first adjusted for organ
and for the main axes of variation between lines. The p-value comes from the t distribution, checked against
shuffled levels. For two related genes, both directions are tested, and each is written when it is significant
(both, when both are). X → Y is marked `direction_clear` only when it is stronger than Y → X *beyond what its
selection alone gives* (`p_direction` < 0.05): the arrow was written because its correlation passed the cut on these
lines, which inflates it (the winner's curse), so a plain comparison with the reverse would favour it. The test asks
how often two equally strong directions, with the forward one drawn so that it passes the same cut, give a gap this
large (at the least favourable common strength). Otherwise the arrow says *direction unclear*. Even when clear, read
it with care: if X's level simply tracks the shared cause more closely than Y's (or is measured more precisely),
X → Y wins without acting first. Every level arrow carries that alert.

Examples (synthetic data):

- *NFE2L2 → SYNTH0239*: *lines with more NFE2L2 (lineage-adjusted) show a stronger SYNTH0239 drug response (r +0.97;
  reverse +0.35)*, q 0.006, direction unclear (p 0.67). NFE2L2's natural level was planted to set how strongly 40 NRF2
  targets respond to dimethyl fumarate, auranofin and bortezomib, while NFE2L2 itself responds alike in every line.
  13 of the 40 come back, all with the right sign (r 0.93–0.97). With 18 lines every written correlation sits just
  above the cut (r about 0.93), so a gap to the reverse is mostly what selection alone gives: only NFE2L2 →
  SYNTH0736 (reverse -0.03) is called clear. No reverse arrow is, and neither is any of the other 3 of the run's 16
  level arrows, which are not among the planted answers (the shuffled-level control expects 3 false ones).
- *lines with more PSMD10 (lineage-adjusted) have fewer cells under Ixazomib 5 µM (r -0.95)*, q 0.03 over all gene ×
  drug-dose tests.
- *lines with more ACSL4 have fewer cells under Artesunate 5 µM (r -0.91)* is significant among the genes tested for
  that drug-dose (q 0.05) but not over all of them (q 0.20): a lead, and its alert says so.

With 18 lines, 10 degrees of freedom remain after the adjustment, so only very strong, broad effects pass (r about
0.93 or more, with many targets). The real 50 lines give much more power.

## What changed in version 5: old rule, new rule, why

Two independent reviews of the real results (50 lines, 1,132 drug-doses) found readings, signs and grades the
evidence did not support. Version 5 corrects them by code. For each change: the old rule, the new rule and the
reason, with the real numbers (measured on the published tables of the real run, where the direction stage of
version 2 had run: 102,590 edges, 11,874 of them drug_target, 17 genotype_response arrows at grade A). Nothing is
removed for doubt: an arrow whose reading was wrong gets the right reading, sign and grade, and every reason is shown.

### D1. Drugs that trap their target (poison classes)

- **Old rule**: a TOP2A drug-target class was "inhibitors of TOP2A", so *inhibiting TOP2A raises TP53* read as *TOP2A
  activity lowers TP53* (sign -1), grade B. The tubulin drugs formed one class whatever they do to microtubules.
- **New rule**: when a compound is in a 'trap' class for that target (`tahoemap/data/drug_classes.json`, each
  membership with its source: a cited code constant, a ChEMBL mechanism or a WHO ATC code) - TOP1 poisons, TOP2
  poisons, PARP trappers, microtubule stabilisers - its class is that trap class: no sign, grade C, and the reading
  says so: *compounds that trap TOP2A on DNA (TOP2 poisons: Amsacrine, Doxorubicin, Epirubicin, Idarubicin,
  Mitoxantrone) raise TP53 (3 of 5 compounds ...): an effect of the DNA damage they cause, not of less TOP2A
  activity*. Microtubule destabilisers form their own class ('inhibitor (microtubule destabiliser)', with the usual
  sign). Doxorubicin is a TOP2 poison, not a TOP1 poison, so its TOP1 listing is a TOP1 'inhibitor' class of one (not
  tested); the TOP1 poison class is Irinotecan and Topotecan. Arrows whose supporting compounds also act on DNA
  directly (intercalators, alkylators) say so.
- **Why**: a TOP2 poison traps TOP2A on DNA and breaks the DNA; the p53 targets rise because of the damage. Less TOP2A
  activity does not raise them. The pooled tubulin class was a wrong grouping (stabilisers and destabilisers act in
  opposite ways on microtubules): it is withdrawn and replaced by two classes, not dropped for doubt.
- **Real data**: TOP2A, TOP2B and TOP1 had 4,393 drug-target arrows with a sign at grade B under the old test (8,642
  under the top-j test with Tahoe's classes). With the classes of the code constants, all of them (8,535 under the stage's
  test family) have sign 0 and grade C; the TOP1 poison class (Irinotecan, Topotecan) gives 78.

### D3. The drug-target test uses how strongly each compound moves the gene (top-j)

- **Old rule**: Y is significant for k of the class's N compounds; a hypergeometric test of k against the share of all
  compounds significant for Y.
- **New rule**: the compounds are ranked by how strongly they move Y (each compound's strongest pooled z that way).
  For j = 2, 3, ..., the chance that j of the N class compounds are among the m_j strongest of the screen, m_j being the
  rank of the class's j-th strongest; the smallest such chance times N - 1 (Bonferroni over the thresholds). A test
  counts where at least 2 compounds of the screen move Y that way (as before). Columns `n_top`, `m_top`,
  `class_size`, `share_supporting` (the old k / N); `contrast` is now the median log2 fold of the supporting
  compounds, and lists in the look-ups break ties of q by that fold. Two compounds only: an alert (*supported by 2
  compounds only (Bortezomib, Ixazomib): shared chemistry or another shared target can explain it*).
- **Why**: a gene that many compounds move a little (FKBP5 is moved by 10% of all compounds) hid the 3 glucocorticoids
  that move it 10x: the count test gave FKBP5 q 0.13 (not an arrow). A pure rank-sum test was considered and
  rejected: it lost 2,038 of the old arrows, among them 817 MAP2K1 arrows where one of the MEK inhibitors (TAK-733) is
  inactive.
- **Real data** (Tahoe's classes, the published tables): FKBP5 q 0.0045, TSC22D3 0.0078, KLF9 0.0078, PER1 0.030,
  DUSP1 0.0083; PSMB5 → HSPA1A, HSPA1B, DNAJB1, BAG3 q 0.013 and PSMD1, PSMC4, PSMA1 0.0083 (the list starts CRYAB,
  KRT16, DYNC1I1, UBC, MLLT11); MAP2K1 → SPRY4 found. With the stage's test family (a test where at least 2 compounds
  of the screen move the gene): 52,744 drug-target arrows, 11,836 of the old 11,874 kept, 38 lost (MTOR 16, TOP2A 8,
  PIK3CA 7, PIK3CB 3, MAP2K1 3, KDR 1: their best threshold's Bonferroni). The reviewers counted every gene in the
  family (p = 1 where fewer than 2 compounds move it): 50,970 arrows, 11,818 kept, 56 lost (MTOR 17, TOP2A 12, PIK3CA
  8, MAP2K1 6, other 13); the stage keeps the old family because, on the synthetic data, counting every gene leaves no
  drug-target arrow at all without ChEMBL. These are method changes, not doubts.

### D4. Drug annotations from Tahoe and ChEMBL

- **Old rule**: Tahoe's targets and its broad mechanism alone.
- **New rule**: Tahoe's and ChEMBL's memberships side by side, labelled in `compounds_source` ([above](#3-drug-targets-drug_target-grade-b-c-for-poisons)); disagreements alerted; Tahoe's annotation never changed.
- **Why**: Clobetasol propionate, the strongest glucocorticoid of the screen, is listed by Tahoe as a CYP3A inhibitor;
  Triamcinolone and Methylprednisolone have no action in Tahoe's list.
- **Real data** (ChEMBL release 37): the NR3C1 activators go from 3 to 6 compounds (Clobetasol propionate,
  Triamcinolone and Methylprednisolone succinate join); 162 classes are tested (116 with Tahoe's alone); FKBP5 q 0.0004.

### D5. Grade A needs the data to back the arrow as a whole

- **Old rule**: A = a recorded genotype, >= 5 lines on each side, q < 0.05, within organs, no co-occurrence, and not
  resting on the global-sensitivity correction.
- **New rule**: also (a) the mean over all the target's drug-doses goes the arrow's way, with and without the
  correction (else *the mean over all 10 of its drug-doses goes the other way (contrast -0.64, without the correction
  -0.39; the TP53-LoF lines respond 1.09x as strongly overall): the arrow rests on its strongest drug-doses
  (Mitoxantrone 5 µM, Idarubicin 5 µM, TAK-901 5 µM)*); (b) less than half of the evidence goes the other way; (c)
  not a floor (*DDB2 mostly falls under these drugs and is 2.7x lower at baseline in the TP53-LoF lines: a smaller fall
  there can be a floor (less left to lose), not less regulation*); (d) the target measured in at least half of each
  side's lines; and (D6, D7) no high expected false share and no heavily mutated lines on the altered side.
- **Why**: ZMAT3's mean over its drug-doses went the other way, DDB2's smaller fall was a floor, GRIN2C was measured
  in fewer than half of a side's lines; all three were grade A. The reviewers also proposed '|retained - 1| >= 0.2'
  and 'other way < 25%'; they were not adopted, because they would demote the core p53 targets CDKN1A, RRM2B and FDXR.
- **Real data**: genotype_response grade A 17 → 14 (ZMAT3, DDB2, GRIN2C to B); 13 with D6 and D7 (POLE → PSPC1 to B).

### D6. The group's expected false share

- **Old rule**: the expected false arrows were given per kind over the whole table only.
- **New rule**: each genotype arrow also carries its group's share (`false_share`): the pseudo-groups' arrows per
  group (in the arrow's family: over the whole table, or within the group only) against the group's own arrows of the
  kind. At 20% or more (as printed): an alert, and no grade A. Every genotype arrow carries its kind's caveat.
- **Why**: one comparison with few arrows can be mostly chance even when the table as a whole is not.
- **Real data**: the TP53 response arrows about 1% (a note); POLE → PSPC1, BRCA2 → LRRN3, KMT2D → DUSP5, SETD1B →
  COL21A1 20% (an alert; POLE → PSPC1 from A to B); the FBXW7 and RB1 within-group baseline arrows 22% (an alert).

### D7. Heavily mutated lines

- **New rule**: a line recording alterations in 15 or more driver genes is heavily mutated (real data: HCT15 25,
  HEC-1-A 21, LS 180 19, RKO 19, LoVo 18, SW48 17, AN3 CA 16; the next, NCI-H1573, 14). When the altered side holds
  at least 2 of them at twice their share among the other lines: *heavily mutated lines: 3 of the 8 POLE-altered lines
  (AN3 CA, HCT15, RKO) record alterations in 15 or more driver genes, against 4 of the 42 others: such lines carry many
  recorded and unrecorded changes, and any of them, or the mutation load itself, could be the cause* - an alert, no
  grade A. The comparison side so enriched: a note.
- **Why**: such lines (microsatellite-unstable or POLE-mutant) carry hundreds of unrecorded changes.
- **Real data**: 40 of 64 groups alerted, 19 arrows; TP53's group gets the note.

### D8. Counting the p53 control

- **Old rule**: a p53 target counted as recovered when its arrow had sign +1.
- **New rule**: it also needs its evidence from rises (rise_share >= 0.5) and the mean contrast agreeing; the others
  are listed (`edge_not_counted`, with `why_not`: *evidence from falls (rise_share 0.00): the p53 targets rise under
  DNA damage*; *the mean contrast goes the other way (-0.64)*; *wrong sign*).
- **Real data**: 22 → 19 recovered (ZMAT3, DDB2, PHLDA3 listed as an edge not counted).

### D9. Same locus

- **Old rule**: none: *CDKN2B → CDKN2A* read *CDKN2B activity raises CDKN2A's level*.
- **New rule**: [above](#1-recorded-genotype-genotype_response-genotype_baseline-genotype_sensitivity-genotype_selectivity-grade-a-b-or-c): within 1 Mb, sign 0, grade C; a genotype group's target absent from most altered lines: grade C (version 6: only within 1 Mb of the source, [V6-2](#v6-2-a-co-absent-target-is-a-shared-deletion-only-near-the-source)).
- **Why**: genes absent from the same lines are 109x more often within 50 kb of each other than by chance (15x at 50-
  200 kb, 7.4x at 0.2-0.5 Mb, 3.1x at 0.5-1 Mb, 1.7x at 1-2 Mb): a deletion takes both.
- **Real data**: CDKN2B → CDKN2A and CDKN2B → ENSG00000264545 from B to C, sign 0; null_baseline 1,663 arrows (618
  from B to C); null_response 27 (23 from B to C).

### D10. Expression programmes

- **Old rule**: a natural knockout whose lines overlap many other line sets had a note (*also absent ... (and N more
  line sets)*) and its usual sign and grade.
- **New rule**: more than 10 overlapping line sets (Jaccard >= 0.5): sign 0, grade C, *an expression programme: N
  other line sets overlap the lines lacking X (overlap 0.5 or more): the direction is not identifiable*; the reading:
  *SEMA4B is 2.05x lower at baseline in the lines without KRT15 than in lines expressing KRT15; these lines also lack
  the genes of 36 other line sets (a shared expression programme): KRT15 and SEMA4B are co-expressed across lines, and
  which acts on which cannot be told*.
- **Why**: partners of a gene absent with more than 600 other line sets differ between these lines 15.2% of the time,
  against 2.6% with 10 or fewer, while random non-partners differ 1.9-2.7% throughout: the arrow then reflects a shared
  programme, not the gene.
- **Real data**: null_baseline 69,849 arrows; grade B 38,332 → 8,589; null_response B 2,026 → 276; null_sensitivity B
  4,194 → 530.

### D12, D13. Allele groups and response strength

- **Old rule**: genotype groups by gene only; no arrow to how strongly lines respond.
- **New rule**: allele, codon, hotspot and amplification groups; the selectivity kinds ([above](#1-recorded-genotype-genotype_response-genotype_baseline-genotype_sensitivity-genotype_selectivity-grade-a-b-or-c)).
- **Why**: KRAS G12C lines respond to the G12C inhibitor adagrasib, other KRAS-mutant lines do not (Hallin J et al.
  2020, Cancer Discov 10:54); a gene-level KRAS group cannot show it.
- **Real data**: 64 → 76 groups (KRAS G12C, G12D, G12V, codon G12; NRAS Q61K, Q61R; PIK3CA E545K and the hotspots;
  TP53 R273H, codon R273, codon R248, hotspot missense). Expected on the user's run (it needs the per-line tensor): KRAS
  p.G12C → response to Adagrasib at 0.5 and 5 µM; TP53 → response to about 14 DNA-damaging drug-doses (sign +1);
  single-dose glucocorticoid-like responses (Phenylephrine 5, Econazole 5, Citalopram 0.05 µM) marked *one dose only*.

### D16. Plain, non-causal words for natural knockouts and drug targets

- **Old rule**: *SYNTH0881 activity strengthens SYNTH0313's drug response*; *inhibiting MTOR lowers RPL3*.
- **New rule**: *lines without SYNTH0881 show a weaker SYNTH0313 drug response (SYNTH0881 may strengthen it)*;
  *compounds annotated to inhibit MTOR lower RPL3 ... (MTOR activity may raise it)*. The genotype readings keep
  *TP53 activity strengthens ...*.
- **Why**: a line that lacks a gene is not an experiment on that gene, and a compound acts on more than its listed
  target: the words should not claim more than the test shows.

### The other additions

- **D2** one test, several sources: `test_id`, `n_same_test`, the note; `info.json` `tests_written_by_kind` (real:
  11,874 drug-target arrows = 8,846 distinct tests under the old test).
- **D11** the natural knockouts' random controls ([controls](#controls-how-much-to-trust-it)); real estimate: about
  28% of the null_baseline arrows would appear for random genes too.
- **D14** `gene_tests.parquet`: each gene's tests and arrows per kind and role.
- **D15** group words with the composition; the missense note.
- **D17** translation inhibitors' share of a response's evidence (`ti_share`): *drug-doses of translation inhibitors
  carry 64% of the evidence (Homoharringtonine 0.5 µM, Harringtonine 5 µM; ...): blocking translation stabilises
  short-lived mRNAs, so a rise there may not be more transcription*. An alert at 50% or more or when the strongest
  drug-dose is one; no sign or grade change. The class (homoharringtonine, harringtonine and other ribosome blockers)
  comes from `drug_classes.json`; Tahoe's 'Protein synthesis inhibitor' label is not used (it also covers MNK / eIF4E
  inhibitors, which do not block the ribosome).

## What changed in version 6: old rule, new rule, why

Each changed reading or grade says so on the arrow itself, in its notes: *rule changed in direction version N: before,
... Now ..., because ...* or *grade A blocked since direction version N: ... (without this rule the arrow would be grade
A)*. The words come from the same constants as this page and the stage README (`tahoemap/direction.py`).

### V6-1. A baseline arrow needs the target expressed on both sides for grade A

- **Old rule** (version 5): the grade-A conditions of D5 applied to response arrows only; a baseline arrow could be
  grade A whatever the share of lines that do not express the target.
- **New rule**: grade A for a `genotype_baseline` arrow also needs the target expressed in more than 75% of each
  side's lines (`BASE_ABSENT_A` = 0.25: the share of a side's lines without it that blocks A). Such an arrow gets the
  alert *Y is not expressed in a of the A altered lines and i of the I others: present in some lines and absent in
  others, so the level difference can follow lineage rather than regulation*, and the note *grade A blocked since
  direction version 6*.
- **Why**: on the real data *TP53 → GRIN2C* (not expressed in 13 of the 33 TP53-altered lines, 1 of the 17 others;
  median 1.3 vs 8.8 CPM) and *TP53 → ACTA2* (11 of 33 vs 0 of 17) were grade A baseline arrows (*TP53 activity raises
  GRIN2C's level*), while the version 5 rule had already taken the GRIN2C response arrow down to B for the same reason.

### V6-2. A co-absent target is a shared deletion only near the source

- **Old rule** (version 5, D9): a genotype group's target absent from most altered lines read *a shared deletion can
  explain it* and was grade C, whatever the distance between the two genes.
- **New rule**: that reading and grade C only when the target lies within 1 Mb of the source on one chromosome
  (`CODELETION_BP`, the same-locus distance), or when coordinates are missing. Otherwise the alert says *lineage, or
  the loss of the source itself, can explain it*, gives both sides' counts, names a known target of the source
  (`P53_TARGETS`, `NRF2_TARGETS` in `tahoemap/direction.py`), and the arrow keeps its grade (at most B, by V6-1).
- **Why**: *TP53 → EDA2R* (EDA2R on Xq12, TP53 on 17p13; EDA2R is a p53 target, absent from 22 of the 33
  TP53-altered lines and 6 of the 17 others) is the expected effect of losing p53, not a deletion. The intended case
  *CDKN2B → CDKN2A* (8 kb apart, absent together from 12 of 13 lines) keeps grade C.

### V6-3. Every changed arrow says what it read before

- **Old rule**: the arrows gave only the new reading and its reason.
- **New rule**: a note on each arrow that a version 5 or 6 rule reads differently: trap classes (*before, these
  compounds were read as inhibitors of TOP2A: 'TOP2A activity lowers POLH' (sign -1, grade B). Now the sign is not
  inferred (sign 0, grade C), because TOP2 poisons act through the DNA damage they cause*), same locus, expression
  programmes, distant co-absence, and the stricter grade-A rules (D5, D6, D7, V6-1: *grade A blocked since direction
  version 5: ...*). Notes never change a grade or a sign.
- **Why**: a reader who saw the earlier published arrows (for example *ZMAT3*, *DDB2* and *GRIN2C* at grade A, or
  *TOP2A activity lowers TP53*) can tell from the arrow itself what changed and why.

## How to read a grade

- **A** (strong): a recorded genotype, at least 5 lines on each side (sharing an organ with the other side), q < 0.05
  over the whole table, compared within organs, no co-occurrence alert either way, no heavily mutated lines
  concentrated on the altered side, and fewer than 20% of the group's arrows of the kind expected false. For a
  response also: not resting on the global-sensitivity correction, the mean over all its drug-doses going its way
  with and without the correction, less than half of the evidence the other way, not a floor, measured in at least
  half of each side's lines. For a baseline level also (version 6): the target expressed in more than 75% of each
  side's lines. For a response strength: seen at 2 or more doses. The strongest kind of directional evidence this
  data can give; read any alert or note it still carries.
- **B** (read its alerts): a genotype result over the whole table with alerts (another alteration on a side, compared
  across organs, the mean going the other way, ...) or only 3–4 lines on a side; a natural knockout with at least 5
  lines lacking the gene; a drug-target result by action. Worth taking seriously.
- **C** (a glimpse): levels; genotype results significant only within their own group, or tissue-confounded; a
  genotype target absent from most altered lines that lies within 1 Mb of the source (or without coordinates); natural
  knockouts with 3–4 lines, absent from whole organs, co-absent with the target, or inside an expression programme;
  any genotype or natural-knockout arrow between two genes at the same locus; a drug-target class that traps its
  target. A lead to check, not a finding.

## Alerts, notes, caveats and support

Every reason the stage writes is kept and shown in full; none is removed. Each reason is in exactly one of four
columns of `edges.parquet`, and `alerts_all` holds all of them in the order the stage wrote them. A rule in the code
(`direction.reason_tier`) decides the column; nobody sorts them by hand.

| Column | What it holds | How to read it |
|---|---|---|
| `alerts` (⚠) | A doubt about this arrow, or a graded reason at or past its threshold. | Read before you trust the arrow. An arrow with no alert carries no ⚠. |
| `notes` | A graded reason below its threshold, and context. | Shown muted, in full. Not a doubt about this arrow by itself, but read it. |
| `caveats` | The same text on every arrow of a kind. | Stated once above each list, not on every row. |
| `support` | Evidence for the arrow. | Read it as support, not as doubt. |

The caveats of each kind:

- `drug_target`: drugs can act on other proteins too (*off-target possible*);
- `level`: tissue and other differences between lines can mimic it (*tissue can mimic it*), and a stronger correlation
  one way can reflect how precisely each gene's level is measured (*precision caveat*);
- `level_sensitivity`: tissue can mimic it;
- the genotype kinds (version 5): the false arrows the controls expect over the whole table, per family (*over the
  whole table the controls expect 0.7 (up to 3.5) of the 9 arrows of this kind to be false (8%)*; label *controls:
  expected false (kind)*). These come from the rows themselves, so a list states the ones its rows carry.

The support: *consistent across N compounds (...)* (drug targets); *the lines lacking X carry a recorded loss of X:
genotype evidence too* (natural knockouts; label *deletion recorded too*); *also at Adagrasib 5 µM (q 0.004)* (a
response strength seen at other doses; label *also at other doses*).

Always notes (version 5): *loss of function is the metadata's inference; 8 of the 10 lines carry a missense change ...*
(*loss of function inferred (missense)*); *4 of the 8 comparison lines are heavily mutated (...)* (*heavily mutated
comparison lines*); *one test for 6 targets (HDAC1, ...)* (*one test for 6 targets*).

**Graded reasons.** Eight reasons are an alert only past a fixed threshold, and a note below it. The thresholds are
constants in `tahoemap/direction.py` and are listed in `direction/README.md` and `info.json` (`reason_tiers`).

| Reason (short label) | Constant | An alert when | Otherwise a note, because |
|---|---|---|---|
| *Y measured in a of the A and i of the I lines* (*target measured in part of the lines*) | `NOTE_MEASURED_FRAC = 0.75` | fewer than 5 measured lines on a side, or fewer than 75% of a side's lines | a few lines without the target cost little when most are measured |
| *supporting drug-doses with artifact flags (N% of the evidence)* (*artifact flags*) | `NOTE_ART_SHARE = 0.5` | the flagged drug-doses carry at least 50% of the evidence (`art_share`), or the strongest supporting drug-dose is one of them (the text then says *the strongest among them*) | the arrow rests mostly on unflagged drug-doses |
| *compared within organs: a of the A ... and i of the I others share an organ* (*within organs, on part of the lines*) | `NOTE_WITHIN_ORGAN_FRAC = 0.5` | fewer than half of either side share an organ with the other side | a within-organ comparison costs lines, not validity |
| *other genes are absent from most of these lines too ... (and N more line sets)* (*also absent*) | `NOTE_COABSENT_SETS = 10` | 10 or fewer line sets overlap in all: a candidate co-deletion (every set is then named) | many genes share the pattern: a tissue programme rather than one deletion (the 3 closest sets are named, the others counted) |
| *X itself is not expressed in k of the n altered lines* (*X not expressed in k of the n altered lines*) | `NOTE_NOT_EXPRESSED_FRAC = 0.25` | k is more than a quarter of n | a few deleted or silenced lines leave most of the comparison intact |
| *drug-doses of translation inhibitors carry N% of the evidence* (*translation inhibitors*) | `NOTE_TI_SHARE = 0.5` | they carry at least 50% (`ti_share`), or the strongest supporting drug-dose is one of them; a drug-target arrow whose supporting compounds all are | the rise rests mostly on drug-doses that do not block translation |
| *random comparison groups give about E such arrows per group ...: about N% of them may be false* (*expected false N% (group)*) | `FALSE_SHARE_ALERT = 0.2` | N is 20 or more (as printed; and the arrow is not grade A) | random groups would give few of this group's arrows |
| *... would appear for any gene (N%)* / *... would appear for any set of lines* (*non-specific N%*) | `FALSE_SHARE_ALERT = 0.2` | N is 20 or more | random genes or random line sets would give few of these arrows |

Lists inside a reason are never cut. *The supporting compounds also share ...* names every shared target. *Co-occurs
with ...* names every co-occurring gene (the same genes as `cooccurs_with` in `groups.parquet`). *Another gene's
alterations sit on the other side ...* names every such gene. *N other gene(s) are absent from exactly these lines
(...)* names all N.

How `art_share` is computed: for each of the target's 10 strongest drug-doses, the contrast between the two sides (z
units). `art_share` = the sum of |contrast| over the drug-doses with an artifact flag (toxic, transcription drop,
cell-cycle shift, ...) / the sum over all 10. The artifact reason lists every flagged drug-dose among the 10, and
`drugdoses_all` lists all 10 with their contrast, folds and flags. For a drug-target arrow, the share is that of the
supporting compounds whose strongest drug-dose is flagged.

**Every other reason is an alert** (short label in brackets):

- few lines (*few lines (3 vs 15)*); tissue-confounded (*tissue-confounded*); compared across organs (*across
  organs*); the lines' organs not known (*organs unknown*);
- co-occurs with another gene's altered lines (*co-occurs*); another gene's altered lines sit on the other side
  (*X alterations on the other side*: X may be the cause, with the opposite sign); either blocks grade A;
- genes absent from exactly the same lines (*co-absent genes*); the lines counted as lacking the gene still read part
  of its level (*maybe low, not absent*); the target also absent from most of these lines (*co-absent with the
  target*);
- the target much lower at baseline in the altered lines (*lower baseline (lost expression?)*: a lost response may
  be lost expression);
- the global-sensitivity correction: the difference exists only relative to the other responding genes (*rests on the
  correction*), the reference differs between the sides, no correction (*partly uncorrected*), or only a line-wide
  one (*line-wide correction only*) at the drug-doses carrying the difference;
- the difference goes the other way at some drug-doses (*both ways*); the target rises at some drug-doses and falls
  at others (*rises at some drug-doses, falls at others*);
- its own permutation p used; none of its drug-doses significant pooled; mechanism not recorded (*sign not
  inferred*, *mechanism partly not recorded*); the cells' counts less trustworthy at the drug-dose;
- significant only within its group or drug-dose (*within its group only (a lead)*);
- drug targets: targets that share the compounds (*shared targets*: any of them could be the cause); the compounds are
  poisons (*poison: sign not inferred*); they also act on DNA (*also act on DNA*); supported by 2 compounds only (*2
  compounds only*); Tahoe's and ChEMBL's annotations disagree (*annotations disagree*);
- version 5: the mean over all drug-doses goes the other way (*mean goes the other way*); a floor (*floor*); heavily
  mutated lines on the altered side (*heavily mutated lines*); same locus (*same locus*); the target absent from most
  altered lines (*co-absent with the target*); an expression programme (*programme: direction not identifiable*); one
  dose only (*one dose only*);
- levels: direction unclear (the reverse is not clearly weaker once the arrow's selection is allowed for).

What this means for a list: the warning sign tells arrows apart. In the synthetic test run, 16 of the 891 edges carry
no alert (11 drug-target, 2 level and 3 level-sensitivity arrows). A list capped at N shows the N strongest
and, after them, any of the N strongest without an alert; every list says how many rows it holds, how many carry ⚠
and how many carry notes, for example *9 arrows, 9 with ⚠, 9 with notes; grade A 0, B 2, C 7*.

An output made before these tiers existed (direction version 2) is still read: there, every reason counts as an
alert, as it did then.

The note Concepts/Probable direction of the vault lists the alert, note and support labels of the run, each with its
count and one reason in full.

## How many tests, and which q

Thousands of genes are tested against every group, so a few false arrows are expected. Two q-values are reported:

- `q`: over the **whole table** of the kind (for example every gene against every genotype group). Grades A and B
  need it below 0.10.
- `q_group`: within the arrow's **own group** (one genotype, or one drug-dose for `level_sensitivity`). Genotype
  and `level_sensitivity` arrows are written when it is below 0.10. When `q` is not, the arrow is grade C, and its
  alert says so and gives the number of such arrows that random groups produce.

So grade A/B arrows are significant both in their group and over the whole table. Grade C arrows of these kinds are
leads: they hold up within their group, and the controls tell you how many of them to expect by chance.

The drug-target family counts a test (a class, a direction, a gene) where at least 2 compounds of the screen move the
gene that way: elsewhere no class can reach 2 supporting compounds. Every gene's tests are counted in
`gene_tests.parquet`: per gene, kind and role (source or target), its tests, its arrows (any grade, and A or B) and
the size of the kind's family, so an arrow can be read against how often its gene was tested.

## Controls: how much to trust it

`controls.json` reports four kinds of control; the vault's Probable direction note and section 10 of
`validation/report.md` show them for the run.

- **Positive.** TP53 → the p53 target genes: how many are found and their ranks among all genes. A target counts as
  recovered when its arrow has sign +1, its evidence comes from rises (rise_share 0.5 or more: the p53 targets rise
  under DNA damage) and its mean contrast agrees; every other tested target says why not (`why_not`), and the arrows
  not counted are listed (`edge_not_counted`). TP53 → cells under DNA-damaging drugs (expected: TP53 activity makes
  the cells more sensitive; a drug counts by a Tahoe target or as a TOP1 / TOP2 poison or a drug acting on DNA, each
  with its source). TP53 → the response strength to those drugs (expected sign +1: the intact lines respond more).
  KRAS p.G12C → the response to Adagrasib (expected sign +1 at 2 or more doses; Hallin J et al. 2020, Cancer Discov
  10:54), when a KRAS p.G12C group can be formed and Adagrasib is screened. KEAP1 → the NRF2 target genes at baseline,
  when KEAP1 is recorded in enough lines.
- **Negative.** 60 random "pseudo-genotypes": random line sets with sizes spread over those of the real groups
  (small and large alike, allele groups included), which resemble no recorded group and no large natural-knockout line
  set. They are tested exactly like the real groups and counted at the real table's cut. Their arrows per group, times
  the number of real groups, is the number of **false arrows to expect**. It is reported per kind next to the real
  counts, with its 95% upper bound: the controls are a small sample, and no false arrow from 60 random groups still
  allows about 3 per 60 groups. It is also in `info.json`, and in the README, which warns when random groups do as
  well as the real ones. The estimate can be low where the real groups overlap other alterations or each other,
  which random groups do not. Where the controls expect about half or more of a kind's arrows to be false, the vault
  and the report mark that kind with ⚠: read those arrows as leads. Version 5 also gives each genotype arrow its
  group's share (`false_share`, [D6](#d6-the-groups-expected-false-share)).
- **Natural knockouts** (version 5, `null_controls`). For the partners' baseline and response: 300 random genes that
  are not partners, per line set, in up to 200 real line sets drawn evenly over five overlap bins (10 or fewer other
  line sets overlapping, 11-50, 51-200, 201-600, more than 600), matched to the set's tested partners by level and
  tested exactly like them: the share of them that would be an arrow, per bin, and per arrow `nonspecific_share`. For
  the cells and the response strength: 60 random line sets with the real sets' sizes. `expected_false_edges` gives
  `expected_nonspecific` (baseline, response) and `expected_false` with its upper bound (cells, response strength).
- **Levels.** The same level tests with every gene's level shuffled over its lines (one shuffle, with its upper
  bound): the arrows a run without any real level effect would give.

The drug-target arrows have no random control; each arrow's alerts say what to doubt.

On the synthetic test data (18 lines, seed 0, the default; `python tests/run_tests.py` and `python
tests/test_direction.py`), the planted answers come back:

- TP53 → the p53 targets: 16 of the 22 planted p53 targets come back, every one with the right sign; 9 are
  significant over the whole table (grade B, as the KMT2D / CTNNB1-altered lines sit on the other side), 7 within the
  TP53 group only (grade C). The control counts 16 (TIGAR, planted to fall under two drugs in the TP53-intact lines, is
  not counted: *evidence from falls (rise_share 0.00)*); 18 of its 28 targets rank in the top 5% of all genes. The
  other 30 TP53 response arrows are planted too: 27 go to the one-dose plant's genes, which Bergenin 5 µM raises in
  the TP53-intact lines only.
- TP53 → cells under Doxorubicin, Topotecan and 5-Fluorouracil (5 µM), grade B, and Topotecan 0.5 µM (grade C), all
  with the expected sign. TP53 → response to Bergenin 5 µM (the one-dose plant) carries the *one dose only* alert.
- Selectivity: KRAS codon G12 → response to Trametinib at 0.05 and 0.5 µM, the two planted doses (sign +1, q_group
  0.019, each naming the other dose as support).
- NFE2L2's natural level → 13 of its 40 planted targets with the right sign (2 with the direction clear; no reverse
  or unplanted arrow called clear). SYNTH0881's natural knockout → 9 of its 9 partners, grade B, non-specific share
  under 1%. The planted expression programme (12 genes, each absent from 6 of the same 8 lines) gives no sign and grade
  C to all its arrows.
- PSMD10 → Ixazomib (q 0.03) and ACSL4 → Artesunate (a lead within its drug-dose); MTAP-null → Pemetrexed (grade C,
  tissue-confounded).
- Drug targets: NR3C1 → 10 of the 10 planted glucocorticoid genes and the promiscuous one (4 of 4 compounds, all among
  the 4 strongest, q 0.002; Triamcinolone in the class by ChEMBL's action); MTOR → 7 of the 40 planted ribosome genes
  (those moved by 3 of the 6 inhibitors; those moved by 2 do not pass the family); HMGCR → 11 of 12 cholesterol genes;
  each with the sign relative to the target's activity. The TOP1 poison class is Irinotecan and Topotecan, the TOP2
  poison class the five TOP2 drugs, and the microtubule stabilisers are never in one class with the destabilisers. The
  planted TOP2 poisons (the p53 genes x3 in the TP53-intact lines, x2 in the others, so that the median line moves)
  give *compounds that trap TOP2A on DNA ... raise CDKN1A* and *... MDM2*, both without a sign and grade C.
- Same locus: CDKN2B → CDKN2A (7,602 bp apart) has no sign and is grade C. Allele groups: KRAS codon G12 (6 lines),
  KRAS G13D (DLD-1, HCT116, LoVo), PIK3CA E545K and hotspot, TP53 R273H and hotspot; the KRAS G12C lines (2) are too
  few. The 5 heavily mutated colon lines (DLD-1, HCT116, RKO, LoVo, SW48) alert every group whose altered side holds
  2 or more of them.
- Random pseudo-groups give 1 arrow over the whole table (0.7 expected over the 44 groups, up to 3.5) and 0.02–0.23
  within-group leads per group. The shuffled levels give 1 level arrow, against the 17 written.

The planted genes with strong line-to-line differences also widen the shared null of the genotype tests: with them,
the TP53 arrows are fewer and their q larger than without them. With 18 lines the power is limited; with the real 50
lines it is higher.

The test also builds full-dimension outputs (1,132 drug-doses × 50 lines in 16 organs, 2,000–16,643 genes) with
planted effects and checks they are found there. These are a genotype-dependent programme, a natural knockout's
partner effects, a lone natural-knockout effect on cell numbers, and a level modulator with its direction. It checks
that a line-wide resistance, a programme that dominates its drug-doses and random driver groups give no false grade-A
arrows, and (version 5, at 2,000 genes) that the genotype-dependent programme stays grade A (39 of 40) while a target
whose mean over its drug-doses goes the other way, a floor target and a target measured in fewer than half of the
altered lines are written but not graded A, each with its reason.

At the full 16,643 genes (direction version 4):

- the programme comes back (39 of 40 genes, grade A);
- the knockout's partners: 30 of 30 responses and 13 of 15 baseline levels;
- the lone knockout effect on cell numbers: q 5e-5 among 6.2 million tests;
- the level modulator: 30 of 30 partners, 28 of them with the direction clear (the test allows for each arrow's
  selection); no reverse arrow is called clear;
- KEAP1 → 7 of 7 NRF2 targets.

The line-wide resistance gives no arrow. Random driver groups give 11 arrows over the whole table, where the
pseudo-groups predict about 6: the controls' estimate can be low where real groups overlap other drivers (here
hypermutated lines carry many of them). Random pseudo-groups are never tissue-confounded with 16 organs. A weaker
effect, such as a 2.5× lower baseline in 12 knockout lines, is not enough for half a million tests (p ~1e-6 to 1e-4): it
stays out of the table. That is the price of controlling false arrows over the whole table.

## The files

`OUT/direction/` (its `README.md` lists every column, and this run's counts and controls):

- `edges.parquet`: one edge per row. `source`, `target` (a gene, `cells under DRUG DOSE` or `response to DRUG DOSE`
  with `target_dd` = the drug-dose row), `kind`, `grade`, `sign`, `reading` (the edge in words), `group` (the
  comparison), the line counts (`n_altered`, `n_intact`, `n_lines`), the effect (`contrast` and, by kind,
  `retained_fraction`, `raw_share`, `baseline_log2_diff`, `r`, `r_reverse`, `direction_clear`, `p_direction`; for drug
  targets `n_compounds`, `n_supporting`, `background_rate`, `compounds`, `compounds_supporting`, `drug_effect`,
  `mechanism_class`, `mechanism_source`, `compounds_source`, `n_top`, `m_top`, `class_size`, `share_supporting`), `T`,
  `p`, `q`, `q_group`, `top_drugdoses` (the drug-doses carrying the difference), `drugdoses_all` (every drug-dose
  behind the arrow, with its flags), `art_share`, `ti_share`, the version 5 columns (`expected_false_group`,
  `group_edges`, `false_share`, `false_share_upper`, `distance_bp`, `same_locus`, `programme_sets`,
  `nonspecific_share`, `allele`, `doses_supporting`, `n_doses_supporting`, `test_id`, `n_same_test`), and the
  reasons: `alerts`, `notes`, `caveats`, `support`, `alerts_all` (all of them, in order) with their counts
  `n_alerts`, `n_notes`, `n_caveats`, `n_support`.
- `groups.parquet`: every comparison group (genotype by gene or allele, natural knockout, pseudo-group): its lines on
  each side, organs, whether it was compared within organs, `allele`, `n_heavily_mutated_altered` /
  `n_heavily_mutated_intact`, `overlapping_line_sets`, its `alerts`, `notes` and `alerts_all`, and how many edges it
  gave per kind (written, any grade; for a pseudo-group, counted at the real cut and not written).
- `selectivity.parquet` (version 5): one row per drug-dose - its selective lines (every one), how selective it is
  (the 3rd-largest sel_z), the organs its selective lines concentrate in, and every group with a selectivity arrow to
  it (q, and whether other doses agree).
- `gene_tests.parquet` (version 5): per gene, kind and role, its tests and arrows.
- `controls.json`: the positive and negative controls, the natural knockouts' random controls and the expected false
  edges per kind, with their 95% upper bounds.
- `info.json`: the counts per kind and grade, the groups and tests (`tests_written_by_kind`: the distinct tests among
  the arrows), the same-locus check (for how many genes the coordinates were known), the cuts, the settings, the
  grade-A constants, peak memory and minutes, and `reason_tiers` (how many edges carry an alert, a note, a caveat,
  support; the edges without an alert by kind; the thresholds).

The method in full is the module docstring of `tahoemap/direction.py`; the stage's own options (memory per chunk,
permutations, pseudo-groups) are those of `python -m tahoemap.direction --help`, and `tahoe run` uses their defaults.
