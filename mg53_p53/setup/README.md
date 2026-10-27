# From an empty machine to the MG53 tables

One command takes an empty Linux machine to every table of the MG53 (TRIM72) upstream / downstream analysis. It uses
Tahoe-100M data only; nothing new is generated. It streams Tahoe-100M from Hugging Face, builds the corrected atlas and
gene panel, runs every MG53 step, and checks your tables against the ones in this repository.

```bash
sudo apt-get update && sudo apt-get install -y git curl python3 python3-venv     # Ubuntu / Debian; once
git clone https://github.com/xuvictor04/tahoe100-pseudomanual.git && cd tahoe100-pseudomanual
git checkout claude/zen-franklin-nyvnah          # until this branch is merged
bash mg53_p53/setup/mg53_setup.sh                # starts in the background; safe to log out
```

| Command | What it does |
|---|---|
| `bash mg53_p53/setup/mg53_setup.sh` | Starts the run, or resumes it, in the background. |
| `bash mg53_p53/setup/mg53_setup.sh status` | Shows which steps are done, whether it is running, and the end of the log. |
| `tail -f ~/Tahoe-100M/.mg53_setup/setup.log` | Follows the log. |
| `bash mg53_p53/setup/mg53_setup.sh stop` | Stops the run. The first command resumes it. |
| `bash mg53_p53/setup/mg53_setup.sh run` | Runs the same steps in this terminal instead of the background. |

Options:

- `--data DIR`: the data folder (default `$TAHOE_DATA`, else `~/Tahoe-100M`).
- `--venv DIR`: the Python environment (default `$TAHOE_VENV`, else `~/tahoe-venv`).
- `--workers N`: how many plates stream at once (default: one per CPU, at most one per ~3 GB of free memory).
- `--redo STEP`: runs STEP and every later step again.

Use the same `--data` with every command.

## What you need

| | |
|---|---|
| OS | Linux (tested: Ubuntu-type, Python 3.13). macOS should work but is untested. |
| Disk | ~28 GB free in the data folder. The atlas pseudobulk takes ~20 GB, the per-cell gene panel ~2.6 GB, and the MG53 outputs and caches ~1-2 GB. Python packages take ~0.5 GB in `~/tahoe-venv`. |
| Memory | 8 GB or more; 16 GB is better. Each streamed plate needs ~3 GB, and each MG53 step stays under ~4 GB. |
| CPUs | 4 or more (more plates stream in parallel). |
| Network | Reaches `huggingface.co`. All 340 GB are downloaded once but never kept. |
| Network (MG53 steps) | Reaches `storage.googleapis.com`, `rest.ensembl.org` / `www.ensembl.org`, `humantfs.ccbr.utoronto.ca` and `omnipathdb.org` once. These provide the TF list, HGNC / Ensembl coordinates and the CollecTRI / DoRothEA regulons. |
| Accounts | None. Tahoe-100M is public (CC0), so no Hugging Face token is needed. |

## The steps

Every step is marked done in `<data>/.mg53_setup/` and skipped on a rerun. An interrupted step picks up where it stopped:

- finished plates, per-cell files and downloads are kept;
- the MG53 steps reuse their caches.

A dropped connection during the stream is retried automatically (up to 3 reruns). For anything else, fix the cause and
rerun the same command. Times are from a 4-CPU, 16 GB machine.

