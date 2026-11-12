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
tahoe similar Dexamethasone 5            # the drug-doses most like one drug-dose (its 50 nearest; --top all)
tahoe signature --up FKBP5,TSC22D3,PER1  # the drug-doses that mimic (or reverse) a gene signature, with a p
tahoe open             # the explorer in a browser; also where the map, the vault and the report are
```

`tahoe similar DRUG [DOSE] [--top N|all]` reads `embed/drug_similarity.parquet`: the cosine of the pooled signatures
and over the per-line contexts, the significant genes they share, the other drug-dose's classes and flags ('k of 50
shown'). Without DOSE: the drug's best dose. `tahoe signature --up A,B[,...] [--down C,D] [--top N|all] [--lines]`
(or `--up @FILE`, one name per line or comma-separated) scores each drug-dose by the mean z of the up genes minus the
down genes (each clipped at ±10; `atlas/effects/DD_z.npy`, else the drug_effects rows with z = 0 elsewhere, which the
output says). The p comes from 1,000 random gene sets of the same sizes matched by pooled-CPM decile (a stable seed);
rows are ranked by p, then score, 25 each way by default. About 5% of the drug-doses reach p ≤ 0.05 for a random
signature: there is no correction across the 1,132 drug-doses. `--lines` names the lines that show the 5 strongest
mimics most. Both work on an exported results folder too (tables only).

Open the explorer by opening `<output>/explorer/web/index.html` in a browser (next section). Open the vault in
Obsidian with *Open folder as vault* on `<output>/vault`, and the map by opening `<output>/map/gene_map.html` in a
browser.

## The explorer: search any gene

The explorer is a set of web pages over every result of the run. Type a gene (a symbol such as TRIM72, an alias
such as MG53, or an Ensembl id), a drug, a cell line or an organ in the search box. Every gene, drug, drug-dose and
cell line has a page:

- **A gene**: every one of the 1,132 drug-doses with its corrected fold change, z and q, sorted by z. A flagged row
  keeps its place and shows its flag in full (for TRIM72, its strongest raisers, Idarubicin 5 µM and
  Homoharringtonine, are listed with their alerts). Then the gene in each of the 50 cell lines, its correlations
  with every other gene, its partners and module, what probably acts on it and what it acts on, its baseline and
  every well.
- **A drug-dose**: the drug's raw corrected values for every gene (exact, as a CSV too), its quality checks, the
  cells left per line, and its wells.
- **A cell line**: its genetics, how each drug-dose affected its cell numbers, and every gene's line effect.

Nothing is capped and nothing is left out for a flag. Each value is the number the pipeline stored (fold change =
2 to the power of the stored log2 value, and labelled as computed). A short preview always says "k of N shown" and
links to all N. The vault notes, the map and the look-ups link to the same pages. [explorer.md](explorer.md)
explains the pages.

**Open it on the computer that made the run.** Double-click `<output>/explorer/web/index.html` (or `tahoe open`). It
reads the data folder next to it (`<output>/explorer/data`), so it needs no network. It needs a current Chrome,
Edge, Firefox or Safari.

**Publish it on GitHub** (optional; the pages become public). The pages go to GitHub Pages (the branch `site` of
the code repository); the large data files go to a second public repository, `Tahoe100-PseudoManual-data`. Then
anyone can open https://xuvictor04.github.io/Tahoe100-PseudoManual/.

```bash
tahoe export ~/tahoe-pub --explorer      # site/, data/ (hard links to the output's files), publish.sh, PUBLISH.md
bash ~/tahoe-pub/publish.sh              # uploads the data, then the pages (it asks for the GitHub sign-in)
```

`export --explorer` never uploads anything; `publish.sh` (Windows: `publish.ps1`) does. It pushes only to the branch
`main` of the data repository and to the branch `site` of the code repository: never to `results`, `finalized` or
the default branch. Two settings on github.com are needed once (`PUBLISH.md` in the export folder says the same):

1. **Create the data repository.** On github.com, click **New repository**. Name it `Tahoe100-PseudoManual-data`.
   Choose **Public**. Do not add a README, a license or a .gitignore. Click **Create repository**.
2. Run the upload (above). The first upload creates the branch `site`.
3. **Turn on GitHub Pages.** Open https://github.com/xuvictor04/Tahoe100-PseudoManual, click the **Settings** tab,
   then **Pages** in the left sidebar (under "Code and automation"). Under "Build and deployment", set **Source** to
   **Deploy from a branch**, choose the branch **site** and the folder **/ (root)**, and click **Save**.
4. Wait up to 10 minutes. The **Actions** tab shows "pages-build-deployment"; then Settings, Pages says "Your site is
   live at https://xuvictor04.github.io/Tahoe100-PseudoManual/".

After every later run: `tahoe run`, then `tahoe export ~/tahoe-pub --explorer --force` (only what changed is
replaced), then `bash ~/tahoe-pub/publish.sh`. The upload is about 5 GB of data (in parts of at most 1.5 GB, one
push each; a part that fails is resumed with `--from-part K`) and about 0.7 GB of pages. The pages are pinned to the
exact data commit, so they never mix data from two runs.

**Disk space for publishing.** The export folder needs more than the output's own explorer:

- The pages are copied (about 0.7 GB). The data files are hard links to the output's files, so they take no space
  at first.
- The upload adds every file it sends to a git folder (`data/.git` and `site/.git`), about 4.5 GB together. They
  stay after the upload. Once the pages are live, you can delete both folders; the next upload makes them again.
  The upload turns off git's automatic repack, so they never need that space twice.
- After the next `tahoe run`, the output has new explorer files, but the previous run's data stay on disk through
  the hard links (about 5.2 GB) until `export --explorer --force` replaces them.

`export --explorer` checks that the copies and the git folders fit on the disk before it writes anything.

**The data repository grows.** Each upload sends the whole data again (about 5 GB). GitHub keeps the replaced data
until its own clean-up, so the stored size of `Tahoe100-PseudoManual-data` can grow over several uploads (GitHub
recommends staying under 5 GB). If GitHub warns about its size, delete that repository on github.com (its Settings
tab, at the bottom) and create it again as in step 1, then upload. Until the new pages are live, the pages online
cannot load the per-gene and per-drug-dose data files; everything else on them keeps working. While the parts
upload, the branch `main` holds only part of the new data, but the pages online keep reading the previous data
commit by its id.

Nothing is left out of these answers because of a flag. A drug-dose with an artifact flag (toxic, transcription
drop, cell-cycle shift, like a neighbouring well, ...), a partner without the same sign in both halves of the
compounds (or a lineage pair, or a read-sharing copy), or a gene in the vector space only through flagged drug-doses
keeps its ranked place, marked `⚠` with the reason (e.g. `⚠ cell-cycle shift, explains ~60% of this change`); each
list says how many items carry an alert. Caveats are shown with their words, not as alerts: 'like a neighbouring well
(top dose)', 'translation inhibitor' and 'rise under a translation inhibitor' (a rise under a drug that stops protein
synthesis may be mRNA stabilisation). Each drug shows Tahoe's annotation and ChEMBL's side by side, with an alert
where they disagree. In the map, the **Spread** slider pulls the
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

`tahoe gene X` lists them too (PROBABLE DIRECTION, with how often the gene was tested when no arrow passed), and
`tahoe line`, `tahoe drug` and `tahoe pair` show theirs.

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

`tahoe update` fetches the newest code. On Windows, with the portable MinGit, that is
`& "C:\tahoe\mingit\cmd\git.exe" -C C:\tahoe\repo pull` (or `git -C C:\tahoe\repo pull` when git is on PATH).
Then `tahoe run` (Windows: the same `python -m tahoemap run --out ...` as before, from `C:\tahoe\repo`) redoes only
the stages whose method changed, and the stages after them. `tahoe` alone shows the plan first. **After this update**
(reference version 3, tables 7, embed 5, relations 5, graph 7, direction 6, validate 9, vault 9, map 11, explorer 4)
any output made before it, including one made before the explorer or the direction stage existed, redoes reference
and every stage after it: `next: reference -> tables -> embed -> relations -> graph -> direction -> validate -> vault
-> map -> explorer`. The build, the effects and the tensor are kept. The reference stage runs right after tensor
(build → effects → tensor → reference → tables → embed → relations → graph → direction → validate → vault → map →
explorer), because tables shows each drug's ChEMBL annotation. About 45–60 minutes on the full data (the explorer
alone about 15–25 minutes, embed with ~6.8 GB of memory), plus the first ChEMBL and Compara downloads (below: up to
about 40 minutes on a slow link). When only the explorer's page files changed in an update, `tahoe run` copies just
those (seconds). The vault keeps your
Obsidian settings; in its graph view the new note *Probable direction*, which every gene note links, shows as a hub
until you add `-file:"Probable direction"` to the graph's filter (a new vault has it).

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
`--offline` (no annotation downloads), `--dims 64` (vector space size), `--from STAGE` / `--to STAGE`, `--redo`
(every stage again; the build then sums every plate again), `--tensor-dtype float16` (halves the 4.4 GB per-well
tensor), `--no-well-tensor`, `--workers N`, `--unreliable-plates plate13|none`, `--min-cells 30`. For the explorer:
`--site-url URL` (where it is published; the validation report, the vault, the map and the look-ups link there;
default `https://<owner>.github.io/<repo>/` of this code's GitHub repository; `none` for no site), `--data-url URL`,
`--with-line-dd` (also every gene's per-line values per drug-dose, about 4.3 GB more), `--pages-max-mb 905` (in MiB
of 1,048,576 bytes: 905 MiB is 0.949 GB, about 50 MB below GitHub Pages' 1 GB limit; above it, parts of the pages
move to the data folder; nothing is dropped). Look-ups take `--top N` or `--top all`.

