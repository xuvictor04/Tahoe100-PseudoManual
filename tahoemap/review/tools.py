"""tools - the custom tools of the review agents (executed here) and the server tools (executed by Anthropic).

    TOOLS                       name -> tool definition (all strict: additionalProperties false, every property
                                required); submit_check lives in verify.CHECK_TOOL
    custom_tools(names)         the definitions of those names, in that order (submit_check included)
    server_tools(web, max_uses, names=None)
                                web_search_20260209 / web_fetch_20260209 definitions, [] when web is False
    tool_definitions(agent, web=True, max_uses=5)
                                everything one agent declares (custom then server tools), in a stable order
    execute(name, input, ctx) -> str
                                run one custom tool call; returns the result text for the tool_result block.
                                Raises ToolError for a call the model should correct or retry (bad input, nothing
                                found under a name, a service down after retries): send str(e) back with
                                is_error = true. submit_review / submit_check: on a valid payload the normalised
                                payload is stored in ctx.submitted (the runner then ends the loop) and an
                                acknowledgement is returned; otherwise ToolError lists what to fix.
    ToolContext(out, entity, cache_dir, http)
                                per attempt: the output folder, the entity under review, the cache folder
                                (default OUT/review/cache) and HttpSettings; it records what the agent retrieved
                                (seen_ids, read_ids), the calls made and the submitted payload.

Literature services, over urllib (no dependency), with a per-service rate limit shared by every thread of the
process, retries with exponential backoff (429 / 5xx / network errors; Retry-After honoured) and an on-disk cache:
    PubMed (NCBI E-utilities): esearch + esummary (pubmed_search), efetch (pubmed_abstracts); 3 requests/s, or 10
        with NCBI_API_KEY; the polite `tool` / `email` parameters come from HttpSettings (env NCBI_TOOL,
        NCBI_EMAIL).
    Europe PMC REST search (europepmc_search; also abstracts of DOI-only papers for verification): 3 requests/s.
    Crossref works/<doi> (verification of DOIs: existence when Europe PMC does not know them, and retraction
        status from the record's update notices): 3 requests/s, `mailto` when known.
Cache: OUT/review/cache/<service>/<xx>/<sha1>.json. Records fetched by id (esummary, efetch, Crossref) are kept
forever, except "does not exist" answers (1 day: a brand-new PMID can be missing for a few hours); search results
are reused for HttpSettings.search_max_age_days (default 30). API keys and e-mail addresses never enter the cache
key or the cached URL.
"""

import hashlib
import html
import json
import os
import random
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass, field

from . import review_dir

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CROSSREF = "https://api.crossref.org/works/"
PUBMED_URL = "https://pubmed.ncbi.nlm.nih.gov/{}/"
DOI_URL = "https://doi.org/{}"

MAX_SEARCH = 20
MAX_ABSTRACTS = 10
ABSTRACT_CHARS = 4_000           # one abstract in a tool result (longer ones are cut, with a note)
RESULT_CHARS = 40_000            # one tool result
LOOKUP_KINDS = ("gene", "drug", "line", "pair")
CONFIDENCE = ("high", "medium", "low")
VERDICTS = ("established", "indirect", "plausible", "unexpected", "contradicted")
MISSING_SOURCES = ("STRING", "pathway", "literature")


class ToolError(Exception):
    """A tool call the model should see as an error (tool_result is_error = true, content = str(e))."""


class NotFoundError(ToolError):
    """The service says the requested record does not exist (HTTP 404)."""


# ----------------------------------------------------------------------------- settings and context
@dataclass
class HttpSettings:
    tool: str = "tahoemap"
    email: str = ""                  # NCBI and Crossref ask for a contact address (env NCBI_EMAIL)
    ncbi_api_key: str = ""           # env NCBI_API_KEY: 10 requests/s instead of 3
    rate: float = 0.0                # requests/s per service; 0 = 3 (10 for NCBI with a key)
    timeout: float = 30.0
    retries: int = 4
    backoff: float = 1.5             # seconds, doubled per retry (+ jitter), at most 60
    offline: bool = False            # answer from the cache only (tests)
    search_max_age_days: float = 30.0
    user_agent: str = "tahoemap-review/1 (Tahoe-100M gene map literature review; python urllib)"

    @classmethod
    def from_env(cls, **kw):
        s = cls(tool=os.environ.get("NCBI_TOOL", "tahoemap"), email=os.environ.get("NCBI_EMAIL", ""),
                ncbi_api_key=os.environ.get("NCBI_API_KEY", ""))
        for k, v in kw.items():
            setattr(s, k, v)
        return s

    def rate_for(self, service):
        if self.rate and self.rate > 0:
            return float(self.rate)
        return 10.0 if service == "ncbi" and self.ncbi_api_key else 3.0


@dataclass
class ToolContext:
    out: str
    entity: dict = field(default_factory=dict)       # {"kind", "name", "entity_id"}
    cache_dir: str = ""                               # default OUT/review/cache
    http: HttpSettings = field(default_factory=HttpSettings.from_env)
    seen_ids: set = field(default_factory=set)        # 'PMID:n' / 'DOI:x' returned by any search or fetch
    read_ids: set = field(default_factory=set)        # 'PMID:n' whose abstract record was fetched
    calls: Counter = field(default_factory=Counter)
    submitted: dict = None                            # the normalised payload of a valid submit call
    submit_attempts: int = 0
    notes: dict = field(default_factory=dict)         # e.g. {"not_retrieved": [...]} for the stored review

    def __post_init__(self):
        if not self.cache_dir:
            self.cache_dir = os.path.join(self.out, "review", "cache")


def make_context(out, entity=None, **http):
    """A ToolContext with settings from the environment (+ HttpSettings overrides)."""
    if entity is not None and not isinstance(entity, dict):
        entity = {"kind": entity.kind, "name": entity.name, "entity_id": entity.entity_id}
    review_dir(out, "cache")
    return ToolContext(out=out, entity=entity or {}, http=HttpSettings.from_env(**http))


# ----------------------------------------------------------------------------- HTTP: rate limit, retries, cache
class _Limiter:
    def __init__(self, rate):
        self.interval = 1.0 / max(rate, 0.1)
        self.lock = threading.Lock()
        self.next = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            t = max(now, self.next)
            self.next = t + self.interval
        if t > now:
            time.sleep(t - now)


_LIMITERS = {}
_LIM_LOCK = threading.Lock()


def _limiter(service, rate):
    with _LIM_LOCK:
        key = (service, rate)
        if key not in _LIMITERS:
            _LIMITERS[key] = _Limiter(rate)
        return _LIMITERS[key]


_SECRET_PARAMS = ("api_key", "email", "tool", "mailto")


def _cache_key(url, params):
    keep = sorted((k, str(v)) for k, v in params.items() if k not in _SECRET_PARAMS)
    return hashlib.sha1((url + "?" + urllib.parse.urlencode(keep)).encode()).hexdigest(), \
        url + "?" + urllib.parse.urlencode(keep)


def _cache_path(ctx, service, key):
    return os.path.join(ctx.cache_dir, service, key[:2], key + ".json")


def cache_get(ctx, service, key, max_age_days=None):
    p = _cache_path(ctx, service, key)
    try:
        with open(p, encoding="utf-8") as fh:
            rec = json.load(fh)
    except (OSError, ValueError):
        return None
    if max_age_days is not None and time.time() - float(rec.get("fetched", 0)) > max_age_days * 86400:
        return None
    return rec


