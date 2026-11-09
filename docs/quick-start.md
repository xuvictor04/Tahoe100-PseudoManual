# Quick start

## Linux / macOS

```bash
git clone -b finalized https://github.com/xuvictor04/Tahoe100-PseudoManual ~/tahoemap-repo
~/tahoemap-repo/tahoe setup        # Python environment ~/tahoe-venv and the `tahoe` command on your PATH
```

Then one of:

```bash
tahoe run --stream     # no download: reads Tahoe-100M from Hugging Face one file at a time (~17 GB of disk)
# or
tahoe download         # ~340 GB into ~/Tahoe-100M (expression files + the 4 small metadata tables; resumes)
tahoe run              # then everything, from the local files
```

`tahoe run` works in the background (safe to log out). `tahoe` alone says where things stand; `tahoe log` follows
the log; `tahoe stop` stops (finished stages and finished plates of the build are kept, and the next `tahoe run`
continues from there; a streamed build keeps streaming, so `tahoe run` and `tahoe run --stream` do the same). A
local build first checks that the download is complete and names the missing files if not (`tahoe download`
resumes it; `--allow-partial` builds from what is there).

When it is done:

```bash
tahoe gene MDM2        # drugs that raise / lower MDM2, in which cell lines, genes that move with / opposite it
tahoe drug Bortezomib  # what a drug does, at each dose, and which drugs act alike
tahoe line A549        # what is special about a cell line
tahoe pair MDM2 CDKN1A # how two genes relate, and under which drugs
tahoe module 12        # one module of the nodal map
tahoe open             # where the HTML map, the Obsidian vault and the validation report are
```

Open the vault in Obsidian with *Open folder as vault* on `<output>/vault`, and the map by opening
`<output>/map/gene_map.html` in a browser.

Nothing is left out of these answers because of a flag. A drug-dose with an artifact flag (toxic, transcription
drop, cell-cycle shift, ...), a partner not replicated in both halves of the compounds, or a gene in the vector space
only through flagged drug-doses keeps its ranked place, marked `⚠` with the reason (e.g. `⚠ cell-cycle shift, explains
~60% of this change`); each list says how many items carry an alert. In the map, the **Spread** slider pulls the
modules apart, the **k-D tour** tab turns the vectors through all dimensions, and the neighbourhood view goes to
depth 4 (its help panel explains every control).

**Which gene probably acts on which.** The direction stage adds arrows SOURCE → TARGET: from the cell lines' recorded
mutations and, without any known mutation, from lines that do not express a gene, from drugs that target a gene and
from genes' natural levels. Each arrow has a grade (A strong, B read its alerts, C a glimpse) and says whether the
source's activity raises or lowers the target (for a drug response: strengthens or weakens it, in the target's own
direction). You find them in a gene note's **Direction (probable)** section
(upstream and downstream of the gene), in drug and cell-line notes, in the map's side panel and as arrows in its
neighbourhood view, and in `validation/report.md`. They are a probable direction, from cell lines: not proof of direct
regulation. [direction.md](direction.md) explains how to read them.

`tahoe gene X` lists them too (PROBABLE DIRECTION), and `tahoe line`, `tahoe drug` and `tahoe pair` show theirs.

## Literature review by AI agents (optional)

With an Anthropic API key, `tahoe review` has an agent review genes, drugs and cell lines against the literature and
puts its cited reviews into the vault and the map. It costs money (about a dollar an entity with the default model;
~15,000 genes), so look first, then start small, best on a copy of the finished run:

```bash
read -rs ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY   # paste the key (not echoed); or --keys-file FILE
tahoe duplicate ~/tm/review1               # a copy of the output (big arrays hard-linked); then --out ~/tm/review1
tahoe review plan --out ~/tm/review1       # the queue and its projected cost
tahoe review run --out ~/tm/review1 --limit 20          # in the foreground: Ctrl-C pauses, rerun resumes
tahoe review status --out ~/tm/review1     # real cost per entity, spend, what the rest would cost
tahoe vault --out ~/tm/review1; tahoe map --out ~/tm/review1
```

[review.md](review.md) has the details: the agents and how to edit them, costs and caps, keys and what happens when
credit runs out, histories, verification, and Windows.

