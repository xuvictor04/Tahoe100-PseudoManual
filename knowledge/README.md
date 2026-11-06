# The MG53 / p53 knowledge base

An [Obsidian](https://obsidian.md) vault. Open this folder — `knowledge/` — as a vault and start at
`00-Index/Home.md`.

It is deliberately independent of the code and the pipeline output next to it: nothing here is imported by
any script, and nothing here is needed to run anything. It exists so that what was *learned* survives
separately from what was *computed*.

## What is in it

| Folder | What it holds |
|---|---|
| `00-Index/` | `Home.md` and the maps of content. Start here. |
| `10-Concepts/` | The biology and the measurement ideas the work rests on — each explained once, linked everywhere. |
| `20-Genes/` | One note per gene the study touches — 343 of them, in 14 subfolders by **what the gene's relation is**, so the file explorer reads as the pathway does. See `00-Index/Genes by relation.md`. |
| `30-Findings/` | What the study concluded, and how much of it survived its own controls. Includes `Corrections and retractions.md`. |
| `40-Methods/` | How each number was produced and the nulls it was tested against. |
| `50-Data/` | What each table in the repository holds. The vault links to the real CSVs rather than copying them. |
| `60-Literature/` | Reading notes and the papers worth knowing. |
| `_build/` | Everything that is not a note: the generator, `annotations.json` (what HGNC, NCBI Gene and UniProt record for each gene, fetched and committed), `gene_universe.csv`, and `gene_knowledge/` holding the written layer. Kept out of the note tree so a gene wikilink can never land on a raw fragment. |

## Two layers, and only one of them is generated

A gene note has a **generated** part and a **written** part, and keeping them apart is the point.

- **Generated** — the frontmatter and the whole "In this dataset" block, rebuilt from the study's tables by
  `_build/build_vault.py` on every run. Always consistent with the data; never hand-edited, because an edit
  would be overwritten.
- **Written** — the prose about what a gene *is*, kept in `_build/gene_knowledge/<SYMBOL>.md` and spliced in.
  Survives every rebuild.

So, to add knowledge about MDM2, write `_build/gene_knowledge/MDM2.md` and rebuild. To change how every gene
note looks, edit the generator. See `00-Index/How this vault is built.md`.

```
python3 knowledge/_build/build_vault.py --results ~/Tahoe-100M/mg53_p53
```

## Conventions

- **Upstream and downstream are regulatory, never positional.** Upstream of MG53 = what raises or lowers its
  expression. Downstream of MG53 = what its level does to p53 and p53's output.
- Chromosomal position is written **3′ of** or **5′ of**. Transcription running past a neighbouring gene into
  TRIM72 and being counted as TRIM72 mRNA is **readthrough spillover** — never "downstream".
- A number without its interval is not a result. A p value without an effect size beside it is not either.
- Claims carry their provenance: a table path, or the analysis document they came from.
- Corrections are recorded, not quietly fixed. `30-Findings/Corrections and retractions.md` is the ledger.