def cache_put(ctx, service, key, rec):
    """Best effort: the cache only saves look-ups. A write that fails (on Windows: another thread or process reading
    that entry at that moment, which forbids replacing it; a full disk) is tried again briefly, then skipped - never
    an error of the look-up, which has its answer."""
    p = _cache_path(ctx, service, key)
    rec = dict(rec, fetched=time.time())
    tmp = f"{p}.{os.getpid()}.{threading.get_ident()}.tmp"
    for wait in (0.05, 0.2, 0.5, None):
        try:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(rec, fh)
            os.replace(tmp, p)
            return True
        except OSError:
            if wait is None:
                break
            time.sleep(wait)
    try:
        os.remove(tmp)
    except OSError:
        pass
    return False


def _scrub(text, ctx):
    s = str(text)
    for secret in (ctx.http.ncbi_api_key, ctx.http.email):
        if secret:
            s = s.replace(secret, "***")
            s = s.replace(urllib.parse.quote(secret), "***")
    return s


def http_get(ctx, service, url, params, max_age_days=None, cache=True):
    """GET url?params (rate-limited per service, retried, cached). Returns the body text. Raises NotFoundError on
    404 and ToolError when the service keeps failing."""
    key, shown = _cache_key(url, params)
    if cache:
        rec = cache_get(ctx, service, key, max_age_days)
        if rec is not None:
            return rec["body"]
    if ctx.http.offline:
        raise ToolError(f"{service}: offline and not in the cache ({shown[:200]})")
    q = dict(params)
    if service == "ncbi":
        q["tool"] = ctx.http.tool
        if ctx.http.email:
            q["email"] = ctx.http.email
        if ctx.http.ncbi_api_key:
            q["api_key"] = ctx.http.ncbi_api_key
    elif service == "crossref" and ctx.http.email:
        q["mailto"] = ctx.http.email
    full = url + ("?" + urllib.parse.urlencode(q) if q else "")
    lim = _limiter(service, ctx.http.rate_for(service))
    last = ""
    for attempt in range(ctx.http.retries + 1):
        if attempt:
            wait = min(60.0, ctx.http.backoff * 2 ** (attempt - 1)) * (0.75 + 0.5 * random.random())
            time.sleep(wait)
        lim.wait()
        try:
            req = urllib.request.Request(full, headers={"User-Agent": ctx.http.user_agent,
                                                        "Accept": "application/json, text/xml;q=0.9, */*;q=0.5"})
            with urllib.request.urlopen(req, timeout=ctx.http.timeout) as r:
                body = r.read().decode("utf-8", "replace")
            if service == "ncbi" and "API rate limit exceeded" in body[:500]:
                last = "NCBI rate limit exceeded"
                continue
            if cache:
                cache_put(ctx, service, key, {"url": shown, "body": body})
            return body
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise NotFoundError(f"{service}: not found ({shown[:200]})") from None
            last = f"HTTP {e.code}"
            if e.code in (429, 500, 502, 503, 504):
                ra = e.headers.get("Retry-After") if e.headers else None
                if ra and ra.strip().isdigit():
                    time.sleep(min(60.0, float(ra)))
                continue
            raise ToolError(f"{service}: HTTP {e.code} for {shown[:200]}") from None
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            last = f"{type(e).__name__}: {_scrub(e, ctx)}"
            continue
    raise ToolError(f"{service}: no answer after {ctx.http.retries + 1} attempts ({last}); try again later or "
                    "continue without this search")


# ----------------------------------------------------------------------------- ids
_PMID = re.compile(r"^(?:pmid\s*[:#]?\s*|https?://(?:www\.)?(?:pubmed\.ncbi\.nlm\.nih\.gov|ncbi\.nlm\.nih\.gov/pubmed)/)"
                   r"?(\d{1,9})/?$", re.I)
_DOI = re.compile(r"^(?:doi\s*:?\s*|https?://(?:dx\.)?doi\.org/)?(10\.\d{4,9}(?:/|%2F)\S+)$", re.I)
# A DOI inside running text or a URL: Crossref's recommended character set (- . _ ; : / letters digits), plus the
# < > # + of old SICI DOIs and the % of URL-encoded ones, with parentheses only in balanced pairs - so
# 'DOI:10.1016/S0092-8674(00)81096-3' is read whole, and the ')' that closes a markdown link or a remark is not
# taken. trim_doi() then drops the punctuation that ends the sentence around it.
_DOI_CH = r"[-._;:/A-Za-z0-9<>#+%]"
DOI_BODY = r"10\.\d{4,9}/(?:" + _DOI_CH + r"|\(" + _DOI_CH + r"*\))+"
_DOI_WHOLE = re.compile(DOI_BODY)
# the same in a URL, whose '/' after the prefix may be percent-encoded ('doi.org/10.1000%2Fx')
DOI_URL_BODY = r"10\.\d{4,9}(?:/|%2[Ff])(?:" + _DOI_CH + r"|\(" + _DOI_CH + r"*\))+"


def trim_doi(d):
    """A DOI matched in text without trailing sentence punctuation (. , ; : quotes) or an unmatched '>' / ')'."""
    while True:
        e = d.rstrip(".,;:'\"")
        if (e.endswith(">") and e.count("<") < e.count(">")) or (e.endswith(")") and e.count("(") < e.count(")")):
            e = e[:-1]
        if e == d:
            return d
        d = e


def _decoded_doi(d):
    """d with its percent-escapes decoded when the result is still a DOI (DOI_BODY's characters only) and holds no
    '%', else None: an escape that decodes to a quote, a space, '=' ... belongs to no DOI a paper carries, and one
    that decodes to '%' ('%25') could make '%%', which Obsidian reads as the start of a comment."""
    dec = urllib.parse.unquote(d)
    return dec if "%" not in dec and _DOI_WHOLE.fullmatch(dec) else None


def clean_doi(raw):
    """(doi, rest): a DOI matched in text -> trimmed, unquoted (only when the decoded text is still a DOI: else it
    is kept as written, so a URL-encoded quote or tag never becomes one), lower-cased; rest = the trimmed-off
    characters."""
    d = trim_doi(raw)
    return (_decoded_doi(d) or d).lower(), raw[len(d):]


def norm_citation(s):
    """'PMID:123' / 'DOI:10.x/y' for a PMID or DOI in any common spelling (bare digits = PMID; doi.org URLs, also
    percent-encoded); None otherwise - also for a DOI with characters outside DOI_BODY's set (quotes, spaces,
    brackets, '=' ..., written or percent-encoded), which is no DOI a paper carries and could break the link it
    becomes."""
    t = str(s or "").strip().rstrip(".,;")
    m = _PMID.match(t)
    if m:
        return f"PMID:{int(m.group(1))}"
    m = _DOI.match(t)
    if m:
        d = _decoded_doi(trim_doi(m.group(1)))
        if d:
            return "DOI:" + d.lower()
    return None


def citation_url(cid):
    """The link of a citation id; a DOI is percent-encoded, so its ( ) < > never end a markdown link early."""
    kind, v = cid.split(":", 1)
    return PUBMED_URL.format(v) if kind == "PMID" else DOI_URL.format(urllib.parse.quote(v, safe="/"))


def cid_text(cid):
    """A citation id as text written into a note (a link's text, a removal marker): the '<' and '>' an old SICI
    DOI may carry are percent-encoded, so no text verification writes can form an HTML tag, and so is a '%' that
    another '%' follows, so none forms an Obsidian comment ('%%')."""
    return re.sub(r"%(?=%)", "%25", cid.replace("<", "%3c").replace(">", "%3e"))


def link(cid):
    """The markdown link of a citation id: [PMID:123](https://pubmed.ncbi.nlm.nih.gov/123/)."""
    return f"[{cid_text(cid)}]({citation_url(cid)})"


