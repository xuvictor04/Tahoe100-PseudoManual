#!/usr/bin/env python3
"""test_review.py - the literature-review runner (tahoemap/review) against a scripted fake API: offline, no key.

    python3 tests/test_review.py [--out FINISHED_OUTPUT] [--workdir DIR] [--keep]

Needs a finished tahoemap output folder (tables, relations, graph ...): --out, else the one tests/run_tests.py leaves
in --workdir (default $TAHOE_TEST_DIR or /tmp/tahoemap_test)/out_seed0. That folder is only read: every case works
in DIR/review_view, whose entries are symbolic links to the output's own entries next to a fresh review/ folder.

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
and --retry-failed. And a crafted malicious review (raw
HTML, script, iframe, javascript: / data: / vbscript: links, a remote image, comments, an unclosed fence, a fabricated
PMID, a verdict the checker does not support, two verdicts on one partner) spliced into the vault and the map: the
note sanitised, unverified verdicts shown as such, one verdict per partner chosen alike in both, the callout's
verification from the counts, the generated footer, a stale connections.parquet; in a browser (Playwright, when
installed) the badges, a slow double-click that pins and a small simulation that animates the sign switch.
Prints PASS / FAIL per check; exit code 1 if anything fails. Takes well under a minute.
"""

import argparse
import contextlib
import glob
import hashlib
import io
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time
import traceback
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

import pandas as pd  # noqa: E402

from tahoemap import cli  # noqa: E402
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


