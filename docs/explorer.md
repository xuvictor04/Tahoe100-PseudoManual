# The explorer: a searchable page over the whole run

The explorer is a set of web pages made by the pipeline stage `explorer`. It shows every gene, drug, drug-dose,
cell line, module and probable-direction arrow of the run, with every value the pipeline stored. You search a name
and follow links. Nothing is hidden:

- every list holds every row of its source table;
- a flag (for example "toxic" or "cell-cycle shift") never removes a row. It is written in the row, in red with ⚠
  when it is an artifact flag, and the row keeps its place in the sort;
- filters are off until you turn one on. A yellow banner then says how many rows they hide;
- numbers are the stored numbers, and downloads give them back bit for bit;
- an empty value always says why it is empty.

The data files and their format are described in [explorer-data.md](explorer-data.md).

## 1. Opening it

| Where | How |
|---|---|
| On your computer | Double-click `OUT/explorer/web/index.html`. The per-line data come from the folder `OUT/explorer/data` next to it, so no network is needed. |
| Online | The GitHub Pages site of the repository (branch `site`), for example `https://<owner>.github.io/<repo>/`. Per-line data come from the data repository named in `d/hosts.js`. |
| A copy of the `site` branch | Works like the online site. Without the network, the per-line tabs say which file is missing and where it lives. |

It needs a current browser: Chrome or Edge 80 or later, Firefox 113 or later, or Safari 16.4 or later. It uses no
server, no cookies, no web fonts and no outside scripts.

The footer of every page says where the per-line data come from: "local folder", "online (...)", or "not reachable"
with the reason. It also gives the run id, the code commit and the version of every stage.

### Where the data live

| Volume | Folder | What it holds | Used by |
|---|---|---|---|
| web | `OUT/explorer/web` (the site) | the pages, `d/` with the pooled value of every gene at every drug-dose, every record table, the vector space, the module and line files | every page |
| data | `OUT/explorer/data` (folder next to `web`, or the data repository) | `x/` one file per gene: its per-line values, per-well values and plate baselines; `p/` one file per drug-dose: every gene's pooled values there | per-line tabs, wells, the drug and drug-dose gene lists |
| data_dd (optional, `--with-line-dd`) | `OUT/explorer/data_dd` | `y/` one file per drug-dose: every gene in every line | the drug-dose Per-line values tab |

When the data volume cannot be reached, everything from the web volume still works, and each page that needs the
data volume names the missing file and where it lives.

## 2. What the numbers are

- **Fold change** is this drug-dose against the same cell line's median over the plate's drug wells. It is **not**
  against DMSO. It is corrected for the library-size (composition) shift and for the position of the well on the
  plate. The DMSO offset of each plate is on the gene's "Baseline & wells" tab.
- **Pooled** values combine all cell lines: per well, the median over the lines; per drug-dose, the mean over its
  used wells. They are float32 numbers, as stored in `atlas/effects`.
- **Per-line** values are one cell line at one drug-dose. They are float16 numbers, as stored in `tensor/`.
- **z** is the robust z of the change (Stouffer over the wells, divided by the plate factor). **q rise** and
  **q fall** are false-discovery-rate values for a rise and a fall, per gene over all drug-doses.
- **Fold** = 2^(log2 fold change). It is computed in the page and marked "(computed)".
- **Call**: "up" when q rise < 0.10 and the fold is at least 1.2; "down" when q fall < 0.10 and the fold is at most
  1/1.2. This is the rule of `tables/drug_effects`. It is a column, not a filter.
- **DD_A** is the log2 relative number of cells of a line at a drug-dose, against the other lines in the same wells.
  **DD_Az** is its z. DD_Az ≤ −3 means the line is depleted. Cell counts of a drug-dose flagged "unreliable plate
  only", "position not correctable" or "wells disagree" are less trustworthy; the row says so.
- **Module score**: the mean z of a module's + arm minus the mean z of its − arm.
- **cos**: the cosine of two vectors of the vector space. +1 means the same response, −1 the opposite.

Numbers are written with the fewest digits that read back to the exact stored value. The "short numbers" box at the
top rounds them to 3 digits for reading; the row drawer and every download keep the exact values.

## 3. Search

The search box is at the top of every page (press `/` to jump to it). Results appear as you type, grouped by kind,
each with the field that matched. Enter opens the first result. "All matches" opens a page that lists every match.