The options that change results (`--dims`, `--min-active`, `--min-responsive`, `--min-cells`,
`--unreliable-plates`, `--layout`, `--tensor-dtype`, `--no-well-tensor`, `--site-url`, `--data-url`,
`--with-line-dd`, `--with-pooled-r`) are remembered for the output folder: a
later `tahoe run` without them keeps them, and giving one with another value redoes the stage it belongs to and every
stage after it (`tahoe` says which stage is out of date and why). The public annotations are downloaded once and
cached; a source that failed to download is retried by the next `tahoe run` with network (`--offline` keeps the run
as it is), and `tahoe run --from reference` (or `tahoe run --refresh-reference`, which downloads even what is cached)
fetches them again and redoes the stages that use them: since reference runs before tables, that is tables, embed and
every later stage.

The reference stage downloads, the first time: HGNC, the Ensembl r112 GTF, UniProt, NCBI, Reactome, Hallmark and
STRING (~200 MB, ~3 min); each drug's ChEMBL record (www.ebi.ac.uk web services: about 52 requests for the 379
drugs, 2.5 to 10 minutes depending on how fast the EBI server answers, one log line per request; a few MB, cached in
`reference/downloads/chembl_drugs.json`); and the Ensembl Compara paralogues (ftp.ensembl.org, a ~140 MB file
streamed; only the human paralogue rows are kept, in `reference/downloads/compara_human_paralogues.tsv.gz`). The
Compara time depends on the link to ftp.ensembl.org: about 2 minutes on a fast link, up to about 30 minutes at the
speed the PC's own GTF download showed (55.5 MB in 12 minutes); it logs its progress every 10 MB, and a dropped
connection starts the file again (up to 4 tries). Later runs use the cache. If PubChem cannot be reached, ChEMBL
matches the drugs by name only; `reference/sources.json` then says 'failed (PubChem not reached ...)' for ChEMBL, each
drug's note says so, and the next run with network fetches ChEMBL again. Offline without the cache, the drug
classes come from the code constants only (every drug reads 'ChEMBL not loaded') and the paralogue table is not
written.

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
C:\tahoe\.venv\Scripts\python.exe -m tahoemap similar Dexamethasone 5 --out C:\tahoe\out
C:\tahoe\.venv\Scripts\python.exe -m tahoemap signature --up "@C:\tahoe\genes.txt" --out C:\tahoe\out
Start-Process C:\tahoe\out\explorer\web\index.html     # the explorer, in the default browser
```

To check the install first (about 7 minutes, synthetic data, no download), from `C:\tahoe\repo`:

```powershell
C:\tahoe\.venv\Scripts\python.exe tests\run_tests.py --workdir C:\tahoe\test
C:\tahoe\.venv\Scripts\python.exe tests\test_port.py
C:\tahoe\.venv\Scripts\python.exe tests\test_windows.py
C:\tahoe\.venv\Scripts\python.exe tests\test_review.py --out C:\tahoe\test\out_seed0   # the review agents, fake API
```

- `run_tests.py` (about 7 minutes) should end with "168 passed, 9 warnings, 0 failed" when Playwright is not
  installed, or "193 passed, 1 warnings, 0 failed" with it (the one warning with Playwright: the 'lowered by mTOR
  inhibitors' module label, a planted effect below what its rule can call on seed 0); `test_review.py` (a few
  minutes, offline, no key) with "0 failed". It works in a folder of its own in the temp folder and only reads
  `--out`.
- The warnings say the browser checks were skipped: those checks open the map and the explorer in a headless
  browser and need Playwright. They are optional. To include them, run
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
- A gene list for `signature --up @FILE` can be written by PowerShell (`>` writes UTF-16) or Notepad: both read
  as plain names.
- Downloads (the reference stage: HGNC, Ensembl, UniProt, NCBI, Reactome, STRING, ChEMBL, Compara ...) are verified by Windows
  itself through `truststore` when it is installed; `requirements.txt` installs it on Windows. Without it, Python on
  Windows cannot verify some servers' certificates (Ensembl's and NCBI's, whose root certificate Windows adds to its
  store only when one of its own programs first needs it) and those sources fail with "certificate verify failed".
  If that happens: `C:\tahoe\.venv\Scripts\python.exe -m pip install truststore`, then
  `C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --out C:\tahoe\out` retries the failed sources. On a
  network that inspects HTTPS, the inspecting certificate must be trusted by the computer.

The explorer is `C:\tahoe\out\explorer\web\index.html` (double-click it), the vault `C:\tahoe\out\vault` and the map
`C:\tahoe\out\map\gene_map.html`. `--stream` reads Tahoe-100M from
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
per-line arrays, the downloads or API-key records, and it refuses while a run works on the output. A few text files
name the folders of your computer (the stage records, `reference/sources.json`, `run.log`, the vault's `Home.md`):
their copies say `<out>` (the output folder), `<data>` (the data folder) and `<cache>` (the reference cache)
instead, and the export's `README.md` lists them; the files in the output folder are not changed.

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

### The explorer on Windows

The explorer is published separately (the pages and a data repository; see "The explorer: search any gene" above for
the two one-time settings on github.com). From `C:\tahoe\repo`, with python.exe from the venv and a portable MinGit
that is not on PATH:

```powershell
C:\tahoe\.venv\Scripts\python.exe -m tahoemap export C:\tahoe\pub --explorer --out C:\tahoe\out
$env:TAHOE_GIT = "C:\tahoe\mingit\cmd\git.exe"      # only when git is not on PATH (the export also finds this one)
powershell -ExecutionPolicy Bypass -File C:\tahoe\pub\publish.ps1
```

`export --explorer` writes `C:\tahoe\pub\site` (the pages), `C:\tahoe\pub\data` (hard links to the output's files),
the upload lists, `publish.ps1` and `PUBLISH.md`. It checks first that the explorer is up to
date and that every file and every upload fits GitHub's limits; it never uploads. `publish.ps1` uploads the data
(about 5 GB, in parts of at most 1.5 GB), pins the pages to that data commit, then uploads the pages (about 0.7 GB).
If a part fails (network, sign-in), run it again from that part, for example
`powershell -ExecutionPolicy Bypass -File C:\tahoe\pub\publish.ps1 -FromPart 2`; `PUBLISH.md` gives the number that
uploads only the pages. The upload leaves git copies of the files in `C:\tahoe\pub\data\.git` and
`C:\tahoe\pub\site\.git` (about 4.5 GB; see "Disk space for publishing" above). After every later run (from
`C:\tahoe\repo`; add `--data C:\tahoe\Tahoe-100M` to `run` when the output was built from a local copy):

```powershell
C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --out C:\tahoe\out
C:\tahoe\.venv\Scripts\python.exe -m tahoemap export C:\tahoe\pub --explorer --force --out C:\tahoe\out
powershell -ExecutionPolicy Bypass -File C:\tahoe\pub\publish.ps1
```

## Resources

Measured on the full data (95.6M cells) on a 4-core machine with 15 GB of memory. The direction stage was measured
on the user's PC at direction version 2 (the code of d523eae: 3.3 min, peak 1.7 GB); version 6 adds tests and is
estimated at about 6 minutes. The vault was measured there too (34,281 notes, 0.73 GB); the newer gene notes add about
a fifth. The explorer's figures are estimates from generated outputs of the full size (it has not yet run on the real
data):

| Stage | Time | Disk it adds | Peak memory |
|---|---|---|---|
| build, `--stream` | ~95 min with 4 workers at ~90 MB/s (network-bound) | 20 GB | ~2.6–3 GB per worker |
| build, local files | faster than streaming (disk-bound); one worker per plate | 20 GB | ~2.6–3 GB per worker |
| effects | 10 min | 0.7 GB | 4.6 GB |
| tensor | 9 min | 3.7 GB, plus 4.4 GB for the per-well tensor (2.2 GB with `--tensor-dtype float16`, none with `--no-well-tensor`) | ~3 GB |
| reference (now right after tensor) | ~3 min the first time (downloads ~200 MB), plus ChEMBL (2.5–10 min, a few MB) and the Compara paralogues (~140 MB streamed: ~2 min on a fast link, up to ~30 min on a slow one); seconds after | 0.2 GB | ~1 GB |
| tables, embed | 2 + 2 min | < 0.1 GB | 6.8 GB (embed) |
| relations, graph, validate | 1 + 2 + 1 min | 0.15 GB | ~3 GB |
| direction | 3.3 min measured at version 2 (PC); ~6 min estimated at version 6 | < 0.1 GB | 1.7 GB measured at version 2 |
| vault, map | 2 min + seconds | about 0.9 GB (0.73 GB measured on the PC for 34,281 notes at an earlier vault version, plus about 22% for the newer gene-note sections), about 26 MB for the map (nothing is left out to make it smaller; the stage warns above 25 MB) | ~1.5 GB, plus up to ~1 GB to read the direction arrows (estimated) |
| explorer | ~15–25 min (estimated) | ~5.9 GB: pages about 0.73 GB, data 5.2 GB (+4.3 GB with `--with-line-dd`); the stage first checks for 1.3 times its estimate (about 5.4 GB), so it needs about 7 GB free | ~2.5–3 GB (estimated; the per-line tensor is read in blocks, so the peak the stage reports is the memory it really uses) |
| publishing the explorer (optional) | upload time | ~5.2 GB in the export folder: the page copies (0.73 GB) and the upload's git copies (~4.5 GB, which can be deleted once the pages are live); plus ~5.2 GB for a while after a later run (the previous run's data, kept by the hard links until `export --explorer --force`) | small |

So: about 36 GB of disk in all and ~1 hour after the build; about 41 GB with the published explorer, and up to
about 47 GB between a later `run` and its `export --explorer --force`. Build workers are sized from free memory; if one
is killed for lack of memory the build stops and says so (finished plates are kept): rerun with fewer `--workers`.

## Test it first (about 7 minutes, no download)

```bash
tahoe test             # synthetic Tahoe-100M with planted answers, the whole pipeline, and 194 checks
```
