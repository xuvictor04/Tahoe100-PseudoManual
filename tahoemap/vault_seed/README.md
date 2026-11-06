# vault_seed — the written layer of the vault

The Obsidian vault (`<out>/vault/`, written by `tahoe vault`) has two layers:

| | Generated | Written (this folder) |
|---|---|---|
| Who owns it | `tahoemap/vault.py` | people, and agents working for them |
| What it is | every note's frontmatter and data sections, the indexes, Home, How to read this vault, the canvases | prose about what a gene *is*, and concept notes |
| On rebuild | overwritten from the run's tables | copied / spliced in again, never changed |

**Never edit a note inside `<out>/vault/` by hand**: the next `tahoe vault` overwrites it. Edit the files here.

## Writing about a gene

Create `genes/<SYMBOL>.md` (the HGNC symbol as Tahoe spells it, e.g. `genes/MDM2.md`) holding only the prose — no
frontmatter, no `# MDM2` title (the generator adds both). Use these sections, in this order:

```
> [!summary] In one line
> One sentence: what the gene is and why it matters.

## What it is

## What is uncertain

## References
```

Then rerun `tahoe vault` (or `python -m tahoemap vault --out <out>`). The fragment is spliced under the gene note's
title, above the generated sections, in every note whose gene has that symbol (a symbol that Tahoe lists twice gets
it in both notes). The vault build logs how many fragments it found and spliced; if that number drops, a fragment
was lost or renamed.

## Writing a concept note

Create `notes/<Title>.md` with a short frontmatter (`type: concept`, `tags: [...]`) and a `# Title` heading. It is
copied to `Concepts/<Title>.md` in the vault. Keep titles unique and different from every gene symbol.

## Rules for the written layer

- **Wikilinks** (a note name in double square brackets) may point only to another note in `notes/`, or to a gene
  symbol. A gene link becomes a live link when that gene has a note in the run (it was detected); otherwise the
  build turns it into plain text. Any other link is turned into plain text too, so do not link generated notes
  (drugs, lines, modules) by name.
- **Never invent a citation.** Author-year-journal only where it is certain; otherwise describe the finding without
  a reference, or say the literature is thin.
- **Numbers carry provenance** — a table path, or the analysis they came from — and an interval, not just a point
  estimate. No p value without its effect size.
- **Upstream and downstream are regulatory, never positional.** Position is "3′ of" / "5′ of"; transcription
  running from a neighbour into a gene is [[Readthrough spillover]].
- **Say what is unknown.** For many genes that is the only honest content.
- **Record corrections** in `notes/Corrections and retractions.md`, do not fix silently.

## Where this content came from

The 105 gene fragments and the concept notes were written for an earlier study on the same data (MG53/TRIM72 and
p53, `old-pipeline/knowledge/`). For this genome-wide vault the fragments keep their "In one line", "What it is",
"What is uncertain" and "References" sections and drop "Why it appears in this work" (it described that study);
sentences that only made sense inside it were rephrased, and numbers that come from it are attributed to "the
earlier MG53/p53 study". Where a transcription-factor fragment discusses a "regulon" or an "inferred activity", it
refers to target-set activity inference used in that study; tahoemap does not compute transcription-factor
activities.

So that a reader of the vault cannot take such a sentence for a result of this run, `tahoe vault` puts a callout
("Written for the earlier MG53/p53 study ...: its score / rank / regulon refer to that study's analysis, which
tahoemap does not compute") above every fragment whose text matches `regulon`, `activity score`, `rank` (the word),
`this batch`, `the association` or `MG53` (case-insensitive; `vault.OLD_STUDY_RE`), and the vault's "How to read"
note says so. A fragment rewritten so that it no longer leans on that study's analysis loses the callout on the next
build.
