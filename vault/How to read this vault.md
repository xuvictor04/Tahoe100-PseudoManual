---
type: "index"
tags: ["index", "help"]
generated_by: "tahoemap"
---

# How to read this vault

Everything here is generated from one run of **tahoemap** on [[Tahoe-100M]], except the written sections (a
gene's "In one line / What it is / What is uncertain / References", and the Concepts notes), which come from
`tahoemap/vault_seed/`. Generated notes are rebuilt on every run: do not edit them; write in `vault_seed/` instead.

The written gene sections come from an **earlier study on the same data** (MG53/TRIM72 and p53). Where one
speaks of a score, a rank, a regulon, an association or "this batch", it means that study's analysis
(transcription-factor activity inferred from target sets, with MG53 as the exposure), which tahoemap does **not**
compute; such sections carry a "Written for the earlier MG53/p53 study" callout (40 in this vault). This run's
own numbers are always in the generated sections.

## The baseline of every fold change

Every fold change is relative to **the same cell line's median over the plate's drug wells** — the typical treated
well, since most drugs leave most genes alone — **not DMSO** (two DMSO wells per plate are too few). For each line
and well: log2 CPM minus that line's plate median, minus the profile's composition (library-size) shift, minus the
well-position effect. So "2× up" means "twice the level of a typical drug well on that plate, in the same line".
*Pooled* values take the median over the lines in each well, then the mean (fold) or a Stouffer sum (z) over the
drug-dose's wells; *per-line* values keep each line. fold = 2^lfc (1 = no change, 0.5 = halved).

*Pooled* means the **median over the cell lines**: a response seen in fewer than about half of the measured lines
(for example one confined to the TP53-wild-type lines) does not reach the pooled lists, the "raised / lowered by"
counts or `tables/drug_effects.parquet`. It appears in the per-line tables (`tables/line_effects.parquet`,
`tables/drug_line_top.parquet`) and in a note's "In which cell lines" section.

## Which lines are measured for a gene

A cell line is **measured** for a gene (`tensor/line_measured.npy`; `expressed` in `tables/line_effects.parquet`;
`n_lines_expressing` in the frontmatter) only when it truly expresses it: at least 25% of the median line (the
atlas's rule) **and** at least 0.25 × the gene's pooled level. Every well also holds ambient RNA, the average
of all its cells, so a line that does not make the gene still reads about a tenth of the pooled level; that reading
moves with the other lines and with cell loss, not with the line's own regulation. Such **ambient-only** lines have no
per-line values ("n.m." = not measured, in a note). A per-line value is also left out where the profile's **expected
count** of the gene (the line's level × the profile's total UMI ÷ 10⁶) is below 2: with 0-1 expected reads
the log2 CPM is the pseudocount and a single read, and a line thinned out by a drug would show false rises. So the
number of lines measured can differ between drug-doses, and re-expression of a gene that a line has silenced is not
seen.

## z, q, significant, clean

- **z** — a robust z against the spread of this gene over the other drug wells on reliable plates (median and
  1.4826 × MAD), Stouffer-combined over the drug-dose's wells and divided by the plate factor on noisy plates. Most
  drug-doses sit in **one well**, so z rests on the spread of other wells, not on replicates.
- **q** — Benjamini–Hochberg within the gene, across all drug-doses (q_up for a rise, q_down for a fall).
- **Significant** — q < 0.10 and a change of at least 1.2× (the atlas's rule).
- **Clean** — no artifact flag on the drug-dose for this gene (a `cell-cycle shift` counts only where it explains
  the gene's change, see below), and none of the gene's own ("position correction uncertain"). Artifact flags:
  `toxic`, `transcription drop`, `cell-cycle shift`, `unreliable plate only`, `position not correctable`, `position correction uncertain`, `wells disagree`. They mark changes that may come from cell death, a global drop in transcription, a
  shift in the cell-cycle mix, a plate that does not reproduce, or a well-position problem — not regulation of the
  gene. Soft caveats that do **not** make a value unclean: `low cells (technical?)`, `plate-row cell shift`,
  `composition shift`, `noisy plate (z scaled)`, `position effect removed`. The exact definitions are in
  `docs/method.md` of the tahoemap repository.
- **Flagged, and the alert ⚠** — nothing is left out of a list, a table or a count because of a flag. A drug-dose
  (or a partner, a well, a single-line cell) that carries a reason for doubt stays in its ranked place and is marked
  **⚠** followed by the reason in plain words, e.g. `⚠ toxic; transcription drop` or `⚠ cell-cycle shift, explains
  ~60% of this change`. Read such a row as "something may have happened to the cells", not as regulation of the
  gene; but read it: a strong, replicated change at a flagged drug-dose can be real. Counts say how many there are
  in all and how many carry an alert. A list capped at N shows the N strongest and also any of the N strongest
  without an alert that rank below them, all in one order, so flagged rows never push unflagged ones out of view.
  Where an estimate leaves technically broken data out (e.g. cell counts of drug-doses whose wells disagree), the
  note says so next to the number.
- **The cell-cycle shift, gene by gene** — `cell-cycle shift` is a flag of the drug-dose: its cells moved into or
  out of S or G2/M (the S-phase and G2/M modules' pooled change). A gene's change at such a drug-dose may then only
  reflect the new mix of phases — for genes that go with the cell cycle. The tables stage measures how much a gene
  goes with it: its slopes on the two modules, fitted over the drug-doses without another artifact flag
  (`cc_slope_S` / `cc_slope_G2M` in `tables/genes.parquet`), and per row the share of the gene's change that the
  drug-dose's shift would explain with those slopes (`cc_share` in `tables/drug_effects.parquet`; 0 when the
  predicted part goes the other way, at most 1). Fitted slopes are attenuated by noise, so the rule multiplies them
  by 2. **`cell-cycle shift (explains ~N% here)`** means: the drug-dose's shift explains only about N%
  of this gene's change, and even with the gene's fitted cycle slopes multiplied by 2 it would explain
  less than half, with a change of at least 1.2× left over. For this gene the shift is then **no artifact**:
  the row is clean and carries no alert (the token stays in its caveats). Where the shift may be the explanation
  the plain artifact flag stays, and the alert says how much it explains: `⚠ cell-cycle shift, explains ~60% of
  this change`. Tables from an older tables stage have no such share: there every row of a `cell-cycle shift`
  drug-dose carries the plain alert.

## A gene note, section by section

- **Frontmatter** — symbol, Ensembl id, registry name and cytoband, module and arm, pooled level (CPM),
  lines expressing it, drug-doses raising / lowering it significantly (`n_dd_up` / `n_dd_down`, all of them;
  `n_dd_up_clean` / `n_dd_down_clean`, those without an alert), whether it is in the vector space (tag
  `evidence-flagged-only` when it is there only through significant drug-doses that carry an alert).
- **Title, name, location**, then the **written section** when someone has written one.
- **At a glance** — a generated "In this data" callout: how many drug-doses raise and lower it significantly pooled
  over the cell lines (median), how many of them carry an alert, and the strongest (fold, z, q, in how many of the
  measured lines it moves) with its alert — and, when that one carries an alert, the strongest without one; when
  fewer than 3 drug-doses without an alert are significant pooled, an "In single lines" sentence names the
  drug-doses that pass the per-line cut in the most lines (`tables/drug_line_top.parquet`), with their alerts; its
  strongest partners by |cos| with each partner's fdr, ⚠ marking those that are not replicated (evidence other than
  `both halves`, i.e. not the same sign with fdr ≤ 0.10 in two random halves of the compounds); its
  module and arm. A gene that is in the vector space only through significant drug-doses that carry an alert says
  so here, with ⚠. (The "In one line" callout above it, when there is one, is the written layer.)
- **Drugs that raise it / lower it** — pooled over the cell lines (median): one ranked list per direction over every
  drug-dose with |z| ≥ 3 or q < 0.10, flagged ones included, strongest first: the 15 strongest, and any of
  the 15 strongest without an alert that rank below them. *Alert* = ⚠ and the artifact flags in plain words
  (see above); *Caveats* = the soft caveats. Bold fold = significant. *Lines up / measured* = lines where that
  drug-dose moves it ≥ 1.2× at per-line z ≥ 2, out of the lines measured for it (see above) with enough cells; the
  first names are the strongest. This count is descriptive (per-line z ≥ 2 is not a significance cut). *Dose
  pattern* = how the effect behaves across the drug's doses (rises with dose, top dose only, all doses, single dose,
  inconsistent). When a listed row carries `cell-cycle shift`, a line under the lists gives the gene's fitted
  cell-cycle slopes. (There is no separate "flagged" section: flagged drug-doses are in these lists.)
- **In which cell lines** — one row per line: TP53 status, the line's own level (CPM; "n.m." = not measured, see
  above), how many drug-doses move it ≥ 1.5× at per-line |z| ≥ 8.4 in that line (with the number that
  carry an alert in brackets; tables from an older tables stage count only clean drug-doses, and the note says so),
  and the strongest of them up and down with its alert, then the strongest without an alert when that is another
  drug-dose. The per-line cut is calibrated on this run (`tables/info.json`): a per-line z rests on one or two wells and its tails are heavier than a normal's, so with ~1,100 drug-doses per gene and line a fixed cut of 3 or 4 is passed by chance; at this cut about 0.0492 chance calls are expected per gene and line over the 1,026 clean drug-doses.
- **Genes that move with it / opposite** — its strongest partners each way, from the gene's 100 nearest by |cos|.
  *cos* = signed cosine of the two gene vectors = the correlation of their denoised responses over every
  (drug-dose, cell line) context (+1 always together, −1 always opposite). *Halves* = the same cosine in two vector
  spaces fitted on two random halves of the compounds (a hash split of the compound names; drug families fall in
  both); *evidence* = `both halves` (the same sign in the full space and in both halves, |cos| ≥ 0.2 in
  each, **and** fdr ≤ 0.10), `⚠ one half` (strong, |cos| ≥ 0.5, in one of the two random halves
  only: not replicated, no error estimate; often one compound), `⚠ not reproduced`. Other alerts: `⚠ same locus` /
  `⚠ readthrough risk` (neighbours on the genome), and ⚠ after the partner's name = the partner is in the vector space
  only through drug-doses that carry an alert. The tables show the 12 strongest per side and any of the
  12 strongest without an alert below them; a partner with an alert keeps its place with it. *fdr* = the
  estimated share of false relations among pairs at least this strong in both halves, from sign concordance between
  the halves (see
  [[FDR calibration and the inflated null]]). *Notes*: known links (shared HGNC gene group, shared Hallmark/Reactome
  pathway, STRING score), **novel candidate** (both halves, fdr ≤ 0.05, |cos| ≥ 0.5, no known
  link, not the same locus, both genes described by HGNC and placed on the genome; assessed only when HGNC, Ensembl,
  STRING and Hallmark or Reactome all loaded), same locus (≤ 50 kb) and **readthrough risk** (same
  strand, ≤ 20 kb, the 5′ gene ≥ 8×
  more expressed: the 3′ gene's counts can be the 5′ gene's transcription, marked ⚠; see
  [[Readthrough spillover]]). A
  relation is a correlation across drugs and lines; it is never evidence that one gene regulates the other.
- **Direction (probable)** — the arrows of the direction stage (`direction/`): **upstream of this gene**, the arrows
  whose target it is, and **downstream of this gene**, the arrows whose source it is (to another gene, or to the
  cells under a drug-dose). Each arrow names its source or target (linked), its grade (A strong, B read its alerts,
  C a glimpse), what the source's activity does (raises, lowers, or not inferred), the evidence (a recorded mutation
  and the lines on each side, lines that do not express the source, compounds that target it, or its natural level
  across the lines), the size of the effect, q, and its alerts (⚠ and a short label per reason; every reason in full
  is in `direction/edges.parquet`). Each list shows the 12 strongest and any of the 12 strongest without an
  alert beyond them, and says how many more there are. An arrow is a **probable** direction, from the screen's cell
  lines: not proof of direct regulation (A → B → C looks like A → C). Kinds, grades, sign, alerts and this run's
  controls: [[Probable direction]]. When the gene has arrows, At a glance says so in one sentence.
