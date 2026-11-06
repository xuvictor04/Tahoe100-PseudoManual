"""verify - checking a submitted review: do the cited papers exist, and do their abstracts say what is claimed?

    check_ids(review, ctx) -> (checked_review, report)
        every cited PMID is looked up with PubMed esummary, every DOI in Europe PMC and then Crossref. A citation
        that does not exist is removed from its item, and the item gets "unverified": true and
        "removed_citations": [...]; links to it in note_markdown are replaced by 'PMID:n (citation removed: not
        found in PubMed)'. Retracted papers stay cited but are listed (report["retracted"], item
        "retracted_citations"). Ids that could not be checked (service down) are kept and listed in
        report["unchecked"]. Ids cited without having been retrieved in the session (ctx.read_ids / ctx.seen_ids)
        are flagged per item ("not_retrieved") and in report["not_retrieved_in_session"]. The input is not
        modified.
    claims(review) -> list of {claim_id, section, index, claim, citations}
        the checkable claims: items of established (E1, E2 ...), missing (M..), contradicted (C..) and
        connection_verdicts (V..) that cite at least one paper.
    fetch_abstracts(review, ctx) -> {citation id: record text or None}
        PubMed records for PMIDs, Europe PMC abstracts for DOIs (None: no abstract available).
    build_check_prompt(review, abstracts, entity=None) -> str
        the user message of the citation-checker agent: each claim with its id and citations, then each cited
        abstract once.
    CHECK_TOOL
        the strict submit_check tool: {verdicts: [{claim_id, verdict, reason}], summary}; verdict one of
        supported / partly / not supported / not checkable.
    submit_check(ctx, payload) -> str
        validates a submit_check call (executed via tools.execute); with ctx.notes["claim_ids"] set by the runner,
        every claim id must get exactly one verdict (one correction allowed). The payload goes to ctx.submitted.
    apply_check(review, check) -> (review, summary)
        each checked item gets "check": {verdict, reason}; review["citation_check"] = {summary, counts}.
    counts(review) -> dict
        verification counts for the vault callout: claims checked, per verdict, unverified items, removed
        citations, retracted citations.

The stored review (runner) = the submitted payload after check_ids (and apply_check with --verify llm), plus
"verification": {"ids": report, "llm": summary or None, "counts": counts(review)}.
"""

import copy
import json
import re
from collections import Counter

from . import tools as TL

CHECK_VERDICTS = ("supported", "partly", "not supported", "not checkable")
SECTION_PREFIX = {"established": "E", "missing": "M", "contradicted": "C", "connection_verdicts": "V"}
VERDICT_MEANING = {
    "established": "a cited paper reports this relation (co-regulation, the same pathway or complex, direct "
                   "regulation, or the drug's known effect)",
    "indirect": "the cited papers place both in a pathway or process that is known to be co-regulated (e.g. by "
                "the same drug class or transcription factor), without a paper on the pair itself",
    "plausible": "consistent with known biology, but no paper on the pair",
    "unexpected": "no support was found after searching",
    "contradicted": "a cited paper reports the opposite direction",
}

CHECK_TOOL = {
    "name": "submit_check",
    "description": (
        "Submit the verdicts of the citation check; this ends the check. Give exactly one verdict for every claim "
        "id listed in the request: supported (the cited abstracts state the claim's literature content), partly "
        "(they support part of it, or a weaker or narrower version), not supported (they do not say it, or say "
        "something else or the opposite), not checkable (no abstract available, or the claim rests on full-text "
        "content the abstracts do not show). The reason names the PMID / DOI that decided the verdict and quotes "
        "or closely paraphrases the deciding words. If the call returns an error, fix the listed problems and call "
        "it again."),
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
                        "reason": {"type": "string",
                                   "description": "one or two sentences: which citation decided it and the words "
                                                  "that did"},
                    },
                    "required": ["claim_id", "verdict", "reason"],
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


def check_ids(review, ctx):
    """(checked copy of the review, report); see the module docstring."""
    r = copy.deepcopy(review)
    ids = list(dict.fromkeys(c for c, _s, _i in TL.cited_ids(r)))
    pmids = [c for c in ids if c.startswith("PMID:")]
    dois = [c for c in ids if c.startswith("DOI:")]
    missing, unchecked, retracted, found = [], [], [], []
    if pmids:
        try:
            sm = TL.esummary_records(ctx, [c.split(":", 1)[1] for c in pmids])
            for c in pmids:
                s = sm.get(c.split(":", 1)[1])
                if s is None:
                    missing.append(c)
                else:
                    found.append(c)
                    if any("Retract" in p for p in s.get("pubtype") or []):
                        retracted.append(c)
        except TL.ToolError:
            unchecked += pmids
    for c in dois:
        doi = c.split(":", 1)[1]
        try:
            hits, _res = TL.europepmc_records(ctx, f'DOI:"{doi}"', 1)
            ok = hits > 0 or TL.crossref_exists(ctx, doi)
            (found if ok else missing).append(c)
        except TL.ToolError:
            unchecked.append(c)
    gone = set(missing)
    have = set(ctx.read_ids) | {x for x in ctx.seen_ids if x.startswith("DOI:")}
    not_retrieved = [c for c in ids if c not in have and c not in gone]
    n_unverified = 0
    for sec in SECTION_PREFIX:
        for it in r.get(sec) or []:
            cits = [TL.norm_citation(c) or c for c in it.get("citations") or []]
            rm = [c for c in cits if c in gone]
            if rm:
                it["citations"] = [c for c in cits if c not in gone]
                it["removed_citations"] = rm
                it["unverified"] = True
                n_unverified += 1
            rt = [c for c in it.get("citations") or [] if c in retracted]
            if rt:
                it["retracted_citations"] = rt
            nr = [c for c in it.get("citations") or [] if c in not_retrieved]
            if nr:
                it["not_retrieved"] = nr
    if gone and r.get("note_markdown"):
        r["note_markdown"] = _strip_from_note(r["note_markdown"], gone)
    report = {"n_cited": len(ids), "pmids_checked": len(pmids) - sum(1 for c in unchecked if c.startswith("PMID:")),
              "dois_checked": len(dois) - sum(1 for c in unchecked if c.startswith("DOI:")), "found": len(found),
              "missing": missing, "retracted": retracted, "unchecked": unchecked,
              "not_retrieved_in_session": not_retrieved, "items_unverified": n_unverified}
    return r, report


