#!/usr/bin/env python3
"""test_review.py - the literature-review runner (tahoemap/review) against a scripted fake API: offline, no key.

    python3 tests/test_review.py [--out FINISHED_OUTPUT] [--workdir DIR] [--keep]

Needs a finished tahoemap output folder (tables, relations, graph ...): --out, else the one tests/run_tests.py leaves
in --workdir/out_seed0 (default $TAHOE_TEST_DIR, else /tmp/tahoemap_test; on Windows tahoemap_test in the temp
folder). That folder is only read: every case works in DIR/review_view, whose entries are symbolic links to the
output's own entries (hard links or copies where this account may not make symbolic links: Windows without Developer
Mode) next to a fresh review/ folder.

Every request goes through the real Anthropic SDK (client.beta.messages.stream, answered with server-sent events)
to tahoemap/review/fake.py, an httpx2 mock transport that answers from a script and checks each request as the API
would; API errors are the SDK's own typed exceptions. PubMed / Europe PMC / Crossref answer from
fake.FakeLiterature. Sockets and urllib are blocked for the whole test, the ANTHROPIC_* variables are removed, and
sleeping between retries is patched out.

Cases: a review end to end (dossier, tool calls, a rejected and an accepted submit_review, id verification that
removes a nonexistent PMID, the citation checker, review JSON, note, ledger, history with every request and
response); pause_turn; refusal; the end_turn and max_tokens nudges and no_review; over_budget; a billing error that
rotates to the second key; every key dead (exit code 3) and the resume with a new key; a new key typed at the prompt;
rate limit / overload / network errors that back off without rotating; --dry-run; 6 entities on 3 threads; Ctrl-C
and SIGTERM mid-run and the resume; keys absent from every file written and every line printed; the error
classification; plan / status / tables and the CLI; a fake review of a gene, a drug and a line spliced into the
vault (the literature section, its callout and resolvable links, the partner tables' Literature column, no broken
link, no other note changed) and the map (the side panel's verdicts); `duplicate` (hard links, duplicated_from.json,
--repo). Then the fixes of the second review: streaming and max_tokens by effort; consecutive cut-offs only; a
transient refusal (stop_details.recommended_model); an empty response; lost responses (timeouts, streams cut or
ended early or closed before message_start, an error event mid-stream: their own retry budget and an estimated
cost; a cap reached through estimates alone is 'failed', retried); the budget line; Ctrl-C
while a submitted review is verified (stored done, the late response recorded, completed by --recheck), and a
--recheck that is itself stopped (still --recheck-able); SIGHUP; Ctrl-C at the key prompt; a cut ledger line; the
run lock (stale, live, reused pid, another computer); a key given to --keys-file; the same error on 5 entities in a
row before any entity of the run got its answer (an error of the entities' own stops one run, not every later one)
and --retry-failed. Then the fixes of the fourth review: a --recheck stopped by --max-usd, by its last key or by a
signal between checker turns leaves the stored review as it was; network failures (one signature) and waits that run
out stop the run also after an answer; the run waits for a slow healthy review before a stop; a request in flight
at the close is charged an estimate and a response lost after it is recorded; a malformed key and local errors are
never charged; status counts every entity after a filtered plan; the projection uses only reviews made with the
same model, effort and --verify; `tahoe stop` stops a foreground review; --fake given a key. Windows fixes: a review
that cannot be stored, ledger lines that cannot be written, `review stop`, the pipeline lock. And a crafted
malicious review (raw
HTML, script, iframe, javascript: / data: / vbscript: links, a remote image, comments, an unclosed fence, a fabricated
PMID, a verdict the checker does not support, two verdicts on one partner) spliced into the vault and the map: the
note sanitised, unverified verdicts shown as such, one verdict per partner chosen alike in both, the callout's
verification from the counts, the generated footer, a stale connections.parquet; in a browser (Playwright, when
installed) the badges, a slow double-click that pins and a small simulation that animates the sign switch. Round 5:
what a removal puts back together (a tag, an autolink, a definition), '^' labels that are no footnote's, Dataview
inline queries, linear time on unclosed '<!--' / '<?' / '<script>', e-mail / mailto / '//host' autolinks; two
reviews of one gene (the latest's verdicts in the vault and the map alike), the callout's unverified count
(retracted-only verdicts too), unread papers the id check removed, and ids not looked up but graded by the checker.
Prints PASS / FAIL per check; exit code 1 if anything fails. Takes well under a minute.
"""

import argparse
import contextlib
import glob
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
# the default work folder: /tmp/tahoemap_test, or on Windows the system temp folder (not C:\tmp)
DEFAULT_WORKDIR = "/tmp/tahoemap_test" if os.name != "nt" else os.path.join(tempfile.gettempdir(), "tahoemap_test")
sys.path.insert(0, REPO)

import pandas as pd  # noqa: E402

from tahoemap import cli  # noqa: E402
from tahoemap.common import find_git, git_out  # noqa: E402
from tahoemap.review import dossier as D  # noqa: E402
from tahoemap.review import fake as F  # noqa: E402
from tahoemap.review import keys as K  # noqa: E402
from tahoemap.review import runner as R  # noqa: E402
from tahoemap.review import history as H  # noqa: E402
from tahoemap.review.history import Ledger, read_jsonl  # noqa: E402

RESULTS = []
SECRETS = set(F.DEFAULT_KEYS)          # every key a case uses; none may appear in a file or in the output
KEY1, KEY2 = F.DEFAULT_KEYS
KEY3 = "sk-ant-fake-3333333333333333-KEY3"
KEY4 = "sk-ant-fake-4444444444444444-KEY4"
KEY5 = "sk-ant-api03-" + "Zq7" * 14 + "-KEY5"         # given by mistake to --keys-file
SECRETS |= {KEY3, KEY4, KEY5}
SLEEPS = []
SCANNED = {"files": 0, "bytes": 0}


# ----------------------------------------------------------------------------- harness
def check(case, name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    RESULTS.append((case, name, status, str(detail)))
    print(f"  [{status}] {case}: {name}" + (f" -- {detail}" if detail else ""), flush=True)
    return ok


def case(fn):
    def wrapped(*a, **k):
        t0 = time.time()
        print(f"\n== {fn.__name__}", flush=True)
        try:
            fn(*a, **k)
        except Exception as e:  # noqa: BLE001
            check(fn.__name__, "ran without an exception", False,
                  f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=6)}")
        print(f"   ({time.time() - t0:.1f} s)", flush=True)
    wrapped.__name__ = fn.__name__
    return wrapped


class Tee(io.TextIOBase):
    """sys.stdout that also keeps everything printed (scanned for keys at the end)."""

    def __init__(self, real):
        self.real, self.buf = real, io.StringIO()

    def write(self, s):
        self.buf.write(s)
        return self.real.write(s)

    def flush(self):
        self.real.flush()


def block_network():
    def no_net(*a, **k):
        raise AssertionError("network access during test_review.py")
    socket.socket.connect = no_net
    socket.socket.connect_ex = no_net
    socket.create_connection = no_net
    urllib.request.urlopen = no_net
    for v in ("ANTHROPIC_API_KEY", "ANTHROPIC_API_KEYS", "ANTHROPIC_AUTH_TOKEN", "NCBI_API_KEY", "NCBI_EMAIL"):
        os.environ.pop(v, None)


def fake_sleep(seconds, stop_event):
    SLEEPS.append(float(seconds))
    return stop_event.is_set()


def _link_or_copy(a, b):
    try:
        os.link(a, b)
    except OSError:
        shutil.copy2(a, b)


def link_entry(src, dst):
    """An entry of a view: a symbolic link to src; where this account may not make one (Windows without Developer
    Mode: WinError 1314), a copy whose files are hard links (else copies). The output is only read either way: every
    stage writes a new file and swaps it in."""
    try:
        os.symlink(src, dst, target_is_directory=os.path.isdir(src))
    except OSError:
        if os.path.isdir(src):
            shutil.copytree(src, dst, copy_function=_link_or_copy)
        else:
            _link_or_copy(src, dst)


def make_view(src, work):
    view = os.path.join(work, "review_view")
    if os.path.lexists(view):
        shutil.rmtree(view)
    os.makedirs(view)
    for e in sorted(os.listdir(src)):
        if e != "review":
            link_entry(os.path.join(src, e), os.path.join(view, e))
    return view


def scan_for_keys(root):
    """Fail if any key (or anything shaped like one) is in a file under root."""
    bad = []
    for dp, _dn, fns in os.walk(root):
        for f in fns:
            p = os.path.join(dp, f)
            if os.path.islink(p):
                continue
            with open(p, "rb") as fh:
                b = fh.read()
            SCANNED["files"] += 1
            SCANNED["bytes"] += len(b)
            t = b.decode("utf-8", "replace")
            if any(s in t for s in SECRETS) or re.search(r"sk-ant-[A-Za-z0-9_\-]{6,}", t):
                bad.append(os.path.relpath(p, root))
    return bad


def reset(view, label):
    """End of a case: no key in any file it wrote; then a fresh review/ folder for the next one."""
    rd = os.path.join(view, "review")
    if os.path.isdir(rd):
        bad = scan_for_keys(rd)
        check(label, "no API key in any file written", not bad, f"{len(bad)} files with a key: {bad[:5]}"
              if bad else f"{sum(1 for _ in glob.iglob(os.path.join(rd, '**'), recursive=True))} paths scanned")
        shutil.rmtree(rd)


def run(view, script, **kw):
    fk = script if isinstance(script, F.FakeAPI) else F.FakeAPI(script)
    kw.setdefault("env_keys", False)
    kw.setdefault("interactive", False)
    kw.setdefault("quiet", True)
    if not (kw.get("limit") or kw.get("max_usd") is not None or kw.get("dry_run")):
        kw.setdefault("no_cap", True)
    res = R.run(view, fake=fk, **kw)
    return res, fk


def ledger(view):
    return Ledger(view).read()


def events(view, rec):
    return read_jsonl(os.path.join(view, rec["history"]))


def good(partner="NQO1", pmids=("31000001",), lookup=None):
    """A short successful review: search (+ a look-up), read the abstracts, submit."""
    first = [{"name": "pubmed_search", "input": {"query": f"{partner} AND NRF2", "max_results": 5}}]
    if lookup:
        first.append({"name": "tahoe_lookup", "input": {"kind": "gene", "name": lookup}})
    return [{"tool_use": first},
            {"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": list(pmids)}}]},
            {"submit_review": F.sample_review(partner, pmids)}]


def kid(secret):
    return K.key_id(secret)


# ----------------------------------------------------------------------------- cases
@case
def classification():
    want = {401: K.DEAD_KEY, 402: K.DEAD_KEY, 403: K.DEAD_KEY, "spend_limit": K.DEAD_KEY, "on_hold": K.DEAD_KEY,
            429: K.WAIT, 529: K.WAIT, 500: K.WAIT, "connection": K.WAIT, "timeout": K.WAIT,
            400: K.ENTITY, 404: K.ENTITY, 413: K.ENTITY}
    got = {w: K.classify(F.sdk_error(w))[0] for w in want}
    wrong = {w: (got[w], c) for w, c in want.items() if got[w] != c}
    check("classification", "SDK exceptions classified (dead key / wait / entity)", not wrong,
          f"{len(want)} errors; wrong: {wrong}" if wrong else
          ", ".join(f"{w}={type(F.sdk_error(w)).__name__}:{got[w]}" for w in want))
    e = F.sdk_error(402)
    _c, info = K.classify(e)
    check("classification", "402 is a billing_error APIStatusError", info["status"] == 402 and
          info["type"] == "billing_error", info)
    check("classification", "Retry-After read from a 429", K.classify(F.sdk_error(429, retry_after=7))[1]
          ["retry_after"] == 7.0)
    K.register_secret(KEY1)
    s = K.scrub(f"401 for x-api-key: {KEY1}; Authorization: Bearer abcdefghijklmnopqrstuvwxyz0123")
    check("classification", "scrub() removes keys and bearer tokens", KEY1 not in s and "abcdefghijklmnop" not in s
          and kid(KEY1) in s, s)


@case
def end_to_end(view, ents):
    g, partner = ents["genes"][0], ents["genes"][1]
    steps = [
        {"tool_use": [{"name": "pubmed_search", "input": {"query": "NQO1 AND NRF2", "max_results": 5}},
                      {"name": "tahoe_lookup", "input": {"kind": "gene", "name": partner["name"]}},
                      {"name": "europepmc_search", "input": {"query": "NQO1 AND KEAP1", "max_results": 3}}]},
        {"web_search": "NQO1 NRF2 target genes",
         "tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001", "31000002"]}}],
         "fallback": "claude-opus-5"},
        {"submit_review": F.sample_review("NQO1", ("31000001", "99999999"))},      # rejected: 99999999 not read
        {"submit_review": F.sample_review("NQO1", ("31000001", "99999999"))},      # accepted; 99999999 noted
    ]
    res, fk = run(view, {"entities": {g["entity_id"]: steps}}, only=g["entity_id"])
    c = "end_to_end"
    check(c, "exit code 0, the entity done", res.exit_code == 0 and res.counts == {"done": 1}, res.counts)
    check(c, "no request the API would reject", not res.violations, res.violations[:3])
    rev = [x for x in fk.calls if x["role"] == "reviewer"]
    chk = [x for x in fk.calls if x["role"] == "checker"]
    check(c, "4 reviewer requests and 1 citation-checker request", len(rev) == 4 and len(chk) == 1,
          [x["step"] for x in fk.calls])
    L = ledger(view)
    rec = L[-1] if L else {}
    check(c, "one ledger line: done, key id, cost, tokens, counts",
          len(L) == 1 and rec.get("status") == "done" and rec.get("key_id") == kid(KEY1)
          and rec.get("cost_usd", 0) > 0 and rec.get("n_requests") == 5 and rec.get("n_tool_calls") == 7
          and rec.get("web_searches") == 1 and rec.get("input_tokens", 0) > 0
          and rec.get("cache_read_input_tokens", 0) > 0 and rec.get("served_models") == ["claude-opus-5-5",
                                                                                         "claude-opus-5"],
          {k: rec.get(k) for k in ("status", "key_id", "cost_usd", "n_requests", "n_tool_calls", "web_searches",
                                   "served_models")})
    missing = [k for k in ("entity_id", "kind", "name", "run_id", "agent", "model", "status", "cost_usd",
                           "input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens",
                           "web_searches", "n_requests", "n_tool_calls", "key_id", "started", "finished", "error")
               if k not in rec]
    check(c, "ledger line has every contract field", not missing, missing)
    ev = events(view, rec)
    kinds = [e["event"] for e in ev]
    req = [e for e in ev if e["event"] == "request"]
    resp = [e for e in ev if e["event"] == "response"]
    tools = [e for e in ev if e["event"] == "tool"]
    starts = [e for e in ev if e["event"] == "start"]
    check(c, "history: start ... end, a request and a response per API call",
          kinds[0] == "start" and kinds[-1] == "end" and len(req) == len(resp) == len(fk.calls) == 5,
          f"{len(req)} requests, {len(resp)} responses, {len(fk.calls)} calls; events {kinds}")
    s0 = starts[0] if starts else {}
    check(c, "start event: system prompt + dossier stored once, with their sha256",
          len(starts) == 2 and s0.get("system_sha256") == hashlib.sha256(s0.get("system", "").encode()).hexdigest()
          and s0.get("dossier_sha256") == hashlib.sha256(s0.get("dossier", "").encode()).hexdigest()
          and "submit_review" in s0.get("tools", []) and "web_search" in s0.get("tools", [])
          and s0.get("key_id") == kid(KEY1) and s0.get("code_version") and s0.get("effort") == "high"
          and starts[1].get("agent") == "citation-checker",
          {k: (s0.get(k) if k != "dossier" else len(s0.get(k, ""))) for k in ("agent", "model", "key_id", "tools")})
    check(c, "every response stored in full (to_dict) with usage and cost",
          all(e["response"].get("id", "").startswith("msg_fake_") and e.get("usage") and e.get("cost_usd") is not None
              and e["response"].get("content") is not None for e in resp))
    n_rev = sum(len(e["messages"]) for e in req if e["agent"] != "citation-checker")
    check(c, "request events hold exactly the messages appended since the previous request",
          n_rev == rev[-1]["n_messages"], f"{n_rev} logged, the last request had {rev[-1]['n_messages']}")
    first = json.dumps(req[0]["messages"]) if req else ""
    check(c, "the dossier is stored once (start event); the first request holds its placeholder",
          H.DOSSIER_REF in first and s0.get("dossier", "")[:200] not in first, f"{len(first)} characters")
    conv = H.conversation(ev)
    dos = D.build(view, "gene", g["entity_id"])
    check(c, "history.conversation() rebuilds exactly what was sent (sha256 of the messages)",
          F.messages_sha256(conv) == rev[-1]["messages_sha256"] and conv[0]["content"] == dos.user_message()
          and F.messages_sha256(H.conversation(ev, "citation-checker")) == chk[-1]["messages_sha256"],
          f"{len(conv)} messages")
    check(c, "tool events: 7 calls, the first submit_review rejected (is_error)",
          len(tools) == 7 and [t["name"] for t in tools if t["is_error"]] == ["submit_review"],
          [(t["name"], t["is_error"]) for t in tools])
    end = ev[-1]
    check(c, "end event: status and totals", end.get("status") == "done" and end.get("totals", {}).get("n_requests")
          == 5)
    rp = os.path.join(view, rec.get("review", "-"))
    rv = json.load(open(rp, encoding="utf-8")) if os.path.exists(rp) else {}
    ver = rv.get("verification", {})
    est = (rv.get("established") or [{}])[0]
    check(c, "review JSON: payload + verification + meta", rv.get("meta", {}).get("entity_id") == g["entity_id"]
          and ver.get("mode") == "llm" and ver.get("llm", {}).get("status") == "done"
          and ver.get("counts", {}).get("claims_checked", 0) >= 3, ver.get("counts"))
    check(c, "verification removed the nonexistent PMID and marked the item unverified",
          ver.get("ids", {}).get("missing") == ["PMID:99999999"] and est.get("unverified") is True
          and est.get("removed_citations") == ["PMID:99999999"] and est.get("citations") == ["PMID:31000001"]
          and est.get("check", {}).get("verdict") == "supported", {k: est.get(k) for k in (
              "citations", "removed_citations", "unverified", "check")})
    note = glob.glob(os.path.join(view, "review", "notes", "gene", "*.md"))
    nt = open(note[0], encoding="utf-8").read() if note else ""
    check(c, "note written for the vault (links kept, removed citation marked)",
          "pubmed.ncbi.nlm.nih.gov/31000001" in nt and "citation removed" in nt, nt[:200])
    conn = pd.read_parquet(os.path.join(view, "review", "connections.parquet"))
    find = pd.read_parquet(os.path.join(view, "review", "findings.parquet"))
    check(c, "connections.parquet and findings.parquet built", len(conn) == 2 and len(find) >= 4
          and set(conn["verdict"]) == {"established", "unexpected"}, f"{len(conn)} connections, {len(find)} findings")
    check(c, "the literature tools answered from the local stub", len(fk.literature.requests) >= 4,
          f"{len(fk.literature.requests)} stub requests")
    reset(view, c)


@case
def pause_turn(view, ents):
    g = ents["genes"][1]
    steps = [{"web_search": "PIR NRF2", "pause": True},
             {"web_search": "PIR NRF2", "tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001"]}}]},
             {"submit_review": F.sample_review("NQO1")}]
    res, fk = run(view, {"entities": {g["entity_id"]: steps}, "checker": "auto"}, only=g["entity_id"],
                  verify="ids")
    c = "pause_turn"
    rev = [x for x in fk.calls if x["role"] == "reviewer"]
    check(c, "done, the paused turn resent as is (1 -> 2 -> 4 messages)",
          res.counts == {"done": 1} and [x["n_messages"] for x in rev] == [1, 2, 4] and not res.violations,
          f"{res.counts} {[x['n_messages'] for x in rev]} {res.violations[:2]}")
    ev = events(view, ledger(view)[-1])
    req = [e for e in ev if e["event"] == "request"]
    m2 = req[1]["messages"] if len(req) > 1 else []
    check(c, "the resend adds only the paused assistant turn (ends with server_tool_use, no 'continue')",
          len(m2) == 1 and m2[0]["role"] == "assistant" and m2[0]["content"][-1]["type"] == "server_tool_use",
          [(m["role"], [b["type"] for b in m["content"]]) for m in m2])
    check(c, "--verify ids: no citation-checker request", not [x for x in fk.calls if x["role"] == "checker"])
    reset(view, c)


@case
def refusal(view, ents):
    g = ents["genes"][2]
    sc = {"entities": {g["entity_id"]: [{"refusal": "bio"}] + good()}}
    res, fk = run(view, sc, only=g["entity_id"])
    rec = ledger(view)[-1]
    c = "refusal"
    check(c, "status refused with stop_details.category", res.counts == {"refused": 1} and rec["status"] ==
          "refused" and rec.get("refusal_category") == "bio" and len(fk.calls) == 1, {k: rec.get(k) for k in (
              "status", "refusal_category", "error")})
    check(c, "no review stored", not glob.glob(os.path.join(view, "review", "reviews", "gene", "*.json")))
    res2, fk2 = run(view, sc, only=g["entity_id"])
    check(c, "refused is final: the next run leaves it alone", not fk2.calls and res2.message == "nothing to do",
          res2.message)
    res3, fk3 = run(view, fk, only=g["entity_id"], redo=True)
    check(c, "--redo reviews it again", res3.counts == {"done": 1}, res3.counts)
    reset(view, c)


@case
def nudges(view, ents):
    g4, g5, g6 = ents["genes"][3:6]
    read = {"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001"]}}]}
    sc = {"entities": {
        g4["entity_id"]: [read, {"end_turn": "I have read the dossier."}, {"submit_review": F.sample_review()}],
        g5["entity_id"]: [{"end_turn": "first"}, {"end_turn": "second"}],
        g6["entity_id"]: [read, {"max_tokens": True, "partial_tool": "submit_review"},
                          {"submit_review": F.sample_review()}]}}
    res, fk = run(view, sc, only=[g4["entity_id"], g5["entity_id"], g6["entity_id"]], concurrency=1, verify="ids")
    c = "nudges"
    st = {r["entity_id"]: r["status"] for r in ledger(view)}
    check(c, "end_turn -> nudge -> done; twice end_turn -> no_review; max_tokens -> nudge -> done",
          st == {g4["entity_id"]: "done", g5["entity_id"]: "no_review", g6["entity_id"]: "done"}
          and not res.violations, f"{st} {res.violations[:2]}")
    by = {r["entity_id"]: r for r in ledger(view)}
    req4 = [e for e in events(view, by[g4["entity_id"]]) if e["event"] == "request"]
    t4 = req4[2]["messages"][-1]["content"][0].get("text", "") if len(req4) > 2 else ""
    check(c, "the end_turn nudge asks for submit_review", "submit_review" in t4 and "without calling" in t4, t4[:90])
    req6 = [e for e in events(view, by[g6["entity_id"]]) if e["event"] == "request"]
    m6 = req6[2]["messages"][-1]["content"] if len(req6) > 2 else []
    check(c, "the max_tokens nudge answers the cut-off tool call (is_error) and asks to finish",
          len(m6) == 2 and m6[0]["type"] == "tool_result" and m6[0].get("is_error") and "output limit" in
          m6[1].get("text", ""), [b.get("type") for b in m6])
    for i in range(2):                                          # no_review is retried up to 2 times, then left alone
        run(view, fk, only=g5["entity_id"], verify="ids")
    _r, fk4 = run(view, sc, only=g5["entity_id"], verify="ids")
    n5 = sum(1 for r in ledger(view) if r["entity_id"] == g5["entity_id"])
    check(c, "no_review retried twice, then left alone", n5 == 3 and not fk4.calls, f"{n5} attempts")
    reset(view, c)


@case
def over_budget(view, ents):
    g = ents["genes"][0]
    sc = F.FakeAPI({"entities": {g["entity_id"]: good()}})
    res, _ = run(view, sc, only=g["entity_id"], per_entity_usd=0.001)
    rec = ledger(view)[-1]
    c = "over_budget"
    check(c, "the attempt ends over_budget after the request that crossed the cap, history kept",
          res.counts == {"over_budget": 1} and rec["n_requests"] == 1 and rec["cap_usd"] == 0.001
          and os.path.exists(os.path.join(view, rec["history"])), {k: rec.get(k) for k in (
              "status", "cost_usd", "cap_usd", "n_requests", "error")})
    n0 = len(sc.calls)
    run(view, sc, only=g["entity_id"], per_entity_usd=0.001)
    check(c, "not retried at the same cap", len(sc.calls) == n0, f"{len(sc.calls) - n0} requests")
    res3, _ = run(view, sc, only=g["entity_id"], per_entity_usd=5.0, verify="ids")
    check(c, "retried with a higher cap", res3.counts == {"done": 1}, res3.counts)
    res4, fk4 = run(view, F.FakeAPI({"entities": {g["entity_id"]: good()}}), only=g["entity_id"], redo=True,
                    max_usd=0.0001, verify="ids")
    rec4 = ledger(view)[-1]
    check(c, "--max-usd reached: the running entity pauses", rec4["status"] == "paused" and len(fk4.calls) == 1,
          {k: rec4.get(k) for k in ("status", "error")})
    reset(view, c)


@case
def billing_rotation(view, ents):
    g = ents["genes"][1]
    res, fk = run(view, {"dead_keys": {KEY1[-4:]: 402}, "entities": {g["entity_id"]: good()}},
                  only=g["entity_id"], verify="ids")
    L = ledger(view)
    c = "billing_rotation"
    check(c, "402 -> key_rotated on key 1, then done on key 2",
          [(r["status"], r["key_id"]) for r in L] == [("key_rotated", kid(KEY1)), ("done", kid(KEY2))]
          and res.exit_code == 0, [(r["status"], r["key_id"], (r.get("error") or "")[:60]) for r in L])
    check(c, "the entity restarted from the beginning on the new key",
          [(x["key"], x["n_messages"]) for x in fk.calls][:2] == [(KEY1[-4:], 1), (KEY2[-4:], 1)],
          [(x["key"], x["n_messages"], x["step"]) for x in fk.calls])
    err = [e for e in events(view, L[0]) if e["event"] == "error"]
    check(c, "history of the first attempt: typed error, status, type, action",
          len(err) == 1 and err[0]["class"] == "APIStatusError" and err[0]["status"] == 402
          and err[0]["type"] == "billing_error" and err[0]["category"] == K.DEAD_KEY, err[:1])
    ks = json.load(open(os.path.join(view, "review", "keys_state.json"), encoding="utf-8"))
    dead = [k["key_id"] for k in ks["keys"] if k["dead"]]
    check(c, "keys_state.json: key 1 dead (ids only)", dead == [kid(KEY1)], dead)
    out = []
    R.status(view, say=out.append)
    txt = "\n".join(out)
    check(c, "review status names the dead key by its id", kid(KEY1) in txt and "Dead keys" in txt,
          [x for x in out if "Dead" in x])
    reset(view, c)


@case
def all_keys_dead(view, ents, work):
    a, b, cc = ents["genes"][0], ents["genes"][1], ents["genes"][2]
    sc = F.FakeAPI({"entities": {a["entity_id"]: good(),
                                 b["entity_id"]: [{"error": 402}, {"error": 401}] + good(),
                                 cc["entity_id"]: good()}})
    only = [a["entity_id"], b["entity_id"], cc["entity_id"]]
    res, _ = run(view, sc, only=only, concurrency=1, verify="ids")
    c = "all_keys_dead"
    st = [(r["entity_id"], r["status"], r["key_id"]) for r in ledger(view)]
    check(c, "every key dead -> exit code 3, paused, the rest not started",
          res.exit_code == 3 and res.paused and "add a key" in res.message
          and st == [(a["entity_id"], "done", kid(KEY1)), (b["entity_id"], "key_rotated", kid(KEY1)),
                     (b["entity_id"], "key_rotated", kid(KEY2))], f"exit {res.exit_code}; {st}")
    kf = os.path.join(work, "keys.txt")
    with open(kf, "w", encoding="utf-8") as fh:
        fh.write(f"# a new key\n{KEY3}\n")
    os.chmod(kf, 0o644)
    n0 = len(sc.calls)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        res2, _ = run(view, sc, only=only, concurrency=1, keys_file=kf, verify="ids")
    printed = buf.getvalue()
    sys.stdout.write(printed)
    after = sc.calls[n0:]
    st2 = {r["entity_id"]: r["status"] for r in ledger(view)}
    check(c, "next run with a new key (--keys-file): resumes, done entities not redone",
          res2.exit_code == 0 and set(st2.values()) == {"done"} and len(ledger(view)) == 5
          and a["entity_id"] not in {x["entity"] for x in after} and {x["key"] for x in after} == {KEY3[-4:]},
          f"exit {res2.exit_code}; {st2}; entities sent: {sorted({x['entity'] for x in after})}")
    if os.name != "nt":                    # (the keys-file permission check is POSIX only: file modes)
        check(c, "warns that the keys file is readable by others", "can be read by other users" in printed)
    os.remove(kf)
    reset(view, c)
    # a terminal: a new key typed at the prompt continues the same run; Enter pauses
    asked = []
    sc2 = F.FakeAPI({"keys": [KEY1], "dead_keys": {KEY1[-4:]: 401}, "entities": {a["entity_id"]: good()}})
    res3, _ = run(view, sc2, only=a["entity_id"], interactive=True, verify="ids",
                  prompt=lambda text: (asked.append(text), KEY4)[1])
    L3 = ledger(view)
    check(c, "interactive: asks once (getpass), the typed key finishes the entity in the same run",
          len(asked) == 1 and "press Enter to stop" in asked[0] and res3.exit_code == 0
          and [(r["status"], r["key_id"]) for r in L3] == [("key_rotated", kid(KEY1)), ("done", kid(KEY4))],
          [(r["status"], r["key_id"]) for r in L3])
    reset(view, c)
    res4, _ = run(view, F.FakeAPI({"keys": [KEY1], "dead_keys": {KEY1[-4:]: 402}, "entities": {}}),
                  only=a["entity_id"], interactive=True, prompt=lambda text: "", verify="ids")
    check(c, "interactive: Enter at the prompt pauses (exit code 3)", res4.exit_code == 3, res4.message[:100])
    reset(view, c)


