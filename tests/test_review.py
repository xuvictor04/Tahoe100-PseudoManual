#!/usr/bin/env python3
"""test_review.py - the literature-review runner (tahoemap/review) against a scripted fake API: offline, no key.

    python3 tests/test_review.py [--out FINISHED_OUTPUT] [--workdir DIR] [--keep]

Needs a finished tahoemap output folder (tables, relations, graph ...): --out, else the one tests/run_tests.py leaves
in --workdir (default $TAHOE_TEST_DIR or /tmp/tahoemap_test)/out_seed0. That folder is only read: every case works
in DIR/review_view, whose entries are symbolic links to the output's own entries next to a fresh review/ folder.

Every request goes through the real Anthropic SDK (client.beta.messages.create) to tahoemap/review/fake.py, an
httpx2 mock transport that answers from a script and checks each request as the API would; API errors are the
SDK's own typed exceptions. PubMed / Europe PMC / Crossref answer from fake.FakeLiterature. Sockets and urllib are
blocked for the whole test, the ANTHROPIC_* variables are removed, and sleeping between retries is patched out.

Cases: a review end to end (dossier, tool calls, a rejected and an accepted submit_review, id verification that
removes a nonexistent PMID, the citation checker, review JSON, note, ledger, history with every request and
response); pause_turn; refusal; the end_turn and max_tokens nudges and no_review; over_budget; a billing error that
rotates to the second key; every key dead (exit code 3) and the resume with a new key; a new key typed at the prompt;
rate limit / overload / network errors that back off without rotating; --dry-run; 6 entities on 3 threads; Ctrl-C
and SIGTERM mid-run and the resume; keys absent from every file written and every line printed; the error
classification; plan / status / tables and the CLI; a fake review of a gene, a drug and a line spliced into the
vault (the literature section, its callout and resolvable links, the partner tables' Literature column, no broken
link, no other note changed) and the map (the side panel's verdicts); `duplicate` (hard links, duplicated_from.json,
--repo).
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
SECRETS |= {KEY3, KEY4}
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
    trip = {(lit[t], lit[t + 1]): Dm["lit_v"][lit[t + 2]] for t in range(0, len(lit) - 3, 4)}
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
    duplicate(view, work, src)
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
