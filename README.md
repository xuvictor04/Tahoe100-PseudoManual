# Tahoe-100M gene map (branch `finalized`)

One command turns [Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M) — 50 cancer cell lines × 379
drugs × 3 doses, ~96 million single cells at 24 h — into a map of **every gene, drug and cell line**, so that for any
gene you can:

1. **see which drugs raised it (or lowered it)**, at which dose, how strongly, and with which caveats;
2. **see in which cell lines** it happened, against each line's own baseline;
3. **see which other genes move with it, and which move opposite to it**, how sure that is, and whether the relation
   is already known (STRING, Reactome, Hallmark, HGNC gene groups) or a candidate new one.

```bash
~/tahoemap-repo/tahoe setup     # once
tahoe run --stream              # everything; reads the data straight from Hugging Face (or: tahoe download; tahoe run)
tahoe gene MDM2                 # then ask
```

Start with [docs/quick-start.md](docs/quick-start.md). `tahoe test` runs the whole pipeline on synthetic data with
planted answers in a few minutes.

## What a run produces

| Output (under `<data>/tahoemap/`) | What it is |
|---|---|
| `vault/` | **An Obsidian vault**: a note per gene (16k+), drug, cell line, plate and module, linked; each gene note has the drugs that raise / lower it, the cell lines, the genes that move with / opposite it, its place in the map, registry facts (HGNC, UniProt, NCBI) and a companion note with the raw and corrected per-well values laid out plate by plate |
| `map/gene_map.html` | **The interactive map**: every gene on the nodal map or the signed vector map, searchable; click a gene for its partners, drugs and lines |
| `validation/report.md` | How well the space recovers known biology, the opposite-arm test, module labels, and **novel candidate relations** |
| `tables/` | The fold-change tables (parquet): per gene × drug-dose, per gene × cell line, per (drug-dose, line), per gene, drug, line, plate, well — every column documented in `tables/README.md` |
| `relations/gene_relations.parquet` | Gene × gene: each gene's 100 strongest partners, signed, with split-half evidence, FDR and known / locus / readthrough flags |
| `embed/` | The vector space: gene, drug-dose, drug, (drug-dose × line) and cell-line vectors |
| `graph/` | The nodal map: modules with their + / − arms, layouts, module scores per drug-dose and line |
| `tensor/` | Per-cell-line layer: every gene × drug-dose × line fold change and z; raw counts per well |
| `atlas/` | The build (counts per well × line × gene) and the corrected effects (method v3) |

`tahoe gene / drug / line / pair / module` answer from these files in the terminal.

## The stages

`tahoe run` runs every stage that is missing or out of date, in order, and can be stopped and resumed:

| Stage | What it does | Real-data time |
|---|---|---|
| build | one pass over all cells → counts per well × cell line × gene (`--stream`: no download) | 0.5–2.5 h |
| effects | the corrected effect of every drug-dose on every gene (composition, plate, well-position corrections; flags) | ~10–20 min |
| tensor | the same per cell line: gene × drug-dose × line fold changes and z | ~10–20 min |
| tables | the fold-change tables | ~2–5 min |
| embed | the vector space (genes, drugs, contexts, lines), also fitted on two halves of the compounds | ~5 min |
| reference | public annotations, downloaded once and cached (`--offline` skips) | ~3 min |
| relations | gene × gene partners, evidence, FDR, known / novel | ~5 min |
| graph | modules, arms, the nodal map and the signed map | ~5–10 min |
| validate | control programmes, opposite-arm test, module labels, novel candidates | ~2 min |
| vault | the Obsidian vault | ~5 min |
| map | the interactive HTML map | ~1 min |

[docs/method.md](docs/method.md) explains every step and every flag.

## The vector space and the nodal map

Each gene is a vector built from how it moves across every (drug-dose, cell line) context; drugs, drug-doses,
contexts and cell lines are vectors in the same space, and a gene vector · a drug vector ≈ that drug's effect on the
gene. In the vector space, two genes that move in opposite directions (the induced and the repressed arm of one
pathway) point opposite ways and sit far apart; on the nodal map, which uses |cosine|, they sit together, as one
island with a + arm and a − arm. On planted data the opposite modules have cosine −0.7 yet share one island.
[docs/vector-space-and-nodal-map.md](docs/vector-space-and-nodal-map.md) explains it in full.

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
```

The synthetic data plant drug effects (some only in TP53-wild-type lines), co-regulated modules, pairs of modules
moved in opposite directions, un-moved genes, and every artifact the method corrects. The tests check each stage
against them: per-line effects appear only where planted, planted modules are tight in the space, opposite modules
point opposite ways and share a nodal-map island on opposite arms, un-moved genes rarely form strong relations, the
FDR is monotone and calibrated, the vault has a note per gene and no broken links.

## Read the results with these in mind

- **Correlation across drug responses is not mechanism.** No genes were knocked out; "moves with" means "responds
  alike to ~1,100 drug-doses in 50 lines". Upstream / downstream are kept for regulatory claims.
- **One time point** (24 h), **cancer cell lines**, **most drug-doses in a single well**, **dose confounded with
  plate**. Fold changes are against the same line's median drug well on the same plate, not DMSO.
- Pairs of neighbouring genes on the same strand can correlate through **readthrough** transcription; such pairs are
  flagged and never called novel.
- "Moves with / opposite" partners carry their evidence: `both halves` = replicated in two random halves of the
  compounds with a false discovery rate ≤ 10%; `one half` = strong in one half only (not replicated, often one
  compound). Pooled lists are medians over the 50 lines: responses confined to a few lines are in the per-line tables.

## Repository layout

| Path | |
|---|---|
| `tahoe` | the command (Linux / macOS); Windows: `python -m tahoemap …` (see the quick start) |
| `tahoemap/` | the package: `atlas_core.py` + `tlib.py` (ported method), `stream.py`, `tensor.py`, `tables.py`, `embed.py`, `reference.py`, `relations.py`, `graph.py`, `validate.py`, `vault.py`, `html_map.py`, `query.py`, `cli.py` |
| `tahoemap/data/control_sets.json` | curated control programmes for validation (from the literature, not Tahoe) |
| `tahoemap/vault_seed/` | the written layer of the vault (add `genes/SYMBOL.md` to add knowledge; it survives rebuilds) |
| `docs/` | quick start, method, the two maps, design contract |
| `tests/` | synthetic data generator, end-to-end tests, port test |
| `tools/port_from_old.py` | how the method was carried over |