def _strip_from_note(md, gone):
    def where(c):
        return "PubMed" if c.startswith("PMID:") else "Crossref or Europe PMC"
    for c in gone:
        v = c.split(":", 1)[1]
        repl = f"{c} (citation removed: not found in {where(c)})"
        if c.startswith("PMID:"):
            md = re.sub(r"\[[^\]]*\]\(https?://pubmed\.ncbi\.nlm\.nih\.gov/" + re.escape(v) + r"/?\)", repl, md)
            md = re.sub(r"(?<![\w/])PMID\s*:?\s*" + re.escape(v) + r"\b(?! \(citation removed)", repl, md)
        else:
            md = re.sub(r"\[[^\]]*\]\(https?://(?:dx\.)?doi\.org/" + re.escape(v) + r"\)", repl, md, flags=re.I)
    return md


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
        return (f"{entity_name} and {it.get('partner', '')}: verdict '{v}', i.e. "
                f"{VERDICT_MEANING.get(v, v)}")
    return ""


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
            out.append({"claim_id": f"{pre}{i + 1}", "section": sec, "index": i,
                        "claim": _claim_text(sec, it, nm), "citations": cits})
    return out


def fetch_abstracts(review, ctx):
    """{citation id: record text, or None when no abstract is available} for every id the claims cite."""
    ids = list(dict.fromkeys(c for cl in claims(review) for c in cl["citations"]))
    out = {}
    pm = [c.split(":", 1)[1] for c in ids if c.startswith("PMID:")]
    if pm:
        try:
            recs = TL.pubmed_records(ctx, pm)
        except TL.ToolError:
            recs = {}
        for p in pm:
            r = recs.get(p)
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
            kind = "PREPRINT (not peer reviewed)" if x.get("source") == "PPR" else (x.get("pubType") or "")
            out[c] = (f"=== {c} ===\nTitle: {TL.clean_markup(x.get('title'))}\nJournal: "
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
         "papers each claim cites. Judge only what the literature part of each claim says; the review's Tahoe data "
         "numbers are not part of the claims and are not yours to check.", "", "<claims>"]
    for c in cl:
        P.append(f"[{c['claim_id']}] ({c['section']}) {c['claim']}")
        P.append(f"    cites: {', '.join(c['citations'])}")
    P += ["</claims>", "", "<abstracts>"]
    for cid in dict.fromkeys(x for c in cl for x in c["citations"]):
        t = abstracts.get(cid)
        P.append(t if t else f"=== {cid} ===\n(no abstract available: claims resting only on this citation are "
                             "not checkable)")
        P.append("")
    P += ["</abstracts>", "", f"There are {len(cl)} claims: " + ", ".join(c["claim_id"] for c in cl) + ". Give one "
          "verdict for each with submit_check."]
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


def apply_check(review, check):
    """(review with item["check"] = {verdict, reason} per checked claim, summary {summary, counts, unmatched})."""
    r = copy.deepcopy(review)
    by_id = {}
    for v in (check or {}).get("verdicts") or []:
        by_id.setdefault(str(v.get("claim_id", "")).strip(), v)
    cnt = Counter()
    for c in claims(r):
        v = by_id.pop(c["claim_id"], None)
        if v is None:
            continue
        verdict = v.get("verdict") if v.get("verdict") in CHECK_VERDICTS else "not checkable"
        r[c["section"]][c["index"]]["check"] = {"verdict": verdict, "reason": v.get("reason", "")}
        cnt[verdict] += 1
    summ = {"summary": (check or {}).get("summary", ""), "counts": dict(cnt), "unmatched": sorted(by_id)}
    r["citation_check"] = summ
    return r, summ


def counts(review):
    """Verification counts of a (checked) review."""
    c = Counter()
    for sec in SECTION_PREFIX:
        for it in review.get(sec) or []:
            if it.get("citations"):
                c["items_citing"] += 1
            if it.get("unverified"):
                c["unverified_items"] += 1
            c["removed_citations"] += len(it.get("removed_citations") or [])
            c["retracted_citations"] += len(it.get("retracted_citations") or [])
            ch = it.get("check")
            if ch:
                c["claims_checked"] += 1
                c[ch["verdict"]] += 1
    out = {k: int(c.get(k, 0)) for k in ("items_citing", "claims_checked", "supported", "partly", "not supported",
                                         "not checkable", "unverified_items", "removed_citations",
                                         "retracted_citations")}
    out["n_citations"] = len({x for x, _s, _i in TL.cited_ids(review)})
    return out
