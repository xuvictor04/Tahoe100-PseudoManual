# From an empty machine to the MG53 tables

One command takes an empty Linux machine to every table of the MG53 (TRIM72) upstream / downstream analysis:

1. It downloads Tahoe-100M from Hugging Face.
2. It builds the corrected atlas and the gene panel.
3. It runs every MG53 step.
4. It checks your tables against the ones in this repository.

Everything comes from Tahoe-100M; nothing new is generated.

```bash
sudo apt-get update && sudo apt-get install -y git curl python3 python3-venv     # Ubuntu / Debian; once
git clone https://github.com/xuvictor04/tahoe100-pseudomanual.git && cd tahoe100-pseudomanual
git checkout claude/zen-franklin-nyvnah          # until this branch is merged
bash mg53_p53/setup/mg53_setup.sh                # starts in the background; safe to log out
```

| Command | What it does |
|---|---|
| `bash mg53_p53/setup/mg53_setup.sh` | Starts the run, or resumes it, in the background. |
| `bash mg53_p53/setup/mg53_setup.sh status` | Shows which steps are done, how far the download is, whether it is running, and the end of the log. |
| `tail -f ~/Tahoe-100M/.mg53_setup/setup.log` | Follows the log. |
| `bash mg53_p53/setup/mg53_setup.sh stop` | Stops the run. The first command resumes it. |
| `bash mg53_p53/setup/mg53_setup.sh run` | Runs the same steps in this terminal instead of the background. |

Options:

- `--data DIR`: the data folder (default `$TAHOE_DATA`, else `~/Tahoe-100M`). Use the same `--data` with every command.
- `--mode full|needed|stream`: how Tahoe-100M gets onto the machine (see below). The default is `full`, or whatever
  mode the folder already uses.
- `--venv DIR`: the Python environment (default `~/tahoe-venv`; made if missing).
- `--workers N`: how many plates are read at once (default: from CPUs and free memory).
- `--redo STEP`: runs STEP and every later step again.

For higher Hugging Face rate limits (optional), make a free read token at huggingface.co/settings/tokens. Then run
`export HF_TOKEN=...` in the same shell before starting.

## Choose a mode

| Mode | What stays on the machine | Free disk needed |
|---|---|---|
| `full` (default) | The whole Tahoe-100M dataset (429 GB, 4,427 files), the same as `tahoe download`, plus the outputs. The whole dataset includes Tahoe's own pseudobulk DE (89 GB) and per-cell `obs_metadata` (2.3 GB), which this analysis does not read. | ~435 GB |
| `needed` | Only what the analysis reads: the 3,388 expression files (338 GB) and the four metadata tables, plus the outputs. | ~350 GB |
| `stream` | Each file is downloaded, processed and deleted, so only the outputs stay (~28 GB). Use it when the disk is small. To run anything else on the cells later, you must download again. | ~33 GB |

All three modes give the same tables: they feed the same files to the same atlas and gene-panel code.

## What you need

| | |
|---|---|
| OS | Linux (tested: Ubuntu-type, Python 3.13). macOS should work but is untested. |
| Disk | The amount for your mode (table above), in the data folder; it includes ~5 GB for the `genome_wide` cache (`mg53_p53/genome_wide/cache`, the per well x line effects of every gene). Python packages take another ~0.5 GB in `~/tahoe-venv`. |
| Memory | 8 GB or more; 16 GB is better. Each plate read at once needs ~3 GB, and each MG53 step stays under ~4 GB (`genome_wide`: ~3-3.5 GB in its first pass, then ~1 GB plus ~0.9 GB for each of its 2 worker processes). |
| CPUs | 4 or more. |
| Network | Reaches `huggingface.co` for the dataset. |
| Network (MG53 steps) | Reaches `storage.googleapis.com`, `rest.ensembl.org` / `www.ensembl.org`, `humantfs.ccbr.utoronto.ca` and `omnipathdb.org` once. These provide the TF list, HGNC / Ensembl coordinates and the CollecTRI / DoRothEA regulons. |
| Accounts | None. Tahoe-100M is public (CC0). `HF_TOKEN` is optional. |

## The steps

A machine check runs first every time: python3 3.9+ with venv, curl, enough disk for the mode, memory, and whether
Hugging Face is reachable. Every step is then marked done in `<data>/.mg53_setup/` and skipped on a rerun. An
interrupted step resumes where it stopped:

- finished files, plates and per-cell files are kept;
- the MG53 steps reuse their caches.

Dropped connections are retried automatically (download: 5 attempts; stream: 4). For anything else, fix the cause
(the log says what) and rerun the same command.