@case
def rate_limit_backoff(view, ents):
    g = ents["genes"][2]
    SLEEPS.clear()
    res, fk = run(view, {"entities": {g["entity_id"]: [{"error": 429, "retry_after": 7}, {"error": 529},
                                                       {"error": "connection"}] + good()}},
                  only=g["entity_id"], verify="ids")
    L = ledger(view)
    c = "rate_limit_backoff"
    check(c, "429, 529 and a network error waited out on the same key, then done",
          res.counts == {"done": 1} and [(r["status"], r["key_id"]) for r in L] == [("done", kid(KEY1))]
          and {x["key"] for x in fk.calls} == {KEY1[-4:]}, [(x["key"], x["step"]) for x in fk.calls])
    check(c, "three back-offs, Retry-After honoured, exponential", len(SLEEPS) == 3 and SLEEPS[0] >= 7.0
          and SLEEPS[2] > SLEEPS[1] * 1.1, [round(s, 1) for s in SLEEPS])
    err = [e for e in events(view, L[0]) if e["event"] == "error"]
    check(c, "errors logged as typed 'wait' events", [(e["class"], e["category"]) for e in err] == [
        ("RateLimitError", K.WAIT), ("OverloadedError", K.WAIT), ("APIConnectionError", K.WAIT)],
        [(e["class"], e["status"]) for e in err])
    reset(view, c)


@case
def dry_run(view, ents):
    res, fk = run(view, {}, kinds="line,drug", limit=3, dry_run=True)
    c = "dry_run"
    d = os.path.join(view, "review", "dry_run")
    summ = json.load(open(os.path.join(d, "summary.json"), encoding="utf-8")) if os.path.exists(os.path.join(d, "summary.json")) \
        else {}
    reqs = sorted(glob.glob(os.path.join(d, "*", "*.request.json")))
    doss = sorted(glob.glob(os.path.join(d, "*", "*.dossier.md")))
    check(c, "nothing sent, no ledger; 3 dossiers and first requests written",
          not fk.calls and not os.path.exists(os.path.join(view, "review", "ledger.jsonl"))
          and len(summ.get("entities", [])) == 3 and len(reqs) == 3 and len(doss) == 3,
          f"{len(fk.calls)} calls, {len(reqs)} requests, {len(doss)} dossiers")
    rq = json.load(open(reqs[0], encoding="utf-8"))["request"] if reqs else {}
    tools = rq.get("tools", [])
    custom = [t for t in tools if "input_schema" in t]
    check(c, "the request: adaptive thinking (no thinking field), effort, fallbacks + beta, caching, strict tools",
          "thinking" not in rq and "tool_choice" not in rq and rq.get("output_config") == {"effort": "high"}
          and rq.get("fallbacks") == "default" and rq.get("betas") == [R.FALLBACK_BETA]
          and rq.get("cache_control") == {"type": "ephemeral"}
          and rq["system"][-1].get("cache_control") == {"type": "ephemeral"}
          and custom and all(t.get("strict") for t in custom)
          and [t["type"] for t in tools if "type" in t] == ["web_search_20260209", "web_fetch_20260209"]
          and rq.get("model") == "claude-opus-5-5" and rq["messages"][0]["role"] == "user",
          {k: rq.get(k) for k in ("model", "output_config", "fallbacks", "betas", "cache_control")})
    reset(view, c)


@case
def concurrency(view, ents):
    six = ents["genes"][:6]
    sc = {"entities": {e["entity_id"]: [dict(s, sleep=0.15) if i == 0 else s for i, s in enumerate(good())]
                       for e in six}}
    res, fk = run(view, sc, only=[e["entity_id"] for e in six], concurrency=3, verify="ids")
    c = "concurrency"
    L = ledger(view)
    threads = {x["thread"] for x in fk.calls}
    iv = sorted((x["t0"], x["t1"]) for x in fk.calls if "t1" in x)
    overlap = max(sum(1 for a, b in iv if a <= t < b) for t, _ in iv) if iv else 0
    check(c, "6 entities done on 3 threads, requests overlapping", res.counts == {"done": 6} and len(L) == 6
          and len(threads) == 3 and overlap >= 2 and not res.violations,
          f"{res.counts}; {len(threads)} threads; up to {overlap} requests at once")
    check(c, "one history file per entity, each whole", all(
        [e["event"] for e in events(view, r)][-1] == "end" for r in L) and len({r["history"] for r in L}) == 6)
    reset(view, c)


@case
def interrupt(view, ents):
    e0, e1, e2, e3, e4 = ents["genes"][:5]
    sc = F.FakeAPI({"entities": {
        e0["entity_id"]: good(),
        e1["entity_id"]: [dict(good()[0], sleep=1.5, signal="SIGINT")] + good()[1:],
        e2["entity_id"]: [dict(good()[0], sleep=2.5)] + good()[1:],
        e3["entity_id"]: good(), e4["entity_id"]: good()}})
    only = [e["entity_id"] for e in (e0, e1, e2, e3, e4)]
    res, _ = run(view, sc, only=only, concurrency=2, verify="ids")
    c = "interrupt"
    st = {r["entity_id"]: r["status"] for r in ledger(view)}
    check(c, "Ctrl-C: exit code 130, the running entities paused, no new ones started",
          res.exit_code == 130 and res.paused and st.get(e0["entity_id"]) == "done"
          and st.get(e1["entity_id"]) == "paused" and st.get(e2["entity_id"]) == "paused"
          and e3["entity_id"] not in st and e4["entity_id"] not in st, f"exit {res.exit_code}; {st}")
    n0 = len(sc.calls)
    res2, _ = run(view, sc, only=only, concurrency=2, verify="ids")
    st2 = {r["entity_id"]: r["status"] for r in ledger(view)}
    sent = {x["entity"] for x in sc.calls[n0:]}
    check(c, "the next run resumes the paused and unstarted entities, not the done one",
          res2.exit_code == 0 and set(st2.values()) == {"done"} and e0["entity_id"] not in sent
          and sent == {e["entity_id"] for e in (e1, e2, e3, e4)}, f"{st2}; sent {sorted(sent)}")
    reset(view, c)
    res3, _ = run(view, {"entities": {e0["entity_id"]: [dict(good()[0], signal="SIGTERM")] + good()[1:]}},
                  only=[e0["entity_id"], e1["entity_id"]], concurrency=1, verify="ids")
    st3 = {r["entity_id"]: r["status"] for r in ledger(view)}
    check(c, "SIGTERM: exit code 143, the running entity paused", res3.exit_code == 143
          and st3 == {e0["entity_id"]: "paused"}, f"exit {res3.exit_code}; {st3}")
    reset(view, c)


@case
def plan_status_cli(view, ents):
    c = "plan_status_cli"
    out = []
    q = R.plan(view, kinds="gene,drug,line", say=out.append)
    check(c, "plan: queue.parquet in priority order, counts and projected cost printed",
          os.path.exists(os.path.join(view, "review", "queue.parquet")) and len(q) == ents["n"]
          and list(q["kind"][:1]) == ["line"] and any("Projected cost" in x for x in out),
          f"{len(q)} entities; {[x for x in out if 'Projected' in x]}")
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC")}
    py = [sys.executable, "-m", "tahoemap", "review"]
    r1 = subprocess.run(py + ["run", "--out", view, "--kinds", "line"], cwd=REPO, env=env, capture_output=True,
                        text=True, timeout=120)
    check(c, "CLI review run without a cap: refuses (exit 2) after printing the projected cost",
          r1.returncode == 2 and "projected cost" in r1.stdout and "Refusing to start" in r1.stdout,
          f"exit {r1.returncode}: {r1.stdout[-200:]} {r1.stderr[-300:]}")
    sp = os.path.join(view, "script.json")
    with open(sp, "w", encoding="utf-8") as fh:
        json.dump({"entities": {ents["lines"][0]["entity_id"]: good()}, "keys": [KEY3]}, fh)
    r2 = subprocess.run(py + ["run", "--out", view, "--only", ents["lines"][0]["entity_id"], "--limit", "1",
                              "--fake", sp, "--verify", "ids"], cwd=REPO, env=env, capture_output=True, text=True,
                        timeout=120)
    check(c, "CLI review run --fake SCRIPT: the line reviewed, exit 0",
          r2.returncode == 0 and "1 done" in r2.stdout and "none the API would have rejected" in r2.stdout,
          f"exit {r2.returncode}: {r2.stdout[-300:]} {r2.stderr[-300:]}")
    os.remove(sp)
    r3 = subprocess.run(py + ["status", "--out", view, "--tables"], cwd=REPO, env=env, capture_output=True,
                        text=True, timeout=120)
    check(c, "CLI review status --tables", r3.returncode == 0 and "Spent:" in r3.stdout and "Tables:" in r3.stdout,
          r3.stdout[-300:] + r3.stderr[-300:])
    for r in (r1, r2, r3):
        SCANNED["bytes"] += len(r.stdout) + len(r.stderr)
        if any(s in r.stdout + r.stderr for s in SECRETS):
            check(c, "no key printed by the CLI", False)
    log = os.path.join(view, "review", "review.log")
    check(c, "the run log (review/review.log) written", os.path.exists(log))
    reset(view, c)


@case
def duplicate(view, work, out):
    c = "duplicate"
    dest, repo = os.path.join(work, "dup_out"), os.path.join(work, "dup_repo")
    for p in (dest, repo):
        shutil.rmtree(p, ignore_errors=True)
    had_review = os.path.exists(os.path.join(out, "review"))
    with contextlib.redirect_stdout(io.StringIO()):
        rec = cli.duplicate(out, dest, repo)
    arrays = sorted(glob.glob(os.path.join(out, "tensor", "*.npy")))
    same_fs = os.stat(out).st_dev == os.stat(work).st_dev
    linked = [a for a in arrays if os.stat(a).st_ino == os.stat(os.path.join(dest, "tensor", os.path.basename(a))
                                                               ).st_ino]
    notes = sorted(glob.glob(os.path.join(out, "vault", "**", "*.md"), recursive=True))[:1]
    copied = [n for n in notes if os.stat(n).st_ino != os.stat(os.path.join(dest, os.path.relpath(n, out))).st_ino]
    check(c, "the output duplicated: big arrays hard-linked (same file system), notes copied",
          arrays and (len(linked) == len(arrays) if same_fs else not linked) and rec["files"]["hard_linked"] > 0
          and copied == notes, f"{rec['files']}; {rec['bytes']['hard_linked'] / 1e6:.0f} MB shared, "
                               f"{rec['bytes']['copied'] / 1e6:.0f} MB copied")
    rec2 = json.load(open(os.path.join(dest, "duplicated_from.json"), encoding="utf-8"))
    git = find_git()                       # (on PATH, $TAHOE_GIT, or a MinGit next to the repository)
    head = git_out(git, REPO, "rev-parse", "HEAD")
    stamps = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(out, "stages", "*.json")))
    check(c, "duplicated_from.json: source, date, code commit, stage stamps",
          rec2["source"] == os.path.abspath(out) and rec2["date"] and rec2["code"]["commit"] == head
          and set(rec2["stages"]) == set(stamps) and len(stamps) >= 5,
          {k: rec2.get(k) for k in ("date",)} | {"stages": sorted(rec2["stages"])})
    clone_head = git_out(git, repo, "rev-parse", "HEAD")
    check(c, "--repo: the code repository cloned", head is not None and clone_head == head
          and (rec2.get("repo_clone") or {}).get("commit") == head, rec2.get("repo_clone"))
    res, _fk = run(dest, {}, kinds="line", limit=1, dry_run=True)
    check(c, "the copy works on its own (a dry run writes into the copy, not the source)",
          res.counts.get("dry_run") == 1 and os.path.exists(os.path.join(dest, "review", "dry_run", "summary.json"))
          and os.path.exists(os.path.join(out, "review")) == had_review, res.message)
    for p in (dest, repo):
        shutil.rmtree(p, ignore_errors=True)
    # a small output with the awkward cases: a temporary file, a symbolic link, a destination in use
    src, dest = os.path.join(work, "dup_src"), os.path.join(work, "dup_dest")
    for p in (src, dest):
        shutil.rmtree(p, ignore_errors=True)
    for d in ("stages", "tensor", "atlas", os.path.join("vault", "genes")):
        os.makedirs(os.path.join(src, d))
    shutil.copy(glob.glob(os.path.join(out, "stages", "*.json"))[0], os.path.join(src, "stages"))
    with open(os.path.join(src, "tensor", "R.npy"), "wb") as fh:
        fh.write(b"\x93NUMPY" + b"0" * 4096)
    with open(os.path.join(src, "tensor", "R.npy.tmp"), "wb") as fh:
        fh.write(b"partial")
    with open(os.path.join(src, "vault", "genes", "NQO1.md"), "w", encoding="utf-8") as fh:
        fh.write("# NQO1\n")
    os.makedirs(os.path.join(work, "elsewhere"), exist_ok=True)
    try:
        os.symlink(os.path.join(work, "elsewhere"), os.path.join(src, "atlas", "pseudobulk"))
        has_link = True
    except OSError:                                   # Windows without symlink rights (junctions: test_windows.py)
        has_link = False
    with contextlib.redirect_stdout(io.StringIO()):
        rec3 = cli.duplicate(src, dest)
    check(c, "temporary files left out, symbolic links kept as links" + ("" if has_link else
                                                                          " (no symlink rights: links not tested)"),
          not os.path.exists(os.path.join(dest, "tensor", "R.npy.tmp")) and rec3["files"]["skipped"] == 1
          and (not has_link or (os.path.islink(os.path.join(dest, "atlas", "pseudobulk"))
                                and rec3["files"]["symlinks"] == 1)), rec3["files"])
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            cli.duplicate(src, dest)
        refused = False
    except SystemExit:
        refused = True
    check(c, "refuses a destination that is not empty", refused)
    for p in (src, dest, os.path.join(work, "elsewhere")):
        shutil.rmtree(p, ignore_errors=True)


@case
def vault_splice(work, src, ents):
    """A fake review of 3 entities (a gene, a drug, a cell line) spliced into the vault and the map: the literature
    section with its callout and resolvable relative links, the Literature column of the partner tables, no broken
    wikilink, and no other note changed (an output without reviews builds exactly as before)."""
    from tahoemap import html_map, vault
    c = "vault_splice"
    sv = os.path.join(work, "splice_view")                # vault/, map/, stages/, review/ of its own; the rest linked
    if os.path.lexists(sv):
        shutil.rmtree(sv)
    os.makedirs(sv)
    for e in sorted(os.listdir(src)):
        if e == "stages":
            shutil.copytree(os.path.join(src, e), os.path.join(sv, e))
        elif e not in ("review", "vault", "map"):
            link_entry(os.path.join(src, e), os.path.join(sv, e))
    vt = os.path.join(sv, "vault")

    def notes():
        out = {}
        for dp, _dn, fns in os.walk(vt):
            if ".obsidian" in dp:
                continue
            for f in fns:
                if f.endswith(".md"):
                    p = os.path.join(dp, f)
                    out[os.path.relpath(p, vt)] = open(p, encoding="utf-8").read()
        return out

    with contextlib.redirect_stdout(io.StringIO()):
        R.plan(sv, kinds="line", say=lambda *a: None)     # review/ with a queue only: still no review to show
        vault.run(sv)
    before = notes()
    sv_vault = os.path.join(src, "vault")
    same_code = (json.load(open(os.path.join(src, "stages", "vault.json"), encoding="utf-8")).get("version") == vault.VERSION
                 if os.path.exists(os.path.join(src, "stages", "vault.json")) else False)
    if same_code and os.path.isdir(sv_vault):
        diff = [k for k, t in before.items() if k != "Home.md" and (not os.path.exists(os.path.join(sv_vault, k))
                                                                    or open(os.path.join(sv_vault, k),
                                                                            encoding="utf-8").read() != t)]
        check(c, "no review (review/ holds only a queue): every note as in the output's own vault", not diff
              and vault.review_fingerprint(sv) is None, f"{len(before)} notes compared (Home.md names the folder); "
                                                        f"differing: {diff[:5]}")
    # the gene, its first partner in its table (moves with it), a drug, a line
    g = ents["genes"][0]
    rel = pd.read_parquet(os.path.join(src, "relations", "gene_relations.parquet"),
                          columns=["col_a", "col_b", "rank", "cos"])
    mine = rel[(rel["col_a"] == g["col"]) & (rel["cos"] > 0)].sort_values("rank")
    pcol = int(mine["col_b"].iloc[0])
    genes = pd.read_parquet(os.path.join(src, "tables", "genes.parquet"), columns=["col", "label"]).set_index("col")
    plabel = str(genes.at[pcol, "label"])
    back = rel[(rel["col_a"] == pcol) & (rel["cos"] > 0)].sort_values("rank").head(vault.N_PARTNERS)
    reverse_shown = int(g["col"]) in set(back["col_b"].astype(int))
    d, ln = ents["drugs"][0], ents["lines"][0]
    gnote = (f"## What the literature says\n\n**In short.** [[{g['name']}]] moves with [[{plabel}]] "
             "([PMID:31000001](https://pubmed.ncbi.nlm.nih.gov/31000001/)).\n\n### What the data show\n"
             f"- raised by [[{d['name']} (drug)]]; strongest in [[{ln['name']} (line)]]\n"
             "- a link to [[NO_SUCH_NOTE_XYZ]] that must become plain text\n\n## Caveats\n- one compound\n")
    sc = {"entities": {g["entity_id"]: good(plabel, ("31000001", "31000002")),
                       d["entity_id"]: good(g["name"], ("31000003",)),
                       ln["entity_id"]: good(plabel, ("31000004",))}}
    sc["entities"][g["entity_id"]][-1]["submit_review"]["note_markdown"] = gnote
    res, fk = run(sv, sc, only=[g["entity_id"], d["entity_id"], ln["entity_id"]], verify="llm")
    check(c, "3 entities reviewed (fake API)", res.counts == {"done": 3} and not res.violations, res.counts)
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC")}
    st = subprocess.run([sys.executable, "-m", "tahoemap", "status", "--out", sv], cwd=REPO, env=env,
                        capture_output=True, text=True, timeout=120).stdout
    vline = next((x for x in st.splitlines() if x.strip().startswith("vault")), "")
    check(c, "after the review the vault and map stages are out of date", "literature reviews" in vline, vline)
    with contextlib.redirect_stdout(io.StringIO()):
        info = vault.run(sv)
        minfo = html_map.run(sv)
    after = notes()
    gpath = next(k for k in after if k.startswith("Genes" + os.sep) and k.endswith(os.sep + g["name"] + ".md"))
    ppath = next(k for k in after if k.startswith("Genes" + os.sep) and k.endswith(os.sep + plabel + ".md"))
    dpath = os.path.join("Drugs", f"{d['name']} (drug).md")
    lpath = os.path.join("Cell lines", f"{ln['name']} (line).md")
    check(c, "the vault stage counts 3 spliced reviews", info.get("literature_notes") == 3 and
          info.get("review", {}).get("notes") == 3, {k: info.get(k) for k in ("literature_notes",
                                                                             "literature_partner_cells", "review")})
    bad_links, ok_notes = [], []
    for k in (gpath, dpath, lpath):
        t = after.get(k, "")
        sec = t.split("## What the literature says", 1)[1].split("\n## ", 1)[0] if "## What the literature says" \
            in t else ""
        links = re.findall(r"\]\((\.\.[^)]+)\)", sec)
        for lk in links:
            if not os.path.exists(os.path.normpath(os.path.join(vt, os.path.dirname(k),
                                                                urllib.parse.unquote(lk)))):
                bad_links.append((k, lk))
        if (t.count("## What the literature says") == 1 and "> [!info] AI-agent literature review" in sec
                and "claude-opus-5-5" in sec and "Verification:" in sec and "supported" in sec
                and any(".jsonl" in x for x in links) and any(x.endswith(".json") for x in links)
                and "pubmed.ncbi.nlm.nih.gov/" in sec and '"literature-review"' in t.split("---", 2)[1]):
            ok_notes.append(k)
    check(c, "gene, drug and line notes: '## What the literature says' with the callout (agent, model, date, "
             "verification counts, history and review links)", len(ok_notes) == 3, ok_notes)
    check(c, "the callout's relative links resolve to the history file and the review JSON", not bad_links,
          bad_links or "all resolve")
    gt = after.get(gpath, "")
    gsec = gt.split("## What the literature says", 1)[1].split("\n## ", 1)[0]
    check(c, "the agent's note: its own heading dropped, '##' demoted, unknown links as plain text",
          "\n### Caveats" in gsec and "NO_SUCH_NOTE_XYZ" in gsec and "[[NO_SUCH_NOTE_XYZ]]" not in gsec
          and f"[[{plabel}]]" in gsec and f"[[{d['name']} (drug)]]" in gsec, gsec[:300])
    tab = gt.split("## Genes that move with it", 1)[1].split("\n## ", 1)[0]
    row = next((x for x in tab.splitlines() if x.startswith(f"| [[{plabel}]] |")), "")
    check(c, "the partner table: a Literature column with the verdict and its linked citations",
          "| Literature |" in tab and "established" in row and "](https://pubmed.ncbi.nlm.nih.gov/31000001/)" in row,
          row[:200])
    prow = next((x for x in after.get(ppath, "").splitlines() if x.startswith(f"| [[{g['name']}]] |")), "")
    check(c, "the partner's own table shows the verdict of the reviewed gene's review" if reverse_shown else
          "the partner's note: no reverse row expected (the reviewed gene is not in its table)",
          (f"({g['name']}'s review)" in prow) if reverse_shown else True, prow[:200])
    names = {os.path.splitext(os.path.basename(k))[0].lower() for k in after}
    names |= {os.path.splitext(f)[0].lower() for dp, _d, fns in os.walk(vt) for f in fns if f.endswith(".canvas")}
    broken = [(k, m) for k, t in after.items() for m in re.findall(r"\[\[([^\]|#]+)", t)
              if re.sub(r"\.(md|canvas)$", "", m.strip(), flags=re.I).lower() not in names]
    check(c, "no unresolved wikilink in the vault", not broken, broken[:5] or f"{len(after)} notes")
    changed = sorted(k for k in after if before.get(k) != after[k])
    allowed = {gpath, dpath, lpath, "Home.md", "How to read this vault.md"}
    extra = [k for k in changed if k not in allowed and k != ppath]
    check(c, "no other note changed (the 3 reviewed, the partner's, Home, How to read)", not extra
          and {gpath, dpath, lpath} <= set(changed) and set(before) == set(after), f"{len(changed)} changed: "
                                                                                   f"{changed[:8]}; extra {extra[:5]}")
    html = open(os.path.join(sv, "map", "gene_map.html"), encoding="utf-8").read()
    m = re.search(r'<script id="tm-data" type="application/json">(.*?)</script>', html, re.S)
    Dm = json.loads(m.group(1)) if m else {}
    ent = {cc: i for i, cc in enumerate(Dm.get("col", []))}
    lit = Dm.get("lit") or []
    # lit: [a, b, kind, citations]; lit_v[kind] = [label, explanation, shown verdict, check_status]
    trip = {(lit[t], lit[t + 1]): Dm["lit_v"][lit[t + 2]][2] for t in range(0, len(lit) - 3, 4)}
    on_map = ent.get(int(g["col"]), 10 ** 9) < Dm.get("n", 0) and ent.get(pcol, 10 ** 9) < Dm.get("n", 0)
    check(c, "the map embeds the verdicts for the side panel's badges", minfo.get("review") is not None and (
        trip.get((ent.get(int(g["col"])), ent.get(pcol))) == "established" if on_map else "lit" in Dm)
        and "litBadge" in html, f"{len(trip)} gene-gene verdicts embedded; {g['name']} - {plabel} on the map: "
                                f"{on_map}")
    st = subprocess.run([sys.executable, "-m", "tahoemap", "status", "--out", sv], cwd=REPO, env=env,
                        capture_output=True, text=True, timeout=120).stdout
    vline = next((x for x in st.splitlines() if x.strip().startswith("vault")), "")
    check(c, "rebuilt: the vault stage is up to date again", vline.split()[1:2] == ["done"], vline)
    bad = scan_for_keys(os.path.join(sv, "review"))
    check(c, "no API key in any file written", not bad, bad[:5])
    shutil.rmtree(sv, ignore_errors=True)


# ----------------------------------------------------------------------------- the vault and the map (review 2, ui)
# findings science#1 / ui#0, ui#1, ui#2, ui#3, ui#5, ui#6, ui#7, ui#8
def own_view(work, src, name):
    """A view of src with stages/ copied and review/, vault/, map/ of its own (everything else linked)."""
    sv = os.path.join(work, name)
    if os.path.lexists(sv):
        shutil.rmtree(sv)
    os.makedirs(sv)
    for e in sorted(os.listdir(src)):
        if e == "stages":
            shutil.copytree(os.path.join(src, e), os.path.join(sv, e))
        elif e not in ("review", "vault", "map"):
            link_entry(os.path.join(src, e), os.path.join(sv, e))
    return sv


def lit_section(text):
    return text.split("## What the literature says", 1)[1].split("\n## ", 1)[0] if "## What the literature says" \
        in text else ""


def outside_fences(text):
    out, fence = [], None
    for line in text.split("\n"):
        f = re.match(r"^(`{3,}|~{3,})", line)
        if fence is None and f:
            fence = f.group(1)
        elif fence is not None and line == fence:
            fence = None
        elif fence is None:
            out.append(line)
    return "\n".join(out), fence


def map_lit(sv):
    """{(entry a, entry b): [label, explanation, shown verdict, check_status]} and the entry of each gene col."""
    html = open(os.path.join(sv, "map", "gene_map.html"), encoding="utf-8").read()
    m = re.search(r'<script id="tm-data" type="application/json">(.*?)</script>', html, re.S)
    Dm = json.loads(m.group(1)) if m else {}
    lit = Dm.get("lit") or []
    return ({(lit[t], lit[t + 1]): Dm["lit_v"][lit[t + 2]] for t in range(0, len(lit) - 3, 4)},
            {cc: i for i, cc in enumerate(Dm.get("col", []))}, Dm.get("n", 0))


MAL_NOTE = """## What the literature says

**In short.** [[{g}]] moves with [[{p0}]] ([PMID:31000003](https://pubmed.ncbi.nlm.nih.gov/31000003/)).
<script>alert('script')</script><img src=x onerror="alert('img')"> <iframe src="https://evil.example/phish"></iframe>
![pixel](https://evil.example/track.png) [click me](javascript:alert(document.cookie)) [d](data:text/html;base64,PHM+)
[vb](vbscript:msgbox(1)) <a href="https://evil.example/a">anchor</a> <style>body{{display:none}}</style>
see https://evil.example/bare and <https://evil.example/auto>; [ok](https://www.ncbi.nlm.nih.gov/gene/1017)
<!-- a closed comment --> visible %% an Obsidian comment %% after
```dataviewjs
dv.paragraph("runs in Obsidian with Dataview")
```
Click [x][r] and ![tracker]

> [r]: javascript:alert('ref')
> [tracker]: https:/evil.example/track.png

> [!note]
> ```dataviewjs
> dv.paragraph("nested in a callout")
> ```

_References were verified against PubMed._
_AI-generated literature review of this run's data; citations were checked against PubMed and their abstracts._

Some setext text
---
<!-- an unclosed comment that would hide the rest
```
an unclosed fence
"""


