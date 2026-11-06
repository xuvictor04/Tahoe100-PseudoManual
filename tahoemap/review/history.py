"""history - what the review agents did: one JSONL file per attempt, and the ledger of all attempts.

    History(out, kind, name, run_id)
        OUT/review/history/<kind>/<safe name>/<run_id>.jsonl: every event of one attempt, one JSON object a line
        ({"event": ..., "time": ..., ...}):
            start     agent, model, effort, key_id, system prompt (text + sha256), tool list (names + definitions),
                      dossier (text + sha256), code version, request settings
            request   the messages appended since the previous request (the first: the dossier message)
            response  response.to_dict() in full, usage, cost of this response, cost of the attempt so far
            tool      name, input, result (cut at 20,000 characters, with a note), is_error, seconds
            error     typed class, status, error type / code, request id, scrubbed message, what the runner did
            end       status, totals
        The citation checker's events go to the same file with "agent": "citation-checker".
    Ledger(out)
        OUT/review/ledger.jsonl: one line per finished attempt (append-only; the latest line of an entity is its
        state). latest() / states() / frame() read it back.

Every line is written whole (one write, then flush) under a lock, and passes through keys.scrub() first, so an API
key can never reach these files. Lines are never rewritten.
"""

import json
import os
import threading
import time

import numpy as np
import pandas as pd

from . import review_dir
from .keys import scrub
from ..common import safe_filename

TOOL_RESULT_CHARS = 20_000
STATUSES = ("done", "refused", "no_review", "over_budget", "failed", "paused", "key_rotated")
LEDGER_FIELDS = ("entity_id", "kind", "name", "run_id", "agent", "model", "status", "cost_usd", "input_tokens",
                 "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "web_searches",
                 "web_fetches", "n_requests", "n_tool_calls", "key_id", "started", "finished", "error")

_FILE_LOCKS = {}
_FILE_LOCKS_LOCK = threading.Lock()


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def _file_lock(path):
    with _FILE_LOCKS_LOCK:
        lk = _FILE_LOCKS.get(path)
        if lk is None:
            lk = _FILE_LOCKS[path] = threading.Lock()
        return lk


def _default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    td = getattr(o, "to_dict", None)                      # SDK models (content blocks, usage)
    if callable(td):
        try:
            return td(mode="json")
        except TypeError:
            return td()
    return str(o)


def to_jsonable(obj):
    """A plain JSON-ready copy (SDK content blocks become dicts)."""
    return json.loads(json.dumps(obj, default=_default))


def append_line(path, rec):
    """Append one scrubbed JSON line (atomic with respect to the other threads of this process)."""
    line = scrub(json.dumps(rec, default=_default, ensure_ascii=False))
    with _file_lock(path):
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
            fh.flush()


def read_jsonl(path):
    out = []
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except ValueError:
                continue                                    # a line cut by a crash: skip it
    return out


class History:
    def __init__(self, out, kind, name, run_id):
        self.out = out
        d = review_dir(out, "history", kind, safe_filename(name))
        self.path = os.path.join(d, f"{run_id}.jsonl")
        self.rel = os.path.relpath(self.path, out).replace(os.sep, "/")
        self.closed = False
        self._lock = threading.Lock()

    def event(self, kind, **data):
        with self._lock:
            if self.closed:
                return
            if kind == "end":
                self.closed = True
            append_line(self.path, {"event": kind, "time": now(), **data})

    def tool(self, agent, name, tool_input, result, is_error, seconds):
        text = str(result)
        if len(text) > TOOL_RESULT_CHARS:
            text = text[:TOOL_RESULT_CHARS] + (f"\n[cut in this history at {TOOL_RESULT_CHARS:,} of {len(text):,} "
                                               "characters; the model got the full result]")
        self.event("tool", agent=agent, name=name, input=tool_input, result=text, is_error=bool(is_error),
                   seconds=round(float(seconds), 3))

    def events(self):
        return read_jsonl(self.path)


class Ledger:
    def __init__(self, out):
        self.out = out
        self.path = os.path.join(review_dir(out), "ledger.jsonl")

    def append(self, rec):
        r = {k: rec.get(k) for k in LEDGER_FIELDS}
        r.update({k: v for k, v in rec.items() if k not in r})
        append_line(self.path, r)
        return r

    def read(self):
        return read_jsonl(self.path)

    def latest(self):
        """entity_id -> its latest ledger line."""
        out = {}
        for r in self.read():
            if r.get("entity_id"):
                out[r["entity_id"]] = r
        return out

    def states(self):
        """entity_id -> {status, n_failed (failed / no_review attempts since the last other outcome), cost_usd (all
        attempts), attempts, last (the latest line)}."""
        st = {}
        for r in self.read():
            e = r.get("entity_id")
            if not e:
                continue
            s = st.setdefault(e, {"status": None, "n_failed": 0, "cost_usd": 0.0, "attempts": 0, "last": None})
            s["attempts"] += 1
            s["cost_usd"] += float(r.get("cost_usd") or 0.0)
            if r.get("status") in ("failed", "no_review"):
                s["n_failed"] += 1
            elif r.get("status") in ("done", "refused", "over_budget"):
                s["n_failed"] = 0
            s["status"] = r.get("status")
            s["last"] = r
        return st

    def frame(self):
        rows = self.read()
        if not rows:
            return pd.DataFrame(columns=list(LEDGER_FIELDS))
        return pd.DataFrame(rows)