| Step | What it does | Time here |
|---|---|---|
| `check` | Checks for python3 3.9+ with venv and curl, enough disk and memory, and that Hugging Face is reachable. | seconds |
| `env` | Makes the Python environment: numpy, pandas, pyarrow, scipy, psutil, fsspec, aiohttp, requests. | ~1 min |
| `metadata` | Downloads the four Tahoe-100M metadata tables. | ~1 min |
| `plates` | Maps each of the 3,388 expression files to its plate, reading one column chunk per file. | ~3 min |
| `stream` | Downloads each file once and reads it into the atlas pseudobulk and the per-cell gene panel. It then replaces the file with an empty stub (`setup/stream_build.py`). | ~3 h; limited by download speed (~35 MB/s here) |
| `atlas_build` | `tahoe_atlas.py build`: indexes and reuses the streamed plates. | ~4 min |
| `atlas_effects` | `tahoe_atlas.py effects`: method-v3 corrected effects (16,643 genes × 1,132 drug-doses × 50 lines). | ~30 min |
| `panel_extract` | `tahoe_gene_panel.py extract`: reuses the per-cell files and builds the well tables. | ~8 min |
| `panel_analyze` | `tahoe_gene_panel.py analyze`: the gene panel with the atlas's corrections. | ~10 min |
| `ida` | TRIM72 × idarubicin per cell line, corrected: the 5 µM fold table (`trim72_idarubicin/corrected/`). | ~2 min |
| `mg53_perturbations` | Which drug-doses and drug classes move TRIM72 (T1, T2). | ~1 min |
| `mg53_coregulation` | Genes co-regulated with TRIM72, untreated partners, and the FUS-TRIM72 locus (T3, T4). | ~25 min |
| `mg53_p53_dependence` | TRIM72 induction in TP53 wild-type vs altered lines (T5). | ~3 min |
| `mg53_downstream` | TRIM72 vs p53 output per line, across drugs, untreated, and in single cells (T6, T7). | ~10 min |
| `mg53_two_way` | TRIM72 vs p53 output over all drug-doses × lines, with TP53 genotype as the control (T9). | ~30 min |
| `mg53_single_cell_all` | The same contrast in single cells of all wells, plus the ATF3-adjusted run (T10). | ~25 min |
| `mg53_upstream_tf` | Transcription-factor activities and cell-line traits vs TRIM72 (T11, T12). | ~5 min |
| `mg53_summary` | Writes `SUMMARY.md` and `summary/T1..T12 *.csv`, including the short answers (T8). | seconds |
| `compare` | Compares your tables with the ones committed here (`compare_with_repo.py`). | seconds |

The whole run took ~5 h here, most of it the stream. If `<data>/data` already holds the full download (3,388 files with
cells, e.g. from `tahoe download`), the script uses it as it is. It skips `plates` and `stream`, `atlas_build` and
`panel_extract` read those files, and the download is never modified.

## What you get

All results are in `<data>/mg53_p53/` (default `~/Tahoe-100M/mg53_p53/`):

| File | What it holds |
|---|---|
| `SUMMARY.md` | The short answers and tables T1-T12. The same tables are CSVs in `summary/`. |
| `<step>/tables/` | Every step's full tables, each folder with a `README_tables.txt` that explains its columns. |
| `trim72_idarubicin/` | TRIM72 fold change per cell line at idarubicin 5 µM, plus all doses, corrected. |
| `compare_with_repo.txt` | Your tables next to the committed ones: `identical` (to 1e-6), `close` (to 1e-3; another numpy/BLAS can do that), or `differs`. |
| `run_mg53_p53.log` | The MG53 steps' log. The setup log is `<data>/.mg53_setup/setup.log`. |

The literature checks are not part of the run: PubMed / Europe PMC, the p53 census and ChIP-Atlas. They need more
internet access; run them with
`~/tahoe-venv/bin/python mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps literature`.

## If something goes wrong

- **A step failed.** The setup log shows the error: the last lines of `status`, or `<data>/.mg53_setup/setup.log`. Fix the
  cause, then rerun `bash mg53_p53/setup/mg53_setup.sh`. Finished work is kept.
- **The machine rebooted.** Rerun the same command to resume.
- **Not enough disk.** Free space, or put the data on a larger disk with `--data /big/disk/Tahoe-100M`. Use the same
  `--data` with every later command.
- **Out of memory during `stream`.** Stop the run, then restart it with fewer plates at once, e.g. `--workers 2`.
- **`stream` refuses to run because `<data>/data` holds files with cells.** That folder has a partial download. Finish
  it (`tahoe download`), or move it away to stream instead. The stream would otherwise replace those files with stubs.
- **Rerun one part.** For example, `--redo mg53_two_way` reruns that step and every later one.