# ----------------------------------------------------------------------------- PubMed
def _summary_line(s):
    pid = s.get("uid", "")
    year = (s.get("pubdate") or s.get("epubdate") or "")[:4]
    pt = [p for p in s.get("pubtype") or [] if p not in ("Journal Article",)]
    doi = next((a.get("value") for a in s.get("articleids") or [] if a.get("idtype") == "doi"), "")
    au = [a.get("name", "") for a in s.get("authors") or [] if a.get("authtype", "Author") == "Author"]
    who = (au[0] + (" ... " + au[-1] if len(au) > 2 else (", " + au[1] if len(au) == 2 else ""))) if au else ""
    flags = ""
    if retraction_status(s.get("pubtype")) == "retracted":
        flags = " | RETRACTED: do not cite as support"
    elif retraction_status(s.get("pubtype")) == "notice":
        flags = " | RETRACTION NOTICE (a notice, not the retracted paper)"
    has_abs = "Has Abstract" in (s.get("attributes") or [])
    title = re.sub(r"\s+", " ", s.get("title") or "").strip()
    return (f"PMID {pid} | {year} | {s.get('source', '')} | {'; '.join(pt) or 'Journal Article'}{flags} | {title} | "
            f"{who}{f' ({len(au)} authors)' if len(au) > 2 else ''}" + (f" | DOI {doi}" if doi else "")
            + ("" if has_abs else " | no abstract"))


def retraction_status(pubtypes):
    """'retracted' (the paper was retracted: PubMed type 'Retracted Publication'), 'notice' (it is itself a
    retraction notice: 'Retraction of Publication') or '' - from PubMed or Europe PMC publication types (a list, or
    Europe PMC's '; '-separated string; any letter case)."""
    if isinstance(pubtypes, str):
        pubtypes = pubtypes.split(";")
    pt = {str(p).strip().lower() for p in pubtypes or []}
    if "retracted publication" in pt:
        return "retracted"
    if "retraction of publication" in pt:
        return "notice"
    return ""


def esummary_records(ctx, pmids):
    """pmid (str) -> esummary dict, or None when PubMed has no such record. Cached per PMID."""
    out, need = {}, []
    for p in dict.fromkeys(str(int(x)) for x in pmids):
        rec = cache_get(ctx, "ncbi_summary", p)
        if rec is not None and (rec.get("summary") is not None or time.time() - rec["fetched"] < 86400):
            out[p] = rec.get("summary")
        else:
            need.append(p)
    for i in range(0, len(need), 200):
        part = need[i:i + 200]
        body = http_get(ctx, "ncbi", ESUMMARY, {"db": "pubmed", "id": ",".join(part), "retmode": "json"},
                        cache=False)
        try:
            res = json.loads(body).get("result", {})
        except ValueError:
            raise ToolError("PubMed esummary returned an unreadable answer; try again") from None
        for p in part:
            s = res.get(p)
            s = None if (s is None or "error" in s) else s
            cache_put(ctx, "ncbi_summary", p, {"summary": s})
            out[p] = s
    return out


def _text_of(el):
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip() if el is not None else ""


def _parse_article(art):
    """One <PubmedArticle> -> dict."""
    mc = art.find("MedlineCitation")
    a = mc.find("Article") if mc is not None else None
    pmid = _text_of(mc.find("PMID")) if mc is not None else ""
    rec = {"pmid": pmid, "title": "", "journal": "", "year": "", "abstract": "", "pubtypes": [], "doi": "",
           "pmcid": "", "authors": [], "mesh": [], "retracted": False}
    if a is not None:
        rec["title"] = _text_of(a.find("ArticleTitle")) or _text_of(a.find("VernacularTitle"))
        j = a.find("Journal")
        if j is not None:
            rec["journal"] = _text_of(j.find("ISOAbbreviation")) or _text_of(j.find("Title"))
            pd_ = j.find("JournalIssue/PubDate")
            if pd_ is not None:
                rec["year"] = _text_of(pd_.find("Year")) or _text_of(pd_.find("MedlineDate"))[:4]
        parts = []
        for at in a.findall("Abstract/AbstractText"):
            lab = at.get("Label") or ""
            t = _text_of(at)
            if t:
                parts.append((lab.upper() + ": " if lab and lab.upper() != "UNLABELLED" else "") + t)
        rec["abstract"] = "\n".join(parts)
        rec["pubtypes"] = [_text_of(p) for p in a.findall("PublicationTypeList/PublicationType")]
        for au in a.findall("AuthorList/Author"):
            nm = (_text_of(au.find("LastName")) + " " + _text_of(au.find("Initials"))).strip() or \
                _text_of(au.find("CollectiveName"))
            if nm:
                rec["authors"].append(nm)
        for e in a.findall("ELocationID"):
            if e.get("EIdType") == "doi" and not rec["doi"]:
                rec["doi"] = _text_of(e)
    if mc is not None:
        rec["mesh"] = [_text_of(m.find("DescriptorName")) for m in mc.findall("MeshHeadingList/MeshHeading")]
        for c in mc.findall("CommentsCorrectionsList/CommentsCorrections"):
            if c.get("RefType") in ("RetractionIn", "RetractionOf"):
                rec["retracted"] = rec["retracted"] or c.get("RefType") == "RetractionIn"
    pdata = art.find("PubmedData")
    if pdata is not None:
        for i in pdata.findall("ArticleIdList/ArticleId"):
            t = i.get("IdType")
            if t == "doi" and not rec["doi"]:
                rec["doi"] = _text_of(i)
            elif t == "pmc":
                rec["pmcid"] = _text_of(i)
    if any("Retracted Publication" in p for p in rec["pubtypes"]):
        rec["retracted"] = True
    return rec


def _parse_book(art):
    bd = art.find("BookDocument")
    rec = {"pmid": _text_of(bd.find("PMID")) if bd is not None else "", "title": "", "journal": "", "year": "",
           "abstract": "", "pubtypes": ["Book chapter"], "doi": "", "pmcid": "", "authors": [], "mesh": [],
           "retracted": False}
    if bd is not None:
        rec["title"] = _text_of(bd.find("ArticleTitle")) or _text_of(bd.find("Book/BookTitle"))
        rec["journal"] = _text_of(bd.find("Book/BookTitle"))
        rec["year"] = _text_of(bd.find("Book/PubDate/Year"))
        rec["abstract"] = "\n".join(_text_of(x) for x in bd.findall("Abstract/AbstractText"))
    return rec


def pubmed_records(ctx, pmids):
    """pmid (str) -> parsed efetch record (title, journal, year, abstract, pubtypes, doi, pmcid, authors, mesh,
    retracted), or None when PubMed returns nothing for it. Cached per PMID."""
    out, need = {}, []
    for p in dict.fromkeys(str(int(x)) for x in pmids):
        rec = cache_get(ctx, "ncbi_record", p)
        if rec is not None and (rec.get("record") is not None or time.time() - rec["fetched"] < 86400):
            out[p] = rec.get("record")
        else:
            need.append(p)
    for i in range(0, len(need), 100):
        part = need[i:i + 100]
        body = http_get(ctx, "ncbi", EFETCH, {"db": "pubmed", "id": ",".join(part), "rettype": "abstract",
                                              "retmode": "xml"}, cache=False)
        try:
            root = ET.fromstring(body.encode("utf-8"))
        except ET.ParseError:
            raise ToolError("PubMed efetch returned unreadable XML; try again") from None
        got = {}
        for art in root.findall("PubmedArticle"):
            r = _parse_article(art)
            got[r["pmid"]] = r
        for art in root.findall("PubmedBookArticle"):
            r = _parse_book(art)
            got[r["pmid"]] = r
        for p in part:
            cache_put(ctx, "ncbi_record", p, {"record": got.get(p)})
            out[p] = got.get(p)
    return out


