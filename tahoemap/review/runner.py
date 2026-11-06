"""runner - review runs: which entities, the agent loop, verification, costs, the queue, status and tables.

    run(out, **options) -> RunResult      review the pending entities (see Options); RunResult.exit_code:
                                          0 finished (or stopped at --limit / --max-usd), 2 refused to start
                                          (no cap, bad option), 3 paused: no working API key (add one and run
                                          again), 130 / 143 stopped by Ctrl-C / SIGTERM (run again to resume)
    plan(out, kinds, only)                OUT/review/queue.parquet (entities in priority order, with their state)
                                          + counts and the projected cost
    status(out, tables=False)             counts by status and kind, spend, projected cost of the rest, dead keys
    build_tables(out)                     OUT/review/connections.parquet and findings.parquet from the reviews
    cli(a)                                `python -m tahoemap review plan|run|status|tables` (cli.py)

The agent loop (docs/DESIGN-review-and-physics.md, Part 2, "Surface"): client.beta.messages.create with the agent's
system prompt (agent + skills, cache_control), its tools (custom, strict, then web_search / web_fetch), output_config
effort, adaptive thinking (thinking omitted), fallbacks="default" with the server-side-fallback-2026-07-01 beta, and
top-level automatic caching. Each response.content is appended unchanged. stop_reason: tool_use -> our tools run and
all results go back in one user message (a valid submit_review ends the loop); pause_turn -> resent as is; refusal ->
status refused (stop_details.category); max_tokens -> one nudge (cut-off tool calls answered as not run); end_turn
without a review -> one nudge, then no_review. The citation checker (verify.py) runs the same loop.

Keys and errors (keys.py): a dead key (401, 402 / billing_error, 403, spend limit, organization on hold) ends the
attempt as key_rotated and the entity restarts from the beginning with the next key; rate limits, overload, 5xx and
network errors wait (after the SDK's own retries: exponential backoff with jitter up to 10 minutes, Retry-After
honoured) and retry the same request; other errors fail the entity. With every key dead the run pauses: on a
terminal it asks for a new key (getpass), else it stops with exit code 3 and the unfinished entities stay pending.

Resume: the latest ledger line of an entity is its state. done and refused are final (unless --redo); failed and
no_review are retried up to 2 more times; over_budget only with a higher per-entity cap; paused and key_rotated
entities start again from the beginning. Nothing is redone that the ledger marks final.

Models and effort: the agent files' (reviewers claude-opus-5-5 / high, checker claude-opus-5-5 / medium); --model and
--effort set the reviewers, or per agent with AGENT=VALUE,... (gene, drug, line, checker, reviewers, all).

Costs (USD; PRICES): from response.usage, per usage.iterations entry at that entry's model when present (a fallback
model bills at its own price), cache writes at 1.25x input (2x for 1-hour entries), cache reads at the model's
cache-read price (claude-opus-5-5: $0.20 per million, 0.05x input), web searches $0.01 each. --per-entity-usd caps
one attempt (a request is not started once the attempt has spent it; the citation checker has its own cap, its
agent's max_usd); --max-usd caps this run (no new entity starts and running ones pause once it is reached). Without
--max-usd or --limit the runner refuses to start unless --no-cap is given; it always prints the projected cost first.

Tests: `--fake SCRIPT` (fake.py) answers every request through the real SDK from a script, with no key and no
network; tests/test_review.py drives every path above with it.
"""

