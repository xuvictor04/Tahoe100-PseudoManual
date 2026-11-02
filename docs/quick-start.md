# Quick start


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
| `tahoe_gene_panel.py` | **The gene panel**: ferroptosis, pyroptosis, p53, NAPEPLD, TRIM72, ABCB1/ABCG2, on the MTAP/Gankyrin method. | ~1 h + minutes |
| `old_drug_effect_uncorrected.py` | Superseded. Reproduces the original uncorrected drug lists, for comparison only. | minutes |
| `tahoe` | The one-line commands of the Quick start (Linux / macOS): status, run, log, bundle, agents, stop, setup, ... (`tahoe help`). | seconds |
| `tahoe_status.py` | What `tahoe status` prints: reads the logs, the job files in `<data>/.tahoe`, the process list and the method version each output records; decides what `tahoe run` redoes. | seconds |
| `tests/` | Synthetic Tahoe-100M data with planted effects and a smoke test of every script (see `tests/README.md`). | ~3 min |
| `trim72_idarubicin/` | TRIM72 (MG53) under idarubicin: Tahoe's published DE rows, and corrected per-line fold changes at 5 uM (see its README). | minutes |
| `mg53_p53/` | MG53 (TRIM72): what raises it and whether it goes with p53 output, on the computed atlas + gene panel (`run_mg53_p53.py`; see its README). | ~45 min |