def sanitize_gaps(c, VT):
    """ui#2 / ui#3 (round 2): what the sanitiser must also stop - a reference definition to javascript: / data: /
    vbscript: or another site inside a blockquote, callout or list item (its destination on the same or the next
    line), a shortcut reference image '![name]', a fence opened inside a blockquote, callout or list item with a
    plugin language, link text the patterns cannot parse (a code span with ']', deeper brackets), a footnote whose
    text is a URL (a reference definition to a renderer without footnotes), what a removal makes (a fence at the
    start of a line, '%%'), a definition / label / title running into a fence, a bare URL inside a word or after an
    allowed one, quadratic time on long bracket runs; and the agent's own provenance in an underscore-italic line
    ('_Citations were checked ..._'). (Checked against commonmark.js 0.31 and marked 18 while fixing; here without
    a JavaScript renderer.)"""
    sn = VT.sanitize_note
    ref = {x: sn(x) for x in ("Click [x][r]\n\n> [r]: javascript:alert(1)", "Click [x][r]\n\n> [r]:\n> javascript:alert(2)",
                              "Click [x][r]\n\n> [r]: data:text/html;base64,PHM+", "Click [x][r]\n\n- [r]: vbscript:msgbox(1)",
                              "Click [x][r]\n\n> > - [r]: javascript:alert(4) \"t\"", "Click [x][r]\n\n- [r]:\njavascript:alert(5)",
                              "Click [x][r]\n\n1) [r\n   x]: https://evil.example/a",
                              "Click [x][r]\n\n> [r]: https://www.ncbi.nlm.nih.gov/gene/1017")}
    vals = list(ref.values())
    check(c, "ui#3: a reference definition is removed at any container depth unless it points to an allowed site",
          not any(re.search(r"javascript|data:|vbscript|evil", v) for v in vals[:-1])
          and all(v.startswith("Click [x][r]") for v in vals)
          and vals[-1].endswith("> [r]: https://www.ncbi.nlm.nih.gov/gene/1017\n>"), ref)
    img = [sn("![pixel]\n\n> [pixel]: https:/evil.example/track.png"),
           sn("![pixel]\n\n[pixel]: https://www.ncbi.nlm.nih.gov/track.png"), sn("![pixel][]\n\n[pixel]: https://doi.org/x"),
           sn("![a [b [c]] d](https://evil.example/x.png)"), sn("![a `]` b](https://evil.example/x.png)")]
    check(c, "ui#2: no image: a shortcut reference image ('![name]') or one the patterns cannot parse is text",
          not any("![" in x for x in img) and "evil.example/track" not in img[0] and img[1].startswith("pixel\n"), img)
    nf = [sn("> [!note]\n> ```dataviewjs\n> dv.paragraph(1)\n> ```"), sn("- ```dataviewjs\n  dv.paragraph(1)\n  ```"),
          sn("> - ~~~ mermaid\n>   graph TD\n>   ~~~"), sn("1. ```dataviewjs\n   x\n   ```"),
          sn("[^1]: ```dataviewjs\n    x\n    ```"), sn("> ```python\n> x = 1\n> ```")]
    check(c, "ui#2: a fence inside a blockquote, callout, list item or footnote keeps only a plain code language",
          not any(re.search(r"dataviewjs|mermaid", x) for x in nf) and nf[0] == "> [!note]\n> ```\n> dv.paragraph(1)\n> ```"
          and nf[-1] == "> ```python\n> x = 1\n> ```", nf)
    lk = [sn("[a `]` b](javascript:alert(1))"), sn("[a [b [c]] d](javascript:alert(1))"),
          sn("[a <b>]</b> c](vbscript:x)"), sn("text[^1]\n\n[^1]: javascript:alert(1)"),
          sn("[ok [deep [er]]](https://pubmed.ncbi.nlm.nih.gov/1/)")]
    dests = [d for x in lk for d in re.findall(r"(?<!\\)\]\(\s*<?([^\s)>]*)", x)]
    check(c, "ui#3: link text the patterns cannot parse never makes a link elsewhere ('](' escaped), a footnote's "
             "URL is no destination; an allowed link with deep brackets stays",
          all(d.startswith(VT.LIT_LINK_PREFIXES) for d in dests) and "]\\(javascript" in lk[0]
          and "]\\(javascript" in lk[1] and "[^1]: \u200bjavascript" in lk[3]
          and lk[4] == "[ok [deep [er]]](https://pubmed.ncbi.nlm.nih.gov/1/)", lk)
    made = [sn("<script>alert(1)</script>```dataviewjs\n<img src=x onerror=alert(2)>"), sn("%<b></b>% hidden?"),
            sn("> [```dataviewjs](javascript:x)\n> dv.paragraph(1)"), sn("<!-- c -->~~~\n<script>alert(3)</script>"),
            sn("<[img](x) src=x onerror=alert(4)>")]
    check(c, "ui#2: what a removal makes is neutralised: a fence at the start of a line (it would hide all that "
             "follows) is text, no %% comment, no nested plugin fence, no tag a removed link puts together",
          all(outside_fences(x)[1] is None and "<script" not in x and "<img" not in x for x in made)
          and made[0].startswith("\\```") and "%%" not in made[1] and "dataviewjs" not in made[2]
          and made[3].startswith("\\~~~"), made)
    edge = [sn("[r]:\n```\n<script>alert(1)</script>\n```\n\n[x][r]"),
            sn('[r]: https://pubmed.ncbi.nlm.nih.gov/1/ "a\n```\n<script>alert(1)</script>\n"\n```'),
            sn("[a\n```\nb]: javascript:alert(1)\n```")]
    check(c, "ui#2: a definition, link label or title above a fence cannot run into it (a blank line before the "
             "fence; a kept definition has no title and a blank line after it), so the fence starts where the "
             "renderer starts it",
          edge[0].startswith("[r]:\n\n```\n") and edge[1].startswith("[r]: https://pubmed.ncbi.nlm.nih.gov/1/\n\n```")
          and edge[2].startswith("[a\n\n```\n"), edge)
    urls = [sn("xhttps://evil.example/a and www.evil.example, xwww.evil.example and ftp://evil.example/f"),
            sn("https://pubmed.ncbi.nlm.nih.gov/1/https://evil.example/b"),
            sn("https://evil.example/x)<https://pubmed.ncbi.nlm.nih.gov/2/>"),
            sn("t[^1]\n\n[^1]: javascript&colon;alert(1)")]
    check(c, "ui#3: no bare URL to another site can start a link (in a word, after an allowed URL, ftp://), an "
             "allowed link next to one stays whole, a footnote's first word is no destination (entities too)",
          not re.search(r"(?:https?|ftp)://(?!pubmed)|www\.evil", "".join(urls[:3]))
          and urls[1].startswith("https://pubmed.ncbi.nlm.nih.gov/1/https:\u200b//")
          and "[https://pubmed.ncbi.nlm.nih.gov/2/](https://pubmed.ncbi.nlm.nih.gov/2/)" in urls[2]
          and "[^1]: \u200bjavascript&colon;" in urls[3], urls)
    t0 = time.time()
    for x in ("![" * 20000, "[" + "\\[" * 40000, "[a\n" * 20000, ("[" + "a" * 299) * 300):
        sn(x)
    check(c, "ui#2: the sanitiser takes linear time on long runs of brackets (no backtracking blow-up)",
          time.time() - t0 < 3, f"{time.time() - t0:.2f} s")
    own = ["_Citations were checked against PubMed and their abstracts._", "_References were verified against PubMed._",
           "*Citations were checked against PubMed.*"]
    kept = ["Two cohorts agree: these claims were verified in independent patient samples.",
            "_The references verified it in mice._"]
    dropped = VT.drop_self_check("Text.\n" + "\n".join(own + kept) + "\n")
    check(c, "ui#2: the vault drops the agent's own provenance in an underscore-italic line; other lines stay",
          dropped == "Text.\n" + "\n".join(kept) + "\n", dropped)
    vault_self_check_rule(c, VT)


def vault_self_check_rule(c, VT):
    """The vault's drop_self_check is verify.drop_self_check, the sentence-level rule of the stored notes: a line that
    reports a finding next to 'citations were checked' (or after 'Verify before relying on it', or in a line opening
    'AI-generated literature review') is kept whole - the earlier line rule dropped any line under 400 characters
    with those words; a sentence that only vouches for the checking, and the disclaimers of its paragraph, go."""
    from tahoemap.review import verify as V
    found = ["Citations were checked, but none links PIR to HMOX1 in hypoxia.",
             "Verify before relying on it: the HMOX1 link rests on one mouse study.",
             "_Citations were checked in PubMed for the pair; none reports PIR with HMOX1._",
             "_AI-generated literature review: NQO1 rises 4x with every NRF2 activator._"]
    mixed = ("NQO1 is an NRF2 target.\n" + "\n".join(found) + "\n_Citations were checked against PubMed and their "
             "abstracts._\n")
    footer = ("NQO1 is an NRF2 target.\n\n_AI-generated literature review of this run's data; citations were checked "
              "against PubMed and their abstracts.\nVerify before relying on it._\n")
    got = {x: VT.drop_self_check(x) for x in [mixed, footer] + [f + "\n" for f in found]}
    check(c, "a finding next to 'citations were checked' (or a disclaimer's words) is kept whole; only the sentence "
             "that just vouches for the checking goes",
          got[mixed] == "NQO1 is an NRF2 target.\n" + "\n".join(found) + "\n"
          and all(got[f + "\n"] == f + "\n" for f in found), got[mixed])
    check(c, "the agent's own footer paragraph (self-check + disclaimers) is dropped whole",
          got[footer] == "NQO1 is an NRF2 target.\n", got[footer])
    emph = {"**NQO1 is up 4x.** Citations were checked against PubMed.\n**HMOX1 rises too.**":
            "**NQO1 is up 4x.**\n**HMOX1 rises too.**\n",
            "Text.\n_Citations were checked against PubMed._\n_The references verified it in mice._\n":
            "Text.\n_The references verified it in mice._\n"}
    got.update({x: VT.drop_self_check(x) for x in emph})
    check(c, "a kept sentence that ends its paragraph keeps its closing emphasis ('_' / '**'), next to a dropped one",
          all(got[x] == want for x, want in emph.items()), [got[x] for x in emph])
    check(c, "the vault applies the same rule as the stored notes (verify.drop_self_check)",
          all(VT.drop_self_check(x) == V.drop_self_check(x) for x in got) and VT.drop_self_check(None) == "",
          [x[:40] for x in got if VT.drop_self_check(x) != V.drop_self_check(x)])


@case
def vault_map_literature(work, src, ents):
    """A crafted malicious review (script / img onerror / iframe / style / javascript:, data:, vbscript: links, a
    remote image, an HTML comment and an unclosed one, an unclosed code fence, a dataviewjs block, a setext heading,
    the agent's own 'citations were checked' line, a partner named with HTML), a fabricated PMID that verification
    removes, a verdict the checker finds not supported and two verdicts on one partner, through the fake API into a
    copy, then the vault and the map: the note is sanitised and keeps its generated sections; an unverified verdict
    reads 'unverified' (vault column, verdict list, map badge), never 'established'; one verdict per partner, the
    same in the vault and the map; the callout's verification from the review's counts (unchecked ids, llm status);
    the generated footer; a connections.parquet older than a review is not used and the vault and map are out of
    date. In a browser (Playwright, when installed): the badges, no script run, and the physics tabs (a slow
    double-click pins; a small simulation animates the sign switch for > 1.5 s)."""
    from tahoemap import html_map, vault as VT
    c = "vault_map_literature"
    # -- the rules, without a run
    pv = VT.pick_verdict
    rule = [pv([{"verdict": "established", "check_status": "unchecked"}, {"verdict": "plausible",
                                                                          "check_status": "unchecked"}])["verdict"],
            pv([{"verdict": "plausible", "check_status": "not_checkable"},
                {"verdict": "established", "check_status": "supported"}])["verdict"],
            pv([{"verdict": "established", "check_status": "not_supported"},
                {"verdict": "plausible", "check_status": "not_checkable"}])["verdict"],
            pv([{"verdict": "indirect", "check_status": "supported"},
                {"verdict": "established", "check_status": "partly"}])["verdict"]]
    check(c, "ui#8: one verdict per partner: the strongest verified one, else the agent's first",
          rule == ["established", "established", "plausible", "established"], rule)
    old = [VT.lit_status({"verdict": "established", "unverified": True, "citations": ""}),
           VT.lit_status({"verdict": "established", "check": "not supported", "citations": "PMID:1"}),
           VT.lit_status({"verdict": "indirect", "citations": "PMID:1;PMID:2"}),
           VT.lit_status({"verdict": "established", "citations": "PMID:1", "check_status": "not_supported",
                          "shown_verdict": "established"})]
    check(c, "science#1: rows without check_status (older reviews) and an inconsistent shown_verdict",
          old == [("citations_removed", "unverified"), ("not_supported", "unverified"), ("unchecked", "indirect"),
                  ("not_supported", "unverified")], old)
    sanitize_gaps(c, VT)
    inj = VT.citation_link('DOI:10.1234/x"><img/src=x/onerror=alert(1)>')
    par = VT.citation_link("DOI:10.1016/S0092-8674(00)81096-3")
    check(c, "ui#3: a DOI with markup is not linked and is escaped; a DOI with parentheses is linked whole",
          "<img" not in inj and "](" not in inj and par == "[DOI:10.1016/S0092-8674(00)81096-3](https://doi.org/"
          "10.1016/S0092-8674%2800%2981096-3)", (inj, par))
    vt = VT.Vault._verification_text
    base = {"mode": "llm", "counts": {"n_citations": 4}, "llm": {"status": "done", "detail": "", "supported": 2,
                                                                 "partly": 0, "not_supported": 1, "not_checkable": 0}}
    t_ok = vt(dict(base, ids={"status": "done", "checked": 4, "removed": 1, "unchecked": 0, "retracted": 0,
                              "found": 3}), {})
    t_un = vt(dict(base, ids={"status": "done", "checked": 1, "removed": 0, "unchecked": 3, "retracted": 0,
                              "found": 1}), {})
    t_old = vt({"mode": "ids", "counts": {"n_citations": 3}, "ids": {"found": 1, "missing": [],
                                                                      "unchecked": ["PMID:1", "PMID:2"]}}, {})
    t_nr = vt(dict(base, ids={"status": "done", "checked": 4, "removed": 0, "unchecked": 0, "retracted": 0},
                   llm={"status": "not_run", "detail": "the run was stopping"}), {})
    t_fail = vt(dict(base, ids={"status": "failed", "detail": "ncbi: no answer", "checked": 0, "removed": 0,
                                "unchecked": 4, "retracted": 0}, llm={"status": "failed", "detail": "over budget"}),
                {})
    t_off = vt({"mode": "off", "counts": {"n_citations": 2}, "ids": {"status": "not_run", "unchecked": 2}}, {})
    check(c, "ui#1: the callout's verification from the counts: 'every cited id looked up' only when none was "
             "left unchecked; unchecked ids, a check not run or failed, and --verify off are said",
          "every cited id looked up in PubMed / Crossref: 3 found, 1 removed" in t_ok and "2 supported" in t_ok
          and "every cited id" not in t_un and "1 of the 4 cited ids looked up" in t_un
          and "3 could not be looked up" in t_un and "every cited id" not in t_old
          and "2 could not be looked up" in t_old and "not checked against the abstracts (the run was stopping)"
          in t_nr and "--recheck" in t_nr and "the id check failed (ncbi: no answer)" in t_fail
          and "the check failed: over budget" in t_fail and "every cited id" not in t_fail
          and "--verify off" in t_off and "were not looked up" in t_off, [t_un, t_old, t_nr, t_fail])
    # -- a run: the malicious review through the fake API
    sv = own_view(work, src, "lit_view")
    g = ents["genes"][1]
    rel = pd.read_parquet(os.path.join(src, "relations", "gene_relations.parquet"), columns=["col_a", "col_b", "rank"])
    genes = pd.read_parquet(os.path.join(src, "tables", "genes.parquet"), columns=["col", "label"]).set_index("col")
    pcols = [int(x) for x in rel[rel["col_a"] == g["col"]].sort_values("rank")["col_b"].head(5)]
    P = [str(genes.at[x, "label"]) for x in pcols]
    evil = "<img src=x onerror=alert('P')>"
    cv = [{"partner": P[0], "verdict": "established", "citations": ["PMID:39999999"]},     # fabricated: removed
          {"partner": P[1], "verdict": "established", "citations": ["PMID:31000002"]},     # checker: not supported
          {"partner": P[2], "verdict": "plausible", "citations": []},                      # two verdicts on P[2]:
          {"partner": P[2], "verdict": "established", "citations": ["PMID:31000003"]},     # ... this one supported
          {"partner": evil, "verdict": "plausible", "citations": []},
          {"partner": P[3], "verdict": "indirect", "citations": ["PMID:31000004", "PMID:31000007"]}]
    rv = F.sample_review(P[2], ("31000003",), note=MAL_NOTE.format(g=g["name"], p0=P[0]))
    rv["connection_verdicts"] = [dict({"relation": "both NRF2 targets", "data_evidence": "moves with: cos +0.60"}, **v)
                                 for v in cv]
    steps = [{"tool_use": [{"name": "pubmed_search", "input": {"query": "x AND NRF2", "max_results": 10}}]},
             {"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000002", "31000003", "31000004",
                                                                            "31000007"]}}]},
             {"submit_review": rv}, {"submit_review": rv}]          # the first is refused: 39999999 was never read
    chk = {"summary": "s", "verdicts": [                            # claims E1, M1, V2, V4, V6 (V1 lost its paper)
        {"claim_id": "E1", "verdict": "supported", "direction": "same as the data", "reason": "PMID:31000003"},
        {"claim_id": "M1", "verdict": "supported", "direction": "not applicable", "reason": "PMID:31000003"},
        {"claim_id": "V2", "verdict": "not supported", "direction": "not stated", "reason": "PMID:31000002: other"},
        {"claim_id": "V4", "verdict": "supported", "direction": "same as the data", "reason": "PMID:31000003"},
        {"claim_id": "V6", "verdict": "partly", "direction": "same as the data", "reason": "one gene only"}]}
    res, _fk = run(sv, {"entities": {g["entity_id"]: steps}, "checker": [{"submit_check": chk}]},
                   only=g["entity_id"], verify="llm")
    rj = os.path.join(sv, "review", "reviews", "gene", os.listdir(os.path.join(sv, "review", "reviews", "gene"))[0])
    js = json.load(open(rj, encoding="utf-8"))
    st = [(v["partner"], v.get("check_status"), v.get("shown_verdict")) for v in js.get("connection_verdicts") or []]
    check(c, "the review stored: the fabricated PMID removed, the checker's 'not supported', unverified shown",
          res.counts == {"done": 1} and [x[1:] for x in st] == [
              ("citations_removed", "unverified"), ("not_supported", "unverified"), ("not_checkable", "plausible"),
              ("supported", "established"), ("not_checkable", "plausible"), ("partly", "indirect")], st)
    with contextlib.redirect_stdout(io.StringIO()):
        VT.run(sv)
        html_map.run(sv)
    vt_dir = os.path.join(sv, "vault")
    gpath = next(os.path.join(dp, f) for dp, _d, fns in os.walk(vt_dir) for f in fns if f == g["name"] + ".md")
    gt = open(gpath, encoding="utf-8").read()
    sec = lit_section(gt)
    rows = {}                                                     # partner -> its Literature cell
    for head in ("## Genes that move with it", "## Genes that move opposite"):
        tab = gt.split(head, 1)[1].split("\n## ", 1)[0] if head in gt else ""
        for line in tab.splitlines() if "| Literature |" in tab else []:
            m = re.match(r"^\| \[\[([^\]|]+)\]\] \|.*\| ([^|]*) \|$", line)
            if m:
                rows[m.group(1)] = m.group(2).strip()
    vline = next((x for x in sec.splitlines() if x.startswith("**Connection verdicts**")), "")
    check(c, "science#1 / ui#0: the vault's Literature column and verdict list show 'unverified' (with the agent's "
             "verdict and why) for the removed and the not-supported verdict, never 'established'",
          rows.get(P[0], "").startswith("unverified (agent: established; citations not found)")
          and rows.get(P[1], "").startswith("unverified (agent: established; not supported)")
          and f"[[{P[0]}]] unverified (agent: established; citations not found)" in vline
          and f"[[{P[1]}]] unverified" in vline and f"[[{P[0]}]] established" not in vline,
          {p: rows.get(p) for p in P[:4]})
    check(c, "ui#8: one verdict per partner: P2's supported 'established' (not its first, 'plausible'), once",
          rows.get(P[2], "").startswith("established (supported) (of 2 verdicts it gave)")
          and vline.count(f"[[{P[2]}]]") == 1 and rows.get(P[3], "").startswith("indirect (partly supported)"),
          {p: rows.get(p) for p in P[2:4]})
    plain, open_fence = outside_fences(sec)
    bad = [x for x in ("<script", "<img", "<iframe", "<a ", "<style", "javascript:", "vbscript:", "data:text",
                       "](https://evil", "![", "<!--", "dataviewjs", "%%", "alert('script')", "display:none",
                       "alert('ref')", "https:/evil", "[tracker]:") if x in sec]
    check(c, "ui#2 / ui#3: no raw HTML, comment, image, script or non-allowlisted link survives in the section; "
             "fences closed; links only to the allowed sites",
          not bad and open_fence is None and not re.search(r"<[A-Za-z/!?]", plain)
          and set(re.findall(r"\]\((https?://[^/)]+)", sec)) <= {"https://pubmed.ncbi.nlm.nih.gov",
                                                                 "https://www.ncbi.nlm.nih.gov"}
          and "[ok](https://www.ncbi.nlm.nih.gov/gene/1017)" in sec and "https:​//evil.example/bare" in sec
          and "&lt;!-- an unclosed comment" in sec and "Some setext text\n\n---" in sec
          and "pixel" in sec and "click me" in sec and "Click [x][r] and tracker" in sec
          and '> ```\n> dv.paragraph("nested in a callout")' in sec,
          bad or re.findall(r"<[A-Za-z/!?].{0,30}", plain))
    heads = re.findall(r"^## (.+)$", gt.split("## What the literature says", 1)[1], re.M)
    check(c, "ui#2: the generated sections after it are still headings (not hidden in a comment or code block)",
          heads[:1] and heads[0] in ("What is on record", "Data") and "Sources" in heads, heads)
    check(c, "ui#3: a partner named with HTML is escaped in the verdict list",
          "&lt;img src\\=x onerror\\=alert('P')&gt; plausible" in vline and evil not in gt, vline[-160:])
    check(c, "ui#2: the generated note_footer is appended; the agent's own 'citations were checked' line is gone",
          js.get("note_footer") and js["note_footer"] in sec and "were checked against PubMed" not in sec
          and "were verified against PubMed" not in sec
          and "every cited id looked up in PubMed / Crossref" in sec, sec[-400:])
    # -- the map: the same verdicts, chosen by the same rule
    trip, ent, n = map_lit(sv)
    a = ent.get(int(g["col"]))
    lab = {P[i]: trip.get((a, ent.get(pcols[i]))) for i in range(4) if ent.get(pcols[i], n) < n}
    same = all(lab[p] is None or lab[p][0] == rows.get(p, "").split(" · ")[0].split(" (agent:")[0]
               .replace(" (of 2 verdicts it gave)", "") for p in lab)
    check(c, "science#1 / ui#0 / ui#8: the map's badges: 'unverified' for the removed and the not-supported "
             "verdict, P2's supported 'established', the same labels as the vault",
          a is not None and a < n and lab.get(P[0], [""])[0] == "unverified" and lab.get(P[1], [""])[0] ==
          "unverified" and lab.get(P[2], [""])[0] == "established (supported)" and same,
          {p: (v[0], v[3]) if v else None for p, v in lab.items()})
    browser_checks(c, sv, g["name"], P)
    # -- ui#5: a review newer than connections.parquet (a run killed before rebuilding the table)
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC")}

    def stage_line(name):
        out = subprocess.run([sys.executable, "-m", "tahoemap", "status", "--out", sv], cwd=REPO, env=env,
                             capture_output=True, text=True, timeout=120).stdout
        return next((x for x in out.splitlines() if x.strip().startswith(name)), "")
    before = (stage_line("vault"), stage_line("map"))
    js["connection_verdicts"].append({"partner": P[4], "verdict": "plausible", "citations": [],
                                      "relation": "r", "data_evidence": "d", "check_status": "not_checkable",
                                      "shown_verdict": "plausible"})
    with open(rj, "w", encoding="utf-8") as fh:
        json.dump(js, fh)
    stale = VT.connections_stale(sv)
    after = (stage_line("vault"), stage_line("map"))
    rows5 = VT.review_connections(sv)
    with contextlib.redirect_stdout(io.StringIO()):
        VT.run(sv)
        html_map.run(sv)
    gt5 = open(gpath, encoding="utf-8").read()
    check(c, "ui#5: a review newer than connections.parquet: the table is stale, status says the vault and the map "
             "are out of date, the verdicts come from the JSONs and reach the rebuilt note",
          before[0].split()[1:2] == ["done"] and stale and all("literature reviews" in x for x in after)
          and any(r["partner"] == P[4] for r in rows5) and f"[[{P[4]}]] plausible" in lit_section(gt5)
          and stage_line("vault").split()[1:2] == ["done"], {"before": before, "after": after, "stale": stale})
    bad = scan_for_keys(os.path.join(sv, "review"))
    check(c, "no API key in any file written", not bad, bad[:5])
    shutil.rmtree(sv, ignore_errors=True)


