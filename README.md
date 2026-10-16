# Tahoe-100M scripts: the all-angles atlas, the gene panel, and the MTAP/Gankyrin trial

Copy this folder's files into your Tahoe-100M download folder (default `~/Tahoe-100M`; on Windows `C:\tahoe\Tahoe-100M`)
and run them from there (on Linux / macOS the `tahoe` command of the Quick start below needs no copying). Replace
older copies too: `tahoe_atlas.py` and `tahoe_gene_panel.py` need the current `tahoe_mtap_gankyrin.py`, and the panel
the current `tahoe_atlas.py` (they stop with a message when they find an older one; the panel's `analyze` warns,
still reads a computed atlas's tables, and leaves the genome-wide look-ups out of its briefs).

**The method is now v3** (see [Method v3](#method-v3-what-changed-and-why)): it fixes weaknesses that the check of the
first full run found in the real data, so the numbers change, MTAP/Gankyrin included. Outputs made before v3 show in
`tahoe status` as `done, but outdated (method v3)`. `tahoe update`, then `tahoe run`, redoes only what v3 needs: the
atlas's effects and angles on its finished build, and the gene panel's analysis on its finished extract (minutes;
the ~96M cells are not read again). Two runs are current:
1. **The atlas** (`tahoe_atlas.py`): one long computation that aggregates the whole dataset and pre-digests it into one
   data package per angle (genes, drugs, classes, cell lines, biomarkers, programs, cell state, ...), followed by one
   Claude agent per angle that does the actual analysis and writes a report.
2. **The gene panel** (`tahoe_gene_panel.py`): the MTAP/Gankyrin method, already run on the real data, applied to the
   ferroptosis, pyroptosis and p53 genes plus NAPEPLD (NAPE-PLD) and TRIM72 (MG53), with cross-links back to MTAP and
   Gankyrin; optionally one agent per pathway.

## Quick start (Linux / macOS)

The `tahoe` command does each step in one short line. Once (`~/repo` = where you cloned this folder):
```bash
git -C ~/repo pull         # gets the tahoe command (skip it on a fresh clone)
~/repo/tahoe setup         # the Python environment ~/tahoe-venv, and the plain 'tahoe' command
```
Setup ends with one line to type in that window (or open a new SSH window). Then:
```bash
tahoe download     # the dataset into ~/Tahoe-100M (about 430 GB, resumes; skip it if the data are there)
tahoe test         # optional: 3-minute test on synthetic data
tahoe run          # the atlas, then the gene panel, in the background (safe to log out)
tahoe              # where everything stands, and the exact command to type next (= tahoe status)
tahoe bundle       # both bundles in one zip, and the one scp line to download it: upload it to Claude
tahoe agents       # after Claude has checked the numbers (asks for the API key each time; it is never saved)
```
Already ran everything with an earlier version? Then:
```bash
tahoe update       # the newest scripts (git pull); it ends with the command to type next
tahoe run          # method v3: the atlas effects + angles, then the gene panel's analysis (the build and the
                   # extract are reused: minutes, not hours), then tahoe bundle and tahoe agents as above
```
- `tahoe run` starts only what is missing or outdated. When the atlas build is complete (`atlas/build_info.json`
  for the same files as the download), it runs the atlas `effects` and `angles` only, else `compute`; then the
  gene panel's `analyze` when its extract is complete, else `all`. The briefs are written again from the repo
  on the way.
- `tahoe log` follows the running job's log (Ctrl-C stops watching, not the run); `tahoe stop` stops a run (finished
  work is reused); `tahoe update` gets the newest scripts (git pull); `tahoe help` lists everything.
- Options go to the script: `tahoe atlas --workers 4`, `tahoe panel analyze`, `tahoe atlas lookup gene MTAP`.
- Nothing is copied: the scripts run from the repo folder with `--data ~/Tahoe-100M` (another folder:
  `export TAHOE_DATA=/path`), and the outputs land where the commands below put them.
- Copies you made in `~/Tahoe-100M` are not run by `tahoe`, but agent briefs written by a run started from them
  name them in their look-up commands. Keep them until the briefs have been written again from the repo (`tahoe run`
  does that). `tahoe status` says when they may go (then
  `cd ~/Tahoe-100M && rm tahoe_atlas.py tahoe_gene_panel.py tahoe_mtap_gankyrin.py`). `tahoe agents` refuses to
  start while a brief names a script that no longer exists, and says what to type.
- Runs started by hand show up in `tahoe status` too, and `tahoe panel` waits for an atlas that is running.

The long commands below still work. Windows: use the PowerShell commands below.

**Order of work.** (`tahoe run` does steps 1 and 2 in this order.)
0. Copy all files over the old ones (see above; with the `tahoe` command: `tahoe update`).
1. Atlas: `check`, then `compute` (~1-1.5 h). Outputs of an older method (`tahoe status`: outdated): `effects`, then
   `angles` (minutes; the build is reused; `effects` removes the old `atlas_bundle.zip`, `angles` writes a new one).
   Run the atlas and the gene panel with the same `--unreliable-plates` (the panel warns and fits its own plate
   factors when they differ), and never point the panel at a `--limit-files` trial atlas (nothing is imported).
2. Gene panel: `check`, then `all` (~1 h); outputs of an older method: `analyze` (minutes; the extract is reused).
   Run it after the atlas: it takes the atlas's composition shift, plate factors and 'wells disagree' (so that
   MTAP and PSMD10 agree between the two), and its agent briefs get the genome-wide atlas look-ups. Never run the two
   long passes at the same time: each reads all ~96M cells.
3. Upload `atlas/atlas_bundle.zip` and `gene_panel/gene_panel_bundle.zip` to Claude to check the numbers (each now
   holds its agent briefs as `briefs/<angle>.md`, so the text the agents get is checked too).
4. Then the agents of each (`tahoe_atlas.py agents`, `tahoe_gene_panel.py agents`). Each remakes its bundle with the
   reports: upload both again. Do not rerun `compute`/`effects`/`angles` or the panel's `all`/`analyze` after the
   agents: that makes every report out of date, and the next `agents` run redoes (and pays for) all of them. To
   remake a bundle, use `bundle`.

Requirements: Python 3.10+ with numpy, pandas, pyarrow (every script); duckdb for `02_find_mtap_gankyrin.py`,
`old_drug_effect_uncorrected.py` and `tahoe_mtap_gankyrin.py coreg`; scipy and psutil are optional (used when present).
For the agents also `claude-agent-sdk` and an Anthropic API key.

| File | What it does | Time |
|---|---|---|
| `00_download_tahoe.sh` | Installs the tools, fixes the Brotli crash, downloads the dataset (resumable; Linux/macOS, Windows below). Skip if your download is intact. | hours |
| `01_preview_parquet.py` | Writes `tahoe_preview.txt` / `.csv`: schema and 100 cells with gene names, for a first look. | seconds |
| `02_find_mtap_gankyrin.py` | Searches every metadata table for MTAP / PSMD10 / Gankyrin and pulls both genes' raw (uncorrected) DE tests into `mtap_search/`. | minutes |
| `tahoe_mtap_gankyrin.py` | The MTAP / Gankyrin trial with all artifact corrections (`mtap_gankyrin/results/`). Also the library the atlas and the panel import: keep the current copy next to them. | ~1 hour |
| `tahoe_atlas.py` | **Every angle of the whole dataset** (all genes, drugs, doses, cell lines), one data package per angle, and a Claude agent per angle that writes a report. | see below |
| `tahoe_gene_panel.py` | **The gene panel**: ferroptosis, pyroptosis, p53, NAPEPLD, TRIM72, on the MTAP/Gankyrin method. | ~1 h + minutes |
| `old_drug_effect_uncorrected.py` | Superseded. Reproduces the original uncorrected drug lists, for comparison only. | minutes |
| `tahoe` | The one-line commands of the Quick start (Linux / macOS): status, run, log, bundle, agents, stop, setup, ... (`tahoe help`). | seconds |
| `tahoe_status.py` | What `tahoe status` prints: reads the logs, the job files in `<data>/.tahoe`, the process list and the method version each output records; decides what `tahoe run` redoes. | seconds |
| `tests/` | Synthetic Tahoe-100M data with planted effects and a smoke test of every script (see `tests/README.md`). | ~3 min |

## Method v3 (what changed and why)

The first full run on the real data (95.6M cells, 1,344 wells, 50 lines) was checked line by line before any agent
ran. The bookkeeping and the arithmetic were exact, and the effects agree with Tahoe's own DESeq2 table (median
per-gene Spearman 0.63 / Pearson 0.83 on the plates compared, 0.84 / 0.90 with our position correction added back;
93% of effects >= 1.2x have the same sign). But the data have technical structure the method did not remove, and it
would have misled the agents. Version 3 of the method fixes it in all three scripts (one definition each, used
identically by the atlas and the gene panel / MTAP trial).

