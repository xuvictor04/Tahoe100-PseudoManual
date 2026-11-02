# The atlas: every angle, with an agent at each endpoint


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

