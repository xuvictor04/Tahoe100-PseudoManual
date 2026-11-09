# Tahoe-100M gene map: results

Exported by `tahoemap export` on 2026-11-09 11:34:17 from the output folder `C:\tahoe\out`. Everything here was computed by tahoemap from the Tahoe-100M single-cell drug screen and public annotation sources (reference/sources.json names them); the code is the tahoemap repository named under Provenance.

## What each folder holds

| folder / file | files | size | what it is |
|---|---|---|---|
| `vault` | 34,286 | 696.8 MiB | the Obsidian vault: a note per gene, drug, cell line, module, plate and concept, and indexes (start at vault/Home.md) |
| `map` | 1 | 19.5 MiB | gene_map.html: the interactive gene map, one self-contained HTML file (works offline) |
| `tables` | 11 | 58.8 MiB | the fold-change tables: which drug-doses raise / lower each gene, pooled and line by line, with flags (parquet; tables/README.md documents every column) |
| `validation` | 10 | 7.0 MiB | does the vector space recover known biology, and what in it is new (start at validation/report.md; README.md there documents the columns) |
| `direction` | 5 | 14.9 MiB | probable direction between genes, from the cell lines (which gene acts on which, or on the cells' growth under a drug): edges with p, q, an evidence grade A / B / C and their alerts, the groups compared and the controls (direction/README.md documents every column; a probable direction, not proof of direct regulation) |
| `graph` | 6 | 29.2 MiB | the nodal map: nodes (map coordinates, module, arm), edges and modules (parquet) |
| `relations` | 3 | 57.9 MiB | gene x gene: each gene's 100 strongest partners, how reproducible, known or new (parquet) |
| `embed` | 20 | 29.3 MiB | the vector space: gene, drug-dose, drug and cell-line vectors (numpy .npy) and their tables |
| `stages` | 12 | 0.0 MiB | one stamp per finished stage: its method version, when it finished, its counts and options |
| `reference` | 4 | 10.2 MiB | public annotation reduced to Tahoe's genes (annotations, gene sets, STRING pairs; parquet) and sources.json (where each source came from) |
| `run.log` | 1 | 0.0 MiB | the log of every pipeline command run on this output |

In all: 34,359 files, 923.7 MiB. `MANIFEST.tsv` lists every file with its size and sha256 (README.md and .gitattributes included; the manifest itself not); `.gitattributes` (`* -text`) makes git store every file byte for byte.

## How to open them

- **The vault**: get the files (clone the repository, or GitHub's *Code - Download ZIP*), then in [Obsidian](https://obsidian.md) choose *Open folder as vault* and pick the `vault` folder. Start at `Home.md`; `How to read this vault.md` explains the notes. On GitHub itself the notes read as plain Markdown, but the [[links]] between them do not work there.
- **The map**: `map/gene_map.html` is one self-contained file. GitHub shows HTML as source code: download the file (*Download raw file*, or clone), then open it in any current browser (Chrome, Edge, Firefox, Safari); it needs no network.
- **The tables**: parquet files, e.g. `pandas.read_parquet("tables/drug_effects.parquet")` in Python or `arrow::read_parquet()` in R; each folder's README.md documents the columns.
- **The validation**: `validation/report.md` reads well on GitHub.

Flags: nothing is left out of a table for a flag; an item with a reason for doubt keeps its ranked place and carries an alert (⚠ and the reason in plain words).

## Provenance

- tahoemap version 1.0.0; code commit `d523eaef3641ab1cb2ef677abf89f57cf80cdd89` on branch `finalized` of https://github.com/xuvictor04/Tahoe100-PseudoManual; no uncommitted changes
- exported 2026-11-09 11:34:17

Stage stamps (`stages/<stage>.json` holds each stage's counts and options):

| stage | method version | finished | state |
|---|---|---|---|
| build | 3 | 2026-11-07 19:57:35 | done |
| effects | 3 | 2026-11-07 20:01:33 | done |
| tensor | 2 | 2026-11-07 20:04:35 | done |
| tables | 4 | 2026-11-09 10:49:27 | done |
| embed | 4 | 2026-11-09 10:50:12 | done |
| reference | 1 | 2026-11-09 11:02:09 | done |
| relations | 4 | 2026-11-09 11:02:27 | done |
| graph | 5 | 2026-11-09 11:04:13 | done |
| direction | 2 | 2026-11-09 11:07:29 | done |
| validate | 4 | 2026-11-09 11:07:47 | done |
| vault | 4 | 2026-11-09 11:10:25 | done |
| map | 6 | 2026-11-09 11:10:38 | done |

## What was left out, and why

- `reference/downloads`: the raw downloaded sources (public files; reference/sources.json says where each came from and when)
- `atlas/effects`: the pooled drug-dose x gene matrices (hundreds of MB each at full scale): only with --with-effects
- `.not_tahoe_input`: a marker that keeps the old scripts from reading the output as input data
- `tensor`: the per-cell-line arrays (several GB at full scale): the tensor stage computes them again from atlas/effects
- `atlas/pseudobulk`: the build: per-well pseudobulk counts (tens of GB at full scale); the build stage makes it again from Tahoe-100M
- `atlas/build_info.json, atlas/file_index.json, atlas/sample_map.csv, atlas/well_position_check.csv`: the atlas's index and build records (stages/build.json and stages/effects.json record the build)

## Checking the files

From this folder, every file against MANIFEST.tsv:

```
python -c "import hashlib; rows = [l.rstrip('\n').split('\t') for l in open('MANIFEST.tsv', encoding='utf-8')][1:]; bad = [p for p, n, h in rows if hashlib.sha256(open(p, 'rb').read()).hexdigest() != h]; print(len(rows), 'files,', len(bad), 'differ:', bad[:10])"
```