**Plates 2 and 3 were too noisy.** They hold the 0.5 and 5 uM doses of the plate 1-3 layout (about 16% of the
drug-doses). Their z-scores were about 1.4x and 2x too wide (18% and 36% of drug wells beyond |z| 1.96, against
5-12% on the other plates), because whole plate rows lost cells or sequencing depth. As a result they gave 49% of the
panel's calls and 43% of the atlas's significant gene calls. *Fix:* a plate factor per plate and dose: the group's
spread over that of the same dose on the other reliable plates, median over genes. Every expression z on that plate
(genes, modules, pathway scores, the p53 contrast) is divided by it; the growth (relative abundance) z are not.
A gene that is noisier on a plate than that plate's median gene (its own spread ratio > 1.3x the factor; in the
first run's numbers PSMD10 and several panel genes were 2-3x their peers on plate 2, the median panel gene ~1.45x)
gets its own, larger factor (ratio / 1.3); it never gets a smaller one. Whether the growth z need a factor too,
the quality angle's `calibration_growth_by_plate.csv` shows. The factor only ever widens (never below 1), so a
quiet plate is never sharpened; part of plate 3's spread may be real activity of its targeted-oncology drugs. The
fold changes are unchanged. Flag: `noisy plate (z scaled)` (factor > 1.2). The factors are in
`effects/plate_scale.csv` and the panel's `results/plate_scale.csv`.

**Plate 13 does not reproduce.** It is a mixed-dose rescue plate (all three doses, plus re-runs of plate 1's failed
wells; DMSO at B11/B12, not H11/H12). Its replicate pairs agree at median r -0.06, against +0.30 for pairs on two
other plates (strong drug-doses: +0.58, none negative). Topotecan 5 uM on plate 9 vs plate 13: r -0.19. Ribociclib,
which sits only there, shows no G1 arrest (S-phase z +0.31 at 5 uM; palbociclib 0.5 uM: -8.9). *Fix:* plate 13 is an
unreliable plate by default (`--unreliable-plates plate13`, or `none`, or another list, on every script). Its wells
are still computed and listed, but they stay out of the reference spread and the plate-factor peers. A drug-dose
that also has a well on a reliable plate uses only those wells; one that sits only on plate 13 keeps it and is
flagged `unreliable plate only`.

**Strong neighbours leaked into the position correction.** The plates share four layouts, so 361 of 367 drugs sit
at the same well position at every dose. A drug's position correction is the median of the other drugs' wells at
that position (about 11 wells of about 4 drugs). When one of those drugs is strong, its effect is subtracted as if
it were positional. Example: sodium salicylate appeared to lower TFRC to 0.64x at all three doses, a mirror image
of dinaciclib, which shares its well position. The same layout also means that dose consistency does not rule out a
position artifact; agreement at a different position is the stronger test. *Fix:* a second pass uses only the clean
donors for each gene (wells whose first-pass |z| < 3). With fewer than 3 clean donors that gene is not corrected in
that well and is flagged `position correction uncertain`.