| Step | Mode | What it does | Time |
|---|---|---|---|
| `env` | all | Makes the Python environment: numpy, pandas, pyarrow, scipy, psutil, fsspec, aiohttp, requests, huggingface_hub, hf_xet. | ~3 min |
| `download` | full, needed | `hf download tahoebio/Tahoe-100M` into the data folder. It is resumable, and every file is then checked. Progress is logged every 10 min. | Set by your bandwidth: 429 GB is ~1.2 h at 100 MB/s, ~4 h at 30 MB/s |
| `metadata`, `plates`, `stream` | stream | Gets the metadata tables and the file-to-plate map. Then each file is downloaded once, read by the atlas build and the gene-panel extract, and replaced by an empty stub (`stream_build.py`). | ~3 h here (~35 MB/s) |
| `atlas_build` | all | `tahoe_atlas.py build`: pseudobulk per well × cell line, ~20 GB. In stream mode it reuses the streamed plates. | ~1 h (stream: minutes) |
| `atlas_effects` | all | `tahoe_atlas.py effects`: method-v3 corrected effects (16,643 genes × 1,132 drug-doses × 50 lines). | ~30 min |
| `panel_extract` | all | `tahoe_gene_panel.py extract`: the per-cell gene panel, ~2.6 GB. In stream mode it reuses the streamed files. | ~1 h (stream: ~8 min) |
| `panel_analyze` | all | `tahoe_gene_panel.py analyze`: the gene panel with the atlas's corrections. | ~10 min |
| `ida` | all | TRIM72 × idarubicin per cell line, corrected: the 5 µM fold table (`trim72_idarubicin/corrected/`). | ~2 min |
| `mg53_perturbations` | all | Which drug-doses and drug classes move TRIM72 (T1, T2). | ~1 min |
| `mg53_coregulation` | all | Genes co-regulated with TRIM72, untreated partners, and the FUS-TRIM72 locus (T3, T4). | ~25 min |
| `mg53_p53_dependence` | all | TRIM72 induction in TP53 wild-type vs altered lines (T5). | ~3 min |
| `mg53_downstream` | all | TRIM72 vs p53 output per line, across drugs, untreated, and in single cells (T6, T7). | ~10 min |
| `mg53_two_way` | all | TRIM72 vs p53 output over all drug-doses × lines, with TP53 genotype as the control (T9). | ~30 min |
| `mg53_single_cell_all` | all | The same contrast in single cells of all wells, plus the ATF3-adjusted run (T10). | ~25 min |
| `mg53_upstream_tf` | all | Transcription-factor activities and cell-line traits vs TRIM72 (T11, T12). | ~5 min |
| `mg53_genome_wide` | all | The list-free version: every atlas gene's per-line effects (one more pass over `atlas/pseudobulk`, kept as a 4.4 GB cache), a p53 program found from the data, TRIM72 against every gene with TP53 genotype as the control, data-driven programs. Writes `genome_wide/GENOME_WIDE.md`. New and not yet run on the real data: if it fails, the setup says so, leaves it pending and still runs `mg53_summary` and `compare`; rerunning the same command retries it. | ~1.5-3 h (estimated) |
| `mg53_summary` | all | Writes `SUMMARY.md` and `summary/T1..T12 *.csv`, including the short answers (T8). | seconds |
| `compare` | all | Compares your tables with the ones committed here (`compare_with_repo.py`). | seconds |

The whole run is the download plus ~5.5-8 h (full, needed), or ~6.5-9 h for stream. The times are from a 4-CPU,
16 GB machine and the repository's own notes; the `genome_wide` time is an estimate from its kernels timed at the real
dimensions.

## What you get

All results are in `<data>/mg53_p53/` (default `~/Tahoe-100M/mg53_p53/`):

| File | What it holds |
|---|---|
| `SUMMARY.md` | The short answers and tables T1-T12. The same tables are CSVs in `summary/`. |
| `<step>/tables/` | Every step's full tables, each folder with a `README_tables.txt` that explains its columns. |
| `genome_wide/GENOME_WIDE.md` | The list-free downstream screen and the Tahoe p53 program (tables in `genome_wide/tables/`). |
| `trim72_idarubicin/` | TRIM72 fold change per cell line at idarubicin 5 µM, plus all doses, corrected. |
| `compare_with_repo.txt` | Your tables next to the committed ones: `identical` (to 1e-6), `close` (to 1e-3; another numpy/BLAS can do that), or `differs`. |
| `run_mg53_p53.log` | The MG53 steps' log. The setup log is `<data>/.mg53_setup/setup.log`. |

In `full` and `needed` mode, the dataset itself stays in `<data>/data` and `<data>/metadata`, for any later analysis.

The literature checks are not part of the run: PubMed / Europe PMC, the p53 census and ChIP-Atlas. They need more
internet access; run them with
`~/tahoe-venv/bin/python mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps literature`.

## If something goes wrong

- **A step failed.** The setup log shows the error: the last lines of `status`, or `<data>/.mg53_setup/setup.log`. For
  the download, `<data>/.mg53_setup/download.console` has `hf`'s own output. Fix the cause, then rerun
  `bash mg53_p53/setup/mg53_setup.sh`. Finished work is kept.
- **The machine rebooted.** Rerun the same command to resume.
- **Not enough disk.** Free space, use `--data` on a larger disk, or use a smaller mode (`--mode needed` or
  `--mode stream`). Use the same `--data` with every later command.
- **Out of memory.** Stop the run, then restart it with fewer plates at once, e.g. `--workers 2`.
- **You already have Tahoe-100M.** Point `--data` at it and use `--mode full`. The download step checks it, fetches
  anything missing, and never deletes your files.
- **Stream mode refuses because `<data>/data` holds files with cells.** Use `--mode full` on that folder, or another
  `--data`. Streaming would replace those files with empty stubs.
- **Rerun one part.** For example, `--redo mg53_two_way` reruns that step and every later one.
- **`mg53_genome_wide` failed.** The run goes on without it: `SUMMARY.md` and `compare_with_repo.txt` are still
  written, the end of the log says `EXCEPT: mg53_genome_wide`, and `status` lists it as pending. Rerun
  `bash mg53_p53/setup/mg53_setup.sh` to retry it; its caches (`<data>/mg53_p53/genome_wide/cache`) are reused and
  nothing else runs again. To run only that step by hand, use the setup's Python environment (system `python3` lacks
  scipy): `~/tahoe-venv/bin/python mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps genome_wide` (a later setup
  run then runs it once more, from its caches, to mark it done).