def browser_checks(c, sv, gname, P):
    """The map in a headless browser (skipped when Playwright or its Chromium is missing): the side panel's badges
    of the malicious review, no script of the review run; ui#7: a small simulation animates the sign switch for
    > 1.5 s; ui#6: a double-click with a 300 ms or a 450 ms gap pins the gene clicked first (user pin) and the
    second click selects nothing; a double-click with a micro-drag in one click pins the gene double-clicked, not
    that of an earlier click."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        check(c, "browser checks", True, "skipped: Playwright is not installed")
        return
    settled = "() => { const s = TAHOE_MAP.sim('{t}'); return s && s.n > 0 && !s.moving; }"
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            try:
                pg = b.new_page(viewport={"width": 1300, "height": 800})
                errs = []
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("dialog", lambda d: (errs.append("dialog: " + d.message), d.dismiss()))
                pg.goto(pathlib.Path(sv, "map", "gene_map.html").resolve().as_uri())
                pg.wait_for_function("() => !!window.TAHOE_MAP")
                sym = pg.evaluate("TAHOE_MAP.data.sym")
                gi = sym.index(gname)
                pg.evaluate(f"TAHOE_MAP.select({gi})")
                pg.wait_for_timeout(200)
                badges = dict(pg.evaluate("""() => [...document.querySelectorAll('#panel .bd.lit, .bd.lit')]
                    .filter(e => e.closest('tr')).map(e => [e.closest('tr').querySelector('td').textContent,
                                                            e.textContent])"""))
                check(c, "browser: the side panel's badges ('lit: unverified' for the removed and the not-supported "
                         "verdict), and nothing of the review runs", badges.get(P[0]) == "lit: unverified"
                      and badges.get(P[1]) == "lit: unverified" and badges.get(P[2]) == "lit: established (supported)"
                      and not errs, {"badges": badges, "errors": errs})
                anim = {}
                for t in ("nbr", "mod"):
                    pg.click(f"#tabs [data-tab='{t}']")
                    pg.wait_for_function(settled.replace("{t}", t), timeout=60000)
                    t0 = time.time()
                    pg.click(f"#pane-{t} [data-k='opp1']")
                    pg.wait_for_timeout(1500)
                    mid = pg.evaluate(f"TAHOE_MAP.sim('{t}')")
                    pg.wait_for_function(settled.replace("{t}", t), timeout=60000)
                    anim[t] = (mid["n"], mid["moving"], round(mid["alpha"], 4), round(time.time() - t0, 2))
                    pg.click(f"#pane-{t} [data-k='opp0']")
                check(c, "ui#7: a small simulation still moves 1.5 s after the sign switch, and settles",
                      all(v[1] and v[0] < 500 for v in anim.values()), anim)
                pg.click("#tabs [data-tab='nbr']")
                res = {}
                for gap in (300, 450):
                    pg.evaluate(f"TAHOE_MAP.select({gi})")
                    pg.wait_for_timeout(100)
                    pg.wait_for_function(settled.replace("{t}", "nbr"), timeout=60000)
                    s = pg.evaluate("TAHOE_MAP.sim('nbr')")
                    box = pg.evaluate("(() => { const r = document.querySelector('#pane-nbr canvas')"
                                      ".getBoundingClientRect(); return [r.left, r.top]; })()")
                    tgt = None
                    for i, f in zip(s["ids"], s["fixed"]):
                        sc = pg.evaluate(f"TAHOE_MAP.screen('nbr', {i})") if i != gi and not f else None
                        if sc and 40 < sc["x"] < sc["w"] - 40 and 40 < sc["y"] < sc["h"] - 40:
                            tgt = (i, box[0] + sc["x"], box[1] + sc["y"])
                            break
                    if tgt is None:
                        res[gap] = "no target"
                        continue
                    i, x, y = tgt
                    pg.mouse.move(x, y)
                    pg.mouse.down()
                    pg.mouse.up()
                    pg.wait_for_timeout(gap)
                    pg.mouse.down(click_count=2)
                    pg.mouse.up(click_count=2)
                    pg.wait_for_timeout(700)
                    s = pg.evaluate("TAHOE_MAP.sim('nbr')")
                    res[gap] = (sym[i], dict(zip(s["ids"], s["fixed"])).get(i),
                                sym[pg.evaluate("TAHOE_MAP.state().sel")])
                check(c, "ui#6: a double-click with a 300 / 450 ms gap pins the gene clicked first (flag 1); the "
                         "second click selects no other gene (300 ms: normally the selection is unchanged)",
                      all(isinstance(v, tuple) and v[1] == 1 and v[2] in (gname, v[0]) for v in res.values())
                      and not errs, {"gaps": res, "errors": errs})
                jit = {}
                for which in ("first", "second"):          # a micro-drag (5 px) in one click of the double-click
                    pg.evaluate(f"TAHOE_MAP.select({gi})")
                    pg.wait_for_timeout(100)
                    pg.wait_for_function(settled.replace("{t}", "nbr"), timeout=60000)
                    s = pg.evaluate("TAHOE_MAP.sim('nbr')")
                    box = pg.evaluate("(() => { const r = document.querySelector('#pane-nbr canvas')"
                                      ".getBoundingClientRect(); return [r.left, r.top]; })()")
                    cand = []
                    for i, f in zip(s["ids"], s["fixed"]):
                        sc = pg.evaluate(f"TAHOE_MAP.screen('nbr', {i})") if i != gi and not f else None
                        if sc and 60 < sc["x"] < sc["w"] - 60 and 60 < sc["y"] < sc["h"] - 60:
                            cand.append((i, box[0] + sc["x"], box[1] + sc["y"]))
                    A = cand[0] if cand else None
                    B = next((q for q in cand[1:] if abs(q[1] - A[1]) + abs(q[2] - A[2]) > 40), None) if A else None
                    if B is None:
                        jit[which] = "no targets"
                        continue
                    pg.mouse.move(A[1], A[2])                  # click gene A ...
                    pg.mouse.down()
                    pg.mouse.up()
                    pg.wait_for_timeout(250)                   # ... then double-click gene B, one click a micro-drag
                    pg.mouse.move(B[1], B[2])
                    pg.mouse.down()
                    if which == "first":
                        pg.mouse.move(B[1] + 5, B[2])
                    pg.mouse.up()
                    pg.mouse.down(click_count=2)
                    if which == "second":
                        pg.mouse.move(B[1] + 5, B[2])
                    pg.mouse.up(click_count=2)
                    pg.wait_for_timeout(700)
                    s = pg.evaluate("TAHOE_MAP.sim('nbr')")
                    fx = dict(zip(s["ids"], s["fixed"]))
                    jit[which] = (sym[A[0]], fx.get(A[0]), sym[B[0]], fx.get(B[0]))
                check(c, "ui#6: a double-click with a micro-drag (5 px) in its first or second click pins the gene "
                         "double-clicked, not the gene of an earlier click",
                      all(isinstance(v, tuple) and v[3] == 1 and not v[1] for v in jit.values()) and not errs,
                      {"micro-drag": jit, "errors": errs})
            finally:
                b.close()
    except Exception as e:  # noqa: BLE001  (no browser binary, sandbox ...)
        if "Executable doesn't exist" in str(e) or "playwright install" in str(e):
            check(c, "browser checks", True, "skipped: Playwright's Chromium is not installed")
            return
        raise


# ----------------------------------------------------------------------------- the review's content and its checks
# (verify.py, tools.py, dossier.py, the agent and skill files; findings science#0, #2, #4, #7, #8, #9, #10, sdk#6,
# ui#4 and the shared verification contract: check_status / shown_verdict / verification / note_footer)
class LitStub(F.FakeLiterature):
    """FakeLiterature with retraction cases and a DOI with parentheses: PMID 31000006 is a retraction NOTICE;
    DOI 10.1000/fake.31000007 is retracted per Crossref's update notices, 10.1000/fake.31000008 per Europe PMC's
    publication type; 'esummary_down' makes PubMed esummary fail."""
    PAREN_DOI = "10.1016/s0092-8674(00)81096-3"

    def __init__(self):
        super().__init__()
        self.papers["31000011"] = dict(self.papers["31000001"], doi=self.PAREN_DOI, title="Fake Cell paper")
        self.esummary_down = False

    def http_get(self, ctx, service, url, params, max_age_days=None, cache=True):
        from tahoemap.review import tools as TL
        if url == TL.ESUMMARY and self.esummary_down:
            raise TL.ToolError("ncbi: no answer after 5 attempts (HTTP 503)")
        body = super().http_get(ctx, service, url, params, max_age_days, cache)
        if url == TL.ESUMMARY:
            d = json.loads(body)
            if "31000006" in d["result"]:
                d["result"]["31000006"]["pubtype"] = ["Retraction of Publication"]
            return json.dumps(d)
        if url.startswith(TL.CROSSREF) and "fake.31000007" in url:
            return json.dumps({"status": "ok", "message": {"DOI": "10.1000/fake.31000007", "updated-by": [
                {"type": "retraction", "DOI": "10.1000/fake.notice", "source": "retraction-watch"}]}})
        if url == TL.EUROPEPMC and "fake.31000008" in str(params.get("query", "")):
            d = json.loads(body)
            for h in d["resultList"]["result"]:
                h["pubType"] = "retracted publication; research-article"
            return json.dumps(d)
        return body


def lit_ctx(work, lib=None, read=(), name="lit_ctx"):
    """A ToolContext with a fresh cache in work/name, answered by lib (installed: uninstall it when done)."""
    from tahoemap.review import tools as TL
    d = os.path.join(work, name)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    lib = (lib or LitStub()).install()
    ctx = TL.ToolContext(out=d, entity={"kind": "gene", "name": "NQO1", "entity_id": "gene:0"})
    ctx.read_ids |= {f"PMID:{p}" for p in read}
    return ctx, lib


def review_with(verdicts, pmids=("31000001",), note=None):
    """sample_review with these connection verdicts (dicts; relation / data_evidence filled in when absent)."""
    rv = F.sample_review("NQO1", pmids, note=note)
    rv["connection_verdicts"] = [dict({"relation": "both NRF2 targets", "data_evidence": "moves with: cos +0.60"},
                                      **v) for v in verdicts]
    return rv


@case
def checker_sees_relation(work):
    """science#0: the citation checker gets each verdict's relation, its direction and the data, against the
    rubric's strict meaning of 'established'; a 'supported' against the data's direction is stored as not
    supported."""
    from tahoemap.review import definitions as Df, tools as TL, verify as V
    c = "checker_sees_relation"
    vi = TL.SUBMIT_REVIEW["input_schema"]["properties"]["connection_verdicts"]["items"]
    ci = V.CHECK_TOOL["input_schema"]["properties"]["verdicts"]["items"]
    check(c, "schemas: a connection verdict carries relation and data_evidence; a check verdict its direction",
          {"relation", "data_evidence"} <= set(vi["required"]) and "direction" in ci["required"]
          and set(ci["properties"]["direction"]["enum"]) == set(V.DIRECTIONS), vi["required"])
    bad = review_with([{"partner": "HMOX1", "verdict": "established", "citations": ["PMID:31000001"],
                        "relation": " "}])
    _r, errs = TL.normalize_review(bad)
    check(c, "submit_review refuses a verdict without its relation", any("relation" in e for e in errs), errs)
    rv = review_with([{"partner": "HMOX1", "verdict": "established", "citations": ["PMID:31000001"],
                       "relation": "both induced by NRF2 (co-induction)",
                       "data_evidence": "moves opposite: cos -0.37, both halves"}])
    ctx, lib = lit_ctx(work, read=("31000001",))
    try:
        r, _e = TL.normalize_review(rv)
        r, _rep = V.check_ids(r, ctx)
        prompt = V.build_check_prompt(r, V.fetch_abstracts(r, ctx), {"name": "NQO1"})
    finally:
        lib.uninstall()
    vblock = prompt.split("[V1]", 1)[1].split("\n[", 1)[0] if "[V1]" in prompt else ""
    check(c, "the V claim shows the relation, the data with its direction, and the strict meaning",
          "both induced by NRF2" in vblock and "data: moves opposite: cos -0.37" in vblock
          and "same pathway or complex alone is not enough" in vblock and "opposite direction" in prompt,
          vblock[:300])
    check(c, "E claims show their data line too", "data: cos 0.71" in prompt.split("[E1]", 1)[-1][:300])
    chk = {"summary": "s", "verdicts": [
        {"claim_id": "E1", "verdict": "supported", "direction": V.SAME, "reason": "PMID:31000001 says so"},
        {"claim_id": "M1", "verdict": "partly", "direction": "not applicable", "reason": "weaker"},
        {"claim_id": "V1", "verdict": "supported", "direction": V.OPPOSITE, "reason": "co-induced by NRF2"}]}
    r2, summ = V.apply_check(r, chk)
    v1, e1, m1 = r2["connection_verdicts"][0], r2["established"][0], r2["missing"][0]
    check(c, "'supported' against the data's direction is stored as not supported -> shown 'unverified'",
          v1["check"]["verdict"] == "not supported" and v1["check_status"] == "not_supported"
          and v1["shown_verdict"] == "unverified" and e1["check_status"] == "supported"
          and m1["check_status"] == "partly" and summ.get("not_supported") == 1,
          {k: v1.get(k) for k in ("check", "check_status", "shown_verdict")})
    chk2 = {"summary": "s", "verdicts": [
        {"claim_id": "E1", "verdict": "partly", "direction": V.OPPOSITE, "reason": "lowered, not raised"},
        {"claim_id": "M1", "verdict": "partly", "direction": "not applicable", "reason": "weaker"},
        {"claim_id": "V1", "verdict": "partly", "direction": "not stated", "reason": "no direction given"}]}
    r3, _s3 = V.apply_check(r, chk2)
    e1b, v1b = r3["established"][0], r3["connection_verdicts"][0]
    check(c, "'partly' against the data's direction is not supported too; 'partly' without a direction stays",
          e1b["check"]["verdict"] == "not supported" and "checker's verdict: partly" in e1b["check"]["reason"]
          and e1b["shown_verdict"] == "unverified" and v1b["check_status"] == "partly"
          and v1b["shown_verdict"] == "established", [e1b["check"], v1b["check"]])
    md = Df.load_agent("citation-checker").system
    check(c, "citation-checker.md: the data line, the direction field and the strict 'established'",
          "`data:`" in md and "`direction`" in md and "complex alone is **not** enough" in md
          and "shown next to each claim in the vault" not in md)


@case
def indirect_needs_citations(work):
    """science#4: 'indirect' needs a citation per gene (two papers), or one review naming both."""
    from tahoemap.review import tools as TL
    c = "indirect_needs_citations"
    ctx, lib = lit_ctx(work, read=("31000001", "31000002", "31000009"))
    try:
        def errs(cits):
            rv = review_with([{"partner": "PIR", "verdict": "indirect", "citations": list(cits)}])
            return [e for e in TL.normalize_review(rv, ctx)[1] if "indirect" in e]
        e0, e1, e2 = errs([]), errs(["PMID:31000001"]), errs(["PMID:31000001", "PMID:31000002"])
        TL.cache_put(ctx, "ncbi_record", "31000009", {"record": {"pmid": "31000009", "pubtypes": [
            "Journal Article", "Review"], "title": "A review naming both"}})
        er = errs(["PMID:31000009"])
        try:
            TL.submit_review(ctx, review_with([{"partner": "PIR", "verdict": "indirect", "citations": []}]))
            refused = False
        except TL.ToolError as e:
            refused = "indirect" in str(e)
    finally:
        lib.uninstall()
    check(c, "no citation or one primary paper: refused; two papers, or one review: accepted",
          e0 and e1 and not e2 and not er and refused, {"none": e0[:1], "one": e1[:1], "two": e2, "review": er})


@case
def doi_parentheses(work):
    """science#7: a DOI with parentheses is read whole (citation lists, bare and linked in the note), linked
    percent-encoded, trailing punctuation dropped; a real one is kept, a made-up one removed whole."""
    from tahoemap.review import tools as TL, verify as V
    c = "doi_parentheses"
    raw = "10.1016/S0092-8674(00)81096-3"
    want = "DOI:" + LitStub.PAREN_DOI
    linked = TL.link_citations(f"Shown before (DOI:{raw}). Also DOI:{raw}.")
    enc = "https://doi.org/10.1016/s0092-8674%2800%2981096-3"
    ids = TL.note_ids(linked + f" [x](https://doi.org/{raw})")
    check(c, "norm_citation, link_citations and note_ids read the whole DOI",
          TL.norm_citation(f"DOI:{raw}.") == want and TL.norm_citation(f"https://doi.org/{raw}") == want
          and TL.norm_citation("https://doi.org/10.1016/S0092-8674%2800%2981096-3") == want
          and linked.count(f"]({enc})") == 2 and f"]({enc})). Also" in linked and linked.endswith(f"]({enc}).")
          and {x[0] for x in ids} == {want} and len(ids) == 5, f"{linked} | {ids}")
    fake = "10.1016/S0092-8674(99)99999-9"
    note = f"Known ([DOI:{raw}](https://doi.org/{raw})); made up ([DOI:{fake}](https://doi.org/{fake})).\n"
    rv = F.sample_review("NQO1", ("31000001",), note=note)
    rv["established"][0]["citations"] += [f"DOI:{raw}", f"DOI:{fake}"]
    ctx, lib = lit_ctx(work, read=("31000001",))
    try:
        r, _e = TL.normalize_review(rv)
        r2, rep = V.check_ids(r, ctx)
    finally:
        lib.uninstall()
    nt = r2["note_markdown"]
    check(c, "the real DOI found and kept; the made-up one removed whole, no fragment left in the note",
          rep["missing"] == ["DOI:" + fake.lower()] and want in r2["established"][0]["citations"]
          and f"DOI:{fake.lower()} (citation removed: not found in Crossref or Europe PMC)" in nt
          and "99999-9)" not in nt.replace(f"DOI:{fake.lower()} (", "") and f"https://doi.org/{raw})" in nt,
          {"missing": rep["missing"], "note": nt})
    sici = "10.1002/(SICI)1097-4636(199905)45:2<123::AID-JBM1>3.0.CO;2-X"
    bad = ['DOI:10.1234/x"><img/src=x/onerror=alert(1)>', "DOI:10.1000/x%22onload%3D", "DOI:10.1000/a b"]
    rv = F.sample_review("NQO1", ("31000001",))
    rv["established"][0]["citations"] = ["PMID:31000001", bad[0]]
    _r, errs = TL.normalize_review(rv)
    check(c, "a citation that is no DOI (quotes, markup, spaces) is refused; an old SICI DOI is read whole",
          all(TL.norm_citation(b) is None for b in bad) and TL.norm_citation("DOI:" + sici) == "DOI:" + sici.lower()
          and any("is not a PMID or DOI" in e for e in errs), errs)


@case
def retractions(work):
    """science#8: retracted papers marked per item, DOIs checked too (Crossref update notices, Europe PMC type), and
    a retraction notice is not itself 'retracted'."""
    from tahoemap.review import tools as TL, verify as V
    c = "retractions"
    rv = review_with([{"partner": "HMOX1", "verdict": "established", "citations": ["DOI:10.1000/fake.31000007"]},
                      {"partner": "PIR", "verdict": "indirect", "citations": ["DOI:10.1000/fake.31000008",
                                                                               "PMID:31000001"]},
                      {"partner": "GCLM", "verdict": "established", "citations": ["PMID:31000002"]}],
                     pmids=("31000005", "31000006"))
    ctx, lib = lit_ctx(work, read=("31000001", "31000002", "31000005", "31000006"))
    try:
        r, errs = TL.normalize_review(rv)
        r2, rep = V.check_ids(r, ctx)
        ab = V.fetch_abstracts(r2, ctx)
        summ = TL._summary_line(TL.esummary_records(ctx, ["31000006"])["31000006"])
    finally:
        lib.uninstall()
    est, cv = r2["established"][0], r2["connection_verdicts"]
    check(c, "retracted: the PMID and both DOIs (Crossref 'updated-by', Europe PMC type); the notice is not",
          not errs and sorted(rep["retracted_ids"]) == ["DOI:10.1000/fake.31000007", "DOI:10.1000/fake.31000008",
                                                        "PMID:31000005"]
          and rep["retraction_notices"] == ["PMID:31000006"] and rep["retracted"] == 3,
          {k: rep.get(k) for k in ("retracted", "retracted_ids", "retraction_notices")})
    check(c, "per-item markers: retracted_citations / retraction_notices; the verdict still shown, with the marker",
          est.get("retracted_citations") == ["PMID:31000005"] and est.get("retraction_notices") == ["PMID:31000006"]
          and cv[0].get("retracted_citations") == ["DOI:10.1000/fake.31000007"]
          and cv[1].get("retracted_citations") == ["DOI:10.1000/fake.31000008"]
          and not cv[2].get("retracted_citations") and cv[0]["shown_verdict"] == "established",
          [(v["partner"], v.get("retracted_citations"), v.get("shown_verdict")) for v in cv])
    check(c, "the checker's abstracts mark the retracted DOI; PubMed search lines tell a notice from a retraction",
          "[RETRACTED" in (ab.get("DOI:10.1000/fake.31000007") or "")
          and "[RETRACTED" in (ab.get("PMID:31000005") or "") and "RETRACTION NOTICE" in summ
          and "RETRACTED:" not in summ, summ)
    p = V.build_check_prompt(r2, dict(ab, **{"DOI:10.1000/fake.31000007": None, "PMID:31000006": None}))
    check(c, "a retracted paper (or a notice) without an abstract is still marked in the checker's prompt",
          "=== DOI:10.1000/fake.31000007 ===  [RETRACTED" in p and "=== PMID:31000006 ===  [RETRACTION NOTICE" in p,
          [x for x in p.splitlines() if x.startswith("=== ")])


@case
def retractions_shown(work, src, ents):
    """science#8 (what readers see): a retracted paper that a verdict cites is shown wherever the verdict is - the
    review tables ('retracted' beside 'citations' in connections / findings; '' for a review stored before
    retractions were recorded), the vault's Literature column and verdict list ('(cites a retracted paper)', the
    paper marked '(retracted)') and the map's badge and tooltip. A verdict whose only papers are retracted reads
    'unverified', never 'established', and is not the verdict picked for its partner (vault and map alike). A table
    written before it had the column is not used (the JSONs are read), and outputs drawn before are out of date."""
    from tahoemap import html_map, vault as VT
    c = "retractions_shown"
    # -- the rules, without a run
    only = {"verdict": "established", "citations": "PMID:31000005", "retracted": "PMID:31000005",
            "check_status": "supported", "shown_verdict": "established"}
    some = {"verdict": "indirect", "citations": "PMID:31000005;PMID:31000001", "retracted": "PMID:31000005",
            "check_status": "not_checkable", "shown_verdict": "indirect"}
    item = {"verdict": "established", "citations": ["PMID:31000005"], "retracted_citations": ["PMID:31000005"],
            "check_status": "not_checkable", "shown_verdict": "established"}
    older = {"verdict": "established", "citations": "PMID:31000005", "check_status": "not_checkable",
             "shown_verdict": "established"}                       # a table or review from before retractions
    st = [VT.lit_status(x) for x in (only, some, item, older)]
    check(c, "a verdict whose only papers are retracted is shown 'unverified' (table row or review item); one that "
             "also cites another paper keeps its verdict; no record of retractions = none",
          st == [("supported", "unverified"), ("not_checkable", "indirect"), ("not_checkable", "unverified"),
                 ("not_checkable", "established")], st)
    lab = [VT.verdict_label(dict(x, check_status=s[0], shown_verdict=s[1]))
           for x, s in zip((only, some, older), (st[0], st[1], st[3]))]
    check(c, "verdict_label (the vault's cell, the map's badge and tooltip): '(cites a retracted paper)' and the "
             "paper named; the retracted-only verdict reads 'unverified (cites a retracted paper)'",
          lab[0][0] == "unverified (cites a retracted paper)"
          and "it cites a retracted paper (PMID:31000005) and nothing else" in lab[0][1]
          and lab[1][0] == "indirect (not checked) (cites a retracted paper)"
          and "it cites a retracted paper (PMID:31000005), which is no support" in lab[1][1]
          and lab[2][0] == "established (not checked)" and "retracted" not in lab[2][1], lab)
    pv = VT.pick_verdict
    picked = [pv([dict(only), {"verdict": "plausible", "citations": "PMID:31000002", "check_status": "not_checkable"}]
                 )["verdict"],
              pv([dict(some, verdict="established", check_status="supported"),
                  {"verdict": "established", "citations": "PMID:31000003", "check_status": "supported"}])["citations"]]
    check(c, "pick_verdict: a verdict resting only on retracted papers is not a verified one; between equal verdicts "
             "and checks, the one that cites no retracted paper",
          picked == ["plausible", "PMID:31000003"], picked)
    # -- a run: verdicts citing the fake library's retracted PMID 31000005, through the fake API
    sv = own_view(work, src, "retracted_view")
    g, g2 = ents["genes"][1], ents["genes"][2]
    rel = pd.read_parquet(os.path.join(src, "relations", "gene_relations.parquet"), columns=["col_a", "col_b", "rank"])
    genes = pd.read_parquet(os.path.join(src, "tables", "genes.parquet"), columns=["col", "label"]).set_index("col")
    pcols = [int(x) for x in rel[rel["col_a"] == g["col"]].sort_values("rank")["col_b"].head(4)]
    P = [str(genes.at[x, "label"]) for x in pcols]
    cv = [{"partner": P[0], "verdict": "established", "citations": ["PMID:31000005"]},                 # only retracted
          {"partner": P[1], "verdict": "indirect", "citations": ["PMID:31000005", "PMID:31000001"]},   # one of two
          {"partner": P[2], "verdict": "established", "citations": ["PMID:31000005"]},                 # two on P[2]:
          {"partner": P[2], "verdict": "plausible", "citations": ["PMID:31000002"]},                   # ... this one
          {"partner": P[3], "verdict": "established", "citations": ["PMID:31000003"]}]                 # none
    rv = F.sample_review(P[3], ("31000003",))
    rv["connection_verdicts"] = [dict({"relation": "both NRF2 targets", "data_evidence": "moves with: cos +0.60"}, **v)
                                 for v in cv]
    steps = [{"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001", "31000002", "31000003",
                                                                            "31000005"]}}]},
             {"submit_review": rv}]
    res, _fk = run(sv, {"entities": {g["entity_id"]: steps}}, only=g["entity_id"], verify="ids")
    rd = os.path.join(sv, "review", "reviews", "gene")
    rj = os.path.join(rd, os.listdir(rd)[0])
    js = json.load(open(rj, encoding="utf-8"))
    # a review stored before retractions were recorded: the same review on another gene, without the lists
    old = json.loads(json.dumps(js))
    old["meta"].update(entity_id=g2["entity_id"], name=g2["name"])
    for sec in ("established", "missing", "contradicted", "unexpected", "connection_verdicts"):
        for it in old.get(sec) or []:
            it.pop("retracted_citations", None)
            it.pop("retraction_notices", None)
    with open(os.path.join(rd, "old-format.json"), "w", encoding="utf-8") as fh:
        json.dump(old, fh)
    R.build_tables(sv)
    conn = pd.read_parquet(os.path.join(sv, "review", "connections.parquet"))
    find = pd.read_parquet(os.path.join(sv, "review", "findings.parquet"))
    new_c, old_c = conn[conn["entity_id"] == g["entity_id"]], conn[conn["entity_id"] == g2["entity_id"]]
    check(c, "the stored review lists the retracted paper on each verdict citing it",
          res.counts == {"done": 1} and [v.get("retracted_citations") or [] for v in js["connection_verdicts"]] ==
          [["PMID:31000005"], ["PMID:31000005"], ["PMID:31000005"], [], []],
          [(v["partner"], v.get("retracted_citations")) for v in js["connection_verdicts"]])
    check(c, "connections / findings carry 'retracted' in the form of 'citations'; '' for an older review JSON",
          list(conn.columns) == R.CONN_COLS and list(find.columns) == R.FIND_COLS
          and list(new_c["retracted"]) == ["PMID:31000005"] * 3 + ["", ""]
          and len(old_c) == 5 and set(old_c["retracted"]) == {""}
          and set(find["retracted"]) == {""} and find["retracted"].map(type).eq(str).all(),
          {"new": list(new_c["retracted"]), "old": list(old_c["retracted"])})
    with contextlib.redirect_stdout(io.StringIO()):
        VT.run(sv)
        html_map.run(sv)
    gpath = next(os.path.join(dp, f) for dp, _d, fns in os.walk(os.path.join(sv, "vault")) for f in fns
                 if f == g["name"] + ".md")
    gt = open(gpath, encoding="utf-8").read()
    rows = {}
    for head in ("## Genes that move with it", "## Genes that move opposite"):
        tab = gt.split(head, 1)[1].split("\n## ", 1)[0] if head in gt else ""
        for line in tab.splitlines() if "| Literature |" in tab else []:
            m = re.match(r"^\| \[\[([^\]|]+)\]\] \|.*\| ([^|]*) \|$", line)
            if m:
                rows[m.group(1)] = m.group(2).strip()
    vline = next((x for x in lit_section(gt).splitlines() if x.startswith("**Connection verdicts**")), "")
    link5 = "[PMID:31000005](https://pubmed.ncbi.nlm.nih.gov/31000005/) (retracted)"
    check(c, "the vault's Literature column: '(cites a retracted paper)', the paper marked '(retracted)'; the verdict "
             "resting only on it reads 'unverified', and P2 shows its other verdict; no marker without a retraction",
          rows.get(P[0], "").startswith("unverified (cites a retracted paper) (agent: established; only retracted "
                                        "papers cited) · " + link5)
          and rows.get(P[1], "").startswith("indirect (not checked) (cites a retracted paper) · " + link5 +
                                            " [PMID:31000001]")
          and rows.get(P[2], "").startswith("plausible (not checked) (of 2 verdicts it gave) · [PMID:31000002]")
          and rows.get(P[3], "").startswith("established (not checked) · [PMID:31000003]")
          and "retracted" not in rows.get(P[2], "") + rows.get(P[3], ""), {p: rows.get(p) for p in P})
    check(c, "the note's verdict list says it too, and never shows the retracted-only verdict as established",
          f"[[{P[0]}]] unverified (cites a retracted paper)" in vline and f"[[{P[0]}]] established" not in vline
          and f"[[{P[1]}]] indirect (not checked) (cites a retracted paper)" in vline
          and "(cites a retracted paper) = a paper it cites is retracted" in gt, vline[:400])
    trip, ent, n = map_lit(sv)
    a = ent.get(int(g["col"]))
    mp = {P[i]: trip.get((a, ent.get(pcols[i]))) for i in range(4) if ent.get(pcols[i], n) < n}
    same = all(mp[p] is None or mp[p][0] == rows.get(p, "").split(" · ")[0].split(" (agent:")[0]
               .replace(" (of 2 verdicts it gave)", "") for p in mp)
    check(c, "the map's badge and tooltip show the same marker; the retracted-only verdict is 'unverified' there "
             "too; the same labels and the same pick as the vault",
          a is not None and len(mp) == 4 and same
          and mp[P[0]][0] == "unverified (cites a retracted paper)" and mp[P[0]][2] == "unverified"
          and "cites a retracted paper (PMID:31000005)" in mp[P[0]][1]
          and mp[P[1]][0] == "indirect (not checked) (cites a retracted paper)"
          and "cites a retracted paper (PMID:31000005)" in mp[P[1]][1]
          and mp[P[2]][0] == "plausible (not checked)" and mp[P[3]][0] == "established (not checked)"
          and "retracted paper" in open(os.path.join(sv, "map", "gene_map.html"), encoding="utf-8").read(),
          {p: v[:3] if v else None for p, v in mp.items()})
    # -- a connections.parquet written before the column: not used, the JSONs are read
    p = os.path.join(sv, "review", "connections.parquet")
    conn.drop(columns=["retracted"]).to_parquet(p, index=False)
    with contextlib.redirect_stdout(io.StringIO()) as buf:
        rows_old = VT.review_connections(sv, one_per_partner=False)
    check(c, "a connections.parquet without the 'retracted' column is not used: the verdicts and their retracted "
             "papers come from the review JSONs",
          not VT.connections_stale(sv) and "written before it recorded retracted papers" in buf.getvalue()
          and [(r["retracted"], r["shown_verdict"]) for r in rows_old if r["entity_id"] == g["entity_id"]][:2]
          == [("PMID:31000005", "unverified"), ("PMID:31000005", "indirect")], buf.getvalue()[-300:])
    fp = VT.review_fingerprint(sv)
    VT.LIT_RENDER -= 1
    try:
        fp_before = VT.review_fingerprint(sv)
    finally:
        VT.LIT_RENDER += 1
    check(c, "the render version is part of the vault and map stamps: outputs drawn before this change are out of "
             "date", fp and fp_before and fp["sha"] != fp_before["sha"] and VT.LIT_RENDER >= 3, (fp, fp_before))
    bad = scan_for_keys(os.path.join(sv, "review"))
    check(c, "no API key in any file written", not bad, bad[:5])
    shutil.rmtree(sv, ignore_errors=True)


def dataview_queries(md):
    """Where md could hold a Dataview inline query: an '=' or '$=' reached from a backtick or from the start of a line
    through nothing but whitespace (JavaScript's trim: Unicode spaces, line breaks, BOM) and container markers - a
    superset of the code spans and code blocks whose trimmed text starts with '=' (Dataview's own test)."""
    return re.findall(r"(?:`|^)(?:[\s\ufeff>]|[-+*](?=[ \t])|\d{1,9}[.)](?=[ \t]))*\$?=.{0,20}", md, re.M)


R5_NOTE = """## What the literature says

**In short.** [[{g}]] moves with [[{p}]] ([PMID:31000003](https://pubmed.ncbi.nlm.nih.gov/31000003/)).
<[img](x) src=x onerror=alert('r5')> <\\url autofocus onfocus=alert('r5u') tabindex=0> <[style](x)>body{{display:none}}
Click [here][r5] and [there][^r5 x]; write to attacker@evil.example or <mailto:a@evil.example>, see //evil.example/x.

[[r5](x)]: javascript:alert('r5ref')
[^r5 x]: javascript:alert('r5fn')

Inline `
= this.file.name` and a block:

```text
$= dv.paragraph("r5")
```
"""


