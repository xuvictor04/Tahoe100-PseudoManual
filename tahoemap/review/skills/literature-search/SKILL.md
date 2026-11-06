---
name: literature-search
description: How to search PubMed and Europe PMC well for genes, drugs and cell lines - field tags, MeSH, symbols and aliases, ambiguous symbols, drug names and salt forms, combining terms, reading the query translation and hit counts, when web search and web fetch help, and when to stop.
---

# Searching the literature

## PubMed

The tool shows how PubMed translated your query and how many records match: read both. A translation you did not
intend (automatic term mapping turned a symbol into a MeSH concept or an unrelated word), zero hits, or tens of
thousands of hits all mean the query needs work before you conclude anything.

Field tags and operators:
- `[tiab]` title or abstract: the default for gene symbols, drug names and cell-line names. `[ti]` title only: precise.
- `[MeSH]` (`[mh]`) subject heading, which includes narrower headings: good for concepts ("NF-E2-Related Factor
  2"[MeSH], "Heme Oxygenase-1"[MeSH], "Topoisomerase II Inhibitors"[pa] for a pharmacological action). `[majr]` =
  major topic. Very recent records are not yet indexed with MeSH, so combine MeSH with `[tiab]` terms using OR.
- `review[pt]` for reviews; `2015:2026[dp]` for dates; `humans[mh]`; `english[la]`.
- `AND`, `OR`, `NOT` in capitals; parentheses for grouping; double quotes for phrases ("heme oxygenase-1"[tiab]);
  truncation `induc*[tiab]` (at least four letters before the asterisk).

Genes:
- Search the symbol and its aliases from the dossier's identity line together:
  `(HMOX1[tiab] OR "HO-1"[tiab] OR "heme oxygenase-1"[tiab])`. Protein names differ from symbols: NRF2 = NFE2L2,
  p53 = TP53, p21 = CDKN1A, HSP70 = HSPA1A/HSPA1B, IkBa = NFKBIA.
- Ambiguous symbols collide with words, other genes or other fields: PIR, CAT, MET, REST, SET, MAX, IMPACT, CA2, AR,
  ATM, CS, GC, p21 (also RAS p21 and PAK1). Use the full name in quotes, require a context term
  (`AND (gene[tiab] OR expression[tiab] OR mRNA[tiab])`), and check the abstracts.
- Mouse and rat symbols differ only in case (Hmox1); PubMed ignores case, so note the species when you read.
- Regulation: add `AND (express*[tiab] OR induc*[tiab] OR regulat*[tiab] OR transcript*[tiab] OR target*[tiab])`.
- A pair: `GENEA[tiab] AND GENEB[tiab]` (with aliases); if nothing, test the shared-regulator hypothesis:
  `(GENEB[tiab]) AND (NRF2[tiab] OR NFE2L2[tiab]) AND (target*[tiab] OR "antioxidant response element"[tiab])`.

Drugs:
- Use the salt-free generic name ("doxorubicin", not "doxorubicin hydrochloride"), plus code names and brand names
  when they are common (dimethyl fumarate = BG-12, Tecfidera; panobinostat = LBH589), and the drug's MeSH heading.
- Drug and gene: `doxorubicin[tiab] AND (CDKN1A[tiab] OR p21[tiab])`; if nothing, the class or the target pathway:
  `("topoisomerase II inhibitor*"[tiab] OR anthracycline*[tiab]) AND CDKN1A[tiab]`.
- Mechanism and potency: `drugname[ti] AND (mechanism[tiab] OR target*[tiab] OR IC50[tiab])`, or a review.

Cell lines:
- Names vary: "NCI-H460" / "H460", "MDA-MB-231" / "MDA-MB231", "HCT116" / "HCT-116". Search the common variants with
  OR, plus the gene, drug or mutation: `(A549[tiab]) AND (KEAP1[tiab] OR NRF2[tiab])`.

Prefer, in this order: a primary paper on exactly the relation in human cells; a review stating it; a primary paper
in another species or cell type (say so). Retracted papers are flagged by the tool and never count as support.

## Europe PMC

Use it when PubMed finds nothing for a pair, to find full-text mentions (results sections and supplementary tables of
open-access papers), for preprints (marked; not peer reviewed), and to look up a DOI.

Syntax: `AND` / `OR` / `NOT` in capitals; quoted terms (`"HMOX1" AND "PIR"`); fields `TITLE:"..."`,
`ABSTRACT:"..."`, `AUTH:"Smith J"`, `DOI:"10.1007/..."`; `SRC:MED` (PubMed records only), `SRC:PPR` (preprints);
`PUB_YEAR:[2015 TO 2026]`. Unfielded terms also match full text. A full-text hit only means the words appear
somewhere: read the abstract (pubmed_abstracts, when there is a PMID) and cite only what it states.

## Web search and web fetch (when available)

Use them for facts that abstracts rarely state: a drug's mechanism, potency or approval (FDA label, DrugBank,
ChEMBL), a cell line's mutations, subtype or misidentification status (Cellosaurus; DepMap), gene aliases and
function (NCBI Gene, UniProt), and very recent work. web_fetch opens only URLs that already appear in the
conversation - in the dossier, a tool result (tahoe_lookup of a line gives its Cellosaurus URLs) or a web_search
result - never one composed from a pattern: fetch a line's Cellosaurus entry through the URL its dossier gives, and
find any other page with web_search first. Do not use them to replace PubMed for literature claims, and do not
cite web pages, vendor sites or summaries in the citation lists; name a database in the note text instead
("Cellosaurus lists KEAP1 p.G333C").

## Planning, budget and stopping

Plan before the first search: list the relations that matter and one or two queries for each. A typical review needs
10-25 searches, 3-6 pubmed_abstracts calls of up to 10 PMIDs each, and 0-5 web calls. Searching is cheap compared
with reading: favour precise queries and batch the abstracts you want to read.

Stop working on a relation when a primary paper or review that states it has been read; or two well-formed queries
(symbol and aliases, PubMed and Europe PMC) found nothing relevant (record them in `literature_checked`); or new
results only repeat papers already seen. Do not search every known-but-absent partner: reason from the dossier for
most of them and search the two to four whose absence is surprising.
