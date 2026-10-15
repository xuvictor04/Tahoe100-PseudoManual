# Tahoe-100M scripts: the all-angles atlas, the gene panel, and the MTAP/Gankyrin trial

Copy this folder's files into your Tahoe-100M download folder (default `~/Tahoe-100M`; on Windows `C:\tahoe\Tahoe-100M`)
and run them from there (on Linux / macOS the `tahoe` command of the Quick start below needs no copying). Replace
older copies too: `tahoe_atlas.py` and `tahoe_gene_panel.py` need the current `tahoe_mtap_gankyrin.py`, and the panel
the current `tahoe_atlas.py` (they stop with a message when they find an older one). The MTAP/Gankyrin method and
numbers are unchanged (only logging, keep-awake, memory use, resuming and printed hints changed), so your earlier
`mtap_gankyrin/` output stays valid. Two runs are current:
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
- `tahoe log` follows the running job's log (Ctrl-C stops watching, not the run); `tahoe stop` stops a run (finished
  work is reused); `tahoe update` gets the newest scripts (git pull); `tahoe help` lists everything.
- Options go to the script: `tahoe atlas --workers 4`, `tahoe panel analyze`, `tahoe atlas lookup gene MTAP`.
- Nothing is copied: the scripts run from the repo folder with `--data ~/Tahoe-100M` (another folder:
  `export TAHOE_DATA=/path`), and the outputs land where the commands below put them. Copies you made in
  `~/Tahoe-100M` are not used: once no run started by hand uses them, delete them there
  (`rm tahoe_atlas.py tahoe_gene_panel.py tahoe_mtap_gankyrin.py`), so an old copy is never run by mistake.
- Runs started by hand show up in `tahoe status` too, and `tahoe panel` waits for an atlas that is running.

The long commands below still work. Windows: use the PowerShell commands below.

**Order of work.**
0. Copy all files over the old ones (see above; not needed with the `tahoe` command).
1. Atlas: `check`, then `compute` (~1-1.5 h).
2. Gene panel: `check`, then `all` (~1 h). Run it after the atlas, so that its agent briefs include the genome-wide
   atlas look-ups. Never run the two long passes at the same time: each reads all ~96M cells.
3. Upload `atlas/atlas_bundle.zip` and `gene_panel/gene_panel_bundle.zip` to Claude to check the numbers.
4. Then the agents of each (`tahoe_atlas.py agents`, `tahoe_gene_panel.py agents`). Each remakes its bundle with the
   reports: upload both again. Do not rerun `compute`/`angles` or the panel's `all`/`analyze` after the agents: that
   makes every report out of date, and the next `agents` run redoes (and pays for) all of them. To remake a bundle,
   use `bundle`.

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
| `tahoe_status.py` | What `tahoe status` prints: reads the logs, the job files in `<data>/.tahoe` and the process list. | seconds |
| `tests/` | Synthetic Tahoe-100M data with planted effects and a smoke test of every script (see `tests/README.md`). | ~3 min |

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
last; `angles`, `agents` and `lookup` refuse effects without that stamp (an interrupted run, or effects from an older
`tahoe_atlas.py`: run `compute` again). On Windows, close agents and look-ups that read `atlas/effects` before
rerunning `compute`.

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
briefs name the Python that ran `angles`, so run `angles` (minutes) on the computer that runs the agents.

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
program. Keep the current `tahoe_mtap_gankyrin.py` and `tahoe_atlas.py` next to it (copy them over older versions;
the MTAP/Gankyrin method and numbers are unchanged, so the earlier `mtap_gankyrin/` output stays valid).

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
delete the folder). The agent briefs are written by `analyze`: they name the Python that ran it, and they offer
genome-wide look-ups (`tahoe_atlas.py lookup`) only if the atlas is already computed in `<data>/atlas`. If the atlas
comes later, rerun `python3 tahoe_gene_panel.py analyze` (minutes) before the panel's agents.

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
  plus toxicity and shutdown flags. This shows, for example, whether CHAC1/SLC7A11/PTGS2 rise with or without a
  general ATF4 stress response.
- **p53.** TP53 status comes from the cell-line driver table (any TP53 row = altered). The analysis checks:
  - which drugs raise p53 targets more in TP53-wild-type than in altered lines in the same wells;
  - a genotype-blind functional p53 status per line, with its agreement with the annotation (AUC) and the
    discordant lines;
  - whether TP53-wild-type lines are depleted more.

  The library has no MDM2 inhibitor: the expected activators are DNA-damaging drugs and antimetabolites, plus
  selinexor (XPO1 inhibitor: keeps p53 in the nucleus). CDKN1A also rises without p53 (HDAC inhibitors), so it is
  never read alone.
- **Loss and level screens.** Lines that lost a gene (e.g. GSDME silencing) are tested for selective depletion
  (the MTAP-null screen) and for re-expression (e.g. DNMT inhibitors; lines with a deletion in the cell-line metadata
  are left out of it: there is nothing to re-express). For every gene, the analysis tests whether a line's baseline
  level predicts which lines a drug depletes (the Gankyrin test), raw and within lineage.
- **Cross-links to the earlier run** (read from `<data>/mtap_gankyrin`; `--prior DIR` or `--prior none`):
  - agreement of the well map, the MTAP-null calls and the MTAP/PSMD10 effects (identical when both runs read the
    same files with the same `--min-cells`; a `--limit-files` trial differs by design);
  - Gankyrin vs p53 and NRF2 activity;
  - CDKN2A deletion (p16 and ARF lost; from the cell-line metadata, not the MTAP-null call: NCI-H460, A498 and A-427
    lost CDKN2A but keep MTAP) vs p53 activity, with MTAP-null as a 9p21 proxy. Expected: no difference in
    DNA-damage responsiveness (DNA damage activates p53 without ARF);
  - MTAP-null vs the ferroptosis genes;
  - drugs significant (drug-level FDR < 0.10) in both runs, with the number expected by chance.
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

Other options: `--workers N`, `--mtap-null LINE1,LINE2`, `--extra-genes MAT2A,PRMT5`, `--min-cells N` (default 30).

## Tests

`tahoe test` or `python3 tests/run_smoke.py` (Windows: `C:\tahoe\.venv\Scripts\python.exe tests\run_smoke.py --workdir C:\tahoe\smoke`)
generates a small synthetic Tahoe-100M download with planted effects (well-position artifacts, a plate-2 DMSO
offset, MTAP-null lines, TP53-dependent p53 activation, NRF2 / ISR / iron / GSDME effects, toxic and shutdown drugs,
a failed well) and checks that every script recovers them. No API key is used. Details in `tests/README.md`.
