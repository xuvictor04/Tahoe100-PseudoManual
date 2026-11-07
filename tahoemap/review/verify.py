"""verify - checking a submitted review: do the cited papers exist, and do their abstracts say what is claimed?

    check_ids(review, ctx) -> (checked_review, report)
        every cited PMID is looked up with PubMed esummary, every DOI in Europe PMC and Crossref. A citation that
        does not exist is removed from its item, and the item gets "unverified": true and "removed_citations":
        [...]; mentions of it in note_markdown become 'PMID:n (citation removed: not found in PubMed)'. The note
        may cite only papers that an item cites (only those are checked against a claim): any other PMID / DOI in
        it becomes 'PMID:n (citation removed: cited only in this text ...)', and any PMC or other Europe PMC id
        (a preprint's PPR ...) 'PMCID:PMCn (citation removed: a PMC or Europe PMC id ...)', and is counted (report
        "note_removed"). The note is read for every form that names a paper (tools.note_matches: PubMed / NCBI
        (also 'pubmed?term=n') / Europe PMC / PMC / doi.org links and bare URLs, a DOI in a publisher's or
        preprint URL, 'PMID n', 'PMIDs a, b, and c', 'DOI:x', 'DOI x'); a link or bare URL to a removed paper is
        replaced whole (link text over several lines and any title included), a reference definition to one is
        deleted and each reference link to it replaced, and the marker's id is written so that it forms no tag or
        Obsidian comment (tools.cid_text; a DOI whose escapes do not decode to one stays encoded:
        tools.clean_doi). One paper cited under its PMID and its DOI (the DOI of its PubMed record, the PMID of
        its Europe PMC record) is one paper: a note link by the other id is cited by the item, and the paper is
        counted once (report "same_paper": {id: the id standing for its paper}). Retractions: a PMID whose PubMed
        publication types include 'Retracted Publication', or a DOI that Europe PMC types as one or whose Crossref
        record carries a retraction / withdrawal / removal update, is retracted (so are the paper's other ids);
        it stays cited, the item lists it in "retracted_citations", and the note gets ' (retracted paper)' after
        each link to / mention of it (after the link's closing ')' or after each reference link to it, never in
        a destination or a definition); "retracted" counts the retracted papers an item cites (a paper cited
        only in the note is removed, not counted). A retraction NOTICE, 'Retraction of Publication', is not
        itself retracted: items list notices in "retraction_notices". Ids that could not be checked (a service
        down) are kept, and listed per item in "unchecked_citations" (every item that cites gets this list, []
        when all its ids were checked). Ids cited without having been retrieved in the session (ctx.read_ids /
        ctx.seen_ids) are flagged per item ("not_retrieved"). The input is not modified. report = {"status":
        "done", "checked", "removed", "unchecked", "retracted" (counts), and "found", "n_cited", "pmids_checked",
        "dois_checked", "note_removed", "items_unverified" (counts), "missing", "unchecked_ids", "retracted_ids",
        "retraction_notices", "note_removed_ids", "not_retrieved_in_session" (lists), "same_paper"}; found /
        checked / n_cited count papers.
    claims(review) -> list of {claim_id, section, index, claim, data, meaning, citations}
        the checkable claims: items of established (E1, E2 ...), missing (M..), contradicted (C..) and
        connection_verdicts (V..) that cite at least one paper. claim = what the review says the papers report;
        data = the relation in this run's data (direction and numbers) the claim is about; meaning = for a
        connection verdict, what the verdict requires of the papers (VERDICT_MEANING, the connection-audit rubric).
    fetch_abstracts(review, ctx) -> {citation id: record text or None}
        PubMed records for PMIDs, Europe PMC abstracts for DOIs (None: no abstract available); retracted papers
        and retraction notices are marked in the record's header.
    build_check_prompt(review, abstracts, entity=None) -> str
        the user message of the citation-checker agent: each claim with its id, the data it is about, the meaning
        of its verdict and its citations, then each cited abstract once.
    CHECK_TOOL
        the strict submit_check tool: {verdicts: [{claim_id, verdict, direction, reason}], summary}; verdict one of
        supported / partly / not supported / not checkable; direction: the direction the papers report compared
        with the data (same as the data / opposite to the data / not stated / not applicable).
    submit_check(ctx, payload) -> str
        validates a submit_check call (executed via tools.execute); with ctx.notes["claim_ids"] set by the runner,
        every claim id must get exactly one verdict (one correction allowed). The payload goes to ctx.submitted.
    apply_check(review, check) -> (review, summary)
        each checked item gets "check": {verdict, direction, reason}. A 'supported' or 'partly' verdict whose direction
        contradicts what the claim needs (an established relation the papers report in the opposite direction; a
        contradiction the papers report in the same direction) is stored as 'not supported'. review
        ["citation_check"] = summary = {summary, counts, unmatched, supported, partly, not_supported,
        not_checkable}.
    annotate(review, ids_checked=None) -> review (in place)
        the shared contract's per-item fields: every connection_verdicts item, and every item of established /
        missing / contradicted / unexpected that cites (or cited) a paper, gets
          check_status: supported | partly | not_supported | not_checkable  (the citation checker's verdict)
                        citations_removed   (it cited papers, and every one was removed as not found)
                        unchecked           (a citation's id was not verified: the id check did not run or could
                                             not reach the service)
                        not_checkable       (ids verified - or nothing cited - but no claim check: --verify ids,
                                             or the checker did not run)
          shown_verdict: the verdict to display - the item's verdict ('established', 'indirect' ... for connection
                        verdicts; the section's name 'established' / 'missing' / 'contradicted' / 'unexpected' for
                        the other items), or 'unverified' when check_status is not_supported or citations_removed.
        ids_checked: whether check_ids ran (None: read from the items' "unchecked_citations").
    finalize(review, mode, ids_report=None, llm=None) -> review
        the review to store: annotate(), then "verification" = {"mode", "ids": {"status": done | not_run | failed,
        "checked", "removed", "unchecked", "retracted", ... (the check_ids report)}, "llm": {"status": done |
        not_run | failed, "detail", "supported", "partly", "not_supported", "not_checkable", "summary", ...},
        "counts": counts(review)}, and "note_footer" = note_footer(verification): a provenance line generated
        from those counts (never written by the agent; a sentence of the note that only vouches for its own
        verification is dropped, keeping the lists and emphasis around it: drop_self_check). A review whose llm
        status is not 'done' can be checked
        again later (claims -> fetch_abstracts -> build_check_prompt -> the checker -> apply_check -> finalize).
    note_footer(verification) -> str
    counts(review, same=None) -> dict
        verification counts: claims checked, per verdict, unverified items, removed citations, retracted
        citations, per check_status, and n_citations (papers: same = check_ids' "same_paper").
"""

import copy
import json
import re
from collections import Counter

from . import tools as TL

CHECK_VERDICTS = ("supported", "partly", "not supported", "not checkable")
CHECK_STATUSES = ("supported", "partly", "not_supported", "not_checkable", "unchecked", "citations_removed")
STATUS_OF = {"supported": "supported", "partly": "partly", "not supported": "not_supported",
             "not checkable": "not_checkable"}
