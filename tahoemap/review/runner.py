"""runner - review runs: which entities, the agent loop, verification, costs, the queue, status and tables.

    run(out, **options) -> RunResult      review the pending entities (see Options); RunResult.exit_code:
                                          0 finished (or stopped at --limit / --max-usd), 2 refused to start
                                          (no cap, bad option), 3 paused: no working API key (add one and run
                                          again), 4 stopped: the same error on SYSTEMATIC_N entities in a row (fix
                                          the cause and run again), 129 / 130 / 143 stopped by SIGHUP / Ctrl-C /
                                          SIGTERM (run again to resume)
    plan(out, kinds, only)                OUT/review/queue.parquet (entities in priority order, with their state)
                                          + counts and the projected cost
    status(out, tables=False)             counts by status and kind, spend, projected cost of the rest, dead keys,
                                          reviews whose verification is incomplete, the run lock
    build_tables(out)                     OUT/review/connections.parquet and findings.parquet from the reviews
                                          (with check_status and shown_verdict of every item, and
                                          'retracted': the retracted papers it cites)
    cli(a)                                `python -m tahoemap review plan|run|status|tables` (cli.py)

The agent loop (docs/DESIGN-review-and-physics.md, Part 2, "Surface"): every request is streamed -
client.beta.messages.stream(**kw) as a context manager, then get_final_message() - with the agent's system prompt
(agent + skills, cache_control), its tools (custom, strict, then web_search / web_fetch), output_config effort,
adaptive thinking (thinking omitted), fallbacks="default" with the server-side-fallback-2026-07-01 beta, top-level
automatic caching, and max_tokens by effort (64K up to high, 128K at xhigh / max). Each non-empty response.content
is appended unchanged (an empty one is never sent back). stop_reason: tool_use -> our tools run and all results go
back in one user message (a valid submit_review ends the loop); pause_turn -> resent as is; refusal -> status
refused (stop_details.category), except when stop_details.recommended_model is set (the fallback model was rate-
limited or overloaded, so it was not tried): then the attempt is 'failed' (retried later) and the recommended model
is logged; max_tokens -> a nudge (cut-off tool calls answered as not run; two cut-offs in a row end it); end_turn
without a review -> a nudge (two in a row: no_review). Every user message after the dossier ends with a budget
line - the spend and requests so far, and near the cap or max_turns a request to submit now - appended, never
edited, so the cached prefix stays the same. The citation checker (verify.py) runs the same loop.

Keys and errors (keys.py): a dead key (401, 402 / billing_error, 403, spend limit, organization on hold) ends the
attempt as key_rotated and the entity restarts from the beginning with the next key; rate limits, overload and 5xx
wait (after the SDK's own retry: exponential backoff with jitter up to 10 minutes, Retry-After honoured, MAX_WAITS
times) and retry the same request; a response lost to a timeout or a dropped connection is re-sent at most
MAX_NET_RETRIES times, and when it may have reached the API it is charged an estimate (lost_cost: the context at the
full input price plus the output of a long answer) to the attempt and the run, marked as estimated in the history
and the ledger; an attempt that reaches its cap only through such estimates is 'failed' (retried later), not
over_budget. Other errors fail the entity; the same error on SYSTEMATIC_N entities in a row before any entity of the run
got its answer stops the run (exit code 4) and those failures are not counted against the entities (an entity that
already stopped a run with that error does not count toward a stop again, so an error of the entities' own stops one
run, not every one). With every key dead the run pauses: on a terminal the main thread asks for a new key (getpass;
Enter or Ctrl-C there pauses, the terminal restored), else it stops with exit code 3 and the unfinished entities stay
pending.

Stopping (Ctrl-C, SIGTERM, SIGHUP, `tahoe stop`, the --max-usd cap): no new entity starts; after STOP_GRACE seconds
the running attempts are closed - a review already submitted is stored as done with its verification as far as it
got (the rest marked not run), the others are paused. A response that arrives after its attempt was closed is still
recorded (a late event in the history, a note line in the ledger).

Resume: the latest ledger line of an entity is its state (bookkeeping 'note' lines aside). done and refused are
final (unless --redo); failed and no_review are retried up to 2 more times (--retry-failed: again); over_budget only
with a higher per-entity cap; paused and key_rotated entities start again from the beginning. --recheck runs only
the verification a stored review lacks (ids that could not be looked up, a citation check that did not run); a
--recheck that is stopped leaves the review and its done line as they were (a ledger note), still to be checked.

Models and effort: the agent files' (reviewers claude-opus-5-5 / high, checker claude-opus-5-5 / medium); --model and
--effort set the reviewers, or per agent with AGENT=VALUE,... (gene, drug, line, checker, reviewers, all).

Costs (USD; PRICES): from response.usage, per usage.iterations entry at that entry's model when present (a fallback
model bills at its own price), cache writes at 1.25x input (2x for 1-hour entries), cache reads at the model's
cache-read price (claude-opus-5-5: $0.20 per million, 0.05x input), web searches $0.01 each, plus the estimates of
lost responses. --per-entity-usd caps one attempt (a request is not started once the attempt has spent it; the
citation checker has its own cap, its agent's max_usd); --max-usd caps this run (no new entity starts and running
ones pause once it is reached). Without --max-usd or --limit the runner refuses to start unless --no-cap is given;
it always prints the projected cost first.

Tests: `--fake SCRIPT` (fake.py) answers every request through the real SDK from a script, with no key and no
network; tests/test_review.py drives every path above with it.
"""

import glob
import hashlib
import json
import os
import random
import signal
import socket
import subprocess
import sys
import threading
import time
import traceback
from collections import Counter, deque
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from . import KINDS, VERSION, review_dir
from . import definitions as DEF
from . import dossier as D
from . import keys as K
from . import tools as TL
from . import verify as V
from .history import DOSSIER_REF, PLACEHOLDER_SOURCE, History, Ledger, now, read_jsonl, to_jsonable
from .. import __version__
from ..common import log, safe_filename, write_json, write_parquet

AGENTS = {"gene": "gene-reviewer", "drug": "drug-reviewer", "line": "line-reviewer"}
CHECKER = "citation-checker"
FALLBACK_BETA = "server-side-fallback-2026-07-01"
# max_tokens per response (thinking included) by effort; every request is streamed, so no HTTP timeout limits it
MAX_TOKENS = {"low": 64_000, "medium": 64_000, "high": 64_000, "xhigh": 128_000, "max": 128_000}
MAX_TOKENS_64K = ("claude-haiku-4-5",)     # models whose output ceiling is 64K
STREAM_TIMEOUT = 600.0              # seconds without a byte on a streamed response (the API sends pings): lost
FINAL = ("done", "refused")
MAX_FAILED = 3                      # failed / no_review attempts in a row before an entity is left alone
MAX_WAITS = 12                      # back-offs of one request before the entity fails (~1 h at the 10-min cap)
MAX_NET_RETRIES = 2                 # re-sends of a request lost to a timeout / dropped connection (after the SDK's own)
LOST_OUT_MIN = 16_000               # output tokens a lost response is charged at least (see lost_cost)
BACKOFF_BASE, BACKOFF_MAX = 5.0, 600.0
STOP_GRACE = 15.0                   # seconds the running entities get to notice Ctrl-C before they are marked paused
SYSTEMATIC_N = 5                    # the same error on this many entities in a row stops the run
BUDGET_WARN, TURNS_WARN = 0.75, 3   # the agent is told to wrap up past 75% of its cap or 3 requests before max_turns
EXIT_OK, EXIT_REFUSED, EXIT_PAUSED, EXIT_SYSTEMATIC = 0, 2, 3, 4
EXIT_SIGHUP, EXIT_SIGINT, EXIT_SIGTERM = 129, 130, 143
CHECK_STATUS = {"supported": "supported", "partly": "partly", "not supported": "not_supported",
                "not checkable": "not_checkable"}

# USD per million tokens: (input, output, cache read). Cache writes: 1.25x input (5-minute), 2x (1-hour).
PRICES = {
    "claude-opus-5-5": (4.00, 20.00, 0.20),
    "claude-opus-5": (5.00, 25.00, 0.50),
    "claude-opus-4-8": (5.00, 25.00, 0.50),
    "claude-opus-4-7": (5.00, 25.00, 0.50),
    "claude-sonnet-5-5": (2.00, 10.00, 0.20),
    "claude-sonnet-5": (2.00, 10.00, 0.20),
    "claude-haiku-5-5": (0.10, 0.50, 0.01),
    "claude-fable-5-1": (10.00, 50.00, 0.25),
    "claude-mythos-5-1": (10.00, 50.00, 0.25),
    "claude-fable-5": (10.00, 50.00, 1.00),
}
HAIKU_LONG = (0.50, 2.50, 0.05)     # claude-haiku-5-5 above 100K prompt tokens
FAMILY = {"opus": (5.00, 25.00, 0.50), "sonnet": (3.00, 15.00, 0.30), "haiku": (1.00, 5.00, 0.10)}
UNKNOWN_PRICE = (10.00, 50.00, 1.00)  # an unknown model is counted at the most expensive price
CACHE_WRITE_5M, CACHE_WRITE_1H = 1.25, 2.0
WEB_SEARCH_USD = 0.01
# the heuristic projection (before real costs exist): turns, tokens added per turn, output per turn by effort
EST_TURNS, EST_GROWTH, EST_WEB = 14, 2_500, 3
EST_OUT = {"low": 800, "medium": 1_500, "high": 2_500, "xhigh": 4_000, "max": 6_000}
EST_CHECK_IN, EST_CHECK_OUT = 12_000, 2_000
MIN_REAL = 3                        # finished entities of a kind before their mean real cost replaces the heuristic

NUDGE_END = ("You ended your turn without calling {tool}. The {what} is only stored through {tool}: call it now "
             "with every field filled (use [] for empty sections).")
NUDGE_MAX = ("Your last response was cut off at the output limit{cut}. Keep the reasoning short and call {tool} "
             "now; shorten long fields (note_markdown at most ~600 words) if needed.")
BUDGET_LINE = "[runner] Budget: {spent} of {cap} used; {turns} of {max_turns} requests made."
BUDGET_NEAR = (" Little is left: stop searching and call {tool} soon with what you have (an attempt that runs out "
               "stores nothing).")
BUDGET_LAST = (" This is your last request: call {tool} now with what you have, with every field filled; anything "
               "else ends the attempt and nothing is stored.")

SLEEP = lambda seconds, stop_event: stop_event.wait(seconds)  # noqa: E731  (patched by tests; True = stopped)

_warned = set()


# ----------------------------------------------------------------------------- prices and cost
def price(model, prompt_tokens=0):
    m = str(model or "")
    base = m[:-5] if m.endswith("-fast") else m
    if base.startswith("claude-haiku-5-5") and prompt_tokens > 100_000:
        return HAIKU_LONG
    if base in PRICES:
        return PRICES[base]
    for k in sorted(PRICES, key=len, reverse=True):          # dated snapshots: claude-opus-5-5-20261101 ...
        if base.startswith(k + "-"):
            return PRICES[k]
    for fam, p in FAMILY.items():
        if fam in base:
            if base not in _warned:
                _warned.add(base)
                log(f"WARNING: no price for model {m}; counting it at {fam} prices {p}")
            return p
    if base not in _warned:
        _warned.add(base)
        log(f"WARNING: no price for model {m}; counting it at {UNKNOWN_PRICE} USD per million tokens")
    return UNKNOWN_PRICE


def _n(d, k):
    v = (d or {}).get(k)
    return int(v) if isinstance(v, (int, float)) and v == v else 0


