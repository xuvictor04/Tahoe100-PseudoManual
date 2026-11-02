---
type: index
tags: [index, meta]
status: current
---

# How this vault is built

> [!summary] In one line
> Two layers: the data layer is generated from the study's tables on every rebuild, the knowledge layer is
> written by hand and survives rebuilds. Edit the wrong one and your work disappears.

## The two layers

| | Generated | Written |
|---|---|---|
| **Who owns it** | `_build/build_vault.py` | people, and agents working for them |
| **What it is** | every gene note's frontmatter and its whole `## In this dataset` block; `Home.md`; `Genes — Map of Content.md`; `Tables — what the study produced.md` | everything else: concepts, findings, methods, literature, and each gene's prose |
| **Where it lives** | inlined into the note | gene prose in `20-Genes/_knowledge/<SYMBOL>.md`; other notes are their own files |
| **On rebuild** | overwritten from the tables | untouched, and spliced back in |

So:

- **To write about a gene** — create `20-Genes/_knowledge/MDM2.md` with just the prose body (no frontmatter,
  no `# MDM2` heading; the generator adds both) and rebuild. It will appear above the data block.
- **To change what every gene note shows** — edit `_build/build_vault.py`.
- **Never edit a `20-Genes/*.md` file directly.** The next rebuild will overwrite it. The fragment is the
  place.

## Rebuilding

```
python3 knowledge/_build/build_vault.py --results ~/Tahoe-100M/mg53_p53
```

Point `--results` at a completed run's output folder. It needs the committed tables in
`mg53_p53/findings/tables/` (which are in the repository) plus two files from the run itself:
`genome_wide/tables/c_screen_genes.csv.gz` and `upstream_tf/tables/a1a2_tf_summary.csv`. While iterating,
`--only-genes MDM2,CDKN1A` rebuilds just those and skips the indexes.

It prints how many notes it wrote, the tier split, and how many knowledge fragments it found and spliced in.
That last number is the one to watch: if it drops, a fragment file has been lost or renamed.

## Tiers

Every gene gets a note. How much *written* attention it gets is its tier, assigned by the generator:

| Tier | Count | Who is in it | What the prose should be |
|---|---|---|---|
| 1 | 50 | the 29 curated p53 effectors, [[TRIM72]] and [[TP53]] themselves, the locus genes, the other routes that disable p53, and the muscle factors | a real note: what the protein does, how it is regulated, what is contested |
| 2 | 55 | the repression arm of [[p53 program P]], the 20 genes MG53 tracks most strongly, the top-ranked transcription factors | short — and for the obscure ones, mostly an honest account of how thin the literature is |
| 3 | 238 | the rest of the programme, the remaining MG53 partners, and every ENSG-only identifier | nothing written; the generated tables are what the vault knows |

A tier-3 note is not a failure. It is a gene whose data is recorded and about which nothing is claimed, which
is the correct state for most of a 195-gene programme.

## Rules the written layer follows

- **Never invent a citation.** Author-year-journal only where it is certain; otherwise describe the finding
  without a reference, or say the literature is thin. A fabricated reference in a knowledge base is worse
  than a missing one.
- **Numbers carry provenance** — a table path, or the analysis document they came from. An interval, not just
  a point estimate. No p value without its effect size.
- **Upstream and downstream are regulatory, never positional.** Position is "3′ of" / "5′ of"; transcription
  running into TRIM72 from a neighbour is [[Readthrough spillover]].
- **Record corrections.** [[Corrections and retractions]] is the ledger and it is meant to grow.
- **Say what is unknown.** For most of the tier-2 genes that is the only honest content, and it is more
  useful than a confident paragraph assembled from nothing.

## Where the numbers come from

The vault holds no copies of the data. Every number in a generated block is read from a table in the
repository or the run, and [[Tables — what the study produced]] lists them with what each one holds. One copy
of every number, and it lives with the code that made it.