SAME, OPPOSITE = "same as the data", "opposite to the data"
DIRECTIONS = (SAME, OPPOSITE, "not stated", "not applicable")
SECTION_PREFIX = {"established": "E", "missing": "M", "contradicted": "C", "connection_verdicts": "V"}
ITEM_SECTIONS = ("established", "missing", "contradicted", "unexpected", "connection_verdicts")
VERDICT_MEANING = {
    "established": "a cited paper reports this relation itself, in the direction the data show: for two genes, "
                   "co-regulation or co-expression of the pair (both shown as targets of one factor in one study, "
                   "or co-induced by one stimulus) or one regulating the other's transcription; for a drug and a "
                   "gene, the drug's effect on the gene in that direction (or on the gene's direct regulator, with "
                   "the gene named as its target); for a cell line, the line's expression of the gene or its "
                   "sensitivity to the drug. Membership of the same pathway or complex alone is not enough",
    "indirect": "no paper on the pair, but the cited papers place both under one regulator or process that moves "
                "them in the direction the data show (at least one paper per gene, or one review naming both)",
    "plausible": "consistent with known biology, with no paper tying the two; the citations need only support the "
                 "background reasoning",
    "unexpected": "no support was found after searching",
    "contradicted": "a cited paper reports the opposite direction in a comparable setting",
}
NOT_FOUND = {"PMID": "not found in PubMed", "DOI": "not found in Crossref or Europe PMC"}
NOTE_ONLY = "cited only in this text, by no claim of the review, so not checked"
NOTE_OTHER = "a PMC or Europe PMC id, not a PMID or DOI, so not checked"

CHECK_TOOL = {
    "name": "submit_check",
    "description": (
        "Submit the verdicts of the citation check; this ends the check. Give exactly one verdict for every claim "
        "id listed in the request: supported (the cited abstracts state the claim's literature content, and for a "
        "connection verdict they meet the verdict's stated meaning, in the direction of the data), partly (they "
        "support part of it, or a weaker or narrower version), not supported (they do not say it, say something "
        "else or the opposite, or report the relation in the direction opposite to the one the claim needs), not "
        "checkable (no abstract available, or the claim rests on full-text content the abstracts do not show). "
        "direction: the direction of the relation the papers report, compared with the claim's data line. The "
        "reason names the PMID / DOI that decided the verdict and quotes or closely paraphrases the deciding "
        "words. If the call returns an error, fix the listed problems and call it again."),
    "strict": True,
    "input_schema": {
        "type": "object",
        "properties": {
            "verdicts": {
                "type": "array",
                "description": "one entry per claim id",
                "items": {
                    "type": "object",
                    "properties": {
                        "claim_id": {"type": "string", "description": "the claim id from the request, e.g. 'E1'"},
                        "verdict": {"type": "string", "enum": list(CHECK_VERDICTS)},
                        "direction": {"type": "string", "enum": list(DIRECTIONS),
                                      "description": "the direction the cited papers report compared with the "
                                                     "claim's data line (co-varying vs moving opposite; raised vs "
                                                     "lowered; sensitive vs resistant); 'not applicable' for "
                                                     "missing claims and claims without a direction"},
                        "reason": {"type": "string",
                                   "description": "one or two sentences: which citation decided it and the words "
                                                  "that did"},
                    },
                    "required": ["claim_id", "verdict", "direction", "reason"],
                    "additionalProperties": False,
                },
            },
            "summary": {"type": "string", "description": "one or two sentences on the review's citations overall"},
        },
        "required": ["verdicts", "summary"],
        "additionalProperties": False,
    },
}


# ----------------------------------------------------------------------------- ids
def _entity_name(review, entity=None):
    if entity:
        return entity.get("name") or entity.get("entity_id") or "the entity"
    return "the entity"


def _doi_status(ctx, doi):
    """(exists: True / False / None = could not be checked, 'retracted' / 'notice' / '', the paper's PMID per Europe
    PMC or '') for a DOI."""
    epmc = cr = None
    try:
        hits, res = TL.europepmc_records(ctx, f'DOI:"{doi}"', 1)
        epmc = (hits, res[0] if res else {})
    except TL.ToolError:
        pass
    try:
        cr = TL.crossref_work(ctx, doi)
    except TL.ToolError:
        pass
    if (epmc and epmc[0] > 0) or (cr and cr.get("exists")):
        exists = True
    elif epmc is not None and cr is not None:
        exists = False
    else:
        exists = None
    st = TL.retraction_status((epmc[1] if epmc else {}).get("pubType")) if exists else ""
    if exists and cr and cr.get("retracted"):
        st = "retracted"
    elif exists and not st and cr and cr.get("notice_of"):
        st = "notice"
    pmid = str((epmc[1] if epmc else {}).get("pmid") or "").strip()
    return exists, st, (f"PMID:{int(pmid)}" if pmid.isdigit() else "")


