---
name: writing-the-note
description: How to write note_markdown, the review section spliced into the entity's Obsidian note - structure, length, tone, sourcing, links, and keeping what the data show apart from what the literature says.
---

# Writing the note

`note_markdown` is placed in the vault note of the gene, drug or cell line, under the heading "What the literature
says". The vault adds a callout above it with the agent, model, date and a link to the full history, and a line
under it, generated after verification, that says what was checked (cited ids, claims against abstracts) and what
was removed. Readers are biologists deciding what to trust and what to test.

## Structure

Start without a title or a level-1 or level-2 heading (the vault supplies the section heading). Use this order and
leave out a part that would be empty:

```
**In short.** Two or three sentences: what the data show about the entity and how that sits with the literature.

### What the data show
- the main facts from the dossier, with their numbers (fold, z, doses, lines; cos, evidence, fdr)

### What the literature says
- the established relations, each with its citation; for drugs and lines the known mechanism or genotype facts
- expected connections that are missing from the data, and why they probably are

### Unexpected or new
- strong relations with no support found, and what was searched ("no paper found for HMOX1 with PIR")

### Caveats
- the data caveats that matter here (flags, a response seen only in a few lines, a readthrough pair, not in the
  vector space)

### Open questions
- one to three concrete, testable questions
```

End with the open questions. Write no footer, disclaimer or statement that anything was verified: the note is
written before anything is checked, and the vault adds the generated line that says what verification actually did.

## Style

- Short: about 150-450 words for a gene, up to about 600 for a drug or a line with many findings. Bullets of one or
  two sentences.
- Keep data and literature apart. Data sentences carry the dossier's numbers and no citation; literature sentences
  carry a citation and say what the paper reports. Never present a paper's finding as something the data show, or
  the reverse.
- Plain, exact words: "the data show", "X et al. report", "no paper found", "suggests" for indirect support. No
  hype ("remarkably", "striking", "novel insight") and no speculation presented as fact.
- Correlation stays correlation: "moves with" or "co-varies with", not "regulates", unless a cited paper shows
  regulation.
- Numbers as in the dossier: fold "4.5x", cosine "+0.69", z "+9.6", doses in uM.
- Link entities of this run that appear in the dossier or in a tahoe_lookup result with wikilinks: genes
  `[[HMOX1]]`, drugs `[[Dimethyl fumarate (drug)]]`, cell lines `[[A549 (line)]]`. Write any other name as plain
  text, so that no link points to a note that does not exist.
- Citations inline, right after the claim: `... ([PMID:24390086](https://pubmed.ncbi.nlm.nih.gov/24390086/))`.
  Cite in the note only papers that are also in the citations of the review's items (established, missing,
  contradicted, connection_verdicts): only those are checked against a claim, and any other PMID or DOI is removed
  from the note after submission ("citation removed: cited only in this text"), however it is written (a PubMed,
  NCBI or Europe PMC link, a publisher's or bioRxiv URL, a bare URL, a reference-style link, "PMIDs 1, 2, and 3",
  "DOI 10.xxxx/yyyy"). Link a paper only as a PubMed or doi.org link as above, by the id its item cites; a PMC id, a
  PMC link or a Europe PMC preprint link is always removed (cite the paper's PMID or DOI).
