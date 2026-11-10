# Tahoe-100M gene map (branch `finalized`)

One command turns [Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M) — 50 cancer cell lines × 379
drugs × 3 doses, ~96 million single cells at 24 h — into a map of **every gene, drug and cell line**, so that for any
gene you can:

1. **see which drugs raised it (or lowered it)**, at which dose, how strongly, and with which caveats;
2. **see in which cell lines** it happened, against each line's own baseline;
3. **see which other genes move with it, and which move opposite to it**, how sure that is, and whether the relation
   is already known (STRING, Reactome, Hallmark, HGNC gene groups) or a candidate new one;
4. **see which genes probably act on it, and what it probably acts on** (its probable direction, upstream and
   downstream, and on the cells' growth under a drug), from the cell lines' recorded mutations and, without any known
   mutation, from lines that do not express a gene, from drugs that target a gene and from genes' natural levels.

All of it can be searched in **the explorer**: web pages with one page per gene, drug, drug-dose and cell line, every
value exact and every list complete (nothing is capped, and nothing is left out because of a flag). Online at
https://xuvictor04.github.io/Tahoe100-PseudoManual/ once published, or on your computer by opening
`<output>/explorer/web/index.html`.

```bash
~/tahoemap-repo/tahoe setup     # once
tahoe run --stream              # everything; reads the data straight from Hugging Face (or: tahoe download; tahoe run)
tahoe open                      # the explorer in a browser: search any gene, drug or cell line
tahoe gene MDM2                 # or ask in the terminal
```

Start with [docs/quick-start.md](docs/quick-start.md). `tahoe test` runs the whole pipeline on synthetic data with
planted answers in a few minutes.

`tahoe run` can be stopped (`tahoe stop`) and resumed at any point: finished stages, and finished plates of the
build, are kept. Options that change results (`--dims`, `--min-cells`, …) are remembered for the output folder
(`run_options.json`); giving one with a new value redoes its stage and everything after it. A local build refuses an
incomplete download unless `--allow-partial`; reference downloads that failed are retried by the next run
(`--refresh-reference` fetches them all again).

## What a run produces

| Output (under `<data>/tahoemap/`) | What it is |
|---|---|
| `explorer/` | **The explorer**: searchable web pages over every result. A gene's page lists every drug-dose with its exact corrected fold change, z, q and flags (flagged rows stay in their ranked place), the gene in each of the 50 cell lines, its correlations with every other gene, its partners, module and probable direction, its baseline and every well. A drug-dose's page holds its raw corrected values for every gene. `web/` is published as GitHub Pages and `data/` as a data repository (`tahoe export DEST --explorer`; [docs/quick-start.md](docs/quick-start.md#the-explorer-search-any-gene)) |
| `vault/` | **An Obsidian vault**: a note per gene (16k+), drug, cell line, plate and module, linked; each gene note has the drugs that raise / lower it, the cell lines, the genes that move with / opposite it, its probable direction (the genes upstream and downstream of it), its place in the map, registry facts (HGNC, UniProt, NCBI) and a companion note with the raw and corrected per-well values laid out plate by plate |
| `map/gene_map.html` | **The interactive map**: every gene on the nodal map or the signed vector map (a Spread slider pulls the modules apart), a k-D tour of the vectors themselves, and physics views (a gene's neighbourhood to depth 1-4, a module, all genes) with the probable-direction arrows; searchable; click a gene for its partners, drugs, lines and probable up- and downstream genes |
| `validation/report.md` | How well the space recovers known biology, the opposite-arm test, module labels, **novel candidate relations**, and the direction stage's controls |
| `direction/` | **Probable direction** (which gene acts on which): arrows SOURCE → TARGET with p, q, a grade A / B / C and their alerts, the groups of lines compared, the controls; `direction/README.md` documents every column ([docs/direction.md](docs/direction.md)) |
| `tables/` | The fold-change tables (parquet): per gene × drug-dose, per gene × cell line, per (drug-dose, line), per gene, drug, line, plate, well — every column documented in `tables/README.md` |
| `relations/gene_relations.parquet` | Gene × gene: each gene's 100 strongest partners, signed, with split-half evidence, FDR and known / locus / readthrough flags |
| `embed/` | The vector space: gene, drug-dose, drug, (drug-dose × line) and cell-line vectors |
| `graph/` | The nodal map: modules with their + / − arms, layouts (t-SNE and modules spread apart), module scores per drug-dose and line |
| `tensor/` | Per-cell-line layer: every gene × drug-dose × line fold change and z; raw counts per well |
| `atlas/` | The build (counts per well × line × gene) and the corrected effects (method v3) |
| `review/` | *Optional, from `tahoe review` (below)*: AI-agent literature reviews of genes, drugs and cell lines — each review with its verification, the full history of every agent run, a ledger of attempts and costs, and every connection verdict and finding as tables; the vault and the map show them |

`tahoe gene / drug / line / pair / module` answer from these files in the terminal (`--top all` prints every row).
`tahoe export DEST` copies the shareable results (vault, map, tables, validation, direction, graph, relations, embed
...) into a folder ready to push to GitHub ([docs/quick-start.md](docs/quick-start.md#put-the-results-on-github)).
`tahoe export DEST --explorer` makes the explorer ready to publish: the pages, the data repository, and a script
that uploads them (it pushes only to the branch `site` and to the data repository).

**Flags are alerts, never removals.** A drug-dose can carry an artifact flag (toxic, transcription drop, cell-cycle
shift, unreliable plate only, position not correctable or correction uncertain, wells disagree); a relation can be
unreplicated; a gene can be in the vector space only through flagged drug-doses. Every list, table, note, look-up
and map panel keeps such an item in its ranked place and marks it with an alert, '⚠' plus the reason in plain words
(e.g. '⚠ toxic; transcription drop', '⚠ cell-cycle shift, explains ~60% of this change'), and says how many items
it holds and how many carry an alert. A list capped at N shows the N strongest and any of the N strongest without an
alert that would fall below them. The cell-cycle shift is judged gene by gene: where the shift explains little of a
gene's change (for example Idarubicin raising TRIM72 / MG53 12.2×, of which the shift would explain ~4%), it is no
artifact for that gene and the value counts as clean
([docs/method.md](docs/method.md#4-tables--the-fold-change-tables)).

## The stages

`tahoe run` runs every stage that is missing or out of date, in order, and can be stopped and resumed:

| Stage | What it does | Real-data time |
|---|---|---|
| build | one pass over all cells → counts per well × cell line × gene (`--stream`: no download) | ~1.5 h streamed |
| effects | the corrected effect of every drug-dose on every gene (composition, plate, well-position corrections; flags) | ~10 min |
| tensor | the same per cell line: gene × drug-dose × line fold changes and z | ~9 min |
| tables | the fold-change tables | ~2 min |
| embed | the vector space (genes, drugs, contexts, lines), also fitted on two halves of the compounds | ~2 min |
| reference | public annotations, downloaded once and cached (`--offline` skips) | ~3 min |
| relations | gene × gene partners, evidence, FDR, known / novel | ~1 min |
| graph | modules, arms, the nodal map and the signed map | ~2 min |
| direction | probable direction between genes (which acts on which), from the cell lines' recorded mutations, natural knockouts, drug targets and natural levels ([docs/direction.md](docs/direction.md)) | ~6–7 min (estimated) |
| validate | control programmes, opposite-arm test, module labels, novel candidates | ~2 min |
| vault | the Obsidian vault | ~2 min |
| map | the interactive HTML map | ~1 min |
| explorer | the explorer: searchable pages with every value, checked against the tables it comes from (every row of each, every value bit for bit) | ~15–25 min (estimated) |

Times were measured on the full data on a 4-core, 15 GB machine (a scale test of this code; its outputs were not
kept), except the direction and explorer stages', which are estimated from generated outputs of the full size (they
have not yet run on the real data); see [docs/quick-start.md](docs/quick-start.md#resources) for disk and memory. An
output that finished before the explorer stage existed runs direction, validate, vault, map and explorer after the
update (their methods changed too), plus any earlier stage whose method changed since it was made (`tahoe` shows the
plan): about 30–45 minutes. [docs/method.md](docs/method.md) explains every step and every flag.

## The vector space and the nodal map

Each gene is a vector built from how it moves across every (drug-dose, cell line) context; drugs, drug-doses,
contexts and cell lines are vectors in the same space, and a gene vector · a drug vector ≈ that drug's effect on the
gene. In the vector space, two genes that move in opposite directions (the induced and the repressed arm of one
pathway) point opposite ways and sit far apart; on the nodal map, which uses |cosine|, they sit together, as one
island with a + arm and a − arm. On planted data the opposite modules have cosine −0.7 yet share one island.
The modules are Louvain communities of a graph that links each gene to its 15 strongest replicated partners by
|cosine| ≥ 0.3 (or ≥ 0.5 in one random half of the compounds); groups over 300 genes or looser than a mean |cosine|
of 0.3 are split again, groups under 5 genes get no module, and a module has a − arm only when its two sides
anti-correlate. [docs/vector-space-and-nodal-map.md](docs/vector-space-and-nodal-map.md) explains it in full.

## Probable direction: which gene acts on which

A correlation has no direction: CDKN1A and MDM2 rise together, and the cosine does not say that both follow TP53. The
direction stage adds arrows SOURCE → TARGET, each from a statistical test. The strongest come from the cell lines'
**recorded mutations**: a mutation was there before the experiment, so it cannot be a consequence of the target.
**Without any known mutation**, a glimpse comes from lines that do not express a gene at all (natural knockouts), from
compounds that target a gene's protein, and from a gene's natural level across the lines. Every arrow has a grade (A
strong, B read its alerts, C a glimpse) and says what the source's activity does: raises or lowers (a level, the
cells' numbers), strengthens or weakens (a drug response), or not inferred. A
doubtful arrow keeps its place with ⚠ and the reason. Random groups of lines, tested the same way, give the number of
false arrows to expect. The arrows appear in the vault's gene, drug and cell-line notes (section Direction
(probable)), in the map's side panel and as arrows on its neighbourhood and maps, and in the validation report. They
are a **probable** direction, from 50 cancer cell lines at one time point: A → B → C looks like A → C, 'not
recorded' is not 'wild type', and drugs act on proteins, not on mRNA. [docs/direction.md](docs/direction.md)
explains it, with examples.

The look-ups show the same arrows: `tahoe gene X` (upstream, downstream, the cells under drugs), `tahoe line X` (its
recorded alterations and natural knockouts), `tahoe drug X` (the cells under its doses, its drug-target arrows) and
`tahoe pair A B` (any arrow between the two); the literature reviewers' dossiers include a gene's arrows.

## The explorer: search a gene and see everything about it

The explorer answers "what happens to this gene?" in one place. Type a symbol (TRIM72), an alias (MG53), an Ensembl
id, a drug, a target, a cell line or an organ; two words ("TRIM72 A549", "TRIM72 idarubicin") go straight to that
gene in that line or under that drug. A gene's page has:

- **Drugs**: every one of the 1,132 drug-doses, sorted by z, with the corrected fold change, z, q, the call, the
  flags in full, and how many cell lines rose or fell. A flagged row keeps its ranked place: TRIM72's strongest
  raisers, Idarubicin 5 µM and Homoharringtonine, carry artifact flags and are listed with them, not removed.
- **Cell lines**: the gene in each of the 50 lines at every drug-dose (per-line values, exact), with the reason for
  every missing value.
- **Correlations, partners, direction, baseline and wells**: its correlation with every other gene, its 100
  strongest partners and the genes that list it, its module, what probably acts on it and what it acts on (every
  arrow, with its alerts, notes and caveats), its baseline in every line, and every well's raw and corrected value.

A drug-dose's page holds the drug's raw corrected information: every gene's exact pooled value (also as a CSV), its
quality checks, the cells left in each line, and its wells. A cell line's page has its genetics, how each drug-dose
changed its cell numbers, and every gene's line effect.

The rules: nothing is capped, nothing is filtered by a flag (filters are opt-in and say how many rows they hide),
text is never cut, every missing value says why, and the values are the bytes the pipeline stored. The explorer
stage stops rather than publish pages that differ from the tables: it rebuilds every row of `tables/drug_effects`
from its own files, bit for bit, and counts every source table's rows in each place they appear. The map, the vault
notes and the look-ups link into it ("15 of 41 shown; all 41 in the explorer").

**Locally**: open `<output>/explorer/web/index.html` (`tahoe open`); it reads the data folder next to it, with no
network. **Online**: `tahoe export DEST --explorer`, then `DEST/publish.sh` (Windows: `publish.ps1`), after two
one-time settings on github.com (a public repository `Tahoe100-PseudoManual-data`, and Pages from the branch `site`);
[docs/quick-start.md](docs/quick-start.md#the-explorer-search-any-gene) has the steps.
[docs/explorer.md](docs/explorer.md) explains the pages, and [docs/explorer-data.md](docs/explorer-data.md) their
file format.

## Literature review agents

`tahoe review` (optional; an Anthropic API key and money) runs one AI agent per gene, drug or cell line over a
finished run: it reads a dossier of what the data say about that entity, searches PubMed, Europe PMC and the web,
and submits a cited review — what is established, what is unexpected, which expected connections are missing, what
is contradicted, and a verdict on each connection. Every cited paper is looked up and a second agent checks each
claim against the abstracts; every request, response and tool call is kept. The reviews appear in the vault (a
"What the literature says" section and a Literature column in the partner tables) and in the map. Keys can run out
mid-run and be replaced; a stopped run resumes where it stopped. A full gene pass is expensive (~15,000 genes): start
with `tahoe review plan`, `--dry-run` and `--limit`, ideally on a copy (`tahoe duplicate`).
[docs/review.md](docs/review.md) explains the agents, costs, keys, histories, verification and the duplicate
workflow.

```bash
tahoe review plan                          # the queue and its projected cost
tahoe review run --kinds line --max-usd 75 # the 50 cell lines (~$60 projected), at most $75; Ctrl-C pauses
tahoe vault; tahoe map                     # show the reviews in the vault and the map
```

## What was carried over, and how it was checked

This branch starts from scratch and takes only what it needs from the earlier work (branch
`claude/tahoe100m-gene-pipeline-lodlx7`): the build and the method-v3 corrected effects of `tahoe_atlas.py` /
`tahoe_mtap_gankyrin.py`, copied function by function by syntax tree (`tools/port_from_old.py`), the synthetic
test-data generator, and the written knowledge of the earlier Obsidian vault (105 gene notes and the concept notes,
in `tahoemap/vault_seed/`). Checks:

- `tests/test_port.py` proves the ported code is the old code, character for character;
- on the synthetic data, every array and table the ported build and effects write is identical, bit for bit, to the
  old scripts' output;
- the tensor stage re-derives the atlas's numbers from its own per-line values while it runs and stops if they
  differ;
- an earlier `tahoe_atlas.py` build can be reused as is (`tahoe run --reuse-atlas ~/Tahoe-100M/atlas`).

## Testing

```bash
tahoe test                      # or: python3 tests/run_tests.py --workdir /tmp/tahoemap_test
python3 tests/test_port.py      # the port is verbatim
python3 tests/test_review.py --workdir /tmp/tahoemap_test   # the review agents against a scripted fake API
python3 tests/test_windows.py   # Windows-only behaviour, simulated on Linux / macOS (seconds)
python3 tests/test_export.py --out /tmp/tahoemap_test/out_seed0   # `tahoe export`, also --explorer (seconds)
python3 tests/test_direction.py --no-scale   # the direction stage against its planted answers (a few minutes;
                                             # without --no-scale also at 4,000 and 8,000 genes, ~15 min)
python3 tests/test_explorer.py --out /tmp/tahoemap_test/out_seed0 --data /tmp/tahoemap_test/data_seed0
python3 tests/test_surfaces.py --out /tmp/tahoemap_test/out_seed0   # links, map, vault and look-ups into it
python3 tests/test_explorer_browser.py --out /tmp/tahoemap_test/out_seed0   # the pages in headless Chromium
```

`tests/test_review.py` (after `run_tests.py`, offline, no key, about 3 minutes) drives the review runner through the
real SDK against a scripted fake API: a review end to end with verification, refusals, nudges, budget caps, a key
that runs out of credit and the rotation to the next, every key dead and the resume, rate limits, Ctrl-C and
SIGTERM, concurrency, a dry run, the CLI, a fake review of a gene, a drug and a line spliced into the vault and the
map, and `duplicate`; it also checks that no key reaches any file or any printed line.

The synthetic data plant drug effects (some only in TP53-wild-type lines), co-regulated modules, pairs of modules
moved in opposite directions, un-moved genes, and every artifact the method corrects. The tests check each stage
against them (106 checks with Playwright installed; without it the 21 browser checks are 6 warnings): the tensor
reproduces the atlas exactly, ambient-only lines and uncountable profiles are masked, per-line effects appear only
where planted (e.g. p53 targets in TP53-wild-type lines only), the per-line cut is calibrated, planted modules are
tight in the space, opposite modules point opposite ways and share a nodal-map island on opposite arms, un-moved
genes rarely form strong relations, the FDR is monotone and calibrated, the vault has a note per gene and no broken
links, the map's spread layouts move the modules apart, flagged drug-doses stay in the map's lists with their alert,
the map's spread slider, tour and neighbourhood depth work in a browser, the look-ups answer, and the direction
stage recovers its planted answers (TP53 → the p53 targets and the cells under DNA-damaging drugs, a natural
knockout's partners, a gene's level → its partners' response) while random groups give no more arrows than expected,
and the vault and the map show the same arrows as the stage wrote. The explorer's checks compare every value it
holds with the arrays and tables, bit for bit (every `drug_effects` row, every per-line and per-well value), check
that every source row is in it, find the planted answers in it (a gene whose strongest raiser carries an artifact
flag keeps that row first), and check that two runs give identical files and that a size limit moves data without
losing any.

## Read the results with these in mind

- **Correlation across drug responses is not mechanism.** No genes were knocked out; "moves with" means "responds
  alike to ~1,100 drug-doses in 50 lines". Upstream / downstream are used only for the direction stage's arrows,
  which are **probable**: from cell lines, not proof of direct regulation.
- **One time point** (24 h), **cancer cell lines**, **most drug-doses in a single well**, **dose confounded with
  plate**. Fold changes are against the same line's median drug well on the same plate, not DMSO.
- Pairs of neighbouring genes on the same strand can correlate through **readthrough** transcription; such pairs
  carry an alert and are never called novel.
- **⚠ marks a reason to doubt, not a verdict.** A flagged drug-dose's change may be its artifact (dying cells, a drop
  in transcription, a shift in the cell-cycle mix), or the drug's own effect; read the reason next to the ⚠.
- "Moves with / opposite" partners carry their evidence: `both halves` = replicated in two random halves of the
  compounds with a false discovery rate ≤ 10%; `one half` = strong in one half only (not replicated, often one
  compound). Pooled lists are medians over the 50 lines: responses confined to a few lines are in the per-line tables.

## Repository layout

| Path | |
|---|---|
| `tahoe` | the command (Linux / macOS); Windows: `python -m tahoemap …` (see the quick start) |
| `tahoemap/review/` | the literature-review agents: agent and skill files (Claude Code format), dossiers, tools, verification, key pool, histories, the runner |
| `tahoemap/` | the package: `atlas_core.py` + `tlib.py` (ported method), `stream.py`, `tensor.py`, `tables.py`, `embed.py`, `reference.py`, `relations.py`, `graph.py`, `direction.py`, `direction_view.py`, `validate.py`, `vault.py`, `html_map.py`, `explorer.py` (+ `tsf_reader.py`, `links.py`), `query.py`, `export.py`, `cli.py` |
| `tahoemap/explorer_app/` | the explorer's pages (index.html, app.css, js/*.js; the stage joins the scripts into app.js) |
| `tahoemap/data/control_sets.json` | curated control programmes for validation (from the literature, not Tahoe) |
| `tahoemap/vault_seed/` | the written layer of the vault (add `genes/SYMBOL.md` to add knowledge; it survives rebuilds) |
| `docs/` | quick start, method, the two maps, the literature review ([review.md](docs/review.md)), design contracts |
| `tests/` | synthetic data generator, end-to-end tests, port test, review, Windows, export, direction, explorer and surface tests |
| `tools/port_from_old.py` | how the method was carried over |