def _same_paper(pairs, ids):
    """{id: the id that stands for its paper}: ids linked by pairs (a PMID and the DOI its record gives, or a DOI and
    the PMID Europe PMC gives) name one paper, which the first of them in ids stands for."""
    parent = {c: c for c in ids}

    def root(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c
    rank = {c: i for i, c in enumerate(ids)}
    for x, y in pairs:
        if x in parent and y in parent:
            rx, ry = root(x), root(y)
            if rx != ry:
                lo, hi = sorted((rx, ry), key=rank.get)
                parent[hi] = lo
    return {c: root(c) for c in ids}


def check_ids(review, ctx):
    """(checked copy of the review, report); see the module docstring."""
    r = copy.deepcopy(review)
    ids = list(dict.fromkeys(c for c, _s, _i in TL.cited_ids(r)))
    pmids = [c for c in ids if c.startswith("PMID:")]
    dois = [c for c in ids if c.startswith("DOI:")]
    missing, unchecked, retracted, notices, found, pairs = [], [], [], [], [], []
    if pmids:
        try:
            sm = TL.esummary_records(ctx, [c.split(":", 1)[1] for c in pmids])
            for c in pmids:
                s = sm.get(c.split(":", 1)[1])
                if s is None:
                    missing.append(c)
                    continue
                found.append(c)
                st = TL.retraction_status(s.get("pubtype"))
                (retracted if st == "retracted" else notices if st == "notice" else []).append(c)
                pairs += [(c, "DOI:" + str(a.get("value") or "").strip().lower()) for a in s.get("articleids") or []
                          if isinstance(a, dict) and a.get("idtype") == "doi" and a.get("value")]
        except TL.ToolError:
            unchecked += pmids
    for c in dois:
        exists, st, pmid = _doi_status(ctx, c.split(":", 1)[1])
        if exists is None:
            unchecked.append(c)
            continue
        (found if exists else missing).append(c)
        (retracted if st == "retracted" else notices if st == "notice" else []).append(c)
        if exists and pmid:
            pairs.append((c, pmid))
    # one paper cited under its PMID and its DOI (an item cites one, the note links the other): one paper, retracted
    # (or a notice) when either id says so
    paper = _same_paper(pairs, ids)
    ret_p, not_p = {paper[c] for c in retracted}, {paper[c] for c in notices}
    retracted = [c for c in ids if paper[c] in ret_p]
    notices = [c for c in ids if paper[c] in not_p and paper[c] not in ret_p]
    gone = set(missing)
    have = set(ctx.read_ids) | {x for x in ctx.seen_ids if x.startswith("DOI:")}
    not_retrieved = [c for c in ids if c.startswith(("PMID:", "DOI:")) and c not in have and c not in gone]
    n_unverified = 0
    for sec in SECTION_PREFIX:
        for it in r.get(sec) or []:
            cits = [TL.norm_citation(c) or c for c in it.get("citations") or []]
            rm = [c for c in cits if c in gone]
            if rm:
                it["citations"] = [c for c in cits if c not in gone]
                it["removed_citations"] = list(dict.fromkeys((it.get("removed_citations") or []) + rm))
                it["unverified"] = True
                n_unverified += 1
            cur = it.get("citations") or []
            for key, lst in (("retracted_citations", retracted), ("retraction_notices", notices),
                             ("not_retrieved", not_retrieved)):
                x = [c for c in cur if c in lst]
                if x:
                    it[key] = x
                else:
                    it.pop(key, None)
            if cur or it.get("removed_citations"):
                it["unchecked_citations"] = [c for c in cur if c in unchecked]
    # the note: removed ids marked; ids no item cites (never checked against a claim) taken out - an id naming the
    # same paper as an item's citation is cited by that item
    why = {c: "citation removed: " + NOT_FOUND[c.split(":", 1)[0]] for c in gone}
    item = set(TL.item_ids(r))
    in_items = {c for c in ids if paper[c] in {paper.get(x, x) for x in item}} | item
    note_only = [c for c in dict.fromkeys(x for x, _a, _b in TL.note_ids(r.get("note_markdown") or ""))
                 if c not in in_items and c not in gone]
    why.update({c: "citation removed: " + (NOTE_OTHER if c.startswith(("PMCID:", "EPMC:")) else NOTE_ONLY)
                for c in note_only})
    if why and r.get("note_markdown"):
        r["note_markdown"] = _strip_from_note(r["note_markdown"], why)
    if retracted and r.get("note_markdown"):
        r["note_markdown"] = _mark_retracted(r["note_markdown"], [c for c in retracted if c in in_items])
    nf, no = _removed_ids(r)
    # counted per paper, among the papers an item still cites (a paper cited only in the note was removed from it)
    cited_by_item = [c for c in ids if c in item]
    one = {}
    for c in cited_by_item:
        one.setdefault(paper[c], c)
    retracted_ids = [c for c in one.values() if c in retracted]
    notice_ids = [c for c in one.values() if c in notices]
    same = {c: paper[c] for c in ids if paper[c] != c}
    n_found = len({paper[c] for c in found})
    report = {"status": "done", "checked": n_found + len(missing), "removed": len(nf),
              "unchecked": len(unchecked), "retracted": len(retracted_ids), "found": n_found,
              "n_cited": len({paper.get(c, c) for c in set(ids) | nf | no}),
              "pmids_checked": len(pmids) - sum(1 for c in unchecked if c.startswith("PMID:")),
              "dois_checked": len(dois) - sum(1 for c in unchecked if c.startswith("DOI:")),
              "note_removed": len(no), "items_unverified": n_unverified, "missing": missing,
              "unchecked_ids": unchecked, "retracted_ids": retracted_ids, "retraction_notices": notice_ids,
              "note_removed_ids": sorted(no), "not_retrieved_in_session": not_retrieved, "same_paper": same}
    annotate(r, ids_checked=True)
    return r, report


# a markdown link (or image) with its destination. Link text: escapes, one level of nested [...], line breaks but no
# blank line (a paragraph ends there), at most 300 items, possessive (linear time on long runs of brackets).
# Destination: one level of ( ) in a URL, or <...>; an optional title in "...", '...' or (...).
_LT_CH = r"(?:[^\[\]\\\n]|\\.|\n(?![ \t]*(?:\n|$)))"
_LINK_TEXT = rf"(?<!\\)\[((?:{_LT_CH}|\[{_LT_CH}{{0,300}}+\]){{0,300}}+)\]"
_NB = r"(?:\n(?![ \t]*\n))"                                    # a line break that is no blank line
_LINK_TITLE = (rf"(?:\s+(?:\"(?:[^\"\n]|{_NB})*\"|'(?:[^'\n]|{_NB})*'|\((?:[^()\n]|{_NB})*\)))?")
_MD_LINK = re.compile(r"!?" + _LINK_TEXT + r"\(\s*(<[^<>\n]*>|(?:[^\s()\\]|\\.|\((?:[^\s()\\]|\\.)*\))*)"
                      + _LINK_TITLE + r"\s*\)")
# after a URL that ends a link's destination: the rest of the link (its title and closing ')')
_DEST_TAIL = re.compile(r">?" + _LINK_TITLE + r"[ \t]*\n?[ \t]*\)")
# a reference definition '[label]: destination "title"' at any container depth (blockquote, list item), its
# destination or title possibly on the next line; and a reference link to one: [text][label], [label][] or [label]
_REF_DEF = re.compile(r"^((?:[ \t]*(?:>|(?:[-+*]|\d{1,9}[.)])(?=[ \t])))*[ \t]*)"
                      r"\[(?!\^)((?:[^\[\]\\\n]|\\.){1,999}+)\]:[ \t]*(?:\n[ \t>]*)?(<[^<>\n]*>|[^\s<>]\S*)[^\n]*"
                      r"(?:\n[ \t>]*(?:\"[^\"\n]*\"|'[^'\n]*'|\([^()\n]*\))[ \t]*(?=\n|$))?\n?", re.M)
_REF_USE = re.compile(r"!?" + _LINK_TEXT + r"(?:\[((?:[^\[\]\\\n]|\\.){0,999}+)\])?")
# a bare URL, with or without its scheme (balanced ( ) allowed): a note id inside one takes the whole URL with it
_BARE_URL = re.compile(r"<?(?:https?://)?(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}/(?:[^\s<>()\[\]]|\([^\s<>()\[\]]*\))*>?")
_MARKED = re.compile(r"\b(PMID:\d{1,9}|PMCID:PMC\d{1,9}|EPMC:[A-Z]{3}/[A-Z0-9]{1,20}|DOI:" + TL.DOI_BODY
                     + r") \(citation removed: ([^)]*)\)")
_RETRACTED_MARK = " (retracted paper)"


def _url_span(md, a, b):
    """The span of the bare URL around md[a:b] (its trailing sentence punctuation left out), or None."""
    for m in _BARE_URL.finditer(md, max(0, a - 300), min(len(md), b + 300)):
        if m.start() <= a and b <= m.end():
            e = m.end()
            while e > b and md[e - 1] in ".,;:!?'\"":
                e -= 1
            s = m.start()
            if md[s] == "<" and md[e - 1:e] != ">":
                s += 1
            if md[e - 1] == ">" and md[s] != "<":
                e -= 1
            return s, e
        if m.start() > a:
            break
    return None


def _enclosing_link(md, s, e):
    """(start, end) of the inline link whose destination is the URL md[s:e], when _MD_LINK could not read that link
    whole (link text with deeper brackets, a code span ...): from its opening '[' (balanced backwards from the '](')
    to its closing ')', or from its '(' when no '[' opens it; None when md[s:e] is no link destination."""
    j = s
    while j > 0 and md[j - 1] in " \t\n<":
        j -= 1
    t = _DEST_TAIL.match(md, e)
    if j < 2 or md[j - 2:j] != "](" or not t:
        return None
    depth = 0
    for i in range(j - 2, max(-1, j - 3000), -1):
        if md[i] in "[]" and not (i and md[i - 1] == "\\"):
            depth += 1 if md[i] == "]" else -1
            if depth == 0:
                return (i - 1 if i and md[i - 1] == "!" else i), t.end()
        elif md.startswith("\n\n", i):
            break
    return j - 1, t.end()


def _ref_key(label):
    """A reference label as CommonMark matches it: case-insensitive, runs of whitespace as one space."""
    return " ".join(label.split()).casefold()


def _ref_defs(md):
    """[(match, key, ids)] of md's reference definitions; ids = the citation ids its destination names."""
    return [(m, _ref_key(m.group(2)), list(dict.fromkeys(c for c, _a, _b in TL.note_ids(m.group(3).strip("<>")))))
            for m in _REF_DEF.finditer(md)]


def _first_defs(defs):
    """{key: ids} of the definition each reference link uses (the first one of its label)."""
    out = {}
    for _m, key, ids in defs:
        out.setdefault(key, ids)
    return out


def _ref_uses(md, keys):
    """[(start, end, key)] of the reference links of md ([text][label], [label][], [label]) to one of these keys;
    not the label of a definition, nor the text of an inline link."""
    out = []
    if not keys:
        return out
    for m in _REF_USE.finditer(md):
        lab = m.group(2)
        if lab is None and md[m.end():m.end() + 1] in ("(", ":"):
            continue
        key = _ref_key(m.group(1) if not lab else lab)
        if key in keys:
            out.append((m.start(), m.end(), key))
    return out


def _marker(c, why):
    return f"{TL.cid_text(c)} ({why[c]})"


def _strip_from_note(md, why):
    """md with every link to / mention of an id in why ({id: 'citation removed: ...'}) replaced by
    'id (citation removed: ...)' (the id as text that forms no tag: tools.cid_text). A markdown link whose
    destination names such an id goes whole (any URL form tools.note_matches reads: PubMed, NCBI, Europe PMC, PMC,
    doi.org, a publisher's URL with the DOI; any letter case or percent-encoding; link text over several lines; any
    title), and so does a bare URL; a reference definition whose destination names one is deleted and each
    reference link to it ([text][label], [label][], [label]) replaced; mentions already marked are left alone."""
    defs = _ref_defs(md)
    gone_keys = {k: [c for c in ids if c in why] for k, ids in _first_defs(defs).items()}
    gone_keys = {k: v for k, v in gone_keys.items() if v}
    for m, _key, ids in reversed(defs):
        if any(c in why for c in ids):
            quote = re.sub(r"[^>]", "", m.group(1))
            md = md[:m.start()] + (quote + "\n" if quote and m.group(0).endswith("\n") else quote) + md[m.end():]
    parts, pos = [], 0
    for a, b, key in _ref_uses(md, set(gone_keys)):
        parts += [md[pos:a], "; ".join(_marker(c, why) for c in gone_keys[key])]
        pos = b
    md = "".join(parts) + md[pos:]

    def link(m):
        dest = m.group(2).strip("<>")
        gone = list(dict.fromkeys(c for c, _a, _b in TL.note_ids(dest) if c in why))
        return "; ".join(_marker(c, why) for c in gone) if gone else m.group(0)
    md = _MD_LINK.sub(link, md)
    spans, last = [], -1
    for c, a, b, _kind in TL.note_matches(md):
        if c not in why or a < last:
            continue
        a, b = _url_span(md, a, b) or (a, b)
        a, b = _enclosing_link(md, a, b) or (a, b)
        if a < last:
            continue
        spans.append((a, b, c))
        last = b
    for a, b, c in reversed(spans):
        md = md[:a] + _marker(c, why) + md[b:]
    return md


def _mark_retracted(md, retracted):
    """md with ' (retracted paper)' after each link to / mention of a retracted paper (once: a mark already there is
    kept), so that the note's reader sees it where the paper is cited: after the closing ')' of a link (never in its
    destination, where it would be read as the link's title), after each reference link whose definition names the
    paper (never in the definition, which shows nothing)."""
    retracted = set(retracted)
    if not retracted or not md:
        return md
    # a mark an earlier version wrote inside a destination (a hidden title) or a definition: moved out below
    md = _MD_LINK.sub(lambda m: m.group(0)[:-len(_RETRACTED_MARK) - 1] + ")"
                      if m.group(0).endswith(_RETRACTED_MARK + ")") else m.group(0), md)
    md = re.sub(r"^([ \t>]*\[[^\[\]\n]+\]:[ \t]*\S+)" + re.escape(_RETRACTED_MARK) + r"[ \t]*$", r"\1", md,
                flags=re.M)
    defs = _ref_defs(md)
    first = _first_defs(defs)
    in_def = [(m.start(), m.end()) for m, _k, _i in defs]
    uses = _ref_uses(md, set(first))
    links = [(m.start(), m.end()) for m in _MD_LINK.finditer(md)] + [(a, b) for a, b, _k in uses]
    ends = {b for _a, b, key in uses if retracted & set(first[key])}
    for c, a, b, _kind in TL.note_matches(md):
        if c not in retracted or any(s <= a < e for s, e in in_def):
            continue
        lk = next(((s, e) for s, e in links if s <= a < e), None)
        if lk:
            ends.add(lk[1])
        else:
            s, e = _url_span(md, a, b) or (a, b)
            ends.add((_enclosing_link(md, s, e) or (s, e))[1])
    for e in sorted(ends, reverse=True):
        if not md.startswith(_RETRACTED_MARK, e):
            md = md[:e] + _RETRACTED_MARK + md[e:]
    return md


def _removed_ids(review):
    """(ids removed as not found, ids removed from the note as cited only there) of a checked review, from the
    items' removed_citations and the note's markers (so a review checked again keeps its earlier removals)."""
    nf, no = set(), set()
    for sec in ITEM_SECTIONS:
        for it in review.get(sec) or []:
            nf |= {TL.norm_citation(c) or c for c in it.get("removed_citations") or []}
    for m in _MARKED.finditer(review.get("note_markdown") or ""):
        c = "DOI:" + TL.clean_doi(m.group(1)[4:])[0] if m.group(1).startswith("DOI:") else m.group(1)
        (nf if m.group(2).startswith("not found") else no).add(c)
    return nf, no


# ----------------------------------------------------------------------------- claims
def _claim_text(sec, it, entity_name):
    if sec == "established":
        return f"{it.get('partner_or_topic', '')}: {it.get('relation', '')}"
    if sec == "missing":
        return (f"The literature reports this connection: {it.get('expected_connection', '')}. (Offered reason why "
                f"the data do not show it: {it.get('likely_reason', '')})")
    if sec == "contradicted":
        return f"A cited paper reports the opposite of this observation: {it.get('claim', '')}"
    if sec == "connection_verdicts":
        v = it.get("verdict", "")
        rel = str(it.get("relation") or "").strip()
        return (f"{entity_name} and {it.get('partner', '')}: verdict '{v}'."
                + (f" What the review says the papers report: {rel}" if rel else
                   " (the review states no relation: judge the verdict's meaning against the abstracts)"))
    return ""


def _data_text(sec, it):
    if sec == "missing":
        return str(it.get("data_status") or "").strip()
    return str(it.get("data_evidence") or "").strip()


def claims(review, entity=None):
    """The checkable claims (items citing at least one paper), with ids E1.., M1.., C1.., V1.. (1-based index
    within the section, so the id points at the same item whatever else is cited)."""
    nm = _entity_name(review, entity)
    out = []
    for sec, pre in SECTION_PREFIX.items():
        for i, it in enumerate(review.get(sec) or []):
            cits = [TL.norm_citation(c) or c for c in it.get("citations") or []]
            if not cits:
                continue
            v = it.get("verdict", "") if sec == "connection_verdicts" else ""
            out.append({"claim_id": f"{pre}{i + 1}", "section": sec, "index": i,
                        "claim": _claim_text(sec, it, nm), "data": _data_text(sec, it),
                        "meaning": VERDICT_MEANING.get(v, "") if v else "", "citations": cits})
    return out


def _retracted_in(review):
    ret, note = set(), set()
    for sec in ITEM_SECTIONS:
        for it in review.get(sec) or []:
            ret |= set(it.get("retracted_citations") or [])
            note |= set(it.get("retraction_notices") or [])
    return ret, note


def fetch_abstracts(review, ctx):
    """{citation id: record text, or None when no abstract is available} for every id the claims cite."""
    ids = list(dict.fromkeys(c for cl in claims(review) for c in cl["citations"]))
    ret, notices = _retracted_in(review)
    out = {}
    pm = [c.split(":", 1)[1] for c in ids if c.startswith("PMID:")]
    if pm:
        try:
            recs = TL.pubmed_records(ctx, pm)
        except TL.ToolError:
            recs = {}
        for p in pm:
            r = recs.get(p)
            if r and f"PMID:{p}" in ret:
                r = dict(r, retracted=True)
            out[f"PMID:{p}"] = TL.format_record(r) if r else None
    for c in ids:
        if not c.startswith("DOI:"):
            continue
        doi = c.split(":", 1)[1]
        try:
            _n, res = TL.europepmc_records(ctx, f'DOI:"{doi}"', 1, core=True)
        except TL.ToolError:
            res = []
        if res and res[0].get("abstractText"):
            x = res[0]
            ab = TL.clean_markup(x.get("abstractText"))
            pts = x.get("pubType") or ((x.get("pubTypeList") or {}).get("pubType") or [])
            st = "retracted" if c in ret else "notice" if c in notices else TL.retraction_status(pts)
            mark = ("  [RETRACTED: do not cite as support]" if st == "retracted" else
                    "  [RETRACTION NOTICE: a notice, not the retracted paper]" if st == "notice" else "")
            kind = "PREPRINT (not peer reviewed)" if x.get("source") == "PPR" else (
                "; ".join(pts) if isinstance(pts, list) else pts or "")
            out[c] = (f"=== {c} ==={mark}\nTitle: {TL.clean_markup(x.get('title'))}\nJournal: "
                      f"{x.get('journalTitle') or x.get('source', '')} ({x.get('pubYear', '?')}) | Type: {kind}\n"
                      f"Abstract:\n{ab[:TL.ABSTRACT_CHARS]}")
        else:
            out[c] = None
    return out


def build_check_prompt(review, abstracts, entity=None):
    """The citation-checker's user message."""
    nm = _entity_name(review, entity)
    cl = claims(review, entity)
    P = [f"Check the claims of a literature review of {nm} (Tahoe-100M gene map) against the abstracts of the "
         "papers each claim cites.",
         "Each claim gives what the review says the papers report, and on a 'data:' line the relation in this run's "
         "data that the claim is about, with its direction (co-varying or moving opposite; raised or lowered; "
         "depleted or not). Do not judge the data's numbers: they tell you which relation, and which direction, "
         "the papers must report. A claim that the papers report the relation the data show (E, and V verdicts "
         "'established' or 'indirect') is not supported when the papers report the opposite direction (co-"
         "induction where the data show the pair moving opposite; a drug lowering a gene the data show raised): "
         "grade it 'not supported' (or 'partly' when the direction is not stated in the abstract), and say so in "
         "the reason. A contradiction (C, V 'contradicted') needs the papers to report the opposite of the data.",
         "A connection verdict (V) is judged against the meaning given with it, which is strict: 'established' "
         "needs a paper on the relation itself (co-regulation or co-expression of the pair, one regulating the "
         "other's transcription, or the drug's effect on the gene); two genes in the same pathway or complex is "
         "not enough.", "", "<claims>"]
    for c in cl:
        P.append(f"[{c['claim_id']}] ({c['section']}) {c['claim']}")
        if c["data"]:
            P.append(f"    data: {c['data']}")
        if c["meaning"]:
            P.append(f"    the verdict requires: {c['meaning']}")
        P.append(f"    cites: {', '.join(c['citations'])}")
    P += ["</claims>", "", "<abstracts>"]
    ret, notices = _retracted_in(review)
    for cid in dict.fromkeys(x for c in cl for x in c["citations"]):
        t = abstracts.get(cid)
        mark = ("  [RETRACTED: do not cite as support]" if cid in ret else
                "  [RETRACTION NOTICE: a notice, not the retracted paper]" if cid in notices else "")
        P.append(t if t else f"=== {cid} ==={mark}\n(no abstract available: claims resting only on this citation "
                             "are not checkable)")
        P.append("")
    P += ["</abstracts>", "", f"There are {len(cl)} claims: " + ", ".join(c["claim_id"] for c in cl) + ". Give one "
          "verdict, with the direction, for each with submit_check."]
    return "\n".join(P) + "\n"


# ----------------------------------------------------------------------------- submit_check
def submit_check(ctx, payload):
    ctx.submit_attempts += 1
    errs = TL.schema_errors(payload, CHECK_TOOL)
    if errs:
        raise TL.ToolError("The check was not accepted; fix these and call submit_check again:\n- "
                           + "\n- ".join(errs[:30]))
    p = json.loads(json.dumps(payload))
    want = ctx.notes.get("claim_ids")
    if want:
        got = [v["claim_id"].strip() for v in p["verdicts"]]
        miss = [c for c in want if c not in got]
        extra = [c for c in got if c not in want]
        dup = [c for c, n in Counter(got).items() if n > 1]
        if (miss or extra or dup) and not ctx.notes.get("ids_warned"):
            ctx.notes["ids_warned"] = True
            msg = ["The check was not accepted yet:"]
            if miss:
                msg.append(f"- no verdict for: {', '.join(miss)}")
            if extra:
                msg.append(f"- unknown claim ids: {', '.join(extra)}")
            if dup:
                msg.append(f"- more than one verdict for: {', '.join(dup)}")
            msg.append("Give exactly one verdict per claim id and call submit_check again.")
            raise TL.ToolError("\n".join(msg))
    ctx.submitted = p
    return "Check received. End your turn."


def _needed_direction(sec, it):
    """The direction of the papers' relation a claim needs, compared with the data (None: no direction)."""
    v = it.get("verdict") if sec == "connection_verdicts" else sec
    if v in ("established", "indirect"):
        return SAME
    if v == "contradicted":
        return OPPOSITE
    return None


def apply_check(review, check):
    """(review with item["check"] = {verdict, direction, reason} per checked claim, summary {summary, counts,
    unmatched, supported, partly, not_supported, not_checkable})."""
    r = copy.deepcopy(review)
    by_id = {}
    for v in (check or {}).get("verdicts") or []:
        by_id.setdefault(str(v.get("claim_id", "")).strip(), v)
    cnt = Counter()
    for c in claims(r):
        v = by_id.pop(c["claim_id"], None)
        if v is None:
            continue
        it = r[c["section"]][c["index"]]
        verdict = v.get("verdict") if v.get("verdict") in CHECK_VERDICTS else "not checkable"
        direction = v.get("direction") if v.get("direction") in DIRECTIONS else "not stated"
        reason = v.get("reason", "")
        need = _needed_direction(c["section"], it)
        if verdict in ("supported", "partly") and need and direction in (SAME, OPPOSITE) and direction != need:
            said = {SAME: "in the data's direction", OPPOSITE: "in the direction opposite to the data"}
            reason = (f"direction: the cited papers report the relation {said[direction]}, the claim needs it "
                      f"{said[need]} (checker's verdict: {verdict}; reason: {reason})")
            verdict = "not supported"
        it["check"] = {"verdict": verdict, "direction": direction, "reason": reason}
        cnt[verdict] += 1
    summ = {"summary": (check or {}).get("summary", ""), "counts": dict(cnt), "unmatched": sorted(by_id)}
    summ.update({STATUS_OF[k]: int(cnt.get(k, 0)) for k in CHECK_VERDICTS})
    r["citation_check"] = summ
    annotate(r)
    return r, summ


# ----------------------------------------------------------------------------- the shared contract
def _item_status(it, cits, ids_checked):
    ch = it.get("check") or {}
    if not cits and it.get("removed_citations"):
        return "citations_removed"
    if cits and ch.get("verdict") in STATUS_OF:
        return STATUS_OF[ch["verdict"]]
    if cits:
        unchecked = it.get("unchecked_citations", None if ids_checked else cits)
        if unchecked is None or unchecked:
            return "unchecked"
    return "not_checkable"


def annotate(review, ids_checked=None):
    """check_status and shown_verdict on every item (see the module docstring); in place, returns the review.
    ids_checked: True after check_ids, False when it did not run (every citation unchecked), None: read from the
    items' unchecked_citations (an item without that list counts as unchecked)."""
    for sec in ITEM_SECTIONS:
        for it in review.get(sec) or []:
            cits = [TL.norm_citation(c) or c for c in it.get("citations") or []]
            if sec != "connection_verdicts" and not cits and not it.get("removed_citations"):
                it.pop("check_status", None)
                it.pop("shown_verdict", None)
                continue
            if ids_checked is False:
                it.pop("unchecked_citations", None)
            st = _item_status(it, cits, ids_checked)
            it["check_status"] = st
            verdict = (it.get("verdict") or "") if sec == "connection_verdicts" else sec
            it["shown_verdict"] = "unverified" if st in ("not_supported", "citations_removed") else verdict
    return review


def _llm_block(llm, mode, review):
    llm = dict(llm or {})
    raw = str(llm.get("status") or "")
    if mode != "llm":
        status, detail = "not_run", f"--verify {mode}"
    elif raw in ("done", "not_run", "failed") and "detail" in llm:     # already in this form (a stored review)
        status, detail = raw, str(llm.get("detail") or "")
    elif raw == "done":
        status, detail = "done", ""
    elif raw.startswith("no claims"):
        status, detail = "done", "no claim cites a paper"
    elif not raw or raw.startswith(("not run", "not_run")):
        status, detail = "not_run", raw[7:].lstrip(": ") or "not run"
    else:
        status = "failed"
        detail = raw + (f": {llm['error']}" if llm.get("error") and raw != "failed" else
                        f" ({llm['error']})" if llm.get("error") else "")
    c = Counter((it.get("check") or {}).get("verdict") for sec in SECTION_PREFIX for it in review.get(sec) or []
                if it.get("check"))
    out = {k: v for k, v in llm.items() if k not in ("status",)}
    out.update({"status": status, "detail": detail})
    out.update({STATUS_OF[k]: int(c.get(k, 0)) for k in CHECK_VERDICTS})
    return out


def _ids_block(report, mode, review):
    n = len({c for c, _s, _i in TL.cited_ids(review)} | set().union(*_removed_ids(review)))
    if mode not in ("ids", "llm"):
        return {"status": "not_run", "detail": f"--verify {mode}", "checked": 0, "removed": 0, "unchecked": n,
                "retracted": 0, "n_cited": n}
    if not report or report.get("error"):
        err = str((report or {}).get("error") or "not run")
        st = "not_run" if err.startswith(("not run", "not_run")) else "failed"
        return {"status": st, "detail": err[7:].lstrip(": ") if st == "not_run" else err, "checked": 0,
                "removed": 0, "unchecked": n, "retracted": 0, "n_cited": n}
    out = dict(report)
    out.setdefault("status", "done")
    for k in ("checked", "removed", "unchecked", "retracted"):
        v = out.get(k)
        out[k] = len(v) if isinstance(v, list) else int(v or 0)
    return out


# drop_self_check: a sentence the agent writes to vouch for its own verification. A clause is a self-check when it is
# only 'citations / references / claims ... were checked / verified ...' followed by words naming what against
# (PubMed, abstracts ...: _CHECKED_AGAINST) and names such a source; a disclaimer when it is only '(this review
# is / was) AI-generated (literature review ...; and not checked by a person)', 'verify before relying on it' or 'not
# checked by a person'. Any other word (a gene, 'pair',
# 'none', a number, a citation) makes the clause content, and a sentence with content is kept whole.
_SELF_HEAD = re.compile(
    r"(?:(?:all|the|its|every|each|these|this|my|our|cited)\s+)*(?:citations?|references?|claims?|PMIDs?|DOIs?|"
    r"papers?|sources?|ids)\s+(?:(?:in|of|cited\s+in)\s+(?:this|the)\s+(?:note|review|text|summary)\s+)?"
    r"(?:were|have\s+been|has\s+been|had\s+been|are|was|is)\s+(?:all\s+|each\s+|also\s+)?"
    r"(?:checked|verified|confirmed|validated|cross-checked|looked\s+up)\b(?P<tail>.*)", re.I | re.S)
_DISCLAIMER = re.compile(
    r"(?:(?:this|the)\s+(?:note|review|text|summary)\s+(?:is|was|has\s+been)\s+)?(?:an?\s+)?AI-generated\b(?P<tail>.*)"
    r"|verify\s+(?:it\s+|this\s+|them\s+)?before\s+relying\s+on\s+(?:it|this|them)"
    r"|not\s+(?:checked|reviewed)\s+by\s+a\s+(?:person|human)", re.I | re.S)
_CHECK_SOURCE = re.compile(r"PubMed|abstracts?\b|Crossref|Europe\s*PMC|citation\s+checker|NCBI", re.I)
_CHECKED_AGAINST = frozenset(
    "against in with by using via on and or the their its each every all cited original pubmed europe pmc crossref "
    "ncbi abstract abstracts full text texts record records database databases paper papers citation citations "
    "checker tool tools metadata retraction retractions status automatically literature review of this run run's "
    "data note summary agent model a an for it them not person human checked reviewed verified is was been has".split())
# a sentence ends after . ! ? (and the emphasis closers right after it), or at a line break before a list item or a
# quoted line; the next line's indentation stays with the next sentence (it may nest a list)
_SENT_END = re.compile(r"(?<=[.!?])[_*]*[ \t]*\n?(?=[ \t]*\S)|\n(?=[ \t]*(?:[-*+>]|\d+[.)])\s)")
_LEAD = re.compile(r"^[\s>]*(?:[-*+]\s+|\d+[.)]\s+)?[_*]*\s*")
_ITEM = re.compile(r"[ \t>]*(?:[-*+]|\d{1,9}[.)])[ \t]+")                    # a line's list marker (after '>')
_MARKER_ONLY = re.compile(r"[ \t>]*(?:(?:[-*+]|\d{1,9}[.)])[ \t]+)*\d{1,9}\.")  # a line so far: only a list marker
_LINE_LEAD = re.compile(r"[ \t>]*(?:(?:[-*+]|\d{1,9}[.)])[ \t]+)*")
_EM_RUN = re.compile(r"[_*]+")


def _only_source_words(tail):
    """True when tail (what follows 'were checked' / 'AI-generated') has no word outside _CHECKED_AGAINST."""
    return all(w.lower() in _CHECKED_AGAINST for w in re.findall(r"[^\W_][\w'-]*", tail or ""))


def _clause_kind(t):
    """'self' (a self-check clause), 'disclaimer', 'content' or 'empty' (see _SELF_HEAD above)."""
    t = _LEAD.sub("", t).strip().rstrip("_*").strip().rstrip(".!").strip()
    if not t:
        return "empty"
    m = _SELF_HEAD.fullmatch(t)
    if m and _CHECK_SOURCE.search(t) and _only_source_words(m.group("tail")):
        return "self"
    m = _DISCLAIMER.fullmatch(t)
    if m and _only_source_words(m.groupdict().get("tail")):
        return "disclaimer"
    return "content"


def _punct(ch):
    return not ch.isalnum() and not ch.isspace()


def _em_pairs(sents, starts):
    """[(run, i, j)]: emphasis spans of a paragraph cut into sentences, opened by the delimiter run 'run' in
    sentence i and closed in sentence j (CommonMark's flanking rules, a closer matching the last opener of the same
    run; code spans and line-initial list markers skipped)."""
    stack, pairs = [], []
    for i, x in enumerate(sents):
        t = re.sub(r"`[^`\n]*`", lambda m: "x" * len(m.group(0)), x)
        lead = _LINE_LEAD.match(t).end() if starts[i] else 0
        for m in _EM_RUN.finditer(t, lead):
            a, b, run = m.start(), m.end(), m.group(0)
            prev = t[a - 1] if a else " "
            nxt = t[b] if b < len(t) else " "
            if prev == "\\":
                continue
            lf = not nxt.isspace() and (not _punct(nxt) or prev.isspace() or _punct(prev))
            rf = not prev.isspace() and (not _punct(prev) or nxt.isspace() or _punct(nxt))
            can_open, can_close = ((lf and (not rf or _punct(prev)), rf and (not lf or _punct(nxt))) if "_" in run
                                   else (lf, rf))
            k = next((n for n in range(len(stack) - 1, -1, -1) if stack[n][0] == run[::-1]), None) if can_close \
                else None
            if k is not None:
                pairs.append((stack[k][0], stack[k][1], i))
                del stack[k:]
            elif can_open:
                stack = stack[-99:] + [(run, i)]
    return pairs


def _drop_in_paragraph(p):
    """p without its self-check sentences (and, when it had one, its disclaimer sentences); p if it has none. The
    structure around a dropped sentence stays: a list item whose every sentence goes loses its marker line, one
    that goes on keeps its marker (and a nested list its indentation), and an emphasis span opened or closed in a
    dropped sentence is closed or opened in the kept text it covered."""
    if "```" in p or "~~~" in p:
        return p
    cuts, ls, pos = [0], 0, 0
    for m in _SENT_END.finditer(p):
        nl = p.rfind("\n", pos, m.start())
        ls, pos = (nl + 1 if nl >= 0 else ls), m.start()
        if m.start() - ls > 40 or not _MARKER_ONLY.fullmatch(p, ls, m.start()):   # not the '.' of a leading '2.'
            cuts.append(m.end())
    cuts.append(len(p))
    sents = []
    for x in (p[cuts[i]:cuts[i + 1]] for i in range(len(cuts) - 1) if cuts[i] < cuts[i + 1]):
        if sents and not x.strip(" \t\n_*"):     # the closing '_' / '**' of the paragraph's last sentence (split
            sents[-1] += x                       # off at its end): it shares that sentence's fate
        else:
            sents.append(x)
    kinds = []
    for x in sents:
        k = {_clause_kind(c) for c in re.split(r";|\s[-–—]\s", x)} - {"empty"}
        kinds.append("empty" if not k else "self" if k <= {"self", "disclaimer"} and "self" in k else
                     "disclaimer" if k == {"disclaimer"} else "content")
    if "self" not in kinds:
        return p
    starts = [i == 0 or sents[i - 1].endswith("\n") for i in range(len(sents))]
    kept = [k == "content" for k in kinds]
    pre, post = [[] for _ in sents], [[] for _ in sents]
    for run, i, j in _em_pairs(sents, starts):
        inside = [n for n in range(i + (not kept[i]), j + kept[j]) if kept[n]]
        if i != j and inside and not (kept[i] and kept[j]):
            if not kept[i]:
                pre[inside[0]].append(run)       # its opener went: the first kept sentence it covered opens it
            if not kept[j]:
                post[inside[-1]].insert(0, run[::-1])   # its closer went: the last kept sentence it covered closes it
    keep, pending = [], None                     # pending: the marker of a dropped sentence whose list item goes on
    for n, (x, k) in enumerate(zip(sents, kinds)):
        ends_line = re.search(r"\n[ \t]*$", x)
        item = _ITEM.match(x) if starts[n] else None
        if k == "content":
            if pre[n]:
                e = _LINE_LEAD.match(x).end()
                x = x[:e] + "".join(pre[n]) + x[e:]
            if post[n]:
                e = re.search(r"[ \t]*\n?[ \t]*$", x).start()
                x = x[:e] + "".join(post[n]) + x[e:]
            if pending is not None and not item:
                x = pending + (re.sub(r"^[ \t>]*" if ">" in pending else r"^[ \t]*", "", x) if starts[n] else x)
            pending = None
            keep.append(x)
            continue
        if item:
            pending = item.group(0)              # it opened a list item: kept only if the item goes on
        if keep and not keep[-1].endswith("\n") and ends_line:
            keep.append("\n")                    # a dropped sentence that ended a line: the next line stays one
    out = re.sub(r"[ \t]+\n", "\n", "".join(keep)).rstrip()
    w = re.match(r"^\s*([_*]+)(?=[^\s_*])", p)
    if out and w and re.search(r"[^\s_*]" + re.escape(w.group(1)) + r"\s*$", p):   # emphasis around the paragraph
        out = (w.group(1) if not out.lstrip().startswith(w.group(1)) else "") + out.strip()
        out += "" if out.endswith(w.group(1)) else w.group(1)
    return out


def drop_self_check(md):
    """note_markdown without the sentences in which the agent vouches for its own verification (the footer an earlier
    writing-the-note template asked for: '_AI-generated ...; citations were checked against PubMed and their
    abstracts. Verify before relying on it._'): a sentence made only of such a claim - citations / references /
    claims were checked or verified, against PubMed, abstracts ... and nothing else - and, in the same paragraph,
    disclaimer sentences ('AI-generated ...', 'Verify before relying on it'). A sentence that says anything more (a
    finding, a gene, a number) is kept whole, and so is the rest of its paragraph; a paragraph left empty goes. What
    surrounds a dropped sentence keeps its form: a list item left empty goes with its marker, one that goes on keeps
    it, a nested item its indentation, and emphasis opened or closed in the dropped sentence stays balanced."""
    if not md:
        return md
    paras = re.split(r"(\n[ \t]*\n)", md)
    out, changed = [], False
    for i in range(0, len(paras), 2):
        q = _drop_in_paragraph(paras[i])
        changed |= q != paras[i]
        if q.strip():
            out += [q, paras[i + 1] if i + 1 < len(paras) else ""]
    if not changed:
        return md
    res = "".join(out).rstrip()
    return res + "\n" if res else res


def finalize(review, mode, ids_report=None, llm=None):
    """The review to store (a copy): annotate(), "verification" and "note_footer" (see the module docstring); a
    sentence of the note in which the agent only says its citations were checked is dropped (drop_self_check)."""
    r = copy.deepcopy(review)
    if r.get("note_markdown"):
        r["note_markdown"] = drop_self_check(r["note_markdown"])
    ids = _ids_block(ids_report, mode, r)
    annotate(r, ids_checked=ids["status"] == "done")
    ver = {"mode": mode, "ids": ids, "llm": _llm_block(llm, mode, r),
           "counts": counts(r, ids.get("same_paper") or {})}
    r["verification"] = ver
    r["note_footer"] = note_footer(ver)
    return r


def _n(n, one):
    return f"{n} {one if n == 1 else one + 's'}"


def note_footer(verification):
    """The provenance line under a review's note, generated from the verification counts (the agent never writes
    one): what was checked, what was removed, what could not be checked."""
    ver = verification or {}
    ids, llm, mode = ver.get("ids") or {}, ver.get("llm") or {}, ver.get("mode")
    head = "_AI-generated literature review of this run's data, not checked by a person."
    if mode not in ("ids", "llm"):
        return head + " Its citations were not checked (verification off). Verify before relying on it._"
    if ids.get("status") == "not_run":
        s = head + f" Its cited ids were not looked up ({_clip(ids.get('detail')) or 'not run'})."
    elif ids.get("status") != "done":
        s = head + f" The id check failed ({_clip(ids.get('detail'))}): its citations were not verified."
    else:
        s = (head + f" Cited ids looked up in PubMed / Crossref: {ids.get('checked', 0)} checked, "
             f"{ids.get('removed', 0)} removed as not found")
        if ids.get("unchecked"):
            s += f", {ids['unchecked']} could not be checked (service unavailable)"
        if ids.get("retracted"):
            s += f", {_n(ids['retracted'], 'retracted paper')} (cited, not support)"
        if ids.get("note_removed"):
            s += f"; {_n(ids['note_removed'], 'paper')} cited only in the text removed"
        s += "."
    st = llm.get("status")
    if mode == "llm" and st == "done" and llm.get("detail"):
        s += " No claim cites a paper, so none was checked against abstracts."
    elif mode == "llm" and st == "done":
        s += (f" Claims checked against the abstracts they cite (citation checker): {llm.get('supported', 0)} "
              f"supported, {llm.get('partly', 0)} partly, {llm.get('not_supported', 0)} not supported, "
              f"{llm.get('not_checkable', 0)} not checkable.")
    elif mode == "llm":
        s += f" Claims not checked against the abstracts ({_clip(llm.get('detail')) or st or 'not run'})."
    else:
        s += " Claims not checked against the abstracts (--verify ids)."
    return s + " Verify before relying on it._"


def _clip(x, n=120):
    t = re.sub(r"[\s_*`]+", " ", str(x or "")).strip()
    return t if len(t) <= n else t[:n - 3] + "..."


def counts(review, same=None):
    """Verification counts of a (checked) review. same: {id: the id standing for its paper} (check_ids' report
    "same_paper"; default: the review's verification), so that a paper cited under its PMID and its DOI counts once
    in n_citations."""
    if same is None:
        same = ((review.get("verification") or {}).get("ids") or {}).get("same_paper") or {}
    c = Counter()
    for sec in ITEM_SECTIONS:
        for it in review.get(sec) or []:
            if sec in SECTION_PREFIX:
                if it.get("citations"):
                    c["items_citing"] += 1
                if it.get("unverified"):
                    c["unverified_items"] += 1
                c["removed_citations"] += len(it.get("removed_citations") or [])
                c["retracted_citations"] += len(it.get("retracted_citations") or [])
                c["items_citing_retracted"] += bool(it.get("retracted_citations"))
                ch = it.get("check")
                if ch:
                    c["claims_checked"] += 1
                    c[ch["verdict"]] += 1
            if it.get("check_status"):
                c["status_" + it["check_status"]] += 1
    keys = ("items_citing", "claims_checked", "supported", "partly", "not supported", "not checkable",
            "unverified_items", "removed_citations", "retracted_citations", "items_citing_retracted")
    out = {k: int(c.get(k, 0)) for k in keys}
    out.update({"status_" + s: int(c.get("status_" + s, 0)) for s in CHECK_STATUSES})
    nf, no = _removed_ids(review)
    out["note_removed"] = len(no)
    out["n_citations"] = len({same.get(x, x) for x in {x for x, _s, _i in TL.cited_ids(review)} | nf | no})
    return out