**Some wells could not be corrected at all.** 15 drug wells had fewer than 3 other-drug wells at their position:
Adagrasib 0.05 uM sits at H10 on 13 plates (221 significant genes at 50 nM, none at 0.5 uM; CASP3 0.85x with
z -12.9), and on plate 13 carbidopa and ribociclib 0.05 uM sit at H11/H12. *Fix:* flag `position not correctable`.

**Library composition.** Effects are CPM ratios: when a few genes take a large share of a well's reads, all others
read lower. TAK-901 5 uM read about 0.5 log2 lower than Tahoe's DESeq2 table for nearly all genes (Ouabain 5 uM
about 0.25). *Fix:* a median-of-ratios shift per well and cell line (the median residual of the genes the line
expresses at >= 10 CPM, as in DESeq2), subtracted from every gene, is saved as `effects/composition_shift.parquet`.
The gene panel and the MTAP trial take it from the computed atlas (`<data>/atlas`; `--atlas DIR` for another one,
`--atlas none` for none), so run the atlas first; without it they say `composition normalisation not applied`. Flag
`composition shift` when a drug-dose's shift is >= 0.2 log2: its effects are relative to the median gene, and a raw
CPM view would differ.

**The 'toxic' flag was mostly noise.** It meant "the well kept less than half the plate's cells". Replicate wells of
one drug-dose did not agree on it (Spearman -0.19; of 14 pairs with one well below that line, none had the other
below). Whole plate rows lost cells (plate 2 row D: all 12 wells, 17 of the 49 'toxic' drug-doses were on plate 2).
*Fix:* `toxic` now means cell loss that no higher dose of the same drug recovers from, judged against the plate row
where that row is itself shifted (> 0.8 log2; a row of toxic 5 uM neighbours is no reason to subtract their loss,
which had relabelled e.g. bortezomib and topotecan 5 uM), and, when the drug-dose has several used wells, seen in
its best well too (selinexor 5 uM: one well -2.5, the other +0.3: not toxic). At the top dose there is no higher
dose to check and most drug-doses have one well, so `toxic` there still rests on one well's cell count; duplicate
wells (plates 6 and 14) agree poorly on cell loss, so treat it as weak evidence alone. Other cell loss is flagged
`low cells (technical?)` (not confirmed, not necessarily technical: antimitotics kill more at a lower dose), and a
shifted plate row `plate-row cell shift`.
`transcription drop` is judged against the plate row too, and `cell-cycle shift` looks at both S and G2/M. The p53
reference doses and the re-expression gating use the new `toxic`.

**Statistics that were too optimistic.**
- Atlas `level_vs_growth` and `proliferation_dependent_drugs` drew 'hits' from inert drug-doses (170 PSMD10
  level-vs-growth hits at q < 0.1, mostly single wells). They now use an empirical null: the robust centre and
  spread of the statistic over the reliable drug-doses.
- Biomarkers: an inert drug-dose could reach more than 3,000 'marker' genes (Aliskiren 0.5 uM: 18 significant genes,
  3,397 markers). Each gene's correlation is now calibrated against its own spread over drug-doses (markers need
  calibrated |z| >= 3). A `replicated` column (the growth pattern agrees between doses or wells, r >= 0.3) ranks
  `selective_drugs` first.
- `feature_response`: a Welch t on 3-line groups gave q ~1e-16 for tiny differences. The group variance is now
  floored at the rest's, and `small_group` marks groups of <= 4 lines.
- Replicates are reported by pair type (`same position, other plate`, `different position`, `same plate`,
  `unreliable plate`), with a same-position null, each drug-dose counted once (Adagrasib 0.05 uM's 16 wells gave
  78 of the 170 same-position pairs); pairs with a well that had no position correction are reported apart. The
  single median r 0.18 had pooled these. Few drug-doses have a replicate at a different position on reliable
  plates (on the real layout 9 drug-doses of Afatinib, Binimetinib and Trametinib), and the briefs name them.
- `lowest_active_dose` needs every higher dose to be active too; otherwise it reads `low dose only (noise?)`
  (18 drugs were 'active' only at 0.05 uM).
- The genes angle's inducible / repressible lists hold at most 25 genes per drug-dose and no noise RNAs. Before,
  Idarubicin 5 uM and TAK-901 5 uM filled 378 and 375 of the 500 rows.
- Gene panel: the p53 WT-vs-altered table has a `pattern` column. `WT induction` needs the WT lines to rise >= 1.2x
  and the all-line P53 score to go up; otherwise it is `relative (altered lines fall)` (read it from the run's
  `p53_wt_vs_altered.csv`: the composition normalisation moves exactly the drug-doses whose altered lines seemed to
  fall). Re-expression is compared with the lines deleted for the gene in the same wells (pure ambient RNA; the
  expressing lines when fewer than 2 are deleted): it needs >= 2 lines up and a dose pattern, and reads
  `lost lines read ambient only: not interpretable` when the lost lines' untreated level is at the ambient floor
  (whether or not any line is deleted for the gene). Pathway scores average the members' z, each on its own noise
  scale, so 6-line CASP5 no longer drives INFLAMMASOME. The crosslinks' shared-drug count is compared with an
  expectation stratified by drug activity: 38 shared drugs had looked like ~3x the ~12 'expected', but strong drugs
  are in every list, and the stratified expectation is about 34.
- The `plate DMSO offset` flag is gone (it was on 28% of best-dose rows and never changed a value). The
  `plate_dmso_offset` column stays.

**Briefs.** The briefs now state the facts above from the data. They list the plates with a factor > 1.2 and the
unreliable plates with their replicate r. They say where DMSO sits, which drug-doses have no data (their only well
failed), which lines have usable expression in < 25% of wells, that ~20 drugs appear twice as salt forms, that
cytostatic drugs deplete lines only weakly at 24 h, and how wide the gap behind the MTAP-null cut is. The focus
briefs no longer assert earlier findings: they say the earlier MTAP / Gankyrin analysis was inconclusive and ask
the agent to test every candidate rise against its dose pattern, flags, cell cycle and the whole proteasome. Both
bundles include the briefs.

