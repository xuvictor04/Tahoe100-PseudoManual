"""history - what the review agents did: one JSONL file per attempt, and the ledger of all attempts.

    History(out, kind, name, run_id)
        OUT/review/history/<kind>/<safe name>/<run_id>.jsonl: every event of one attempt, one JSON object a line
        ({"event": ..., "time": ..., ...}):
            start     agent, model, effort, key_id, system prompt (text + sha256), tool list (names + definitions),
                      dossier (text + sha256), code version, request settings
            request   the messages appended since the previous request (the first: the dossier message, with
                      the dossier text, stored once in the start event, as the placeholder {{dossier}};
                      conversation() puts it back)
            response  response.to_dict() in full, usage, cost of this response, cost of the attempt so far ("late":
                      true after the end event: it arrived after the attempt was closed)
            tool      name, input, result (cut at 20,000 characters, with a note), is_error, seconds
            error     typed class, status, error type / code, request id, scrubbed message, what the runner did
                      (and for a lost response: estimated_cost_usd, the estimate charged for it; class
                      InFlightAtStop: a request in flight when the stopping run closed the attempt, charged an
                      estimate; "late": true after the end event: lost after the attempt was closed)
            end       status, totals
        The citation checker's events go to the same file, "agent": "citation-checker", after a start event of
        its own ("phase": "citation check": its system prompt, tools, claim ids, key id, sha256 of its prompt).
    conversation(events, agent=None) -> list of messages
        the messages of the last request of an agent's (latest) conversation, rebuilt from the events exactly as
        they were sent (placeholders filled from the start event).
    Ledger(out)
        OUT/review/ledger.jsonl: one line per finished attempt (append-only; the latest line of an entity is its
        state). latest() / states() / frame() read it back. Bookkeeping lines have status "note" and a "note"
        text: the cost of a response that arrived after its attempt was closed ("late": true; when an estimate was
        charged for that request at the close, the difference - possibly negative - with "replaces_estimate_usd"
        and minus the estimate as "estimated_usd"), an estimate for a response lost after its attempt was closed
        ("late": true, "estimated_usd"), a failure the run put down to a systematic error ("uncount_failed": true,
        with the error's "signature"), or a --recheck that was stopped before it finished ("recheck": true; the
        stored review is unchanged); they change the spend or the failure count, never the state.

Every line is written whole (one write, then flush) under a lock, and passes through keys.scrub() first, so an API
key can never reach these files. Lines are never rewritten. A file that ends in a cut line (a crash, a full disk)
gets a newline before the next line, and read_jsonl skips a cut line but keeps a whole line glued to its end.
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
DOSSIER_REF = "{{dossier}}"                 # in the first request event: the dossier text of the start event
PLACEHOLDER_SOURCE = {DOSSIER_REF: "start.dossier"}
STATUSES = ("done", "refused", "no_review", "over_budget", "failed", "paused", "key_rotated")
NOTE = "note"                               # a bookkeeping ledger line (a late cost, an uncounted failure ...)
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


def _ends_without_newline(path):
    try:
        with open(path, "rb") as fh:
            fh.seek(0, os.SEEK_END)
            if fh.tell() == 0:
                return False
            fh.seek(-1, os.SEEK_END)
            return fh.read(1) != b"\n"
    except OSError:
        return False


def append_line(path, rec):
    """Append one scrubbed JSON line (atomic with respect to the other threads of this process). If the file ends
    in a cut line (a crash or a full disk during an earlier write), a newline goes first, so the fragment stays a
    line of its own (skipped by read_jsonl) and the new line is kept whole."""
    line = scrub(json.dumps(rec, default=_default, ensure_ascii=False))
    with _file_lock(path):
        lead = "\n" if _ends_without_newline(path) else ""
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(lead + line + "\n")
            fh.flush()


_DECODER = json.JSONDecoder()


def _recover(line):
    """A JSON object glued to the end of a cut line (written before the newline guard existed), or None."""
    i = line.find("{", 1)
    while i > 0:
        try:
            obj, end = _DECODER.raw_decode(line, i)
            if end == len(line) and isinstance(obj, dict):
                return obj
        except ValueError:
            pass
        i = line.find("{", i + 1)
    return None


def read_jsonl(path):
    """The JSON objects of a JSONL file. A line cut by a crash is skipped; a whole line glued to its end (an older
    file without the newline guard) is kept."""
    out = []
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except ValueError:
                obj = _recover(line)                        # a cut line, perhaps with a whole line after it
                if obj is not None:
                    out.append(obj)
    return out


class History:
    def __init__(self, out, kind, name, run_id):
        self.out = out
        d = review_dir(out, "history", kind, safe_filename(name))
        self.path = os.path.join(d, f"{run_id}.jsonl")
        self.rel = os.path.relpath(self.path, out).replace(os.sep, "/")
        self.closed = False
        self._lock = threading.Lock()

    def event(self, kind, late=False, **data):
        """Append one event; after the end event only `late` ones (a response that arrived, or was lost, after the
        attempt was closed, so its cost is on record)."""
        with self._lock:
            if self.closed and not late:
                return
            if kind == "end":
                self.closed = True
            append_line(self.path, {"event": kind, "time": now(), **({"late": True} if late else {}), **data})

    def tool(self, agent, name, tool_input, result, is_error, seconds):
        text = str(result)
        if len(text) > TOOL_RESULT_CHARS:
            text = text[:TOOL_RESULT_CHARS] + (f"\n[cut in this history at {TOOL_RESULT_CHARS:,} of {len(text):,} "
                                               "characters; the model got the full result]")
        self.event("tool", agent=agent, name=name, input=tool_input, result=text, is_error=bool(is_error),
                   seconds=round(float(seconds), 3))

    def events(self):
        return read_jsonl(self.path)


def conversation(events, agent=None):
    """The full messages of the last request of `agent`'s latest conversation in these history events (default:
    the first agent of the file, the reviewer), with the placeholders filled from its start event."""
    agent = agent or next((e.get("agent") for e in events if e.get("event") == "start"), None)
    start, msgs = {}, []
    for e in events:
        if e.get("agent") != agent:
            continue
        if e.get("event") == "start":
            start, msgs = e, []
        elif e.get("event") == "request":
            add = json.loads(json.dumps(e.get("messages") or []))
            for ph, src in (e.get("placeholders") or {}).items():
                text = start.get(src.split(".", 1)[1], "") if src.startswith("start.") else ""
                for m in add:
                    if isinstance(m.get("content"), str):
                        m["content"] = m["content"].replace(ph, text)
            msgs += add
    return msgs


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
        """entity_id -> its latest ledger line (bookkeeping "note" lines left out)."""
        out = {}
        for r in self.read():
            if r.get("entity_id") and not r.get("note"):
                out[r["entity_id"]] = r
        return out

    def states(self):
        """entity_id -> {status, n_failed (failed / no_review attempts since the last other outcome), cost_usd (all
        attempts), attempts, last (the latest line), stopped_runs (the errors - signatures, "*" when the line has
        none - of the failures the run put down to a systematic error since the last other outcome)}. Bookkeeping
        lines ("note": the cost of a response that came after its attempt ended; "uncount_failed": a failure the run
        put down to a systematic error; a recheck that did not finish) change the cost, the failure count or
        stopped_runs, not the state."""
        st = {}
        for r in self.read():
            e = r.get("entity_id")
            if not e:
                continue
            s = st.setdefault(e, {"status": None, "n_failed": 0, "cost_usd": 0.0, "attempts": 0, "last": None,
                                  "stopped_runs": []})
            s["cost_usd"] += float(r.get("cost_usd") or 0.0)
            if r.get("note"):
                if r.get("uncount_failed"):
                    s["n_failed"] = max(0, s["n_failed"] - 1)
                    sig = r.get("signature")
                    s["stopped_runs"].append(tuple(sig) if isinstance(sig, (list, tuple)) else "*")
                continue
            s["attempts"] += 1
            if r.get("status") in ("failed", "no_review"):
                s["n_failed"] += 1
            elif r.get("status") in ("done", "refused", "over_budget"):
                s["n_failed"] = 0
                s["stopped_runs"] = []
            s["status"] = r.get("status")
            s["last"] = r
        return st

    def frame(self):
        rows = self.read()
        if not rows:
            return pd.DataFrame(columns=list(LEDGER_FIELDS))
        return pd.DataFrame(rows)