def _tokens_usd(u, model):
    prompt = _n(u, "input_tokens") + _n(u, "cache_creation_input_tokens") + _n(u, "cache_read_input_tokens")
    pin, pout, pread = price(model, prompt)
    cc = u.get("cache_creation") or {}
    if cc and (_n(cc, "ephemeral_5m_input_tokens") or _n(cc, "ephemeral_1h_input_tokens")):
        w = _n(cc, "ephemeral_5m_input_tokens") * CACHE_WRITE_5M + _n(cc, "ephemeral_1h_input_tokens") * CACHE_WRITE_1H
    else:
        w = _n(u, "cache_creation_input_tokens") * CACHE_WRITE_5M
    return (_n(u, "input_tokens") * pin + w * pin + _n(u, "cache_read_input_tokens") * pread
            + _n(u, "output_tokens") * pout) / 1e6


def usage_cost(usage, model, served=None):
    """(USD, summary) of one response's usage dict (response.usage.to_dict()); `model` = the requested model,
    `served` = response.model. With usage.iterations, every entry is priced at its own model (an entry that names
    none: the requested model, or the served one for a fallback_message entry); without, all at the served model."""
    u = usage or {}
    its = u.get("iterations") or []
    served = served or model
    if its:
        usd = sum(_tokens_usd(it, it.get("model") or (served if it.get("type") == "fallback_message" else model))
                  for it in its)
    else:
        usd = _tokens_usd(u, served)
    st = u.get("server_tool_use") or {}
    web = _n(st, "web_search_requests")
    usd += web * WEB_SEARCH_USD
    summ = {k: _n(u, k) for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens",
                                  "cache_read_input_tokens")}
    summ["web_searches"] = web
    summ["web_fetches"] = _n(st, "web_fetch_requests")
    return float(usd), summ


def heuristic_cost(agent, model, effort, dossier_chars, web=True, verify="llm", checker=None):
    """Projected USD of one review before any real costs exist: EST_TURNS requests whose context grows by
    EST_GROWTH tokens a turn, read from cache, plus the output at this effort, web searches and the checker."""
    tools = TL.tool_definitions(agent, web=web)
    S = (len(agent.system) + len(json.dumps(tools))) / 3.5
    Dt = dossier_chars / 3.3
    pin, pout, pread = price(model, S + Dt)
    usd = (S + Dt) * CACHE_WRITE_5M * pin
    for i in range(1, EST_TURNS):
        usd += (S + Dt + i * EST_GROWTH) * pread + EST_GROWTH * CACHE_WRITE_5M * pin
    usd += EST_TURNS * EST_OUT.get(effort, 2_500) * pout
    usd = usd / 1e6 + (EST_WEB * WEB_SEARCH_USD if web else 0.0)
    if verify == "llm" and checker is not None:
        cin, cout, _ = price(checker.model, EST_CHECK_IN)
        usd += (EST_CHECK_IN * CACHE_WRITE_5M * cin + EST_CHECK_OUT * cout) / 1e6
    return float(usd)


# ----------------------------------------------------------------------------- options and results
@dataclass
class Options:
    kinds: tuple = KINDS
    only: object = None                 # comma list, '@file', or a list
    limit: int = 0                      # entities to start in this run (0 = all pending)
    max_usd: float = None               # total cap of this run
    per_entity_usd: float = None        # default: the agent file's max_usd
    concurrency: int = 4
    model: str = None                   # reviewers' model, or AGENT=MODEL,... (default: the agent files')
    effort: str = None                  # reviewers' effort, or AGENT=EFFORT,... (default: the agent files')
    verify: str = "llm"                 # llm | ids | off
    web: bool = True
    web_max_uses: int = 5
    keys_file: str = None
    redo: bool = False
    retry_failed: bool = False          # retry failed / no_review entities even after MAX_FAILED attempts
    recheck: bool = False               # only re-run the verification of stored reviews that lack it (see recheck)
    dry_run: bool = False
    fake: object = None                 # path of a fake script, or a fake.FakeAPI (tests)
    no_cap: bool = False
    interactive: bool = None            # None: a terminal
    prompt: object = None               # the getpass replacement (tests)
    env_keys: bool = True               # read ANTHROPIC_API_KEY(S)
    default_chain: bool = True          # fall back to the SDK's default credentials
    agents_dir: str = None
    skills_dir: str = None
    quiet: bool = False


@dataclass
class RunResult:
    exit_code: int = 0
    counts: dict = field(default_factory=dict)
    spent_usd: float = 0.0
    started: int = 0
    message: str = ""
    paused: bool = False
    violations: list = field(default_factory=list)   # --fake: requests the API would have rejected


# ----------------------------------------------------------------------------- selection and state
def parse_only(only):
    if not only:
        return []
    if isinstance(only, (list, tuple)):
        items = list(only)
    else:
        s = str(only).strip()
        if s.startswith("@"):
            with open(os.path.expanduser(s[1:]), encoding="utf-8") as fh:
                items = [ln.split("#", 1)[0] for ln in fh]
        else:
            items = s.split(",")
    return list(dict.fromkeys(x.strip() for x in items if x and x.strip()))


def parse_kinds(kinds):
    if isinstance(kinds, str):
        kinds = [k.strip() for k in kinds.split(",") if k.strip()]
    kinds = list(kinds or KINDS)
    bad = [k for k in kinds if k not in KINDS]
    if bad:
        raise ValueError(f"--kinds: unknown {bad}; use {','.join(KINDS)}")
    return tuple(kinds)


def select(out, kinds=KINDS, only=None):
    """The entities to consider, in priority order (dossier.entities); with `only`, those names in the given order
    (entity ids 'gene:12' / 'drug:X' / 'line:CVCL_x', names, gene symbols or aliases)."""
    kinds = parse_kinds(kinds)
    ents = D.entities(out, kinds)
    names = parse_only(only)
    if not names:
        return ents
    by_id = {e: i for i, e in enumerate(ents["entity_id"])}
    by_name = {}
    for i, (k, n) in enumerate(zip(ents["kind"], ents["name"])):
        by_name.setdefault(str(n).lower(), []).append(i)
    rows, missing = [], []
    for nm in names:
        hit = []
        if nm in by_id:
            hit = [by_id[nm]]
        elif nm.lower() in by_name:
            hit = by_name[nm.lower()]
        if hit:
            rows += [ents.iloc[i].to_dict() for i in hit]
            continue
        found = False
        for k in kinds:
            if ":" in nm and nm.split(":", 1)[0] in KINDS and nm.split(":", 1)[0] != k:
                continue
            try:
                name, eid, _key = D.resolve(out, k, nm)
            except Exception:  # noqa: BLE001  (query.NotFound, ambiguous names ...)
                continue
            if eid in by_id:
                rows.append(ents.iloc[by_id[eid]].to_dict())
            else:
                rows.append({"kind": k, "name": name, "entity_id": eid, "label": name, "priority": 0.0})
            found = True
            break
        if not found:
            missing.append(nm)
    if missing:
        raise ValueError(f"--only: not found in this run: {', '.join(missing[:20])}")
    df = pd.DataFrame(rows)
    return df.drop_duplicates("entity_id").reset_index(drop=True)


def entity_cap(run_or_opts, agent):
    p = getattr(run_or_opts, "per_entity_usd", None)
    return float(p) if p else float(agent.max_usd)


def to_run(state, redo, cap, retry_failed=False):
    """(run it?, why not) for one entity's ledger state."""
    if redo or state is None:
        return True, ""
    st = state["status"]
    if st in FINAL:
        return False, st
    if st in ("failed", "no_review") and state["n_failed"] >= MAX_FAILED and not retry_failed:
        return False, f"{st} {state['n_failed']} times (--retry-failed retries it)"
    if st == "over_budget" and cap <= float((state["last"] or {}).get("cap_usd") or 0) + 1e-9:
        return False, "over_budget (raise --per-entity-usd to retry)"
    return True, ""


def per_agent(value, what):
    """--model / --effort -> {agent name: value}. A plain value sets the three reviewers; 'AGENT=X,AGENT=Y' sets
    those agents, AGENT being an agent name (gene-reviewer, drug-reviewer, line-reviewer, citation-checker) or
    gene / drug / line / checker / reviewers / all."""
    if not value:
        return {}
    v = str(value).strip()
    if "=" not in v:
        return {AGENTS[k]: v for k in KINDS}
    names = {**{k: [AGENTS[k]] for k in KINDS}, **{AGENTS[k]: [AGENTS[k]] for k in KINDS},
             "checker": [CHECKER], CHECKER: [CHECKER], "reviewers": [AGENTS[k] for k in KINDS],
             "all": [AGENTS[k] for k in KINDS] + [CHECKER]}
    out = {}
    for part in v.split(","):
        if not part.strip():
            continue
        k, _eq, x = (t.strip() for t in part.partition("="))
        if k not in names or not x:
            raise ValueError(f"{what}: '{part.strip()}' is not AGENT=VALUE with AGENT one of "
                             f"{', '.join(sorted(names))}")
        for n in names[k]:
            out[n] = x
    return out


def load_agents(opts):
    """kind -> AgentDef for the three reviewers, plus 'checker', with --model / --effort applied."""
    models, efforts = per_agent(opts.model, "--model"), per_agent(opts.effort, "--effort")
    bad = sorted({e for e in efforts.values() if e not in DEF.EFFORTS})
    if bad:
        raise ValueError(f"--effort: {', '.join(bad)} is not one of {', '.join(DEF.EFFORTS)}")
    ag = {}
    for k, name in [(k, AGENTS[k]) for k in KINDS] + [("checker", CHECKER)]:
        a = DEF.load_agent(name, opts.agents_dir, opts.skills_dir)
        a.model = models.get(name, a.model)
        a.effort = efforts.get(name, a.effort)
        ag[k] = a
    return ag


def projection(out, sel, states, agents, opts, sample=3):
    """kind -> (USD per entity, basis): the mean real cost of the kind's finished entities once MIN_REAL exist,
    else heuristic_cost from the mean size of a few dossiers."""
    real = {}
    kinds = {}
    for e, s in states.items():
        if s["status"] in ("done", "no_review", "over_budget", "refused"):
            k = e.split(":", 1)[0]
            real.setdefault(k, []).append(s["cost_usd"])
    for k in KINDS:
        if not len(sel) or k not in set(sel["kind"]):
            continue
        if len(real.get(k, [])) >= MIN_REAL:
            kinds[k] = (float(np.mean(real[k])), f"mean real cost of {len(real[k])} reviewed {k}s")
            continue
        sizes = []
        for eid in sel.loc[sel["kind"] == k, "entity_id"].head(sample):
            try:
                sizes.append(len(D.build(out, k, eid).text))
            except Exception:  # noqa: BLE001
                continue
        chars = float(np.mean(sizes)) if sizes else float(D.MAX_CHARS)
        a = agents[k]
        kinds[k] = (heuristic_cost(a, a.model, a.effort, chars, opts.web, opts.verify, agents["checker"]),
                    f"estimate from the dossier size (~{chars:,.0f} characters) and ~{EST_TURNS} requests")
    return kinds


def _fmt_usd(x):
    x = float(x)
    return f"${x:,.0f}" if x >= 1000 else f"${x:,.2f}" if x >= 0.1 or x == 0 else f"${x:.4f}"


