# Tahoe-100M gene map (branch `finalized`)

One command turns [Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M) — 50 cancer cell lines × 379
drugs × 3 doses, ~96 million single cells at 24 h — into a map of **every gene, drug and cell line**, so that for any
gene you can:

1. **see which drugs raised it (or lowered it)**, at which dose, how strongly, and with which caveats (each drug
   with Tahoe's annotation and ChEMBL's side by side);
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
| `vault/` | **An Obsidian vault**: a note per gene (16k+), drug, cell line, plate and module, linked; each gene note has the drugs that raise / lower it (with a rough DMSO-referenced fold change and the wells), the cell lines, the genes that move with / opposite it, its probable direction (the genes upstream and downstream of it, and the tests that gave no arrow), its place in the map, registry facts (HGNC, UniProt, NCBI) and a companion note with the raw and corrected per-well values laid out plate by plate. Drug notes show Tahoe's and ChEMBL's annotations side by side, the mechanism classes with their sources, each dose's neighbouring-well reading, the most similar drug-doses and the lines a drug-dose singles out |
| `map/gene_map.html` | **The interactive map**: every gene on the nodal map or the signed vector map (it opens with the modules spread apart; the Spread slider goes back to the t-SNE layout), a k-D tour of the vectors themselves (its axes named by drug-doses), and physics views (a gene's neighbourhood to depth 1-4, a module, all genes) with the probable-direction arrows; search finds genes, drugs, drug-doses and cell lines; click a gene for its partners, drugs, lines and probable up- and downstream genes |
| `validation/report.md` | How well the space recovers known biology, the opposite-arm test, the drug check (Tahoe and ChEMBL classes), neighbouring wells, module labels (gene sets, the drug classes that drive a module, lineage) with their alerts, **novel candidate relations** (lineage pairs and near-identical copies marked), known line-selective responses, and the direction stage's controls |
| `direction/` | **Probable direction** (which gene acts on which): arrows SOURCE → TARGET with p, q, a grade A / B / C and their alerts, the groups of lines compared, the controls, the drug-doses that single out some lines (`selectivity.parquet`) and every gene's tests (`gene_tests.parquet`); `direction/README.md` documents every column ([docs/direction.md](docs/direction.md)) |
| `tables/` | The fold-change tables (parquet): per gene × drug-dose, per gene × cell line, per (drug-dose, line) with growth, response strength and line selectivity (`drug_line_response.parquet`), per gene, drug, line, plate, well; every drug-dose's up and down gene sets (`drugdose_signatures.gmt`) — every column documented in `tables/README.md` |
| `relations/gene_relations.parquet` | Gene × gene: each gene's 100 strongest partners, signed, with the same-sign-in-both-halves evidence, FDR, known / locus / readthrough flags, lineage pairs and read-sharing copies |
| `embed/` | The vector space: gene, drug-dose, drug, (drug-dose × line) and cell-line vectors; each drug-dose's 50 most similar drug-doses (`drug_similarity.parquet`) |
| `graph/` | The nodal map: modules with their + / − arms and their technical and cell-cycle covariates, layouts (t-SNE and modules spread apart), module scores per drug-dose and line, the modules as gene sets (`modules.gmt`) |
| `reference/` | Public annotation reduced to Tahoe's genes (HGNC, Ensembl coordinates of every gene, UniProt, NCBI, Reactome, Hallmark, STRING, Ensembl Compara paralogues) and each drug's ChEMBL record: its mechanisms, targets and mechanism classes (`drug_annotations.parquet`, `drug_mechanisms.parquet`, `drug_classes.parquet`) |
| `tensor/` | Per-cell-line layer: every gene × drug-dose × line fold change and z; raw counts per well |
| `atlas/` | The build (counts per well × line × gene) and the corrected effects (method v3) |
| `review/` | *Optional, from `tahoe review` (below)*: AI-agent literature reviews of genes, drugs and cell lines — each review with its verification, the full history of every agent run, a ledger of attempts and costs, and every connection verdict and finding as tables; the vault and the map show them |

`tahoe gene / drug / line / pair / module` answer from these files in the terminal (`--top all` prints every row).
`tahoe similar DRUG [DOSE]` lists the drug-doses most like one drug-dose. `tahoe signature --up A,B [--down C,D]`
ranks the drug-doses that mimic or reverse a gene signature, with a p from 1,000 random gene sets of the same sizes.
`tahoe export DEST` copies the shareable results (vault, map, tables, validation, direction, graph, relations, embed
...) into a folder ready to push to GitHub ([docs/quick-start.md](docs/quick-start.md#put-the-results-on-github)).
The few text files that name this computer's folders (the stage stamps, sources.json, run.log, the vault's Home
note) are copied with `<out>`, `<data>` and `<cache>` in place of those folders; the export's README lists them.
`tahoe export DEST --explorer` makes the explorer ready to publish: the pages, the data repository, and a script
that uploads them (it pushes only to the branch `site` and to the data repository).

**Flags are alerts, never removals.** A drug-dose can carry an artifact flag (toxic, transcription drop, cell-cycle
shift, unreliable plate only, position not correctable or correction uncertain, wells disagree, like a neighbouring
well); a relation can lack the same sign in both halves of the compounds, or be a lineage pair or a read-sharing copy;
a gene can be in the vector space only through flagged drug-doses. Some flags are caveats, not artifacts: 'like a
neighbouring well (top dose)', 'like a neighbouring well (not this gene)', 'translation inhibitor' and 'rise under a
translation inhibitor' (each with its plain words wherever it is shown). Every list, table, note, look-up
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
| reference | public annotations and each drug's ChEMBL record, downloaded once and cached (`--offline` uses the cache); reads only the build's tables, so it runs before tables | ~3 min, plus ChEMBL (2.5–10 min, depending on how fast the EBI server answers) and Compara (~2 min on a fast link, up to ~30 min on a slow one) the first time; both log their progress |
| tables | the fold-change tables; the neighbouring-well rule, the translation-inhibitor caveat, a rough DMSO-referenced fold change, growth and line selectivity per (drug-dose, line), Tahoe's and ChEMBL's annotations | ~2 min |
| embed | the vector space (genes, drugs, contexts, lines), also fitted on two halves of the compounds; the drug-dose similarity | ~2 min |
| relations | gene × gene partners, evidence, FDR, known / novel, lineage pairs (with their null) and read-sharing copies | ~1 min |
| graph | modules, arms, the nodal map and the signed map; module covariates and how much each map keeps | ~2 min |
| direction | probable direction between genes (which acts on which), from the cell lines' recorded mutations, natural knockouts, drug targets and natural levels ([docs/direction.md](docs/direction.md)) | 3.3 min measured on the real data at direction version 2 (peak 1.7 GB); ~6 min estimated for version 6 |
| validate | control programmes, opposite-arm test, drug check, neighbouring wells, module labels and alerts, novel candidates, line-selective controls | ~2 min |
| vault | the Obsidian vault | ~2 min |
| map | the interactive HTML map | ~1 min |
| explorer | the explorer: searchable pages with every value, checked against the tables it comes from (every row of each, every value bit for bit) | ~15–25 min (estimated) |

Times were measured on the full data on a 4-core, 15 GB machine (a scale test of this code; its outputs were not
kept); the direction stage's on the user's PC at direction version 2; the explorer's is estimated from generated
outputs of the full size (it has not yet run on the real data); see
[docs/quick-start.md](docs/quick-start.md#resources) for disk and memory. After this update any earlier output,
including one made before the explorer existed, redoes reference and every stage after it (each of their methods
changed: reference 3, tables 7, embed 5, relations 5, graph 7, direction 6, validate 9, vault 9, map 11, explorer 4);
the build, the effects and the tensor are kept. That is about 45–60 minutes on the full data, plus the first ChEMBL
and Compara downloads (`tahoe` shows the plan first).
[docs/method.md](docs/method.md) explains every step and every flag.

**Stage order.** build → effects → tensor → reference → tables → embed → relations → graph → direction → validate →
vault → map → explorer. The reference stage reads only atlas/, so it runs before tables: every later stage can show
each drug's annotation from Tahoe and from ChEMBL side by side and use the same mechanism classes. So `tahoe run
--from reference` (or `--refresh-reference`) also redoes tables, embed and every later stage.

## The vector space and the nodal map

Each gene is a vector built from how it moves across every (drug-dose, cell line) context; drugs, drug-doses,
contexts and cell lines are vectors in the same space, and a gene vector · a drug vector ≈ that drug's effect on the
gene. In the vector space, two genes that move in opposite directions (the induced and the repressed arm of one
pathway) point opposite ways and sit far apart; on the nodal map, which uses |cosine|, they sit together, as one
island with a + arm and a − arm. On planted data the opposite modules have cosine −0.7 yet share one island.
The modules are Louvain communities of a graph that links each gene to its 15 strongest partners with the same sign
in both halves of the compounds by |cosine| ≥ 0.3 (or ≥ 0.5 in one random half of the compounds); groups over 300 genes or looser than a mean |cosine|
of 0.3 are split again, groups under 5 genes get no module, and a module has a − arm only when its two sides
anti-correlate. [docs/vector-space-and-nodal-map.md](docs/vector-space-and-nodal-map.md) explains it in full.

**How far to trust a partner.** Each gene keeps its 100 strongest partners; a reason to doubt a pair is an alert
shown with it. 'Both halves' means the same sign in both halves of the compounds: the halves share the lines and
plates, so this guards against single-compound effects, not against everything (98% of the partners pass it). A
**lineage pair** is two genes expressed in few lines, mostly the same ones: such genes often move together whatever
their regulation, and lineage_p says how unusual the pair is among pairs that share their lines as much. A
**read-sharing copy** is a pair whose reads can be counted for either gene (near-identical paralogues, a pseudogene
and its parent, a read-through transcript and its part). Counts come in two units: rows (a gene and one of its
partners) and pairs (distinct gene pairs).

**How much a map keeps.** A flat map keeps about a third of each gene's 15 strongest partners among its 50 nearest
genes (0.36 on the nodal and signed maps, 0.31 spread; 0.003 by chance; measured on the published tables). Read the
partner lists, not the distance on the map.

**Drug-doses that act alike.** `embed/drug_similarity.parquet` lists each drug-dose's 50 most similar drug-doses. A
drug-dose whose nearest drug-doses of other compounds are mostly of one other class gets a note (8 on the published
tables: Phenylephrine 5 µM, Econazole 5 µM, Citalopram 0.05 µM and Clobetasol propionate look like glucocorticoids).
Salt forms of one compound that disagree get an alert (13 of 57 pair-doses).

**Module covariates.** A module that moves with a technical measure of the wells (UMI or genes per cell, cell loss,
the composition shift) or with the cell-cycle shift says so (`graph/modules.parquet` covariate_tag; 82 of 235 modules
on the published tables). A note, not an alert.

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

Version 5 corrects readings the reviews found wrong: drugs that trap their target on DNA (TOP1 / TOP2 poisons) no
longer give a sign; the drug-target test uses how strongly each compound moves the gene; Tahoe's and ChEMBL's
annotations are used side by side; grade A needs the whole of the evidence to agree; two genes at the same locus, or
a gene inside an expression programme, give no sign; natural knockouts and drug targets say 'may'. It adds arrows to
a drug-dose's response strength from the mutations that single out some lines (`selectivity.parquet`), allele groups
(KRAS codon G12, hotspots), each group's expected false share, an alert for heavily mutated lines and for evidence
carried by translation inhibitors, and every gene's tests (`gene_tests.parquet`: a gene with no arrow was tested,
and how often). Every change is listed with its old rule, new rule and reason in docs/direction.md.

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

The explorer also has: the drug page's Annotations block (Tahoe and ChEMBL side by side, the classes with their
sources, every ChEMBL mechanism row), the drug-dose's neighbouring-well block and its tabs 'Lines: response and
growth' and 'Similar drug-doses', the line page's 'Response and growth', the gene Direction tab's 'tested in N
comparisons' with every row of `direction/gene_tests.parquet`, 'false (group)' and 'Same test as' on every arrow
table, How to cite, `web/schema.json` (every column of every table) and the GMT files on Downloads.

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

## Drug annotations, mechanism classes and the checks on the wells

**Drug annotations (ChEMBL).** The reference stage looks up every screened drug in ChEMBL (web services, about 52
requests and 2.5 to 10 minutes for the 379 real drugs, depending on how fast the EBI server answers; one log line per
request; cached in `reference/downloads/chembl_drugs.json`; `--offline` uses the cache). A drug is matched by its
structure (PubChem id → InChIKey) and by its name. When PubChem cannot be reached the drugs are matched by name only:
the ChEMBL source then reads 'failed (PubChem not reached ...)' in `reference/sources.json`, each drug's note says so,
and the next run with network fetches ChEMBL again. A ChEMBL mechanism text 'Unknown' counts as no mechanism (status
'no ChEMBL mechanism (ChEMBL: Unknown)'). When the drug metadata file of the download is gone (the data folder moved
or deleted after the build), Tahoe's annotation is taken from the build's `atlas/effects/drugdose.csv`, and every
drug's note and `reference/sources.json` (`tahoe_annotation`) say so. Tahoe's targets and
mechanism stay verbatim next to ChEMBL's molecule, mechanisms, actions, targets and ATC codes, with an alert where
they disagree ('Targets differ', 'Mechanism differs', 'Action differs', 'Identity unsure'). Tahoe's annotation is
never changed. On the real data (ChEMBL 37): 377 of 379 drugs matched (HI-TOPK-032 and DTP3 not found), 284 with a
curated mechanism (3 more, Artesunate, Auranofin and Darinaparsin, have only ChEMBL's 'Unknown'), 19 with an
alert.

**Mechanism classes** (`tahoemap/data/drug_classes.json`, read by `tahoemap/mechanisms.py`). Code reads the classes;
nobody edits a result by hand. A drug is in a class by a cited code constant (by the molecule's name: works offline),
by a ChEMBL mechanism rule, or by a WHO ATC code that ChEMBL reports; each membership names its route. The classes:
TOP1 and TOP2 poisons, PARP trappers, tubulin stabilisers (taxanes) and destabilisers, DNA alkylators, intercalators
and binders, antimetabolites, translation inhibitors (harringtonine, homoharringtonine), glucocorticoid receptor
agonists and antagonists, proteasome, HDAC, HMG-CoA reductase and Smoothened inhibitors. Tahoe's label 'Protein
synthesis inhibitor' is not a class rule: it also covers four MNK / eIF4E inhibitors that do not stop protein
synthesis (the file lists them under 'not_members', with the reason).

**Neighbouring wells.** Two wells that touch on a plate can share a signal (liquid carried over, or a local problem).
The tables stage compares every pair of touching wells of two compounds. When a drug-dose shares most of its genes
with its neighbour and the drug's higher doses do not move them, it gets 'like a neighbouring well': an artifact flag,
but only for the genes the neighbour moves the same way (its other genes read '... (not this gene)'). At a drug's top
dose there is no higher dose to check: the tier is 'top dose', an alert that is not an artifact flag (the row stays
clean). The validation report lists every such drug-dose with its neighbour and wells. Rule changed in tables version 5. Old rule: clean = no atlas artifact flag.
New rule: also not 'like a neighbouring well' for that gene. Reason: touching wells share signatures 3.5 to 4 times
more often than wells 3 or more apart (e.g. Citalopram 0.05 µM next to Clobetasol propionate on plate10). On the
published tables (an earlier version) the rule marks 13 drug-doses 'artifact' and 11 'top dose'; the full run gives
the final count.

**Translation inhibitors.** A drug that stops protein synthesis raises many short-lived mRNAs whatever their pathway.
Every drug-dose of such a drug carries 'translation inhibitor', and each gene that rises there 'rise under a
translation inhibitor': a caveat, never an artifact (Homoharringtonine and Harringtonine on the real data). The
validation report also lists the strongest raisers of each set without them.

**Dose and plate.** Each dose of a drug sits on its own plate, so the pattern over the doses compares plates as much
as doses (`drugs.parquet` dose_plates). Most drug-doses are one well (`n_wells`): their lines are not replicate
treatments. `drug_effects.parquet` lfc_vs_dmso is a rough fold change against the plate's two DMSO wells: a sign
check, not a replacement for the corrected fold change.

**Growth and line selectivity.** `tables/drug_line_response.parquet` holds every drug-dose × line: how many genes the
line moves beyond the per-line cut, how far it stands out among the lines (sel_z; selective at sel_z ≥ 3 with ≥ 20
genes), its relative abundance after 24 h and how strongly it shows the drug-dose's consensus response.

**TP53 'not recorded'.** Reading changed in tables version 5. Old: `lines.parquet` tp53_status read 'wild type' when
no TP53 alteration was recorded. New: 'not recorded' (shown as 'not recorded (presumed wild type, not confirmed)').
Reason: the metadata lists driver alterations only, so a line may carry one that is not listed.

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
python3 tests/test_mechanisms.py      # the drug classes and the ChEMBL matching on the fixture (seconds)
python3 tests/test_tables_rules.py    # the neighbouring-well, translation, selectivity and TP53 rules on toy arrays
python3 tests/test_relations_rules.py # read-sharing copies, the lineage null, counts in two units, similarity
python3 tests/test_validate_rules.py  # the module-label rule, the line-control AUROC
python3 tests/test_fix_back.py --out /tmp/tahoemap_test/out_seed0   # the rules changed after the reviews of the
                                      # published results (caveats next to named values, per-line signs, ...)
```

`tests/test_review.py` (after `run_tests.py`, offline, no key, about 3 minutes) drives the review runner through the
real SDK against a scripted fake API: a review end to end with verification, refusals, nudges, budget caps, a key
that runs out of credit and the rotation to the next, every key dead and the resume, rate limits, Ctrl-C and
SIGTERM, concurrency, a dry run, the CLI, a fake review of a gene, a drug and a line spliced into the vault and the
map, and `duplicate`; it also checks that no key reaches any file or any printed line.

The synthetic data plant drug effects (some only in TP53-wild-type lines), co-regulated modules, pairs of modules
moved in opposite directions, un-moved genes, and every artifact the method corrects; and, since the second wave, a
neighbouring-well copy (an artifact and a top-dose tier), a translation inhibitor, TOP2 poisons, a promiscuous
glucocorticoid gene, KRAS codon-12 and one-dose selectivity, an expression programme, a lineage-restricted gene set
and its broad twin, and a p53 target that falls. `run_tests.py` runs the reference stage offline on a fixture
(`tests/fixtures/reference_cache`: the ChEMBL records of the 94 synthetic drugs and the Ensembl GTF genes of the
panel), so drug annotations, mechanism classes and gene coordinates are tested without network. The tests check each
stage against them (194 checks with Playwright installed, the four offline unit scripts and the 19 checks of
`tests/test_fix_back.py` included: 193 pass on seed 0 and 1 is a warning: the 'lowered by mTOR inhibitors' module
label, whose planted fall is below what the label rule can call; a stronger fall makes the ribosome genes join the
proteasome genes' module, which the curated proteasome set then names. The direction edges are compared with the
version 6 fixture of seed 0. Without Playwright the browser checks are skipped with a warning: 168 passed, 9
warnings): the tensor
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
losing any. The second wave's checks follow every new rule to its planted answer: the neighbouring-well tiers
and their per-gene reading, the translation-inhibitor caveat, the DMSO sign check, drug_line_response bit for bit
against the atlas, TP53 'not recorded', both annotations and the classes, the direction version 5 rules (D1-D17),
lineage pairs and their broad twin, the drug-dose similarity, the module labels, and the same words in the vault,
the look-ups, the map and the explorer (never '0e+00', never TP53 'wild type').

## Read the results with these in mind

- **Correlation across drug responses is not mechanism.** No genes were knocked out; "moves with" means "responds
  alike to ~1,100 drug-doses in 50 lines". Upstream / downstream are used only for the direction stage's arrows,
  which are **probable**: from cell lines, not proof of direct regulation.
- **One time point** (24 h), **cancer cell lines**, **most drug-doses in a single well**, **dose confounded with
  plate** (each dose on its own plate). Fold changes are against the same line's median drug well on the same plate,
  not DMSO; `lfc_vs_dmso` is a rough sign check against the plate's DMSO wells.
- **Neighbouring wells** can share a signal. 'like a neighbouring well' marks the genes a touching well moves the same
  way; at a drug's top dose the data cannot tell a carried-over signal from a real effect ('top dose': an alert, not an artifact flag).
- **Translation inhibitors** (Homoharringtonine, Harringtonine) raise short-lived mRNAs whatever their pathway: a rise
  there may be mRNA stabilisation, not activation. Read 'rise under a translation inhibitor' that way.
- **Two annotations.** Tahoe's annotation and ChEMBL's are shown side by side; where they disagree an alert says so.
  Neither is overwritten. A rule that needs a mechanism class names where the class came from.
- Pairs of neighbouring genes on the same strand can correlate through **readthrough** transcription; such pairs
  carry an alert and are never called novel.
- **⚠ marks a reason to doubt, not a verdict.** A flagged drug-dose's change may be its artifact (dying cells, a drop
  in transcription, a shift in the cell-cycle mix), or the drug's own effect; read the reason next to the ⚠.
- "Moves with / opposite" partners carry their evidence: `both halves` = the same sign in both halves of the
  compounds, with a false discovery rate ≤ 10% (the halves share the lines and plates: this guards against
  single-compound effects, not against everything); `one half` = strong in one half only (often one compound).
  Pooled lists are medians over the 50 lines: responses confined to a few lines are in the per-line tables.
- **Lineage pairs** (two genes expressed in few lines, mostly the same ones) move together whatever their regulation;
  **read-sharing copies** (near-identical paralogues, a pseudogene and its parent, a read-through transcript) can
  share reads. Both carry an alert; lineage_p says how unusual a lineage pair is.
- **Expression programmes.** Genes absent from overlapping sets of lines form a programme: an arrow from one of them
  gives no sign (which gene acts cannot be told). Arrows from natural knockouts and drug targets say 'may'.

## How to cite

The results derive from the Tahoe-100M dataset (Hugging Face `tahoebio/Tahoe-100M`), released under the licence
CC0-1.0. Please cite: Zhang J, Ubas AA, de Borja R, Svensson V, Thomas N, Thakar N, Lai I, Winters A, Khan U, Jones
MG, et al. Tahoe-100M: A Giga-Scale Single-Cell Perturbation Atlas for Context-Dependent Gene Function and Cellular
Modeling. bioRxiv 2025. doi:10.1101/2025.02.20.639398. The explorer's About page and the exported results' README say
the same; the public annotation sources each have their own terms (`reference/sources.json` names them).

## Repository layout

| Path | |
|---|---|
| `tahoe` | the command (Linux / macOS); Windows: `python -m tahoemap …` (see the quick start) |
| `tahoemap/review/` | the literature-review agents: agent and skill files (markdown with YAML front matter), dossiers, tools, verification, key pool, histories, the runner |
| `tahoemap/` | the package: `atlas_core.py` + `tlib.py` (ported method), `common.py` (shared helpers, the flag tokens and their words), `stream.py`, `tensor.py`, `reference.py`, `mechanisms.py` (drug classes), `tables.py`, `embed.py`, `relations.py`, `graph.py`, `direction.py`, `direction_view.py`, `validate.py`, `vault.py`, `html_map.py`, `explorer.py` (+ `tsf_reader.py`, `links.py`), `query.py`, `export.py`, `cli.py` |
| `tahoemap/data/drug_classes.json` | the drug mechanism classes, their rules and their cited sources (code constants; Tahoe's annotation is never a class rule) |
| `tahoemap/explorer_app/` | the explorer's pages (index.html, app.css, js/*.js; the stage joins the scripts into app.js) |
| `tahoemap/data/control_sets.json` | curated control programmes for validation (from the literature, not Tahoe) |
| `tahoemap/vault_seed/` | the written layer of the vault (add `genes/SYMBOL.md` to add knowledge; it survives rebuilds) |
| `docs/` | quick start, method, the two maps, the literature review ([review.md](docs/review.md)), design contracts |
| `tests/` | synthetic data generator, end-to-end tests, port test, review, Windows, export, direction, explorer and surface tests, the unit scripts of the second wave, the offline reference fixture (`tests/fixtures/reference_cache`) |
| `tools/port_from_old.py` | how the method was carried over |