def format_record(r, max_chars=ABSTRACT_CHARS):
    au = r.get("authors") or []
    who = ", ".join(au[:3]) + (f", ... ({len(au)} authors)" if len(au) > 3 else "")
    pt = "; ".join(r.get("pubtypes") or []) or "Journal Article"
    mark = ("  [RETRACTED: do not cite as support]" if r.get("retracted") else
            "  [RETRACTION NOTICE: a notice, not the retracted paper]"
            if retraction_status(r.get("pubtypes")) == "notice" else "")
    head = [f"=== PMID {r['pmid']} ===" + mark,
            f"Title: {r.get('title') or '-'}",
            f"Journal: {r.get('journal') or '-'} ({r.get('year') or '?'}) | Type: {pt}"
            + (f" | DOI {r['doi']}" if r.get("doi") else "") + (f" | {r['pmcid']}" if r.get("pmcid") else ""),
            f"Authors: {who or '-'}"]
    ab = r.get("abstract") or ""
    if not ab:
        head.append("Abstract: (none in PubMed: only the title is available; do not cite this paper for anything "
                    "the title does not say)")
    else:
        if len(ab) > max_chars:
            ab = ab[:max_chars].rsplit(" ", 1)[0] + f" ... [abstract cut at {max_chars} characters]"
        head.append("Abstract:\n" + ab)
    if r.get("mesh"):
        head.append("MeSH: " + "; ".join(r["mesh"][:15]))
    return "\n".join(head)


def pubmed_search(ctx, query, max_results):
    q = str(query or "").strip()
    if not q:
        raise ToolError("query is empty")
    n = max(1, min(MAX_SEARCH, int(max_results or MAX_SEARCH)))
    body = http_get(ctx, "ncbi", ESEARCH, {"db": "pubmed", "term": q, "retmax": n, "retmode": "json",
                                           "sort": "relevance"}, max_age_days=ctx.http.search_max_age_days)
    try:
        r = json.loads(body).get("esearchresult", {})
    except ValueError:
        raise ToolError("PubMed esearch returned an unreadable answer; try again") from None
    if r.get("ERROR"):
        raise ToolError(f"PubMed could not run this query: {r['ERROR']}")
    ids = [str(x) for x in r.get("idlist", [])]
    lines = [f"PubMed search: {q}"]
    tr = r.get("querytranslation", "")
    if tr:
        lines.append(f"PubMed read it as: {tr[:600]}")
    el, wl = r.get("errorlist") or {}, r.get("warninglist") or {}
    for k, v in list(el.items()) + list(wl.items()):
        if v:
            lines.append(f"Note from PubMed ({k}): {', '.join(map(str, v))[:300]}")
    count = int(r.get("count", 0) or 0)
    lines.append(f"{count:,} results" + (f"; the {len(ids)} most relevant (PubMed Best Match):" if ids else "."))
    if ids:
        sm = esummary_records(ctx, ids)
        for p in ids:
            s = sm.get(p)
            lines.append(_summary_line(s) if s else f"PMID {p} | (no summary)")
            ctx.seen_ids.add(f"PMID:{p}")
            doi = next((a.get("value") for a in (s or {}).get("articleids") or [] if a.get("idtype") == "doi"), "")
            if doi:
                ctx.seen_ids.add("DOI:" + doi.lower())
        lines.append("Read abstracts with pubmed_abstracts before citing any of these.")
    elif count == 0:
        lines.append("Nothing found. Check the query (symbols and aliases, field tags, AND/OR grouping) before "
                     "concluding that the literature is silent.")
    return "\n".join(lines)


def pubmed_abstracts(ctx, pmids):
    ids, bad = [], []
    for x in pmids or []:
        c = norm_citation(x)
        (ids.append(c.split(":", 1)[1]) if c and c.startswith("PMID:") else bad.append(str(x)))
    if not ids:
        raise ToolError("give PubMed ids (digits, e.g. '12345678' or 'PMID:12345678')"
                        + (f"; not PMIDs: {', '.join(bad[:5])}" if bad else ""))
    extra = ids[MAX_ABSTRACTS:]
    ids = list(dict.fromkeys(ids[:MAX_ABSTRACTS]))
    recs = pubmed_records(ctx, ids)
    out = []
    for p in ids:
        r = recs.get(p)
        if r is None:
            out.append(f"=== PMID {p} ===\nNot found in PubMed: this PMID does not exist (or is not yet public). "
                       "Do not cite it.")
            continue
        ctx.seen_ids.add(f"PMID:{p}")
        ctx.read_ids.add(f"PMID:{p}")
        if r.get("doi"):
            ctx.seen_ids.add("DOI:" + r["doi"].lower())
        out.append(format_record(r))
    if extra:
        out.append(f"(only the first {MAX_ABSTRACTS} PMIDs are fetched per call; not fetched: {', '.join(extra)})")
    if bad:
        out.append(f"(not PMIDs, ignored: {', '.join(bad[:10])})")
    text = "\n\n".join(out)
    return text if len(text) <= RESULT_CHARS else text[:RESULT_CHARS] + "\n[result cut]"


# ----------------------------------------------------------------------------- Europe PMC
def clean_markup(t):
    """Text without HTML entities and tags (Europe PMC titles and abstracts carry both)."""
    t = html.unescape(html.unescape(str(t or "")))
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).strip()


def europepmc_records(ctx, query, n, core=False):
    body = http_get(ctx, "europepmc", EUROPEPMC, {"query": query, "format": "json", "pageSize": int(n),
                                                  "resultType": "core" if core else "lite"},
                    max_age_days=ctx.http.search_max_age_days)
    try:
        d = json.loads(body)
    except ValueError:
        raise ToolError("Europe PMC returned an unreadable answer; try again") from None
    return int(d.get("hitCount", 0) or 0), (d.get("resultList") or {}).get("result") or []


def europepmc_search(ctx, query, max_results):
    q = str(query or "").strip()
    if not q:
        raise ToolError("query is empty")
    n = max(1, min(MAX_SEARCH, int(max_results or MAX_SEARCH)))
    hits, res = europepmc_records(ctx, q, n)
    lines = [f"Europe PMC search: {q}", f"{hits:,} results" + (f"; the first {len(res)} by relevance:" if res
                                                               else ".")]
    for r in res:
        ids = []
        if r.get("pmid"):
            ids.append(f"PMID {r['pmid']}")
            ctx.seen_ids.add(f"PMID:{int(r['pmid'])}")
        if r.get("pmcid"):
            ids.append(r["pmcid"])
        if r.get("doi"):
            ids.append(f"DOI {r['doi']}")
            ctx.seen_ids.add("DOI:" + str(r["doi"]).lower())
        if not ids:
            ids.append(f"{r.get('source', '')}:{r.get('id', '')}")
        src = r.get("source", "")
        pts = list(dict.fromkeys(x.strip() for x in (r.get("pubType") or "").split(";") if x.strip()))
        kind = "PREPRINT (not peer reviewed)" if src == "PPR" else "; ".join(pts[:3])
        title = clean_markup(r.get("title"))
        au = (r.get("authorString") or "")
        lines.append(f"{' | '.join(ids)} | {r.get('pubYear', '')} | {r.get('journalTitle', '') or src} | "
                     f"{kind[:60]} | {title} | {au[:80] + ('...' if len(au) > 80 else '')}")
    if res:
        lines.append("Papers with a PMID: read them with pubmed_abstracts before citing. Cite papers without a "
                     "PMID by DOI, and only for what this list or a fetched page shows.")
    elif hits == 0:
        lines.append("Nothing found. Europe PMC syntax: AND / OR / NOT in capitals, phrases in double quotes, fields "
                     "such as TITLE:, ABSTRACT:, AUTH:, DOI:, SRC:MED (PubMed records only).")
    return "\n".join(lines)