# ----------------------------------------------------------------------------- one run
class Run:
    def __init__(self, out, opts, pool, agents, fake=None):
        self.out, self.opts, self.pool, self.agents, self.fake = out, opts, pool, agents, fake
        self.ledger = Ledger(out)
        self.stop = threading.Event()
        self.stop_reason = ""
        self.stop_signal = None
        self.lock = threading.Lock()
        self._keys_lock = threading.Lock()
        self.spent = 0.0
        self.started = 0
        self.active = {}                # entity_id -> Attempt
        self.counts = Counter()
        self.cap_hit = False
        self.keys_paused = False
        self.code = code_version()
        self.streak = []                # the failed attempts in a row with the same error: (sig, entity_id, rec)
        self.systematic = None          # (signature, error) once SYSTEMATIC_N in a row stopped the run
        self.answered = False           # an attempt of this run got its answer from the API (no systematic stop)
        self.stopped_runs = {}          # entity_id -> the errors with which it already stopped an earlier run
        pool.stopping = self.stop.is_set

    def outcome(self, att, status, rec):
        """Called once per finished attempt (keys_state#1): the same error on SYSTEMATIC_N entities in a row, before
        any attempt of this run got its answer (done, refused, no_review, over_budget, a refusal to retry), stops the
        run. An entity that already stopped an earlier run with this same error joins the streak (its failure is
        then not counted either) but does not count toward the stop: an error that is the entities' own (a request
        too large for each of them, ...) stops one run, and the next goes on past them and counts their failures."""
        with self.lock:
            sig = att.fail_sig if status == "failed" else None
            if self.systematic is not None:            # stopped: only the same error joins (to be uncounted)
                if sig is not None and sig == self.systematic[0]:
                    self.streak.append((sig, att.entity_id, rec))
                return
            if status in ("done", "refused", "no_review", "over_budget") or rec.get("transient_refusal"):
                self.answered = True                   # the API works for this run: failures are the entities' own
                self.streak = []
                return
            if sig is None or self.answered:
                return
            if self.streak and self.streak[-1][0] != sig:
                self.streak = []
            self.streak.append((sig, att.entity_id, rec))
            new = [e for g, e, _r in self.streak if not ({g, "*"} & self.stopped_runs.get(e, set()))]
            if len(new) >= SYSTEMATIC_N:
                self.systematic = (sig, rec.get("error") or "")
        if self.systematic is not None and not self.stop.is_set():
            self.request_stop(f"the same error on {SYSTEMATIC_N} entities in a row ({' '.join(map(str, sig))})")
            log(f"STOPPING: the same error on {SYSTEMATIC_N} entities in a row: {K.scrub(self.systematic[1])[:300]}")

    def add_spend(self, usd):
        with self.lock:
            self.spent += usd
            if self.opts.max_usd is not None and self.spent >= float(self.opts.max_usd) and not self.cap_hit:
                self.cap_hit = True
                log(f"The total cap of this run (--max-usd {self.opts.max_usd}) is reached: no new entities start, "
                    "running ones pause")

    def cap_reached(self):
        return self.opts.max_usd is not None and self.spent >= float(self.opts.max_usd)

    def request_stop(self, reason, sig=None):
        if not self.stop.is_set():
            self.stop_reason = reason
            self.stop_signal = sig
            self.stop.set()

    def sleep(self, seconds):
        """Wait (interruptibly); True when the run is stopping."""
        return bool(SLEEP(seconds, self.stop)) or self.stop.is_set()

    def save_keys(self, *_):
        """OUT/review/keys_state.json: the key ids and which are dead (never a key itself)."""
        with self._keys_lock:                       # several threads can see a key die at once
            write_json({"updated": now(), "keys": self.pool.describe()},
                       os.path.join(review_dir(self.out), "keys_state.json"))