**What changes in the numbers.** Every z, FDR, call and flag can move compared with earlier runs. Expect plates 2 and
3 to lose many calls, drug-doses with a plate-13 well to rest on their other wells, position-corrected values to
change where a strong drug shares the position, composition-shift drug-doses to move by up to ~0.5 log2 for all
genes, and `toxic` to become rarer. Unchanged: the build and extract (the cells are not read again), failed wells,
`--min-cells`, the expression rules, the MTAP-null call and the TP53 annotation. **MTAP / Gankyrin:** the
conclusion is expected to stay that there is no clean inducer. MTAP had no convincing inducer (its one call,
clobetasol 0.05 uM 1.30x, is inconsistent across doses). PSMD10 mRNA does rise 1.3-2.2x with about 15 drug-doses
(dinaciclib 5 uM, NG25 5 uM, XRK3F2 0.5 uM, ...), and Tahoe's own table ranks the same drug-doses on top, but nearly
all of them come with toxicity, a transcription drop or the whole proteasome. Read the v3 tables before restating it.

**Flags** (the `flags` column of every drug-dose table; the strings are exact, one definition in both scripts):

| Flag | Means | What to do |
|---|---|---|
| `toxic` | < -1 log2 cells vs the plate (and after subtracting the plate row's median where the row itself moved > 0.8 log2), the best used well < -0.5 too, and no higher dose of the drug recovering to >= -1 | Cytotoxicity: effects partly reflect dying or stressed cells. At the top dose it rests on one well's cell count (duplicate wells agree poorly): weak evidence alone |
| `low cells (technical?)` | < half the plate's cells, but not confirmed as dose-consistent loss beyond its row | Not confirmed: a row that lost cells, a non-monotonic dose response (antimitotics), toxic neighbours, or a well that did not replicate. Do not call the drug toxic from it alone; a drug-dose with many significant genes is still active: read its effects with the cell-loss caveat |
| `plate-row cell shift` | The other drug wells of its plate row are shifted together (cells by > 0.8 log2 either way, or UMI per cell < -0.4 log2) | Technical: confirm on another plate |
| `transcription drop` | Genes or UMIs per cell fall vs the plate and its row (< -0.3 / < -0.5 log2) | Global shutdown: many genes fall together |
| `cell-cycle shift` | S or G2/M module moved > 0.5 log2 (or > 0.25 with \|z\| >= 4) | Cycle genes follow the cell-cycle mix |
| `composition shift` | The drug-dose's composition shift is >= 0.2 log2 | Effects are relative to the median gene |
| `noisy plate (z scaled)` | Plate factor > 1.2 (the group's, or the gene's own where it is noisier there): its z were divided by it | Fold changes are unchanged; prefer agreement on another plate |
| `unreliable plate only` | Only wells on an unreliable plate (default plate 13) | Unconfirmed |
| `position correction uncertain` | (per gene) < 3 clean other-drug wells at the position: not corrected | Could be positional |
| `position not correctable` | < 3 other-drug wells at the position at all | No position correction: unconfirmed |
| `position effect removed` | (per gene) the correction moved it by > 0.2 log2 | Check that the corrected value still holds |
| `wells disagree` | >= 2 wells whose z over the top 500 genes correlate at r < 0.1, with >= 100 significant genes | Not replicated |
| `whole proteasome up/down` | (gene panel, PSMD10) the whole proteasome moves with it | Not Gankyrin-specific |

**New columns and files.**
- Atlas `effects/`: `composition_shift.parquet` (sample, cell_line_id, shift_log2), `plate_scale.csv` (plate, dose,
  n_wells, factor_raw, factor, group), `posunc.npy` / `DD_posunc.npy` (position correction uncertain per well /
  drug-dose x gene), `DD_poseff.npy` (position effect removed), `plate_scale_gene.npy` (each gene's z divisor per
  plate group). `wells.csv` adds `composition_shift_log2`, `unreliable_plate`, `plate_scale` / `plate_scale_group_id`,
  the plate-row medians (`row_cells_log2`, `row_umi_per_cell_log2`, `row_genes_per_cell_log2`),
  `cells_log2_beyond_row`, `position_clean_donors_median` and `position_not_correctable`. `drugdose.csv` adds
  `composition_shift_log2`, `plate_scale`, `unreliable_plate_only`, `position_not_correctable`, `replicate_r`,
  `n_wells_all` / `wells_left_out`, `cells_log2_best_well` and `cells_log2_best_higher_dose`. `complete.json` says
  version 3; `angles/complete.json` is written when `angles` finishes (`tahoe status` needs it).
- Atlas angles: `quality/calibration_by_plate.csv` (% of the measured |z| > 1.96 and > 3 per plate and dose, before
  and after the factors), `quality/calibration_by_plate_gene.csv` (the focus genes and the genes widened most beyond
  their plate's factor), `quality/replicate_by_plate_pair.csv`, `quality/replicates.csv` with `pair_type`,
  `quality/composition_shifts.csv`, `quality/position_not_correctable_wells.csv`; `small_group` in
  `line_response/feature_response_top.csv`; `replicated` in the biomarker tables; `plate_scale_gene` in the focus
  tables.
- Gene panel `results/`: `run_info.json` (method_version 3 and the run's settings; written last, read by
  `tahoe status`), `plate_scale.csv`, `plate_scale_by_gene.csv`, `replicate_pairs.csv`, `well_effects.csv.gz` (per
  well: unreliable plate, plate factor, composition shift, and every gene's and score's log2FC and z, the value
  before the position correction and its position state), `pattern` in `p53_wt_vs_altered.csv`. The MTAP trial
  writes `run_info.json`, `plate_scale.csv` and `plate_scale_by_gene.csv` too.
- Every drug-dose table: `plate_scale_gene` (the gene's own z divisor) and `cells_log2_best_well` (the input of
  `toxic`). A gene measured in fewer than 5 lines in a typical well (real CASP5: 4 colorectal lines in nearly every
  well) is computed from the lines it has; other genes need >= 5 measured lines per well, as in the atlas.
- `README_effects.md` (atlas) and `results/README_columns.txt` (panel) describe every column.

## Setup

The download is about 430 GB (4,427 files), plus ~25 GB for the outputs (atlas ~20 GB, gene panel ~3 GB): check the
free space first.

**Linux / macOS:** `bash 00_download_tahoe.sh` (or `bash 00_download_tahoe.sh /data/Tahoe-100M`) installs the packages
and downloads into `~/Tahoe-100M`.

**Windows (PowerShell):** check the free space with `Get-PSDrive C` first. Use the Python of your environment directly
(here `C:\tahoe\.venv`):
```powershell
C:\tahoe\.venv\Scripts\python.exe -m pip install -U huggingface_hub hf_xet "brotli>=1.2.0" numpy pandas pyarrow duckdb scipy psutil
C:\tahoe\.venv\Scripts\hf.exe download tahoebio/Tahoe-100M --repo-type dataset --local-dir C:\tahoe\Tahoe-100M
```
Rerunning the download resumes it. On a `process() takes no keyword arguments` error run
`C:\tahoe\.venv\Scripts\python.exe -m pip uninstall -y brotli brotlicffi` and download again. Optional, for higher rate
limits: `$env:HF_TOKEN="hf_xxx"` first. In the commands below, Windows users type `C:\tahoe\.venv\Scripts\python.exe`
where Linux shows `python3` (if the path has spaces, PowerShell needs `& "C:\path with spaces\python.exe" ...`).

Each script indexes the download once (reads only the file footers; `file_index.json` in its output folder) and
indexes it again by itself when parquet files appear or vanish later, e.g. when the download finished after an
earlier run; `--reindex` forces it. Folders that hold a `file_index.json` (the scripts' outputs) are never read as data.

**Logs and long runs.** Every long command writes its own log into its output folder (`atlas/atlas.log`,
`atlas/agents.log`, `gene_panel/gene_panel.log`, `gene_panel/agents.log`, `mtap_gankyrin/mtap_gankyrin.log`), including
worker lines and a crash traceback, and keeps the computer from sleeping while it runs (Windows: power request; macOS:
caffeinate; Linux: systemd-inhibit where available). A laptop still sleeps when its lid is closed: keep it plugged in,
lid open.
- Linux/macOS, to survive logout: `nohup python3 tahoe_atlas.py compute > /dev/null 2>&1 &`, then
  `tail -f atlas/atlas.log` (Ctrl-C stops watching, not the run).
- Windows: run the command in a PowerShell window and leave it open (no nohup needed); follow the log from a second
  window with `Get-Content atlas\atlas.log -Wait`. Clicking inside the window can pause the run (QuickEdit
  "Select" in the title bar): press Esc to resume.
The scripts print the exact commands for your computer (`check`, and the end of every run).

## 1. The atlas: every angle, with an agent at each endpoint

Free disk: ~20 GB for `atlas/pseudobulk`. Memory: ~2.5 GB per build worker (the script sizes itself to what is free),
~5 GB for `effects`.

### Compute (no agents, no API key needed)
```bash
cd ~/Tahoe-100M                                            # tahoe_atlas.py and tahoe_mtap_gankyrin.py both here
python3 tahoe_atlas.py check                               # preflight: FAIL lines must be fixed; agent lines may say warn
nohup python3 tahoe_atlas.py compute > /dev/null 2>&1 &    # build + effects + angles, about 1-1.5 h
tail -f atlas/atlas.log
```
```powershell
cd C:\tahoe\Tahoe-100M
C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py check
C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py compute   # leave the window open; log in atlas\atlas.log
```
If the data sit on a hard drive rather than an SSD, `check` says so and suggests `--workers 2`, which reads more
smoothly (some cloud VMs report SSDs as hard drives, so it is only a suggestion; the build never changes the worker
count by itself). `compute` ends by writing `atlas/atlas_bundle.zip` (a few MB: the key tables of every angle plus the
log). Download it and upload it to Claude, which checks the numbers (well positions, artifact corrections, known
biology) before any money is spent on agents. If the run stops part-way, run the same command again: finished plates
are reused. `effects` swaps each matrix in only once it is fully written and stamps `atlas/effects/complete.json`
last; `angles`, `agents` and `lookup` refuse effects without that stamp (an interrupted run: run `compute` again)
or with an older method's version in it (run `effects`, then `angles`: minutes, the build is reused; `tahoe run`
does that). Options of the method: `--unreliable-plates LIST|none` (default `plate13` when present) on `effects`,
`compute` and `all`. On Windows, close agents and look-ups that read `atlas/effects` before rerunning `compute`.

### Agents (after the check)
```bash
python3 -m pip install claude-agent-sdk   # bundles the Claude Code engine the agents run on (Python 3.10+)
export ANTHROPIC_API_KEY=sk-ant-...     # from console.anthropic.com; add to ~/.bashrc to keep it
python3 tahoe_atlas.py check            # now also makes one tiny live agent call (about one cent)
nohup python3 tahoe_atlas.py agents > /dev/null 2>&1 &     # log: atlas/agents.log
```
```powershell
C:\tahoe\.venv\Scripts\python.exe -m pip install claude-agent-sdk
$env:ANTHROPIC_API_KEY="sk-ant-..."     # in the same window
C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py check
C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py agents   # log: atlas\agents.log
```
When the agents finish, `atlas/atlas_bundle.zip` is remade with every report added (`python3 tahoe_atlas.py bundle`
remakes it any time): upload it to Claude to turn each report into a doc. `all` runs both stages in one go. The
briefs name the Python and the `tahoe_atlas.py` that ran `angles` (their look-up commands run them), so run `angles`
(minutes) on the computer that runs the agents, and keep that `tahoe_atlas.py` where it is until the agents are done.
`agents` refuses briefs that name a script that no longer exists: run `angles` again first.

| Step | What it does | Time (estimate) |
|---|---|---|
| `build` | One pass over all ~96M cells: counts per well x cell line x gene (one worker per plate). | 20-60 min |
| `effects` | Corrected effect of every drug-dose on every gene (16,643 genes tested in the real data), on growth of every line, and how strongly each line shows each drug's response (method v3: composition shift, plate factors, unreliable plates, two-pass position correction). | ~5 min (the first real run took 4.2 min on 30 CPUs; v3 adds ~5%); up to ~15 min on a slow machine |
| `angles` | One folder per angle with tables, a `brief.md` for its agent, and cards for every drug and line. | ~5 min |
| `agents` | One Claude agent per angle reads its folder, runs its own Python checks, writes `report.md`; then an overview agent reads all reports. | 30-90 min |

Corrections shared with the gene panel and the MTAP/Gankyrin trial (method v3, see above): plate baseline = median
of the plate's drug wells (never DMSO); composition (median-of-ratios) shift per well and line; leave-drug-out
well-position correction in two passes (the second with clean donors only); robust z against the spread of the drug
wells on reliable plates, widened per plate and dose by the plate factor; Stouffer over a drug-dose's wells (its
reliable ones when it has any); BH FDR within each gene; failed wells removed; non-expressing lines left out per
gene; growth z with counting noise; the flags of the table above on every drug-dose.

### Angles (one report each, in `atlas/reports/`)
| Report | Question |
|---|---|
| `01_quality` | Where are the traps: well positions (and wells that cannot be corrected), plate factors and z calibration per plate and dose, unreliable plates, composition shifts, plate DMSO offsets, failed wells, replicate agreement by pair type |
| `02_drugs` | What each drug does: signature size, potency, specificity vs toxicity/shutdown, look-alike drugs |
| `03_genes` | Which drugs move each gene: clean, dose-consistent inducers and repressors genome-wide |
| `04_classes` | Do drugs with the same mechanism or target share a signature; outliers; target mRNA feedback |
| `05_cell_lines` | Selective depletion by mutation, protein change, lineage, and genome-wide gene loss (the MTAP-null screen for every lost gene) |
| `06_biomarkers` | Which genes' baseline expression predicts who a drug kills, for every gene x drug (the Gankyrin level-vs-response test for every gene), raw and within lineage |
| `07_line_response` | Which lines respond transcriptionally to each drug, and what predicts it |
| `08_programs` | Data-driven gene programs, the drugs that drive them, and line dependence |
| `09_cell_state` | Cell-cycle shifts, toxicity, proliferation-dependent killing, cycle-driven genes |
| `50_focus_MTAP`, `50_focus_PSMD10` | Everything on each focus gene (`--focus-genes MTAP,PSMD10,MAT2A` to add more) |
| `00_overview` | Top findings across all angles and the 10 best leads |

Quick look-ups any time: `python3 tahoe_atlas.py lookup gene PSMD10` (also `drug Bortezomib`, `line MIA`,
`corr MTAP`). Every drug and line also has a ready card in `atlas/angles/drugs/cards/` and `.../cell_lines/cards/`.

### Agent options and cost
`--model sonnet` (default) or `opus` (deeper, ~2x cost); `--budget 5` = USD cap per agent (12 agents -> at most about
$60; typical use is well below). The cap is the agent SDK's own cost estimate, which can overshoot slightly; an agent
that ends without writing its report gets one nudge, paid from what is left of its own cap (skipped when less than
$0.25 or 10% is left). `--parallel 3`; `--angles drugs,genes,focus` to run a subset; `--redo` to rerun reports that
are already up to date (otherwise finished reports are skipped, so a rerun only redoes failed ones; but rerunning
`angles`/`compute`, or the panel's `analyze`/`all`, rewrites the briefs and makes every report out of date, so remake
a bundle with `bundle`, not `all`); `--dry-run` writes the prompts without calling anything. Each agent's work log is
`atlas/angles/<angle>/agent.log`; costs and status are in `atlas/reports/agents_summary.csv`.

What agents may do: read anything in the atlas folder, run the look-up commands their brief names, write in their
own angle folder, run shell commands and Python (they are told the exact interpreter, e.g.
`C:\tahoe\.venv\Scripts\python.exe`; on Windows also to write paths in Python as raw strings or with forward slashes).
Refused outright: delete, kill, sudo, git, package installs (pip, `python -m pip`, conda, apt), network tools (curl,
wget, ssh) and similar.
On Windows the agents use the PowerShell tool (plus Bash if Git for Windows is installed) with the same refusals
(Remove-Item/del/rd, Stop-Process/taskkill, Invoke-WebRequest/curl, git, pip, winget, Start-Process, ...). Refusal
rules match command text: they are guard rails, not a security boundary. No web access unless you add `--web`
(literature checks). `--sandbox` additionally runs their shell sandboxed: Linux needs
`sudo apt-get install -y bubblewrap socat`, macOS has it built in, Windows does not support it (`check` warns and
`agents` stops with a message).

## 2. The gene panel: ferroptosis, pyroptosis, p53, NAPEPLD, TRIM72

`tahoe_gene_panel.py` applies the MTAP/Gankyrin method to your gene list:
- **Ferroptosis (13):** PTGS2, CHAC1, SLC7A11, GPX4, ACSL4, LPCAT3, AIFM2 (FSP1), NFE2L2, HMOX1, TFRC, FTH1, FTL, NCOA4.
- **Pyroptosis (11):** GSDMD, GSDME, NLRP3, AIM2, PYCARD (ASC), CASP1, CASP4, CASP5, CASP3, IL1B, IL18.
- **p53 (11):** TP53, CDKN1A (p21), MDM2, BBC3 (PUMA), PMAIP1 (NOXA), BAX, GADD45A, SESN1, SESN2, FDXR, ZMAT3.
- **Additional:** NAPEPLD (NAPE-PLD) and TRIM72 (MG53).

It extracts MTAP, PSMD10 (Gankyrin), CDKN2A and CDKN2B again for the cross-links, and 73 context genes (more p53
targets, NRF2, ATF4/ISR, UPR, heat shock, interferon, NF-kB) that tell a specific response from a general stress
program. Keep the current `tahoe_mtap_gankyrin.py` and `tahoe_atlas.py` next to it (copy them over older versions:
it stops when `tahoe_mtap_gankyrin.py` is older than method v3). It takes the composition shift, the plate factors
and 'wells disagree' from the computed atlas (`<data>/atlas`, `--atlas DIR|none`) once its effects are method v3, so
MTAP and PSMD10 agree between the two; without it, it fits its own plate factors and says so. An earlier
`mtap_gankyrin/` output made before v3 is still compared, but differs by design (summary.txt says why);
`tahoe mtap` redoes its analysis with v3 in minutes.

```bash
python3 tahoe_gene_panel.py check                                   # preflight: data, genes, TP53 annotation, earlier run, disk
python3 tahoe_gene_panel.py all --limit-files 30 --out panel_trial  # optional trial (minutes) in its own folder
nohup python3 tahoe_gene_panel.py all > /dev/null 2>&1 &            # the full run: extract + analyze + bundle (~1 h)
tail -f gene_panel/gene_panel.log
```
```powershell
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py check
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py all       # leave the window open; log in gene_panel\gene_panel.log
```
The trial gets its own folder so that its results, briefs and bundle never mix with the full run's; it reads only the
first files, so its cross-links to the earlier run differ by design (look at `panel_trial/results/summary.txt`, then
delete the folder). The agent briefs are written by `analyze`: they name the Python and the scripts that ran it,
and they offer genome-wide look-ups (`tahoe_atlas.py lookup`) only if the atlas is already computed in
`<data>/atlas`. If the atlas comes later, or is computed again, rerun `python3 tahoe_gene_panel.py analyze`
(minutes) before the panel's agents: then the panel also takes the atlas's composition shift and plate factors
(`tahoe status` says when; `tahoe run` does it).

| Step | What it does | Time (estimate) |
|---|---|---|
| `extract` | One pass over all cells: per-cell counts of the panel, anchor and context genes plus the S/G2M/proteasome modules (`gene_panel/cells/`, ~2.5 GB; resumable). | ~1 h, like the MTAP/Gankyrin extract (longer from a hard drive); up to ~3 GB memory per worker + ~1 GB for the main process |
| `analyze` | Corrected drug effects per gene, pathway scores, the p53 screens, loss and level screens, cell cycle, co-regulation, cross-links, positive controls, `summary.txt`, the agent briefs, and the bundle. | a few minutes (~2-4 GB memory) |
| `agents` | One Claude agent per pathway (ferroptosis, pyroptosis, p53, napepld_trim72, crosslinks) plus an overview. | ~20-45 min |

What `analyze` does (all with the corrections above; `gene_panel/results/README_columns.txt` explains every file; a
rerun of `analyze` moves the earlier results to `gene_panel/results/previous_run/`):
- **Expression.** Which lines express each gene. A line counts as expressing a gene (and enters its drug effects)
  when it reads >= 25% of the median line, >= 1 CPM and >= 2x the level ambient RNA alone gives (ambient = the share
  of the pooled MTAP level that the MTAP-null lines read, times the gene's pooled level), so lines that only carry
  ambient RNA of a gene few lines express are left out. Genes with fewer than 2 counts per well x line profile are
  flagged `low counts` and get no calls; scores built only from such genes are flagged `low counts`. In a real
  Tahoe file, PYCARD (ASC), CASP1 and CASP5 are near zero in almost every line and GSDMD is low (median ~5 CPM).
  NLRP3, AIM2 and IL1B are expressed in a handful of lines (AIM2 e.g. in C32 and NCI-H2122; IL1B in RPMI-7951, HOP62
  and NCI-H1792), and TRIM72 is low (a few lines at ~10-20 CPM). Expect much of the inflammasome to be untestable or
  line-specific.
- **Drug effects.** Effects on every gene (`<GENE>_drug_summary.csv`, one row per drug; `..._by_dose.csv`). Every
  drug-dose carries its stress context: ISR, NRF2, UPR, heat-shock, interferon, NF-kB, p53 and cell-cycle scores,
  plus the flags of the [Method v3](#method-v3-what-changed-and-why) table and its `plate_scale` and
  `composition_shift_log2`. This shows, for example, whether CHAC1/SLC7A11/PTGS2 rise with or without a general ATF4
  stress response. Calls use the dose-level FDR. Pathway scores are the mean member z (each member on its own noise
  scale); their fold change is the mean member log2FC.
- **p53.** TP53 status comes from the cell-line driver table (any TP53 row = altered). The analysis checks:
  - which drugs raise p53 targets more in TP53-wild-type than in altered lines in the same wells, and whether that
    is `WT induction` or only `relative (altered lines fall)` (the `pattern` column);
  - a genotype-blind functional p53 status per line, with its agreement with the annotation (AUC) and the
    discordant lines;
  - whether TP53-wild-type lines are depleted more.

  The library has no MDM2 inhibitor: the expected activators are DNA-damaging drugs and antimetabolites, plus
  selinexor (XPO1 inhibitor: keeps p53 in the nucleus). CDKN1A also rises without p53 (HDAC inhibitors), so it is
  never read alone.
- **Loss and level screens.** Lines that lost a gene (e.g. GSDME silencing) are tested for selective depletion
  (the MTAP-null screen) and for re-expression (e.g. DNMT inhibitors; lines with a deletion in the cell-line metadata
  are left out of it: there is nothing to re-express). Re-expression is compared with the lines deleted for the gene
  in the same wells (pure ambient RNA) and needs >= 2 lines up and a dose pattern; lost lines that read no more than
  ambient give `lost lines read ambient only: not interpretable`. For every gene, the analysis tests whether a line's
  baseline level predicts which lines a drug depletes (the Gankyrin test), raw and within lineage.
- **Cross-links to the earlier run** (read from `<data>/mtap_gankyrin`; `--prior DIR` or `--prior none`):
  - agreement of the well map, the MTAP-null calls and the MTAP/PSMD10 effects (identical when both runs read the
    same files with the same `--min-cells`; a `--limit-files` trial differs by design);
  - Gankyrin vs p53 and NRF2 activity;
  - CDKN2A deletion (p16 and ARF lost; from the cell-line metadata, not the MTAP-null call: NCI-H460, A498 and A-427
    lost CDKN2A but keep MTAP) vs p53 activity, with MTAP-null as a 9p21 proxy. Expected: no difference in
    DNA-damage responsiveness (DNA damage activates p53 without ARF);
  - MTAP-null vs the ferroptosis genes;
  - drugs significant (drug-level FDR < 0.10) for MTAP / PSMD10 and for a panel gene, with the number expected
    among drugs of the same activity (strong drugs are in every list). Without an earlier run these are this run's
    MTAP / PSMD10 lists: the same wells, so no reproducibility claim.
- **Positive controls** (`positive_controls.csv`, summary section 3). Each expected effect is listed with its
  verdict and whether it is expected at 24 h (`expected_at_24h`):
  - robust: DNA damage -> p53 targets (more in TP53-wild-type lines); proteasome inhibitors -> proteasome and
    heat-shock genes and HMOX1; the HSP90 inhibitor -> heat-shock genes; ciclopirox -> TFRC; antimitotics -> G2/M;
    dinaciclib -> transcription drop;
  - uncertain at 24 h or at <= 5 uM: decitabine / 5-azacytidine -> GSDME in silenced lines and interferon genes
    (demethylation needs several divisions; usually seen after days); dimethyl fumarate -> NRF2 targets and HMOX1;
    COX inhibitors -> PTGS2 (reported only).

  A robust control that is absent lowers trust in the data; an uncertain one that is absent says nothing about the
  method.

Start with `gene_panel/results/summary.txt` (section 1 checks the artifacts and the agreement with the earlier run,
section 3 the positive controls), then upload `gene_panel/gene_panel_bundle.zip` to Claude to check the numbers
before any agent runs. Scope: mRNA 24 h after the drug. That means no protein, lipid peroxidation, iron, caspase or
gasdermin cleavage, and no death mode: the reports speak of a "ferroptosis-like signature" and label hypotheses.

Agents (after Claude has checked the bundle; same SDK, API key, options, refusal rules and cost cap as the atlas).
Their progress goes to `gene_panel/agents.log`; each agent's own work log is `gene_panel/angles/<pathway>/agent.log`.
Reports: `gene_panel/reports/01_ferroptosis.md` ... `05_crosslinks.md` and `00_overview.md`; costs and status in
`gene_panel/reports/agents_summary.csv`. When the agents finish, `gene_panel/gene_panel_bundle.zip` is remade with
the reports: upload it to Claude. At most 6 agents x `--budget` (default $5) = $30; typical use is well below.
```bash
nohup python3 tahoe_gene_panel.py agents > /dev/null 2>&1 &   # or --dry-run first; --angles p53,ferroptosis for a subset
tail -f gene_panel/agents.log
```
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-..."     # in the same window
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py agents   # log: gene_panel\agents.log
```
Other options:
- `--unreliable-plates LIST|none` (default `plate13` when present) and `--atlas DIR|none` (the atlas to take the
  composition shift and plate factors from; default `<data>/atlas`): see Method v3.
- `--genes "SYM[:pathway],..."` adds genes; it needs a new `--out`, because the per-cell files of another gene list
  are never mixed. Aliases are accepted: FSP1, DFNA5, ASC, MG53, NAPE-PLD, P21, PUMA, NOXA.
- `--tp53-wt` / `--tp53-altered` override the annotation, and `--mtap-null` overrides the MTAP-null call.
- `--layout`, `--min-cells` and `--workers` work as in the MTAP/Gankyrin trial.

## 3. The MTAP / Gankyrin trial (earlier; already run)

```bash
python3 tahoe_mtap_gankyrin.py all --limit-files 30                       # quick trial
nohup python3 tahoe_mtap_gankyrin.py all > /dev/null 2>&1 &               # full run (reuses the trial's work)
python3 tahoe_mtap_gankyrin.py coreg                                      # optional, slow: genome-wide co-regulation
```
Windows: `C:\tahoe\.venv\Scripts\python.exe tahoe_mtap_gankyrin.py all`. The log is `mtap_gankyrin/mtap_gankyrin.log`.
Check section 1 of `mtap_gankyrin/results/summary.txt` first: H1 should be the top well for MTAP, D10 for
Gankyrin, and plate 2 should top the Gankyrin DMSO list. If not, the well positions read from the cell barcodes
are wrong: get the plate layout as a CSV with `sample` and `well` columns and rerun with `--layout layout.csv`
(the atlas and the panel take the same `--layout` option).

Method v3: `tahoe mtap` (or `python3 tahoe_mtap_gankyrin.py analyze`, minutes) redoes the analysis of an earlier
trial on its extract. Like the panel, it takes the composition shift and plate factors from the atlas computed with
v3 (`--atlas DIR|none`), so compute the atlas first; it writes `results/run_info.json` (method version 3).

Other options: `--workers N`, `--mtap-null LINE1,LINE2`, `--extra-genes MAT2A,PRMT5`, `--min-cells N` (default 30),
`--unreliable-plates LIST|none` (default `plate13`).

## Tests

`tahoe test` or `python3 tests/run_smoke.py` (Windows: `C:\tahoe\.venv\Scripts\python.exe tests\run_smoke.py --workdir C:\tahoe\smoke`)
generates a small synthetic Tahoe-100M download with planted effects (well-position artifacts, a plate-2 DMSO
offset, MTAP-null lines, TP53-dependent p53 activation, NRF2 / ISR / iron / GSDME effects, toxic and shutdown drugs,
a failed well) and checks that every script recovers them. No API key is used. Details in `tests/README.md`.
Method v3 adds a planted case for each fix: a noisy plate, an unreliable mixed-dose `plate13`, a strong and an inert
drug sharing one position, a drug at the same position on every plate (not correctable), a composition-shift drug,
a plate row that loses cells (technical, not toxic), and a panel run without an earlier MTAP/Gankyrin output. The
smoke test also checks that the atlas and the panel agree on MTAP and PSMD10, the version stamps, and that
`tahoe status` calls older outputs outdated.