# ----------------------------------------------------------------------------- Crossref (verification)
_RETRACT_UPDATES = ("retraction", "withdrawal", "removal")


def crossref_work(ctx, doi):
    """What verification needs of a DOI's Crossref record: {"exists", "retracted", "notice_of"}. exists False on a
    404. retracted: the record's "updated-by" (Crossref's update notices, which include the Retraction Watch data)
    holds a retraction, withdrawal or removal. notice_of: the DOIs this record's "update-to" retracts, i.e. the
    DOI is itself a retraction notice. Cached (a "does not exist" answer for 1 day; retraction status for
    HttpSettings.search_max_age_days, since a paper can be retracted later). Raises ToolError when Crossref cannot
    be reached."""
    key = hashlib.sha1(doi.lower().encode()).hexdigest()
    rec = cache_get(ctx, "crossref_work", key)
    if rec is not None and time.time() - rec["fetched"] < (
            ctx.http.search_max_age_days * 86400 if rec.get("exists") else 86400):
        return {k: rec.get(k) for k in ("exists", "retracted", "notice_of")}
    try:
        body = http_get(ctx, "crossref", CROSSREF + urllib.parse.quote(doi, safe="/"), {}, cache=False)
        try:
            msg = (json.loads(body) or {}).get("message") or {}
        except ValueError:
            msg = {}

        def kinds(field):
            return [u for u in msg.get(field) or [] if isinstance(u, dict)
                    and str(u.get("type", "")).lower() in _RETRACT_UPDATES]
        out = {"exists": True, "retracted": bool(kinds("updated-by")),
               "notice_of": [str(u.get("DOI", "")).lower() for u in kinds("update-to")]}
    except NotFoundError:
        out = {"exists": False, "retracted": False, "notice_of": []}
    cache_put(ctx, "crossref_work", key, dict(out, doi=doi))
    return out


def crossref_exists(ctx, doi):
    """True / False (404) for a DOI; raises ToolError when Crossref cannot be reached."""
    return bool(crossref_work(ctx, doi)["exists"])


# ----------------------------------------------------------------------------- tahoe_lookup
def tahoe_lookup(ctx, kind, name):
    from . import dossier
    from .. import query as Q
    if kind not in LOOKUP_KINDS:
        raise ToolError(f"kind must be one of {', '.join(LOOKUP_KINDS)}")
    try:
        return dossier.summary(ctx.out, kind, str(name))
    except Q.NotFound as e:
        raise ToolError(str(e)) from None
    except Q.Missing as e:
        raise ToolError(f"not available in this run: {e}") from None


# ----------------------------------------------------------------------------- submit_review
_CIT_ITEMS = {"type": "array", "items": {"type": "string"},
              "description": "PMIDs ('PMID:12345678') or DOIs ('DOI:10.1000/xyz') of papers retrieved in this "
                             "session; [] when none"}


def _obj(props, desc=""):
    d = {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}
    if desc:
        d["description"] = desc
    return d


def _s(desc):
    return {"type": "string", "description": desc}


def _arr(item, desc):
    return {"type": "array", "items": item, "description": desc}


_CONF = {"type": "string", "enum": list(CONFIDENCE), "description": "how sure the review is (see connection-audit)"}

SUBMIT_REVIEW = {
    "name": "submit_review",
    "description": (
        "Submit the finished literature review of the entity under review; this ends the review. Call it once, "
        "when the searches are done, with every section filled (use [] for a section with nothing in it). "
        "Citations are PMIDs or DOIs of papers retrieved in this session with pubmed_search, pubmed_abstracts or "
        "europepmc_search; a PMID must have had its abstract read with pubmed_abstracts. The call is checked: if "
        "it returns an error listing problems, fix them and call it again. A connection verdict 'established' or "
        "'contradicted' needs a citation, 'indirect' one per gene (or one review naming both). After submission "
        "the cited ids and the claims are checked as far as the run's settings allow; the vault says what was "
        "checked, so note_markdown says nothing about verification."),
    "strict": True,
    "input_schema": _obj({
        "summary": _s("2-4 sentences: what the data show about the entity and how that compares with the "
                      "literature"),
        "established": _arr(_obj({
            "partner_or_topic": _s("the partner gene, drug, line or topic (e.g. 'NQO1', 'response to "
                                   "Dimethyl fumarate')"),
            "relation": _s("the relation the cited papers report, in one or two sentences"),
            "data_evidence": _s("the numbers from the dossier that show it (cos, evidence, fold, z, lines)"),
            "citations": _CIT_ITEMS,
            "confidence": _CONF}), "relations in the data that retrieved papers report"),
        "unexpected": _arr(_obj({
            "observation": _s("what the data show"),
            "data_evidence": _s("the numbers from the dossier"),
            "why_unexpected": _s("why it is not expected from what is known"),
            "literature_checked": _arr({"type": "string"}, "the exact queries run (PubMed / Europe PMC / web) "
                                                           "that found no support"),
            "confidence": _CONF}), "strong, trustworthy observations with no support found after searching"),
        "missing": _arr(_obj({
            "expected_connection": _s("the expected relation that the data do not show"),
            "source": {"type": "string", "enum": list(MISSING_SOURCES),
                       "description": "where the expectation comes from"},
            "data_status": _s("what the data show instead (cos and rank, not measured, not in the space ...)"),
            "likely_reason": _s("the most likely reason it is absent"),
            "citations": _CIT_ITEMS}), "expected connections that are absent from the data"),
        "contradicted": _arr(_obj({
            "claim": _s("what the data show that a paper reports the opposite of"),
            "data_evidence": _s("the numbers from the dossier"),
            "citations": _CIT_ITEMS}), "observations a retrieved paper contradicts"),
        "connection_verdicts": _arr(_obj({
            "partner": _s("a gene symbol as in the dossier; 'drug:<name>' or 'line:<name>' for drugs and lines"),
            "verdict": {"type": "string", "enum": list(VERDICTS), "description": "connection-audit rubric"},
            "relation": _s("one sentence: what the cited papers report about the two, with its direction (e.g. "
                           "'each is an NRF2 target induced by electrophiles'); for plausible / unexpected the "
                           "reasoning, or 'no paper found'"),
            "data_evidence": _s("the relation in this run's data with its direction and numbers (e.g. 'moves "
                                "opposite: cos -0.37, both halves, fdr 0.01'; 'raised 3.2x at 5 uM, z +8.1')"),
            "citations": _CIT_ITEMS}), "one verdict per data partner (or drug / line) examined"),
        "open_questions": _arr({"type": "string"}, "questions the data raise that the literature does not answer"),
        "note_markdown": _s("the vault note section (writing-the-note); citations as "
                            "[PMID:123](https://pubmed.ncbi.nlm.nih.gov/123/), only of papers that an item above "
                            "cites (any other is removed from the note)")}),
}

