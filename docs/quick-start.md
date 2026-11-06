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

## Already ran the earlier `tahoe_atlas.py`?

Its build (the one long pass over all cells) can be reused, which saves the 1–2 hour build:

```bash
tahoe run --reuse-atlas ~/Tahoe-100M/atlas
```

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
continues from the finished stages. Then, from `C:\tahoe\repo`, with the same `--out`:

```powershell
C:\tahoe\.venv\Scripts\python.exe -m tahoemap status --out C:\tahoe\out
C:\tahoe\.venv\Scripts\python.exe -m tahoemap gene MDM2 --out C:\tahoe\out
```

The vault is `C:\tahoe\out\vault` and the map `C:\tahoe\out\map\gene_map.html`. `--stream` reads Tahoe-100M from
Hugging Face with `curl`, which ships with Windows 10 and later. To work from a local copy instead (~340 GB):

```powershell
C:\tahoe\.venv\Scripts\hf.exe download tahoebio/Tahoe-100M --repo-type dataset --local-dir C:\tahoe\Tahoe-100M `
  --include "data/*.parquet" --include "metadata/gene_metadata.parquet" --include "metadata/sample_metadata.parquet" `
  --include "metadata/cell_line_metadata.parquet" --include "metadata/drug_metadata.parquet"
C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --data C:\tahoe\Tahoe-100M --out C:\tahoe\out
```

## Resources

Measured on the full data (95.6M cells) on a 4-core machine with 15 GB of memory:

| Stage | Time | Disk it adds | Peak memory |
|---|---|---|---|
| build, `--stream` | ~95 min with 4 workers at ~90 MB/s (network-bound) | 20 GB | ~2.6–3 GB per worker |
| build, local files | faster than streaming (disk-bound); one worker per plate | 20 GB | ~2.6–3 GB per worker |
| effects | 10 min | 0.7 GB | 4.6 GB |
| tensor | 9 min | 3.7 GB, plus 4.4 GB for the per-well tensor (2.2 GB with `--tensor-dtype float16`, none with `--no-well-tensor`) | ~3 GB |
| tables, embed | 2 + 2 min | < 0.1 GB | 6.8 GB (embed) |
| reference | ~3 min the first time (downloads ~200 MB), seconds after | 0.2 GB | ~1 GB |
| relations, graph, validate | 1 + 2 + 1 min | 0.15 GB | ~3 GB |
| vault, map | 2 min + seconds | 0.6 GB (35,000 notes), 10 MB | ~1.5 GB |

So: about 30 GB of disk in all and ~30 minutes after the build. Build workers are sized from free memory; if one
is killed for lack of memory the build stops and says so (finished plates are kept): rerun with fewer `--workers`.

## Test it first (3–5 minutes, no download)

```bash
tahoe test             # synthetic Tahoe-100M with planted answers, the whole pipeline, and ~25 checks
```