def sanitize_round5(c, VT):
    """Round 5 (display checkers): what a removal or an un-escape puts back together is neutralised too (a tag, an
    autolink, a definition: '<[img](x) src=x onerror=...>', '<\\url ...>', '[[r](x)]: javascript:...'); a '^' label
    that is no footnote's is a definition like any other; no Dataview inline query (a space, line break, NBSP or other
    Unicode space before the '=', a fenced or indented code block); no linear-time-breaking run of unclosed '<!--',
    '<?' or '<script>'; no e-mail address, 'mailto:' or '//host' an autolinker would link. (Checked while fixing with
    commonmark.js 0.31, marked 18 (GFM) and markdown-it 15 (linkify, footnotes) over 6,558 generated cases: no tag, no
    event handler, no link but to the allowed sites, no Dataview query, no generated section swallowed.)"""
    sn = VT.sanitize_note
    made = {x: sn(x) for x in (
        "<[img](x) src=x onerror=alert(1)>", "![<](x)img src=x onerror=alert(1)>",
        "<\\url autofocus onfocus=alert(1) tabindex=0>", "<[img](x) src=https&#58;//evil.example/pixel.png>",
        "<[style](x)>body{display:none}", "<[javascript:alert(1)](x)>", "<\\\\url onfocus=alert(1)>",
        "<[1](x)@evil.example>", "Click [here][r]\n\n[[r](x)]: javascript:alert(1)")}
    check(c, "round 5: a tag, an autolink or a definition that a removed link / image or an un-escaped '\\url' puts "
             "together is text ('<' escaped at the end, links removed before definitions)",
          made["<[img](x) src=x onerror=alert(1)>"] == "&lt;img src=x onerror=alert(1)>"
          and not any(re.search(r"<[A-Za-z/!?]|\]: *javascript|\[r\]:|[^\u200b]@evil", v) for v in made.values()),
          made)
    caret = {x: sn(x) for x in ("Click [x][^r x]\n\n[^r x]: javascript:alert(1)",
                                "Click [x][^a\\]b]\n\n[^a\\]b]: javascript:alert(1)", "[^r x]: https://evil.example/",
                                "Click [x][r]\n\n[r]: \u00a0javascript:alert(1)", "t[^1]\n\n[^1]: javascript:alert(1)")}
    vals = list(caret.values())
    check(c, "round 5: a '^' label that is no footnote's ('[^r x]:', '[^a\\]b]:') and a destination after a NBSP are "
             "definitions, removed; a footnote's first word still defanged",
          not any("javascript" in v or "evil" in v for v in vals[:4]) and "[^1]: \u200bjavascript" in vals[4], caret)
    dv = {x: sn(x) for x in ("x ``\t\n$= dv.el(1)``", "`\u3000$= dv.paragraph(1)`", "```text\n$= dv.paragraph(1)\n```",
                             "text `\n= this.file.name`", "`\u00a0= this.file.name`", "`\u2003= this.file.name`",
                             "```\n= elink(\"https://evil.example/\", \"PubMed record\")\n```",
                             "Para.\n\n    = this.file.name", "> text `\n> = this.file.name`", "\\``= x`",
                             "~~~\n\u00a0\n\n  $= dv.el(1)\n~~~", "- a\n\n      = this.file.name")}
    check(c, "round 5: no Dataview inline query: a zero-width space before the '=' of a code span (after any space "
             "or line break), of a code block's first line (fenced or indented, in a container too)",
          not any(dataview_queries(v) for v in dv.values())
          and dv["```text\n$= dv.paragraph(1)\n```"] == "```text\n\u200b$= dv.paragraph(1)\n```",
          {k: v for k, v in dv.items() if dataview_queries(v)} or dv)
    t0 = time.time()
    for x in ("<!--" * 40000, "<?" * 80000, "<script>" * 20000, "<script " * 20000 + ">", "<style>" * 20000 + "x",
              "`" * 50000 + " " * 50000, " " * 100000 + "x", "> " * 50000 + "x"):
        sn(x)
    check(c, "round 5: linear time on runs of unclosed '<!--', '<?', '<script>' (each was quadratic: ~35-65 s)",
          time.time() - t0 < 3, f"{time.time() - t0:.2f} s")
    em = {x: sn(x) for x in ("<mailto:a@evil.example>", "write to attacker@evil.example now", "see //evil.example/x",
                             "https\uff1a//evil.example", "/\\/evil.example", "a&#64;evil.example",
                             "https:&#47;&#47;evil.example/x", "https://evil.example/u@evil.example",
                             "https://pubmed.ncbi.nlm.nih.gov/1/")}
    check(c, "round 5: no e-mail address (a zero-width space before its '@', also after an entity or escape), no "
             "'mailto:', no '//host' (linkify-it) can be autolinked; an allowed bare URL stays whole",
          not any(re.search(r"(?<!\u200b)@|mailto:|(?<!\u200b)//", v) for v in list(em.values())[:-1])
          and em["https://pubmed.ncbi.nlm.nih.gov/1/"] == "https://pubmed.ncbi.nlm.nih.gov/1/", em)


@case
def vault_round5(work, src, ents):
    """Round 5 (display and e2e checkers) through a run: a crafted note (sanitize_round5's attacks) and verdicts -
    one citing only a retracted paper, one the checker grades not supported, one citing an unread, made-up PMID -
    reviewed through the fake API (--verify llm); an older review JSON of the same gene with another verdict on a
    partner, and a gene whose latest review gave no verdict; a gene reviewed while the PubMed id look-up was down
    (the checker graded its claims all the same). Then the vault and the map: the note sanitised; the vault and the
    map show the latest review's verdicts alike; the callout counts every verdict shown 'unverified' (the retracted
    one too), does not flag papers the id check removed as unread, and does not call claims 'ids not checked' that
    show the checker's verdict."""
    from tahoemap import html_map, vault as VT
    from tahoemap.review import tools as TL
    c = "vault_round5"
    sanitize_round5(c, VT)
    # -- the callout, without a run
    vt = VT.Vault._verification_text
    base = {"mode": "llm", "counts": {"n_citations": 3, "status_not_supported": 1, "status_citations_removed": 0},
            "llm": {"status": "done", "detail": "", "supported": 1, "partly": 0, "not_supported": 1,
                    "not_checkable": 0}}
    items = {"connection_verdicts": [
        {"verdict": "established", "citations": ["PMID:5"], "retracted_citations": ["PMID:5"],
         "unchecked_citations": [], "check_status": "supported", "shown_verdict": "established"},
        {"verdict": "indirect", "citations": ["PMID:7"], "unchecked_citations": ["PMID:7"],
         "check_status": "unchecked", "shown_verdict": "indirect"}],
        "established": [{"citations": ["PMID:2"], "unchecked_citations": ["PMID:2"], "check_status": "not_supported",
                         "check": {"verdict": "not supported"}, "shown_verdict": "unverified"}]}
    ids = {"status": "done", "checked": 1, "removed": 0, "unchecked": 2, "retracted": 1, "found": 1,
           "not_retrieved_in_session": []}
    t_items = vt(dict(base, ids=ids), {"not_retrieved": ["PMID:9"]}, items)
    t_old = vt(dict(base, ids={k: v for k, v in ids.items() if k != "not_retrieved_in_session"} | {"missing":
                                                                                                    ["PMID:9"]}),
               {"not_retrieved": ["PMID:9", "PMID:8"]})
    check(c, "the callout counts what is shown 'unverified' by the labels' rule (a retracted-only verdict too), tells "
             "claims marked 'ids not checked' from those the checker graded, and flags as unread only what the id "
             "check left cited",
          '1 connection verdict and 1 other claim shown as "unverified"' in t_items
          and '1 claim citing them is marked "ids not checked", 1 was graded by the citation checker all the same'
          in t_items and "without having been read" not in t_items
          and "1 paper cited without having been read" in t_old and '1 shown as "unverified"' in t_old,
          [t_items, t_old])
    # -- run 1: the crafted review
    sv = own_view(work, src, "r5_view")
    G = ents["genes"]
    g, g2, g3 = G[3], G[4], G[5]
    rel = pd.read_parquet(os.path.join(src, "relations", "gene_relations.parquet"), columns=["col_a", "col_b", "rank"])
    genes = pd.read_parquet(os.path.join(src, "tables", "genes.parquet"), columns=["col", "label"]).set_index("col")
    pcols = [int(x) for x in rel[rel["col_a"] == g["col"]].sort_values("rank")["col_b"].head(5)]
    P = [str(genes.at[x, "label"]) for x in pcols]
    cv = [{"partner": P[0], "verdict": "established", "citations": ["PMID:31000005"]},     # only retracted
          {"partner": P[1], "verdict": "established", "citations": ["PMID:31000002"]},     # checker: not supported
          {"partner": P[2], "verdict": "established", "citations": ["PMID:39999999"]},     # unread, made up: removed
          {"partner": P[3], "verdict": "plausible", "citations": ["PMID:31000003"]}]       # supported
    rv = F.sample_review(P[3], ("31000003",), note=R5_NOTE.format(g=g["name"], p=P[3]))
    rv["connection_verdicts"] = [dict({"relation": "both NRF2 targets", "data_evidence": "moves with: cos +0.60"}, **v)
                                 for v in cv]
    steps = [{"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000002", "31000003", "31000005"]}}]},
             {"submit_review": rv}, {"submit_review": rv}]          # the first is refused: 39999999 was never read
    chk = {"summary": "s", "verdicts": [
        {"claim_id": x, "verdict": "not supported" if x == "V2" else "supported", "direction": "same as the data",
         "reason": "r"} for x in ("E1", "M1", "V1", "V2", "V4")]}
    res, _fk = run(sv, {"entities": {g["entity_id"]: steps}, "checker": [{"submit_check": chk}]},
                   only=g["entity_id"], verify="llm")
    rd = os.path.join(sv, "review", "reviews", "gene")
    rj = os.path.join(rd, os.listdir(rd)[0])
    js = json.load(open(rj, encoding="utf-8"))
    vids = (js.get("verification") or {}).get("ids") or {}
    # -- run 2: the PubMed id look-up down; the checker reads the abstracts and grades every claim all the same
    orig = TL.esummary_records

    def down(ctx, pmids):
        raise TL.ToolError("ncbi: no answer after 5 attempts (HTTP 503)")
    rv3 = F.sample_review(P[0], ("31000001",))
    chk3 = {"summary": "s", "verdicts": [{"claim_id": x, "verdict": "supported", "direction": "same as the data",
                                          "reason": "r"} for x in ("E1", "M1", "V1")]}
    TL.esummary_records = down
    try:
        res3, _fk = run(sv, {"entities": {g3["entity_id"]: [
            {"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001"]}}]}, {"submit_review": rv3}]},
            "checker": [{"submit_check": chk3}]}, only=g3["entity_id"], verify="llm")
    finally:
        TL.esummary_records = orig
    js3 = next((json.load(open(os.path.join(rd, f), encoding="utf-8")) for f in os.listdir(rd)
                if f != os.path.basename(rj)), {})
    check(c, "the runs: retracted-only, not supported and removed verdicts stored; the unread made-up PMID removed "
             "(so not left 'not retrieved'); with the id look-up down the checker still graded the claims",
          res.counts == {"done": 1} and res3.counts == {"done": 1}
          and [v.get("check_status") for v in js["connection_verdicts"]] == ["supported", "not_supported",
                                                                             "citations_removed", "supported"]
          and "PMID:39999999" in (js["meta"].get("not_retrieved") or []) and vids.get("not_retrieved_in_session") == []
          and ((js3.get("verification") or {}).get("ids") or {}).get("unchecked") == 1
          and [v.get("check_status") for v in js3.get("connection_verdicts") or []][:1] == ["supported"],
          {"g": [(v["partner"], v.get("check_status")) for v in js["connection_verdicts"]], "ids": vids,
           "meta_nr": js["meta"].get("not_retrieved"), "g3": (js3.get("verification") or {}).get("ids")})
    # -- an older review of g (another verdict on P3, one on P4), and g2: an older review with verdicts, the latest
    # with none
    old = json.loads(json.dumps(js))
    old["meta"].update(run_id="20250101-000000-old", reviewed="2025-01-01T00:00:00Z")
    old["connection_verdicts"][3].update(verdict="established", citations=["PMID:31000001"], check_status="supported",
                                         shown_verdict="established", check={"verdict": "supported"})
    old["connection_verdicts"].append(dict(old["connection_verdicts"][3], partner=P[4]))
    two = [json.loads(json.dumps(old)), json.loads(json.dumps(js))]
    for x, (run_id, when) in zip(two, (("20250101-000000-old", "2025-01-01T00:00:00Z"),
                                       ("20260101-000000-new", "2026-01-01T00:00:00Z"))):
        x["meta"].update(entity_id=g2["entity_id"], name=g2["name"], run_id=run_id, reviewed=when)
    two[1]["connection_verdicts"] = []
    p2 = [str(genes.at[int(x), "label"]) for x in rel[rel["col_a"] == g2["col"]].sort_values("rank")["col_b"].head(4)]
    for v, p in zip(two[0]["connection_verdicts"], p2):        # on g2's own partners: pairs the map's panel lists
        v["partner"] = p
    for name, x in (("AAA_older_copy.json", old), ("AAB_g2_old.json", two[0]), ("AAC_g2_new.json", two[1])):
        with open(os.path.join(rd, name), "w", encoding="utf-8") as fh:
            json.dump(x, fh)
    R.build_tables(sv)
    conn = pd.read_parquet(os.path.join(sv, "review", "connections.parquet"))
    by_table = sorted((r["entity_id"], r["partner"], r["shown_verdict"]) for r in VT.review_connections(sv))
    os.replace(os.path.join(sv, "review", "connections.parquet"), os.path.join(sv, "review", "c.parquet"))
    by_json = sorted((r["entity_id"], r["partner"], r["shown_verdict"]) for r in VT.review_connections(sv))
    os.replace(os.path.join(sv, "review", "c.parquet"), os.path.join(sv, "review", "connections.parquet"))
    mine = {p: v for e, p, v in by_table if e == g["entity_id"]}
    check(c, "review_connections: only each entity's latest review (from the table and from the JSONs alike): P3's "
             "current verdict, nothing of the older review's P4, nothing of g2's older review",
          len(conn[conn["entity_id"] == g["entity_id"]]) == 9 and by_table == by_json
          and mine.get(P[3]) == "plausible" and P[4] not in mine
          and not any(e == g2["entity_id"] for e, _p, _v in by_table), by_table)
    with contextlib.redirect_stdout(io.StringIO()):
        VT.run(sv)
        html_map.run(sv)

    def note(gene):
        return open(next(os.path.join(dp, f) for dp, _d, fns in os.walk(os.path.join(sv, "vault")) for f in fns
                         if f == gene["name"] + ".md"), encoding="utf-8").read()
    gt, gt2, gt3 = note(g), note(g2), note(g3)
    sec, sec3 = lit_section(gt), lit_section(gt3)
    rows = {}
    for head in ("## Genes that move with it", "## Genes that move opposite"):
        tab = gt.split(head, 1)[1].split("\n## ", 1)[0] if head in gt else ""
        for line in tab.splitlines() if "| Literature |" in tab else []:
            m = re.match(r"^\| \[\[([^\]|]+)\]\] \|.*\| ([^|]*) \|$", line)
            if m:
                rows[m.group(1)] = m.group(2).strip()
    vline = next((x for x in sec.splitlines() if x.startswith("**Connection verdicts**")), "")
    callout = next((x for x in sec.splitlines() if x.startswith("> Verification:")), "")
    trip, ent, n = map_lit(sv)
    a = ent.get(int(g["col"]))
    mp = {P[i]: trip.get((a, ent.get(pcols[i]))) for i in range(5) if ent.get(pcols[i], n) < n}
    check(c, "two reviews of one gene: the vault's table and verdict list and the map's badge show the latest "
             "review's verdict on P3 (not the older 'established'), and nothing of the older one's P4",
          rows.get(P[3], "").startswith("plausible (supported) · [PMID:31000003]") and f"[[{P[3]}]] plausible" in vline
          and f"[[{P[4]}]]" not in vline and rows.get(P[4], "") in ("", "\u2014")
          and (mp.get(P[3]) or [""])[0] == "plausible (supported)"
          and mp.get(P[4]) is None,
          {"rows": {p: rows.get(p) for p in P}, "map": {p: (v or [""])[0] for p, v in mp.items()}})
    a2 = ent.get(int(g2["col"]))
    check(c, "a gene whose latest review gave no verdict shows none (vault and map), not its older review's",
          "## What the literature says" in gt2 and "**Connection verdicts**" not in lit_section(gt2)
          and not any(k[0] == a2 for k in trip), lit_section(gt2)[:300])
    check(c, "the callout counts the three verdicts shown 'unverified' (the retracted-only one too), and does not flag "
             "the made-up PMID the id check removed as cited unread",
          '3 connection verdicts shown as "unverified"' in callout and "without having been read" not in callout
          and vline.count("unverified") == 3, callout)
    co3 = next((x for x in sec3.splitlines() if x.startswith("> Verification:")), "")
    vline3 = next((x for x in sec3.splitlines() if x.startswith("**Connection verdicts**")), "")
    check(c, "an id the look-up could not reach, but the checker graded: the callout says the claims show the "
             "checker's verdict (not 'ids not checked'), as the verdict does",
          "1 could not be looked up" in co3 and "graded by the citation checker all the same" in co3
          and "ids not checked" not in co3 and "established (supported)" in vline3, [co3, vline3[:200]])
    plain, open_fence = outside_fences(sec)
    check(c, "the crafted note in the vault: nothing put back together (no tag, definition or javascript: link), no "
             "e-mail / mailto / '//host' link, no Dataview query, and the generated lines after it are intact",
          not re.search(r"<[A-Za-z/!?]", plain) and "javascript" not in sec
          and "attacker\u200b@evil.example" in sec and "mailto:" not in sec and "\u200b//evil.example/x" in sec
          and not dataview_queries(sec) and "\u200b$= dv.paragraph" in sec and open_fence is None
          and vline and js.get("note_footer", "")[:40] in sec,
          re.findall(r"<[A-Za-z/!?].{0,30}", plain) or dataview_queries(sec) or sec[:600])
    bad = scan_for_keys(os.path.join(sv, "review"))
    check(c, "no API key in any file written", not bad, bad[:5])
    shutil.rmtree(sv, ignore_errors=True)


@case
def drug_dossier_trustworthy_dose(view, ents):
    """science#9: a dose is called the best trustworthy one only without an artifact flag; when no dose is, the
    dossier says so and shows the flags."""
    c = "drug_dossier_trustworthy_dose"
    wrong, n_none, moved = [], 0, []
    for d in ents["drugs"]:
        dos = D.build(view, "drug", d["name"])
        dt, t = dos.data, dos.text
        flags = dt.get("dose_artifact_flags") or {}
        shown = str(dt.get("shown_dose"))
        heads = [x for x in t.splitlines() if x.startswith("## Top genes at ")]
        tw = [x for x in heads if "(best trustworthy dose)" in x]
        if dt.get("shown_dose_trustworthy"):
            ok = (not flags.get(shown) and len(tw) == 1 and tw[0].startswith(f"## Top genes at {shown} uM")
                  and "FLAGGED" not in tw[0])
            vd = str(dt.get("vector_dose"))
            if vd != shown:
                moved.append(d["name"])
                # the flagged vector dose keeps its full lists (at the full limit), marked as the vector dose
                _nm, _e, key = D.resolve(view, "drug", d["name"])
                _P, full = D._drug(D.context(view), key, dict(D.LIMITS))
                rec = full["top_genes"][vd]
                ok = ok and any(x.startswith(f"## Top genes at {vd} uM (the drug's vector dose)") for x in heads) \
                    and all(len(rec[k]) == min(rec["n_" + k], D.LIMITS["top_genes"]) for k in ("up", "down"))
        else:
            n_none += 1
            ok = (not tw and "- No trustworthy dose:" in t and "NO dose is trustworthy" in t
                  and all(f"{k} uM: {v}" in t for k, v in flags.items() if v))
        if not ok:
            wrong.append((d["name"], shown, flags, tw))
    check(c, "every drug dossier: 'best trustworthy dose' only on a dose without artifact flags (a flagged vector "
             "dose keeps its full lists, marked); otherwise said plainly, with the flags", not wrong and ents["drugs"]
          and moved and n_none,
          wrong[:3] or f"{len(ents['drugs'])} drugs; {n_none} without a trustworthy dose; full lists of a clean dose "
                       f"first, then of the flagged vector dose, for {moved[:5]}")


@case
def cellosaurus_url_in_dossier(view, ents, work):
    """sdk#6 / science#10: the line's Cellosaurus URLs are written out in its dossier and in tahoe_lookup's result
    (web_fetch opens only URLs present in the conversation); no prompt tells the agent to compose one."""
    from tahoemap.review import tools as TL
    c = "cellosaurus_url_in_dossier"
    ln = ents["lines"][0]
    cv = ln["entity_id"].split(":", 1)[1]
    url = f"https://www.cellosaurus.org/{cv}.txt"
    ctx = TL.ToolContext(out=view, entity={"kind": "gene", "name": "x", "entity_id": "gene:0"},
                         cache_dir=os.path.join(work, "lit_ctx"))
    look = TL.execute("tahoe_lookup", {"kind": "line", "name": cv}, ctx)
    check(c, "the URL in the line's dossier (user message) and in tahoe_lookup's result",
          url in D.build(view, "line", ln["entity_id"]).user_message() and url in look, url)
    rd = os.path.join(REPO, "tahoemap", "review")
    texts = {os.path.relpath(p, rd): open(p, encoding="utf-8").read() for p in
             glob.glob(os.path.join(rd, "agents", "*.md")) + glob.glob(os.path.join(rd, "skills", "*", "SKILL.md"))}
    composed = [k for k, t in texts.items() if re.search(r"cellosaurus\.org/(?:<|CVCL_)", t)]
    lr = texts[os.path.join("agents", "line-reviewer.md")]
    check(c, "no agent or skill file gives a Cellosaurus URL to compose; line-reviewer points to the dossier's",
          not composed and "Cellosaurus URL given in the dossier" in lr, composed)


@case
def note_provenance(work):
    """science#2 / ui#4: no agent writes its own 'citations were checked' line; the note may cite only the review's
    checked citations (others stripped and counted, and the agent warned once); the footer is generated from the
    verification counts."""
    from tahoemap.review import tools as TL, verify as V
    c = "note_provenance"
    rd = os.path.join(REPO, "tahoemap", "review")
    claims_check = [p for p in glob.glob(os.path.join(rd, "agents", "*.md")) + glob.glob(os.path.join(rd, "skills",
                                                                                                      "*", "SKILL.md"))
                    if re.search(r"citations were checked|were checked against PubMed", open(p, encoding="utf-8").read(), re.I)]
    wn = open(os.path.join(rd, "skills", "writing-the-note", "SKILL.md"), encoding="utf-8").read()
    check(c, "no agent or skill file has the agent claim its own verification; writing-the-note forbids it",
          not claims_check and "Write no footer" in wn, claims_check)
    note = ("Known [PMID:31000001](https://pubmed.ncbi.nlm.nih.gov/31000001/); only here "
            "[PMID:31000003](https://pubmed.ncbi.nlm.nih.gov/31000003/) and PMID 31000004.\n")
    ctx, lib = lit_ctx(work, read=("31000001", "31000003", "31000004"))
    try:
        rv = F.sample_review("NQO1", ("31000001",), note=note)
        try:
            TL.submit_review(ctx, rv)
            warned = ""
        except TL.ToolError as e:
            warned = str(e)
        TL.submit_review(ctx, rv)
        r, rep = V.check_ids(ctx.submitted, ctx)
    finally:
        lib.uninstall()
    nt = r["note_markdown"]
    check(c, "submit_review warns once about papers cited only in the note",
          "note_markdown" in warned and "PMID:31000003" in warned and ctx.submitted is not None, warned[:200])
    check(c, "the note's ids that no item cites are removed and counted; the item's paper stays linked",
          rep["note_removed"] == 2 and rep["note_removed_ids"] == ["PMID:31000003", "PMID:31000004"]
          and "pubmed.ncbi.nlm.nih.gov/31000003" not in nt and "PMID:31000004 (citation removed: cited only" in nt
          and "](https://pubmed.ncbi.nlm.nih.gov/31000001/)" in nt and V.counts(r)["note_removed"] == 2, nt)
    feet = {m: V.finalize(r, m, rep if m != "off" else None,
                          {"status": "done"} if m == "llm" else None)["note_footer"] for m in ("off", "ids", "llm")}
    failed = V.finalize(r, "llm", rep, {"status": "failed", "error": "over budget"})["note_footer"]
    check(c, "the footer is generated from the counts: off / ids / llm done / llm failed",
          "were not checked (verification off)" in feet["off"] and "(--verify ids)" in feet["ids"]
          and "2 papers cited only in the text removed" in feet["ids"] and "citation checker" in feet["llm"]
          and "not checked against the abstracts (failed (over budget))" in failed
          and all(x.startswith("_AI-generated") and x.endswith("_") for x in list(feet.values()) + [failed]),
          feet["llm"])
    old = dict(r, note_markdown=r["note_markdown"] + "\n_AI-generated literature review of this run's data; "
               "citations were checked against PubMed and their abstracts.\nVerify before relying on it._\n")
    kept = V.finalize(old, "ids", rep)["note_markdown"]
    check(c, "an agent-written 'citations were checked' footer (old template) is dropped from the stored note",
          "citations were checked" not in kept and kept.strip() == r["note_markdown"].strip(), kept[-200:])
    prose = "Two cohorts agree: these claims were verified in independent patient samples [PMID:31000001].\n"
    check(c, "a note sentence about verification in the science (no PubMed / abstracts / disclaimer) is kept",
          V.drop_self_check(prose) == prose)
    ctx3, lib = lit_ctx(work, read=("31000001",), name="lit_ctx")
    try:
        said = TL.submit_review(ctx3, F.sample_review("NQO1", ("31000001",)))
    finally:
        lib.uninstall()
    check(c, "submit_review's answer does not tell the agent its citations will be checked (it may be --verify off)",
          "checked" not in said and "Review received" in said, said)


@case
def note_citation_forms(work):
    """science#2 (round 3): every paper the note names - PubMed, NCBI and Europe PMC links, bare URLs, 'PMIDs a, b'
    lists, PMC links and ids, Europe PMC preprint links - is one of the review's checked citations, or is removed and
    counted; a
    percent-encoded DOI never turns into markup in the stored note; a sentence about the literature search with a
    finding in it is kept (only a sentence that just vouches for the verification goes); science#8: the note marks
    a retracted paper where it is cited."""
    from tahoemap import vault as VA
    from tahoemap.review import tools as TL, verify as V
    c = "note_citation_forms"
    made_up = ["99999999", "99999998", "99999997", "99999996", "99999995"]
    note = (f"Known [PMID:31000001](https://pubmed.ncbi.nlm.nih.gov/31000001/) (Smith, PMID 31000001, 2020). Made up "
            f"[Smith et al. 2020](https://www.ncbi.nlm.nih.gov/pubmed/{made_up[0]}), [Jones](https://europepmc.org/"
            f"article/MED/{made_up[1]}), [Lee](https://europepmc.org/abstract/MED/{made_up[2]}/), "
            f"<https://www.ncbi.nlm.nih.gov/pubmed/?term={made_up[3]}> and https://europepmc.org/article/MED/"
            f"{made_up[4]}?x=1. Real, cited only here: PMIDs 31000003, 31000004 and 31000002. PMC: "
            "[Kim](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9999999/), PMCID: PMC1234567 and "
            "![fig](https://europepmc.org/article/PMC/PMC7654321); a preprint [Wu](https://europepmc.org/article/PPR/"
            "PPR123456). Retracted, cited by the item: "
            "[PMID:31000005](https://www.ncbi.nlm.nih.gov/pubmed/31000005).\n\n"
            "Encoded: [this paper](https://doi.org/10.1000/x%22%3E%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E) and "
            "DOI:10.1002/x%3Cscript%3E.\n\n"
            "References were checked in PubMed and Europe PMC full text for the pair; none links PIR to HMOX1, so the "
            "pair is a novel candidate.\n\n"
            "NQO1 is a classic NRF2 target. All citations were verified against PubMed abstracts.\n\n"
            "_AI-generated literature review of this run's data; citations were checked against PubMed and their "
            "abstracts.\nVerify before relying on it._\n")
    ctx, lib = lit_ctx(work, read=("31000001", "31000002", "31000003", "31000004", "31000005"))
    try:
        rv = F.sample_review("NQO1", ("31000001", "31000005"), note=note)
        try:
            TL.submit_review(ctx, rv)
            warned = ""
        except TL.ToolError as e:
            warned = str(e)
        TL.submit_review(ctx, rv)
        r, rep = V.check_ids(ctx.submitted, ctx)
        r_again, rep_again = V.check_ids(r, ctx)
    finally:
        lib.uninstall()
    fin = V.finalize(r, "ids", rep)
    nt, shown = fin["note_markdown"], VA.sanitize_note(fin["note_markdown"])
    gone = {"PMID:" + p for p in made_up} | {"PMID:31000002", "PMID:31000003", "PMID:31000004",
                                             "PMCID:PMC9999999", "PMCID:PMC1234567", "PMCID:PMC7654321",
                                             "EPMC:PPR/PPR123456"}
    check(c, "submit_review's one warning names the papers the note cites in other link forms, PMC ids included",
          all(x in warned for x in ("PMID:99999999", "PMID:99999998", "PMID:31000002", "PMCID:PMC9999999",
                                    "a PMC or Europe PMC id is always removed")), warned[:300])
    check(c, "every link form and list is read: the made-up PMIDs removed as not found, the note-only papers and "
             "PMC ids removed as cited only here, all counted",
          {"PMID:" + p for p in made_up} <= set(rep["missing"])
          and set(rep["note_removed_ids"]) == gone - {"PMID:" + p for p in made_up}
          and rep["note_removed"] == 7 and V.counts(fin)["note_removed"] == 7
          and "7 papers cited only in the text removed" in fin["note_footer"]
          and "PMID:2020" not in nt and all(f"{x} (citation removed: " in nt for x in gone), rep["note_removed_ids"])
    dests = re.findall(r"\]\(\s*<?([^)\s>]+)", shown) + re.findall(r"https?://[^\s)\]>]+", shown)
    named = {x for d in dests for x, _a, _b in TL.note_ids(d)}
    check(c, "the note shown in the vault links no paper but the review's checked citations",
          named <= set(TL.item_ids(fin)) and not any(p in shown for p in ("ncbi.nlm.nih.gov/pubmed/9999",
                                                                          "europepmc.org/article/MED/9999",
                                                                          "PMC9999999/")), sorted(named))
    check(c, "a percent-encoded DOI stays encoded: no tag or quote in the stored note or in the agent's warning",
          not re.search(r"<(?:img|script)|\"", nt) and "<img" not in warned and "<script" not in warned
          and "DOI:10.1000/x%22%3e%3cimg%20src%3dx%20onerror%3dalert(1)%3e (citation removed: not found" in nt
          and "DOI:10.1002/x%3cscript%3e (citation removed: not found" in nt
          and TL.norm_citation("DOI:10.1000/x%22%3E%3Cimg%3E") is None
          and TL.link("DOI:10.1002/(sici)1-2(3)4:5<6::aid-x7>8.0.co;2-y").startswith(
              "[DOI:10.1002/(sici)1-2(3)4:5%3c6"),
          nt[nt.find("Encoded"):][:300])
    check(c, "a sentence about the literature search with its finding is kept whole; a sentence (or footer) that only "
             "vouches for the verification is dropped",
          "References were checked in PubMed and Europe PMC full text for the pair; none links PIR to HMOX1, so the "
          "pair is a novel candidate." in nt and "NQO1 is a classic NRF2 target." in nt
          and "verified against PubMed abstracts" not in nt and "citations were checked" not in nt
          and "Verify before relying" not in nt, nt[-400:])
    lst = ("- NQO1 and HMOX1 are NRF2 targets [PMID:31000001](https://pubmed.ncbi.nlm.nih.gov/31000001/). The claims "
           "were checked by the citation checker.\n- Citations were checked against PubMed.\n- HMOX1 up 3x\n"
           "* Citations were verified in PubMed. NQO1 up 4.5x\n")
    want = ("- NQO1 and HMOX1 are NRF2 targets [PMID:31000001](https://pubmed.ncbi.nlm.nih.gov/31000001/).\n"
            "- HMOX1 up 3x\n* NQO1 up 4.5x\n")
    check(c, "in a list, only those sentences go: the other items, their lines and their markers stay",
          V.drop_self_check(lst) == want, repr(V.drop_self_check(lst)))
    check(c, "science#8: a retracted paper is marked where the note cites it, once (a second check adds nothing)",
          "[PMID:31000005](https://www.ncbi.nlm.nih.gov/pubmed/31000005) (retracted paper)" in nt
          and nt.count("(retracted paper)") == 1 and r_again["note_markdown"] == r["note_markdown"]
          and rep_again["note_removed"] == 7, nt[:200])