TOOLS = {
    "pubmed_search": {
        "name": "pubmed_search",
        "description": (
            "Search PubMed (NCBI E-utilities) and list the most relevant records: PMID, year, journal, publication "
            "type, title, first and last author, DOI, and whether an abstract exists. Use it to find papers on the "
            "entity, its data partners and the drugs that move it. The query uses full PubMed syntax: field tags "
            "such as [tiab], [MeSH], [pt] and [dp], AND / OR / NOT, parentheses, quoted phrases. The answer also "
            "shows how PubMed translated the query and the total number of hits, which tell you whether a zero or "
            "a flood of results comes from the query itself. It returns no abstracts: read those with "
            "pubmed_abstracts before citing a paper. Results are cached, so repeating a query costs nothing."),
        "strict": True,
        "input_schema": _obj({"query": _s("a PubMed query, e.g. 'HMOX1[tiab] AND (NRF2[tiab] OR NFE2L2[tiab])'"),
                              "max_results": {"type": "integer",
                                              "description": "how many records to list, 1-20 (larger values are "
                                                             "read as 20)"}}),
    },
    "pubmed_abstracts": {
        "name": "pubmed_abstracts",
        "description": (
            "Fetch the PubMed records of up to 10 PMIDs: title, journal, year, publication types (Review, "
            "Retracted Publication ...), DOI, PMCID, authors, MeSH terms and the full abstract. Use it on every "
            "paper before citing it, because titles overstate and abstracts carry the species, cell type, "
            "direction and method that decide whether a paper supports a claim. A PMID that does not exist is "
            "reported as not found. Records are cached."),
        "strict": True,
        "input_schema": _obj({"pmids": _arr({"type": "string"}, "1-10 PubMed ids, e.g. ['38643749', '21251620']; "
                                                                 "more than 10 are not fetched")}),
    },
    "europepmc_search": {
        "name": "europepmc_search",
        "description": (
            "Search Europe PMC, which indexes PubMed plus preprints and, for open-access papers, the full text "
            "(so a gene pair mentioned only in a results section or a supplementary table can be found). Lists "
            "PMID / PMCID / DOI, year, journal, type (preprints are marked), title and authors; no abstracts. Use "
            "it when PubMed finds nothing for a pair or when you need full-text mentions; read any paper with a "
            "PMID through pubmed_abstracts before citing it. Syntax: AND / OR / NOT in capitals, quoted phrases, "
            "fields such as TITLE:, ABSTRACT:, DOI:, SRC:MED; plain terms also match full text."),
        "strict": True,
        "input_schema": _obj({"query": _s("a Europe PMC query, e.g. '\"HMOX1\" AND \"PIR\" AND (NRF2 OR NFE2L2)'"),
                              "max_results": {"type": "integer", "description": "1-20 (larger values are read as "
                                                                                 "20)"}}),
    },
    "tahoe_lookup": {
        "name": "tahoe_lookup",
        "description": (
            "Look up another gene, drug or cell line in this Tahoe-100M run and get its short dossier: identity, "
            "expression, module, strongest drug responses, strongest partners with their evidence (genes); per-dose "
            "activity, top genes, targets' mRNA, depleted lines, nearest drugs (drugs); drivers, baseline-specific "
            "genes, depleting drugs, strongest responses (lines). kind 'pair' with name 'GENE_A|GENE_B' gives the "
            "two genes' cosine, its two compound halves, evidence and fdr, their ranks for each other, STRING score "
            "and the drug-doses that move both. Use it to check a partner (is it driven by the same drugs? in the "
            "same module?) or the data for a relation a paper reports. Names are case-insensitive; aliases and "
            "salt-free drug names work; an unknown name returns close matches."),
        "strict": True,
        "input_schema": _obj({"kind": {"type": "string", "enum": list(LOOKUP_KINDS),
                                       "description": "gene, drug, line, or pair"},
                              "name": _s("gene symbol / drug name / cell line name or Cellosaurus id; for a pair "
                                         "'GENE_A|GENE_B'")}),
    },
    "submit_review": SUBMIT_REVIEW,
}


def custom_tools(names):
    """The definitions of these custom tools, in the given order (submit_check from verify)."""
    out = []
    for n in names:
        if n in TOOLS:
            out.append(TOOLS[n])
        elif n == "submit_check":
            from .verify import CHECK_TOOL
            out.append(CHECK_TOOL)
        elif n in ("web_search", "web_fetch"):
            continue
        else:
            raise KeyError(f"unknown tool {n}")
    return out


def server_tools(web, max_uses, names=None):
    """Anthropic's web tools (run on Anthropic's servers; not executed here). [] when web is False. names: the
    agent's tool list, to declare only the web tools it lists."""
    if not web:
        return []
    out = []
    m = max(1, int(max_uses))
    for n, t in (("web_search", "web_search_20260209"), ("web_fetch", "web_fetch_20260209")):
        if names is None or n in names:
            out.append({"type": t, "name": n, "max_uses": m})
    return out


def tool_definitions(agent, web=True, max_uses=5):
    """Every tool one agent (definitions.AgentDef) declares: its custom tools then its web tools."""
    return custom_tools(agent.custom_tools) + server_tools(web, max_uses, agent.server_tools)


# ----------------------------------------------------------------------------- validation of submissions
def _check_obj(x, schema, path, errs):
    t = schema.get("type")
    if t == "object":
        if not isinstance(x, dict):
            errs.append(f"{path}: expected an object")
            return
        for k in schema["required"]:
            if k not in x:
                errs.append(f"{path}.{k}: missing")
        for k in x:
            if k not in schema["properties"]:
                errs.append(f"{path}.{k}: not a field of this tool")
        for k, sub in schema["properties"].items():
            if k in x:
                _check_obj(x[k], sub, f"{path}.{k}", errs)
    elif t == "array":
        if not isinstance(x, list):
            errs.append(f"{path}: expected a list")
            return
        for i, v in enumerate(x):
            _check_obj(v, schema["items"], f"{path}[{i}]", errs)
    elif t == "string":
        if not isinstance(x, str):
            errs.append(f"{path}: expected text")
        elif "enum" in schema and x not in schema["enum"]:
            errs.append(f"{path}: '{x}' is not one of {', '.join(schema['enum'])}")
    elif t == "integer":
        if not isinstance(x, int) or isinstance(x, bool):
            errs.append(f"{path}: expected an integer")


def schema_errors(payload, tool):
    """Problems of a payload against a tool's input schema (the API enforces strict schemas; fakes may not)."""
    errs = []
    _check_obj(payload, tool["input_schema"], "input", errs)
    return errs


_LINK = re.compile(r"\[[^\]]*\]\((?:[^()]|\([^()]*\))*\)")          # a markdown link; one level of ( ) in the URL
_BARE = re.compile(r"\b(?:PMID\s*[:#]?\s*(\d{4,9})(?!\d)|DOI\s*:?\s*(" + DOI_BODY + "))", re.I)
_REMOVED = " (citation removed"                                       # verify's marker after a removed id
# The ways a note can name a paper (note_matches): PMIDs as PubMed / NCBI / Europe PMC links (also NCBI's search form
# 'ncbi.nlm.nih.gov/pubmed?term=123') and as 'PMID 123', 'PMIDs 1, 2 and 3' / 'PMIDs 1, 2, and 3', 'PubMed ID 123';
# DOIs as doi.org links ('/' percent-encoded or not), 'DOI:10.x/y' and 'DOI 10.x/y' (as the tools print them), and
# in any other URL that carries one in its path or its id= / doi= parameter (publishers, bioRxiv: _url_doi); PMC
# ids as PMC / Europe PMC links and 'PMCID PMC123' / 'PMC123', and Europe PMC links to records of other sources
# (preprints PPR ..., as 'EPMC:PPR/x'): no item may cite those ids, so verification removes them from the note. A
# further number of a 'PMIDs' list needs 7 digits or more, so a year or a count ('PMID 31000004, 2020') is not read
# as one.
_PMID_LIST = re.compile(r"\b(?:PMIDs?|PubMed\s+IDs?)\s*[:#]?\s*(\d{4,9})(?!\d)"
                        r"((?:\s*(?:,\s*(?:(?:and|or)\b|&)|,|;|&|\band\b|\bor\b)\s*\d{7,9}(?!\d))*)", re.I)
