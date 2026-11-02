# Tahoe-100M pseudo-manual

Tools for mining [Tahoe-100M](https://huggingface.co/datasets/tahoebio/Tahoe-100M) — 50 pooled cancer cell
lines × 379 drugs × 3 doses, single-cell mRNA at 24 h — plus one full study built on it.

Copy this folder's files into your Tahoe-100M download folder (default `~/Tahoe-100M`; on Windows
`C:\tahoe\Tahoe-100M`) and run them from there. On Linux / macOS the `tahoe` command needs no copying.
Replace older copies too: `tahoe_atlas.py` and `tahoe_gene_panel.py` need the current
`tahoe_mtap_gankyrin.py`, and the panel needs the current `tahoe_atlas.py`.

**The method is v3.** Outputs made before v3 show in `tahoe status` as `done, but outdated (method v3)`.
`tahoe update`, then `tahoe run`, redoes only what v3 needs — minutes, and the ~96M cells are not read again.
See [docs/method-v3.md](docs/method-v3.md).

## Where everything is

| Path | What it is |
|---|---|
| **[docs/quick-start.md](docs/quick-start.md)** | **start here** — install, download, run |
| [docs/method-v3.md](docs/method-v3.md) | what v3 changed in the method and why the numbers moved |
| [docs/setup.md](docs/setup.md) | disk, memory and time needed |
| [docs/atlas.md](docs/atlas.md) | `tahoe_atlas.py` — aggregate the whole dataset into one package per angle, then one agent per angle |
| [docs/gene-panel.md](docs/gene-panel.md) | `tahoe_gene_panel.py` — the MTAP/Gankyrin method applied to ferroptosis, pyroptosis, p53, NAPEPLD, TRIM72, ABCB1/ABCG2 |
| [docs/mtap-gankyrin.md](docs/mtap-gankyrin.md) | the earlier MTAP / Gankyrin trial |
| [docs/tests.md](docs/tests.md) | the test suite |
| **[mg53_p53/](mg53_p53/)** | **the MG53 / p53 study** — a nine-step pipeline and its findings. See [mg53_p53/README.md](mg53_p53/README.md) |
| **[knowledge/](knowledge/)** | **the Obsidian knowledge base** — concepts, per-gene notes, findings, methods. See [knowledge/README.md](knowledge/README.md) |
| [tests/](tests/) | synthetic-data smoke tests |
| [trim72_idarubicin/](trim72_idarubicin/) | a small independent cross-check of one drug-dose, kept because the pipeline's per-line numbers are validated against it |

## The two things in this repository

**1. The tools.** `tahoe_atlas.py` computes once over the whole dataset and pre-digests it into a data
package per angle (genes, drugs, classes, cell lines, biomarkers, programs, cell state, …); an agent per
angle then writes a report. `tahoe_gene_panel.py` applies the same method to named gene sets.
`tahoe_status.py` tells you what has been computed and what is outdated. `tahoe` is the command wrapper.

These live at the top level on purpose: they are imported by path and by name from many places
(`import tahoe_gene_panel as P`), so moving them would break the pipeline.

**2. The MG53 / p53 study** in [mg53_p53/](mg53_p53/). Nine steps, each a script plus its committed output
tables, asking what raises or lowers MG53 (TRIM72) expression and what MG53's level does to p53 and p53's
output. The committed `*/tables/*.csv` are the **regression reference**: a fresh run compares itself against
them and reports identical / close / differs per table. The write-ups are in
[mg53_p53/findings/](mg53_p53/findings/).

## Scope note for the MG53 / p53 study

"Upstream" and "downstream" are always **regulatory**, never positional. Upstream of MG53 = what raises or
lowers its expression. Downstream of MG53 = what its level does to p53 and p53's output.

TRIM72 sits 10.6 kb 3′ of PYCARD-AS1 and 17 kb 3′ of FUS **on the same strand**, so transcription running
past those genes is counted as TRIM72 mRNA. That is called **readthrough spillover** and never "downstream";
chromosomal position is written "3′ of" or "5′ of".