@case
def note_links_and_structure(work, view, ents):
    """Round 4 (the citation layer's checkers): every common way of naming a paper is read - 'DOI 10.x/y' as the tools
    print it, NCBI's 'pubmed?term=' links, 'PMIDs a, b, and c', a DOI in a publisher's or bioRxiv URL or in
    doi.org/10.x%2Fy - so a paper cited only in the note is removed, counted and warned about; a link whose text
    runs over two lines, with a '...' or (...) title, or by reference ([x][1] + '[1]: url') is removed whole (its
    definition too), and a link to a retracted paper is marked after its closing ')' or after each reference link,
    never in a destination or a definition; verification writes no '%%'; a paper an item cites by PMID and the note
    links by DOI (or the reverse) is one paper - kept, marked if retracted, counted once - and a retracted paper
    cited only in the note is not counted; dropping a self-check sentence keeps the lists and emphasis around it."""
    from tahoemap import vault as VA
    from tahoemap.review import tools as TL, verify as V
    c = "note_links_and_structure"
    ids = lambda t: [x for x, _a, _b in TL.note_ids(t)]                                   # noqa: E731
    # -- the forms, one by one
    single = {"(DOI 10.1000/fake.31000004)": "DOI:10.1000/fake.31000004",
              "[a](https://www.ncbi.nlm.nih.gov/pubmed?term=31000009)": "PMID:31000009",
              "https://www.ncbi.nlm.nih.gov/pubmed/?db=pubmed&term=31000009%5Buid%5D": "PMID:31000009",
              "https://www.biorxiv.org/content/10.1101/2020.01.01.123456v2.full.pdf": "DOI:10.1101/2020.01.01.123456",
              "[p](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0123456&type=printable)":
                  "DOI:10.1371/journal.pone.0123456",
              "https://www.frontiersin.org/articles/10.3389/fimmu.2020.01234/full": "DOI:10.3389/fimmu.2020.01234",
              "<https://doi.org/10.1000%2Ffake.31000003>": "DOI:10.1000/fake.31000003"}
    got = {x: ids(x) for x in single}
    lists = ids("(PMIDs 31000001, 31000002, and 31000003; PMIDs 31000004, 31000006, or 31000007)")
    check(c, "each form names its paper: 'DOI 10.x', pubmed?term=, a DOI in a publisher's / bioRxiv URL (version and "
             "'/full' dropped), doi.org with %2F, 'PMIDs a, b, and c' / 'a, b, or c'; a ratio or a year is no id",
          all(got[x] == [w] for x, w in single.items())
          and lists == [f"PMID:3100000{n}" for n in (1, 2, 3, 4, 6, 7)]
          and ids("ratio 3/10.5, PMID 31000004, 2020, and/10.1000/x") == ["PMID:31000004"]
          and TL.link_citations("(DOI 10.1000/fake.31000004)") == "([DOI:10.1000/fake.31000004](https://doi.org/"
                                                                    "10.1000/fake.31000004))",
          {x: g for x, g in got.items() if g != [single[x]]} or lists)
    # -- a fake review through the runner: the forms in its note, then the note as the vault shows it
    note = ("NQO1 is an NRF2 target ([PMID:31000001](https://pubmed.ncbi.nlm.nih.gov/31000001/)) (PMIDs 31000001, "
            "31000002, and 31000003) (DOI 10.1000/fake.31000004) [PubMed](https://www.ncbi.nlm.nih.gov/pubmed?term="
            "31000009). Preprint https://www.biorxiv.org/content/10.1000/fake.31000010v1.full and [PLOS](https://"
            "journals.plos.org/x/article?id=10.1000/fake.31000008&type=printable), <https://doi.org/10.1000%2Ffake."
            "31000007>.\n\nRetracted, cited by the item: [Doe et\nal.](https://pubmed.ncbi.nlm.nih.gov/31000005/ "
            "'Doe') and [Lee][]; only here: [Smith][s].\n\n[s]: https://pubmed.ncbi.nlm.nih.gov/31000006/\n"
            "[Lee]: https://pubmed.ncbi.nlm.nih.gov/31000005/\n")
    only_here = ["PMID:31000002", "PMID:31000003", "DOI:10.1000/fake.31000004", "PMID:31000009",
                 "DOI:10.1000/fake.31000010", "DOI:10.1000/fake.31000008", "DOI:10.1000/fake.31000007",
                 "PMID:31000006"]
    g = ents["genes"][min(6, len(ents["genes"]) - 1)]
    rv = F.sample_review("NQO1", ("31000001", "31000005"), note=note)
    steps = [{"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": [str(p) for p in range(31000001,
                                                                                                    31000011)]}}]},
             {"submit_review": rv}, {"submit_review": rv}]
    res, _fk = run(view, {"entities": {g["entity_id"]: steps}}, only=g["entity_id"], verify="ids")
    rec = ledger(view)[-1] if ledger(view) else {}
    st = json.load(open(os.path.join(view, rec["review"]), encoding="utf-8")) if rec.get("review") else {}
    nt = st.get("note_markdown") or ""
    shown = VA.sanitize_note(VA.drop_self_check(nt))
    warned = " ".join(x for x in map(json.dumps, events(view, rec) if rec else []) if "not accepted yet" in x)
    ver = (st.get("verification") or {}).get("ids") or {}
    check(c, "the run: every paper the note names but no item cites is removed (marker in place), counted, and was "
             "named in the reviewer's one warning",
          res.counts == {"done": 1} and sorted(ver.get("note_removed_ids") or []) == sorted(only_here)
          and ver.get("note_removed") == 8 and "8 papers cited only in the text removed" in st.get("note_footer", "")
          and all(f"{x} (citation removed: cited only in this text" in nt for x in only_here)
          and all(x in warned for x in only_here), {"removed": ver.get("note_removed_ids"), "note": nt[:400],
                                                   "warned": warned[:300]})
    check(c, "the vault's note links no paper but the items' (no term= link, no preprint or publisher URL, no "
             "'%2F' DOI, no third id of a list, no reference link to a removed paper), and shows each removal",
          not re.search(r"term=3100000|biorxiv|plos\.org|10\.1000%2F|and 31000003\)|\[Smith\]|\[s\]:|31000006/",
                        shown)
          and shown.count("(citation removed: cited only in this text") == 8, shown[:600])
    check(c, "a retracted paper's two-line link is marked after its ')' (not as a title), a reference link after "
             "its use (not in the definition, which the vault keeps); counted once",
          "[Doe et\nal.](https://pubmed.ncbi.nlm.nih.gov/31000005/ 'Doe') (retracted paper)" in shown
          and "[Lee][] (retracted paper)" in shown and "[Lee]: https://pubmed.ncbi.nlm.nih.gov/31000005/" in shown
          and "/ (retracted paper)" not in nt and ver.get("retracted") == 1
          and "1 retracted paper (cited, not support)" in st.get("note_footer", ""), shown[-400:])
    reset(view, c)
    # -- the link forms, removed or marked
    why = {"PMID:31000002": "citation removed: x"}
    u2, u5 = "https://pubmed.ncbi.nlm.nih.gov/31000002/", "https://pubmed.ncbi.nlm.nih.gov/31000005/"
    strip = {f"A ([Smith et\nal.]({u2})).": "A (PMID:31000002 (citation removed: x)).",
             f"A ([S]({u2} 'T')), ([J]({u2} (T))).": "A (PMID:31000002 (citation removed: x)), (PMID:31000002 "
                                                     "(citation removed: x)).",
             f"A [S][1], [s][], [S] and [ok].\n\n[1]: {u2}\n[S]:\n  <{u2}>\n  \"T\"\n[ok]: {u5}\n":
                 "A PMID:31000002 (citation removed: x), PMID:31000002 (citation removed: x), PMID:31000002 "
                 f"(citation removed: x) and [ok].\n\n[ok]: {u5}\n",
             f"> A [S][q]\n>\n> [q]: {u2}\n": "> A PMID:31000002 (citation removed: x)\n>\n>\n",
             f"Deep [a [b [c]] d]({u2}) end.": "Deep PMID:31000002 (citation removed: x) end."}
    out = {x: V._strip_from_note(x, why) for x in strip}
    check(c, "a link over two lines, with a '...' or (...) title, by reference (full, collapsed, shortcut; its "
             "definition, in a blockquote too) or with deeper brackets is removed whole",
          all(out[x] == w for x, w in strip.items()), {x[:30]: o for x, o in out.items() if o != strip[x]})
    mark = {f"A ([Doe et\nal.]({u5} 'x')).": f"A ([Doe et\nal.]({u5} 'x') (retracted paper)).",
            f"A ([Doe]({u5} (retracted paper))).": f"A ([Doe]({u5}) (retracted paper)).",     # as stored before
            f"A [Doe][1].\n\n[1]: {u5} (retracted paper)": f"A [Doe][1] (retracted paper).\n\n[1]: {u5}",
            f"A [Doe][1], [1] and [x [y [z]]]({u5}).\n\n[1]: {u5}":
                f"A [Doe][1] (retracted paper), [1] (retracted paper) and [x [y [z]]]({u5}) (retracted paper)."
                f"\n\n[1]: {u5}"}
    out = {x: V._mark_retracted(x, ["PMID:31000005"]) for x in mark}
    check(c, "the retraction mark goes after the whole link or each reference link, once; a mark an earlier version "
             "left in a destination or definition is moved there",
          all(out[x] == w and V._mark_retracted(w, ["PMID:31000005"]) == w for x, w in mark.items()),
          {x[:30]: o for x, o in out.items() if o != mark[x]})
    # -- no '%%' from verification; one paper under two ids
    ctx, lib = lit_ctx(work, read=[str(p) for p in range(31000001, 31000011)])
    try:
        pct = TL.normalize_review(F.sample_review("NQO1", ("31000001",), note=(
            "NQO1 is induced ([a](https://doi.org/10.1000/a%25%25b)). KEY FINDING: HMOX1 rises 4.5x in A549. Also "
            "([c](https://doi.org/10.1000/c%25%25d)) and DOI:10.1000/e%%f.\n")), ctx)[0]
        r_pct, _rep = V.check_ids(pct, ctx)
        TL.pubmed_abstracts(ctx, ["31000001", "31000005"])                  # the agent read them (records cached)
        ctx.seen_ids.add("DOI:10.1000/fake.31000001")
        alias = F.sample_review("NQO1", ("31000005",), note="NQO1 ([Doe 2020](https://doi.org/10.1000/fake.31000005)"
                                ") and ([x](https://pubmed.ncbi.nlm.nih.gov/31000005/)).\n")
        TL.submit_review(ctx, alias)
        r_al, rep_al = V.check_ids(ctx.submitted, ctx)
        rev = F.sample_review("NQO1", (), note="NQO1 ([Smith](https://pubmed.ncbi.nlm.nih.gov/31000001/)).\n")
        for it in rev["established"] + rev["connection_verdicts"][:1]:
            it["citations"] = ["DOI:10.1000/fake.31000001"]
        r_rev, rep_rev = V.check_ids(TL.normalize_review(rev, ctx)[0], ctx)
        lone = F.sample_review("NQO1", ("31000001",), note="NQO1 [x](https://pubmed.ncbi.nlm.nih.gov/31000001/) and "
                               "[y](https://pubmed.ncbi.nlm.nih.gov/31000005/).\n")
        r_lone, rep_lone = V.check_ids(TL.normalize_review(lone, ctx)[0], ctx)
    finally:
        lib.uninstall()
    fin_al, fin_lone = V.finalize(r_al, "ids", rep_al), V.finalize(r_lone, "ids", rep_lone)
    check(c, "verification writes no '%%' (a link's text, a removal marker), so the vault's comment filter hides "
             "no finding",
          "%%" not in r_pct["note_markdown"] and "KEY FINDING: HMOX1 rises 4.5x" in VA.sanitize_note(
              r_pct["note_markdown"]) and "%%" not in TL.link_citations("DOI:10.1000/a%25%25b DOI:10.1000/e%%f")
          and TL.cid_text("DOI:10.1000/e%%f") == "DOI:10.1000/e%25%f", r_pct["note_markdown"])
    check(c, "one paper cited by PMID in the item and by DOI (and PMID) in the note: no warning, kept, marked as "
             "retracted after each link, counted once",
          ctx.submit_attempts == 1 and rep_al["note_removed"] == 0 and rep_al["n_cited"] == 1
          and V.counts(fin_al)["n_citations"] == 1 and rep_al["retracted"] == 1
          and rep_al["same_paper"] == {"DOI:10.1000/fake.31000005": "PMID:31000005"}
          and r_al["note_markdown"].count("(retracted paper)") == 2
          and "fake.31000005) (retracted paper)" in r_al["note_markdown"], r_al["note_markdown"])
    check(c, "the reverse (the item cites the DOI, the note links the PMID): kept, counted once",
          rep_rev["note_removed"] == 0 and rep_rev["n_cited"] == 1 and "(citation removed" not in r_rev["note_markdown"],
          r_rev["note_markdown"])
    check(c, "a retracted paper cited only in the note is removed and not counted as a cited retracted paper",
          rep_lone["retracted"] == 0 and rep_lone["retracted_ids"] == [] and rep_lone["note_removed"] == 1
          and "retracted" not in fin_lone["note_footer"]
          and "1 paper cited only in the text removed" in fin_lone["note_footer"], fin_lone["note_footer"])
    # -- dropping a self-check sentence keeps the structure around it
    drop = {"1. A is up.\n2. Citations were checked against PubMed.\n3. B is down.\n": "1. A is up.\n3. B is down.\n",
            "- A is up.\n- Citations were checked against PubMed.\n  NQO1 is up 4.5x.\n- B is down.":
                "- A is up.\n- NQO1 is up 4.5x.\n- B is down.\n",
            "- A is up.\n  - Citations were checked against PubMed.\n  - NQO1 is up 4.5x.":
                "- A is up.\n  - NQO1 is up 4.5x.\n",
            "_NQO1 is up. Citations were checked against PubMed._ HMOX1 is down.":
                "_NQO1 is up._ HMOX1 is down.\n",
            "SYNTH0303 moves with SYNTH0347. **Caveat: one partner is unexplained. All citations were verified against "
            "PubMed.**": "SYNTH0303 moves with SYNTH0347. **Caveat: one partner is unexplained.**\n",
            "**Citations were checked against PubMed. Caveat: X is up 4x.**": "**Caveat: X is up 4x.**\n",
            "Intro. _This review was AI-generated and not checked by a person. Citations were verified against their "
            "abstracts._": "Intro.\n",
            "> - Citations were checked against PubMed. NQO1 up.\n> - B": "> - NQO1 up.\n> - B\n"}
    out = {x: V.drop_self_check(x) for x in drop}
    check(c, "a dropped self-check leaves no empty list item, moves no line into another item, keeps a nested list "
             "nested and its emphasis closed; 'This review was AI-generated ...' is a disclaimer",
          all(out[x] == w for x, w in drop.items()), {x[:40]: o for x, o in out.items() if o != drop[x]})


@case
def check_status_contract(work):
    """The shared contract: check_status and shown_verdict on every connection verdict and every citing item,
    'verification' {ids, llm} counts, for each way an item can end up."""
    from tahoemap.review import tools as TL, verify as V
    c = "check_status_contract"
    vs = [{"partner": "A1", "verdict": "established", "citations": ["PMID:39999999"]},
          {"partner": "A2", "verdict": "contradicted", "citations": ["PMID:31000002"]},
          {"partner": "A3", "verdict": "plausible", "citations": []},
          {"partner": "A4", "verdict": "indirect", "citations": ["PMID:31000001", "PMID:31000003"]}]
    rv = review_with(vs)
    ctx, lib = lit_ctx(work, read=("31000001", "31000002", "31000003"))
    try:
        r, _e = TL.normalize_review(rv)
        ri, rep = V.check_ids(r, ctx)
        lib.esummary_down = True                                        # PubMed unreachable (a fresh cache)
        ctx2, _l = lit_ctx(work, lib=lib, read=("31000001",), name="lit_ctx_down")
        ru, repu = V.check_ids(r, ctx2)
    finally:
        lib.uninstall()
    st = lambda rr: [(v["partner"], v.get("check_status"), v.get("shown_verdict"))  # noqa: E731
                     for v in rr["connection_verdicts"]]
    check(c, "after the id check: citations_removed -> 'unverified'; valid ids, no claim check -> not_checkable",
          st(ri) == [("A1", "citations_removed", "unverified"), ("A2", "not_checkable", "contradicted"),
                     ("A3", "not_checkable", "plausible"), ("A4", "not_checkable", "indirect")]
          and ri["established"][0]["shown_verdict"] == "established" and "check_status" not in ri["unexpected"][0],
          st(ri))
    check(c, "PubMed unreachable: unchecked, the agent's verdict shown, counted", repu["unchecked"] == 4
          and [x[1] for x in st(ru)] == ["unchecked", "unchecked", "not_checkable", "unchecked"]
          and [x[2] for x in st(ru)] == ["established", "contradicted", "plausible", "indirect"], (st(ru), repu))
    chk = {"summary": "s", "verdicts": [
        {"claim_id": "V2", "verdict": "not supported", "direction": "not stated", "reason": "no"},
        {"claim_id": "V4", "verdict": "partly", "direction": V.SAME, "reason": "one gene"}]}
    rl, summ = V.apply_check(ri, chk)
    fin = V.finalize(rl, "llm", rep, dict(summ, status="done"))
    ver = fin["verification"]
    check(c, "after the claim check: not_supported -> 'unverified', partly -> its verdict; the verification block",
          st(fin) == [("A1", "citations_removed", "unverified"), ("A2", "not_supported", "unverified"),
                      ("A3", "not_checkable", "plausible"), ("A4", "partly", "indirect")]
          and all(isinstance(ver["ids"][k], int) for k in ("checked", "removed", "unchecked", "retracted"))
          and ver["ids"]["removed"] == 1 and ver["llm"]["status"] == "done"
          and (ver["llm"]["not_supported"], ver["llm"]["partly"]) == (1, 1) and fin["note_footer"].startswith("_AI"),
          {"ids": {k: ver["ids"][k] for k in ("checked", "removed", "unchecked", "retracted")},
           "llm": {k: ver["llm"][k] for k in ("status", "supported", "partly", "not_supported", "not_checkable")}})
    off = V.finalize(r, "off")
    check(c, "--verify off: every citing item unchecked, ids and llm not_run",
          [x[1] for x in st(off)] == ["unchecked", "unchecked", "not_checkable", "unchecked"]
          and off["verification"]["ids"]["status"] == "not_run" and off["verification"]["llm"]["status"] ==
          "not_run", st(off))


@case
def contract_end_to_end(view, ents):
    """A review through the runner (fake API, --verify llm): the stored JSON carries the contract fields and the
    note footer; the checker's request held the data lines."""
    c = "contract_end_to_end"
    g = ents["genes"][5]
    res, _fk = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="llm")
    rec = ledger(view)[-1] if ledger(view) else {}
    rv = json.load(open(os.path.join(view, rec["review"]), encoding="utf-8")) if rec.get("review") else {}
    ver = rv.get("verification") or {}
    cvs = rv.get("connection_verdicts") or []
    check(c, "every connection verdict and citing item has check_status / shown_verdict; verification and footer",
          res.counts == {"done": 1} and cvs and all(v.get("check_status") in V_STATUSES and v.get("shown_verdict")
                                                     for v in cvs)
          and all(it.get("check_status") for s in ("established", "missing") for it in rv.get(s) or [])
          and ver.get("llm", {}).get("status") == "done" and isinstance(ver.get("ids", {}).get("checked"), int)
          and "citation checker" in (rv.get("note_footer") or ""),
          {"verdicts": [(v.get("partner"), v.get("check_status"), v.get("shown_verdict")) for v in cvs],
           "footer": rv.get("note_footer")})
    conv = H.conversation(events(view, rec), "citation-checker") if rec else []
    prompt = conv[0]["content"] if conv and isinstance(conv[0]["content"], str) else json.dumps(conv[:1])
    check(c, "the checker's prompt held each claim's data line and the verdict's meaning",
          "data: moves with: cos 0.71" in prompt and "the verdict requires:" in prompt, prompt[:200])
    reset(view, c)


V_STATUSES = ("supported", "partly", "not_supported", "not_checkable", "unchecked", "citations_removed")


# ----------------------------------------------------------------------------- runner, keys and ledger (review 2)
def user_msgs_after_first(view, rec, agent=None):
    """The user messages of a history's reviewer conversation after the first (the dossier)."""
    conv = H.conversation(events(view, rec), agent)
    return [m for m in conv[1:] if m["role"] == "user"]


@case
def streaming_and_max_tokens(view, ents):
    """sdk#1, sdk#2: every request is streamed; max_tokens by effort; only cut-offs in a row end a conversation."""
    c = "streaming_and_max_tokens"
    g, g2, g3 = ents["genes"][0], ents["genes"][1], ents["genes"][2]
    res, fk = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="llm")
    rev = [x for x in fk.calls if x["role"] == "reviewer"]
    chk = [x for x in fk.calls if x["role"] == "checker"]
    check(c, "every request streamed (client.beta.messages.stream), none rejected",
          res.counts == {"done": 1} and fk.calls and all(x["stream"] for x in fk.calls) and not res.violations,
          [(x["role"], x["stream"]) for x in fk.calls])
    check(c, "max_tokens 64K at effort high (reviewer) and medium (checker)",
          {x["max_tokens"] for x in rev} == {64000} and {x["max_tokens"] for x in chk} == {64000},
          [(x["role"], x["max_tokens"]) for x in fk.calls])
    reset(view, c)
    res2, fk2 = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids", effort="xhigh")
    check(c, "max_tokens 128K at effort xhigh; 64K on a model whose ceiling is 64K",
          res2.counts == {"done": 1} and {x["max_tokens"] for x in fk2.calls} == {128000}
          and R.max_tokens_for("claude-opus-5-5", "max") == 128000
          and R.max_tokens_for("claude-haiku-4-5", "max") == 64000, [x["max_tokens"] for x in fk2.calls])
    reset(view, c)
    read = {"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001"]}}]}
    cut = {"max_tokens": True}
    sc = {"entities": {g2["entity_id"]: [cut, read, read, cut, {"submit_review": F.sample_review()}],
                       g3["entity_id"]: [read, cut, cut, {"submit_review": F.sample_review()}]}}
    res3, _ = run(view, sc, only=[g2["entity_id"], g3["entity_id"]], concurrency=1, verify="ids")
    st = {r["entity_id"]: r["status"] for r in ledger(view)}
    check(c, "a second cut-off after useful turns gets a nudge too (done); two in a row end it (no_review)",
          st == {g2["entity_id"]: "done", g3["entity_id"]: "no_review"} and not res3.violations, st)
    reset(view, c)


@case
def transient_refusal(view, ents):
    """sdk#0, keys_state#9: a refusal with stop_details.recommended_model (the fallback model was busy) is not
    final: recorded as failed with the recommended model, and retried by the next run."""
    c = "transient_refusal"
    g = ents["genes"][3]
    sc = F.FakeAPI({"entities": {g["entity_id"]: [{"refusal": "bio", "recommended_model": "claude-opus-4-8"}]
                                 + good()}})
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        res, _ = run(view, sc, only=g["entity_id"], verify="ids", quiet=False)
    sys.stdout.write(buf.getvalue())
    rec = ledger(view)[-1]
    check(c, "status failed (not refused), with the category, the recommended model and the reason",
          res.counts == {"failed": 1} and rec["status"] == "failed" and rec.get("recommended_model") ==
          "claude-opus-4-8" and rec.get("refusal_category") == "bio" and rec.get("transient_refusal") is True
          and "fallback model was unavailable" in (rec.get("error") or "")
          and "recommended model: claude-opus-4-8" in buf.getvalue(),
          {k: rec.get(k) for k in ("status", "recommended_model", "refusal_category", "error")})
    res2, _ = run(view, sc, only=g["entity_id"], verify="ids")
    check(c, "the next run retries it (done)", res2.counts == {"done": 1}, res2.counts)
    reset(view, c)


@case
def empty_response(view, ents):
    """sdk#3: an empty end_turn response is never echoed back as an assistant message with content []."""
    c = "empty_response"
    g = ents["genes"][4]
    read = {"tool_use": [{"name": "pubmed_abstracts", "input": {"pmids": ["31000001"]}}]}
    res, fk = run(view, {"entities": {g["entity_id"]: [read, {"empty": True},
                                                       {"submit_review": F.sample_review()}]}},
                  only=g["entity_id"], verify="ids")
    rec = ledger(view)[-1]
    conv = H.conversation(events(view, rec))
    empty = [i for i, m in enumerate(conv) if m["role"] == "assistant" and not m.get("content")]
    roles = [m["role"] for m in conv]
    check(c, "done after the nudge; no empty assistant turn sent; nothing the API would reject",
          res.counts == {"done": 1} and not empty and not res.violations and roles[-2:] == ["user", "user"]
          and "without calling" in json.dumps(conv[-1]), f"{res.counts}; roles {roles}; {res.violations[:2]}")
    reset(view, c)