def make_view(src, work):
    view = os.path.join(work, "review_view")
    if os.path.lexists(view):
        shutil.rmtree(view)
    os.makedirs(view)
    for e in sorted(os.listdir(src)):
        if e != "review":
            os.symlink(os.path.join(src, e), os.path.join(view, e))
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
    rv = json.load(open(rp)) if os.path.exists(rp) else {}
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
    nt = open(note[0]).read() if note else ""
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
    ks = json.load(open(os.path.join(view, "review", "keys_state.json")))
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
    with open(kf, "w") as fh:
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
    summ = json.load(open(os.path.join(d, "summary.json"))) if os.path.exists(os.path.join(d, "summary.json")) \
        else {}
    reqs = sorted(glob.glob(os.path.join(d, "*", "*.request.json")))
    doss = sorted(glob.glob(os.path.join(d, "*", "*.dossier.md")))
    check(c, "nothing sent, no ledger; 3 dossiers and first requests written",
          not fk.calls and not os.path.exists(os.path.join(view, "review", "ledger.jsonl"))
          and len(summ.get("entities", [])) == 3 and len(reqs) == 3 and len(doss) == 3,
          f"{len(fk.calls)} calls, {len(reqs)} requests, {len(doss)} dossiers")
    rq = json.load(open(reqs[0]))["request"] if reqs else {}
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
    with open(sp, "w") as fh:
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
    rec2 = json.load(open(os.path.join(dest, "duplicated_from.json")))
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    stamps = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(out, "stages", "*.json")))
    check(c, "duplicated_from.json: source, date, code commit, stage stamps",
          rec2["source"] == os.path.abspath(out) and rec2["date"] and rec2["code"]["commit"] == head
          and set(rec2["stages"]) == set(stamps) and len(stamps) >= 5,
          {k: rec2.get(k) for k in ("date",)} | {"stages": sorted(rec2["stages"])})
    clone_head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True)
    check(c, "--repo: the code repository cloned", clone_head.stdout.strip() == head
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
    with open(os.path.join(src, "vault", "genes", "NQO1.md"), "w") as fh:
        fh.write("# NQO1\n")
    os.makedirs(os.path.join(work, "elsewhere"), exist_ok=True)
    os.symlink(os.path.join(work, "elsewhere"), os.path.join(src, "atlas", "pseudobulk"))
    with contextlib.redirect_stdout(io.StringIO()):
        rec3 = cli.duplicate(src, dest)
    check(c, "temporary files left out, symbolic links kept as links",
          not os.path.exists(os.path.join(dest, "tensor", "R.npy.tmp")) and rec3["files"]["skipped"] == 1
          and os.path.islink(os.path.join(dest, "atlas", "pseudobulk")) and rec3["files"]["symlinks"] == 1,
          rec3["files"])
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
            os.symlink(os.path.join(src, e), os.path.join(sv, e))
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
    same_code = (json.load(open(os.path.join(src, "stages", "vault.json"))).get("version") == vault.VERSION
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
            os.symlink(os.path.join(src, e), os.path.join(sv, e))
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
            sn("> [```dataviewjs](javascript:x)\n> dv.paragraph(1)"), sn("<!-- c -->~~~\n<script>alert(3)</script>")]
    check(c, "ui#2: what a removal makes is neutralised: a fence at the start of a line (it would hide all that "
             "follows) is text, no %% comment, no nested plugin fence",
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
    js = json.load(open(rj))
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
                pg.goto("file://" + os.path.abspath(os.path.join(sv, "map", "gene_map.html")))
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
                    if re.search(r"citations were checked|were checked against PubMed", open(p).read(), re.I)]
    wn = open(os.path.join(rd, "skills", "writing-the-note", "SKILL.md")).read()
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
    rv = json.load(open(os.path.join(view, rec["review"]))) if rec.get("review") else {}
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
    rv = json.load(open(rp)) if rp and os.path.exists(rp) else {}
    ver = rv.get("verification") or {}
    check(c, "Ctrl-C during the citation check: the review is stored as done (ids checked, claims not run)",
          res.exit_code == 130 and [r["status"] for r in main] == ["done"]
          and main[-1].get("stopped_during_verification") and ver.get("ids", {}).get("status") == "done"
          and ver.get("llm", {}).get("status") == "not_run" and "not checked against the abstracts"
          in (rv.get("note_footer") or "") and glob.glob(os.path.join(view, "review", "notes", "gene", "*.md")),
          {"exit": res.exit_code, "ledger": [(r["status"], r.get("note")) for r in L], "llm": ver.get("llm")})
    ev = events(view, main[-1]) if main else []
    kinds = [e["event"] for e in ev]
    check(c, "the late response: a ledger note line with its cost, a late event after the history's end",
          len(late) == 1 and late[0]["cost_usd"] > 0 and "end" in kinds and kinds.index("end") < len(kinds) - 1
          and ev[-1].get("late") and ev[-1]["event"] == "response", {"late": late[:1], "events": kinds[-3:]})
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
    rv1 = json.load(open(rp)) if rp else {}
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
    rv2 = json.load(open(rp)) if rp else {}
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
            os.kill(os.getpid(), S.SIGINT)
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
    ks = json.load(open(os.path.join(view, "review", "keys_state.json")))
    check(c, "asked in the main thread; Ctrl-C interrupts the prompt at once (no hang), the run stops cleanly",
          seen.get("main") and seen.get("restored") and not seen.get("timed_out") and took < 4
          and res.exit_code in (3, 130) and [k["dead"] for k in ks["keys"]] == [True]
          and [r["status"] for r in ledger(view)] == ["key_rotated"],
          {"seen": seen, "took": round(took, 1), "exit": res.exit_code})
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
    with open(lp, "w") as fh:
        json.dump({"pid": p.pid, "host": socket.gethostname(), "started": "x"}, fh)
    lk = R._RunLock(d)
    ok, why = lk.acquire()
    rec = json.load(open(lp)) if ok else {}
    lk.release()
    check(c, "a lock whose process is gone is removed; the new lock holds pid, host, process start",
          ok and rec.get("pid") == os.getpid() and rec.get("host") == socket.gethostname()
          and isinstance(rec.get("process_start"), float), (ok, why, rec))
    live = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    try:
        time.sleep(0.2)
        ps = R._proc_start(live.pid)
        with open(lp, "w") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x", "process_start": ps}, fh)
        ok2, why2 = R._RunLock(d).acquire()
        with open(lp, "w") as fh:
            json.dump({"pid": live.pid, "host": socket.gethostname(), "started": "x",
                       "process_start": (ps or 0) - 3600}, fh)
        lk3 = R._RunLock(d)
        ok3, why3 = lk3.acquire()
        lk3.release()
        with open(lp, "w") as fh:
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
    with open(sp, "w") as fh:
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
    for kf in (["--keys-file", KEY5], ["--keys-file=" + KEY5], ["--background", "--keys-file", KEY5]):
        w = subprocess.run(["bash", os.path.join(REPO, "tahoe"), "review", "run", "--out", view, "--limit", "1"] + kf,
                           cwd=view, env=env, capture_output=True, text=True, timeout=120)
        SCANNED["bytes"] += len(w.stdout) + len(w.stderr)
        outs.append((w.returncode, w.stdout + w.stderr))
    check(c, "the tahoe wrapper refuses it before anything runs (also --background), without echoing it",
          all(rc == 1 and KEY5 not in o and KEY5[8:30] not in o and "looks like an API key" in o for rc, o in outs)
          and not os.path.exists(os.path.join(view, "console.log")), [(rc, K.scrub(o)[:90]) for rc, o in outs])
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


# ----------------------------------------------------------------------------- main
def pick_entities(view):
    e = D.entities(view)
    genes = e[(e["kind"] == "gene") & e["in_space"].fillna(False).astype(bool)].head(8).to_dict("records")
    return {"genes": genes, "lines": e[e["kind"] == "line"].to_dict("records"),
            "drugs": e[e["kind"] == "drug"].to_dict("records"), "n": len(e)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=os.environ.get("TAHOE_TEST_DIR", "/tmp/tahoemap_test"))
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
    drug_dossier_trustworthy_dose(view, ents)
    cellosaurus_url_in_dossier(view, ents, work)
    note_provenance(work)
    note_citation_forms(work)
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
