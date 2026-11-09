# Explorer data: the file format and every file

The pipeline stage `explorer` (code: `tahoemap/explorer.py`) turns a finished run into static web pages with all of
its data. This page describes the data files: their format (TSF1), where each file lives, and what each file holds.
The pages themselves are described in `docs/explorer.md`.

Nothing in these files is capped or filtered. Every list holds every row of its source table. Flags sit next to
the values; they never remove a row. Values are the bytes the pipeline stored.

## 1. Where the files are

The stage writes `OUT/explorer/`:

| Folder | What | Published as |
|---|---|---|
| `web/` | the page (`index.html`, `app.js`, `app.css`), `d/` (data files), `map/gene_map.html` | GitHub Pages branch `site` |
| `data/` | `x/` one file per gene, `p/` one file per drug-dose, `w/` parts moved by the size guard | repository `<repo>-data` |
| `data_dd/` | only with `--with-line-dd`: `y/` one file per drug-dose with every gene's per-line values | repository `<repo>-data-dd` |
| `manifest.json` | every file with its volume and bytes, the run id, the moves of the size guard | not published |

Each volume also holds `probe.js`, `README.md`, `MANIFEST.tsv` (path, bytes, sha256 of every other file) and
`.gitattributes` (`* -text`, so that git never changes a byte). `web/` also holds `.nojekyll` and `tsf_reader.py`.

The stage writes into `OUT/explorer.tmp/` and then swaps it in. A stage that stops leaves the previous
`OUT/explorer/` as it was.

## 2. The file format (TSF1)

Every data file is one ASCII line:

```
TAHOE_SHARD("<id>","<base64 of zlib.compress(container, 6)>");
```

`<id>` is the file's path inside its volume without `.js`, for example `core`, `g/06/0675`, `x/16/16642`. The page
reads a file with a `<script>` tag (same site or a local folder) or with `fetch` of its text (raw.githubusercontent.com).
The text matches `^TAHOE_SHARD\("([^"]+)","([A-Za-z0-9+/=]*)"\);\s*$`.

The container, after base64 decoding and zlib inflating:

```
bytes 0..3     b"TSF1"
bytes 4..7     H: the length of the header in bytes (uint32, little-endian)
bytes 8..8+H   the header: UTF-8 JSON (sorted keys, ASCII only, no NaN), then spaces up to a multiple of 8
from B0        the blobs. B0 = 8 + H rounded up to a multiple of 8. Blob offsets are relative to B0 and are
               multiples of 8; zero bytes pad between blobs.
```

The header:

```
{"fmt": 1, "id": "g/00/0000", "run": "856b4a94a590", "kind": "gene-bucket", "meta": {...},
 "arrays": {"lfc": {"t": "f32", "shape": [16, 282], "off": 0, "n": 18048, "sh": 1}, ...},
 "tables": {"rel": {"n": 800, "cols": [
     {"name": "_row", "t": "i32", "off": 18048, "n": 3200, "sh": 1, "pd": "int32"},
     {"name": "symbol_b", "t": "str", "v": ["TP53", null, ...], "pd": "str"},
     {"name": "evidence", "t": "dict", "d": ["both halves", "one half", "not reproduced"],
      "c": {"t": "u8", "off": 21248, "n": 800, "sh": 0}, "pd": "str"}, ...]}}}
```

- **Types (`t`):** `f32 f16 f64 i8 u8 i16 u16 i32 u32`. There is no 64-bit integer: an int64 column is stored as
  `i32` when every value fits, otherwise as `f64`.
- **`n`:** the blob's length in bytes (not the number of values).
- **`shape`:** arrays only. Table columns have the table's `n` rows.
- **`sh`: 1** means byte-planar: an array of k-byte items is stored as k planes (all first bytes, then all second
  bytes, ...). Un-shuffle before reading the numbers. Items of 1 byte are never shuffled.
- **Byte order:** little-endian.
- **Missing values:** NaN in float columns. An integer column with missing values has `"na"`: the value that marks
  them (`-2147483648` for `i32`; `255` for `u8` booleans).