@case
def lost_responses(view, ents):
    """sdk#2: timeouts and streams cut short are re-sent on a small budget of their own, and a lost response that
    may have been billed is charged an estimate, marked as estimated."""
    c = "lost_responses"
    g, g2, g3, g4, g5, g6 = ents["genes"][:6]
    SLEEPS.clear()
    sc = {"entities": {g["entity_id"]: [{"error": "timeout"}] + good(),
                       g2["entity_id"]: [dict(good()[0], drop=True)] + good(),
                       g3["entity_id"]: [dict(good()[0], drop="clean")] + good(),
                       g4["entity_id"]: [{"error": "connection"}] + good(),
                       g5["entity_id"]: [dict(good()[0], drop="overloaded")] + good(),
                       g6["entity_id"]: [dict(good()[0], drop="empty")] + good()}}
    six = (g, g2, g3, g4, g5, g6)
    res, fk = run(view, sc, only=[e["entity_id"] for e in six], concurrency=1, verify="ids")
    by = {r["entity_id"]: r for r in ledger(view)}
    est = {e: round(by[e].get("estimated_usd") or 0, 4) for e in by}
    check(c, "a timeout, a stream broken off, one ended early, one with an overloaded event, one closed before "
             "message_start, a connection error: re-sent, all done",
          res.counts == {"done": 6} and not res.violations and len(SLEEPS) == 6, f"{res.counts}; {res.violations[:2]}")
    check(c, "lost responses charged an estimate (in the ledger, included in cost_usd); a connection never made "
             "is not", all(est[e["entity_id"]] >= 0.32 and by[e["entity_id"]]["cost_usd"] > est[e["entity_id"]]
                          for e in (g, g2, g3, g5, g6)) and est[g4["entity_id"]] == 0, est)
    kw = {"model": "claude-opus-5-5", "max_tokens": 64000, "messages": [{"role": "user", "content": "x" * 30000}]}
    lc = [R.lost_cost(kw), R.lost_cost(kw, max_out=20000), R.lost_cost(kw, max_out=50000), R.lost_cost(kw, 2)]
    check(c, "the estimate: context at the full input price + 16K output tokens at least, twice the attempt's longest "
             "answer, at most max_tokens; once per send", abs(lc[0] - (10000 * 4 + 16000 * 20) / 1e6) < 0.002
          and abs(lc[1] - (10000 * 4 + 40000 * 20) / 1e6) < 0.002 and abs(lc[2] - (10000 * 4 + 64000 * 20) / 1e6)
          < 0.002 and abs(lc[3] - 2 * lc[0]) < 1e-9, [round(x, 4) for x in lc])
    err5 = [e for e in events(view, by[g5["entity_id"]]) if e["event"] == "error"]
    check(c, "an error event mid-stream (HTTP 200, overloaded_error) waits and retries like a 529",
          len(err5) == 1 and err5[0]["category"] == K.WAIT and err5[0].get("type") == "overloaded_error"
          and not err5[0].get("network"), [(e.get("class"), e.get("status"), e.get("type")) for e in err5])
    err = [e for e in events(view, by[g["entity_id"]]) if e["event"] == "error"]
    err2 = [e for e in events(view, by[g2["entity_id"]]) if e["event"] == "error"]
    check(c, "history: the error events carry the estimate and how the request was lost",
          len(err) == 1 and err[0]["class"] == "APITimeoutError" and err[0].get("network")
          and err[0].get("estimated_cost_usd", 0) > 0 and len(err2) == 1 and err2[0].get("phase") == "stream",
          [(e.get("class"), e.get("phase"), e.get("estimated_cost_usd")) for e in err + err2])
    reset(view, c)
    res2, fk2 = run(view, {"entities": {g5["entity_id"]: [{"error": "timeout"}] * 4 + good()}},
                    only=g5["entity_id"], verify="ids", per_entity_usd=50)
    rec = ledger(view)[-1]
    check(c, "timeouts: at most 2 re-sends, then the entity fails (not 12 waits)",
          rec["status"] == "failed" and len(fk2.calls) == 3 and "APITimeoutError" in (rec.get("error") or ""),
          {"status": rec["status"], "calls": len(fk2.calls), "error": (rec.get("error") or "")[:80]})
    reset(view, c)
    sc3 = F.FakeAPI({"entities": {g5["entity_id"]: [{"error": "timeout"}] + good()}})
    res3, _ = run(view, sc3, only=g5["entity_id"], verify="ids", per_entity_usd=0.3)
    rec3 = ledger(view)[-1]
    check(c, "the estimate counts against the per-entity cap: the attempt stops, nothing more sent; as 'failed' "
             "(a network problem), not over_budget", rec3["status"] == "failed" and len(sc3.calls) == 1
          and rec3.get("estimated_usd", 0) >= 0.3 and "estimated for responses lost" in (rec3.get("error") or ""),
          {k: rec3.get(k) for k in ("status", "cost_usd", "estimated_usd", "error")})
    res4, _ = run(view, sc3, only=g5["entity_id"], verify="ids", per_entity_usd=0.3)
    check(c, "so the next run retries it at the same cap (done)", res4.counts == {"done": 1}, res4.counts)
    reset(view, c)


@case
def budget_lines(view, ents):
    """science#5: every user message after the dossier ends with the spend and requests so far; near the cap or
    max_turns the agent is asked to submit now."""
    c = "budget_lines"
    g = ents["genes"][5]
    res, _ = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids")
    rec = ledger(view)[-1]
    um = user_msgs_after_first(view, rec)
    last = [m["content"][-1] for m in um]
    check(c, "after the tool results: a text block '[runner] Budget: $x of $3.00 used; n of N requests made.'",
          res.counts == {"done": 1} and len(um) == 2 and all(b.get("type") == "text" and
                                                             b["text"].startswith("[runner] Budget:") and
                                                             "of $3.00 used" in b["text"] for b in last)
          and um[0]["content"][0]["type"] == "tool_result", [b.get("text", b.get("type"))[:70] for b in last])
    near = R.budget_text(2.4, 3.0, 5, 30, 0.2, "submit_review")
    final = R.budget_text(2.0, 3.0, 5, 30, 1.1, "submit_review")
    turns = R.budget_text(0.5, 3.0, 29, 30, 0.1, "submit_review")
    check(c, "past 75% of the cap: 'stop searching'; when the next request is the last: 'This is your last "
             "request'", "stop searching and call submit_review" in near and "last request" not in near
          and "This is your last request" in final and "This is your last request" in turns
          and "Little is left" not in R.budget_text(0.5, 3.0, 5, 30, 0.1, "submit_review"), [near, final])
    reset(view, c)


@case
def stop_after_submit(view, ents):
    """keys_state#0, #5, #8: a review submitted before the stop is stored as done (its citation check marked not
    run), the checker's late response is recorded, and `review run --recheck` completes the check without the
    reviewer."""
    c = "stop_after_submit"
    g = ents["genes"][6]
    grace = R.STOP_GRACE
    R.STOP_GRACE = 0.5
    try:
        sc = F.FakeAPI({"entities": {g["entity_id"]: good()},
                        "checker": {g["name"]: [{"submit_check": "auto", "signal": "SIGINT", "sleep_after": 1.5}]}})
        res, _ = run(view, sc, only=g["entity_id"], verify="llm")
        time.sleep(2.0)                                 # the checker's answer comes after the run has ended
    finally:
        R.STOP_GRACE = grace
    L = ledger(view)
    main = [r for r in L if r.get("status") != "note"]
    late = [r for r in L if r.get("status") == "note" and r.get("late")]
    rp = os.path.join(view, main[-1]["review"]) if main and main[-1].get("review") else ""
    rv = json.load(open(rp, encoding="utf-8")) if rp and os.path.exists(rp) else {}
    ver = rv.get("verification") or {}
    check(c, "Ctrl-C during the citation check: the review is stored as done (ids checked, claims not run)",
          res.exit_code == 130 and [r["status"] for r in main] == ["done"]
          and main[-1].get("stopped_during_verification") and ver.get("ids", {}).get("status") == "done"
          and ver.get("llm", {}).get("status") == "not_run" and "not checked against the abstracts"
          in (rv.get("note_footer") or "") and glob.glob(os.path.join(view, "review", "notes", "gene", "*.md")),
          {"exit": res.exit_code, "ledger": [(r["status"], r.get("note")) for r in L], "llm": ver.get("llm")})
    ev = events(view, main[-1]) if main else []
    kinds = [e["event"] for e in ev]
    est = float(main[-1].get("estimated_usd") or 0) if main else 0.0
    inflight = [e for e in ev if e["event"] == "error" and e.get("class") == "InFlightAtStop"]
    real = float(ev[-1].get("cost_usd") or 0) if ev else 0.0
    check(c, "the checker's request in flight at the close: charged an estimate (done line, history error event)",
          est > 0 and len(inflight) == 1 and abs(inflight[0]["estimated_cost_usd"] - est) < 1e-6
          and kinds.index("error") < kinds.index("end"), {"estimated_usd": est, "events": kinds[-4:]})
    check(c, "the late response: a ledger note line whose real cost replaces that estimate, a late event after the "
          "history's end", len(late) == 1 and real > 0 and abs(late[0].get("replaces_estimate_usd", 0) - est) < 1e-6
          and abs(late[0]["cost_usd"] - (real - est)) < 1e-5 and abs(late[0].get("estimated_usd", 0) + est) < 1e-6
          and abs(sum(float(r["cost_usd"]) for r in L) - float(main[-1]["cost_usd"]) + est - real) < 1e-5
          and "end" in kinds and kinds.index("end") < len(kinds) - 1 and ev[-1].get("late")
          and ev[-1]["event"] == "response", {"late": late[:1], "events": kinds[-3:]})
    st = Ledger(view).states()[g["entity_id"]]
    out = []
    R.status(view, say=out.append)
    check(c, "its state stays done; status points at --recheck", st["status"] == "done"
          and any("--recheck" in x for x in out), [x for x in out if "recheck" in x])
    grace = R.STOP_GRACE
    R.STOP_GRACE = 0.5
    try:                                                # a --recheck that is itself stopped while the checker runs
        sc = F.FakeAPI({"checker": {g["name"]: [{"submit_check": "auto", "signal": "SIGINT", "sleep_after": 1.5}]}})
        res1, fk1 = run(view, sc, only=g["entity_id"], verify="llm", recheck=True)
        time.sleep(2.0)
    finally:
        R.STOP_GRACE = grace
    L1 = ledger(view)
    st1 = Ledger(view).states()[g["entity_id"]]
    rv1 = json.load(open(rp, encoding="utf-8")) if rp else {}
    out1 = []
    R.status(view, say=out1.append)
    check(c, "a --recheck stopped while the checker runs: a ledger note, the review unchanged, still --recheck-able",
          res1.exit_code == 130 and [x["role"] for x in fk1.calls] == ["checker"]
          and [r.get("note") for r in L1[len(L):] if not r.get("late")] == ["recheck: paused"]
          and st1["last"] == main[-1] and st1["status"] == "done" and R.recheck_pending(view, st1, "llm")
          and rv1.get("verification", {}).get("llm", {}).get("status") == "not_run"
          and any("--recheck" in x for x in out1),
          {"exit": res1.exit_code, "new lines": [(r["status"], r.get("note")) for r in L1[len(L):]],
           "pending": R.recheck_pending(view, st1, "llm")})
    old_line = {"entity_id": g["entity_id"], "kind": "gene", "name": g["name"], "status": "done", "recheck": True,
                "review_unchanged": True, "error": "recheck stopped: stopped by SIGINT; the stored review is unchanged"}
    st_old = dict(st1, last=old_line)                   # the line an earlier version wrote for a stopped recheck
    check(c, "a done line of an earlier version without the review's path or statuses: read from the review JSON",
          R.recheck_pending(view, st_old, "llm") and not R.recheck_pending(view, st_old, "ids"),
          {"llm": R.recheck_pending(view, st_old, "llm"), "ids": R.recheck_pending(view, st_old, "ids")})
    n_files = len(glob.glob(os.path.join(view, "review", "history", "gene", "*", "*.jsonl")))
    res2, fk2 = run(view, F.FakeAPI({"checker": "auto"}), only=g["entity_id"], verify="llm", recheck=True)
    rv2 = json.load(open(rp, encoding="utf-8")) if rp else {}
    last = ledger(view)[-1]
    check(c, "--recheck: only the citation checker runs; the stored review gets the check (llm done)",
          res2.exit_code == 0 and fk2.calls and {x["role"] for x in fk2.calls} == {"checker"}
          and rv2.get("verification", {}).get("llm", {}).get("status") == "done" and last["status"] == "done"
          and last.get("recheck") and rv2.get("meta", {}).get("recheck_history")
          and len(glob.glob(os.path.join(view, "review", "history", "gene", "*", "*.jsonl"))) == n_files + 1
          and "citation checker" in (rv2.get("note_footer") or ""),
          {"calls": [x["role"] for x in fk2.calls], "llm": rv2.get("verification", {}).get("llm", {}).get("status"),
           "ledger": (last["status"], last.get("recheck"))})
    res3, fk3 = run(view, F.FakeAPI({"checker": "auto"}), only=g["entity_id"], verify="llm", recheck=True)
    res4, fk4 = run(view, F.FakeAPI({}), only=g["entity_id"], verify="llm")
    check(c, "then nothing is left to check or review", not fk3.calls and not fk4.calls
          and res3.message == res4.message == "nothing to do", [res3.message, res4.message])
    conn = pd.read_parquet(os.path.join(view, "review", "connections.parquet"))
    find = pd.read_parquet(os.path.join(view, "review", "findings.parquet"))
    check(c, "connections.parquet and findings.parquet carry check_status and shown_verdict",
          {"check_status", "shown_verdict"} <= set(conn.columns) and {"check_status", "shown_verdict"}
          <= set(find.columns) and set(conn["check_status"]) <= set(V_STATUSES) and conn["shown_verdict"].all(),
          conn[["partner", "verdict", "check_status", "shown_verdict"]].to_dict("records"))
    reset(view, c)


@case
def sighup(view, ents):
    """keys_state#5: SIGHUP (the terminal closed) stops the run like SIGTERM."""
    c = "sighup"
    g = ents["genes"][7]
    if not hasattr(__import__("signal"), "SIGHUP"):
        check(c, "no SIGHUP on this system", True)
        return
    res, _ = run(view, {"entities": {g["entity_id"]: [dict(good()[0], signal="SIGHUP")] + good()[1:]}},
                 only=g["entity_id"], verify="ids")
    st = {r["entity_id"]: r["status"] for r in ledger(view)}
    check(c, "SIGHUP: exit code 129, the running entity paused (the process not killed)",
          res.exit_code == 129 and st == {g["entity_id"]: "paused"}, f"exit {res.exit_code}; {st}")
    reset(view, c)


@case
def key_prompt_ctrl_c(view, ents):
    """keys_state#2: the key prompt runs in the main thread without holding the pool lock; Ctrl-C there ends the
    prompt at once (getpass restores the terminal in its finally) and the run stops cleanly."""
    c = "key_prompt_ctrl_c"
    g = ents["genes"][0]
    seen = {}

    def prompt(text):
        import signal as S
        import threading
        seen["main"] = threading.current_thread() is threading.main_thread()
        try:
            S.raise_signal(S.SIGINT)               # (Ctrl-C; os.kill(own pid) would end the process on Windows)
            t1 = time.time() + 5
            while time.time() < t1:                    # a getpass waiting for input
                time.sleep(0.05)
            seen["timed_out"] = True
            return ""
        finally:
            seen["restored"] = True                    # (getpass restores the terminal here)
    t0 = time.time()
    res, _ = run(view, F.FakeAPI({"keys": [KEY1], "dead_keys": {KEY1[-4:]: 401}, "entities": {}}),
                 only=g["entity_id"], interactive=True, prompt=prompt, verify="ids")
    took = time.time() - t0
    ks = json.load(open(os.path.join(view, "review", "keys_state.json"), encoding="utf-8"))
    check(c, "asked in the main thread; Ctrl-C interrupts the prompt at once (no hang) and works like Enter there: "
          "the run pauses for a key (exit code 3, the add-a-key message)",
          seen.get("main") and seen.get("restored") and not seen.get("timed_out") and took < 4
          and res.exit_code == 3 and res.paused and "add a key" in res.message
          and [k["dead"] for k in ks["keys"]] == [True]
          and [r["status"] for r in ledger(view)] == ["key_rotated"],
          {"seen": seen, "took": round(took, 1), "exit": res.exit_code, "message": res.message[:120]})
    pool = K.KeyPool(env=False, interactive=True, default_chain=False, prompt=lambda t: (pool.describe(), "")[1])
    try:
        pool.current()
        ok = False
    except K.AllKeysDead:
        ok = True
    check(c, "describe() works while a prompt is open (the pool lock is not held)", ok)
    reset(view, c)


@case
def ledger_cut_line(work):
    """keys_state#3: a cut last line does not swallow the next line; an old glued line is recovered."""
    c = "ledger_cut_line"
    d = os.path.join(work, "ledger_cut")
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, "review"))
    led = Ledger(d)
    led.append({"entity_id": "gene:1", "status": "done", "cost_usd": 1.0})
    with open(led.path, "a", encoding="utf-8") as fh:
        fh.write('{"entity_id": "gene:2", "status": "do')            # a write cut short (disk full, a kill)
    led.append({"entity_id": "gene:3", "status": "done", "cost_usd": 2.0})
    st = led.states()
    check(c, "after a cut line the next line is kept (newline guard)", set(st) == {"gene:1", "gene:3"}
          and st["gene:3"]["cost_usd"] == 2.0, sorted(st))
    with open(led.path, "a", encoding="utf-8") as fh:
        fh.write('{"entity_id": "gene:4", "sta{"entity_id": "gene:5", "status": "done", "cost_usd": 3.0}\n')
    check(c, "a whole line glued to a cut one (an older file) is recovered", set(led.states()) ==
          {"gene:1", "gene:3", "gene:5"}, sorted(led.states()))
    shutil.rmtree(d, ignore_errors=True)


@case
def run_lock(work):
    """keys_state#4: the run lock holds pid, host and process start time; a lock whose process is gone (or whose
    pid is now another process) is stale and removed, a live one is refused with the lock's path."""
    c = "run_lock"
    d = os.path.join(work, "lock_out")
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, "review"))
    lp = os.path.join(d, "review", ".run.lock")
    p = subprocess.Popen([sys.executable, "-c", "pass"])
    p.wait()
    with open(lp, "w", encoding="utf-8") as fh:
        json.dump({"pid": p.pid, "host": socket.gethostname(), "started": "x"}, fh)
    lk = R._RunLock(d)
    ok, why = lk.acquire()
    rec = json.load(open(lp, encoding="utf-8")) if ok else {}
    lk.release()
    check(c, "a lock whose process is gone is removed; the new lock holds pid, host, process start",
          ok and rec.get("pid") == os.getpid() and rec.get("host") == socket.gethostname()
          and isinstance(rec.get("process_start"), float), (ok, why, rec))
    live = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    try:
        time.sleep(0.2)
        ps = R._proc_start(live.pid)
        with open(lp, "w", encoding="utf-8") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x", "process_start": ps}, fh)
        ok2, why2 = R._RunLock(d).acquire()
        with open(lp, "w", encoding="utf-8") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x",
                       "process_start": (ps or 0) - 3600}, fh)
        lk3 = R._RunLock(d)
        ok3, why3 = lk3.acquire()
        lk3.release()
        with open(lp, "w", encoding="utf-8") as fh:
            json.dump({"pid": live.pid, "host": "some-other-computer", "started": "x"}, fh)
        ok4, why4 = R._RunLock(d).acquire()
    finally:
        live.kill()
        live.wait()
    check(c, "a live run's lock is refused, naming the lock file; a reused pid (younger process) is stale; "
             "another computer's lock is refused", not ok2 and lp in why2 and ok3 and not ok4
          and "another computer" in why4, [why2, why3, why4])
    check(c, "_alive: False for a finished process, True for this one", not R._alive(p.pid) and R._alive(os.getpid()))
    shutil.rmtree(d, ignore_errors=True)


@case
def keys_file_is_a_key(view, ents):
    """keys_state#10: a key given to --keys-file is refused without being shown (also through the CLI)."""
    c = "keys_file_is_a_key"
    g = ents["genes"][0]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        res, fk = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], keys_file=KEY5,
                      quiet=False)
    printed = buf.getvalue()
    sys.stdout.write(K.scrub(printed))
    check(c, "refused (exit 2), nothing sent, the message says it looks like a key and does not show it",
          res.exit_code == 2 and not fk.calls and "looks like an API key" in res.message and KEY5 not in res.message
          and KEY5 not in printed and KEY5[8:30] not in printed, res.message[:160])
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC")}
    sp = os.path.join(view, "script.json")
    with open(sp, "w", encoding="utf-8") as fh:
        json.dump({"entities": {}}, fh)
    r = subprocess.run([sys.executable, "-m", "tahoemap", "review", "run", "--out", view, "--only", g["entity_id"],
                        "--limit", "1", "--fake", sp, "--keys-file", "/home/someone/" + KEY5], cwd=REPO, env=env,
                       capture_output=True, text=True, timeout=120)
    os.remove(sp)
    SCANNED["bytes"] += len(r.stdout) + len(r.stderr)
    logs = "".join(open(f, encoding="utf-8", errors="replace").read() for f in glob.glob(
        os.path.join(view, "review", "*.log")))
    check(c, "CLI: exit 2, the key in neither the output nor review.log", r.returncode == 2
          and KEY5 not in r.stdout + r.stderr + logs and "looks like an API key" in r.stdout,
          f"exit {r.returncode}: {K.scrub(r.stdout[-200:])}")
    outs = []
    for kf in ([] if os.name == "nt" else (["--keys-file", KEY5], ["--keys-file=" + KEY5],
                                           ["--background", "--keys-file", KEY5])):    # (the bash wrapper)
        w = subprocess.run(["bash", os.path.join(REPO, "tahoe"), "review", "run", "--out", view, "--limit", "1"] + kf,
                           cwd=view, env=env, capture_output=True, text=True, timeout=120)
        SCANNED["bytes"] += len(w.stdout) + len(w.stderr)
        outs.append((w.returncode, w.stdout + w.stderr))
    check(c, "the tahoe wrapper refuses it before anything runs (also --background), without echoing it",
          all(rc == 1 and KEY5 not in o and KEY5[8:30] not in o and "looks like an API key" in o for rc, o in outs)
          and not os.path.exists(os.path.join(view, "console.log")), [(rc, K.scrub(o)[:90]) for rc, o in outs])
    # the same key given to --fake: refused, in neither the output nor review.log (no traceback through the run log)
    r = subprocess.run([sys.executable, "-m", "tahoemap", "review", "run", "--out", view, "--limit", "1", "--fake",
                        KEY5], cwd=REPO, env=env, capture_output=True, text=True, timeout=120)
    SCANNED["bytes"] += len(r.stdout) + len(r.stderr)
    logs = "".join(open(f, encoding="utf-8", errors="replace").read() for f in glob.glob(
        os.path.join(view, "review", "*.log")))
    res2 = R.run(view, fake=KEY5, only=g["entity_id"], limit=1, env_keys=False, interactive=False, quiet=True)
    res3 = R.run(view, fake=os.path.join(view, "no-such-script.json"), only=g["entity_id"], limit=1, env_keys=False,
                 interactive=False, quiet=True)
    check(c, "--fake KEY (CLI): exit 2, refused as a key, the key in neither the output nor review.log; a missing "
          "script: exit 2 with its path", r.returncode == 2 and KEY5 not in r.stdout + r.stderr + logs
          and KEY5[8:30] not in r.stdout + r.stderr + logs and "looks like an API key" in r.stdout
          and "Traceback" not in r.stdout + r.stderr + logs and res2.exit_code == 2 and KEY5 not in res2.message
          and res3.exit_code == 2 and "no-such-script.json" in res3.message,
          {"exit": r.returncode, "out": K.scrub(r.stdout[-160:] + r.stderr[-160:]), "missing": res3.message[:120]})
    outs = []
    for kf in ([] if os.name == "nt" else (["--fake", KEY5], ["--fake=" + KEY5])):     # (the bash wrapper)
        w = subprocess.run(["bash", os.path.join(REPO, "tahoe"), "review", "run", "--out", view, "--limit", "1"] + kf,
                           cwd=view, env=env, capture_output=True, text=True, timeout=120)
        SCANNED["bytes"] += len(w.stdout) + len(w.stderr)
        outs.append((w.returncode, w.stdout + w.stderr))
    check(c, "the tahoe wrapper refuses a key given to --fake too, without echoing it",
          all(rc == 1 and KEY5 not in o and KEY5[8:30] not in o and "--fake expects" in o for rc, o in outs),
          [(rc, K.scrub(o)[:90]) for rc, o in outs])
    reset(view, c)


@case
def systematic_failures(view, ents):
    """keys_state#1: the same error on 5 entities in a row stops the run (exit 4) instead of failing the whole
    queue, and those failures are not counted; --retry-failed retries entities left alone after 3 failures."""
    c = "systematic_failures"
    six = ents["genes"][:6]
    sc = {"entities": {e["entity_id"]: [{"error": 404}] for e in six}}
    res, fk = run(view, sc, only=[e["entity_id"] for e in six], concurrency=1, verify="ids")
    L = ledger(view)
    failed = [r["entity_id"] for r in L if r["status"] == "failed"]
    notes = [r["entity_id"] for r in L if r.get("uncount_failed")]
    st = Ledger(view).states()
    check(c, "the same 404 on 5 entities in a row: the run stops (exit 4), the 6th is not started",
          res.exit_code == 4 and len(failed) == 5 and six[5]["entity_id"] not in st and "same error" in res.message
          and len(fk.calls) == 5, f"exit {res.exit_code}; {len(failed)} failed; {res.message[:120]}")
    check(c, "those failures are not counted against the entities (ledger notes; n_failed 0)",
          sorted(notes) == sorted(failed) and all(st[e]["n_failed"] == 0 and st[e]["status"] == "failed"
                                                  for e in failed), {e: st[e]["n_failed"] for e in failed})
    res2, _ = run(view, {"entities": {e["entity_id"]: good() for e in six}}, only=[e["entity_id"] for e in six],
                  concurrency=2, verify="ids")
    check(c, "fixed: the next run reviews all 6", res2.counts == {"done": 6}, res2.counts)
    reset(view, c)
    # not fixed: the next run stops again; the 5 that stopped the first one do not count toward it (5 others do)
    many = ents["genes"][:8] + ents["drugs"][:4]
    ids = [e["entity_id"] for e in many]
    sc = {"entities": {e: [{"error": 404}] for e in ids}}
    res, fk = run(view, sc, only=ids, concurrency=1, verify="ids")
    first = {r["entity_id"] for r in ledger(view) if r["status"] == "failed"}
    res2, fk2 = run(view, sc, only=ids, concurrency=1, verify="ids")
    st = Ledger(view).states()
    failed2 = [r["entity_id"] for r in ledger(view)[len(first) * 2:] if r["status"] == "failed"]
    check(c, "the cause not fixed: the next run stops too, after 5 entities that had not stopped a run; none counted",
          res.exit_code == res2.exit_code == 4 and len(fk.calls) == 5 and len(fk2.calls) == 10
          and set(failed2) >= first and all(st[e]["n_failed"] == 0 for e in failed2)
          and "5 of these had stopped an earlier run" in res2.message,
          {"exit": (res.exit_code, res2.exit_code), "calls": (len(fk.calls), len(fk2.calls)),
           "n_failed": sorted({st[e]["n_failed"] for e in failed2}), "message": res2.message[-140:]})
    reset(view, c)
    # an error that is the entities' own (413 on 5 entities at the head of the queue): one run stops, the next goes
    # on past them and counts their failures; after 3 they are left alone
    five, healthy = ents["genes"][:5], ents["genes"][5:8]
    ids = [e["entity_id"] for e in five + healthy]
    sc = {"entities": {**{e["entity_id"]: [{"error": 413}] for e in five},
                       **{e["entity_id"]: good() for e in healthy}}}
    codes, nf = [], []
    for _i in range(4):
        res, fk = run(view, sc, only=ids, concurrency=1, verify="ids")
        st = Ledger(view).states()
        codes.append(res.exit_code)
        nf.append([st[e["entity_id"]]["n_failed"] for e in five])
    res5, fk5 = run(view, sc, only=ids, concurrency=1, verify="ids")
    check(c, "the same 413 on 5 entities of their own: the first run stops, the next reviews the others and counts "
          "the 5 failures; they are left alone after 3",
          codes == [4, 0, 0, 0] and nf == [[0] * 5, [1] * 5, [2] * 5, [3] * 5]
          and all(st[e["entity_id"]]["status"] == "done" for e in healthy) and not fk5.calls
          and res5.exit_code == 0 and res5.message == "nothing to do",
          {"exit codes": codes, "n_failed": [x[0] for x in nf], "5th run calls": len(fk5.calls)})
    res, fk = run(view, sc, only=ids, concurrency=1, verify="ids", retry_failed=True)
    check(c, "--retry-failed then tries the 5 again without stopping the run", res.exit_code == 0
          and res.counts == {"failed": 5} and len(fk.calls) == 5, {"exit": res.exit_code, "counts": res.counts})
    reset(view, c)
    # after an answer in this run, the same error on 5 entities in a row is theirs: counted, the run goes on
    six = ents["genes"][:7]
    sc = {"entities": {six[0]["entity_id"]: good(), six[6]["entity_id"]: good(),
                       **{e["entity_id"]: [{"error": 413}] for e in six[1:6]}}}
    res, fk = run(view, sc, only=[e["entity_id"] for e in six], concurrency=1, verify="ids")
    st = Ledger(view).states()
    check(c, "after an entity of this run got its answer: 5 failures in a row do not stop the run, and count",
          res.exit_code == 0 and res.counts == {"done": 2, "failed": 5}
          and all(st[e["entity_id"]]["n_failed"] == 1 for e in six[1:6]),
          {"exit": res.exit_code, "counts": res.counts})
    reset(view, c)
    g = six[0]
    for err in (400, 413, 400):
        run(view, {"entities": {g["entity_id"]: [{"error": err}]}}, only=g["entity_id"], verify="ids")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        res3, fk3 = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids",
                        quiet=False)
    sys.stdout.write(buf.getvalue())
    res4, fk4 = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids",
                    retry_failed=True)
    check(c, "after 3 failures it is left alone (the message names --retry-failed); --retry-failed reviews it",
          not fk3.calls and "--retry-failed" in buf.getvalue() and res4.counts == {"done": 1},
          {"left alone": not fk3.calls, "retry": res4.counts})
    reset(view, c)


def _sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest() if os.path.exists(path) else None