- **Genes** are found by symbol, label, Ensembl id, HGNC id and symbol, aliases, previous symbols, words of the
  name, Entrez id, UniProt id and cytoband.
- **Drugs** by name, salt base, each target, and mechanism of action (fine and broad).
- **Cell lines** by name (also without punctuation: "NCIH460" finds NCI-H460), Cellosaurus id, DepMap id, organ,
  driver gene, protein change (for example "R273H") and TP53 status.
- **Modules, gene sets and direction groups** are searched too.
- **Two words** give a combined view: "TRIM72 A549" opens TRIM72 in the line A549; "TRIM72 idarubicin" opens TRIM72
  under every dose of idarubicin, in every line.
- **Prefixes** `gene:`, `drug:`, `line:` and `module:` search one kind only.

Best matches come first: an exact name or id, then an exact alias, then names that start with the text, aliases that
start with it, a whole word (of a name, target, mechanism or organ), and last any piece of text.

An alias opens the gene with a notice, for example "MG53 is an alias of TRIM72 (HGNC)". A Tahoe gene below the
detection cut (pooled level under 2 counts per million) has no values; the search says so instead of "not found".
An unknown name of any kind (gene, drug, line, drug-dose, module, group, plate) opens the search with a notice, and
the search shows the nearest names (2 letters different or fewer).

## 4. The pages

Every page of a kind has the same tabs in the same order, and every tab label carries its count, for example
"All genes (16,643 + 3)" or "Cell lines (50 × 3)". Every name in every table is a link to its page.

### Home (`#/`)

The search box, example searches, what the run holds (counts and method), the Browse lists (with every cell line by
organ), and links to the map, the vault, the documents, "What is where" and Downloads.

### Browse (`#/browse/<list>`)

Complete, sortable tables: genes, drugs, drug-doses, cell lines (by organ), modules, direction groups, and every
probable-direction arrow (built from the direction files when the list is opened).

### Gene (`#/gene/<symbol>`)

The top of the page names the gene: symbol, HGNC name, cytoband and position, biotype, every alias and previous
symbol, its module and arm, the number of lines that truly express it, and links (vault note, plates note, map,
HGNC, Ensembl, UniProt, NCBI, GeneCards).