- **Where it sits** — its module and arm, its positions on the two maps, the length of its vector, and the 5
  drug-doses whose vectors **predict** the largest rise and fall of the gene (gene vector · drug-dose vector, in z
  units), with the 5 strongest predictions among drug-doses without an artifact flag (⚠ = the drug-dose, or
  the gene at it, carries one), next to the **observed** z. Agreement means the gene follows the programme it shares
  with its partners; a gap means it departs from it for that drug.
- **What is on record** — the registries' own words (HGNC, Ensembl, UniProt, NCBI Gene), with accession links. When
  there is no record the note says so and claims nothing more.
- **Data** — the exact files and rows behind every number, and the link to the gene's **plates note**: its raw CPM
  and its corrected well effect (W2) in every well of every plate, as 8 × 12 grids (bold = DMSO wells).

## The vector space and the nodal map

- **Vector space** (`embed/`): each gene is a vector whose direction is its response pattern across all active,
  trustworthy (drug-dose, line) contexts. Two genes that respond oppositely point in opposite directions (cos near
  −1). Drug-doses live in the same space: the dot product of a gene vector and a drug-dose vector approximately
  reproduces the observed z (the part of it that the space's shared programmes explain).
- **Nodal map** (`graph/`, x and y): a 2D layout of 1 − |cos|. Opposite genes count as related, so the two arms of
  one pathway — the genes it switches on and the genes it switches off — land in **one island**. Islands are
  **modules**. A module has a **− arm** only when ≥ 5 of its genes sit on the negative side of its main
  direction **and** the two sides anti-correlate (mean cos between them ≤ -0.2): then the + arm rises where
  the − arm falls. Otherwise it is **single-armed** (every gene +), and its notes say so with the measured mean cos
  between the sides (`graph/modules.parquet`). The **signed map** (xs, ys) uses 1 − cos and puts opposite genes far
  apart.
- A **module canvas** (Modules/…canvas) shows the module's genes at their nodal-map positions (green = + arm, red =
  − arm, in modules with two opposite arms) with the graph's edges (+ together, − opposite).

