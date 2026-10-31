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
- `--no-export-all-genes`: the `export` step leaves out `all_genes/` (every gene at the per-profile level, ~21 GB), and
  the run needs ~24 GB less disk. The choice is kept for this data folder; `--export-all-genes` turns it back on (add
  `--redo mg53_export` if the export has already run).

For higher Hugging Face rate limits (optional), make a free read token at huggingface.co/settings/tokens. Then run
`export HF_TOKEN=...` in the same shell before starting.

## Choose a mode

| Mode | What stays on the machine | Free disk needed |
|---|---|---|
| `full` (default) | The whole Tahoe-100M dataset (429 GB, 4,427 files), the same as `tahoe download`, plus the outputs. The whole dataset includes Tahoe's own pseudobulk DE (89 GB) and per-cell `obs_metadata` (2.3 GB); the analysis does not need them, but the `export` step copies Tahoe's DE rows of TRIM72 and the up- / downstream genes into `export/tahoe_deseq2/`. | ~471 GB (~447 with `--no-export-all-genes`) |
| `needed` | Only what the analysis reads: the 3,388 expression files (338 GB) and the four metadata tables, plus the outputs. | ~386 GB (~362) |
| `stream` | Each file is downloaded, processed and deleted, so only the outputs stay (~53 GB, ~25 of them the `export` tables). Use it when the disk is small. To run anything else on the cells later, you must download again. | ~69 GB (~45) |

All three modes give the same tables: they feed the same files to the same atlas and gene-panel code (only `full` adds
`export/tahoe_deseq2/`, Tahoe's own DE rows).

## What you need

| | |
|---|---|
| OS | Linux (tested: Ubuntu-type, Python 3.13). macOS should work but is untested. |
| Disk | The amount for your mode (table above), in the data folder; it includes ~5 GB for the `genome_wide` cache (`mg53_p53/genome_wide/cache`, the per well x line effects of every gene) and ~36 GB at the peak of the `export` step (~25 GB kept: `all_genes/` ~21 GB, the up- / downstream gene tables, ~3.9 MB per selected gene and folder, and, in `full` mode, Tahoe's DE rows, ~3.2 MB per gene; ~4.6 GB of temporary counts while it runs). The budget holds for ~2,000 selected-gene entries; the step checks the free disk itself before it writes anything. Python packages take another ~0.5 GB in `~/tahoe-venv`. |
| Memory | 8 GB or more; 16 GB is better. Each plate read at once needs ~3 GB, and each MG53 step stays under ~4 GB (`genome_wide`: ~3-3.5 GB in its first pass, then ~1 GB plus ~0.9 GB for each of its 2 worker processes; `export`: ~2-3 GB). |
| CPUs | 4 or more. Most steps use a fixed few: they wait on the disk more than on the CPU. More CPUs speed up `mg53_genome_wide`'s screen, its longest part: up to 16 worker processes of 2 threads each, as free memory allows (`MG53_CPUS=N` caps the CPUs it counts). |
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
| `mg53_export` | all | The data as tables in `export/` (its `README.md` defines every file and column, with units): cell lines, drugs, wells (used or excluded, and why), drug-doses; per (plate, well, drug, concentration, cell line) the raw counts, the uncorrected log2 changes (vs the plate's DMSO wells and vs its drug-well median) and the method-v3 corrected effect, for TRIM72, for the genes the data tie to it upstream and downstream, and for every expressed atlas gene (`all_genes/`, Parquet; `--no-export-all-genes` leaves it out); Tahoe's own DE rows of those genes in `full` mode. One more pass over `atlas/pseudobulk`. New and not yet run on the real data: if it fails, the setup says so, leaves it pending and still runs `mg53_summary` and `compare`. If `mg53_genome_wide` failed, it still writes everything that does not need it and says what is missing. | ~30-45 min, +15-40 min for Tahoe's DE rows (estimated) |
| `mg53_summary` | all | Writes `SUMMARY.md` and `summary/T1..T12 *.csv`, including the short answers (T8). | seconds |
| `compare` | all | Compares your tables with the ones committed here (`compare_with_repo.py`). | seconds |

The whole run is the download plus ~6-9 h (full, needed), or ~7-10 h for stream. The times are from a 4-CPU,
16 GB machine and the repository's own notes; the `genome_wide` and `export` times are estimates from their kernels timed
at the real dimensions.

## What you get

All results are in `<data>/mg53_p53/` (default `~/Tahoe-100M/mg53_p53/`):

| File | What it holds |
|---|---|
| `SUMMARY.md` | The short answers and tables T1-T12. The same tables are CSVs in `summary/`. |
| `<step>/tables/` | Every step's full tables, each folder with a `README_tables.txt` that explains its columns. |
| `genome_wide/GENOME_WIDE.md` | The list-free downstream screen and the Tahoe p53 program (tables in `genome_wide/tables/`). |
| `export/` | The data themselves, raw, uncorrected and corrected, as CSV and Parquet; `export/README.md` defines every file and column. `metadata/` (cell lines with TP53 group and genotype features, drugs, wells used or excluded and why, drug-doses, plates); `TRIM72/` (every plate, well, drug, dose and line; per well; per drug-dose x line; per drug-dose; drug-dose x line matrices); `upstream/` and `downstream/` (the genes the data tie to TRIM72, each with why it is there, and their values); `all_genes/` (every expressed gene, Parquet; `python3 mg53_p53/export/export_genes.py --export <data>/mg53_p53/export --genes FUS,ATF3 --out x.csv` writes any genes as CSV); `tahoe_deseq2/` (Tahoe's own DE rows, `full` mode). |
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
- **`mg53_export` failed, or stopped for lack of disk.** The run goes on without it, as for `mg53_genome_wide` below; the
  log says what it needs (e.g. "needs ~27 GB free"; a resumed run counts only what it still has to write). Free disk
  or restart with `--no-export-all-genes` (then
  `--redo mg53_export`), and rerun: finished parts of the export (`<data>/mg53_p53/export/.state`) are kept. If
  `mg53_genome_wide` had failed, `export/downstream/` is empty (its `NOTE.md` says why); when a later run finishes
  `mg53_genome_wide`, the export runs again by itself: its gene tables (TRIM72, upstream, downstream) are rebuilt and,
  in `full` mode, Tahoe's DE rows are read again (~15-40 min); `all_genes/` is kept (with `--no-export-all-genes` the
  pass and the selected-gene store are rebuilt too, because they hold only the selected genes). Deleting
  `export/all_genes/` to get its ~21 GB back is safe: the next export run rebuilds it.
- **`mg53_genome_wide` failed.** The run goes on without it: `SUMMARY.md` and `compare_with_repo.txt` are still
  written, the end of the log says `EXCEPT: mg53_genome_wide`, and `status` lists it as pending. Rerun
  `bash mg53_p53/setup/mg53_setup.sh` to retry it; its caches (`<data>/mg53_p53/genome_wide/cache`) are reused and
  nothing else runs again. To run only that step by hand, use the setup's Python environment (system `python3` lacks
  scipy): `~/tahoe-venv/bin/python mg53_p53/run_mg53_p53.py --data ~/Tahoe-100M --steps genome_wide` (a later setup
  run then runs it once more, from its caches, to mark it done).