@case
def recheck_stopped(view, ents):
    """core#1: a --recheck stopped before its citation check finished - by --max-usd, by its last key dying, by a
    signal between two checker turns - leaves the stored review and note as they were: no done line, a 'recheck:
    paused' ledger note with its cost, the entity still --recheck-able; an unstopped --recheck then completes it."""
    c = "recheck_stopped"
    g = ents["genes"][3]
    run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids")
    rp = R.review_paths(view, "gene", g["name"])
    grace = R.STOP_GRACE
    R.STOP_GRACE = 0.5
    try:
        for label, script, kw, code in [
                ("--max-usd reached after the checker's first turn",
                 {"checker": {g["name"]: [{"end_turn": "checking"}, {"submit_check": "auto"}]}}, {"max_usd": 0.001}, 0),
                ("no key left (the only key dies at the checker)",
                 {"keys": [KEY1], "dead_keys": {KEY1[-4:]: 402}, "checker": "auto"}, {}, 3),
                ("SIGINT between two checker turns (the answer within the grace)",
                 {"checker": {g["name"]: [{"end_turn": "checking", "signal": "SIGINT"}, {"submit_check": "auto"}]}},
                 {}, 130)]:
            n0 = len(ledger(view))
            before = (_sha(rp["review"]), _sha(rp["note"]))
            res, fk = run(view, script, only=g["entity_id"], verify="llm", recheck=True, **kw)
            new = ledger(view)[n0:]
            st = Ledger(view).states()[g["entity_id"]]
            meta = json.load(open(rp["review"], encoding="utf-8")).get("meta") or {}
            check(c, f"{label}: exit {code}; the review and note unchanged; only a 'recheck: paused' note; still "
                  "--recheck-able", res.exit_code == code and (_sha(rp["review"]), _sha(rp["note"])) == before
                  and [(r["status"], r.get("note"), r.get("recheck")) for r in new] == [("note", "recheck: paused",
                                                                                        True)]
                  and st["status"] == "done" and R.recheck_pending(view, st, "llm") and not meta.get("rechecked")
                  and {x["role"] for x in fk.calls} == {"checker"},
                  {"exit": res.exit_code, "new lines": [(r["status"], r.get("note"), r.get("cost_usd")) for r in new],
                   "unchanged": (_sha(rp["review"]), _sha(rp["note"])) == before, "rechecked": meta.get("rechecked")})
    finally:
        R.STOP_GRACE = grace
    res, fk = run(view, {"checker": "auto"}, only=g["entity_id"], verify="llm", recheck=True)
    rv = json.load(open(rp["review"], encoding="utf-8"))
    check(c, "then a --recheck that is not stopped completes the check (a done line)", res.exit_code == 0
          and rv["verification"]["llm"]["status"] == "done" and rv["meta"].get("rechecked")
          and ledger(view)[-1]["status"] == "done", {"exit": res.exit_code, "llm": rv["verification"]["llm"]})
    reset(view, c)


@case
def breaker_network(view, ents):
    """core#2: network failures (one signature, whichever class: connection errors, timeouts ...) and back-offs that
    run out are the run's, never one entity's: 5 entities in a row stop the run (exit 4, uncounted) also after an
    entity of the run got its answer, and the next run with the network still down stops after 5 again."""
    c = "breaker_network"
    pool = ents["genes"][:8] + ents["drugs"][:6]
    ids = [e["entity_id"] for e in pool]
    cases = [("connection errors after an answer", lambda i: good() if i == 0 else [{"error": "connection"}] * 3, 1),
             ("timeouts after an answer", lambda i: good() if i == 0 else [{"error": "timeout"}] * 3, 1),
             ("connection errors and timeouts in turn, before any answer",
              lambda i: [{"error": "connection" if i % 2 else "timeout"}] * 3, 0)]
    for label, steps, n_done in cases:
        sc = {"entities": {e: steps(i) for i, e in enumerate(ids)}}
        res, fk = run(view, sc, only=ids, concurrency=1, verify="ids")
        L = ledger(view)
        st = Ledger(view).states()
        failed = [r["entity_id"] for r in L if r["status"] == "failed"]
        notes = [r["entity_id"] for r in L if r.get("uncount_failed")]
        est = [r["entity_id"] for r in L if r.get("estimated_usd")]
        check(c, f"{label}: the run stops after 5 failures (exit 4), not counted, the rest not started",
              res.exit_code == 4 and len(failed) == 5 and sorted(notes) == sorted(failed)
              and all(st[e]["n_failed"] == 0 for e in failed) and len(st) == 5 + n_done
              and res.counts == ({"done": 1, "failed": 5} if n_done else {"failed": 5})
              and len(fk.calls) == 3 * n_done + 15 and set(est) <= set(failed)
              and "(network)" in res.message and "not counted" in res.message,
              {"exit": res.exit_code, "counts": res.counts, "calls": len(fk.calls), "message": res.message[:110]})
        if n_done == 0:
            res2, fk2 = run(view, sc, only=ids, concurrency=1, verify="ids")
            st2 = Ledger(view).states()
            check(c, "the network still down: the next run stops after 5 again (network failures always count "
                  "toward a stop), none counted", res2.exit_code == 4 and len(fk2.calls) == 15
                  and all(s["n_failed"] == 0 for s in st2.values()),
                  {"exit": res2.exit_code, "calls": len(fk2.calls)})
        reset(view, c)
    waits = R.MAX_WAITS
    R.MAX_WAITS = 1
    try:
        sc = {"entities": {e: (good() if i == 0 else [{"error": 529}] * 2) for i, e in enumerate(ids)}}
        res, fk = run(view, sc, only=ids, concurrency=1, verify="ids")
    finally:
        R.MAX_WAITS = waits
    st = Ledger(view).states()
    check(c, "overload that outlasts the back-offs on 5 entities after an answer: the run stops too (exit 4)",
          res.exit_code == 4 and res.counts == {"done": 1, "failed": 5} and len(st) == 6
          and all(s["n_failed"] == 0 for s in st.values()) and "back-offs" in res.message,
          {"exit": res.exit_code, "counts": res.counts, "message": res.message[:110]})
    reset(view, c)


@case
def breaker_waits_for_running(view, ents):
    """core#3: 5 fast failures of the entities' own (413) while a slow healthy review is running: no new entity
    starts, the run waits for it, and its answer shows that the API works - the run goes on, the review is done (not
    paused), the 5 failures count; when the running one fails too without an answer, the run stops (exit 4)."""
    c = "breaker_waits_for_running"
    six = ents["genes"][:6]
    ids = [e["entity_id"] for e in six]
    grace = R.STOP_GRACE
    R.STOP_GRACE = 1.0
    try:
        slow = [dict(good()[0], sleep=1.5)] + good()[1:]
        sc = {"entities": {ids[0]: slow, **{e: [{"error": 413}] for e in ids[1:]}}}
        res, fk = run(view, sc, only=ids, concurrency=2, verify="ids")
    finally:
        R.STOP_GRACE = grace
    st = Ledger(view).states()
    t413 = [x.get("t1", 0) for x in fk.calls if x["step"] == "error:413"]
    t_ok = min((x.get("t1", 0) for x in fk.calls if x["entity"] == ids[0]), default=0)
    check(c, "the healthy review's answer comes after the 5th failure: the run goes on, the review done, the 5 "
          "failures counted", res.exit_code == 0 and res.counts == {"done": 1, "failed": 5}
          and st[ids[0]]["status"] == "done" and all(st[e]["n_failed"] == 1 for e in ids[1:])
          and not any(r.get("uncount_failed") for r in ledger(view)) and len(t413) == 5 and max(t413) < t_ok,
          {"exit": res.exit_code, "counts": res.counts, "413s done before the answer": bool(t413)
           and max(t413) < t_ok})
    reset(view, c)
    eight = ents["genes"][:8]
    ids = [e["entity_id"] for e in eight]
    sc = {"entities": {ids[0]: [{"error": 404, "sleep": 1.5}], **{e: [{"error": 404}] for e in ids[1:]}}}
    res, fk = run(view, sc, only=ids, concurrency=2, verify="ids")
    L = ledger(view)
    failed = [r["entity_id"] for r in L if r["status"] == "failed"]
    notes = [r["entity_id"] for r in L if r.get("uncount_failed")]
    check(c, "the running one fails too, without an answer: the run stops (exit 4), none started meanwhile, none "
          "counted", res.exit_code == 4 and len(failed) == 6 and ids[0] in failed and sorted(notes) == sorted(failed)
          and len(fk.calls) == 6 and "before the API had answered" in res.message,
          {"exit": res.exit_code, "failed": len(failed), "calls": len(fk.calls), "message": res.message[:100]})
    reset(view, c)


@case
def stopped_in_flight(view, ents):
    """core#4, e2e#10: a request in flight when a stopping run closes its attempt is charged an estimate (it may be
    billed); a response lost after the close is still recorded (a late error event, and a ledger note for what it
    costs beyond the estimate already charged)."""
    c = "stopped_in_flight"
    g = ents["genes"][4]
    grace = R.STOP_GRACE
    R.STOP_GRACE = 0.5
    try:
        first = dict(good()[0], signal="SIGINT", sleep_after=1.5, drop=True)
        res, fk = run(view, {"entities": {g["entity_id"]: [first] + good()[1:]}}, only=g["entity_id"], verify="ids")
        time.sleep(2.0)                                 # the stream breaks after the run has ended
    finally:
        R.STOP_GRACE = grace
    L = ledger(view)
    ev = events(view, L[0]) if L else []
    kinds = [e["event"] for e in ev]
    infl = [i for i, e in enumerate(ev) if e["event"] == "error" and e.get("class") == "InFlightAtStop"]
    est = float(L[0].get("estimated_usd") or 0) if L else 0.0
    check(c, "in flight at the close: the paused line is charged an estimate (estimated_usd), the history has an "
          "InFlightAtStop error event before its end", res.exit_code == 130 and [r["status"] for r in L] == ["paused"]
          and est > 0 and abs(L[0]["cost_usd"] - est) < 1e-6 and len(infl) == 1 and infl[0] < kinds.index("end")
          and abs(ev[infl[0]]["estimated_cost_usd"] - est) < 1e-6,
          {"exit": res.exit_code, "ledger": [(r["status"], r.get("cost_usd"), r.get("estimated_usd")) for r in L],
           "events": kinds})
    check(c, "the response lost after the close: a late error event after the end, not charged twice",
          kinds and kinds[-1] == "error" and ev[-1].get("late") and ev[-1].get("estimated_cost_usd") == 0
          and abs(ev[-1].get("estimated_at_close_usd", 0) - est) < 1e-6 and len(L) == 1, ev[-1] if ev else None)
    reset(view, c)

    class Retrying(F.FakeAPI):                          # an SDK that re-sends once itself (as the real client does)
        def client(self, secret):
            return super().client(secret).with_options(max_retries=1)
    R.STOP_GRACE = 0.5
    try:
        sc = Retrying({"entities": {g["entity_id"]: [{"error": "timeout", "signal": "SIGINT", "sleep_after": 1.0},
                                                     {"error": "timeout"}] + good()}})
        res, fk = run(view, sc, only=g["entity_id"], verify="ids")
        time.sleep(3.0)                                 # the SDK's re-send times out after the run has ended
    finally:
        R.STOP_GRACE = grace
    L = ledger(view)
    ev = events(view, L[0]) if L else []
    est0 = float(L[0].get("estimated_usd") or 0) if L else 0.0
    notes = [r for r in L if r.get("status") == "note"]
    check(c, "lost after the close, re-sent by the SDK (2 sends): a late ledger note for the estimate beyond the one "
          "charged at the close, and a late error event", [r["status"] for r in L] == ["paused", "note"]
          and est0 > 0 and notes[0].get("late") and abs(notes[0]["estimated_usd"] - est0) < 1e-6
          and abs(notes[0]["cost_usd"] - est0) < 1e-6 and len(fk.calls) == 2 and ev and ev[-1]["event"] == "error"
          and ev[-1].get("late") and ev[-1].get("estimated_sends") == 2,
          {"ledger": [(r["status"], r.get("cost_usd"), r.get("estimated_usd"), r.get("late")) for r in L],
           "calls": len(fk.calls), "last event": (ev[-1]["event"], ev[-1].get("late")) if ev else None})
    out = []
    R.status(view, say=out.append)
    check(c, "review status counts both estimates", any(R._fmt_usd(2 * est0) + " of it estimated" in x for x in out),
          [x for x in out if "Spent" in x])
    reset(view, c)


@case
def malformed_key(view, ents):
    """core#6: a request that could not even be written on this machine (an illegal header value, an unusable URL,
    the proxy refused it) never reached the API and is not charged; a malformed key (two keys in one variable) is
    dead from the start: nothing is sent, the run pauses for a key."""
    c = "malformed_key"
    import anthropic
    import httpx2
    req = httpx2.Request("POST", F.FAKE_BASE_URL + "/v1/messages")
    want = {"LocalProtocolError": False, "UnsupportedProtocol": False, "ProxyError": False, "ConnectError": False,
            "ConnectTimeout": False, "ReadError": True, "RemoteProtocolError": True, "ReadTimeout": True}
    got = {}
    for name in want:
        e = anthropic.APIConnectionError(request=req)
        e.__cause__ = getattr(httpx2, name)("fake: Illegal header value", request=req)
        cat, info = K.classify(e)
        got[name] = (cat == K.WAIT and info.get("network")) and info.get("sent")
    check(c, "local errors (illegal header, unsupported protocol, proxy) are 'never sent', unlike lost responses",
          got == want, got)
    g = ents["genes"][0]
    os.environ["ANTHROPIC_API_KEY"] = KEY3 + "\n" + KEY4
    try:
        res, fk = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids", env_keys=True)
    finally:
        os.environ.pop("ANTHROPIC_API_KEY", None)
    ks = json.load(open(os.path.join(view, "review", "keys_state.json"), encoding="utf-8"))
    check(c, "two keys in ANTHROPIC_API_KEY: the key is dead from the start (malformed), nothing sent, paused "
          "(exit 3)", res.exit_code == 3 and not fk.calls and "malformed" in res.message
          and [(k["dead"], "malformed" in k["reason"]) for k in ks["keys"]] == [(True, True)]
          and KEY3 not in res.message and KEY4 not in res.message,
          {"exit": res.exit_code, "calls": len(fk.calls), "message": K.scrub(res.message)[:120]})
    reset(view, c)


@case
def status_whole_queue(view, ents):
    """e2e#7: `review status` counts every entity, whatever the last `review plan --kinds/--only` wrote to
    queue.parquet."""
    c = "status_whole_queue"
    two = [e["entity_id"] for e in ents["genes"][:2]]
    run(view, {"entities": {e: good() for e in two}}, only=two, verify="ids")
    full = []
    R.status(view, say=full.append)
    outs = []
    for kw in ({"kinds": "line"}, {"only": ents["lines"][0]["entity_id"]}):
        R.plan(view, say=lambda *a: None, **kw)
        o = []
        R.status(view, say=o.append)
        outs.append(o)
    q = pd.read_parquet(os.path.join(view, "review", "queue.parquet"))
    check(c, "after a plan of one line, status is the same as before: every kind counted, nothing 'not in the "
          "queue', the projection over all the rest", len(q) == 1 and all(o == full for o in outs)
          and not any("not in the queue" in x for x in full)
          and any(ln.split()[:2] == ["gene", "2"] for x in full for ln in x.splitlines())
          and any(f"rest ({ents['n'] - 2:,} entities)" in x for x in full),
          {"queue rows": len(q), "same": [o == full for o in outs], "status": [x for x in full if "rest" in x]})
    reset(view, c)


@case
def projection_settings(view, ents):
    """e2e#8: the mean real cost replaces the estimate only for the model, effort and --verify mode the reviews ran
    with; the ledger lines record effort and verify."""
    c = "projection_settings"
    ids = [e["entity_id"] for e in ents["genes"][:3]]
    run(view, {"entities": {e: good() for e in ids}}, only=ids, verify="ids")
    mean = sum(float(r["cost_usd"]) for r in ledger(view)) / 3

    def gene_line(**kw):
        out = []
        R.plan(view, kinds="gene", say=out.append, **kw)
        return next((x for x in out if x.strip().startswith("gene:")), "")
    same = gene_line(verify="ids")
    others = [gene_line(verify="ids", model="claude-fable-5-1"), gene_line(), gene_line(verify="ids", effort="low")]
    check(c, "same settings: the mean real cost of the 3 reviews; another model, --verify or effort: the estimate "
          "(and how many reviews were left out)", "mean real cost of 3 genes reviewed with these settings" in same
          and f"~{R._fmt_usd(mean)} " in same
          and all("estimate from the dossier size" in x and "3 genes were reviewed with another" in x for x in others),
          [same] + others)
    check(c, "every attempt's ledger line records the reviewer's effort and the --verify mode",
          all(r.get("effort") == "high" and r.get("verify") == "ids" for r in ledger(view)),
          [(r.get("effort"), r.get("verify")) for r in ledger(view)])
    reset(view, c)


@case
def stop_foreground(view, ents):
    """e2e#9: `tahoe stop` also stops a `tahoe review run` in the foreground of another terminal (found through
    review/.run.lock), as SIGTERM: exit code 143, the running entity paused."""
    c = "stop_foreground"
    import threading
    if os.name == "nt":
        check(c, "the tahoe wrapper (bash) is not used on Windows: `review stop` is (windows_file_locks)", True)
        return
    g = ents["genes"][5]
    env = {k: v for k, v in os.environ.items() if not k.startswith("ANTHROPIC")}
    sp = os.path.join(view, "script.json")
    with open(sp, "w", encoding="utf-8") as fh:
        json.dump({"entities": {g["entity_id"]: [dict(good()[0], sleep=4)] + good()[1:]}}, fh)
    p = subprocess.Popen([sys.executable, "-m", "tahoemap", "review", "run", "--out", view, "--only", g["entity_id"],
                          "--limit", "1", "--fake", sp, "--verify", "ids"], cwd=REPO, env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    got = {}
    t = threading.Thread(target=lambda: got.update(out=p.communicate()[0]), daemon=True)   # (reaped at once)
    t.start()
    t0 = time.time()
    while not glob.glob(os.path.join(view, "review", "history", "gene", "*", "*.jsonl")) and time.time() - t0 < 60:
        time.sleep(0.1)
    time.sleep(0.3)
    w = subprocess.run(["bash", os.path.join(REPO, "tahoe"), "stop", "--out", view], env=env, capture_output=True,
                       text=True, timeout=200)
    t.join(60)
    w2 = subprocess.run(["bash", os.path.join(REPO, "tahoe"), "stop", "--out", view], env=env, capture_output=True,
                        text=True, timeout=60)
    os.remove(sp)
    SCANNED["bytes"] += len(w.stdout) + len(w.stderr) + len(got.get("out") or "")
    check(c, "tahoe stop: the foreground review found and stopped (exit 143, the entity paused); then 'Nothing is "
          "running.'", w.returncode == 0 and "foreground" in w.stdout and "Stopped." in w.stdout
          and p.returncode == 143 and [r["status"] for r in ledger(view)] == ["paused"]
          and w2.returncode == 0 and "Nothing is running." in w2.stdout,
          {"stop": (w.returncode, w.stdout[:90]), "review exit": p.returncode,
           "ledger": [r["status"] for r in ledger(view)], "again": w2.stdout.strip()})
    reset(view, c)


# ----------------------------------------------------------------------------- Windows fixes (file locks, stop)
@case
def windows_file_locks(view, ents):
    """W-REV-1 / W-REV-4 (Windows, where a file another program has open cannot be replaced and Excel can hold the
    ledger; simulated with PermissionError): a review that cannot be stored is a 'failed' ledger line with the review
    kept in its history's end event - never an attempt that vanishes; a store refused once is tried again; ledger
    lines that cannot be written wait (in order) and are written later, or - when the ledger stays held - go to
    ledger.unwritten.jsonl, read as part of the ledger and moved into it by the next run; `review stop` stops a
    running review through review/.stop (exit 143, the entity paused); a review run refuses while a pipeline command
    holds OUT/.pipeline.lock."""
    import threading
    c = "windows_file_locks"
    g, g2, g3 = ents["genes"][0], ents["genes"][1], ents["genes"][2]
    real_write, real_retry, real_append, waits = R.write_json, R.retry_io, H.append_line, R.LEDGER_WAITS
    R.retry_io = lambda fn: real_retry(fn, waits=(0.0, 0.0))
    R.LEDGER_WAITS = (0.0,)
    refused = {"n": 0, "max": 0}

    def write_json(obj, path):
        if os.sep + "reviews" + os.sep in path and refused["n"] < refused["max"]:
            refused["n"] += 1
            raise PermissionError(13, "Access is denied", path)
        return real_write(obj, path)
    try:
        R.write_json = write_json
        refused.update(n=0, max=99)
        res, _ = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids")
        L = ledger(view)
        end = next((e for e in reversed(events(view, L[-1])) if e.get("event") == "end"), {}) if L else {}
        kept = (end.get("unstored_review") or {}).get("meta") or {}
        check(c, "a review that cannot be stored: a 'failed' line saying so (retried next run), the review kept in "
              "the history's end event; nothing on disk", res.exit_code == 0 and [r["status"] for r in L] == ["failed"]
              and "could not store the review" in (L[-1].get("error") or "") and L[-1].get("store_failed")
              and kept.get("entity_id") == g["entity_id"] and (end.get("unstored_review") or {}).get("summary")
              and not os.path.exists(R.review_paths(view, "gene", g["name"])["review"])
              and Ledger(view).states()[g["entity_id"]]["status"] == "failed",
              {"exit": res.exit_code, "ledger": [(r["status"], (r.get("error") or "")[:70]) for r in L]})
        reset(view, c)
        refused.update(n=0, max=1)
        res, _ = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids")
        check(c, "a store refused once (an antivirus or sync tool holding the file) is tried again: done",
              [r["status"] for r in ledger(view)] == ["done"] and refused["n"] == 1
              and os.path.exists(R.review_paths(view, "gene", g["name"])["review"]), refused)
        reset(view, c)
    finally:
        R.write_json = real_write
    lp = os.path.join(view, "review", "ledger.jsonl")
    held = {"n": 0, "max": 0}

    def append_line(path, rec):
        if path == lp and held["n"] < held["max"]:
            held["n"] += 1
            raise PermissionError(13, "The process cannot access the file because it is being used by another "
                                      "process", path)
        return real_append(path, rec)
    try:
        H.append_line = append_line
        held.update(n=0, max=1)
        res, _ = run(view, {"entities": {g["entity_id"]: good(), g2["entity_id"]: good()}},
                     only=f"{g['entity_id']},{g2['entity_id']}", verify="ids", concurrency=1)
        L = ledger(view)
        check(c, "a ledger line that cannot be written for a moment waits and is written with the next, in order",
              [(r["entity_id"], r["status"]) for r in L] == [(g["entity_id"], "done"), (g2["entity_id"], "done")]
              and held["n"] == 1, [(r["entity_id"], r["status"]) for r in L])
        reset(view, c)
        held.update(n=0, max=10 ** 6)
        res, _ = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids")
        un = os.path.join(view, "review", "ledger.unwritten.jsonl")
        spilled = read_jsonl(un)
        st = Ledger(view).states().get(g["entity_id"]) or {}
        held.update(max=0)
        res2, _ = run(view, {"entities": {g3["entity_id"]: good()}}, only=g3["entity_id"], verify="ids")
        L = read_jsonl(lp)
        check(c, "a ledger held for the whole run (Excel): its lines go to ledger.unwritten.jsonl, counted as the "
              "ledger (status done); the next run moves them into ledger.jsonl",
              [r["status"] for r in spilled] == ["done"] and st.get("status") == "done" and not os.path.exists(un)
              and [(r["entity_id"], r["status"]) for r in L] == [(g["entity_id"], "done"), (g3["entity_id"], "done")],
              {"spilled": len(spilled), "state": st.get("status"), "after": [r["entity_id"] for r in L]})
        reset(view, c)
    finally:
        H.append_line = real_append
        R.retry_io, R.LEDGER_WAITS = real_retry, waits
    # review stop: from another thread (another window, on Windows), through review/.stop
    got = {}
    t = threading.Thread(target=lambda: got.update(res=run(view, {"entities": {g2["entity_id"]: [
        dict(good()[0], sleep=3)] + good()[1:]}}, only=g2["entity_id"], verify="ids")[0]), daemon=True)
    t.start()
    t0 = time.time()
    while not glob.glob(os.path.join(view, "review", "history", "gene", "*", "*.jsonl")) and time.time() - t0 < 60:
        time.sleep(0.1)
    said = []
    code = R.stop_run(view, say=said.append, wait=90)
    t.join(60)
    res = got.get("res")
    check(c, "review stop: the running review stops as with Ctrl-C (exit 143, the entity paused), the stop file "
          "is gone, and it says so", code == 0 and res is not None and res.exit_code == 143
          and [r["status"] for r in ledger(view)] == ["paused"] and any("Stopped." in x for x in said)
          and not os.path.exists(os.path.join(view, "review", R.STOP_FILE)),
          {"exit": getattr(res, "exit_code", None), "ledger": [r["status"] for r in ledger(view)], "said": said[-1:]})
    reset(view, c)
    said = []
    R.stop_run(view, say=said.append, wait=1)
    check(c, "review stop with no run going on says so", said and "No review run" in said[0], said)
    live = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    pl = os.path.join(view, ".pipeline.lock")
    try:
        time.sleep(0.2)
        with open(pl, "w", encoding="utf-8") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x",
                       "process_start": R._proc_start(live.pid)}, fh)
        res, fk = run(view, {"entities": {g["entity_id"]: good()}}, only=g["entity_id"], verify="ids")
    finally:
        live.kill()
        live.wait()
        os.remove(pl)
    check(c, "a review run refuses (exit 2, nothing sent) while a pipeline command holds OUT/.pipeline.lock",
          res.exit_code == 2 and "pipeline command" in res.message and not fk.calls, res.message[:120])
    reset(view, c)


# ----------------------------------------------------------------------------- main
def pick_entities(view):
    e = D.entities(view)
    genes = e[(e["kind"] == "gene") & e["in_space"].fillna(False).astype(bool)].head(8).to_dict("records")
    return {"genes": genes, "lines": e[e["kind"] == "line"].to_dict("records"),
            "drugs": e[e["kind"] == "drug"].to_dict("records"), "n": len(e)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=os.environ.get("TAHOE_TEST_DIR", DEFAULT_WORKDIR))
    ap.add_argument("--out", default=None, help="a finished tahoemap output (default WORKDIR/out_seed0)")
    ap.add_argument("--keep", action="store_true", help="keep WORKDIR/review_view after the test")
    a = ap.parse_args()
    src = os.path.abspath(a.out or os.path.join(a.workdir, "out_seed0"))
    if not os.path.exists(os.path.join(src, "stages", "tables.json")):
        sys.exit(f"test_review.py needs a finished tahoemap output: {src} has none (run tests/run_tests.py first, "
                 "or give --out)")
    work = os.path.abspath(a.workdir)
    os.makedirs(work, exist_ok=True)
    tee = Tee(sys.stdout)
    sys.stdout = tee
    t0 = time.time()
    block_network()
    R.SLEEP = fake_sleep
    view = make_view(src, work)
    print(f"test_review.py: output {src} (read only), view {view}")
    ents = pick_entities(view)
    if len(ents["genes"]) < 6 or not ents["lines"]:
        sys.exit("test_review.py: the output needs at least 6 genes in the vector space and a cell line")
    classification()
    end_to_end(view, ents)
    pause_turn(view, ents)
    refusal(view, ents)
    nudges(view, ents)
    over_budget(view, ents)
    billing_rotation(view, ents)
    all_keys_dead(view, ents, work)
    rate_limit_backoff(view, ents)
    dry_run(view, ents)
    concurrency(view, ents)
    interrupt(view, ents)
    plan_status_cli(view, ents)
    vault_splice(work, src, ents)
    vault_map_literature(work, src, ents)
    duplicate(view, work, src)
    checker_sees_relation(work)
    indirect_needs_citations(work)
    doi_parentheses(work)
    retractions(work)
    retractions_shown(work, src, ents)
    vault_round5(work, src, ents)
    drug_dossier_trustworthy_dose(view, ents)
    cellosaurus_url_in_dossier(view, ents, work)
    note_provenance(work)
    note_citation_forms(work)
    note_links_and_structure(work, view, ents)
    check_status_contract(work)
    contract_end_to_end(view, ents)
    streaming_and_max_tokens(view, ents)
    transient_refusal(view, ents)
    empty_response(view, ents)
    lost_responses(view, ents)
    budget_lines(view, ents)
    stop_after_submit(view, ents)
    sighup(view, ents)
    key_prompt_ctrl_c(view, ents)
    ledger_cut_line(work)
    run_lock(work)
    keys_file_is_a_key(view, ents)
    systematic_failures(view, ents)
    recheck_stopped(view, ents)
    breaker_network(view, ents)
    breaker_waits_for_running(view, ents)
    stopped_in_flight(view, ents)
    malformed_key(view, ents)
    status_whole_queue(view, ents)
    projection_settings(view, ents)
    stop_foreground(view, ents)
    windows_file_locks(view, ents)
    for d in ("lit_ctx", "lit_ctx_down"):
        shutil.rmtree(os.path.join(work, d), ignore_errors=True)
    sys.stdout = tee.real
    printed = tee.buf.getvalue()
    leaked = [s[-4:] for s in SECRETS if s in printed]
    check("keys", "no API key in anything printed", not leaked, f"{len(printed):,} characters printed" if not
          leaked else f"keys ending {leaked}")
    check("keys", "files scanned for keys", SCANNED["files"] > 50, f"{SCANNED['files']} files, "
          f"{SCANNED['bytes'] / 1e6:.1f} MB")
    if not a.keep:
        shutil.rmtree(view, ignore_errors=True)
    n_fail = sum(1 for r in RESULTS if r[2] == "FAIL")
    print(f"\ntest_review.py: {len(RESULTS)} checks, {n_fail} failed, {time.time() - t0:.0f} s")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