- **`str` columns:** the values are in the header (`"v"`), `null` = missing.
- **`dict` columns:** the distinct values are in `"d"` (`null` = missing) and `"c"` is an array of codes into it.
- **`pd`:** the pandas dtype the column had in the source (`bool`, `boolean`, `int64`, `Int64`, `float32`, `str`,
  `object:bool`, ...). `tahoemap.explorer.read_shard` uses it to give back the column as it was. A `u8` column with
  `pd` `bool` or `boolean` holds 0 / 1 (and 255 = missing for `boolean`).
- **float16** has no JS typed array in older browsers: decode it through a 65,536-entry table. NaN stays NaN.

Reading in Python: `tsf_reader.py` (numpy only; also in `web/`), or `tahoemap.explorer.read_shard(path)`, which
returns `(header, arrays, tables)` with tables as pandas DataFrames.

## 3. Rules that hold in every file

- **Run id.** Every file carries `run`: the first 12 hex characters of sha256 over the sorted (stage, version,
  finished) of every other stage's stamp, and the explorer's VERSION. `d/core.js`, `d/hosts.js` and each volume's
  `probe.js` carry it too. A page must refuse a file whose run differs from `core.js` and say: "this data is from run
  X, the page from run Y: the data were re-published; reload".
- **`_row`.** Every record table starts with `_row`: the row of the source table (0-based, in the file's order).
  The stage checks, per source table, that the views hold every row they must (section 6).
- **Derived columns** start with `_` (`_role`, `_cmp`, `_dg`, `_n_edges`, `_grp`). Every other column is the source's
  column with the source's values.
- **Text is never shortened.** Strings are stored whole.
- **Flags.** `flag` arrays are codes into `d/flags.js`. Each code's string is exactly what `tables.flag_strings`
  writes for that (drug-dose, gene); the stage stops unless these strings equal `tables/drug_effects.parquet`
  `flags` on every row.

## 4. Small files

### `d/hosts.js` (plain JSON, not TSF1)

```
TAHOE_HOSTS({"data":["<data URL>/"],"data_dd":["<data_dd URL>/"],"release":[],"run":"<run>"});
```

`data`: where the data volume is published, in the order to try (`export --pin-data` puts the URL pinned to a
commit first). Empty when the stage had no `--data-url`: then only the local folder `../data/` is tried.

### `probe.js` in each volume (plain JSON)

```
TAHOE_PROBE({"counts":{"columns":C,"drugdoses":D,"genes":G,"lines":L},"explorer_version":1,"run":"<run>",
             "shards":<data files in this volume>,"volume":"web"|"data"|"data_dd"});
```

A page loads a volume's `probe.js` from each source in turn and keeps the first one whose `run` is right.

### `OUT/explorer/manifest.json`

`{"run", "explorer_version", "fits", "pages_max_mb", "moves": [...], "manifest_sha256": {volume: sha256 of its
MANIFEST.tsv}, "volumes": {volume: {"files", "bytes"}}, "files": [[volume, path, bytes], ...]}`.

## 5. The data files

Dimensions: G genes, C = G + 3 columns (the 3 summed atlas modules S_PHASE, G2M_PHASE, PROTEASOME are the last
columns), D drug-doses, L lines, W wells, P plates, M modules, Dr drugs (in the order of `tables/drugs.parquet`,
sorted by name), K vector dimensions, Ccc cell-cycle-flagged drug-doses (`core.js` `cc_dd`).

Paths (zero-padded numbers): `d/g/{b//100:02d}/{b:04d}.js` with b = col // 16; `x/{col//1000:02d}/{col:05d}.js`;
`p/{dd//100:02d}/{dd:04d}.js`; `y/{dd//100:02d}/{dd:04d}.js`; `d/l/{line:02d}.js`; `d/m/{module:03d}.js`;
`d/dg/{k:03d}.js`; `d/dr/{i:03d}.js`. `core.js` meta `paths` repeats these.

### Web volume, `d/` (kind in brackets)

**`core.js`** (`core`)
- arrays: `cc_dd` i32 [Ccc] (the cell-cycle-flagged drug-doses, the order of the `cc` arrays); `drug_of_dd` i32 [D]
  (row of `tables/drugs.parquet` for each drug-dose); `well_umi` f64 [W] (tensor/well_umi.npy).
- tables (every column of the source, plus `_row`): `drugdoses` (tables/drugdoses.parquet), `edd`
  (embed/drugdoses.parquet), `drugs` (tables/drugs.parquet), `edrugs` (embed/drugs.parquet), `lines`
  (tables/lines.parquet), `plates` (tables/plates.parquet), `wells` (tables/wells.parquet), `plate_scale`
  (atlas/effects/plate_scale.csv), `failed_wells` (atlas/effects/failed_wells.csv), `sample_map`
  (atlas/sample_map.csv), `modules` (graph/modules.parquet), `mlabels` (validation/module_labels.csv), `components`
  (embed/components.parquet), `broad` (embed/broad_components.csv), `fdr_curve` (relations/fdr_curve.csv); and
  `drivers` (line, gene, type, change: tables/lines.parquet drivers and driver_changes split per gene).
- meta: `run`, `explorer_version`, `versions` (per stage), `commit`, `site_url`, `data_url`, `repo`, `results_url`,
  `counts`, `constants` (Q_CUT, LFC_MIN, KEEP_Z, LINE_Z, STRONG_LFC, line_z_threshold, min_cells,
  unreliable_plates, DEPLETE_Z, ABUNDANCE_UNTRUSTED, ARTIFACT_FLAGS, CC_CLEARED, PATTERNS, MAX_LINES_LISTED,
  TOP_CELLS, PLATE_SCALE_FLAG, BUCKET, DG_PER_SHARD, and the relations rules REPRO_MIN, REPRO_FDR, ONE_HALF,
  REL_TOP), `FLAG_WORDS` (plain words for every flag token), `column_docs` ({"<file>": {"intro", "cols"}} for
  tables/*, direction/edges and groups, relations/gene_relations and fdr_curve, graph/nodes, edges and modules,
  reference/annotations, gene_sets and string_pairs, embed/genes, drugs, drugdoses, contexts, components and
  broad_components, and every validation CSV, read from validation/README.md; explorer.EXTRA_DOCS holds the ones
  whose stage writes no column docs),
  `arrays` (what each array of g/, x/, p/, y/ holds), `paths`, `where` ({move: "data"}), `moves`, `missing`
  (source files that were not there), `stamps` (every other stage's stamp), `info` (the info.json files of the run),
  `vault` ({available, home, plate}), `map`, `app`, `baseline_note`, `line_dd`, `pooled_r`.

**`flags.js`** (`flags`): table `flags`, one row per code: `s` (the exact flags string; code 0 is ""), `clean` (u8:
1 = no artifact flag), `art` (artifact tokens), `cav` (other tokens), `ccc` (the cleared cell-cycle token "cell-cycle
shift (explains ~N% here)"), `n` (cells with this code). Meta: `words`, `artifact_flags`, `no_words` (tokens without
words; empty), `dtype` (`u16`, or `u32` above 65,536 strings).

**`search.js`** (`search`): tables `g` (genes: col, symbol, label, ensembl_id, noise_rna, and from
reference/annotations: hgnc_id, hgnc_symbol, name, aliases, prev_symbols, entrez_id, uniprot, location, chrom,
biotype, locus_type; included from embed/genes; module (0 = in the space, in no module; empty = not in the space)
and arm from graph/nodes), `d` (drugs: drug, salt_base, targets, moa_fine, moa_broad,
approved), `l` (lines: line, cell_name, cell_line_id, Cell_ID_DepMap, Organ, drivers, driver_changes, tp53_status),
`m` (modules: module, n_genes, top_plus, top_minus, label), `s` (gene sets: source, set, set_id, set_size,
n_present), `q` (direction groups: group_id, kind, gene, gene_col, description).

**`below.js`** (`below`): table `b` (symbol, ensembl_id, token_id): the Tahoe genes below the atlas's detection cut,
from the Tahoe gene metadata (atlas/file_index.json). Meta `available` False with `reason` when it is not reachable.

**`ddarr.js`** (`ddarr`): arrays f32 `DD_A`, `DD_Az`, `DD_beta`, `DD_rcor` [D, L], `DD_r2_modules` [D, L, 3];
`usable` u8 [D, L] (used wells of the drug-dose where the line has at least min_cells cells); `well_line_cells`,
`well_line_umi` [W, L]; `module_pooled_z` [M, D] (row m-1 = module m); `drugdose_vectors` [D, K], `drug_vectors`
[Dr, K], `line_baseline_vectors`, `line_response_vectors` [L, K], `singular_values` [K]; per well x line `A2`, `zA`,
`VA`, `wbeta`, `wrcor` [W, L] and `wr2` [W, L, 3] (atlas/effects A2, zA, VA, beta, rcor, r2_modules). Table
`contexts` (embed/contexts.parquet).

**`genes.js`** (`genes`): tables `genes` (tables/genes.parquet), `egenes` (embed/genes.parquet), `agenes`
(atlas/effects/genes.csv: every column, the 3 modules included).

**`space/u.js`, `space/h1.js`, `space/h2.js`** (`space`): `included` i32 [Ni] (embed/included_cols) and `unit` f32
(embed/gene_unit, gene_unit_half1, gene_unit_half2): rows of `included` only when every other row is NaN (meta
`rows` = "included"), else every row (`rows` = "all"). `u.js` also `row_mean`, `row_scale` [Ni].
**`space/ctx.js`**: `vectors` f32 [contexts, K] (embed/context_vectors; rows = contexts j).

**`linecpm.js`** (`linecpm`): `line_cpm` f32 [L, C], `expr_mask` u8 [L, C], `line_measured` u8 [L, G].

**`sets.js`** (`sets`): table `sets` (reference/gene_sets.parquet, every row).

**`groups.js`** (`groups`): table `groups` (direction/groups.parquet, every row and column, plus `_cmp` its
comparison number, `_dg` its `d/dg/` file, `_n_edges` its arrows); table `cmp` (the comparisons that only arrows
name, such as drug targets and gene levels: `_cmp`, `text` (the edges' `group` text), `kinds`, `n_edges`, `_dg`).
Comparisons are numbered: every group by `group_id`, then every other `group` text by text. An arrow belongs to the
group whose `description` equals its `group` text.

**`val.js`** (`val`): tables `control_sets`, `drug_moa`, `module_enrichment`, `module_labels`, `novel_edges`,
`novel_members`, `opposite_pairs` (validation/*.csv) and `well_position_check` (atlas/well_position_check.csv).
Meta: `metrics` (validation/metrics.json), `report` (validation/report.md), `direction_controls`
(direction/controls.json).

**`docs.js`** (`docs`): meta `docs` {path: text}: tables/README.md, direction/README.md, validation/README.md,
atlas/effects/README_effects.md and every `docs/*.md` of the code.

**`files.js`** (`files`): table `files` (pattern, where, view, what, files, bytes): every file pattern of OUT
(`explorer.INVENTORY`) with where it is in the explorer or why it is not, and its files and bytes in this run; table
`unmapped` (path, bytes): files the inventory does not describe (empty when complete).

**`pooledr.js`** (`pooledr`, only with `--with-pooled-r`): `zq` i16 [G, D]: pooled z x 100 rounded (-32768 = NaN),
a ranking helper for pooled-profile r against every gene.

**`g/NN/BBBB.js`** (`gene-bucket`, 16 genes or fewer; meta `bucket`, `cols` [c0, c1), `symbols`)
- arrays: `cols` i32 [n]; `lfc`, `z`, `q_up`, `q_dn` f32 [n, D] (DD_lfc, DD_z, DD_qup, DD_qdn, exact); `flag`
  u16 [n, D]; `nl` u8 [n, D, 5]; `cc` f32 [n, Ccc]; `pat` i8 [n, Dr, 2]; `lcen`, `lsc` f32 [n, L]; `gvec` f32 [n, K].
- `nl[..., k]`, counted over the lines: 0 lines with a value; 1 lines with per-line z >= 2 and fold >= 1.2; 2 lines
  with z <= -2 and fold <= 1/1.2 (the drug_effects n_lines_* rule); 3 lines with z >= t and lfc >= log2 1.5; 4 lines
  with z <= -t and lfc <= -log2 1.5 (t = `line_z_threshold`, the line_effects rule). From `tables.line_counts`.
- `pat[g, drug, 0 / 1]`: the drug's dose pattern for the gene, rise / fall: codes into `PATTERNS`
  (`tables.dose_shape_codes`); -1 = not computed.
- tables (each with `_row`): `genes`, `egenes`, `ann` (reference/annotations.parquet), `sets`
  (reference/gene_sets.parquet), `string` (reference/string_pairs.parquet: every pair touching a gene of the bucket),
  `le` (tables/line_effects.parquet), `dlt` (tables/drug_line_top.parquet), `rel` (relations/gene_relations.parquet
  rows with col_a in the bucket, every column), `relb` (rows with col_b in the bucket: col_a, col_b, rank, cos,
  evidence, alert), `node` (graph/nodes.parquet), `gedge` (graph/edges.parquet touching), `dir`
  (direction/edges.parquet rows with source_col or target_col in the bucket, every column, plus `_role` = source /
  target / both), `dgrp` (direction/groups.parquet with gene_col in the bucket), `nmem`
  (validation/novel_members.csv), `nedge` (validation/novel_edges.csv touching), `vault` (col, gene, plates: the
  gene's vault notes, from vault/.tahoemap-paths.json; vault/Home.md without that file).
- `tables/drug_effects.parquet` rows are not stored here: the arrays reproduce every one of them (notable =
  |z| >= KEEP_Z or q_up < 0.10 or q_dn < 0.10; the stage checks each row).

**`g/mod.js`** (`gene-modules`): the 3 summed modules: `cols`, `lfc`, `z`, `q_up`, `q_dn`, `flag` [3, D]; table
`agenes` (their atlas/effects/genes.csv rows). Their flags are the atlas's gene-level rule on the module column.

**`l/LL.js`** (`line`; meta `line`, `cell_name`, `cell_line_id`, `vault`): array `ms` f16 [M, D]
(graph/module_scores.npy at the line); tables `le` (every line_effects row of the line), `grp` (`_grp` row of
direction/groups.parquet, group_id, side altered / intact: every group whose altered_lines or intact_lines name the
line), `comp` (atlas/effects/composition_shift.parquet rows of the line).

**`m/MMM.js`** (`module`; meta `module`, `vault`): arrays `pz` f32 [D] (module_pooled_z row), `ms` f16 [D, L]
(module_scores row); tables `module` (graph/modules.parquet row), `label` (validation/module_labels.csv row),
`members` (graph/nodes.parquet rows of the module), `enr` (validation/module_enrichment.csv rows), `nmem`
(validation/novel_members.csv rows), `edges` (graph/edges.parquet rows with both ends in the module). `m/000.js`
holds the genes of the space that no module took (no arrays).

**`dg/KKK.js`** (`dir-groups`; meta `cmp` [first, last+1)): comparisons 32k to 32k+31: tables `groups` (their
direction/groups.parquet rows, plus `_cmp`) and `edges` (every arrow of these comparisons, every column, plus `_cmp`).

**`dr/III.js`** (`drug`; meta `drug`, `drug_index`, `dds`, `vault`): tables `de` (every tables/drug_effects.parquet
row of the drug's doses, every column), `dir` (direction/edges.parquet rows that are drug_target arrows naming the
drug in `compounds`, or whose target_dd is one of its doses), `edrug` (embed/drugs.parquet row), `moa`
(validation/drug_moa.csv row of its moa_fine), `ctl` (validation/control_sets.csv rows whose best_dd_up or
best_dd_down name the drug).

### Data volume

**`x/NN/CCCCC.js`** (`gene-lines`; meta `col`, `symbol`, `label`): `lfc`, `z` f16 [D, L] (tensor/DDL_lfc.npy,
DDL_z.npy at the gene, exact); `poseff` f32 [D] (DD_poseff); `w1`, `w2`, `wz` f32 [W] (W1, W2, Z); `counts` f32 [W]
(tensor/well_counts.npy; raw CPM = counts / well_umi x 1e6); `wpu` u8 [W] (posunc); `pbase` f32 [P, L]
(tensor/plate_base.npy); `poff` f32 [P] (plate_offset); `slot` f32 [96] (slot_median); `psg` f32 [plate-scale
groups] (plate_scale_gene). The 3 module columns have no `lfc`, `z`, `counts`, `pbase` (meta `module`, `absent`).

**`p/NN/DDDD.js`** (`drugdose`; meta `dd`, `drug`, `dose`): every column at the drug-dose: `lfc`, `z`, `q_up`,
`q_dn`, `poseff` f32 [C]; `flag` u16 [C]; `nl` u8 [C, 5] (255 for the modules); `pat` i8 [C, 2] (the drug's
pattern; -1 for the modules); `cc` f32 [C] (only at a cell-cycle-flagged drug-dose); `ms` f16 [M, L].

**`w/<web id>.js`** (`moved`; meta `from`, `part`, `move`): a part the size guard moved out of web file
`d/<web id>.js`. The web file's meta `moved` names it, and `core.js` `where` lists the moves.

### data_dd volume (optional)

**`y/NN/DDDD.js`** (`drugdose-lines`; meta `dd`, `drug`): `lfc`, `z` f16 [G, L] (every gene's per-line values at
the drug-dose, exact).

## 6. Checks the stage makes (and the stamp)

The stage stops, and leaves the previous explorer as it was, when:
- any `tables/drug_effects.parquet` row differs from the explorer's values (lfc, fold, z, q, flags, clean, cc_share,
  n_lines_*, pattern_*, symbol, drug, dose, conc), or the rows are not exactly the notable pairs;
- the lines_up / lines_down names (12 at most) differ from the names the per-line values give;
- a view lacks a source row it must hold (R1);
- a file is above 95 MiB, a folder holds more than 1,000 entries, or a path is longer than 80 characters;
- the self-check finds a difference: every 97th data file and every top-level web file are decoded and compared
  with the sources (arrays bit for bit, tables row by row through `_row`);
- the web volume is above `--pages-max-mb` (default 950 MiB) after every move (section 7).

`stages/explorer.json` info: `run`, `assets_sha` (sha256 of tahoemap/explorer_app), `volumes` (files and bytes),
`web_bytes_before_moves`, `moves`, `parts` (bytes per folder), `complete` ({source: {"rows", "views": {view: [held,
must hold]}}}), `complete_ok`, `checks` (drug_effects, lines_up_down, limits, self_check), `warnings`, `missing`,
`unmapped_files`, `flag_words_missing`, `map`, `app`, `steps_s` (seconds per step), `peak_rss_mb`, `minutes`.

## 7. The size guard

Above `--pages-max-mb`, these parts move from the web volume to the data volume, in this order, until the web volume
fits: `l.ms` (the line files' module scores), `g.rel` (the gene buckets' `rel` tables), `m.ms` (the module files'
module scores). A moved part keeps its bytes (the container is split, not re-encoded). If the volume is still too
large, the stage stops with the size of each part. It never drops data.

## 8. What a page must handle

- A file whose `run` is not `core.js` `run`: refuse it and say the data were re-published.
- A data volume that cannot be reached (no local `../data/`, no host in `hosts.js`, or every host fails): say which
  file, where it lives and how to get it. Everything in the web volume still works.
- `core.js` `missing`: source files the run did not have. Say which file is missing instead of showing an empty list.
- `core.js` `where`: parts moved to the data volume; load them from `w/<id>.js`.
- `index.html` without the app files: the stage wrote a page that says the app files are missing.

## 9. Sizes on the real data

Measured on the published real tables and on arrays at the real dimensions (16,643 genes, 1,132 drug-doses, 50
lines, 1,329 wells, 14 plates): web volume about 0.66 GB (gene buckets 0.48 GB, of which records 0.19 GB), about
1,970 files; data volume about 5.2 GB (x/ 4.8 GB, p/ 0.43 GB), 17,782 files; data_dd about 4.3 GB. The largest web
file is the map (about 25 MB); the largest data files are about 0.3 MB (x/) and 0.4 MB (p/).