| Tab | What it holds |
|---|---|
| Overview | Four short answers: what moves the gene (with the strongest rises and falls; a flagged row keeps its place with ⚠ and its flags), in which lines, what moves with it, and what probably acts on it. Each preview says "k of N shown" and links to the full list. |
| Drugs | Every drug-dose (1,132 on the real data): fold, log2 fold change, z, q rise, q fall, call, flags in full, line counts, dose patterns, whether the row is in `tables/drug_effects`, the position effect removed, the z the vector space predicts, the drug's mechanism, targets and flags. The list starts with the strongest rise, so a flagged strongest raiser is the first row. Click a row for every field and the per-line values. |
| Cell lines | The per-line block: a heatmap of every line at every drug-dose (never averaged), a long table with one row per (drug-dose, line), and the pipeline tables `line_effects` and `drug_line_top`. Rows can be ordered by organ, TP53 status, a driver gene or response; columns by pooled z, drug or mechanism. Group rows (for example "mean of the TP53-altered lines") can be added; they are computed in the page and labelled so. |
| Correlations | (a) the cosine with every other gene of the vector space, with both halves, z, fdr and evidence (the 100 stored partners show the pipeline's own values; the rest are computed in the page with the same formulas); (b) baseline co-expression across the lines; (c) pooled-profile r for one partner through the pair page. |
| Partners & module | The stored partners with every column and alert, the genes that list this one, STRING partners, gene sets, graph edges, and the module: every member, its pooled z at every drug-dose and its per-line scores. |
| Direction | Every probable-direction arrow into the gene, from it to other genes, and from it to how many cells remain, with every alert (⚠, in full), note (muted, in full), support reason and the drug-doses behind it. The caveat every arrow of a kind carries is written once above each list. |
| Baseline & wells | The level in each line, the plate baselines that every fold change is relative to, the DMSO offset per plate, the well-position medians as a 96-well grid, and every well with W1, W2, Z, raw counts and raw CPM. |
| Annotation | Every annotation field in full, gene sets and STRING partners. |
| Downloads | CSV files of the drug-doses, the drug-dose × line table, the wells and the correlations, and the raw data files of the gene. |

Three sub-pages narrow the view: `#/gene/X/line/A549` (every drug-dose in one line), `#/gene/X/drug/<drug>` (the
drug's doses in every line), `#/gene/X/dd/<dd>` (every line and every well at one drug-dose).

### Drug (`#/drug/<name>`)

The top of the page gives the compound, mechanism, targets, its doses with their flags, and links (vault note,
PubChem, DrugBank).

| Tab | What it holds |
|---|---|
| Overview | Every column of `tables/drugs`; the doses side by side (one column per dose: every column of `tables/drugdoses` and `embed/drugdoses`, in groups, with the meaning of each); what each flag of the doses means; the drug's row of `embed/drugs`; its mechanism class (`validation/drug_moa`) and every drug of the same class; the control gene sets that name it. |
| Genes × doses | Every gene at each dose, exact: fold, log2 fold change, z, q rise, q fall, call, flags, line counts, position effect, and the dose patterns. "Strongest rise: max z" and "Strongest fall: min z" sum up the doses; the list starts with the strongest rise. Sort by any column, for example "z at 5 µM". The 3 summed modules are listed below the genes. When the data volume cannot be reached, the list shows the drug's rows of `tables/drug_effects` with a yellow banner that says so and why. |
| Cell lines | A heatmap and a table of DD_A, DD_Az (depleted marked), response beta and r, and the S-phase, G2/M and proteasome effects, for every line at every dose. |
| Modules | Every module's pooled score at each dose. |
| Similar drugs | The cosine of the drug's vector with every other drug, highest first. A drug whose vector may be weak (few significant genes at its vector dose, an artifact flag there, or an untrusted dose) keeps its place with the reason written out. |
| Direction | Every arrow through the drug's targets, and every arrow to how many cells remain under one of its doses. |
| Downloads | CSV files and the drug's raw data files. |

### Drug-dose (`#/dd/<number>`, also `#/dd/<drug>/<dose>`)

This is the drug's raw corrected information at one dose.

| Tab | What it holds |
|---|---|
| QC | A one-line summary, then every column of `tables/drugdoses` and `embed/drugdoses` in groups (the drug-dose; wells and plates; cells, UMI and genes per cell; composition shift; well position; plate factor; cell cycle and proteasome; flags with their meaning; genes it moves; the vector space), each with its definition. Then a volcano plot of every gene (flagged genes ringed in red). |
| All genes | Every gene, exact float32: fold, log2 fold change, z, q rise, q fall, call, flags, clean, cell-cycle share, line counts, whether it is in `tables/drug_effects`, the position effect removed, dose patterns, noise RNA, in the vector space, module (from the search index; an older explorer without it shows a "Load the module of every gene" button) and the predicted z. Click a row for the gene's value in each line. The 3 summed modules are listed apart. "CSV: all genes and the 3 modules (exact float32)" saves every row. |
| Cell lines | Every line: DD_A, DD_Az, depleted, whether the cell counts are trustworthy, response beta and r, S / G2M / proteasome effects, usable wells, its cells in the used wells and in every well. |
| Wells | Every well of the drug-dose (used or left out) with every column of `tables/wells`; its failed wells; each well × line (cells, UMI, relative abundance A2 and zA, response); and one gene's W1, W2, Z, raw counts and raw CPM in each well. |
| Modules | Every module's pooled score, and each module's score in each line (heatmap and table). |
| Per-line values | Every gene in every line at this drug-dose. With the optional data_dd volume: a heatmap of every gene (in the order of the All genes tab) and the long table of every gene × line. Without it: the page says so, a row's drawer shows one gene's values, and the button "Load the per-line values of the genes on this page of the list" loads a page of genes with a progress line. That is a batch you start, not a cap. |
| Direction | Every arrow to how many cells remain at this drug-dose. |
| Vector space | Its fit status, the cosine with every other drug-dose, and its (drug-dose, line) contexts. |
| Downloads | CSV files and the raw data files. |

### Cell line (`#/line/<name>`, also by Cellosaurus or DepMap id)

The top of the page gives the organ, ids, TP53 status, every driver (a gene link and its variant), how many
drug-doses deplete it, and links (vault note, Cellosaurus, DepMap).

| Tab | What it holds |
|---|---|
| Identity | A notice that the line's gene × drug-dose block is reached gene by gene or drug-dose by drug-dose and is never cut; a box to open any gene in this line; every column of `tables/lines`; its drivers. |
| Genetics | Every direction group that holds the line, by kind: genotype groups (a recorded mutation or loss), natural-knockout line sets (lines without a gene; `genes_same_lines` lists every gene absent from exactly the same lines), and the random pseudo-groups. Each row is the full group row, and says whether the line is on the altered side. |
| Sensitivity | Every drug-dose: DD_A, DD_Az, depleted, trustworthy cell counts, response beta and r, S / G2M / proteasome effects, usable wells and the drug-dose's flags, from the most depleted. |
| Genes | Every `line_effects` row of the line: baseline, truly expressed, response spread, drug-doses up and down at the calibrated cut, and the strongest of them with their flags. |
| Baseline | Every gene's level in the line: CPM, expressed (atlas rule), truly expressed, the median line's CPM, the ratio to it, in how many lines the gene is truly expressed, and whether it is a natural knockout here. |
| Modules | Every module at every drug-dose in this line (heatmap and table). |
| Vector space | The line's response and baseline vectors, one row per component, the components where it is among the most sensitive lines, and every other line by cosine. |
| Wells | Every well of the screen with the line's cells, UMI, relative abundance, response and composition shift there. |
| Downloads | CSV files and the raw data files. |

### Other pages

| Page | What it holds |
|---|---|
| Module (`#/module/<n>`) | Tabs: the module and label records; every member (arm, axis projection, degree); its pooled score at every drug-dose; its score in each line (heatmap and table); enrichment and novel members; edges within the module. Module 0 lists the genes of the space that no module took. `#/module/S_PHASE`, `G2M_PHASE` and `PROTEASOME` show the 3 summed atlas modules at every drug-dose. |
| Direction group (`#/group/<id>`) | The group's description, its lines on each side (links), its alerts and notes, every column, and all of its arrows. `#/group/cmp:<n>` is a comparison that only arrows name (drug targets, gene levels). |
| Pair (`#/pair/<A>/<B>`) | How two genes relate in the vector space (their stored partner rows, or the cosine, halves, fdr and evidence computed here); their pooled profiles over every drug-dose (scatter, Pearson and Spearman r over the active, trustworthy drug-doses and over all); every drug-dose with both genes' values; the per-line r in each line (from both genes' per-line files, at least 5 shared drug-doses); the arrows between them. |
| Gene set (`#/set/<source>/<set>`) | Its control-set row, every member with its mean and largest cosine to the other members, and the module enrichment rows that name it. |
| Plate (`#/plate/<plate>`) | The 96 wells as an 8 × 12 grid (drug, dose, cells; DMSO, left-out and failed wells marked), the plate record, every well, the plate factors and the failed wells. |
| What is where (`#/files`) | Every file pattern of the output folder: where it is in the explorer (web or data volume), or why it is not published, the page that shows it, and its files and bytes in this run. |
| About (`#/about`) | How the numbers were made, exactness, every cut and constant of the run, what each flag means, provenance, and the documents. |
| Downloads (`#/downloads`) | The data file format and the Python reader, where each volume is, a finder that gives the file of any gene, drug, drug-dose, line or module, and the raw URL of every pipeline file on the results branch. |
| Documents (`#/doc/<path>`) | The READMEs of the tables, direction and validation, the validation report and these documents, as text. |

## 5. Tables

Every list uses the same table:

- **Sort** by clicking a column title. Empty values always go last, and rows with equal values keep their order.
  Some tables have buttons for common orders (for example "strongest rise first").
- **Pages** of 100, 1,000 or 10,000 rows. The page holds real rows, so the browser's find (Ctrl+F) and printing
  work.
- **Filters** are buttons and boxes above the table; each says how many rows it keeps. While one is on, a yellow
  banner says "Showing k of N; N − k hidden by: ..." with a button to clear it.
- **Columns**: "Simple" shows the main columns, "All" every column, "Choose columns" any set. The line above the
  table says how many columns are hidden.
- **?** next to a column title opens its definition. "What each column means", under the table, lists them all.
  Columns marked "(computed)" are computed in the page.
- **Click a row** (or press Enter on it) to see every field of that row in full, with its definition.
- **Compact text** shortens long text to its start and "… (+3 more reasons)"; the drawer and the downloads keep it
  whole.
- **CSV: rows shown** saves the rows that pass the filters, in the shown order and columns. **CSV: all N rows**
  saves every row and every column.

The address of the page keeps the table's state after `?` (for example `?sort=z:asc&f=sigup&page=2`), so a view can
be shared or bookmarked. The back and forward buttons of the browser work.

## 6. Downloads

CSV files are made in the page and are exact:

- float32 values are written with the fewest digits (1 to 9) that read back to the same float32 value when read as a
  64-bit number and rounded to float32 (as pandas and numpy do);
- float16 values with the fewest digits (1 to 5) that round to the same float16;
- an empty field means no value, and the column `missing_reason` says why;
- files start with a byte-order mark so that spreadsheet programs read them as UTF-8.

File names carry the run id, for example `TRIM72_drugdoses_<run>.csv`, `TRIM72_lines_x_drugdoses_<run>.csv`,
`Idarubicin_hydrochloride_5uM_all_genes_<run>.csv`, `A549_sensitivity_<run>.csv` and `A549_genes_<run>.csv`.

The raw data files can be read in Python with `tsf_reader.py` (in the web folder; numpy only). The Downloads page
finds the file of any gene, drug, drug-dose, line or module.

## 7. When something is missing

- **The data volume cannot be reached** (no `data` folder next to `web`, no network, or the host does not answer):
  the per-line tabs show a box that names the file, where it lives, every place the page looked, and what still
  works. Every tab built from the web volume stays complete. The drug's genes × doses and the drug-dose's all-genes
  lists then show the rows of `tables/drug_effects` (|z| ≥ 3 or q < 0.10) with a yellow banner that says so.
- **The data are from another run**: the page refuses them and says "this data is from run X, the page from run Y:
  the data were re-published; reload".
- **The optional data_dd volume was not made**: the drug-dose Per-line values tab says so and loads the genes gene
  by gene.
- **A script error**: a red banner lists what failed, with a button that copies the diagnostics.

## 8. For developers

The page is plain JavaScript in `tahoemap/explorer_app/` (`index.html`, `app.css`, `js/*.js`). The stage joins the
`js/` files in name order into `app.js`. There are no modules, no build step and no outside libraries.

| File | What it does |
|---|---|
| `00_util.js` | `TM.h` (make an element), `TM.href.*` (links), `TM.fmt.*` (numbers), `TM.ready`, the error banner, `TM.errorBox` |
| `10_tsf.js` | `TM.tsf.decode` / `parse`: the TSF1 decoder (float16 through a lookup table) |
| `20_load.js` | `TM.load.web(id)`, `TM.load.data(id, volume)`: sources in order, one load per file, run-id check, cache; `TM.ids.*` |
| `30_table.js` | `TM.table(opts)`: the one table component; `TM.tableCols`, `TM.subTable`, `TM.record`, `TM.recordOf`, `TM.tabBar`, `TM.tabbed` (pages with tabs), `TM.fileLinks` |
| `40_heat.js` | `TM.heat(opts)`: the canvas heatmap |
| `50_plot.js` | `TM.plot.spark / strip / bars / scatter / plate96` |
| `60_search.js` | `TM.search`: the index, ranking, two-word views, the results page |
| `70_route.js` | `TM.data` (the shared model), `TM.route`, the home page, the footer, `TM.boot` |
| `80_gene.js` | the gene page and its sub-pages; `TM.dirTable` (any list of arrows) |
| `81_drug.js` | `TM.drug`: the drug page; the drug-dose QC groups and the cell-number columns shared with the other pages |
| `82_dd.js` | `TM.dd`: the drug-dose page, with the per-line batch loader |
| `83_line.js` | `TM.line`: the cell-line page |
| `84_misc.js` | module, group, pair, set, plate, browse, files, about, downloads and documents |
| `90_csv.js` | `TM.csv`: exact number text and CSV files |

Every page calls `TM.ready('<kind>/<tab>')` when it has drawn what it draws without user action; the tests wait for
it. After a change to these files, `python -c "from tahoemap import explorer; explorer.refresh_assets('OUT')"`
copies them again without rebuilding the data. `tests/test_explorer_browser.py --out OUT` checks the pages in
headless Chromium (it needs Playwright for Python; without it the test prints a warning and skips).