## Drug, line, plate and module notes

- **Drug** — doses (wells, significant genes, replicate agreement, cell loss, cell-cycle and proteasome module z,
  flags with ⚠ before the artifact flags), the genes each dose raises and lowers (every significant gene counts;
  those with an alert are marked, a bare ⚠ standing for the dose's own alert named after the dose), the modules it
  moves, the lines it depletes and the lines that respond most, the nearest drugs in the vector space, and (Direction
  (probable)) the genes that set how the cells fare under it and the drug-target arrows of its compound classes.
- **Cell line** — organ, TP53 status, drivers, the drug-doses that deplete it, how strongly it responds (both over
  all drug-doses, flagged ones marked ⚠), the genes it moves most, the genes it has unusually high or lacks, and the
  programmes that do not respond in it; and (Direction (probable)) its recorded alterations as the direction stage
  grouped them, and the genes it does not express that served as natural knockouts, with the arrows each gave.
- **Plate** — dose, reliability, plate factor, DMSO and failed wells, an 8 × 12 layout and a 96-row well table
  (wells on an unreliable plate, without a position correction, not used in their drug-dose or failed are marked ⚠).
- **Module** — label from the validation stage, enrichment, the drugs that raise or lower it (flagged ones marked
  ⚠), the lines where it responds most, candidate new members, and every member by arm.

## Conventions

- Wikilinks are note names; drugs end in "(drug)", cell lines in "(line)".
- "Upstream" and "downstream" are regulatory words; chromosomal position is "5′ of" / "3′ of".
- A number in a note is read from the table named next to it, or is a simple function of it named with it (CPM =
  counts ÷ total × 10⁶, a predicted z = a dot product, a level ratio); nothing is re-estimated by the vault.
- The global graph view starts filtered: no indexes, Plate notes, plates notes or cell lines (every gene note links
  every line, so lines would pull all genes into one ball); change the filter in the graph settings to see them.
  Plates notes are excluded from search and the quick switcher (Settings → Files and links → Excluded files); open
  them from a gene note.