_LIST_ITEM = re.compile(r"\d{7,9}")
_PMID_URL = re.compile(r"(?:pubmed\.ncbi\.nlm\.nih\.gov/|ncbi\.nlm\.nih\.gov/pubmed(?:/|(?=\?))|\bpubmed\.gov/"
                       r"|europepmc\.org/(?:article|abstract)s?/MED/)(?:\?(?:[^\s#()<>\[\]]*&)?term=)?(\d{1,9})(?!\d)",
                       re.I)
_PMC_URL = re.compile(r"(?:ncbi\.nlm\.nih\.gov/pmc/articles/|pmc\.ncbi\.nlm\.nih\.gov/articles/"
                      r"|europepmc\.org/(?:(?:article|abstract)s?/PMC/|articles?/))(PMC\d{1,9})(?!\d)", re.I)
_PMC_WORD = re.compile(r"(?:\bPMCID\s*[:#]?\s*)?\b(PMC\d{4,9})(?!\d)", re.I)
_EPMC_OTHER = re.compile(r"europepmc\.org/(?:article|abstract)s?/(PPR|PAT|AGR|CBA|CTX|ETH|HIR|NBK)/([A-Za-z0-9]{1,20})"
                         r"(?![A-Za-z0-9])", re.I)
_NOTE_DOI = re.compile(r"doi\.org/(" + DOI_URL_BODY + r")|\bDOI\s*:?\s*(" + DOI_BODY + ")", re.I)
# a DOI in another URL: after a '/' of its path or in an id= / doi= parameter; _url_doi checks that a host starts the
# URL it is in, and drops what such URLs add after the DOI (a bioRxiv version 'v2', '/full', '.pdf' ...)
_URL_DOI = re.compile(r"(?:/|[?&;](?:id|doi)=)(" + DOI_URL_BODY + ")", re.I)
_URL_STOP = re.compile(r"[\s()<>\[\]\"'`]")             # what ends a URL token read backwards from a DOI in it
_URL_HOST = re.compile(r"(?:https?://)?((?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,})(?::\d+)?/", re.I)
_URL_DOI_TAIL = re.compile(r"(?:[./](?:full|abstract|abs|pdf|epdf|fulltext|full-text|summary|meta|references|figures|"
                           r"html|full\.pdf|fulltext\.html|supplementary-material))+$", re.I)
_PREPRINT_HOSTS = ("biorxiv.org", "medrxiv.org")    # their URLs add the version to the DOI: 10.1101/2020.01.01.1v2


def _url_doi(md, m):
    """(doi, start of the URL's host, end of the DOI in md) for a _URL_DOI match inside a URL (not a doi.org one:
    _NOTE_DOI reads those), else None."""
    head = md[max(0, m.start() - 300):m.start()]
    tok = _URL_STOP.split(head)[-1]
    h = _URL_HOST.match(tok)
    host = h.group(1).lower() if h else ""
    if not h or host == "doi.org" or host.endswith(".doi.org"):
        return None
    raw = m.group(1).split("#")[0]                    # a URL's fragment is no part of its DOI
    doi, rest = clean_doi(raw)
    shown = len(raw) - len(rest)
    cut = _URL_DOI_TAIL.sub("", doi)
    if host.endswith(_PREPRINT_HOSTS):
        cut = re.sub(r"v\d{1,3}$", "", cut)
    if cut != doi and _DOI_WHOLE.fullmatch(cut):
        doi = cut
    return doi, m.start() - len(tok) + h.start(1), m.start(1) + shown