import glob
import hashlib
import json
import os
import random
import signal
import subprocess
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
        pool.stopping = self.stop.is_set

    def outcome(self, att, status, rec):
        """Called once per finished attempt: tracks the same error on entity after entity (keys_state#1)."""
        with self.lock:
            sig = att.fail_sig if status == "failed" else None
            if sig is not None:
                if self.streak and self.streak[-1][0] != sig:
                    self.streak = []
                self.streak.append((sig, att.entity_id, rec))
                if len(self.streak) >= SYSTEMATIC_N and self.systematic is None:
                    self.systematic = (sig, rec.get("error") or "")
            elif status in ("done", "refused", "no_review", "over_budget"):
                self.streak = []
        if self.systematic is not None and sig is not None and not self.stop.is_set():
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
    """One try at one entity with one key: the conversation(s), its history file and its ledger line."""

    def __init__(self, run, ent, key, n):
        self.run, self.ent, self.key, self.n = run, ent, key, n
        self.kind, self.name, self.entity_id = ent["kind"], ent["name"], ent["entity_id"]
        self.run_id = new_run_id()
        self.hist = History(run.out, self.kind, self.name, self.run_id)
        self.started = now()
        self.cost = 0.0
        self.tok = Counter()
        self.n_requests = 0
        self.n_tool_calls = 0
        self.models = []
        self.lock = threading.RLock()
        self.finalized = False
        self.agent = run.agents[self.kind]
        self.cap = entity_cap(run.opts, self.agent)
        self.extra = {}

    # -------------------------------------------------------------- bookkeeping
    def add(self, usd, summ, model):
        with self.lock:
            self.cost += usd
            self.tok.update(summ)
            self.n_requests += 1
            if model and model not in self.models:
                self.models.append(model)
        self.run.add_spend(usd)

    def finish(self, status, error=None, store=None, **extra):
        """Write the ledger line and the history's end event, once (the first caller wins). `store` runs first,
        under the same lock (the review files of a done attempt). Returns the status written, or None."""
        with self.lock:
            if self.finalized:
                return None
            self.finalized = True
            if store is not None:
                store()
            err = K.scrub(error)[:2000] if error else None
            rec = {"entity_id": self.entity_id, "kind": self.kind, "name": self.name, "run_id": self.run_id,
                   "agent": self.agent.name, "model": self.agent.model, "status": status,
                   "cost_usd": round(self.cost, 6), "n_requests": self.n_requests, "n_tool_calls": self.n_tool_calls,
                   "key_id": self.key.key_id, "started": self.started, "finished": now(), "error": err,
                   "cap_usd": self.cap, "attempt": self.n, "served_models": list(self.models),
                   "history": self.hist.rel, **{k: int(self.tok.get(k, 0)) for k in (
                       "input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens",
                       "web_searches", "web_fetches")}}
            rec.update(self.extra)
            rec.update(extra)
            self.run.ledger.append(rec)
            self.hist.event("end", status=status, error=err, totals={
                "cost_usd": round(self.cost, 6), "n_requests": self.n_requests, "n_tool_calls": self.n_tool_calls,
                **{k: int(v) for k, v in self.tok.items()}}, **{k: v for k, v in extra.items()})
        with self.run.lock:
            self.run.counts[status] += 1
            self.run.active.pop(self.entity_id, None)
        if not self.run.opts.quiet:
            log(f"  {self.entity_id} ({self.name}): {status}  {_fmt_usd(self.cost)}"
                + (f"  [{err[:160]}]" if err and status != "done" else ""))
        return status

    # -------------------------------------------------------------- the attempt
    def execute(self):
        r = self.run
        try:
            dos = D.build(r.out, self.kind, self.entity_id)
        except Exception as e:  # noqa: BLE001
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
        return self.finish(status, error=_info_text(info))

    def complete(self, dos, ctx):
        """Verification, then the review JSON + note, then the ledger line."""
        r = self.run
        review = ctx.submitted
        mode = r.opts.verify
        report, llm = None, None
        checked = review
        if mode in ("ids", "llm"):
            try:
                checked, report = V.check_ids(review, ctx)
            except Exception as e:  # noqa: BLE001
                report = {"error": K.scrub(f"{type(e).__name__}: {e}")}
                self.hist.event("error", agent="verify", **{"class": type(e).__name__, "message": report["error"]})
        if mode == "llm" and not r.stop.is_set():
            checked, llm = self.citation_check(checked, ctx)
        elif mode == "llm":
            llm = {"status": "not run: the run was stopping"}
        final = dict(checked)
        final["verification"] = {"mode": mode, "ids": report, "llm": llm, "counts": V.counts(checked)}
        final["meta"] = {
            "entity_id": self.entity_id, "kind": self.kind, "name": self.name, "agent": self.agent.name,
            "model": self.agent.model, "served_models": list(self.models), "effort": self.agent.effort,
            "checker_model": r.agents["checker"].model if mode == "llm" else None, "run_id": self.run_id,
            "key_id": self.key.key_id, "reviewed": now(), "cost_usd": round(self.cost, 6),
            "tokens": {k: int(v) for k, v in self.tok.items()}, "n_requests": self.n_requests,
            "n_tool_calls": self.n_tool_calls, "history": self.hist.rel, "dossier_sha256": dos.sha256,
            "system_sha256": self.agent.system_sha256, "code_version": r.code,
            "not_retrieved": list(ctx.notes.get("not_retrieved") or [])}
        paths = review_paths(r.out, self.kind, self.name)

        def store():
            write_json(final, paths["review"])
            D.write_text(paths["note"], final.get("note_markdown") or "")
        check = (llm or {}).get("status") if mode == "llm" else mode
        return self.finish("done", store=store, verify=mode, check_status=check,
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
                r.keys_paused = True
                r.request_stop("no working API key")
                return checked, {"status": "not run: no working API key"}
        if status == "submitted":
            out, summ = V.apply_check(checked, ctx.submitted)
            summ["status"] = "done"
            return out, summ
        return checked, {"status": status, "error": _info_text(info)}


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
def call(att, agent, client, kw):
    """One request, with the wait-class errors retried here (after the SDK's own retries). Raises _KeyDead,
    _Failed or _Stopped."""
    waits = 0
    while True:
        try:
            return client.beta.messages.create(**kw)
        except Exception as e:  # noqa: BLE001  (classified below)
            cat, info = K.classify(e)
            act = {K.DEAD_KEY: "rotate the key and restart the entity", K.ENTITY: "fail the entity",
                   K.WAIT: "wait and retry"}[cat]
            if cat == K.WAIT and waits >= MAX_WAITS:
                act = f"fail the entity (still failing after {waits} waits)"
            att.hist.event("error", agent=agent.name, category=cat, action=act, **info)
            if cat == K.DEAD_KEY:
                raise _KeyDead(info) from None
            if cat == K.ENTITY:
                if info.get("status") is None:              # not an API error: keep the traceback
                    info["traceback"] = K.scrub("".join(traceback.format_exception(type(e), e, e.__traceback__,
                                                                                   limit=4)))[-3000:]
                raise _Failed(info) from None
            if waits >= MAX_WAITS:
                raise _Failed(info) from None
            waits += 1
            delay = min(BACKOFF_MAX, BACKOFF_BASE * 2 ** (waits - 1)) * random.uniform(0.75, 1.25)
            if info.get("retry_after"):
                delay = max(delay, min(BACKOFF_MAX, float(info["retry_after"])))
            log(f"  {att.entity_id}: {info['class']} ({info.get('status') or 'network'}); waiting {delay:.0f} s "
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


def converse(att, agent, client, kw, messages, ctx, cap, elide=None):
    """The agent loop of one conversation -> (status, info). status: submitted | refused | no_review |
    over_budget | paused | key_dead | failed. elide: {placeholder: text stored in the start event} for the
    history's first request event."""
    run = att.run
    tool = agent.submit_tool or "submit_review"
    what = "review" if tool == "submit_review" else "check"
    spent = 0.0
    logged = 0
    nudged = {"end": False, "max": False}
    turns = 0
    while True:
        if run.stop.is_set():
            return "paused", {"message": run.stop_reason or "stopped"}
        if run.cap_reached():
            return "paused", {"message": f"the total cap of this run (--max-usd {run.opts.max_usd}) was reached"}
        if spent >= cap:
            return "over_budget", {"message": f"{_fmt_usd(spent)} spent; the cap is {_fmt_usd(cap)}"}
        if turns >= agent.max_turns:
            return "no_review", {"message": f"{agent.max_turns} requests (max_turns) without a {what}"}
        if logged == 0 and elide:
            att.hist.event("request", agent=agent.name, n=turns + 1, messages=_elided(messages, elide),
                           placeholders={ph: PLACEHOLDER_SOURCE[ph] for ph in elide})
        else:
            att.hist.event("request", agent=agent.name, n=turns + 1, messages=_serialize(messages[logged:]))
        logged = len(messages)
        try:
            resp = call(att, agent, client, dict(kw, messages=messages))
        except _KeyDead as e:
            return "key_dead", e.info
        except _Failed as e:
            return "failed", e.info
        except _Stopped:
            return "paused", {"message": run.stop_reason or "stopped"}
        turns += 1
        d = resp.to_dict(mode="json")
        usd, summ = usage_cost(d.get("usage") or {}, kw["model"], d.get("model"))
        spent += usd
        att.add(usd, summ, d.get("model"))
        att.hist.event("response", agent=agent.name, n=turns, response=d, usage=d.get("usage"), cost_usd=round(usd, 6),
                       attempt_cost_usd=round(att.cost, 6))
        messages.append({"role": "assistant", "content": resp.content})
        sr = resp.stop_reason
        uses = [b for b in resp.content if getattr(b, "type", None) == "tool_use"]
        if sr == "refusal":
            sd = resp.stop_details
            return "refused", {"category": getattr(sd, "category", None),
                               "explanation": getattr(sd, "explanation", None),
                               "message": f"refused ({getattr(sd, 'category', None) or 'no category'})"}
        if sr == "pause_turn":
            continue                                   # resend as is: the server resumes its tool loop
        if sr == "max_tokens":
            if nudged["max"]:
                return "no_review", {"message": f"cut off at max_tokens twice without a {what}"}
            nudged["max"] = True
            content = [{"type": "tool_result", "tool_use_id": b.id, "is_error": True,
                        "content": "Not run: your response was cut off at the output limit, so this call may be "
                                   "incomplete. Call it again if you still need it."} for b in uses]
            cut = f" (the {len(uses)} tool call(s) in it were not run)" if uses else ""
            content.append({"type": "text", "text": NUDGE_MAX.format(cut=cut, tool=tool)})
            messages.append({"role": "user", "content": content})
            continue
        if uses:                                       # tool_use (also if a tool call came with another reason)
            results = run_tools(att, agent, resp, ctx)
            messages.append({"role": "user", "content": results})
            if ctx.submitted is not None:
                return "submitted", {}
            continue
        if nudged["end"]:
            return "no_review", {"message": f"ended its turn twice without calling {tool}"}
        nudged["end"] = True
        messages.append({"role": "user", "content": [{"type": "text",
                                                      "text": NUDGE_END.format(tool=tool, what=what)}]})


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
    """OUT/review/.run.lock: one review run per output folder at a time."""

    def __init__(self, out):
        self.path = os.path.join(review_dir(out), ".run.lock")
        self.held = False

    def acquire(self):
        for _ in range(2):
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                with os.fdopen(fd, "w") as fh:
                    json.dump({"pid": os.getpid(), "started": now()}, fh)
                self.held = True
                return True, ""
            except FileExistsError:
                try:
                    with open(self.path, encoding="utf-8") as fh:
                        pid = int(json.load(fh).get("pid"))
                except (OSError, ValueError, TypeError, AttributeError):
                    pid = None
                if pid and pid != os.getpid() and _alive(pid):
                    return False, f"another review run (pid {pid}) is working on this output"
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


def _alive(pid):
    if os.name != "posix":
        return True
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def _install_signals(run):
    if threading.current_thread() is not threading.main_thread():
        return {}
    old = {}

    def handler(signum, frame):
        name = signal.Signals(signum).name
        if run.stop.is_set() and signum == signal.SIGINT:
            raise KeyboardInterrupt                     # a second Ctrl-C: stop waiting
        run.request_stop(f"stopped by {name}", signum)
        log(f"{name}: no new entities start; the running ones are paused (Ctrl-C again to stop at once)")
    for s in (signal.SIGINT, signal.SIGTERM):
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


def run(out, **kw):
    """Review the pending entities of OUT (see the module docstring and Options)."""
    opts = Options(**kw)
    out = os.path.abspath(out)
    say = (lambda *a: None) if opts.quiet else print
    try:
        opts.kinds = parse_kinds(opts.kinds)
        if opts.verify not in ("llm", "ids", "off"):
            raise ValueError("--verify must be llm, ids or off")
        if int(opts.concurrency) < 1:
            raise ValueError("--concurrency must be at least 1")
        agents = load_agents(opts)
        sel = select(out, opts.kinds, opts.only)
    except (ValueError, FileNotFoundError) as e:
        say(f"review run: {e}")
        return RunResult(EXIT_REFUSED, message=str(e))
    ledger = Ledger(out)
    states = ledger.states()
    todo = []
    for r in sel.to_dict("records"):
        ok, _why = to_run(states.get(r["entity_id"]), opts.redo, entity_cap(opts, agents[r["kind"]]))
        if ok:
            todo.append(r)
    if opts.limit and opts.limit > 0:
        todo = todo[:int(opts.limit)]
    by_kind = Counter(r["kind"] for r in todo)
    proj = projection(out, pd.DataFrame(todo) if todo else sel.head(0), states, agents, opts)
    est = sum(proj[k][0] * n for k, n in by_kind.items() if k in proj)
    say(f"{len(todo):,} entities to review " + "(" + ", ".join(f"{n:,} {k}s" for k, n in by_kind.items()) + ")"
        + f" of {len(sel):,} selected; projected cost {_fmt_usd(est)}")
    for k, (usd, basis) in proj.items():
        if by_kind.get(k):
            say(f"  {k}: ~{_fmt_usd(usd)} each ({basis})")
    if not todo:
        say("Nothing to review: every selected entity is done (or left alone after repeated failures); --redo "
            "reviews them again.")
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
        except OSError as e:                            # --keys-file missing or unreadable
            say(f"review run: {e}")
            return RunResult(EXIT_REFUSED, message=str(e))
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
        res = _run_threads(rn, todo, states, say)
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


def _process(rn, ent, prior):
    n = prior
    while True:
        if rn.stop.is_set():
            return
        try:
            key = rn.pool.current()
        except K.AllKeysDead:
            rn.keys_paused = True
            rn.request_stop("no working API key")
            return
        n += 1
        att = Attempt(rn, ent, key, n)
        with rn.lock:
            rn.active[ent["entity_id"]] = att
        try:
            status = att.execute()
        except Exception as e:  # noqa: BLE001  (a bug: record it and go on with the next entity)
            tb = K.scrub("".join(traceback.format_exception(type(e), e, e.__traceback__, limit=6)))
            att.hist.event("error", agent=att.agent.name, **{"class": type(e).__name__, "message": tb[-3000:]})
            status = att.finish("failed", error=f"{type(e).__name__}: {e}")
        if status == "key_rotated":
            rn.pool.mark_dead(key, att.extra.get("dead_reason") or "dead key")
            continue
        return


def _run_threads(rn, todo, states, say):
    q = deque(todo)
    t0 = time.time()

    def worker():
        while True:
            with rn.lock:
                if rn.stop.is_set() or rn.cap_hit or not q:
                    return
                ent = q.popleft()
                rn.started += 1
            prior = (states.get(ent["entity_id"]) or {}).get("attempts", 0)
            _process(rn, ent, prior)

    n = max(1, min(int(rn.opts.concurrency), len(todo)))
    log(f"Reviewing {len(todo):,} entities with {n} thread(s); keys: "
        + ", ".join(f"{k['key_id']} ({k['source']})" for k in rn.pool.describe()))
    old = _install_signals(rn)
    threads = [threading.Thread(target=worker, name=f"review-{i}", daemon=True) for i in range(n)]
    try:
        for t in threads:
            t.start()
        while any(t.is_alive() for t in threads):
            for t in threads:
                t.join(0.2)
            if rn.stop.is_set() and not rn.keys_paused:
                deadline = time.time() + STOP_GRACE
                while any(t.is_alive() for t in threads) and time.time() < deadline:
                    for t in threads:
                        t.join(0.2)
                break
    except KeyboardInterrupt:
        rn.request_stop("stopped by Ctrl-C", signal.SIGINT)
    finally:
        _restore_signals(old)
    with rn.lock:
        running = list(rn.active.values())
    for att in running:                                 # still in a request: paused, resumed by the next run
        att.finish("paused", error=rn.stop_reason or "stopped")
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
    if rn.keys_paused:
        res.exit_code, res.paused = EXIT_PAUSED, True
        res.message = (f"PAUSED: {rn.stop_reason}. The unfinished entities stay pending: add a key "
                       "(ANTHROPIC_API_KEY, ANTHROPIC_API_KEYS or --keys-file) and run the same command again.")
        log(res.message)
    elif rn.stop_signal is not None:
        res.exit_code = EXIT_SIGTERM if rn.stop_signal == signal.SIGTERM else EXIT_SIGINT
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
        write_json({"call": "client.beta.messages.create", "agent": a.name, "entity_id": dos.entity_id,
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
    for r in rows:
        spend[r.get("kind") or "?"] += float(r.get("cost_usd") or 0.0)
    say(f"Spent: {_fmt_usd(sum(spend.values()))} in {len(rows):,} attempts"
        + (" (" + ", ".join(f"{k} {_fmt_usd(v)}" for k, v in sorted(spend.items())) + ")" if spend else ""))
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
        say(f"A review run holds {lp} (if no run is going on, it is stale: the next run removes it)")
    if tables:
        n_c, n_f = build_tables(out)
        say(f"Tables: {n_c:,} connection verdicts -> review/connections.parquet, {n_f:,} findings -> "
            "review/findings.parquet")
    return q


def read_json_safe(p):
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


CONN_COLS = ["entity_id", "kind", "name", "partner", "partner_kind", "partner_col", "verdict", "citations",
             "n_citations", "check", "unverified", "model", "run_id", "reviewed"]
FIND_COLS = ["entity_id", "kind", "name", "section", "item", "title", "detail", "data_evidence", "confidence",
             "source", "citations", "n_citations", "check", "unverified", "model", "run_id", "reviewed"]
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


def build_tables(out):
    """OUT/review/connections.parquet (one row per connection verdict) and findings.parquet (one row per item of
    established / unexpected / missing / contradicted, and per open question) from the stored reviews."""
    rd = os.path.join(out, "review", "reviews")
    conn, find = [], []
    cols = None
    for kind in KINDS:
        for f in sorted(glob.glob(os.path.join(rd, kind, "*.json"))):
            r = read_json_safe(f)
            if not isinstance(r, dict):
                continue
            meta = r.get("meta") or {}
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
                             "check": (it.get("check") or {}).get("verdict", ""),
                             "unverified": bool(it.get("unverified"))})
            for sec, (tk, dk, ek) in SECTIONS.items():
                for i, it in enumerate(r.get(sec) or []):
                    cits = it.get("citations") or []
                    detail = it.get(dk, "") if dk else ""
                    if sec == "unexpected" and it.get("literature_checked"):
                        detail = (detail + " | searched: " + "; ".join(it["literature_checked"])).strip(" |")
                    find.append({**base, "section": sec, "item": i, "title": it.get(tk, ""), "detail": detail,
                                 "data_evidence": it.get(ek, ""), "confidence": it.get("confidence", ""),
                                 "source": it.get("source", ""), "citations": ";".join(cits),
                                 "n_citations": len(cits), "check": (it.get("check") or {}).get("verdict", ""),
                                 "unverified": bool(it.get("unverified"))})
            for i, qn in enumerate(r.get("open_questions") or []):
                find.append({**base, "section": "open_questions", "item": i, "title": qn, "detail": "",
                             "data_evidence": "", "confidence": "", "source": "", "citations": "", "n_citations": 0,
                             "check": "", "unverified": False})
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
        print(f"review: unknown action '{action}'; use plan, run, status or tables")
        return EXIT_REFUSED
    if not os.path.isdir(os.path.join(out, "tables")):
        print(f"review: {out} holds no finished run (no tables/ folder); give --out with a tahoemap output folder")
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
        print(f"review {action}: {e}")
        return EXIT_REFUSED
    from ..tlib import start_run_log
    start_run_log(os.path.join(review_dir(out), "review.log"), "tahoemap review run")
    res = run(out, kinds=a.kinds, only=a.only, limit=a.limit, max_usd=a.max_usd, concurrency=a.concurrency,
              keys_file=a.keys_file, redo=a.redo, dry_run=a.dry_run, fake=a.fake, no_cap=a.no_cap, **common)
    return res.exit_code                       # (run() has said why)
