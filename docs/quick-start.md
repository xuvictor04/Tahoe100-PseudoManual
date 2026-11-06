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
the log; `tahoe stop` stops (finished stages are kept, and the next `tahoe run` continues from there).

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
| Tahoe-100M data | `~/Tahoe-100M` | `TAHOE_DATA=/path` or `--data` |
| Output | `<data>/tahoemap` | `TAHOE_OUT=/path` or `--out` |
| Python environment | `~/tahoe-venv` | `TAHOE_VENV=/path` |

Options go through `tahoe run` to `python -m tahoemap run` (all of them: `python -m tahoemap --help`):
`--offline` (no annotation downloads), `--dims 64` (vector space size), `--from STAGE` / `--to STAGE`, `--redo`,
`--tensor-dtype float16` (halves the 4.4 GB per-well tensor), `--no-well-tensor`, `--workers N`,
`--unreliable-plates plate13|none`, `--min-cells 30`.

## Windows

There is no `tahoe` wrapper; run the package directly from the repository folder in PowerShell:

```powershell
C:\tahoe\.venv\Scripts\python.exe -m pip install numpy pandas pyarrow scipy scikit-learn networkx psutil
C:\tahoe\.venv\Scripts\python.exe -m tahoemap run --data C:\tahoe\Tahoe-100M
C:\tahoe\.venv\Scripts\python.exe -m tahoemap gene MDM2 --data C:\tahoe\Tahoe-100M
```

(`--stream` needs `curl`, which ships with Windows 10 and later.)

## Resources

| | Time (4–8 cores) | Disk | Memory |
|---|---|---|---|
| build (local files) | 30–90 min | 17 GB | ~2.6 GB per worker |
| build (`--stream`) | 1.5–2.5 h (network-bound) | 17 GB | ~2.6 GB per worker |
| effects + tensor | 20–40 min | 0.7 GB + 6–8 GB | ~6 GB |
| tables … map | 15–30 min | ~1–2 GB (vault ~0.5 GB) | ~4 GB |

## Test it first (3–5 minutes, no download)

```bash
tahoe test             # synthetic Tahoe-100M with planted answers, the whole pipeline, and ~25 checks
```
