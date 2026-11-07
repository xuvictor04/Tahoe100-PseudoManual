---
name: citations
description: Citation rules for the review agents - formats for PMIDs and DOIs, which papers may be cited, what a citation must support, reviews, preprints, retractions, database facts, and how cited ids and claims are verified after submission.
---

# Citations

## Formats

- In the citation lists of the review: `PMID:12345678` or `DOI:10.1016/j.redox.2024.103134`, the DOI exactly as
  the paper gives it (parentheses and other characters included, e.g. `DOI:10.1016/S0092-8674(00)81096-3`). PMC ids
  are not accepted: give the paper's PMID.
- In `note_markdown`: `[PMID:12345678](https://pubmed.ncbi.nlm.nih.gov/12345678/)` and
  `[DOI:10.xxxx/yyyy](https://doi.org/10.xxxx/yyyy)`, placed right after the sentence they support.

## What may be cited

Only papers that a tool returned in this session, and a PMID only after its abstract was read with pubmed_abstracts.
The review is refused once if it cites anything else, and its citations are checked afterwards. Papers you remember,
however well known, must be found and read like any other: search for them (author, year, topic) and read the
abstract; if the search does not find them, do not cite them.

## What a citation must support

A citation supports a claim when its abstract states the claim, or the title states it and the abstract agrees:

- the same genes (resolve aliases; check ambiguous symbols such as p21 or PIR in the text), the same drug (salt forms
  and class members are not interchangeable unless the paper says so);
- the same direction (induced versus repressed; co-expressed versus anti-correlated);
- the setting: when the paper is in mouse, another tissue, or at another time, the claim says so;
- causal words ("regulates", "target of", "required for") only when the paper shows causation (knockdown or
  knockout, reporter or promoter assay, ChIP); otherwise "co-induced", "associated", "reported together".

One or two precise citations per claim are better than several loose ones. A review is a good source for
well-established background (a factor's canonical targets); for a specific relation prefer the primary paper when
you found it. A preprint can be cited (say "preprint" in the note; confidence at most medium). A paper the tools
mark as retracted is never support, and a retraction notice ("Retraction of Publication") supports only the fact of
the retraction.

Database facts (STRING score, Reactome or Hallmark membership, HGNC groups, Cellosaurus or DepMap entries) are not
citations: state them in the text with their source ("STRING 916").

When nothing is found, the citation list is empty and the text says so. An empty list is correct for `unexpected`
and usual for `plausible`.

## Verification after submission

Depending on the run's settings, every cited PMID is looked up in PubMed and every DOI in Europe PMC and Crossref
(also for retraction); an id that does not exist is removed, its item is marked unverified and the note shows the
removal. A PMID or DOI that the note cites but no item cites is removed from the note, in whatever form it is
written (a link or bare URL to PubMed, an NCBI search, Europe PMC, doi.org, or a publisher's or bioRxiv page with
the DOI in it; a reference-style link; "PMIDs 1, 2, and 3"; "DOI 10.xxxx/yyyy"), and so is any PMC id or Europe PMC
preprint id. Cite a paper in the note by the id its item uses (a link by its other id, the DOI of a PMID the item
cites, counts as the same paper only when PubMed or Europe PMC records both). A retracted paper stays cited, but its
item records the retraction and the note marks it "(retracted paper)" after each link to it. Then a citation checker
reads each claim - with the relation and direction in the data (`data_evidence`) - next to the abstracts it cites,
and records supported, partly, not supported or not checkable; a connection verdict whose citations do not carry it
is shown as "unverified". The vault adds a generated line saying what was checked: never write one yourself.