## Already ran the earlier `tahoe_atlas.py`?

Its build (the one long pass over all cells) can be reused, which saves the 1–2 hour build:

```bash
tahoe run --reuse-atlas ~/Tahoe-100M/atlas
```

## After an update of the code

`tahoe update` (Windows: `git -C C:\tahoe\repo pull`) fetches the newest code; then `tahoe run` (Windows: the same
`python -m tahoemap run --out ...` as before) redoes only the stages whose method changed, and the stages after them.
`tahoe` alone shows the plan first. An output that finished before the **direction** stage existed runs `direction`,
`validate`, `vault` and `map`, and also any earlier stage whose method changed since the output was made (the plan says
which and why: an output made with older code, for example, may also redo `tables`, `embed`, `reference`,
`relations` and `graph`: about 15–25 minutes in all on the full data, with embed's ~6.8 GB of memory). The build, the effects and the tensor are kept unless the plan names them. The vault keeps your Obsidian
settings; in its graph view the new note *Probable direction*, which every gene note links, shows as a hub until you add
`-file:"Probable direction"` to the graph's filter (a new vault has it).

## Folders and options

| Setting | Default | Change with |
|---|---|---|
| Tahoe-100M data | `~/Tahoe-100M` | `--data /path` on any `tahoe` command, or `TAHOE_DATA=/path` |
| Output | `<data>/tahoemap` | `--out /path` on any `tahoe` command, or `TAHOE_OUT=/path` |
| Python environment | `~/tahoe-venv` | `TAHOE_VENV=/path` |

`--data` / `--out` choose the folders of that one command, so give the same ones to every command on that run
(`tahoe run --out /big/tm`, then `tahoe --out /big/tm`, `tahoe stop --out /big/tm`, `tahoe gene MDM2 --out /big/tm`);
the environment variables set them once for the session.

Options go through `tahoe run` to `python -m tahoemap run` (all of them: `python -m tahoemap --help`):
`--offline` (no annotation downloads), `--dims 64` (vector space size), `--from STAGE` / `--to STAGE`, `--redo`,
`--tensor-dtype float16` (halves the 4.4 GB per-well tensor), `--no-well-tensor`, `--workers N`,
`--unreliable-plates plate13|none`, `--min-cells 30`.

The options that change results (`--dims`, `--min-active`, `--min-responsive`, `--min-cells`,
`--unreliable-plates`, `--layout`, `--tensor-dtype`, `--no-well-tensor`) are remembered for the output folder: a
later `tahoe run` without them keeps them, and giving one with another value redoes the stage it belongs to and every
stage after it (`tahoe` says which stage is out of date and why). The public annotations are downloaded once and
cached; a source that failed to download is retried by the next `tahoe run` with network (`--offline` keeps the run
as it is), and `tahoe run --from reference` (or `tahoe run --refresh-reference`, which downloads even what is cached)
fetches them again and redoes the stages that use them, the vault included.

## Windows

There is no `tahoe` wrapper; run the package with Python in PowerShell. It needs Python 3.10 or newer
(python.org; tick *Add python.exe to PATH*) and Git (git-scm.com):

```powershell
git clone -b finalized https://github.com/xuvictor04/Tahoe100-PseudoManual C:\tahoe\repo
cd C:\tahoe\repo
python -m venv C:\tahoe\.venv
C:\tahoe\.venv\Scripts\python.exe -m pip install -r requirements.txt
C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --stream --out C:\tahoe\out
```

The run works in this window (keep it open; the computer is kept awake): Ctrl-C stops it, and the same command
continues from the finished stages. A run started with `Start-Process -PassThru` (say with its output redirected to
files) is stopped with `Stop-Process -Id <its Id>`: the build's worker processes and their downloads end with it.
One computing command at a time per output folder: a second `run` (or stage) on the same `--out` refuses while the
first, or a worker process it left running, is alive (`C:\tahoe\out\.pipeline.lock`; the message says how to end
a leftover worker: `taskkill /T /F /PID <pid>`). Then, from `C:\tahoe\repo`, with the same `--out`:

```powershell
C:\tahoe\.venv\Scripts\python.exe -m tahoemap status --out C:\tahoe\out
C:\tahoe\.venv\Scripts\python.exe -m tahoemap gene MDM2 --out C:\tahoe\out
```

To check the install first (about 5 minutes, synthetic data, no download), from `C:\tahoe\repo`:

```powershell
C:\tahoe\.venv\Scripts\python.exe tests\run_tests.py --workdir C:\tahoe\test
C:\tahoe\.venv\Scripts\python.exe tests\test_port.py
C:\tahoe\.venv\Scripts\python.exe tests\test_windows.py
C:\tahoe\.venv\Scripts\python.exe tests\test_review.py --out C:\tahoe\test\out_seed0   # the review agents, fake API
```

- `run_tests.py` should end with "49 passed, 0 warnings, 0 failed"; `test_review.py` (a few minutes, offline, no
  key) with "0 failed". It works in a folder of its own in the temp folder and only reads `--out`.
- The one warning you may see is "browser check skipped": that check opens the map in a headless browser and
  needs Playwright. It is optional. To include it, run
  `C:\tahoe\.venv\Scripts\python.exe -m pip install playwright`, then
  `C:\tahoe\.venv\Scripts\python.exe -m playwright install chromium`.
- `test_port.py` (and `duplicate --repo`, and the code commit recorded with each literature review) needs git. If
  git is not on PATH (for example a portable MinGit), put its `cmd` folder on PATH or set
  `$env:TAHOE_GIT = "C:\path\to\git.exe"` first.
- Windows cannot replace a file that another program has open. Before running a stage again on an output, close
  what reads it: a look-up or a notebook, Excel with one of its CSV files, a literature review run on it (or on a
  duplicate of it, whose big arrays are the same files). Otherwise the stage stops with "Cannot replace (or write)
  ...: another program has it open"; nothing is lost, and the same command runs it again.
- With Windows Smart App Control on, Windows may block a library file the first time Python loads it ("An
  Application Control policy has blocked this file"). Running the same command again usually works. A stopped
  run continues from its finished stages.
- Downloads (the reference stage: HGNC, Ensembl, UniProt, NCBI, Reactome, STRING ...) are verified by Windows
  itself through `truststore` when it is installed; `requirements.txt` installs it on Windows. Without it, Python on
  Windows cannot verify some servers' certificates (Ensembl's and NCBI's, whose root certificate Windows adds to its
  store only when one of its own programs first needs it) and those sources fail with "certificate verify failed".
  If that happens: `C:\tahoe\.venv\Scripts\python.exe -m pip install truststore`, then
  `C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --out C:\tahoe\out` retries the failed sources. On a
  network that inspects HTTPS, the inspecting certificate must be trusted by the computer.

The vault is `C:\tahoe\out\vault` and the map `C:\tahoe\out\map\gene_map.html`. `--stream` reads Tahoe-100M from
Hugging Face with `curl`, which ships with Windows 10 and later. To work from a local copy instead (~340 GB):

```powershell
C:\tahoe\.venv\Scripts\hf.exe download tahoebio/Tahoe-100M --repo-type dataset --local-dir C:\tahoe\Tahoe-100M `
  --include "data/*.parquet" --include "metadata/gene_metadata.parquet" --include "metadata/sample_metadata.parquet" `
  --include "metadata/cell_line_metadata.parquet" --include "metadata/drug_metadata.parquet"
C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --data C:\tahoe\Tahoe-100M --out C:\tahoe\out
```

## Put the results on GitHub

`export` copies the shareable results of a finished run into a new folder, ready to be committed and pushed as a
branch of its own: the vault, the map, the tables, the validation report, the probable directions (`direction/`), the
graph, the relations, the vector space, the stage records, the derived reference tables and any literature reviews,
with a `README.md` (what each folder
holds, the code version and commit, the date, the sizes, what was left out and why), a `MANIFEST.tsv` (size and
sha256 of every file) and a `.gitattributes` that stops git from changing line ends. It never copies the build, the
per-line arrays, the downloads or API-key records, and it refuses while a run works on the output.

- **GitHub refuses files over 100 MB.** A file over 95 MiB is not copied; the command and `README.md` list it (use
  Git LFS or a GitHub release for it). GitHub also refuses one push over 2 GB: when the total is larger, the
  command says so; commit and push in parts (e.g. `vault` first, then the rest).
- **The repository is public, so the results become public** once pushed. Push to a private repository of your own
  if they should not be.
- **Pushing needs a GitHub sign-in.** The first `git push` asks for it: Git Credential Manager (part of Git for
  Windows) opens a GitHub sign-in window or browser page; sign in with an account that may write to the repository.
  If no sign-in appears and the push fails with an authentication error, the git in use has no credential manager:
  install Git for Windows (git-scm.com), or give a GitHub personal access token as the password. Git also needs a
  name and e-mail for the commit (`git config user.name` / `user.email`, below).

Linux / macOS:

```bash
tahoe export ~/tahoe-results                 # add --out /path if your output is not the default
cd ~/tahoe-results
git init
git checkout --orphan results               # a branch that holds only the results, no code history
git config user.name "Your Name"; git config user.email "you@example.com"
git add -A
git commit -m "tahoemap results"
git remote add origin https://github.com/xuvictor04/Tahoe100-PseudoManual.git
git push -u origin results
```

Windows (PowerShell, from `C:\tahoe\repo`; with a portable MinGit in `C:\tahoe\mingit`, else use `git` from PATH):

```powershell
C:\tahoe\.venv\Scripts\python.exe -m tahoemap export C:\tahoe\results --out C:\tahoe\out
cd C:\tahoe\results
$git = "C:\tahoe\mingit\cmd\git.exe"
& $git init
& $git checkout --orphan results
& $git config core.longpaths true          # vault paths can pass Windows' 260-character limit
& $git config user.name "Your Name"
& $git config user.email "you@example.com"
& $git add -A
& $git commit -m "tahoemap results"
& $git remote add origin https://github.com/xuvictor04/Tahoe100-PseudoManual.git
& $git push -u origin results
```

To update the branch after a new run: `export` again into the same folder with `--force` (it replaces only the files
its earlier export wrote, and copies only what changed), then `git add -A`, `git commit -m "..."` and `git push`.
The command itself prints these next steps with your folder in them.

## Resources

Measured on the full data (95.6M cells) on a 4-core machine with 15 GB of memory (the direction stage, and what it
adds to the vault and the map, are estimates: they were measured on generated outputs of the full size, because the
stage has not yet run on the real data):

| Stage | Time | Disk it adds | Peak memory |
|---|---|---|---|
| build, `--stream` | ~95 min with 4 workers at ~90 MB/s (network-bound) | 20 GB | ~2.6–3 GB per worker |
| build, local files | faster than streaming (disk-bound); one worker per plate | 20 GB | ~2.6–3 GB per worker |
| effects | 10 min | 0.7 GB | 4.6 GB |
| tensor | 9 min | 3.7 GB, plus 4.4 GB for the per-well tensor (2.2 GB with `--tensor-dtype float16`, none with `--no-well-tensor`) | ~3 GB |
| tables, embed | 2 + 2 min | < 0.1 GB | 6.8 GB (embed) |
| reference | ~3 min the first time (downloads ~200 MB), seconds after | 0.2 GB | ~1 GB |
| relations, graph, validate | 1 + 2 + 1 min | 0.15 GB | ~3 GB |
| direction | ~6–7 min (estimated) | < 0.1 GB | 1.3–1.8 GB (estimated) |
| vault, map | 2 min + seconds | 0.6 GB (35,000 notes; the direction sections add ~0.06 GB), 10 MB (~17–19 MB with the direction arrows; a page that would pass 20 MB first leaves out the grade C readings) | ~1.5 GB, plus up to ~1 GB to read the direction arrows (estimated) |

So: about 30 GB of disk in all and ~40 minutes after the build. Build workers are sized from free memory; if one
is killed for lack of memory the build stops and says so (finished plates are kept): rerun with fewer `--workers`.

## Test it first (3–5 minutes, no download)

```bash
tahoe test             # synthetic Tahoe-100M with planted answers, the whole pipeline, and 49 checks
```