def code_version():
    v = f"tahoemap {__version__}, review format {VERSION}"
    try:
        here = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        r = subprocess.run(["git", "-C", here, "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                           timeout=10)
        if r.returncode == 0 and r.stdout.strip():
            d = subprocess.run(["git", "-C", here, "status", "--porcelain", "--", "tahoemap"], capture_output=True,
                               text=True, timeout=10)
            v += f", commit {r.stdout.strip()}" + (" + local changes" if d.stdout.strip() else "")
    except (OSError, subprocess.SubprocessError):
        pass
    return v


def new_run_id():
    return time.strftime("%Y%m%d-%H%M%S") + "-" + "%06x" % random.randrange(16 ** 6)


def max_tokens_for(model, effort):
    """max_tokens of one response (thinking included): 64K up to effort high, 128K at xhigh / max (64K on models
    whose ceiling is 64K)."""
    n = MAX_TOKENS.get(effort, 64_000)
    if any(str(model or "").startswith(m) for m in MAX_TOKENS_64K):
        n = min(n, 64_000)
    return n


def build_request(agent, web=True, web_max_uses=5):
    """The static part of every request of one agent (messages are added per call); sent with
    client.beta.messages.stream(**kw)."""
    kw = {"model": agent.model, "max_tokens": max_tokens_for(agent.model, agent.effort),
          "system": [{"type": "text", "text": agent.system, "cache_control": {"type": "ephemeral"}}],
          "tools": TL.tool_definitions(agent, web=web, max_uses=web_max_uses),
          "output_config": {"effort": agent.effort},
          "cache_control": {"type": "ephemeral"},
          "timeout": STREAM_TIMEOUT}
    if "haiku" not in agent.model:                 # no server-side fallback for Haiku
        kw["betas"] = [FALLBACK_BETA]
        kw["fallbacks"] = "default"
    if not kw["tools"]:
        del kw["tools"]
    return kw


def request_settings(kw):
    return {k: v for k, v in kw.items() if k not in ("system", "tools", "messages")}


class _Stopped(Exception):
    def __init__(self, message=""):
        super().__init__(message)
        self.message = message


class _OverBudget(Exception):
    pass


class _StreamCut(Exception):
    """The stream ended (without an error) before the response was complete."""


class _KeyDead(Exception):
    def __init__(self, info):
        super().__init__(info.get("message", ""))
        self.info = info


class _Failed(Exception):
    def __init__(self, info):
        super().__init__(info.get("message", ""))
        self.info = info


class Attempt:
    """One try at one entity with one key: the conversation(s), its history file and its ledger line. With
    recheck=True: only the verification a stored review lacks (`review run --recheck`), no reviewer."""

    def __init__(self, run, ent, key, n, recheck=False):
        self.run, self.ent, self.key, self.n = run, ent, key, n
        self.kind, self.name, self.entity_id = ent["kind"], ent["name"], ent["entity_id"]
        self.run_id = new_run_id()
        self.hist = History(run.out, self.kind, self.name, self.run_id)
        self.started = now()
        self.cost = 0.0
        self.estimated = 0.0            # USD of it charged as estimates for responses lost on the way
        self.tok = Counter()
        self.max_out = 0                # the largest output_tokens of a response of this attempt (lost_cost)
        self.n_requests = 0
        self.n_tool_calls = 0
        self.models = []
        self.lock = threading.RLock()
        self.finalized = False
        self.agent = run.agents[self.kind]
        self.cap = entity_cap(run.opts, self.agent)
        self.extra = {}
        self.recheck = recheck
        self.fail_sig = None            # the error of a failed attempt (the systematic-failure check)
        self.pending = None             # once the review is submitted: pending(reason) stores it as done

    # -------------------------------------------------------------- bookkeeping
    def add(self, usd, summ, model):
        with self.lock:
            self.cost += usd
            self.tok.update(summ)
            self.max_out = max(self.max_out, int(summ.get("output_tokens") or 0))
            self.n_requests += 1
            if model and model not in self.models:
                self.models.append(model)
        self.run.add_spend(usd)

    def add_estimate(self, usd):
        """Charge the estimated cost of a lost response (it may have been billed) to the attempt and the run."""
        with self.lock:
            self.cost += usd
            self.estimated += usd
        self.run.add_spend(usd)

    def record_response(self, agent, n, d, usd, summ):
        """Count one response and put it in the history. A response that arrives after the attempt was closed (the
        run stopped and marked it) still counts: a late event after the history's end, and a ledger note line."""
        with self.lock:                                 # (finish() takes the same lock: counted once, in order)
            late = self.finalized
            self.add(usd, summ, d.get("model"))
            if not late:
                self.hist.event("response", agent=agent.name, n=n, response=d, usage=d.get("usage"),
                                cost_usd=round(usd, 6), attempt_cost_usd=round(self.cost, 6))
                return
            self.hist.event("response", late=True, agent=agent.name, n=n, response=d, usage=d.get("usage"),
                            cost_usd=round(usd, 6))
        self.run.ledger.append({
            "entity_id": self.entity_id, "kind": self.kind, "name": self.name, "run_id": self.run_id,
            "agent": agent.name, "model": d.get("model"), "status": "note", "cost_usd": round(usd, 6),
            "note": "a response that arrived after its attempt had been closed (the run was stopping)",
            "late": True, "key_id": self.key.key_id, "finished": now(), "history": self.hist.rel,
            **{k: int(v) for k, v in summ.items()}})

    def finish(self, status, error=None, store=None, **extra):
        """Write the ledger line and the history's end event, once (the first caller wins). `store` runs first,
        under the same lock (the review files of a done attempt). Returns the status written, or None. A recheck
        attempt writes 'done' or, for any other outcome, a ledger note (the entity stays done)."""
        with self.lock:
            if self.finalized:
                return None
            self.finalized = True
            if store is not None:
                store()
            err = K.scrub(error)[:2000] if error else None
            written = status
            if self.recheck and status != "done":
                written = "note"
                extra = dict(extra, note=f"recheck: {status}", recheck=True)
            rec = {"entity_id": self.entity_id, "kind": self.kind, "name": self.name, "run_id": self.run_id,
                   "agent": self.agent.name, "model": self.agent.model, "status": written,
                   "cost_usd": round(self.cost, 6), "n_requests": self.n_requests, "n_tool_calls": self.n_tool_calls,
                   "key_id": self.key.key_id, "started": self.started, "finished": now(), "error": err,
                   "cap_usd": self.cap, "attempt": self.n, "served_models": list(self.models),
                   "history": self.hist.rel, **{k: int(self.tok.get(k, 0)) for k in (
                       "input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens",
                       "web_searches", "web_fetches")}}
            if self.estimated:
                rec["estimated_usd"] = round(self.estimated, 6)
            rec.update(self.extra)
            rec.update(extra)
            self.run.ledger.append(rec)
            self.hist.event("end", status=status, error=err, totals={
                "cost_usd": round(self.cost, 6), "estimated_usd": round(self.estimated, 6),
                "n_requests": self.n_requests, "n_tool_calls": self.n_tool_calls,
                **{k: int(v) for k, v in self.tok.items()}}, **{k: v for k, v in extra.items()})
        with self.run.lock:
            self.run.counts[status if not self.recheck else f"recheck {status}"] += 1
            self.run.active.pop(self.entity_id, None)
        if not self.recheck:
            self.run.outcome(self, status, rec)
        if not self.run.opts.quiet:
            log(f"  {self.entity_id} ({self.name}): {'recheck ' if self.recheck else ''}{status}  "
                f"{_fmt_usd(self.cost)}" + (f"  [{err[:160]}]" if err and status != "done" else ""))
        return status

    def finish_pending(self, reason):
        """The run is stopping and this attempt is still running: a submitted review is stored as done (with the
        verification as far as it got; the rest is marked not run), a recheck leaves the stored review as it is,
        anything else is paused (and starts again next run)."""
        if self.pending is not None:
            return self.pending(reason)
        return self.finish("paused", error=reason)

    # -------------------------------------------------------------- the attempt
    def execute(self):
        r = self.run
        try:
            dos = D.build(r.out, self.kind, self.entity_id)
        except Exception as e:  # noqa: BLE001
            self.fail_sig = ("dossier", type(e).__name__)
            return self.finish("failed", error=f"dossier: {type(e).__name__}: {e}")
        agent = self.agent
        kw = build_request(agent, r.opts.web, r.opts.web_max_uses)
        messages = [{"role": "user", "content": dos.user_message()}]
        self.hist.event("start", agent=agent.name, model=agent.model, effort=agent.effort, key_id=self.key.key_id,
                        entity={"kind": self.kind, "name": self.name, "entity_id": self.entity_id},
                        attempt=self.n, code_version=r.code, system_sha256=agent.system_sha256, system=agent.system,
                        tools=[t["name"] for t in kw.get("tools", [])], tool_definitions=kw.get("tools", []),
                        dossier_sha256=dos.sha256, dossier=dos.text, request=request_settings(kw),
                        cap_usd=self.cap, verify=r.opts.verify, web=r.opts.web)
        ctx = TL.make_context(r.out, {"kind": self.kind, "name": self.name, "entity_id": self.entity_id})
        status, info = converse(self, agent, r.pool.client(self.key), kw, messages, ctx, self.cap,
                                elide={DOSSIER_REF: dos.text})
        if status == "submitted":
            return self.complete(dos, ctx)
        if status == "key_dead":
            self.extra["dead_reason"] = _info_text(info)[:300]
            return self.finish("key_rotated", error=_info_text(info))
        if status == "refused":
            return self.finish("refused", error=_info_text(info), refusal_category=info.get("category"))
        if status == "refused_transient":           # the fallback model was busy: not final, retried later
            log(f"  {self.entity_id}: refused ({info.get('category') or 'no category'}) while the fallback model "
                f"was unavailable; it will be retried (recommended model: {info.get('recommended_model')})")
            return self.finish("failed", error=_info_text(info), refusal_category=info.get("category"),
                               recommended_model=info.get("recommended_model"), transient_refusal=True)
        if status == "failed":
            self.fail_sig = _signature(info)
        return self.finish(status, error=_info_text(info))

    def complete(self, dos, ctx):
        """Verification, then the review JSON + note, then the ledger line. From here on the attempt is stored as
        done whatever happens: if the run stops (Ctrl-C, SIGTERM, SIGHUP, the --max-usd cap, no key left) before
        the verification is finished, the review is stored with the verification as far as it got, the rest
        marked not run (`review run --recheck` completes it later)."""
        r = self.run
        mode = r.opts.verify
        st = {"ids": (ctx.submitted, None), "llm": None}       # each entry replaced whole (read by another thread)
        self.pending = lambda why: self.store_done(dos, ctx, st, mode, stopping=why)
        if mode in ("ids", "llm") and not r.stop.is_set():
            try:
                st["ids"] = V.check_ids(ctx.submitted, ctx)
            except Exception as e:  # noqa: BLE001
                err = K.scrub(f"{type(e).__name__}: {e}")
                self.hist.event("error", agent="verify", **{"class": type(e).__name__, "message": err})
                st["ids"] = (ctx.submitted, {"error": err})
        if mode == "llm" and not r.stop.is_set():
            st["llm"] = self.citation_check(st["ids"][0], ctx)
        return self.store_done(dos, ctx, st, mode)

    def store_done(self, dos, ctx, st, mode, stopping=None):
        r = self.run
        checked, report = st["ids"]
        llm = None
        if st["llm"] is not None:
            checked, llm = st["llm"]
        elif mode == "llm":
            llm = {"status": "not run: " + (stopping or r.stop_reason or "the run was stopping")}
        if mode in ("ids", "llm") and report is None:
            report = {"error": "not run: " + (stopping or r.stop_reason or "the run was stopping")}
        final = V.finalize(checked, mode, report, llm)
        final["meta"] = {
            "entity_id": self.entity_id, "kind": self.kind, "name": self.name, "agent": self.agent.name,
            "model": self.agent.model, "served_models": list(self.models), "effort": self.agent.effort,
            "checker_model": r.agents["checker"].model if mode == "llm" else None, "run_id": self.run_id,
            "key_id": self.key.key_id, "reviewed": now(), "cost_usd": round(self.cost, 6),
            "estimated_usd": round(self.estimated, 6), "tokens": {k: int(v) for k, v in self.tok.items()},
            "n_requests": self.n_requests, "n_tool_calls": self.n_tool_calls, "history": self.hist.rel,
            "dossier_sha256": dos.sha256, "system_sha256": self.agent.system_sha256, "code_version": r.code,
            "not_retrieved": list(ctx.notes.get("not_retrieved") or [])}
        paths = review_paths(r.out, self.kind, self.name)

        def store():
            write_json(final, paths["review"])
            D.write_text(paths["note"], final.get("note_markdown") or "")
        ver = final["verification"]
        return self.finish("done", store=store, verify=mode, check_status=ver["llm"]["status"] if mode == "llm"
                           else ver["ids"]["status"] if mode == "ids" else "off",
                           ids_status=ver_status(ver, "ids"), llm_status=ver_status(ver, "llm"),
                           review=os.path.relpath(paths["review"], r.out).replace(os.sep, "/"),
                           **({"stopped_during_verification": stopping} if stopping else {}))

    def recheck_review(self):
        """`review run --recheck`: the verification a stored review lacks - the id look-ups when they did not run
        or could not reach PubMed / Crossref, and (with --verify llm) the citation check when it did not finish -
        without running the reviewer again. The review JSON and note are rewritten; the ledger gets a done line
        with the cost of the check."""
        r = self.run
        paths = review_paths(r.out, self.kind, self.name)
        stored = read_json_safe(paths["review"])
        if not isinstance(stored, dict):
            return self.finish("failed", error="--recheck: the stored review is missing or unreadable")
        # stopped before it finished: a ledger note (finish() writes one for a recheck that is not done), so the
        # entity's state stays its earlier done line, which says what the stored review lacks: still --recheck-able
        self.pending = lambda why: self.finish("paused", error=f"recheck stopped: {why}; the stored review is "
                                               "unchanged", review_unchanged=True)
        mode = r.opts.verify
        ver0, meta0 = stored.get("verification") or {}, stored.get("meta") or {}
        need_ids, need_llm = needs_recheck(stored, mode)
        eff = "llm" if (mode == "llm" or ver_status(ver0, "llm") == "done") else "ids"
        review = {k: v for k, v in stored.items() if k not in ("verification", "meta", "note_footer")}
        ent = {"kind": self.kind, "name": self.name, "entity_id": self.entity_id}
        ctx = TL.make_context(r.out, ent)
        nr = set(meta0.get("not_retrieved") or [])
        cited = {c for c, _s, _i in TL.cited_ids(review)}
        ctx.read_ids |= {c for c in cited if c.startswith("PMID:") and c not in nr}
        ctx.seen_ids |= {c for c in cited if c not in nr}
        self.hist.event("start", agent="recheck", phase="recheck", entity=ent, key_id=self.key.key_id,
                        code_version=r.code, verify=mode, review=os.path.relpath(paths["review"], r.out),
                        ids=need_ids, llm=need_llm, previous={"ids": ver_status(ver0, "ids"),
                                                             "llm": ver_status(ver0, "llm")})
        checked, report = review, ver0.get("ids")
        if need_ids:
            try:
                checked, report = V.check_ids(review, ctx)
            except Exception as e:  # noqa: BLE001
                report = {"error": K.scrub(f"{type(e).__name__}: {e}")}
                self.hist.event("error", agent="verify", **{"class": type(e).__name__, "message": report["error"]})
        llm = ver0.get("llm")
        if need_llm and not r.stop.is_set():
            checked, llm = self.citation_check(checked, ctx)
        elif need_llm:
            llm = {"status": "not run: " + (r.stop_reason or "the run was stopping")}
        final = V.finalize(checked, eff, report, llm)
        final["meta"] = dict(meta0, rechecked=now(), recheck_run_id=self.run_id, recheck_history=self.hist.rel,
                             recheck_cost_usd=round(self.cost, 6),
                             checker_model=r.agents["checker"].model if need_llm else meta0.get("checker_model"))

        def store():
            write_json(final, paths["review"])
            D.write_text(paths["note"], final.get("note_markdown") or "")
        ver = final["verification"]
        return self.finish("done", store=store, verify=eff, recheck=True, check_status=ver["llm"]["status"]
                           if eff == "llm" else ver["ids"]["status"], ids_status=ver_status(ver, "ids"),
                           llm_status=ver_status(ver, "llm"),
                           review=os.path.relpath(paths["review"], r.out).replace(os.sep, "/"))

    def citation_check(self, checked, rctx):
        r = self.run
        ent = {"kind": self.kind, "name": self.name, "entity_id": self.entity_id}
        try:
            claims = V.claims(checked, ent)
            if not claims:
                return checked, {"status": "no claims cite a paper"}
            abstracts = V.fetch_abstracts(checked, rctx)
            prompt = V.build_check_prompt(checked, abstracts, ent)
        except Exception as e:  # noqa: BLE001
            return checked, {"status": "failed", "error": K.scrub(f"{type(e).__name__}: {e}")}
        agent = r.agents["checker"]
        kw = build_request(agent, web=False)
        key = self.key
        status, info = "failed", {}
        psha = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        while True:
            ctx = TL.make_context(r.out, ent)
            ctx.notes["claim_ids"] = [c["claim_id"] for c in claims]
            messages = [{"role": "user", "content": prompt}]
            self.hist.event("start", agent=agent.name, phase="citation check", model=agent.model,
                            effort=agent.effort, key_id=key.key_id, system_sha256=agent.system_sha256,
                            system=agent.system, tools=[t["name"] for t in kw.get("tools", [])],
                            tool_definitions=kw.get("tools", []), prompt_sha256=psha,
                            claim_ids=ctx.notes["claim_ids"], request=request_settings(kw),
                            cap_usd=float(agent.max_usd))
            status, info = converse(self, agent, r.pool.client(key), kw, messages, ctx, float(agent.max_usd))
            if status != "key_dead":
                break
            r.pool.mark_dead(key, _info_text(info))
            try:
                key = r.pool.current()
            except K.AllKeysDead:
                if not r.stop.is_set():
                    r.keys_paused = True
                r.request_stop("no working API key")
                return checked, {"status": "not run: no working API key"}
        if status == "submitted":
            out, summ = V.apply_check(checked, ctx.submitted)
            summ["status"] = "done"
            return out, summ
        if status == "paused":
            return checked, {"status": "not run: " + (_info_text(info) or "the run was stopping")}
        return checked, {"status": status, "error": _info_text(info)}


def _signature(info):
    """What makes two failures 'the same error' (the systematic-failure check)."""
    return (str(info.get("class") or "?"), info.get("status"), str(info.get("type") or info.get("error_code") or ""))


def ver_status(ver, what):
    """The status (done | not_run | failed | partial) of the 'ids' or 'llm' step of a stored verification, also for
    reviews stored by older versions."""
    b = (ver or {}).get(what)
    if not isinstance(b, dict) or not b:
        return "not_run"
    st = str(b.get("status") or "")
    if what == "ids":
        if b.get("error") or st == "failed":
            return "failed"
        if st == "not_run":
            return "not_run"
        u = b.get("unchecked")
        return "partial" if (len(u) if isinstance(u, (list, tuple)) else int(u or 0)) else "done"
    if st in ("done", "no claims cite a paper"):
        return "done"
    if not st or st.startswith(("not run", "not_run")):
        return "not_run"
    return "failed"


def needs_recheck(review, mode):
    """(ids, llm): which verification steps `review run --recheck --verify MODE` would run on a stored review."""
    ver = (review or {}).get("verification") or {}
    if mode not in ("ids", "llm"):
        return False, False
    return ver_status(ver, "ids") != "done", mode == "llm" and ver_status(ver, "llm") != "done"


def recheck_pending(out, state, mode):
    """True when a done entity's stored review lacks verification `--recheck --verify MODE` would run: from its
    ledger line (ids_status / llm_status) when it has them, else from the review JSON (the line's review path, else
    the entity's own: a line of an older version, or of a recheck stopped before it finished)."""
    last = (state or {}).get("last") or {}
    if (state or {}).get("status") != "done" or mode not in ("ids", "llm"):
        return False
    if "ids_status" in last and "llm_status" in last:
        return last["ids_status"] != "done" or (mode == "llm" and last["llm_status"] != "done")
    rel = last.get("review")
    if rel:
        path = os.path.join(out, rel)
    elif last.get("kind") and last.get("name"):
        path = review_paths(out, last["kind"], last["name"])["review"]
    else:
        return False
    js = read_json_safe(path)
    return isinstance(js, dict) and any(needs_recheck(js, mode))


def _info_text(info):
    if not info:
        return ""
    if isinstance(info, str):
        return info
    parts = [str(info.get(k)) for k in ("class", "status", "type", "error_code", "category") if info.get(k)]
    msg = info.get("api_message") or info.get("message") or info.get("explanation") or ""
    return (" ".join(parts) + (": " if parts and msg else "") + str(msg)).strip()


def review_paths(out, kind, name):
    s = safe_filename(name)
    return {"review": os.path.join(review_dir(out, "reviews", kind), s + ".json"),
            "note": os.path.join(review_dir(out, "notes", kind), s + ".md")}


# ----------------------------------------------------------------------------- the agent loop
def lost_cost(kw, sends=1, max_out=0):
    """A conservative estimate (USD) of a response lost on the way (a timeout, a dropped connection, a stream cut
    short), which may have been processed and billed: the whole context (~3 characters a token) at the full input
    price (no cache discount) plus the output of a long answer - twice the longest answer of this attempt so far
    (`max_out` tokens), at least LOST_OUT_MIN tokens (~6x a typical answer at effort high), at most max_tokens -
    once per send that may have reached the API. (A stream is cut when the connection drops, so the full max_tokens
    is not a likely bill.)"""
    chars = sum(len(json.dumps(to_jsonable(kw.get(k)))) for k in ("system", "tools", "messages"))
    tokens = chars / 3.0
    pin, pout, _ = price(kw.get("model"), tokens)
    out = min(int(kw.get("max_tokens") or 64_000), max(LOST_OUT_MIN, 2 * int(max_out or 0)))
    return sends * (tokens * pin + out * pout) / 1e6


def call(att, agent, client, kw, conv):
    """One request, streamed (client.beta.messages.stream(**kw) as a context manager, then get_final_message(): no
    HTTP timeout limits a long generation, and bytes keep flowing). Wait-class errors are retried here (after the
    SDK's own retry): rate limits / overload / 5xx up to MAX_WAITS times, timeouts and dropped connections (a
    'lost response') only MAX_NET_RETRIES times. A lost response that may have reached the API is charged an
    estimate (lost_cost) to the attempt and the run, logged as estimated, and counted in conv["spent"] (and
    conv["estimated"]) against the conversation's cap. Raises _KeyDead, _Failed, _OverBudget or _Stopped."""
    waits = nets = 0
    while True:
        opened = False
        try:
            with client.beta.messages.stream(**kw) as stream:      # (the request is sent here)
                opened = True
                try:
                    resp = stream.get_final_message()
                except (AssertionError, RuntimeError) as e:        # no message_start, events out of order
                    raise _StreamCut(f"the response stream broke off ({type(e).__name__})") from None
            if resp is None or resp.stop_reason is None:
                raise _StreamCut("the response stream ended before the message was complete")
            return resp
        except Exception as e:  # noqa: BLE001  (classified below)
            if isinstance(e, _StreamCut):
                cat, info = K.WAIT, {"class": "StreamCut", "status": None, "type": None, "message": str(e),
                                     "network": True, "sent": True}
            else:
                cat, info = K.classify(e)
            sends = 0
            if opened:                                  # cut after the response had started: it was processed
                info["phase"] = "stream"
                sends = 1
            elif info.get("network") and info.get("sent"):
                sends = 1 + int(getattr(client, "max_retries", K.SDK_MAX_RETRIES) or 0)
            est = 0.0
            if sends:
                est = lost_cost(kw, sends, att.max_out)
                att.add_estimate(est)
                conv["spent"] += est
                conv["estimated"] += est
                info["estimated_cost_usd"], info["estimated_sends"] = round(est, 6), sends
            net = bool(info.get("network"))
            used, limit = (nets, MAX_NET_RETRIES) if net else (waits, MAX_WAITS)
            act = {K.DEAD_KEY: "rotate the key and restart the entity", K.ENTITY: "fail the entity",
                   K.WAIT: "wait and retry"}[cat]
            over = conv["spent"] >= conv["cap"]
            if cat == K.WAIT and used >= limit:
                act = f"fail the entity (still failing after {used} {'re-sends' if net else 'waits'})"
            elif cat == K.WAIT and over:
                act = "fail the attempt: with the estimated cost of lost responses it reached its cap"
            att.hist.event("error", agent=agent.name, category=cat, action=act, **info)
            if est:
                log(f"  {att.entity_id}: a response was lost ({info['class']}); charged an estimated "
                    f"{_fmt_usd(est)} (it may have been billed)")
            if cat == K.DEAD_KEY:
                raise _KeyDead(info) from None
            if cat == K.ENTITY:
                if info.get("status") is None:              # not an API error: keep the traceback
                    info["traceback"] = K.scrub("".join(traceback.format_exception(type(e), e, e.__traceback__,
                                                                                   limit=4)))[-3000:]
                raise _Failed(info) from None
            if used >= limit:
                raise _Failed(info) from None
            if over:
                raise _OverBudget() from None
            if att.run.cap_reached():
                raise _Stopped(f"the total cap of this run (--max-usd {att.run.opts.max_usd}) was reached") from None
            if net:
                nets += 1
            else:
                waits += 1
            k = waits + nets
            delay = min(BACKOFF_MAX, BACKOFF_BASE * 2 ** (k - 1)) * random.uniform(0.75, 1.25)
            if info.get("retry_after"):
                delay = max(delay, min(BACKOFF_MAX, float(info["retry_after"])))
            log(f"  {att.entity_id}: {info['class']} ({info.get('status') or 'network'}); waiting {delay:.0f} s "
                f"({nets}/{MAX_NET_RETRIES} re-sends)" if net else
                f"  {att.entity_id}: {info['class']} ({info.get('status') or 'network'}); waiting {delay:.0f} s "
                f"({waits}/{MAX_WAITS})")
            if att.run.sleep(delay):
                raise _Stopped() from None


def _serialize(messages):
    return to_jsonable(messages)


def run_tools(att, agent, resp, ctx):
    """Run the custom tool calls of a response; the tool_result blocks, in order."""
    results = []
    allowed = set(agent.custom_tools)
    for b in resp.content:
        if getattr(b, "type", None) != "tool_use":
            continue
        t0 = time.time()
        inp = b.input if isinstance(b.input, dict) else {}
        err = False
        if b.name not in allowed:
            text, err = f"unknown tool '{b.name}': this agent's tools are {', '.join(sorted(allowed))}", True
        else:
            try:
                text = TL.execute(b.name, inp, ctx)
            except TL.ToolError as e:
                text, err = str(e), True
            except Exception as e:  # noqa: BLE001  (a bug in a tool must not end the review)
                text, err = f"{b.name} failed: {type(e).__name__}: {K.scrub(e)}", True
                log(f"  {att.entity_id}: tool {b.name} raised {type(e).__name__}: {K.scrub(e)}")
        with att.lock:
            att.n_tool_calls += 1
        att.hist.tool(agent.name, b.name, inp, text, err, time.time() - t0)
        res = {"type": "tool_result", "tool_use_id": b.id, "content": text}
        if err:
            res["is_error"] = True
        results.append(res)
    return results


def _elided(msgs, elide):
    """The first request's messages for the history, with texts already stored in the start event (the dossier)
    replaced by their placeholder; history.conversation() puts them back."""
    out = _serialize(msgs)
    if elide and out and isinstance(out[0].get("content"), str):
        for ph, text in elide.items():
            if text and text in out[0]["content"]:
                out[0]["content"] = out[0]["content"].replace(text, ph)
    return out


def _over_cap(conv, cap):
    """(status, info) of a conversation that reached its cap: over_budget (final at this cap) when its own responses
    cost that much; 'failed' (retried later, like other failures) when only the estimates of lost responses took it
    there - a network problem, not the entity."""
    real, est = conv["spent"] - conv.get("estimated", 0.0), conv.get("estimated", 0.0)
    if est and real < cap:
        return "failed", {"class": "LostResponses", "message": (
            f"{_fmt_usd(real)} spent and {_fmt_usd(est)} estimated for responses lost on the way (timeouts, dropped "
            f"connections) reached the cap of {_fmt_usd(cap)}; retried by a later run")}
    return "over_budget", {"message": f"{_fmt_usd(conv['spent'])} spent" + (
        f" ({_fmt_usd(est)} of it estimated for lost responses)" if est else "") + f"; the cap is {_fmt_usd(cap)}"}


def budget_text(spent, cap, turns, max_turns, last_usd, tool):
    """The line each user message ends with, so the agent knows its spend and requests (and wraps up in time)."""
    t = BUDGET_LINE.format(spent=_fmt_usd(spent), cap=_fmt_usd(cap), turns=turns, max_turns=max_turns)
    left = max_turns - turns
    if left <= 1 or spent + last_usd >= cap:
        t += BUDGET_LAST.format(tool=tool)
    elif spent >= BUDGET_WARN * cap or left <= TURNS_WARN:
        t += BUDGET_NEAR.format(tool=tool)
    return t


def converse(att, agent, client, kw, messages, ctx, cap, elide=None):
    """The agent loop of one conversation -> (status, info). status: submitted | refused | refused_transient |
    no_review | over_budget | paused | key_dead | failed. elide: {placeholder: text stored in the start event} for
    the history's first request event. Every user message after the first ends with a budget line (spend and
    requests so far; near the cap or max_turns it asks for the final call), appended - never edited - so the
    cached prefix stays the same."""
    run = att.run
    tool = agent.submit_tool or "submit_review"
    what = "review" if tool == "submit_review" else "check"
    conv = {"spent": 0.0, "cap": cap, "estimated": 0.0}
    logged = 0
    nudged = {"end": False, "max": False}
    turns = 0
    last_usd = 0.0
    while True:
        if run.stop.is_set():
            return "paused", {"message": run.stop_reason or "stopped"}
        if run.cap_reached():
            return "paused", {"message": f"the total cap of this run (--max-usd {run.opts.max_usd}) was reached"}
        if conv["spent"] >= cap:
            return _over_cap(conv, cap)
        if turns >= agent.max_turns:
            return "no_review", {"message": f"{agent.max_turns} requests (max_turns) without a {what}"}
        if logged == 0 and elide:
            att.hist.event("request", agent=agent.name, n=turns + 1, messages=_elided(messages, elide),
                           placeholders={ph: PLACEHOLDER_SOURCE[ph] for ph in elide})
        else:
            att.hist.event("request", agent=agent.name, n=turns + 1, messages=_serialize(messages[logged:]))
        logged = len(messages)
        try:
            resp = call(att, agent, client, dict(kw, messages=messages), conv)
        except _KeyDead as e:
            return "key_dead", e.info
        except _Failed as e:
            return "failed", e.info
        except _OverBudget:
            return _over_cap(conv, cap)
        except _Stopped as e:
            return "paused", {"message": e.message or run.stop_reason or "stopped"}
        turns += 1
        d = resp.to_dict(mode="json")
        usd, summ = usage_cost(d.get("usage") or {}, kw["model"], d.get("model"))
        conv["spent"] += usd
        last_usd = usd
        att.record_response(agent, turns, d, usd, summ)
        if resp.content:                               # never an empty assistant turn (the API rejects it)
            messages.append({"role": "assistant", "content": resp.content})
        sr = resp.stop_reason
        uses = [b for b in resp.content if getattr(b, "type", None) == "tool_use"]
        if sr != "max_tokens":
            nudged["max"] = False                      # only cut-offs in a row end the conversation
        if sr == "refusal":
            sd = resp.stop_details
            cat, rm = getattr(sd, "category", None), getattr(sd, "recommended_model", None)
            info = {"category": cat, "explanation": getattr(sd, "explanation", None), "recommended_model": rm,
                    "message": f"refused ({cat or 'no category'})"}
            if rm:                                     # the fallback model was rate-limited / overloaded: transient
                info["message"] += (f"; the fallback model was unavailable, so it was not tried (a retry may "
                                    f"succeed; recommended model: {rm})")
                return "refused_transient", info
            return "refused", info
        if sr == "pause_turn":
            continue                                   # resend as is: the server resumes its tool loop
        budget = budget_text(conv["spent"], cap, turns, agent.max_turns, last_usd, tool)
        if sr == "max_tokens":
            if nudged["max"]:
                return "no_review", {"message": f"cut off at max_tokens twice in a row without a {what}"}
            nudged["max"] = True
            content = [{"type": "tool_result", "tool_use_id": b.id, "is_error": True,
                        "content": "Not run: your response was cut off at the output limit, so this call may be "
                                   "incomplete. Call it again if you still need it."} for b in uses]
            cut = f" (the {len(uses)} tool call(s) in it were not run)" if uses else ""
            content.append({"type": "text", "text": NUDGE_MAX.format(cut=cut, tool=tool) + "\n\n" + budget})
            messages.append({"role": "user", "content": content})
            continue
        if uses:                                       # tool_use (also if a tool call came with another reason)
            results = run_tools(att, agent, resp, ctx)
            nudged["end"] = False
            if ctx.submitted is not None:
                messages.append({"role": "user", "content": results})
                return "submitted", {}
            messages.append({"role": "user", "content": results + [{"type": "text", "text": budget}]})
            continue
        if nudged["end"]:
            return "no_review", {"message": f"ended its turn twice without calling {tool}"}
        nudged["end"] = True                           # (after an empty response: a second user turn in a row,
        messages.append({"role": "user", "content": [  # which the API joins to the one before)
            {"type": "text", "text": NUDGE_END.format(tool=tool, what=what) + "\n\n" + budget}]})


# ----------------------------------------------------------------------------- the run
def _make_pool(out, opts, fake):
    factory = fake.client if fake is not None else None
    pool = K.KeyPool(keys_file=opts.keys_file, env=opts.env_keys, interactive=opts.interactive,
                     client_factory=factory, default_chain=opts.default_chain and fake is None, prompt=opts.prompt)
    if fake is not None and not len(pool):
        for k in fake.keys():
            pool.add(k, "fake script")
    return pool


class _RunLock:
    """OUT/review/.run.lock: one review run per output folder at a time. It holds the pid, the host and the start
    time of the process; a lock whose process is gone (or whose pid now belongs to a younger process) is stale and
    removed - on POSIX and on Windows."""

    def __init__(self, out):
        self.path = os.path.join(review_dir(out), ".run.lock")
        self.held = False

    def acquire(self):
        for _ in range(2):
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                with os.fdopen(fd, "w") as fh:
                    json.dump({"pid": os.getpid(), "host": socket.gethostname(), "started": now(),
                               "process_start": _proc_start(os.getpid())}, fh)
                self.held = True
                return True, ""
            except FileExistsError:
                alive, who = lock_state(self.path)
                if alive:
                    return False, (f"another review run ({who}) is working on this output (lock file {self.path}; "
                                   "if you are sure no review run is going on, delete that file)")
                try:
                    os.remove(self.path)                # stale: its process is gone
                except OSError:
                    pass
        return False, f"cannot create {self.path}"

    def release(self):
        if self.held:
            try:
                os.remove(self.path)
            except OSError:
                pass
            self.held = False


def lock_state(path):
    """(alive, description) of a review/.run.lock: alive unless its process is certainly gone."""
    try:
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
        pid = int(rec.get("pid"))
    except (OSError, ValueError, TypeError, AttributeError):
        return False, "unreadable lock"
    host = rec.get("host")
    who = f"pid {pid}" + (f" on {host}" if host else "") + (f", started {rec['started']}" if rec.get("started") else "")
    if host and host != socket.gethostname():
        return True, who + " (another computer: its process cannot be checked from here)"
    if pid == os.getpid() or not _alive(pid):
        return False, who
    t0, t1 = rec.get("process_start"), _proc_start(pid)
    if isinstance(t0, (int, float)) and t1 is not None and abs(t1 - t0) > 2.0:
        return False, who + " (that pid is now another process)"
    return True, who


def _proc_start(pid):
    """The start time (epoch seconds) of process pid, where it can be told (psutil, Linux /proc, Windows); else
    None."""
    try:
        import psutil
        return float(psutil.Process(pid).create_time())
    except Exception:  # noqa: BLE001  (not installed, no such process, no access)
        pass
    if sys.platform.startswith("linux"):
        try:
            with open(f"/proc/{pid}/stat", encoding="utf-8") as fh:
                ticks = int(fh.read().rsplit(")", 1)[1].split()[19])
            with open("/proc/stat", encoding="utf-8") as fh:
                btime = next(int(x.split()[1]) for x in fh if x.startswith("btime"))
            return round(btime + ticks / os.sysconf("SC_CLK_TCK"), 2)
        except (OSError, ValueError, IndexError, StopIteration):
            return None
    if os.name == "nt":
        try:
            import ctypes
            from ctypes import wintypes
            k32 = ctypes.WinDLL("kernel32", use_last_error=True)
            k32.OpenProcess.restype = wintypes.HANDLE
            k32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
            h = k32.OpenProcess(0x1000, False, pid)                     # PROCESS_QUERY_LIMITED_INFORMATION
            if not h:
                return None
            try:
                ft = [wintypes.FILETIME() for _ in range(4)]
                if not k32.GetProcessTimes(h, *(ctypes.byref(f) for f in ft)):
                    return None
                t = (ft[0].dwHighDateTime << 32) | ft[0].dwLowDateTime    # 100-ns ticks since 1601
                return round(t / 1e7 - 11644473600.0, 2)
            finally:
                k32.CloseHandle(h)
        except Exception:  # noqa: BLE001
            return None
    return None


def _alive(pid):
    """False when process pid is certainly gone (POSIX: kill 0; Windows: OpenProcess / GetExitCodeProcess, or
    psutil when installed); True when it runs or cannot be told."""
    if pid <= 0:
        return False
    if os.name == "posix":
        try:
            os.kill(pid, 0)
            return True
        except ProcessLookupError:
            return False
        except OSError:                                 # PermissionError: it exists (another user's)
            return True
    try:
        import psutil
        return bool(psutil.pid_exists(pid))
    except ImportError:
        pass
    try:
        import ctypes
        from ctypes import wintypes
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k32.OpenProcess.restype = wintypes.HANDLE
        k32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        h = k32.OpenProcess(0x1000, False, pid)                         # PROCESS_QUERY_LIMITED_INFORMATION
        if not h:
            return ctypes.get_last_error() == 5                         # ERROR_ACCESS_DENIED: it exists
        try:
            code = wintypes.DWORD()
            if not k32.GetExitCodeProcess(h, ctypes.byref(code)):
                return True
            return code.value == 259                                    # STILL_ACTIVE
        finally:
            k32.CloseHandle(h)
    except Exception:  # noqa: BLE001  (cannot tell: assume it runs; the message names the lock file)
        return True


def _install_signals(run):
    """Ctrl-C (SIGINT), SIGTERM and, where it exists, SIGHUP (the terminal closed) stop the run cleanly. Ctrl-C at
    the key prompt interrupts it (getpass restores the terminal) and the run pauses."""
    if threading.current_thread() is not threading.main_thread():
        return {}
    old = {}

    def handler(signum, frame):
        name = signal.Signals(signum).name
        if run.stop.is_set() and signum == signal.SIGINT:
            raise KeyboardInterrupt                     # a second Ctrl-C: stop waiting
        run.request_stop(f"stopped by {name}", signum)
        log(f"{name}: no new entities start; the running ones are paused (Ctrl-C again to stop at once)")
        if run.pool.prompting_here():
            raise KeyboardInterrupt                     # out of getpass (it restores the terminal): the prompt stops
    sigs = [signal.SIGINT, signal.SIGTERM] + ([signal.SIGHUP] if hasattr(signal, "SIGHUP") else [])
    for s in sigs:
        try:
            old[s] = signal.signal(s, handler)
        except (ValueError, OSError):
            pass
    return old


def _restore_signals(old):
    for s, h in old.items():
        try:
            signal.signal(s, h)
        except (ValueError, OSError):
            pass


def _load_fake(fake):
    if fake is None:
        return None
    from . import fake as F
    return F.load(fake) if isinstance(fake, str) else fake


def _say(*a):
    """print(), scrubbed of anything shaped like a key, and quiet when the console is gone (SIGHUP, closed pipe)."""
    try:
        print(*(K.scrub(x) for x in a), flush=True)
    except (OSError, ValueError):
        pass


def recheck_cost(agents):
    """Projected USD of one --recheck (one citation-checker conversation)."""
    c = agents["checker"]
    cin, cout, _ = price(c.model, EST_CHECK_IN)
    return (EST_CHECK_IN * CACHE_WRITE_5M * cin + EST_CHECK_OUT * cout) / 1e6


def run(out, **kw):
    """Review the pending entities of OUT (see the module docstring and Options)."""
    opts = Options(**kw)
    out = os.path.abspath(out)
    say = (lambda *a: None) if opts.quiet else _say
    try:
        opts.kinds = parse_kinds(opts.kinds)
        if opts.verify not in ("llm", "ids", "off"):
            raise ValueError("--verify must be llm, ids or off")
        if int(opts.concurrency) < 1:
            raise ValueError("--concurrency must be at least 1")
        if opts.recheck and (opts.verify == "off" or opts.dry_run or opts.redo):
            raise ValueError("--recheck re-runs the verification of stored reviews: it goes with --verify llm or "
                             "ids, not with --verify off, --dry-run or --redo")
        agents = load_agents(opts)
        sel = select(out, opts.kinds, opts.only)
    except (ValueError, FileNotFoundError) as e:
        say(f"review run: {e}")
        return RunResult(EXIT_REFUSED, message=K.scrub(e))
    ledger = Ledger(out)
    states = ledger.states()
    todo, left_failed = [], 0
    for r in sel.to_dict("records"):
        s = states.get(r["entity_id"])
        if opts.recheck:
            if recheck_pending(out, s, opts.verify):
                todo.append(r)
            continue
        ok, _why = to_run(s, opts.redo, entity_cap(opts, agents[r["kind"]]), opts.retry_failed)
        if ok:
            todo.append(r)
        elif s and s["status"] in ("failed", "no_review"):
            left_failed += 1
    if opts.limit and opts.limit > 0:
        todo = todo[:int(opts.limit)]
    by_kind = Counter(r["kind"] for r in todo)
    if opts.recheck:
        est = recheck_cost(agents) * len(todo) if opts.verify == "llm" else 0.0
        say(f"{len(todo):,} stored reviews to check again (--recheck --verify {opts.verify}: the verification they "
            f"lack, not the review) of {len(sel):,} selected; projected cost {_fmt_usd(est)}")
    else:
        proj = projection(out, pd.DataFrame(todo) if todo else sel.head(0), states, agents, opts)
        est = sum(proj[k][0] * n for k, n in by_kind.items() if k in proj)
        say(f"{len(todo):,} entities to review " + "(" + ", ".join(f"{n:,} {k}s" for k, n in by_kind.items()) + ")"
            + f" of {len(sel):,} selected; projected cost {_fmt_usd(est)}")
        for k, (usd, basis) in proj.items():
            if by_kind.get(k):
                say(f"  {k}: ~{_fmt_usd(usd)} each ({basis})")
    if not todo:
        if opts.recheck:
            say(f"Nothing to check again: every selected stored review has its verification (--verify {opts.verify}).")
        else:
            say("Nothing to review: every selected entity is done (or left alone after repeated failures); --redo "
                "reviews them again." + (f" Left alone after {MAX_FAILED} failed attempts: {left_failed:,} "
                                         "(--retry-failed tries those again, and not the done ones)."
                                         if left_failed else ""))
        build_tables(out)
        return RunResult(EXIT_OK, message="nothing to do")
    if opts.dry_run:
        return dry_run(out, todo, agents, opts, est, say)
    if opts.max_usd is None and not opts.limit and not opts.no_cap:
        msg = ("Refusing to start without a spending cap: give --max-usd X (the most this run may spend, in USD) or "
               "--limit N (the number of entities), or --no-cap to run without one.")
        say(msg)
        return RunResult(EXIT_REFUSED, message=msg)
    if opts.max_usd is not None:
        per = ", ".join(f"{k} {_fmt_usd(entity_cap(opts, agents[k]))}" for k in by_kind)
        say(f"Cap: {_fmt_usd(float(opts.max_usd))} for this run; per entity {per}")
    fake = _load_fake(opts.fake)
    lit = fake.literature.install() if fake is not None and fake.literature is not None else None
    lock = _RunLock(out)
    ok, why = lock.acquire()
    if not ok:
        say(f"review run: {why}; wait for it to finish (or stop it) first.")
        if lit:
            lit.uninstall()
        return RunResult(EXIT_REFUSED, message=why)
    try:
        try:
            pool = _make_pool(out, opts, fake)
        except (OSError, ValueError) as e:              # --keys-file missing, unreadable, or a key itself
            say(f"review run: {K.scrub(e)}")
            return RunResult(EXIT_REFUSED, message=K.scrub(e))
        rn = Run(out, opts, pool, agents, fake)
        pool.on_dead = rn.save_keys
        try:
            pool.current()
        except K.AllKeysDead as e:
            msg = (f"Paused before starting: {e}. Add a key (ANTHROPIC_API_KEY, ANTHROPIC_API_KEYS or --keys-file) "
                   "and run again.")
            say(msg)
            rn.save_keys()
            return RunResult(EXIT_PAUSED, message=msg, paused=True)
        res = _run_threads(rn, todo, states, say, recheck=opts.recheck)
        if fake is not None:
            res.violations = list(fake.violations)
            log(f"Fake API: {len(fake.calls)} requests, "
                + (f"{len(fake.violations)} the API would have rejected: " + "; ".join(fake.violations[:5])
                   if fake.violations else "none the API would have rejected"))
        return res
    finally:
        lock.release()
        if lit:
            lit.uninstall()


def _process(rn, ent, prior, recheck=False):
    n = prior
    while True:
        if rn.stop.is_set():
            return
        try:
            key = rn.pool.current()
        except K.AllKeysDead:
            if not rn.stop.is_set():
                rn.keys_paused = True
            rn.request_stop("no working API key")
            return
        n += 1
        att = Attempt(rn, ent, key, n, recheck=recheck)
        with rn.lock:
            rn.active[ent["entity_id"]] = att
        try:
            status = att.recheck_review() if recheck else att.execute()
        except Exception as e:  # noqa: BLE001  (a bug: record it and go on with the next entity)
            tb = K.scrub("".join(traceback.format_exception(type(e), e, e.__traceback__, limit=6)))
            att.hist.event("error", agent=att.agent.name, **{"class": type(e).__name__, "message": tb[-3000:]})
            att.fail_sig = ("bug", type(e).__name__)
            status = att.finish("failed", error=f"{type(e).__name__}: {e}")
        if status == "key_rotated":
            rn.pool.mark_dead(key, att.extra.get("dead_reason") or "dead key")
            continue
        return


def _run_threads(rn, todo, states, say, recheck=False):
    q = deque(todo)
    t0 = time.time()

    rn.stopped_runs = {e: set(s.get("stopped_runs") or ()) for e, s in states.items() if s.get("stopped_runs")}

    def worker():
        while True:
            with rn.lock:
                if rn.stop.is_set() or rn.cap_hit or not q:
                    return
                ent = q.popleft()
                rn.started += 1
            prior = (states.get(ent["entity_id"]) or {}).get("attempts", 0)
            _process(rn, ent, prior, recheck)

    n = max(1, min(int(rn.opts.concurrency), len(todo)))
    log(f"{'Checking again' if recheck else 'Reviewing'} {len(todo):,} entities with {n} thread(s); keys: "
        + ", ".join(f"{k['key_id']} ({k['source']})" for k in rn.pool.describe()))
    old = _install_signals(rn)
    rn.pool.main_prompts = bool(old)                    # this (main) thread asks for a key when a worker needs one
    threads = [threading.Thread(target=worker, name=f"review-{i}", daemon=True) for i in range(n)]
    try:
        for t in threads:
            t.start()
        deadline = None
        while any(t.is_alive() for t in threads):
            rn.pool.serve_prompt()
            for t in threads:
                t.join(0.2 / len(threads))
            if rn.stop.is_set():
                deadline = deadline or time.time() + STOP_GRACE
                if time.time() >= deadline:
                    break
    except KeyboardInterrupt:
        rn.request_stop("stopped by Ctrl-C", signal.SIGINT)
    finally:
        rn.pool.main_prompts = False
        _restore_signals(old)
    with rn.lock:
        running = list(rn.active.values())
    for att in running:                                 # still running: submitted reviews stored, the rest paused
        att.finish_pending(rn.stop_reason or "stopped")
    if rn.systematic is not None:                       # those failures are the run's, not the entities': uncounted
        with rn.lock:
            streak = list(rn.streak)
        for sig, eid, rec in streak:
            rn.ledger.append({"entity_id": eid, "kind": rec.get("kind"), "name": rec.get("name"),
                              "run_id": rec.get("run_id"), "status": "note", "cost_usd": 0.0,
                              "note": "systematic error: the run stopped; this failure is not counted against the "
                                      "entity", "uncount_failed": True, "signature": list(sig), "finished": now(),
                              "error": rec.get("error")})
    rn.save_keys()
    try:
        n_conn, n_find = build_tables(rn.out)
    except Exception as e:  # noqa: BLE001
        n_conn = n_find = 0
        log(f"  could not build the review tables: {type(e).__name__}: {e}")
    left = len(q)
    c = dict(rn.counts)
    summary = (f"Review run: {rn.started:,} started, " + ", ".join(f"{v} {k}" for k, v in sorted(c.items()))
               + f"; spent {_fmt_usd(rn.spent)} in {(time.time() - t0) / 60:.1f} min; {left:,} not started"
               + f"; tables: {n_conn:,} connections, {n_find:,} findings")
    log(summary)
    res = RunResult(EXIT_OK, counts=c, spent_usd=rn.spent, started=rn.started, message=summary)
    if rn.systematic is not None:
        sig, err = rn.systematic
        res.exit_code, res.paused = EXIT_SYSTEMATIC, True
        again = sum(1 for g, e, _r in streak if {g, "*"} & rn.stopped_runs.get(e, set()))
        res.message = (f"STOPPED: the same error on {len(streak)} entities in a row, before any entity of this run got "
                       f"its answer ({' '.join(map(str, sig))}): {K.scrub(err)[:400].rstrip('. ')}. Most likely it "
                       "is not about these entities: fix the cause (the model's availability to your organisation, "
                       "a beta, the network ...) and run the same command again; these failures are not counted "
                       "against the entities. If it is about them after all, run the same command again as it is: "
                       "an entity that already stopped a run with this error no longer counts toward a stop, so the "
                       "next run goes on past them and counts their failures"
                       + (f" ({again} of these had stopped an earlier run with it)." if again else "."))
        log(res.message)
    elif rn.keys_paused:
        res.exit_code, res.paused = EXIT_PAUSED, True
        res.message = (f"PAUSED: {rn.stop_reason}. The unfinished entities stay pending: add a key "
                       "(ANTHROPIC_API_KEY, ANTHROPIC_API_KEYS or --keys-file) and run the same command again.")
        log(res.message)
    elif rn.stop_signal is not None:
        res.exit_code = {signal.SIGTERM: EXIT_SIGTERM, getattr(signal, "SIGHUP", -1): EXIT_SIGHUP}.get(
            rn.stop_signal, EXIT_SIGINT)
        res.paused = True
        res.message = f"Stopped ({rn.stop_reason}); run the same command again to resume."
        log(res.message)
    elif rn.cap_hit:
        res.message = summary + f" -- stopped at the cap (--max-usd {rn.opts.max_usd})"
    return res


# ----------------------------------------------------------------------------- dry run
def dry_run(out, todo, agents, opts, est, say):
    d = review_dir(out, "dry_run")
    rows = []
    for ent in todo:
        k = ent["kind"]
        try:
            dos = D.build(out, k, ent["entity_id"])
        except Exception as e:  # noqa: BLE001
            rows.append({"entity_id": ent["entity_id"], "error": f"{type(e).__name__}: {e}"})
            continue
        a = agents[k]
        kw = build_request(a, opts.web, opts.web_max_uses)
        kw["messages"] = [{"role": "user", "content": dos.user_message()}]
        base = os.path.join(review_dir(out, "dry_run", k), safe_filename(dos.name))
        D.write_text(base + ".dossier.md", dos.text)
        write_json({"call": "client.beta.messages.stream", "agent": a.name, "entity_id": dos.entity_id,
                    "dossier_sha256": dos.sha256, "system_sha256": a.system_sha256, "request": kw},
                   base + ".request.json")
        rows.append({"entity_id": dos.entity_id, "kind": k, "name": dos.name, "agent": a.name, "model": a.model,
                     "dossier_chars": len(dos.text), "system_chars": len(a.system),
                     "projected_usd": round(heuristic_cost(a, a.model, a.effort, len(dos.text), opts.web, opts.verify,
                                                           agents["checker"]), 4),
                     "request": os.path.relpath(base + ".request.json", out).replace(os.sep, "/")})
    write_json({"written": now(), "entities": rows, "projected_usd": round(est, 2), "verify": opts.verify,
                "web": opts.web}, os.path.join(d, "summary.json"))
    say(f"Dry run: {len(rows):,} dossiers and first requests written to {d} (nothing was sent; projected cost "
        f"{_fmt_usd(est)})")
    return RunResult(EXIT_OK, message="dry run", counts={"dry_run": len(rows)})


# ----------------------------------------------------------------------------- plan / status / tables
def queue_frame(out, sel, states, agents, opts):
    q = sel.copy()
    st, att, cost, run_it, why = [], [], [], [], []
    for r in q.to_dict("records"):
        s = states.get(r["entity_id"])
        ok, w = to_run(s, False, entity_cap(opts, agents[r["kind"]]))
        st.append(s["status"] if s else "pending")
        att.append(int(s["attempts"]) if s else 0)
        cost.append(float(s["cost_usd"]) if s else 0.0)
        run_it.append(ok)
        why.append(w)
    q["status"], q["attempts"], q["cost_usd"], q["to_review"], q["left_because"] = st, att, cost, run_it, why
    return q


def plan(out, kinds=KINDS, only=None, say=print, **kw):
    opts = Options(kinds=kinds, only=only, **kw)
    agents = load_agents(opts)
    sel = select(out, parse_kinds(kinds), only)
    states = Ledger(out).states()
    q = queue_frame(out, sel, states, agents, opts)
    p = os.path.join(review_dir(out), "queue.parquet")
    write_parquet(q, p)
    pend = q[q["to_review"]]
    proj = projection(out, pend if len(pend) else q.head(0), states, agents, opts)
    say(f"Review queue: {p}")
    _print_counts(q, say)
    total = 0.0
    for k in KINDS:
        n = int((pend["kind"] == k).sum())
        if n and k in proj:
            total += n * proj[k][0]
            say(f"  {k}: {n:,} to review x ~{_fmt_usd(proj[k][0])} = {_fmt_usd(n * proj[k][0])}   ({proj[k][1]})")
    say(f"Projected cost of the {len(pend):,} entities to review: {_fmt_usd(total)} (model "
        f"{agents['gene'].model}, effort {agents['gene'].effort}, verify {opts.verify})")
    return q


def _print_counts(q, say):
    tab = q.groupby(["kind", "status"]).size().unstack(fill_value=0)
    tab = tab.reindex([k for k in KINDS if k in tab.index])
    say("  " + tab.to_string().replace("\n", "\n  "))


def status(out, tables=False, say=print, **kw):
    opts = Options(**kw)
    agents = load_agents(opts)
    led = Ledger(out)
    states = led.states()
    qp = os.path.join(out, "review", "queue.parquet")
    try:
        sel = pd.read_parquet(qp)[["kind", "name", "entity_id", "label", "priority"]] if os.path.exists(qp) \
            else select(out, KINDS)
    except Exception:  # noqa: BLE001
        sel = select(out, KINDS)
    q = queue_frame(out, sel, states, agents, opts)
    extra = sorted(set(states) - set(q["entity_id"]))
    say(f"Literature review of {out}")
    if not len(q):
        say("  no entities")
    else:
        _print_counts(q, say)
    if extra:
        say(f"  ({len(extra)} reviewed entities are not in the queue: {', '.join(extra[:5])} ...)")
    rows = led.read()
    spend = Counter()
    est = 0.0
    for r in rows:
        spend[r.get("kind") or "?"] += float(r.get("cost_usd") or 0.0)
        est += float(r.get("estimated_usd") or 0.0)
    n_att = sum(1 for r in rows if not r.get("note"))
    say(f"Spent: {_fmt_usd(sum(spend.values()))} in {n_att:,} attempts"
        + (" (" + ", ".join(f"{k} {_fmt_usd(v)}" for k, v in sorted(spend.items())) + ")" if spend else "")
        + (f"; {_fmt_usd(est)} of it estimated for responses lost on the way" if est else ""))
    open_usd = _unfinished_spend(out, rows)
    if open_usd[0]:
        say(f"  plus {_fmt_usd(open_usd[1])} in {open_usd[0]} attempt(s) without a ledger line (running now, or their "
            "run was killed): in their history files only")
    pend = q[q["to_review"]]
    if len(pend):
        proj = projection(out, pend, states, agents, opts)
        tot = sum(proj[k][0] * int((pend["kind"] == k).sum()) for k in proj)
        say(f"Projected cost of the rest ({len(pend):,} entities): {_fmt_usd(tot)}   ("
            + "; ".join(f"{k}: ~{_fmt_usd(v[0])} each, {v[1]}" for k, v in proj.items()) + ")")
    else:
        say("Nothing left to review.")
    ks = read_json_safe(os.path.join(out, "review", "keys_state.json")) or {}
    dead = [k for k in ks.get("keys") or [] if k.get("dead")]
    say("Dead keys: " + (", ".join(f"{k['key_id']} ({k.get('reason', '')[:80]})" for k in dead) if dead else "none")
        + (f"   (as of {ks.get('updated')})" if ks.get("updated") else ""))
    lp = os.path.join(out, "review", ".run.lock")
    if os.path.exists(lp):
        alive, who = lock_state(lp)
        if alive:
            say(f"A review run ({who}) holds {lp}; if you are sure none is going on, delete that file")
        else:
            say(f"{lp} is stale ({who}: that process is gone): the next run removes it (or delete it)")
    rc = sum(1 for st in states.values() if recheck_pending(out, st, opts.verify))
    if rc:
        say(f"{rc:,} stored reviews lack part of their verification (--verify {opts.verify}): "
            f"`review run --recheck --verify {opts.verify}` completes it without reviewing them again")
    if tables:
        n_c, n_f = build_tables(out)
        say(f"Tables: {n_c:,} connection verdicts -> review/connections.parquet, {n_f:,} findings -> "
            "review/findings.parquet")
    return q


def _unfinished_spend(out, rows):
    """(n, USD) of history files with responses but no end event and no ledger line (an attempt running now, or one
    whose run was killed). Only the files the ledger does not name are read."""
    known = {r.get("history") for r in rows}
    n, usd = 0, 0.0
    for f in glob.glob(os.path.join(out, "review", "history", "*", "*", "*.jsonl")):
        rel = os.path.relpath(f, out).replace(os.sep, "/")
        if rel in known:
            continue
        ev = read_jsonl(f)
        if any(e.get("event") == "end" for e in ev):
            continue
        c = sum(float(e.get("cost_usd") or 0.0) for e in ev if e.get("event") == "response")
        c += sum(float(e.get("estimated_cost_usd") or 0.0) for e in ev if e.get("event") == "error")
        if c:
            n, usd = n + 1, usd + c
    return n, usd


def read_json_safe(p):
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


CONN_COLS = ["entity_id", "kind", "name", "partner", "partner_kind", "partner_col", "verdict", "citations",
             "n_citations", "retracted", "check", "unverified", "check_status", "shown_verdict", "model", "run_id",
             "reviewed"]
FIND_COLS = ["entity_id", "kind", "name", "section", "item", "title", "detail", "data_evidence", "confidence",
             "source", "citations", "n_citations", "retracted", "check", "unverified", "check_status",
             "shown_verdict", "model", "run_id", "reviewed"]
SECTIONS = {"established": ("partner_or_topic", "relation", "data_evidence"),
            "unexpected": ("observation", "why_unexpected", "data_evidence"),
            "missing": ("expected_connection", "likely_reason", "data_status"),
            "contradicted": ("claim", None, "data_evidence")}


def _gene_cols(out):
    try:
        g = D.context(out).genes()
    except Exception:  # noqa: BLE001
        return {}
    m = {}
    for c, s, lab in zip(g["col"], g.get("symbol", g["label"]), g["label"]):
        for x in (s, lab):
            if isinstance(x, str) and x:
                m.setdefault(x.upper(), int(c))
    return m


def _annotated(review):
    """A copy of a stored review with check_status / shown_verdict on its items (verify.annotate), for reviews
    stored before those fields existed: their ids count as checked when the id check ran and reached the
    services."""
    import copy
    r = copy.deepcopy(review)
    ids = ((r.get("verification") or {}).get("ids") or {})
    u = ids.get("unchecked")
    n_un = len(u) if isinstance(u, (list, tuple)) else int(u or 0)
    ok = bool(ids) and not ids.get("error") and not n_un
    try:
        V.annotate(r, ids_checked=True if ok else None)
    except Exception:  # noqa: BLE001  (an older verify module, an odd file: the columns stay empty)
        pass
    return r


def _retracted(it):
    """An item's retracted citations (verify.check_ids: "retracted_citations") in the form of the 'citations' column,
    'PMID:1;DOI:x'; '' when it cites none - also for a review stored before retractions were recorded."""
    r = it.get("retracted_citations")
    if isinstance(r, str):
        r = r.split(";")
    return ";".join(str(x).strip() for x in r if str(x).strip()) if isinstance(r, (list, tuple)) else ""


def build_tables(out):
    """OUT/review/connections.parquet (one row per connection verdict) and findings.parquet (one row per item of
    established / unexpected / missing / contradicted, and per open question) from the stored reviews. 'citations'
    and 'retracted' (the retracted papers among them) are 'PMID:1;DOI:x' strings."""
    rd = os.path.join(out, "review", "reviews")
    conn, find = [], []
    cols = None
    for kind in KINDS:
        for f in sorted(glob.glob(os.path.join(rd, kind, "*.json"))):
            r = read_json_safe(f)
            if not isinstance(r, dict):
                continue
            meta = r.get("meta") or {}
            if any("check_status" not in it for it in r.get("connection_verdicts") or []):
                r = _annotated(r)                      # a review stored before check_status existed
            base = {"entity_id": meta.get("entity_id"), "kind": kind, "name": meta.get("name"),
                    "model": meta.get("model"), "run_id": meta.get("run_id"), "reviewed": meta.get("reviewed")}
            for it in r.get("connection_verdicts") or []:
                p = str(it.get("partner") or "")
                pk = p.split(":", 1)[0] if ":" in p and p.split(":", 1)[0] in ("drug", "line") else "gene"
                pc = None
                if pk == "gene":
                    if cols is None:
                        cols = _gene_cols(out)
                    pc = cols.get(p.upper())
                cits = it.get("citations") or []
                conn.append({**base, "partner": p, "partner_kind": pk, "partner_col": pc,
                             "verdict": it.get("verdict"), "citations": ";".join(cits), "n_citations": len(cits),
                             "retracted": _retracted(it), "check": (it.get("check") or {}).get("verdict", ""),
                             "unverified": bool(it.get("unverified")), "check_status": it.get("check_status") or "",
                             "shown_verdict": it.get("shown_verdict") or it.get("verdict") or ""})
            for sec, (tk, dk, ek) in SECTIONS.items():
                for i, it in enumerate(r.get(sec) or []):
                    cits = it.get("citations") or []
                    detail = it.get(dk, "") if dk else ""
                    if sec == "unexpected" and it.get("literature_checked"):
                        detail = (detail + " | searched: " + "; ".join(it["literature_checked"])).strip(" |")
                    find.append({**base, "section": sec, "item": i, "title": it.get(tk, ""), "detail": detail,
                                 "data_evidence": it.get(ek, ""), "confidence": it.get("confidence", ""),
                                 "source": it.get("source", ""), "citations": ";".join(cits),
                                 "n_citations": len(cits), "retracted": _retracted(it),
                                 "check": (it.get("check") or {}).get("verdict", ""),
                                 "unverified": bool(it.get("unverified")),
                                 "check_status": it.get("check_status") or "",
                                 "shown_verdict": it.get("shown_verdict") or (sec if it.get("check_status") else "")})
            for i, qn in enumerate(r.get("open_questions") or []):
                find.append({**base, "section": "open_questions", "item": i, "title": qn, "detail": "",
                             "data_evidence": "", "confidence": "", "source": "", "citations": "", "n_citations": 0,
                             "retracted": "", "check": "", "unverified": False, "check_status": "",
                             "shown_verdict": ""})
    c = pd.DataFrame(conn, columns=CONN_COLS)
    c["partner_col"] = c["partner_col"].astype("Int64")
    write_parquet(c, os.path.join(review_dir(out), "connections.parquet"))
    write_parquet(pd.DataFrame(find, columns=FIND_COLS), os.path.join(review_dir(out), "findings.parquet"))
    return len(conn), len(find)


def history_events(out, rel):
    """The events of one history file (rel = the path stored in the ledger / review meta)."""
    return read_jsonl(os.path.join(out, rel))


# ----------------------------------------------------------------------------- CLI
def cli(a):
    """`python -m tahoemap review ACTION` (cli.py hands over its parsed arguments). Returns the exit code."""
    names = list(getattr(a, "names", None) or [])
    action = names[0] if names else "status"
    out = a.out
    if action not in ("plan", "run", "status", "tables"):
        _say(f"review: unknown action '{action}'; use plan, run, status or tables")
        return EXIT_REFUSED
    if not os.path.isdir(os.path.join(out, "tables")):
        _say(f"review: {out} holds no finished run (no tables/ folder); give --out with a tahoemap output folder")
        return EXIT_REFUSED
    common = {"model": a.model, "effort": a.effort, "verify": a.verify, "web": a.web,
              "web_max_uses": a.web_max_uses, "per_entity_usd": a.per_entity_usd}
    try:
        if action == "plan":
            plan(out, kinds=a.kinds, only=a.only, **common)
            return EXIT_OK
        if action == "status":
            status(out, tables=a.tables, **common)
            return EXIT_OK
        if action == "tables":
            n_c, n_f = build_tables(out)
            print(f"{n_c:,} connection verdicts -> {os.path.join(out, 'review', 'connections.parquet')}\n"
                  f"{n_f:,} findings -> {os.path.join(out, 'review', 'findings.parquet')}")
            return EXIT_OK
    except (ValueError, FileNotFoundError) as e:
        _say(f"review {action}: {e}")
        return EXIT_REFUSED
    from ..tlib import start_run_log
    start_run_log(os.path.join(review_dir(out), "review.log"), "tahoemap review run")
    try:
        res = run(out, kinds=a.kinds, only=a.only, limit=a.limit, max_usd=a.max_usd, concurrency=a.concurrency,
                  keys_file=a.keys_file, redo=a.redo, dry_run=a.dry_run, fake=a.fake, no_cap=a.no_cap,
                  retry_failed=getattr(a, "retry_failed", False), recheck=getattr(a, "recheck", False), **common)
    except KeyboardInterrupt:                  # a second Ctrl-C: stopped at once (the ledger has what finished)
        _say("review run: stopped at once (second Ctrl-C). Finished reviews are kept; run the same command again to "
             "resume.")
        return EXIT_SIGINT
    return res.exit_code                       # (run() has said why)
