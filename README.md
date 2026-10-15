# Tahoe-100M scripts: MTAP/Gankyrin trial and the all-angles atlas

Copy this folder's files into your Tahoe-100M download folder (default `~/Tahoe-100M`) and run them from there.
Requirements: Python 3.10+, numpy, pandas, pyarrow, duckdb (the download script installs them); for the agents
also `pip install claude-agent-sdk` and an Anthropic API key.

| File | What it does | Time |
|---|---|---|
| `00_download_tahoe.sh` | Installs the tools, fixes the Brotli crash, downloads the dataset (resumable). Skip if your download is intact. | hours |
| `01_preview_parquet.py` | Writes `tahoe_preview.txt` / `.csv`: schema and 100 cells with gene names, for a first look. | seconds |
| `02_find_mtap_gankyrin.py` | Searches every metadata table for MTAP / PSMD10 / Gankyrin and pulls both genes' raw (uncorrected) DE tests into `mtap_search/`. | minutes |
| `tahoe_mtap_gankyrin.py` | The MTAP / Gankyrin trial run with all artifact corrections. Results in `mtap_gankyrin/results/`. Also a library the atlas imports: keep it next to `tahoe_atlas.py`. | ~1 hour |
| `tahoe_atlas.py` | **Every angle of the whole dataset** (all genes, drugs, doses, cell lines), one data package per angle, and a Claude agent per angle that writes a report. | see below |
| `old_drug_effect_uncorrected.py` | Superseded. Reproduces the original uncorrected drug lists, for comparison only. | minutes |

## The atlas: every angle, with an agent at each endpoint

Free disk: ~20 GB for `atlas/pseudobulk`. Memory: ~2.5 GB per build worker (the script sizes itself to what
is free), ~5 GB for `effects`.

### On Windows (PowerShell)
Use the Python of your environment directly (here `C:\tahoe\.venv`); no `nohup` is needed:
```powershell
cd C:\tahoe\Tahoe-100M                                   # tahoe_atlas.py and tahoe_mtap_gankyrin.py both here
C:\tahoe\.venv\Scripts\python.exe -m pip install numpy pandas pyarrow scipy psutil
C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py check
C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py compute
```
Leave the window open while it runs. The script keeps the PC from sleeping (on a laptop: stay plugged in and keep
the lid open) and writes its log to `atlas\atlas.log`. If the data sit on a hard drive rather than an SSD, `check`
suggests a `--workers` number that reads more smoothly. Later, for the agents: `$env:ANTHROPIC_API_KEY="sk-ant-..."`
in the same window, `...\python.exe -m pip install claude-agent-sdk`, then `...\python.exe tahoe_atlas.py agents`.
On Windows the agents use PowerShell (with the same delete/kill/network refusals as on Linux); `--sandbox` is not
available there.

### 1. Compute (no agents, no API key needed)
```bash
cd ~/Tahoe-100M                                         # tahoe_atlas.py and tahoe_mtap_gankyrin.py both here
python3 tahoe_atlas.py check                            # preflight: FAIL lines must be fixed; agent lines may say warn
nohup python3 tahoe_atlas.py compute > atlas.log 2>&1 & # build + effects + angles, about 1-1.5 h
tail -f atlas.log                                       # Ctrl-C stops watching, not the run
```
`compute` ends by writing `atlas/atlas_bundle.zip` (a few MB: the key tables of every angle plus the log).
Download it and upload it to Claude, which checks the numbers (well positions, artifact corrections, known
biology) before any money is spent on agents. If the run stops part-way, run the same command again: finished
plates are reused.

### 2. Agents (after the check)
```bash
pip install claude-agent-sdk            # bundles the Claude Code engine the agents run on (Python 3.10+)
export ANTHROPIC_API_KEY=sk-ant-...     # from console.anthropic.com; add to ~/.bashrc to keep it
python3 tahoe_atlas.py check            # now also makes one tiny live agent call (about one cent)
nohup python3 tahoe_atlas.py agents > agents.log 2>&1 &
```
When the agents finish, `atlas/atlas_bundle.zip` is remade with every report added (`python3 tahoe_atlas.py
bundle` remakes it any time): upload it to Claude to turn each report into a doc. `all` runs both stages in one
go. The computation steps (each reuses the previous one's output):

| Step | What it does | Time (estimate) |
|---|---|---|
| `build` | One pass over all ~96M cells: counts per well x cell line x gene (one worker per plate). | 20-60 min |
| `effects` | Corrected effect of every drug-dose on every gene (~15,000 genes), on growth of every line, and how strongly each line shows each drug's response. | 10-20 min |
| `angles` | One folder per angle with tables, a `brief.md` for its agent, and cards for every drug and line. | ~5 min |
| `agents` | One Claude agent per angle reads its folder, runs its own Python checks, writes `report.md`; then an overview agent reads all reports. | 30-90 min |

Corrections carried over from the MTAP/Gankyrin work: plate baseline = median of the plate's drug wells (never
DMSO); leave-drug-out well-position correction; robust z against the spread of all wells; Stouffer over plates;
BH FDR within each gene; failed wells removed; non-expressing lines left out per gene; growth z with counting
noise; toxicity, transcription-shutdown and cell-cycle flags on every drug-dose.

### Angles (one report each, in `atlas/reports/`)
| Report | Question |
|---|---|
| `01_quality` | Where are the traps: well positions, plate DMSO offsets, failed wells, replicate agreement, z calibration |
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
`--model sonnet` (default) or `opus` (deeper, ~2x cost); `--budget 5` = hard USD cap per agent (12 agents ->
at most $60; typical use is well below); `--parallel 3`; `--angles drugs,genes,focus` to run a subset;
`--redo` to rerun reports that are already up to date (otherwise finished reports are skipped, so a rerun only
redoes failed ones); `--dry-run` writes the prompts without calling anything. Each agent's work log is
`atlas/angles/<angle>/agent.log`; costs and status are in `atlas/reports/agents_summary.csv`.

What agents may do: read anything in the atlas folder, write in their own angle folder, run shell commands and
Python. Refused outright: rm, kill, sudo, git, pip/apt, curl/wget/ssh and similar. No web access unless you add
`--web` (literature checks); `--sandbox` additionally runs their shell inside bubblewrap
(`sudo apt-get install -y bubblewrap socat`).

## The MTAP / Gankyrin trial (earlier)

```bash
python3 tahoe_mtap_gankyrin.py all --limit-files 30                      # quick trial
nohup python3 tahoe_mtap_gankyrin.py all > mtap_gankyrin.log 2>&1 &     # full run (reuses the trial's work)
python3 tahoe_mtap_gankyrin.py coreg                                     # optional, slow: genome-wide co-regulation
```
Check section 1 of `mtap_gankyrin/results/summary.txt` first: H1 should be the top well for MTAP, D10 for
Gankyrin, and plate 2 should top the Gankyrin DMSO list. If not, the well positions read from the cell barcodes
are wrong: get the plate layout as a CSV with `sample` and `well` columns and rerun with `--layout layout.csv`
(the atlas takes the same `--layout` option).

Other options: `--workers N`, `--mtap-null LINE1,LINE2`, `--extra-genes MAT2A,PRMT5`, `--min-cells N` (default 30).
