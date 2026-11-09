# Direction: which gene probably acts on which

The relations stage links genes that respond alike. That link has no direction: CDKN1A and MDM2 rise together, but
the cosine does not say that both follow TP53. The **direction** stage adds arrows **SOURCE → TARGET**: which gene
probably acts on which, or on how many cells of a line remain under a drug. It is computed by code from the run's own
tables and the cell lines' recorded genetics; nothing is edited by hand. Every arrow:

- comes from a statistical test, with a p-value and a Benjamini–Hochberg q. A pair without such a result (q < 0.10
  in its family of tests) is not an arrow;
- carries a **grade** (A, B or C) and its **alerts**, each doubt in plain words. Nothing that passes is dropped
  because of doubt: a doubtful arrow keeps its place, with '⚠' and the reason, and a lower grade;
- is a **probable** direction, from 50 cancer cell lines at one time point. It is not proof that the source regulates
  the target directly ([what an arrow does not say](#what-an-arrow-does-not-say)).

The strongest evidence is the cell lines' **recorded mutations** (loss or gain of function): a mutation was there
before the experiment, so it cannot be a consequence of the target, and that is what makes the arrow point one way.
**Without any known mutation**, three other sources give a glimpse of the direction: lines that do not express a gene
at all (natural knockouts), compounds that target a gene's protein, and a gene's natural level across the lines.

Contents: [Running it](#running-it) · [Where you see the arrows](#where-you-see-the-arrows) ·
[How to read an arrow](#how-to-read-an-arrow) · [What an arrow does not say](#what-an-arrow-does-not-say) ·
[The kinds of evidence](#the-kinds-of-evidence-from-strongest-to-weakest) · [Grades](#how-to-read-a-grade) ·
[Alerts](#alerts) · [How many tests, and which q](#how-many-tests-and-which-q) ·
[Controls](#controls-how-much-to-trust-it) · [Files](#the-files)

## Running it

The stage is part of the pipeline. `tahoe run` runs it after `graph`; `validate`, `vault` and `map` come after it
and show its arrows:

```
build → effects → tensor → tables → embed → reference → relations → graph → direction → validate → vault → map
```

- **An output that finished before this stage existed**: after updating the code (`tahoe update`, or `git pull` in
  the code folder on Windows), `tahoe run` runs `direction`, `validate`, `vault` and `map`, and also any earlier stage
  whose method changed since the output was made (`tahoe` alone shows the plan first, with the reason). An output made
  with exactly the code before this stage gets `next: direction -> validate -> vault -> map` (about 10–12 minutes on
  the full data, an estimate); one made with older code also redoes `tables`, `embed`, `reference`, `relations` and
  `graph` (about 15–25 minutes, with embed's ~6.8 GB of memory). The build, the effects and the tensor are kept.
- **Alone, in the foreground**: `tahoe direction` (Windows:
  `C:\tahoe\.venv\Scripts\python.exe -m tahoemap direction --out C:\tahoe\out`). Like any stage run again, it marks
  `validate`, `vault` and `map` out of date, and the next `tahoe run` redoes them.
- **No option is needed.** The cell lines' genetics come from Tahoe-100M's `metadata/cell_line_metadata.parquet`: in
  the data folder (`--data`), in a streamed build's own copy of the metadata, or else the file the build indexed
  (`atlas/file_index.json`). Without the metadata (or without relations, drug targets or cell numbers) the kinds of
  evidence that need it have nothing to test, and the stage still finishes.
- **Time and memory** at full scale (16,643 genes × 1,132 drug-doses × 50 lines): about 6–7 minutes and 1.3–1.8 GB
  of memory on 4 CPUs. These are estimates: they were measured on generated outputs of the full size
  (`tests/test_direction.py`), because the stage has not yet run on the real data. `info.json` (and
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
    evidence (with the lines on each side), the effect, q and the alerts. It is capped at 12 rows. When the gene has
    arrows, its *At a glance* names the strongest one each way, and the frontmatter counts them
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
  - To stay under its size limit, a very large page first leaves out the readings of the grade C rows, then other
    long texts; an arrow between two genes is never left out, and the page says what it shortened.
- **The validation report** (`validation/report.md`, section 8; `metrics.json`, key `direction`): the positive
  controls with their ranks, and per kind the arrows written against the false arrows the controls expect.

- **The look-ups.** `tahoe gene X` has a section PROBABLE DIRECTION: upstream, downstream, and the cells under drugs
  (10 rows per list by the same cap rule; `--top N` shows N, and a capped list names the `--top` that lists it all),
  each row with its evidence, its numbers and its alerts as short labels. A drug target that the screen does not measure
  (such as NR3C1) has its own arrows: `tahoe gene NR3C1` lists them, and `tahoe pair NR3C1 GENE` gives the arrows
  between them with every alert in full. `tahoe line X` lists the line's recorded alterations and its natural knockouts,
  with the arrows that came out of each. `tahoe drug X` lists the arrows to the cells under its doses and its
  drug-target arrows. `tahoe pair A B` shows any arrow between the two genes, either way, with every alert in full, and
  the genes with an arrow to both. On a console that cannot show '→' or '⚠' (a Windows code page), they print as '->'
  and '!'.
- **The literature reviewers' dossiers** (`tahoe review`) end a gene's dossier with its arrows (upstream, downstream,
  cells, capped by the same rule, with the caveat), so that the reviewers can check them against the literature.

An output without this stage (made before it existed) still opens everywhere: the vault, the map, the look-ups, the
dossiers and section 8 of the validation report each say in one sentence that the direction stage has not run.

## How to read an arrow

An arrow, as the vault, the map and the look-ups write it (from the synthetic test data, where TP53 was planted; one
line, wrapped here):

```
TP53 → CDKN1A  [B]  TP53 activity strengthens CDKN1A's drug response (mutation: response; q 0.025)  ⚠ within organs,
on part of the lines; KMT2D, CTNNB1 alterations on the other side; TP53 not expressed in 2 of the 10 altered lines;
line-wide correction only; artifact flags
```

- **TP53 → CDKN1A**: the source and the target. The target can be a gene, or *cells under DRUG DOSE*: how many cells
  of each line remain under that drug-dose, relative to the other lines in the same wells.
- **[B]**: the [grade](#how-to-read-a-grade). It would be A (5 or more lines on each side, q < 0.05, compared within
  organs), but the lines it is compared against are largely the KMT2D- and CTNNB1-altered colon lines, so either of
  those alterations could be the cause (*KMT2D, CTNNB1 alterations on the other side*).
- **TP53 activity strengthens CDKN1A's drug response**: the **sign**, always the effect of the *source's activity*.
  For a level or the cells: *raises* or *lowers*. For a drug response: *strengthens* or *weakens* - how strongly the
  target responds, **in its own direction**. CDKN1A rises under these drugs (3.00x), and less where TP53 is lost
  (1.32x), so TP53's activity strengthens the rise. For a target that *falls* under the drugs, *strengthens* means it
  falls further: the source deepens the fall, i.e. represses it there. Read which from **all** the drug-doses the
  arrow lists (`top_drugdoses`; `rise_share` is the share of the evidence from drug-doses where the target rises),
  not from the first: a target can rise under some drugs and fall under others. When each direction carries at
  least a quarter of the evidence the arrow is alerted *rises at some drug-doses, falls at others*, and its sign then
  says how strongly the target responds, not whether the source induces or represses it.
  *Not inferred*: the mutation's mechanism is not recorded. For cells: *lowers the cells' numbers (makes them more
  sensitive)* or *raises them (protects the cells)*.
- **mutation: response**: the [kind of evidence](#the-kinds-of-evidence-from-strongest-to-weakest), here a recorded
  mutation of the source, tested against the target's drug response.
- **q 0.025**: the Benjamini–Hochberg q over the whole table of its kind. For an arrow significant only within its own
  group, both are given: *q 0.243 over the table, 0.006 within its group* ([which q](#how-many-tests-and-which-q)).
- **⚠ ...**: the [alerts](#alerts), as short labels; the full reasons are in the vault's and the map's evidence and
  in `direction/edges.parquet` (column `alerts`).

The evidence behind it, in words (column `reading`): *CDKN1A responds less in the TP53-LoF lines than in the other
lines: 1.32x vs 3.00x at 5-Fluorouracil 5 µM; TP53 activity strengthens CDKN1A's drug response*. The comparison (column
`group`): *TP53 loss of function (10 lines) vs not recorded (8)*.

**One test, several sources.** Some tests stand for several sources at once. Compounds that share several listed
targets give one result for all of those targets. Genes absent from exactly the same lines give one comparison. The
vault, the map and the look-ups show such a test as one row that names every source, and its alert says that any of
them could be the cause. In the synthetic run, one class of HDAC inhibitors gives 50 rows that each name HDAC1, HDAC2,
HDAC3, HDAC8, HDAC10 and HDAC11 (300 edges), and the run's 506 edges make 233 rows (the vault counts them as 233
arrows). `edges.parquet` keeps one edge per source.

## What "direction" means here

The source is what the test **conditions on**. The target is what **differs with it**. The source can be:

- **A recorded mutation of the source gene.** The mutation was there before the experiment: it cannot be a
  consequence of the target.
- **The source gene's absence from some lines.** The lines that lack it are a natural knockout.
- **Compounds that target the source's protein.** The drug acts on the source; the target's mRNA follows.
- **The source gene's natural level.** A weak hint only: its level is not set by the experiment.

The target can be another gene (its level: at baseline, or under the compounds for a drug target; or its response
to the drugs) or the cells themselves (how many cells of the line remain under a drug-dose, relative to the other
lines in the same well).

## What an arrow does not say

- It is **not proof of direct regulation**. A → B → C looks like A → C: the test sees that the target follows the
  source, not how many steps lie between them. Another alteration carried by the same lines can be the real cause
  (the co-occurrence alerts name the ones the metadata records).
- **"Not recorded" is not "wild type"**. The metadata lists driver alterations, and a line may carry one that is not
  listed. The comparison is "altered" against "no record of that gene".
- There is **one time point** (~24 h). Fast and slow effects are mixed; compensation and feedback are not seen.
- **Drugs act on proteins**, not on mRNA, and a compound can act on other proteins than its listed target. A
  drug-target arrow says what the compounds do; it speaks of the source's activity only through the target the
  compounds are listed for.
- An arrow from a gene's **natural level** comes from natural differences between lines. Tissue and other differences
  can produce the same pattern. And when one direction is stronger than the other, that can come from one gene's level
  being *measured more precisely* (or tracking a shared cause more closely), not from it acting first. Every level
  arrow carries that alert, and all of them are grade C: a glimpse.
- The **controls' counts of false arrows** are estimates from a small sample (each comes with its 95% upper bound),
  and they can be low where the real groups overlap other alterations, tissue programmes or each other.
- The lines are **cancer cell lines**: a dependence seen there need not hold in normal cells.

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
drug response in the target's own direction. For a loss-of-function group, that is when the target is higher, or
responds more strongly (rises more, or falls more), where the source is intact. For gain of function the sign is
reversed. For "altered (any record)" it is not inferred (0).

**Organs.** When the lines are shuffled within organs, every shuffle keeps the organ make-up of the two sides. The
comparison is then between lines of the same organ, and no tissue alert is raised. Only lines in organs that hold
both sides carry it, and the alert says how many. When the comparison has to run across organs, the arrow says so.
It is called *tissue-confounded* when the two sides' organs differ more than chance, for example when most
KRAS-mutant lines are pancreatic; such an arrow is grade C, as for a natural knockout.

**Other alterations.** When another gene's altered lines overlap the altered side (*co-occurs with X*), or sit on the
other side (*X alterations on the other side*: the lines compared against are largely X-altered), X could be the
cause - with the same or the opposite sign. Either blocks grade A. On the synthetic data, as in real colon lines, the
TP53-intact colon lines are the KMT2D-mutant (MSI) ones.

Examples (from the synthetic test data, where TP53's effects were planted; the last one shows a doubtful arrow):

- *TP53 → CDKN1A, grade B, q 0.025 over the whole table*: CDKN1A responds 1.32x vs 3.00x at 5-Fluorouracil 5 µM in
  the TP53-LoF lines vs the other lines ([above](#how-to-read-an-arrow)). Its alerts say that KMT2D alterations are
  in 4 of the 8 comparison lines and CTNNB1 alterations in 3, and in none of the 10 TP53-altered lines (so it is not
  grade A), and that TP53 itself is not expressed in 2 of the 10 altered lines (deletions). They also say that at
  these drug-doses too few other genes respond to check for a resistance specific to the drugs, so only the lines'
  overall responsiveness was corrected.
- *TP53 → BAX, grade B, q 0.092*: 1.12x vs 1.89x at 5-Fluorouracil 5 µM. Its extra alert: none of its drug-doses is
  significant pooled (a response only part of the lines show).
- *TP53 → XPC, grade C*: 0.87x vs 1.73x at 5-Fluorouracil 0.5 µM; q 0.010 within the TP53 group, 0.38 over the whole
  table. Its alert says it is a lead, not a finding, and that random groups give about 1.9 such arrows over the 38
  groups.
- *TP53 → cells under Doxorubicin (hydrochloride) 5 µM, grade B, q 0.063*: 1.15x in the TP53-LoF lines vs 0.74x in
  the other lines; *TP53 activity lowers the cells' numbers (makes them more sensitive)*. The same holds at
  5-Fluorouracil and Topotecan 5 µM.
- *CDKN2B → CDKN2A, grade C*: CDKN2A is 8.78x lower at baseline in the CDKN2B-LoF lines. The alerts say why not to
  believe it as written. It is significant only within its group. It is tissue-confounded (3 of the 6 CDKN2B-altered
  lines are pancreatic, 0 of the 12 others), which alone makes it grade C. And the two genes are deleted together
  (co-occurs with CDKN2A-altered lines). The controls agree: random groups give about 4.4 such within-group arrows of
  this kind, against the 1 written, and the vault and the report mark the kind with ⚠.

### 2. Natural knockouts (`null_response`, `null_baseline`, `null_sensitivity`; grade B or C)

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

Examples (synthetic data):

- *SYNTH0881 → SYNTH0313, grade B, q 2e-06*: *SYNTH0313 responds less in the lines without SYNTH0881 than in lines
  expressing SYNTH0881: 1.47x vs 3.29x at Dexamethasone 5 µM; SYNTH0881 activity strengthens SYNTH0313's drug
  response*.
  SYNTH0881 was planted as a gene that 6 lines (in 4 organs) do not express, and whose 9 partners respond 0.25× as
  strongly there; all 9 come back at grade B, compared within organs.
- *MTAP → cells under Pemetrexed 5 µM, grade C*: 0.64x in the lines without MTAP vs 1.17x in lines expressing MTAP;
  *MTAP activity protects the cells*. The alerts say it is tissue-confounded (3 of the 5 MTAP-null lines are
  pancreatic, 0 of the 13 others), that it co-occurs with the CDKN2A / CDKN2B deletions (MTAP is deleted together
  with them), and that CDKN2A and CDKN2B are absent from most of these lines too (overlap 0.62 and 0.57): any of them
  could be the cause. The CDKN2A- and CDKN2B-null rows under Pemetrexed name MTAP the same way.

### 3. Drug targets (`drug_target`; grade B)

A target annotated for at least 2 distinct compounds of one mechanism (inhibitor, activator, or unclear). One molecule
counts once, whatever its names: salt forms, letter case and salt words are merged (the real drug list has 'Ixazomib'
and 'Ixazomib citrate', 'Larotrectinib' and 'Larotrectinib sulfate', 'crizotinib' and 'Crizotinib (hydrochloride)'), and
its names are joined with ' / ' in `compounds`. If a gene moves the same way under at least 2 of them, more often than
under compounds in general (Fisher's exact test), the arrow reads "inhibiting X raises / lowers Y". The sign is relative
to X's activity: an inhibitor that raises Y means X's activity lowers Y. The edge names the class's compounds
(`compounds`), those that move Y that way (`compounds_supporting`) and what they do to Y's level (`drug_effect`). Alerts
name the compounds and any other targets they share.

Examples (synthetic data):

- *activating NR3C1 raises SYNTH0033 (3 of 3 compounds; 4% of all compounds)*, grade B, q 0.021: *NR3C1 activity
  raises SYNTH0033's level* (Betamethasone dipropionate, Budesonide, Dexamethasone).
- *inhibiting MTOR lowers SYNTH0185 (3 of 6 compounds; 3% of all compounds)*: *MTOR activity raises SYNTH0185's
  level* (sign +1; Everolimus, Rapamycin and Temsirolimus of the six).
- *inhibiting HMGCR raises SYNTH0151 (2 of 2 compounds)*: *HMGCR activity lowers SYNTH0151's level* (sign -1;
  Pitavastatin, Pravastatin).

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

## How to read a grade

- **A** (strong): a recorded genotype, at least 5 lines on each side (sharing an organ with the other side), q < 0.05
  over the whole table, compared within organs, no co-occurrence alert either way (another gene's altered lines on
  the same side, or on the other side); for a response, not resting on the global-sensitivity correction. The
  strongest kind of directional evidence this data can give; any alert it still carries is a note to read.
- **B** (read its alerts): a genotype result over the whole table with alerts (another alteration on a side, compared
  across organs, ...) or only 3–4 lines on a side; a natural knockout with at least 5 lines lacking the gene; a
  drug-target result. Worth taking seriously.
- **C** (a glimpse): levels; genotype results significant only within their own group, or tissue-confounded; natural
  knockouts with 3–4 lines, absent from whole organs, or co-absent with the target. A lead to check, not a finding.

## Alerts

Every doubt is written out in plain words, in column `alerts` ('⚠ ' + the reasons, '; '-joined). The vault and the
map show each reason by a short label, with the full reason in the evidence or the tooltip. The alerts you will meet
(short label in brackets):

- few lines (*few lines (3 vs 15)*); tissue-confounded (*tissue-confounded*); compared across organs (*across
  organs*); compared within organs on part of the lines (*within organs, on part of the lines*);
- co-occurs with another gene's altered lines (*co-occurs*); another gene's altered lines sit on the other side
  (*X alterations on the other side*: X may be the cause, with the opposite sign); either blocks grade A;
- the source itself is not expressed in some altered lines (*TP53 not expressed in 2 of the 10 altered lines*:
  deletion or silencing); a recorded deletion in the lines that lack the gene (*deletion recorded too*); genes absent
  from exactly the same lines (*co-absent genes*), or from most of them (*also absent: ...*);
- the target is much lower at baseline in the altered lines (*lower baseline (lost expression?)*: a lost response may
  be lost expression); the target measured in only some lines;
- the global-sensitivity correction: the difference exists only relative to the other responding genes (*rests on the
  correction*), the reference differs between the sides, no correction (*partly uncorrected*), or only a line-wide
  one (*line-wide correction only*) at the drug-doses carrying the difference;
- its own permutation p used; artifact flags of the supporting drug-doses (*artifact flags*); none of its drug-doses
  significant pooled; mechanism not recorded (*sign not inferred*);
- significant only within its group or drug-dose (*within its group only (a lead)*);
- drug targets: drugs act on other proteins too (*off-target possible*), the number of compounds, targets that share
  the compounds (*shared targets*);
- levels: tissue and other differences can mimic it (*tissue can mimic it*), the measurement-precision caveat
  (*precision caveat*), direction unclear (the reverse is not clearly weaker once the arrow's selection is allowed
  for).

The note Concepts/Probable direction of the vault lists the labels of the run, each with its count and one reason in
full.

## How many tests, and which q

Thousands of genes are tested against every group, so a few false arrows are expected. Two q-values are reported:

- `q`: over the **whole table** of the kind (for example every gene against every genotype group). Grades A and B
  need it below 0.10.
- `q_group`: within the arrow's **own group** (one genotype, or one drug-dose for `level_sensitivity`). Genotype
  and `level_sensitivity` arrows are written when it is below 0.10. When `q` is not, the arrow is grade C, and its
  alert says so and gives the number of such arrows that random groups produce.

So grade A/B arrows are significant both in their group and over the whole table. Grade C arrows of these kinds are
leads: they hold up within their group, and the controls tell you how many of them to expect by chance.

## Controls: how much to trust it

`controls.json` reports three kinds of control; the vault's Probable direction note and section 8 of
`validation/report.md` show them for the run.

- **Positive.** TP53 → the p53 target genes: how many are found, with the right sign, and their ranks among all
  genes. TP53 → cells under DNA-damaging drugs (expected: TP53 activity makes the cells more sensitive). KEAP1 → the
  NRF2 target genes at baseline, when KEAP1 is recorded in enough lines.
- **Negative.** 60 random "pseudo-genotypes": random line sets with sizes spread over those of the real groups
  (small and large alike), which resemble no recorded group and no large natural-knockout line set. They are tested
  exactly like the real groups and counted at the real table's cut. Their arrows per group, times the number of real
  groups, is the number of **false arrows to expect**. It is reported per kind next to the real counts, with its 95%
  upper bound: the controls are a small sample, and no false arrow from 60 random groups still allows about 3 per
  60 groups (about 1.9 over 38 real groups). It is also in `info.json`, and in the README, which warns when random
  groups do as well as the real ones. The estimate can be low where the real groups overlap other alterations or
  each other, which random groups do not (see the full-scale results below). Where the controls
  expect about half or more of a kind's arrows to be false, the vault and the report mark that kind with ⚠: read
  those arrows as leads.
- **Levels.** The same level tests with every gene's level shuffled over its lines (one shuffle, with its upper
  bound): the arrows a run without any real level effect would give.

The natural knockouts and the drug-target arrows have no random control; each arrow's alerts say what to doubt.

On the synthetic test data (18 lines, seed 0, the default; `python tests/run_tests.py` and `python
tests/test_direction.py`), the planted answers come back:

- TP53 → the p53 targets: 9 come back, every one with the right sign, and every TP53 response arrow is a p53 target. 2
  are significant over the whole table (CDKN1A, q 0.025, and BAX, q 0.092: grade B, as the KMT2D / CTNNB1-altered
  lines sit on the other side), 7 within the TP53 group only (grade C). 16 of the 22 planted p53 targets rank in the
  top 5% of all genes.
- TP53 → cells under Doxorubicin, Topotecan and 5-Fluorouracil (5 µM), grade B, and Topotecan 0.5 µM (grade C), all
  with the expected sign.
- NFE2L2's natural level → 13 of its 40 planted targets with the right sign (1 with the direction clear; no reverse
  or unplanted arrow called clear). SYNTH0881's natural knockout → 9 of its 9 partners, grade B.
- PSMD10 → Ixazomib (q 0.03) and ACSL4 → Artesunate (a lead within its drug-dose); MTAP-null → Pemetrexed (grade C,
  tissue-confounded).
- The glucocorticoid (NR3C1), MTOR and statin (HMGCR) drug classes, each with the sign relative to the target's
  activity.
- Random pseudo-groups give no arrow over the whole table (up to 1.9 per kind over the 38 groups at the 95% bound),
  and 0.05–0.12 within-group leads per group. The shuffled levels give 3 level arrows (up to 7.75), against the 16
  written.

The planted genes with strong line-to-line differences also widen the shared null of the genotype tests (see
[above](#1-recorded-genotype-genotype_response-genotype_baseline-genotype_sensitivity-grade-a-b-or-c)): with them,
the TP53 arrows are fewer and their q larger than without them. With 18 lines the power is limited; with the real 50
lines it is higher.

The test also builds full-dimension outputs (1,132 drug-doses × 50 lines in 16 organs, 4,000–16,643 genes) with
planted effects and checks they are found there. These are a genotype-dependent programme, a natural knockout's
partner effects, a lone natural-knockout effect on cell numbers, and a level modulator with its direction. It checks
that a line-wide resistance, a programme that dominates its drug-doses and random driver groups give no false grade-A
arrows.

At the full 16,643 genes:

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

- `edges.parquet`: one edge per row. `source`, `target` (a gene, or `cells under DRUG DOSE` with `target_dd` = the
  drug-dose row), `kind`, `grade`, `sign`, `reading` (the edge in words), `group` (the comparison), the line counts
  (`n_altered`, `n_intact`, `n_lines`), the effect (`contrast` and, by kind, `retained_fraction`, `raw_share`,
  `baseline_log2_diff`, `r`, `r_reverse`, `direction_clear`, `p_direction`; for drug targets `n_compounds`,
  `n_supporting`, `background_rate`, `compounds`, `compounds_supporting`, `drug_effect`), `T`, `p`, `q`, `q_group`,
  `alerts`, `n_alerts`, `top_drugdoses` (the drug-doses carrying the difference).
- `groups.parquet`: every comparison group (genotype, natural knockout, pseudo-group): its lines on each side, organs,
  whether it was compared within organs, its alerts, and how many edges it gave (written, any grade; for a
  pseudo-group, counted at the real cut and not written).
- `controls.json`: the positive and negative controls and the expected false edges per kind, with their 95% upper
  bounds.
- `info.json`: the counts per kind and grade, the groups and tests, the cuts, the settings, peak memory and minutes.

The method in full is the module docstring of `tahoemap/direction.py`; the stage's own options (memory per chunk,
permutations, pseudo-groups) are those of `python -m tahoemap.direction --help`, and `tahoe run` uses their defaults.
