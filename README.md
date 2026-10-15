# Tahoe-100M scripts: the all-angles atlas, the gene panel, and the MTAP/Gankyrin trial

Copy this folder's files into your Tahoe-100M download folder (default `~/Tahoe-100M`; on Windows `C:\tahoe\Tahoe-100M`)
and run them from there. Two runs are current:
1. **The atlas** (`tahoe_atlas.py`): one long computation that aggregates the whole dataset and pre-digests it into one
   data package per angle (genes, drugs, classes, cell lines, biomarkers, programs, cell state, ...), followed by one
   Claude agent per angle that does the actual analysis and writes a report.
2. **The gene panel** (`tahoe_gene_panel.py`): the MTAP/Gankyrin method, already run on the real data, applied to the
   ferroptosis, pyroptosis and p53 genes plus NAPEPLD (NAPE-PLD) and TRIM72 (MG53), with cross-links back to MTAP and
   Gankyrin; optionally one agent per pathway.

Requirements: Python 3.10+ with numpy, pandas, pyarrow (every script); duckdb for `02_find_mtap_gankyrin.py`,
`old_drug_effect_uncorrected.py` and `tahoe_mtap_gankyrin.py coreg`; scipy and psutil are optional (used when present).
For the agents also `claude-agent-sdk` and an Anthropic API key.

| File | What it does | Time |
|---|---|---|
| `00_download_tahoe.sh` | Installs the tools, fixes the Brotli crash, downloads the dataset (resumable; Linux/macOS, Windows below). Skip if your download is intact. | hours |
| `01_preview_parquet.py` | Writes `tahoe_preview.txt` / `.csv`: schema and 100 cells with gene names, for a first look. | seconds |
| `02_find_mtap_gankyrin.py` | Searches every metadata table for MTAP / PSMD10 / Gankyrin and pulls both genes' raw (uncorrected) DE tests into `mtap_search/`. | minutes |
| `tahoe_mtap_gankyrin.py` | The MTAP / Gankyrin trial with all artifact corrections (`mtap_gankyrin/results/`). Also the library the atlas and the panel import: keep it next to them. | ~1 hour |
| `tahoe_atlas.py` | **Every angle of the whole dataset** (all genes, drugs, doses, cell lines), one data package per angle, and a Claude agent per angle that writes a report. | see below |
| `tahoe_gene_panel.py` | **The gene panel**: ferroptosis, pyroptosis, p53, NAPEPLD, TRIM72, on the MTAP/Gankyrin method. | ~1 h + minutes |
| `old_drug_effect_uncorrected.py` | Superseded. Reproduces the original uncorrected drug lists, for comparison only. | minutes |
| `tests/` | Synthetic Tahoe-100M data with planted effects and a smoke test of every script (see `tests/README.md`). | ~2 min |

## Setup

**Linux / macOS:** `bash 00_download_tahoe.sh` (or `bash 00_download_tahoe.sh /data/Tahoe-100M`) installs the packages
and downloads into `~/Tahoe-100M`.

**Windows (PowerShell):** use the Python of your environment directly (here `C:\tahoe\.venv`):
```powershell
C:\tahoe\.venv\Scripts\python.exe -m pip install -U huggingface_hub hf_xet "brotli>=1.2.0" numpy pandas pyarrow duckdb scipy psutil
C:\tahoe\.venv\Scripts\hf.exe download tahoebio/Tahoe-100M --repo-type dataset --local-dir C:\tahoe\Tahoe-100M
```
Rerunning the download resumes it. On a `process() takes no keyword arguments` error run
`C:\tahoe\.venv\Scripts\python.exe -m pip uninstall -y brotli brotlicffi` and download again. Optional, for higher rate
limits: `$env:HF_TOKEN="hf_xxx"` first. In the commands below, Windows users type `C:\tahoe\.venv\Scripts\python.exe`
where Linux shows `python3` (if the path has spaces, PowerShell needs `& "C:\path with spaces\python.exe" ...`).

**Logs and long runs.** Every long command writes its own log into its output folder (`atlas/atlas.log`,
`atlas/agents.log`, `gene_panel/gene_panel.log`, `mtap_gankyrin/mtap_gankyrin.log`), including worker lines and a
crash traceback, and keeps the computer from sleeping while it runs (Windows: power request; macOS: caffeinate;
Linux: systemd-inhibit where available). A laptop still sleeps when its lid is closed: keep it plugged in, lid open.
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
are reused.