def link_citations(md):
    """Bare 'PMID:123' / 'PMID 123' / 'PMIDs 1, 2 and 3' / 'PubMed ID 123' / 'DOI:10.x/y' / 'DOI 10.x/y' in markdown
    become links; existing links are left alone."""
    out, pos = [], 0
    for m in _LINK.finditer(md):
        out.append(_link_bare(md[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_link_bare(md[pos:]))
    return "".join(out)


def _one_pmid_each(m):
    """'PMIDs 1, 2 and 3' / 'PubMed ID 1' -> 'PMID 1, PMID 2 and PMID 3' / 'PMID 1' (each is then linked)."""
    if not m.group(2) and m.group(0)[:4].upper() == "PMID" and m.group(0)[4:5].upper() != "S":
        return m.group(0)
    return "PMID " + m.group(1) + _LIST_ITEM.sub(lambda x: "PMID " + x.group(0), m.group(2))


def _link_bare(s):
    def rep(m):
        if m.group(1):
            cid, rest = f"PMID:{int(m.group(1))}", ""
        else:
            doi, rest = clean_doi(m.group(2))
            cid = "DOI:" + doi
        if m.string.startswith(_REMOVED, m.end() - len(rest)):
            return m.group(0)                        # an id verification removed: plain text, as it put it
        return link(cid) + rest
    return _BARE.sub(rep, _PMID_LIST.sub(_one_pmid_each, s))


def note_matches(md):
    """[(citation id, start, end, 'url' | 'word')] of every paper a note names - linked, as a bare URL or in words
    (see _PMID_LIST ... above): 'PMID:n', 'DOI:x', 'PMCID:PMCn' or 'EPMC:SRC/id'; 'url' when the span is the id's
    part of a URL (from its host on). Ids already marked '(citation removed ...)' by verification, and a match
    inside another (the 'PMC123' of a PMC link), are left out."""
    found = []
    for m in _PMID_URL.finditer(md):
        found.append((f"PMID:{int(m.group(1))}", m.start(), m.end(), "url"))
    for m in _PMID_LIST.finditer(md):
        found.append((f"PMID:{int(m.group(1))}", m.start(), m.end(1), "word"))
        for x in _LIST_ITEM.finditer(m.group(2)):
            found.append((f"PMID:{int(x.group(0))}", m.start(2) + x.start(), m.start(2) + x.end(), "word"))
    for rx, kind in ((_PMC_URL, "url"), (_PMC_WORD, "word")):
        for m in rx.finditer(md):
            found.append(("PMCID:" + m.group(1).upper(), m.start(), m.end(), kind))
    for m in _EPMC_OTHER.finditer(md):
        found.append((f"EPMC:{m.group(1).upper()}/{m.group(2).upper()}", m.start(), m.end(), "url"))
    for m in _NOTE_DOI.finditer(md):
        g = 1 if m.group(1) else 2
        raw = m.group(g).split("#")[0] if g == 1 else m.group(g)
        doi, rest = clean_doi(raw)
        found.append(("DOI:" + doi, m.start(), m.start(g) + len(raw) - len(rest), "url" if g == 1 else "word"))
    for m in _URL_DOI.finditer(md):
        u = _url_doi(md, m)
        if u:
            found.append(("DOI:" + u[0], u[1], u[2], "url"))
    out, last = [], -1
    for c, a, b, kind in sorted(found, key=lambda x: (x[1], -x[2])):
        if a < last:
            continue                                  # inside an earlier match (the PMC id of a PMC link)
        last = b
        if not md.startswith(_REMOVED, b):
            out.append((c, a, b, kind))
    return out


def note_ids(md):
    """[(citation id, start, end)] of every PMID / DOI / PMC id linked or named in a note (note_matches), except
    those already marked '(citation removed ...)' by verification."""
    return [(c, a, b) for c, a, b, _k in note_matches(md)]


def item_ids(review):
    """The citation ids of the review's items (established, missing, contradicted, connection_verdicts)."""
    return list(dict.fromkeys(c for c, sec, _i in cited_ids(review, note=False)))


def cited_ids(review, note=True):
    """Every citation id of a review payload: (normalised id, section, index) for the item lists, plus (note=True)
    the ids linked or named in note_markdown (section 'note_markdown', index -1)."""
    out = []
    for sec in ("established", "missing", "contradicted", "connection_verdicts"):
        for i, it in enumerate(review.get(sec) or []):
            for c in it.get("citations") or []:
                n = norm_citation(c)
                if n:
                    out.append((n, sec, i))
    if note:
        out += [(c, "note_markdown", -1) for c, _a, _b in note_ids(review.get("note_markdown") or "")]
    return out


def _is_review(ctx, cid):
    """True when cid is a PMID whose PubMed record (in the cache: the agent has read it) is a review."""
    if ctx is None or not cid.startswith("PMID:"):
        return False
    rec = (cache_get(ctx, "ncbi_record", cid.split(":", 1)[1]) or {}).get("record") or {}
    return any("Review" in p for p in rec.get("pubtypes") or [])


def _record_doi(ctx, cid):
    """'DOI:x' of a PMID whose PubMed record is in the cache (the agent read its abstract), else ''."""
    if ctx is None or not cid.startswith("PMID:"):
        return ""
    rec = (cache_get(ctx, "ncbi_record", cid.split(":", 1)[1]) or {}).get("record") or {}
    doi = str(rec.get("doi") or "").strip()
    return (norm_citation("DOI:" + doi) or "") if doi else ""


def normalize_review(payload, ctx=None):
    """(normalised copy, problems): citations as 'PMID:n' / 'DOI:x' (unreadable ones are problems), the verdicts
    the rubric requires citations for ('established', 'contradicted'; 'indirect': two, or one review - ctx gives
    the cached PubMed records), bare ids in note_markdown linked, whitespace trimmed."""
    errs = schema_errors(payload, SUBMIT_REVIEW)
    if errs:
        return None, errs
    r = json.loads(json.dumps(payload))
    for sec in ("established", "missing", "contradicted", "connection_verdicts"):
        for i, it in enumerate(r[sec]):
            cits = []
            for c in it["citations"]:
                n = norm_citation(c)
                if n is None:
                    errs.append(f"{sec}[{i}].citations: '{c}' is not a PMID or DOI (write 'PMID:12345678' or "
                                f"'DOI:10.xxxx/yyy'; PMC ids: give the paper's PMID; a DOI with characters other "
                                f"than letters, digits, - . _ ; : / ( ) < > # +: cite its PMID)")
                elif n not in cits:
                    cits.append(n)
            it["citations"] = cits
    for i, it in enumerate(r["established"]):
        if not it["citations"]:
            errs.append(f"established[{i}] ({it['partner_or_topic'][:40]}): an established relation needs at least "
                        "one citation; without one it is 'plausible' or 'unexpected'")
    for i, it in enumerate(r["contradicted"]):
        if not it["citations"]:
            errs.append(f"contradicted[{i}]: a contradiction needs the citation that reports the opposite")
    for i, it in enumerate(r["connection_verdicts"]):
        who = f"connection_verdicts[{i}] ({it['partner'][:40]})"
        if it["verdict"] in ("established", "contradicted") and not it["citations"]:
            errs.append(f"{who}: verdict '{it['verdict']}' needs a citation")
        elif it["verdict"] == "indirect" and len(it["citations"]) < 2 and not (
                it["citations"] and _is_review(ctx, it["citations"][0])):
            errs.append(f"{who}: verdict 'indirect' needs the papers placing both under the shared regulator or "
                        "process - at least one citation per gene (or drug), or one review naming both; without "
                        "them it is 'plausible'")
        for k in ("relation", "data_evidence"):
            it[k] = it[k].strip()
            if not it[k]:
                errs.append(f"{who}.{k}: empty (say what the papers report, and the direction and numbers in the "
                            "data, so that the verdict can be checked)")
    if not r["summary"].strip():
        errs.append("summary: empty")
    if not r["note_markdown"].strip():
        errs.append("note_markdown: empty")
    r["note_markdown"] = link_citations(r["note_markdown"].strip()) + "\n"
    r["summary"] = r["summary"].strip()
    return r, errs


def submit_review(ctx, payload):
    ctx.submit_attempts += 1
    r, errs = normalize_review(payload, ctx)
    if errs:
        raise ToolError("The review was not accepted; fix these and call submit_review again:\n- "
                        + "\n- ".join(errs[:40]))
    ids = list(dict.fromkeys(c for c, _s_, _i in cited_ids(r)))
    unread = [c for c in ids if c.startswith("PMID:") and c not in ctx.read_ids]
    unseen = [c for c in ids if c.startswith("DOI:") and c not in ctx.seen_ids]
    in_items = set(item_ids(r))
    in_note = list(dict.fromkeys(x for x, _a, _b in note_ids(r["note_markdown"])))
    # one paper under its PMID and its DOI (the DOI of a PubMed record the agent read): cited by the item
    doi_of = {c: _record_doi(ctx, c) for c in in_items | set(in_note) if c.startswith("PMID:")}
    same = {d for c, d in doi_of.items() if c in in_items and d} | {c for c, d in doi_of.items() if d in in_items}
    note_only = [c for c in in_note if c not in in_items and c not in same]
    if (unread or unseen or note_only) and not ctx.notes.get("retrieval_warned"):
        ctx.notes["retrieval_warned"] = True
        msg = ["The review was not accepted yet:"]
        if unread:
            msg.append(f"- PMIDs whose abstracts were not read (read them with pubmed_abstracts, or remove the "
                       f"citations): {', '.join(unread[:30])}")
        if unseen:
            msg.append(f"- DOIs no search returned (find them with europepmc_search 'DOI:\"...\"', or remove the "
                       f"citations): {', '.join(cid_text(c) for c in unseen[:30])}")
        if note_only:
            msg.append("- papers cited in note_markdown (in any form: a link, a bare URL such as a publisher's or "
                       "bioRxiv page, 'PMIDs 1, 2, and 3', 'DOI 10.x/y') but in no item's citations, so no claim of "
                       "the review is checked against them; they are removed from the note unless an item cites "
                       "them (add them to the item whose claim they support, or take them out of the note"
                       + ("; a PMC or Europe PMC id is always removed: cite the paper's PMID or DOI" if any(
                           c.startswith(("PMCID:", "EPMC:")) for c in note_only) else "")
                       + f"): {', '.join(cid_text(c) for c in note_only[:30])}")
        msg.append("Then call submit_review again.")
        raise ToolError("\n".join(msg))
    ctx.notes["not_retrieved"] = unread + unseen
    ctx.submitted = r
    return "Review received. Nothing more is needed; end your turn."


# ----------------------------------------------------------------------------- dispatch
def execute(name, input, ctx):
    """Run one custom tool call -> result text. Raises ToolError for an error result (see the module docstring)."""
    ctx.calls[name] += 1
    inp = input or {}
    try:
        if name == "pubmed_search":
            return pubmed_search(ctx, inp.get("query", ""), inp.get("max_results", MAX_SEARCH))
        if name == "pubmed_abstracts":
            p = inp.get("pmids") or []
            return pubmed_abstracts(ctx, p if isinstance(p, list) else [p])
        if name == "europepmc_search":
            return europepmc_search(ctx, inp.get("query", ""), inp.get("max_results", MAX_SEARCH))
        if name == "tahoe_lookup":
            return tahoe_lookup(ctx, inp.get("kind", ""), inp.get("name", ""))
        if name == "submit_review":
            return submit_review(ctx, inp)
        if name == "submit_check":
            from . import verify
            return verify.submit_check(ctx, inp)
    except ToolError:
        raise
    except (ValueError, TypeError, KeyError) as e:
        raise ToolError(f"{name}: could not use this input ({type(e).__name__}: {_scrub(e, ctx)})") from None
    raise ToolError(f"unknown tool '{name}'")