### Agents (after the check)
```bash
pip install claude-agent-sdk            # bundles the Claude Code engine the agents run on (Python 3.10+)
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
are already up to date (otherwise finished reports are skipped, so a rerun only redoes failed ones); `--dry-run`
writes the prompts without calling anything. Each agent's work log is `atlas/angles/<angle>/agent.log`; costs and
status are in `atlas/reports/agents_summary.csv`.

What agents may do: read anything in the atlas folder, write in their own angle folder, run shell commands and
Python (they are told the exact interpreter, e.g. `C:\tahoe\.venv\Scripts\python.exe`). Refused outright: delete,
kill, sudo, git, package installs (pip, `python -m pip`, conda, apt), network tools (curl, wget, ssh) and similar.
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
program. Keep `tahoe_mtap_gankyrin.py` next to it (and `tahoe_atlas.py` for the agents).

```bash
python3 tahoe_gene_panel.py check                                # preflight: data, genes, TP53 annotation, earlier run, disk
nohup python3 tahoe_gene_panel.py all > /dev/null 2>&1 &         # extract + analyze + bundle
tail -f gene_panel/gene_panel.log
python3 tahoe_gene_panel.py all --limit-files 30 --out panel_trial   # optional quick trial first (separate folder)
```
```powershell
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py check
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py all       # leave the window open; log in gene_panel\gene_panel.log
```

| Step | What it does | Time (estimate) |
|---|---|---|
| `extract` | One pass over all cells: per-cell counts of the panel, anchor and context genes plus the S/G2M/proteasome modules (`gene_panel/cells/`, ~2.5 GB; resumable). | ~1 h, like the MTAP/Gankyrin extract (longer from a hard drive) |
| `analyze` | Corrected drug effects per gene, pathway scores, the p53 screens, loss and level screens, cell cycle, co-regulation, cross-links, positive controls, `summary.txt`, the agent briefs, and the bundle. | a few minutes (< 1 GB memory) |
| `agents` | One Claude agent per pathway (ferroptosis, pyroptosis, p53, napepld_trim72, crosslinks) plus an overview. | ~20-45 min |

What `analyze` does (all with the corrections above; `gene_panel/results/README_columns.txt` explains every file):
- **Expression.** Which lines express each gene. A line is left out of a gene's drug effects when it reads below 25%
  of the median line or below 1 CPM. Genes with fewer than 2 counts per well x line profile are flagged
  `low counts` and get no calls. TRIM72 is expected to be absent in cancer lines, and NLRP3, CASP5, AIM2 and IL1B to
  be near zero.
- **Drug effects.** Effects on every gene (`<GENE>_drug_summary.csv`, one row per drug; `..._by_dose.csv`). Every
  drug-dose carries its stress context: ISR, NRF2, UPR, heat-shock, interferon, NF-kB, p53 and cell-cycle scores,
  plus toxicity and shutdown flags. This shows, for example, whether CHAC1/SLC7A11/PTGS2 rise with or without a
  general ATF4 stress response.
- **p53.** TP53 status comes from the cell-line driver table (any TP53 row = altered). The analysis checks:
  - which drugs raise p53 targets more in TP53-wild-type than in altered lines in the same wells;
  - a genotype-blind functional p53 status per line, with its agreement with the annotation (AUC) and the
    discordant lines;
  - whether TP53-wild-type lines are depleted more.

  The library has no MDM2 inhibitor, so DNA-damaging drugs and antimetabolites are the expected activators.
- **Loss and level screens.** Lines that lost a gene (e.g. GSDME silencing) are tested for selective depletion
  (the MTAP-null screen) and for re-expression (e.g. DNMT inhibitors). For every gene, the analysis tests whether a
  line's baseline level predicts which lines a drug depletes (the Gankyrin test), raw and within lineage.
- **Cross-links to the earlier run** (read from `<data>/mtap_gankyrin`; `--prior DIR` or `--prior none`):
  - agreement of the well map, the MTAP-null calls and the MTAP/PSMD10 effects (identical when `--min-cells` is the
    same);
  - Gankyrin vs p53 and NRF2 activity;
  - MTAP/CDKN2A(ARF)-null vs p53 activity and the ferroptosis genes;
  - drugs that top both analyses.
- **Positive controls** (`positive_controls.csv`, summary section 3). Each expected effect is listed with its
  verdict:
  - DNA damage -> p53 targets (more in TP53-wild-type lines);
  - dimethyl fumarate -> NRF2 targets and HMOX1;
  - proteasome inhibitors -> proteasome and heat-shock genes;
  - ciclopirox -> TFRC;
  - decitabine / 5-azacytidine -> GSDME in silenced lines, and interferon genes;
  - antimitotics -> G2/M;
  - dinaciclib -> transcription drop.

Start with `gene_panel/results/summary.txt` (section 1 checks the artifacts and the agreement with the earlier run,
section 3 the positive controls), then upload `gene_panel/gene_panel_bundle.zip` to Claude to check the numbers
before any agent runs. Scope: mRNA 24 h after the drug. That means no protein, lipid peroxidation, iron, caspase or
gasdermin cleavage, and no death mode: the reports speak of a "ferroptosis-like signature" and label hypotheses.

Agents (after the check; same SDK, API key, options, refusal rules and log/cost behaviour as the atlas; log in
`gene_panel/agents.log`, reports in `gene_panel/reports/`). At most 6 agents x `--budget` (default $5) = $30;
typical use is well below.
```bash
python3 tahoe_gene_panel.py agents          # or --dry-run first; --angles p53,ferroptosis for a subset
```
```powershell
C:\tahoe\.venv\Scripts\python.exe tahoe_gene_panel.py agents
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

`python3 tests/run_smoke.py` (Windows: `C:\tahoe\.venv\Scripts\python.exe tests\run_smoke.py --workdir C:\tahoe\smoke`)
generates a small synthetic Tahoe-100M download with planted effects (well-position artifacts, a plate-2 DMSO
offset, MTAP-null lines, TP53-dependent p53 activation, NRF2 / ISR / iron / GSDME effects, toxic and shutdown drugs,
a failed well) and checks that every script recovers them. No API key is used. Details in `tests/README.md`.
